"""Monta 09-documento-final/suplemento.qmd (material suplementar do artigo) a partir de _esqueleto_suplemento.qmd.

Cada linha @@TABELA <nome>@@ do esqueleto vira o conteúdo da seção, lido dos arquivos do projeto sem digitar números:

  s1_busca           S1   estratégias de busca: apêndice B (PRISMA-S) de 07-relatorio/relatorio.qmd, sem caminhos de
                          arquivo no texto
  s2_atalhos         S2   atalhos A1 a A5 × recomendações de Garritty et al. (2024) × consequência provável, de
                          09-documento-final/insumos/garritty_2024.md, seção 4 (se o arquivo não existir: "em preparação")
  s3_emendas         S3   emendas, uma linha cada, da tabela "Resumo" de 00-protocolo/emendas.md, com a data e se foram
                          decididas antes ou depois de ver os dados (pelo tipo da emenda; a Emenda 3 tem texto próprio,
                          porque, além da correção de registro, trocou o árbitro do risco de viés)
  s4_caracteristicas S4   09-documento-final/insumos/tabelas/caracteristicas.md e, na segunda tabela (tbl-s4-excluidos),
                          os excluídos no texto completo que poderiam parecer elegíveis (PRISMA 16b): as chaves de
                          09-documento-final/referencias_excluidos.bib, com o critério de 03-textos/elegibilidade_tc_final.csv
                          e quem decidiu, de 00-protocolo/correcao_atribuicao.csv
  s5_rob             S5   insumos/tabelas/rob2.md, robins.md e epoc.md; o EPOC recodificado em B/A/I/n.a., com legenda
  s6_efeitos         S6   insumos/tabelas/individuais.md
  s7_fora            S7   insumos/tabelas/fora.md
  s8_sensibilidades  S8   insumos/tabelas/sens.md e as linhas do agrupamento amplo de insumos/tabelas/sof.md
  s9_caixa           S9   insumos/caixa_oqf_celulas.md e insumos/caixa_oqf_painel.md
  s10_regional       S10  insumos/tabelas/regional.md e viabilidade.md
  s11_checklists     S11  "em preparação" (os checklists são preenchidos depois do texto final)

As tabelas copiadas ganham legendas novas, sem caminhos de arquivo, e rótulos tbl-s<n>-... próprios do suplemento.
Tabelas largas vão em ::: {.tabela-larga} ou ::: {.landscape}, sempre no nível de cima. Nenhum travessão (U+2014): em
célula de tabela vira "n.a."; no texto, vírgula. Marcadores {arquivo:caminho} do esqueleto são resolvidos como no
artigo (montar_revisao_final.resolver_marcadores). O YAML montado recebe pendencias-abertas, rascunho e nocite com as
chaves dos incluídos, como o artigo.

Checagens (sai com erro): marcador ou "@@" que sobrar; seção do contrato revista/rotulos.yml (lista "suplemento")
sem ID no documento; "](../"; travessão.

USO (de qualquer pasta):  python3 09-documento-final/montar_suplemento.py
Render (só este arquivo):  cd 09-documento-final && TYPST_IGNORE_SYSTEM_FONTS=true TYPST_IGNORE_EMBEDDED_FONTS=true \\
                           quarto render suplemento.qmd --to typst
"""
import csv
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # não deixar __pycache__ na pasta do documento
D = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("montar_revisao_final", D / "montar_revisao_final.py")
mrf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mrf)

R, INS, REV = mrf.R, mrf.INS, mrf.REV
ESQUELETO = D / "_esqueleto_suplemento.qmd"
SAIDA = D / "suplemento.qmd"
TRAVESSAO = "—"
RX_ARQ = r"`[^`\n]+\.(?:md|qmd|csv|py|json|R|yml)`"


