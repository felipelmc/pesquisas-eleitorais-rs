#!/usr/bin/env python3
"""
Recupera resumos (abstracts) para os 336 registros em registros_336.csv.

Cascata por registro (para no primeiro resumo real >= 40 palavras):
  1. OpenAlex (por DOI e, se falhar, pelo id_fonte / W-id)
  2. Crossref (campo "abstract", tags JATS removidas)
  3. Semantic Scholar Graph API (abstract; tldr guardado como fallback)
  4. Europe PMC (abstractText, por DOI)
  5. OpenAlex por título (só para registros sem DOI, ano +-1)
  6. Meta tags da página de pouso do DOI (ou da coluna url, se não houver DOI)

Reaproveita resumos reais já recuperados numa sessão anterior
(02-triagem/sem_resumo/registros.json e sem_resumo_sn1/registros.json),
marcando a fonte como "sessao_anterior:<fonte original>". TLDRs de sessão
anterior não contam como resumo real, mas ficam guardados como fallback.

Não usa Sci-Hub, LibGen, Anna's Archive, Z-Library, ResearchGate,
Academia.edu, Scribd nem espelhos, nem contorna paywall/login/captcha.

Saída: 02-triagem/sem_resumo_revisao/resumos_recuperados.csv
"""

import csv
import json
import re
import sys
import time
import unicodedata
import difflib
from html import unescape
from urllib.parse import quote

import requests

BASE_DIR = "/Users/felipelmc/Desktop/pesquisas-eleitorais-rs/02-triagem"
INPUT_CSV = f"{BASE_DIR}/sem_resumo_revisao/registros_336.csv"
PREV_FILES = [
    f"{BASE_DIR}/sem_resumo/registros.json",
    f"{BASE_DIR}/sem_resumo_sn1/registros.json",
]
OUTPUT_CSV = f"{BASE_DIR}/sem_resumo_revisao/resumos_recuperados.csv"
LOG_FILE = f"{BASE_DIR}/sem_resumo_revisao/recuperar_resumos.log"

DATA_CONSULTA = "2026-09-23"
MIN_WORDS = 40
USER_AGENT = "pesquisas-eleitorais-rs (systematic review; contact via GitHub felipelmc)"
HEADERS = {"User-Agent": USER_AGENT}

BLOCKED_DOMAINS = [
    "sci-hub", "libgen", "annas-archive", "anna-archive", "z-lib", "zlibrary",
    "researchgate.net", "academia.edu", "scribd.com",
]

PLACEHOLDER_EXACT = {
    "no abstract available", "abstract not available", "not available",
    "no abstract", "n/a", "abstract unavailable", "no abstract provided",
    "sem resumo", "resumo nao disponivel", "resumo indisponivel",
}

session = requests.Session()
session.headers.update(HEADERS)


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, file=sys.stderr)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def normalize_ws(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def strip_tags(text):
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    return unescape(text)


def word_count(text):
    text = (text or "").strip()
    if not text:
        return 0
    return len(text.split())


def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)
    )


def normalize_title(t):
    t = strip_accents((t or "").lower())
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def is_placeholder(text):
    t = normalize_ws(text).lower().strip(" .")
    if not t:
        return True
    if t in PLACEHOLDER_EXACT:
        return True
    if len(t) < 60 and ("no abstract" in t or "abstract not available" in t or "not available" in t):
        return True
    return False


def is_blocked_url(url):
    u = (url or "").lower()
    return any(b in u for b in BLOCKED_DOMAINS)


def title_match(t1, t2, year1=None, year2=None):
    n1, n2 = normalize_title(t1), normalize_title(t2)
    if not n1 or not n2:
        return False
    ratio = difflib.SequenceMatcher(None, n1, n2).ratio()
    if ratio < 0.90:
        return False
    if year1 and year2:
        try:
            if abs(int(year1) - int(year2)) > 1:
                return False
        except (ValueError, TypeError):
            pass
    return True


def reconstruct_abstract(inv_index):
    if not inv_index:
        return ""
    positions = {}
    max_pos = 0
    for word, idxs in inv_index.items():
        for i in idxs:
            positions[i] = word
            if i > max_pos:
                max_pos = i
    return " ".join(positions.get(i, "") for i in range(max_pos + 1))


def safe_get(url, params=None, timeout=20):
    try:
        return session.get(url, params=params, timeout=timeout)
    except requests.RequestException as e:
        log(f"  ERRO de rede em {url}: {e}")
        return None


