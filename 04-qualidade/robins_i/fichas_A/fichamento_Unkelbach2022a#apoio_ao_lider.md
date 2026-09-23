---
citekey: Unkelbach2022a
ficha_id: Unkelbach2022a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Unkelbach2022a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Unkelbach2022a-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 28
faixas_lidas: 1-20,21-28
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "we were not able to model time-varying individual effects" (p. 25); "includes data from different respondents every day in a representative cross-sectional" (p. 13)
- **resultado_avaliado** — resposta: apoio_ao_lider: Tabela 2 (folha 19 do PDF), coluna SPD, coeficiente de CMVI (β = 0.102, SE = 0.041, OR = 1.107, defasagem de 1 dia), modelo logístico multinível com SES objetiva e interação CMVI × SES — evidência: "For the SPD, CMVI was positively associated with voting intention" (p. 17)
- **desenho_resultado** — resposta: outro — evidência: "we combined the RCS data with results of published preelection polls" (p. 9); "includes data from different respondents every day in a representative cross-sectional" (p. 13)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado, como: o modelo principal só tem SES objetiva, CMVI e a interação; não há controle de tendência temporal nem do apoio subjacente ao SPD, e os próprios autores admitem que pesquisa e intenção medida no RCS podem refletir as mesmas oscilações gerais da opinião ; interesse_politico: nao_controlado, como: ausente do modelo principal (Tabela 2); entra só na checagem de robustez com covariáveis (Tabela A3, no suplemento não anexado ao PDF), relatada como sem mudança significativa ; preferencia_previa / partidarismo: nao_controlado, como: identificação partidária ausente do modelo principal; entra só na mesma checagem de robustez (Tabela A3) — evidência: "we estimated multilevel models with objective SES, CMVI," (p. 17); "general swings of public opinion" (p. 23); "Second, we included covariates (gender, age, general interest in politics, campaign" (p. 20)

