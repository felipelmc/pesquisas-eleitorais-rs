"""Monta 09-documento-final/revisao_final.qmd a partir do esqueleto redigido à mão.

O texto corrido está em 09-documento-final/_esqueleto_revisao_final.qmd (do redator; este script não o altera).
Cada linha que contém só um marcador é trocada pelo conteúdo gerado dos arquivos do projeto, sem digitar números:

  @@FIGURA <nome>@@   ![legenda](revista/figuras/saida/<nome>){#fig-... fig-alt="..."}, com legenda e texto
                      alternativo de revista/figuras/legendas.yml (marcadores {arquivo:caminho} resolvidos lendo os
                      JSON e CSV; ver resolver_marcadores). `largura: larga` envolve a figura em ::: {.figura-larga}.
                      O arquivo sai sem extensão: o Typst usa o .svg (default-image-extension em revista/_revista.yml)
                      e o HTML e o .docx devem usar o .png. O script exige os dois em revista/figuras/saida/.
  @@TABELA <nome>@@   tabela com legenda e rótulo, conforme revista/rotulos.yml:
    caracteristicas   Tab. 1  características agregadas dos 41 estudos (n e %), de insumos/tabelas/numeros.json
                              pela entrada tab1_caracteristicas de revista/numeros_v2.json
    sof               Tab. 2  resumo dos achados (SoF narrativa) em 4 blocos, de revista/celulas.json,
                              06-analise/certeza.csv e swim_resumo.json (via celulas.json); n e unidade por estudo da
                              entrada sof_n_por_estudo de numeros_v2.json; envolvida em ::: {.landscape}
    hipoteses         Tab. 3  hipóteses do protocolo × evidência × certeza, de revista/tabelas/hipoteses.yml;
                              envolvida em ::: {.tabela-larga}
    oqf_principal     Tab. 4  caixa OQF da pergunta principal: prosa em revista/tabelas/oqf_principal.yml, números de
                              insumos/tabelas/numeros.json, 06-analise/caixa_ferramentas.csv e insumos/caixa_oqf.json
    transferibilidade Tab. 5  fatores de transferibilidade, de revista/tabelas/transferibilidade.yml e das entradas
                              transf_* de numeros_v2.json
    pendencias        Apêndice A  pendências de 07-relatorio/_pendencias_abertas.json, com etapa, tarefa, pacote e
                              esforço da tabela de 08-revisao-humana/README.md
  Continuam disponíveis, fora do contrato de rótulos atual: swim, regional, caixa_celulas e mecanismos.

  Tabelas 1 e 2 em "grid table" do Pandoc (grade_md), e não em tabela pipe: só a grid table tem célula que ocupa
  várias colunas, e o Pandoc a leva ao Typst (table.cell(colspan: n)), ao HTML (colspan) e ao .docx (gridSpan) sem
  código próprio de formato. Assim, as linhas de grupo ("Desenho", "Apoio a quem aparece à frente"...) ocupam a
  largura toda, em vez de ficarem presas à primeira coluna. O Quarto não aplica tbl-colwidths a tabela com colspan;
  a largura de cada coluna vem do número de traços da grade (grade_md). Cada célula fica numa linha do fonte (a
  trava conferir_reestruturacao.py lê o span .enunciado, a certeza e o k na mesma linha), exceto a de certeza da Tab. 2,
  que tem quebra de linha fixa entre os símbolos ⊕ e a palavra (duas linhas, com barra invertida no fim da primeira).
  Na Tab. 2: as notas de rodapé entram como última linha da tabela, ocupando as seis colunas, e por isso saem no
  corpo da tabela (sans 7,6 pt no Typst); um bloco Typst cru (```{=typst}```, ignorado no HTML e no .docx) abre um
  escopo #[ ... ] só em volta dela, com inset e entrelinha menores; a coluna Estudos cita cada estudo na forma
  narrativa (@chave, n = x unidade), com o n fora da citação e sempre no mesmo formato; os enunciados levam
  *bandwagon*, *underdog* e *momentum* em itálico (o texto, sem a ênfase, continua igual ao de certeza.csv).

Metadados: no YAML do revisao_final.qmd montado (não no esqueleto), o script grava `pendencias-abertas: <n>` (de
07-relatorio/_pendencias_abertas.json), `rascunho: true` se n > 0 e revista/_revista.yml não declarar `estado: final`, e `nocite` com todas as chaves de
07-relatorio/incluidos.csv, para que a desambiguação de citeproc ("2021a/b") seja a mesma do suplemento, das figuras
e de revista/rotulos_autor_ano.json.

Checagens (sai com erro): marcador ou "@@" que sobrar; figura sem .svg ou .png em revista/figuras/saida/; rótulo
{#fig-/#tbl-/#qdr-} do texto montado fora de revista/rotulos.yml; marcador de legenda que não resolve.

USO (de qualquer pasta):
  python3 09-documento-final/montar_revisao_final.py [--esqueleto E] [--saida S] [--legendas L]
  python3 09-documento-final/montar_revisao_final.py --previas [nome ...]
      grava revista/tabelas/previa_<nome>.md para cada tabela (todas, sem nomes) e não monta o artigo
Só lê arquivos do projeto e só escreve o .qmd montado (ou as prévias).
"""
import argparse
import csv
import importlib.util
import json
import os
import re
import sys
import unicodedata
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import yaml

R = Path(__file__).resolve().parents[1]
D = R / "09-documento-final"
INS = D / "insumos"
REV = D / "revista"
TAB = REV / "tabelas"
FIG_SAIDA = REV / "figuras/saida"
LEGENDAS = REV / "figuras/legendas.yml"
ROTULOS = yaml.safe_load((REV / "rotulos.yml").read_text(encoding="utf-8"))


def ler(p):
    return Path(p).read_text(encoding="utf-8").rstrip("\n")


