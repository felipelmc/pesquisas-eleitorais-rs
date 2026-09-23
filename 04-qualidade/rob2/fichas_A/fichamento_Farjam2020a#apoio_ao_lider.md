---
citekey: Farjam2020a
ficha_id: Farjam2020a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Farjam2020a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Farjam2020a-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 10
faixas_lidas: 1-10
---

## 00_Resultado
- **unidade_randomizacao** — resposta: individual — evidência: "assigned to groups of approximately 190 participants, with each group" (p. 3)
- **resultado_avaliado** — resposta: apoio_ao_lider: Tabela 2 (p. 417 impressa), Modelo 2, linha Poll (regressão ordinal bayesiana de efeitos mistos com atitude política linear e quadrática além de idade e gênero) — evidência: "Bayesian Estimates for Mixed-Effect Models Predicting Votes for the Most Popular" (p. 6)
- **efeito_de_interesse** — resposta: atribuicao — evidência: (metadados fornecidos pelo coordenador)

## D1b_Recrutamento_cluster
- **d1b_q1_identificados_antes** — resposta: NA_secao — evidência: (fluxo: unidade_randomizacao = individual)
- **d1b_q2_recrutamento_afetado** — resposta: NA_secao — evidência: (fluxo: unidade_randomizacao = individual)
- **d1b_q3_desequilibrio_participantes** — resposta: NA_secao — evidência: (fluxo: unidade_randomizacao = individual)
- **d1b_julgamento_proposto** — resposta: NA_secao — evidência: (fluxo: unidade_randomizacao = individual)

## D1_Randomizacao
- **d1_q1_sequencia_aleatoria** — resposta: PS — evidência: "assigned to groups of approximately 190 participants, with each group" (p. 3)
- **d1_q2_ocultacao** — resposta: PS — evidência: "the experiment was programed using oTree" (p. 3)
- **d1_q3_desequilibrio_base** — resposta: SI — evidência: 999
- **d1_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 1.1 a 1.3)

## D2_Desvios_atribuicao
- **d2_q1_participantes_cientes** — resposta: S — evidência: "For treatments that included the poll, participants were informed that" (p. 3)
- **d2_q2_executores_cientes** — resposta: PN — evidência: "the experiment was programed using oTree" (p. 3)
- **d2_q3_desvios_contexto** — resposta: PN — evidência: "Participants were compensated with 2$, and the average duration of the" (p. 3)
- **d2_q4_desvios_afetam** — resposta: NA — evidência: (fluxo: 2.3 = PN)
- **d2_q5_desvios_equilibrados** — resposta: NA — evidência: (fluxo: 2.3 = PN)
- **d2_q6_analise_apropriada** — resposta: PS — evidência: "groups that saw the poll results and those that did not." (p. 5)
- **d2_q7_impacto_analise** — resposta: NA — evidência: (fluxo: 2.6 = PS)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: PS — evidência: "All 1,113 participants in this study were recruited via Amazon Mechanical Turk" (p. 3); "and not receiving any reward (which only two participants did)." (p. 3)
- **d3_q2_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 3.1 = PS)
- **d3_q3_faltante_pode_depender** — resposta: NA — evidência: (fluxo: 3.1 = PS)
- **d3_q4_faltante_provavelmente_depende** — resposta: NA — evidência: (fluxo: 3.1 = PS)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: N — evidência: "based on votes within the group, $200 was distributed among the" (p. 3)
- **d4_q2_medida_diferiu** — resposta: PN — evidência: "Voting for the minority option was coded as 0, voting for the" (p. 5)
- **d4_q3_avaliadores_cientes** — resposta: S — evidência: "For treatments that included the poll, participants were informed that" (p. 3)
- **d4_q4_avaliacao_influenciavel** — resposta: PN — evidência: "we ensured and emphasized the anonymity of participants at all stages of" (p. 4)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: NA — evidência: (fluxo: 4.4 = PN)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: PN — evidência: "As the bandwagon effect describes popular opinions becoming more popular, we" (p. 5)
- **d5_q3_selecao_analises** — resposta: PN — evidência: "The models only differ in that model 1 does" (p. 5)
- **d5_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Resultado localizado: Tabela 2 (folha 6 do PDF; p. 417 impressa), Modelo 2, linha "Poll": 0.31 [0.07, 0.58], Bayes factor 166:1. Na camada de texto do PDF os sinais de menos da tabela se perderam; nenhum número da tabela foi usado como trecho.