## B_Triagem
- **b1_tentou_controlar** — resposta: PN — evidência: "we estimated multilevel models with objective SES, CMVI," (p. 17); "One could argue that our study design" (p. 9)
- **b2_confundimento_descarta** — resposta: PY — evidência: "voting intention was also associated with poll results published the day after" (p. 23); "general swings of public opinion" (p. 23)
- **b3_medida_inadequada** — resposta: PN — evidência: "Which party will you vote for in the federal election?" (p. 10)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "Potentially, unobserved confounders such as external events during the investigated" (p. 9); "general swings of public opinion" (p. 23)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q4_controles_negativos** — resposta: PY — evidência: "voting intention was also associated with poll results published the day after" (p. 23); "The binomial test did not reach" (p. 20)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Não há desenho quase-experimental formal: a exposição (CMVI, participação projetada do partido nas pesquisas publicadas) varia só entre os 55 dias de campo, e o modelo não tem tendência temporal nem efeitos de período. O texto traz: (i) argumento verbal contra eventos externos que movam ao mesmo tempo pesquisa e intenção (coleta das pesquisas dias antes; eventos próximos ao RCS seriam mais salientes); (ii) teste de direção com pesquisas publicadas no dia seguinte ao dia de campo (Tabela A4, suplemento): para o SPD a intenção também se associa às pesquisas posteriores, e o teste binomial entre partidos dá p = 0,500; (iii) defasagens de 0 e 2 dias com estimativa parecida para o SPD; (iv) interação CMVI × percepção de ter visto pesquisas positiva para o SPD; (v) ICC do SPD de 0,005, pouca variação entre dias. Sem balanço entre dias, sem controle de covariáveis variantes no tempo no modelo principal — evidência: "it would have been rather unlikely for an external" (p. 10); "voting intention was also associated with poll results published the day after" (p. 23); "The binomial test did not reach" (p. 20)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_nao — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_critico — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "results of preelection polls published 1 day before the RCS" (p. 9)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = NA)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "The data were obtained from Wahlrecht.de" (p. 9)
- **d2_q5_outros_erros** — resposta: PN — evidência: "a lag of 1 day was chosen" (p. 9); "we used the average of these results" (p. 9)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: PY — evidência: "voting intentions on a daily basis over the last 8 weeks" (p. 9)
- **d3_q2_eventos_excluidos** — resposta: PN — evidência: "the analysis dataset consisted of 5291 respondents nested in" (p. 17)
- **d3_q3_selecao_pos_inicio** — resposta: PN — evidência: "We excluded participants whose postal codes indicated that they cast their vote" (p. 13)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = PN)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = PY e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: Y — evidência: "we matched the RCS data with the most recently published poll results" (p. 9)
- **d4_q2_outcome_completo** — resposta: NI — evidência: 999
- **d4_q3_confundidores_completos** — resposta: NI — evidência: 999
- **d4_q4_casos_completos** — resposta: Y — evidência: "did not impute incomplete or missing data and instead used listwise deletion" (p. 13)
- **d4_q5_exclusao_relacionada** — resposta: NI — evidência: 999
- **d4_q6_explicada_modelo** — resposta: WN — evidência: "Consequently, these variables only varied between" (p. 13); "we listwise excluded all cases with missing data on the" (p. 9)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = Y)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.4 = Y)
- **d4_q11_evidencia_sem_vies** — resposta: PN — evidência: "We did not impute incomplete or missing data" (p. 13)
- **d4_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: PN — evidência: "voting intention was assessed by the single item" (p. 10)
- **d5_q2_avaliadores_cientes** — resposta: PY — evidência: "read or see any results of current opinion polls" (p. 11)
- **d5_q3_influenciada** — resposta: PN — evidência: "The RCS is a large-scale, cross-sectional survey based on phone" (p. 8)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: Y — evidência: "We preregistered all our analyses on the open science framework" (p. 8)
- **d6_q2_selecao_medidas** — resposta: N — evidência: "voting intention was assessed by the single item" (p. 10)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "As indicated by preregistration, we conducted further analyses to assess the" (p. 17); "Instead of a time lag of 1 day, other time lags" (p. 20)
- **d6_q4_selecao_subgrupos** — resposta: N — evidência: "The complete results are displayed in Table 2" (p. 17)
- **d6_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_critico — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: afastado_do_nulo — evidência: "general swings of public opinion" (p. 23); "Both aspects could have decreased the association between CMVI and measured" (p. 22)

## Notas do codificador
Resultado avaliado: coeficiente de CMVI na coluna SPD da Tabela 2 (folha 19), mesmo valor relatado no texto da folha 17 (β = 0.102, OR = 1.107, p unicaudal = 0.006). O resultado existe no PDF. A nota 14 (folha 17) traz um modelo só com CMVI com estimativa parecida (β = 0.096). A escolha do SPD como "líder" é do coordenador: o texto diz que o SPD liderou as pesquisas só no último mês aproximado dos 55 dias (folha 23), e a CDU/CSU liderava no início; a exposição é contínua (participação projetada), não "estar à frente".

Classificador: variante a. A exposição é o valor da pesquisa publicada no dia anterior ao dia de campo, atribuído uma vez a cada entrevistado de um RCS (cortes transversais diários); não há mudança de tratamento ao longo de um seguimento. Desenho "outro": série diária de pesquisas publicadas casada com corte transversal repetido, regressão logística multinível com a variação da exposição só entre dias (nível 2); não é painel de indivíduos nem DiD.

B1 = PN: o modelo que gera o resultado ajusta só a SES objetiva (moderador de interesse, centrada no grupo, portanto ortogonal à exposição de nível 2) e a interação; nenhuma variável que responda pelo confundimento no nível do dia (tendência, apoio subjacente, eventos). Os autores argumentam contra o confundimento (folhas 9-10) em vez de ajustá-lo. A versão com covariáveis individuais (Tabela A3) está no suplemento, não no PDF, e ajuste individual não resolveria o confundimento de nível 2. B2 = PY: a exposição (intenção de voto projetada pelas pesquisas) e o desfecho (intenção de voto no RCS) são duas medidas do mesmo apoio da população ao longo do tempo; os autores reconhecem que ambos podem só refletir "general swings of public opinion" e que medem "the same underlying core construct" (folha 23). Pelo codebook, B2 Y/PY leva a risco crítico.

