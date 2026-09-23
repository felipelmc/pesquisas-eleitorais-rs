---
citekey: Cornejo2023a
ficha_id: Cornejo2023a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Cornejo2023a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Cornejo2023a-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 36
faixas_lidas: 1-20,21-36
---

## 00_Resultado
- **unidade_randomizacao** — resposta: individual — evidência: "The sample was divided into two randomly-assigned groups that" (p. 18)
- **resultado_avaliado** — resposta: apoio_ao_lider: Tabela A6, col. (1) Aggregate Effect (logit, opositores e indecisos; Strategic Voting Effect 0.35*, EP 0.19, N=545) — evidência: "Table A6. Logistic Regression Model" (p. 34); "Aggregate Effect" (p. 34)
- **efeito_de_interesse** — resposta: atribuicao — evidência: (metadados fornecidos pelo coordenador)

## D1b_Recrutamento_cluster
- **d1b_q1_identificados_antes** — resposta: NA_secao — evidência: (fluxo: unidade_randomizacao = individual)
- **d1b_q2_recrutamento_afetado** — resposta: NA_secao — evidência: (fluxo: unidade_randomizacao = individual)
- **d1b_q3_desequilibrio_participantes** — resposta: NA_secao — evidência: (fluxo: unidade_randomizacao = individual)
- **d1b_julgamento_proposto** — resposta: NA_secao — evidência: (fluxo: unidade_randomizacao = individual)

## D1_Randomizacao
- **d1_q1_sequencia_aleatoria** — resposta: PS — evidência: "The sample was divided into two randomly-assigned groups" (p. 18)
- **d1_q2_ocultacao** — resposta: PS — evidência: "The survey randomly assigned a question asking if the respondent" (p. 18)
- **d1_q3_desequilibrio_base** — resposta: PN — evidência: "The treatment appears balanced across observed covariates" (p. 18)
- **d1_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 1.1 a 1.3)

