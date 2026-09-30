"""Barra de navegação e Open Graph nas páginas de documento de docs/ (e aviso de rascunho e noindex fora da versão final).

USO:  python3 ferramentas/barra_publicacao.py <docs/> <07-relatorio/_pendencias_abertas.json>
A vitrine (index.html) tem cabeçalho próprio e fica de fora. Idempotente: não injeta duas vezes.

Versão final (`estado: final` em 09-documento-final/revista/_revista.yml, Emenda 7): sem o aviso "RASCUNHO NÃO
VALIDADO" na barra e sem noindex; a marca de rascunho fica só na declaração de uso de IA do artigo (R7.23).
Fora da versão final, com pendências abertas, a barra traz o aviso e as páginas levam noindex, como antes.
"""
import html
import json
import os
import re
import sys

docs, pend = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
n = pend["n"]
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_rev = open(os.path.join(RAIZ, "09-documento-final/revista/_revista.yml"), encoding="utf-8").read()
_m = re.search(r"(?m)^estado:\s*(\w+)", _rev)
FINAL = bool(_m and _m.group(1) == "final")
RASCUNHO = n > 0 and not FINAL

PAGINAS = {
    "revisao.html": "Artigo",
    "apendices.html": "Apêndices",
    "linguagem-simples.html": "Em linguagem simples",
}
LINKS = [("index.html", "Início"), ("revisao.html", "Artigo"), ("revisao.pdf", "PDF (artigo e apêndices)"),
         ("apendices.html", "Apêndices"), ("linguagem-simples.html", "Em linguagem simples"),
         ("pacote-replicacao.zip", "Pacote de replicação")]
DESCRICAO = ("Síntese sistemática de evidências conduzida com agentes de IA: pesquisas eleitorais publicadas "
             "mudam o voto?")


def barra(atual):
    itens = []
    for href, rot in LINKS:
        if href == atual:
            itens.append(f'<strong style="font-weight:600">{html.escape(rot)}</strong>')
        else:
            itens.append(f'<a href="{href}" style="color:#1f4e79;text-decoration:none">{html.escape(rot)}</a>')
    aviso = ('<span style="color:#b91c1c;font-weight:700;letter-spacing:.03em">RASCUNHO NÃO VALIDADO</span> '
             if RASCUNHO else "")
    return ('<div id="barra-nav" role="navigation" aria-label="Documentos da síntese" '
            'style="position:relative;z-index:1100;background:#fbfaf7;border-bottom:1px solid #d8d6cf;'
            'padding:8px 18px;font:500 14px/1.5 \'Fira Sans\',system-ui,sans-serif;display:flex;'
            'flex-wrap:wrap;gap:6px 18px;align-items:center">'
            + aviso + " · ".join(itens) + "</div>")


def cabeca(titulo):
    t = html.escape(f"{titulo} (rascunho não validado)" if RASCUNHO else titulo)
    robots = '<meta name="robots" content="noindex, nofollow">' if RASCUNHO else ""
    return (robots + f'<meta property="og:title" content="{t}">'
            f'<meta property="og:description" content="{html.escape(DESCRICAO)}">')


for nome, titulo in PAGINAS.items():
    p = os.path.join(docs, nome)
    if not os.path.exists(p):
        print("não existe, pulado:", nome)
        continue
    s = open(p, encoding="utf-8").read()
    if 'id="barra-nav"' not in s:
        i = s.find(">", s.find("<body")) + 1
        s = s[:i] + barra(nome) + s[i:]
    if 'property="og:title"' not in s:
        s = re.sub(r"<head([^>]*)>", lambda m: f"<head{m.group(1)}>" + cabeca(titulo), s, count=1)
    open(p, "w", encoding="utf-8").write(s)
    print("barra e metadados:", nome)
