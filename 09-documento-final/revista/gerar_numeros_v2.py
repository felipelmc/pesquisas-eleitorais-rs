"""Gera 09-documento-final/revista/numeros_v2.json: a ÚNICA porta de entrada para números derivados que o texto
novo usa e que não estão prontos em outro arquivo do projeto.

USO (de qualquer pasta):  python3 09-documento-final/revista/gerar_numeros_v2.py

Cada entrada: {"valor": ..., "formatado": "...", "formula": "texto", "fontes": ["arquivo", ...]}, com vírgula
decimal e U+2212 no formatado (entradas com lista de estudos trazem também "chaves"). Nenhum número é digitado:
tudo é lido dos arquivos. As conferências cruzadas (asserts) param o script se as fontes discordarem.

Para acrescentar uma entrada: escreva uma função que devolva {nome: entrada} (use entrada(...)) e ponha-a em
ENTRADAS, no fim do arquivo.
"""
import ast
import csv
import json
import re
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[2]
SAIDA = R / "09-documento-final/revista/numeros_v2.json"

F_PRISMA = "07-relatorio/prisma_contagens.json"
F_PEND = "07-relatorio/_pendencias_abertas.json"
F_SWIM = "06-analise/swim_principal/swim_resumo.json"
F_ENTRADA = "06-analise/swim_entrada_principal.csv"
F_EFEITOS = "06-analise/efeitos.csv"
F_FORA = "06-analise/montar_entradas_swim.py"
F_ROB = "04-qualidade/rob_geral.csv"
F_MASTER = "05-decomposicao/fichamentos_master.csv"
F_INCL = "07-relatorio/incluidos.csv"
F_NUM = "09-documento-final/insumos/tabelas/numeros.json"
F_RELAT = "07-relatorio/relatorio.qmd"


# ---------------------------------------------------------------- utilidades
def ljson(rel):
    return json.load(open(R / rel, encoding="utf-8"))


def lcsv(rel):
    return list(csv.DictReader(open(R / rel, encoding="utf-8-sig")))


def fmt(v, casas=None):
    """Formato pt-BR: ponto de milhar em inteiros, vírgula decimal, U+2212 no sinal negativo."""
    if isinstance(v, int) or (isinstance(v, float) and casas is None and float(v).is_integer()):
        s = f"{int(v):,}".replace(",", ".")
    else:
        s = f"{float(v):,.{casas if casas is not None else 2}f}"
        s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return s.replace("-", "−")


def entrada(valor, formula, fontes, casas=None, **extra):
    e = {"valor": valor, "formatado": fmt(valor, casas), "formula": formula, "fontes": list(fontes)}
    e.update(extra)
    return e


def confere(cond, msg):
    if not cond:
        sys.exit(f"ERRO de conferência: {msg}")


def dicionario_fora():
    """Lê o dicionário FORA de montar_entradas_swim.py pela árvore sintática, sem executar o script."""
    arvore = ast.parse((R / F_FORA).read_text(encoding="utf-8"))
    for no in arvore.body:
        if isinstance(no, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "FORA" for t in no.targets):
            return ast.literal_eval(no.value)
    sys.exit("ERRO: dicionário FORA não encontrado")


def estudo_do_efeito(id_efeito):
    return id_efeito.rsplit("-", 1)[0]


# ---------------------------------------------------------------- entradas: PRISMA
def prisma_totais():
    p = ljson(F_PRISMA)
    b, o = p["bases"], p["outros_metodos"]
    out = {}
    for nome, campo, descr in [
        ("relatos_buscados_total", "buscados", "relatos buscados para texto completo"),
        ("relatos_nao_recuperados_total", "nao_recuperados", "relatos buscados e não recuperados"),
        ("relatos_avaliados_total", "avaliados", "relatos avaliados no texto completo"),
    ]:
        out[nome] = entrada(b[campo] + o[campo],
                            f"{descr}: bases.{campo} + outros_metodos.{campo} = {b[campo]} + {o[campo]}",
                            [F_PRISMA])
    return out