# ================================================================ utilidades
def tabela_sem_legenda(md):
    """Separa as linhas da tabela pipe (sem a legenda ': ...') de um .md gerado por gerar_tabelas_relatorio.py."""
    linhas = [l for l in mrf.ler(md).splitlines() if l.startswith("|")]
    if len(linhas) < 3:
        raise SystemExit(f"ERRO: tabela vazia em {md}")
    return linhas


def legenda(texto, rotulo, larguras=None):
    attr = f"#{rotulo}" + (f' tbl-colwidths="[{",".join(str(x) for x in larguras)}]"' if larguras else "")
    return f": {mrf.uma_linha(texto)} {{{attr}}}"


def bloco(tabela_linhas, texto_legenda, rotulo, larguras=None):
    return "\n".join(tabela_linhas) + "\n\n" + legenda(texto_legenda, rotulo, larguras)


def envolver(classe, conteudo):
    return f"::: {{.{classe}}}\n\n{conteudo}\n\n:::"


def celulas(linha):
    return [c.strip() for c in linha.strip().strip("|").split("|")]


def montar_linha(cels):
    return "| " + " | ".join(cels) + " |"


def sem_pares(txt):
    """PRESS é "Peer Review of Electronic Search Strategies"; o texto público não usa "revisão por pares"."""
    return re.sub(r"(revis(?:ão|ões))\s+por\s+pares", r"\1 por outro especialista", txt)


def sem_caminhos(txt):
    """Tira do texto as referências a arquivo e a linha de arquivo (`protocolo.md` linha 97; linhas 175 a 177)."""
    nums = r"\d+(?:\s*(?:,|a|e)\s*\d+)*"
    txt = re.sub(r"\s*\((?:[^()]*?)?" + RX_ARQ + r"(?:[^()]*?)?\)", "", txt)          # parêntese com arquivo
    txt = re.sub(r"[,;]?\s*" + RX_ARQ + r"(?:,?\s*linhas?\s+" + nums + r")?", "", txt)  # arquivo solto
    txt = re.sub(r"\s*\((?:linhas?|p-)\s*" + nums + r"\)", "", txt)                  # (linha 12)
    txt = re.sub(r"\s*\(linhas?\s+" + nums + r":[^()]*\)", "", txt)                  # (linha 354: "...")
    txt = re.sub(r"\s*\(p-\d+(?:\s*(?:,|e)\s*p-\d+)*\)", "", txt)                     # (p-80 e p-81)
    txt = re.sub(r",\s*p-\d+(?=\))", "", txt)                                           # , p-68)
    txt = re.sub(r"[,;]\s*linhas?\s+" + nums + r"(?=[)\].;,])", "", txt)             # , linha 89)
    txt = re.sub(r"\(\s*[,;]?\s*\)", "", txt)
    txt = re.sub(r"\s+([.,;:)])", r"\1", txt)
    return re.sub(r"[ \t]{2,}", " ", txt).strip()


def sem_travessao(txt):
    """Travessão: célula que é só "—" vira "n.a."; no resto do texto, vírgula."""
    fora = []
    for l in txt.split("\n"):
        if l.startswith("|"):
            cs = celulas(l)
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cs):
                fora.append(l)
                continue
            cs = ["n.a." if c == TRAVESSAO else c for c in cs]
            l = montar_linha(cs)
        l = re.sub(r"\s*" + TRAVESSAO + r"\s*", ", ", l)
        fora.append(l)
    return "\n".join(fora)


# ================================================================ S1
def s1_busca():
    rel = mrf.ler(R / "07-relatorio/relatorio.qmd")
    m = re.search(r"^# Apêndice B[^\n]*\n(.*?)(?=^# )", rel, flags=re.S | re.M)
    if not m:
        raise SystemExit("ERRO: apêndice B (estratégias de busca) não encontrado em 07-relatorio/relatorio.qmd")
    txt = m.group(1).strip()
    # sementes e proveniência da busca por citação: o texto cita arquivos; troca por uma referência neutra
    txt = re.sub(r"Sementes e proveniência em `[^`]+`(?: e `[^`]+`)?\.",
                 "Sementes e proveniência nos arquivos da busca por citação do projeto.", txt)
    partes, em_codigo = [], False
    for l in txt.split("\n"):
        if l.startswith("```"):
            em_codigo = not em_codigo
            partes.append(l)
            continue
        partes.append(l if em_codigo else sem_caminhos(l) if l.strip() else l)
    return "\n".join(partes)


