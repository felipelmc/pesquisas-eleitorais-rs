"""Aplica as decisões dos árbitros de efeitos (08-revisao-humana/efeitos/arbitragem/<chave>.json) aos CSVs
05-decomposicao/efeitos/<chave>.csv. Cada alteração só é aplicada se o valor atual for o `de` que o árbitro
leu; senão vai para a lista de conflitos. Registro linha a linha em 05-decomposicao/correcoes_sessao_2026-09-23.csv.

Exceções decididas pelo coordenador (motivo no registro):
- Morton2015a: estimando ATT -> associacao não é aplicado nas linhas de diferença-em-diferenças; a regra
  congelada de b2_estimando (passo 3) dá ATT para DiD. O prompt do árbitro estava errado nesse ponto.
  E41 e E42 (antes e depois só nas unidades tratadas) mudam para associacao.
- Brugarolas2021: sistema_eleitoral não é preenchido por conhecimento externo (codebook: 999 quando o texto
  não informa).
- Alabrese2024a: o árbitro recomendou a mesma correção de comparador_tipo (outro -> outro_resultado) e de
  estimando (outro -> associacao) nas linhas não principais; aplicada a todas as linhas com esses valores.
"""
import csv, json, glob
from pathlib import Path

raiz = Path(__file__).resolve().parents[2]
dir_efeitos = raiz / "05-decomposicao/efeitos"
registro = raiz / "05-decomposicao/correcoes_sessao_2026-09-23.csv"


def igual(a, b):
    a, b = ("" if a is None else str(a)).strip(), ("" if b is None else str(b)).strip()
    if a == b:
        return True
    try:
        return abs(float(a) - float(b)) < 1e-9
    except ValueError:
        return False


def pular(chave, id_efeito, campo, de, para):
    if chave == "Morton2015a" and campo == "estimando" and str(de) == "ATT" \
            and id_efeito not in ("Morton2015a-E41", "Morton2015a-E42"):
        return "DiD mantém ATT pela regra congelada de b2_estimando (passo 3); o prompt do árbitro estava errado"
    if chave == "Brugarolas2021" and campo == "sistema_eleitoral":
        return "codebook: 999 quando o texto não informa; o árbitro usou conhecimento externo"
    return None


log, conflitos, pulados = [], [], []
for arq in sorted(glob.glob(str(raiz / "08-revisao-humana/efeitos/arbitragem/*.json"))):
    arb = json.load(open(arq, encoding="utf-8"))
    chave = arb["chave"]
    caminho = dir_efeitos / f"{chave}.csv"
    linhas = list(csv.DictReader(open(caminho, encoding="utf-8")))
    campos = list(linhas[0].keys())
    por_id = {l["id_efeito"]: l for l in linhas}
    fonte = f"08-revisao-humana/efeitos/arbitragem/{chave}.json"
    for dec in arb.get("decisoes", []):
        if dec.get("veredito") != "corrigir":
            continue
        idf = dec["id_efeito"]
        if idf not in por_id:
            conflitos.append((chave, idf, "*", "id_efeito não existe"))
            continue
        for alt in dec.get("alteracoes", []):
            campo, de, para = alt["campo"], alt.get("de", ""), alt.get("para", "")
            if campo not in campos:
                conflitos.append((chave, idf, campo, "campo não existe no CSV"))
                continue
            motivo_pulo = pular(chave, idf, campo, de, para)
            if motivo_pulo:
                pulados.append((chave, idf, campo, de, para, motivo_pulo))
                continue
            atual = por_id[idf][campo]
            if not igual(atual, de):
                conflitos.append((chave, idf, campo, f"valor atual {atual!r} ≠ 'de' do árbitro {de!r}"))
                continue
            por_id[idf][campo] = "" if para is None else str(para)
            log.append({"chave": chave, "id_efeito": idf, "campo": campo, "de": atual, "para": por_id[idf][campo],
                        "origem": "arbitro_ia (claude-opus-5-5), comparação com re-extração cega",
                        "fonte": fonte, "justificativa": (dec.get("justificativa") or "")[:500],
                        "pagina": dec.get("pagina", ""), "trecho": (dec.get("trecho") or "")[:300]})
    if chave == "Alabrese2024a":
        for l in linhas:
            for campo, de, para in (("comparador_tipo", "outro", "outro_resultado"), ("estimando", "outro", "associacao")):
                if l[campo] == de:
                    l[campo] = para
                    log.append({"chave": chave, "id_efeito": l["id_efeito"], "campo": campo, "de": de, "para": para,
                                "origem": "coordenador de IA, extensão da recomendação do árbitro às linhas não principais",
                                "fonte": fonte, "justificativa": "mesma correção que o árbitro aplicou às linhas principais",
                                "pagina": "", "trecho": ""})
    modelo = linhas[0]
    for nova in arb.get("linhas_novas", []):
        if nova.get("id_efeito") in por_id:
            conflitos.append((chave, nova.get("id_efeito"), "*", "linha nova com id já existente"))
            continue
        linha = {c: "" for c in campos}
        for c in ("ficha_id", "chave", "id_estudo"):
            linha[c] = modelo.get(c, "")
        extras = [k for k in nova if k not in campos]
        for c in campos:
            if c in nova and c not in ("verificado_humano",):
                linha[c] = "" if nova[c] is None else str(nova[c])
        linhas.append(linha)
        log.append({"chave": chave, "id_efeito": linha["id_efeito"], "campo": "*linha_nova*", "de": "",
                    "para": "linha nova", "origem": "arbitro_ia (claude-opus-5-5)", "fonte": fonte,
                    "justificativa": (nova.get("justificativa") or nova.get("nota") or "")[:500] +
                    (f" [campos fora do CSV ignorados: {', '.join(extras)}]" if extras else ""),
                    "pagina": nova.get("pagina", ""), "trecho": (nova.get("evidencia") or "")[:300]})
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)

with open(registro, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["chave", "id_efeito", "campo", "de", "para", "origem", "fonte", "justificativa", "pagina", "trecho"])
    w.writeheader()
    w.writerows(log)
with open(raiz / "08-revisao-humana/efeitos/aplicacao_arbitragem.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["tipo", "chave", "id_efeito", "campo", "detalhe"])
    for c in conflitos:
        w.writerow(["conflito", *c])
    for p in pulados:
        w.writerow(["nao_aplicado", p[0], p[1], p[2], f"{p[3]} -> {p[4]}: {p[5]}"])
print(f"{len(log)} alterações aplicadas; {len(conflitos)} conflitos; {len(pulados)} não aplicadas por regra")
for c in conflitos:
    print("CONFLITO", c)
