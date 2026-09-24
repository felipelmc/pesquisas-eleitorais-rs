"""Textos visíveis da vitrine: termos proibidos, enunciados literais e números na lista branca.

USO (de qualquer pasta):
    python3 09-documento-final/vitrine/qa/testar_textos.py [docs/index.html]

Fontes de texto:
  1. a camada estática de docs/index.html (sem <script>, <style> e atributos);
  2. qa/capturas/texto_visivel.txt e qa/capturas/texto_estados.txt, gravados por capturar.mjs (texto renderizado,
     gavetas abertas, cada análise de sensibilidade e os estudos fora da síntese). Se forem mais antigos que o
     index.html, viram AVISO e não entram.

Checagens (reusa 09-documento-final/conferir_reestruturacao.py):
  - proibições do artigo: "Neutro", "sem efeito", "benéfic", "danos", "significativ", travessão, "revisão por pares";
  - os 18 enunciados literais de revista/celulas.json aparecem inteiros;
  - datas só da lista permitida; todo número dentro da lista branca do artigo (v1, JSON e CSV de síntese,
    numeros_v2.json, celulas.json), estendida com fontes que só a vitrine mostra, recalculadas aqui de forma
    independente: swim_*/tabelas/swim_direcao.csv, meta_entrada_*.csv (g e EP por efeito), contagens de risco de
    viés por domínio (rob_*_consenso.csv, rob_geral.csv), estudos por país (master) e estudos distintos por bloco
    do mapa (celulas.json). Tamanhos de arquivo (calculados na montagem), o commit e a tag ficam de fora.
Sai com 1 se houver FALHA.
"""
import collections
import csv
import importlib.util
import json
import os
import re
import sys
from decimal import Decimal
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
QA = Path(__file__).resolve().parent


