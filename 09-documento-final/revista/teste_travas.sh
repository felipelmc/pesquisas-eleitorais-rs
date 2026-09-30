#!/usr/bin/env bash
# Teste das travas da reestruturação (etapa 0). Roda da raiz do projeto, qualquer que seja a pasta atual.
#   bash 09-documento-final/revista/teste_travas.sh
# 1. gera revista/celulas.json e revista/numeros_v2.json;
# 2. roda conferir_reestruturacao.py com o v1 como "novo": tem de FALHAR, e as falhas de Células têm de ser só
#    "nenhum span .enunciado" (18). As únicas outras falhas aceitas são as heranças da estrutura antiga do v1:
#    "](../" nos caminhos de figura e @tbl- fora do contrato revista/rotulos.yml;
# 3. roda conferir_numeros.py comparando o v1 com ele mesmo: saída vazia e código 0.
# O v1 é conferido em modo rascunho contra a cópia congelada das 18 pendências de 24/09/2026
# (revista/pendencias_2026-09-24.json), para o teste não depender do estado atual do projeto.
# Sai com 0 se tudo sair como esperado.
set -u
RAIZ="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$RAIZ" || exit 1
V1=09-documento-final/_revisao_final_v1_oqf.qmd
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
ok=1

echo "## 1. gerar_celulas.py"
python3 09-documento-final/revista/gerar_celulas.py || { echo "ERRO: gerar_celulas.py"; exit 1; }
echo "## 2. gerar_numeros_v2.py"
python3 09-documento-final/revista/gerar_numeros_v2.py || { echo "ERRO: gerar_numeros_v2.py"; exit 1; }

echo "## 3. conferir_reestruturacao.py --novo $V1 (tem de falhar por falta de spans .enunciado)"
python3 09-documento-final/conferir_reestruturacao.py --novo "$V1" --modo rascunho \
  --pendencias 09-documento-final/revista/pendencias_2026-09-24.json > "$TMP/reest.txt"
rc=$?
cat "$TMP/reest.txt"
python3 - "$TMP/reest.txt" "$rc" <<'EOF' || ok=0
import re, sys
txt, rc = open(sys.argv[1], encoding="utf-8").read(), int(sys.argv[2])
cats, atual = {}, None
for l in txt.splitlines():
    m = re.match(r"^== (.+?): (FALHA|AVISO|OK)", l)
    if m:
        atual = m.group(1); cats[atual] = []
    elif atual and l.strip().startswith("FALHA"):
        cats[atual].append(l.strip()[5:].strip())
erros = []
if rc != 1:
    erros.append(f"código de saída {rc}, esperado 1")
cel = cats.get("Células", [])
if len(cel) != 18 or not all("nenhum span" in f for f in cel):
    erros.append(f"Células: esperadas 18 falhas 'nenhum span', vieram {len(cel)}")
heranca = {"Proibições": lambda f: '"](../"' in f,
           "Estrutura: rótulos e seções": lambda f: "não está em revista/rotulos.yml" in f}
outras = {}
for c, fs in cats.items():
    if c == "Células" or not fs:
        continue
    inesperadas = [f for f in fs if not (c in heranca and heranca[c](f))]
    if inesperadas:
        erros.append(f"{c}: falhas inesperadas: {inesperadas}")
    else:
        outras[c] = len(fs)
print("\n-- resumo do teste no v1")
print(f"   código de saída: {rc}")
print(f"   Células: {len(cel)} falha(s), todas por falta de span .enunciado")
for c, n in outras.items():
    print(f"   {c}: {n} falha(s) herdadas da estrutura antiga do v1 (esperadas pelas regras novas)")
for e in erros:
    print(f"   ERRO: {e}")
sys.exit(1 if erros else 0)
EOF

echo "## 4. conferir_numeros.py v1 v1 (saída vazia)"
python3 09-documento-final/conferir_numeros.py "$V1" "$V1" > "$TMP/num.txt"
rc=$?
if [ "$rc" -ne 0 ] || [ -s "$TMP/num.txt" ]; then
  echo "ERRO: conferir_numeros.py não saiu vazio (código $rc):"; cat "$TMP/num.txt"; ok=0
else
  echo "   saída vazia, código 0"
fi

if [ "$ok" -eq 1 ]; then echo "## TESTE DAS TRAVAS: OK"; exit 0; else echo "## TESTE DAS TRAVAS: FALHOU"; exit 1; fi
