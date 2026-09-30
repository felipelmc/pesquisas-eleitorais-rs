"""Aceite do PDF de journal (artigo ou suplemento).

USO (da raiz):  python3 09-documento-final/revista/verificar_pdf.py <arquivo.pdf> [--artigo | --suplemento | --completo] [--log <render.log>]
                [--segundo <outra_compilacao.pdf>]

Checa:
- log do render (se dado): sem "unknown font", citação não encontrada, "did not converge", "warning";
- pdfinfo: título com "RASCUNHO NÃO VALIDADO" (enquanto houver pendências), autor e palavras-chave;
- pdffonts: tudo embutido, nenhuma Type 3, só STIX Two, Fira Sans e Fira Mono;
- texto (pdftotext, normalizado): no artigo, 11 caixas "Pendente de revisão humana", os IDs de
  07-relatorio/_pendencias_abertas.json, pelo menos 18 símbolos ⊕; em qualquer um, nenhum "?@", "@fig-", "@tbl-",
  "@sec-", ":::", "{#", "@@", "[Abertura";
- página 1, cabeças e rodapés: nenhum "journal", "vol.", "ISSN", "©", "recebido", "aceito", "revisado por pares";
- mancha: nas páginas em pé, nenhum texto (exceto a marca-d'água) fora de x = 20 a 190 mm;
- reprodutibilidade (se --segundo): os dois PDFs são idênticos byte a byte.
Versão final (`estado: final` em revista/_revista.yml, Emenda 7): sem marca no título nem na p. 1 e sem caixas de
pendência; "RASCUNHO NÃO VALIDADO" exatamente uma vez no artigo (declaração de uso de IA) e no máximo uma vez nos
apêndices; nenhum "[A confirmar pelo autor]". Com --completo (PDF juntado: artigo + apêndices), confere também que as
pendências abertas, menos a P038, aparecem no texto, e as caixas e ⊕ do artigo não são contadas.
Sai com 1 se houver FALHA.
"""
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import pymupdf

R = Path(__file__).resolve().parents[2]
MM = 72 / 25.4
falhas, avisos = [], []


def falha(msg):
    falhas.append(msg)


def aviso(msg):
    avisos.append(msg)


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def normalizar(t):
    t = unicodedata.normalize("NFC", t)
    t = re.sub(r"-\n(\w)", r"\1", t)          # hifenização de fim de linha
    t = t.replace("​", "")
    return re.sub(r"\s+", " ", t)


