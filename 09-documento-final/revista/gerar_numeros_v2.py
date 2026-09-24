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


# ---------------------------------------------------------------- entradas: Tab. 1 (características agregadas)
F_CELULAS = "09-documento-final/revista/celulas.json"
F_DIRECAO = "06-analise/swim_principal/tabelas/swim_direcao.csv"


def pct(n, den):
    return round(100 * n / den, 1)


def tab1_caracteristicas():
    """Contagens e porcentagens da Tab. 1. Tudo de numeros.json, menos as faixas de ano de publicação, que saem do
    ano do relato principal de cada estudo em incluidos.csv (a mesma fonte do ano_min/ano_max de numeros.json)."""
    num = ljson(F_NUM)
    n_est = num["estudos"]
    linhas = []
    for grupo in ("desenho", "familia", "realismo", "regiao", "eleicao", "construto"):
        confere(sum(num[grupo].values()) == n_est, f"numeros.json: {grupo} não soma {n_est}")
        for cod, n in sorted(num[grupo].items(), key=lambda x: (-x[1], x[0])):
            linhas.append({"grupo": grupo, "codigo": cod, "n": n, "denominador": n_est, "pct": pct(n, n_est)})
    # faixas de ano de publicação (relato principal)
    anos = {r["chave"]: r["ano"] for r in lcsv(F_INCL)}
    master = [r["citekey"] for r in lcsv(F_MASTER)]
    vals = [int(anos[k]) for k in master]
    confere(min(vals) == num["ano_min"] and max(vals) == num["ano_max"], "faixa de anos difere de numeros.json")
    faixas = [(2010, 2014), (2015, 2019), (2020, 2024)]
    confere(faixas[0][0] <= min(vals) and max(vals) <= faixas[-1][1], "ano fora das faixas previstas")
    for a, b in faixas:
        n = sum(a <= v <= b for v in vals)
        linhas.append({"grupo": "periodo", "codigo": f"{a}-{b}", "n": n, "denominador": n_est, "pct": pct(n, n_est)})
    # risco de viés geral por ferramenta (denominador = resultados avaliados com a ferramenta)
    for ferr, dist in num["rob_por_ferr"].items():
        den = sum(dist.values())
        for cod, n in sorted(dist.items(), key=lambda x: (-x[1], x[0])):
            linhas.append({"grupo": f"rob_{ferr}", "codigo": cod, "n": n, "denominador": den, "pct": pct(n, den)})
    confere(sum(sum(d.values()) for d in num["rob_por_ferr"].values()) == num["rob_resultados"],
            "resultados de risco de viés não somam rob_resultados")
    return {"tab1_caracteristicas": entrada(
        n_est, "Tab. 1: n e % por característica; denominador = 41 estudos (desenho, família, realismo, região, "
               "eleição, desfechos e faixas de ano do relato principal) ou resultados avaliados com cada ferramenta "
               "(risco de viés geral); % com 1 casa",
        [F_NUM, F_INCL, F_MASTER], linhas=linhas)}


# ---------------------------------------------------------------- entradas: Tab. 2 (SoF), n por estudo e unidade
F_CERTEZA = "06-analise/certeza.csv"
CHAVE_CEL = ("familia_intervencao", "construto_outcome", "comparador_tipo", "celula_alvo", "classe_desenho")
UNIDADES_AGREGADAS = [("secao_eleitoral", "seções eleitorais"), ("distrito_eleitoral", "distritos eleitorais"),
                      ("departamento", "departamentos"), ("pais", "países")]
NAO_UNIDADE = {"por", "em", "no", "na", "de", "do", "da", "a", "e", "com", "sem", "até"}


def fmt_milhar(n):
    return f"{n:,}".replace(",", ".")


def unidade_da_justificativa(justificativa, n, chave, k):
    """1ª regra: a unidade escrita junto do n no domínio de imprecisão da justificativa GRADE da célula
    (certeza.csv), p. ex. "300 eleições de grupo em Agranov2017a", "1 estudo (545 respondentes)". Vale a ocorrência
    do n seguida, em até 80 caracteres, da chave do estudo; numa célula de 1 estudo, a primeira ocorrência. A unidade
    é a primeira palavra depois do n, mais "de <palavra>" quando vier logo em seguida (\"eleições de grupo\")."""
    m = re.search(r"Imprecisão:(.*?)(?:Viés de publicação:|$)", justificativa, re.S)
    if not m:
        return None
    imp = m.group(1)
    for achado in re.finditer(r"(?<![\d.,])" + re.escape(fmt_milhar(n)) + r"(?![\d.,]*\d)", imp):
        depois = imp[achado.end():achado.end() + 80]
        if k > 1 and chave not in depois:
            continue
        pal = re.match(r"\s+([a-zà-ú]+)(?:\s+de\s+([a-zà-ú]+))?", depois)
        if not pal or pal.group(1) in NAO_UNIDADE:
            return None
        u = pal.group(1)
        if pal.group(2) and pal.group(2) not in NAO_UNIDADE:
            u += " de " + pal.group(2)
        return u
    return None


