---
citekey: Alabrese2024a
ficha_id: Alabrese2024a#mobilizacao
n_fichas_do_texto: 2
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Alabrese2024a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Alabrese2024a-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 69
faixas_lidas: 1-20,21-40,41-60,61-69
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "both national and local margins are measured before the vote is realized" (p. 23)
- **resultado_avaliado** — resposta: mobilizacao: Tabela 2, col. 2 (comparecimento), interação NationalPollmargin w1 × LocalSafety t-1 = -0.1763 (0.0275); EF distrito + região×ano; EP cluster distrito — evidência: "Table 2: The effect of national opinion poll margins interacted with local" (p. 30); "-0.1763***" (p. 30)
- **desenho_resultado** — resposta: painel_unidades_com_efeitos_fixos — evidência: "exploiting a panel of UK constituencies spanning general elections from 1983" (p. 7)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — a margem das pesquisas nacionais acompanha a preferência nacional real; os EF de região×ano absorvem o nível nacional, mas não a interação entre a disputa nacional real (e o esforço de campanha que ela desloca para cadeiras disputadas) e a segurança local; interesse_politico: nao_controlado — nenhuma medida de interesse, campanha ou cobertura local variável no tempo; só EF de distrito (invariantes) e de região×ano; preferencia_previa: controlado — LocalSafety t-1 (margem Con-Lab da eleição anterior) e EF de distrito; parcial, pois a defasagem da margem com EF de distrito é um painel dinâmico — evidência: "The specification may not entirely rule out the possibility that aggregate" (p. 24); "the one right from the previous general election" (p. 13)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "such as constituency, year, or region-by-year fixed effects" (p. 23)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: B1 = Y)
- **b3_medida_inadequada** — resposta: N — evidência: "Turnout is the ratio between the total number of votes" (p. 30)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "The specification may not entirely rule out the possibility that aggregate" (p. 24); "tight races are correlated with more campaign spending" (p. 9)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q4_controles_negativos** — resposta: PN — evidência: "enables a placebo test, allowing us to verify whether opinion polls" (p. 21)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Painel de distritos com EF; unidade da diferenciação = distrito (nome constante; mudanças de fronteira tratadas por suposição de que o nome preserva a fronteira). Tendências prévias: nenhum teste. Balanço de base: só estatísticas descritivas (Tabela A.1). Covariáveis variantes no tempo: nenhuma além de LocalSafety t-1 e EF. Robustez: coeficiente estável entre EF de ano e de região×ano e gradiente por semana (w1 a w4) na Tabela 2; heterogeneidade por quintil (Figura 5) e por subamostra (Tabela A.5). Atrito diferencial: não discutido. Placebo (pós-eleição) só na análise de survey, não neste resultado. — evidência: "Under the assumption that constituencies retaining the same name over" (p. 12); "Reassuringly, coefficients remain largely unchanged when different fixed effects" (p. 29)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "both national and local margins are measured before the vote is realized" (p. 23)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = NA)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "we focus on national polls produced within four weeks" (p. 15)
- **d2_q5_outros_erros** — resposta: PY — evidência: "Under the assumption that constituencies retaining the same name over" (p. 12); "averaging across the existing pollsters active during" (p. 15)
- **d2_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: PY — evidência: "This work considers all general elections between 1983 and 2017" (p. 12)
- **d3_q2_eventos_excluidos** — resposta: PN — evidência: "the data cover all general elections between 1983 and 2017" (p. 30)
- **d3_q3_selecao_pos_inicio** — resposta: PY — evidência: "where both a Conservative and a Labour candidate competed at least" (p. 13)
- **d3_q4_associadas_intervencao** — resposta: PN — evidência: "This cleaning process eliminates the constituencies of Northern Ireland" (p. 13)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = PN)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = PY e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: PY — evidência: "Corresponding opinion polling data covering the electoral campaign of each general" (p. 18)
- **d4_q2_outcome_completo** — resposta: PY — evidência: "Electoral results at the constituency level are extracted from the" (p. 18)
- **d4_q3_confundidores_completos** — resposta: PY — evidência: "such as constituency, year, or region-by-year fixed effects" (p. 23)
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
- **d5_q1_medida_diferiu** — resposta: PN — evidência: "Turnout is the ratio between the total number of votes" (p. 30)
- **d5_q2_avaliadores_cientes** — resposta: PN — evidência: "Electoral results at the constituency level are extracted from the" (p. 18)
- **d5_q3_influenciada** — resposta: NA — evidência: (fluxo: 5.2 = PN)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: PN — evidência: "CAGE working paper no. 707" (p. 1)
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "with constituency-level turnout as the dependent variable" (p. 28)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "In the odd-numbered columns, we account for constituency and year-fixed effects" (p. 28)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "Additional insights from Table A.5 reveal that this interaction" (p. 29)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: afastado_do_nulo — evidência: (derivado dos domínios)

