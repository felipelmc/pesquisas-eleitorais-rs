---
citekey: Geers2018
ficha_id: Geers2018#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Geers2018.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Geers2018-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 19
faixas_lidas: 1-19
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "tested with multinomial logistic regression analyses" (p. 11); "we controlled for various individual predispositions measured" (p. 8)
- **resultado_avaliado** — resposta: mobilizacao: Tabela 2, coluna Crystallization (vs abstention), linha Poll news / In newspapers (coef. −30.835, EP 15.597, p < 0.05; logit multinomial, N = 765) — evidência: "Crystallization (vs abstention)" (p. 13); "and leads undecided voters to abstain from casting a vote" (p. 13)
- **desenho_resultado** — resposta: coorte_ou_painel_individuos — evidência: "we use a panel dataset and link this to a substantive" (p. 7)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — não há medida da preferência real da população; como é uma única eleição, o conteúdo das pesquisas é comum a todos e só varia entre indivíduos pela escolha de veículos, o que torna este confundidor pouco relevante entre indivíduos ; interesse_politico: controlado — interesse político em escala de 7 pontos medido em t-2 entra no modelo ; preferencia_previa / partidarismo: nao_controlado — só ideologia (esquerda-direita) e extremismo ideológico medidos em t-2 entram como proxies parciais; identificação ou força partidária e a preferência em t-1 não entram como covariáveis, e a escolha do jornal (fonte da variação na exposição) é plausivelmente ligada ao partidarismo — evidência: "political interest, which is measured with an item that asked" (p. 8); "ideology, which is measured with a variable tapping" (p. 9); "we controlled for various individual predispositions measured" (p. 8)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "We also included several control variables" (p. 8)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: B1 = Y)
- **b3_medida_inadequada** — resposta: PN — evidência: "respondents were asked which party they ended up voting for" (p. 8)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "We also included several control variables" (p. 8); "we controlled for various individual predispositions measured" (p. 8)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q4_controles_negativos** — resposta: PN — evidência: "Neither newspaper exposure, nor television" (p. 12)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Não há desenho quase-experimental: painel de indivíduos com regressão logística multinomial ajustada por covariáveis (seleção em observáveis), sem efeitos fixos individuais, sem teste de tendências prévias e sem defesa explícita da ausência de confundimento não medido. O texto traz: (i) comparação descritiva entre quem ficou e quem saiu do painel em interesse político e uso de mídia; (ii) teste de mudanças entre t-2 e t-1 sem efeitos; (iii) modelos com exposição geral a jornal/TV no lugar da exposição a conteúdo, sem efeito — evidência: "from the drop-outs on the most important variables" (p. 7); "tested whether voters also converted or crystallized between t-2 and t-1" (p. 8); "Neither newspaper exposure, nor television" (p. 12)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_nao — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado de 1.1 a 1.5 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: NI — evidência: 999
- **d2_q2_eventos_depois** — resposta: PY — evidência: "At t, the post-election wave, respondents were asked" (p. 8)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = PY)
- **d2_q4_classificacao_influenciada** — resposta: PN — evidência: "All items with political content were coded in collaboration" (p. 9); "we asked respondents about their exposure to the various media outlets" (p. 10)
- **d2_q5_outros_erros** — resposta: PY — evidência: "we are restricted to self-reported measures of news exposure" (p. 17)
- **d2_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: WN — evidência: "Therefore, we include campaign news as from August" (p. 9); "tested whether voters also converted or crystallized between t-2 and t-1" (p. 8)
- **d3_q2_eventos_excluidos** — resposta: NA — evidência: (fluxo: 3.1 = WN)
- **d3_q3_selecao_pos_inicio** — resposta: PN — evidência: "Most respondents dropped out between May and June." (p. 7)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = PN)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = WN e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: PN — evidência: "we only included those respondents that have participated in all waves" (p. 7)
- **d4_q2_outcome_completo** — resposta: N — evidência: "we only included those respondents that have participated in all waves" (p. 7)
- **d4_q3_confundidores_completos** — resposta: PY — evidência: "due to missing values on this variable, we decided to not include" (p. 8)
- **d4_q4_casos_completos** — resposta: Y — evidência: "In this study, we only included those respondents" (p. 7)
- **d4_q5_exclusao_relacionada** — resposta: PY — evidência: "Most respondents dropped out between May and June." (p. 7)
- **d4_q6_explicada_modelo** — resposta: WN — evidência: "from the drop-outs on the most important variables" (p. 7)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = Y)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.4 = Y, 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: PN — evidência: "from the drop-outs on the most important variables" (p. 7); "In the other waves, the recontact rate is very high." (p. 7)
- **d4_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: PN — evidência: "At t, the post-election wave, respondents were asked" (p. 8)
- **d5_q2_avaliadores_cientes** — resposta: PY — evidência: "respondents were asked which party they ended up voting for" (p. 8)
- **d5_q3_influenciada** — resposta: PN — evidência: "respondents were asked which party they ended up voting for" (p. 8)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "For theoretical reasons, the impact of the variables on the outcome" (p. 11); "As robustness check, we also estimated a multinomial regression model" (p. 11)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "As robustness check, we also estimated a multinomial regression model" (p. 11)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "we ran an additional analysis to test the interaction" (p. 14)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Resultado avaliado: Tabela 2 (folha 13 do PDF), coluna "Crystallization (vs abstention)", linha Poll news / In newspapers (−30.835, EP 15.597, p < 0.05). O contraste é cristalização (indeciso ou não votante em t-1 que vota num partido em t) contra abstenção em t; a categoria-base "abstention" inclui qualquer respondente que se absteve em t, inclusive quem tinha partido em t-1, de modo que o contraste é só aproximação de mobilização. A exposição é contínua (frequência autodeclarada de leitura de cada jornal × proporção média de matérias sobre pesquisas no veículo, média sobre 6 jornais).