def carregar(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class Texto(HTMLParser):
    BLOCOS = {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "section", "article", "header", "footer", "figcaption",
              "summary", "dd", "dt", "td", "th", "blockquote", "caption", "br", "ul", "ol", "table", "span"}

    def __init__(self):
        super().__init__()
        self.partes, self.ignorar = [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript") or "tamanho-arquivo" in (a.get("class") or ""):
            self.ignorar += 1
        if tag in self.BLOCOS and tag != "span":
            self.partes.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.ignorar = max(0, self.ignorar - 1)
        if tag in self.BLOCOS and tag != "span":
            self.partes.append("\n")

    def handle_data(self, d):
        if not self.ignorar:
            self.partes.append(d)


def texto_estatico(html):
    # os tamanhos de arquivo ficam num span com classe tamanho-arquivo: removidos antes do parser
    html = re.sub(r'<span class="doc-tam tamanho-arquivo">[^<]*</span>', " ", html)
    p = Texto()
    p.feed(html)
    return re.sub(r"[ \t]+", " ", "".join(p.partes))


def main():
    alvo = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "docs/index.html"
    if not alvo.is_absolute():
        alvo = RAIZ / alvo
    cr = carregar("conferir_reestruturacao", RAIZ / "09-documento-final/conferir_reestruturacao.py")
    rel = cr.Relatorio()
    html = alvo.read_text(encoding="utf-8")
    dados = json.loads(re.search(r'<script type="application/json" id="dados-vitrine">(.*?)</script>', html, re.S)
                       .group(1).replace("<\\/", "</"))
    textos = [("estático", texto_estatico(html))]
    for nome in ("texto_visivel.txt", "texto_estados.txt"):
        p = QA / "capturas" / nome
        if not p.exists():
            rel.add("Relato", "AVISO", f"{nome} ausente: rode qa/capturar.mjs para conferir o texto renderizado")
        elif p.stat().st_mtime < alvo.stat().st_mtime:
            rel.add("Relato", "AVISO", f"{nome} é mais antigo que {alvo.name}: rode qa/capturar.mjs de novo")
        else:
            textos.append((nome, p.read_text(encoding="utf-8")))

    # retira o que não é número da revisão: tamanhos de arquivo, commit e tag
    retirar = [d["tamanho"] for d in dados["documentos"] if d["tamanho"]] + [dados["meta"]["commit"], dados["meta"]["tag_anterior"]]
    limpos = []
    for nome, t in textos:
        for r in retirar:
            t = t.replace(r, " ")
        limpos.append((nome, t))

    # proibições
    for nome, t in limpos:
        for pad, fl, rot in cr.PROIBIDOS_TEXTO:
            for m in re.finditer(pad, t, fl):
                rel.add("Proibições", "FALHA", f"{nome}: {rot}: …{t[max(0, m.start() - 50):m.end() + 50]!r}…")
    if not rel.itens.get("Proibições"):
        rel.add("Proibições", "OK", "nenhum termo proibido")

    # enunciados literais
    celulas = json.load(open(RAIZ / "09-documento-final/revista/celulas.json", encoding="utf-8"))["celulas"]
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    tudo = norm(" ".join(t for _, t in limpos))
    faltam = [c["id"] for c in celulas if norm(c["enunciado"]) not in tudo]
    rel.add("Células", "FALHA" if faltam else "OK",
            f"enunciados literais ausentes: {faltam}" if faltam else f"{len(celulas)} enunciados literais presentes")

    # lista branca do artigo
    v1 = (RAIZ / "09-documento-final/_revisao_final_v1_oqf.qmd").read_text(encoding="utf-8")
    chaves, anos_bib = cr.chaves_bib(cr.BIBS, rel)
    incl = list(csv.DictReader(open(cr.INCLUIDOS, encoding="utf-8-sig")))
    rx = cr.regex_chaves(chaves | {r["chave"] for r in incl})
    v1_limpo = cr.limpar(v1, rx)
    v1_ing = cr.linhas_ingles(v1)
    v1_sem = cr.RX_DATA.sub(" ", v1_limpo)
    lb = cr.montar_lista_branca(cr.RX_DATA_CURTA.sub(" ", v1_sem), v1_ing, rx, rel)
    datas_ok = cr.datas_permitidas(v1) | {(24, 9, 2026), (25, 9, 2026)}
    anos_ok = anos_bib | {int(r["ano"]) for r in incl if r["ano"].isdigit()} | {c for _, _, c in datas_ok}
    anos_ok |= {int(v) for _, tok, v, neg, dec, pct in cr.tokens_numericos(v1_sem, v1_ing)
                if v is not None and not dec and not pct and re.fullmatch(r"(?:19|20)\d\d", tok)}

    # extensões da vitrine, recalculadas aqui
    def num_csv(rel_path, colunas=None):
        for r in csv.DictReader(open(RAIZ / rel_path, encoding="utf-8-sig")):
            for c, v in r.items():
                if colunas and c not in colunas:
                    continue
                d = cr.numero_de_string(v or "")
                if d is not None:
                    lb.com_variantes(d, rel_path)
    for p in sorted((RAIZ / "06-analise").glob("swim_*/tabelas/swim_direcao.csv")):
        num_csv(str(p.relative_to(RAIZ)))
    for p in sorted((RAIZ / "06-analise").glob("meta_entrada_*.csv")):
        num_csv(str(p.relative_to(RAIZ)), {"yi", "sei", "vi"})
    for p in sorted((RAIZ / "06-analise").glob("meta_*/tabelas/*.csv")):
        num_csv(str(p.relative_to(RAIZ)))
    for f in ("rob2", "robins_i", "epoc"):
        cont = collections.defaultdict(collections.Counter)
        desac = collections.Counter()
        for r in csv.DictReader(open(RAIZ / f"04-qualidade/rob_{f}_consenso.csv", encoding="utf-8-sig")):
            cont[r["dominio"]][r["julgamento_consenso"]] += 1
            desac[r["dominio"]] += r["julgamento_a"] != r["julgamento_b"]
        for d, c in cont.items():
            for n in list(c.values()) + [sum(c.values()), desac[d]]:
                lb.exato(Decimal(n), "RoB por domínio")
    geral = collections.Counter()
    for r in csv.DictReader(open(RAIZ / "04-qualidade/rob_geral.csv", encoding="utf-8-sig")):
        geral[(r["ferramenta"], r["rob_geral"])] += 1
        geral[r["ferramenta"]] += 1
    for n in geral.values():
        lb.exato(Decimal(n), "RoB geral")
    paises = collections.Counter()
    for r in csv.DictReader(open(RAIZ / "05-decomposicao/fichamentos_master.csv", encoding="utf-8-sig")):
        partes = [re.split(r" — | \(", x.strip())[0].strip() for x in r["pais_estudo"].split(" ; ")]
        if len(partes) > 5:
            lb.exato(Decimal(len(partes)), "países do estudo multinacional")
            continue
        for x in set(partes):
            paises["Países Baixos" if x == "Holanda" else x] += 1
    for n in paises.values():
        lb.exato(Decimal(n), "estudos por país")
    blocos = collections.defaultdict(set)
    for c in celulas:
        blocos[c["bloco"]] |= set(c["estudos"])
        blocos[(c["bloco"], c["classe_desenho"])] |= set(c["estudos"])
    for s in blocos.values():
        lb.exato(Decimal(len(s)), "estudos distintos por bloco do mapa")

    total = 0
    for nome, t in limpos:
        lim = cr.limpar(t, rx, codigo=False)
        total += cr.conferir_datas_e_numeros(nome, t, lim, set(), lb, datas_ok, anos_ok, rel)
    if not any(n == "FALHA" for n, _ in rel.itens.get("Números", [])):
        rel.add("Números", "OK", f"{total} números conferidos contra a lista branca ({len(lb.v)} valores)")
    if not any(n == "FALHA" for n, _ in rel.itens.get("Datas", [])):
        rel.add("Datas", "OK", "datas dentro da lista permitida")
    rel.imprimir()
    sys.exit(1 if rel.falhas() else 0)


if __name__ == "__main__":
    main()
