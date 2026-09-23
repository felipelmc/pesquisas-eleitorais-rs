---
citekey: Erlich2023
ficha_id: Erlich2023#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Erlich2023.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Erlich2023-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 73
faixas_lidas: 1-20,21-40,41-60,61-73
---

## 00_Resultado
- **unidade_randomizacao** — resposta: individual — evidência: "continuous blocking (Moore 2012) to allocate respondents to either the placebo" (p. 15)
- **resultado_avaliado** — resposta: mobilizacao: Tabela N.12 (Apêndice N.2), coluna Vote, regressão logística com controle Female, coeficiente de American Treatment em log-odds vs. Placebo (−0.09, EP 0.54; N = 181) — evidência: "Outcome of MIPO|X analysis" (p. 56); "vote is a binary variable and logistic regression is used" (p. 56)
- **efeito_de_interesse** — resposta: atribuicao — evidência: (metadados fornecidos pelo coordenador)

## D1b_Recrutamento_cluster
- **d1b_q1_identificados_antes** — resposta: NA_secao — evidência: NA_secao
- **d1b_q2_recrutamento_afetado** — resposta: NA_secao — evidência: NA_secao
- **d1b_q3_desequilibrio_participantes** — resposta: NA_secao — evidência: NA_secao
- **d1b_julgamento_proposto** — resposta: NA_secao — evidência: NA_secao

## D1_Randomizacao
- **d1_q1_sequencia_aleatoria** — resposta: PS — evidência: "I randomize which of the subjects will be exposed" (p. 3); "continuous blocking (Moore 2012) to allocate respondents to either the placebo" (p. 15)
- **d1_q2_ocultacao** — resposta: PS — evidência: "From the data on this recruitment questionnaire, I used multivariate" (p. 15)
- **d1_q3_desequilibrio_base** — resposta: PS — evidência: "yielded balance across all variables, with the exception of gender" (p. 18); "p = 0.0034" (p. 48)
- **d1_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 1.1 a 1.3)

## D2_Desvios_atribuicao
- **d2_q1_participantes_cientes** — resposta: PN — evidência: "This story served to mask the fact for the treatment groups" (p. 16); "and debriefed them about the experiment" (p. 18)
- **d2_q2_executores_cientes** — resposta: SI — evidência: 999
- **d2_q3_desvios_contexto** — resposta: PN — evidência: "listen to the story only once carefully" (p. 67)
- **d2_q4_desvios_afetam** — resposta: NA — evidência: (fluxo: 2.3 = PN)
- **d2_q5_desvios_equilibrados** — resposta: NA — evidência: (fluxo: 2.4 = NA)
- **d2_q6_analise_apropriada** — resposta: PS — evidência: "the models do show relatively lower turnout in both treatment groups" (p. 25)
- **d2_q7_impacto_analise** — resposta: NA — evidência: (fluxo: 2.6 = PS)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: N — evidência: "of the 19 subjects who attrited, or" (p. 55); "none came from the American Treatment Group" (p. 55)
- **d3_q2_evidencia_sem_vies** — resposta: N — evidência: "I cannot rule out that this attrition is not independent" (p. 55)
- **d3_q3_faltante_pode_depender** — resposta: PS — evidência: "could be related to potential outcomes" (p. 25)
- **d3_q4_faltante_provavelmente_depende** — resposta: PS — evidência: "none came from the American Treatment Group" (p. 55); "it is unclear why priming an American polling firm" (p. 55)
- **d3_julgamento_proposto** — resposta: proposta_alto — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: PN — evidência: "In this survey, I asked respondents about their voting" (p. 18)
- **d4_q2_medida_diferiu** — resposta: PN — evidência: "recontacted subjects via a post-election phone survey" (p. 18)
- **d4_q3_avaliadores_cientes** — resposta: PN — evidência: "This story served to mask the fact for the treatment groups" (p. 16)
- **d4_q4_avaliacao_influenciavel** — resposta: NA — evidência: (fluxo: 4.3 = PN)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: PN — evidência: "vote is a binary variable and logistic regression is used" (p. 56)
- **d5_q3_selecao_analises** — resposta: PN — evidência: "the same ATE is present as when I do not attempt" (p. 25)
- **d5_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_alto — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Desenho: experimento lab-in-the-field em Kaspi (Geórgia), 208 sujeitos alocados individualmente a Placebo, American Treatment ou Georgian Treatment por blocagem multivariada contínua (estratos por gênero mais seis variáveis) a partir do questionário de recrutamento; recrutados tardios alocados por blocagem sequencial (p. 15 e 18). Embora os sujeitos fossem convidados ao laboratório em grupos de 10 (p. 15), o texto descreve a atribuição por indivíduo (cada um ouvia o áudio em fones), por isso `unidade_randomizacao = individual` e o bloco D1b recebe NA_secao. O desfecho de mobilização é o comparecimento autodeclarado (coluna Vote da Tabela N.12, binária, logit com Female), medido na pesquisa telefônica pós-eleitoral. Coeficiente American Treatment = −0.09 (0.54), N = 181 de 208.