def ljson(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def lcsv(p):
    return list(csv.DictReader(open(p, encoding="utf-8-sig")))


def lyaml(p):
    return yaml.safe_load(Path(p).read_text(encoding="utf-8"))


def chaves_bib():
    ks = set()
    for bib in (R / "07-relatorio/references.bib", D / "referencias_contexto.bib", D / "referencias_metodo.bib",
                D / "referencias_excluidos.bib"):
        if bib.exists():
            ks |= set(re.findall(r"^@\w+\{([^,]+),", ler(bib), flags=re.M))
    return ks


CHAVES = chaves_bib()


def citar(texto):
    """Troca chaves de estudo soltas (ex.: Gerber2020a) por @chave, sem mexer nas que já têm @."""
    for k in sorted(CHAVES, key=len, reverse=True):
        texto = re.sub(rf"(?<![@\w]){re.escape(k)}(?![\w-])", "@" + k, texto)
    return texto


def meio_para_cima(x, casas=2):
    """Arredonda com `casas` decimais, meio para cima, sobre a representação decimal curta do float (repr): 0,975 vira
    0,98. O f-string arredonda o binário (0,97499...) e daria 0,97, e o limite inferior 0,025 já dava 0,03. Zero sai
    sem sinal (nunca "−0,00")."""
    d = Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-casas), rounding=ROUND_HALF_UP)
    return d.copy_abs() if d.is_zero() else d


def virgula(x, casas=2):
    return f"{meio_para_cima(x, casas):.{casas}f}".replace(".", ",")


def pt(x, casas=2):
    """Número em pt-BR: vírgula decimal, ponto de milhar e sinal de menos U+2212. Decimais arredondados meio para cima
    (meio_para_cima), em toda proporção, IC e marcador que passa por aqui."""
    if isinstance(x, bool):
        return str(x)
    if isinstance(x, int):
        s = f"{x:,}".replace(",", ".")
    else:
        s = f"{meio_para_cima(x, casas):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s.replace("-", "−")


def uma_linha(s):
    return re.sub(r"\s+", " ", str(s)).strip()


def celula(s):
    """Texto seguro para célula de tabela pipe."""
    return uma_linha(s).replace("|", "/")


def pipe(cab, linhas):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for l in linhas:
        out.append("| " + " | ".join(celula(x) for x in l) + " |")
    return "\n".join(out)


def largura_txt(s):
    """Largura de exibição de um texto, como o Pandoc a mede ao ler grid tables (biblioteca doclayout): caractere
    combinante vale 0, caractere largo do leste asiático (W, F) vale 2, os demais (inclusive ⊕, ◯, ±, δ), 1."""
    return sum(0 if unicodedata.combining(ch) else 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
               for ch in s)


def grade_md(cab, linhas, larguras):
    """Grid table do Pandoc. `linhas`: lista em que cada item é uma lista de células (cada célula é um texto ou uma
    lista de textos, um por linha do fonte) ou um texto solto, que vira uma linha de uma célula só ocupando todas as
    colunas (colspan). `larguras`: proporção de cada coluna (em %). O Quarto não aplica tbl-colwidths a tabela com
    célula que ocupa várias colunas (modules/tablecolwidths.lua, is_simple); as larguras vêm então da própria grade:
    o Pandoc dá a cada coluna (traços + 1) / largura total da linha. Por isso o número de traços de cada coluna é
    proporcional a `larguras`, numa escala em que toda célula e toda linha de colspan cabem numa linha do fonte."""
    n = len(cab)
    if len(larguras) != n:
        raise SystemExit(f"ERRO: {len(larguras)} larguras para {n} colunas")
    norm = []
    for l in linhas:
        if isinstance(l, str):
            norm.append(celula(l))
        else:
            if len(l) != n:
                raise SystemExit(f"ERRO: linha de tabela com {len(l)} células; esperado {n}")
            norm.append([[celula(x)] if isinstance(x, str) else [celula(y) for y in x] for x in l])
    minimo = [max(3, largura_txt(celula(c))) for c in cab]
    for l in norm:
        if not isinstance(l, str):
            for j, c in enumerate(l):
                minimo[j] = max(minimo[j], *(largura_txt(x) for x in c))
    span = max([largura_txt(l) for l in norm if isinstance(l, str)] or [0])
    # coluna j ocupa c_j = larg_j + 3 caracteres (conteúdo, dois espaços e um separador); c_j proporcional a larguras
    escala = max([(m + 3) / p for m, p in zip(minimo, larguras)] + [(span + 3 + n) / sum(larguras), 80 / sum(larguras)])
    larg = [max(m, round(escala * p) - 3) for m, p in zip(minimo, larguras)]
    interna = sum(larg) + 3 * (n - 1)
    if span > interna:
        raise SystemExit("ERRO: linha de colspan mais longa que a tabela (grade_md)")

    def pad(s, w):
        return s + " " * (w - largura_txt(s))

    def sep(ch="-"):
        return "+" + "+".join(ch * (w + 2) for w in larg) + "+"

    out = [sep(), "| " + " | ".join(pad(celula(c), w) for c, w in zip(cab, larg)) + " |", sep("=")]
    for l in norm:
        if isinstance(l, str):
            out.append("| " + pad(l, interna) + " |")
        else:
            altura = max(len(c) for c in l)
            for i in range(altura):
                out.append("| " + " | ".join(pad(c[i] if i < len(c) else "", w) for c, w in zip(l, larg)) + " |")
        out.append(sep())
    return "\n".join(out)


ESTRANGEIRAS_ENUNCIADO = r"[Bb]andwagon|[Uu]nderdog|[Mm]omentum"


def italico_estrangeiras(texto):
    """Põe *bandwagon*, *underdog* e *momentum* em itálico (só as ocorrências ainda sem ênfase)."""
    return re.sub(rf"(?<![*\w])({ESTRANGEIRAS_ENUNCIADO})(?![*\w])", r"*\1*", texto)


_GT = None


def gt():
    """07-relatorio/gerar_tabelas_relatorio.py importado por caminho (dir_rot, rebaix, num). O módulo lê arquivos
    relativos à raiz ao ser importado; por isso a pasta de trabalho muda só durante a importação."""
    global _GT
    if _GT is None:
        cwd = os.getcwd()
        sys.dont_write_bytecode = True
        os.chdir(R)
        try:
            spec = importlib.util.spec_from_file_location("gerar_tabelas_relatorio",
                                                          R / "07-relatorio/gerar_tabelas_relatorio.py")
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
        finally:
            os.chdir(cwd)
        _GT = mod
    return _GT


