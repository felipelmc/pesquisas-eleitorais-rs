#!/usr/bin/env bash
# Copia para o repositório privado com o histórico completo (felipelmc/pesquisas-eleitorais-rs-completo) os arquivos
# que ficam fora do Git público: os caminhos do bloco "resumos de terceiros" do .gitignore (resumos, lotes e pareceres
# de triagem, ledger de decisões, amostras e filas com resumo). Faz commit e push no privado. Os PDFs não vão.
#
# USO (da raiz):  bash ferramentas/arquivar_privado.sh [pasta do clone do privado]
# Padrão da pasta: ../pesquisas-eleitorais-rs-completo, ao lado desta cópia de trabalho (clonada se não existir).
set -euo pipefail
raiz="$(cd "$(dirname "$0")/.." && pwd)"
destino="${1:-$(dirname "$raiz")/pesquisas-eleitorais-rs-completo}"
remoto="https://github.com/felipelmc/pesquisas-eleitorais-rs-completo.git"

[ -d "$destino/.git" ] || git clone -q "$remoto" "$destino"
git -C "$destino" pull -q --ff-only

# caminhos entre os marcadores do bloco no .gitignore
caminhos=$(awk '/^# >>> resumos de terceiros/{f=1; next} /^# <<< resumos de terceiros/{f=0} f && $0 !~ /^#/ && NF' \
  "$raiz/.gitignore")
[ -n "$caminhos" ] || { echo "bloco 'resumos de terceiros' não encontrado no .gitignore" >&2; exit 1; }

cd "$raiz"
n=0
while IFS= read -r c; do
  c="${c#/}"
  for p in $c; do                     # expande curingas relativos à raiz
    [ -e "$p" ] || continue
    rsync -a --relative "./$p" "$destino/"
    n=$((n + 1))
  done
done <<< "$caminhos"
echo "$n caminhos copiados para $destino"

cd "$destino"
git add -A
if git diff --cached --quiet; then
  echo "nada mudou no privado"
else
  git commit -q -m "Arquivo privado: arquivos locais da cópia de trabalho em $(date +%Y-%m-%d)"
  git push -q
  echo "commit e push feitos no privado"
fi