# ================================================================ S2
def _tabela_md(texto):
    linhas = [l for l in texto.splitlines() if l.startswith("|")]
    if len(linhas) < 3:
        return None, []
    return celulas(linhas[0]), [celulas(l) for l in linhas[2:]]


def s2_atalhos():
    arq = INS / "garritty_2024.md"
    if not arq.exists():
        return "Em preparação: o cruzamento dos atalhos com as recomendações de @Garritty2024Rapid ainda não foi feito."
    txt = mrf.ler(arq)
    sec4 = re.search(r"^## 4\.[^\n]*\n(.*?)(?=^## \d)", txt, flags=re.S | re.M)
    if not sec4:
        raise SystemExit("ERRO: seção 4 de garritty_2024.md não encontrada")
    corpo = sec4.group(1)
    subs = re.split(r"(?m)^### ", corpo)
    intro = subs[0]
    linhas_rec, linhas_cons, outras = [], [], []
    for s in subs[1:]:
        titulo, resto = s.split("\n", 1)
        m = re.match(r"(A\d)\.\s*(.*)", titulo.strip())
        cab, rows = _tabela_md(resto.split("**Consequência provável.**")[0])
        if m:
            aid, nome = m.group(1), sem_caminhos(m.group(2))
            for r in rows:
                d = dict(zip(cab, r))
                rec = d.get("Recomendação", "")
                if "Etapa" in d:
                    rec = f"{d['Etapa']}: {rec}"
                porque = d.get("Por quê") or d.get("O que a revisão fez") or ""
                linhas_rec.append([f"{aid}", sem_caminhos(rec), sem_caminhos(d.get("Dentro ou fora", "")),
                                   sem_caminhos(porque)])
            cons = resto.split("**Consequência provável.**", 1)[1] if "**Consequência provável.**" in resto else ""
            cons = re.split(r"\n#{2,3} ", cons)[0]
            itens = []
            for l in cons.strip().splitlines():
                l = l.strip()
                if not l:
                    continue
                l = re.sub(r"^-\s+", "", l)
                itens.append(sem_caminhos(l))
            linhas_cons.append([f"**{aid}** {nome}", " ".join(itens)])
        elif titulo.startswith("Outras recomendações"):
            for r in rows:
                d = dict(zip(cab, r))
                outras.append([sem_caminhos(d.get("Recomendação", "")), sem_caminhos(d.get("Situação", ""))])
    if not linhas_rec or not linhas_cons:
        raise SystemExit("ERRO: garritty_2024.md, seção 4, sem as tabelas esperadas")
    nota_ia = ("Nenhuma das 24 recomendações trata de agentes de IA no lugar de revisores; quando a recomendação pede "
               "uma segunda pessoa, o atalho foi classificado como fora, mesmo com dois avaliadores de IA.")
    if "Nenhuma das 24 recomendações" not in intro:
        nota_ia = ""
    t1 = bloco([mrf.pipe(["Atalho", "Recomendação de Garritty et al.", "Dentro ou fora", "Por quê"],
                         linhas_rec)],
               f"Atalhos declarados no protocolo frente às recomendações de @Garritty2024Rapid (número da "
               f"recomendação no artigo). {nota_ia} Julgamento de IA, não conferido por humano.",
               "tbl-s2-atalhos", [8, 24, 16, 52])
    t2 = bloco([mrf.pipe(["Atalho", "Consequência provável para os resultados"], linhas_cons)],
               "Consequência provável de cada atalho. É inferência, não resultado medido; na maior parte dos casos, a "
               "direção do viés sobre *bandwagon* × *underdog* é indeterminada.", "tbl-s2-consequencias", [22, 78])
    t1, t2 = sem_pares(t1), sem_pares(t2)
    partes = [envolver("tabela-larga", t1), envolver("tabela-larga", t2)]
    if outras:
        t3 = bloco([mrf.pipe(["Recomendação", "Situação nesta revisão"], outras)],
                   "Outras recomendações que a revisão não segue ou segue em parte, fora dos atalhos declarados.",
                   "tbl-s2-outras", [35, 65])
        partes.append(sem_pares(t3))
    return "\n\n".join(partes)


