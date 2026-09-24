"""Trava dos passes de estilo: compara números, chaves de citação, callouts e rótulos de certeza entre duas
versões do documento final. A saída tem de ser vazia (código 0) para o passe ser aceito.

USO:  python3 09-documento-final/conferir_numeros.py <antes.qmd> <depois.qmd>
Compara multiconjuntos de: números (inteiros e decimais, com vírgula ou ponto, sinais e %), @chaves,
títulos de callout "Pendente de revisão humana", IDs de pendência (P0xx) e frases de certeza
(muito baixa, baixa, moderada, alta como palavras após "certeza"). Ignora o bloco YAML.
"""
import re, sys
from collections import Counter

def sem_yaml(s):
    if s.startswith("---"):
        fim = s.find("\n---", 3)
        if fim != -1:
            return s[fim + 4:]
    return s

def extrair(s):
    s = sem_yaml(s)
    return {
        "numeros": Counter(re.findall(r"[−-]?\d+(?:[.,]\d+)*%?", s)),
        "chaves": Counter(re.findall(r"@([A-Za-z][\w:-]*\w)", s)),
        "pendencias": Counter(re.findall(r"\bP0\d\d\b", s)),
        "callouts": Counter(re.findall(r"Pendente de revisão humana", s)),
        "certezas": Counter(re.findall(r"certeza (muito baixa|baixa|moderada|alta)", s)),
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
