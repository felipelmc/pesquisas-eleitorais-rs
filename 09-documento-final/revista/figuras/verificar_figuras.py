"""Confere as 7 figuras do artigo contra as origens. Sai com código 1 se algo falhar.

USO (de qualquer pasta)
    python3 09-documento-final/revista/figuras/verificar_figuras.py

Checagens
  (i)   contagens dos dados_*.csv iguais às da origem:
          células       x celulas.json e swim_principal/swim_resumo.json
          direção       x swim_principal e swim_sens_com_excluidos_amplo (tabelas/swim_direcao.csv) e celulas.json
          PRISMA        x 07-relatorio/prisma_contagens.json (e cada n desenhado no SVG); contagem do JSON fora da
                        figura só se for 0 (caixa que não se aplica); os casos limítrofes da legenda (n, inclusões e
                        exclusões) x 00-protocolo/correcao_atribuicao.csv e rs_log.jsonl
          risco de viés x 04-qualidade/rob_*_consenso.csv e rob_geral.csv
          realismo      x tabelas T9 e T14 impressas por insumos/contagens_mecanismos_moderadores.py
          metas         x meta_entrada_*.csv e meta_*/meta_resumo.json; efeitos em ordem de erro-padrão crescente;
                        risco de viés de cada efeito x 04-qualidade/rob_geral.csv e a frase da legenda sobre ele;
                        rótulo "g (IC)" com arredondamento decimal meio para cima e presente no SVG
  (ii)  texto dos SVG sem termo proibido (benéfic, danos, Neutro, "sem efeito", significativ, travessão) nem
        número com ponto decimal (ponto só como separador de milhar: 1.767); sem espaço inicial ou final em
        <text> (o Typst o descarta e estica o resto); só a família Fira Sans; corpo mínimo de 7 pt; PNG a
        300 dpi na largura declarada
  (iii) arestas de dados/dag_arestas.csv iguais às de 00-protocolo/dag_v1.mmd (e nós iguais)
  (iv)  legendas.yml com legenda, alt e largura para as 7 figuras; alt sem números; marcadores resolvidos
Só lê arquivos.
"""
import collections
import csv
import html
import json
import re
import subprocess
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.dont_write_bytecode = True  # não deixa __pycache__ nas pastas dos módulos importados por caminho

R = Path(__file__).resolve().parents[3]
FIG = R / "09-documento-final/revista/figuras"
DADOS = FIG / "dados"
SAIDA = FIG / "saida"
NOMES = ["modelo_logico", "prisma", "rob", "celulas", "direcao", "metas", "realismo"]
LARGURA = {"texto": 140, "larga": 168}  # larga = 140 mm da mancha + 2 x 14 mm do pad do template (sem redução)
CORPO_MIN = 7.0  # pt; tema_revista.R
erros = []


def erro(msg):
    erros.append(msg)


