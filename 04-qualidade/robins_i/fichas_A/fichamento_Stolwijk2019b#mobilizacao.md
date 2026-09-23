---
citekey: Stolwijk2019b
ficha_id: Stolwijk2019b#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Stolwijk2019b.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Stolwijk2019b-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 21
faixas_lidas: 1-20,21-21
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "shows the results of logistic regressions with and without control variables" (p. 11)
- **resultado_avaliado** — resposta: mobilizacao: Tabela 1, col. 3 (CBPS logit), linha Poll exposure, 0.57 (OR 1.77), N = 747; única covariável = Propensity to see polls (CBPS) — evidência: "Table 1. Logistic regression of poll exposure on turnout." (p. 12); "Based on the CBPS logit model, being exposed to polls increases the" (p. 12)
- **desenho_resultado** — resposta: coorte_ou_painel_individuos — evidência: "A four-wave panel survey was carried out in the" (p. 9); "report results using a CBPS (Imai and Ratkovic, 2014)." (p. 10)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — a exposição é ter visto qualquer pesquisa (não o conteúdo) e o escore de propensão não traz medida da preferência agregada; relevância baixa para comparecimento ; interesse_politico: controlado — interesse na campanha das três ondas anteriores entra no CBPS, mas mudanças de interesse durante as quatro semanas de exposição não (são tratadas como mediador) ; preferencia_previa / partidarismo: nao_controlado — nenhuma medida de identificação ou força partidária entra no CBPS; só a intenção prévia de votar capta parte disso (autoposicionamento esquerda-direita aparece só no modelo multivariado da col. 2) — evidência: "The predictors include intention to turn out, campaign cynicism" (p. 10); "as much relevant information from the three waves preceding the EP14 campaign" (p. 10); "self-placement (wave 1) and attention to campaign news (wave 3)." (p. 12)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "when controlling for the prior probability of" (p. 12)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: B1 = Y)
- **b3_medida_inadequada** — resposta: PN — evidência: "Turnout was measured directly after the elections (wave 4) by asking respondents" (p. 10); "providing answer options suggested by Duff et al. (2007)" (p. 18)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "The predictors include intention to turn out, campaign cynicism" (p. 10); "Those who are more likely to cast a vote are more" (p. 10)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q4_controles_negativos** — resposta: PN — evidência: "this effect is likely driven by differences in sample composition" (p. 11)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Ajuste por escore de propensão (CBPS) entrado como covariável única numa logit, sem pareamento propriamente dito. Variáveis que explicam a seleção: intenção de votar, cinismo, interesse na campanha, eficácia informacional e exposição prévia a pesquisas, em várias ondas anteriores à campanha (lista completa só no apêndice online, não incluído no PDF). Balanço de covariáveis após o CBPS e suporte comum não são mostrados no texto principal; mídia (TV, jornal, internet), educação e esquerda-direita entram só no modelo multivariado da col. 2, não na col. 3. Exposição e desfecho foram ambos autodeclarados na onda 4, depois da eleição — evidência: "The predictors include intention to turn out, campaign cynicism" (p. 10); "see the Online appendix for a full list of the estimates" (p. 10); "Since multiple waves of these variables are included, CBPS" (p. 10)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado de 1.1 a 1.5 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: PN — evidência: "was asked (both in wave 3 and 4) whether or not" (p. 11); "never seen any polls in the last four weeks of the campaign" (p. 18)
- **d2_q2_eventos_depois** — resposta: PY — evidência: "never seen any polls in the last four weeks of the campaign" (p. 18)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = PY)
- **d2_q4_classificacao_influenciada** — resposta: WY — evidência: "was asked (both in wave 3 and 4) whether or not" (p. 11); "Turnout was measured directly after the elections (wave 4) by asking respondents" (p. 10)
- **d2_q5_outros_erros** — resposta: PY — evidência: "the effect of self-reported poll exposure on self-reported turnout" (p. 11); "was rather skewed as 59% reported to see no poll" (p. 18)
- **d2_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: PY — evidência: "one month prior to the May 2014 elections for the EP" (p. 9)
- **d3_q2_eventos_excluidos** — resposta: N — evidência: "Turnout was measured directly after the elections (wave 4) by asking respondents" (p. 10)
- **d3_q3_selecao_pos_inicio** — resposta: PN — evidência: "The sample was drawn from the Kantar Public database." (p. 9)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = PN)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = PY e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: PN — evidência: "A total of 1433 respondents participated in wave 1" (p. 9); "and 747 in wave 5" (p. 9)
- **d4_q2_outcome_completo** — resposta: PN — evidência: "A total of 1433 respondents participated in wave 1" (p. 9); "and 747 in wave 5" (p. 9)
- **d4_q3_confundidores_completos** — resposta: PY — evidência: "it has a slightly lower N, due to missing values on left-right" (p. 12)
- **d4_q4_casos_completos** — resposta: PY — evidência: "and 747 in wave 5" (p. 9); "we replicated our results using imputed data for drop-outs after wave 1" (p. 18)
- **d4_q5_exclusao_relacionada** — resposta: PY — evidência: "higher (42.7% versus 18.0%), than that reported by the EP" (p. 18)
- **d4_q6_explicada_modelo** — resposta: WN — evidência: "The predictors include intention to turn out, campaign cynicism" (p. 10); "Panel attrition did not lead to a" (p. 10)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = PY)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: PY — evidência: "we replicated our results using imputed data for drop-outs after wave 1" (p. 18)
- **d4_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: PN — evidência: "Turnout was measured directly after the elections (wave 4) by asking respondents" (p. 10)
- **d5_q2_avaliadores_cientes** — resposta: Y — evidência: "the effect of self-reported poll exposure on self-reported turnout" (p. 11)
- **d5_q3_influenciada** — resposta: WY — evidência: "Self-reported turnout is prone to over-reporting." (p. 18); "over-reporting should not be related to poll" (p. 18)
- **d5_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "by asking respondents whether they had voted" (p. 10)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "shows the results of logistic regressions with and without control variables" (p. 11); "it was decided to recode this into exposure to" (p. 18)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "Based on the CBPS logit model, being exposed to polls increases the" (p. 12)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: favorece_intervencao — evidência: "Those who are more likely to cast a vote are more" (p. 10); "interested in the campaign and more likely to see polls." (p. 10)

