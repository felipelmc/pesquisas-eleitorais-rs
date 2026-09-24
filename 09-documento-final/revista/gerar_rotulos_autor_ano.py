"""Gera 09-documento-final/revista/rotulos_autor_ano.json: o rótulo de citação no texto de cada chave dos incluídos,
com o sufixo de ano que o citeproc dá no próprio artigo (ex.: "Agranov et al. 2017", "Araujo e Gatto 2021a").

USO (de qualquer pasta; rode antes preparar_referencias.py):
    python3 09-documento-final/revista/gerar_rotulos_autor_ano.py

Por que o contexto importa: o citeproc do pandoc (3.8, CSL da APSA em pt-BR) atribui o sufixo de desambiguação
("2021a/b") pela ordem da PRIMEIRA CITAÇÃO no documento, e não pela data nem pela ordem da bibliografia. Até a etapa 8
este script citava as chaves na ordem de 07-relatorio/incluidos.csv, em que o preprint @Araujo2021 vem antes do artigo
@Araujo2021a; no artigo, @Araujo2021a é citado no texto e @Araujo2021 só no nocite, e as figuras saíam com "2021b"
para o estudo que o texto chama de "2021a".

Como:
 1. monta o artigo em memória (montar_revisao_final.montar_texto, sem exigir as figuras, que são geradas depois
    deste script) e lê do AST do pandoc (quarto pandoc -t json, sem citeproc) a ordem em que cada chave de
    revista/referencias.json é citada pela primeira vez, na ordem do documento; depois vêm as chaves de
    07-relatorio/incluidos.csv que faltam, na ordem do nocite que o montador grava;
 2. um documento temporário com [@chave] em parágrafo próprio, nessa ordem, passa por `quarto pandoc --citeproc
    --csl revista/american-political-science-association.csl --bibliography revista/referencias.json -t json`, com
    `lang: pt-BR`; o rótulo de cada chave dos incluídos é a citação sem os parênteses.
Conferências (param com erro):
 (a) o suplemento montado em memória (montar_suplemento.montar_texto) dá os mesmos rótulos;
 (b) citar também, no fim, todas as outras entradas de referencias.json não muda nenhum rótulo;
 (c) na bibliografia do artigo, relatos com o mesmo rótulo-base vêm na ordem da letra (2021a antes de 2021b); se não
     vierem, acerte ANTES_NA_BIBLIOGRAFIA em preparar_referencias.py (o citeproc desempata a bibliografia pela ordem
     das entradas no JSON).

Saída: {chave: rótulo}, só strings, em ordem alfabética de chave.
"""
import csv
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
R = Path(__file__).resolve().parents[2]
D = R / "09-documento-final"
REV = D / "revista"
CSL = REV / "american-political-science-association.csl"
BIB = REV / "referencias.json"
INCL = R / "07-relatorio/incluidos.csv"
SAIDA = REV / "rotulos_autor_ano.json"


