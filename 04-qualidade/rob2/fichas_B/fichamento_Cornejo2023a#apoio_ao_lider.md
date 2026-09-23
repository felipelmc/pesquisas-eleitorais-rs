---
citekey: Cornejo2023a
ficha_id: Cornejo2023a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Cornejo2023a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Cornejo2023a-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 36
faixas_lidas: 1-20,21-36
---

## 00_Resultado
- **unidade_randomizacao** — resposta: individual — evidência: "The sample was divided into two randomly-assigned groups" (p. 18)
- **resultado_avaliado** — resposta: apoio_ao_lider: Tabela A6, coluna (1) "Aggregate Effect" (corresponde à Figura 4, painel "3rd Parties + DK"); coeficiente "Strategic Voting Effect"; modelo com controle State dummy; N=545, entre eleitores de oposição e indecisos — evidência: "Table A6. Logistic Regression Model – Vote Choice Effect (among opposition" (p. 34)
- **efeito_de_interesse** — resposta: atribuicao — evidência: (metadados fornecidos pelo coordenador)

## D1b_Recrutamento_cluster
- **d1b_q1_identificados_antes** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_q2_recrutamento_afetado** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_q3_desequilibrio_participantes** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_julgamento_proposto** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)

## D1_Randomizacao
- **d1_q1_sequencia_aleatoria** — resposta: PS — evidência: "The sample was divided into two randomly-assigned groups" (p. 18)
- **d1_q2_ocultacao** — resposta: SI — evidência: 999
- **d1_q3_desequilibrio_base** — resposta: N — evidência: "The treatment appears balanced across observed covariates" (p. 18)
- **d1_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 1.1 a 1.3)