def main():
    args = sys.argv[1:]
    pdf = Path(args[0])
    artigo = "--suplemento" not in args and "--completo" not in args
    log = args[args.index("--log") + 1] if "--log" in args else None
    segundo = args[args.index("--segundo") + 1] if "--segundo" in args else None
    pend = json.load(open(R / "07-relatorio/_pendencias_abertas.json", encoding="utf-8"))
    ids = [p["id"] for p in pend["pendencias"]]
    m_estado = re.search(r"(?m)^estado:\s*(\w+)", (R / "09-documento-final/revista/_revista.yml").read_text(encoding="utf-8"))
    final = bool(m_estado and m_estado.group(1) == "final")
    # rascunho: marca no título do PDF, na p. 1 e 11 caixas de pendência. Na versão final (Emenda 7), a marca
    # fica só na abertura da declaração de uso de IA (R7.23), e as pendências abertas vão para os apêndices.
    rascunho = pend["n"] > 0 and not final
    completo = "--completo" in args   # PDF juntado (artigo + apêndices): confere também os IDs das pendências

    # log
    if log:
        txt = Path(log).read_text(encoding="utf-8", errors="replace")
        for pad in ("unknown font", "not found", "did not converge", "WARNING", "warning:"):
            if pad.lower() in txt.lower():
                linhas = [l for l in txt.splitlines() if pad.lower() in l.lower()][:3]
                falha(f"log do render contém '{pad}': {linhas}")

    # metadados
    info = run("pdfinfo", str(pdf))
    meta = dict(l.split(":", 1) for l in info.splitlines() if ":" in l)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    if rascunho and "RASCUNHO NÃO VALIDADO" not in meta.get("Title", ""):
        falha(f"título do PDF sem 'RASCUNHO NÃO VALIDADO': {meta.get('Title')!r}")
    for campo in ("Author", "Keywords"):
        if not meta.get(campo):
            falha(f"pdfinfo sem {campo}")
    paginas = int(meta.get("Pages", "0"))

    # fontes
    fontes = run("pdffonts", str(pdf)).splitlines()[2:]
    for l in fontes:
        partes = l.split()
        nome = partes[0]
        if "Type 3" in l:
            falha(f"fonte Type 3: {nome}")
        emb = re.search(r"\s(yes|no)\s+(yes|no)\s+(yes|no)\s", l)
        if emb and emb.group(1) != "yes":
            falha(f"fonte não embutida: {nome}")
        base = nome.split("+")[-1]
        if not re.match(r"(STIXTwo(Text|Math)|FiraSans|FiraMono)", base):
            falha(f"fonte fora do conjunto do projeto: {base}")

    doc = pymupdf.open(pdf)
    texto = normalizar("\n".join(p.get_text() for p in doc))

    # conteúdo
    n_marca = texto.count("RASCUNHO NÃO VALIDADO")
    if final and artigo and n_marca != 1:
        falha(f"'RASCUNHO NÃO VALIDADO' aparece {n_marca} vez(es) (versão final: só na declaração de uso de IA)")
    if final and not artigo and not completo and n_marca > 1:
        falha(f"'RASCUNHO NÃO VALIDADO' aparece {n_marca} vezes nos apêndices")
    if final and "[A confirmar pelo autor]" in texto:
        falha("marcador '[A confirmar pelo autor]' no PDF")
    if final and completo:
        faltam = [i for i in ids if i != "P038" and i not in texto]
        if faltam:
            falha(f"IDs de pendência abertos ausentes do PDF: {faltam}")
    if artigo:
        n_caixas = len(re.findall(r"PENDENTE DE REVISÃO HUMANA", texto, flags=re.I))
        if n_caixas != (0 if final else 11):
            falha(f"caixas 'Pendente de revisão humana': {n_caixas} (esperado {0 if final else 11})")
        if not final:
            faltam = [i for i in ids if i not in texto]
            if faltam:
                falha(f"IDs de pendência ausentes do PDF: {faltam}")
        if texto.count("⊕") < 18:
            falha(f"símbolos ⊕: {texto.count('⊕')} (esperado ao menos 18)")
    for pad in ("?@", "@fig-", "@tbl-", "@sec-", "@qdr-", ":::", "{#", "@@", "[Abertura", "??"):
        if pad in texto:
            i = texto.index(pad)
            falha(f"resto de marcação '{pad}': …{texto[max(0, i - 40):i + 40]}…")

    # página 1, cabeças e rodapés
    proib = re.compile(r"\b(journal|vol\.|issn|recebido|aceito|revisado por pares)\b|©", re.I)
    p1 = normalizar(doc[0].get_text())
    if proib.search(p1):
        falha(f"página 1 com termo de revista: {proib.search(p1).group(0)}")
    if rascunho and "RASCUNHO NÃO VALIDADO" not in p1:
        falha("página 1 sem 'RASCUNHO NÃO VALIDADO'")
    for i, pg in enumerate(doc):
        h = pg.rect.height
        for b in pg.get_text("blocks"):
            x0, y0, x1, y1, t = b[:5]
            if y1 < 22 * MM or y0 > h - 22 * MM:
                if proib.search(t):
                    falha(f"p. {i + 1}: cabeça/rodapé com termo de revista: {t.strip()[:60]}")

    # mancha (páginas em pé)
    for i, pg in enumerate(doc):
        if pg.rect.width > pg.rect.height:
            continue
        for x0, y0, x1, y1, t, *_ in pg.get_text("words"):
            if "RASCUNHO" in t or "VALIDADO" in t or t in ("NÃO",):
                continue
            if x0 < 20 * MM - 0.5 or x1 > 190 * MM + 0.5:
                falha(f"p. {i + 1}: texto fora da mancha ({x0 / MM:.1f}–{x1 / MM:.1f} mm): {t[:40]}")
                break

    # reprodutibilidade
    if segundo:
        if Path(segundo).read_bytes() != pdf.read_bytes():
            falha("duas compilações diferentes byte a byte")

    print(f"{pdf.name}: {paginas} páginas")
    for a in avisos:
        print("AVISO", a)
    for f in falhas:
        print("FALHA", f)
    if not falhas:
        print("OK")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