# ================================================================ S3
TIPO_EMENDA = {"A": "contingência prevista no protocolo", "B": "emenda antes da triagem",
               "C": "emenda depois de ver dados", "D": "método planejado não executado",
               "E": "correção de erro ou incoerência"}
ANTES_DEPOIS = {"A": "antes de ver os dados dos estudos (contingência prevista no protocolo)",
                "B": "antes de ver os dados", "C": "depois de ver os dados", "D": "não se aplica",
                "E": "correção de registro ou de omissão, sem nova decisão de método"}


# Emenda 3: 00-protocolo/emendas.md, seção da Emenda 3 (codebooks copiados e troca do árbitro previsto no protocolo por
# decisão de custo do autor) e linha do Resumo ("extração e RoB (G7), antes de qualquer avaliação")
EMENDA3_OBJETO = ("codebooks de risco de viés copiados para o protocolo; troca do árbitro do RoB (decisão de custo do "
                  "autor, antes de qualquer avaliação)")
EMENDA3_QUANDO = ("correção de registro (codebooks) e decisão de método (árbitro), ambas antes de qualquer avaliação de "
                  "risco de viés")


def s3_emendas():
    txt = mrf.ler(R / "00-protocolo/emendas.md")
    resumo = txt.split("## Resumo", 1)[1].split("\n## ", 1)[0]
    linhas = []
    titulos = dict(re.findall(r"(?m)^## (Emenda \d+) \S+ \d\d/\d\d/\d{4} \S+ (.+)$", txt))
    for l in resumo.splitlines():
        if not re.match(r"\|\s*(E\d{3}|Emenda \d+)\s*\|", l):
            continue
        idd, data, versao, secao, tipo, etapa, reexec = celulas(l)
        a, m_, d = data.split("-")
        tipos = re.findall(r"[A-E]", tipo)
        objeto = titulos.get(idd, secao)
        objeto = re.sub(r"\s*\(tipo[^)]*\)\s*$", "", objeto)
        quando = "; ".join(ANTES_DEPOIS[t] for t in tipos)
        if idd == "Emenda 6":
            quando = "6a: " + ANTES_DEPOIS["E"] + "; 6b: " + ANTES_DEPOIS["C"]
        if idd == "Emenda 3":  # tipo E, mas a emenda também registrou uma decisão de método do autor
            objeto = EMENDA3_OBJETO
            quando = EMENDA3_QUANDO
        linhas.append([idd, f"{d}/{m_}/{a}", sem_caminhos(objeto), " e ".join(f"{t} ({TIPO_EMENDA[t]})" for t in tipos),
                       sem_caminhos(etapa), quando, sem_caminhos(reexec)])
    if not linhas:
        raise SystemExit("ERRO: tabela Resumo de 00-protocolo/emendas.md sem linhas")
    t = bloco([mrf.pipe(["Emenda", "Data", "Objeto", "Tipo", "Etapa no momento", "Antes ou depois de ver os dados",
                         "Reexecução exigida"], linhas)],
              "Emendas ao protocolo, na ordem em que foram decididas. Tipos do log de emendas: A, contingência prevista "
              "acionada; B, emenda antes da triagem; C, emenda depois de ver dados; D, método planejado não "
              "executado; E, correção de erro ou incoerência. As emendas E001 e E002 aplicam regras de validação "
              "da busca previstas no protocolo e não mudaram o protocolo.", "tbl-s3-emendas",
              [9, 9, 20, 16, 16, 18, 12])
    return envolver("landscape", t)