# ================================================================ marcadores {arquivo:caminho}
ALIASES = {
    # alias: (arquivo relativo à raiz, subcaminho inicial ou None)
    "num": ("09-documento-final/insumos/tabelas/numeros.json", None),
    "numeros": ("09-documento-final/insumos/tabelas/numeros.json", None),
    "nv2": ("09-documento-final/revista/numeros_v2.json", None),
    "numeros_v2": ("09-documento-final/revista/numeros_v2.json", None),
    "celulas": ("09-documento-final/revista/celulas.json", None),
    "meta": ("09-documento-final/insumos/tabelas/numeros.json", "meta"),
    "meta_mesmo_candidato": ("09-documento-final/insumos/tabelas/numeros.json", "meta_mesmo_candidato"),
    "meta_resumo": ("06-analise/meta_exploratoria/meta_resumo.json", None),
    "meta_exploratoria": ("06-analise/meta_exploratoria/meta_resumo.json", None),
    "meta_resumo_mesmo_candidato": ("06-analise/meta_mesmo_candidato/meta_resumo.json", None),
    "meta_mesmo_candidato_resumo": ("06-analise/meta_mesmo_candidato/meta_resumo.json", None),
    "swim": ("06-analise/swim_principal/swim_resumo.json", None),
    "swim_resumo": ("06-analise/swim_principal/swim_resumo.json", None),
    "prisma": ("07-relatorio/prisma_contagens.json", None),
    "prisma_contagens": ("07-relatorio/prisma_contagens.json", None),
    "pendencias": ("07-relatorio/_pendencias_abertas.json", None),
    "certeza": ("06-analise/certeza.csv", None),
    "caixa_oqf": ("09-documento-final/insumos/caixa_oqf.json", None),
}
RX_MARCADOR = re.compile(r"\{(\w[\w./-]*):([^{}\s|]+)(?:\|(\d))?\}")
_CACHE_ARQ = {}


def _arquivo(rel, bases):
    for b in bases:
        p = (b / rel).resolve()
        if p.exists():
            return p
    raise KeyError(f"arquivo não encontrado: {rel}")


def _carregar(p):
    if p not in _CACHE_ARQ:
        _CACHE_ARQ[p] = lcsv(p) if p.suffix == ".csv" else ljson(p)
    return _CACHE_ARQ[p]


def _navegar(obj, caminho):
    if not caminho:
        return obj
    for parte in caminho.split("."):
        if isinstance(obj, list):
            if re.fullmatch(r"-?\d+", parte):
                obj = obj[int(parte)]
            elif "=" in parte:  # seletor col=valor[&col2=valor2] em lista de dicts (CSV)
                conds = [c.split("=", 1) for c in parte.split("&")]
                achados = [x for x in obj if all(str(x.get(k)) == v for k, v in conds)]
                if len(achados) != 1:
                    raise KeyError(f"seletor {parte!r} achou {len(achados)} linhas")
                obj = achados[0]
            else:
                raise KeyError(f"{parte!r} não indexa lista")
        elif isinstance(obj, dict):
            if parte not in obj:
                raise KeyError(f"chave {parte!r} ausente")
            obj = obj[parte]
        else:
            raise KeyError(f"{parte!r}: valor não navegável")
    return obj


def formatar(v, casas=None):
    if isinstance(v, dict) and "formatado" in v:  # entrada de numeros_v2.json
        return v["formatado"]
    if isinstance(v, bool) or v is None:
        raise KeyError(f"valor não imprimível: {v!r}")
    if isinstance(v, int):
        return pt(v)
    if isinstance(v, float):
        if casas is None and v.is_integer():
            return pt(int(v))
        return pt(v, 2 if casas is None else casas)
    if isinstance(v, str):
        if casas is not None:
            try:
                return pt(float(v.replace("−", "-").replace(",", ".")), casas)
            except ValueError:
                pass
        return v
    raise KeyError(f"valor não imprimível: {type(v).__name__}")


def resolver_marcadores(texto, aliases=None, bases=None, calc=None, onde=""):
    """Troca marcadores {arquivo:caminho} e {arquivo:caminho|n} pelo valor lido do arquivo.
    - arquivo: um alias (ALIASES, mais os do próprio YAML de legendas) ou um caminho .json/.csv relativo à raiz, a
      09-documento-final/ ou à pasta do YAML; `calc` e `nv2cit` são especiais (valores calculados pelo montador e
      chaves de uma entrada de numeros_v2.json como citação [@a; @b]).
    - caminho: partes separadas por ponto; números indexam listas; em CSV, `col=valor` (ou `col=v&col2=w`) escolhe a
      linha. Uma entrada de numeros_v2.json (com `formatado`) imprime o formatado.
    - |n: casas decimais (sem isso, float sai com 2 casas; inteiro, com ponto de milhar; string, como está).
    """
    aliases = {**ALIASES, **(aliases or {})}
    bases = bases or [R, D]
    calc = calc or {}

    def troca(m):
        alias, caminho, casas = m.group(1), m.group(2), m.group(3)
        casas = int(casas) if casas is not None else None
        try:
            if alias == "calc":
                return str(calc[caminho])
            if alias == "nv2cit":
                chaves = ljson(REV / "numeros_v2.json")[caminho]["chaves"]
                return "[" + "; ".join("@" + k for k in chaves) + "]" if chaves else "(nenhum)"
            if alias in aliases:
                rel, sub = aliases[alias]
                obj = _navegar(_carregar(_arquivo(rel, bases)), sub)
            elif re.search(r"\.(json|csv)$", alias):
                obj = _carregar(_arquivo(alias, bases))
            else:
                raise KeyError(f"alias desconhecido: {alias}")
            return formatar(_navegar(obj, caminho), casas)
        except (KeyError, IndexError) as e:
            raise SystemExit(f"ERRO: marcador {m.group(0)} em {onde or 'texto'} não resolve: {e}")
    saida = RX_MARCADOR.sub(troca, texto)
    sobra = re.findall(r"\{\w[\w./-]*:[^{}\s]*\}", saida)
    if sobra:
        raise SystemExit(f"ERRO: marcador não resolvido em {onde or 'texto'}: {sobra}")
    return saida


# ================================================================ figuras
def aliases_do_yaml(leg):
    for chave in ("_arquivos", "arquivos", "_fontes", "fontes", "_aliases", "aliases"):
        v = leg.get(chave) if isinstance(leg, dict) else None
        if isinstance(v, dict):
            # aceita alias: caminho  ou  alias: {arquivo: caminho, base: prefixo}
            return {k: ((str(p["arquivo"]), p.get("base")) if isinstance(p, dict) else (str(p), None))
                    for k, p in v.items()}
    return {}


