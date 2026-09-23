---
citekey: Tyszler2015
ficha_id: Tyszler2015#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Tyszler2015.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Tyszler2015-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 33
faixas_lidas: 1-20,21-33
---

## 00_Resultado
- **unidade_randomizacao** — resposta: cluster — evidência: "value of the intermediate option is constant for a given electorate" (p. 15)
- **resultado_avaliado** — resposta: apoio_ao_lider: Figura 4, barras "Majoritarian Set" — comparação entre a condição "Low Importance (u=3), Uninformed" e a condição "Low Importance (u=3), Informed" (Tabela 1); desfecho contado é a fração de eleições em que o vencedor pertence ao Majoritarian Set — evidência: "Low Importance (u = 3), Uninformed" (p. 31); "Bars show for each treatment the fraction of election outcomes" (p. 28)
- **efeito_de_interesse** — resposta: atribuicao — evidência: (metadados fornecidos pelo coordenador)

## D1b_Recrutamento_cluster
- **d1b_q1_identificados_antes** — resposta: SI — evidência: 999
- **d1b_q2_recrutamento_afetado** — resposta: SI — evidência: 999
- **d1b_q3_desequilibrio_participantes** — resposta: SI — evidência: 999
- **d1b_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 1b.1 a 1b.3)

## D1_Randomizacao
- **d1_q1_sequencia_aleatoria** — resposta: SI — evidência: 999
- **d1_q2_ocultacao** — resposta: SI — evidência: 999
- **d1_q3_desequilibrio_base** — resposta: SI — evidência: 999
- **d1_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 1.1 a 1.3)