def ler_csv(caminho):
    with open(caminho, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def ler_json(rel):
    with open(R / rel, encoding="utf-8") as f:
        return json.load(f)


def quase(a, b, tol=1e-9):
    if a in ("", None) or b in ("", None):
        return (a in ("", None)) and (b in ("", None))
    return abs(float(a) - float(b)) <= tol


def inteiro_br(n):
    return f"{int(n):,}".replace(",", ".")


# ================================================================ (i) contagens
def conf_celulas():
    cj = ler_json("09-documento-final/revista/celulas.json")
    swim = {tuple(g[k] for k in cj["chave"]): g for g in ler_json("06-analise/swim_principal/swim_resumo.json")["grupos"]}
    d = ler_csv(DADOS / "dados_celulas.csv")
    por_id = {c["id"]: c for c in cj["celulas"]}
    if len(d) != cj["n_celulas"] + cj["n_vazias"]:
        erro(f"células: {len(d)} linhas no CSV; celulas.json tem {cj['n_celulas']} + {cj['n_vazias']} vazia(s)")
    vistas = set()
    for r in d:
        if r["id"] == "vazia":
            chaves = [tuple(v[k] for k in cj["chave"]) for v in cj["vazias"]
                      if v["comparador_tipo"] == r["comparador"] and v["familia_intervencao"] == r["familia"]
                      and v["classe_desenho"] == r["classe"]]
            if len(chaves) != 1:
                erro(f"células: linha vazia sem par em celulas.json: {r}")
                continue
            k = chaves[0]
            if r["k"] != "0" or r["marca"] != "vazia":
                erro(f"células: célula vazia com k ou marca errados: {r['k']} {r['marca']}")
        else:
            c = por_id.get(r["id"])
            if not c:
                erro(f"células: id {r['id']} fora de celulas.json")
                continue
            k = tuple(c[x] for x in cj["chave"])
            if (r["familia"], r["comparador"], r["classe"]) != (k[0], k[2], k[4]):
                erro(f"células: chave de {r['id']} difere de celulas.json")
            pares = [("k", "k"), ("n_com_direcao", "n_estudos_com_direcao"), ("n_a_favor", "n_beneficos"),
                     ("n_contra", "n_danosos"), ("n_mistos", "n_mistos"), ("n_nulos", "n_nulos")]
            for a, b in pares:
                if int(r[a]) != int(c[b]):
                    erro(f"células {r['id']}: {a} = {r[a]} no CSV e {c[b]} em celulas.json")
            if not quase(r["proporcao"], c["proporcao"]):
                erro(f"células {r['id']}: proporção difere")
            ic = c["ic_proporcao"] or ["", ""]
            if not (quase(r["ic_inf"], ic[0]) and quase(r["ic_sup"], ic[1])):
                erro(f"células {r['id']}: IC difere")
            if r["certeza"] != c["certeza"] or r["certeza_texto"] != c["certeza_texto"]:
                erro(f"células {r['id']}: certeza difere")
            esperado = (f"{c['n_beneficos']} de {c['n_estudos_com_direcao']}" if c["n_estudos_com_direcao"]
                        else f"{c['n_nulos']} nulo")
            if not r["rotulo_xy"].startswith(esperado):
                erro(f"células {r['id']}: rótulo x de y '{r['rotulo_xy']}' não começa com '{esperado}'")
        g = swim.get(k)
        if not g:
            erro(f"células: {k} fora de swim_resumo.json")
            continue
        for a, b in [("k", "k_estudos"), ("n_com_direcao", "n_estudos"), ("n_a_favor", "n_beneficos"),
                     ("n_contra", "n_danosos"), ("n_mistos", "n_mistos"), ("n_nulos", "n_nulos")]:
            if int(r[a]) != int(g[b]):
                erro(f"células {r['id']}: {a} = {r[a]} no CSV e {g[b]} em swim_resumo.json")
        vistas.add(k)
    if vistas != set(swim):
        erro(f"células: grupos da SWiM principal sem linha no CSV: {set(swim) - vistas}")


def conf_direcao():
    d = ler_csv(DADOS / "dados_direcao.csv")
    prin = ler_csv(R / "06-analise/swim_principal/tabelas/swim_direcao.csv")
    amplo = ler_csv(R / "06-analise/swim_sens_com_excluidos_amplo/tabelas/swim_direcao.csv")
    ctr = lambda r: r["excluido_rob_critico"] == "TRUE"
    orig_p = collections.Counter()
    chaves_p = set()
    for r in prin:
        fam, con, comp, cel, cls = [x.strip() for x in r["grupo"].split("|")]
        orig_p[(r["chave"], con, cel, cls, r["direcao"], r["rob_geral"], ctr(r))] += 1
        chaves_p.add((r["chave"], con, cel))
    fig_p = collections.Counter((r["chave"], r["construto"], r["celula_alvo"], r["classe"], r["direcao"], r["rob_geral"],
                                 r["excluido_critico"] == "1") for r in d if r["painel"] == "principal")
    if orig_p != fig_p:
        erro(f"direção (principal): CSV difere de swim_direcao.csv: {(orig_p - fig_p) + (fig_p - orig_p)}")
    orig_f = collections.Counter()
    for r in amplo:
        con, cel, cls = [x.strip() for x in r["grupo"].split("|")]
        if (r["chave"], con, cel) not in chaves_p:
            orig_f[(r["chave"], con, cel, cls, r["direcao"], r["rob_geral"], ctr(r))] += 1
    fig_f = collections.Counter((r["chave"], r["construto"], r["celula_alvo"], r["classe"], r["direcao"], r["rob_geral"],
                                 r["excluido_critico"] == "1") for r in d if r["painel"] == "fora")
    if orig_f != fig_f:
        erro(f"direção (fora da contagem): CSV difere do agrupamento amplo: {(orig_f - fig_f) + (fig_f - orig_f)}")
    # contagens por célula (sem os críticos) = celulas.json
    cj = ler_json("09-documento-final/revista/celulas.json")
    por_cel = collections.defaultdict(collections.Counter)
    for r in d:
        if r["painel"] == "principal" and r["excluido_critico"] == "0" and r["celula_id"] != "vazia":
            por_cel[r["celula_id"]][r["direcao"]] += 1
    for c in cj["celulas"]:
        esperado = {"benefico": c["n_beneficos"], "danoso": c["n_danosos"], "misto": c["n_mistos"], "nulo": c["n_nulos"]}
        obtido = {k: por_cel[c["id"]].get(k, 0) for k in esperado}
        if esperado != obtido:
            erro(f"direção: contagem da célula {c['id']} difere de celulas.json: {obtido} x {esperado}")


def valor_json(obj, caminho):
    for p in caminho.split("."):
        obj = obj[int(p)] if isinstance(obj, list) else obj[p]
    return obj


def casos_limitrofes():
    """Casos limítrofes do texto completo decididos pelo autor: linhas da etapa 07 mantidas como humanas em
    00-protocolo/correcao_atribuicao.csv, conferidas no rs_log.jsonl (evento decisao_override de ator humano na mesma
    seq). Conta registros distintos (a linha de teste repete a decisão de outra). Devolve (total, inclusões, exclusões)."""
    log = {}
    for l in open(R / "rs_log.jsonl", encoding="utf-8"):
        e = json.loads(l)
        log[e.get("seq")] = e
    dec = {}
    for r in ler_csv(R / "00-protocolo/correcao_atribuicao.csv"):
        if (r["etapa"], r["classificacao"], r["ator_real"]) != ("07_textos_elegibilidade", "mantida", "humano"):
            continue
        e = log.get(int(r["seq"]))
        if not e or e.get("evento") != "decisao_override" or (e.get("ator") or {}).get("tipo") != "humano":
            erro(f"PRISMA: seq {r['seq']} de correcao_atribuicao.csv não é decisão humana no rs_log.jsonl")
            continue
        for o in e["dados"]["overrides"]:
            if o["rodada"] != "tc" or dec.get(o["id_rs"], o["decisao"]) != o["decisao"]:
                erro(f"PRISMA: override {o} fora do texto completo ou em conflito com outro do mesmo registro")
            dec[o["id_rs"]] = o["decisao"]
    return len(dec), sum(d == "incluir" for d in dec.values()), sum(d == "excluir" for d in dec.values())


def conf_prisma(textos_svg, legenda=""):
    pj = ler_json("07-relatorio/prisma_contagens.json")
    d = ler_csv(DADOS / "dados_prisma.csv")
    usados = set()
    for r in d:
        if not r["caminho_json"]:
            continue
        v = valor_json(pj, r["caminho_json"])
        usados.add(r["caminho_json"])
        if int(r["n"]) != int(v):
            erro(f"PRISMA: {r['caminho_json']} = {r['n']} no CSV e {v} no JSON")
        if inteiro_br(v) not in r["texto"]:
            erro(f"PRISMA: texto '{r['texto']}' sem o n formatado {inteiro_br(v)}")
        alvo = r["texto"].replace("{n}", inteiro_br(v))
        num = re.search(r"\(n = ([\d.]+)\)|^([\d.]+) ", alvo)
        n_txt = (num.group(1) or num.group(2)) if num else inteiro_br(v)
        padrao = f"(n = {n_txt})" if num and num.group(1) else f"{n_txt} relatos"
        if padrao not in textos_svg["prisma"]:
            erro(f"PRISMA: '{padrao}' não aparece no SVG")
    obrig = []
    for ramo in ("bases", "outros_metodos"):
        b = pj[ramo]
        obrig += [f"{ramo}.removidos_antes_triagem.duplicatas", f"{ramo}.removidos_antes_triagem.outros_motivos",
                  f"{ramo}.triados", f"{ramo}.excluidos_triagem", f"{ramo}.buscados", f"{ramo}.nao_recuperados",
                  f"{ramo}.avaliados", f"{ramo}.excluidos_elegibilidade.total", f"{ramo}.incluidos_relatos"]
        obrig += [f"{ramo}.removidos_antes_triagem.automacao_por_filtro.{k}" for k in b["removidos_antes_triagem"]["automacao_por_filtro"]]
        obrig += [f"{ramo}.excluidos_elegibilidade.motivos.{k}" for k in b["excluidos_elegibilidade"]["motivos"]]
        obrig += [f"{ramo}.identificados.{k}" for k, v in b["identificados"].items() if not isinstance(v, dict)]
        if "por_fonte" in b["identificados"]:
            obrig += [f"{ramo}.identificados.por_fonte.{k}" for k in b["identificados"]["por_fonte"]]
    obrig += ["incluidos.estudos", "incluidos.relatos"]
    faltam = [c for c in obrig if c not in usados and valor_json(pj, c) != 0]
    if faltam:
        erro(f"PRISMA: contagens do JSON que a figura não desenha: {faltam}")
    if "(n = 0)" in textos_svg["prisma"]:
        erro("PRISMA: caixa ou item com n = 0 desenhado (deveria ser omitido)")
    n, ni, ne = casos_limitrofes()
    frase = f"exceto {n} casos limítrofes decididos pelos autores ({ni} inclusões e {ne} exclusões)"
    if frase not in re.sub(r"\s+", " ", legenda):
        erro(f"PRISMA: a legenda não traz '{frase}' (contagem de correcao_atribuicao.csv e rs_log.jsonl)")
    for ramo in ("bases", "outros_metodos"):
        b = pj[ramo]
        if b["removidos_antes_triagem"]["automacao"] != sum(b["removidos_antes_triagem"]["automacao_por_filtro"].values()):
            erro(f"PRISMA: automação do ramo {ramo} não é a soma dos filtros")


ROB_NIVEL = {"baixo": 1, "algumas_preocupacoes": 2, "moderado": 2, "incerto": 2, "alto": 3, "grave": 3, "critico": 4}


def conf_rob():
    d = ler_csv(DADOS / "dados_rob.csv")
    fig = collections.Counter()
    tot = {}
    for r in d:
        fig[(r["ferramenta"], r["dominio"], r["julgamento"])] += int(r["n"])
        tot.setdefault((r["ferramenta"], r["dominio"]), int(r["total"]))
        if int(r["nivel"]) != ROB_NIVEL[r["julgamento"]]:
            erro(f"RoB: nível errado para {r['julgamento']}")
        if not quase(r["proporcao"], int(r["n"]) / int(r["total"]), 1e-12):
            erro(f"RoB: proporção errada em {r['ferramenta']} {r['dominio']} {r['julgamento']}")
    orig = collections.Counter()
    for f in ("rob2", "robins_i", "epoc"):
        for r in ler_csv(R / f"04-qualidade/rob_{f}_consenso.csv"):
            orig[(f, r["dominio"], r["julgamento_consenso"])] += 1
    for r in ler_csv(R / "04-qualidade/rob_geral.csv"):
        orig[(r["ferramenta"], "geral", r["rob_geral"])] += 1
    if orig != fig:
        erro(f"RoB: contagens diferem da origem: {(orig - fig) + (fig - orig)}")
    somas = collections.Counter()
    for (f, dom, j), n in fig.items():
        somas[(f, dom)] += n
    for k, n in somas.items():
        if tot[k] != n:
            erro(f"RoB: total de {k} = {tot[k]} no CSV, soma {n}")


def tabela_md(saida, titulo):
    bloco = saida.split(f"## {titulo}")[1].split("\n## ")[0]
    linhas = [l for l in bloco.splitlines() if l.startswith("| ")]
    cab = [c.strip() for c in linhas[0].strip("|").split("|")]
    return [dict(zip(cab, [c.strip() for c in l.strip("|").split("|")])) for l in linhas[1:]]


def conf_realismo():
    out = subprocess.run([sys.executable, str(R / "09-documento-final/insumos/contagens_mecanismos_moderadores.py")],
                         cwd=R, capture_output=True, text=True, check=True).stdout
    d = ler_csv(DADOS / "dados_realismo.csv")
    cats = ["benefico", "danoso", "misto", "nulo", "benefico*", "danoso*"]
    for tab in ("T9", "T14"):
        titulo = {"T9": "T9.", "T14": "T14."}[tab]
        linhas = tabela_md(out, titulo)
        orig = {(l["realismo_contexto"], c): int(l[c]) for l in linhas for c in cats}
        fig = collections.Counter()
        for r in d:
            if r["tabela"] != tab:
                continue
            fig[(r["realismo"], r["direcao"] + ("*" if r["excluido_critico"] == "1" else ""))] += 1
        for k, v in orig.items():
            if fig.get(k, 0) != v:
                erro(f"realismo {tab}: {k} = {fig.get(k, 0)} no CSV e {v} na tabela do script")
        extra = set(fig) - set(orig)
        if extra:
            erro(f"realismo {tab}: categorias no CSV que não estão na tabela: {extra}")


ROB_GERAL = {(r["chave"], r["construto_outcome"]): r["rob_geral"] for r in ler_csv(R / "04-qualidade/rob_geral.csv")}
ROB_LEGENDA = {"baixo": "risco baixo", "algumas_preocupacoes": "algumas preocupações", "alto": "risco alto",
               "critico": "risco crítico"}


def dec_br(x, casas=2):
    d = Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-casas), rounding=ROUND_HALF_UP)
    if d.is_zero():
        d = d.copy_abs()
    return f"{d:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".").replace("-", "\u2212")


