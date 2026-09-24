"""Gera 09-documento-final/revista/rotulos_autor_ano.json: o rótulo de citação no texto de cada chave dos incluídos,
como o CSL da APSA renderiza em pt-BR (ex.: "Agranov et al. 2017", "Dahlgaard et al. 2015a").

USO (de qualquer pasta; rode antes preparar_referencias.py):
    python3 09-documento-final/revista/gerar_rotulos_autor_ano.py

Como: um documento temporário com `[@chave]` em parágrafo próprio para cada uma das chaves de
07-relatorio/incluidos.csv passa por `quarto pandoc --citeproc --csl revista/american-political-science-association.csl
--bibliography revista/referencias.json -t plain`, com `lang: pt-BR`; o rótulo é a citação sem os parênteses.

Contexto de desambiguação: todas as chaves dos incluídos (estudos e relatos secundários) citadas juntas. É o contexto
do suplemento (a tabela S4 cita os relatos secundários) e do artigo montado, que recebe `nocite` com as mesmas chaves
(montar_revisao_final.py e montar_suplemento.py). Assim "2015a/b" sai igual em texto, figuras, suplemento e vitrine.
O script confere que citar também todas as outras entradas de referencias.json não muda nenhum rótulo; se mudar, para.

Saída: {chave: rótulo}, só strings, em ordem alfabética de chave.
"""
import csv
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

R = Path(__file__).resolve().parents[2]
D = R / "09-documento-final"
REV = D / "revista"
CSL = REV / "american-political-science-association.csl"
BIB = REV / "referencias.json"
INCL = R / "07-relatorio/incluidos.csv"
SAIDA = REV / "rotulos_autor_ano.json"


def renderizar(chaves):
    corpo = "---\nlang: pt-BR\nsuppress-bibliography: true\n---\n\n" + "\n\n".join(f"[@{k}]" for k in chaves) + "\n"
    with tempfile.TemporaryDirectory() as tmp:
        md = Path(tmp) / "rotulos.md"
        md.write_text(corpo, encoding="utf-8")
        r = subprocess.run(["quarto", "pandoc", str(md), "--citeproc", "--csl", str(CSL), "--bibliography", str(BIB),
                            "-t", "plain", "--wrap=none"], capture_output=True, text=True, check=False)
    if r.returncode != 0 or "[WARNING] Citeproc" in r.stderr:
        sys.exit(f"ERRO no citeproc: {r.stderr.strip()}")
    pars = [p.strip() for p in r.stdout.strip().split("\n\n") if p.strip()]
    if len(pars) != len(chaves):
        sys.exit(f"ERRO: {len(pars)} parágrafos para {len(chaves)} chaves")
    out = {}
    for k, p in zip(chaves, pars):
        m = re.fullmatch(r"\((.+)\)", p)
        if not m:
            sys.exit(f"ERRO: citação de {k} fora do formato esperado: {p!r}")
        out[k] = m.group(1)
    return out


def main():
    if not BIB.exists():
        sys.exit("revista/referencias.json não existe; rode antes revista/preparar_referencias.py")
    chaves = [r["chave"] for r in csv.DictReader(open(INCL, encoding="utf-8-sig"))]
    if len(chaves) != len(set(chaves)):
        sys.exit("ERRO: chaves repetidas em incluidos.csv")
    no_bib = {it["id"] for it in json.loads(BIB.read_text(encoding="utf-8"))}
    faltam = sorted(set(chaves) - no_bib)
    if faltam:
        sys.exit(f"ERRO: chaves dos incluídos sem entrada em referencias.json: {faltam}")
    rotulos = renderizar(chaves)
    # conferência: citar também as demais entradas (contexto e método) não pode mudar a desambiguação
    outras = sorted(no_bib - set(chaves))
    com_todas = renderizar(chaves + outras)
    mudam = {k: (rotulos[k], com_todas[k]) for k in chaves if rotulos[k] != com_todas[k]}
    if mudam:
        sys.exit(f"ERRO: rótulos mudam quando as demais referências são citadas: {mudam}")
    SAIDA.write_text(json.dumps(dict(sorted(rotulos.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sufixo = {k: v for k, v in rotulos.items() if re.search(r"\d{4}[a-z]$", v)}
    print(f"rotulos_autor_ano.json: {len(rotulos)} rótulos; com sufixo de desambiguação: {len(sufixo)} "
          f"({', '.join(f'{k} = {v}' for k, v in sorted(sufixo.items()))})")


if __name__ == "__main__":
    main()