## Notas do codificador
Resultado avaliado: Tabela 1 (folha 12 do PDF), coluna 3 "CBPS logit", linha Poll exposure = 0.57 (odds ratio 1.77), N = 747, única covariável o escore de propensão (linha "Propensity to see polls"; "Covariates included" = NO nessa coluna). Encontrado.

Desenho: painel de quatro ondas de jovens eleitores holandeses (EP 2014), com ajuste por Covariate Balancing Propensity Score entrado como covariável numa logit. Classifiquei como coorte_ou_painel_individuos e não como pareamento porque não há pareamento nem ponderação: o escore entra linearmente na regressão. Por isso registrei em qe_* o que se pediria de um pareamento (variáveis da seleção, balanço, suporte comum) e o texto principal não mostra balanço nem suporte comum (remete ao apêndice online, ausente do PDF).

Domínio 1 (variante a, sem mudança de exposição modelada): 1.1 = SN. O escore usa intenção de votar, cinismo, interesse na campanha, eficácia e exposição prévia a pesquisas das ondas 1 a 3 (o interesse aparece logo depois de "campaign cynicism, inter-", com hifenização de fim de linha, por isso não copiei). Não entram no CBPS, pelo que o texto principal mostra: consumo de mídia/atenção a notícias (o marcador mais forte de quem vê pesquisas), educação, partidarismo ou força partidária. A exposição é um indicador de atenção à campanha nas quatro semanas finais, medida na mesma entrevista pós-eleitoral que o desfecho, então a intenção e o engajamento que crescem durante a campanha também confundem. A queda do coeficiente de 1.25 (sem ajuste) para 0.57 mostra seleção forte; a col. 2, com mídia e educação, dá 0.67, o que atenua a preocupação, mas o resultado avaliado é a col. 3. 1.2 e 1.3 = NA pelo fluxo. 1.4 = PN: não há controle negativo nem análise de viés quantitativa; a própria diferença entre modelos indica seleção importante, que já está em 1.1. Algoritmo: 1.1 SN leva a grave; pressupostos do ajuste parcialmente críveis. Proposta: grave.