def unidade_do_fichamento(m, n):
    """2ª regra, conservadora, quando a justificativa não diz a unidade:
    - unidade de análise agregada (seção, distrito, departamento, país) e desfecho agregado: o nome da unidade;
    - unidade 'individuo' e n igual ao tamanho total codificado no fichamento (b2_n_total): 'indivíduos';
    - nos demais casos, sem unidade (a tabela mostra só o n)."""
    ua, nivel = m["unidade_analise"], m["nivel_desfecho"]
    for cod, rot in UNIDADES_AGREGADAS:
        if ua.startswith(cod) or (ua.startswith("outro") and cod in ua.split("(")[0]):
            return rot if "agregad" in nivel else None
    total = re.match(r"\s*(\d+)", m["b2_n_total"])
    if ua == "individuo" and total and int(total.group(1)) == n:
        return "indivíduos"
    return None


def sof_n_por_estudo():
    cel = ljson(F_CELULAS)["celulas"]
    master = {r["citekey"]: r for r in lcsv(F_MASTER)}
    cert = {tuple(r[c] for c in CHAVE_CEL): r for r in lcsv(F_CERTEZA)}
    nam = {}
    for r in lcsv(F_DIRECAO):
        nam[(r["chave"], r["grupo"])] = int(r["n_amostra"]) if r["n_amostra"] not in ("", "NA") else None
    por_celula, com_n, fontes_u = {}, 0, {"justificativa GRADE": 0, "fichamento": 0, "sem unidade": 0}
    for c in cel:
        chave_c = tuple(c[k] for k in CHAVE_CEL)
        grupo = " | ".join(chave_c)
        just = cert[chave_c]["justificativa"]
        lista = []
        for ch in c["estudos"]:
            confere((ch, grupo) in nam, f"{ch} sem linha em swim_direcao.csv no grupo {grupo}")
            n = nam[(ch, grupo)]
            u, fonte_u = None, None
            if n is not None:
                com_n += 1
                u = unidade_da_justificativa(just, n, ch, c["k"])
                fonte_u = "justificativa GRADE" if u else None
                if u is None:
                    u = unidade_do_fichamento(master[ch], n)
                    fonte_u = "fichamento" if u else None
                fontes_u[fonte_u or "sem unidade"] += 1
            lista.append({"chave": ch, "n": n, "unidade": u, "fonte_unidade": fonte_u})
        por_celula[c["id"]] = lista
    return {"sof_n_por_estudo": entrada(
        com_n, "n do efeito principal de cada estudo em cada célula (coluna n_amostra de swim_direcao.csv, junção por "
               "chave + grupo); unidade pela justificativa GRADE da célula (domínio de imprecisão, certeza.csv) ou, na "
               "falta, pela regra de unidade_do_fichamento (unidade_analise, nivel_desfecho e b2_n_total); pares com "
               f"unidade da justificativa: {fontes_u['justificativa GRADE']}, do fichamento: {fontes_u['fichamento']}, "
               f"sem unidade: {fontes_u['sem unidade']}",
        [F_DIRECAO, F_CELULAS, F_CERTEZA, F_MASTER], por_celula=por_celula)}


