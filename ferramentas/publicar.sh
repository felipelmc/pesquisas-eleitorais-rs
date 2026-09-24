#!/usr/bin/env bash
# Gera a versão publicada no GitHub Pages (pasta docs/), a partir da raiz do projeto:
#   bash ferramentas/publicar.sh
# Produtos (HTML autocontido: CSS, JS, fontes e figuras embutidos):
# - docs/index.html                vitrine interativa (09-documento-final/vitrine/)
# - docs/revisao.html|.pdf|.docx   artigo (09-documento-final/revisao_final.qmd, montado do esqueleto)
# - docs/suplemento.html|.pdf      material suplementar (09-documento-final/suplemento.qmd)
# - docs/linguagem-simples.html    resumo em linguagem simples (09-documento-final/linguagem_simples.qmd)
# - docs/relatorio-tecnico.html|.docx  manuscrito PRISMA (07-relatorio/relatorio.qmd)
# - docs/revisao-humana.html       guia 08-revisao-humana/README.md
# Nada de dados brutos, fichas ou PDFs de terceiros vai para docs/. A pasta é limpa por lista branca.
set -euo pipefail
raiz="$(cd "$(dirname "$0")/.." && pwd)"
docs="$raiz/docs"
fd="$raiz/09-documento-final"
export PYTHONDONTWRITEBYTECODE=1

# 0. versões
qv="$(quarto --version)"
[[ "$qv" == 1.9.* ]] || { echo "Quarto $qv; o projeto foi montado com 1.9.35" >&2; exit 1; }
quarto typst --version | grep -q "0.14" || { echo "Typst embutido no Quarto não é 0.14" >&2; exit 1; }
export TYPST_IGNORE_SYSTEM_FONTS=true TYPST_IGNORE_EMBEDDED_FONTS=true
export SOURCE_DATE_EPOCH="$(git -C "$raiz" log -1 --format=%ct -- 09-documento-final/)"

# 1. insumos gerados e montagem (sem digitar números)
cd "$raiz"
python3 09-documento-final/revista/gerar_celulas.py
python3 09-documento-final/revista/gerar_numeros_v2.py
python3 09-documento-final/revista/preparar_referencias.py
python3 09-documento-final/revista/gerar_rotulos_autor_ano.py
python3 09-documento-final/revista/figuras/preparar_dados_figuras.py
Rscript 09-documento-final/revista/figuras/gerar_figuras.R
python3 09-documento-final/revista/figuras/verificar_figuras.py
python3 09-documento-final/montar_revisao_final.py
python3 09-documento-final/montar_suplemento.py
python3 09-documento-final/conferir_reestruturacao.py

# 2. artigo: PDF (Typst), HTML e .docx
cd "$fd"
quarto render revisao_final.qmd --to typst -M keep-typ:false --output revisao.pdf --output-dir "$docs" 2>&1 | tee /tmp/rs_render_revisao.log
quarto render revisao_final.qmd --to typst -M keep-typ:false --output _revisao_repro.pdf > /dev/null 2>&1
python3 revista/verificar_pdf.py "$docs/revisao.pdf" --artigo --log /tmp/rs_render_revisao.log --segundo _revisao_repro.pdf
rm -f _revisao_repro.pdf
quarto render revisao_final.qmd --to html --output revisao.html --output-dir "$docs"
quarto render revisao_final.qmd --to docx --output revisao.docx --output-dir "$docs"

# 3. suplemento e linguagem simples
quarto render suplemento.qmd --to typst -M keep-typ:false --output suplemento.pdf --output-dir "$docs" 2>&1 | tee /tmp/rs_render_sup.log
python3 revista/verificar_pdf.py "$docs/suplemento.pdf" --suplemento --log /tmp/rs_render_sup.log
quarto render suplemento.qmd --to html --output suplemento.html --output-dir "$docs"
quarto render linguagem_simples.qmd --to html --output linguagem-simples.html --output-dir "$docs"

# 4. relatório técnico e guia da revisão humana
cd "$raiz/07-relatorio"
quarto render relatorio.qmd --to html -M embed-resources:true -M self-contained-math:true \
  --output relatorio-tecnico.html --output-dir "$docs"
quarto render relatorio.qmd --to docx --output relatorio-tecnico.docx --output-dir "$docs"
cd "$raiz/08-revisao-humana"
quarto pandoc README.md --standalone --embed-resources --toc \
  --metadata title="Revisão humana: o que falta e como fazer" --metadata lang=pt-BR \
  -o "$docs/revisao-humana.html"

# 5. barra de navegação, aviso de rascunho, noindex e Open Graph nas páginas de documento
python3 "$raiz/ferramentas/barra_publicacao.py" "$docs" "$raiz/07-relatorio/_pendencias_abertas.json"

# 6. vitrine (por último, para conferir as âncoras dos documentos)
cd "$raiz"
python3 09-documento-final/vitrine/exportar_dados.py
python3 09-documento-final/vitrine/montar_vitrine.py
python3 09-documento-final/vitrine/qa/testar_sanitizacao.py "$docs"
python3 09-documento-final/vitrine/qa/testar_textos.py
python3 09-documento-final/vitrine/qa/checar_links.py "$docs"
python3 09-documento-final/vitrine/qa/verificar_licencas.py

# 7. docs/ só com a lista branca
touch "$docs/.nojekyll"
python3 - "$docs" <<'EOF'
import os, shutil, sys
docs = sys.argv[1]
permitidos = {".nojekyll", "index.html", "revisao.html", "revisao.pdf", "revisao.docx", "suplemento.html",
              "suplemento.pdf", "linguagem-simples.html", "relatorio-tecnico.html", "relatorio-tecnico.docx",
              "revisao-humana.html", "CNAME"}
for nome in os.listdir(docs):
    if nome not in permitidos:
        p = os.path.join(docs, nome)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
        print("removido de docs/:", nome)
EOF
ls -la "$docs"
