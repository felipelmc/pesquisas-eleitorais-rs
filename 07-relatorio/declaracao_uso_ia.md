# Declaração de uso de inteligência artificial

**RASCUNHO NÃO VALIDADO** (7 pendências abertas; decisões de IA na triagem sem validação calculada com finalidade validação da rodada ativa; juízos de IA sem validação humana (seção 7)).

Projeto: Exposição a pesquisas eleitorais publicadas → intenção de voto (bandwagon/underdog). Tipo de revisão: efetividade_swim. Modo de autonomia: autopiloto; triagem: subagentes.

Gerado a partir de `rs_log.jsonl` até o evento seq 873 (sha256 dos eventos `3f8d501c50856764…`) e de `dados/decisoes.jsonl` (6511 decisões). Nenhum número foi digitado à mão.

## 1. Ferramentas e modelos

| Modelo | Tipo de ator | Etapas | Primeiro uso | Último uso | Eventos | Decisões | Parâmetros |
|---|---|---|---|---|---|---|---|
| (modelo não registrado: ia_coordenador) | ia_coordenador | 04_busca, 06_triagem_ta, 07_textos_elegibilidade, 08_piloto_extracao, 09_extracao_rob, 10_sintese, 11_relato | 2026-09-19 | 2026-09-23 | 7 | 0 | não registrados |
| claude-opus-5 | ia_subagente, script | 06_triagem_ta, decisões ta | 2026-09-19 | 2026-09-20 | 117 | 2785 | não registrados |
| claude-sonnet-5 | ia_subagente, script | 06_triagem_ta, decisões ta | 2026-09-19 | 2026-09-20 | 117 | 2785 | não registrados |

## 2. Papéis por etapa

| Etapa | Tipo de ator | Papel | Eventos | N |
|---|---|---|---|---|
| 00_configuracao | script | ambiente | ambiente_verificado | 1 |
| 00_configuracao | script | init | projeto_criado | 1 |
| 01_pergunta | humano | revisor_humano_1 | portao | 1 |
| 03_protocolo | humano | revisor_humano_1 | emenda_protocolo, portao | 3 |
| 03_protocolo | script | rs.py buscar openalex | artefato_versionado | 4 |
| 04_busca | humano | revisor_humano_1 | pendencia_fechada | 2 |
| 04_busca | ia_coordenador | autopiloto | portao | 1 |
| 04_busca | script | autopiloto | pendencia_aberta | 1 |
| 04_busca | script | rs.py buscar openalex | busca_registrada | 4 |
| 04_busca | script | rs.py importar | busca_registrada, busca_substituida | 2 |
| 04_busca | script | script | pendencia_aberta | 1 |
| 05_organizacao | humano | revisor_humano_1 | dedup_revisado | 2 |
| 05_organizacao | script | dedup | dedup_executado, pendencia_aberta, pendencia_fechada | 17 |
| 05_organizacao | script | filtrar | filtro_formal | 7 |
| 05_organizacao | script | rs.py importar | importacao | 8 |
| 06_triagem_ta | humano | ia_coordenador_emenda6 | decisao_override | 1 |
| 06_triagem_ta | humano | revisor_humano_1 | decisao_override | 337 |
| 06_triagem_ta | ia_coordenador | autopiloto | portao | 1 |
| 06_triagem_ta | ia_subagente | revisor_A | lote_mesclado | 114 |
| 06_triagem_ta | ia_subagente | revisor_B | lote_mesclado | 114 |
| 06_triagem_ta | script | autopiloto | pendencia_aberta | 1 |
| 06_triagem_ta | script | triagem_lotes | lote_preparado, lote_rejeitado, pendencia_aberta, pendencia_fechada, triagem_consolidada | 34 |
| 06_triagem_ta | script | validacao | artefato_versionado, lote_preparado, pendencia_aberta, validacao_calculada | 7 |
| 07_textos_elegibilidade | humano | revisor_humano_1 | decisao_override, pendencia_fechada | 25 |
| 07_textos_elegibilidade | ia_coordenador | autopiloto | portao | 1 |
| 07_textos_elegibilidade | script | autopiloto | pendencia_aberta | 1 |
| 07_textos_elegibilidade | script | rs.py bola-de-neve | busca_registrada | 3 |
| 07_textos_elegibilidade | script | rs.py textos | ligacao_relatos, pendencia_aberta, pendencia_fechada, retratacoes_verificadas, textos_atualizados | 59 |
| 07_textos_elegibilidade | script | triagem_lotes | fila_gerada | 3 |
| 08_piloto_extracao | humano | revisor_humano_1 | pendencia_fechada | 2 |
| 08_piloto_extracao | ia_coordenador | autopiloto | portao | 1 |
| 08_piloto_extracao | script | autopiloto | pendencia_aberta | 1 |
| 08_piloto_extracao | script | script | pendencia_aberta | 1 |
| 09_extracao_rob | humano | revisor_humano_1 | pendencia_fechada | 2 |
| 09_extracao_rob | ia_coordenador | autopiloto | portao | 1 |
| 09_extracao_rob | script | autopiloto | pendencia_aberta | 1 |
| 09_extracao_rob | script | rs.py analise | efeitos_verificados, extracao_consolidada, pendencia_aberta, pendencia_fechada | 25 |
| 09_extracao_rob | script | rs.py qualidade | fila_gerada, pendencia_aberta, pendencia_fechada, rob_consolidado | 12 |
| 09_extracao_rob | script | script | pendencia_aberta | 1 |
| 10_sintese | humano | revisor_humano_1 | pendencia_fechada | 1 |
| 10_sintese | ia_coordenador | autopiloto | portao | 1 |
| 10_sintese | script | autopiloto | pendencia_aberta | 1 |
| 10_sintese | script | rs.py analise | analise_executada | 39 |
| 10_sintese | script | rs.py caixa | caixa_gerada, pendencia_aberta | 3 |
| 10_sintese | script | script | pendencia_aberta | 2 |
| 11_relato | humano | revisor_humano_1 | pendencia_fechada | 1 |
| 11_relato | ia_coordenador | autopiloto | portao | 1 |
| 11_relato | script | autopiloto | pendencia_aberta | 1 |
| 11_relato | script | prisma | erro, prisma_gerado | 8 |
| 11_relato | script | rs.py handoff | relatorio_gerado | 6 |

