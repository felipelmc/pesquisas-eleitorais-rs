---
citekey: Stolwijk2019b
ficha_id: Stolwijk2019b#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Stolwijk2019b.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Stolwijk2019b-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 21
faixas_lidas: 1-20,21
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "we used as much relevant information from the three waves preceding" (p. 10)
- **resultado_avaliado** — resposta: mobilizacao: Tabela 1, coluna 3 (CBPS logit turnout), linha Poll exposure — evidência: "The more precise CBPS approach for correcting sample composition" (p. 12)
- **desenho_resultado** — resposta: pareamento — evidência: "various matching procedures are being developed" (p. 10)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — não consta entre os preditores do CBPS nem do modelo multivariado ; interesse_politico: controlado — via interesse na campanha (waves 1-3), um dos preditores do CBPS ; preferencia_previa/partidarismo: nao_controlado — autoposicionamento esquerda-direita entra só no modelo multivariado (coluna 2), não no CBPS — evidência: "The predictors include intention to turn out, campaign" (p. 10); "left-right self-placement (wave 1) and attention" (p. 12)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "report results using a CBPS (Imai and Ratkovic" (p. 10)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: b1_tentou_controlar = Y)
- **b3_medida_inadequada** — resposta: PN — evidência: "tried to minimize this potential by providing answer options" (p. 18)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "The predictors include intention to turn out, campaign" (p. 10)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: d1a_q1_controlou_importantes = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: d1a_q1_controlou_importantes = SN)
- **d1a_q4_controles_negativos** — resposta: NI — evidência: 999

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Seleção: os autores listam as variáveis de base usadas para estimar a propensão a ver pesquisas (intenção de votar, cinismo de campanha, interesse na campanha, eficácia informacional, exposição prévia a pesquisas antes da wave 3) e alegam que o CBPS capta tanto os níveis iniciais quanto as tendências dessas variáveis ao longo do tempo. Balanço de covariáveis entre grupos e suporte comum não são reportados no texto principal; o texto remete ao apêndice online (não incluído neste PDF) para as estimativas completas dos preditores do CBPS — evidência: "does not only serve as a control for different" (p. 10)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: PY — evidência: "each participant was asked (both in wave 3 and" (p. 11)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: d2_q1_distinguiveis_inicio = PY)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: d2_q1_distinguiveis_inicio = PY)
- **d2_q4_classificacao_influenciada** — resposta: NI — evidência: 999
- **d2_q5_outros_erros** — resposta: NI — evidência: 999
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: NI — evidência: 999
- **d3_q2_eventos_excluidos** — resposta: NA — evidência: (fluxo: d3_q1_seguimento_inicio = NI)
- **d3_q3_selecao_pos_inicio** — resposta: PN — evidência: "Panel attrition did not lead to a significant difference" (p. 10)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: d3_q3_selecao_pos_inicio = PN)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: d3_q4_associadas_intervencao = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: d3_q1_seguimento_inicio ≠ SN e d3_q5_influenciadas_outcome ≠ Y/PY)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: d3_q6_analise_corrigiu = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: d3_q7_sensibilidade = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: PY — evidência: "it has a slightly lower N, due to missing values" (p. 12)
- **d4_q2_outcome_completo** — resposta: Y — evidência: "whether they had voted (n ¼ 319/43%) or not" (p. 10)
- **d4_q3_confundidores_completos** — resposta: NI — evidência: 999
- **d4_q4_casos_completos** — resposta: Y — evidência: "we have rerun this model on an imputed dataset" (p. 18)
- **d4_q5_exclusao_relacionada** — resposta: NI — evidência: 999
- **d4_q6_explicada_modelo** — resposta: WN — evidência: "does not only serve as a control for different" (p. 10)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: d4_q4_casos_completos = Y)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: d4_q7_imputacao = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: d4_q8_mar_mcar = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: d4_q7_imputacao = NA)
- **d4_q11_evidencia_sem_vies** — resposta: Y — evidência: "rerun this model on an imputed dataset and found similar results" (p. 18)
- **d4_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: PN — evidência: "Turnout was measured directly after the elections (wave 4)" (p. 10)
- **d5_q2_avaliadores_cientes** — resposta: Y — evidência: "The survey was conducted using Computer Assisted Web Interviewing" (p. 9)
- **d5_q3_influenciada** — resposta: WY — evidência: "Self-reported turnout is prone to over-reporting" (p. 18)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "by asking respondents whether they had voted" (p. 10)
- **d6_q3_selecao_analises** — resposta: N — evidência: "Table 1 shows the results of logistic regressions with and" (p. 11)
- **d6_q4_selecao_subgrupos** — resposta: N — evidência: "Table 1 shows the results of logistic regressions with and" (p. 11)
- **d6_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: afastado_do_nulo — evidência: (derivado dos domínios)

## Notas do codificador
Resultado localizado: Tabela 1 (p. 351 impressa / folha 12 do PDF), coluna "CBPS logit turnout", linha "Poll exposure" = 0.57** (1.77), N = 747. Não há outros resultados de mobilização a fichar neste despacho.

