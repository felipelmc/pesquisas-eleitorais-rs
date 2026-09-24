"""Sanitização do que vai para o GitHub Pages.

USO (de qualquer pasta):
    python3 09-documento-final/vitrine/qa/testar_sanitizacao.py docs/                 # todo o docs/
    python3 09-documento-final/vitrine/qa/testar_sanitizacao.py docs/ --so index.html # só alguns arquivos

Lê HTML (inclusive o JSON embutido), texto de PDF (pdftotext) e XML de .docx. Sai com 1 se houver FALHA.
Checa:
  - e-mails e caminhos locais (/Users/, ~/, revisoes/pesquisas-eleitorais);
  - campos proibidos como chave de JSON: evidencia, trecho, justificativa, ator_registrado, observacao, aviso,
    pdf_path, descricao, verificado_humano, validado_humano, outcome, modelo, subgrupo;
  - os nomes verificado_humano e validado_humano em qualquer lugar (o texto diz "não validado", nunca o campo);
  - vazamento de texto literal, por janelas deslizantes de n caracteres:
      evidencia (efeitos.csv) e trecho (rob_*_consenso.csv), citações dos PDFs: n = 25;
      outcome, modelo e subgrupo (efeitos.csv): n = 40;
      justificativa do RoB e do GRADE e descricao das pendências: n = 50 (frases comuns do português
      geram coincidências curtas legítimas; 50 caracteres pegam cópia de trecho);
  - títulos (inteiros) e resumos (janelas de 40 caracteres) de registros não incluídos;
  - trechos de 50 caracteres dos prompts do projeto (AVISO) e a menção a pontos_para_o_revisor.
"""
import argparse
import csv
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
N = 25
csv.field_size_limit(10 ** 9)


def ler_csv(rel):
    p = RAIZ / rel
    if not p.exists():
        return []
    with open(p, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip().lower()


def texto_arquivo(p):
    if p.suffix == ".html":
        t = p.read_text(encoding="utf-8", errors="replace")
        t = re.sub(r"data:[\w/+.-]+;base64,[A-Za-z0-9+/=]+", " ", t)          # fontes e imagens embutidas
        t = re.sub(r"/\*! d3-7\.9\.0\.min\.js.*?(?=window\.V = window\.V)", " ", t, flags=re.S)  # D3 minificado
        t = t.replace("\\u003c", "<").replace("<\\/", "</")
        return t
    if p.suffix == ".pdf":
        r = subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True)
        return r.stdout
    if p.suffix == ".docx":
        with zipfile.ZipFile(p) as z:
            return " ".join(re.sub(r"<[^>]+>", " ", z.read(n).decode("utf-8", "replace"))
                            for n in z.namelist() if n.endswith(".xml"))
    if p.suffix in (".txt", ".md", ".json", ".css", ".js", ".svg", ".xml"):
        return p.read_text(encoding="utf-8", errors="replace")
    return ""


