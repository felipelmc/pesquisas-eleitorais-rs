"""Prepara os dados das 7 figuras do artigo: 09-documento-final/revista/figuras/dados/dados_<nome>.csv.

USO (da raiz do projeto)
    python3 09-documento-final/revista/figuras/preparar_dados_figuras.py

Só lê arquivos do projeto e só escreve em 09-documento-final/revista/figuras/dados/. Nenhuma análise nova:
cada CSV traz exatamente o que a figura desenha, copiado ou contado dos arquivos de origem, com os rótulos
prontos em português (direção pela dir_rot de 07-relatorio/gerar_tabelas_relatorio.py, sem asteriscos de
Markdown; a coluna `italico` diz quando o rótulo é palavra estrangeira). Junções só por chave, id_efeito ou
pelas colunas-chave da célula. O desenho (posições, cores, fontes) fica em gerar_figuras.R.

Saídas
    dados/dados_modelo_logico.csv   nós do DAG (00-protocolo/dag_v1.mmd) e moderadores (tabela Z da teoria)
    dados/dag_arestas.csv           arestas do DAG, na ordem do .mmd
    dados/dados_prisma.csv          linhas das caixas do fluxo PRISMA 2020 (07-relatorio/prisma_contagens.json), sem
                                    os itens com n = 0, que não se aplicam a esta revisão (PRISMA 2020: omitir caixas
                                    que não se aplicam)
    dados/dados_rob.csv             julgamentos de risco de viés por ferramenta, domínio e nível (04-qualidade/)
    dados/dados_celulas.csv         células de revista/celulas.json (proporção, IC, x de y, certeza) e a vazia
    dados/dados_direcao.csv         direção por estudo e célula (SWiM principal e painel fora da contagem)
    dados/dados_metas.csv           efeitos das duas metas exploratórias, em ordem de precisão (menor erro-padrão
                                    primeiro), com o risco de viés do resultado, e as estimativas combinadas
    dados/dados_realismo.csv        um registro por estudo x célula, realismo x direção (T9 e T14)
"""
import collections
import contextlib
import csv
import importlib.util
import io
import json
import os
import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.dont_write_bytecode = True  # não deixa __pycache__ nas pastas dos módulos importados por caminho

R = Path(__file__).resolve().parents[3]
os.chdir(R)  # gerar_tabelas_relatorio.py e contagens_mecanismos_moderadores.py leem caminhos relativos à raiz
DADOS = R / "09-documento-final/revista/figuras/dados"


def importar(nome, caminho, silencioso=False):
    spec = importlib.util.spec_from_file_location(nome, R / caminho)
    mod = importlib.util.module_from_spec(spec)
    if silencioso:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    else:
        spec.loader.exec_module(mod)
    return mod


gtr = importar("gerar_tabelas_relatorio", "07-relatorio/gerar_tabelas_relatorio.py")
cmm = importar("contagens_mecanismos_moderadores", "09-documento-final/insumos/contagens_mecanismos_moderadores.py",
               silencioso=True)


def ler_csv(rel):
    with open(R / rel, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def ler_json(rel):
    with open(R / rel, encoding="utf-8") as f:
        return json.load(f)


def gravar(nome, linhas, campos):
    DADOS.mkdir(parents=True, exist_ok=True)
    with open(DADOS / nome, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
        w.writeheader()
        for l in linhas:
            faltam = set(campos) - set(l)
            if faltam:
                sys.exit(f"ERRO ({nome}): linha sem os campos {sorted(faltam)}: {l}")
            w.writerow({c: l[c] for c in campos})
    print(f"{nome}: {len(linhas)} linhas")


def sem_md(s):
    """Tira os asteriscos de Markdown; devolve (texto, itálico?)."""
    return s.replace("*", ""), "*" in s


def dir_rotulo(d, construto, celula):
    return sem_md(gtr.dir_rot(d, construto, celula))


INT = gtr.inteiro  # inteiro pt-BR com ponto de milhar


def dec_br(x, casas=2):
    """Decimal pt-BR arredondado meio para cima sobre repr(x) (0,975 -> 0,98; o f-string daria 0,97), com vírgula e
    sinal de menos U+2212; zero sai sem sinal."""
    d = Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-casas), rounding=ROUND_HALF_UP)
    if d.is_zero():
        d = d.copy_abs()
    return f"{d:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".").replace("-", "\u2212")

# ------------------------------------------------------------------ vocabulário comum
FAM_CURTA = {"pesquisa_pre_eleitoral": "pesquisa", "agregador_projecao": "agregador ou projeção",
             "boca_de_urna": "boca de urna", "outro": "apuração parcial"}
COMP = {"sem_pesquisa": "sem pesquisa", "mesmo_candidato_atras": "mesmo candidato atrás",
        "outro_resultado": "outro resultado", "outro": "outro comparador",
        "antes_depois_proibicao": "antes e depois da proibição", "unidades_nao_expostas": "unidades não expostas"}
