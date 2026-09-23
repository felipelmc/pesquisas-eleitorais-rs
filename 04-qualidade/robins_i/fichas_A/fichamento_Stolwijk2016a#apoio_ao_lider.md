---
citekey: Stolwijk2016a
ficha_id: Stolwijk2016a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Stolwijk2016a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Stolwijk2016a-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 21
faixas_lidas: 1-20,21-21
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "logistic regression analysis was performed predicting vote choice" (p. 13)
- **resultado_avaliado** — resposta: apoio_ao_lider: Tabela 1 (p. 567 impressa; p. 14 do PDF), regressão logística da escolha de voto (onda 2), linha Poll exposure index, coef. 0.01 (EP 0.00), OR 1.01, EP robusto agrupado por respondente, N = 6.384 pares respondente-partido — evidência: "Results of a Logistic Regression Predicting Vote Choice by Poll Exposure" (p. 14)
- **desenho_resultado** — resposta: coorte_ou_painel_individuos — evidência: "using a two-wave panel survey at the start and" (p. 7); "set of 6,384 cases representing all possible combinations" (p. 8)
- **confundidores_controlados** — resposta: apoio_latente: controlado (parcialmente) — pela variação agregada da intenção de voto de cada partido nas pesquisas entre as ondas (change in vote share, constante por partido) e pelo voto na onda 1; não há controle da cobertura não eleitoral (tom geral) do veículo sobre o partido, que os autores admitem como explicação alternativa ; interesse_politico: nao_controlado — ausente do modelo da Tabela 1; a nota 19 só afirma que incluí-lo (e conhecimento político, interesse em pesquisas) não muda substancialmente os efeitos, sem mostrar a estimativa; a quantidade de pesquisas expostas (amount of polls) controla em parte o volume de consumo de mídia ; preferencia_previa: controlado — voto na onda 1, avaliação do partido (onda 1), ansiedade e entusiasmo (onda 1) no modelo; a exposição seletiva por veículo segue possível depois da linha de base — evidência: "To control for shifts in vote intention described by polls" (p. 13); "interest in polls, and interest in politics" (p. 13); "likewise did not substantially change the effects reported" (p. 13); "Vote choice (wave 1)" (p. 14); "one alternative explanation for the results found" (p. 18)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "Table 1 shows the results controlling for amount of poll exposure" (p. 13)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: B1 = Y)
- **b3_medida_inadequada** — resposta: N — evidência: "Both panel waves included an official-format voting form" (p. 9)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "one alternative explanation for the results found" (p. 18); "Shifts in polls during the campaign are likely" (p. 16); "Future research using a rolling cross section design could still" (p. 16)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q4_controles_negativos** — resposta: PN — evidência: "poll reports precede changes in media coverage, supporting the argument" (p. 18)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Painel de duas ondas com variável dependente defasada (sem efeitos fixos de indivíduo). Unidade: par respondente-partido (base empilhada). Sem teste de tendências prévias (só duas ondas). Balanço de base: controle por voto, avaliação do partido e emoções na onda 1, mas a onda 1 (23/8 a 1/9) foi a campo depois do início da janela de exposição (21/8). Covariável variante no tempo: variação agregada nas pesquisas por partido. Atrito de 31% entre ondas, sem análise de atrito diferencial por exposição (só comparação com o censo). Robustez relatada: modelo multinível cruzado, bootstrap por partido, índice não transformado, índice recodificado sem dois codificadores, controles extras (nota 19) — evidência: "first wave was fielded on August 23" (p. 8); "starts August 21" (p. 10); "net sample of 1,064 respondents (31% panel attrition)" (p. 8); "results are obtained if this model is estimated as a cross-classified" (p. 13); "Using this poll exposure index for the model in this article yields" (p. 11)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: N — evidência: "covers the same period as the panel survey and starts August 21" (p. 10)
- **d2_q2_eventos_depois** — resposta: Y — evidência: "up to the date of the election (September 22)" (p. 10); "The second wave was fielded the day" (p. 8)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = Y)
- **d2_q4_classificacao_influenciada** — resposta: PN — evidência: "sums were multiplied by the number of days this respondent used" (p. 11)
- **d2_q5_outros_erros** — resposta: PY — evidência: "the reliability could not be calculated for the evaluation of polls" (p. 11); "exposure to polls is not the same as observing" (p. 12)
- **d2_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: PY — evidência: "first wave was fielded on August 23" (p. 8); "starts August 21" (p. 10)
- **d3_q2_eventos_excluidos** — resposta: N — evidência: "The second wave was fielded the day" (p. 8)
- **d3_q3_selecao_pos_inicio** — resposta: PN — evidência: "sampling quota and finished it" (p. 8)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = PN)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = PY e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: PY — evidência: "set of 6,384 cases representing all possible combinations" (p. 8)
- **d4_q2_outcome_completo** — resposta: N — evidência: "net sample of 1,064 respondents (31% panel attrition)" (p. 8)
- **d4_q3_confundidores_completos** — resposta: PN — evidência: "does not allow for missing values, regression imputation" (p. 10)
- **d4_q4_casos_completos** — resposta: Y — evidência: "cases representing all possible combinations of the 1,064" (p. 8)
- **d4_q5_exclusao_relacionada** — resposta: NI — evidência: 999
- **d4_q6_explicada_modelo** — resposta: PY — evidência: "Vote choice (wave 1)" (p. 14)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = Y)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: PN — evidência: "comparable in terms of age and region to national census data" (p. 8)
- **d4_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: N — evidência: "Both panel waves included an official-format voting form" (p. 9)
- **d5_q2_avaliadores_cientes** — resposta: PY — evidência: "could indicate their vote choice on this form" (p. 9)
- **d5_q3_influenciada** — resposta: WY — evidência: "after the elections (September 22) and completed on September 24" (p. 8)
- **d5_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "being the one directly affecting the distribution of seats in parliament" (p. 9)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "have been repeated using the untransformed poll index" (p. 12); "results are obtained if this model is estimated as a cross-classified" (p. 13)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "cases representing all possible combinations of the 1,064" (p. 8)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Leitura: PDF inteiro (21 folhas, faixas 1-20 e 21-21), incluindo notas de rodapé, Tabelas 1 e 2 e referências. Os apêndices suplementares (A a D, citados no texto) não estão anexados ao PDF.