# ---------------------------------------------------------------- OpenAlex

def openalex_by_doi(doi):
    url = f"https://api.openalex.org/works/doi:{quote(doi, safe='')}"
    r = safe_get(url)
    if r is None or r.status_code != 200:
        return None, url
    try:
        data = r.json()
    except ValueError:
        return None, url
    text = normalize_ws(reconstruct_abstract(data.get("abstract_inverted_index")))
    return (text if text else None), url


def openalex_by_id(wid):
    wid = wid.strip()
    url = f"https://api.openalex.org/works/{wid}"
    r = safe_get(url)
    if r is None or r.status_code != 200:
        return None, url
    try:
        data = r.json()
    except ValueError:
        return None, url
    text = normalize_ws(reconstruct_abstract(data.get("abstract_inverted_index")))
    return (text if text else None), url


def openalex_by_title(title, year):
    url = "https://api.openalex.org/works"
    params = {"filter": f"title.search:{title}", "per_page": 5}
    r = safe_get(url, params=params)
    if r is None or r.status_code != 200:
        return None, url
    try:
        data = r.json()
    except ValueError:
        return None, url
    for item in data.get("results", []):
        t2 = item.get("title", "") or ""
        y2 = item.get("publication_year")
        if title_match(title, t2, year, y2):
            text = normalize_ws(reconstruct_abstract(item.get("abstract_inverted_index")))
            if text:
                return text, item.get("id", url)
    return None, url


# ---------------------------------------------------------------- Crossref

def crossref_by_doi(doi):
    url = f"https://api.crossref.org/works/{quote(doi, safe='')}"
    r = safe_get(url)
    if r is None or r.status_code != 200:
        return None, url
    try:
        data = r.json()
    except ValueError:
        return None, url
    abstract = (data.get("message") or {}).get("abstract")
    if not abstract:
        return None, url
    text = normalize_ws(strip_tags(abstract))
    return (text if text else None), url


# --------------------------------------------------------- Semantic Scholar

# Circuito de proteção: se o pool público (sem chave) estiver saturado
# (comum quando a saída de rede é compartilhada por várias sessões), muitas
# tentativas consecutivas de 429 não vão se resolver com mais espera.
# Depois de algumas falhas totais seguidas, desligamos o S2 pelo resto da
# execução em vez de gastar minutos por registro em backoff inútil; os
# demais passos da cascata (Europe PMC, página de pouso, TLDR de sessão
# anterior) continuam normalmente.
_S2_STATE = {"disabled": False, "consecutive_failures": 0, "max_consecutive": 3}


