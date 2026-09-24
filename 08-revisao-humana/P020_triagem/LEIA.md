# P020: fila humana da triagem de títulos e resumos (ta_v1)

Esta pasta traz os 81 registros de `02-triagem/fila_humana_ta_v1.csv` que os dois triadores de IA não resolveram sozinhos. Cada um vem com a sugestão de um terceiro leitor.

**A sugestão é de IA** (claude-opus-5-5), feita sem ver os pareceres. O terceiro leitor leu só `id_rs`, `titulo`, `resumo`, `ano` e `veiculo` e aplicou os critérios C1 a C5 de `02-triagem/prompts/ta_v1.md`, na ordem em que aparecem lá. Ele não viu a coluna `pareceres` nem outros arquivos do projeto. A sugestão não substitui a decisão humana: quem decide é o revisor.

## Arquivos

- `terceiro_leitor.json`: uma entrada por registro, com `decisao`, `criterio_falhou`, `justificativa` e `trecho` (citação literal do título ou do resumo).
- `fila_humana_ta_v1.csv`: a fila original com todas as colunas, na ordem original, incluindo `pareceres`. As colunas humanas estão vazias. No fim foram acrescentadas `sugestao_terceiro_leitor`, `criterio_sugerido`, `trecho_sugerido`, `justificativa_sugerida` e `ordem_revisao`. As linhas vêm ordenadas por `ordem_revisao`: 1 são as exclusões sugeridas, 2 os casos incertos e 3 as inclusões.

O arquivo se chama `fila_humana_ta_v1.csv`, e não `..._com_sugestao.csv`, porque o `triagem override` tira a rodada do nome do arquivo (regex `fila_humana_(.+)\.csv`). Com o sufixo, a rodada lida seria `ta_v1_com_sugestao`.

## Contagens da sugestão

| Sugestão | n | Por critério |
|---|---|---|
| excluir | 47 | C2: 33 · C3: 6 · C5: 5 · C4: 3 |
| incerto | 34 | C2: 20 · C4: 9 · C5: 3 · C3: 1 · C1: 1 |
| incluir | 0 | nenhum |
| **Total** | **81** | |

Alguns registros não têm um resumo que sirva para julgar: o campo traz só o orientador, uma nota de tese, a repetição do título, uma lista de periódicos ou um trecho de livro (dedicatória, notas, lista de tabelas ou o parágrafo de abertura de um capítulo). Esses ficaram como `incerto`, pela regra de que registro sem resumo nunca é excluído, mesmo quando o título sugere que um critério falha. Os 13 registros da obra mexicana sobre as eleições de 2018 (RS1381 a RS1443) trazem como resumo a sinopse do livro. Onze deles foram sugeridos para exclusão (C2) só pelo título, e a justificativa de cada um diz isso. Os outros dois (RS1384, o volume, e RS1410, sobre participação) ficaram `incerto`.

## Como preencher

Para cada linha, preencha na planilha:

- `decisao_humana`: `incluir`, `excluir` ou `incerto` (maiúsculas e acentos não importam). Linha deixada em branco é ignorada.
- `criterio_humano`: o critério que falhou (`C1` a `C5`) quando a decisão for `excluir`. Nos outros casos, opcional.
- `motivo_humano`: uma frase curta com o motivo. Pode repetir a justificativa sugerida se você concordar com ela.

Não mude `id_rs` e não apague colunas. Salve como CSV (UTF-8), com o mesmo nome, nesta pasta.

## Como registrar

Na raiz do projeto:

```bash
python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py --dir . triagem override --fila 08-revisao-humana/P020_triagem/fila_humana_ta_v1.csv --por revisor_humano_1
python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py --dir . triagem consolidar --rodada ta_v1 --regra liberal
```

Use `--por revisor_humano_1` só depois de você mesmo ter revisado as linhas preenchidas.