## 3. Prompts, critérios e instrumentos arquivados

| Arquivo ou referência | sha256 (prefixo) | Primeiro evento (seq) |
|---|---|---|
| 00-protocolo/ancoras_validacao.csv | `731f41e2233ff11c` | 20 |
| 00-protocolo/codebook_elegibilidade.csv | `65dddc46db76bb2c` | 319 |
| 00-protocolo/codebook_v0_efetividade.csv | `47a0cc5ad53896ed` | 718 |
| 00-protocolo/exploracao_EX1.csv | `0bab9d73a0d37d69` | 3 |
| 00-protocolo/exploracao_EX2.csv | `a480ba19830ca555` | 4 |
| 00-protocolo/exploracao_EX3.csv | `6f41b6d852c081e9` | 6 |
| 00-protocolo/exploracao_EX4.csv | `b16d20b937705df6` | 7 |
| 00-protocolo/protocolo.md | `88530b9042361ced` | 552 |
| 02-triagem/prompts/ta_v1.md | `cd9cbfe00d4e4e45` | 31 |
| 04-qualidade/rob_epoc_concordancia.csv | `85bbe6fa8f1a84dc` | 739 |
| 04-qualidade/rob_epoc_consenso.csv | `d84678f651e80fe0` | 749 |
| 04-qualidade/rob_epoc_consenso.csv | `e05d2a59fdd941b9` | 739 |
| 04-qualidade/rob_geral.csv | `27378b9abc936385` | 745 |
| 04-qualidade/rob_geral.csv | `88ff4d90d0b525db` | 749 |
| 04-qualidade/rob_geral.csv | `e3832bc9649de3b2` | 747 |
| 04-qualidade/rob_rob2_concordancia.csv | `313ae6c801888d70` | 745 |
| 04-qualidade/rob_rob2_concordancia.csv | `ea5cfabab960fefb` | 737 |
| 04-qualidade/rob_rob2_consenso.csv | `873b9106e5659c9b` | 745 |
| 04-qualidade/rob_rob2_consenso.csv | `929b0734603102cc` | 737 |
| 04-qualidade/rob_robins_i_concordancia.csv | `36d4b13bfcb47291` | 735 |
| 04-qualidade/rob_robins_i_concordancia.csv | `4714c56d7c816f6c` | 747 |
| 04-qualidade/rob_robins_i_consenso.csv | `3db4722042e1f5e4` | 735 |
| 04-qualidade/rob_robins_i_consenso.csv | `529303335860418b` | 747 |
| 05-decomposicao/efeitos_extraidos.csv | `2af2c34a6953dbab` | 741 |
| 05-decomposicao/efeitos_extraidos.csv | `2e04ab6865a70580` | 848 |
| 05-decomposicao/efeitos_extraidos.csv | `360ac9417c1aad38` | 751 |
| 05-decomposicao/efeitos_extraidos.csv | `49459d80e51c24d6` | 801 |
| 05-decomposicao/efeitos_extraidos.csv | `52c4fc0c7e1868e4` | 727 |
| 05-decomposicao/efeitos_extraidos.csv | `8441cefc501c842d` | 797 |
| 05-decomposicao/efeitos_extraidos.csv | `8634976d7f7dc686` | 719 |
| 05-decomposicao/efeitos_extraidos.csv | `d1ad5e8ae22c8204` | 768 |
| 05-decomposicao/efeitos_para_sintese.csv | `4fbbdc293dc82ebc` | 755 |
| 05-decomposicao/efeitos_para_sintese.csv | `59a5beae4e717565` | 770 |
| 05-decomposicao/efeitos_para_sintese.csv | `6a380ae3b2c18085` | 803 |
| 05-decomposicao/efeitos_para_sintese.csv | `d9366aa7b5ef7f20` | 850 |
| 05-decomposicao/efeitos_preparacao_avisos.csv | `24bfdbf2823d7d16` | 741 |
| 05-decomposicao/efeitos_preparacao_avisos.csv | `4c8e64bb54a17994` | 719 |
| 05-decomposicao/efeitos_preparacao_avisos.csv | `5650391bd3872236` | 797 |
| 05-decomposicao/efeitos_preparacao_avisos.csv | `b9effdf49516a3a3` | 727 |
| 05-decomposicao/piloto_fichamentos_master.csv | `fcd13c961915f578` | 722 |
| 05-decomposicao/verificacao_efeitos.csv | `4de484f2729e68e4` | 798 |
| 05-decomposicao/verificacao_efeitos.csv | `74e55594bbae85d8` | 728 |
| 05-decomposicao/verificacao_efeitos.csv | `8f4850551295b114` | 752 |
| 05-decomposicao/verificacao_efeitos.csv | `8ff77b0faf6c16cc` | 849 |
| 05-decomposicao/verificacao_efeitos.csv | `d8d3297ac36510a0` | 802 |
| 05-decomposicao/verificacao_efeitos.csv | `e0a8519f89ceb95d` | 742 |
| 05-decomposicao/verificacao_efeitos.csv | `e9765beb6c8f9b8a` | 720 |
| criterios_sha (evento lote_preparado) | `cd9cbfe00d4e4e45` | 31 |
| prompt da rodada ta_v1 (A) | `cd9cbfe00d4e4e45` | decisoes.jsonl |
| prompt da rodada ta_v1 (B) | `cd9cbfe00d4e4e45` | decisoes.jsonl |
| prompt da rodada ta_v1_estab (A) | `cd9cbfe00d4e4e45` | decisoes.jsonl |
| prompt da rodada ta_v1_estab (B) | `cd9cbfe00d4e4e45` | decisoes.jsonl |
| prompt_sha (evento lote_mesclado) | `cd9cbfe00d4e4e45` | 36 |