CLASSE = {"randomizado": "randomizado", "nao_randomizado": "não randomizado"}
BLOCO = {  # bloco de celulas.json -> (rótulo, sentido positivo)
    "apoio_principal": ("Apoio a quem aparece à frente", "a favor = bandwagon"),
    "viabilidade": ("Viabilidade", "a favor = apoio à opção viável"),
    "momentum": ("Momentum", "a favor = apoio a quem ganha apoio"),
    "mobilizacao": ("Comparecimento", "a favor = mobilização"),
    "outro_alvo": ("Outro alvo", "sem posição única de líder ou azarão"),
}
BLOCO_DE_CELULA = {("apoio_ao_lider", "principal"): "apoio_principal", ("apoio_ao_lider", "viabilidade"): "viabilidade",
                   ("apoio_ao_lider", "momentum"): "momentum", ("mobilizacao", "mobilizacao"): "mobilizacao",
                   ("apoio_ao_lider", "outro"): "outro_alvo"}
ORDEM_BLOCO = ["apoio_principal", "viabilidade", "momentum", "mobilizacao", "outro_alvo"]
ESTRANGEIRAS = re.compile(r"bandwagon|underdog|momentum|survey|post hoc", re.I)
CERTEZA_NIVEL = {"muito_baixa": 1, "baixa": 2, "moderada": 3, "alta": 4}
ROB_NIVEL = {"baixo": 1, "algumas_preocupacoes": 2, "moderado": 2, "incerto": 2, "alto": 3, "grave": 3, "critico": 4}
ROB_ROT = {"baixo": "baixo", "algumas_preocupacoes": "algumas preocupações", "moderado": "moderado",
           "incerto": "incerto", "alto": "alto", "grave": "grave", "critico": "crítico"}
DESENHO_ORDEM = list(gtr.DESENHO) + ["outro"]  # laboratório induzido, laboratório real, survey, natural, campo, painel
GLIFO = {"benefico": "a_favor", "danoso": "contra", "misto": "misto", "nulo": "nulo"}


def rotulo_comparacao(familia, comparador):
    return f"{FAM_CURTA[familia]} × {COMP[comparador]}"


celulas = ler_json("09-documento-final/revista/celulas.json")
CHAVE_CEL = tuple(celulas["chave"])
CEL = {tuple(c[k] for k in CHAVE_CEL): c for c in celulas["celulas"]}
VAZIAS = {tuple(c[k] for k in CHAVE_CEL): c for c in celulas["vazias"]}
M = gtr.M  # master de extração (citekey -> linha)


# ------------------------------------------------------------------ 1. modelo lógico
NOS_PT = {
    "exposicao": "exposição à pesquisa", "percepcao_viabilidade": "percepção de viabilidade",
    "calculo_estrategico": "cálculo estratégico", "heuristica_consenso": "heurística de consenso",
    "conformidade": "conformidade", "simpatia_azarao": "simpatia pelo azarão", "emocoes": "emoções",
    "apoio_ao_lider": "apoio a quem aparece à frente", "complacencia": "complacência",
    "desmobilizacao": "desmobilização", "apoio_latente": "apoio latente", "interesse_politico": "interesse político",
    "preferencia_previa": "preferência prévia", "pesquisa_t1": "pesquisa anterior", "pesquisa_t2": "pesquisa seguinte",
    "divulgacao_enviesada": "divulgação enviesada", "resposta_ao_survey": "resposta ao survey",
}
# papéis: 00-protocolo/teoria_programa.md, seção 3 (papéis das variáveis) e classes do .mmd
PAPEL = {
    "exposicao": "exposicao", "apoio_ao_lider": "desfecho", "percepcao_viabilidade": "mediador",
    "calculo_estrategico": "mecanismo", "heuristica_consenso": "mecanismo", "conformidade": "mecanismo",
    "simpatia_azarao": "mecanismo", "emocoes": "mecanismo", "complacencia": "perverso", "desmobilizacao": "perverso",
    "divulgacao_enviesada": "perverso", "apoio_latente": "confundidor", "interesse_politico": "confundidor",
    "preferencia_previa": "confundidor", "resposta_ao_survey": "colisor", "pesquisa_t1": "pesquisa",
    "pesquisa_t2": "pesquisa",
}
# elos da tabela por elo (teoria_programa.md, seção 2): aresta -> código do elo
ELO = {("exposicao", "percepcao_viabilidade"): "E1", ("percepcao_viabilidade", "calculo_estrategico"): "E2",
       ("calculo_estrategico", "apoio_ao_lider"): "E2", ("exposicao", "heuristica_consenso"): "E3",
       ("heuristica_consenso", "apoio_ao_lider"): "E3", ("exposicao", "conformidade"): "E4",
       ("conformidade", "apoio_ao_lider"): "E4", ("exposicao", "simpatia_azarao"): "E5",
       ("simpatia_azarao", "apoio_ao_lider"): "E5", ("exposicao", "emocoes"): "E6", ("emocoes", "apoio_ao_lider"): "E6",
       ("exposicao", "complacencia"): "E7", ("complacencia", "desmobilizacao"): "E7",
       ("divulgacao_enviesada", "pesquisa_t1"): "E8"}