def conf_metas(textos_svg=None, legenda=""):
    legenda = re.sub(r"\s+", " ", legenda)
    d = ler_csv(DADOS / "dados_metas.csv")
    for painel, f_ent, f_res in (("a", "06-analise/meta_entrada_exploratoria.csv", "06-analise/meta_exploratoria/meta_resumo.json"),
                                 ("b", "06-analise/meta_entrada_mesmo_candidato.csv", "06-analise/meta_mesmo_candidato/meta_resumo.json")):
        ent = {e["id_efeito"]: e for e in ler_csv(R / f_ent)}
        res = ler_json(f_res)
        g = res["grupos"][0]["resultado"]
        x = [r for r in d if r["painel"] == painel]
        ef = [r for r in x if r["tipo"] == "efeito"]
        if {r["id_efeito"] for r in ef} != set(ent):
            erro(f"metas {painel}: efeitos diferem de {f_ent}")
        for r in ef:
            e = ent.get(r["id_efeito"])
            if e and not (quase(r["estimativa"], e["yi"]) and quase(r["ep"], e["sei"])):
                erro(f"metas {painel}: {r['id_efeito']} difere da entrada")
            if e and not quase(float(r["ic_sup"]) - float(r["ic_inf"]), 2 * 1.959963984540054 * float(e["sei"]), 1e-9):
                erro(f"metas {painel}: IC de {r['id_efeito']} não é g ± 1,96 EP")
        eps = [float(r["ep"]) for r in sorted(ef, key=lambda r: int(r["ordem"]))]
        if eps != sorted(eps):
            erro(f"metas {painel}: efeitos fora da ordem de erro-padrão crescente")
        for r in x:
            partes = [float(r["estimativa"]), float(r["ic_inf"]), float(r["ic_sup"])]
            esperado = "{} ({} a {})".format(*(dec_br(v) for v in partes))
            if r["rotulo_valor"] != esperado:
                erro(f"metas {painel}: rótulo '{r['rotulo_valor']}' difere de '{esperado}'")
            elif textos_svg is not None and r["rotulo_valor"] not in textos_svg:
                erro(f"metas {painel}: rótulo '{r['rotulo_valor']}' não aparece no SVG")
        for r in ef:
            e = ent.get(r["id_efeito"])
            if e and ROB_GERAL.get((e["chave"], e["construto_outcome"])) != r["rob_geral"]:
                erro(f"metas {painel}: risco de viés de {r['id_efeito']} difere de 04-qualidade/rob_geral.csv")
        niveis = {r["rob_geral"] for r in ef}
        m = re.search(rf"painel \*\*{painel}\*\*(?: estão em|, em) (algumas preocupações|risco \w+)", legenda)
        if len(niveis) != 1 or not m or m.group(1) != ROB_LEGENDA.get(niveis.pop()):
            erro(f"metas {painel}: a frase da legenda sobre o risco de viés não bate com rob_geral.csv")
        cb = [r for r in x if r["tipo"] == "combinado"]
        if len(cb) != 1 or not (quase(cb[0]["estimativa"], g["estimativa"]) and quase(cb[0]["ic_inf"], g["ic"][0])
                                and quase(cb[0]["ic_sup"], g["ic"][1])):
            erro(f"metas {painel}: estimativa combinada difere de {f_res}")
        if any(not quase(r["delta"], res["parametros"]["delta"]) for r in x):
            erro(f"metas {painel}: delta difere de parametros.delta")
        if any(int(r["k_estudos"]) != res["grupos"][0]["k_estudos"] or int(r["k_efeitos"]) != res["grupos"][0]["k_efeitos"]
               for r in x):
            erro(f"metas {painel}: k difere")


