#!/usr/bin/env bash
# Gera a versão publicada no GitHub Pages (pasta docs/), a partir da raiz do projeto:
#   bash docs/publicar.sh
# Páginas (HTML autocontido: CSS, JS e figuras embutidos):
# - docs/index.html: página de entrada (09-documento-final/index.qmd), com as mensagens principais
#   extraídas do próprio documento final
# - docs/revisao.html e revisao.docx: documento final no formato OQF adaptado (09-documento-final/revisao_final.qmd)
# - docs/relatorio-tecnico.html e relatorio-tecnico.docx: manuscrito PRISMA (07-relatorio/relatorio.qmd)
# - docs/revisao-humana.html: o guia 08-revisao-humana/README.md
# Nada de dados brutos, fichas ou PDFs vai para docs/.
set -euo pipefail
raiz="$(cd "$(dirname "$0")/.." && pwd)"
docs="$raiz/docs"

# 1. relatório técnico
cd "$raiz/07-relatorio"
quarto render relatorio.qmd --to html -M embed-resources:true -M self-contained-math:true \
  --output relatorio-tecnico.html --output-dir "$docs"
quarto render relatorio.qmd --to docx --output relatorio-tecnico.docx --output-dir "$docs"

# 2. documento final
cd "$raiz/09-documento-final"
quarto render revisao_final.qmd --to html -M embed-resources:true -M self-contained-math:true \
  --output revisao.html --output-dir "$docs"
quarto render revisao_final.qmd --to docx --output revisao.docx --output-dir "$docs"

# 3. página de entrada, com as mensagens principais do documento final
python3 - "$raiz/09-documento-final/revisao_final.qmd" "$raiz/09-documento-final/_mensagens_principais.md" <<'EOF'
import re, sys
s = open(sys.argv[1], encoding="utf-8").read()
m = re.search(r"^#\s+Mensagens principais[^\n]*\n(.*?)(?=^#\s)", s, flags=re.S | re.M)
if not m:
    sys.exit("seção 'Mensagens principais' não encontrada em revisao_final.qmd")
corpo = m.group(1).strip()
# citações viram texto simples na página de entrada (a página não tem bibliografia)
corpo = re.sub(r"\s*\[@[^\]]+\]", "", corpo)
corpo = re.sub(r"@([A-Za-z][\w-]*\d{4}\w*)", r"\1", corpo)
open(sys.argv[2], "w", encoding="utf-8").write(corpo + "\n\nOs números e a certeza de cada mensagem estão na [revisão final](revisao.html).\n")
EOF
quarto render index.qmd --output index.html --output-dir "$docs"

# 4. guia da revisão humana
cd "$raiz/08-revisao-humana"
quarto pandoc README.md --standalone --embed-resources --toc \
  --metadata title="Revisão humana: o que falta e como fazer" --metadata lang=pt-BR \
  -o "$docs/revisao-humana.html"

# 5. barra de navegação e aviso de rascunho nas páginas de documento
python3 - "$docs" "$raiz/07-relatorio/_pendencias_abertas.json" <<'EOF'
import sys, json, os
docs, n = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))["n"]
barra = ('<div id="barra-nav" style="background:#fff3cd;border-bottom:1px solid #e0c36b;padding:8px 16px;font-size:0.95rem">'
         '<strong>Rascunho não validado.</strong> '
         '<a href="index.html">Início</a> · <a href="revisao.html">Revisão final</a> · '
         '<a href="relatorio-tecnico.html">Relatório técnico</a> · '
         f'<a href="revisao-humana.html">Guia da revisão humana ({n} pendências)</a></div>')
for nome in ("revisao.html", "relatorio-tecnico.html", "revisao-humana.html"):
    p = os.path.join(docs, nome)
    s = open(p, encoding="utf-8").read()
    if 'id="barra-nav"' not in s:
        i = s.find(">", s.find("<body")) + 1
        s = s[:i] + barra + s[i:]
        open(p, "w", encoding="utf-8").write(s)
EOF

touch "$docs/.nojekyll"
rm -rf "$docs/index_files" "$docs/relatorio_files" "$docs/revisao_final_files" "$docs/prisma.png" "$docs/relatorio.docx"
ls -la "$docs"