Versões ativas no estado: criterios_ta = 02-triagem/prompts/ta_v1.md; filtros = filtros_v2; protocolo = v1; rodada_ta = ta_v1.

## 4. Validação do uso de IA

Limiares de referência (references/ia-validacao.md da skill):

- Triagem T/A: recall >= 0,95 com limite inferior do IC >= 0,90; amostra com >= 60 incluídos humanos
- Calibração humana: kappa >= 0,6 e concordância >= 75%
- Extração categórica: kappa ou PABAK >= 0,7 e concordância >= 80% por variável
- Dados numéricos de efeito: 100% verificados na página do PDF

_Nenhuma validação com finalidade validação da rodada ativa (ta_v1)._

### Elusão e estabilidade

| Seq | Data | Finalidade | Rodada | Amostra ou reexecução | Taxa de elusão | Perdidos estimados | N |
|---|---|---|---|---|---|---|---|
| 184 | 2026-09-19 | estabilidade | ta_v1 | ta_v1_estab |  |  | 158 |

Amostras de elusão registradas: 0.

## 5. Portões e responsabilidade humana

| Portão | Etapa | Tipo de ator | Aprovado por | Data | Motivo |
|---|---|---|---|---|---|
| G1 | 01_pergunta | humano | revisor_humano_1 | 2026-09-19 |  |
| G2 | 03_protocolo | humano | revisor_humano_1 | 2026-09-19 |  |
| G3 | 04_busca | ia_coordenador | autopiloto | 2026-09-19 |  |
| G4 | 06_triagem_ta | ia_coordenador | autopiloto | 2026-09-19 |  |
| G5 | 07_textos_elegibilidade | ia_coordenador | autopiloto | 2026-09-20 |  |
| G6 | 08_piloto_extracao | ia_coordenador | autopiloto | 2026-09-20 |  |
| G7 | 09_extracao_rob | ia_coordenador | autopiloto | 2026-09-23 |  |
| G8 | 10_sintese | ia_coordenador | autopiloto | 2026-09-23 |  |
| G9 | 11_relato | ia_coordenador | autopiloto | 2026-09-23 |  |

