---
citekey: Lago2015
ficha_id: Lago2015#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Lago2015.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Lago2015-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 40
faixas_lidas: 1-20,21-40
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "last Lower-House election held in a sample of 46 democracies" (p. 11)
- **resultado_avaliado** — resposta: apoio_ao_lider | Tabela 2, Modelo 3 (interativo; MQO, EP robustos): termo de interação ENEP × nº de dias de embargo de pesquisas antes da eleição — evidência: "ENEP*#Days of Poll Embargo .002**" (p. 34)
- **desenho_resultado** — resposta: outro — evidência: "Estimation is by OLS with robust standard errors." (p. 14)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — modelo só inclui ENEP, limiar legal, % assentos superiores e idade da democracia, sem medida de preferência real da população ; interesse_politico: nao_controlado — nenhuma variável de interesse político médio do eleitorado entra no modelo ; preferencia_previa/partidarismo: nao_controlado — nenhuma variável de partidarismo prévio do eleitorado entra no modelo — evidência: "We control for three standard variables affecting the amount" (p. 13)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "We control for three standard variables affecting the amount" (p. 13)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: b1_tentou_controlar=Y)
- **b3_medida_inadequada** — resposta: N — evidência: "Wasted votes are a standard variable used to capture electoral coordination" (p. 12)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "We control for three standard variables affecting the amount" (p. 13)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q4_controles_negativos** — resposta: N — evidência: "there are no outliers or influential observations" (p. 14)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: 999 — evidência: 999
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_sem_informacao — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "Number of Days of Poll Embargo prior the Election Day" (p. 13)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = NA)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "The source is Chung (2012)" (p. 13)
- **d2_q5_outros_erros** — resposta: PN — evidência: "Effective Number of Electoral Parties (ENEP) by Laakso and" (p. 13)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: Y — evidência: "the data are dependent on the availability of information" (p. 11)
- **d3_q2_eventos_excluidos** — resposta: N — evidência: "at the national level in the last parliamentary election held" (p. 12)
- **d3_q3_selecao_pos_inicio** — resposta: N — evidência: "An election is deemed to be democratic when and where" (p. 12)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = N)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = Y e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: Y — evidência: "# Days of Poll Embargo 46 2.478 4.902" (p. 33)
- **d4_q2_outcome_completo** — resposta: Y — evidência: "% of Wasted Votes 46 .063 .062" (p. 33)
- **d4_q3_confundidores_completos** — resposta: Y — evidência: "ENEP 46 5.039 2.180 1.932 11.209" (p. 33)
- **d4_q4_casos_completos** — resposta: NA — evidência: (fluxo: 4.1-4.3 = Y)
- **d4_q5_exclusao_relacionada** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q6_explicada_modelo** — resposta: NA — evidência: (fluxo: 4.5 = NA)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 4.1-4.3 = Y e 4.5/4.9/4.10 = NA)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: N — evidência: "We have several sources for the electoral results:" (p. 12)
- **d5_q2_avaliadores_cientes** — resposta: N — evidência: "and the respective Electoral Commissions" (p. 13)
- **d5_q3_influenciada** — resposta: NA — evidência: (fluxo: 5.2 = N)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "The dependent variable is the percentage of wasted votes" (p. 12)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "we have run three specifications: a first model" (p. 14)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "Observations 46" (p. 34)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios; confundimento não mapeável para direção)

## Notas do codificador
Desenho: regressão OLS cross-country (N=46), uma observação por país (última eleição para a câmara baixa), sem painel, sem efeitos fixos de país, sem desenho de experimento natural, RDD, VI ou pareamento — por isso `desenho_resultado=outro` e não há "pressupostos de quase-experimento" (tendências prévias, densidade no corte, primeiro estágio, suporte comum) para relatar (`qe_testes_pressupostos=999`).

Domínio 1 (confundimento): os únicos controles do modelo (ENEP, limiar legal nacional, % assentos no tier superior, idade da democracia) são variáveis institucionais; nenhum dos três confundidores do protocolo (`apoio_latente`, `interesse_politico`, `preferencia_previa`/partidarismo) tem qualquer proxy no modelo agregado por país. Como não há variação identificada (painel, IV, RDD) e o N é pequeno (46 países), o confundimento residual por fatores de cultura política/qualidade institucional correlacionados tanto com a legislação de embargo quanto com o voto desperdiçado foi julgado provavelmente substancial (`SN`), levando à proposta de domínio 1 = `grave`. Os confundidores do protocolo são definidos em nível individual (percepção/interesse/partidarismo do eleitor) e não têm um análogo direto e mensurável no nível país deste resultado agregado; registrei os três como `nao_controlado` porque nenhuma proxy de nível país para eles aparece no modelo, mas a arbitragem humana deve considerar se a ausência de análogo é diferente de "não controlado".

Domínio 2 (classificação da intervenção): a variável de dias de embargo vem de fonte externa e independente (Chung 2012), fixada antes da observação do resultado, e a ENEP é uma medida padrão consolidada (Laakso e Taagepera 1979); por isso domínio 2 = `baixo`.

Domínio 3 (seleção): os critérios de seleção da amostra de países (disponibilidade de dados em Chung 2012; país livre pela Freedom House) são características prévias à observação do resultado, não pós-tratamento nem relacionadas ao outcome; domínio 3 = `baixo`.

Domínio 4 (dados faltantes): a Tabela 1 mostra Obs=46 para todas as variáveis do modelo (outcome, ENEP, exposição e controles), ou seja, sem perdas na amostra analisada; domínio 4 = `baixo`.

Domínio 5 (mensuração do outcome): votos desperdiçados vêm de resultados eleitorais oficiais (bases eleitorais e comissões eleitorais), registro administrativo objetivo, não sujeito a um "avaliador" que conheça a exposição; domínio 5 = `baixo`.

Domínio 6 (seleção do resultado relatado): o artigo relata de forma transparente os três modelos (1, 2 e 3) lado a lado na Tabela 2, o que reduz o risco de relato seletivo, mas o texto explicitamente destaca o modelo interativo (Modelo 3) como o de "maior R² ajustado" e enfatiza a significância da interação como a confirmação da hipótese ("More importantly..."), um padrão compatível com busca de especificação (garden of forking paths) mesmo com divulgação completa; não há menção de plano de análise pré-registrado para a análise agregada (`d6_q1=NI`). Por isso propus domínio 6 = `moderado` em vez de `baixo`.

Resultado de `{RESULTADOS}` localizado sem dificuldade: coeficiente impresso do embargo (.002) corresponde exatamente à linha "ENEP*#Days of Poll Embargo" do Modelo 3, Tabela 2 (p. 34), confirmando a identificação do coordenador.

Nenhuma sobreposição adicional do algoritmo das ferramentas além do já registrado nas notas de domínio acima.