## D2_Desvios_atribuicao
- **d2_q1_participantes_cientes** — resposta: PS — evidência: "the respondent was aware of the results of a recently released poll" (p. 18)
- **d2_q2_executores_cientes** — resposta: PS — evidência: "The polling firm BGC Beltrán y Asocs. conducted a telephone survey" (p. 18)
- **d2_q3_desvios_contexto** — resposta: PN — evidência: "the experiment simply provided polling information without any interpretation" (p. 18)
- **d2_q4_desvios_afetam** — resposta: NA — evidência: (fluxo: 2.3 = PN)
- **d2_q5_desvios_equilibrados** — resposta: NA — evidência: (fluxo: 2.4 = NA)
- **d2_q6_analise_apropriada** — resposta: PS — evidência: "Randomization guarantees that the treatment and control groups in the" (p. 18); "the analysis focuses on the portion of the sample in which" (p. 20)
- **d2_q7_impacto_analise** — resposta: NA — evidência: (fluxo: 2.6 = PS)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: PS — evidência: "(1=support for anti-PRI leading candidate; 0=otherwise)" (p. 19); "Nuevo León (N=290)" (p. 33); "Michoacán (N=255)" (p. 33)
- **d3_q2_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 3.1 = PS)
- **d3_q3_faltante_pode_depender** — resposta: NA — evidência: (fluxo: 3.2 = NA)
- **d3_q4_faltante_provavelmente_depende** — resposta: NA — evidência: (fluxo: 3.3 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: PN — evidência: "which candidate would you vote for?" (p. 19)
- **d4_q2_medida_diferiu** — resposta: N — evidência: "Subsequently, both treatment and control groups were asked a question" (p. 19)
- **d4_q3_avaliadores_cientes** — resposta: PS — evidência: "Did you know that an electoral poll, recently released by a" (p. 19)
- **d4_q4_avaliacao_influenciavel** — resposta: PS — evidência: "Subsequently, both treatment and control groups were asked a question" (p. 19)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: PN — evidência: "the vignette did not include any message inviting third-party supporters to defect" (p. 18)
- **d4_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: PN — evidência: "which constitutes the dependent variable in the" (p. 19)
- **d5_q3_selecao_analises** — resposta: SI — evidência: 999
- **d5_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Resultado avaliado: a string de {RESULTADOS} no despacho está truncada ("col. (1) «Aggregate E"); interpretei como Tabela A6, col. (1) "Aggregate Effect" (p. 34), coeficiente 0.35* (0.19), N=545, amostra de "potential strategic voters" (simpatizantes de partidos atrás nas pesquisas e indecisos), com dummy de estado. Atenção ao mapeamento para `apoio_ao_lider`: a VD é apoio ao candidato anti-PRI com melhor posição (p. 34), enquanto a vinheta põe o PRI empatado na frente em Michoacán e liderando em Nuevo León (p. 19). Em Nuevo León o candidato da VD é o segundo colocado, não o líder; o construto do protocolo (voto em quem a informação mostra à frente) pode não corresponder a este resultado. Cabe ao coordenador/humanos decidir.

D1 (proposta_baixo): 1.1 PS porque o texto diz "randomly-assigned" sem descrever o mecanismo. 1.2 PS: experimento embutido no questionário telefônico da segunda onda do painel, com a pergunta atribuída aleatoriamente pelo próprio questionário a respondentes já recrutados; o texto não descreve a ocultação. Se os humanos entenderem que isso é SI, o domínio passa a algumas_preocupacoes. 1.3 PN: Tabela A4 (p. 32-33) sem diferenças relevantes (College+ p=0.0763). Os tamanhos dos grupos (365 tratamento contra 311 controle) diferem mais do que se espera de uma alocação 1:1 simples (cerca de 2 EP), e a razão de alocação pretendida não é informada. Também há divergência entre "roughly 650 respondents" (p. 18) e os 676 da Tabela A4. Vale anotar, mas sozinho não sugere problema na randomização.

D2 (proposta_baixo): 2.1 PS: o grupo de tratamento ouviu a informação da pesquisa, mas o texto não diz que os respondentes foram informados do experimento (estratégia "indireta", p. 18). 2.2 PS: os entrevistadores leem a vinheta, então conhecem a condição. 2.3 PN: a intervenção é uma única vinheta lida na entrevista, sem espaço para desvios. 2.6 PS: comparação por grupo designado, sem exclusão por adesão. Ressalva para os humanos: a análise se restringe a um subgrupo ("opposition and undecided voters"; em col. 1, N=545 de 676). O texto não diz se o partidarismo e a condição de "don't know" que definem o subgrupo foram medidos antes da vinheta (onda 1 ou início da onda 2) ou depois dela. Se o subgrupo foi definido com variáveis pós-tratamento, a comparação deixa de ser randomizada e 2.6/2.7 devem ser revistos. Pergunta para contato com o autor.

D3 (proposta_baixo): 3.1 PS: a VD codifica 1 = anti-PRI e 0 = qualquer outra resposta (incluindo "não sabe"), e as N da Tabela A5 (290+255=545) batem com a col. (1) da Tabela A6. A atrição alta entre as ondas do painel (Tabela A3, p. 31; entrevistas completas de 39% e 45%) aconteceu antes da randomização, que foi feita na onda 2. Por isso não entra no D3, mas afeta a validade externa.

D4 (proposta_algumas_preocupacoes): desfecho autodeclarado (intenção de voto) perguntado logo depois da vinheta. O avaliador é o próprio respondente e sabe a informação que recebeu (4.3 PS), e intenção declarada logo após o estímulo é suscetível a demanda do experimentador (4.4 PS). 4.5 PN porque a vinheta é neutra, não traz nome do jornal nem da empresa de pesquisa, não convida à deserção, e o texto não indica que o respondente sabia da manipulação. Pelo algoritmo, 4.4 PS com 4.5 PN leva a algumas preocupações.

D5 (proposta_algumas_preocupacoes): 5.1 SI: não há menção a pré-registro nem a plano de análise. 5.2 PN: há uma única pergunta de intenção de voto como VD. 5.3 SI: há várias análises possíveis e não há plano. A amostra analisada é um subconjunto justificado pela teoria ("portion of the sample in which strategic behavior is anticipated", p. 20), o efeito na amostra completa não aparece, os efeitos relatados são marginais (p < 0.06; 0.35 com p < 0.1) e há seis colunas de subgrupos. Esses sinais podem justificar PS, que levaria o domínio a alto. Deixei SI por falta de indício direto de escolha pelo resultado; é decisão para os humanos.

Geral: pior domínio = algumas preocupações (D4 e D5). Não agravei para alto, mas os humanos devem pesar em conjunto a incerteza sobre a definição do subgrupo (D2) e a possível seleção de análise (D5). Direção imprevisível.
