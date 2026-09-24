"""Monta 09-documento-final/revisao_final.qmd a partir do esqueleto redigido à mão.

O texto corrido está em 09-documento-final/_esqueleto_revisao_final.qmd. Cada linha que contém só um marcador
@@TABELA <nome>@@ é trocada por uma tabela copiada ou montada a partir dos arquivos do projeto, sem digitar números:

  swim            09-documento-final/insumos/tabelas/swim.md (SWiM principal por célula do protocolo)
  regional        09-documento-final/insumos/tabelas/regional.md
  caixa_celulas   09-documento-final/insumos/caixa_oqf_celulas.md, com legenda
  oqf_principal   caixa OQF da pergunta principal (pesquisa pré-eleitoral × apoio), montada de
                  06-analise/caixa_ferramentas.csv, 09-documento-final/insumos/caixa_oqf.json e
                  09-documento-final/insumos/tabelas/numeros.json
  mecanismos      (disponível, fora do texto atual por tamanho) quadro-resumo da seção 2.10 de 09-documento-final/insumos/mecanismos_moderadores.md,
                  sem as marcas de fonte [C: n] e com as chaves de estudo como citações @chave
  pendencias      18 pendências de 07-relatorio/_pendencias_abertas.json, com etapa, tarefa, pacote e esforço
                  da tabela de 08-revisao-humana/README.md

USO (da raiz):  python3 09-documento-final/montar_revisao_final.py
Só lê arquivos do projeto e só escreve 09-documento-final/revisao_final.qmd.
"""
import csv
import json
import re
from pathlib import Path

R = Path(__file__).resolve().parents[1]
D = R / "09-documento-final"
INS = D / "insumos"


def ler(p):
    return Path(p).read_text(encoding="utf-8").rstrip("\n")


def chaves_bib():
    ks = set()
    for bib in (R / "07-relatorio/references.bib", D / "referencias_contexto.bib"):
        ks |= set(re.findall(r"^@\w+\{([^,]+),", ler(bib), flags=re.M))
    return ks


CHAVES = chaves_bib()


def citar(texto):
    """Troca chaves de estudo soltas (ex.: Gerber2020a) por @chave, sem mexer nas que já têm @."""
    for k in sorted(CHAVES, key=len, reverse=True):
        texto = re.sub(rf"(?<![@\w]){re.escape(k)}(?![\w-])", "@" + k, texto)
    return texto


def virgula(x, casas=2):
    return f"{x:.{casas}f}".replace(".", ",")


# ---------------------------------------------------------------- tabelas copiadas
def t_swim():
    return ler(INS / "tabelas/swim.md")


def t_regional():
    return ler(INS / "tabelas/regional.md")


def t_caixa_celulas():
    corpo = ler(INS / "caixa_oqf_celulas.md")
    leg = ("\n\n: Caixa de ferramentas célula a célula (`09-documento-final/gerar_caixa_oqf.py`, a partir de "
           "`06-analise/swim_principal/swim_resumo.json`, `06-analise/certeza.csv` e `06-analise/caixa_ferramentas.csv`). "
           "Direção: estudos a favor (*bandwagon*, viabilidade, *momentum* a favor ou mobilização), contra e nulos. "
           "Rótulo pela regra `caixa-3`, calculado no nível família × desfecho × desenho e repetido em cada célula; "
           "certeza GRADE sobre a direção, rascunho de IA não validado. {#tbl-caixa-celulas "
           "tbl-colwidths=\"[12,14,11,9,20,12,7,8,7]\"}")
    return corpo + leg


