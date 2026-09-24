"""Links da vitrine: todo href existe em docs/ e toda âncora existe na página de destino.

USO (de qualquer pasta):
    python3 09-documento-final/vitrine/qa/checar_links.py [docs/index.html ...]

- "#id": o id tem de existir na própria página (FALHA se não existir);
- "arquivo" ou "arquivo#id": o arquivo tem de existir em docs/. Documento ainda não publicado vira AVISO.
  Âncora ausente num documento publicado é FALHA, salvo se a âncora estiver no contrato de rótulos do artigo
  (revista/rotulos.yml): aí vira AVISO, porque o artigo novo ainda não substituiu a versão publicada;
- links externos são listados (INFO); a página não carrega nada de fora, mas pode apontar para fora.
Sai com 1 se houver FALHA.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

RAIZ = Path(__file__).resolve().parents[3]
DOCS = RAIZ / "docs"


class Coleta(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        if tag in ("a", "link", "area") and a.get("href") is not None:
            self.hrefs.append(a["href"])


def coletar(p):
    c = Coleta()
    html = p.read_text(encoding="utf-8", errors="replace")
    # a vitrine é autocontida: ignora HTML dentro dos <script> (JSON e JS) para não contar links de dados
    c.feed(re.sub(r"<script\b.*?</script>", " ", html, flags=re.S))
    # links gerados pelo JS a partir dos dados (href="revisao.html#...") também são conferidos
    js_hrefs = re.findall(r"href=\\?\"([^\"\\]+)\\?\"", " ".join(re.findall(r"<script\b.*?</script>", html, flags=re.S)))
    js_hrefs += re.findall(r"href=\"(revisao\.html#[\w-]+|[\w.-]+\.(?:html|pdf|docx)(?:#[\w-]+)?)", html)
    # links montados pelo JS com dados (gaveta do mapa: revisao.html#<seção do bloco>)
    m = re.search(r'<script type="application/json" id="dados-vitrine">(.*?)</script>', html, re.S)
    if m:
        import json
        dados = json.loads(m.group(1).replace("<\\/", "</"))
        js_hrefs += [f"revisao.html#{b['secao']}" for b in dados.get("blocos", [])]
    return c, [h for h in js_hrefs if not h.startswith(("http", "#", "data:")) and not re.search(r"['\s+]", h)]


def contrato():
    t = (RAIZ / "09-documento-final/revista/rotulos.yml").read_text(encoding="utf-8")
    return set(re.findall(r"\b((?:sec|fig|tbl|qdr)-[\w-]+)", t)) | {"mensagens-principais", "resumo-executivo", "resumo",
                                                                     "abstract", "informacoes-adicionais", "referencias"}


def main():
    alvos = [Path(a) if Path(a).is_absolute() else RAIZ / a for a in sys.argv[1:]] or [DOCS / "index.html"]
    falhas, avisos, info = [], [], []
    ids_cache = {}
    ctr = contrato()
    for alvo in alvos:
        c, js = coletar(alvo)
        ids_cache[alvo.name] = c.ids
        todos = [(h, "html") for h in c.hrefs] + [(h, "js") for h in sorted(set(js))]
        vistos = set()
        for h, origem in todos:
            if (h, origem) in vistos:
                continue
            vistos.add((h, origem))
            u = urlparse(h)
            if u.scheme in ("http", "https", "mailto"):
                info.append(f"{alvo.name}: link externo {h}")
                continue
            arq, anc = unquote(u.path), u.fragment
            if not arq:
                if anc and anc not in c.ids:
                    falhas.append(f"{alvo.name}: âncora #{anc} não existe na página")
                continue
            destino = (alvo.parent / arq).resolve()
            if not destino.exists():
                avisos.append(f"{alvo.name}: {arq} ainda não existe em docs/ (documento não publicado)")
                continue
            if anc:
                if destino.name not in ids_cache:
                    ids_cache[destino.name] = coletar(destino)[0].ids if destino.suffix == ".html" else set()
                if anc not in ids_cache[destino.name]:
                    if anc in ctr:
                        avisos.append(f"{alvo.name}: {arq}#{anc}: âncora do contrato do artigo novo, ainda ausente na versão publicada")
                    else:
                        falhas.append(f"{alvo.name}: {arq}#{anc}: âncora inexistente no destino")
        print(f"{alvo.name}: {len(set(c.hrefs))} href(s) no HTML, {len(set(js))} gerado(s) pelo JS")
    for i in sorted(set(info)):
        print("INFO  ", i)
    for a in sorted(set(avisos)):
        print("AVISO ", a)
    for f in sorted(set(falhas)):
        print("FALHA ", f)
    print("RESULTADO:", "FALHA" if falhas else "OK", f"({len(set(falhas))} falha(s), {len(set(avisos))} aviso(s))")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