Classificador: individual. Cada participante foi designado a um de seis "grupos" de cerca de 190 pessoas, cada grupo = um tratamento (poll sim/não × sistema eleitoral). O grupo é só o eleitorado que divide os US$ 200; não há sorteio de grupos pré-existentes nem interação entre participantes durante a votação. Por isso D1b = NA_secao. A dependência entre votos é tratada no modelo por efeitos aleatórios de participante e de tema (folha 7), não de grupo.

D1: a palavra "randomly" está hifenizada na quebra de linha ("ran-/domly assigned", folha 3); pela regra de não atravessar hifenização, o trecho citado começa em "assigned". A aleatorização é declarada mas o mecanismo não é descrito (PS). Ocultação: alocação automática por software (oTree) num experimento online, o que torna a ocultação provável (PS), mas o texto não a descreve. Não há tabela de linha de base por grupo (1.3 = SI). Pelo algoritmo (1.2 PS; 1.1 PS; 1.3 SI) = baixo. Um revisor mais cauteloso poderia propor algumas preocupações pela ausência de comparação de linha de base.

D2: os participantes nos braços com pesquisa foram informados dela (2.1 = S); a intervenção foi entregue pelo software, sem executor humano (2.2 = PN). Sessão única e curta (12 min), sem indício de desvios causados pelo contexto (2.3 = PN). Análise compara os braços como designados (2.6 = PS). Baixo.

D3: 1.113 participantes; só dois abandonaram. Ressalva: houve teste de compreensão (acertar ao menos 4 de 5 perguntas) e o texto não diz quantos foram barrados, nem se isso ocorreu depois da designação; a Tabela 2 não informa o N analisado. Julguei PS pelo pequeno número de abandonos declarados; se o teste de compreensão excluiu pessoas após a designação (as instruções diferiam por braço), a pergunta 3.1 poderia virar SI. Ponto para contato com o autor.

D4: desfecho é o voto real, incentivado (dinheiro efetivamente distribuído às organizações), registrado pelo software e codificado igualmente em todos os braços (0/1/2 segundo a posição da organização na pesquisa prévia). O participante é o "avaliador" e sabe que viu a pesquisa (4.3 = S), mas o desfecho é uma escolha comportamental com consequência real e anonimato garantido, não um julgamento subjetivo; o conhecimento do tratamento é o próprio mecanismo do efeito, não um erro de medida (4.4 = PN). Demanda do experimentador é possível em tese, mas os participantes não sabiam da existência de outros braços e o voto tinha custo real. Baixo. Ressalva: os participantes foram informados de que os respondentes da pesquisa prévia também podiam votar (folha 3), o que pode ter dado à pesquisa um peso estratégico no resultado do grupo; isso é parte da intervenção, não da medida.

D5: nenhum registro, protocolo ou plano de análise prévio é mencionado; dados e scripts estão disponíveis em repositório (folha 4), o que não substitui plano prévio (5.1 = SI). A codificação do desfecho decorre da definição teórica do efeito bandwagon (5.2 = PN). Os dois modelos (com e sem atitude política) são relatados e têm estimativa idêntica para Poll (0.31), o que torna improvável seleção pelo resultado entre análises (5.3 = PN). Ainda assim há flexibilidade analítica não pré-especificada (estrutura bayesiana, priors vagos, escolha de controles). Pelo algoritmo (5.1 SI com 5.2 e 5.3 PN) = algumas preocupações.

Geral: pior domínio = D5 com algumas preocupações; nenhum alto; não agravei. Direção do viés: imprevisível.

Perguntas para contato com o autor: número excluído pelo teste de compreensão e momento em relação à designação; existência de plano de análise prévio; tabela de linha de base por braço.
