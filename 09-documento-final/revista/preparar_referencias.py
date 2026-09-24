"""Junta os .bib do artigo e do suplemento num CSL JSON corrigido: 09-documento-final/revista/referencias.json.

USO (de qualquer pasta):
    python3 09-documento-final/revista/preparar_referencias.py [--sem-rede]

Fontes (só leitura; nenhum .bib é alterado):
    07-relatorio/references.bib                    estudos incluídos, relatos secundários e revisões anteriores
    09-documento-final/referencias_contexto.bib    contexto brasileiro (leis, PLs, notícias) e Cosgun2026
    09-documento-final/referencias_metodo.bib      referências metodológicas (se não existir, avisa e segue)

Passos:
 1. Cada .bib é convertido com `quarto pandoc -f bibtex -t csljson`. Antes da conversão, uma cópia temporária de
    cada entrada sem `langid` recebe `langid = {brazilian}`: sem isso o pandoc passa todo título para "sentence case"
    como se fosse inglês e estraga nomes próprios ("india", "Marcos do val", "Altera a lei"). O idioma verdadeiro de
    cada item é gravado depois, no passo 4. As chaves não mudam.
 2. Sobreposições de metadados (dicionário SOBREPOSICOES, com a fonte de cada uma), vindas de
    09-documento-final/insumos/revisoes_anteriores.md, seção 5, por pedido do coordenador; não tocam no .bib.
 3. Tipos: a Lei 9.504 e a Res. TSE 23.600 viram `legislation` com autor institucional; os PLs viram `bill`;
    a notícia do STF segue como `webpage`; os demais @misc sem tipo recebem o tipo do dicionário TIPOS.
 3b. Partículas de sobrenome ("van der", "de") passam de dropping- a non-dropping-particle, para a citação sair
    "van der Meer" e "de Vreese".
 4. `language: en` nos itens em inglês (detecção por palavras funcionais, com IDIOMA_FIXO para os casos certos);
    itens em português recebem `pt-BR` e em dinamarquês, `da`.
 5. Títulos inteiros em CAIXA ALTA passam a caixa de título.
 6. Itens com DOI e sem container-title, volume, issue ou page (tipos article-journal, chapter, paper-conference)
    são completados pela API do Crossref (https://api.crossref.org/works/<doi>), com cache em
    revista/crossref_cache.json. Só campos ausentes; nada que já existe é trocado. Se o título do Crossref não
    bater com o do .bib (similaridade < 0,6), nada é completado e o log registra o motivo.
 7. Toda mudança vai para revista/referencias_log.md.

Com --sem-rede, só o cache é usado (DOI fora do cache fica sem completar, com aviso no log).
"""
import argparse
import difflib
import json
import re
import ssl
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

R = Path(__file__).resolve().parents[2]
D = R / "09-documento-final"
REV = D / "revista"
BIBS = [R / "07-relatorio/references.bib", D / "referencias_contexto.bib", D / "referencias_metodo.bib"]
SAIDA = REV / "referencias.json"
CACHE = REV / "crossref_cache.json"
LOG = REV / "referencias_log.md"
UA = "pesquisas-eleitorais-rs/preparar_referencias.py (Python urllib; revisao sistematica academica)"


