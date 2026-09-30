# P036 e P042: validação humana do GRADE

## Os juízos rascunhados

Os juízos foram rascunhados em 24/09/2026 por um subagente de IA (`claude-opus-5-5`), com `06-analise/prompt_grade_v2.md`:

- `06-analise/certeza.csv` tem 18 células da SWiM principal. São 15 muito baixa, 2 baixa (Westwood2020a; Stolwijk2019b e Brugarolas2021) e 1 moderada (Gerber2020a, efeito nulo dentro de ±δ).
- `06-analise/certeza_agrupamento_amplo.csv` tem 7 linhas do agrupamento amplo, que é descritivo e foi decidido depois de ver os dados. Todas ficaram em muito baixa.

Em todas as linhas, `validado_humano = 0`. A certeza qualifica a **direção** do efeito, não a magnitude.

## A P042

A P042 foi aberta em 24/09/2026 quando o coordenador de IA rodou `rs caixa`. É a caixa de ferramentas, obrigatória só em avaliação de política (OQF) e aqui opcional. Ela pede o mesmo que a P036: juízos de certeza validados por humano nas 22 linhas de `06-analise/caixa_ferramentas.csv`. Feche as duas juntas.

## A planilha

O arquivo é `grade_decisao_humana.csv`, com uma linha por célula. Traz a certeza, o enunciado e a justificativa da IA, e colunas vazias para a sua decisão.

## Decisões que o rascunho deixou explícitas para você

1. **RoB 2 com preocupação só no domínio 5** (resultado relatado sem plano prévio): Westwood2020a, Meer2015a, Boukouras2020a e Gerber2020a. Esses casos não foram rebaixados. Se forem rebaixados, Westwood2020a cai de baixa para muito baixa e Gerber2020a de moderada para baixa.
2. **Célula Stolwijk2019b + Brugarolas2021:** o rebaixamento por risco de viés foi de 1 nível, embora Stolwijk2019b seja grave. Com 2 níveis, a célula fica em muito baixa.
3. **Viés de publicação:** houve rebaixamento onde há estudos pequenos, todos na mesma direção e sem nenhum nulo. No agrupamento amplo randomizado de apoio (9 de 9 *bandwagon*), é esse rebaixamento que leva a muito baixa; sem ele, a certeza seria baixa. É a mesma questão da versão anterior da P036.
4. **Composição das células:** depende dos pontos em `08-revisao-humana/efeitos/pontos_para_o_revisor.md` (dicionário `FORA`, alvo de Witsman2016a-E01, comparador de Grillo2024c, ano em experimentos de laboratório). Se mudar algum, refaça a SWiM e o GRADE da célula.
5. **RoB sem validação:** nenhum julgamento de RoB foi validado por humano (P033). Os números dos efeitos foram conferidos pelo autor em bloco em 30/09/2026 (P039, Emenda 7). O GRADE herda o RoB não validado.

## Como registrar

1. Para cada linha, preencha `certeza_humana` e, se quiser, `enunciado_humano` e `motivo_humano` na planilha.
2. Leve a decisão para `06-analise/certeza.csv`: ajuste `certeza`, `enunciado` e `justificativa` onde discordar, e ponha `validado_humano = 1` nas linhas conferidas. Faça o mesmo em `certeza_agrupamento_amplo.csv`.
3. Rode `rs --dir . caixa`.
4. Feche as pendências:
   ```bash
   rs --dir . pendencia fechar P036 --motivo "GRADE validado: <resumo>" --por revisor_humano_1
   rs --dir . pendencia fechar P042 --motivo "mesma validação da P036" --por revisor_humano_1
   rs --dir . pendencia fechar P035 --motivo "G8 confirmado" --por revisor_humano_1
   ```
5. Se alguma certeza mudar, rode `bash ferramentas/refazer_produtos.sh`: a sentinela da `09-documento-final/spec_final.md` (seção 10) diz quais seções do artigo reescrever, com os prompts de `09-documento-final/prompts_final/`.