Domínio 1 (confundimento, variante a — a análise reportada em Table 1 col. 3 é um efeito tipo intenção-de-tratar sobre exposição medida uma vez, sem ajuste por desvios/mudanças de protocolo durante o seguimento). O CBPS foi calculado com cinco preditores (intenção de votar, cinismo de campanha, interesse na campanha, eficácia informacional, exposição prévia a pesquisas antes da wave 3), medidos nas três waves anteriores à campanha. Dos três confundidores importantes do protocolo, só "interesse_politico" tem um proxy razoável nessa lista (interesse na campanha); "apoio_latente" (preferência real pelo partido/candidato) e "preferencia_previa"/partidarismo (autoposicionamento esquerda-direita) não entram no CBPS — o autoposicionamento entra só no modelo multivariado da coluna 2, não na coluna 3 avaliada aqui. Por isso respondi 1.1 = SN (confundimento não controlado provavelmente substancial), levando o domínio 1 a proposta_grave, e não a proposta_baixo_exceto_confundimento (que exigiria confundimento de base plausivelmente bem controlado). Não sobrepus o algoritmo formal da ferramenta: seguí o critério do próprio prompt de 1.1 diante da lista de confundidores do protocolo.

Domínio 2: a exposição a pesquisas foi perguntada em wave 3 e wave 4 (últimas quatro semanas), e o turnout foi perguntado em wave 4 (logo após a eleição). O texto não deixa explícito se o "poll exposure" usado na Tabela 1 é o de wave 3 ou wave 4, nem a ordem exata de aplicação dos itens dentro da wave 4 (exposição e voto podem ter sido perguntados na mesma entrevista, o que levantaria dúvida sobre se a classificação da exposição foi de algum modo colorida pelo próprio ato de ter votado ou não). Não há texto que confirme nem descarte isso, por isso 2.4 e 2.5 = NI.

Domínio 3: a amostra final (N = 747) é o painel completo até a wave 4, de um total inicial de 1433 na wave 1. Os autores testam diferença de composição do painel só para idade, gênero e escolaridade (sem diferença significativa), não para interesse político ou engajamento — por isso não presumi se a atrição se relaciona ao desfecho real (3.1 e itens dependentes = NI/NA).

Domínio 4: o modelo da Tabela 1 (coluna 3) usa N = 747, igual ao modelo base sem controles, sugerindo ausência de perda adicional de casos pelos preditores do CBPS (ao contrário do modelo multivariado da coluna 2, que perde casos por falta de autoposicionamento esquerda-direita). Os autores relatam terem reestimado o modelo com dados imputados como checagem de robustez à atrição do painel, com resultados semelhantes — tratei isso como evidência de sensibilidade favorável (4.11 = Y), o que moderou a proposta do domínio 4 para "moderado" em vez de "grave", apesar das lacunas de informação sobre completude dos confundidores (4.3) e sobre a relação entre exclusão e desfecho verdadeiro (4.5).

Domínio 5: o desfecho é autorrelatado (o próprio respondente informa se votou), medido pela mesma pergunta padronizada para todos, o que apoia 5.1 = PN. Como é autorrelato, o próprio respondente "sabe" da sua exposição a pesquisas (5.2 = Y), mas o texto só documenta um problema geral de sobrerrelato do voto (nota 2), sem ligá-lo especificamente a saber ou não da exposição a pesquisas; por isso 5.3 = WY (viés provável, mas não necessariamente substancial e não diferencial por grupo).

Domínio 6: não há menção de pré-registro ou plano de análise prévio no texto (6.1 = NI). A Tabela 1 reporta as três especificações (logit simples, multivariado, CBPS) lado a lado e de forma consistente, o que pesa contra seleção de análises ou subgrupos para este resultado específico (6.3 e 6.4 = N, mesma evidência reaproveitada por se tratar da mesma tabela/mesma frase que descreve as três colunas).

Direção do viés: como o confundimento não controlado mais plausível (apoio latente/partidarismo e interesse político geral) tende a aumentar tanto a exposição a pesquisas quanto o turnout na mesma direção, classifiquei a direção provável como afastado_do_nulo (infla o efeito estimado de poll exposure sobre turnout), mas essa é uma inferência metodológica minha a partir do domínio 1, não uma afirmação dos autores — fica marcada como proposta para o julgamento humano.

Limitação transversal a várias respostas: o artigo remete repetidamente a um "Online appendix" (para a lista completa de estimativas do CBPS, o SEM completo e resultados com dados imputados) que não está incluído neste arquivo PDF. Isso limita a verificação de qe_testes_pressupostos (balanço/suporte comum) e de qualquer detalhe fino sobre a imputação (nota 4). Sinalizo para os avaliadores humanos que esse apêndice, se obtido, pode mudar as respostas de 1.2/1.3 (aqui NA por fluxo) e de qe_pressupostos_crediveis_proposta.
