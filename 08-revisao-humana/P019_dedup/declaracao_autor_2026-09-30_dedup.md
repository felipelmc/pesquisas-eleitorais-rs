# Declaração do autor sobre a aplicação da deduplicação (30/09/2026)

Este arquivo transcreve as decisões que o autor (`revisor_humano_1`) tomou em chat com o coordenador de IA (Claude Code, `claude-opus-5-5`) em 30/09/2026, depois da versão de entrega, numa revisão geral do projeto. Completa a declaração de `08-revisao-humana/declaracao_autor_2026-09-30.md`, em que o autor já concordava com as sugestões da IA nos 145 pares candidatos, mas escolhera não aplicá-las. A Emenda 8 registra a aplicação.

## Decisões

1. **Aplicar a deduplicação nesta versão.** Corrigir antes a ferramenta (`revisao-sistematica`), que não levava as decisões de triagem dos registros absorvidos ao registro que os absorveu, e depois aplicar as 145 decisões de `dedup_revisao_v1.csv` (66 fusões, 56 rejeições e 23 ligações).
2. **Regra para decisões divergentes.** Quando um registro absorvido tem decisão de triagem diferente da do registro que o absorve, vale a mais inclusiva: decisão registrada por `triagem override` vence decisão de IA; depois, incluir > incerto > excluir. No empate, fica a do registro que absorve. A alternativa, descartar a decisão do absorvido, daria 521 relatórios buscados em vez de 522; a diferença é um registro (Jiang2024a, que herda o `incerto` de Zhang2025a).
3. **Os 9 pares de versão que a aplicação deixa como candidatos.** Ligar os 9 como versões do mesmo trabalho, como a IA sugeriu (confiança alta). As decisões estão em `dedup_revisao_v2_versoes.csv`, com `decidido_por = revisor_humano_1`.

| Par (id_registro) | O que é |
|---|---|
| B05-00037 ~ B05-00098 | Larcinese, 2010 (SSRN) e 2012 (*British Journal of Political Science*) |
| B05-00067 ~ B05-00734 | Gerber2020a (*AEJ: Applied*) e Gerber2017c (RePEc), relatos incluídos do mesmo estudo |
| B05-00263 ~ B05-00265, B05-00265 ~ B05-00642, B05-00265 ~ B05-00646 | Chernov, três versões no SSRN e o *working paper* do NBER |
| SN1-00237 ~ SN1-00833 | Gentzkow, 2009, SSRN e NBER |
| SN1-00641 ~ SN1-00847 | Hoffman, 2017, NBER e SSRN |
| SN1-00887 ~ SN1-00888 | Bursztyn, 2021, SSRN e NBER |
| SN2-00385 ~ SN2-00386 | Snowberg, 2025, SSRN e NBER |

Esses pares estavam ligados automaticamente antes. Com as ligações humanas da v1, cada estudo passaria a ter dois registros publicados, e a regra automática não liga dois publicados no mesmo estudo; por isso voltaram a candidatos.

## O que o autor não decidiu aqui

A revisão do risco de viés e dos juízos GRADE está em andamento. P033, P035, P036 e P042 continuam abertas até o autor declarar que a concluiu.
