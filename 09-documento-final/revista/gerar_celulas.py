"""Gera 09-documento-final/revista/celulas.json: as células da síntese principal com certeza GRADE, com ID curto.

USO (de qualquer pasta):  python3 09-documento-final/revista/gerar_celulas.py

Fontes (só leitura):
  06-analise/certeza.csv                         enunciado, certeza, estudos, delta (uma linha por célula julgada)
  06-analise/swim_principal/swim_resumo.json     k, contagens de direção, proporção, IC de Clopper-Pearson, p do sinal

Junção só pelas colunas-chave (familia_intervencao, construto_outcome, comparador_tipo, celula_alvo, classe_desenho).
Nenhum número é digitado aqui. Grupos da SWiM sem linha em certeza.csv (k = 0) vão para "vazias", sem ID.

IDs C01...Cnn: ordem por bloco (apoio principal, viabilidade, momentum, mobilização), dentro do bloco randomizado
antes de não randomizado, depois pelo comparador na ordem do PICOC (sem pesquisa, mesmo candidato atrás, outro
resultado, outro, antes e depois da proibição, unidades não expostas) e, no empate, pela família de exposição na
ordem do PICOC (pesquisa pré-eleitoral, agregador ou projeção, boca de urna, apuração parcial). A ordem é
determinística: os IDs só mudam se mudarem as células. Se um celulas.json anterior tiver outro ID para a mesma
célula, o script avisa.
"""
import csv
import hashlib
import json
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[2]
SAIDA = R / "09-documento-final/revista/celulas.json"
F_CERTEZA = "06-analise/certeza.csv"
F_SWIM = "06-analise/swim_principal/swim_resumo.json"

CHAVE = ("familia_intervencao", "construto_outcome", "comparador_tipo", "celula_alvo", "classe_desenho")
BLOCOS = [  # (nome, construto, celula_alvo)
    ("apoio_principal", "apoio_ao_lider", "principal"),
    ("viabilidade", "apoio_ao_lider", "viabilidade"),
    ("momentum", "apoio_ao_lider", "momentum"),
    ("mobilizacao", "mobilizacao", "mobilizacao"),
]
DESENHO = ["randomizado", "nao_randomizado"]
COMPARADOR = ["sem_pesquisa", "mesmo_candidato_atras", "outro_resultado", "outro", "antes_depois_proibicao",
              "unidades_nao_expostas"]
FAMILIA = ["pesquisa_pre_eleitoral", "agregador_projecao", "boca_de_urna", "outro"]
CERTEZA_TEXTO = {"muito_baixa": "muito baixa", "baixa": "baixa", "moderada": "moderada", "alta": "alta"}


def sha256(rel):
    return hashlib.sha256((R / rel).read_bytes()).hexdigest()


def pos(lista, valor, rotulo):
    if valor not in lista:
        sys.exit(f"ERRO: {rotulo} desconhecido na ordenação: {valor!r}")
    return lista.index(valor)


def bloco_de(chave):
    for i, (nome, construto, alvo) in enumerate(BLOCOS):
        if chave[1] == construto and chave[3] == alvo:
            return i, nome
    sys.exit(f"ERRO: célula fora dos blocos previstos: {chave}")