def ler_mermaid(rel):
    """Nós (id -> nome), arestas [(de, para, tipo)] na ordem do arquivo e classes (id -> classe)."""
    nos, arestas, classes = {}, [], {}
    tok_re = re.compile(r"^\s*([A-Za-z0-9_]+)(?:\[([^\]]+)\])?\s*$")
    for linha in open(R / rel, encoding="utf-8"):
        s = linha.strip()
        if not s or s.startswith("%%") or s.startswith("flowchart") or s.startswith("classDef"):
            continue
        m = re.match(r"class\s+([\w,]+)\s+(\w+)", s)
        if m:
            for i in m.group(1).split(","):
                classes[i] = m.group(2)
            continue
        partes = re.split(r"\s*(-->|-\.->)\s*", s)
        ids = []
        for p in partes[0::2]:
            m = tok_re.match(p)
            if not m:
                sys.exit(f"ERRO: token do mermaid não reconhecido: {p!r}")
            i, nome = m.group(1), m.group(2)
            if nome:
                nos[i] = nome
            ids.append(i)
        for a, seta, b in zip(ids, partes[1::2], ids[1:]):
            arestas.append((a, b, "tracejada" if seta == "-.->" else "solida"))
    return nos, arestas, classes


def ler_tabela_z():
    """Moderadores da tabela Z (teoria_programa.md, seção 4): nome sem o parêntese explicativo."""
    txt = open(R / "00-protocolo/teoria_programa.md", encoding="utf-8").read()
    bloco = txt.split("## 4. Tabela Z")[1].split("\n## ")[0]
    mods = []
    for l in bloco.splitlines():
        if l.startswith("| ") and not l.startswith("| Moderador") and not l.startswith("|---"):
            nome = l.split("|")[1].strip()
            nome = re.sub(r"\s*\(.*\)\s*$", "", nome)
            mods.append(nome[0].lower() + nome[1:])
    if len(mods) < 5:
        sys.exit("ERRO: tabela Z não encontrada em teoria_programa.md")
    return mods


def fig_modelo_logico():
    nos, arestas, classes = ler_mermaid("00-protocolo/dag_v1.mmd")
    for i, nome in nos.items():
        if nome not in NOS_PT or nome not in PAPEL:
            sys.exit(f"ERRO: nó do DAG sem rótulo ou papel: {nome}")
    for (a, b), e in ELO.items():
        if not any(nos[x] == a and nos[y] == b for x, y, _ in arestas):
            sys.exit(f"ERRO: aresta de elo {e} ({a} -> {b}) não está no .mmd")
    linhas = []
    for o, (i, nome) in enumerate(nos.items(), start=1):
        linhas.append({"elemento": "no", "ordem": o, "id": i, "nome": nome, "rotulo": NOS_PT[nome],
                       "papel": PAPEL[nome], "tracejado": int(classes.get(i) == "perverso"),
                       "colisor": int(classes.get(i) == "colisor")})
    for o, nome in enumerate(ler_tabela_z(), start=1):
        linhas.append({"elemento": "moderador", "ordem": o, "id": f"Z{o:02d}", "nome": "", "rotulo": nome,
                       "papel": "moderador", "tracejado": 0, "colisor": 0})
    gravar("dados_modelo_logico.csv", linhas,
           ["elemento", "ordem", "id", "nome", "rotulo", "papel", "tracejado", "colisor"])
    ar = [{"ordem": o, "de_id": a, "para_id": b, "de": nos[a], "para": nos[b], "de_rotulo": NOS_PT[nos[a]],
           "para_rotulo": NOS_PT[nos[b]], "tipo": t, "elo": ELO.get((nos[a], nos[b]), "")}
          for o, (a, b, t) in enumerate(arestas, start=1)]
    gravar("dag_arestas.csv", ar, ["ordem", "de_id", "para_id", "de", "para", "de_rotulo", "para_rotulo", "tipo", "elo"])


# ------------------------------------------------------------------ 2. PRISMA
MOTIVO = {  # critérios de elegibilidade (00-protocolo/codebook_elegibilidade.csv; protocolo, seção 3)
    "c1_populacao_contexto": "população ou contexto fora do escopo",
    "c2_intervencao_estudada": "pesquisa não é a exposição estudada",
    "c3_desfecho": "sem desfecho de voto ou comparecimento",
    "c4_desenho_elegivel": "desenho não elegível",
    "c5_estudo_primario": "não é estudo primário",
    "c6_nao_retratado": "retratado",
}
FONTE_ROT = {"openalex": "OpenAlex", "bdtd": "BDTD"}


