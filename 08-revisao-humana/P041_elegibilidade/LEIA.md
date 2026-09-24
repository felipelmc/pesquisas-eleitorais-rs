# P041: conferência humana da elegibilidade no texto completo (antes P028 e P040)

A fila é `03-textos/fila_humana_tc.csv`, com 165 textos: 47 propostos para inclusão e 118 para exclusão. As propostas são de fichadores de IA (Opus, um PDF por agente). Cada linha traz o critério proposto, um trecho literal e a página. Esses trechos passaram pelo gate de citações.

Na fila, os textos já decididos por você não aparecem. São as 17 decisões limítrofes que você tomou na conversa em 19 e 20/09 (Emenda 6a).

## Ordem sugerida

1. **As 47 inclusões.** Elas definem os estudos da síntese. Confira os critérios c1 a c4 na ficha: `03-textos/fichas_elegibilidade/fichamento_<chave>.md`.
2. **As 3 decisões em que a IA estendeu uma regra sua a casos novos** (Emenda 6a, eventos seq 669 a 671): RS4220, RS4487 e RS4361, todas exclusões por C2. Elas entraram no ledger como humanas. Confirme ou reverta com `triagem override --etapa tc`.
3. **As 118 exclusões.** Os motivos mais comuns são c2 (exposição que não é pesquisa eleitoral publicada) e c1.
4. **Os 15 textos novos da Emenda 6b**, todos propostos para exclusão: Buckley2022, Matos2013, Strijbis2017a, Schonbrodt2013, Selb2012, Santos2021, Cancela2016, Marinovic2013, Pekar2021, Heeb2023, Prosser2015a, Magalhaes2012a, Wall2017, Poland2021a e HashemPesaran2024a.

## Como registrar

Preencha `decisao_humana` (`incluir`, `excluir` ou `aguardando`), `criterio_humano` nas exclusões e `motivo`. Depois:

```bash
rs() { python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py "$@"; }
rs --dir . triagem override --fila 03-textos/fila_humana_tc.csv --etapa tc --por revisor_humano_1
rs --dir . textos elegibilidade consolidar --master 03-textos/fichamentos_master.csv --codebook 00-protocolo/codebook_elegibilidade.csv
```

A pendência fecha sozinha quando `n_pendentes_conferencia` chega a 0. Depois feche o portão: `rs --dir . pendencia fechar P023 --motivo "..." --por revisor_humano_1`.

Se uma decisão mudar o conjunto de incluídos, refaça a extração do estudo afetado e a cadeia do README.