# ---------------------------------------------------------------- entradas: Tab. 5 (transferibilidade)
def transferibilidade():
    """Quantos estudos incluídos têm cada fator de transferibilidade do protocolo (seção 9), pelo fichamento."""
    M = lcsv(F_MASTER)
    cel = ljson(F_CELULAS)["celulas"]
    sint_mob = sorted({e for c in cel if c["bloco"] == "mobilizacao" for e in c["estudos"]})
    na_sintese = {e for c in cel for e in c["estudos"]}
    mob = sorted(r["citekey"] for r in M if "mobilizacao" in r["construto_outcome"])
    vo_sim = sorted(r["citekey"] for r in M if r["voto_obrigatorio"].strip().lower().startswith("sim"))
    vo_nao = sorted(r["citekey"] for r in M if r["voto_obrigatorio"].strip().lower().startswith("não"))
    dois_t = sorted(r["citekey"] for r in M if r["sistema_eleitoral"].strip() == "maioria_dois_turnos")
    proib = sorted(r["citekey"] for r in M if r["comparador_tipo"].strip() == "antes_depois_proibicao")
    embargo = sorted(r["citekey"] for r in M if re.search(r"blackout|embargo", r["intervencao_descricao"] + " " +
                                                         r["comparador"], re.I) and r["citekey"] not in proib)
    conf = sorted(r["citekey"] for r in M if "confianca_pesquisas" in r["moderadores_relatados"])
    confere(len(mob) == sum(v for k, v in ljson(F_NUM)["construto"].items() if "mobilizacao" in k),
            "estudos de comparecimento diferem de numeros.json")
    fm = [F_MASTER]
    return {
        "transf_voto_obrigatorio_sim": entrada(
            len(vo_sim), "estudos do master com voto_obrigatorio começando por 'sim'", fm, chaves=vo_sim),
        "transf_voto_obrigatorio_informado": entrada(
            len(vo_sim) + len(vo_nao), "estudos com voto_obrigatorio 'sim' ou 'não' (os demais: 999, não informado)",
            fm, chaves=sorted(vo_sim + vo_nao)),
        "transf_voto_obrigatorio_sim_comparecimento": entrada(
            len(set(vo_sim) & set(mob)), "estudos com desfecho de comparecimento (construto com mobilizacao) e "
                                         "voto_obrigatorio 'sim'", fm, chaves=sorted(set(vo_sim) & set(mob))),
        "transf_comparecimento_estudos": entrada(
            len(mob), "estudos do master com mobilizacao no construto_outcome", fm + [F_NUM], chaves=mob),
        "transf_comparecimento_sintese": entrada(
            len(sint_mob), "estudos nas células de comparecimento (bloco mobilizacao) da síntese principal",
            [F_CELULAS], chaves=sint_mob),
        "transf_dois_turnos": entrada(
            len(dois_t), "estudos do master com sistema_eleitoral = maioria_dois_turnos", fm, chaves=dois_t),
        "transf_regulacao": entrada(
            len(proib) + len(embargo), "estudos cuja variação vem de regra de divulgação: comparador_tipo = "
                                       "antes_depois_proibicao, mais os que descrevem embargo ou blackout de pesquisas "
                                       "em intervencao_descricao ou comparador", fm, chaves=sorted(proib + embargo)),
        "transf_regulacao_proibicao": entrada(
            len(proib), "estudos com comparador_tipo = antes_depois_proibicao (proibição de boca de urna)", fm,
            chaves=proib),
        "transf_regulacao_embargo": entrada(
            len(embargo), "estudos que descrevem embargo ou blackout de pesquisas (intervencao_descricao ou "
                          "comparador), fora os de proibição acima", fm, chaves=embargo),
        "transf_regulacao_na_sintese": entrada(
            len(set(proib + embargo) & na_sintese), "desses, os que estão em alguma célula da síntese principal",
            fm + [F_CELULAS], chaves=sorted(set(proib + embargo) & na_sintese)),
        "transf_confianca": entrada(
            len(conf), "estudos com confianca_pesquisas em moderadores_relatados", fm, chaves=conf),
    }


# ---------------------------------------------------------------- entradas: valores dos efeitos principais (suplemento)
def efeitos_principais_valores():
    """Valores de cada efeito principal que as tabelas do suplemento (S6, S7 e S10, geradas por
    07-relatorio/gerar_tabelas_relatorio.py) imprimem: g alinhado (yi), EP (sei), efeito em p.p., p0, p1, β e n.
    Ficam aqui para que cada número do suplemento tenha fonte registrada; nada é recalculado."""
    campos = ("yi", "sei", "efeito_pp", "p0", "p1", "beta", "n_total", "n1", "n2")
    valores = {}
    for r in lcsv(F_EFEITOS):
        if r["modelo_principal"] != "sim":
            continue
        v = {}
        for c in campos:
            if r.get(c) not in (None, "", "NA"):
                try:
                    v[c] = float(r[c])
                except ValueError:
                    pass
        valores[r["id_efeito"]] = v
    return {"efeitos_principais_valores": entrada(
        len(valores), "efeitos com modelo_principal = sim em 06-analise/efeitos.csv, com os campos que as tabelas do "
                      "suplemento imprimem (yi, sei, efeito_pp, p0, p1, beta, n_total, n1, n2), sem arredondar",
        [F_EFEITOS], valores=valores)}


ENTRADAS = [prisma_totais, prisma_filtro_ano, estudos_fora_da_sintese, pendencias, tab1_caracteristicas,
            sof_n_por_estudo, transferibilidade, efeitos_principais_valores]


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