D1 (variante a; proposta_grave). 1.1 = SN: controles são sexo, educação, idade (t-4), ideologia, extremismo ideológico e interesse político (t-2), exposição a issue news e a poll news no outro meio. Interesse político está controlado. Partidarismo/força da preferência prévia não está: só ideologia como proxy. Como a exposição a issue news em jornais (que capta o volume de leitura de jornal) entra junto, o coeficiente de poll news em jornais é identificado sobretudo pela composição dos jornais lidos (Telegraaf, Volkskrant etc.), que tende a variar com partidarismo, classe e engajamento; a colinearidade entre as duas medidas de jornal (mesma frequência de leitura multiplicada por médias de veículo) ajuda a explicar o coeficiente muito grande e o EP largo. Confundimento residual provavelmente substancial. 1.4 = PN: não há controle negativo propriamente dito; o modelo com exposição geral a jornal e TV sem efeito (nota 15) é uma checagem fraca, e o modelo agregado (nota 16) sem efeito de poll news e a inversão de sinais entre meios são sinais de fragilidade, mas não evidência direta de confundimento grave (por isso não Y/PY). Algoritmo V2: 1.1 = SN e 1.4 = PN → grave. apoio_latente: numa eleição única o conteúdo das pesquisas é comum; não é o confundidor central aqui.

D2 (proposta_moderado). 2.1 = NI: o texto não diz em que onda a frequência de uso de cada veículo foi medida, então não se sabe se a exposição era definida no início do seguimento (t-1). 2.2 = PY: o desfecho é o voto relatado na onda pós-eleição. 2.4 = PN: o conteúdo foi codificado por codificadores independentes da amostra e a frequência de uso é autodeclarada separadamente. 2.5 = PY: exposição autodeclarada (limitação admitida pelos autores), atribuição das médias por veículo a cada leitor (medida ecológica), alfa de Krippendorff de 0,74 e exclusão de fontes on-line (exceto sites de jornais). Erro de classificação provavelmente não diferencial; moderado.

D3 (proposta_moderado). 3.1 = WN: exposição prevalente; o conteúdo conta desde 22/08 (antes de t-1, 30/08) e parte do efeito pode ter ocorrido antes de t-1 (quem já cristalizou até t-1 aparece como estável). Os autores testaram t-2→t-1 sem efeitos, o que sugere que o problema não é substancial. 3.3 = PN: a restrição a quem respondeu todas as ondas é tratada como dado faltante no D4, e a maior parte das saídas ocorreu entre maio e junho, antes da campanha.

D4 (proposta_moderado). A análise usa 765 dos 1537 respondentes iniciais (1187 em t-1; 1162 em t): análise de casos completos. 4.5 = PY: o desfecho envolve comparecimento, e a saída de painéis tende a se associar a menor engajamento; a comparação dos autores cobre só interesse político e uso de mídia. 4.6 = WN: interesse político e uso de mídia estão no modelo e os autores dizem que os que ficaram não diferem muito dos que saíram, então o viés provavelmente não é substancial. 4.11 = PN: só há comparação descritiva, sem análise de sensibilidade ou método robusto à ausência. A nota 5 trata "refuse" na última onda e "no right to vote" como faltantes, sem dizer quantos. Algoritmo: WN em 4.6 → moderado.

D5 (proposta_baixo). Voto e abstenção autodeclarados na onda pós-eleição, com a mesma pergunta para todos; o respondente conhece a própria exposição, mas não há razão para que isso mude o relato do voto. Ressalva para os humanos: a sobredeclaração de comparecimento pode se correlacionar com o engajamento e com o hábito de ler jornal; se isso for considerado erro diferencial, 5.3 pode passar a WY e o domínio a moderado.

D6 (proposta_moderado). 6.1 = NI: não há menção a pré-registro ou plano de análise (a pedir aos autores). As hipóteses são declaradas a priori, e o resultado avaliado contraria a H2a (que previa efeito positivo), o que reduz a suspeita de seleção pelo resultado. As alternativas estão divulgadas nas notas: categorias estável+abstenção colapsadas (efeitos sobre cristalização "marginally significant"), logit binário (poll news em jornais sobre cristalização apenas marginalmente significativo) e modelo agregado sem separar meios (sem efeito de poll news). Por isso 6.2 e 6.3 = PN. Se os humanos entenderem que a escolha da especificação separada por meio e da base "abstention" foi guiada pelo resultado, 6.3 passaria a PY e o domínio a grave.

Geral: proposta_grave, pelo D1 grave (nenhum domínio crítico; B2 = NA, B3 = PN), com quatro domínios moderados reforçando a proposta. Direção imprevisível: o confundimento pelo partidarismo e pela escolha de jornal não tem sentido previsível, e o erro de medida não diferencial puxaria para o nulo.

Perguntas NI para contato com os autores: onda em que foi medida a exposição a cada veículo (2.1) e existência de plano de análise prévio (6.1).