# ---------------------------------------------------------------- caixa da pergunta principal
def t_oqf_principal():
    num = json.load(open(INS / "tabelas/numeros.json", encoding="utf-8"))
    caixa = [r for r in csv.DictReader(open(R / "06-analise/caixa_ferramentas.csv", encoding="utf-8"))
             if r["familia_intervencao"] == "pesquisa_pre_eleitoral"]
    corpos = {r["classe_desenho"]: r for r in caixa if r["dimensao"] == "efeito" and r["construto_outcome"] == "apoio_ao_lider"}
    impl = next(r for r in caixa if r["dimensao"] == "implementacao")
    custo = next(r for r in caixa if r["dimensao"] == "custo")
    cel = [c for c in json.load(open(INS / "caixa_oqf.json", encoding="utf-8"))["celulas"]
           if c["familia"] == "pesquisa_pre_eleitoral" and c["construto"] == "apoio_ao_lider"]
    estudos = sorted({e for c in cel for e in c["estudos"]})
    certezas = sorted({c["certeza"].replace("_", " ") for c in cel})
    m1, m2 = num["meta"], num["meta_mesmo_candidato"]
    nomes_des = {"randomizado": "randomizados", "nao_randomizado": "não randomizados"}
    forca = "; ".join(f"{nomes_des[k]}: {v['rotulo']}, força {v['forca']}" for k, v in sorted(corpos.items(), reverse=True))

    linhas = [
        ("Escala",
         f"Não estimada. Não há meta-análise principal. As duas metas exploratórias deram g = {m1['g']} "
         f"(IC 95% {m1['ic'][0]} a {m1['ic'][1]}; {m1['k_estudos']} estudos) e g = {m2['g']} "
         f"(IC 95% {m2['ic'][0]} a {m2['ic'][1]}; {m2['k_estudos']} estudos), ambas com menos de 4 graus de liberdade",
         "`swim_resumo.json`; `meta_exploratoria/` e `meta_mesmo_candidato/` (@sec-apoio)",
         "muito baixa (a das células)"),
        ("Força",
         f"Inconclusivo ({forca}). São {len(cel)} células com {len(estudos)} estudos, somando alvo principal, "
         f"viabilidade e *momentum*",
         "`caixa_ferramentas.csv` (regra `caixa-3`) e `certeza.csv`",
         " e ".join(certezas) + " em todas as células"),
        ("Mecanismo",
         "Descritivo. Voto estratégico e viabilidade é o canal com mais estudos e testes diretos em laboratório; "
         "a heurística de consenso tem uma manipulação, em vinheta (@Lammers2022a); a conformidade não foi isolada "
         "por nenhum estudo",
         "fichamento por IA (`fichamentos_master.csv`); @sec-mecanismo",
         "sem GRADE (descritivo)"),
        ("Moderador",
         "Descritivo. Na célula principal, todos os estudos hipotéticos ou induzidos vão na direção *bandwagon*, e "
         "só um experimento de pesquisa usou eleição real (@Farjam2020a); o partidarismo não atenuou o efeito no único teste "
         "pré-especificado dentro da síntese principal (@Cornejo2023a); nenhum moderador teve estudos suficientes para teste",
         "fichamento por IA e SWiM principal; @sec-moderadores",
         "sem GRADE (descritivo)"),
        ("Implementação",
         f"Não se aplica: a exposição a pesquisas não é um programa implementado por um gestor. A caixa gerada "
         f"registra \"{impl['rotulo']}\" por falta das variáveis de implementação",
         "`pergunta.md`; protocolo, seção 8; @sec-percepcao",
         "não se aplica"),
        ("Percepção",
         "Não se aplica: a revisão é só de efeito e não sintetizou achados qualitativos sobre como eleitores "
         "percebem as pesquisas",
         "protocolo, seções 8 e 9; @sec-percepcao",
         "não se aplica"),
        ("Custo",
         f"Não se aplica à exposição. A caixa gerada registra \"{custo['rotulo']}\" porque não há dado de custo "
         f"no fichamento",
         "`caixa_ferramentas.csv`; @sec-percepcao",
         "não se aplica"),
    ]
    cab = "| Dimensão | Resultado para pesquisa pré-eleitoral × apoio a quem aparece à frente | Evidência | Certeza |\n|---|---|---|---|\n"
    corpo = "".join(f"| {a} | {b} | {c} | {d} |\n" for a, b, c, d in linhas)
    leg = ("\n: Caixa de ferramentas no formato OQF para a pergunta principal. Rótulos pela regra `caixa-3`; "
           "certeza GRADE sobre a direção, rascunho de IA não validado. {#tbl-oqf tbl-colwidths=\"[12,50,24,14]\"}")
    return cab + corpo + leg