def figura(nome, legendas_path=LEGENDAS, exigir_arquivos=True):
    """Imagem com legenda e rótulo. exigir_arquivos=False (uso de revista/gerar_rotulos_autor_ano.py, que roda antes
    das figuras) não confere se o .svg e o .png existem; o texto sai igual."""
    if not Path(legendas_path).exists():
        raise SystemExit(f"ERRO: {Path(legendas_path).relative_to(R) if Path(legendas_path).is_relative_to(R) else legendas_path} "
                         f"não existe; as legendas das figuras são escritas pelo programador das figuras "
                         f"(revista/figuras/legendas.yml) antes da montagem")
    leg = lyaml(legendas_path) or {}
    figs = ROTULOS.get("figuras") or {}
    if nome not in figs:
        raise SystemExit(f"ERRO: figura {nome!r} não está em revista/rotulos.yml")
    if nome not in leg or not isinstance(leg[nome], dict):
        raise SystemExit(f"ERRO: figura {nome!r} sem entrada em {Path(legendas_path).name}")
    for ext in ("svg", "png"):
        if exigir_arquivos and not (FIG_SAIDA / f"{nome}.{ext}").exists():
            raise SystemExit(f"ERRO: revista/figuras/saida/{nome}.{ext} não existe")
    e = leg[nome]
    if not e.get("legenda") or not e.get("alt"):
        raise SystemExit(f"ERRO: figura {nome!r} sem legenda ou sem alt em {Path(legendas_path).name}")
    al = aliases_do_yaml(leg)
    bases = [R, D, Path(legendas_path).parent]
    legenda = uma_linha(resolver_marcadores(str(e["legenda"]), al, bases, onde=f"legenda de {nome}"))
    alt = uma_linha(resolver_marcadores(str(e["alt"]), al, bases, onde=f"alt de {nome}"))
    alt = re.sub(r'"([^"]*)"', "“\\1”", alt).replace('"', "”")
    img = f'![{legenda}](revista/figuras/saida/{nome}){{#{figs[nome]} fig-alt="{alt}"}}'
    if str(e.get("largura", "texto")).strip() == "larga":
        return "::: {.figura-larga}\n\n" + img + "\n\n:::"
    return img


# ================================================================ tabelas antigas (fora do contrato atual)
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


# ================================================================ Tab. 1: características
ROT_TAB1 = {
    "desenho": ("Desenho", {
        "survey_experiment": "experimento de *survey*", "lab_preferencias_induzidas": "laboratório, preferências induzidas",
        "experimento_natural": "experimento natural", "lab_candidatos_reais": "laboratório, candidatos reais",
        "painel_individual": "painel individual", "experimento_campo": "experimento de campo",
        "outro": "outros desenhos"}),
    "familia": ("Formato da exposição", {
        "pesquisa_pre_eleitoral": "pesquisa pré-eleitoral", "agregador_projecao": "agregador ou projeção",
        "boca_de_urna": "boca de urna antes do fechamento", "apuracao_parcial": "apuração parcial oficial"}),
    "realismo": ("Realismo do contexto", {
        "real": "eleição real", "induzido": "preferências induzidas em laboratório",
        "hipotetico": "eleição hipotética (vinheta)"}),
    "regiao": ("Região", {
        "outro": "fora da América Latina", "brasil": "Brasil", "america_latina": "América Latina (sem o Brasil)",
        "america_latina + brasil + outro": "multinacional, com Brasil e América Latina", "999": "não informada"}),
    "eleicao": ("Tipo de eleição", {
        "candidato_partido": "candidatos ou partidos", "simulada_abstrata": "simulada, abstrata",
        "referendo": "referendo"}),
    "construto": ("Desfechos extraídos", {
        "apoio_ao_lider": "só apoio a quem aparece à frente", "mobilizacao": "só comparecimento",
        "apoio_ao_lider + mobilizacao": "os dois"}),
    "periodo": ("Ano de publicação (relato principal)", {}),
    "rob_rob2": ("Risco de viés geral, RoB 2 ({den} resultados randomizados)", {
        "algumas_preocupacoes": "algumas preocupações", "alto": "alto", "baixo": "baixo"}),
    "rob_robins_i": ("Risco de viés geral, ROBINS-I V2 ({den} resultados)", {
        "moderado": "moderado", "grave": "grave", "critico": "crítico", "baixo": "baixo"}),
    "rob_epoc": ("Risco de viés geral, EPOC ({den} resultados)", {
        "alto": "alto", "baixo": "baixo", "incerto": "incerto"}),
}


def t_caracteristicas():
    ent = ljson(REV / "numeros_v2.json")["tab1_caracteristicas"]
    num = ljson(INS / "tabelas/numeros.json")
    linhas, grupo_atual = [], None
    ordem_grupo = list(ROT_TAB1)
    def chave(l):  # grupos na ordem de ROT_TAB1; dentro do grupo, n decrescente e, no empate, a ordem dos rótulos
        rot = list(ROT_TAB1[l["grupo"]][1])
        return (ordem_grupo.index(l["grupo"]), -l["n"] if l["grupo"] != "periodo" else 0,
                rot.index(l["codigo"]) if l["codigo"] in rot else 0, l["codigo"])
    for l in sorted(ent["linhas"], key=chave):
        g = l["grupo"]
        titulo, rot = ROT_TAB1[g]
        if g != grupo_atual:
            linhas.append(f"**{titulo.format(den=l['denominador'])}**")  # linha de grupo, nas duas colunas
            grupo_atual = g
        if g == "periodo":
            a, b = l["codigo"].split("-")
            nome = f"{a} a {b}"
        else:
            if l["codigo"] not in rot:
                raise SystemExit(f"ERRO: Tab. 1 sem rótulo para {g} = {l['codigo']!r}")
            nome = rot[l["codigo"]]
        linhas.append([f" {nome}", f"{l['n']} ({pt(l['pct'], 1)})"])
    leg = (f"Características dos {num['estudos']} estudos incluídos. n (%) de estudos; no risco de viés, n (%) de "
           f"resultados avaliados com cada ferramenta ({num['rob_resultados']} resultados de {num['rob_estudos']} "
           "estudos; os julgamentos de IA não foram validados por humano). \"Outros desenhos\": painel de distritos, "
           "campanha simulada, corte transversal de países, desenho múltiplo e *rolling cross-section*. "
           "Estudo a estudo nos Apêndices C e D.")
    # só no Typst: a tabela (menos de uma página) flutua para o alto ou o pé da página em que cabe inteira, e o texto
    # preenche o resto; assim nenhuma linha de grupo fica sozinha no pé da página, separada das suas linhas
    # (a figura flutuante sai centrada no Typst; o show rule devolve as células à esquerda, como nas outras tabelas)
    abre = "```{=typst}\n#[\n#set figure(placement: auto)\n#show table: set align(left)\n```"
    fecha = "```{=typst}\n]\n```"
    return (abre + "\n\n" + grade_md(["Característica", "n (%)"], linhas, [72, 28])
            + f"\n\n: {leg} {{#{ROTULOS['tabelas']['caracteristicas']}}}\n\n" + fecha)