def prisma_filtro_ano():
    p = ljson(F_PRISMA)
    out, soma, partes = {}, 0, []
    for ramo in ("bases", "outros_metodos"):
        filtros = p[ramo]["removidos_antes_triagem"].get("automacao_por_filtro", {})
        if "ano" not in filtros:
            continue
        v = filtros["ano"]
        confere(v <= p[ramo]["removidos_antes_triagem"]["automacao"], f"filtro de ano maior que a automação em {ramo}")
        out[f"excluidos_filtro_ano_{ramo}"] = entrada(
            v, f"{ramo}.removidos_antes_triagem.automacao_por_filtro.ano (exclusão automática por script, antes da triagem)",
            [F_PRISMA])
        soma += v
        partes.append(f"{ramo} = {v}")
    if len(partes) == 2:
        out["excluidos_filtro_ano_total"] = entrada(soma, "soma dos dois ramos: " + " + ".join(partes), [F_PRISMA])
    return out


# ---------------------------------------------------------------- entradas: estudos que não contribuem
def estudos_fora_da_sintese():
    master = [r["citekey"] for r in lcsv(F_MASTER)]
    incluidos = ljson(F_PRISMA)["incluidos"]["estudos"]
    num = ljson(F_NUM)
    confere(len(master) == len(set(master)) == incluidos == num["estudos"],
            f"número de estudos: master {len(master)}, PRISMA {incluidos}, numeros.json {num['estudos']}")
    relatos = {r["chave"] for r in lcsv(F_INCL)}
    confere(set(master) <= relatos, f"estudos do master sem relato em incluidos.csv: {set(master) - relatos}")

    principais = [r for r in lcsv(F_EFEITOS) if r["modelo_principal"] == "sim"]
    com_principal = {r["chave"] for r in principais}
    swim = ljson(F_SWIM)
    na_sintese = {e for g in swim["grupos"] for e in g["estudos"]}
    confere(na_sintese == {r["chave"] for r in lcsv(F_ENTRADA) if r["rob_geral"] != "critico"},
            "estudos da SWiM principal diferem dos da entrada principal sem risco crítico")
    criticos_rob = {r["chave"] for r in lcsv(F_ROB) if r["rob_geral"] == "critico"}
    fora = dicionario_fora()

    sem_principal = set(master) - com_principal
    criticos = criticos_rob & set(master)
    confere(not (criticos & na_sintese), f"estudo crítico dentro da síntese principal: {criticos & na_sintese}")
    so_fora = set(master) - na_sintese - criticos - sem_principal
    # cada estudo "só fora da contagem" tem todos os efeitos principais no dicionário FORA
    for ch in so_fora:
        ids = {r["id_efeito"] for r in principais if r["chave"] == ch}
        confere(ids and ids <= set(fora), f"{ch} não está na síntese, não é crítico e tem principal fora do FORA: "
                                          f"{sorted(ids - set(fora))}")
    confere(len(na_sintese) + len(criticos) + len(so_fora) + len(sem_principal) == len(master),
            "síntese + críticos + fora + sem principal não somam os estudos incluídos")
    # conferência com numeros.json
    confere(sorted(criticos) == num["criticos"], f"críticos: {sorted(criticos)} x numeros.json {num['criticos']}")
    confere(sorted(so_fora) == num["fora_estudos_so_fora"],
            f"fora da contagem: {sorted(so_fora)} x numeros.json {num['fora_estudos_so_fora']}")
    confere(sorted(sem_principal) == num["sem_principal"],
            f"sem principal: {sorted(sem_principal)} x numeros.json {num['sem_principal']}")
    # conferência com o relatório técnico (frase "Destino de cada estudo na síntese")
    rel = (R / F_RELAT).read_text(encoding="utf-8")
    m = re.search(r"Destino de cada estudo na síntese:(.*?)\n", rel)
    confere(m, "frase 'Destino de cada estudo na síntese' não encontrada no relatório técnico")
    frase = m.group(1)
    partes = re.search(r"(\d+) entram na SWiM principal; (\d+) têm os resultados principais em risco de viés crítico"
                       r".*?\((.*?)\); (\d+) têm todos os efeitos principais fora da contagem.*?\((.*?)\); e (\d+) não "
                       r"têm efeito principal", frase)
    confere(partes, "a frase do relatório técnico mudou de forma; ajuste a expressão regular")
    n_sint, n_crit, l_crit, n_fora, l_fora, n_sem = partes.groups()
    chaves_rel = lambda s: set(re.findall(r"@(\w+)", s))
    confere(int(n_sint) == len(na_sintese), f"relatório: {n_sint} na síntese x {len(na_sintese)}")
    confere(int(n_crit) == len(criticos) and chaves_rel(l_crit) == criticos, "relatório: críticos divergem")
    confere(int(n_fora) == len(so_fora) and chaves_rel(l_fora) == so_fora, "relatório: fora da contagem divergem")
    confere(int(n_sem) == len(sem_principal), "relatório: sem efeito principal diverge")

    fontes = [F_MASTER, F_EFEITOS, F_SWIM, F_ENTRADA, F_ROB, F_FORA, F_NUM, F_INCL, F_PRISMA, F_RELAT]
    total = criticos | so_fora | sem_principal
    return {
        "estudos_fora_da_sintese_principal": entrada(
            len(total), f"estudos incluídos ({len(master)}) − estudos da SWiM principal ({len(na_sintese)}) = "
                        f"{len(criticos)} em risco crítico + {len(so_fora)} só com efeitos fora da contagem + "
                        f"{len(sem_principal)} sem efeito principal", fontes, chaves=sorted(total)),
        "estudos_risco_critico": entrada(
            len(criticos), "estudos com rob_geral = critico em rob_geral.csv (fora da SWiM principal pelo "
                           "--excluir-rob critico; Gasperoni2015a também tem o principal no dicionário FORA)",
            [F_ROB, F_SWIM, F_FORA], chaves=sorted(criticos)),
        "estudos_so_fora_da_contagem": entrada(
            len(so_fora), "estudos com efeito principal, fora da SWiM principal e sem risco crítico; todos os "
                          "efeitos principais de cada um estão no dicionário FORA",
            [F_EFEITOS, F_SWIM, F_FORA, F_ROB], chaves=sorted(so_fora)),
        "estudos_sem_efeito_principal": entrada(
            len(sem_principal), "estudos do master de extração sem nenhuma linha com modelo_principal = sim em "
                                "efeitos.csv", [F_MASTER, F_EFEITOS], chaves=sorted(sem_principal)),
    }


# ---------------------------------------------------------------- entradas: pendências
def pendencias():
    p = ljson(F_PEND)
    abertas = [x["id"] for x in p["pendencias"] if x.get("status", "aberta") == "aberta"]
    confere(len(abertas) == p["abertas"], f"_pendencias_abertas.json: abertas = {p['abertas']}, lista = {len(abertas)}")
    return {"pendencias_abertas": entrada(len(abertas), "pendências com status aberta em _pendencias_abertas.json "
                                                        "(o JSON do PRISMA lista uma a menos, anterior à P042)",
                                          [F_PEND], chaves=abertas)}


ENTRADAS = [prisma_totais, prisma_filtro_ano, estudos_fora_da_sintese, pendencias]


def main():
    saida = {}
    for f in ENTRADAS:
        novas = f()
        repetidas = set(novas) & set(saida)
        confere(not repetidas, f"entrada repetida: {repetidas}")
        saida.update(novas)
    SAIDA.write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k, v in saida.items():
        print(f"{k} = {v['formatado']}" + (f"  {v['chaves']}" if "chaves" in v and len(v["chaves"]) <= 18 else ""))


if __name__ == "__main__":
    main()
