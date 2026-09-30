"""Pacote de replicação público da síntese (docs/pacote-replicacao.zip), sem resumos nem e-mails de terceiros.

USO (da raiz):  python3 ferramentas/montar_pacote.py docs/pacote-replicacao.zip

O repositório completo (trilha de auditoria) é privado. Este pacote leva o que um terceiro precisa para conferir e
refazer a síntese a partir dos efeitos extraídos (Emenda 7; auditoria final, itens A29 e A35):

- protocolo, emendas, pergunta, teoria do programa e codebooks (00-protocolo/);
- estratégias de busca ativas, log de buscas e a conferência do PRESS (01-busca/);
- registros deduplicados SÓ com metadados bibliográficos: sem resumo, sem instituição e sem e-mail (dados/);
- decisões de triagem e de texto completo, incluídos e contagens do PRISMA;
- fichamentos (sem o caminho local do PDF), efeitos por estudo, risco de viés e toda a síntese (06-analise/, sem a
  pasta de versões superadas), com os scripts de montagem do repositório;
- declaração de uso de IA, listas de conferência, a declaração do autor e as pendências abertas;
- o artigo em PDF (docs/revisao.pdf, se já existir) e uma cópia da skill `revisao-sistematica` (scripts e licença do
  próprio autor), que tem o motor de SWiM, meta-análise, PRISMA e deduplicação;
- LEIA.md, LICENSE (MIT), LICENSE-CC-BY-4.0.md, CITATION.cff, ambiente.txt e MANIFESTO.csv (caminho no pacote,
  origem, bytes e SHA256 de cada arquivo).

Não entram: resumos (dados/registros*.csv, lotes de triagem, fontes brutas), PDFs de terceiros, fichas de
elegibilidade e de extração em Markdown, prompts e pacotes de revisão humana, o log bruto da skill.

Sanitização (sai com erro se falhar): nenhum endereço de e-mail, nenhum caminho local (/Users/, ~/), e nenhum trecho
de 60 caracteres de um resumo de registro não incluído aparece em arquivo de texto do pacote.
"""
import csv
import hashlib
import io
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

csv.field_size_limit(10 ** 9)
R = Path(__file__).resolve().parents[1]
SKILL = Path.home() / ".claude/skills/revisao-sistematica"
RX_EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[a-z]{2,}", re.I)
RX_LOCAL = re.compile(r"/Users/[^\s\"'`)<>]*|~/(?:Desktop|revisoes)[^\s\"'`)<>]*")
TEXTO = {".md", ".csv", ".txt", ".json", ".py", ".R", ".mmd", ".yml", ".yaml", ".cff", ".svg", ".qmd", ".tsv"}
COLS_REGISTROS = ["id_rs", "id_estudo", "chave", "fontes", "n_fontes", "tipo_duplicata", "metodo_identificacao",
                  "id_fonte", "doi", "titulo", "titulo_alt", "autores", "ano", "tipo_publicacao", "idioma", "veiculo",
                  "volume", "numero", "paginas", "url"]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def csv_bytes(cols, linhas):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(linhas)
    return buf.getvalue().encode("utf-8")