# ================================================================ Tab. 2: SoF
BLOCOS_SOF = [("apoio_principal", "Apoio a quem aparece à frente"),
              ("viabilidade", "Viabilidade: apoio à opção mostrada como viável"),
              ("momentum", "*Momentum*: partido mostrado ganhando ou perdendo apoio"),
              ("mobilizacao", "Comparecimento")]
FAM_SOF = {"pesquisa_pre_eleitoral": "Pesquisa pré-eleitoral", "agregador_projecao": "Agregador ou projeção",
           "boca_de_urna": "Boca de urna antes do fechamento das urnas", "outro": "Apuração parcial oficial"}
COMP_SOF = {"sem_pesquisa": "frente a nenhuma pesquisa",
            "mesmo_candidato_atras": "candidato mostrado à frente, frente ao mesmo candidato mostrado atrás",
            "outro_resultado": "frente a outro resultado de pesquisa",
            "outro": "frente a outra apresentação do resultado",
            "antes_depois_proibicao": "antes e depois da proibição",
            "unidades_nao_expostas": "unidades expostas frente a não expostas"}
DES_SOF = {"randomizado": "randomizados", "nao_randomizado": "não randomizados"}
GRADE = {"muito_baixa": "⊕◯◯◯", "baixa": "⊕⊕◯◯", "moderada": "⊕⊕⊕◯", "alta": "⊕⊕⊕⊕"}
NIVEL_TXT = {"muito_baixa": "muito baixa", "baixa": "baixa", "moderada": "moderada", "alta": "alta"}
DOMINIOS_SOF = ["risco de viés", "inconsistência", "indireção", "imprecisão", "viés de publicação"]
EXPLICA_DOMINIO = {
    "risco de viés": "por risco de viés nos estudos da célula (RoB 2, ROBINS-I V2 ou EPOC)",
    "inconsistência": "por inconsistência entre os estudos na direção",
    "indireção": "por indireção (realismo do contexto, tipo de eleição, contraste ou estimando; protocolo, seção 9)",
    "imprecisão": "por imprecisão (poucos estudos, IC da proporção largo ou efeitos frente a ±δ)",
    "viés de publicação": "por suspeita de viés de publicação",
}


def grade(nivel):
    return f"[{GRADE[nivel]}]{{.grade}} {NIVEL_TXT[nivel]}"


def grade_quebrada(nivel):
    """Célula de certeza da Tab. 2 em duas linhas do fonte: símbolos, quebra de linha fixa (barra invertida no fim da
    linha) e a palavra. A palavra nunca divide a linha com os símbolos nem é hifenizada ao lado deles."""
    return [f"[{GRADE[nivel]}]{{.grade}}\\", NIVEL_TXT[nivel]]


def frase_direcao(c):
    g = gt()
    constr, alvo = c["construto_outcome"], c["celula_alvo"]
    pos, neg = g.dir_rot("benefico", constr, alvo), g.dir_rot("danoso", constr, alvo)
    tipo = "mobilizacao" if constr == "mobilizacao" else alvo
    pos_txt = {"principal": f"na direção {pos}", "viabilidade": f"na direção de {pos}",
               "momentum": pos, "mobilizacao": f"na direção de {pos}"}[tipo]
    neg_txt = {"principal": neg, "viabilidade": neg, "momentum": neg, "mobilizacao": f"de {neg}"}[tipo]
    y = c["n_estudos_com_direcao"]
    if y == 0:
        partes = ["nenhum estudo com direção definida"]
    else:
        partes = [f"{c['n_beneficos']} de {y} {pos_txt}" + (f", {c['n_danosos']} {neg_txt}" if c["n_danosos"] else "")]
    if c["n_mistos"]:
        partes.append(f"{c['n_mistos']} misto" + ("s" if c["n_mistos"] > 1 else ""))
    if c["n_nulos"]:
        partes.append(f"{c['n_nulos']} nulo" + ("s" if c["n_nulos"] > 1 else "") + " por ±δ")
    if c.get("n_sem_direcao"):
        partes.append(f"{c['n_sem_direcao']} sem direção")
    txt = "; ".join(partes)
    if c["proporcao"] is not None and c["ic_proporcao"]:
        lo, hi = c["ic_proporcao"]
        txt += f" (proporção {pt(float(c['proporcao']))}; IC 95% {pt(float(lo))} a {pt(float(hi))})"
    return txt


def estudos_sof(cid, n_por_celula):
    """k e, por estudo, a citação narrativa seguida do n, sempre no formato "@chave, n = x unidade" (ou "n não
    relatado"): o n fica fora da citação e não entra no link."""
    k = len(n_por_celula[cid])
    partes = []
    for e in n_por_celula[cid]:
        if e["n"] is None:
            partes.append(f"@{e['chave']}, n não relatado")
        else:
            partes.append(f"@{e['chave']}, n = {pt(e['n'])}" + (f" {e['unidade']}" if e["unidade"] else ""))
    return f"{k} estudo{'s' if k > 1 else ''}: " + "; ".join(partes)


