"""Junta o risco de viés geral (04-qualidade/rob_geral.csv) aos efeitos extraídos.

USO (depois de `rs analise preparar-efeitos` e `rs analise verificar-efeitos`)
    python3 05-decomposicao/juntar_rob.py
    rs --dir . analise efeitos --in 05-decomposicao/efeitos_para_sintese.csv

A skill não tem comando para esta junção (references/06-decomposicao.md, seção 8). A chave é
chave + construto_outcome, nunca o título; a contagem de linhas não pode mudar.
"""
import pandas as pd

ler = lambda p: pd.read_csv(p, dtype=str, keep_default_na=False)
ef = ler("05-decomposicao/efeitos_extraidos.csv").drop(columns=["rob_geral"], errors="ignore")
rob = ler("04-qualidade/rob_geral.csv")[["chave", "construto_outcome", "rob_geral"]]
out = ef.merge(rob, on=["chave", "construto_outcome"], how="left")
assert len(out) == len(ef)
out.to_csv("05-decomposicao/efeitos_para_sintese.csv", index=False)
print("ok junção", len(out))
