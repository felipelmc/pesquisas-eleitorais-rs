"""Licenças e integridade do que a vitrine embute.

USO (de qualquer pasta):
    python3 09-documento-final/vitrine/qa/verificar_licencas.py [docs/index.html]

- vendor/: cada arquivo confere com vendor/SHA256SUMS, e cada biblioteca tem o LICENSE ao lado;
- fontes: cada woff2 embutido (base64 decodificado da página) é byte a byte o arquivo oficial, cujo SHA256 confere
  com revista/fontes/SHA256SUMS; os textos OFL-STIX.txt e OFL-Fira.txt estão na página;
- bibliotecas embutidas: o aviso de licença completo (ISC do D3) está na página junto do código;
- bibliotecas guardadas em vendor/ e não embutidas (topojson-client, world-atlas) só são listadas;
- o rodapé visível credita as fontes (OFL) e o D3 (ISC).
Sai com 1 se houver FALHA.
"""
import base64
import hashlib
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
VIT = RAIZ / "09-documento-final/vitrine"
FONTES = RAIZ / "09-documento-final/revista/fontes"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def somas(p, base):
    out = {}
    for l in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([0-9a-f]{64})\s+(\S+)$", l.strip())
        if m:
            out[m.group(2)] = m.group(1)
    return out


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    alvo = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "docs/index.html"
    if not alvo.is_absolute():
        alvo = RAIZ / alvo
    html = alvo.read_text(encoding="utf-8")
    falhas, ok, info = [], [], []

    # vendor
    sv = somas(VIT / "vendor/SHA256SUMS", VIT)
    for nome, h in sv.items():
        p = VIT / nome
        if nome.endswith("SHA256SUMS"):
            continue
        if not p.exists():
            falhas.append(f"vendor: {nome} listado e ausente")
        elif sha(p.read_bytes()) != h:
            falhas.append(f"vendor: {nome} com SHA256 diferente do registrado")
        else:
            ok.append(f"vendor: {nome} confere")
    for lib, lic in (("d3-7.9.0.min.js", "LICENSE-d3.txt"), ("topojson-client-3.1.0.min.js", "LICENSE-topojson-client.txt"),
                     ("world-atlas-2.0.2-countries-110m.json", "LICENSE-world-atlas.txt")):
        if not (VIT / "vendor" / lic).exists():
            falhas.append(f"vendor: {lib} sem {lic}")
        codigo = (VIT / "vendor" / lib).read_text(encoding="utf-8")
        embutido = codigo[:2000] in html
        if embutido:
            if norm((VIT / "vendor" / lic).read_text(encoding="utf-8")) not in norm(html):
                falhas.append(f"página: {lib} embutido sem o aviso de licença completo ({lic})")
            else:
                ok.append(f"página: {lib} embutido com o aviso {lic}")
        else:
            info.append(f"página: {lib} não embutido (guardado em vendor/ com {lic})")

    # fontes
    sf = somas(FONTES / "SHA256SUMS", FONTES)
    for nome in ("OFL-STIX.txt", "OFL-Fira.txt"):
        texto = (FONTES / nome).read_text(encoding="utf-8")
        if sf.get(nome) and sha((FONTES / nome).read_bytes()) != sf[nome]:
            falhas.append(f"fontes: {nome} com SHA256 diferente do registrado")
        if norm(texto) not in norm(html.replace("* /", "*/")):
            falhas.append(f"página: texto de {nome} ausente")
        else:
            ok.append(f"página: {nome} presente")
    oficiais = {sha(p.read_bytes()): p.name for p in (FONTES / "woff2").glob("*.woff2")}
    for p in (FONTES / "woff2").glob("*.woff2"):
        chave = f"woff2/{p.name}"
        if chave in sf and sf[chave] != sha(p.read_bytes()):
            falhas.append(f"fontes: {p.name} com SHA256 diferente do registrado")
    emb = re.findall(r"url\(data:font/woff2;base64,([A-Za-z0-9+/=]+)\)", html)
    if not emb:
        falhas.append("página: nenhuma fonte woff2 embutida")
    for b64 in emb:
        h = sha(base64.b64decode(b64))
        if h not in oficiais:
            falhas.append("página: fonte embutida que não é byte a byte um woff2 oficial")
        elif f"woff2/{oficiais[h]}" not in sf:
            falhas.append(f"página: {oficiais[h]} embutida sem registro em SHA256SUMS")
        else:
            ok.append(f"página: {oficiais[h]} embutida, idêntica ao oficial")

    # créditos visíveis
    rod = re.search(r'<footer class="rodape">(.*?)</footer>', html, re.S)
    txt = re.sub(r"<[^>]+>", " ", rod.group(1)) if rod else ""
    for termo in ("Open Font License", "D3", "ISC", "STIX Two Text", "Fira Sans"):
        if termo not in txt:
            falhas.append(f"rodapé: crédito sem {termo!r}")
    if not falhas:
        ok.append("rodapé: créditos de fontes e bibliotecas presentes")

    for o in ok:
        print("OK    ", o)
    for i in info:
        print("INFO  ", i)
    for f in falhas:
        print("FALHA ", f)
    print("RESULTADO:", "FALHA" if falhas else "OK", f"({len(falhas)} falha(s))")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