def fig_prisma():
    pj = ler_json("07-relatorio/prisma_contagens.json")
    cod = {r["variavel"] for r in ler_csv("00-protocolo/codebook_elegibilidade.csv")}
    linhas = []

    def add(caixa, ramo, fase, texto, caminho=None, estilo="normal"):
        n = ""
        if caminho:
            v = pj
            for p in caminho.split("."):
                v = v[p]
            n = v
            if v == 0 and estilo == "normal":
                return  # item com n = 0 não se aplica: fica fora da caixa (verificar_figuras.py confere que é 0)
            texto = texto.replace("{n}", INT(v))
        linhas.append({"caixa": caixa, "ramo": ramo, "fase": fase, "linha": sum(1 for l in linhas if l["caixa"] == caixa) + 1,
                       "texto": texto, "n": n, "caminho_json": caminho or "", "estilo": estilo})

    for ramo, pre in (("bases", "b"), ("outros_metodos", "o")):
        j = f"{ramo}"
        if ramo == "bases":
            add("b_ident", ramo, "identificacao", "Registros identificados em bases (n = {n})", f"{j}.identificados.bases", "titulo")
            for f, _ in sorted(pj[ramo]["identificados"]["por_fonte"].items(), key=lambda x: -x[1]):
                add("b_ident", ramo, "identificacao", f"{FONTE_ROT.get(f, f)} (n = {{n}})", f"{j}.identificados.por_fonte.{f}")
            add("b_ident", ramo, "identificacao", "registros de estudos (n = {n})", f"{j}.identificados.registros_estudos")
        else:
            add("o_ident", ramo, "identificacao", "Registros identificados por busca de citações (n = {n})",
                f"{j}.identificados.busca_citacoes", "titulo")
            add("o_ident", ramo, "identificacao", "sites e organizações (n = {n})", f"{j}.identificados.sites_organizacoes")
            add("o_ident", ramo, "identificacao", "outros (n = {n})", f"{j}.identificados.outros")
        c = f"{pre}_removidos"
        add(c, ramo, "identificacao", "Removidos por script:", None, "titulo")
        add(c, ramo, "identificacao", ("duplicatas (n = {n})" if ramo == "bases" else
                                        "duplicatas ou já identificados nas bases (n = {n})"),
            f"{j}.removidos_antes_triagem.duplicatas")
        filtros = pj[ramo]["removidos_antes_triagem"]["automacao_por_filtro"]
        if set(filtros) != {"ano"} or filtros["ano"] != pj[ramo]["removidos_antes_triagem"]["automacao"]:
            sys.exit(f"ERRO: automação do ramo {ramo} não é só o filtro de ano: {filtros}")
        add(c, ramo, "identificacao", "publicados antes de 2010, filtro de ano (n = {n})",
            f"{j}.removidos_antes_triagem.automacao_por_filtro.ano")
        add(c, ramo, "identificacao", "outros motivos (n = {n})", f"{j}.removidos_antes_triagem.outros_motivos")
        add(f"{pre}_triados", ramo, "triagem", "Títulos e resumos triados por IA (n = {n})", f"{j}.triados", "titulo")
        add(f"{pre}_excl_triagem", ramo, "triagem", "Registros excluídos na triagem por IA (n = {n})",
            f"{j}.excluidos_triagem", "titulo")
        add(f"{pre}_buscados", ramo, "triagem", "Relatos buscados para recuperação (n = {n})", f"{j}.buscados", "titulo")
        add(f"{pre}_nao_rec", ramo, "triagem", "Relatos não recuperados (n = {n})", f"{j}.nao_recuperados", "titulo")
        add(f"{pre}_avaliados", ramo, "triagem", "Relatos avaliados no texto completo (n = {n})", f"{j}.avaliados", "titulo")
        add(f"{pre}_excl_tc", ramo, "triagem", "Relatos excluídos (n = {n}):", f"{j}.excluidos_elegibilidade.total", "titulo")
        mot = pj[ramo]["excluidos_elegibilidade"]["motivos"]
        for m_, v in sorted(mot.items(), key=lambda x: -x[1]):
            if m_ not in cod or m_ not in MOTIVO:
                sys.exit(f"ERRO: motivo de exclusão sem rótulo ou fora do codebook: {m_}")
            add(f"{pre}_excl_tc", ramo, "triagem", f"{MOTIVO[m_]} (n = {{n}})", f"{j}.excluidos_elegibilidade.motivos.{m_}")
        add(f"{pre}_seta_incl", ramo, "inclusao", "{n} relatos", f"{j}.incluidos_relatos", "seta")
    add("incluidos", "geral", "inclusao", "Estudos incluídos na síntese (n = {n})", "incluidos.estudos", "titulo")
    add("incluidos", "geral", "inclusao", "Relatos dos estudos incluídos (n = {n})", "incluidos.relatos", "titulo")
    gravar("dados_prisma.csv", linhas, ["caixa", "ramo", "fase", "linha", "texto", "n", "caminho_json", "estilo"])


