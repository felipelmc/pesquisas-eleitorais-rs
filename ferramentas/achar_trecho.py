"""Para cada citação reprovada no gate, acha na camada de texto do PDF o trecho literal mais próximo.

Uso: python3 achar_trecho.py <verificacao_citacoes.csv> <pasta_pdfs>
Imprime: ficha | variavel | pagina_citada | pagina_sugerida | score | citacao | sugestao
"""
import csv, sys, re, difflib
import pymupdf

def norm_ws(s):
    return re.sub(r'\s+', ' ', s).strip()

def melhor(cit, texto):
    palavras = texto.split()
    n = len(cit.split())
    best = (0.0, '')
    for k in (n - 1, n, n + 1):
        if k < 2:
            continue
        for i in range(0, max(1, len(palavras) - k + 1)):
            cand = ' '.join(palavras[i:i + k])
            r = difflib.SequenceMatcher(None, cit.lower(), cand.lower()).ratio()
            if r > best[0]:
                best = (r, cand)
    return best

rows = [r for r in csv.DictReader(open(sys.argv[1], encoding='utf-8-sig')) if r['status'] != 'OK']
cache = {}
for r in rows:
    ch = r['citekey']
    if ch not in cache:
        cache[ch] = [norm_ws(p.get_text()) for p in pymupdf.open(f"{sys.argv[2]}/{ch}.pdf")]
    pags = cache[ch]
    p = int(r['pagina_indicada'])
    best = (0.0, '', 0)
    for q in range(max(1, p - 2), min(len(pags), p + 2) + 1):
        sc, cand = melhor(r['citacao'], pags[q - 1])
        if sc > best[0]:
            best = (sc, cand, q)
    print(f"{r['ficha']} | {r['variavel']} | {p} | {best[2]} | {best[0]:.2f} | {r['citacao']} || {best[1]}")
