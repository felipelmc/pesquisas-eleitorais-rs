"""Trava dos passes de estilo: compara números, chaves de citação, callouts, rótulos de certeza e a estrutura entre
duas versões do documento final. A saída tem de ser vazia (código 0) para o passe ser aceito.

USO:  python3 09-documento-final/conferir_numeros.py <antes.qmd> <depois.qmd>
Compara multiconjuntos de:
  numeros     inteiros e decimais, com vírgula ou ponto, sinais e %; ignora o YAML, as linhas de cerca de Div
              (^:::) e os atributos {#...}/{.…}/{chave=…}
  chaves      @chaves (inclui @fig-/@tbl-/@sec-/@qdr-)
  pendencias  IDs P0xx
  callouts    títulos "Pendente de revisão humana"
  certezas    "certeza muito baixa|baixa|moderada|alta"
  titulos_id  títulos com ID (^#+ ... {#id ...}), como nível + ID + classes
  divs        classes e atributos das cercas de Div (::: {.classe ...})
  rotulos     rótulos {#fig-...}, {#tbl-...} e {#qdr-...}
  enunciados  spans [texto]{.enunciado cel="Cxx"}: conteúdo (espaços normalizados) + cel, que não podem mudar
  marcadores  "[A confirmar pelo autor]"
"""
import re
import sys
from collections import Counter

ATRIBUTO = r"\{(?=[#.]|[\w-]+=)[^{}\n]*\}"
SPAN = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\{([^{}]*\.enunciado\b[^{}]*)\}")


def sem_yaml(s):
    if s.startswith("---"):
        fim = s.find("\n---", 3)
        if fim != -1:
            return s[fim + 4:]
    return s


def espacos(s):
    return re.sub(r"\s+", " ", s.replace(" ", " ")).strip()


def titulos_id(s):
    out = []
    for m in re.finditer(r"^(#+)\s.*?(\{[^{}\n]*#[\w-]+[^{}\n]*\})\s*$", s, flags=re.M):
        attrs = m.group(2)
        ident = re.search(r"#([\w-]+)", attrs).group(1)
        classes = " ".join(sorted(re.findall(r"(?<![\w-])\.[\w-]+|(?<![\w-])-(?=[\s}])", attrs)))
        out.append(f"{m.group(1)} #{ident} {classes}".strip())
    return out


def extrair(s):
    s = sem_yaml(s)
    s_num = re.sub(r"^:::.*$", "", s, flags=re.M)
    s_num = re.sub(ATRIBUTO, " ", s_num)
    return {
        "numeros": Counter(re.findall(r"[−-]?\d+(?:[.,]\d+)*%?", s_num)),
        "chaves": Counter(re.findall(r"@([A-Za-z][\w:-]*\w)", s)),
        "pendencias": Counter(re.findall(r"\bP0\d\d\b", s)),
        "callouts": Counter(re.findall(r"Pendente de revisão humana", s)),
        "certezas": Counter(re.findall(r"certeza (muito baixa|baixa|moderada|alta)", s)),
        "titulos_id": Counter(titulos_id(s)),
        "divs": Counter(espacos(m) for m in re.findall(r"^:{3,}\s*(\{[^{}\n]*\}|[^\s:{][^\n]*?)\s*$", s, flags=re.M)),
        "rotulos": Counter(re.findall(r"\{[^{}\n]*#((?:fig|tbl|qdr)-[\w-]+)", s)),
        "enunciados": Counter(
            (re.search(r"cel\s*=\s*\"?([\w]+)\"?", a).group(1) if re.search(r"cel\s*=", a) else "sem cel") + " | " + espacos(t)
            for t, a in SPAN.findall(s)),
        "marcadores": Counter(re.findall(r"\[A confirmar pelo autor\]", s)),
    }


a, b = (extrair(open(p, encoding="utf-8").read()) for p in sys.argv[1:3])
problemas = 0
for k in a:
    faltam, sobram = a[k] - b[k], b[k] - a[k]
    if faltam or sobram:
        problemas += 1
        print(f"[{k}] sumiram: {dict(faltam)}")
        print(f"[{k}] apareceram: {dict(sobram)}")
sys.exit(1 if problemas else 0)
