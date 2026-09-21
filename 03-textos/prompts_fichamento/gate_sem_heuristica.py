"""Confere as citações de uma ficha com as mesmas funções do verify_citacoes.py, sem a heurística
de 'PDF sem camada de texto' (que dá falso positivo em teses com sumário cheio de pontilhados)."""
import sys, re, os
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.expanduser('~/.claude/skills/fichamento-sistematico/scripts'))
import verify_citacoes as v
ficha, pdf = sys.argv[1:3]
md = open(ficha, encoding='utf-8').read(); fm = v.ler_frontmatter(md)
off = int(re.sub(r"[^0-9\-]", "", fm.get("offset_pagina", "0")) or "0")
pags = v.extrair_paginas(pdf); amostra = " ".join(pags)[:20000]; ne = [c for c in amostra if not c.isspace()]
print('frac_alfa amostra:', round(sum(c.isalpha() for c in ne)/len(ne), 3))
norm = [v.normalizar(p) for p in pags]; ns = [p.replace(' ', '') for p in norm]
ok = 0; ruins = []
for it in v.extrair_citacoes(md):
    q = v.normalizar(it['citacao'])
    alvos = [p + off - 1 for p in it['paginas'] if 0 <= p + off - 1 < len(norm)]
    if any(q and (q in norm[i] or q.replace(' ', '') in ns[i]) for i in alvos): ok += 1
    else: ruins.append((it['variavel'], it['paginas'], it['citacao'][:90]))
print('OK', ok, 'problemas', len(ruins)); [print(' ', r) for r in ruins]
