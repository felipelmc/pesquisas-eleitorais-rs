---
citekey: Feltovich2022
ficha_id: Feltovich2022#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Feltovich2022.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Feltovich2022-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 19
faixas_lidas: 1-19
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "the incumbent straw-vote share and its square (allowing for" (p. 15)
- **resultado_avaliado** — resposta: apoio_ao_lider: Tabela 9 (probit, efeitos marginais médios, EP agrupado por sessão), regressor Incumbent straw vote share; col. Vote for Incumbent (Election-Only), células EH+EL = 0.248 (0.037); col. Vote for Incumbent (Message), células MH+ML = 0.442 (0.059); sinal positivo lido pelos autores como efeito bandwagon — evidência: "Incumbent straw vote share" (p. 16); "0.248∗∗∗" (p. 16); "0.442∗∗" (p. 16); "There is an apparent bandwagon effect, with voters more likely" (p. 15)
- **desenho_resultado** — resposta: outro — evidência: "hence, we do not vary whether there is a straw poll" (p. 3); "We estimate separate models for the election-only and messages treatments" (p. 15)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado (como: a parcela na prévia é a própria agregação das preferências do grupo, movidas pela renda comum dada pelo incumbente; o modelo só inclui o voto do próprio sujeito na prévia, o ganho da prévia e dummies de tamanho de grupo; renda do cidadão não entra, os autores supõem que a prévia a incorpora) ; interesse_politico: controlado (como: por desenho, todos os eleitores votam na prévia e todos veem o resultado, então a exposição não depende do interesse; não foi medido) ; preferencia_previa: controlado (como: dummy do voto do próprio sujeito no incumbente na prévia, só nos modelos de voto individual) — evidência: "when applicable, a straw-poll vote for the incumbent" (p. 15); "should incorporate other information voters had before polling, such as income" (p. 15); "First, everyone is polled, rather than a sample of the electorate." (p. 3); "simultaneously and costlessly votes, and then the results are announced" (p. 3)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "when applicable, a straw-poll vote for the incumbent" (p. 15); "Voted for incumbent in straw" (p. 16)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: B1 = Y)
- **b3_medida_inadequada** — resposta: N — evidência: "The dependent variable is either a vote for the" (p. 15); "were programmed in z-Tree" (p. 5)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: SN — evidência: "the right-hand variables are a constant, the" (p. 15); "should incorporate other information voters had before polling, such as income" (p. 15); "Other variables: Quality, performance, message length (both candidates), and group size." (p. 16)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = SN)
- **d1a_q4_controles_negativos** — resposta: N — evidência: "While its impact was not one of our research questions" (p. 17)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: nenhum teste de pressuposto para o efeito da prévia; a presença da prévia não varia entre tratamentos (é instrumento de identificação do efeito das mensagens), a parcela do incumbente na prévia não é atribuída pelo desenho e o efeito da prévia não é pergunta de pesquisa; não há balanço, placebo, tendências nem análise de sensibilidade para esse regressor — evidência: "hence, we do not vary whether there is a straw poll" (p. 3); "In our setting, the straw poll is used as an identification device." (p. 17); "While its impact was not one of our research questions" (p. 17)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_nao — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "after the poll vote counts and winner were announced" (p. 5); "takes place immediately after the straw poll" (p. 3)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "takes place immediately after the straw poll" (p. 3); "simultaneously and costlessly votes, and then the results are announced" (p. 3)
- **d2_q5_outros_erros** — resposta: PN — evidência: "were programmed in z-Tree" (p. 5); "First, everyone is polled, rather than a sample of the electorate." (p. 3)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: Y — evidência: "takes place immediately after the straw poll" (p. 3)
- **d3_q2_eventos_excluidos** — resposta: N — evidência: "incumbent or reelection, so the sample is all" (p. 15)
- **d3_q3_selecao_pos_inicio** — resposta: N — evidência: "a challenger is nominated, equally likely to be any" (p. 3); "Next, a straw poll is run." (p. 3)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = N)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.3 = N)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = Y e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: Y — evidência: "First, everyone is polled, rather than a sample of the electorate." (p. 3)
- **d4_q2_outcome_completo** — resposta: Y — evidência: "our setting does not allow for abstention" (p. 17)
- **d4_q3_confundidores_completos** — resposta: PY — evidência: "simultaneously and costlessly votes, and then the results are announced" (p. 3)
- **d4_q4_casos_completos** — resposta: NA — evidência: (fluxo: 4.1, 4.2 e 4.3 = Y/PY)
- **d4_q5_exclusao_relacionada** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q6_explicada_modelo** — resposta: NA — evidência: (fluxo: 4.5 = NA)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 4.1, 4.2 e 4.3 = Y/PY)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: N — evidência: "were programmed in z-Tree" (p. 5); "Again, everyone simultaneously and costlessly votes." (p. 3)
- **d5_q2_avaliadores_cientes** — resposta: PN — evidência: "were programmed in z-Tree" (p. 5)
- **d5_q3_influenciada** — resposta: NA — evidência: (fluxo: 5.2 = PN)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: N — evidência: "While its impact was not one of our research questions" (p. 17); "of false positives, our emphasis is on results connected" (p. 6)
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "The dependent variable is either a vote for the" (p. 15)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "of all regressions, including those not reported in the main text" (p. 6)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "We estimate separate models for the election-only and messages treatments" (p. 15)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: afastado_do_nulo — evidência: (derivado de 1.1 e confundidores_controlados)

