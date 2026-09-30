#!/usr/bin/env bash
# Gera a versão publicada no GitHub Pages (pasta docs/), a partir da raiz do projeto:
#   bash ferramentas/publicar.sh
# Produtos da versão de entrega (Emenda 7; HTML autocontido: CSS, JS, fontes e figuras embutidos):
# - docs/revisao.pdf               PDF único: artigo (revisao_final.qmd, montado do esqueleto) seguido dos apêndices
#                                  (suplemento.qmd, montado de _esqueleto_suplemento.qmd), com paginação contínua
# - docs/revisao.html              artigo em HTML
# - docs/apendices.html            apêndices em HTML
# - docs/linguagem-simples.html    resumo em linguagem simples (09-documento-final/linguagem_simples.qmd)
# - docs/pacote-replicacao.zip     pacote de replicação sem resumos nem e-mails de terceiros (ferramentas/montar_pacote.py)
# - docs/index.html                vitrine interativa (09-documento-final/vitrine/)
# Nada de dados brutos, fichas ou PDFs de terceiros vai para docs/. A pasta é limpa por lista branca.
set -euo pipefail
raiz="$(cd "$(dirname "$0")/.." && pwd)"
docs="$raiz/docs"
fd="$raiz/09-documento-final"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
export PYTHONDONTWRITEBYTECODE=1

# 0. versões
qv="$(quarto --version)"
[[ "$qv" == 1.9.* ]] || { echo "Quarto $qv; o projeto foi montado com 1.9.35" >&2; exit 1; }
tv="$(quarto typst --version 2>&1)"
[[ "$tv" == *"0.14"* ]] || { echo "Typst embutido no Quarto não é 0.14: $tv" >&2; exit 1; }
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
python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd

# 2. PDF único: artigo (em pé) + apêndices (deitados), com a numeração de página contínua
cd "$fd"
quarto render revisao_final.qmd --to typst -M keep-typ:false --output _artigo.pdf 2>&1 | tee "$tmp/render_artigo.log"
quarto render revisao_final.qmd --to typst -M keep-typ:false --output _artigo_repro.pdf > /dev/null 2>&1
python3 revista/verificar_pdf.py _artigo.pdf --artigo --log "$tmp/render_artigo.log" --segundo _artigo_repro.pdf
n_artigo="$(pdfinfo _artigo.pdf | awk '/^Pages:/ {print $2}')"
quarto render suplemento.qmd --to typst -M keep-typ:false -M continuacao:true -M "pagina-inicial:$((n_artigo + 1))" \
  --output _apendices.pdf 2>&1 | tee "$tmp/render_apendices.log"
python3 revista/verificar_pdf.py _apendices.pdf --suplemento --log "$tmp/render_apendices.log"
python3 "$raiz/ferramentas/juntar_pdf.py" _artigo.pdf _apendices.pdf "$docs/revisao.pdf"
python3 revista/verificar_pdf.py "$docs/revisao.pdf" --completo
rm -f _artigo.pdf _artigo_repro.pdf _apendices.pdf

# 3. HTML: artigo, apêndices e linguagem simples
quarto render revisao_final.qmd --to html --output revisao.html --output-dir "$docs"
quarto render suplemento.qmd --to html --output apendices.html --output-dir "$docs"
quarto render linguagem_simples.qmd --to html --output linguagem-simples.html --output-dir "$docs"

# 4. barra de navegação e Open Graph nas páginas de documento (aviso de rascunho e noindex só fora da versão final)
python3 "$raiz/ferramentas/barra_publicacao.py" "$docs" "$raiz/07-relatorio/_pendencias_abertas.json"

# 5. pacote de replicação (sem resumos nem e-mails de terceiros), conferido pela sanitização
cd "$raiz"
python3 ferramentas/montar_pacote.py "$docs/pacote-replicacao.zip"

# 6. vitrine (por último, para conferir as âncoras dos documentos)
python3 09-documento-final/vitrine/exportar_dados.py
python3 09-documento-final/vitrine/montar_vitrine.py --final
python3 09-documento-final/vitrine/qa/testar_sanitizacao.py "$docs"
python3 09-documento-final/vitrine/qa/testar_textos.py
python3 09-documento-final/vitrine/qa/checar_links.py "$docs/index.html" "$docs/revisao.html" "$docs/apendices.html" "$docs/linguagem-simples.html"
python3 09-documento-final/vitrine/qa/verificar_licencas.py

# 7. docs/ só com a lista branca
touch "$docs/.nojekyll"
python3 - "$docs" <<'PY'
import os, shutil, sys
docs = sys.argv[1]
permitidos = {".nojekyll", "index.html", "revisao.html", "revisao.pdf", "apendices.html", "linguagem-simples.html",
              "pacote-replicacao.zip", "CNAME"}
for nome in os.listdir(docs):
    if nome not in permitidos:
        p = os.path.join(docs, nome)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
        print("removido de docs/:", nome)
PY
ls -la "$docs"