def rebaixamentos(justificativa):
    """(lista de (domínio, níveis), partida) a partir da rebaix() de gerar_tabelas_relatorio.py."""
    txt = gt().rebaix(justificativa)
    m = re.search(r"\(partida (\w+)\)\s*$", txt)
    partida = m.group(1) if m else "NR"
    corpo = re.sub(r"\s*\(partida \w+\)\s*$", "", txt)
    regs = []
    if corpo != "nenhum":
        for parte in corpo.split("; "):
            mm = re.fullmatch(r"(.+) −(\d)", parte.strip())
            if not mm or mm.group(1) not in DOMINIOS_SOF:
                raise SystemExit(f"ERRO: rebaixamento fora do padrão: {parte!r}")
            regs.append((mm.group(1), int(mm.group(2))))
    return regs, partida


def t_sof():
    cel = ljson(REV / "celulas.json")
    celulas = cel["celulas"]
    n_por_celula = ljson(REV / "numeros_v2.json")["sof_n_por_estudo"]["por_celula"]
    cert = {tuple(r[k] for k in cel["chave"]): r for r in lcsv(R / "06-analise/certeza.csv")}
    # letras: uma por (domínio, níveis) e uma para o ponto de partida baixo, em ordem fixa
    por_cel, usados = {}, set()
    for c in celulas:
        regs, partida = rebaixamentos(cert[tuple(c[k] for k in cel["chave"])]["justificativa"])
        itens = [("dom", d, n) for d, n in regs] + ([("partida", "baixa", 0)] if partida == "baixa" else [])
        por_cel[c["id"]] = itens
        usados |= set(itens)
    ordem = sorted(usados, key=lambda x: (x[0] == "partida", DOMINIOS_SOF.index(x[1]) if x[0] == "dom" else 0, x[2]))
    letra = {it: "abcdefghijklmnopqrstuvwxyz"[i] for i, it in enumerate(ordem)}

    cab = ["Comparação e desenho", "Estudos (k; n do efeito principal)", "Direção (x de y com direção definida)",
           "Certeza", "O que a evidência diz", "Notas"]
    linhas = []
    for bloco, titulo in BLOCOS_SOF:
        cs = [c for c in celulas if c["bloco"] == bloco]
        if not cs:
            continue
        linhas.append(f"**{titulo}**")  # linha de grupo, nas seis colunas
        for c in cs:
            comp = f"{FAM_SOF[c['familia_intervencao']]}, {COMP_SOF[c['comparador_tipo']]} ({DES_SOF[c['classe_desenho']]})"
            notas = ", ".join(letra[it] for it in sorted(por_cel[c["id"]], key=lambda it: letra[it]))
            linhas.append([comp, estudos_sof(c["id"], n_por_celula), frase_direcao(c), grade_quebrada(c["certeza"]),
                           f"[{italico_estrangeiras(uma_linha(c['enunciado']))}]{{.enunciado cel=\"{c['id']}\"}}",
                           notas or "n.a."])
    notas_txt = []
    for it in ordem:
        if it[0] == "partida":
            notas_txt.append(f"*{letra[it]}* Ponto de partida baixo: corpo de evidência avaliado com a ferramenta "
                             "EPOC (protocolo, seção 9); nas demais células, alto.")
        else:
            _, dom, n = it
            notas_txt.append(f"*{letra[it]}* Rebaixada {n} níve{'l' if n == 1 else 'is'} {EXPLICA_DOMINIO[dom]}.")
    vazias = cel.get("vazias", [])
    extra = ""
    if vazias:
        crit = sorted({e for v in vazias for e in v.get("excluidos_rob_critico", [])})
        extra = (f" {len(vazias)} célula prevista ficou sem estudo na análise principal (agregador ou projeção, "
                 f"comparecimento, frente a nenhuma pesquisa, não randomizados), porque o único estudo "
                 f"[{'; '.join('@' + k for k in crit)}] está em risco de viés crítico; ela não foi julgada."
                 if len(vazias) == 1 else f" {len(vazias)} células previstas ficaram sem estudo e não foram julgadas.")
    leg = ("Resumo dos achados por célula da síntese principal (SWiM, sem os estudos em risco de viés crítico). "
           "Direção: x de y = estudos na direção indicada entre os y que têm direção definida; estudos mistos e nulos "
           "por ±δ ficam fora do denominador; proporção com IC 95% de Clopper-Pearson. Certeza GRADE: ⊕⊕⊕⊕ alta, "
           "⊕⊕⊕◯ moderada, ⊕⊕◯◯ baixa, ⊕◯◯◯ muito baixa; ela qualifica a direção, não a magnitude, e foi julgada "
           "só por IA, sem validação humana. n na unidade de cada estudo, quando a unidade está registrada; os n não são somados. "
           "O agrupamento amplo, decidido depois de ver os dados, fica fora desta tabela (Apêndice F).")
    linhas.append("*Notas.* " + " ".join(notas_txt) + extra)  # notas na última linha, nas seis colunas
    tabela = grade_md(cab, linhas, [15, 18, 17, 9, 33, 8])
    rot = ROTULOS["tabelas"]["sof"]
    # só no Typst: escopo #[ ... ] em volta da tabela, com inset e entrelinha menores (as notas cabem na página)
    abre = ("```{=typst}\n#[\n#set table(inset: (x: 3.5pt, y: 2.2pt))\n#show table: set par(leading: 0.4em)\n```")
    fecha = "```{=typst}\n]\n```"
    return ("::: {.landscape}\n\n" + abre + "\n\n" + tabela
            + f"\n\n: {leg} {{#{rot}}}\n\n" + fecha + "\n\n:::")


# ================================================================ Tab. 3: hipóteses
def certeza_hipotese(l, por_id):
    cels = l.get("celulas") or []
    for cid in cels:
        if cid not in por_id:
            raise SystemExit(f"ERRO: hipoteses.yml, linha {l['id']}: célula {cid} não existe em celulas.json")
    nota = l.get("certeza_nota")
    if not cels:
        txt = "sem GRADE (descritivo)"
        stf = l.get("sem_teste_formal")
        if stf:
            txt += "; sem teste formal (" + (stf if isinstance(stf, str) else "menos de 4 estudos por nível") + ")"
        return txt + (f"; {nota}" if nota else "")
    niveis = sorted({por_id[c]["certeza"] for c in cels}, key=list(GRADE).index)
    if len(niveis) == 1:
        txt = grade(niveis[0])
    else:
        txt = f"de {grade(niveis[0])} a {grade(niveis[-1])}"
    return txt + (f", {nota}" if nota else "")