# ================================================================ (iii) DAG
def ler_mermaid():
    nos, arestas = {}, []
    for linha in open(R / "00-protocolo/dag_v1.mmd", encoding="utf-8"):
        s = linha.strip()
        if not s or s.startswith(("%%", "flowchart", "classDef", "class ")):
            continue
        partes = re.split(r"\s*(-->|-\.->)\s*", s)
        ids = []
        for p in partes[0::2]:
            m = re.match(r"^\s*([A-Za-z0-9_]+)(?:\[([^\]]+)\])?\s*$", p)
            if not m:
                erro(f"DAG: token do mermaid não reconhecido: {p!r}")
                return {}, []
            if m.group(2):
                nos[m.group(1)] = m.group(2)
            ids.append(m.group(1))
        for a, seta, b in zip(ids, partes[1::2], ids[1:]):
            arestas.append((a, b, "tracejada" if seta == "-.->" else "solida"))
    return nos, [(nos[a], nos[b], t) for a, b, t in arestas]


def conf_dag():
    nos, arestas = ler_mermaid()
    fig = [(r["de"], r["para"], r["tipo"]) for r in ler_csv(DADOS / "dag_arestas.csv")]
    if collections.Counter(fig) != collections.Counter(arestas):
        erro(f"DAG: arestas diferem do .mmd: faltam {set(arestas) - set(fig)}; sobram {set(fig) - set(arestas)}")
    dn = {r["nome"] for r in ler_csv(DADOS / "dados_modelo_logico.csv") if r["elemento"] == "no"}
    if dn != set(nos.values()):
        erro(f"DAG: nós diferem do .mmd: {dn ^ set(nos.values())}")
    teoria = open(R / "00-protocolo/teoria_programa.md", encoding="utf-8").read()
    bloco = teoria.split("## 4. Tabela Z")[1].split("\n## ")[0]
    n_z = sum(1 for l in bloco.splitlines() if l.startswith("| ") and not l.startswith(("| Moderador", "|---")))
    n_m = sum(1 for r in ler_csv(DADOS / "dados_modelo_logico.csv") if r["elemento"] == "moderador")
    if n_z != n_m:
        erro(f"DAG: {n_m} moderadores no quadro e {n_z} na tabela Z")