# ================================================================ S4 a S10: tabelas copiadas
def s4_caracteristicas():
    linhas = [l.replace("(sem efeito principal extraído)", "(nenhum efeito principal extraído)")
              for l in tabela_sem_legenda(INS / "tabelas/caracteristicas.md")]
    t = bloco(linhas,
              "Características dos estudos incluídos, um por linha, com os relatos adicionais do mesmo estudo entre "
              "parênteses. Ano do relato principal. Construto: desfechos extraídos do estudo. Risco de viés geral por "
              "resultado (ferramenta: julgamento), rascunho de IA não validado; \"não avaliado\" quando o estudo não "
              "tem efeito principal.", "tbl-s4-caracteristicas", [15, 5, 15, 10, 13, 9, 7, 9, 17])
    return envolver("landscape", t) + "\n\n" + s4_excluidos()


CRITERIO = {  # critérios de elegibilidade do protocolo (seção 3; 00-protocolo/codebook_elegibilidade.csv)
    "c1_populacao_contexto": "C1: população ou contexto fora do escopo",
    "c2_intervencao_estudada": "C2: pesquisa não é a exposição estudada",
    "c3_desfecho": "C3: sem desfecho de voto ou comparecimento",
    "c4_desenho_elegivel": "C4: desenho não elegível",
    "c5_estudo_primario": "C5: não é estudo primário",
    "c6_nao_retratado": "C6: retratado",
}


