---
citekey: Brugarolas2021
ficha_id: Brugarolas2021#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Brugarolas2021.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Brugarolas2021-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 8
faixas_lidas: 1-8
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "could be treated as an intention to treat (ITT) effect rather than" (p. 4)
- **resultado_avaliado** — resposta: mobilizacao | Seção 3.2 "Main Result": diferença de médias entre tratados e controles na janela [-0.8; 0.8] dias em torno da divulgação — evidência: "increased the turnout intention by 5.1% (CI: [2.0,9.0])" (p. 6)
- **desenho_resultado** — resposta: regressao_descontinua — evidência: "local randomization regression discontinuity approach" (p. 1)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — o teste de balanço só cobre gênero, idade e tamanho do município, não apoio latente à liderança ; interesse_politico: nao_controlado — mesmo conjunto de covariáveis, sem medida de interesse político ; preferencia_previa: nao_controlado — nenhuma covariável de partidarismo ou preferência prévia entra no teste de balanço — evidência: "predetermined covariates (gender, age, and town size) are balanced" (p. 4)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "To deal with this potential bias, we use a local randomization approach" (p. 2)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: b1_tentou_controlar=Y)
- **b3_medida_inadequada** — resposta: PN — evidência: "strong but imperfect correlation between turnout intention and reported vote" (p. 2)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: WN — evidência: "similar in terms of both their observable and nonobservable characteristics" (p. 4)
- **d1a_q2_medidos_validamente** — resposta: Y — evidência: "gender, age, and town size quotas" (p. 2)
- **d1a_q3_controlou_pos_intervencao** — resposta: N — evidência: "predetermined covariates (gender, age, and town size) are balanced" (p. 4)
- **d1a_q4_controles_negativos** — resposta: N — evidência: "little evidence of RD effects for any of the possible windows" (p. 6)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: RD com variável de corrida categórica (horário da entrevista); janela ótima [-0.8; 0.8] dias escolhida por teste de balanço (T² de Hotelling) aninhado nas 3 covariáveis predeterminadas; robustez a 13 janelas (ATE de 3,4% a 5,1%); 3 placebos com cortes alternativos, sem efeito significativo; nenhum teste de densidade/manipulação do escore (não é o desenho de continuidade) — evidência: "This window comprises four time intervals (mass points) before and" (p. 4); "we used the automatic data-driven window selection procedure" (p. 4); "the ATE in the 13 windows reported in Table A2" (p. 6); "little evidence of RD effects for any of the possible windows" (p. 6)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 1.1 a 1.4 e qe_testes_pressupostos)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "every unit whose score exceeds the cutoff is assigned to the treatment" (p. 2)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1=Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2=NA)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "the day and time of the interview define the running variable" (p. 2)
- **d2_q5_outros_erros** — resposta: Y — evidência: "did not ask whether the respondent had seen the newly released poll" (p. 4)
- **d2_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: Y — evidência: "the day and time of the interview define the running variable" (p. 2)
- **d3_q2_eventos_excluidos** — resposta: N — evidência: "We removed all observations from this interval following the" (p. 3)
- **d3_q3_selecao_pos_inicio** — resposta: N — evidência: "predetermined covariates (gender, age, and town size) are balanced" (p. 4)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3=N)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4=NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1=Y e 3.5=NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6=NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7=NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: Y — evidência: "the day and time of the interview define the running variable" (p. 2)
- **d4_q2_outcome_completo** — resposta: PY — evidência: "comprises 296 respondents" (p. 4)
- **d4_q3_confundidores_completos** — resposta: Y — evidência: "gender, age, and town size quotas" (p. 2)
- **d4_q4_casos_completos** — resposta: NA — evidência: (fluxo: 4.1=Y, 4.2=PY, 4.3=Y)
- **d4_q5_exclusao_relacionada** — resposta: NA — evidência: (fluxo: 4.4=NA)
- **d4_q6_explicada_modelo** — resposta: NA — evidência: (fluxo: 4.5=NA)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4=NA)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7=NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8=NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7=NA)
- **d4_q11_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 4.1-4.3 não PN/N/NI)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: N — evidência: "Our outcome variable is turnout intention, defined as the proportion" (p. 2)
- **d5_q2_avaliadores_cientes** — resposta: NI — evidência: 999
- **d5_q3_influenciada** — resposta: NI — evidência: 999
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: PN — evidência: "we used the automatic data-driven window selection procedure" (p. 4)
- **d6_q2_selecao_medidas** — resposta: N — evidência: "Our outcome variable is turnout intention, defined as the proportion" (p. 2)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "the ATE in the 13 windows reported in Table A2" (p. 6)
- **d6_q4_selecao_subgrupos** — resposta: N — evidência: "Our outcome variable is turnout intention, defined as the proportion" (p. 2)
- **d6_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado de confundidores_controlados e d1a_q1)