# ------------------------------------------------------------------ 3. risco de viés
FERR = {"rob2": ("RoB 2", "04-qualidade/rob_rob2_consenso.csv"),
        "robins_i": ("ROBINS-I V2", "04-qualidade/rob_robins_i_consenso.csv"),
        "epoc": ("EPOC", "04-qualidade/rob_epoc_consenso.csv")}
# Nomes dos domínios: dimensões dos codebooks 00-protocolo/codebook_v0_{rob2,robins_i}.csv (sem acento no
# identificador) e descrições das variáveis de 00-protocolo/codebook_v0_epoc.csv. O dicionário só acentua e
# conferido contra os codebooks abaixo.
DOM_ROB2 = {"D1": ("D1_Randomizacao", "D1 randomização"),
            "D1b": ("D1b_Recrutamento_cluster", "D1b recrutamento (cluster)"),
            "D2": ("D2_Desvios_atribuicao", "D2 desvios da atribuição"),
            "D3": ("D3_Dados_faltantes", "D3 dados faltantes"),
            "D4": ("D4_Mensuracao", "D4 mensuração do desfecho"),
            "D5": ("D5_Resultado_relatado", "D5 resultado relatado")}
DOM_ROBINS = {"D1": ("D1a_Confundimento_linha_de_base", "D1 confundimento"),
              "D2": ("D2_Classificacao_intervencoes", "D2 classificação da exposição"),
              "D3": ("D3_Selecao_participantes", "D3 seleção de participantes"),
              "D4": ("D4_Dados_faltantes", "D4 dados faltantes"),
              "D5": ("D5_Mensuracao_outcome", "D5 mensuração do desfecho"),
              "D6": ("D6_Resultado_relatado", "D6 resultado relatado")}
EPOC_FORA_DO_GERAL = {"cg_sequencia_aleatoria", "cg_ocultacao_alocacao"}  # Emenda 4a


def fig_rob():
    cb = {f: ler_csv(f"00-protocolo/codebook_v0_{f}.csv") for f in FERR}
    dims = {f: {r["dimensao"] for r in cb[f]} for f in cb}
    for f, dic in (("rob2", DOM_ROB2), ("robins_i", DOM_ROBINS)):
        for d, (dim, _) in dic.items():
            if dim not in dims[f]:
                sys.exit(f"ERRO: domínio {d} ({dim}) não está no codebook de {f}")
    epoc_desc = {r["variavel"]: r["descricao"] for r in cb["epoc"]}
    linhas = []
    for f, (frot, arq) in FERR.items():
        rs = ler_csv(arq)
        doms = []
        for r in rs:
            if r["dominio"] not in doms:
                doms.append(r["dominio"])
        if f == "rob2":
            ordem = [d for d in DOM_ROB2 if d in doms]
            rot = {d: DOM_ROB2[d][1] for d in ordem}
            grupo = {d: "dominio" for d in ordem}
        elif f == "robins_i":
            ordem = [d for d in DOM_ROBINS if d in doms]
            rot = {d: DOM_ROBINS[d][1] for d in ordem}
            grupo = {d: "dominio" for d in ordem}
        else:
            cg = [v for v in epoc_desc if v.startswith("cg_") and v in doms]
            its = [v for v in epoc_desc if v.startswith("its_") and v in doms]
            ordem = cg + its
            rot = {}
            for d in ordem:
                t = epoc_desc[d]
                t = t[0].lower() + t[1:]
                t = t.replace("outcomes", "desfechos").replace("outcome", "desfecho")
                t = t.replace("intervenção", "exposição")
                if d in EPOC_FORA_DO_GERAL:
                    t += " \u2020"  # fora do julgamento geral (Emenda 4a); explicado na nota da figura
                rot[d] = t
            grupo = {d: ("com grupo de comparação" if d.startswith("cg_") else "série temporal interrompida")
                     for d in ordem}
        if set(ordem) != set(doms):
            sys.exit(f"ERRO: domínios de {arq} sem rótulo: {set(doms) - set(ordem)}")
        for o, d in enumerate(ordem, start=1):
            cont = collections.Counter(r["julgamento_consenso"] for r in rs if r["dominio"] == d)
            tot = sum(cont.values())
            for j, n in sorted(cont.items(), key=lambda x: ROB_NIVEL[x[0]]):
                linhas.append({"ferramenta": f, "ferramenta_rotulo": frot, "grupo": grupo[d], "dominio": d,
                               "dominio_rotulo": rot[d], "ordem": o, "julgamento": j, "julgamento_rotulo": ROB_ROT[j],
                               "nivel": ROB_NIVEL[j], "n": n, "total": tot, "proporcao": n / tot})
        geral = [r for r in ler_csv("04-qualidade/rob_geral.csv") if r["ferramenta"] == f]
        cont = collections.Counter(r["rob_geral"] for r in geral)
        tot = sum(cont.values())
        for j, n in sorted(cont.items(), key=lambda x: ROB_NIVEL[x[0]]):
            linhas.append({"ferramenta": f, "ferramenta_rotulo": frot, "grupo": "geral", "dominio": "geral",
                           "dominio_rotulo": "julgamento geral", "ordem": len(ordem) + 1, "julgamento": j,
                           "julgamento_rotulo": ROB_ROT[j], "nivel": ROB_NIVEL[j], "n": n, "total": tot,
                           "proporcao": n / tot})
    gravar("dados_rob.csv", linhas, ["ferramenta", "ferramenta_rotulo", "grupo", "dominio", "dominio_rotulo", "ordem",
                                     "julgamento", "julgamento_rotulo", "nivel", "n", "total", "proporcao"])