def s4_excluidos():
    """Excluídos no texto completo que poderiam parecer elegíveis (PRISMA 16b), um por linha: as chaves de
    referencias_excluidos.bib (as citadas na seção 3.1 do artigo), o critério que falhou (elegibilidade_tc_final.csv)
    e quem decidiu (correcao_atribuicao.csv: autor no caso limítrofe; IA estendendo regra do autor; ou IA)."""
    chaves = re.findall(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,", mrf.ler(D / "referencias_excluidos.bib"))
    if not chaves:
        raise SystemExit("ERRO: referencias_excluidos.bib sem entradas")
    elig = {r["chave"]: r for r in csv.DictReader(open(R / "03-textos/elegibilidade_tc_final.csv", encoding="utf-8-sig"))}
    quem = {}
    for r in csv.DictReader(open(R / "00-protocolo/correcao_atribuicao.csv", encoding="utf-8-sig")):
        if r["etapa"] == "07_textos_elegibilidade" and r["evento"] == "decisao_override":
            quem[r["objeto"].split()[0]] = (r["classificacao"], r["ator_real"])
    linhas = []
    for k in chaves:
        e = elig.get(k)
        if e is None or e["decisao"] != "excluir" or e["criterio_falhou"] not in CRITERIO:
            raise SystemExit(f"ERRO: {k} não está como exclusão com critério conhecido em elegibilidade_tc_final.csv")
        cls, ator = quem.get(e["id_rs"], ("", ""))
        if (cls, ator) == ("mantida", "humano"):
            decisor = "autor (caso limítrofe)"
        elif ator.startswith("ia_"):
            decisor = "IA, estendendo regra do autor"
        elif not ator:
            decisor = "IA"
        else:
            raise SystemExit(f"ERRO: atribuição inesperada de {k} ({e['id_rs']}): {cls} / {ator}")
        linhas.append((e["criterio_falhou"], k.lower(), [f"@{k}", CRITERIO[e["criterio_falhou"]], decisor]))
    linhas = [l for _, _, l in sorted(linhas)]
    return bloco([mrf.pipe(["Estudo", "Motivo da exclusão (critério do protocolo)", "Quem decidiu"], linhas)],
                 "Estudos excluídos na leitura do texto completo que poderiam parecer elegíveis (PRISMA 16b), com o "
                 "critério de elegibilidade que não atenderam. As exclusões decididas pela IA aguardam conferência "
                 "humana (P041).", "tbl-s4-excluidos", [30, 45, 25])


def recodificar_epoc(linhas):
    mapa = {"baixo": "B", "alto": "A", "incerto": "I", "não se aplica": "n.a."}
    out = linhas[:2]
    for l in linhas[2:]:
        cs = celulas(l)
        novos = cs[:2]
        for c in cs[2:]:
            marca = "†" if c.endswith("†") else ""
            base = c.rstrip("†")
            if base not in mapa:
                raise SystemExit(f"ERRO: valor EPOC inesperado: {c!r}")
            novos.append(mapa[base] + marca)
        out.append(montar_linha(novos))
    return out


def s5_rob():
    rob2 = bloco(tabela_sem_legenda(INS / "tabelas/rob2.md"),
                 "RoB 2 por domínio (consenso), para os resultados randomizados. D1b: recrutamento em desenho por "
                 "conglomerado. † = domínio em desacordo entre os avaliadores de IA A e B, com o consenso proposto pelo "
                 "árbitro de IA; nenhum julgamento validado por humano.", "tbl-s5-rob2")
    robins = bloco(tabela_sem_legenda(INS / "tabelas/robins.md"),
                   "ROBINS-I V2 por domínio (consenso), para experimentos naturais, quase-experimentos e painéis. "
                   "† como na tabela anterior.", "tbl-s5-robins")
    epoc = bloco(recodificar_epoc(tabela_sem_legenda(INS / "tabelas/epoc.md")),
                 "EPOC por critério (consenso), para proibições e comparações com unidades agregadas. B = baixo; "
                 "A = alto; I = incerto; n.a. = critério que não se aplica ao desenho. GC = critérios para desenho com "
                 "grupo controle; ITS = série temporal interrompida. Sequência aleatória e ocultação da alocação ficam "
                 "fora do geral (Emenda 4a). † como nas tabelas anteriores.", "tbl-s5-epoc", [10, 7] + [5] * 16 + [3])
    return envolver("landscape", rob2 + "\n\n" + robins + "\n\n" + epoc)


def s6_efeitos():
    t = bloco(tabela_sem_legenda(INS / "tabelas/individuais.md"),
              "Efeitos principais por estudo. g de Hedges alinhado: positivo = *bandwagon*, viabilidade, *momentum* a "
              "favor ou mobilização. EP = erro-padrão. NR = não calculado ou não relatado; nulo por ±δ = IC 95% inteiro "
              "dentro de ±δ. \"Na contagem?\" diz se o efeito entra no teste de sinal da síntese principal e, se não, "
              "por quê. Nenhum efeito foi conferido por humano na página do texto (P039).",
              "tbl-s6-efeitos", [14, 6, 9, 10, 13, 14, 24, 10])
    return envolver("tabela-larga", t)


def s7_fora():
    t = bloco(tabela_sem_legenda(INS / "tabelas/fora.md"),
              "Efeitos principais fora da contagem e motivo registrado para cada um, na versão depois das arbitragens "
              "de 23/09/2026.", "tbl-s7-fora", [14, 6, 9, 16, 55])
    return envolver("tabela-larga", t)


def s8_sensibilidades():
    sens = bloco(tabela_sem_legenda(INS / "tabelas/sens.md"),
                 "Análises de sensibilidade da SWiM no agrupamento amplo (desfecho × célula de alvo × classe de "
                 "desenho). O agrupamento amplo junta famílias e comparadores que o protocolo manda separar e é "
                 "descritivo, decidido depois de ver os dados (Emenda 5). Certeza GRADE só para o agrupamento amplo "
                 "sem outras mudanças; nas demais análises, sem GRADE próprio.", "tbl-s8-sensibilidades",
                 [15, 13, 9, 25, 14, 11, 5, 8])
    sof = tabela_sem_legenda(INS / "tabelas/sof.md")
    amplo = sof[:2] + [l for l in sof[2:] if celulas(l)[0].startswith("agrupamento amplo")]
    if len(amplo) <= 2:
        raise SystemExit("ERRO: sof.md sem linhas do agrupamento amplo")
    sof_amplo = bloco(amplo,
                      "Resumo dos achados do agrupamento amplo, *post hoc* (GRADE, rascunho de IA não validado). n de "
                      "cada estudo como nas células do protocolo (artigo, Tabela 2). A certeza qualifica a direção, não "
                      "a magnitude. Esta análise não aparece no resumo dos achados do artigo.", "tbl-s8-sof-amplo",
                      [24, 26, 20, 8, 22])
    return envolver("landscape", sens + "\n\n" + sof_amplo)


FAMILIA_PAINEL = {"Agregador ou projeção": "agregador_projecao", "Boca de urna": "boca_de_urna",
                  "Apuração parcial oficial": "outro", "Pesquisa pré-eleitoral": "pesquisa_pre_eleitoral"}
CONSTRUTO_PAINEL = {"Apoio": "apoio_ao_lider", "Comparecimento": "mobilizacao"}
ORDEM_CERTEZA = ["muito_baixa", "baixa", "moderada", "alta"]


def painel_por_celulas(linhas):
    """Refaz as colunas Certeza (maior entre as células) e Estudos (união) do painel a partir de revista/celulas.json;
    mantém Rótulo e Força como a ferramenta da caixa gerou."""
    cel = json.load(open(D / "revista/celulas.json", encoding="utf-8"))["celulas"]
    cab = celulas(linhas[0])
    i_int, i_res, i_cer, i_est = (cab.index(c) for c in ("Intervenção", "Resultado", "Certeza", "Estudos"))
    saida = linhas[:2]
    for l in linhas[2:]:
        cols = celulas(l)
        fam, con = FAMILIA_PAINEL[cols[i_int]], CONSTRUTO_PAINEL[cols[i_res]]
        grupo = [c for c in cel if c["familia_intervencao"] == fam and c["construto_outcome"] == con]
        if not grupo:
            raise SystemExit(f"ERRO: painel sem células para {cols[i_int]} × {cols[i_res]}")
        cols[i_cer] = max((c["certeza"] for c in grupo), key=ORDEM_CERTEZA.index).replace("_", " ")
        cols[i_est] = str(len({e for c in grupo for e in c["estudos"]}))
        saida.append("| " + " | ".join(cols) + " |")
    return saida


def s9_caixa():
    cel = bloco(tabela_sem_legenda(INS / "caixa_oqf_celulas.md"),
                "Caixa de ferramentas célula a célula. Direção: estudos a favor (*bandwagon*, viabilidade, *momentum* a "
                "favor ou mobilização), contra e nulos. Rótulo pela regra `caixa-3`, calculado no nível formato de "
                "exposição × desfecho × desenho e repetido em cada célula; certeza GRADE sobre a direção, rascunho de "
                "IA não validado.", "tbl-s9-celulas", [12, 14, 11, 9, 20, 12, 7, 8, 7])
    painel = bloco(painel_por_celulas(tabela_sem_legenda(INS / "caixa_oqf_painel.md")),
                   "Painel OQF por formato de exposição e desfecho: rótulo e força pela regra `caixa-3`, como saíram da "
                   "ferramenta da caixa; certeza GRADE (a maior entre as células do painel) e número de estudos (união "
                   "das células) refeitos a partir das 18 células, porque a ferramenta leu uma só célula por formato × "
                   "desfecho × desenho. Com todas as células, o rótulo segue Inconclusivo em todas as linhas; a força "
                   "da linha de pesquisa pré-eleitoral × comparecimento foi calculada pela ferramenta com certeza "
                   "baixa e depende da revisão da caixa (P042).", "tbl-s9-painel")
    return envolver("landscape", cel) + "\n\n" + painel


def s10_regional():
    reg = bloco(tabela_sem_legenda(INS / "tabelas/regional.md"),
                "Estudos codificados com região Brasil ou América Latina no fichamento. @Lago2015 é um corte transversal "
                "de 46 países, entre eles o Brasil.", "tbl-s10-regional", [13, 20, 14, 23, 30])
    viab = bloco(tabela_sem_legenda(INS / "tabelas/viabilidade.md"),
                 "Efeitos principais de viabilidade e de *momentum*. Positivo = mais apoio à opção mostrada como viável, "
                 "menos à mostrada como inviável ou abaixo da cláusula, ou mais apoio ao partido mostrado ganhando "
                 "apoio. Direção do estudo na síntese principal (NR quando o estudo não entra nela).",
                 "tbl-s10-viabilidade", [13, 5, 9, 11, 11, 9, 11, 9, 10, 12])
    return envolver("tabela-larga", reg) + "\n\n" + envolver("landscape", viab)


def s11_checklists():
    return ("Em preparação. As listas de conferência do PRISMA 2020, do SWiM, do PRISMA-S e do PRISMA-trAIce (esta "
            "última só como lista de conferência) serão preenchidas depois da versão final do texto, com o local de "
            "cada item no artigo.")


SECOES = {"s1_busca": s1_busca, "s2_atalhos": s2_atalhos, "s3_emendas": s3_emendas,
          "s4_caracteristicas": s4_caracteristicas, "s5_rob": s5_rob, "s6_efeitos": s6_efeitos, "s7_fora": s7_fora,
          "s8_sensibilidades": s8_sensibilidades, "s9_caixa": s9_caixa, "s10_regional": s10_regional,
          "s11_checklists": s11_checklists}


# ================================================================ montagem
def main():
    esq = mrf.ler(ESQUELETO)
    esq = mrf.resolver_marcadores(esq, onde="_esqueleto_suplemento.qmd")

    def troca(m):
        nome = m.group(1)
        if nome not in SECOES:
            raise SystemExit(f"ERRO: seção desconhecida: @@TABELA {nome}@@")
        return sem_travessao(SECOES[nome]())
    saida = re.sub(r"^@@TABELA (\w+)@@[ \t]*$", troca, esq, flags=re.M)
    # seção que começa com página deitada: título e introdução entram na página deitada, para não sobrar uma
    # página em pé só com o título (o ::: {.landscape} continua no nível de cima)
    saida = re.sub(r"(?m)^(# [^\n]*\{#s\d+-[\w-]+[^}\n]*\}\n\n(?:(?!# |:::)[^\n]*\n+)*?)(::: \{\.landscape\}\n\n)",
                   r"\2\1", saida)
    saida = mrf.metadados(saida, mrf.linhas_metadados())

    erros = []
    if "@@" in saida:
        erros.append("sobrou '@@'")
    ids = set(re.findall(r"\{[^{}\n]*#([\w-]+)", saida))
    for s in mrf.ROTULOS.get("suplemento") or []:
        if s not in ids:
            erros.append(f"seção #{s} do contrato sem ID no suplemento")
    if "](../" in saida:
        erros.append("caminho com '](../'")
    if TRAVESSAO in saida:
        erros.append("travessão (U+2014) no texto")
    if erros:
        raise SystemExit("ERRO em suplemento.qmd:\n  " + "\n  ".join(erros))
    SAIDA.write_text(saida + "\n", encoding="utf-8")
    n_tab = len(re.findall(r"(?m)^: .*\{#tbl-", saida))
    n_tok = len(re.findall(r"\S+", saida))
    print(f"suplemento.qmd escrito; {n_tab} tabelas; {n_tok} tokens")


if __name__ == "__main__":
    main()