Domínio 1 (variante a): 1.1 = SN porque apoio_latente, o confundidor central, não é controlado e o confundimento é provavelmente substancial (é o mesmo construto nos dois lados). 1.2 e 1.3 NA pelo fluxo. 1.4 = PY: o teste com pesquisas publicadas no dia seguinte ao dia de campo funciona como controle negativo de exposição (a pesquisa posterior não pode causar a intenção anterior) e, para o SPD, a intenção também se associa às pesquisas posteriores (Tabela A4, suplemento); o teste binomial não sustenta a direção causal. Usei PY, não Y, porque os autores dão explicação alternativa (pesquisas do dia seguinte coletadas em dias próximos ao RCS). Pelo algoritmo, 1.1 = SN com 1.4 = PY dá proposta_critico. Os testes de defasagem 0 e 2 dias e a interação com percepção são coerentes com efeito, mas não afastam a tendência comum.

Domínio 2: exposição atribuída por data a partir de fonte externa (Wahlrecht.de), sem relação com o desfecho; erros possíveis (média entre institutos, uso da pesquisa mais recente quando não houve nova, publicação à noite, respondentes que não viram a pesquisa) são não diferenciais e tratados por desenho (defasagem de 1 dia). A exposição do protocolo é a pesquisa publicada, não a vista. Proposta baixo.

Domínio 3: todos os entrevistados de cada dia são analisados com a pesquisa do dia anterior; exclusões por residência no Sarre (característica anterior à exposição) e gênero não binário; as exclusões por dados faltantes ficam no domínio 4. A exposição cumulativa às pesquisas das semanas anteriores (usuários "prevalentes") é, aqui, um problema de confundimento temporal, já contado no domínio 1. Proposta baixo.

Domínio 4: a amostra cai de 7068 (folha 9) para 5291 (folha 17), cerca de 25%, por exclusão listwise de faltantes em escolaridade, ocupação e intenção de voto, mais Sarre e gênero não binário; o texto não separa quanto se perde no desfecho e quanto nas covariáveis (4.2, 4.3 e 4.5 = NI, pedem contato com autores ou o suplemento). 4.6 = WN: a exposição varia só entre dias e a perda tende a não depender da pesquisa publicada no dia anterior, logo o viés no coeficiente de CMVI provavelmente não é substancial; mas não há análise de sensibilidade (4.11 = PN) e os pesos amostrais não foram usados. Proposta moderado.

Domínio 5: mesmo item de intenção de voto (entrevista telefônica do RCS) em todos os dias. 5.2 = PY porque o desfecho é autodeclarado por quem pode ter visto as pesquisas (a exposição), mas a entrevista é um survey eleitoral geral, sem manipulação nem referência à hipótese, então a demanda do entrevistador é improvável (5.3 = PN). Proposta baixo. Os autores notam que o desfecho inclui indecisos e não votantes e que as pesquisas publicam projeções, não dados brutos (folha 22); isso tende a atenuar a associação, não a criar viés diferencial.

Domínio 6: análises pré-registradas no OSF, desfecho de item único, os seis partidos relatados na Tabela 2, defasagem de 1 dia pré-registrada e as de 0 e 2 dias relatadas como exploratórias com resultado parecido. Os p-valores são unicaudais (pré-registrado). Não vi o pré-registro. Proposta baixo.

Geral: proposta_critico pelo domínio 1 crítico e por B2 = PY. Direção: o confundimento por apoio latente empurra a associação para cima (pesquisas e intenção sobem juntas), por isso afastado_do_nulo; há mecanismos de atenuação citados pelos autores (folha 22), que considero menores que o confundimento estrutural. Um avaliador humano pode preferir imprevisivel.

Dúvidas para o consenso: se B1 deveria ser PY, dada a checagem com covariáveis da Tabela A3 (suplemento não disponível no PDF) e o argumento contra eventos externos; se isso muda o domínio 1 para grave, e não crítico.