## D2_Desvios_atribuicao
- **d2_q1_participantes_cientes** — resposta: S — evidência: "participants know the aggregate induced preferences of all voters before casting their" (p. 15)
- **d2_q2_executores_cientes** — resposta: SI — evidência: 999
- **d2_q3_desvios_contexto** — resposta: SI — evidência: 999
- **d2_q4_desvios_afetam** — resposta: NA — evidência: (fluxo: 2.3 = SI)
- **d2_q5_desvios_equilibrados** — resposta: NA — evidência: (fluxo: 2.4 = NA)
- **d2_q6_analise_apropriada** — resposta: PS — evidência: "For each cell, we have observations from six electorates" (p. 15)
- **d2_q7_impacto_analise** — resposta: NA — evidência: (fluxo: 2.6 = PS)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: S — evidência: "For each cell, we have observations from six electorates" (p. 15)
- **d3_q2_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 3.1 = S)
- **d3_q3_faltante_pode_depender** — resposta: NA — evidência: (fluxo: 3.2 = NA)
- **d3_q4_faltante_provavelmente_depende** — resposta: NA — evidência: (fluxo: 3.3 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: N — evidência: "figure 4 shows, across treatments, the fraction of elections where the winner" (p. 16)
- **d4_q2_medida_diferiu** — resposta: N — evidência: "Plurality rule determines the winner, with ties broken by equal probability random" (p. 15)
- **d4_q3_avaliadores_cientes** — resposta: PN — evidência: "Plurality rule determines the winner, with ties broken by equal probability random" (p. 15)
- **d4_q4_avaliacao_influenciavel** — resposta: NA — evidência: (fluxo: 4.3 = PN)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: N — evidência: "Bars show for each treatment the fraction of election outcomes" (p. 28)
- **d5_q3_selecao_analises** — resposta: N — evidência: "we observe this 72-88% of the time with uninformed voters and 93-96%" (p. 22)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Desenho: experimento de laboratório comportamental (CREED/Universidade de Amsterdã, 2008), 12 sessões, 288 sujeitos, 24 eleitorados independentes de 12 votantes cada, cada eleitorado enfrentando 40 eleições. O desenho é 2x2 (valor da opção intermediária um=3/8 × informado/desinformado), "all variations were made across subjects" (p. 13, PDF 14), e "the value of the intermediate option is constant for a given electorate...according to the treatment" (p. 15): a condição é fixa para o eleitorado inteiro (12 votantes), não sorteada eleição a eleição. Por isso `unidade_randomizacao = cluster`: quem recebe o tratamento é o eleitorado/sessão como bloco, não cada votante individualmente (a randomização individual descrita no texto — "preferences are independently and randomly drawn", p. 6 — é sobre a ordem de preferência de cada votante em cada eleição, uma covariável do desenho, não o braço informado/desinformado que define o resultado do coordenador). O resultado do coordenador (Figura 4, p. 28) é a fração de eleições em que o vencedor pertence ao Majoritarian Set, comparando "Low Importance (u=3), Uninformed" vs. "Low Importance (u=3), Informed" (Tabela 1, p. 31).

D1b: o artigo não descreve como os 288 sujeitos foram recrutados nem se a identificação/inscrição dos participantes individuais ocorreu antes do sorteio de qual eleitorado seria alocado a qual dos quatro tratamentos (nenhuma menção a lista de inscrição, sorteio de sessões, ou comparação de covariáveis dos sujeitos entre eleitorados) — por isso 1b.1, 1b.2 e 1b.3 = SI (não presumo o procedimento). Sem qualquer informação sobre a lógica de recrutamento, não há como afastar `baixo`; proponho `algumas_preocupacoes`.

D1: o texto nunca descreve o mecanismo pelo qual os 24 eleitorados foram alocados aos quatro braços do desenho 2x2 — não há a palavra "random"/"randomly" associada à alocação de eleitorados a tratamentos em nenhum trecho do artigo (busquei "random", "assign" e "treatment" no texto inteiro); o único uso de "random" nesse contexto é para o desempate de eleições ("ties broken by an equal probability random draw", p. 6) e para o sorteio da ordem de preferência de cada votante a cada eleição (p. 6-7), não para a alocação de eleitorados a condições. Por isso 1.1 = SI, não PS: não há nem uma declaração vaga ("nós randomizamos") a que aplicar a regra de "aleatorizamos sem descrição tende a PS" — simplesmente não há menção alguma ao procedimento de alocação das sessões aos tratamentos. Consequentemente 1.2 (ocultação da sequência) também é SI, e 1.3 (desequilíbrio de linha de base entre eleitorados nas quatro condições) é SI: o artigo não relata qualquer comparação de covariáveis dos eleitorados/sujeitos entre os quatro braços. Com os três itens SI, não há como propor `baixo`; como também não há indício concreto de um problema real (ex.: alocação por conveniência declarada), não proponho `alto`. Proponho `algumas_preocupacoes`, registrando que um revisor humano pode considerar que a ausência total de descrição da alocação (não apenas da ocultação) é mais grave do que uma "preocupação" típica e prefira `alto` — é uma decisão de julgamento humano.

D2: os sujeitos necessariamente sabem em qual condição estão (a própria manipulação é a informação mostrada a eles: "participants know the aggregate induced preferences of all voters before casting their", p. 15, para os tratamentos informados; nos desinformados, sabem que não recebem essa informação) — por isso 2.1 = S. Isso é constitutivo do desenho (a exposição do protocolo É a informação mostrada), não uma falha de mascaramento evitável; registro essa ressalva para o julgamento humano, como fiz para outros textos com desfecho comportamental incentivado. Não há descrição de "executores" humanos distintos dos sujeitos (o experimento é computadorizado via z-Tree, sem intervenção humana diferencial por sessão relatada) — 2.2 = SI, o que aciona 2.3 (SI, nenhum desvio de protocolo relatado), deixando 2.4 e 2.5 em NA pelo fluxo. Quanto a 2.6, o texto relata que cada uma das quatro células manteve as seis unidades de eleitorado planejadas ("For each cell, we have observations from six electorates", p. 15) e que a Figura 4 usa os desfechos de todas as eleições de todos os eleitorados de cada tratamento (nenhuma exclusão de eleitorado ou de eleição mencionada); isso é indício forte, mas indireto (não uma declaração explícita de "usamos ITT"), de que a análise incluiu os eleitorados conforme alocados — por isso 2.6 = PS, não S, o que deixa 2.7 em NA pelo fluxo. Proponho `baixo` para o domínio 2: a "consciência da condição" é inerente ao objeto de estudo, não uma fonte de desvio de protocolo, e não há indício de exclusão pós-alocação.

D3: o desenho planejado (seis eleitorados por célula, quatro células = 24 eleitorados, 288 sujeitos) é exatamente o que é reportado como observado ("For each cell, we have observations from six electorates", p. 15), sem menção de perda de eleitorados, sujeitos ou eleições — 3.1 = S. O fluxo (3.2 só se 3.1 = N/PN/SI) deixa 3.2-3.4 em NA. Proponho `baixo`.

D4: o desfecho do coordenador (fração de eleições cujo vencedor está no Majoritarian Set) é calculado mecanicamente a partir dos votos registrados pelo sistema, segundo uma regra fixa e idêntica em todos os tratamentos ("Plurality rule determines the winner, with ties broken by equal probability random", p. 15) — não há instrumento subjetivo nem qualquer diferença de procedimento de apuração entre os braços, sustentando 4.1 = N e 4.2 = N. Isso aciona 4.3: como a apuração é automática e determinada por uma regra matemática fixa sobre os votos (não há um avaliador humano que julgue o resultado), a "consciência da intervenção pelo avaliador" não é diretamente aplicável no sentido usual do domínio; respondo PN (não declarado explicitamente que "não há avaliador humano", mas fortemente implícito pelo desenho computadorizado e pela regra de decisão mecânica), o que deixa 4.4 e 4.5 em NA pelo fluxo. Proponho `baixo`: um desfecho de contagem de votos apurado por regra fixa e automática é pouco suscetível a viés de mensuração diferencial entre braços.

D5: o artigo (2015, working paper/journal de economia experimental) não menciona qualquer plano de análise pré-registrado — 5.1 = SI, sem presumir ausência. Não há indício de seleção do desfecho entre medidas alternativas: a Figura 4 relata tanto "Majoritarian Set" quanto "Majoritarian Candidate" para as quatro células do desenho de forma uniforme ("Bars show for each treatment the fraction of election outcomes", p. 28), não apenas o recorte mais favorável — 5.2 = N. Também não há indício de seleção entre análises alternativas: o texto relata a faixa completa observada nas quatro condições, incluindo a variação entre elas ("we observe this 72-88% of the time with uninformed voters and 93-96%", p. 22), em vez de reportar apenas o resultado mais forte — 5.3 = N. Como 5.2 e 5.3 são N, proponho `baixo`, mesmo com 5.1 = SI (mesma lógica adotada para textos anteriores desta revisão).

Geral: nenhum domínio foi classificado como `alto`, mas dois domínios ligados à alocação dos eleitorados aos tratamentos (D1b e D1) ficaram em `algumas_preocupacoes` por ausência total de descrição do mecanismo de alocação das sessões/eleitorados às quatro condições — o artigo nunca usa a palavra "random" associada a essa alocação, apenas ao desempate de eleições e ao sorteio da ordem de preferência dentro de cada eleição. Proponho `algumas_preocupacoes` para o geral, sinalizando que um avaliador humano pode entender que a combinação de dois domínios de alocação sem qualquer informação justifica `alto` — é uma escolha de julgamento que deixo para a arbitragem humana. `direcao_vies_proposta = imprevisivel`: a ausência de descrição do mecanismo de alocação não indica, por si, se o viés (se existir) favoreceria a condição informada ou desinformada.

O PDF (33 páginas, incluindo referências, notas e as sete figuras/tabelas numeradas antes da lista de apêndices online) não traz apêndice ou material suplementar anexado ao arquivo (apenas um link para material suplementar hospedado externamente, p. 32); os apêndices A-H citados no texto (QRE, MLC, instruções experimentais etc.) não estão neste arquivo. O resultado de {RESULTADOS} (Figura 4, braço um=3, informado vs. desinformado) foi localizado na Seção 4.1 (texto, p. 16) e na própria Figura 4 (p. 28), com a definição das condições na Tabela 1 (p. 31).