# ------------------------------------------------------------------ 4. células
def fig_celulas():
    swim = {tuple(g[k] for k in CHAVE_CEL): g for g in ler_json("06-analise/swim_principal/swim_resumo.json")["grupos"]}
    linhas = []
    ordem = 0
    for b in ORDEM_BLOCO[:4]:
        cels = [c for c in celulas["celulas"] if c["bloco"] == b]
        vaz = [v for v in celulas["vazias"] if BLOCO_DE_CELULA[(v["construto_outcome"], v["celula_alvo"])] == b]
        for c in cels + vaz:
            ordem += 1
            k = tuple(c[x] for x in CHAVE_CEL)
            g = swim[k]
            vazia = "id" not in c
            n_dir = g["n_estudos"]
            if vazia:
                marca = "vazia"
            elif g["proporcao_benefica"] is None:
                marca = "nulo"
            else:
                marca = "proporcao"
            extra = []
            if g["n_mistos"]:
                extra.append(f"{g['n_mistos']} misto")
            if g["n_nulos"]:
                extra.append(f"{g['n_nulos']} nulo")
            if vazia:
                rot_xy = "k = 0"
            elif n_dir == 0:
                rot_xy = "; ".join(extra)
            else:
                rot_xy = f"{g['n_beneficos']} de {n_dir}" + (" (+" + "; +".join(extra) + ")" if extra else "")
            p = g["proporcao_benefica"]
            maioria = "" if p is None else ("a_favor" if p > 0.5 else "contra" if p < 0.5 else "empate")
            ic = g["ic_proporcao"] or ["", ""]
            linhas.append({
                "ordem": ordem, "id": c.get("id", "vazia"), "bloco": b, "bloco_rotulo": BLOCO[b][0],
                "bloco_sentido": BLOCO[b][1], "familia": k[0], "comparador": k[2], "classe": k[4],
                "classe_rotulo": CLASSE[k[4]], "rotulo_linha": rotulo_comparacao(k[0], k[2]),
                "k": g["k_estudos"], "n_com_direcao": n_dir, "n_a_favor": g["n_beneficos"], "n_contra": g["n_danosos"],
                "n_mistos": g["n_mistos"], "n_nulos": g["n_nulos"], "proporcao": "" if p is None else p,
                "ic_inf": ic[0], "ic_sup": ic[1], "rotulo_xy": rot_xy, "marca": marca, "maioria": maioria,
                "certeza": "" if vazia else c["certeza"],
                "certeza_nivel": "" if vazia else CERTEZA_NIVEL[c["certeza"]],
                "certeza_texto": "não julgada" if vazia else c["certeza_texto"],
                "rotulo_marca": {"vazia": "sem estudo", "nulo": "nulo por ±δ"}.get(marca, ""),
                "excluidos_critico": "|".join(c["excluidos_rob_critico"]),
            })
    gravar("dados_celulas.csv", linhas, list(linhas[0]))


# ------------------------------------------------------------------ 5. direção por estudo
def desenho_cod(ch):
    return gtr.desenho_cod(ch)


def rob_nivel(r):
    return ROB_NIVEL[r]