Custo de API registrado: não registrado.

Nenhum evento do log traz custo ou uso de tokens de API. A triagem por subagentes do Claude Code não registra custo por chamada.

## 6. Pendências abertas

As descrições estão como foram registradas na abertura de cada pendência (data e seq do evento `pendencia_aberta` na coluna "Aberta em"): contagens e pendências citadas podem ter mudado desde então. Pendências citadas que já foram fechadas levam, entre colchetes, o fechamento e as sucessoras; a seção 7 traz o estado atual.

| Id | Tipo | Etapa | Portão | Aberta em | Descrição (como registrada na abertura) | N |
|---|---|---|---|---|---|---|
| P006 | validacao_humana | 06_triagem_ta | G4 | 2026-09-19 (seq 165) | codificar em dupla, às cegas, a amostra amostra01 (141 registros) | 141 |
| P007 | validacao_humana | 06_triagem_ta | G4 | 2026-09-19 (seq 167) | codificar em dupla, às cegas, a amostra elusao01 (300 registros) | 300 |
| P008 | revisao_humana_portao | 06_triagem_ta | G4 | 2026-09-19 (seq 186) | confirmar a aprovação automática do G4: nenhuma validação humana (finalidade validacao) calculada para a rodada ativa ta_v1 (rs.py validar calcular); P005 aberta: resolver 47 divergências da triagem (ta_v1) com `triagem override --fila 02-triagem/fila_humana_ta_v1.csv`; P006 aberta: codificar em dupla, às cegas, a amostra amostra01 (141 registros); P007 aberta: codificar em dupla, às cegas, a amostra elusao01 (300 registros) [P005: fechada em 2026-09-19 (seq 402); substituída por P012 → P016 → P020, fechada em 2026-09-30] |  |
| P033 | revisao_humana_portao | 09_extracao_rob | G7 | 2026-09-23 (seq 754) | confirmar a aprovação automática do G7: 554 efeitos sem verificação humana na página do PDF (apto_g7 = 0; ex.: Agranov2017a-E01, Agranov2017a-E02, Agranov2017a-E03, Agranov2017a-E04, Agranov2017a-E05); RoB de rob2 (seq 745) com 23 de 23 resultados sem validação humana (todos_validados_humano diferente de true): a concordância entre avaliadores não humanos não valida; resolva por humano no consenso e consolide de novo; RoB de robins_i (seq 747) com 13 de 13 resultados sem validação humana (todos_validados_humano diferente de true): a concordância entre avaliadores não humanos não valida; resolva por humano no consenso e consolide de novo; RoB de epoc (seq 749) com 7 de 7 resultados sem validação humana (todos_validados_humano diferente de true): a concordância entre avaliadores não humanos não valida; resolva por humano no consenso e consolide de novo; P032 aberta: conferir 100% dos dados de efeito na página do PDF e marcar verificado_humano [substitui P027] [P032: fechada em 2026-09-24 (seq 799); substituída por P039, fechada em 2026-09-30] [P027: fechada em 2026-09-23 (seq 743); substituída por P032 → P039, fechada em 2026-09-30] |  |
| P035 | revisao_humana_portao | 10_sintese | G8 | 2026-09-23 (seq 780) | confirmar a aprovação automática do G8: P034 aberta: GRADE das 7 células em 06-analise/certeza.csv rascunhado por subagente (claude-opus-5-5), validado_humano vazio; revisor humano deve confirmar ou alterar cada juízo (ver ponto sobre viés de publicação na célula 1) [P034: fechada em 2026-09-23 (seq 782); substituída por P036, aberta] |  |
| P036 | certeza_humana | 10_sintese |  | 2026-09-23 (seq 781) | GRADE refeito após a Emenda 5: 21 linhas em 06-analise/certeza.csv (17 células do protocolo + 4 do agrupamento amplo descritivo), rascunhadas por subagente (claude-opus-5-5) com validado_humano vazio; decidir em especial o rebaixamento por viés de publicação no agrupamento amplo de apoio randomizado (baixa × moderada) |  |
| P042 | certeza_caixa | 10_sintese | G8 | 2026-09-24 (seq 831) | completar certeza (GRADE/CERQual) e enunciados das células pendentes | 22 |

