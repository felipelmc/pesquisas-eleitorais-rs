---
citekey: Klor2017a
ficha_id: Klor2017a#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Klor2017a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Klor2017a-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 47
faixas_lidas: 1-20,21-40,41-47
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "two-sided sign test using the normal approximation to the binomial distribution" (p. 14)
- **resultado_avaliado** — resposta: mobilizacao: Figura 1 (taxa média de comparecimento sem e com informação por distribuição de preferências) e teste de sinais bilateral do texto (sem informação, pouco abaixo de 25%, contra 40% com informação na distribuição 3 contra 4; z = 3,125; p < 0,001) — evidência: "Figure 1: Average Turnout Rate by Distribution of Preferences" (p. 41); "two-sided sign test using the normal approximation to the binomial distribution" (p. 14)
- **desenho_resultado** — resposta: outro — evidência: "Subjects have to decide again whether or not to vote." (p. 13); "Whereas the average turnout rate before the provision of" (p. 14)
- **confundidores_controlados** — resposta: apoio_latente: controlado, a preferência de cada sujeito e portanto a distribuição revelada são sorteadas pelo computador a cada rodada, sem preferência real subjacente ; interesse_politico: controlado, comparação dentro do sujeito (cada sujeito é seu próprio controle entre a etapa sem e a etapa com informação) em laboratório com incentivos monetários fixos ; preferencia_previa/partidarismo: controlado, a cor preferida é sorteada a cada rodada e todos os sujeitos recebem a informação, sem exposição seletiva — evidência: "randomly assigned each subject to one of two teams" (p. 12); "preferred color is again randomly decided" (p. 13); "the unit of observation is the subject" (p. 14)

## B_Triagem
- **b1_tentou_controlar** — resposta: PY — evidência: "the unit of observation is the subject" (p. 14); "randomly assigned each subject to one of two teams" (p. 12)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: B1 = PY)
- **b3_medida_inadequada** — resposta: N — evidência: "She decides whether to vote or abstain." (p. 13); "the computer will collect the seven decisions of the" (p. 38)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: WN — evidência: "Every subject knows that her decision in one stage is independent" (p. 12); "The provision of information for other divisions of the electorates" (p. 14)
- **d1a_q2_medidos_validamente** — resposta: Y — evidência: "computer performs a separate draw for each participant" (p. 38)
- **d1a_q3_controlou_pos_intervencao** — resposta: N — evidência: "two-sided sign test using the normal approximation to the binomial distribution" (p. 14)
- **d1a_q4_controles_negativos** — resposta: N — evidência: "The provision of information for other divisions of the electorates" (p. 14); "when the division is six versus one" (p. 15)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: contraste antes-depois dentro do sujeito, não é DiD, RDD, IV nem pareamento. A ordem é fixa (a decisão com informação vem sempre na segunda etapa da mesma rodada, sem contrabalanceamento), mas não há retorno sobre a primeira etapa antes da segunda e as duas decisões são pagas de forma independente; a tendência entre rodadas (aprendizado) afeta as duas etapas por igual. Como controle negativo implícito, nas distribuições desequilibradas (5x2, 6x1, 7x0) não há mudança significativa entre as etapas (p > 0,8; p > 0,65; p > 0,8), o que sugere ausência de efeito de ordem. A linha de base é a taxa sem informação agregada (pouco abaixo de 25%), não restrita às rodadas 3x4, o que é aceitável porque sem informação o sujeito não conhece a distribuição sorteada. Não há teste formal de efeito de ordem — evidência: "Every subject knows that her decision in one stage is independent" (p. 12); "The provision of information for other divisions of the electorates" (p. 14); "Whereas the average turnout rate before the provision of" (p. 14)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 1.1 a 1.5 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "you will be given no information about the color preferences" (p. 38); "you will receive information about the color" (p. 38)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = NA)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "computer performs a separate draw for each participant" (p. 38); "you will receive information about the color" (p. 38)
- **d2_q5_outros_erros** — resposta: PN — evidência: "The experiment began after all subjects had solved all questions successfully." (p. 12)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: Y — evidência: "Each experimental session entailed 20 independent rounds." (p. 12); "Subjects have to decide again whether or not to vote." (p. 13)
- **d3_q2_eventos_excluidos** — resposta: N — evidência: "we consider, for each subject, the average across all the" (p. 14)
- **d3_q3_selecao_pos_inicio** — resposta: N — evidência: "were recruited from the pool of undergraduate and graduate students" (p. 11); "In each session 21 subjects participated as voters." (p. 11)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = N)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = Y e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: PY — evidência: "computer performs a separate draw for each participant" (p. 38); "All decisions that you make during the experiment will be implemented by" (p. 38)
- **d4_q2_outcome_completo** — resposta: PY — evidência: "In each session 21 subjects participated as voters." (p. 11); "Number of Subjects" (p. 46)
- **d4_q3_confundidores_completos** — resposta: PY — evidência: "computer performs a separate draw for each participant" (p. 38)
- **d4_q4_casos_completos** — resposta: NA — evidência: (fluxo: 4.1, 4.2 e 4.3 = PY)
- **d4_q5_exclusao_relacionada** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q6_explicada_modelo** — resposta: NA — evidência: (fluxo: 4.5 = NA)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 4.1, 4.2 e 4.3 = PY)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: N — evidência: "decide whether to vote for the color that you prefer" (p. 38); "She decides whether to vote or abstain." (p. 13)
- **d5_q2_avaliadores_cientes** — resposta: PN — evidência: "the computer will collect the seven decisions of the" (p. 38)
- **d5_q3_influenciada** — resposta: NA — evidência: (fluxo: 5.2 = PN)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "Whereas the average turnout rate before the provision of" (p. 14)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "The provision of information for other divisions of the electorates" (p. 14)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "when the division is six versus one" (p. 15); "The provision of information for other divisions of the electorates" (p. 14)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Desenho: experimento de laboratório (84 estudantes, 4 sessões de 21, 20 rodadas, eleitorados de 7 sorteados a cada rodada). A informação sobre a distribuição de preferências (a "pesquisa") não é randomizada entre sujeitos: todos votam primeiro sem informação e depois com informação, na mesma rodada. O resultado avaliado (Figura 1, p. 41, e teste de sinais bilateral na p. 14) é, portanto, um contraste antes-depois dentro do sujeito, avaliado por ROBINS-I como indica o protocolo. `desenho_resultado = outro` porque nenhuma categoria do codebook descreve um contraste antes-depois intra-sujeito em laboratório; `variante_d1 = a` porque a análise é uma comparação simples sem tratamento de desvios ou de confundimento variável no tempo.

