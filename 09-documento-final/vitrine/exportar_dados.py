"""Exporta os dados da vitrine para build/vitrine.json.

USO (de qualquer pasta; o script muda para a raiz do projeto):
    python3 09-documento-final/vitrine/exportar_dados.py

Só lê arquivos do projeto. Grava apenas 09-documento-final/vitrine/build/vitrine.json.
Nenhum número é digitado aqui: contagens, proporções, IC, p, g e certezas vêm dos arquivos de síntese, e a
formatação reusa as funções de 07-relatorio/gerar_tabelas_relatorio.py (num, g_fmt, p_fmt, ic_fmt, rot, dir_rot,
contagem, pais_fmt, desenho_cod, fam_cod, rebaix). O módulo lê dados/ e o master na importação; nada disso sai no
JSON, e a lista de campos permitidos (SCHEMA) barra qualquer chave que não esteja prevista.

Asserts (a exportação falha se algum quebrar):
- os enunciados das células são iguais em 06-analise/certeza.csv, revista/celulas.json e insumos/caixa_oqf.json;
- as contagens das células batem com 06-analise/swim_principal/swim_resumo.json;
- as mensagens vêm do AST do artigo (ou do v1, marcadas como provisórias) e o texto de cada uma está no documento;
- as pendências vêm só de 07-relatorio/_pendencias_abertas.json;
- a raia de cada evento do processo sai do ator.id e de 00-protocolo/correcao_atribuicao.csv (seq 793 = IA);
- o fluxo PRISMA fecha em cada ramo, e 41 = 27 + 3 + 7 + 4.
"""
import ast
import collections
import csv
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

VITRINE = Path(__file__).resolve().parent
RAIZ = VITRINE.parents[1]
DOCFINAL = RAIZ / "09-documento-final"
SAIDA = VITRINE / "build" / "vitrine.json"

BIBS = ["07-relatorio/references.bib", "09-documento-final/referencias_contexto.bib",
        "09-documento-final/referencias_metodo.bib"]
CSL = "09-documento-final/revista/american-political-science-association.csl"
TERMOS_EN = {"bandwagon", "underdog", "momentum", "survey", "surveys", "online", "post hoc", "leave-one-out",
             "rolling cross-section", "forest plot", "abstract", "working paper"}


# ------------------------------------------------------------------ utilidades
def falha(msg):
    sys.exit(f"exportar_dados.py: ERRO: {msg}")


def confere(cond, msg):
    if not cond:
        falha(msg)


def ler_csv(rel):
    with open(RAIZ / rel, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def ler_json(rel):
    with open(RAIZ / rel, encoding="utf-8") as f:
        return json.load(f)


def sha(rel):
    return hashlib.sha256((RAIZ / rel).read_bytes()).hexdigest()


def md_en(s):
    """'*bandwagon*' -> '<i lang="en">bandwagon</i>' (as saídas de dir_rot/contagem usam asterisco só em termo inglês)."""
    return re.sub(r"\*([^*]+)\*", r'<i lang="en">\1</i>', s)


def sem_md(s):
    return re.sub(r"\*([^*]+)\*", r"\1", s)


def carregar_gt():
    os.chdir(RAIZ)  # o módulo usa R = '.'
    spec = importlib.util.spec_from_file_location("gt", RAIZ / "07-relatorio/gerar_tabelas_relatorio.py")
    gt = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gt)
    return gt


# ------------------------------------------------------------------ rótulos públicos (nomes de categorias, não números)
BLOCOS = [
    ("apoio_principal", "Apoio a quem aparece à frente", "sec-apoio"),
    ("viabilidade", "Viabilidade e voto estratégico", "sec-viabilidade"),
    ("momentum", '<i lang="en">Momentum</i>', "sec-momentum"),
    ("mobilizacao", "Comparecimento", "sec-comparecimento"),
]
CLASSES = [("randomizado", "Randomizado"), ("nao_randomizado", "Não randomizado")]
COMPARADOR = {"sem_pesquisa": "sem pesquisa", "mesmo_candidato_atras": "o mesmo candidato atrás",
              "outro_resultado": "outro resultado de pesquisa", "outro": "outro comparador",
              "antes_depois_proibicao": "antes e depois da proibição",
              "unidades_nao_expostas": "unidades não expostas"}
FAMILIA = {"pesquisa_pre_eleitoral": "pesquisa pré-eleitoral", "agregador_projecao": "agregador ou projeção",
           "boca_de_urna": "boca de urna", "outro": "apuração parcial oficial",
           "apuracao_parcial": "apuração parcial oficial"}
NIVEL = {"muito_baixa": 1, "baixa": 2, "moderada": 3, "alta": 4}
CERTEZA_TXT = {"muito_baixa": "muito baixa", "baixa": "baixa", "moderada": "moderada", "alta": "alta"}
GLIFO = {"benefico": "pos", "danoso": "neg", "misto": "misto", "nulo": "nulo", "sem_direcao": "sem"}
ROB_SIMBOLO = {"baixo": "+", "algumas_preocupacoes": "−", "moderado": "−", "alto": "×", "grave": "×",
               "critico": "!", "incerto": "?"}
ROB_NIVEL = {"baixo": 1, "algumas_preocupacoes": 2, "moderado": 2, "incerto": 2, "alto": 3, "grave": 3, "critico": 4}
FERR = {"rob2": "RoB 2", "robins_i": "ROBINS-I", "epoc": "EPOC"}
REALISMO = {"real": "real", "induzido": "preferências induzidas", "hipotetico": "hipotético"}
REGIAO = {"outro": "outras regiões", "america_latina": "América Latina", "brasil": "Brasil", "999": "não relatada"}
DESENHO_COD = {"lab_preferencias_induzidas": "laboratório, preferências induzidas",
               "lab_candidatos_reais": "laboratório, candidatos reais", "survey_experiment": "experimento de survey",
               "experimento_natural": "experimento natural", "experimento_campo": "experimento de campo",
               "painel_individual": "painel individual", "outro": "outro desenho"}
MOTIVO_EXCL = {"c1_populacao_contexto": "população ou contexto", "c2_intervencao_estudada": "exposição estudada",
               "c3_desfecho": "desfecho", "c4_desenho_elegivel": "desenho"}
PORTAO = {"G1": "pergunta", "G2": "protocolo", "G3": "busca", "G4": "triagem de títulos e resumos",
          "G5": "elegibilidade no texto completo", "G6": "piloto de extração", "G7": "extração e risco de viés",
          "G8": "síntese e certeza", "G9": "relato"}
ETAPAS_PEND = [("04_busca", "Busca"), ("05_organizacao", "Deduplicação"), ("06_triagem_ta", "Triagem"),
               ("07_textos_elegibilidade", "Texto completo"), ("08_piloto_extracao", "Piloto de extração"),
               ("09_extracao_rob", "Extração e risco de viés"), ("10_sintese", "Síntese e certeza"),
               ("11_relato", "Relato")]
# motivo público de cada efeito fora da contagem, por padrão do texto do dicionário FORA (o texto não é publicado)
MOTIVO_FORA = [
    (r"conferência humana pendente|^idem \(E02 passou", "efeito principal aguarda conferência humana"),
    (r"interação|moderador", "estima uma interação com moderador, e não o contraste da exposição"),
    (r"contraste de formato", "compara dois formatos da mesma previsão, e não exposição e não exposição"),
    (r"alvos opostos agregados|alvos agregados", "junta alvos opostos numa só medida"),
    (r"não é apoio ao líder nem contraste", "não mede apoio ao líder nem o contraste da exposição"),
]


def unidade(ch, gt):
    u = gt.M[ch]["unidade_analise"].strip().lower()
    if u.startswith("individuo"):
        return "pessoas"
    if u.startswith("distrito_eleitoral"):
        return "distritos"
    if u.startswith("secao_eleitoral"):
        return "seções eleitorais"
    if u.startswith("pais"):
        return "países"
    if "departamento" in u:
        return "departamentos"
    return "unidades do estudo"