D1 (proposta_algumas_preocupacoes): 1.1 PS porque o texto diz que randomizou e usou blocagem (Moore 2012) sem descrever o componente de acaso; 1.2 PS porque a alocação foi calculada sobre os dados do recrutamento, depois da inclusão (os tardios, sequencialmente, também depois da inclusão), mas não há descrição de quem executou e se os recrutadores conheciam o esquema. 1.3 PS: gênero ficou desequilibrado (feminino 0.46 placebo, 0.62 EUA, 0.74 Geórgia; p = 0.0034, Tabela K.8) apesar de gênero ser a variável de estratificação, o que é difícil de atribuir ao acaso e sugere falha na implementação da blocagem ou nas entradas sequenciais. O teste conjunto não rejeita o equilíbrio (p = 0.2778, Tabela K.6) e o autor controla por gênero. Algoritmo: 1.2 PS com 1.3 PS leva a algumas preocupações.

D2 (proposta_baixo): os participantes não eram informados do braço (a primeira notícia servia para mascarar o tratamento; debriefing só no contato pós-eleitoral), por isso 2.1 PN. Não há informação sobre o conhecimento da alocação pela equipe do laboratório (2.2 SI; o instrumento tem perguntas marcadas "[FOR CONTROL GROUP]" e "[FOR TREATMENT GROUPS]", o que sugere que o dispositivo sabia o braço, mas não diz se a equipe sabia). Intervenção única em áudio, sem relato de desvios (2.3 PN). A análise compara os grupos como designados; as perdas pertencem ao D3 (2.6 PS).

D3 (proposta_alto): 19 sujeitos (cerca de 9%) não responderam ao contato e o modelo de voto usa 181 de 208. A perda é fortemente diferencial: 0 de 72 no American Treatment contra 11 de 63 no Placebo (82.5% entrevistados) e 8 de 73 no Georgian Treatment (Tabela N.11). O próprio autor diz que não pode descartar que a perda dependa dos desfechos potenciais e trata o padrão como inesperado. A correção MIPO|X controla apenas por gênero, o que não é evidência de ausência de viés (3.2 N). Comparecimento é o tipo de desfecho em que quem não atende ou recusa o contato tende a diferir (menor engajamento), e a perda concentrada no comparador torna provável a dependência do valor verdadeiro (3.3 PS, 3.4 PS). Pelo algoritmo, alto.

D4 (proposta_baixo): comparecimento autodeclarado por telefone é medida usual, embora sujeita a superdeclaração (4.1 PN); mesma pesquisa telefônica para todos os braços (4.2 PN). Em desfecho autodeclarado o avaliador é o participante; ele ouviu a notícia, mas não sabia que havia braços nem a qual pertencia, por isso 4.3 PN. Dúvida: o debriefing ocorreu na mesma ligação e a ordem entre o debriefing e a pergunta sobre voto não é relatada. Se o comitê entender que ouvir a pesquisa atribuída a uma universidade americana equivale a saber a intervenção recebida (4.3 PS, 4.4 PS, 4.5 PN), o domínio passa a algumas preocupações, sem mudar o geral.

D5 (proposta_algumas_preocupacoes): o texto não menciona pré-registro nem plano de análise (5.1 SI; pode valer contato com o autor). Há uma única medida binária de voto; a escolha de voto não foi analisada por não resposta (nota 38). O autor informa que a estimativa sem MIPO|X é a mesma, e o resultado relatado é nulo (5.2 PN, 5.3 PN). O algoritmo leva a algumas preocupações por falta de plano prévio.

Geral: proposta_alto pelo pior domínio (D3), com preocupações adicionais em D1 e D5. Direção: imprevisivel. Se os perdidos do placebo forem sobretudo não votantes, o comparecimento observado do placebo sobe e o efeito do American Treatment fica mais negativo (favoreceria o comparador), mas o texto não informa as razões das perdas nem o comparecimento dos perdidos, por isso não atribuí direção. Observação: a Tabela N.12 rotula como "Placebo" a linha que parece ser o intercepto (8.99 e 1.91).