# ---------------------------------------------------------------- mecanismos
def t_mecanismos():
    txt = ler(INS / "mecanismos_moderadores.md")
    bloco = txt.split("### 2.10 Quadro-resumo dos mecanismos", 1)[1].split("\n## ", 1)[0]
    linhas = [l for l in bloco.splitlines() if l.startswith("|")]
    saida = []
    for l in linhas:
        l = re.sub(r"\s*\[C: [^\]]*\]", "", l)
        l = l.replace("Estudos que testam com dados (mediação, contraste de canal ou relato)",
                      "Estudos que testam com dados")
        saida.append(citar(l))
    leg = ("\n: Quadro-resumo dos mecanismos (síntese descritiva de `09-documento-final/insumos/mecanismos_moderadores.md`, "
           "seção 2.10, a partir do fichamento por IA). A certeza só existe onde a afirmação coincide com uma célula de "
           "`06-analise/certeza.csv`. {#tbl-mecanismos tbl-colwidths=\"[14,24,18,20,12,12]\"}")
    return "\n".join(saida) + "\n" + leg


# ---------------------------------------------------------------- pendências
def t_pendencias():
    pend = json.load(open(R / "07-relatorio/_pendencias_abertas.json", encoding="utf-8"))["pendencias"]
    readme = ler(R / "08-revisao-humana/README.md")
    tab = readme.split("## Ordem sugerida e esforço", 1)[1].split("\n## ", 1)[0]
    info, ordem = {}, {}
    for l in tab.splitlines():
        if not re.match(r"\|\s*\d+\s*\|", l):
            continue
        cols = [c.strip() for c in l.strip().strip("|").split("|")]
        n, ids, etapa, tarefa, pacote, esforco = cols
        if pacote == "seção abaixo":
            pacote = "`README.md`, seção dos portões"
        for pid in re.findall(r"P\d{3}", ids):
            info[pid] = (etapa, tarefa, pacote, esforco)
            ordem[pid] = int(n)
    # A linha "P036 e P042" do README descreve as duas pela P036. Para a P042, a tarefa vem do registro
    # da própria pendência em _pendencias_abertas.json (descrição e n), sem alterar o README.
    p042 = next((p for p in pend if p["id"] == "P042"), None)
    if p042 and "P042" in info:
        etapa, _, pacote, esforco = info["P042"]
        tarefa = (f"completar a certeza (GRADE/CERQual) e os enunciados das {p042['n']} células pendentes que o "
                  "`rs caixa` apontou; na prática, pede a mesma validação da P036")
        info["P042"] = (etapa, tarefa, pacote, esforco)
    pend = sorted(pend, key=lambda p: (ordem.get(p["id"], 99), p["id"]))
    cab = "| Id | Etapa | O que falta | Pacote em `08-revisao-humana/` | Esforço |\n|---|---|---|---|---|\n"
    corpo = ""
    for p in pend:
        etapa, tarefa, pacote, esforco = info.get(p["id"], ("NR", p["descricao"], "NR", "NR"))
        corpo += f"| {p['id']} | {etapa} | {tarefa} | {pacote} | {esforco} |\n"
    leg = (f"\n: Pendências humanas abertas ({len(pend)}), de `07-relatorio/_pendencias_abertas.json`; etapa, tarefa, "
           "pacote e esforço copiados de `08-revisao-humana/README.md` (a tarefa da P042, do registro da pendência), "
           "na ordem das etapas. {#tbl-pendencias "
           "tbl-colwidths=\"[7,15,48,18,12]\"}")
    return cab + corpo + leg


TABELAS = {"swim": t_swim, "regional": t_regional, "caixa_celulas": t_caixa_celulas,
           "oqf_principal": t_oqf_principal, "mecanismos": t_mecanismos, "pendencias": t_pendencias}


def main():
    esq = ler(D / "_esqueleto_revisao_final.qmd")
    def troca(m):
        return TABELAS[m.group(1)]()
    saida = re.sub(r"^@@TABELA (\w+)@@$", troca, esq, flags=re.M)
    faltam = re.findall(r"@@\w+", saida)
    if faltam:
        raise SystemExit(f"marcadores não resolvidos: {faltam}")
    (D / "revisao_final.qmd").write_text(saida + "\n", encoding="utf-8")
    print("revisao_final.qmd escrito;", len(re.findall(r"\S+", saida)), "tokens")


if __name__ == "__main__":
    main()