## Notas do codificador
Desenho. A exposição (margem média das pesquisas nacionais na última semana, a mesma para todos os distritos numa eleição) só é identificada pela interação com a margem local da eleição anterior (LocalSafety t-1), num painel de cerca de 650 distritos em 9 eleições (1983-2017) com EF de distrito e de região×ano. Não é DiD com grupos tratado/controle; classifiquei como painel_unidades_com_efeitos_fixos, que o codebook ROBINS-I prevê. Se o coordenador entender que o desenho é DiD com unidades agregadas, o texto iria para EPOC.

D1 (proposta_grave). variante_d1 = a: exposição e margem local medidas antes do voto, sem mudanças de exposição no seguimento. 1.1 = SN: o confundidor apoio_latente não é controlado para a interação. A margem das pesquisas acompanha a disputa nacional real; eleições nacionalmente desequilibradas mudam o esforço de campanha, os gastos e a cobertura, e essa mudança provavelmente difere entre cadeiras seguras e disputadas (os próprios autores citam, na p. 9, que disputas apertadas atraem mais gasto de campanha). Os EF de região×ano não absorvem essa heterogeneidade, e os autores admitem na p. 24 que fatores distrito×eleição não ficam descartados. interesse_politico também não é medido. preferencia_previa é tratada pela margem defasada e pelos EF de distrito, mas incluir uma função do resultado defasado com EF de distrito num painel curto (T = 9) cria o viés de painel dinâmico. Escolhi SN, e não WN, porque a exposição não pode ser separada da competitividade nacional real, que é plausivelmente o maior confundidor. 1.2 e 1.3 = NA pelo fluxo. 1.4 = PN: não há controle negativo para este resultado; o único placebo (entrevistados pós-eleição, Tabela 4) vale para a análise de survey e não sugere confundimento grave. Pelo algoritmo, 1.1 = SN leva a grave; não levaria a crítico porque 1.4 não é Y/PY. qe = proposta_parcial: há estabilidade entre conjuntos de EF, mas nenhum teste de tendências prévias, nenhum balanço e nenhum placebo agregado.

D2 (proposta_moderado). 2.1 = Y: a exposição é medida antes do voto a partir de arquivos de pesquisas publicadas; 2.4 = N. 2.5 = PY: dois erros de classificação não diferenciais prováveis: (i) LocalSafety t-1 supõe que o distrito que conserva o nome tem a mesma fronteira, apesar das revisões de fronteira no período; (ii) a média das pesquisas não mede a exposição efetiva dos eleitores, e o próprio Apêndice C mostra diferenças sistemáticas entre institutos e jornais. Na p. 15 a média é descrita como feita sobre os institutos "active during the 2017 general election campaign", o que parece erro de redação; se for literal, a medida de exposição dos anos anteriores fica comprometida. Pelo algoritmo, 2.5 = PY leva a moderado.

D3 (proposta_baixo). Entram todas as eleições de 1983 a 2017. 3.3 = PY: a amostra se restringe a distritos em que Conservadores e Trabalhistas competiram ao menos uma vez no período inteiro, e distritos que mudam de nome viram novas unidades. 3.4 = PN: a restrição exclui sobretudo a Irlanda do Norte e não depende da margem nacional das pesquisas.

D4 (proposta_baixo). Resultados eleitorais oficiais e pesquisas arquivadas: dados provavelmente completos (PY em 4.1 a 4.3), e o resto é NA pelo fluxo.

D5 (proposta_baixo). O desfecho vem de registros eleitorais oficiais, medidos igualmente em todos os distritos. 5.1 e 5.2 = PN.

D6 (proposta_moderado). É um working paper sem plano de análise prévio mencionado (6.1 = PN). Relatam várias janelas, conjuntos de EF e subamostras (6.2 a 6.4 = PN). Pela versão 2 do ROBINS-I, sem plano e sem indício de seleção, a proposta é moderado. A nota 22 (p. 29) cita modelos disponíveis só "on request".

Geral (proposta_grave): pior domínio grave (D1), com D2 e D6 moderados. Nenhuma pergunta sem informação pede contato com os autores; a mais útil seria a lista de institutos usada na média de cada ano (p. 15).

Específico de mobilizacao (Tabela 2, col. 2, p. 30; N = 4.676; EP cluster por distrito). Resultado localizado. Direção proposta afastado_do_nulo: a competitividade nacional real e o esforço de campanha concentrado em cadeiras disputadas quando a eleição está aberta deprimiriam o comparecimento nas cadeiras seguras, no mesmo sentido do coeficiente negativo. É uma proposta; se os avaliadores preferirem cautela, imprevisivel.