def semantic_scholar_by_doi(doi):
    """Retorna (abstract_or_None, tldr_or_None, url). Dorme ~1.1s ao final de cada chamada feita."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi, safe='')}"
    if _S2_STATE["disabled"]:
        return None, None, url
    params = {"fields": "abstract,tldr"}
    abstract, tldr = None, None
    max_attempts = 2
    backoffs = [3, 6]
    got_response = False
    for attempt in range(max_attempts):
        r = safe_get(url, params=params)
        if r is None:
            time.sleep(1.1)
            break
        if r.status_code == 200:
            got_response = True
            try:
                data = r.json()
            except ValueError:
                data = {}
            a = data.get("abstract")
            if a:
                abstract = normalize_ws(a)
            t = data.get("tldr")
            if t and t.get("text"):
                tldr = normalize_ws(t["text"])
            break
        elif r.status_code == 429:
            wait = backoffs[min(attempt, len(backoffs) - 1)]
            log(f"  Semantic Scholar 429, aguardando {wait}s (tentativa {attempt+1})")
            time.sleep(wait)
            continue
        elif r.status_code == 404:
            got_response = True
            break
        else:
            log(f"  Semantic Scholar status {r.status_code} para {doi}")
            break
    time.sleep(1.1)

    if got_response:
        _S2_STATE["consecutive_failures"] = 0
    else:
        _S2_STATE["consecutive_failures"] += 1
        if _S2_STATE["consecutive_failures"] >= _S2_STATE["max_consecutive"]:
            _S2_STATE["disabled"] = True
            log("  Semantic Scholar: pool público parece saturado (429 persistente); "
                "desligando esta fonte pelo resto da execução.")
    return abstract, tldr, url


# ------------------------------------------------------------- Europe PMC

def europepmc_by_doi(doi):
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    # resultType "lite" (o padrão) nunca inclui abstractText; precisa de "core".
    params = {"query": f'DOI:"{doi}"', "format": "json", "resultType": "core"}
    r = safe_get(url, params=params)
    if r is None or r.status_code != 200:
        return None, url
    try:
        data = r.json()
    except ValueError:
        return None, url
    results = (data.get("resultList") or {}).get("result", [])
    for item in results:
        abstract = item.get("abstractText")
        if abstract:
            text = normalize_ws(strip_tags(abstract))
            if text:
                return text, url
    return None, url


# ------------------------------------------------------------- Landing page

META_NAMES = ["citation_abstract", "dc.description", "og:description", "description"]

META_PATTERNS = []
for name in META_NAMES:
    esc = re.escape(name)
    META_PATTERNS.append((name, re.compile(
        rf'<meta[^>]+(?:name|property)=["\']{esc}["\'][^>]*content=["\'](.*?)["\']',
        re.IGNORECASE | re.DOTALL)))
    META_PATTERNS.append((name, re.compile(
        rf'<meta[^>]+content=["\'](.*?)["\'][^>]*(?:name|property)=["\']{esc}["\']',
        re.IGNORECASE | re.DOTALL)))

BOT_BLOCK_MARKERS = [
    "captcha", "are you a human", "access denied", "verify you are human",
    "please enable javascript and cookies", "attention required! | cloudflare",
]


def landing_page_meta(target_url):
    if not target_url or is_blocked_url(target_url):
        return None, target_url
    r = safe_get(target_url, timeout=25)
    if r is None:
        return None, target_url
    if r.status_code != 200:
        return None, r.url
    if is_blocked_url(r.url):
        return None, r.url
    ctype = r.headers.get("Content-Type", "")
    if "html" not in ctype.lower():
        return None, r.url
    html = r.text
    low = html.lower()
    if any(m in low for m in BOT_BLOCK_MARKERS):
        return None, r.url
    for name, pattern in META_PATTERNS:
        m = pattern.search(html)
        if m:
            text = normalize_ws(strip_tags(unescape(m.group(1))))
            if word_count(text) >= MIN_WORDS and not is_placeholder(text):
                return text, r.url
    return None, r.url


# ------------------------------------------------------------------ Sessão anterior

def load_previous_session():
    lookup = {}
    for fpath in PREV_FILES:
        try:
            with open(fpath, encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, ValueError) as e:
            log(f"Aviso: não foi possível ler {fpath}: {e}")
            continue
        for rec in data:
            id_rs = rec.get("id_rs")
            if id_rs:
                lookup[id_rs] = rec
    return lookup


# ------------------------------------------------------------------ Núcleo

def resolve_record(row, prev_lookup, stats):
    id_rs = row["id_rs"]
    doi = (row.get("doi") or "").strip()
    titulo = (row.get("titulo") or "").strip()
    ano = (row.get("ano") or "").strip()
    id_fonte = (row.get("id_fonte") or "").strip()
    url_col = (row.get("url") or "").strip()

    fallback_tldr = None
    fallback_tldr_url = ""

    # --- 1. Reaproveitar sessão anterior, se houver resumo real
    prev = prev_lookup.get(id_rs)
    if prev:
        resumo_prev = normalize_ws(prev.get("resumo_externo") or "")
        fonte_prev = (prev.get("fonte_resumo") or "").strip()
        if resumo_prev:
            if resumo_prev.startswith("[TLDR]"):
                fallback_tldr = normalize_ws(resumo_prev[len("[TLDR]"):])
                fallback_tldr_url = f"https://doi.org/{doi}" if doi else url_col
            elif word_count(resumo_prev) >= MIN_WORDS and not is_placeholder(resumo_prev):
                stats["sessao_anterior"] += 1
                return {
                    "id_rs": id_rs, "doi": doi, "titulo": titulo,
                    "resumo": resumo_prev,
                    "fonte_resumo": f"sessao_anterior:{fonte_prev}" if fonte_prev else "sessao_anterior:desconhecida",
                    "url_fonte": f"https://doi.org/{doi}" if doi else url_col,
                    "n_palavras": word_count(resumo_prev),
                    "data_consulta": DATA_CONSULTA,
                }

    # --- 2. Cascata ao vivo
    # 2a. OpenAlex por DOI
    if doi:
        text, src = openalex_by_doi(doi)
        if text and word_count(text) >= MIN_WORDS and not is_placeholder(text):
            stats["openalex"] += 1
            return _mk(id_rs, doi, titulo, text, "openalex", src)

    # 2b. OpenAlex por id_fonte (W-id)
    if id_fonte:
        text, src = openalex_by_id(id_fonte)
        if text and word_count(text) >= MIN_WORDS and not is_placeholder(text):
            stats["openalex"] += 1
            return _mk(id_rs, doi, titulo, text, "openalex", src)

    # 2c. Crossref
    if doi:
        text, src = crossref_by_doi(doi)
        if text and word_count(text) >= MIN_WORDS and not is_placeholder(text):
            stats["crossref"] += 1
            return _mk(id_rs, doi, titulo, text, "crossref", src)

    # 2d. Semantic Scholar
    if doi:
        text, tldr, src = semantic_scholar_by_doi(doi)
        if text and word_count(text) >= MIN_WORDS and not is_placeholder(text):
            stats["semantic_scholar"] += 1
            return _mk(id_rs, doi, titulo, text, "semantic_scholar", src)
        if tldr and not fallback_tldr:
            fallback_tldr = tldr
            fallback_tldr_url = src

    # 2e. Europe PMC
    if doi:
        text, src = europepmc_by_doi(doi)
        if text and word_count(text) >= MIN_WORDS and not is_placeholder(text):
            stats["europepmc"] += 1
            return _mk(id_rs, doi, titulo, text, "europepmc", src)

    # 2f. OpenAlex por título (registros sem DOI)
    if not doi and titulo:
        text, src = openalex_by_title(titulo, ano)
        if text and word_count(text) >= MIN_WORDS and not is_placeholder(text):
            stats["openalex"] += 1
            return _mk(id_rs, doi, titulo, text, "openalex", src)

    # 2g. Meta tags da página de pouso
    target = f"https://doi.org/{doi}" if doi else url_col
    text, src = landing_page_meta(target)
    if text and word_count(text) >= MIN_WORDS and not is_placeholder(text):
        stats["landing_meta"] += 1
        return _mk(id_rs, doi, titulo, text, "landing_meta", src)

    # --- 3. Fallback TLDR (sessão anterior ou desta sessão)
    if fallback_tldr:
        stats["semantic_scholar_tldr"] += 1
        return _mk(id_rs, doi, titulo, fallback_tldr, "semantic_scholar_tldr", fallback_tldr_url)

    # --- 4. Nada encontrado
    stats["nenhum"] += 1
    return _mk(id_rs, doi, titulo, "", "nenhum", "")


def _mk(id_rs, doi, titulo, resumo, fonte, url_fonte):
    return {
        "id_rs": id_rs,
        "doi": doi,
        "titulo": titulo,
        "resumo": resumo,
        "fonte_resumo": fonte,
        "url_fonte": url_fonte or "",
        "n_palavras": word_count(resumo),
        "data_consulta": DATA_CONSULTA,
    }


def main():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"Início: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    with open(INPUT_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    log(f"Registros carregados: {len(rows)}")

    prev_lookup = load_previous_session()
    log(f"Registros na sessão anterior: {len(prev_lookup)}")

    stats = {
        "sessao_anterior": 0, "openalex": 0, "crossref": 0,
        "semantic_scholar": 0, "europepmc": 0, "landing_meta": 0,
        "semantic_scholar_tldr": 0, "nenhum": 0,
    }
    errors = []

    out_rows = []
    for i, row in enumerate(rows, 1):
        try:
            result = resolve_record(row, prev_lookup, stats)
        except Exception as e:
            log(f"ERRO inesperado em {row.get('id_rs')}: {e}")
            errors.append((row.get("id_rs"), str(e)))
            result = _mk(row["id_rs"], row.get("doi", ""), row.get("titulo", ""), "", "nenhum", "")
            stats["nenhum"] += 1
        out_rows.append(result)
        if i % 20 == 0 or i == len(rows):
            log(f"Progresso: {i}/{len(rows)} | {stats}")

    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "id_rs", "doi", "titulo", "resumo", "fonte_resumo",
            "url_fonte", "n_palavras", "data_consulta",
        ])
        writer.writeheader()
        writer.writerows(out_rows)

    log(f"Concluído. Estatísticas finais: {stats}")
    log(f"Erros: {len(errors)}")
    for id_rs, msg in errors:
        log(f"  {id_rs}: {msg}")
    log(f"Saída escrita em: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
