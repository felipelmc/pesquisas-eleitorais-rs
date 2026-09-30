"""Junta o artigo e os apêndices num PDF só (a versão de entrega é um PDF autocontido; Emenda 7).

USO:  python3 ferramentas/juntar_pdf.py <artigo.pdf> <apendices.pdf> <saida.pdf>

Os apêndices são compilados à parte (página deitada, pipeline de montar_suplemento.py), com `continuacao: true` e
`pagina-inicial` = páginas do artigo + 1, para a numeração seguir contínua. Este script só concatena: mantém os
metadados do artigo (título, autor, palavras-chave), o sumário lateral (outline) dos dois arquivos e acrescenta um item
"Apêndices" no sumário, apontando para a primeira página deles.
"""
import logging
import sys

from pypdf import PdfReader, PdfWriter

logging.getLogger("pypdf").setLevel(logging.ERROR)  # avisos de tamanho de anotação ao juntar; os links ficam

artigo, apendices, saida = sys.argv[1:4]
ra, rb = PdfReader(artigo), PdfReader(apendices)
w = PdfWriter()
w.append(ra, import_outline=True)
inicio = len(w.pages)
w.append(rb, outline_item="Apêndices", import_outline=True)
meta = {k: v for k, v in (ra.metadata or {}).items() if isinstance(v, str)}
w.add_metadata(meta)
with open(saida, "wb") as f:
    w.write(f)
print(f"{saida}: {len(ra.pages)} páginas do artigo + {len(rb.pages)} dos apêndices (a partir da p. {inicio + 1})")