# ================================================================ (ii) SVG e PNG
PROIBIDOS = [r"ben[eé]fic", r"danos", r"neutro", r"sem efeito", r"significativ", "—"]


def textos_svg(nome):
    t = (SAIDA / f"{nome}.svg").read_text(encoding="utf-8")
    txt = [html.unescape(re.sub(r"<[^>]+>", "", m)) for m in re.findall(r"<text\b[^>]*>(.*?)</text>", t, re.S)]
    return t, txt


def conf_svg(nome, largura_mm):
    svg, bruto = textos_svg(nome)
    for x in bruto:
        if x != x.strip(" "):
            erro(f"{nome}.svg: texto com espaço inicial ou final (o leitor de SVG do Typst o descarta e estica o resto): '{x}'")
    txt = [x.replace("\u00a0", " ") for x in bruto]
    junto = "\n".join(txt)
    for p in PROIBIDOS:
        for x in txt:
            if re.search(p, x, re.I):
                erro(f"{nome}.svg: termo proibido ({p}) em '{x}'")
    for x in txt:
        for tok in re.findall(r"\d+(?:[.,]\d+)+", x):
            if "." in tok and not re.fullmatch(r"\d{1,3}(?:\.\d{3})+(?:,\d+)?", tok):
                erro(f"{nome}.svg: número com ponto decimal '{tok}' em '{x}'")
    fams = set(re.findall(r"font-family:\s*([^;'\"]+|\"[^\"]+\"|'[^']+')", svg))
    fams = {f.strip().strip('"').strip("'") for f in fams}
    if fams - {"Fira Sans"}:
        erro(f"{nome}.svg: famílias de fonte fora de Fira Sans: {fams - {'Fira Sans'}}")
    tams = [float(x) for x in re.findall(r"font-size:\s*([\d.]+)px", svg)]
    if tams and min(tams) < CORPO_MIN - 1e-6:
        erro(f"{nome}.svg: corpo {min(tams)} pt abaixo de {CORPO_MIN:g} pt")
    m = re.search(r"<svg[^>]*\bwidth='([\d.]+)pt'", svg)
    if not m or abs(float(m.group(1)) - largura_mm / 25.4 * 72) > 0.5:
        erro(f"{nome}.svg: largura diferente de {largura_mm} mm")
    png = (SAIDA / f"{nome}.png").read_bytes()
    if png[:8] != b"\x89PNG\r\n\x1a\n":
        erro(f"{nome}.png: não é PNG")
    else:
        w = int.from_bytes(png[16:20], "big")
        if abs(w - largura_mm / 25.4 * 300) > 2:
            erro(f"{nome}.png: {w} px de largura; esperado {largura_mm} mm a 300 dpi")
    return junto


