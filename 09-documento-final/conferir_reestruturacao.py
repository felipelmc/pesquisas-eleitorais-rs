"""Trava da reestruturação do documento final (artigo de revisão sistemática).

USO (da raiz):
  python3 09-documento-final/conferir_reestruturacao.py [--v1 09-documento-final/_revisao_final_v1_oqf.qmd]
      [--novo 09-documento-final/revisao_final.qmd] [--suplemento 09-documento-final/suplemento.qmd]

Sai com 0 se passar e 1 se houver alguma FALHA. Imprime um relatório por categoria (FALHA / AVISO / OK).
Só lê arquivos; não escreve nada.

Categorias
  Datas         dd/mm/aaaa só da lista permitida (v1, 00-protocolo/*.md, 24/09/2026 e 25/09/2026); dd/mm só se casar
                com uma data dessa lista.
  Números       todo número do texto novo, depois do pré-processamento, tem de estar na lista branca: números do v1,
                folhas numéricas dos JSON e CSV de síntese (com arredondamentos de 0 a 3 casas e ×100 nas proporções;
                cada arredondamento entra nas duas variantes, meio para cima sobre a representação decimal, que é a
                dos montadores desde a etapa 6c (0,975 → 0,98), e a do f-string do Python, que arredonda o binário
                (0,975 → 0,97) e é a dos insumos gerados antes),
                numeros_v2.json e celulas.json. Decimal, porcentagem ou inteiro > 10 fora da lista = FALHA; inteiro
                ≤ 10 = AVISO. Anos (19xx/20xx) passam também se estiverem no v1, nos .bib ou em incluidos.csv.
                Número sem sinal casa com o valor absoluto; número com sinal negativo só com valor negativo.
                Os números escritos nos campos de texto de certeza*.csv (enunciado e justificativa do GRADE) entram
                na lista branca, porque as notas de rebaixamento da SoF saem deles.
  Células       cada célula de revista/celulas.json tem ao menos um [enunciado literal]{.enunciado cel="Cxx"}; no mesmo
                parágrafo (ou na mesma linha, se o span estiver numa tabela) aparecem "certeza <nível>" e o k. Fora dos
                spans, "x de y" (exceto "x de y efeitos"), "p = ..." e "IC 95% a a b" têm de bater com uma célula do
                parágrafo; p e IC logo depois de um g, EP ou β são de tamanho de efeito e não entram nessa conferência
                (entram na de números). "x de y" com y certo e x que não é contagem de direção vira AVISO
                (pode ser subconjunto, como "3 de 4 em laboratório").
  Estrutura     11 callouts "Pendente de revisão humana" com o mesmo multiconjunto de conjuntos de P0xx do v1;
                tabela tbl-pendencias com os IDs de 07-relatorio/_pendencias_abertas.json (primeira coluna);
                toda @chave nos .bib; todo @fig-/@tbl-/@sec-/@qdr- no contrato revista/rotulos.yml e definido no
                documento; @sec- só para seção numerada; links suplemento.html#id no contrato.
  Proibições    "Neutro", "sem efeito", "benéfic", "danos", "significativ", travessão, "](../", "column-", caminho de
                arquivo em texto corrido (fora de código e de legenda de tabela), "revisão/revisado por pares".
  Revisões ant. frase que cita Hardmeier, Moy & Rinke ou Barnfield com verbo de conclusão só passa se
                insumos/revisoes_anteriores.md marcar a obra como verificada (sem o arquivo: AVISO).
  Relato        marcadores "[A confirmar pelo autor]" e palavras por seção de nível 1 (só informa).

Pré-processamento antes de extrair números: remove YAML, comentários HTML, blocos e spans de código, linhas ":::",
linhas "@@...@@", atributos {#...}/{.…}/{chave=…}, URLs e destinos de link, @chaves e chaves de estudo soltas (dos
.bib e de incluidos.csv), P000, C00, rótulos fig-/tbl-/sec-/qdr-, domínios D1, elos E1/H1/A1/B01/G9/S1/M1,
itens/seções/§/Emendas/Fig./Tab./Quadro/Apêndice com número, leis e atos, nomes de ferramenta com dígito
(RoB 2, ROBINS-I V2, PRISMA 2020, caixa-3, G9, modelos e versões x.y.z), "IC 95%" e a numeração de seção no início
de título. Normalização: U+2212 → "-", vírgula decimal → ponto, ponto seguido de exatamente 3 dígitos em inteiro →
milhar (no bloco em inglês, vírgula de milhar e ponto decimal).
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation
from pathlib import Path

R = Path(__file__).resolve().parents[1]
D = R / "09-documento-final"
REV = D / "revista"

BIBS = [R / "07-relatorio/references.bib", D / "referencias_contexto.bib", D / "referencias_metodo.bib",
        D / "referencias_excluidos.bib"]
LISTA_JSON = (["07-relatorio/prisma_contagens.json"]
              + sorted(str(p.relative_to(R)) for p in (R / "06-analise").glob("swim_*/swim_resumo.json"))
              + sorted(str(p.relative_to(R)) for p in (R / "06-analise").glob("meta_*/meta_resumo.json"))
              + ["09-documento-final/insumos/tabelas/numeros.json", "09-documento-final/insumos/caixa_oqf.json",
                 "09-documento-final/revista/celulas.json", "09-documento-final/revista/numeros_v2.json",
                 "07-relatorio/_pendencias_abertas.json"])
LISTA_CSV = sorted(str(p.relative_to(R)) for p in (R / "06-analise").glob("certeza*.csv"))
DELTA_TXT = "06-analise/_delta_celula.txt"
PEND = R / "07-relatorio/_pendencias_abertas.json"
CELULAS = REV / "celulas.json"
ROTULOS = REV / "rotulos.yml"
REVISOES = D / "insumos/revisoes_anteriores.md"
INCLUIDOS = R / "07-relatorio/incluidos.csv"
TITULO_PENDENTE = "Pendente de revisão humana"
N_CALLOUTS = 11
DATAS_FIXAS = ["24/09/2026", "25/09/2026"]
MARCADOR_AUTOR = "[A confirmar pelo autor]"
NIVEIS = ["muito baixa", "baixa", "moderada", "alta"]
POR_EXTENSO = {1: ["um", "uma", "único", "única"], 2: ["dois", "duas"], 3: ["três"], 4: ["quatro"], 5: ["cinco"],
               6: ["seis"], 7: ["sete"], 8: ["oito"], 9: ["nove"], 10: ["dez"]}


# =============================================================== relatório
class Relatorio:
    ORDEM = ["Datas", "Números", "Células", "Estrutura: callouts", "Estrutura: apêndice", "Estrutura: citações",
             "Estrutura: rótulos e seções", "Proibições", "Revisões anteriores", "Relato"]

    def __init__(self):
        self.itens = defaultdict(list)

    def add(self, cat, nivel, msg):
        self.itens[cat].append((nivel, msg))

    def falhas(self):
        return sum(1 for v in self.itens.values() for n, _ in v if n == "FALHA")

    def avisos(self):
        return sum(1 for v in self.itens.values() for n, _ in v if n == "AVISO")

    def imprimir(self):
        for cat in self.ORDEM + [c for c in self.itens if c not in self.ORDEM]:
            v = self.itens.get(cat, [])
            nf = sum(1 for n, _ in v if n == "FALHA")
            na = sum(1 for n, _ in v if n == "AVISO")
            status = "FALHA" if nf else "AVISO" if na else "OK"
            extra = f" ({nf} falha(s), {na} aviso(s))" if (nf or na) else ""
            print(f"== {cat}: {status}{extra}")
            for nivel in ("FALHA", "AVISO", "INFO", "OK"):
                for n, msg in v:
                    if n == nivel:
                        print(f"   {n:5}  {msg}")
        print(f"\nRESULTADO: {'FALHA' if self.falhas() else 'OK'} ({self.falhas()} falha(s), {self.avisos()} aviso(s))")


# =============================================================== leitura
def resolver(p):
    p = Path(p)
    if p.is_absolute() or p.exists():
        return p
    return R / p


def ler(p):
    return Path(p).read_text(encoding="utf-8")


def chaves_bib(caminhos, rel=None):
    ks, anos = set(), set()
    for b in caminhos:
        if not b.exists():
            if rel is not None:
                rel.add("Estrutura: citações", "AVISO", f"arquivo .bib ausente (ignorado): {b.relative_to(R)}")
            continue
        t = ler(b)
        ks |= set(re.findall(r"^@\w+\s*\{\s*([^,\s]+)\s*,", t, flags=re.M))
        anos |= {int(a) for a in re.findall(r"(?:year|date)\s*=\s*[{\"]?\s*((?:19|20)\d\d)", t, flags=re.I)}
    return ks, anos


def ler_rotulos():
    txt = ler(ROTULOS)
    try:
        import yaml
        return yaml.safe_load(txt)
    except ImportError:
        pass
    dados, secao = {}, None
    for linha in txt.splitlines():
        linha = linha.split("#", 1)[0].rstrip() if not linha.lstrip().startswith("- ") else linha.split("  #")[0].rstrip()
        if not linha.strip():
            continue
        m = re.match(r"^(\w+):\s*$", linha)
        if m:
            secao = m.group(1)
            continue
        m = re.match(r"^\s+-\s*(\S+)", linha)
        if m and secao:
            dados.setdefault(secao, []).append(m.group(1))
            continue
        m = re.match(r"^\s+(\w+):\s*(\S+)", linha)
        if m and secao:
            dados.setdefault(secao, {})[m.group(1)] = m.group(2)
    return dados


# =============================================================== pré-processamento
def _apaga(m):
    return "\n" * m.group(0).count("\n") or " "


def sem_yaml(s):
    if s.startswith("---"):
        fim = re.search(r"\n(---|\.\.\.)\s*\n", s[3:])
        if fim:
            corte = 3 + fim.end()
            return "\n" * s[:corte].count("\n") + s[corte:]
    return s


def sem_comentarios_e_codigo(s):
    s = sem_yaml(s)
    s = re.sub(r"<!--.*?-->", _apaga, s, flags=re.S)
    s = re.sub(r"^(```+|~~~+)[^\n]*\n.*?^\1[ \t]*$", _apaga, s, flags=re.S | re.M)
    s = re.sub(r"(`+)[^`\n]+?\1", " ", s)
    return s


def regex_chaves(chaves):
    if not chaves:
        return None
    alt = "|".join(re.escape(k) for k in sorted(chaves, key=len, reverse=True))
    return re.compile(rf"(?<![\w@])(?:{alt})(?![\w])")


LISTA_NUM = r"\d+[a-z]?(?:\.\d+)*(?:\s*(?:,|e|a|ou|and|to)\s*\d+[a-z]?(?:\.\d+)*)*"
PADROES_REMOCAO = [
    (r"^:::.*$", re.M),                                              # cercas de Div
    (r"^@@.*@@\s*$", re.M),                                          # marcadores de figura/tabela
    (r"\{(?=[#.]|[\w-]+=)[^{}\n]*\}", 0),                            # atributos
    (r"\]\([^)\n]*\)", 0),                                           # destinos de link (o "]" some junto)
    (r"<https?://[^>\s]+>", 0),
    (r"https?://[^\s)>\]]+", 0),
    (r"(?<![\w@])@\{[^}]*\}", 0),
    (r"(?<![\w@])@[\w][\w:\-]*", 0),                                 # @chaves e @fig-/@tbl-/@sec-
]
PADROES_REMOCAO_2 = [
    (r"\bP\d{3}\b", 0),
    (r"\bC\d{2}\b", 0),
    (r"\b(?:fig|tbl|sec|qdr)-[\w-]+", 0),
    (r"\bD\d+[a-z]?\b", 0),
    (r"\b[EHABGSM]\d+[a-z]?\b", 0),
    (r"(?i:\b(?:itens|item|items|cap\.|caps\.|seções|seção|secao|section|sections|emendas|emenda|amendments?|"
     r"fig\.|figs\.|figura|figuras|figure|figures|tab\.|tabela|tabelas|table|tables|quadro|quadros|box|"
     r"apêndice|apêndices|appendix|anexo|capítulo|capítulos))\s?" + LISTA_NUM, 0),
    (r"§\s?" + LISTA_NUM, 0),
    (r"\bS\s?\d+[a-z]?\b", 0),
    (r"\bE00\d+\b", 0),
    (r"\b(?:Lei|Leis|Res\.|Resolução|Resolucao|PL|PLs|ADI|ADIs|art\.|arts\.|Decreto|EC|LC)(?:-[A-Z]+)?\s*"
     r"(?:n\.?\s?º|nº|n°|n\.|no\.)?\s*\d[\d./-]*(?:\s*(?:,|e)\s*\d[\d./-]*)*", 0),
    (r"\bRoB\s?2\b", 0),
    (r"\bROBINS-[IE](?:\s?V\d)?\b", 0),
    (r"\bPRISMA(?:-[A-Za-z]+)?\s?20\d\d\b", 0),
    (r"\bPRESS\s?20\d\d\b", 0),
    (r"\bcaixa-\d+\b", 0),
    (r"\b(?:Claude\s)?(?:Opus|Sonnet|Haiku|Fable)\s?\d+(?:[.-]\d+)*\b", 0),
    (r"\bv?\d+\.\d+\.\d+\b", 0),                                     # versões x.y.z
    (r"^(#{1,6})\s+\d+(?:\.\d+)*\.?(?=\s)", re.M),                   # numeração no início de título
]
PADRAO_IC = [(r"\bIC\s?95\s?%|\b95\s?%\s?(?:CI|IC)\b|\bIC95\b|\bCI95\b", 0)]


def limpar(s, rx_chaves, manter_ic=False, codigo=True):
    """Aplica o pré-processamento preservando o número de linhas."""
    if codigo:
        s = sem_comentarios_e_codigo(s)
    for p, fl in PADROES_REMOCAO:
        s = re.sub(p, _apaga, s, flags=fl)
    if rx_chaves is not None:
        s = rx_chaves.sub(" ", s)
    for p, fl in PADROES_REMOCAO_2:
        if p.startswith("^(#{1,6})"):
            s = re.sub(p, r"\1", s, flags=fl)
        else:
            s = re.sub(p, _apaga, s, flags=fl)
    if not manter_ic:
        for p, fl in PADRAO_IC:
            s = re.sub(p, " ", s, flags=fl)
    return s


# =============================================================== blocos em inglês e Divs
def divs(texto):
    """Lista de Divs: dict(attrs, ini, fim, conteudo) com linhas 0-based. Ignora cercas dentro de blocos de código."""
    linhas = texto.split("\n")
    pilha, saida, em_codigo = [], [], None
    for i, l in enumerate(linhas):
        m = re.match(r"^(```+|~~~+)", l)
        if m:
            if em_codigo is None:
                em_codigo = m.group(1)
            elif l.startswith(em_codigo):
                em_codigo = None
            continue
        if em_codigo:
            continue
        m = re.match(r"^(:{3,})\s*(.*?)\s*:*\s*$", l)
        if not m:
            continue
        attrs = m.group(2)
        if attrs:
            pilha.append((attrs, i))
        elif pilha:
            a, ini = pilha.pop()
            saida.append({"attrs": a, "ini": ini, "fim": i, "conteudo": "\n".join(linhas[ini + 1:i])})
    return saida


def linhas_ingles(texto):
    linhas = texto.split("\n")
    ing = set()
    for d in divs(texto):
        if re.search(r"lang\s*=\s*\"?en", d["attrs"]):
            ing |= set(range(d["ini"], d["fim"] + 1))
    nivel_abs = None
    for i, l in enumerate(linhas):
        m = re.match(r"^(#{1,6})\s+(.*)$", l)
        if m:
            nivel = len(m.group(1))
            if nivel_abs is not None and nivel <= nivel_abs:
                nivel_abs = None
            if re.search(r"abstract", re.sub(r"\{.*?\}", "", m.group(2)), re.I):
                nivel_abs = nivel
        if nivel_abs is not None:
            ing.add(i)
    return ing


# =============================================================== números
RX_NUM = re.compile(r"(?<![\w.,])(\d+(?:[.,]\d+)*)(\s?%)?(?![\w])")
RX_DATA = re.compile(r"(?<![\d/])(\d{1,2})/(\d{1,2})/(\d{4})(?![\d/])")
RX_DATA_CURTA = re.compile(r"(?<![\d/])(\d{1,2})/(\d{1,2})(?![\d/])")


def para_decimal(tok, ingles=False):
    """Devolve (Decimal, eh_decimal) ou None."""
    if ingles:
        if re.fullmatch(r"[1-9]\d{0,2}(,\d{3})+(\.\d+)?", tok):
            s = tok.replace(",", "")
        elif "," in tok and "." not in tok and tok.count(",") == 1:
            s = tok.replace(",", ".")
        else:
            s = tok
    else:
        if re.fullmatch(r"[1-9]\d{0,2}(\.\d{3})+(,\d+)?", tok):
            s = tok.replace(".", "").replace(",", ".")
        elif "," in tok:
            if tok.count(",") != 1 or "." in tok:
                return None
            s = tok.replace(",", ".")
        else:
            s = tok
    try:
        return Decimal(s), "." in s
    except InvalidOperation:
        return None


def canon(d):
    if d == 0:
        return "0"
    return format(d.normalize(), "f")


def tokens_numericos(texto_limpo, ingles_linhas=frozenset()):
    """(linha 1-based, token original, Decimal com sinal, tem_sinal_negativo, eh_decimal, eh_pct)."""
    saida = []
    for i, l in enumerate(texto_limpo.split("\n")):
        l = l.replace("\u2212", "-")
        for m in RX_NUM.finditer(l):
            conv = para_decimal(m.group(1), i in ingles_linhas)
            if conv is None:
                saida.append((i + 1, m.group(0), None, False, False, False))
                continue
            v, eh_dec = conv
            ini = m.start()
            neg = ini >= 1 and l[ini - 1] == "-" and (ini < 2 or not re.match(r"[\w.,]", l[ini - 2]))
            saida.append((i + 1, m.group(0).strip(), -v if neg else v, neg, eh_dec, bool(m.group(2))))
    return saida


class ListaBranca:
    def __init__(self):
        self.v = {}

    def _put(self, d, fonte):
        self.v.setdefault(canon(d), fonte)

    def exato(self, d, fonte):
        self._put(d, fonte)

    def com_variantes(self, x, fonte):
        if isinstance(x, bool) or x is None:
            return
        dx = x if isinstance(x, Decimal) else Decimal(repr(x)) if isinstance(x, float) else Decimal(x)
        fx = float(dx)
        alvos = [dx]
        if 0 <= fx <= 1:
            alvos.append(dx * 100)
        for a in alvos:
            self._put(a, fonte)
            for casas in range(4):
                q = Decimal(1).scaleb(-casas)
                # meio para cima sobre repr (0,975 -> 0,98, formatadores atuais) e f-string (0,975 -> 0,97, insumos antigos)
                self._put(a.quantize(q, rounding=ROUND_HALF_UP), fonte)
                self._put(Decimal(f"{float(a):.{casas}f}"), fonte)

    def contem(self, d, neg):
        if canon(d) in self.v:
            return True
        return (not neg) and canon(-d) in self.v

    def fonte(self, d):
        return self.v.get(canon(d)) or self.v.get(canon(-d))


def numero_de_string(s):
    s = s.strip().replace("\u2212", "-")
    s = re.sub(r"^[<>≤≥]\s*", "", s)
    m = re.fullmatch(r"(-?)(\d+(?:[.,]\d+)*)\s?%?", s)
    if not m:
        return None
    conv = para_decimal(m.group(2))
    if conv is None:
        return None
    return -conv[0] if m.group(1) else conv[0]


def folhas(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from folhas(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from folhas(v)
    else:
        yield obj


def montar_lista_branca(v1_limpo, v1_ing, rx_chaves, rel):
    lb = ListaBranca()
    for _, _, v, _, _, _ in tokens_numericos(v1_limpo, v1_ing):
        if v is not None:
            lb.exato(v, "v1")
    for rel_path in LISTA_JSON:
        p = R / rel_path
        if not p.exists():
            rel.add("Números", "AVISO", f"fonte da lista branca ausente: {rel_path}")
            continue
        for f in folhas(json.load(open(p, encoding="utf-8"))):
            if isinstance(f, (int, float)) and not isinstance(f, bool):
                lb.com_variantes(f, rel_path)
            elif isinstance(f, str):
                d = numero_de_string(f)
                if d is not None:
                    lb.com_variantes(d, rel_path)
    for rel_path in LISTA_CSV:
        for linha in csv.DictReader(open(R / rel_path, encoding="utf-8-sig")):
            for col, val in linha.items():
                d = numero_de_string(val or "")
                if d is not None:
                    lb.com_variantes(d, rel_path)
                elif val and col in ("enunciado", "justificativa"):
                    for _, _, v, _, _, _ in tokens_numericos(limpar(val, rx_chaves, codigo=False)):
                        if v is not None:
                            lb.com_variantes(v, f"{rel_path} ({col})")
    p = R / DELTA_TXT
    if p.exists():
        for m in RX_NUM.finditer(ler(p)):
            conv = para_decimal(m.group(1), ingles=True)
            if conv:
                lb.com_variantes(conv[0], DELTA_TXT)
    return lb


def datas_permitidas(v1_bruto):
    textos = [v1_bruto] + [ler(p) for p in sorted((R / "00-protocolo").glob("*.md"))] + [" ".join(DATAS_FIXAS)]
    ds = set()
    for t in textos:
        ds |= {(int(a), int(b), int(c)) for a, b, c in RX_DATA.findall(t)}
    return ds


def conferir_datas_e_numeros(nome, bruto, limpo, ingles, lb, datas_ok, anos_ok, rel):
    curtas_ok = {(d, m) for d, m, _ in datas_ok}
    linhas = limpo.split("\n")
    for i, l in enumerate(linhas):
        for m in RX_DATA.finditer(l):
            d = tuple(int(x) for x in m.groups())
            if d not in datas_ok:
                rel.add("Datas", "FALHA", f"{nome} linha {i + 1}: data {m.group(0)} fora da lista permitida")
        l = RX_DATA.sub(" ", l)
        for m in RX_DATA_CURTA.finditer(l):
            dd, mm = int(m.group(1)), int(m.group(2))
            if 1 <= dd <= 31 and 1 <= mm <= 12:
                if (dd, mm) not in curtas_ok:
                    rel.add("Datas", "FALHA", f"{nome} linha {i + 1}: data {m.group(0)} fora da lista permitida")
        l = RX_DATA_CURTA.sub(" ", l)
        linhas[i] = l
    limpo = "\n".join(linhas)
    fora = defaultdict(list)
    total = 0
    for ln, tok, v, neg, eh_dec, eh_pct in tokens_numericos(limpo, ingles):
        total += 1
        if v is None:
            rel.add("Números", "AVISO", f"{nome} linha {ln}: número não interpretado '{tok}'")
            continue
        if lb.contem(v, neg):
            continue
        eh_ano = (not eh_dec and not eh_pct and not neg and re.fullmatch(r"(?:19|20)\d\d", tok.strip()))
        if eh_ano and int(v) in anos_ok:
            continue
        if eh_pct:
            nivel, tipo = "FALHA", "porcentagem"
        elif eh_dec:
            nivel, tipo = "FALHA", "decimal"
        elif eh_ano:
            nivel, tipo = "FALHA", "ano fora do v1, dos .bib e de incluidos.csv"
        elif abs(v) > 10:
            nivel, tipo = "FALHA", "inteiro > 10"
        else:
            nivel, tipo = "AVISO", "inteiro ≤ 10"
        fora[(nivel, tipo, tok)].append(ln)
    for (nivel, tipo, tok), lns in sorted(fora.items(), key=lambda x: (x[0][0], x[1][0])):
        amostra = bruto.split("\n")[lns[0] - 1].strip()
        achado = re.search(rf"(?<![\d.,]){re.escape(tok.lstrip('-').replace(' ', ''))}(?![\d])", amostra)
        pos_tok = achado.start() if achado else -1
        trecho = amostra[max(0, pos_tok - 50):pos_tok + 50] if pos_tok >= 0 else amostra[:100]
        rel.add("Números", nivel, f"{nome} '{tok}' ({tipo}, fora da lista branca) nas linhas {lns}: …{trecho}…")
    return total


# =============================================================== células
RX_SPAN = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\{([^{}]*\.enunciado\b[^{}]*)\}")


def norm_espacos(s):
    return re.sub(r"\s+", " ", s.replace("\u00a0", " ")).strip()


def casa(texto_num, alvo, ingles=False):
    """Compara um número escrito com o valor da célula, com a tolerância das casas decimais escritas."""
    if alvo is None:
        return False
    t = texto_num.replace("\u2212", "-").strip()
    neg = t.startswith("-")
    conv = para_decimal(t.lstrip("-"), ingles)
    if conv is None:
        return False
    v = -conv[0] if neg else conv[0]
    casas = len(str(conv[0]).split(".")[1]) if "." in str(conv[0]) else 0
    return abs(float(v) - float(alvo)) <= 0.5 * 10 ** (-casas) + 1e-9


def contexto_de_efeito(texto, ini):
    antes = texto[max(0, ini - 60):ini]
    antes = re.split(r"(?<=[.!?])\s|\n", antes)[-1]
    return bool(re.search(r"\bg\s*(?:=|de\b)|\bg\s+[−-]?\d|\bEP\b|\bSE\b|β|\bd\s*=|\bOR\s*=", antes))


def unidades(texto):
    """Mapeia linha (0-based) → (ini, fim) do parágrafo ou, em tabela, da própria linha."""
    linhas = texto.split("\n")
    mapa, ini = {}, 0
    for i in range(len(linhas) + 1):
        if i == len(linhas) or not linhas[i].strip():
            for j in range(ini, i):
                mapa[j] = (j, j) if linhas[j].lstrip().startswith("|") else (ini, i - 1)
            ini = i + 1
    return mapa


def conferir_celulas(nome, bruto, celulas, rx_chaves, rel, exigir=True):
    por_id = {c["id"]: c for c in celulas}
    spans = []
    for m in RX_SPAN.finditer(bruto):
        cel = re.search(r"cel\s*=\s*\"?([A-Za-z]\d+)\"?", m.group(2))
        linha = bruto.count("\n", 0, m.start())
        spans.append({"cel": cel.group(1) if cel else None, "conteudo": m.group(1), "ini": m.start(),
                      "fim": m.end(), "linha": linha})
    mapa = unidades(bruto)
    linhas = bruto.split("\n")
    validos = defaultdict(list)
    for s in spans:
        if s["cel"] is None:
            rel.add("Células", "FALHA", f"{nome} linha {s['linha'] + 1}: span .enunciado sem atributo cel")
            continue
        c = por_id.get(s["cel"])
        if c is None:
            rel.add("Células", "FALHA", f"{nome} linha {s['linha'] + 1}: cel=\"{s['cel']}\" não existe em celulas.json")
            continue
        if norm_espacos(s["conteudo"]) != norm_espacos(c["enunciado"]):
            rel.add("Células", "FALHA", f"{nome} linha {s['linha'] + 1}: span {s['cel']} com texto diferente do "
                                        f"enunciado de certeza.csv: «{norm_espacos(s['conteudo'])[:90]}…»")
            continue
        validos[s["cel"]].append(s)
    # enunciado literal fora de span
    sem_spans = RX_SPAN.sub(" ", bruto)
    for c in celulas:
        if norm_espacos(c["enunciado"]) in norm_espacos(sem_spans):
            rel.add("Células", "AVISO", f"{nome}: enunciado de {c['id']} aparece literal fora de um span .enunciado")
    if not exigir:
        return
    for c in celulas:
        if not validos.get(c["id"]):
            rel.add("Células", "FALHA", f"{c['id']} ({c['bloco']}, {c['familia_intervencao']}, {c['comparador_tipo']}, "
                                        f"{c['classe_desenho']}): nenhum span [enunciado]{{.enunciado cel=\"{c['id']}\"}}")
            continue
        problemas_por_span = []
        for s in validos[c["id"]]:
            a, b = mapa.get(s["linha"], (s["linha"], s["linha"]))
            ini_u = sum(len(x) + 1 for x in linhas[:a])
            fim_u = sum(len(x) + 1 for x in linhas[:b + 1])
            unidade = bruto[ini_u:fim_u]
            cels_unid = [por_id[x["cel"]] for x in spans
                         if ini_u <= x["ini"] < fim_u and x["cel"] in por_id and x in validos.get(x["cel"], [])]
            probs, avisos = [], []
            # certeza
            nivel = c["certeza_texto"]
            rx_nivel = nivel.replace(" ", r"\s+")
            achou = re.search(r"certeza\s+" + rx_nivel + r"\b", unidade, re.I)
            if not achou:  # linha de tabela: "⊕◯◯◯ muito baixa"
                achou = re.search(r"[⊕◯○]+\s*(?:\*\*)?" + rx_nivel + r"\b", unidade, re.I)
            if not achou:
                probs.append(f"falta \"certeza {nivel}\" no mesmo parágrafo")
            niveis_unid = {x["certeza_texto"] for x in cels_unid}
            for m in re.finditer(r"certeza\s+(muito\s+baixa|baixa|moderada|alta)\b", RX_SPAN.sub(" ", unidade), re.I):
                if norm_espacos(m.group(1).lower()) not in niveis_unid:
                    avisos.append(f"o parágrafo também diz \"certeza {norm_espacos(m.group(1))}\", que não é de "
                                  f"nenhuma célula com span nele")
            # k
            limpo_u = limpar(unidade, rx_chaves, manter_ic=True, codigo=True)
            ints = {int(v) for _, _, v, neg, dec, pct in tokens_numericos(limpo_u)
                    if v is not None and not dec and not pct and not neg}
            k = c["k"]
            if k not in ints and not any(re.search(rf"\b{w}\b", unidade, re.I) for w in POR_EXTENSO.get(k, [])):
                probs.append(f"falta o k = {k} no mesmo parágrafo")
            # x de y, p, IC (fora dos spans)
            fora_spans = limpar(RX_SPAN.sub(" ", unidade), rx_chaves, manter_ic=True, codigo=True).replace("\u2212", "-")
            for m in re.finditer(r"(?<![\w.,])(\d+)\s+de\s+(\d+)(?![\d.,]*\d)(?!\s+(?:dos\s+|das\s+)?efeitos?\b)",
                                 fora_spans):
                x, y = int(m.group(1)), int(m.group(2))
                ok_y = [cc for cc in cels_unid if y in (cc["k"], cc["n_estudos_com_direcao"])]
                if not ok_y:
                    probs.append(f"\"{m.group(0)}\" não bate com k nem com os estudos com direção da célula")
                elif not any(x in (cc["n_beneficos"], cc["n_danosos"], cc["n_mistos"], cc["n_nulos"]) for cc in ok_y):
                    avisos.append(f"\"{m.group(0)}\": x não é contagem de direção da célula (subconjunto?)")
            for m in re.finditer(r"\bp\s*=\s*([−-]?\d[\d.,]*\d|\d)", fora_spans):
                if contexto_de_efeito(fora_spans, m.start()):
                    continue
                if not any(casa(m.group(1), cc["p_sinal"]) for cc in cels_unid):
                    probs.append(f"\"{m.group(0)}\" não bate com o p do teste de sinal "
                                 f"({', '.join(str(cc['p_sinal']) for cc in cels_unid)})")
            for m in re.finditer(r"(?:\bIC\s?95\s?%?|\bIC95\b)\s*(?:de\s+|:\s*)?([−-]?\d[\d.,]*)\s+(?:a|até)\s+"
                                 r"([−-]?\d[\d.,]*\d|\d)", fora_spans):
                if contexto_de_efeito(fora_spans, m.start()):
                    continue
                if not any(cc["ic_proporcao"] and casa(m.group(1), cc["ic_proporcao"][0])
                           and casa(m.group(2), cc["ic_proporcao"][1]) for cc in cels_unid):
                    probs.append(f"\"{m.group(0)}\" não bate com o IC da proporção "
                                 f"({'; '.join(str(cc['ic_proporcao']) for cc in cels_unid)})")
            problemas_por_span.append((s, probs, avisos))
        bons = [x for x in problemas_por_span if not x[1]]
        if bons:
            s, _, avisos = bons[0]
            rel.add("Células", "OK", f"{c['id']}: span literal na linha {s['linha'] + 1}, com certeza e k no parágrafo")
            for a in avisos:
                rel.add("Células", "AVISO", f"{c['id']} (linha {s['linha'] + 1}): {a}")
        for s, probs, avisos in problemas_por_span:
            if probs:
                rel.add("Células", "FALHA", f"{c['id']} (linha {s['linha'] + 1}): " + "; ".join(probs))
                for a in avisos:
                    rel.add("Células", "AVISO", f"{c['id']} (linha {s['linha'] + 1}): {a}")


# =============================================================== estrutura
def callouts_pendentes(texto):
    saida = []
    for d in divs(sem_comentarios_e_codigo(texto)):
        if ".callout" not in d["attrs"] and "callout-" not in d["attrs"]:
            continue
        m = re.search(r"title\s*=\s*\"([^\"]*)\"", d["attrs"])
        titulo = m.group(1) if m else None
        if titulo is None:
            primeira = next((l for l in d["conteudo"].split("\n") if l.strip()), "")
            mh = re.match(r"^#{1,6}\s+(.*?)\s*(\{.*\})?\s*$", primeira)
            titulo = mh.group(1) if mh else None
        if titulo and norm_espacos(titulo) == TITULO_PENDENTE:
            saida.append({"linha": d["ini"] + 1, "ids": frozenset(re.findall(r"\bP\d{3}\b", d["conteudo"]))})
    return saida


def conferir_callouts(novo, v1, rel):
    cn, cv = callouts_pendentes(novo), callouts_pendentes(v1)
    if len(cn) != N_CALLOUTS:
        rel.add("Estrutura: callouts", "FALHA", f"{len(cn)} callouts \"{TITULO_PENDENTE}\" (esperados {N_CALLOUTS}; "
                                                f"o v1 tem {len(cv)})")
    mn, mv = Counter(c["ids"] for c in cn), Counter(c["ids"] for c in cv)
    for ids, n in (mv - mn).items():
        rel.add("Estrutura: callouts", "FALHA", f"conjunto de IDs do v1 ausente no texto novo: {sorted(ids)} (×{n})")
    for ids, n in (mn - mv).items():
        linhas = [c["linha"] for c in cn if c["ids"] == ids]
        rel.add("Estrutura: callouts", "FALHA", f"conjunto de IDs que não existe no v1: {sorted(ids)} (×{n}; linhas {linhas})")
    if len(cn) == N_CALLOUTS and mn == mv:
        rel.add("Estrutura: callouts", "OK", f"{len(cn)} callouts com os mesmos conjuntos de IDs do v1")


def conferir_apendice(novo, rel):
    pend = json.load(open(PEND, encoding="utf-8"))
    esperados = {p["id"] for p in pend["pendencias"]}
    linhas = sem_comentarios_e_codigo(novo).split("\n")
    idx = next((i for i, l in enumerate(linhas) if re.match(r"^:?\s*:\s.*\{#tbl-pendencias\b", l)
                or re.match(r"^:\s.*\{#tbl-pendencias\b", l)), None)
    if idx is None:
        if any(re.match(r"^@@TABELA pendencias@@\s*$", l) for l in linhas):
            rel.add("Estrutura: apêndice", "AVISO", "tabela de pendências ainda como marcador @@TABELA pendencias@@; "
                                                   "confira o texto montado")
        else:
            rel.add("Estrutura: apêndice", "FALHA", "tabela {#tbl-pendencias} não encontrada")
        return
    j = idx - 1
    while j >= 0 and not linhas[j].strip():
        j -= 1
    tabela = []
    while j >= 0 and linhas[j].lstrip().startswith("|"):
        tabela.append(linhas[j])
        j -= 1
    ids = set()
    for l in tabela:
        primeira = l.strip().strip("|").split("|")[0].strip().strip("*")
        if re.fullmatch(r"P\d{3}", primeira):
            ids.add(primeira)
    if ids == esperados:
        rel.add("Estrutura: apêndice", "OK", f"tbl-pendencias lista as {len(esperados)} pendências abertas")
    else:
        if esperados - ids:
            rel.add("Estrutura: apêndice", "FALHA", f"pendências abertas fora da tabela: {sorted(esperados - ids)}")
        if ids - esperados:
            rel.add("Estrutura: apêndice", "FALHA", f"IDs na tabela que não estão abertos: {sorted(ids - esperados)}")


PREFIXOS_REF = ("fig-", "tbl-", "sec-", "qdr-", "eq-", "lst-", "thm-", "lem-", "cor-", "prp-", "cnj-", "def-", "exm-",
                "exr-", "sol-", "rem-")


def citacoes(texto):
    t = sem_comentarios_e_codigo(texto)
    t = re.sub(r"<https?://[^>\s]+>|https?://[^\s)>\]]+", " ", t)
    brutas = re.findall(r"(?<![\w@])@\{([^}]+)\}|(?<![\w@])@([\w][\w:.#$%&+?<>~/-]*)", t)
    out = []
    for a, b in brutas:
        k = (a or b).rstrip(".:;,-")
        out.append(k)
    return out


def conferir_citacoes(nome, texto, chaves, rel):
    faltam = Counter(k for k in citacoes(texto) if not k.startswith(PREFIXOS_REF) and k not in chaves)
    for k, n in sorted(faltam.items()):
        rel.add("Estrutura: citações", "FALHA", f"{nome}: @{k} não existe nos .bib (×{n})")
    if not faltam:
        rel.add("Estrutura: citações", "OK", f"{nome}: todas as @chaves existem nos .bib")


def definicoes(texto, rot):
    t = sem_comentarios_e_codigo(texto)
    defs = {}
    for i, l in enumerate(t.split("\n")):
        for m in re.finditer(r"\{[^{}\n]*#((?:fig|tbl|sec|qdr)-[\w-]+)[^{}\n]*\}", l):
            tipo = "titulo" if re.match(r"^#{1,6}\s", l) else "outro"
            numerada = not re.search(r"\.unnumbered\b|(?<![\w-])-(?=[\s}])", m.group(0))
            defs.setdefault(m.group(1), (i + 1, tipo, numerada))
        m = re.match(r"^#\|\s*label:\s*((?:fig|tbl)-[\w-]+)", l)
        if m:
            defs.setdefault(m.group(1), (i + 1, "outro", True))
        m = re.match(r"^@@(FIGURA|TABELA)\s+(\w+)@@\s*$", l)
        if m:
            mapa = rot.get("figuras" if m.group(1) == "FIGURA" else "tabelas") or {}
            if m.group(2) in mapa:
                defs.setdefault(mapa[m.group(2)], (i + 1, "marcador", True))
    return defs


def conferir_rotulos(nome, texto, rot, rel, suplemento_ids=None):
    contrato = {"fig": set((rot.get("figuras") or {}).values()), "tbl": set((rot.get("tabelas") or {}).values()),
                "qdr": set((rot.get("quadros") or {}).values()), "sec": set(rot.get("secoes") or [])}
    sem_numero = set(rot.get("ancoras_sem_numero") or [])
    defs = definicoes(texto, rot)
    refs = Counter(k for k in citacoes(texto) if k.startswith(("fig-", "tbl-", "sec-", "qdr-")))
    falhou = False
    for ref, n in sorted(refs.items()):
        tipo = ref.split("-", 1)[0]
        if ref not in contrato[tipo]:
            rel.add("Estrutura: rótulos e seções", "FALHA", f"{nome}: @{ref} não está em revista/rotulos.yml (×{n})")
            falhou = True
        if ref not in defs:
            rel.add("Estrutura: rótulos e seções", "FALHA", f"{nome}: @{ref} citado e não definido no documento")
            falhou = True
        elif tipo == "sec":
            ln, onde, numerada = defs[ref]
            if onde != "titulo" or not numerada or ref in sem_numero:
                rel.add("Estrutura: rótulos e seções", "FALHA", f"{nome}: @{ref} aponta para seção sem número "
                                                                f"(linha {ln}); use [texto](#{ref})")
                falhou = True
    for ref, (ln, _, _) in sorted(defs.items()):
        tipo = ref.split("-", 1)[0]
        if ref not in contrato[tipo] and ref not in sem_numero:
            rel.add("Estrutura: rótulos e seções", "AVISO", f"{nome}: rótulo {ref} (linha {ln}) fora do contrato rotulos.yml")
    ancoras_doc = set(re.findall(r"\{[^{}\n]*#([\w-]+)", sem_comentarios_e_codigo(texto)))
    for m in re.finditer(r"\]\(#([\w-]+)\)", texto):
        if m.group(1) not in ancoras_doc:
            rel.add("Estrutura: rótulos e seções", "AVISO", f"{nome}: link para #{m.group(1)} sem âncora no documento")
    sup_contrato = set(rot.get("suplemento") or [])
    for m in re.finditer(r"suplemento\.html#([\w-]+)", texto):
        if m.group(1) not in sup_contrato:
            rel.add("Estrutura: rótulos e seções", "FALHA", f"{nome}: link suplemento.html#{m.group(1)} fora do contrato")
            falhou = True
        elif suplemento_ids is not None and m.group(1) not in suplemento_ids:
            rel.add("Estrutura: rótulos e seções", "FALHA", f"{nome}: suplemento.html#{m.group(1)} não definido no suplemento")
            falhou = True
    if not falhou:
        rel.add("Estrutura: rótulos e seções", "OK", f"{nome}: {sum(refs.values())} referências cruzadas conferidas")


# =============================================================== proibições
PROIBIDOS_TEXTO = [
    (r"Neutro", 0, "\"Neutro\""),
    (r"sem efeito", re.I, "\"sem efeito\""),
    (r"benéfic", re.I, "\"benéfic\""),
    (r"\bdanos", re.I, "\"danos\""),
    (r"significativ", re.I, "\"significativ\""),
    (r"\u2014", 0, "travessão"),
    (r"revis(?:ão|ões|ad[oa]s?)\s+por\s+pares", re.I, "\"revisão/revisado por pares\""),
]
PROIBIDOS_BRUTO = [(r"\]\(\.\./", 0, "\"](../\""), (r"column-", 0, "\"column-\"")]


def conferir_proibicoes(nome, texto, rel):
    n0 = sum(1 for _ in rel.itens.get("Proibições", []))
    corpo = re.sub(r"<!--.*?-->", _apaga, sem_yaml(texto), flags=re.S)
    sem_codigo = sem_comentarios_e_codigo(texto)
    for alvo, padroes in ((sem_codigo, PROIBIDOS_TEXTO), (corpo, PROIBIDOS_BRUTO)):
        for p, fl, rot in padroes:
            for i, l in enumerate(alvo.split("\n")):
                for m in re.finditer(p, l, fl):
                    rel.add("Proibições", "FALHA", f"{nome} linha {i + 1}: {rot}: …{l[max(0, m.start() - 40):m.end() + 40]}…")
    prosa = re.sub(r"\]\([^)\n]*\)|<https?://[^>\s]+>|https?://[^\s)>\]]+", " ", sem_codigo)
    for i, l in enumerate(prosa.split("\n")):
        if re.match(r"^:\s", l):
            continue  # legenda de tabela
        for m in re.finditer(r"\b\d\d-[a-z]+/", l):
            rel.add("Proibições", "FALHA", f"{nome} linha {i + 1}: caminho de arquivo em texto corrido: "
                                           f"…{l[max(0, m.start() - 40):m.end() + 40]}…")
    if sum(1 for _ in rel.itens.get("Proibições", [])) == n0:
        rel.add("Proibições", "OK", f"{nome}: nenhum termo proibido")


# =============================================================== revisões anteriores
VERBOS = (r"\b(?:conclu(?:i|em|iu|íram|iram|ía|íam)|mostr(?:a|am|ou|aram|ava|avam)|encontr(?:a|am|ou|aram|ava|avam)|"
          r"apont(?:a|am|ou|aram|ava|avam)|indic(?:a|am|ou|aram|ava|avam)|suger(?:e|em|iu|iram|ia|iam)|"
          r"revel(?:a|am|ou|aram|ava|avam)|conclude[sd]?|show(?:s|ed)?|find(?:s)?|found|point(?:s|ed)|"
          r"indicate[sd]?|suggest(?:s|ed)?|reveal(?:s|ed)?)\b")


def conferir_revisoes(nome, texto, rel):
    chaves_rev = {}
    for b in BIBS:
        if not b.exists():
            continue
        for m in re.finditer(r"^@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=^@|\Z)", ler(b), flags=re.M | re.S):
            k, corpo = m.group(1), m.group(2)
            autor = re.search(r"author\s*=\s*[{\"](.*?)[}\"],?\s*$", corpo, flags=re.M | re.I)
            for sobrenome in ("Hardmeier", "Moy", "Barnfield"):
                if k.lower().startswith(sobrenome.lower()) or (autor and re.search(rf"\b{sobrenome}\b", autor.group(1))):
                    chaves_rev[k] = sobrenome
    corpo = sem_comentarios_e_codigo(texto)
    frases = []
    for par in re.split(r"\n\s*\n", corpo):
        for f in re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ@\[*(])", par):
            citadas = {k for k in chaves_rev if re.search(rf"@{re.escape(k)}(?![\w])", f)}
            if citadas and re.search(VERBOS, f, re.I):
                frases.append((citadas, norm_espacos(f)))
    if not REVISOES.exists():
        rel.add("Revisões anteriores", "AVISO", f"{REVISOES.relative_to(R)} ainda não existe; "
                                                f"{len(frases)} frase(s) com verbo de conclusão sobre revisões anteriores")
        for citadas, f in frases:
            rel.add("Revisões anteriores", "AVISO", f"{nome}: {sorted(citadas)}: «{f[:160]}»")
        return
    doc = ler(REVISOES)
    secoes = re.split(r"(?m)^(?=#{1,6}\s)", doc)
    verificada = {}
    for sobrenome in ("Hardmeier", "Moy", "Barnfield"):
        sec = [s for s in secoes if re.match(r"#{1,6}\s[^\n]*" + sobrenome, s)]
        verificada[sobrenome] = bool(sec) and not re.search(r"não\s+verificad", sec[0], re.I)
    rel.add("Revisões anteriores", "INFO", "verificadas em revisoes_anteriores.md: "
            + ", ".join(f"{k} = {'sim' if v else 'não'}" for k, v in verificada.items()))
    ok = True
    for citadas, f in frases:
        nao = sorted(k for k in citadas if not verificada.get(chaves_rev[k]))
        if nao:
            ok = False
            rel.add("Revisões anteriores", "FALHA", f"{nome}: conclusão atribuída a obra não verificada {nao}: «{f[:160]}»")
    if ok:
        rel.add("Revisões anteriores", "OK", f"{nome}: {len(frases)} frase(s) com verbo de conclusão, todas sobre obras verificadas")


# =============================================================== relato
def contar_palavras(t):
    return len(re.findall(r"[0-9A-Za-zÀ-ÿ]+(?:[-'’][0-9A-Za-zÀ-ÿ]+)*", t))


def relato(nome, texto, rx_chaves, rel):
    n = texto.count(MARCADOR_AUTOR)
    rel.add("Relato", "INFO", f"{nome}: {n} marcador(es) \"{MARCADOR_AUTOR}\"")
    t = sem_comentarios_e_codigo(texto)
    t = re.sub(r"^:::.*$|^@@.*@@\s*$", "", t, flags=re.M)
    t = re.sub(r"\{(?=[#.]|[\w-]+=)[^{}\n]*\}", " ", t)
    t = re.sub(r"\]\([^)\n]*\)", "]", t)
    linhas = [l for l in t.split("\n") if not l.lstrip().startswith("|") and not re.match(r"^:\s", l)]
    secoes, atual = [], ("(antes do primeiro título)", [])
    for l in linhas:
        m = re.match(r"^#\s+(.*)$", l)
        if m:
            secoes.append(atual)
            atual = (norm_espacos(m.group(1)), [])
        else:
            atual[1].append(l)
    secoes.append(atual)
    total = 0
    for titulo, ls in secoes:
        w = contar_palavras("\n".join(ls))
        if w or not titulo.startswith("("):
            total += w
            rel.add("Relato", "INFO", f"{nome}: {w:6d} palavras  # {titulo}")
    rel.add("Relato", "INFO", f"{nome}: {total:6d} palavras no total (prosa; sem tabelas e legendas de tabela)")
    for d in divs(sem_comentarios_e_codigo(texto)):
        if re.search(r"\.(mensagens-principais|resumo)\b", d["attrs"]):
            w = contar_palavras(re.sub(r"^#.*$", "", d["conteudo"], flags=re.M))
            rel.add("Relato", "INFO", f"{nome}: {w:6d} palavras no bloco ::: {{{d['attrs'].strip('{}')}}}")


# =============================================================== principal
def main():
    ap = argparse.ArgumentParser(description="Trava da reestruturação do documento final.")
    ap.add_argument("--v1", default="09-documento-final/_revisao_final_v1_oqf.qmd")
    ap.add_argument("--novo", default="09-documento-final/revisao_final.qmd")
    ap.add_argument("--suplemento", default=None)
    a = ap.parse_args()
    rel = Relatorio()

    p_v1, p_novo = resolver(a.v1), resolver(a.novo)
    for p in (p_v1, p_novo):
        if not p.exists():
            sys.exit(f"arquivo não encontrado: {p}")
    if a.suplemento:
        p_sup = resolver(a.suplemento)
        if not p_sup.exists():
            sys.exit(f"arquivo não encontrado: {p_sup}")
    else:
        p_sup = D / "suplemento.qmd"
        if not p_sup.exists():
            rel.add("Relato", "AVISO", "suplemento.qmd ausente; não conferido")
            p_sup = None
    if not CELULAS.exists():
        sys.exit("revista/celulas.json não existe; rode 09-documento-final/revista/gerar_celulas.py")

    v1, novo = ler(p_v1), ler(p_novo)
    sup = ler(p_sup) if p_sup else None
    chaves, anos_bib = chaves_bib(BIBS, rel)
    chaves_incl, anos_incl = set(), set()
    for r in csv.DictReader(open(INCLUIDOS, encoding="utf-8-sig")):
        chaves_incl.add(r["chave"])
        if re.fullmatch(r"(?:19|20)\d\d", r.get("ano", "")):
            anos_incl.add(int(r["ano"]))
    rx_chaves = regex_chaves(chaves | chaves_incl)
    rot = ler_rotulos()
    celulas = json.load(open(CELULAS, encoding="utf-8"))["celulas"]

    # lista branca, datas e anos
    v1_limpo = limpar(v1, rx_chaves)
    v1_ing = linhas_ingles(v1)
    v1_sem_datas = RX_DATA.sub(" ", v1_limpo)
    lb = montar_lista_branca(RX_DATA_CURTA.sub(" ", v1_sem_datas), v1_ing, rx_chaves, rel)
    datas_ok = datas_permitidas(v1)
    anos_v1 = {int(v) for _, tok, v, neg, dec, pct in tokens_numericos(v1_sem_datas, v1_ing)
               if v is not None and not dec and not pct and re.fullmatch(r"(?:19|20)\d\d", tok)}
    anos_v1 |= {c for _, _, c in datas_ok}
    anos_ok = anos_v1 | anos_bib | anos_incl

    docs = [("novo", novo)] + ([("suplemento", sup)] if sup is not None else [])
    total_nums = 0
    for nome, texto in docs:
        total_nums += conferir_datas_e_numeros(nome, texto, limpar(texto, rx_chaves), linhas_ingles(texto),
                                               lb, datas_ok, anos_ok, rel)
    if not any(n == "FALHA" for n, _ in rel.itens.get("Datas", [])):
        rel.add("Datas", "OK", f"datas conferidas contra {len(datas_ok)} datas permitidas")
    if not any(n in ("FALHA", "AVISO") for n, _ in rel.itens.get("Números", [])):
        rel.add("Números", "OK", f"{total_nums} números conferidos contra a lista branca ({len(lb.v)} valores)")
    else:
        rel.add("Números", "INFO", f"{total_nums} números conferidos contra a lista branca ({len(lb.v)} valores)")

    conferir_celulas("novo", novo, celulas, rx_chaves, rel, exigir=True)
    if sup is not None:
        conferir_celulas("suplemento", sup, celulas, rx_chaves, rel, exigir=False)

    conferir_callouts(novo, v1, rel)
    conferir_apendice(novo, rel)
    sup_ids = set(re.findall(r"\{[^{}\n]*#([\w-]+)", sup)) if sup is not None else None
    for nome, texto in docs:
        conferir_citacoes(nome, texto, chaves, rel)
    conferir_rotulos("novo", novo, rot, rel, sup_ids)
    if sup is not None:
        faltam = [s for s in (rot.get("suplemento") or []) if s not in sup_ids]
        for s in faltam:
            rel.add("Estrutura: rótulos e seções", "AVISO", f"suplemento: seção #{s} do contrato não definida")
    for nome, texto in docs:
        conferir_proibicoes(nome, texto, rel)
    conferir_revisoes("novo", novo, rel)
    for nome, texto in docs:
        relato(nome, texto, rx_chaves, rel)

    rel.imprimir()
    sys.exit(1 if rel.falhas() else 0)


if __name__ == "__main__":
    main()
