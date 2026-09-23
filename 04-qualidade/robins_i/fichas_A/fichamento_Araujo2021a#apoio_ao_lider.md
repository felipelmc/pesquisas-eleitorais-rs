---
citekey: Araujo2021a
ficha_id: Araujo2021a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Araujo2021a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Araujo2021a-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 20
faixas_lidas: 1-20
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "Treatment is a dummy that takes a value of 1" (p. 11)
- **resultado_avaliado** — resposta: apoio_ao_lider: Figura 2, Modelo 1 (frontrunner), OLS, primeiro turno (+5,69 pp); Figura 3, Modelo 1 (frontrunner), OLS, segundo turno (+11,76 pp) — evidência: "support for the announced frontrunner is 5.69 pp higher in treated units" (p. 12); "Bolsonaro’s vote share increases by 11.76 pp in voting machines" (p. 14)
- **desenho_resultado** — resposta: experimento_natural — evidência: "2018 Brazilian election provides a unique natural experimental setting" (p. 5)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — só covariáveis sociodemográficas por urna (idade média, mulheres, escolaridade), fuso, comparecimento, atraso de fechamento e % de erro biométrico; sem voto anterior nem efeitos fixos de local; os autores admitem que urnas tratadas e de controle diferem (Norte/Nordeste) e que não há pesquisas por urna ; interesse_politico: nao_controlado — só o comparecimento por urna, que é pós-exposição e proxy fraco ; preferencia_previa / partidarismo: nao_controlado — o voto de 2014 entra só como checagem de balanço (Apêndice M), não como controle, e mostra que as urnas tratadas eram mais pró-PT — evidência: "means that treated and untreated units are dissimilar across" (p. 11); "Polls of voting intentions are not available" (p. 14); "characteristics of voters registered to cast ballots on each voting machine" (p. 12)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "Our models also include a vector of covariates" (p. 11)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: B1 = Y)
- **b3_medida_inadequada** — resposta: PN — evidência: "we code five different outcome variables" (p. 10)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "means that treated and untreated units are dissimilar across" (p. 11); "Polls of voting intentions are not available" (p. 14); "units exposed to information in 2018 were more prone to" (p. 15)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q4_controles_negativos** — resposta: PN — evidência: "our placebo treatment shows no indication of a bandwagon effect" (p. 16); "evidence to suggest that units treated in 2018 were already more predisposed" (p. 15)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Experimento natural (atraso por falha da biometria como fonte de variação). Exogeneidade defendida por argumento (falhas equiprováveis entre seções com biometria), sem teste formal; balanço de base: autores admitem que tratadas e controle diferem (mais Norte/Nordeste, eleitorado mais jovem e menos escolarizado); modelos com e sem controles pré-tratamento não mudam a estimativa (Apêndice D); checagem com voto de 2014 (Apêndice M): tratadas eram mais pró-PT, não mais pró-Bolsonaro; placebo com atraso antes das 19:00 sem efeito de adesão; robustez sem Acre, só seções com falha biométrica e por tamanho de seção. Sem voto defasado como controle, sem efeitos fixos de local e sem teste de descontinuidade no horário — evidência: "there is no reason to believe that the occurrence of technical glitches" (p. 11); "controls for characteristics of the electorate do not change our estimates" (p. 11); "means that treated and untreated units are dissimilar across" (p. 11); "our placebo treatment shows no indication of a bandwagon effect" (p. 16); "we rerun our estimates without Acre-based observations" (p. 14)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "machines that remained open after preliminary results started being announced" (p. 11)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q4_classificacao_influenciada** — resposta: PN — evidência: "include the time of actual closure of each voting machine" (p. 11)
- **d2_q5_outros_erros** — resposta: PY — evidência: "our empirical strategy captures the impact of information exposure indirectly" (p. 15); "it is not possible to know how many voters cast ballots after" (p. 12)
- **d2_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: PY — evidência: "are available for each round of the election for all 454,490" (p. 10)
- **d3_q2_eventos_excluidos** — resposta: PN — evidência: "we code five different outcome variables" (p. 10)
- **d3_q3_selecao_pos_inicio** — resposta: PN — evidência: "all voting machines contained ballots cast for our five outcome variables" (p. 10)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = PN)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = PY e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: PY — evidência: "include the time of actual closure of each voting machine" (p. 11)
- **d4_q2_outcome_completo** — resposta: PY — evidência: "are available for each round of the election for all 454,490" (p. 10)
- **d4_q3_confundidores_completos** — resposta: PY — evidência: "characteristics of voters registered to cast ballots on each voting machine" (p. 12)
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
- **d5_q1_medida_diferiu** — resposta: PN — evidência: "electronic voting machines means that electoral results are calculated speedily" (p. 7)
- **d5_q2_avaliadores_cientes** — resposta: PN — evidência: "voting machines shuffle the order of individual votes" (p. 12)
- **d5_q3_influenciada** — resposta: NA — evidência: (fluxo: 5.2 = PN)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "we code five different outcome variables" (p. 10)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "Our results also remain stable in a series of robustness checks" (p. 14)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "Results across these models are largely consistent with the ones" (p. 14)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: "units exposed to information in 2018 were more prone to" (p. 15); "it is not possible to know how many voters cast ballots after" (p. 12)