def fig_direcao():
    prin = ler_csv("06-analise/swim_principal/tabelas/swim_direcao.csv")
    amplo = ler_csv("06-analise/swim_sens_com_excluidos_amplo/tabelas/swim_direcao.csv")
    ent = ler_csv("06-analise/swim_entrada_com_excluidos.csv")
    ordem_cel = {tuple(c[k] for k in CHAVE_CEL): i for i, c in
                 enumerate(celulas["celulas"] + celulas["vazias"])}
    linhas = []

    def linha(painel, b, classe, cel_id, rot_cel, ordem_cel_, r, construto, celula):
        d = r["direcao"]
        drot, ital = dir_rotulo(d, construto, celula)
        crit = r["excluido_rob_critico"] == "TRUE"
        return {"painel": painel, "bloco": b, "bloco_rotulo": BLOCO[b][0], "classe": classe,
                "classe_rotulo": CLASSE[classe], "secao": f"{BLOCO[b][0]}, {CLASSE[classe]}",
                "celula_id": cel_id, "rotulo_celula": rot_cel, "ordem_celula": ordem_cel_,
                "chave": r["chave"], "construto": construto, "celula_alvo": celula,
                "direcao": d, "glifo": GLIFO[d], "direcao_rotulo": drot, "italico": int(ital),
                "rob_geral": r["rob_geral"], "rob_rotulo": ROB_ROT[r["rob_geral"]], "rob_nivel": rob_nivel(r["rob_geral"]),
                "excluido_critico": int(crit), "nota": "risco crítico, fora do teste" if crit else "",
                "desenho_fino": desenho_cod(r["chave"]), "regra": r["regra"]}

    vistos = set()
    for r in prin:
        fam, construto, comp, celula, classe = [p.strip() for p in r["grupo"].split("|")]
        k = (fam, construto, comp, celula, classe)
        c = CEL.get(k) or VAZIAS.get(k)
        if c is None:
            sys.exit(f"ERRO: grupo da SWiM principal fora de celulas.json: {k}")
        b = BLOCO_DE_CELULA[(construto, celula)]
        linhas.append(linha("principal", b, classe, c.get("id", "vazia"), rotulo_comparacao(fam, comp), ordem_cel[k],
                            r, construto, celula))
        vistos.add((r["chave"], construto, celula))
    # painel fora da contagem: linhas do agrupamento amplo com efeitos fora da contagem que não estão na principal
    comp_de = collections.defaultdict(set)
    for e in ent:
        if e["modelo_principal"] == "sim":
            comp_de[(e["chave"], e["construto_outcome"], e["celula_alvo"])].add((e["familia_intervencao"], e["comparador_tipo"]))
    for r in amplo:
        construto, celula, classe = [p.strip() for p in r["grupo"].split("|")]
        if (r["chave"], construto, celula) in vistos:
            continue
        b = BLOCO_DE_CELULA[(construto, celula)]
        comps = sorted(comp_de[(r["chave"], construto, celula)])
        if not comps:
            sys.exit(f"ERRO: sem efeito principal em swim_entrada_com_excluidos para {r['chave']} {construto} {celula}")
        rot = "; ".join(rotulo_comparacao(f, c) for f, c in comps)
        linhas.append(linha("fora", b, classe, "", rot, 0, r, construto, celula))

    def chave_ordem(l):
        return (0 if l["painel"] == "principal" else 1, ORDEM_BLOCO.index(l["bloco"]),
                ["randomizado", "nao_randomizado"].index(l["classe"]),
                l["ordem_celula"] if l["painel"] == "principal" else 0, l["rotulo_celula"],
                DESENHO_ORDEM.index(l["desenho_fino"]), l["rob_nivel"], l["chave"].lower())
    linhas.sort(key=chave_ordem)
    for i, l in enumerate(linhas, start=1):
        l["ordem"] = i
    campos = ["ordem", "painel", "bloco", "bloco_rotulo", "classe", "classe_rotulo", "secao", "celula_id",
              "rotulo_celula", "ordem_celula", "chave", "construto", "celula_alvo", "direcao", "glifo",
              "direcao_rotulo", "italico", "rob_geral", "rob_rotulo", "rob_nivel", "excluido_critico", "nota",
              "desenho_fino", "regra"]
    gravar("dados_direcao.csv", linhas, campos)


# ------------------------------------------------------------------ 6. metas exploratórias
ROTULO_EFEITO = {  # subgrupo de efeitos.csv, abreviado (só texto, sem números digitados)
    "Tyszler2015-E01": "opção intermediária de valor baixo",
    "Tyszler2015-E02": "opção intermediária de valor alto",
    "Lammers2022a-E06": "estudo 2a, vinheta heurística",
    "Lammers2022a-E07": "estudo 2a, vinheta de igualdade",
    "Lammers2022a-E08": "estudo 2b, vinheta heurística",
    "Lammers2022a-E09": "estudo 2b, vinheta de igualdade",
}
ROB_GERAL = {(r["chave"], r["construto_outcome"]): r["rob_geral"] for r in ler_csv("04-qualidade/rob_geral.csv")}
METAS = [("a", "06-analise/meta_entrada_exploratoria.csv", "06-analise/meta_exploratoria/meta_resumo.json",
          "Pesquisa × sem pesquisa"),
         ("b", "06-analise/meta_entrada_mesmo_candidato.csv", "06-analise/meta_mesmo_candidato/meta_resumo.json",
          "Mesmo candidato à frente × atrás")]