def t_hipoteses():
    dados = lyaml(TAB / "hipoteses.yml")
    por_id = {c["id"]: c for c in ljson(REV / "celulas.json")["celulas"]}
    linhas = []
    for l in dados["linhas"]:
        est = []
        for e in l.get("estudos") or []:
            est.append(f"@{e['chave']}" + (f", {e['suf']}" if e.get("suf") else ""))
        cit = ("[" + "; ".join(est) + "]") if est else "nenhum"
        interp = l.get("so_interpretacao") or []
        if interp:
            cit += "; só interpretação: [" + "; ".join("@" + k for k in interp) + "]"
        for k in [e["chave"] for e in l.get("estudos") or []] + interp:
            if k not in CHAVES:
                raise SystemExit(f"ERRO: hipoteses.yml, linha {l['id']}: chave {k} fora dos .bib")
        linhas.append([f"**{l['id']}** {uma_linha(l['hipotese'])}", cit, citar(uma_linha(l["evidencia"])) + ".",
                       certeza_hipotese(l, por_id)])
    leg = ("Hipóteses e elos da teoria da exposição registrada no protocolo e o que a evidência incluída diz sobre "
           "cada um. E1 a E8: elos do modelo lógico; R1 a R3: teorias rivais. Síntese descritiva a partir do "
           "fichamento por IA, conferido em bloco pelo autor (Emenda 7). A certeza GRADE só aparece quando a hipótese coincide com "
           "uma célula da síntese principal e qualifica a direção do efeito nessa célula, não o mecanismo; nas "
           "demais linhas, sem GRADE. Nenhuma célula tem 4 estudos por nível de moderador, e por isso nenhuma "
           "hipótese de moderação teve teste formal.")
    rot = ROTULOS["tabelas"]["hipoteses"]
    return ("::: {.tabela-larga}\n\n" + pipe(["Hipótese do protocolo", "Estudos que testam com dados",
                                               "O que a evidência diz", "Certeza"], linhas)
            + f"\n\n: {leg} {{#{rot} tbl-colwidths=\"[24,22,36,18]\"}}\n\n:::")


# ================================================================ Tab. 4: caixa OQF da pergunta principal
def calc_oqf():
    caixa = [r for r in lcsv(R / "06-analise/caixa_ferramentas.csv") if r["familia_intervencao"] == "pesquisa_pre_eleitoral"]
    corpos = {r["classe_desenho"]: r for r in caixa if r["dimensao"] == "efeito" and r["construto_outcome"] == "apoio_ao_lider"}
    impl = next(r for r in caixa if r["dimensao"] == "implementacao")
    custo = next(r for r in caixa if r["dimensao"] == "custo")
    cel = [c for c in ljson(INS / "caixa_oqf.json")["celulas"]
           if c["familia"] == "pesquisa_pre_eleitoral" and c["construto"] == "apoio_ao_lider"]
    nomes_des = {"randomizado": "randomizados", "nao_randomizado": "não randomizados"}
    return {
        "forca": "; ".join(f"{nomes_des[k]}: {v['rotulo']}, força {v['forca']}" for k, v in sorted(corpos.items(), reverse=True)),
        "n_celulas": len(cel),
        "n_estudos": len({e for c in cel for e in c["estudos"]}),
        "certezas": " e ".join(sorted({c["certeza"].replace("_", " ") for c in cel})),
        "rotulo_implementacao": impl["rotulo"],
        "rotulo_custo": custo["rotulo"],
    }


def t_oqf_principal():
    dados = lyaml(TAB / "oqf_principal.yml")
    calc = calc_oqf()
    linhas = []
    for l in dados["linhas"]:
        vals = [resolver_marcadores(uma_linha(l[c]), calc=calc, onde=f"oqf_principal.yml ({l['dimensao']})")
                for c in ("resultado", "evidencia", "certeza")]
        if re.search(r"\b\d\d-[a-z]+/|\.(csv|json|md|qmd|py)\b", " ".join(vals)):
            raise SystemExit(f"ERRO: oqf_principal.yml ({l['dimensao']}) tem caminho de arquivo")
        linhas.append([l["dimensao"]] + vals)
    rot = ROTULOS["tabelas"]["oqf_principal"]
    larg = ",".join(str(x) for x in dados.get("larguras", [12, 50, 24, 14]))
    return (pipe(["Dimensão", "Resultado para pesquisa pré-eleitoral × apoio a quem aparece à frente", "Evidência",
                  "Certeza"], linhas)
            + f"\n\n: {uma_linha(dados['legenda'])} {{#{rot} tbl-colwidths=\"[{larg}]\"}}")


# ================================================================ Tab. 5: transferibilidade
def t_transferibilidade():
    dados = lyaml(TAB / "transferibilidade.yml")
    linhas = []
    for l in dados["linhas"]:
        vals = [resolver_marcadores(uma_linha(l[c]), onde=f"transferibilidade.yml ({l['fator']})")
                for c in ("brasil", "estudos", "dizer")]
        linhas.append([l["fator"]] + vals)
    rot = ROTULOS["tabelas"]["transferibilidade"]
    larg = ",".join(str(x) for x in dados.get("larguras", [14, 32, 24, 30]))
    return ("::: {.tabela-larga}\n\n"
            + pipe(["Fator", "Como é no Brasil", "Estudos incluídos com a condição", "O que se pode dizer"], linhas)
            + f"\n\n: {uma_linha(dados['legenda'])} {{#{rot} tbl-colwidths=\"[{larg}]\"}}\n\n:::")


# ================================================================ pendências
def t_pendencias():
    pend = ljson(R / "07-relatorio/_pendencias_abertas.json")["pendencias"]
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
    leg = (f"\n: Pendências humanas abertas ({len(pend)}), na ordem das etapas, do registro de estado da revisão; "
           "etapa, tarefa, pacote de revisão e esforço estimado vêm do guia de revisão humana do projeto (a tarefa da "
           "P042, do registro da própria pendência). {#" + ROTULOS["tabelas"]["pendencias"]
           + " tbl-colwidths=\"[7,15,48,18,12]\"}")
    return cab + corpo + leg


TABELAS = {"caracteristicas": t_caracteristicas, "sof": t_sof, "hipoteses": t_hipoteses,
           "oqf_principal": t_oqf_principal, "transferibilidade": t_transferibilidade, "pendencias": t_pendencias,
           # fora do contrato atual de rótulos (a checagem reprova se forem usadas)
           "swim": t_swim, "regional": t_regional, "caixa_celulas": t_caixa_celulas, "mecanismos": t_mecanismos}


