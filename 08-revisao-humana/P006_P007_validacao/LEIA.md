# P006 e P007: validação humana cega da triagem de títulos e resumos

As planilhas são **cegas**: não trazem nenhuma decisão de IA, e nada de IA foi acrescentado nelas. A validação só vale se for feita por humanos que não viram os pareceres da IA.

## P006: amostra de validação (141 registros, dois codificadores)

1. Cada codificador trabalha na própria cópia, sem ver a do outro:
   - codificador 1: `amostra01_h1.xlsx`, colunas `decisao_h1` e `criterio_h1`;
   - codificador 2: `amostra01_h2.xlsx`, colunas `decisao_h2` e `criterio_h2`.

   Os valores possíveis são `incluir`, `excluir` e `incerto`. Toda exclusão leva o critério C1 a C5 de `02-triagem/prompts/ta_v1.md`.
2. Junte as duas cópias na planilha oficial:
   `python3 08-revisao-humana/P006_P007_validacao/juntar_h1_h2.py`
3. Na planilha oficial (`02-triagem/validacao/ta_v1/amostra01_cega.xlsx`), preencha `decisao_consenso` nas discordâncias.
4. Calcule: `rs --dir . validar calcular --planilha 02-triagem/validacao/ta_v1/amostra01_cega.xlsx`. O comando fecha a P006 se os limiares forem atingidos: recall ≥ 0,95, com limite inferior ≥ 0,90.

## P007: amostra de elusão (300 registros que a IA excluiu, um codificador)

1. Codifique `decisao_h1` e `criterio_h1` direto em `02-triagem/validacao/ta_v1/elusao01_cega.xlsx`.
2. Calcule: `rs --dir . validar calcular --planilha 02-triagem/validacao/ta_v1/elusao01_cega.xlsx`.

Observação: a amostra de elusão foi sorteada antes da Emenda 6b. Alguns dos registros sem resumo dela voltaram depois ao texto completo. Codifique mesmo assim, porque a amostra mede a triagem de IA original.

Depois das duas: `rs --dir . pendencia fechar P008 --motivo "..." --por revisor_humano_1`, junto com a P020.
