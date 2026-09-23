---
citekey: Lago2015
ficha_id: Lago2015#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Lago2015.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Lago2015-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 40
faixas_lidas: 1-20,21-40
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "parliamentary election held in every country" (p. 12)
- **resultado_avaliado** — resposta: Tabela 2, Modelo 3 (MQO, EP robustos, n = 46 países): interação ENEP × nº de dias de embargo de pesquisas = .002** (.001), sobre a proporção de votos desperdiçados; lido com sinal trocado como exposição a pesquisas — evidência: "ENEP*#Days of Poll" (p. 34); "the interaction between ENEP and the Number of Days of" (p. 15)
- **desenho_resultado** — resposta: outro — evidência: "Estimation is by OLS with robust standard errors" (p. 14)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — a distribuição de preferências só entra via ENEP, calculado a partir dos votos da mesma eleição (variável pós-exposição), sem medida prévia ; interesse_politico: nao_controlado — análise agregada por país sem nenhuma medida de interesse ou atenção política ; preferencia_previa / partidarismo: nao_controlado — nenhuma medida de partidarismo ou de estrutura de clivagens no nível do país; os únicos controles são cláusula de barreira, % de assentos no nível superior e (inverso da) idade da democracia — evidência: "We control for three standard variables affecting the amount of wasted votes:" (p. 13)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "We control for three standard variables affecting the amount of wasted votes:" (p. 13)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: B1 = Y)
- **b3_medida_inadequada** — resposta: PN — evidência: "did not obtain parliamentary representation) at the national level" (p. 12)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "Finally, the ban on pre-election polls is more" (p. 25); "more widespread in PR (or multiparty systems) than in single-member" (p. 5)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q4_controles_negativos** — resposta: N — evidência: "no evidence of an interaction between the Age of Democracy and poll" (p. 15)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Não é quase-experimento: regressão transversal com uma eleição por país (46 países), seleção em observáveis com três controles; nenhuma estratégia de identificação nem teste de pressuposto; só diagnóstico de outliers/observações influentes e regressão robusta; os autores reconhecem que mudanças de embargo dentro dos países seriam o experimento natural adequado — evidência: "Diagnostic tests indicate that there are no outliers or influential observations" (p. 14); "within countries are natural experiments that should be examined in detail" (p. 25)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_nao — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "Number of Days of Poll Embargo prior the Election Day" (p. 13)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = NA)
- **d2_q4_classificacao_influenciada** — resposta: PN — evidência: "The source is Chung (2012)." (p. 13)
- **d2_q5_outros_erros** — resposta: PN — evidência: "The value 0 means that there is no" (p. 13)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: PY — evidência: "in the last Lower-House election held in a sample of 46 democracies" (p. 11)
- **d3_q2_eventos_excluidos** — resposta: N — evidência: "The dependent variable is the percentage of wasted votes" (p. 12)
- **d3_q3_selecao_pos_inicio** — resposta: PN — evidência: "There have been two criteria for selecting countries and elections." (p. 11); "An election is deemed to be democratic when and where" (p. 12)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = PN)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = PY e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: Y — evidência: "dependent on the availability of information about the number of days" (p. 11)
- **d4_q2_outcome_completo** — resposta: Y — evidência: "Table A1. Elections Included in the Analysis" (p. 39)
- **d4_q3_confundidores_completos** — resposta: Y — evidência: "(Inverse) Age of Democracy" (p. 33)
- **d4_q4_casos_completos** — resposta: NA — evidência: (fluxo: 4.1, 4.2 e 4.3 = Y)
- **d4_q5_exclusao_relacionada** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q6_explicada_modelo** — resposta: NA — evidência: (fluxo: 4.5 = NA)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 4.1, 4.2 e 4.3 = Y)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: PN — evidência: "We have several sources for the electoral results: the European Election" (p. 12)
- **d5_q2_avaliadores_cientes** — resposta: PN — evidência: "and the respective Electoral Commissions." (p. 13)
- **d5_q3_influenciada** — resposta: NA — evidência: (fluxo: 5.2 = PN)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "Wasted votes are a standard variable used" (p. 12)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "we have run three specifications: a first model with only variables" (p. 14); "When running robust regressions the results do not change appreciably." (p. 14)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "determinants of wasted votes in our sample of 46 countries" (p. 14)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Resultado localizado: Tabela 2, Modelo 3 (p. 34), termo ENEP*#Days of Poll Embargo = .002** (.001); o efeito principal do embargo no mesmo modelo é -.008** (.002). O desfecho é a proporção de votos em partidos sem representação (coordenação eleitoral), não o voto no líder: é um substituto indireto de apoio_ao_lider. Isso é questão de indireção (GRADE), não de medida inválida, por isso B3 = PN.