# ================================================================ YAML do documento montado
def chaves_incluidos():
    return [r["chave"] for r in lcsv(R / "07-relatorio/incluidos.csv")]


def metadados(texto, extra_linhas):
    """Acrescenta chaves ao YAML inicial do documento montado (cria o bloco se não houver); as chaves repetidas do
    esqueleto são substituídas no texto montado."""
    novas = {l.split(":", 1)[0] for l in extra_linhas if not l.startswith(" ")}
    m = re.match(r"^---\n(.*?)\n(---|\.\.\.)\n", texto, flags=re.S)
    if m:
        corpo = m.group(1).split("\n")
        filtrado, pular = [], False
        for l in corpo:
            if re.match(r"^[\w-]+:", l):
                pular = l.split(":", 1)[0] in novas
            if not pular:
                filtrado.append(l)
        return "---\n" + "\n".join(filtrado + extra_linhas) + "\n" + m.group(2) + "\n" + texto[m.end():]
    return "---\n" + "\n".join(extra_linhas) + "\n---\n\n" + texto


def estado_revista():
    """`final` se revista/_revista.yml declarar `estado: final` (versão de entrega, Emenda 7); senão `rascunho`."""
    m = re.search(r"(?m)^estado:\s*(\w+)", ler(REV / "_revista.yml"))
    return "final" if m and m.group(1) == "final" else "rascunho"


def chaves_apendices():
    """Chaves citadas nos apêndices (suplemento.qmd), na ordem em que aparecem. Na versão final, os apêndices vêm no
    mesmo PDF do artigo e não têm lista própria (suppress-bibliography): estas chaves entram no nocite dos dois
    documentos, para que a lista de referências do artigo cubra os apêndices e a desambiguação ("2021a/b") seja a
    mesma nos dois."""
    spec = importlib.util.spec_from_file_location("montar_suplemento_ap", D / "montar_suplemento.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    bib = chaves_bib()
    vistas = []
    for k in re.findall(r"@([\w-]+)", m.corpo()):
        if k in bib and k not in vistas:
            vistas.append(k)
    return vistas


def linhas_metadados():
    n = ljson(R / "07-relatorio/_pendencias_abertas.json")["abertas"]
    linhas = ["# gerado por montar_revisao_final.py / montar_suplemento.py", f"pendencias-abertas: {n}"]
    # rascunho: marca-d'água e cabeçalho. Na versão final (estado: final), a marca fica só na declaração de IA.
    if n > 0 and estado_revista() != "final":
        linhas.append("rascunho: true")
    chaves = chaves_incluidos()
    chaves += [k for k in chaves_apendices() if k not in chaves]
    linhas.append("nocite: |")
    linhas.append("  " + ", ".join("@" + k for k in chaves))
    return linhas


# ================================================================ montagem e checagens
def trocar_marcadores(texto, tabelas, legendas_path=LEGENDAS, exigir_figuras=True):
    def troca(m):
        tipo, nome = m.group(1), m.group(2)
        if tipo == "FIGURA":
            return figura(nome, legendas_path, exigir_figuras)
        if nome not in tabelas:
            raise SystemExit(f"ERRO: tabela desconhecida: @@TABELA {nome}@@")
        return tabelas[nome]()
    return re.sub(r"^@@(FIGURA|TABELA) (\w+)@@[ \t]*$", troca, texto, flags=re.M)


def checar(saida, nome_doc, contrato=None):
    erros = []
    if "@@" in saida:
        erros.append(f"sobrou '@@': {sorted(set(re.findall(r'@@[^\n]{0,40}', saida)))[:5]}")
    if contrato is None:
        contrato = (set((ROTULOS.get("figuras") or {}).values()) | set((ROTULOS.get("tabelas") or {}).values())
                    | set((ROTULOS.get("quadros") or {}).values()))
    for rot in re.findall(r"\{[^{}\n]*#((?:fig|tbl|qdr)-[\w-]+)", saida):
        if rot not in contrato:
            erros.append(f"rótulo {rot} fora de revista/rotulos.yml")
    for rot in re.findall(r"\]\((\.\./[^)]*)\)", saida):
        erros.append(f"caminho com '../': {rot}")
    if erros:
        raise SystemExit(f"ERRO em {nome_doc}:\n  " + "\n  ".join(erros))


def montar_texto(esqueleto=D / "_esqueleto_revisao_final.qmd", legendas=LEGENDAS, exigir_figuras=True):
    """Texto do revisao_final.qmd montado, sem gravar (também usado por revista/gerar_rotulos_autor_ano.py)."""
    saida = trocar_marcadores(ler(esqueleto), TABELAS, Path(legendas), exigir_figuras)
    return metadados(saida, linhas_metadados())


def previas(nomes):
    nomes = nomes or ["caracteristicas", "sof", "hipoteses", "oqf_principal", "transferibilidade", "pendencias"]
    for n in nomes:
        if n not in TABELAS:
            raise SystemExit(f"ERRO: tabela desconhecida: {n}")
        conteudo = TABELAS[n]()
        checar(conteudo, f"prévia {n}")
        (TAB / f"previa_{n}.md").write_text(conteudo + "\n", encoding="utf-8")
        print(f"revista/tabelas/previa_{n}.md")


def main():
    ap = argparse.ArgumentParser(description="Monta revisao_final.qmd a partir do esqueleto.")
    ap.add_argument("--esqueleto", default=str(D / "_esqueleto_revisao_final.qmd"))
    ap.add_argument("--saida", default=str(D / "revisao_final.qmd"))
    ap.add_argument("--legendas", default=str(LEGENDAS))
    ap.add_argument("--previas", nargs="*", default=None, metavar="TABELA",
                    help="grava revista/tabelas/previa_<nome>.md e não monta o artigo")
    a = ap.parse_args()
    if a.previas is not None:
        previas(a.previas)
        return
    saida = montar_texto(a.esqueleto, a.legendas)
    checar(saida, Path(a.saida).name)
    Path(a.saida).write_text(saida + "\n", encoding="utf-8")
    print(f"{Path(a.saida).name} escrito;", len(re.findall(r"\S+", saida)), "tokens")


if __name__ == "__main__":
    main()