def fig_metas():
    linhas = []
    for painel, f_ent, f_res, titulo in METAS:
        res = ler_json(f_res)
        if len(res["grupos"]) != 1:
            sys.exit(f"ERRO: {f_res} deveria ter um grupo")
        g = res["grupos"][0]
        r = g["resultado"]
        # ordem por precisão, do menor ao maior erro-padrão (declarada na legenda); empate por chave e efeito
        ent = sorted(ler_csv(f_ent), key=lambda e: (float(e["sei"]), e["chave"].lower(), e["id_efeito"]))
        if {e["chave"] for e in ent} != set(g["estudos"]) or len(ent) != g["k_efeitos"]:
            sys.exit(f"ERRO: entrada {f_ent} não bate com {f_res}")
        n_por = collections.Counter(e["chave"] for e in ent)
        delta = res["parametros"]["delta"]
        for o, e in enumerate(ent, start=1):
            yi, sei = float(e["yi"]), float(e["sei"])
            extra = ""
            if n_por[e["chave"]] > 1:
                if e["id_efeito"] not in ROTULO_EFEITO:
                    sys.exit(f"ERRO: efeito {e['id_efeito']} precisa de rótulo próprio")
                extra = ROTULO_EFEITO[e["id_efeito"]]
            rob = ROB_GERAL.get((e["chave"], e["construto_outcome"]))
            if rob is None or (e.get("rob_geral") and e["rob_geral"] != rob):
                sys.exit(f"ERRO: risco de viés de {e['id_efeito']} ausente ou diferente entre rob_geral.csv e {f_ent}")
            lo, hi = yi - 1.959963984540054 * sei, yi + 1.959963984540054 * sei
            linhas.append({"painel": painel, "painel_titulo": titulo, "ordem": o, "tipo": "efeito", "chave": e["chave"],
                           "id_efeito": e["id_efeito"], "rotulo_extra": extra, "estimativa": yi, "ep": sei,
                           "ic_inf": lo, "ic_sup": hi, "rotulo_valor": f"{dec_br(yi)} ({dec_br(lo)} a {dec_br(hi)})",
                           "rob_geral": rob, "delta": delta, "k_estudos": g["k_estudos"], "k_efeitos": g["k_efeitos"]})
        linhas.append({"painel": painel, "painel_titulo": titulo, "ordem": len(ent) + 1, "tipo": "combinado",
                       "chave": "", "id_efeito": "", "rotulo_extra": "", "estimativa": r["estimativa"], "ep": r["ep"],
                       "ic_inf": r["ic"][0], "ic_sup": r["ic"][1],
                       "rotulo_valor": f"{dec_br(r['estimativa'])} ({dec_br(r['ic'][0])} a {dec_br(r['ic'][1])})",
                       "rob_geral": "", "delta": delta, "k_estudos": g["k_estudos"], "k_efeitos": g["k_efeitos"]})
    gravar("dados_metas.csv", linhas, list(linhas[0]))


# ------------------------------------------------------------------ 7. realismo
REAL_ROT = {"hipotetico": "hipotético", "induzido": "induzido", "real": "real"}
DESFECHO_T = {"T9": ("apoio_ao_lider", {"principal"}, "Apoio a quem aparece à frente (célula principal)"),
              "T14": ("mobilizacao", None, "Comparecimento")}


def fig_realismo():
    linhas = []
    for tab, (construto, cels, rot) in DESFECHO_T.items():
        for ch, ds in sorted(cmm.dirs.items()):
            for (c, ce, classe, d) in ds:
                if c != construto or (cels and ce not in cels):
                    continue
                nivel = cmm.norm(M[ch]["realismo_contexto"])
                direcao = d.split(" ")[0]
                crit = "crítico" in d
                drot, ital = dir_rotulo(direcao, construto, ce)
                linhas.append({"tabela": tab, "desfecho": construto, "desfecho_rotulo": rot, "classe": classe,
                               "classe_rotulo": CLASSE[classe], "realismo": nivel, "realismo_rotulo": REAL_ROT[nivel],
                               "chave": ch, "celula_alvo": ce, "direcao": direcao, "glifo": GLIFO[direcao],
                               "direcao_rotulo": drot, "italico": int(ital), "excluido_critico": int(crit)})
    ordem_dir = ["benefico", "misto", "nulo", "danoso"]
    linhas.sort(key=lambda l: (l["tabela"] != "T9", l["classe"] != "randomizado", l["realismo"],
                               l["excluido_critico"], ordem_dir.index(l["direcao"]), l["chave"].lower()))
    gravar("dados_realismo.csv", linhas, list(linhas[0]))


if __name__ == "__main__":
    fig_modelo_logico()
    fig_prisma()
    fig_rob()
    fig_celulas()
    fig_direcao()
    fig_metas()
    fig_realismo()