Desenho: regressão MQO transversal entre 46 países, uma eleição por país (2009-2013), com a exposição (lei de embargo, dias) comparada entre países. Não há variação dentro das unidades nem estratégia de identificação. Classifiquei como `outro` e variante `a` (só confundimento de linha de base).

D1 (proposta_grave). B1 = Y: há ajuste por três controles. 1.1 = SN: os três confundidores do protocolo não são controlados. Além deles, o texto mostra que o embargo se concentra em democracias jovens (p. 25) e em sistemas de RP ou multipartidários (p. 5), ou seja, a exposição acompanha características institucionais e históricas de cada país que também afetam o voto desperdiçado. Idade da democracia e dois traços do sistema eleitoral são controlados, mas n = 46 com uma observação por país deixa muito confundimento residual plausível (cultura política, institucionalização partidária, entrada estratégica de partidos, ambiente de mídia). Escolhi SN e não WN porque o confundimento não controlado provavelmente é substancial. Ponto adicional para os humanos: o ENEP, que modera o efeito e entra como controle, é calculado a partir dos votos da mesma eleição. Portanto é pós-exposição e ligado mecanicamente ao voto desperdiçado: se o embargo piora a coordenação, o ENEP sobe. A pergunta 1.3 caiu por fluxo (1.1 = SN), mas esse problema afeta diretamente o termo de interação avaliado. 1.4 = N porque não há controles negativos nem análise de viés; o único teste relatado é a ausência de interação entre idade da democracia e embargo (nota 11). Se os avaliadores entenderem o ENEP pós-exposição como uma "outra consideração" que indica confundimento grave (1.4 = PY), o domínio e o geral passam a proposta_critico. É a principal dúvida desta ficha.

D2 (proposta_baixo). A lei de embargo é anterior ao desfecho e vem de fonte externa (Chung 2012). Risco residual em 2.5: o dado de embargo é de 2012, mas as eleições vão de 2009 a 2013, e mudanças na lei nesse intervalo gerariam erro de classificação. Também não se considera a aplicação efetiva do embargo nem o acesso a pesquisas por mídia estrangeira ou internet. Julguei PN porque o texto não indica mudanças.

D3 (proposta_baixo). A amostra depende da disponibilidade do dado de Chung e do status "Free" da Freedom House, sem seleção evidente por característica pós-exposição. O desfecho é a eleição inteira sob a regra vigente. Há exposição prevalente (leis antigas), sem tempo imortal; por isso 3.1 = PY.

D4 (proposta_baixo). Os 46 países têm todos os dados (Tabelas 1 e A1). Os confundidores do protocolo não são medidos, mas isso já pesa em D1.

D5 (proposta_baixo). O desfecho vem de resultados eleitorais oficiais e as regras de cálculo (nível inferior nos sistemas mistos, segundo turno) não dependem da exposição.

D6 (proposta_moderado). 6.1 = NI: não há plano de análise nem pré-registro, e pede contato com os autores. São relatados os três modelos, e o efeito aditivo do embargo não é significativo (Modelo 2). A hipótese condicional ao número de partidos está enunciada na seção teórica (p. 9), mas sem plano prévio não dá para descartar que a especificação interativa tenha sido escolhida depois de ver o nulo aditivo. Mesmo com 6.2 a 6.4 = PN, a falta de plano impede o "baixo".

Geral (proposta_grave): pior domínio = D1 grave; os outros são baixos, exceto D6 moderado. Direção imprevisível: o confundimento entre países pode ir para qualquer lado, e o ENEP pós-exposição tende a inflar a interação, mas o texto não permite quantificar.