## D2_Desvios_atribuicao
- **d2_q1_participantes_cientes** — resposta: S — evidência: "Did you know that an electoral poll, recently released" (p. 19)
- **d2_q2_executores_cientes** — resposta: PS — evidência: "The survey randomly assigned a question asking if" (p. 18)
- **d2_q3_desvios_contexto** — resposta: SI — evidência: 999
- **d2_q4_desvios_afetam** — resposta: NA — evidência: (fluxo: 2.3 = SI)
- **d2_q5_desvios_equilibrados** — resposta: NA — evidência: (fluxo: 2.4 = NA)
- **d2_q6_analise_apropriada** — resposta: S — evidência: "provides an estimate of the impact of being informed about the electoral poll" (p. 18)
- **d2_q7_impacto_analise** — resposta: NA — evidência: (fluxo: 2.6 = S)
- **d2_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: S — evidência: "the portion of the sample in which strategic behavior is anticipated" (p. 20)
- **d3_q2_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 3.1 = S)
- **d3_q3_faltante_pode_depender** — resposta: NA — evidência: (fluxo: 3.2 = NA)
- **d3_q4_faltante_provavelmente_depende** — resposta: NA — evidência: (fluxo: 3.3 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: N — evidência: "which candidate would you vote for" (p. 19)
- **d4_q2_medida_diferiu** — resposta: N — evidência: "both treatment and control groups were asked a question" (p. 19)
- **d4_q3_avaliadores_cientes** — resposta: S — evidência: "were not asked whether they were aware of the results" (p. 18)
- **d4_q4_avaliacao_influenciavel** — resposta: PS — evidência: "Did you know that an electoral poll, recently released" (p. 19)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: PN — evidência: "vignette did not include any message inviting third-party supporters to defect" (p. 18)
- **d4_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: N — evidência: "Support for the anti-PRI candidate with better standing in the polls" (p. 34)
- **d5_q3_selecao_analises** — resposta: N — evidência: "table A6 in the Appendix reports the complete regressions including" (p. 20)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
D1: a sequência é descrita apenas como "randomly-assigned groups", sem detalhar o mecanismo de geração (número aleatório, sorteio), por isso 1.1=PS ("aleatorizamos" sem descrição, conforme a regra do prompt). Não há qualquer menção a como a alocação foi ocultada até a entrevista (1.2=SI). A Tabela A4 mostra covariáveis balanceadas entre tratamento e controle (todos p>0.05), sustentando 1.3=N. Isso não chega a "baixo" porque a ocultação é desconhecida; proponho algumas_preocupacoes.

D2: neste desenho (informação fornecida na própria entrevista telefônica), a "atribuição" e o "conhecimento da intervenção" pelo participante são a mesma coisa — o respondente do grupo tratamento é informado explicitamente do resultado da pesquisa eleitoral (vinheta lida por telefone), e o grupo controle simplesmente não recebe a pergunta sobre a pesquisa. Isso não é, em si, um desvio problemático, mas é inerente ao desenho. Como o instrumento de entrevista difere por braço, é provável que quem conduziu a ligação soubesse a que braço o respondente pertencia (2.2=PS), embora o texto não afirme isso explicitamente. Não há qualquer discussão no artigo sobre desvios do protocolo causados pelo contexto do estudo (2.3=SI) — nem confirmando nem negando. A análise compara diretamente os grupos definidos pela atribuição (efeito de "being informed"), sem exclusão por adesão, o que sustenta 2.6=S. Por causa da lacuna de informação em 2.3, não atribuo "baixo" a este domínio; proponho algumas_preocupacoes.

D3: a amostra usada no modelo "Aggregate Effect" (N=545) é menor que o total de respondentes randomizados na Tabela A4 (365+311=676). A diferença é explicada no corpo do texto como uma restrição analítica pré-especificada e baseada em características de linha de base (identificação partidária e proximidade nas pesquisas): a análise foca deliberadamente na "portion of the sample in which strategic behavior is anticipated to occur" (eleitores de partidos atrás nas pesquisas e indecisos), não em perda de dados de desfecho. Não há evidência de não resposta adicional ao item de intenção de voto dentro desse subgrupo. Por isso considero 3.1=S e o domínio baixo. Fica registrado, porém, que essa restrição de elegibilidade também é relevante para D5 (ver abaixo) e para a generalização do efeito, ainda que não seja, estritamente, "dado faltante".

D4: o desfecho é autorrelatado (intenção de voto) e o "avaliador" é o próprio respondente, que necessariamente sabe se foi ou não exposto à vinheta com os números da pesquisa (2.1/4.3=S). Isso cria um canal plausível de efeito de demanda: o respondente acabou de ouvir quem lidera e quem está atrás na pesquisa e, na pergunta seguinte, informa para quem vai votar — mecanismo que é justamente o objeto de teste da hipótese 3a, mas que também pode inflar a medida por desejabilidade/coerência percebida (4.4=PS). Reduz esse risco o fato de a vinheta não conter nenhuma sugestão explícita de defecção ("did not include any message inviting third-party supporters to defect"), o que torna uma influência substancial menos provável (4.5=PN), sem eliminá-la. Não proponho "baixo" aqui, dado que o canal de influência (4.4) permanece aberto por desenho; proponho algumas_preocupacoes.

D5: não há registro de pré-registro ou plano de análise pré-especificado para este experimento de sobrevivência de 2015 (5.1=SI). O desfecho de interesse, porém, é definido de forma única e explícita na nota da Tabela A6 ("Support for the anti-PRI candidate with better standing in the polls"), sem indício de que tenha sido escolhido dentre várias operacionalizações possíveis (5.2=N). A regressão reportada para este coeficiente também aparece como a especificação única e "completa" citada no texto ("table A6 ... reports the complete regressions including a state dummy"), sem evidência de seleção entre múltiplas análises alternativas para este número (5.3=N). Como 5.2 e 5.3 = N, proponho baixo para este domínio mesmo com 5.1=SI.

Geral: três domínios (D1, D2, D4) receberam algumas_preocupacoes por razões distintas, mas nenhum chega a alto — nenhuma evidência direta no texto aponta um problema substancial e concreto (todas as incertezas são de ausência de detalhe, não de detalhe que revele falha). Não vi motivo textual para agravar a preocupações-em-vários-domínios até "alto"; proponho algumas_preocupacoes no geral. Sobre a direção do viés, os canais identificados (efeito de demanda no autorrelato, que tenderia a inflar o efeito estratégico na direção da hipótese) e a falta de informação sobre ocultação da alocação (direção incerta) não permitem uma previsão segura de sentido único; mantenho imprevisivel.

Resultados de {RESULTADOS}: o único resultado listado para Cornejo2023a|rob2 (apoio_ao_lider, Tabela A6) foi localizado no texto sem problemas.