## Notas do codificador
Resultado avaliado: apoio_ao_lider = participação de votos de Bolsonaro (frontrunner) por urna, Modelo 1 da Figura 2 (1º turno, +5,69 pp, N = 452.656) e Modelo 1 da Figura 3 (2º turno, +11,76 pp, N = 453.016), OLS com erros agrupados na urna. As duas estimativas compartilham desenho, dados e especificação, por isso ficam numa só ficha; as respostas valem para as duas. Os coeficientes numéricos estão nos gráficos (imagem) e no texto; a tabela está no Apêndice F on-line, que não está no PDF.

Classificador: variante a. A exposição é definida uma vez por urna (fechou depois das 19:00 BRT) e a análise é transversal, sem mudanças de intervenção no seguimento.

Domínio 1 (proposta_grave): 1.1 = SN. A atribuição do "tratamento" depende do atraso das filas, e os próprios autores reconhecem que urnas tratadas e de controle diferem (concentração no Norte/Nordeste, eleitorado mais jovem e menos escolarizado). O ajuste é só por idade média, índice de mulheres, escolaridade, fuso, comparecimento, atraso e % de erro biométrico. Não há controle para apoio_latente (voto anterior no município/seção, efeitos fixos de local de votação ou município), nem para partidarismo; o voto de 2014 entra só como teste de balanço e mostra desequilíbrio (tratadas mais pró-PT). Urnas que fecham tarde tendem a ser seções grandes e urbanas, uma fonte plausível de confundimento não ajustada. Chamo de SN (e não WN) também pelo tamanho do efeito: como só uma parte dos eleitores de cada urna tratada votou depois das 19:00 (os autores não sabem quantos), +5,69 pp e +11,76 pp na urna inteira implicariam mudanças muito grandes entre os poucos expostos, o que sugere diferença de base entre as urnas mais do que efeito da informação. 1.2 e 1.3 = NA pelo fluxo. Mesmo assim, registro que o modelo controla o comparecimento, que os autores dizem poder ser afetado pela exposição (variável pós-intervenção), e o atraso de fechamento, quase colinear com o tratamento. 1.4 = PN porque os controles negativos dos autores (placebo de atraso antes das 19:00; voto de 2014) não apontam confundimento a favor do líder. A suspeita sobre o tamanho do efeito é consideração minha, não controle negativo do texto. Pelo algoritmo do ROBINS-I V2, 1.1 = SN com 1.4 = PN leva a grave. Pressupostos do experimento natural: proposta_parcial (há placebo, teste com 2014 e robustez, mas o balanço falha e a exogeneidade é só argumentada).

Domínio 2 (proposta_moderado): a classificação da urna vem do registro oficial do horário da última votação, objetivo e não influenciado pelo desfecho (2.1 = Y, 2.4 = PN). 2.5 = PY: a exposição de interesse é individual (ver a apuração antes de votar), mas o tratamento é da urna, e a maioria dos votos de uma urna tratada foi dada antes das 19:00; os autores admitem que medem a exposição indiretamente e que não sabem se os eleitores viram a informação. É erro de classificação em grande parte não diferencial, que tende a diluir o efeito. Proponho moderado, e não grave, por isso.

Domínio 3 (proposta_baixo): todas as urnas do país entram; só saem as que não têm votos para a variável de desfecho (nota 13; cerca de 0,4% no Modelo 1). O desfecho da urna soma votos dados antes e depois do marco das 19:00; tratei isso como diluição (domínio 2) e não como seleção.

Domínio 4 (proposta_baixo): dados administrativos para quase todas as urnas (N de 452.656 e 453.016 em 454.490). Os N vêm das figuras; a completude das covariáveis é inferida pelos N dos modelos, não declarada.

Domínio 5 (proposta_baixo): votos contados pelas urnas eletrônicas, mesma medida para tratadas e controle, sem avaliador humano.

Domínio 6 (proposta_moderado): 6.1 = NI (não há plano de análise prévio ou pré-registro citado; há dados de replicação no Dataverse). Os cinco desfechos são relatados e há vários testes de robustez nos apêndices, por isso 6.2 a 6.4 = PN. Pelo algoritmo V2, sem plano prévio e sem sinal de seleção leva a moderado. Inconsistências de relato que o humano pode querer conferir: a nota das Figuras 2 e 3 lista os controles "time zone, age, percentage of women voters and years of schooling", enquanto o texto e os gráficos mostram também atraso, % de erro biométrico e comparecimento; o número de urnas tratadas no 2º turno aparece como 1.024 (p. 3) e 1.084 (p. 11).

Geral (proposta_grave): o pior domínio é o 1 (grave), com os domínios 2 e 6 moderados. Não agravei para crítico: B2 e B3 não se aplicam e a tentativa de ajuste existe.

Direção do viés: imprevisível. A diluição da exposição e o desequilíbrio pró-PT em 2014 puxariam para o nulo; o confundimento por tamanho/urbanização das seções e a magnitude implausível sugerem viés afastado do nulo. O texto não permite escolher.

Contato com autores: 6.1 (plano de análise prévio); proporção de eleitores que votou depois das 19:00 nas urnas tratadas; tabela do Apêndice F com a especificação exata do Modelo 1.