def arquivos():
    """Lista (caminho no pacote, origem legível, bytes)."""
    itens = []

    def add(rel, destino=None):
        p = R / rel
        itens.append((destino or rel, rel, p.read_bytes()))

    def add_glob(padrao, excluir=()):
        for p in sorted(R.glob(padrao)):
            rel = str(p.relative_to(R))
            if p.is_file() and not any(x in rel for x in excluir) and "__pycache__" not in rel:
                add(rel)

    # protocolo
    for f in ("protocolo.md", "emendas.md", "pergunta.md", "teoria_programa.md", "dag_v1.mmd",
              "codebook_elegibilidade.csv", "codebook_v0_efetividade.csv", "codebook_v0_rob2.csv",
              "codebook_v0_robins_i.csv", "codebook_v0_epoc.csv", "correcao_atribuicao.csv", "ancoras_validacao.csv"):
        add(f"00-protocolo/{f}")
    # busca
    for f in ("S-oa-en-v5.txt", "S-oa-pt-v3.txt", "S-oa-es-v3.txt", "S-bdtd-v3.txt"):
        add(f"01-busca/strings/{f}")
    add("01-busca/log_buscas.csv")
    add("01-busca/press_revisor_humano_1.md")
    # registros só com metadados bibliográficos
    for f in ("registros_unicos.csv",):
        linhas = list(csv.DictReader(open(R / "dados" / f, encoding="utf-8-sig")))
        for l in linhas:
            for c in COLS_REGISTROS:
                l[c] = RX_EMAIL.sub("[e-mail removido]", l.get(c) or "")
        itens.append((f"dados/{f}", f"dados/{f} (colunas: {', '.join(COLS_REGISTROS)})",
                      csv_bytes(COLS_REGISTROS, linhas)))
    # decisões e relato
    for rel in ("02-triagem/triagem_ta_final.csv", "03-textos/elegibilidade_tc_final.csv",
                "07-relatorio/incluidos.csv", "07-relatorio/prisma_contagens.json", "07-relatorio/prisma.svg",
                "07-relatorio/checklist_prisma.csv", "07-relatorio/checklist_swim.csv",
                "07-relatorio/declaracao_uso_ia.md", "07-relatorio/_pendencias_abertas.json",
                "09-documento-final/declaracao_ia_v2.md", "08-revisao-humana/declaracao_autor_2026-09-30.md",
                "08-revisao-humana/P019_dedup/declaracao_autor_2026-09-30_dedup.md",
                "08-revisao-humana/P019_dedup/dedup_revisao_v2_versoes.csv"):
        add(rel)
    # decisões de deduplicação do autor (P019, aplicadas pela Emenda 8), sem os resumos truncados dos pares
    linhas = list(csv.DictReader(open(R / "08-revisao-humana/P019_dedup/dedup_revisao_v1.csv", encoding="utf-8-sig")))
    cols = [c for c in linhas[0] if not c.startswith("resumo_")]
    itens.append(("08-revisao-humana/P019_dedup/dedup_revisao_v1.csv",
                  "08-revisao-humana/P019_dedup/dedup_revisao_v1.csv (sem resumo_a e resumo_b)", csv_bytes(cols, linhas)))
    # extração: master sem o caminho local do PDF
    linhas = list(csv.DictReader(open(R / "05-decomposicao/fichamentos_master.csv", encoding="utf-8-sig")))
    cols = [c for c in linhas[0] if c != "pdf_path"]
    itens.append(("05-decomposicao/fichamentos_master.csv", "05-decomposicao/fichamentos_master.csv (sem pdf_path)",
                  csv_bytes(cols, linhas)))
    add_glob("05-decomposicao/efeitos/*.csv")
    for rel in ("05-decomposicao/efeitos_extraidos.csv", "05-decomposicao/efeitos_para_sintese.csv",
                "05-decomposicao/verificacao_efeitos.csv", "05-decomposicao/juntar_rob.py"):
        add(rel)
    # risco de viés
    add_glob("04-qualidade/rob_*_consenso.csv")
    add("04-qualidade/rob_geral.csv")
    # síntese
    add_glob("06-analise/*", excluir=("_superado", "06-analise/prompt_"))
    for pasta in sorted(R.glob("06-analise/swim_*")) + sorted(R.glob("06-analise/meta_*")):
        if pasta.is_dir():
            add_glob(f"{pasta.relative_to(R)}/**/*")
    add_glob("06-analise/tabelas/*")
    # tabelas que não entram nos apêndices do PDF: estudos da região, viabilidade e listas de conferência (PRISMA
    # 2020, resumo, PRISMA-S, SWiM, PRISMA-trAIce), com o local de cada item no artigo final e nos apêndices
    for f in ("regional.md", "viabilidade.md"):
        add(f"09-documento-final/insumos/tabelas/{f}", f"tabelas-extras/{f}")
    for p in sorted((R / "09-documento-final/insumos/tabelas").glob("checklist_*.md")):
        add(str(p.relative_to(R)), f"tabelas-extras/{p.name}")
    # artigo
    if (R / "docs/revisao.pdf").exists():
        add("docs/revisao.pdf", "artigo/revisao.pdf")
    # skill (motor da síntese), com a licença do autor
    for p in sorted((SKILL / "scripts").rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
            rel = p.relative_to(SKILL)
            itens.append((f"skill-revisao-sistematica/{rel}", f"skill revisao-sistematica/{rel}", p.read_bytes()))
    itens.append(("skill-revisao-sistematica/LICENSE.txt", "skill revisao-sistematica/LICENSE.txt",
                  (SKILL / "LICENSE.txt").read_bytes()))
    # documentos do pacote
    for f in ("LICENSE", "LICENSE-CC-BY-4.0.md", "CITATION.cff"):
        add(f)
    add("ferramentas/pacote/LEIA.md", "LEIA.md")
    itens.append(("ambiente.txt", "gerado por montar_pacote.py", ambiente().encode("utf-8")))
    return itens


def versao(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return (r.stdout or r.stderr).strip().splitlines()[0]
    except Exception as e:  # noqa: BLE001
        return f"não disponível ({type(e).__name__})"


def ambiente():
    r_pac = versao(["Rscript", "-e", 'cat(R.version.string, "| metafor", as.character(packageVersion("metafor")), '
                                     '"| clubSandwich", as.character(packageVersion("clubSandwich")))'])
    return "\n".join([
        "Ambiente em que a síntese e o artigo foram gerados",
        f"Python: {versao([sys.executable, '--version'])}",
        f"R: {r_pac}",
        f"Quarto: {versao(['quarto', '--version'])}",
        f"Typst (embutido no Quarto): {versao(['quarto', 'typst', '--version'])}",
        "",
    ])


def resumos_de_terceiros():
    """Trechos de 60 caracteres (do meio) de cada resumo de registro não incluído, para a sanitização."""
    incl = {l["chave"] for l in csv.DictReader(open(R / "07-relatorio/incluidos.csv", encoding="utf-8-sig"))}
    trechos = set()
    for l in csv.DictReader(open(R / "dados/registros_unicos.csv", encoding="utf-8-sig")):
        t = re.sub(r"\s+", " ", l.get("resumo") or "").strip()
        if len(t) >= 200 and l.get("chave") not in incl:
            meio = len(t) // 2
            trecho = t[meio:meio + 60]
            if trecho not in re.sub(r"\s+", " ", l.get("titulo") or ""):   # resumo que repete o título não conta
                trechos.add(trecho)
    return trechos


def sanitizar(itens):
    trechos = resumos_de_terceiros()
    erros = []
    for destino, _, b in itens:
        if Path(destino).suffix not in TEXTO and Path(destino).name not in ("LICENSE",):
            continue
        t = b.decode("utf-8", errors="replace")
        for m in RX_EMAIL.finditer(t):
            erros.append(f"{destino}: e-mail {m.group(0)!r}")
            break
        for m in RX_LOCAL.finditer(t):
            erros.append(f"{destino}: caminho local {m.group(0)[:60]!r}")
            break
        tn = re.sub(r"\s+", " ", t)
        for tr in trechos:
            if tr in tn:
                erros.append(f"{destino}: trecho de resumo de terceiro: {tr[:40]!r}…")
                break
    return erros


def main():
    saida = Path(sys.argv[1] if len(sys.argv) > 1 else R / "docs/pacote-replicacao.zip")
    itens = arquivos()
    erros = sanitizar(itens)
    if erros:
        raise SystemExit("ERRO: pacote não sanitizado (nada gravado):\n  " + "\n  ".join(erros[:40])
                         + (f"\n  ... e mais {len(erros) - 40}" if len(erros) > 40 else ""))
    manifesto = csv_bytes(["caminho", "origem", "bytes", "sha256"],
                          [{"caminho": d, "origem": o, "bytes": len(b), "sha256": sha(b)} for d, o, b in itens])
    data = (1980, 1, 1, 0, 0, 0)  # datas fixas: o zip não muda se o conteúdo não mudar
    with zipfile.ZipFile(saida, "w", zipfile.ZIP_DEFLATED) as z:
        for destino, _, b in sorted(itens) + [("MANIFESTO.csv", "", manifesto)]:
            zi = zipfile.ZipInfo(f"pacote-replicacao/{destino}", date_time=data)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, b)
    print(f"{saida}: {len(itens) + 1} arquivos, {saida.stat().st_size / 1e6:.1f} MB; sanitização OK")


if __name__ == "__main__":
    main()
