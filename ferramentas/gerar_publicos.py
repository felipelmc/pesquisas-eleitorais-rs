"""Versões públicas, sem resumos nem trechos de terceiros, dos arquivos que ficam só no disco local.

USO (da raiz do projeto):  python3 ferramentas/gerar_publicos.py

Por quê: desde 30/09/2026 o repositório é público, e os arquivos com resumos de terceiros (registros com resumo,
ledger de decisões com trechos citados, decisões de deduplicação com os resumos dos pares) ficam fora do Git, no
disco local e no repositório privado com o histórico completo. Este script grava em `publico/` o que deles pode ser
aberto, para a triagem e a deduplicação continuarem auditáveis no repositório público:

- `publico/registros_unicos_sem_resumo.csv`: os registros deduplicados, só com metadados bibliográficos (as mesmas
  colunas do pacote de replicação, `ferramentas/montar_pacote.COLS_REGISTROS`);
- `publico/decisoes_sem_trechos.csv`: cada decisão de triagem e de texto completo do ledger (`dados/decisoes.jsonl`),
  sem `trecho`, `justificativa` e `motivo_override`, que citam ou parafraseiam o resumo;
- `publico/dedup_revisao_v1_sem_resumos.csv`: as 145 decisões de deduplicação dos autores, sem `resumo_a` e `resumo_b`.

E-mails viram "[e-mail removido]". Rode de novo depois de qualquer comando do `rs.py` que mude esses arquivos.
"""
import csv
import importlib.util
import io
import json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("montar_pacote", R / "ferramentas/montar_pacote.py")
mp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mp)
SAIDA = R / "publico"
CAMPOS_FORA_DO_LEDGER = {"trecho", "justificativa", "motivo_override"}


def limpar(v):
    return mp.RX_EMAIL.sub("[e-mail removido]", "" if v is None else str(v))


def gravar(nome, colunas, linhas):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=colunas, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    for l in linhas:
        w.writerow({c: limpar(l.get(c)) for c in colunas})
    (SAIDA / nome).write_text(buf.getvalue(), encoding="utf-8")
    print(f"publico/{nome}: {len(linhas)} linhas")


def main():
    SAIDA.mkdir(exist_ok=True)
    unicos = list(csv.DictReader(open(R / "dados/registros_unicos.csv", encoding="utf-8-sig")))
    gravar("registros_unicos_sem_resumo.csv", mp.COLS_REGISTROS, unicos)

    ledger = [json.loads(l) for l in open(R / "dados/decisoes.jsonl", encoding="utf-8") if l.strip()]
    colunas = [c for c in dict.fromkeys(k for d in ledger for k in d) if c not in CAMPOS_FORA_DO_LEDGER]
    gravar("decisoes_sem_trechos.csv", colunas, ledger)

    dedup = list(csv.DictReader(open(R / "08-revisao-humana/P019_dedup/dedup_revisao_v1.csv", encoding="utf-8-sig")))
    gravar("dedup_revisao_v1_sem_resumos.csv", [c for c in dedup[0] if not c.startswith("resumo_")], dedup)

    trechos = mp.resumos_de_terceiros()
    for p in sorted(SAIDA.glob("*.csv")):
        t = " ".join(p.read_text(encoding="utf-8").split())
        achados = [tr for tr in trechos if tr in t]
        if achados:
            raise SystemExit(f"ERRO: {p.name} tem trecho de resumo de terceiro: {achados[0][:40]!r}")


if __name__ == "__main__":
    main()