# ------------------------------------------------------------------ extração de texto do artigo (AST)
def pandoc_json(rel):
    r = subprocess.run(["quarto", "pandoc", "-f", "markdown", "-t", "json", str(RAIZ / rel)],
                       capture_output=True, text=True, cwd=RAIZ)
    confere(r.returncode == 0, f"quarto pandoc falhou em {rel}: {r.stderr[:400]}")
    return json.loads(r.stdout)


def blocos_para_html(doc, blocos):
    frag = {"pandoc-api-version": doc["pandoc-api-version"], "meta": {}, "blocks": blocos}
    cmd = ["quarto", "pandoc", "-f", "json", "-t", "html", "--citeproc", "--csl", str(RAIZ / CSL),
           "-M", "lang=pt-BR", "-M", "suppress-bibliography=true", "--wrap=none"]
    for b in BIBS:
        if (RAIZ / b).exists():
            cmd += ["--bibliography", str(RAIZ / b)]
    r = subprocess.run(cmd, input=json.dumps(frag), capture_output=True, text=True, cwd=RAIZ)
    confere(r.returncode == 0, f"pandoc (json -> html) falhou: {r.stderr[:400]}")
    confere("???" not in r.stdout, f"citação não resolvida no trecho extraído: {r.stdout[:300]}")
    html = r.stdout.strip()
    for t in sorted(TERMOS_EN, key=len, reverse=True):
        html = re.sub(rf"<em>({re.escape(t)})</em>", r'<i lang="en">\1</i>', html, flags=re.I)
    return html


def texto_plano(blocos, doc):
    frag = {"pandoc-api-version": doc["pandoc-api-version"], "meta": {}, "blocks": blocos}
    r = subprocess.run(["quarto", "pandoc", "-f", "json", "-t", "plain", "--wrap=none"], input=json.dumps(frag),
                       capture_output=True, text=True)
    return re.sub(r"\s+", " ", r.stdout).strip()


def achar_div(blocos, classe):
    for b in blocos:
        if b["t"] == "Div":
            if classe in b["c"][0][1]:
                return b
            achado = achar_div(b["c"][1], classe)
            if achado:
                return achado
    return None


def secao_por_id(blocos, ident):
    """Blocos entre o cabeçalho com id `ident` e o próximo cabeçalho de mesmo nível ou acima, ou a próxima Div."""
    saida, dentro, nivel = [], False, None
    for b in blocos:
        if b["t"] == "Header":
            if dentro and b["c"][0] <= nivel:
                break
            if b["c"][1][0] == ident:
                dentro, nivel = True, b["c"][0]
                continue
        if dentro:
            if b["t"] == "Div":
                break
            saida.append(b)
    return saida


def extrair_mensagens():
    artigo = "09-documento-final/revisao_final.qmd"
    doc = pandoc_json(artigo) if (RAIZ / artigo).exists() else None
    div = achar_div(doc["blocks"], "mensagens-principais") if doc else None
    if div and not any(b["t"] == "BulletList" for b in div["c"][1]):
        div = None  # bloco ainda vazio no artigo novo (marcador da etapa 4): usa o v1, marcado como provisório
    if div:
        blocos, fonte, provisorio = div["c"][1], artigo, False
        blocos = [b for b in blocos if b["t"] != "Header"]
    else:
        fonte = "09-documento-final/_revisao_final_v1_oqf.qmd"
        doc = pandoc_json(fonte)
        blocos, provisorio = secao_por_id(doc["blocks"], "mensagens-principais"), True
    listas = [b for b in blocos if b["t"] == "BulletList"]
    confere(len(listas) == 1, f"mensagens: esperava uma lista em {fonte}, achei {len(listas)}")
    itens = []
    plano_doc = texto_plano(doc["blocks"], doc)
    for item in listas[0]["c"]:
        html = blocos_para_html(doc, item)
        m = re.match(r"^(?:<p>)?\s*<strong>(.*?)</strong>\s*(.*?)(?:</p>)?$", html, flags=re.S)
        confere(m, f"mensagem sem título em negrito: {html[:120]}")
        titulo = m.group(1).strip().rstrip(".")
        plano = texto_plano(item, doc)
        confere(plano[:60] in plano_doc, "mensagem extraída não está no texto do documento")
        itens.append({"titulo": titulo, "html": m.group(2).strip()})
    return {"provisorio": provisorio, "fonte": fonte, "itens": itens}


def extrair_linguagem_simples():
    rel = "09-documento-final/linguagem_simples.qmd"
    if (RAIZ / rel).exists():
        doc = pandoc_json(rel)
        blocos = [b for b in doc["blocks"] if b["t"] in ("Para", "BulletList", "OrderedList", "Header")]
        return {"provisorio": False, "fonte": rel, "html": blocos_para_html(doc, blocos)}
    fonte = "09-documento-final/_revisao_final_v1_oqf.qmd"
    doc = pandoc_json(fonte)
    blocos = [b for b in secao_por_id(doc["blocks"], "resumo-executivo") if b["t"] == "Para"]
    confere(blocos, "resumo executivo do v1 não encontrado")
    return {"provisorio": True, "fonte": fonte, "html": blocos_para_html(doc, blocos)}


