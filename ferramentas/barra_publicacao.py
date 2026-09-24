"""Barra de navegação com aviso de rascunho, noindex e Open Graph nas páginas de documento de docs/.

USO:  python3 ferramentas/barra_publicacao.py <docs/> <07-relatorio/_pendencias_abertas.json>
A vitrine (index.html) tem cabeçalho próprio e fica de fora. Idempotente: não injeta duas vezes.
"""
import html
import json
import os
import re
import sys

docs, pend = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
n = pend["n"]

PAGINAS = {
    "revisao.html": "Artigo",
    "suplemento.html": "Material suplementar",
    "linguagem-simples.html": "Em linguagem simples",
    "relatorio-tecnico.html": "Relatório técnico",
    "revisao-humana.html": "Guia da revisão humana",
}
LINKS = [("index.html", "Início"), ("revisao.html", "Artigo"), ("revisao.pdf", "PDF"),
         ("suplemento.html", "Suplemento"), ("linguagem-simples.html", "Em linguagem simples"),
         ("relatorio-tecnico.html", "Relatório técnico"),
         ("revisao-humana.html", f"Guia da revisão humana ({n} pendências)")]


def barra(atual):
    itens = []
    for href, rot in LINKS:
        if href == atual:
            itens.append(f'<strong style="font-weight:600">{html.escape(rot)}</strong>')
        else:
            itens.append(f'<a href="{href}" style="color:#1f4e79;text-decoration:none">{html.escape(rot)}</a>')
    aviso = ('<span style="color:#b91c1c;font-weight:700;letter-spacing:.03em">RASCUNHO NÃO VALIDADO</span>'
             if n > 0 else "")
    return ('<div id="barra-nav" role="navigation" aria-label="Documentos da revisão" '
            'style="position:relative;z-index:1100;background:#fbfaf7;border-bottom:1px solid #d8d6cf;'
            'padding:8px 18px;font:500 14px/1.5 \'Fira Sans\',system-ui,sans-serif;display:flex;'
            'flex-wrap:wrap;gap:6px 18px;align-items:center">'
            + aviso + " " + " · ".join(itens) + "</div>")


def cabeca(titulo):
    t = html.escape(f"{titulo} (rascunho não validado)")
    return ('<meta name="robots" content="noindex, nofollow">'
            f'<meta property="og:title" content="{t}">'
            '<meta property="og:description" content="Rascunho não validado de revisão sistemática: '
            'pesquisas eleitorais publicadas mudam o voto?">')


for nome, titulo in PAGINAS.items():
    p = os.path.join(docs, nome)
    if not os.path.exists(p):
        print("não existe, pulado:", nome)
        continue
    s = open(p, encoding="utf-8").read()
    if 'id="barra-nav"' not in s:
        i = s.find(">", s.find("<body")) + 1
        s = s[:i] + barra(nome) + s[i:]
    if 'name="robots"' not in s:
        s = re.sub(r"<head([^>]*)>", lambda m: f"<head{m.group(1)}>" + cabeca(titulo), s, count=1)
    open(p, "w", encoding="utf-8").write(s)
    print("barra e metadados:", nome)
