---
citekey: Farjam2020a
ficha_id: Farjam2020a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Farjam2020a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Farjam2020a-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 10
faixas_lidas: 1-10
---

## 00_Resultado
- **unidade_randomizacao** — resposta: individual — evidência: "assigned to groups of approximately 190 participants, with each group" (p. 3)
- **resultado_avaliado** — resposta: apoio_ao_lider: Tabela 2 (p. 417 impressa), Modelo 2, linha Poll — regressão ordinal de efeitos mistos bayesiana que acrescenta atitude política (termo linear e quadrático) aos controles do Modelo 1; estimativa 0.31 [0.07, 0.58], Bayes Factor 166:1 — evidência: "Predicting Votes for the Most Popular Option" (p. 6)
- **efeito_de_interesse** — resposta: atribuicao — evidência: (metadados fornecidos pelo coordenador)

## D1b_Recrutamento_cluster
- **d1b_q1_identificados_antes** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_q2_recrutamento_afetado** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_q3_desequilibrio_participantes** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_julgamento_proposto** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)

## D1_Randomizacao
- **d1_q1_sequencia_aleatoria** — resposta: PS — evidência: "assigned to groups of approximately 190 participants, with each group" (p. 3); "one of the political issues was randomly selected by computer" (p. 3)
- **d1_q2_ocultacao** — resposta: SI — evidência: 999
- **d1_q3_desequilibrio_base** — resposta: SI — evidência: 999
- **d1_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 1.1 a 1.3)

