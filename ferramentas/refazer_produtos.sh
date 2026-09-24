#!/usr/bin/env bash
# Refaz os produtos de relato depois que a síntese (06-analise/) ou as pendências mudarem, a partir da raiz:
#   bash ferramentas/refazer_produtos.sh
# Pré-requisito: a cadeia de análise do README ("Refazer os produtos depois de fechar pendências", passos 1 a 4)
# já rodou, com rs pendencia listar > 07-relatorio/_pendencias_abertas.json e rs declaracao-ia por último.
#
# 1. Sentinela: compara o SHA256 das fontes da síntese com o registrado em 09-documento-final/spec_v2.md (seção 10).
#    Se algo mudou, o texto do artigo (escrito por agentes a partir dessas fontes) precisa ser reescrito nas seções
#    listadas na spec antes de publicar; o script para e diz quais fontes mudaram.
# 2. Tabelas de insumo (07-relatorio/gerar_tabelas_relatorio.py) e caixa OQF (gerar_caixa_oqf.py).
# 3. Publicação completa (ferramentas/publicar.sh), com todas as travas.
set -euo pipefail
raiz="$(cd "$(dirname "$0")/.." && pwd)"
cd "$raiz"
export PYTHONDONTWRITEBYTECODE=1

python3 - <<'EOF'
import hashlib, re, sys
spec = open("09-documento-final/spec_v2.md", encoding="utf-8").read()
bloco = spec.split("## 10. Sentinela", 1)[1]
mudou = []
for sha, arq in re.findall(r"^([0-9a-f]{64})\s+(\S+)$", bloco, flags=re.M):
    atual = hashlib.sha256(open(arq, "rb").read()).hexdigest()
    if atual != sha:
        mudou.append(arq)
if mudou:
    print("SENTINELA: estas fontes mudaram desde a redação do artigo:", *mudou, sep="\n  ")
    print("Reescreva as seções indicadas na seção 10 de 09-documento-final/spec_v2.md (prompts em "
          "09-documento-final/prompts_v2/), regenere celulas.json e numeros_v2.json, rode as travas e atualize a "
          "sentinela na spec. Só então publique.")
    sys.exit(2)
print("sentinela: fontes da síntese iguais às da redação")
EOF

python3 07-relatorio/gerar_tabelas_relatorio.py 09-documento-final/insumos/tabelas
python3 09-documento-final/gerar_caixa_oqf.py
bash ferramentas/publicar.sh