def importar(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def pandoc_json(texto, citeproc=False):
    with tempfile.TemporaryDirectory() as tmp:
        md = Path(tmp) / "doc.md"
        md.write_text(texto, encoding="utf-8")
        cmd = ["quarto", "pandoc", str(md), "-f", "markdown", "-t", "json"]
        if citeproc:
            cmd += ["--citeproc", "--csl", str(CSL), "--bibliography", str(BIB)]
        r = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if r.returncode != 0:
        sys.exit(f"ERRO no pandoc: {r.stderr.strip()}")
    if citeproc and "[WARNING] Citeproc" in r.stderr:
        sys.exit(f"ERRO no citeproc: {r.stderr.strip()}")
    return json.loads(r.stdout)


def citacoes_em_ordem(no, saida):
    """Chaves das citações (Cite) em ordem de documento, numa busca em profundidade pelo AST (a mesma ordem em que o
    pandoc percorre o documento: na tabela, a legenda vem antes do corpo)."""
    if isinstance(no, dict):
        if no.get("t") == "Cite":
            for c in no["c"][0]:
                saida.append(c["citationId"])
        for v in no.values():
            citacoes_em_ordem(v, saida)
    elif isinstance(no, list):
        for v in no:
            citacoes_em_ordem(v, saida)
    return saida


def ordem_do_documento(texto, conhecidas):
    """Chaves de `conhecidas` na ordem da primeira citação no corpo do texto (sem o YAML, onde fica o nocite)."""
    doc = pandoc_json(texto)
    vistas = []
    for k in citacoes_em_ordem(doc["blocks"], []):
        if k in conhecidas and k not in vistas:
            vistas.append(k)
    return vistas


def texto_puro(inlines):
    out = []
    for x in inlines:
        t, c = x.get("t"), x.get("c")
        if t == "Str":
            out.append(c)
        elif t in ("Space", "SoftBreak", "LineBreak"):
            out.append(" ")
        elif t in ("Emph", "Strong", "Underline", "SmallCaps", "Strikeout", "Superscript", "Subscript"):
            out.append(texto_puro(c))
        elif t in ("Span", "Quoted"):
            out.append(texto_puro(c[1]))
        elif t == "Link":
            out.append(texto_puro(c[1]))
        elif t == "Cite":
            out.append(texto_puro(c[1]))
    return "".join(out)


def rotular(ordem, chaves_rotulo):
    """Cita `ordem` (um parágrafo por chave) e devolve ({chave: rótulo} para chaves_rotulo, ordem da bibliografia)."""
    corpo = "---\nlang: pt-BR\n---\n\n" + "\n\n".join(f"[@{k}]" for k in ordem) + "\n"
    doc = pandoc_json(corpo, citeproc=True)
    rot, bib = {}, []
    for b in doc["blocks"]:
        if b["t"] == "Para" and len(b["c"]) == 1 and b["c"][0]["t"] == "Cite":
            cit = b["c"][0]["c"][0]
            if len(cit) != 1:
                sys.exit(f"ERRO: parágrafo com {len(cit)} citações")
            k = cit[0]["citationId"]
            m = re.fullmatch(r"\((.+)\)", texto_puro(b["c"][0]["c"][1]).strip())
            if not m:
                sys.exit(f"ERRO: citação de {k} fora do formato esperado: {texto_puro(b['c'][0]['c'][1])!r}")
            if k in chaves_rotulo:
                rot[k] = m.group(1)
        elif b["t"] == "Div" and b["c"][0][0] == "refs":
            bib = [d["c"][0][0].removeprefix("ref-") for d in b["c"][1] if d["t"] == "Div"]
    faltam = [k for k in chaves_rotulo if k not in rot]
    if faltam:
        sys.exit(f"ERRO: sem rótulo para {faltam}")
    return rot, bib


def main():
    if not BIB.exists():
        sys.exit("revista/referencias.json não existe; rode antes revista/preparar_referencias.py")
    chaves = [r["chave"] for r in csv.DictReader(open(INCL, encoding="utf-8-sig"))]
    if len(chaves) != len(set(chaves)):
        sys.exit("ERRO: chaves repetidas em incluidos.csv")
    no_bib = [it["id"] for it in json.loads(BIB.read_text(encoding="utf-8"))]
    faltam = sorted(set(chaves) - set(no_bib))
    if faltam:
        sys.exit(f"ERRO: chaves dos incluídos sem entrada em referencias.json: {faltam}")

    mrf = importar("montar_revisao_final", D / "montar_revisao_final.py")
    msup = importar("montar_suplemento", D / "montar_suplemento.py")
    conhecidas = set(no_bib)

    def contexto(texto):
        corpo = ordem_do_documento(texto, conhecidas)
        return corpo + [k for k in chaves if k not in corpo]  # nocite: incluídos, depois do corpo

    ordem_art = contexto(mrf.montar_texto(exigir_figuras=False))
    rotulos, bib_art = rotular(ordem_art, set(chaves))

    # (a) suplemento
    rot_sup, _ = rotular(contexto(msup.montar_texto()), set(chaves))
    difere = {k: (rotulos[k], rot_sup[k]) for k in chaves if rotulos[k] != rot_sup[k]}
    if difere:
        sys.exit(f"ERRO: rótulos diferentes no artigo e no suplemento (artigo, suplemento): {difere}")
    # (b) demais entradas citadas no fim
    rot_todas, _ = rotular(ordem_art + [k for k in no_bib if k not in ordem_art], set(chaves))
    mudam = {k: (rotulos[k], rot_todas[k]) for k in chaves if rotulos[k] != rot_todas[k]}
    if mudam:
        sys.exit(f"ERRO: rótulos mudam quando as demais referências são citadas: {mudam}")
    # (c) bibliografia na ordem da letra
    grupos = {}
    for k, v in rotulos.items():
        m = re.fullmatch(r"(.+ \d{4})([a-z])", v)
        if m:
            grupos.setdefault(m.group(1), []).append((m.group(2), k))
    fora = []
    for base, itens in grupos.items():
        pela_letra = [k for _, k in sorted(itens)]
        pela_bib = sorted(pela_letra, key=bib_art.index)
        if pela_letra != pela_bib:
            fora.append(f"{base}: letras {pela_letra}, bibliografia {pela_bib}")
    if fora:
        sys.exit("ERRO: na bibliografia do artigo, a ordem não segue a letra do sufixo (acerte ANTES_NA_BIBLIOGRAFIA "
                 "em preparar_referencias.py): " + "; ".join(fora))

    SAIDA.write_text(json.dumps(dict(sorted(rotulos.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sufixo = {k: v for k, v in rotulos.items() if re.search(r"\d{4}[a-z]$", v)}
    print(f"rotulos_autor_ano.json: {len(rotulos)} rótulos, no contexto de citação do artigo (igual ao do "
          f"suplemento); com sufixo de desambiguação: {len(sufixo)} "
          f"({', '.join(f'{k} = {v}' for k, v in sorted(sufixo.items()))}); bibliografia na ordem da letra")


if __name__ == "__main__":
    main()
