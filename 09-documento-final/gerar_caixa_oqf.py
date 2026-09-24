"""Tabelas da caixa de ferramentas no formato OQF para o documento final (09-documento-final/).

Só lê arquivos do projeto. Junta, por célula (família × construto × comparador × célula de alvo × classe de
desenho), a contagem de direções da SWiM principal (06-analise/swim_principal/swim_resumo.json), a certeza e o
enunciado GRADE (06-analise/certeza.csv) e o rótulo da caixa-3 no nível família × construto × desenho
(06-analise/caixa_ferramentas.csv). Nenhum número é digitado.

USO (da raiz):  python3 09-documento-final/gerar_caixa_oqf.py
Saída: 09-documento-final/insumos/caixa_oqf_celulas.md, caixa_oqf_painel.md e caixa_oqf.json
"""
import csv, json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
OUT = R / "09-documento-final/insumos"
NOMES = {
    "pesquisa_pre_eleitoral": "Pesquisa pré-eleitoral", "agregador_projecao": "Agregador ou projeção",
    "boca_de_urna": "Boca de urna",
    "apoio_ao_lider": "Apoio", "mobilizacao": "Comparecimento",
    "principal": "a quem aparece à frente", "viabilidade": "viabilidade", "momentum": "*momentum*",
    "sem_pesquisa": "sem pesquisa", "mesmo_candidato_atras": "mesmo candidato atrás",
    "outro_resultado": "outro resultado", "antes_depois_proibicao": "antes × depois da proibição",
    "unidades_nao_expostas": "unidades não expostas", "outro": "outro",
    "randomizado": "randomizado", "nao_randomizado": "não randomizado",
    "muito_baixa": "muito baixa", "baixa": "baixa", "moderada": "moderada", "alta": "alta",
}
FAMILIA = {"outro": "Apuração parcial oficial"}
def n(x):
    return NOMES.get(x, x)
def nf(x):
    return FAMILIA.get(x, NOMES.get(x, x))

swim = json.load(open(R / "06-analise/swim_principal/swim_resumo.json", encoding="utf-8"))
por_grupo = {}
for g in swim["grupos"]:
    chave = (g["familia_intervencao"], g["construto_outcome"], g["comparador_tipo"], g["celula_alvo"], g["classe_desenho"])
    por_grupo[chave] = g
caixa = {(r["familia_intervencao"], r["construto_outcome"], r["classe_desenho"]): r
         for r in csv.DictReader(open(R / "06-analise/caixa_ferramentas.csv", encoding="utf-8")) if r["dimensao"] == "efeito"}

linhas = []
for c in csv.DictReader(open(R / "06-analise/certeza.csv", encoding="utf-8")):
    chave = (c["familia_intervencao"], c["construto_outcome"], c["comparador_tipo"], c["celula_alvo"], c["classe_desenho"])
    g = por_grupo.get(chave, {})
    cx = caixa.get((c["familia_intervencao"], c["construto_outcome"], c["classe_desenho"]), {})
    linhas.append({
        "familia": c["familia_intervencao"], "construto": c["construto_outcome"], "comparador": c["comparador_tipo"],
        "celula_alvo": c["celula_alvo"], "desenho": c["classe_desenho"], "estudos": c["estudos"].split("|"),
        "n_estudos": g.get("n_estudos"), "beneficos": g.get("n_beneficos"), "danosos": g.get("n_danosos"),
        "nulos": g.get("n_nulos"), "mistos": g.get("n_mistos"), "p_sinal": g.get("p_sinal"),
        "ic_proporcao": g.get("ic_proporcao"), "certeza": c["certeza"], "enunciado": c["enunciado"],
        "rotulo_caixa": cx.get("rotulo", ""), "forca_caixa": cx.get("forca", ""), "validado_humano": c["validado_humano"],
    })

def fmt_p(p):
    return "não se aplica" if p is None else f"{p:.3f}".replace(".", ",")

cab = ("| Intervenção | Resultado | Comparador | Desenho | Estudos | Direção (a favor / contra / nulo) | p do teste de sinal | Rótulo | Certeza |\n"
       "|---|---|---|---|---|---|---|---|---|\n")
corpo = ""
for l in sorted(linhas, key=lambda l: (l["construto"], l["familia"], l["celula_alvo"], l["comparador"], l["desenho"])):
    resultado = n(l["construto"]) + ("" if l["construto"] == "mobilizacao" else f" ({n(l['celula_alvo'])})")
    direcao = f"{l['beneficos']} / {l['danosos']} / {l['nulos']}" + (f" ({l['mistos']} misto)" if l["mistos"] else "")
    corpo += (f"| {nf(l['familia'])} | {resultado} | {n(l['comparador'])} | {n(l['desenho'])} | {len(l['estudos'])} "
              f"({', '.join('@' + e for e in l['estudos'])}) | {direcao} | {fmt_p(l['p_sinal'])} | "
              f"{l['rotulo_caixa'] or 'Inconclusivo'} | {n(l['certeza'])} |\n")
(OUT / "caixa_oqf_celulas.md").write_text(cab + corpo, encoding="utf-8")

painel = [r for r in csv.DictReader(open(R / "06-analise/caixa_ferramentas.csv", encoding="utf-8")) if r["dimensao"] == "efeito_painel"]
cab2 = "| Intervenção | Resultado | Rótulo | Força | Certeza | Estudos |\n|---|---|---|---|---|---|\n"
corpo2 = "".join(f"| {nf(r['familia_intervencao'])} | {n(r['construto_outcome'])} | {r['rotulo']} | {r['forca']} | {n(r['certeza'])} | {r['n_estudos']} |\n" for r in painel)
(OUT / "caixa_oqf_painel.md").write_text(cab2 + corpo2, encoding="utf-8")
json.dump({"celulas": linhas, "painel": painel}, open(OUT / "caixa_oqf.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(linhas), "células;", len(painel), "linhas de painel")