D1 (proposta_moderado): os três confundidores do protocolo estão controlados por desenho (preferências sorteadas pelo computador, comparação dentro do sujeito, todos expostos). O confundidor não controlado é o tempo/ordem: a etapa com informação vem sempre depois da etapa sem informação, sem contrabalanceamento, e o teste de sinais não ajusta nada. Respondi 1.1 = WN (e não SN) porque as duas decisões são quase simultâneas, sem retorno entre elas, com pagamento independente, e porque nas distribuições desequilibradas a mesma sequência não muda o comparecimento (p. 14-15), o que funciona como controle negativo para efeito de ordem (1.4 = N). Pelo algoritmo, 1.1 = WN com 1.2 = Y, 1.3 = N e 1.4 = N leva a moderado. Observação para os humanos: a linha de base do teste é a taxa sem informação agregada de todas as rodadas (pouco abaixo de 25%), não só das rodadas 3x4; como na etapa 1 o sujeito não conhece a distribuição sorteada, isso não deveria introduzir confundimento, mas o texto não detalha exatamente quais médias entram no teste de sinais.

D2 (proposta_baixo): as condições (fase 1 sem informação, fase 2 com informação) são definidas pelo programa antes da decisão; a checagem de compreensão reduz o risco de o sujeito não perceber a informação.

D3 (proposta_baixo): todos os 84 sujeitos entram; as rodadas 3x4 são definidas por sorteio no início da rodada, antes da exposição; o teste usa a média de cada sujeito sobre todas as rodadas.

D4 (proposta_baixo): decisões registradas por computador; Tabela 2 (p. 46) mostra 84 sujeitos na distribuição 3x4. O texto não declara ausência de perdas, por isso PY e não Y.

D5 (proposta_baixo): o desfecho é a decisão de votar registrada pelo computador, igual nas duas etapas, com custo monetário de 4 fichas. O participante conhece a condição (inevitável em contraste intra-sujeito) e pode haver demanda do experimentador (ser informado e depois perguntado "de novo"), mas a decisão é incentivada e não passa por avaliador; por isso 5.2 = PN. Os humanos podem preferir 5.2 = Y e 5.3 = WY, o que levaria o domínio a moderado.

D6 (proposta_moderado): não há plano de análise prévio ou registro mencionado (6.1 = NI; texto de 2006, pedir aos autores se necessário). Uma única medida de comparecimento; os contrastes para as outras três distribuições são relatados junto (p. 14-15), então 6.2 a 6.4 = PN. Pelo algoritmo, 6.1 = NI com 6.2 a 6.4 = N/PN leva a moderado.

Geral (proposta_moderado): pior domínio moderado (D1 e D6). Não agravei para grave por "vários moderados" porque são apenas dois e o moderado de D6 decorre só da ausência de plano prévio, sem sinal de seleção de resultados; os humanos podem agravar. Direção imprevisível: o efeito de ordem pode tanto inflar quanto reduzir o comparecimento na segunda etapa.

Contato com autores: 6.1 (plano de análise) e composição exata das médias do teste de sinais (linha de base agregada ou só rodadas 3x4). Resultado indicado pelo coordenador encontrado (Figura 1 na p. 41; teste de sinais na p. 14).
