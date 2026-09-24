#!/usr/bin/env bash
# Gera a versão publicada no GitHub Pages (pasta docs/), a partir da raiz do projeto:
#   bash docs/publicar.sh
# - docs/index.html: o relatório em HTML autocontido (CSS, JS e figuras embutidos)
# - docs/relatorio.docx: cópia do .docx renderizado em 07-relatorio/
# - docs/revisao-humana.html: o guia 08-revisao-humana/README.md em HTML
# Nada de dados brutos, fichas ou PDFs vai para docs/.
set -euo pipefail
raiz="$(cd "$(dirname "$0")/.." && pwd)"
cd "$raiz/07-relatorio"
quarto render relatorio.qmd --to html -M embed-resources:true -M self-contained-math:true \
  --output index.html --output-dir "$raiz/docs"
cp relatorio.docx "$raiz/docs/relatorio.docx"
cd "$raiz/08-revisao-humana"
quarto pandoc README.md --standalone --embed-resources --toc \
  --metadata title="Revisão humana: o que falta e como fazer" --metadata lang=pt-BR \
  -o "$raiz/docs/revisao-humana.html"
python3 - "$raiz/docs/index.html" "$raiz/07-relatorio/_pendencias_abertas.json" <<'EOF'
import sys, json
p = sys.argv[1]
n = json.load(open(sys.argv[2], encoding="utf-8"))["n"]
s = open(p, encoding="utf-8").read()
barra = ('<div style="background:#fff3cd;border-bottom:1px solid #e0c36b;padding:8px 16px;font-size:0.95rem">'
         '<strong>Rascunho não validado.</strong> '
         f'<a href="revisao-humana.html">Guia da revisão humana ({n} pendências)</a> · '
         '<a href="relatorio.docx">Baixar .docx</a></div>')
if 'Guia da revisão humana' not in s:
    i = s.find('>', s.find('<body')) + 1
    s = s[:i] + barra + s[i:]
    open(p, "w", encoding="utf-8").write(s)
EOF
touch "$raiz/docs/.nojekyll"
rm -rf "$raiz/docs/index_files" "$raiz/docs/relatorio_files"
ls -la "$raiz/docs"