## Notas do codificador
Resultado avaliado: um só construto (apoio_ao_lider) com duas colunas da Tabela 9 (Election-Only, EH+EL; Message, MH+ML), avaliadas juntas nesta ficha; onde as colunas diferem, isso está dito abaixo. A Tabela 9 não informa o N de nenhuma coluna (a Tabela 5, com o mesmo tipo de amostra, informa 5,910 sujeito-rodadas). As estrelas "∗∗∗" em 0.248 e em −0.088 não estão definidas na nota da tabela (que só define †, ∗ e ∗∗): erro de relato menor, sem efeito sobre o risco de viés.

Desenho: experimento de laboratório com tratamentos randomizados (mensagens × variância), mas o regressor avaliado (parcela do incumbente na prévia) NÃO é atribuído pelo desenho: é o agregado dos votos do próprio grupo na prévia. Por isso a leitura por ROBINS-I, como associação observacional dentro do experimento (desenho_resultado = outro). Exposição pontual (prévia anunciada logo antes da eleição, na mesma rodada), sem mudanças de exposição durante o seguimento: variante_d1 = a.

D1 (proposta_grave): 1.1 = SN. O confundidor central, apoio_latente, é a própria preferência do grupo, movida pela renda que o incumbente deu a todos os cidadãos (renda idêntica entre cidadãos; Tabela 5 mostra que a renda prediz fortemente o voto). O modelo da Tabela 9 controla só o voto do próprio sujeito na prévia (binário e cheap talk), o ganho da prévia e o tamanho do grupo; não controla renda nem qualidade/desempenho do incumbente, que os autores supõem já incorporados na prévia. Assim, a parcela na prévia continua carregando o sinal comum sobre o desempenho do incumbente, que também move o voto na eleição: o coeficiente positivo mistura bandwagon com persistência da preferência real, e os próprios autores o chamam de "apparent". Escolhi SN e não WN porque o regressor é quase mecanicamente uma medida da preferência latente que se quer separar. Na coluna Message há um agravante: o modelo inclui dummies de características das mensagens, enviadas DEPOIS do anúncio da prévia e ajustadas por ela (Figura 4, Tabela 8), isto é, variáveis pós-exposição (mediadores); pelo fluxo 1.3 fica NA porque 1.1 = SN, mas isso reforça a preocupação para essa coluna (o 0.442 é efeito "direto", condicional às mensagens). 1.4 = N: não há controle negativo nem análise de viés (o texto não traz consideração que sugira confundimento grave; a conclusão vem do meu raciocínio sobre o desenho). Pelo algoritmo, 1.1 = SN com 1.4 = N leva a grave. Os humanos podem considerar crítico, já que não há estratégia nenhuma de identificação para o efeito da prévia (qe_pressupostos_crediveis_proposta = proposta_nao) e os autores dizem que o efeito da prévia não era pergunta de pesquisa.

D2 (proposta_baixo): parcela na prévia registrada pelo software e anunciada antes da eleição; classificação não pode ser influenciada pelo desfecho.

D3 (proposta_baixo): unidade = sujeito-rodada, excluídos os candidatos, definidos (nomeação do desafiante) antes da prévia; não há seleção por características pós-exposição.

D4 (proposta_baixo): todos votam na prévia e na eleição (sem abstenção), dados gerados pelo software. 4.3 = PY porque o N da Tabela 9 não é informado.

D5 (proposta_baixo): voto registrado pelo z-Tree, mesma medida em todos os níveis de exposição; não há avaliador humano do desfecho. Não é survey com vinheta: o voto decide a eleição e o pagamento, o que reduz demanda do experimentador.

D6 (proposta_moderado): experimento não pré-registrado e o efeito da prévia não era hipótese (6.1 = N). 6.2 a 6.4 = PN: os dois desfechos (voto e reeleição) e os dois tratamentos são relatados, e o coeficiente da prévia é controle numa regressão focada em mensagens, com pouco incentivo para seleção por resultado. Mas há regressões não relatadas "available from the authors" e a especificação (termo quadrático, dummy de ganho) não foi pré-definida; pelo algoritmo, sem plano prévio e sem indício de seleção, moderado.

Geral (proposta_grave): pior domínio = D1 grave; D6 moderado não agrava além de grave. Direção (afastado_do_nulo): o confundimento pela preferência latente comum tende a inflar a associação positiva entre parcela na prévia e voto no incumbente.

Contato com autores: N da Tabela 9; modelo com renda do cidadão e qualidade do incumbente como controles; dados no Dataverse (doi 10.7910/DVN/DAYSCX) permitiriam reestimar.