# ================================================================ (iv) legendas
LEGENDAS = {}


def conf_legendas():
    import yaml
    leg = yaml.safe_load(open(FIG / "legendas.yml", encoding="utf-8"))
    LEGENDAS.update({k: str(v.get("legenda", "")) for k, v in leg.items() if isinstance(v, dict) and k in NOMES})
    arqs = leg.get("_arquivos", {})
    cache = {}
    larguras = {}
    for nome in NOMES:
        e = leg.get(nome)
        if not isinstance(e, dict):
            erro(f"legendas.yml: falta a figura {nome}")
            continue
        for campo in ("legenda", "alt", "largura"):
            if not str(e.get(campo, "")).strip():
                erro(f"legendas.yml: {nome} sem {campo}")
        if e.get("largura") not in LARGURA:
            erro(f"legendas.yml: {nome} com largura inválida {e.get('largura')!r}")
        larguras[nome] = LARGURA.get(e.get("largura"), 0)
        alt = str(e.get("alt", ""))
        if re.search(r"\d", alt):
            erro(f"legendas.yml: alt de {nome} tem número")
        for campo in ("legenda", "alt"):
            for p in PROIBIDOS:
                if re.search(p, str(e.get(campo, "")), re.I):
                    erro(f"legendas.yml: termo proibido ({p}) em {nome}.{campo}")
        for alias, caminho, casas in re.findall(r"\{([a-z_0-9]+):([^{}|]+)(?:\|(\d+))?\}", str(e.get("legenda", ""))):
            if alias not in arqs:
                erro(f"legendas.yml: {nome} usa alias desconhecido {alias}")
                continue
            a = arqs[alias]
            if a["arquivo"] not in cache:
                cache[a["arquivo"]] = ler_json(a["arquivo"])
            try:
                v = valor_json(cache[a["arquivo"]], (a["base"] + "." if a.get("base") else "") + caminho)
            except (KeyError, IndexError, ValueError, TypeError):
                erro(f"legendas.yml: {nome}: marcador {{{alias}:{caminho}}} não resolve")
                continue
            if isinstance(v, (dict, list)) or (isinstance(v, float) and not casas):
                erro(f"legendas.yml: {nome}: marcador {{{alias}:{caminho}}} dá {type(v).__name__} sem formatação")
            if isinstance(v, str) and re.search(r"\d\.\d", v) and not re.fullmatch(r"\d{1,3}(?:\.\d{3})+", v):
                erro(f"legendas.yml: {nome}: marcador {{{alias}:{caminho}}} dá número com ponto decimal: {v}")
    return larguras