## D2_Desvios_atribuicao
- **d2_q1_participantes_cientes** — resposta: S — evidência: "For treatments that included the poll, participants were informed" (p. 3)
- **d2_q2_executores_cientes** — resposta: N — evidência: "the experiment was programed using oTree" (p. 3)
- **d2_q3_desvios_contexto** — resposta: SI — evidência: 999
- **d2_q4_desvios_afetam** — resposta: NA — evidência: (fluxo: 2.3 = SI)
- **d2_q5_desvios_equilibrados** — resposta: NA — evidência: (fluxo: 2.4 = NA)
- **d2_q6_analise_apropriada** — resposta: S — evidência: "Table 2 lists the estimates of the models" (p. 5)
- **d2_q7_impacto_analise** — resposta: NA — evidência: (fluxo: 2.6 = S)
- **d2_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: S — evidência: "which only two participants did" (p. 3)
- **d3_q2_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 3.1 = S)
- **d3_q3_faltante_pode_depender** — resposta: NA — evidência: (fluxo: 3.2 = NA)
- **d3_q4_faltante_provavelmente_depende** — resposta: NA — evidência: (fluxo: 3.3 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: N — evidência: "an experimental design in which votes have real political consequences" (p. 1)
- **d4_q2_medida_diferiu** — resposta: N — evidência: "the experiment was programed using oTree" (p. 3)
- **d4_q3_avaliadores_cientes** — resposta: N — evidência: "based on votes within the group, $200 was distributed" (p. 3)
- **d4_q4_avaliacao_influenciavel** — resposta: NA — evidência: (fluxo: 4.3 = N)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: N — evidência: "Voting for the minority option was coded as 0" (p. 5)
- **d5_q3_selecao_analises** — resposta: N — evidência: "The models only differ in that model 1 does not control" (p. 5)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
D1: o texto afirma que "the experiment consisted of six treatments" e que os participantes foram atribuídos aos seis braços. A frase original ("The participants were ran-domly assigned to groups...") tem a palavra "randomly" fragmentada por hifenização de fim de linha no PDF (confirmado na camada de texto: os tokens aparecem separados como "ran-" e "domly"), por isso não pode ser citada inteira pelas regras de evidência. Uso como evidência o trecho limpo "assigned to groups of approximately 190 participants, with each group" (p. 3), que mostra que a unidade atribuída é o participante individual, complementado por "one of the political issues was randomly selected by computer" (p. 3), que mostra que a mesma plataforma (oTree) usa sorteio computacional em outra etapa do desenho. Como o texto não descreve o mecanismo de geração da sequência para a atribuição de tratamento (apenas o fato da atribuição), classifico 1.1 como PS, não S ("aleatorizamos" sem descrição). Não há qualquer menção a ocultação da alocação (1.2=SI): é um experimento on-line automatizado, mas o artigo não descreve procedimento de ocultação. Não há tabela de balanceamento de covariáveis entre os seis braços (1.3=SI). Como 1.2 é desconhecido e 1.3 não mostra evidência de desequilíbrio, proponho algumas_preocupacoes (não dá para afirmar baixo por causa da lacuna em 1.2, e não há indício para alto).

D1b: não se aplica. A unidade de randomização é o participante individual (cada pessoa foi atribuída a um dos seis tratamentos); os "grupos" mencionados no texto são os braços do experimento, não clusters pré-existentes (turma, escola, município) sorteados como unidade.

D2: os participantes necessariamente sabem o conteúdo a que foram expostos (ver ou não a pesquisa), porque essa exposição é o próprio tratamento (2.1=S). Não há um "executor" humano interagindo com o participante: o experimento é inteiramente automatizado via oTree, o que reduz o canal de desvio por quem entrega a intervenção (2.2=N). O artigo não discute desvios do protocolo causados pelo contexto do estudo (2.3=SI); a única perda de participantes mencionada (dois que saíram sem receber recompensa) é tratada aqui como dado faltante (D3), não como desvio de intervenção. A análise de Tabela 2 modela diretamente o efeito da atribuição (coeficiente "Poll") sobre o voto, sem exclusão por adesão (2.6=S). Por causa da lacuna em 2.3, não atribuo baixo; proponho algumas_preocupacoes.

D3: apenas dois participantes, de um total de 1.113, deixaram o experimento sem votar e sem receber recompensa; a esmagadora maioria tem dados do desfecho (3.1=S). Proponho baixo.

D4: o desfecho é um voto real, registrado automaticamente pelo software, não um autorrelato de opinião (4.1=N), medido da mesma forma em todos os braços pela mesma plataforma oTree (4.2=N). Como o registro é comportamental e automático (baseado nos votos, não em avaliação humana), não há avaliador cuja ciência da alocação pudesse influenciar a medida (4.3=N). Proponho baixo.

D5: não há menção a pré-registro ou plano de análise pré-especificado (5.1=SI). O desfecho é definido de forma única (ranking maioria/meio/minoria, codificado 0/1/2), sem indício de escolha entre múltiplas operacionalizações possíveis (5.2=N). Os dois modelos relatados na Tabela 2 diferem apenas pela inclusão de atitude política, e ambos são explicitamente descritos e comparados no texto, sem indício de seleção entre análises alternativas não relatadas (5.3=N). Como 5.2 e 5.3=N, proponho baixo mesmo com 5.1=SI.

Geral: dois domínios (D1 e D2) recebem algumas_preocupacoes por lacunas de relato (ocultação da alocação; desvios de contexto), não por evidência direta de um problema; os demais três domínios são baixo. Não há, no texto, indício concreto que justifique agravar para alto; proponho algumas_preocupacoes no geral. Não identifico um mecanismo textual que aponte uma direção previsível do viés (as incertezas são de ausência de detalhe, não de um mecanismo de distorção conhecido); mantenho imprevisivel.

Nota sobre a citação da Tabela 2: o título completo da tabela contém a palavra "Effect" (ligadura "ff"); como havia alternativa, usei como evidência apenas a parte final do título, "Predicting Votes for the Most Popular Option" (p. 6), que já identifica a tabela sem ambiguidade.

Resultados de {RESULTADOS}: o único resultado listado para Farjam2020a|rob2 (apoio_ao_lider, Tabela 2, Modelo 2, linha Poll) foi localizado no texto sem problemas.