def janelas(texto, passo=1, n=N):
    t = norm(texto)
    return {t[i:i + n] for i in range(0, max(0, len(t) - n + 1), passo) if len(re.findall(r"[a-zà-ú]", t[i:i + n])) >= n * 0.6}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta")
    ap.add_argument("--so", nargs="*", help="nomes de arquivo dentro da pasta (padrão: todos)")
    a = ap.parse_args()
    pasta = Path(a.pasta)
    if not pasta.is_absolute():
        pasta = (Path.cwd() / pasta) if (Path.cwd() / pasta).exists() else RAIZ / pasta
    arquivos = sorted(p for p in pasta.rglob("*") if p.is_file() and p.suffix in (".html", ".pdf", ".docx", ".json", ".txt", ".md", ".svg"))
    if a.so:
        arquivos = [p for p in arquivos if p.name in a.so]
    falhas, avisos = [], []

    # ---- fontes proibidas, por tamanho de janela
    proib = {25: set(), 40: set(), 50: set()}
    for r in ler_csv("06-analise/efeitos.csv"):
        proib[25] |= janelas(r.get("evidencia") or "")
        for c in ("outcome", "modelo", "subgrupo"):
            proib[40] |= janelas(r.get(c) or "", n=40)
    for f in ("rob2", "robins_i", "epoc"):
        for r in ler_csv(f"04-qualidade/rob_{f}_consenso.csv"):
            proib[25] |= janelas(r.get("trecho") or "")
            proib[50] |= janelas(r.get("justificativa") or "", n=50)
    for rel in ("06-analise/certeza.csv", "06-analise/certeza_agrupamento_amplo.csv"):
        for r in ler_csv(rel):
            proib[50] |= janelas(r.get("justificativa") or "", n=50)
    pend = json.load(open(RAIZ / "07-relatorio/_pendencias_abertas.json", encoding="utf-8"))
    for p in pend["pendencias"]:
        proib[50] |= janelas(p.get("descricao") or "", n=50)
    # títulos e resumos de registros não incluídos
    incl = {norm(r["titulo"]) for r in ler_csv("07-relatorio/incluidos.csv")}
    titulos_proib, resumo_proib = set(), set()
    for r in ler_csv("dados/registros_unicos.csv"):
        t = norm(r.get("titulo", ""))
        if len(t) >= 40 and t not in incl:
            titulos_proib.add(t)
        res = r.get("resumo") or ""
        if len(res) >= 80 and t not in incl:
            resumo_proib |= janelas(res, passo=40, n=40)
    # prompts do projeto
    prompts = set()
    for p in list(RAIZ.glob("**/prompt*.md")) + list(RAIZ.glob("**/prompts*/**/*.md")) + list(RAIZ.glob("**/INSTRUCOES*.md")):
        if "node_modules" in p.parts or "vitrine" in p.parts:
            continue
        try:
            prompts |= janelas(p.read_text(encoding="utf-8", errors="replace"), passo=5, n=50)
        except OSError:
            pass
    # os enunciados literais das células são públicos por definição
    enunciados = {25: set(), 40: set(), 50: set()}
    for c in json.load(open(RAIZ / "09-documento-final/revista/celulas.json", encoding="utf-8"))["celulas"]:
        for n in enunciados:
            enunciados[n] |= janelas(c["enunciado"], n=n)
    for n in proib:
        proib[n] -= enunciados[n]
    prompts -= enunciados[50]
    # o título e o subtítulo do artigo aparecem nos prompts e são públicos
    prompts -= janelas("Pesquisas eleitorais publicadas mudam o voto? Revisão sistemática rápida sobre os efeitos "
                       "bandwagon e underdog e o comparecimento", n=50)
    prompts -= janelas(" https://felipelamarca.com/pesquisas-eleitorais-rs/ ", n=50)

    campos = r'"(evidencia|trecho|justificativa|ator_registrado|observacao|aviso|pdf_path|descricao|verificado_humano|validado_humano|outcome|modelo|subgrupo)"\s*:'
    for p in arquivos:
        nome = p.relative_to(pasta)
        bruto = texto_arquivo(p)
        if not bruto:
            continue
        for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.-]+", bruto):
            if not re.search(r"@(?:\d|media|font-face|keyframes|supports|import|charset|unpublished|misc|article|book)", m.group(0)):
                falhas.append(f"{nome}: e-mail: {m.group(0)}")
        for pad in ("/Users/", "~/", "revisoes/pesquisas-eleitorais", "pontos_para_o_revisor"):
            if pad in bruto:
                falhas.append(f"{nome}: contém {pad!r}")
        for m in re.finditer(campos, bruto):
            falhas.append(f"{nome}: campo proibido {m.group(1)!r} em JSON")
        for pad in ("verificado_humano", "validado_humano"):
            if pad in bruto:
                falhas.append(f"{nome}: nome de campo {pad!r} no texto")
        t = norm(re.sub(r"<[^>]+>", " ", bruto))
        vaz = {n: {t[i:i + n] for i in range(max(0, len(t) - n + 1)) if t[i:i + n] in proib[n]} for n in proib}
        vaz_res = {t[i:i + 40] for i in range(max(0, len(t) - 39)) if t[i:i + 40] in resumo_proib}
        vaz_pr = {t[i:i + 50] for i in range(max(0, len(t) - 49)) if t[i:i + 50] in prompts}
        for n, v in vaz.items():
            if v:
                falhas.append(f"{nome}: {len(v)} trecho(s) literais de {n}+ caracteres de campo proibido, ex.: {sorted(v)[:3]}")
        if vaz_res:
            falhas.append(f"{nome}: {len(vaz_res)} trecho(s) de resumos de registros não incluídos, ex.: {sorted(vaz_res)[:3]}")
        if vaz_pr:
            avisos.append(f"{nome}: {len(vaz_pr)} trecho(s) de 50 caracteres coincidem com prompts do projeto, ex.: {sorted(vaz_pr)[:2]}")
        for tit in titulos_proib:
            if tit in t:
                falhas.append(f"{nome}: título de registro não incluído: {tit[:80]}")
        print(f"conferido: {nome} ({len(bruto) // 1024} kB de texto)")

    print(f"\n{len(arquivos)} arquivo(s); {sum(len(v) for v in proib.values())} janelas proibidas; {len(titulos_proib)} títulos de não incluídos; "
          f"{len(resumo_proib)} janelas de resumos; {len(prompts)} janelas de prompts")
    for a_ in avisos:
        print("AVISO ", a_)
    for f in falhas:
        print("FALHA ", f)
    print("RESULTADO:", "FALHA" if falhas else "OK", f"({len(falhas)} falha(s), {len(avisos)} aviso(s))")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