## Notas do codificador
Domínio 1: a análise é de intenção de tratar (o texto diz explicitamente que a estimativa "could be treated as an intention to treat (ITT) effect", p. 4), então variante_d1 = a. O desenho é RD por randomização local com variável de corrida categórica (horário da entrevista): a credibilidade do argumento de identificação vem do teste de balanço nas covariáveis predeterminadas (gênero, idade, tamanho do município) e da robustez a 13 janelas e 3 placebos, não de ajuste por covariável nenhuma. Como nenhum dos três confundidores do protocolo (apoio_latente, interesse_politico, preferencia_previa/partidarismo) é testado nem controlado — só as covariáveis de desenho amostral são balanceadas —, marquei 1.1 = WN e não SN: o argumento de randomização local (o texto afirma que unidades devem ser "similar in terms of both their observable and nonobservable characteristics", p. 4) é desenhado para cobrir também confundidores não observados dentro da janela estreita, mas isso nunca é testado empiricamente para atitudes políticas, só para as 3 covariáveis demográficas. Um segundo avaliador pode preferir SN dado que não há nenhum teste direto de covariáveis políticas; documentei o raciocínio para arbitragem humana. Domínio 1 = moderado.

Domínio 2: a classificação do tratamento (antes/depois do corte) é objetiva e não pode ser influenciada pelo outcome (2.4 = N), mas o próprio artigo reconhece que a pesquisa de acompanhamento não perguntou se o respondente viu a pesquisa divulgada (p. 4), o que é evidência direta de erro de classificação da exposição não relacionado ao outcome (2.5 = Y). Domínio 2 = moderado por essa lacuna de exposição, não por viés de conhecimento do outcome.

Domínio 3: não há atrito de amostra nem seleção pós-tratamento; o "donut hole" (2.2) remove só a janela de status de tratamento ambíguo, não eventos de outcome; domínio 3 = baixo.

Domínio 4: dados de tratamento e confundidores vêm do desenho amostral da pesquisa (cotas), portanto completos; dados de outcome muito provavelmente completos dado que os N de cada janela são relatados exatamente, mas o texto não discute não resposta ao item de intenção de voto, por isso 4.2 = PY (não Y). Domínio 4 = baixo.

Domínio 5: a medida do desfecho é o mesmo item de intenção de voto perguntado uniformemente antes e depois do corte, então não há risco de medida diferencial (5.1 = N); o texto não discute se o item foi coletado/apurado sabendo o grupo do respondente (é uma pesquisa padrão da CIS, não um estudo com avaliadores mascarados), por isso marquei NI em 5.2 e 5.3 em vez de presumir. Isso conta nos SI/NI abaixo. Domínio 5 = baixo, mas com duas lacunas de informação assinaladas.

Domínio 6: a janela do resultado principal foi escolhida por um algoritmo de balanço de covariáveis descrito antes de olhar o resultado (data-driven, não claramente pré-registrado), por isso 6.1 = PN; a robustez às 13 janelas é reportada de forma transparente (a mesma direção e significância em quase todas), o que atenua a preocupação de seleção pelo resultado em 6.3, mas ainda marquei PN por não haver um plano de análise pré-especificado explícito. Nenhuma seleção de medida (item único de intenção de voto) nem de subgrupo. Domínio 6 = baixo.

Geral: dois domínios moderados (1 e 2), nenhum grave ou crítico, B2 e B3 não sinalizam risco crítico (B2 = NA, B3 = PN) → geral = moderado, pelo algoritmo "algum moderado, nenhum grave ou crítico".

Direção do viés: não chutei; marquei imprevisível porque o confundimento não testado (apoio latente, interesse político, partidarismo) poderia empurrar o efeito em qualquer direção sem mais informação no texto.

O único resultado de mobilizacao pedido pelo coordenador (Seção 3.2, janela [-0.8; 0.8]) foi localizado sem problema. Nenhum resultado da lista ficou sem correspondência no texto.