Domínio 2: a exposição é "ter visto pesquisas nas últimas quatro semanas da campanha", perguntada na onda 4 (após a eleição); não é distinguível no início do seguimento (onda 3), mas o voto ocorre no dia da eleição, ao fim da janela, então 2.2 = PY e 2.3 = NA. 2.4 = WY: a exposição é lembrada e declarada depois do desfecho, na mesma entrevista, por quem já votou ou não; viés de recordação é plausível, mas não há como saber o tamanho (SY é defensável; escolhi WY porque a medida da onda 3 também existe e o padrão de resultados é coerente entre modelos). 2.5 = PY: exposição autodeclarada, dicotomizada (0 vs. 1 ou mais) e com recordação de quatro semanas. Proposta: moderado (WY em 2.4 e PY em 2.5); humanos podem agravar para grave se considerarem SY em 2.4.

Domínio 3: seguimento parte da onda 3 (um mês antes da eleição), que coincide aproximadamente com o início da janela de quatro semanas. Seleção da amostra por cotas no banco Kantar antes da exposição; a perda entre ondas é tratada no domínio 4. Proposta: baixo.

Domínio 4: 1433 participantes na onda 1 e 747 na última onda (o texto escreve "wave 5", erro de digitação do original para a onda 4), perda de cerca de 48%; a análise é de casos completos (N = 747). A perda provavelmente se relaciona com o comparecimento: o comparecimento declarado no painel é 42.7% contra 18.0% oficial para 18 a 24 anos, o que combina desistência de não votantes e sobrerrelato. 4.6 = WN: intenção prévia e interesse no modelo explicam parte da ausência, e os autores relatam que a atrição não alterou idade, gênero e educação, mas não é claro que expliquem tudo. 4.11 = PY porque os autores dizem ter replicado com dados imputados para desistentes após a onda 1; a análise está só no apêndice online, não verificável no PDF. Pelo algoritmo, 4.11 PY poderia levar a baixo; sobrepus para moderado pela perda de quase metade da amostra e pela impossibilidade de verificar a imputação.

Domínio 5: mesma pergunta para todos (5.1 = PN), mas o desfecho é autodeclarado pelo participante, que sabe se viu pesquisas (5.2 = Y). Sobrerrelato de voto é reconhecido; os autores afirmam, com base no apêndice, que ele não se relaciona com a exposição. Se quem é mais atento à campanha também sobrerrelata mais, o viés infla o efeito. 5.3 = WY. Proposta: moderado.

Domínio 6: nenhum plano de análise prévio ou pré-registro mencionado (6.1 = NI, pedir aos autores). Uma medida de desfecho; três modelos relatados lado a lado; a dicotomização da exposição foi decidida pela assimetria da distribuição, não pelos resultados. 6.2 a 6.4 = PN. Proposta: moderado (6.1 NI).

Geral: domínio 1 grave, domínios 2, 4, 5 e 6 moderados, domínio 3 baixo. Pelo pior domínio, grave. Direção: confundimento residual por engajamento (quem tende a votar tende a ver pesquisas, como os próprios autores dizem) e recordação da exposição após o voto tendem a inflar a associação positiva, então favorece_intervencao.

Perguntas NI que pedem contato com autores: 6.1 (plano de análise prévio). Apêndice online (lista completa de preditores do CBPS, balanço, análise com imputação) não estava no PDF.