# ------------------------------------------------------------------ rótulos autor-ano (citeproc, mesmo CSL do artigo)
def rotulos_autor_ano(chaves):
    pronto = DOCFINAL / "revista/figuras/rotulos_autor_ano.json"
    if pronto.exists():
        d = json.load(open(pronto, encoding="utf-8"))
        if all(c in d for c in chaves):
            return {c: d[c] for c in chaves}
    md = "---\nlang: pt-BR\nsuppress-bibliography: true\n---\n\n" + "\n\n".join(f"ROT:{c}: @{c}" for c in chaves)
    r = subprocess.run(["quarto", "pandoc", "-f", "markdown", "-t", "plain", "--wrap=none", "--citeproc",
                        "--csl", str(RAIZ / CSL), "--bibliography", str(RAIZ / BIBS[0])],
                       input=md, capture_output=True, text=True, cwd=RAIZ)
    confere(r.returncode == 0, f"citeproc falhou: {r.stderr[:300]}")
    out = {}
    for linha in r.stdout.splitlines():
        m = re.match(r"^ROT:(\S+): (.+)$", linha.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    faltam = [c for c in chaves if c not in out or "???" in out[c]]
    confere(not faltam, f"rótulo autor-ano não gerado para {faltam}")
    return out


# ------------------------------------------------------------------ exportação
def main():
    gt = carregar_gt()
    num, inteiro, p_fmt, ic_fmt, g_fmt = gt.num, gt.inteiro, gt.p_fmt, gt.ic_fmt, gt.g_fmt

    celjs = ler_json("09-documento-final/revista/celulas.json")
    nv2 = ler_json("09-documento-final/revista/numeros_v2.json")
    ntab = ler_json("09-documento-final/insumos/tabelas/numeros.json")
    prisma = ler_json("07-relatorio/prisma_contagens.json")
    pend = ler_json("07-relatorio/_pendencias_abertas.json")
    caixa = ler_json("09-documento-final/insumos/caixa_oqf.json")
    swim_p = ler_json("06-analise/swim_principal/swim_resumo.json")
    cert = ler_csv("06-analise/certeza.csv")
    cert_amp = ler_csv("06-analise/certeza_agrupamento_amplo.csv")
    dirp = ler_csv("06-analise/swim_principal/tabelas/swim_direcao.csv")
    dir_exc = ler_csv("06-analise/swim_sens_com_excluidos_amplo/tabelas/swim_direcao.csv")
    incl = ler_csv("07-relatorio/incluidos.csv")

    CH = ("familia_intervencao", "construto_outcome", "comparador_tipo", "celula_alvo", "classe_desenho")
    chave5 = lambda r: tuple(r[c] for c in CH)

    # ---------- asserts de consistência das células
    cert_k = {chave5(r): r for r in cert}
    swim_k = {chave5(g): g for g in swim_p["grupos"]}
    caixa_k = {(c["familia"], c["construto"], c["comparador"], c["celula_alvo"], c["desenho"]): c
               for c in caixa["celulas"]}
    confere(len(celjs["celulas"]) == len(cert) == 18, "número de células diferente de 18 entre celulas.json e certeza.csv")
    for c in celjs["celulas"]:
        k = chave5(c)
        confere(k in cert_k and k in swim_k and k in caixa_k, f"célula {c['id']} sem par nas fontes")
        confere(c["enunciado"] == cert_k[k]["enunciado"] == caixa_k[k]["enunciado"],
                f"enunciado de {c['id']} difere entre certeza.csv, celulas.json e caixa_oqf.json")
        g = swim_k[k]
        for a, b in (("k", "k_estudos"), ("n_beneficos", "n_beneficos"), ("n_danosos", "n_danosos"),
                     ("n_mistos", "n_mistos"), ("n_nulos", "n_nulos"), ("p_sinal", "p_sinal")):
            confere(c[a] == g[b], f"{c['id']}: {a} = {c[a]} difere de swim_resumo.json ({g[b]})")
        confere(c["certeza"] == cert_k[k]["certeza"] == caixa_k[k]["certeza"], f"certeza de {c['id']} diverge")
        confere(set(c["estudos"]) == set(g["estudos"]), f"estudos de {c['id']} divergem da SWiM")

    # ---------- rótulos e estudos
    chaves = sorted(gt.M, key=str.lower)
    rot_aa = rotulos_autor_ano(chaves)
    ano = {r["chave"]: r["ano"] for r in incl}
    sintese = set(nv2["estudos_fora_da_sintese_principal"]["chaves"])
    criticos = set(nv2["estudos_risco_critico"]["chaves"])
    so_fora = set(nv2["estudos_so_fora_da_contagem"]["chaves"])
    sem_princ = set(nv2["estudos_sem_efeito_principal"]["chaves"])
    em_sintese = set(ntab["swim_principal_estudos"])
    confere(len(gt.M) == ntab["estudos"] == prisma["incluidos"]["estudos"], "número de estudos diverge")
    confere(len(em_sintese) + len(criticos) + len(so_fora) + len(sem_princ) == len(gt.M),
            "41 ≠ síntese + críticos + só fora + sem principal")
    confere(sintese == criticos | so_fora | sem_princ, "estudos fora da síntese divergem de numeros_v2.json")

    fonte_fora = open(RAIZ / "06-analise/montar_entradas_swim.py", encoding="utf-8").read()
    FORA = ast.literal_eval(re.search(r"^FORA = (\{.*?^\})", fonte_fora, re.S | re.M).group(1))
    motivo_fora_est = collections.defaultdict(list)
    ultimo = None
    for idef, txt in FORA.items():
        alvo = None
        for padrao, publico in MOTIVO_FORA:
            if re.search(padrao, txt):
                alvo = publico
                break
        if txt.startswith("idem") and alvo is None:
            alvo = ultimo
        confere(alvo, f"efeito fora da contagem sem motivo público mapeado: {idef}")
        ultimo = alvo
        ch = idef.rsplit("-", 1)[0]
        if alvo not in motivo_fora_est[ch]:
            motivo_fora_est[ch].append(alvo)

    rob_por = collections.defaultdict(list)
    for r in gt.rob:
        rob_por[r["chave"]].append({"construto": r["construto_outcome"], "ferramenta": FERR[r["ferramenta"]],
                                    "geral": r["rob_geral"], "geral_rot": gt.rot(r["rob_geral"]),
                                    "simbolo": ROB_SIMBOLO[r["rob_geral"]], "nivel": ROB_NIVEL[r["rob_geral"]]})

    estudos = {}
    for ch in chaves:
        regs = [x.strip() for x in gt.M[ch]["regiao"].split("+")]
        if ch in em_sintese:
            situ, motivo = "sintese", None
        elif ch in criticos:
            situ, motivo = "critico", "risco de viés crítico: fica fora da análise principal"
        elif ch in so_fora:
            situ, motivo = "fora", "; ".join(motivo_fora_est.get(ch, [])) or None
            confere(motivo, f"estudo só fora da contagem sem motivo: {ch}")
        else:
            situ = "sem_principal"
            motivo = ("nenhum efeito extraído" if ch not in gt.efe_chaves
                      else "nenhum efeito marcado como principal")
        dc = gt.desenho_cod(ch)
        estudos[ch] = {
            "rotulo": rot_aa[ch], "ano": ano.get(ch, "NR"), "pais": gt.pais_fmt(ch), "regioes": regs,
            "regiao_rot": ", ".join(REGIAO.get(x, x) for x in regs),
            "desenho": md_en(gt.desenho_fmt(ch)).replace("experimento de survey", 'experimento de <i lang="en">survey</i>'),
            "desenho_cod": dc, "familia": gt.fam_cod(ch), "familia_rot": FAMILIA[gt.fam_cod(ch)],
            "realismo": gt.M[ch]["realismo_contexto"], "realismo_rot": REALISMO.get(gt.M[ch]["realismo_contexto"], "NR"),
            "unidade": unidade(ch, gt), "rob": rob_por.get(ch, []), "situacao": situ, "motivo": motivo,
        }

    # ---------- células
    nam = {(r["chave"], r["grupo"]): r for r in dirp}
    celulas, por_bloco = [], collections.defaultdict(lambda: collections.defaultdict(list))
    for c in celjs["celulas"]:
        k = chave5(c)
        g = swim_k[k]
        construto, alvo = c["construto_outcome"], c["celula_alvo"]
        pos = gt.dir_rot("benefico", construto, alvo)
        neg = gt.dir_rot("danoso", construto, alvo)
        linhas = []
        for ch in c["estudos"]:
            d = nam.get((ch, g["grupo"]))
            confere(d, f"{c['id']}: {ch} sem linha em swim_direcao.csv")
            rob_e = [x for x in estudos[ch]["rob"] if x["construto"] == construto]
            confere(len(rob_e) == 1, f"{c['id']}: risco de viés de {ch} em {construto} não é único")
            n_am = d["n_amostra"]
            linhas.append({
                "chave": ch, "direcao": d["direcao"], "glifo": GLIFO[d["direcao"]],
                "direcao_rot": md_en(gt.dir_rot(d["direcao"], construto, alvo)),
                "n_efeitos": int(d["n_efeitos"]), "n_pos": int(d["n_beneficos"]), "n_neg": int(d["n_danosos"]),
                "n_amostra": int(n_am) if n_am else None, "n_fmt": inteiro(n_am) if n_am else "NR",
                "rob": rob_e[0],
            })
        ordem_dir = {"benefico": 0, "misto": 1, "nulo": 2, "danoso": 3, "sem_direcao": 4}
        linhas.sort(key=lambda x: (ordem_dir[x["direcao"]], x["chave"].lower()))
        reb = gt.rebaix(cert_k[k]["justificativa"])
        m = re.match(r"^(.*) \(partida (\w+)\)$", reb)
        confere(m, f"rebaixamentos em formato inesperado: {reb}")
        rebs = [] if m.group(1) == "nenhum" else [x.strip() for x in m.group(1).split(";")]
        n_dir = c["n_estudos_com_direcao"]
        cel = {
            "id": c["id"], "bloco": c["bloco"], "familia": c["familia_intervencao"],
            "familia_rot": FAMILIA[c["familia_intervencao"]], "construto": construto,
            "comparador": c["comparador_tipo"], "comparador_rot": COMPARADOR[c["comparador_tipo"]],
            "alvo": alvo, "classe": c["classe_desenho"], "classe_rot": dict(CLASSES)[c["classe_desenho"]],
            "enunciado": c["enunciado"], "certeza": c["certeza"], "certeza_rot": CERTEZA_TXT[c["certeza"]],
            "nivel": NIVEL[c["certeza"]], "k": c["k"], "n_dir": n_dir, "n_pos": c["n_beneficos"],
            "n_neg": c["n_danosos"], "n_mistos": c["n_mistos"], "n_nulos": c["n_nulos"],
            "pos_rot": md_en(pos), "neg_rot": md_en(neg),
            "contagem": md_en(gt.contagem(g, construto, alvo)),
            "x_de_y": (f"{c['n_beneficos']} de {n_dir}" if n_dir else None),
            "proporcao": c["proporcao"], "proporcao_fmt": num(c["proporcao"]) if c["proporcao"] is not None else None,
            "ic": c["ic_proporcao"], "ic_fmt": ic_fmt(c["ic_proporcao"]) if c["ic_proporcao"] else None,
            "p": c["p_sinal"], "p_fmt": p_fmt(c["p_sinal"]) if c["p_sinal"] is not None else None,
            "delta_fmt": num(c["delta"], 4 if c["delta"] and round(c["delta"], 3) != c["delta"] else 3),
            "estudos": linhas, "excluidos_critico": c["excluidos_rob_critico"],
            "rebaixamentos": rebs, "partida": m.group(2), "caixa": caixa_k[k]["rotulo_caixa"],
            "secao": dict((b, s) for b, _, s in BLOCOS)[c["bloco"]],
        }
        celulas.append(cel)
        por_bloco[c["bloco"]][c["classe_desenho"]].append(c["id"])
    vazias = [{"familia": v["familia_intervencao"], "familia_rot": FAMILIA[v["familia_intervencao"]],
               "construto": v["construto_outcome"], "comparador": v["comparador_tipo"],
               "comparador_rot": COMPARADOR[v["comparador_tipo"]], "alvo": v["celula_alvo"],
               "classe": v["classe_desenho"], "excluidos_critico": v["excluidos_rob_critico"],
               "bloco": "mobilizacao" if v["construto_outcome"] == "mobilizacao" else
               {"principal": "apoio_principal"}.get(v["celula_alvo"], v["celula_alvo"])} for v in celjs["vazias"]]
    caixa_rotulos = collections.Counter(c["caixa"] for c in celulas)
    blocos = [{"id": b, "rotulo": r, "secao": s,
               "classes": [{"classe": cl, "rotulo": cr, "celulas": por_bloco[b][cl],
                            "vazias": [i for i, v in enumerate(vazias) if v["bloco"] == b and v["classe"] == cl]}
                           for cl, cr in CLASSES]} for b, r, s in BLOCOS]

    # ---------- estudos fora da síntese (estudo a estudo, em cinza)
    fora_linhas = []
    for r in dir_exc:
        ch = r["chave"]
        if estudos[ch]["situacao"] not in ("critico", "fora"):
            continue
        construto, alvo, classe = [x.strip() for x in r["grupo"].split("|")]
        fora_linhas.append({
            "chave": ch, "construto": construto, "alvo": alvo, "classe": classe,
            "grupo_rot": ("comparecimento" if construto == "mobilizacao" else
                          "apoio, " + {"principal": "célula principal", "viabilidade": "viabilidade",
                                       "momentum": "momentum", "outro": "outro alvo"}[alvo])
                         + " · " + dict(CLASSES)[classe].lower(),
            "direcao": r["direcao"], "glifo": GLIFO[r["direcao"]],
            "direcao_rot": md_en(gt.dir_rot(r["direcao"], construto, alvo)) if alvo != "outro" else
            {"benefico": "positivo", "danoso": "negativo"}.get(r["direcao"], r["direcao"]),
            "n_efeitos": int(r["n_efeitos"]), "n_pos": int(r["n_beneficos"]), "n_neg": int(r["n_danosos"]),
            "n_fmt": inteiro(r["n_amostra"]) if r["n_amostra"] else "NR",
        })
    for ch in sorted(sem_princ | (criticos | so_fora) - {x["chave"] for x in fora_linhas}, key=str.lower):
        fora_linhas.append({"chave": ch, "construto": None, "alvo": None, "classe": None, "grupo_rot": None,
                            "direcao": "sem_direcao", "glifo": "sem", "direcao_rot": "nenhum efeito principal",
                            "n_efeitos": 0, "n_pos": 0, "n_neg": 0, "n_fmt": "NR"})
    confere({x["chave"] for x in fora_linhas} == sintese, "linhas fora da síntese não cobrem os 14 estudos")

    # ---------- PRISMA
    def ramo(nome, rotulo, b):
        confere(sum(b["identificados"][x] for x in b["identificados"] if x != "por_fonte")
                - b["removidos_antes_triagem"]["duplicatas"] - b["removidos_antes_triagem"]["automacao"]
                - b["removidos_antes_triagem"]["outros_motivos"] == b["a_triar"], f"PRISMA {nome}: identificação não fecha")
        confere(b["triados"] - b["excluidos_triagem"] == b["buscados"], f"PRISMA {nome}: triagem não fecha")
        confere(b["buscados"] - b["nao_recuperados"] == b["avaliados"], f"PRISMA {nome}: recuperação não fecha")
        confere(b["avaliados"] - b["excluidos_elegibilidade"]["total"] - b["aguardando_classificacao"]
                == b["incluidos_relatos"], f"PRISMA {nome}: elegibilidade não fecha")
        ident = sum(v for kk, v in b["identificados"].items() if kk != "por_fonte")
        return {
            "id": nome, "rotulo": rotulo, "identificados": ident, "identificados_fmt": inteiro(ident),
            "por_fonte": [{"fonte": {"openalex": "OpenAlex", "bdtd": "BDTD"}.get(f, f), "n": v, "n_fmt": inteiro(v)}
                          for f, v in b["identificados"].get("por_fonte", {}).items()],
            "duplicatas": b["removidos_antes_triagem"]["duplicatas"],
            "automacao": b["removidos_antes_triagem"]["automacao"],
            "triados": b["triados"], "excluidos_triagem": b["excluidos_triagem"], "buscados": b["buscados"],
            "nao_recuperados": b["nao_recuperados"], "avaliados": b["avaliados"],
            "excluidos_elegibilidade": b["excluidos_elegibilidade"]["total"],
            "motivos": [{"motivo": MOTIVO_EXCL[m_], "n": v} for m_, v in
                        sorted(b["excluidos_elegibilidade"]["motivos"].items(), key=lambda x: -x[1])],
            "incluidos": b["incluidos_relatos"],
        }
    ramos = [ramo("bases", "Bases (OpenAlex e BDTD)", prisma["bases"]),
             ramo("citacoes", "Busca por citações", {**prisma["outros_metodos"],
                                                     "identificados": {"busca_citacoes": prisma["outros_metodos"]["identificados"]["busca_citacoes"]}})]
    confere(prisma["outros_metodos"]["identificados"]["sites_organizacoes"] == 0
            and prisma["outros_metodos"]["identificados"]["outros"] == 0, "PRISMA: outros métodos com fontes não previstas")
    confere(sum(r["incluidos"] for r in ramos) == prisma["incluidos"]["relatos"], "PRISMA: relatos não somam")
    fluxo_estudos = {
        "estudos": ntab["estudos"], "com_efeitos": ntab["estudos_com_efeitos"],
        "com_principal": ntab["estudos_com_principal"], "sintese": ntab["n_swim_principal_estudos"],
        "sem_efeitos": sorted(set(gt.M) - gt.efe_chaves), "sem_principal": sorted(sem_princ),
        "criticos": sorted(criticos), "so_fora": sorted(so_fora),
    }
    confere(fluxo_estudos["estudos"] - len(fluxo_estudos["sem_efeitos"]) == fluxo_estudos["com_efeitos"],
            "fluxo: estudos com efeitos não fecha")
    confere(fluxo_estudos["estudos"] - len(sem_princ) == fluxo_estudos["com_principal"], "fluxo: principal não fecha")
    confere(fluxo_estudos["com_principal"] - len(criticos) - len(so_fora) == fluxo_estudos["sintese"],
            "fluxo: síntese não fecha")

    # ---------- sensibilidades (contando a direção)
    CERT_AMP = {(r["construto_outcome"], r["celula_alvo"], r["classe_desenho"]): r for r in cert_amp}
    ORDEM_ALVO = {"principal": 0, "viabilidade": 1, "momentum": 2, "outro": 3, "mobilizacao": 4}

    def grupo_amplo(g, com_grade):
        construto, alvo, classe = g["construto_outcome"], g["celula_alvo"], g["classe_desenho"]
        c = CERT_AMP.get((construto, alvo, classe)) if com_grade else None
        bloco = "mobilizacao" if construto == "mobilizacao" else {"principal": "apoio_principal"}.get(alvo, alvo)
        pos = gt.dir_rot("benefico", construto, alvo) if alvo != "outro" else "positivo"
        return {"rotulo": (("Comparecimento" if construto == "mobilizacao" else
                            {"principal": "Apoio a quem está à frente", "viabilidade": "Viabilidade",
                             "momentum": '<i lang="en">Momentum</i>', "outro": "Apoio, outro alvo"}[alvo])),
                "classe_rot": dict(CLASSES)[classe], "bloco": bloco, "pos_rot": md_en(pos),
                "k": g["k_estudos"], "n_dir": g["n_estudos"], "n_pos": g["n_beneficos"], "n_neg": g["n_danosos"],
                "n_mistos": g["n_mistos"], "n_nulos": g["n_nulos"],
                "proporcao": g["proporcao_benefica"], "ic": g["ic_proporcao"],
                "ic_fmt": ic_fmt(g["ic_proporcao"]) if g["ic_proporcao"] else None,
                "p_fmt": p_fmt(g["p_sinal"]) if g["p_sinal"] is not None else None,
                "certeza": c["certeza"] if c else None, "nivel": NIVEL[c["certeza"]] if c else None,
                "certeza_rot": CERTEZA_TXT[c["certeza"]] if c else None,
                "estudos": [rot_aa[e] for e in g["estudos"]],
                "ordem": [ORDEM_ALVO[alvo if construto != "mobilizacao" else "mobilizacao"], classe != "randomizado"]}

    analises = []
    prot = []
    for c in celulas:
        prot.append({"rotulo": FAMILIA[c["familia"]].capitalize() + " · " + c["comparador_rot"],
                     "classe_rot": c["classe_rot"], "bloco": c["bloco"], "pos_rot": c["pos_rot"], "k": c["k"],
                     "n_dir": c["n_dir"], "n_pos": c["n_pos"], "n_neg": c["n_neg"], "n_mistos": c["n_mistos"],
                     "n_nulos": c["n_nulos"], "proporcao": c["proporcao"], "ic": c["ic"], "ic_fmt": c["ic_fmt"],
                     "p_fmt": c["p_fmt"], "certeza": c["certeza"], "nivel": c["nivel"], "certeza_rot": c["certeza_rot"],
                     "estudos": [rot_aa[e["chave"]] for e in c["estudos"]], "ordem": [0, 0]})
    for v in vazias:
        prot.append({"rotulo": v["familia_rot"].capitalize() + " · " + v["comparador_rot"],
                     "classe_rot": dict(CLASSES)[v["classe"]], "bloco": v["bloco"], "pos_rot": "", "k": 0,
                     "n_dir": 0, "n_pos": 0, "n_neg": 0, "n_mistos": 0, "n_nulos": 0, "proporcao": None, "ic": None,
                     "ic_fmt": None, "p_fmt": None, "certeza": None, "nivel": None, "certeza_rot": None,
                     "estudos": [], "ordem": [0, 1]})
    analises.append({"id": "protocolo", "rotulo": "Células do protocolo", "post_hoc": False, "grade": True,
                     "grupos": prot})
    SENS = [("amplo", "swim_sens_agrupamento_amplo", "Agrupamento amplo", True, True),
            ("real", "swim_sens_so_contexto_real_amplo", "Só contexto real", True, False),
            ("pre2010", "swim_sens_sem_pre2010_amplo", "Sem dados anteriores a 2010", True, False),
            ("araujo", "swim_sens_sem_araujo_amplo", f"Sem {rot_aa['Araujo2021a']}", True, False),
            ("excluidos", "swim_sens_com_excluidos_amplo", "Com os efeitos fora da contagem", True, False)]
    for ident, pasta, rotulo, post_hoc, grade in SENS:
        s = ler_json(f"06-analise/{pasta}/swim_resumo.json")
        gs = [grupo_amplo(g, grade) for g in s["grupos"] if g["k_estudos"] > 0]
        gs.sort(key=lambda x: x["ordem"])
        analises.append({"id": ident, "rotulo": rotulo, "post_hoc": post_hoc, "grade": grade, "grupos": gs})
    real = next(a for a in analises if a["id"] == "real")
    amplo = next(a for a in analises if a["id"] == "amplo")
    g_real = next(g for g in real["grupos"] if g["bloco"] == "apoio_principal" and g["classe_rot"] == "Randomizado")
    g_amplo = next(g for g in amplo["grupos"] if g["bloco"] == "apoio_principal" and g["classe_rot"] == "Randomizado")

    # ---------- metas exploratórias
    ent = {r["id_efeito"]: r for r in ler_csv("06-analise/efeitos.csv")}
    es_para_chave = {r["id_estudo"]: r["chave"] for r in ent.values()}
    metas = []
    for ident, pasta, entrada, titulo in (
            ("a", "meta_exploratoria", "meta_entrada_exploratoria.csv", "Mostrar uma pesquisa, frente a não mostrar"),
            ("b", "meta_mesmo_candidato", "meta_entrada_mesmo_candidato.csv", "O mesmo candidato à frente, frente a atrás")):
        mr = ler_json(f"06-analise/{pasta}/meta_resumo.json")
        confere(len(mr["grupos"]) == 1, f"{pasta}: esperava um grupo")
        gm = mr["grupos"][0]
        r = gm["resultado"]
        linhas = ler_csv(f"06-analise/{entrada}")
        confere(len(linhas) == gm["k_efeitos"], f"{pasta}: k de efeitos diverge da entrada")
        efs = []
        for l in linhas:
            yi, sei = float(l["yi"]), float(l["sei"])
            efs.append({"chave": l["chave"], "rotulo": rot_aa[l["chave"]], "efeito": l["id_efeito"].rsplit("-", 1)[1],
                        "yi": yi, "lo": yi - 1.959964 * sei, "hi": yi + 1.959964 * sei,
                        "g_fmt": g_fmt(yi), "ep_fmt": num(sei, 3)})
        efs.sort(key=lambda e: (e["rotulo"], e["efeito"]))
        loo = ler_csv(gm["sensibilidade"]["leave_one_out"]["tabela"])
        metas.append({
            "id": ident, "titulo": titulo, "k_estudos": gm["k_estudos"], "k_efeitos": gm["k_efeitos"],
            "g": r["estimativa"], "g_fmt": g_fmt(r["estimativa"]), "ic": r["ic"], "ic_fmt": " a ".join(g_fmt(x) for x in r["ic"]),
            "pi": r["pi"], "pi_fmt": " a ".join(g_fmt(x) for x in r["pi"]), "p_fmt": p_fmt(r["p"]),
            "gl_fmt": num(r["gl"]), "gl": r["gl"], "tau2_fmt": num(r["tau2"]), "i2_fmt": num(r["I2"], 0),
            "rve_confiavel": r["rve_confiavel"], "delta": mr["parametros"]["delta"],
            "delta_fmt": num(mr["parametros"]["delta"], 4 if round(mr["parametros"]["delta"], 3) != mr["parametros"]["delta"] else 3),
            "efeitos": efs,
            "loo": [{"sem": rot_aa[es_para_chave[x["estudo_removido"]]], "g_fmt": g_fmt(x["estimativa"]),
                     "ic_fmt": f"{g_fmt(x['ic_inf'])} a {g_fmt(x['ic_sup'])}",
                     "muda": x["estudo_removido"] in gm["sensibilidade"]["leave_one_out"]["estudos_que_mudam_conclusao"]}
                    for x in loo],
        })
        confere(r["gl"] < 4 and not r["rve_confiavel"], f"{pasta}: o carimbo 'menos de 4 gl' não vale mais")

    # ---------- risco de viés por domínio
    DOMS = {
        "rob2": [("D1", "Randomização"), ("D1b", "Recrutamento (conglomerado)"), ("D2", "Desvios da intervenção"),
                 ("D3", "Dados faltantes"), ("D4", "Mensuração do desfecho"), ("D5", "Relato seletivo")],
        "robins_i": [("D1", "Confundimento"), ("D2", "Classificação da exposição"), ("D3", "Seleção"),
                     ("D4", "Dados faltantes"), ("D5", "Mensuração do desfecho"), ("D6", "Relato seletivo")],
        "epoc": [("cg_sequencia_aleatoria", "Sequência aleatória*"), ("cg_ocultacao_alocacao", "Ocultação da alocação*"),
                 ("cg_caracteristicas_base", "Características de base"), ("cg_linha_base_outcome", "Desfecho na linha de base"),
                 ("cg_dados_incompletos", "Dados incompletos"), ("cg_conhecimento_alocacao", "Conhecimento da alocação"),
                 ("cg_contaminacao", "Contaminação"), ("cg_relato_seletivo", "Relato seletivo"),
                 ("cg_outros_riscos", "Outros riscos"), ("its_intervencao_independente", "ITS: intervenção independente"),
                 ("its_forma_efeito_pre_especificada", "ITS: forma do efeito pré-especificada"),
                 ("its_coleta_nao_afetada", "ITS: coleta não afetada"), ("its_conhecimento_alocacao", "ITS: conhecimento da alocação"),
                 ("its_dados_incompletos", "ITS: dados incompletos"), ("its_relato_seletivo", "ITS: relato seletivo"),
                 ("its_outros_riscos", "ITS: outros riscos")],
    }
    rob = []
    for f in ("rob2", "robins_i", "epoc"):
        cont = collections.defaultdict(collections.Counter)
        desac = collections.Counter()
        for r in ler_csv(f"04-qualidade/rob_{f}_consenso.csv"):
            cont[r["dominio"]][r["julgamento_consenso"]] += 1
            if r["julgamento_a"] != r["julgamento_b"]:
                desac[r["dominio"]] += 1
        confere(set(cont) == {d for d, _ in DOMS[f]}, f"domínios de {f} divergem do previsto: {sorted(cont)}")
        geral = collections.Counter(r["rob_geral"] for r in gt.rob if r["ferramenta"] == f)
        rob.append({"ferramenta": FERR[f], "id": f, "n_resultados": sum(geral.values()),
                    "geral": [{"j": j, "rot": gt.rot(j), "simbolo": ROB_SIMBOLO[j], "nivel": ROB_NIVEL[j], "n": n}
                              for j, n in sorted(geral.items(), key=lambda x: ROB_NIVEL[x[0]])],
                    "dominios": [{"id": d, "rotulo": rt, "desacordos": desac[d],
                                  "j": [{"j": j, "rot": gt.rot(j), "simbolo": ROB_SIMBOLO[j], "nivel": ROB_NIVEL[j], "n": n}
                                        for j, n in sorted(cont[d].items(), key=lambda x: (ROB_NIVEL[x[0]], x[0]))]}
                                 for d, rt in DOMS[f]]})
    confere(sum(x["n_resultados"] for x in rob) == ntab["rob_resultados"], "RoB: número de resultados diverge")

    # ---------- processo (linha do tempo): portões e emendas do log, raia pelo ator.id
    corr = {int(r["seq"]): r for r in ler_csv("00-protocolo/correcao_atribuicao.csv") if r["seq"].strip().isdigit()}
    eventos = []
    with open(RAIZ / "rs_log.jsonl", encoding="utf-8") as f:
        for linha in f:
            e = json.loads(linha)
            if e["evento"] in ("portao", "emenda_protocolo") or e["seq"] == 793:
                eventos.append(e)

    def raia(e):
        c = corr.get(e["seq"])
        if c and c["classificacao"] == "mantida" and c["ator_real"] == "humano":
            return "humano"
        aid, tipo = e["ator"]["id"] or "", e["ator"]["tipo"] or ""
        if aid.startswith("ia_") or aid == "autopiloto" or tipo.startswith("ia"):
            return "ia"
        if c and c["classificacao"] == "corrigida" and c["ator_real"].startswith("ia"):
            return "ia"
        if tipo == "script":
            return "script"
        falha(f"evento seq {e['seq']} com ator humano não confirmado em correcao_atribuicao.csv")

    ROT_EMENDA_LOG = {552: "Emenda 1", 718: "Emenda 2", 793: "Emenda 6b"}
    proc = []
    for e in eventos:
        ts = dt.datetime.strptime(e["ts"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        if e["evento"] == "portao":
            g = e["dados"]["portao"]
            rotulo, tipo = f"{g}: {PORTAO[g]}", "portao"
        else:
            confere(e["seq"] in ROT_EMENDA_LOG, f"emenda do log sem rótulo: seq {e['seq']}")
            rotulo, tipo = ROT_EMENDA_LOG[e["seq"]], "emenda"
        proc.append({"seq": e["seq"], "ts": e["ts"], "t": ts.timestamp(), "rotulo": rotulo, "tipo": tipo,
                     "raia": raia(e), "gravado_humano": e["ator"]["tipo"] == "humano"})
    r793 = next(p for p in proc if p["seq"] == 793)
    confere(r793["raia"] == "ia", "seq 793 (Emenda 6b) tem de cair na raia IA")
    confere({p["rotulo"].split(":")[0] for p in proc if p["raia"] == "humano"} == {"G1", "G2", "Emenda 1"},
            "raia humana diferente de G1, G2 e Emenda 1")
    # saídas finais de script (gerado_em dos arquivos de resultado)
    scripts = []
    for rel, rotulo in (("06-analise/swim_principal/swim_resumo.json", "SWiM principal e sensibilidades"),
                        ("06-analise/meta_exploratoria/meta_resumo.json", "metas exploratórias"),
                        ("07-relatorio/prisma_contagens.json", "fluxo PRISMA calculado")):
        ge = ler_json(rel)["gerado_em"]
        scripts.append({"ts": ge, "t": dt.datetime.strptime(ge, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc).timestamp(), "rotulo": rotulo})
    # emendas registradas só no protocolo (sem evento próprio no log): data e id, sem raia
    em_md = open(RAIZ / "00-protocolo/emendas.md", encoding="utf-8").read()
    emendas = []
    for m_ in re.finditer(r"^\| (E00\d|Emenda \d) \| (\d{4}-\d{2}-\d{2}) \| [^|]* \| [^|]* \| ([A-E](?: e [A-E])?) \|", em_md, re.M):
        emendas.append({"id": m_.group(1), "data": m_.group(2), "tipo": m_.group(3),
                        "t": dt.datetime.strptime(m_.group(2), "%Y-%m-%d").replace(tzinfo=dt.timezone.utc).timestamp()})
    confere(len(emendas) == 8, f"esperava 8 emendas na tabela de emendas.md, achei {len(emendas)}")
    dias_log = collections.Counter()
    with open(RAIZ / "rs_log.jsonl", encoding="utf-8") as f:
        for linha in f:
            dias_log[json.loads(linha)["ts"][:10]] += 1
    dias = sorted(dias_log)
    processo = {"eventos": proc, "scripts": scripts, "emendas": emendas,
                "dias_com_evento": dias, "inicio": dias[0], "fim": dias[-1]}

    # ---------- países
    cont_p = collections.Counter()
    multinacional = []
    nr = []
    for ch in chaves:
        p = gt.pais_fmt(ch)
        if p == "NR":
            nr.append(ch)
        elif "países" in p:
            multinacional.append({"chave": ch, "rotulo": rot_aa[ch], "n_paises": int(p.split()[0]),
                                  "inclui_brasil": "Brasil" in p})
        else:
            for x in p.split("; "):
                cont_p[x.strip()] += 1
    paises = {"lista": [{"pais": k, "n": v} for k, v in sorted(cont_p.items(), key=lambda x: (-x[1], x[0]))],
              "multinacional": multinacional, "nao_relatado": [rot_aa[c] for c in nr],
              "brasil": [rot_aa[c] for c in chaves if gt.pais_fmt(c) == "Brasil"]}
    confere(paises["brasil"] == [rot_aa["Araujo2021a"]], "Brasil: esperava só Araujo2021a como estudo brasileiro")

    # ---------- pendências (só de _pendencias_abertas.json; o que fazer e esforço do README da revisão humana)
    readme = open(RAIZ / "08-revisao-humana/README.md", encoding="utf-8").read()
    fazer = {}
    for l in readme.splitlines():
        m_ = re.match(r"\| \d+ \| (P\d+)(?: e (P\d+))? \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", l)
        if m_:
            for p in (m_.group(1), m_.group(2)):
                if p:
                    txt = re.sub(r"\*\*|`", "", m_.group(4)).strip()
                    fazer[p] = {"fazer": txt, "esforco": m_.group(6).strip()}
    ids = [p["id"] for p in pend["pendencias"]]
    confere(pend["abertas"] == len(ids) == nv2["pendencias_abertas"]["valor"], "número de pendências diverge")
    confere(set(ids) == set(fazer), f"pendências sem linha no README: {set(ids) ^ set(fazer)}")
    etapas = []
    for et, rotulo in ETAPAS_PEND:
        its = [p for p in pend["pendencias"] if p["etapa"] == et]
        portoes = sorted({p["portao"] for p in its if p["portao"]})
        etapas.append({"id": et, "rotulo": rotulo, "portoes": portoes,
                       "itens": [{"id": p["id"], "fazer": fazer[p["id"]]["fazer"], "esforco": fazer[p["id"]]["esforco"],
                                  "portao": p["portao"]} for p in its]})
    confere(sum(len(e["itens"]) for e in etapas) == len(ids), "pendência em etapa não prevista")
    pendencias = {"abertas": len(ids), "fechadas": 0, "etapas": etapas}

    # ---------- documentos (tamanho calculado na montagem)
    DOCS = [("revisao.pdf", "Artigo em PDF", "A4, formato de artigo de revista, com a faixa de rascunho", "artigo"),
            ("revisao.html", "Artigo em HTML", "o mesmo texto, com links para cada seção", "artigo"),
            ("revisao.docx", "Artigo em .docx", "para comentar e editar", "artigo"),
            ("suplemento.html", "Suplemento", "estratégias de busca, tabelas estudo a estudo e checklists", "suplemento"),
            ("suplemento.pdf", "Suplemento em PDF", "as mesmas tabelas, para imprimir", "suplemento"),
            ("linguagem-simples.html", "Resumo em linguagem simples", "o que a revisão encontrou, sem jargão", "apoio"),
            ("relatorio-tecnico.html", "Relatório técnico", "o relatório completo gerado ao longo da revisão", "apoio"),
            ("revisao-humana.html", "Guia da revisão humana", "o que falta conferir e como", "apoio")]
    documentos = []
    for arq, rotulo, desc, grupo in DOCS:
        p = RAIZ / "docs" / arq
        tam = p.stat().st_size if p.exists() else None
        documentos.append({"arquivo": arq, "rotulo": rotulo, "desc": desc, "grupo": grupo,
                           "existe": p.exists(), "bytes": tam,
                           "tamanho": (f"{num(tam / 1048576, 1)} MB" if tam and tam >= 1048576
                                       else f"{inteiro(tam / 1024)} kB" if tam else None),
                           "formato": arq.rsplit(".", 1)[1].upper()})

    # ---------- meta e números para os marcadores
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=RAIZ).stdout.strip()
    data_iso = subprocess.run(["git", "log", "-1", "--format=%cs"], capture_output=True, text=True, cwd=RAIZ).stdout.strip()
    data_br = dt.datetime.strptime(data_iso, "%Y-%m-%d").strftime("%d/%m/%Y") if data_iso else "NR"
    n_mb = sum(1 for c in celulas if c["certeza"] == "muito_baixa")
    confere(n_mb == ntab["certeza_contagem"]["muito_baixa"], "contagem de células com certeza muito baixa diverge")
    numeros = {
        "estudos": str(len(gt.M)), "relatos": str(prisma["incluidos"]["relatos"]), "efeitos": inteiro(ntab["efeitos"]),
        "celulas": str(len(celulas)), "celulas_muito_baixa": str(n_mb), "pendencias": str(len(ids)),
        "pendencias_fechadas": "0", "estudos_sintese": str(ntab["n_swim_principal_estudos"]),
        "criticos": str(len(criticos)), "so_fora": str(len(so_fora)), "sem_principal": str(len(sem_princ)),
        "estudos_com_efeitos": str(ntab["estudos_com_efeitos"]), "estudos_com_principal": str(ntab["estudos_com_principal"]),
        "registros_bases": inteiro(ramos[0]["identificados"]), "registros_citacoes": inteiro(ramos[1]["identificados"]),
        "ano_min": str(ntab["ano_min"]), "ano_max": str(ntab["ano_max"]),
        "celulas_inconclusivo": str(caixa_rotulos.get("Inconclusivo", 0)),
        "amplo_apoio_rand_k": str(g_amplo["k"]), "amplo_apoio_rand_pos": str(g_amplo["n_pos"]),
        "real_apoio_rand_k": str(g_real["k"]), "real_apoio_rand_estudos": ", ".join(g_real["estudos"]),
        "lago_paises": str(multinacional[0]["n_paises"]) if multinacional else "NR",
        "lago_rotulo": rot_aa["Lago2015"], "araujo_rotulo": rot_aa["Araujo2021a"], "tyszler_rotulo": rot_aa["Tyszler2015"],
        "rob_arbitro": str(ntab["rob_dominios"].get("arbitro_ia", 0)),
        "rob_dominios_total": str(sum(ntab["rob_dominios"].values())),
        "rob_resultados": str(ntab["rob_resultados"]),
        "data_versao": data_br,
        "data_inicio": dt.datetime.strptime(dias[0], "%Y-%m-%d").strftime("%d/%m/%Y"),
        "data_fim": dt.datetime.strptime(dias[-1], "%Y-%m-%d").strftime("%d/%m/%Y"),
    }
    confere(caixa_rotulos.get("Inconclusivo", 0) == len(celulas), "nem todas as células estão como Inconclusivo")

    saida = {
        "meta": {"titulo": "Pesquisas eleitorais publicadas mudam o voto?",
                 "subtitulo": "Revisão sistemática rápida sobre os efeitos bandwagon e underdog e o comparecimento",
                 "autor": "Felipe Lamarca", "afiliacao": "MAPE/IESP-UERJ", "data_versao": data_br,
                 "commit": commit, "tag_anterior": "v1-oqf-2026-09-24", "url": "https://felipelamarca.com/pesquisas-eleitorais-rs/",
                 "fontes": {rel: sha(rel) for rel in ("06-analise/certeza.csv", "06-analise/swim_principal/swim_resumo.json",
                                                      "07-relatorio/_pendencias_abertas.json",
                                                      "09-documento-final/revista/celulas.json")}},
        "numeros": numeros,
        "heroi": {"pontos": len(gt.M)},
        "mensagens": extrair_mensagens(),
        "linguagem_simples": extrair_linguagem_simples(),
        "prisma": {"ramos": ramos, "relatos": prisma["incluidos"]["relatos"], "estudos": prisma["incluidos"]["estudos"],
                   "fluxo_estudos": {k: v for k, v in fluxo_estudos.items()}},
        "blocos": blocos, "celulas": celulas, "vazias": vazias,
        "estudos": estudos, "fora": fora_linhas,
        "sensibilidades": analises, "metas": metas, "rob": rob, "processo": processo, "paises": paises,
        "pendencias": pendencias, "documentos": documentos,
    }
    validar(saida)
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"vitrine.json: {len(celulas)} células, {len(estudos)} estudos, {len(ids)} pendências, "
          f"mensagens {'PROVISÓRIAS (v1)' if saida['mensagens']['provisorio'] else 'do artigo'}, "
          f"linguagem simples {'PROVISÓRIA (v1)' if saida['linguagem_simples']['provisorio'] else 'do documento'}")


# ------------------------------------------------------------------ SCHEMA: campos permitidos por bloco
# None = valor primitivo (ou lista de primitivos); dict = objeto com essas chaves; [dict] = lista de objetos;
# "*" como chave = dicionário de chaves livres cujos valores seguem o esquema indicado.
ROB_ITEM = {"construto": None, "ferramenta": None, "geral": None, "geral_rot": None, "simbolo": None, "nivel": None}
J = {"j": None, "rot": None, "simbolo": None, "nivel": None, "n": None}
GRUPO = {"rotulo": None, "classe_rot": None, "bloco": None, "pos_rot": None, "k": None, "n_dir": None, "n_pos": None,
         "n_neg": None, "n_mistos": None, "n_nulos": None, "proporcao": None, "ic": None, "ic_fmt": None, "p_fmt": None,
         "certeza": None, "nivel": None, "certeza_rot": None, "estudos": None, "ordem": None}
SCHEMA = {
    "meta": {"titulo": None, "subtitulo": None, "autor": None, "afiliacao": None, "data_versao": None, "commit": None,
             "tag_anterior": None, "url": None, "fontes": {"*": None}},
    "numeros": {"*": None},
    "heroi": {"pontos": None},
    "mensagens": {"provisorio": None, "fonte": None, "itens": [{"titulo": None, "html": None}]},
    "linguagem_simples": {"provisorio": None, "fonte": None, "html": None},
    "prisma": {"relatos": None, "estudos": None,
               "ramos": [{"id": None, "rotulo": None, "identificados": None, "identificados_fmt": None,
                          "por_fonte": [{"fonte": None, "n": None, "n_fmt": None}], "duplicatas": None,
                          "automacao": None, "triados": None, "excluidos_triagem": None, "buscados": None,
                          "nao_recuperados": None, "avaliados": None, "excluidos_elegibilidade": None,
                          "motivos": [{"motivo": None, "n": None}], "incluidos": None}],
               "fluxo_estudos": {"estudos": None, "com_efeitos": None, "com_principal": None, "sintese": None,
                                 "sem_efeitos": None, "sem_principal": None, "criticos": None, "so_fora": None}},
    "blocos": [{"id": None, "rotulo": None, "secao": None,
                "classes": [{"classe": None, "rotulo": None, "celulas": None, "vazias": None}]}],
    "celulas": [{"id": None, "bloco": None, "familia": None, "familia_rot": None, "construto": None, "comparador": None,
                 "comparador_rot": None, "alvo": None, "classe": None, "classe_rot": None, "enunciado": None,
                 "certeza": None, "certeza_rot": None, "nivel": None, "k": None, "n_dir": None, "n_pos": None,
                 "n_neg": None, "n_mistos": None, "n_nulos": None, "pos_rot": None, "neg_rot": None, "contagem": None,
                 "x_de_y": None, "proporcao": None, "proporcao_fmt": None, "ic": None, "ic_fmt": None, "p": None,
                 "p_fmt": None, "delta_fmt": None, "excluidos_critico": None, "rebaixamentos": None, "partida": None,
                 "caixa": None, "secao": None,
                 "estudos": [{"chave": None, "direcao": None, "glifo": None, "direcao_rot": None, "n_efeitos": None,
                              "n_pos": None, "n_neg": None, "n_amostra": None, "n_fmt": None, "rob": ROB_ITEM}]}],
    "vazias": [{"familia": None, "familia_rot": None, "construto": None, "comparador": None, "comparador_rot": None,
                "alvo": None, "classe": None, "excluidos_critico": None, "bloco": None}],
    "estudos": {"*": {"rotulo": None, "ano": None, "pais": None, "regioes": None, "regiao_rot": None, "desenho": None,
                      "desenho_cod": None, "familia": None, "familia_rot": None, "realismo": None, "realismo_rot": None,
                      "unidade": None, "rob": [ROB_ITEM], "situacao": None, "motivo": None}},
    "fora": [{"chave": None, "construto": None, "alvo": None, "classe": None, "grupo_rot": None, "direcao": None,
              "glifo": None, "direcao_rot": None, "n_efeitos": None, "n_pos": None, "n_neg": None, "n_fmt": None}],
    "sensibilidades": [{"id": None, "rotulo": None, "post_hoc": None, "grade": None, "grupos": [GRUPO]}],
    "metas": [{"id": None, "titulo": None, "k_estudos": None, "k_efeitos": None, "g": None, "g_fmt": None, "ic": None,
               "ic_fmt": None, "pi": None, "pi_fmt": None, "p_fmt": None, "gl": None, "gl_fmt": None, "tau2_fmt": None,
               "i2_fmt": None, "rve_confiavel": None, "delta": None, "delta_fmt": None,
               "efeitos": [{"chave": None, "rotulo": None, "efeito": None, "yi": None, "lo": None, "hi": None,
                            "g_fmt": None, "ep_fmt": None}],
               "loo": [{"sem": None, "g_fmt": None, "ic_fmt": None, "muda": None}]}],
    "rob": [{"ferramenta": None, "id": None, "n_resultados": None, "geral": [J],
             "dominios": [{"id": None, "rotulo": None, "desacordos": None, "j": [J]}]}],
    "processo": {"eventos": [{"seq": None, "ts": None, "t": None, "rotulo": None, "tipo": None, "raia": None,
                              "gravado_humano": None}],
                 "scripts": [{"ts": None, "t": None, "rotulo": None}],
                 "emendas": [{"id": None, "data": None, "tipo": None, "t": None}],
                 "dias_com_evento": None, "inicio": None, "fim": None},
    "paises": {"lista": [{"pais": None, "n": None}],
               "multinacional": [{"chave": None, "rotulo": None, "n_paises": None, "inclui_brasil": None}],
               "nao_relatado": None, "brasil": None},
    "pendencias": {"abertas": None, "fechadas": None,
                   "etapas": [{"id": None, "rotulo": None, "portoes": None,
                               "itens": [{"id": None, "fazer": None, "esforco": None, "portao": None}]}]},
    "documentos": [{"arquivo": None, "rotulo": None, "desc": None, "grupo": None, "existe": None, "bytes": None,
                    "tamanho": None, "formato": None}],
}
PROIBIDOS = {"evidencia", "trecho", "outcome", "modelo", "subgrupo", "justificativa", "descricao", "arquivo_pendencia",
             "ator_registrado", "observacao", "aviso", "pdf_path", "validado_humano", "verificado_humano",
             "pontos_para_o_revisor"}


def validar(obj, esquema=SCHEMA, caminho="vitrine"):
    if esquema is None:
        if isinstance(obj, dict) or (isinstance(obj, list) and any(isinstance(x, (dict, list)) for x in obj)):
            falha(f"{caminho}: esperava valor primitivo, achei estrutura")
        return
    if isinstance(esquema, list):
        if not isinstance(obj, list):
            falha(f"{caminho}: esperava lista")
        for i, x in enumerate(obj):
            validar(x, esquema[0], f"{caminho}[{i}]")
        return
    if not isinstance(obj, dict):
        falha(f"{caminho}: esperava objeto")
    for k, v in obj.items():
        if k in PROIBIDOS:
            falha(f"{caminho}.{k}: campo proibido na vitrine")
        if "*" in esquema:
            validar(v, esquema["*"], f"{caminho}.{k}")
        elif k not in esquema:
            falha(f"{caminho}.{k}: chave fora do SCHEMA")
        else:
            validar(v, esquema[k], f"{caminho}.{k}")


if __name__ == "__main__":
    main()
