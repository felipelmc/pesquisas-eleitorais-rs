---
citekey: Feltovich2022
ficha_id: Feltovich2022#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Feltovich2022.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Feltovich2022-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 19
faixas_lidas: 1-19
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "the election takes place immediately after the straw poll" (p. 3)
- **resultado_avaliado** — resposta: Tabela 9, colunas "Vote for Incumbent (Election-Only)" e "Vote for Incumbent (Message)"; regressor = parcela de votos do incumbente na prévia (efeito bandwagon) — evidência: "Vote for Incumbent (Election-Only)" (p. 16); "Vote for Incumbent (Message)" (p. 16)
- **desenho_resultado** — resposta: coorte_ou_painel_individuos — evidência: "sample is all subject-rounds, excluding candidates, or all group-rounds" (p. 15)
- **confundidores_controlados** — resposta: apoio_latente: controlado — qualidade do titular/desafiante (θ) entra como controle na regressão ; interesse_politico: sem_informacao — não discutido pelos autores, exposição à prévia é universal e obrigatória por desenho ; preferencia_previa_partidarismo: sem_informacao — não discutido; ambiente de laboratório sem partidarismo real — evidência: "Other variables: Quality, performance, message length (both candidates), and group size." (p. 16); 999; 999

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "Other variables: Quality, performance, message length (both candidates), and group size." (p. 16)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: b1_tentou_controlar=Y)
- **b3_medida_inadequada** — resposta: N — evidência: "programmed in z-Tree" (p. 5)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: PY — evidência: "Other variables: Quality, performance, message length (both candidates), and group size." (p. 16)
- **d1a_q2_medidos_validamente** — resposta: Y — evidência: "Quality was randomly drawn for challengers" (p. 5)
- **d1a_q3_controlou_pos_intervencao** — resposta: Y — evidência: "after the poll vote counts and winner were announced" (p. 5)
- **d1a_q4_controles_negativos** — resposta: N — evidência: "Clustering by group instead of session, using linear models" (p. 6)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: 999 — evidência: 999
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_sem_informacao — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 1.1 a 1.4 e qe_testes_pressupostos)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "simultaneously and costlessly votes, and then the results are announced" (p. 3)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1=Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2=NA)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "programmed in z-Tree" (p. 5)
- **d2_q5_outros_erros** — resposta: N — evidência: "programmed in z-Tree" (p. 5)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: Y — evidência: "the election takes place immediately after the straw poll" (p. 3)
- **d3_q2_eventos_excluidos** — resposta: NA — evidência: (fluxo: 3.1=Y)
- **d3_q3_selecao_pos_inicio** — resposta: N — evidência: "sample is all subject-rounds, excluding candidates, or all group-rounds" (p. 15)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3=N)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.3=N)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.3=N)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.3=N)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.3=N)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: Y — evidência: "we do not allow abstention in polling and the election" (p. 3)
- **d4_q2_outcome_completo** — resposta: Y — evidência: "we do not allow abstention in polling and the election" (p. 3)
- **d4_q3_confundidores_completos** — resposta: Y — evidência: "Quality was randomly drawn for challengers" (p. 5)
- **d4_q4_casos_completos** — resposta: NA — evidência: (fluxo: 4.1,4.2,4.3=Y)
- **d4_q5_exclusao_relacionada** — resposta: NA — evidência: (fluxo: 4.1,4.2,4.3=Y)
- **d4_q6_explicada_modelo** — resposta: NA — evidência: (fluxo: 4.1,4.2,4.3=Y)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.1,4.2,4.3=Y)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.1,4.2,4.3=Y)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.1,4.2,4.3=Y)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.1,4.2,4.3=Y)
- **d4_q11_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 4.1,4.2,4.3=Y)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: N — evidência: "programmed in z-Tree" (p. 5)
- **d5_q2_avaliadores_cientes** — resposta: N — evidência: "programmed in z-Tree" (p. 5)
- **d5_q3_influenciada** — resposta: NA — evidência: (fluxo: 5.2=N)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: N — evidência: "especially important in experiments—like ours—that were not preregistered" (p. 6)
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "We examine voters’ responses to campaigning with four probits" (p. 15)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "Clustering by group instead of session, using linear models" (p. 6)
- **d6_q4_selecao_subgrupos** — resposta: N — evidência: "sample is all subject-rounds, excluding candidates, or all group-rounds" (p. 15)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado de d1a_q3 e d6_q1)