## 7. Declaração de responsabilidade

As ferramentas de IA listadas foram usadas como apoio sob supervisão humana. A decisão de usar IA e a forma de uso, os critérios, o protocolo e as conclusões são responsabilidade dos revisores humanos, que conferiram as saídas conforme os portões e as validações acima, exceto nos juízos listados abaixo: eles foram feitos por IA sem validação humana registrada, são rascunhos de IA e devem ser relatados como tais.

- Risco de viés (rob2): 23 de 23 resultados sem validação humana na consolidação (`rob_consolidado`, seq 745, 2026-09-23); a concordância entre avaliadores de IA não valida.
- Risco de viés (robins_i): 13 de 13 resultados sem validação humana na consolidação (`rob_consolidado`, seq 747, 2026-09-23); a concordância entre avaliadores de IA não valida.
- Risco de viés (epoc): 7 de 7 resultados sem validação humana na consolidação (`rob_consolidado`, seq 749, 2026-09-23); a concordância entre avaliadores de IA não valida.
- Certeza da evidência (GRADE/CERQual) em `06-analise/certeza.csv` (sha256 `c075097a6f119c05…`): 18 de 18 linhas sem `validado_humano`.
- Certeza da evidência (GRADE/CERQual) em `06-analise/certeza_agrupamento_amplo.csv` (sha256 `29878705b08a6fd1…`): 7 de 7 linhas sem `validado_humano`.
- Rótulos da caixa de ferramentas: 22 de 22 linhas pendentes ou em rascunho (`caixa_gerada`, seq 873, 2026-09-30).
- Portão G4 (06_triagem_ta), aprovado por autopiloto (ia_coordenador) em 2026-09-19 (seq 185): confirmação humana pendente (P008).
- Portão G7 (09_extracao_rob), aprovado por autopiloto (ia_coordenador) em 2026-09-23 (seq 753): confirmação humana pendente (P033).
- Portão G8 (10_sintese), aprovado por autopiloto (ia_coordenador) em 2026-09-23 (seq 779): confirmação humana pendente (P035).
- Triagem de títulos e resumos: decisões de IA sem validação calculada com finalidade validação da rodada ativa (seção 4).
- Pendências abertas em triagem de títulos e resumos (06_triagem_ta): P006 (validacao_humana), P007 (validacao_humana); descrição na seção 6.
- Pendências abertas em síntese e certeza (10_sintese): P036 (certeza_humana), P042 (certeza_caixa); descrição na seção 6.

Portões aprovados sem humano e confirmados depois por humano: G3 (P004, fechada em 2026-09-30, seq 855); G5 (P023, fechada em 2026-09-30, seq 844); G6 (P026, fechada em 2026-09-30, seq 846); G9 (P038, fechada em 2026-09-30, seq 859).

Validação humana completa registrada: dados de efeito, 560 de 560 efeitos verificados por humano na página do PDF e aptos para o G7 (`efeitos_verificados`, seq 872, 2026-09-30).

Decisões de IA não validadas estão sinalizadas como pendências.