def main():
    larguras = conf_legendas()
    textos = {}
    for nome in NOMES:
        for ext in ("svg", "png"):
            if not (SAIDA / f"{nome}.{ext}").exists():
                erro(f"falta saida/{nome}.{ext}")
        if (SAIDA / f"{nome}.svg").exists() and (SAIDA / f"{nome}.png").exists():
            textos[nome] = conf_svg(nome, larguras.get(nome, 0))
    conf_celulas()
    conf_direcao()
    if "prisma" in textos:
        conf_prisma(textos, LEGENDAS.get("prisma", ""))
    conf_rob()
    conf_realismo()
    conf_metas(textos.get("metas"), LEGENDAS.get("metas", ""))
    conf_dag()
    # rótulos de célula (x de y) e estudos desenhados
    if "celulas" in textos:
        for r in ler_csv(DADOS / "dados_celulas.csv"):
            if r["rotulo_xy"] not in textos["celulas"]:
                erro(f"células: '{r['rotulo_xy']}' não aparece no SVG")
    if erros:
        print(f"verificar_figuras: {len(erros)} FALHA(S)")
        for e in erros:
            print(" -", e)
        sys.exit(1)
    print("verificar_figuras: OK (7 figuras; contagens, textos dos SVG, arestas do DAG e legendas conferidos)")


if __name__ == "__main__":
    main()