## Notas do codificador

**Resultado bundlado.** O item de `{RESULTADOS}` reúne duas colunas da Tabela 9 ("Election-Only" e "Message") sob o mesmo construto `apoio_ao_lider` (efeito bandwagon da parcela de votos do incumbente na prévia sobre o voto na eleição). As duas colunas foram localizadas no texto (p. 16) e nenhuma parte do resultado ficou sem correspondência.

**Domínio 1 (confundimento) — sobreposição do algoritmo.** 1.1=PY e 1.2=Y porque a variável mais plausivelmente confundidora neste desenho — a qualidade real do titular/desafiante (θ), que move tanto o resultado da prévia quanto o voto — é uma variável de desenho conhecida com certeza pelos autores (sorteada pelo software) e entra como controle nas regressões da Tabela 9 (nota de tabela, p. 16), embora seus coeficientes não sejam reportados no corpo do texto. 1.3=Y porque, na coluna "Message" (mas não na "Election-Only"), o modelo controla o conteúdo das mensagens de campanha, que são emitidas depois da prévia e podem mediar o próprio efeito bandwagon (ordem dos eventos: prévia anunciada antes das mensagens, p. 5). Pelo algoritmo estrito do ROBINS-I, 1.3=Y tende a levar a "grave"; propus "moderado" em vez disso porque (a) o problema só afeta a metade "Message" do resultado bundlado, não a "Election-Only"; e (b) o sinal do coeficiente bandwagon é qualitativamente o mesmo com e sem esses controles (comparando as duas colunas da Tabela 9), sugerindo que o ajuste não inverte nem distorce grosseiramente a estimativa. 1.4=N não tem trecho direto sobre controles negativos; usei como proxy indireta a nota de robustez da nota de rodapé 9 (p. 6), que mostra que os autores testaram especificações alternativas sem achar diferenças relevantes — isso é uma inferência minha, não uma resposta explícita dos autores sobre confundimento residual, e um humano pode preferir NI aqui.

**B3 e D2/D5 — evidência indireta.** Não há discussão explícita no texto sobre "adequação da medida do outcome" ou "quem avaliou o outcome": o voto é registrado automaticamente pelo software z-Tree (p. 5), sem avaliador humano. Usei essa característica de desenho como evidência para as respostas N em b3_medida_inadequada, d2_q4, d2_q5, d5_q1 e d5_q2. Um humano pode preferir tratar isso como NI se entender que o registro automatizado não responde diretamente à pergunta sobre mascaramento/adequação.

**Domínio 6 (não pré-registrado).** O texto declara explicitamente que o experimento "were not preregistered" (p. 6) e que nem todos os resultados relatados estão ligados a uma das seis hipóteses numeradas (H1–H6); o efeito bandwagon da Tabela 9 é apresentado como observação, não como teste de hipótese pré-especificada. Isso pesou para d6_q1=N e para propor "moderado" no domínio 6, mesmo sem evidência direta de fishing de medidas/subgrupos para este resultado específico (d6_q2, d6_q3, d6_q4 = PN/N).

**Confundidores do protocolo sem análogo claro.** `interesse_politico` e `preferencia_previa/partidarismo` são construtos do contexto de pesquisas eleitorais reais; este é um jogo de laboratório abstrato, sem partidos e com exposição universal e obrigatória à prévia (sem seleção por interesse). Codifiquei ambos como `sem_informacao` (não `nao_controlado`) porque os autores simplesmente não discutem a aplicabilidade desses construtos ao seu desenho, e não porque haja uma tentativa frustrada de controle.

**Cobertura de leitura.** Faixa única 1-19 (documento inteiro: introdução, teoria, procedimentos experimentais, todas as tabelas e figuras, discussão, limitações e lista de referências). Não há apêndice/material suplementar anexado a este PDF (o texto remete a um SI hospedado externamente, não incluído no arquivo).

## Linha final

OK Feltovich2022 robins_i: fichas=1 paginas=19 faixas=1-19 SI=0 NA_secao=5 propostas_gerais=moderado duvidas=1.3/1.4 no domínio 1 dependem de inferência indireta (mediador só na coluna Message; sem trecho direto sobre controles negativos); avaliador humano pode preferir NI em 1.4 ou grave no domínio 1 se discordar da leitura de robustez.