Resultado: o índice de exposição a pesquisas é contínuo (soma, por partido, das avaliações de pesquisas nos veículos usados, ponderada pelos dias de uso); a Tabela 1 usa a versão não transformada. O desfecho é o voto (Zweitstimme) declarado na onda 2, colhida de 22 a 24/9, depois da eleição.

D1 (proposta_grave). Variante a: exposição acumulada ao longo da campanha, sem desvios de protocolo. 1.1 = SN. A preferência prévia está bem controlada (voto, avaliação e emoções na onda 1) e o apoio latente só em parte, pela variação agregada das pesquisas por partido. O interesse político não entra no modelo da Tabela 1: a nota 19 diz que ele não muda os efeitos, mas não mostra o número. O ponto principal é o confundidor que os próprios autores admitem (p. 18): o tom geral da cobertura de cada veículo sobre o partido acompanha o tom das pesquisas nesse veículo e afeta o voto por conta própria, e nada no modelo o controla. Além disso, a onda 1 (23/8 a 1/9) foi a campo depois do início da janela de exposição (21/8), e a variação nas pesquisas é medida durante a exposição. Esses controles podem ser em parte pós-exposição e tendem a enviesar para o nulo, como os autores reconhecem (p. 7-8). 1.4 = PN: não há controles negativos; os autores levantam a explicação alternativa e citam um estudo que apoia a direção pesquisa → cobertura, sem teste próprio. Com 1.1 = SN e 1.4 = PN, o algoritmo dá grave. Se o humano julgar o confundimento pela linha editorial como não substancial (WN), a proposta cai para moderado.

D2 (proposta_moderado). A exposição acumula durante o seguimento (2.1 = N), mas o voto ocorre depois do fim da janela de exposição (2.2 = Y). A classificação combina a codificação de conteúdo, independente do respondente, com os dias de uso declarados. O texto não diz em qual onda o uso de mídia foi medido; se foi na onda 2, a lembrança pode ter sido influenciada pelo voto, mas o componente específico do partido vem da codificação (2.4 = PN). 2.5 = PY: a confiabilidade da avaliação das pesquisas não pôde ser calculada (alfa de Krippendorff 0,32 para SPD nas avaliações de atores e 0,65 para a presença de pesquisa); a amostra de veículos é limitada (primeiras páginas); exposição não é observação. Esse erro é provavelmente não diferencial. A robustez com o índice recodificado dá resultado equivalente (nota 14).

D3 (proposta_baixo). O seguimento começa praticamente no início da campanha. A perda entre as ondas foi tratada como dados faltantes (D4), não como seleção.

D4 (proposta_moderado). 31% de atrito entre as ondas e análise só com quem respondeu a onda 2 (casos completos no desfecho). Não há análise do atrito por exposição ou voto; a única comparação é com o censo (idade, região; mais homens e menos baixa escolaridade). 4.5 = NI: a relação entre abandono e voto é plausível (eleitores menos engajados), mas o texto não informa. 4.6 = PY, porque o voto na onda 1 e as demais covariáveis provavelmente explicam boa parte dessa relação. A avaliação do partido e as emoções faltantes foram preenchidas por imputação de regressão simples, e esses valores imputados entram na Tabela 1 (nota 19). Proponho moderado em vez de baixo por causa do atrito alto sem análise e da imputação simples de confundidores.

D5 (proposta_moderado). O desfecho é autodeclarado e colhido depois de o resultado da eleição ser conhecido. É possível um viés de lembrança a favor dos vencedores, correlacionado com a exposição positiva a pesquisas sobre esses partidos (5.3 = WY).

D6 (proposta_moderado). Não há plano de análise pré-registrado mencionado (6.1 = NI, sem trecho que o afirme ou negue). Pedir aos autores. A escolha da Zweitstimme é justificada; as análises alternativas são relatadas como equivalentes, mas sem números.

Geral (proposta_grave): pior domínio grave (D1), com quatro domínios moderados reforçando. Direção imprevisível: o confundimento pela linha editorial e o viés de lembrança pós-eleitoral afastam do nulo; o erro não diferencial de exposição e os controles pós-exposição puxam para o nulo.