def main():
    certeza = list(csv.DictReader(open(R / F_CERTEZA, encoding="utf-8-sig")))
    swim = json.load(open(R / F_SWIM, encoding="utf-8"))
    grupos = {tuple(g[c] for c in CHAVE): g for g in swim["grupos"]}
    if len(grupos) != len(swim["grupos"]):
        sys.exit("ERRO: chaves repetidas em swim_resumo.json")

    linhas = {}
    for r in certeza:
        if r["dimensao"] != "efeito":
            sys.exit(f"ERRO: dimensão inesperada em certeza.csv: {r['dimensao']}")
        k = tuple(r[c] for c in CHAVE)
        if k in linhas:
            sys.exit(f"ERRO: célula repetida em certeza.csv: {k}")
        if k not in grupos:
            sys.exit(f"ERRO: célula de certeza.csv sem grupo na SWiM principal: {k}")
        linhas[k] = r

    def ordem(k):
        b, _ = bloco_de(k)
        return (b, pos(DESENHO, k[4], "classe_desenho"), pos(COMPARADOR, k[2], "comparador_tipo"),
                pos(FAMILIA, k[0], "familia_intervencao"))

    celulas = []
    for i, k in enumerate(sorted(linhas, key=ordem), start=1):
        r, g = linhas[k], grupos[k]
        estudos = [e for e in r["estudos"].split("|") if e]
        if set(estudos) != set(g["estudos"]):
            sys.exit(f"ERRO: estudos diferentes entre certeza.csv e swim_resumo.json em {k}: "
                     f"{estudos} x {g['estudos']}")
        if g["k_estudos"] != len(estudos):
            sys.exit(f"ERRO: k da SWiM ({g['k_estudos']}) difere do número de estudos de certeza.csv em {k}")
        if r["certeza"] not in CERTEZA_TEXTO:
            sys.exit(f"ERRO: certeza desconhecida em {k}: {r['certeza']!r}")
        celulas.append({
            "id": f"C{i:02d}",
            "bloco": bloco_de(k)[1],
            **dict(zip(CHAVE, k)),
            "enunciado": r["enunciado"],
            "certeza": r["certeza"],
            "certeza_texto": CERTEZA_TEXTO[r["certeza"]],
            "estudos": estudos,
            "k": g["k_estudos"],
            "n_estudos_com_direcao": g["n_estudos"],
            "n_beneficos": g["n_beneficos"],
            "n_danosos": g["n_danosos"],
            "n_mistos": g["n_mistos"],
            "n_nulos": g["n_nulos"],
            "n_sem_direcao": g.get("n_sem_direcao"),
            "proporcao": g.get("proporcao_benefica"),
            "ic_proporcao": g.get("ic_proporcao"),
            "p_sinal": g.get("p_sinal"),
            "delta": float(r["delta"]) if r["delta"] else None,
            "excluidos_rob_critico": g.get("excluidos_rob_critico", {}).get("estudos", []),
            "validado_humano": r["validado_humano"],
        })

    vazias = []
    for k, g in grupos.items():
        if k in linhas:
            continue
        if g["k_estudos"] != 0:
            sys.exit(f"ERRO: grupo da SWiM com estudos e sem linha em certeza.csv: {k} (k = {g['k_estudos']})")
        vazias.append({**dict(zip(CHAVE, k)), "k": 0, "estudos": [],
                       "excluidos_rob_critico": g.get("excluidos_rob_critico", {}).get("estudos", []),
                       "motivo": "k = 0 na SWiM principal; sem linha em certeza.csv (não julgada)"})

    # aviso de estabilidade dos IDs
    if SAIDA.exists():
        try:
            antigo = {tuple(c[x] for x in CHAVE): c["id"] for c in json.load(open(SAIDA, encoding="utf-8"))["celulas"]}
            mudou = [(antigo[tuple(c[x] for x in CHAVE)], c["id"]) for c in celulas
                     if tuple(c[x] for x in CHAVE) in antigo and antigo[tuple(c[x] for x in CHAVE)] != c["id"]]
            if mudou:
                print(f"AVISO: IDs mudaram em relação ao celulas.json anterior: {mudou}", file=sys.stderr)
        except (ValueError, KeyError):
            pass

    saida = {
        "descricao": "Células da síntese principal com certeza GRADE (06-analise/certeza.csv), com contagens da "
                     "SWiM principal. Gerado por 09-documento-final/revista/gerar_celulas.py; não edite à mão.",
        "fontes": {F_CERTEZA: sha256(F_CERTEZA), F_SWIM: sha256(F_SWIM)},
        "chave": list(CHAVE),
        "n_celulas": len(celulas),
        "n_vazias": len(vazias),
        "celulas": celulas,
        "vazias": vazias,
    }
    SAIDA.write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"celulas.json: {len(celulas)} células ({celulas[0]['id']} a {celulas[-1]['id']}), {len(vazias)} vazia(s)")


if __name__ == "__main__":
    main()