def contexto_ssl():
    """Python do python.org não traz certificados no macOS: usa o certifi, se houver, ou o /etc/ssl/cert.pem."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        pass
    if Path("/etc/ssl/cert.pem").exists():
        return ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    return ssl.create_default_context()

# ------------------------------------------------------------------ 2. sobreposições (fonte anotada em cada uma)
FONTE_REVISOES = ("09-documento-final/insumos/revisoes_anteriores.md, seção 5 (tabela \"Como essas obras aparecem "
                  "no projeto\"), aplicada por pedido do coordenador em 24/09/2026")
SOBREPOSICOES = {
    "Hardmeier2008": {
        "fonte": FONTE_REVISOES + "; autor e páginas também no Crossref (10.4135/9781848607910.n48); "
                                  "organizadores citados por Barnfield e por Moy e Rinke",
        "campos": {
            "author": [{"family": "Hardmeier", "given": "Sibylle"}],
            "editor": [{"family": "Donsbach", "given": "Wolfgang"}, {"family": "Traugott", "given": "Michael W."}],
            "page": "504-514",
            "publisher": "SAGE Publications",
            "publisher-place": "London",
        },
    },
    "MoyRinke2012": {
        "fonte": FONTE_REVISOES + "; autores, organizadores, livro e páginas também no Crossref "
                                  "(10.1057/9780230374959_11 e 10.1057/9780230374959)",
        "campos": {
            "author": [{"family": "Moy", "given": "Patricia"}, {"family": "Rinke", "given": "Eike Mark"}],
            "editor": [{"family": "Holtz-Bacha", "given": "Christina"}, {"family": "Strömbäck", "given": "Jesper"}],
            "container-title": "Opinion Polls and the Media: Reflecting and Shaping Public Opinion",
            "page": "225-245",
            "publisher": "Palgrave Macmillan",
            "publisher-place": "Basingstoke",
        },
    },
    "Barnfield2019": {
        "fonte": FONTE_REVISOES + "; ano do fascículo impresso (2020), mantido como pede o coordenador; "
                                  "a chave continua Barnfield2019",
        "campos": {"issued": {"date-parts": [[2020]]}},
    },
}

# ------------------------------------------------------------------ 3. tipos
TIPOS = {
    # chave: (tipo CSL, autor institucional ou None, motivo)
    "Brasil1997Lei9504": ("legislation", "Brasil", "lei federal"),
    "TSE2019Res23600": ("legislation", "Tribunal Superior Eleitoral", "resolução do TSE"),
    "BrasilCamara2022PL2567": ("bill", None, "projeto de lei"),
    "BrasilSenado2022PL2558": ("bill", None, "projeto de lei"),
    "STF2006ADI3741": ("webpage", None, "notícia do STF (página institucional)"),
    "SenadoNoticias2022CPIPesquisas": ("webpage", None, "notícia da Agência Senado (página institucional)"),
    "ESOMARWAPOR2022": ("report", None, "relatório de associação profissional"),
    "Sterne2025ROBINSIV2": ("webpage", None, "ferramenta publicada em página própria (riskofbias.info)"),
    "EPOC2017RoB": ("report", None, "documento de orientação em PDF do grupo EPOC"),
    "Schaefer2025OQF": ("article", None, "preprint (tipo CSL article)"),
}

# ------------------------------------------------------------------ 4. idioma
IDIOMA_FIXO = {  # só onde a detecção automática poderia errar; o log mostra todos
    "Dahlgaard2015b": "da",
    "Schaefer2025OQF": "pt-BR",
    "Lamarca2026Livro": "pt-BR",
    "Cosgun2026": "en",
}
PAL_EN = {"the", "of", "and", "in", "on", "to", "for", "with", "a", "an", "how", "what", "is", "are", "from", "by",
          "do", "does", "when", "more", "polls", "poll", "voting", "voters", "vote", "election", "elections",
          "effect", "effects", "evidence", "can", "we", "their", "study", "public", "opinion", "systematic",
          "review", "reviews", "risk", "bias", "guideline", "statement"}
PAL_PT = {"de", "da", "do", "das", "dos", "e", "para", "sobre", "pesquisas", "pesquisa", "eleitorais", "eleitoral",
          "com", "não", "uma", "um", "nº", "lei", "que", "em", "por", "revisão", "sistemática", "políticas", "públicas",
          "através", "normas", "eleições", "projeto", "apresenta", "pedido", "criação", "declara", "funciona"}
PAL_DA = {"og", "af", "på", "hvordan", "påvirkes", "vælgerne", "meningsmålinger", "effekten", "partierne"}

MINUSCULAS_TITULO = {"a", "an", "and", "as", "at", "but", "by", "for", "from", "in", "into", "nor", "of", "on", "or",
                     "the", "to", "with", "vs", "via"}
CAMPOS_CROSSREF = ("container-title", "volume", "issue", "page")
TIPOS_CROSSREF = {"article-journal", "chapter", "paper-conference"}


class Log:
    def __init__(self):
        self.linhas = []

    def add(self, chave, campo, antes, depois, fonte):
        self.linhas.append((chave, campo, antes, depois, fonte))

    def aviso(self, chave, texto):
        self.linhas.append((chave, "AVISO", "", texto, ""))


def fmt(v):
    if v is None or v == "":
        return "(ausente)"
    if isinstance(v, (dict, list)):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


# ------------------------------------------------------------------ 1. conversão
def com_langid(texto):
    """Acrescenta `langid = {brazilian}` às entradas sem langid (só na cópia temporária)."""
    partes = re.split(r"(?m)^(?=@\w+\s*\{)", texto)
    out = []
    for p in partes:
        m = re.match(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", p)
        if not m or m.group(1).lower() in ("comment", "preamble", "string") or re.search(r"(?im)^\s*langid\s*=", p):
            out.append(p)
            continue
        out.append(p[:m.end()] + "\n  langid = {brazilian}," + p[m.end():])
    return "".join(out)


def converter(bib):
    with tempfile.NamedTemporaryFile("w", suffix=".bib", delete=False, encoding="utf-8") as tmp:
        tmp.write(com_langid(bib.read_text(encoding="utf-8")))
        caminho = tmp.name
    try:
        r = subprocess.run(["quarto", "pandoc", "-f", "bibtex", "-t", "csljson", caminho],
                           capture_output=True, text=True, check=False)
    finally:
        Path(caminho).unlink(missing_ok=True)
    if r.returncode != 0:
        sys.exit(f"ERRO: quarto pandoc falhou em {bib}: {r.stderr.strip()}")
    return json.loads(r.stdout)


# ------------------------------------------------------------------ utilidades de texto
def texto_puro(s):
    return re.sub(r"<[^>]+>", "", s or "")


def normaliza(s):
    s = unicodedata.normalize("NFKD", texto_puro(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]+", " ", s).split()


def caixa_de_titulo(s):
    palavras = s.lower().split(" ")
    out = []
    for i, w in enumerate(palavras):
        if i > 0 and w in MINUSCULAS_TITULO and not out[-1].endswith(":"):
            out.append(w)
        else:
            out.append(w[:1].upper() + w[1:])
    return " ".join(out)


def em_caixa_alta(s):
    letras = [c for c in texto_puro(s) if c.isalpha()]
    return len(letras) >= 4 and all(c.isupper() for c in letras)


def detectar_idioma(item):
    if item["id"] in IDIOMA_FIXO:
        return IDIOMA_FIXO[item["id"]], "IDIOMA_FIXO"
    palavras = normaliza(item.get("title", "")) + normaliza(item.get("container-title", ""))
    brutas = set(re.findall(r"[\wçãõáéíóúâêôàåæø]+", texto_puro(item.get("title", "")).lower()))
    en = sum(w in PAL_EN for w in palavras)
    pt = sum(w in PAL_PT for w in brutas) + 2 * sum(c in texto_puro(item.get("title", "")) for c in "ãõçê")
    da = sum(w in PAL_DA for w in brutas)
    if da > max(en, pt):
        return "da", f"palavras funcionais (en {en}, pt {pt}, da {da})"
    if pt > en:
        return "pt-BR", f"palavras funcionais (en {en}, pt {pt})"
    return "en", f"palavras funcionais (en {en}, pt {pt})"


# ------------------------------------------------------------------ 6. Crossref
def ler_cache():
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def crossref(doi, cache, sem_rede):
    chave = doi.lower()
    if chave in cache:
        return cache[chave]
    if sem_rede:
        return {"erro": "fora do cache (--sem-rede)"}
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30, context=contexto_ssl()) as resp:
            msg = json.loads(resp.read().decode("utf-8"))["message"]
            guardar = {k: msg.get(k) for k in ("DOI", "type", "title", "container-title", "volume", "issue", "page",
                                               "article-number", "publisher", "issued", "author")}
            cache[chave] = {"ok": guardar, "consultado_em": time.strftime("%Y-%m-%d")}
    except urllib.error.HTTPError as e:
        cache[chave] = {"erro": f"HTTP {e.code}", "consultado_em": time.strftime("%Y-%m-%d")}
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        return {"erro": f"falha de rede: {e}"}  # não entra no cache: tenta de novo na próxima rodada
    time.sleep(0.2)
    return cache[chave]


def primeiro(v):
    if isinstance(v, list):
        return v[0] if v else None
    return v


def completar_crossref(item, cache, sem_rede, log, contagem):
    doi = item.get("DOI")
    if not doi:
        return
    faltam = [c for c in CAMPOS_CROSSREF if not item.get(c)]
    if not faltam:
        return
    if item.get("type") not in TIPOS_CROSSREF:
        contagem["tipo_sem_campos"].append(item["id"])
        return
    resp = crossref(doi, cache, sem_rede)
    if "ok" not in resp:
        log.aviso(item["id"], f"Crossref sem resposta para {doi}: {resp.get('erro')}")
        return
    cr = resp["ok"]
    t_bib, t_cr = " ".join(normaliza(item.get("title", ""))), " ".join(normaliza(primeiro(cr.get("title")) or ""))
    sim = difflib.SequenceMatcher(None, t_bib, t_cr).ratio()
    if sim < 0.6:
        log.aviso(item["id"], f"título do Crossref não bate com o do .bib (similaridade {sim:.2f}: "
                              f"«{primeiro(cr.get('title'))}»); nada completado")
        return
    novos = {
        "container-title": primeiro(cr.get("container-title")),
        "volume": cr.get("volume"),
        "issue": cr.get("issue"),
        "page": cr.get("page") or cr.get("article-number"),
    }
    if novos["volume"] and not re.match(r"^\d", str(novos["volume"])):
        log.aviso(item["id"], f"Crossref {doi}: volume não numérico ({novos['volume']!r}, publicação antecipada?); "
                              f"volume e número não completados")
        novos["volume"] = novos["issue"] = None
    mudou = False
    for campo in faltam:
        v = novos.get(campo)
        if v in (None, "", []):
            continue
        v = str(v).replace("–", "-")
        item[campo] = v
        log.add(item["id"], campo, None, v, f"Crossref {doi} (similaridade de título {sim:.2f})")
        mudou = True
    if mudou:
        contagem["crossref"] += 1
    else:
        log.aviso(item["id"], f"Crossref {doi} sem os campos que faltam ({', '.join(faltam)})")


# ------------------------------------------------------------------ principal
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--sem-rede", action="store_true", help="usa só o cache do Crossref")
    a = ap.parse_args()
    log = Log()
    itens, origem = [], {}
    for bib in BIBS:
        if not bib.exists():
            print(f"AVISO: {bib.relative_to(R)} não existe; seguindo sem ele", file=sys.stderr)
            log.aviso("(arquivo)", f"{bib.relative_to(R)} não existe; seguindo sem ele")
            continue
        for it in converter(bib):
            if it["id"] in origem:
                sys.exit(f"ERRO: chave repetida {it['id']} em {origem[it['id']]} e {bib.relative_to(R)}")
            origem[it["id"]] = str(bib.relative_to(R))
            it.pop("language", None)  # langid temporário do passo 1
            itens.append(it)

    por_id = {it["id"]: it for it in itens}
    contagem = {"crossref": 0, "tipo_sem_campos": []}

    # 2. sobreposições
    for chave, sob in SOBREPOSICOES.items():
        it = por_id.get(chave)
        if it is None:
            log.aviso(chave, "sobreposição prevista, mas a chave não está nos .bib")
            continue
        for campo, valor in sob["campos"].items():
            if it.get(campo) != valor:
                log.add(chave, campo, it.get(campo), valor, sob["fonte"])
                it[campo] = valor

    # 3. tipos
    for chave, (tipo, autor, motivo) in TIPOS.items():
        it = por_id.get(chave)
        if it is None:
            log.aviso(chave, f"tipo {tipo} previsto, mas a chave não está nos .bib")
            continue
        if it.get("type") != tipo:
            log.add(chave, "type", it.get("type"), tipo, motivo)
            it["type"] = tipo
        if autor is not None:
            novo = [{"literal": autor}]
            if it.get("author") != novo:
                log.add(chave, "author", it.get("author"), novo, f"autor institucional ({motivo})")
                it["author"] = novo
    for it in itens:
        if not it.get("type"):
            log.add(it["id"], "type", "", "document", "tipo vazio na conversão e sem regra em TIPOS")
            it["type"] = "document"

    # 3b. partículas de sobrenome: o pandoc grava "van der" (Meer) e "de" (Vreese, Kock) como dropping-particle,
    # que o CSL apaga na citação ("Meer 2015"). Em sobrenomes neerlandeses a partícula faz parte do nome citado:
    # passa a non-dropping-particle, que a APSA mostra na citação e ignora na ordenação (demote sort-only).
    for it in itens:
        for papel in ("author", "editor"):
            for nome in it.get(papel) or []:
                if nome.get("dropping-particle") and not nome.get("non-dropping-particle"):
                    antes = dict(nome)
                    nome["non-dropping-particle"] = nome.pop("dropping-particle")
                    log.add(it["id"], papel, antes, dict(nome), "partícula de sobrenome passada a non-dropping-particle "
                                                               "(citação \"van der Meer\", não \"Meer\")")

    # 4. idioma e 5. caixa alta
    for it in itens:
        lang, como = detectar_idioma(it)
        it["language"] = lang
        log.add(it["id"], "language", None, lang, f"detecção: {como}")
        for campo in ("title", "container-title"):
            if it.get(campo) and em_caixa_alta(it[campo]):
                novo = caixa_de_titulo(it[campo])
                log.add(it["id"], campo, it[campo], novo, "título inteiro em caixa alta passado a caixa de título")
                it[campo] = novo

    # 6. Crossref
    cache = ler_cache()
    for it in itens:
        completar_crossref(it, cache, a.sem_rede, log, contagem)
    CACHE.write_text(json.dumps(dict(sorted(cache.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    SAIDA.write_text(json.dumps(itens, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # 7. log
    linhas = [
        "# Log de preparar_referencias.py",
        "",
        "Gerado por `09-documento-final/revista/preparar_referencias.py`; não edite à mão. Uma linha por mudança em "
        "relação ao que o `quarto pandoc -f bibtex -t csljson` produz dos .bib (que não são alterados).",
        "",
        f"- Entradas: {len(itens)} ({', '.join(f'{sum(1 for v in origem.values() if v == b)} de {b}' for b in sorted(set(origem.values())))}).",
        f"- Entradas completadas pelo Crossref: {contagem['crossref']}.",
        f"- Avisos: {sum(1 for l in log.linhas if l[1] == 'AVISO')}.",
        f"- Com DOI, mas de tipo que não usa periódico, volume, número ou páginas (report, thesis, book, article), "
        f"por isso sem consulta ao Crossref: {', '.join(contagem['tipo_sem_campos']) or 'nenhuma'}.",
        "",
        "| Chave | Campo | Antes | Depois | Fonte ou motivo |",
        "|---|---|---|---|---|",
    ]
    for chave, campo, antes, depois, fonte in log.linhas:
        cel = lambda s: str(s).replace("|", "/").replace("\n", " ")
        if campo == "AVISO":
            linhas.append(f"| {cel(chave)} | AVISO |  | {cel(depois)} |  |")
        else:
            linhas.append(f"| {cel(chave)} | {cel(campo)} | {cel(fmt(antes))} | {cel(fmt(depois))} | {cel(fonte)} |")
    LOG.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"referencias.json: {len(itens)} entradas; {contagem['crossref']} completadas pelo Crossref; "
          f"{sum(1 for l in log.linhas if l[1] == 'AVISO')} aviso(s); log em {LOG.relative_to(R)}")


if __name__ == "__main__":
    main()
