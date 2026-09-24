"""Compara a extração original (linhas principais de 05-decomposicao/efeitos/<chave>.csv) com a
re-extração cega (08-revisao-humana/efeitos/cega/<chave>.json). Junção por chave + construto_outcome.
Saída: 08-revisao-humana/efeitos/comparacao_cega.csv (uma linha por efeito principal original) e
comparacao_cega_estudos.csv (resumo por estudo). É triagem para a conferência humana (P032): não
decide nada."""
import csv, json, glob, math
from pathlib import Path

raiz = Path(__file__).resolve().parents[2]
NUM = ["beta", "se", "t", "p", "or_", "efeito_pp", "se_pp", "p0", "p1", "m1", "m2", "sd1", "sd2", "n1", "n2",
       "n_total", "ci_lo", "ci_hi", "r", "f", "sdy"]
CHAVE_VALOR = ["beta", "efeito_pp", "t", "or_", "m1", "p1", "r", "f"]

def num(v):
    try:
        x = float(str(v).replace(",", ".").strip())
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None

def casa(a, b):
    """Mesmo valor impresso (tolerância de arredondamento) ou mesmo valor com sinal trocado."""
    if a is None or b is None:
        return None
    for s in (1, -1):
        bb = s * b
        if abs(a - bb) <= max(0.011 * max(abs(a), abs(bb)), 0.0051):
            return "igual" if s == 1 else "sinal_trocado"
        for fa in (100, 0.01):  # proporção × p.p.
            if abs(a - bb * fa) <= max(0.011 * abs(a), 0.0051):
                return "igual_escala" if s == 1 else "sinal_trocado_escala"
    return None

import re, unicodedata
# Mesma regra de classe_desenho() em ~/.claude/skills/revisao-sistematica/scripts/R/_cli.R
NAO_RAND = re.compile(r"(^|[^a-z])(nao|non|not|sem|without|un|no)[ _-]*(randomi[sz]|random|aleatori)|"
                      r"(^|[^a-z])(quas[ei]|pseudo)[ _-]*(randomi[sz]|random|aleatori|experim)|"
                      r"(^|[^a-z])(como[ _-]*se|as[ _-]*if)[ _-]*(randomi[sz]|random|aleatori)")
RAND = re.compile(r"(^|[^a-z])(rct|ecr|ecra)([^a-z]|$)|randomi[sz]|aleatori|experimento de campo|field experiment|ensaio clinico")
ALEAT_MODELO = re.compile(r"(efeitos?|interceptos?|coeficientes?)[ _-]+aleatori[a-z]*|random[ _-]+(effects?|intercepts?|slopes?)|"
                          r"(amostra|amostragem)[ _-]+aleatori[a-z]*|random(ly)?[ _-]+(sampl[a-z]*|selected)")

def randomizado(txt):
    s = unicodedata.normalize("NFKD", txt or "").encode("ascii", "ignore").decode().lower()
    if NAO_RAND.search(s):
        return False
    return bool(RAND.search(ALEAT_MODELO.sub(" ", s)))

linhas, estudos = [], []
for arq in sorted(glob.glob(str(raiz / "05-decomposicao/efeitos/*.csv"))):
    chave = Path(arq).stem
    orig = [r for r in csv.DictReader(open(arq, encoding="utf-8")) if r.get("modelo_principal") == "sim"]
    jcaminho = raiz / f"08-revisao-humana/efeitos/cega/{chave}.json"
    if not jcaminho.exists():
        estudos.append({"chave": chave, "situacao": "sem_reextracao_cega", "n_orig_principais": len(orig)})
        continue
    cega = json.load(open(jcaminho, encoding="utf-8"))
    efc = cega.get("efeitos", [])
    cons_o = sorted({r["construto_outcome"] for r in orig})
    cons_c = sorted({e.get("construto_outcome", "") for e in efc})
    n_div = 0
    for r in orig:
        cand = [e for e in efc if e.get("construto_outcome") == r["construto_outcome"]]
        melhor, pontos, detalhe = None, -1, ""
        for e in cand:
            acertos = []
            for c in CHAVE_VALOR + ["se", "p0", "n_total"]:
                k = casa(num(r.get(c)), num(e.get(c)))
                if k:
                    acertos.append(f"{c}:{k}")
            if len(acertos) > pontos:
                melhor, pontos, detalhe = e, len(acertos), ";".join(acertos)
        principal_casou = any(x.split(":")[0] in CHAVE_VALOR for x in detalhe.split(";") if x)
        sinal = "sinal_trocado" in detalhe
        campos_div = []
        if melhor:
            for c in ("alvo_efeito", "comparador_tipo", "estimando"):
                if (r.get(c) or "").strip() and (melhor.get(c) or "").strip() and r[c].strip() != str(melhor[c]).strip():
                    campos_div.append(f"{c}: {r[c]} × {melhor[c]}")
            if randomizado(r.get("desenho")) != randomizado(melhor.get("desenho")):
                campos_div.append("classe_desenho: " + ("randomizado" if randomizado(r.get("desenho")) else "nao_randomizado")
                                  + " × " + ("randomizado" if randomizado(melhor.get("desenho")) else "nao_randomizado"))
        if not cand:
            situacao = "construto_ausente_na_cega"
        elif not principal_casou:
            situacao = "valor_principal_diferente"
        elif sinal:
            situacao = "sinal_diferente"
        elif campos_div:
            situacao = "valor_igual_classificacao_diferente"
        else:
            situacao = "concorda"
        if situacao != "concorda":
            n_div += 1
        linhas.append({
            "chave": chave, "id_efeito": r["id_efeito"], "construto_outcome": r["construto_outcome"],
            "situacao": situacao, "valores_que_casam": detalhe, "classificacao_divergente": " | ".join(campos_div),
            "orig_modelo": (r.get("modelo") or "")[:160], "cega_modelo": ((melhor or {}).get("modelo") or "")[:160],
            "orig_valor": "; ".join(f"{c}={r[c]}" for c in NUM if (r.get(c) or "").strip()),
            "cega_valor": "; ".join(f"{c}={(melhor or {}).get(c)}" for c in NUM if (melhor or {}).get(c) not in (None, "")),
            "orig_pagina": r.get("pagina"), "cega_pagina": (melhor or {}).get("pagina"),
            "cega_nota": ((melhor or {}).get("nota") or "")[:400]})
    estudos.append({"chave": chave, "situacao": "comparado", "n_orig_principais": len(orig), "n_cega": len(efc),
                    "construtos_orig": ",".join(cons_o), "construtos_cega": ",".join(cons_c),
                    "criterio_cega": json.dumps(cega.get("criterio_modelo_principal", {}), ensure_ascii=False),
                    "n_divergentes": n_div})

saida = raiz / "08-revisao-humana/efeitos"
with open(saida / "comparacao_cega.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0])); w.writeheader(); w.writerows(linhas)
with open(saida / "comparacao_cega_estudos.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["chave", "situacao", "n_orig_principais", "n_cega", "construtos_orig", "construtos_cega", "criterio_cega", "n_divergentes"]
    w = csv.DictWriter(f, fieldnames=campos); w.writeheader(); w.writerows(estudos)
from collections import Counter
print(Counter(l["situacao"] for l in linhas))
print([e["chave"] for e in estudos if e.get("n_divergentes")])
