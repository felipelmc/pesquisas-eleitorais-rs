---
citekey: Tal2015a
ficha_id: Tal2015a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Tal2015a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Tal2015a-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 9
faixas_lidas: 1-9
---

## 00_Resultado
- **unidade_randomizacao** — resposta: individual — evidência: "the subject was assigned a random preference order over the candidates" (p. 5)
- **resultado_avaliado** — resposta: apoio_ao_lider — Fig. 5 e Fig. 6 (condição n = 1.009 eleitores, grupo C): proporção de votos para qi/q'i quando o candidato preferido do eleitor lidera vs. é o segundo colocado na pesquisa (Fig. 5), e quando q'i lidera vs. é o segundo colocado, dado que qi está em último na pesquisa (Fig. 6) — evidência: "Voting behavior for 1,009 voters" (p. 6); "candidate qi is ranked last in the poll" (p. 7)
- **efeito_de_interesse** — resposta: atribuicao — evidência: (metadados fornecidos pelo coordenador)

## D1b_Recrutamento_cluster
- **d1b_q1_identificados_antes** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_q2_recrutamento_afetado** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_q3_desequilibrio_participantes** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_julgamento_proposto** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)

## D1_Randomizacao
- **d1_q1_sequencia_aleatoria** — resposta: PS — evidência: "the subject was assigned a random preference order over the candidates" (p. 5)
- **d1_q2_ocultacao** — resposta: SI — evidência: 999
- **d1_q3_desequilibrio_base** — resposta: SI — evidência: 999
- **d1_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 1.1 a 1.3)

## D2_Desvios_atribuicao
- **d2_q1_participantes_cientes** — resposta: S — evidência: "presented in the voting bar to the left of each candidate" (p. 4)
- **d2_q2_executores_cientes** — resposta: SI — evidência: 999
- **d2_q3_desvios_contexto** — resposta: SI — evidência: 999
- **d2_q4_desvios_afetam** — resposta: NA — evidência: (fluxo: 2.3 = SI)
- **d2_q5_desvios_equilibrados** — resposta: NA — evidência: (fluxo: 2.4 = NA)
- **d2_q6_analise_apropriada** — resposta: N — evidência: "we focused our analysis on group C" (p. 6)
- **d2_q7_impacto_analise** — resposta: S — evidência: "Since group B behaved in a completely predictable way" (p. 6)
- **d2_julgamento_proposto** — resposta: proposta_alto — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: PS — evidência: "We collected at least 10 game instances for any combination of poll" (p. 5)
- **d3_q2_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 3.1 = PS)
- **d3_q3_faltante_pode_depender** — resposta: NA — evidência: (fluxo: 3.2 = NA)
- **d3_q4_faltante_provavelmente_depende** — resposta: NA — evidência: (fluxo: 3.3 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: N — evidência: "each participant to vote (only once) for one of the" (p. 3)
- **d4_q2_medida_diferiu** — resposta: N — evidência: "For every instance of the game, a poll was generated using" (p. 4)
- **d4_q3_avaliadores_cientes** — resposta: S — evidência: "presented in the voting bar to the left of each candidate" (p. 4)
- **d4_q4_avaliacao_influenciavel** — resposta: PS — evidência: "The reward to the subject was determined solely by the winning" (p. 5)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: PN — evidência: "in contrast to our first hypothesis, about 5% of votes were cast" (p. 5)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: N — evidência: "neither of these correlations was statistically significant, and thus the effect" (p. 6)
- **d5_q3_selecao_analises** — resposta: N — evidência: "As for the sixth hypothesis, we observed very similar qualitative and" (p. 6)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_alto — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Desenho: experimento comportamental online (AAMAS 2015), sem pré-registro declarado, com dois jogos de votação. O resultado do coordenador (Fig. 5 e Fig. 6) vem do primeiro jogo ("poll-voting game"): um único sujeito humano vota uma vez, após ver uma pesquisa pré-eleitoral não vinculante, entre três candidatos com ranking de preferência privado. Cada sujeito jogou até 20 instâncias em sequência com o mesmo n; a cada instância, o sorteio da configuração da pesquisa (entre 12 combinações de "gap-leader"/"gap-last") e a ordem de preferência do sujeito sobre os candidatos foram atribuídos aleatoriamente ("Each game sampled a random poll configuration from the 12 configurations...In addition, the subject was assigned a random preference order over the candidates", p. 5). Por isso classifiquei `unidade_randomizacao = individual`: é o sujeito (em cada instância de jogo) que é sorteado para uma configuração/ordem de preferência, não um cluster de participantes. O item do coordenador reúne dois recortes do mesmo jogo (n = 1.009, grupo C): Fig. 5 (qi líder vs. segundo colocado na pesquisa) e Fig. 6 (q'i líder vs. segundo colocado, dado qi em último); ambos localizados no mesmo corpo de resultados da Seção 5.1 (p. 6-7), com o mesmo procedimento experimental, por isso optei por uma única ficha.

D1: a atribuição aleatória é declarada ("random preference order", "random poll configuration", p. 5) mas sem qualquer detalhe do mecanismo de geração do acaso (gerador de números aleatórios, algoritmo de sorteio) — por isso 1.1 = PS, não S ("aleatorizamos sem descrição" tende a PS). Não há nenhuma menção a como a sequência foi ocultada até a inclusão do sujeito na instância do jogo (1.2 = SI). Diferente do caso de um ensaio entre grupos paralelos, aqui não há uma comparação de linha de base entre "grupo pesquisa-líder" e "grupo pesquisa-segundo-colocado" relatada no texto (o mesmo conjunto de sujeitos passa por várias condições ao longo das 20 instâncias); o texto não discute explicitamente comparabilidade de covariáveis entre condições, então 1.3 = SI (sem informação, não presumo balanceamento). Com 1.2 e 1.3 ambos SI, pelo algoritmo do RoB 2 a ausência de informação sobre ocultação e sobre desequilíbrio já impede "baixo"; proponho `algumas_preocupacoes`, sem indício concreto de problema que justifique "alto".

D2: os sujeitos veem diretamente sua própria condição na interface do jogo — a pesquisa é mostrada nas barras de votação ao lado de cada candidato ("presented in the voting bar to the left of each candidate", p. 4) — portanto 2.1 = S; não há mascaramento possível nesse tipo de jogo online de decisão única. Não há "executor" humano descrito (sistema automatizado), então 2.2 = SI, o que aciona 2.3 (também SI, nenhum desvio de contexto relatado), deixando 2.4 e 2.5 em NA pelo fluxo. O ponto crítico do domínio é 2.6: os autores relatam explicitamente que restringiram toda a análise da Seção 5.1 (inclusive as Fig. 5 e 6, que são o próprio resultado do coordenador) a um subconjunto comportamentalmente definido dos sujeitos — "we focused our analysis on group C" (p. 6) — excluindo o "grupo A" (sujeitos que votam quase aleatoriamente) e o "grupo B" (sujeitos que sempre votam no candidato preferido, "Since group B behaved in a completely predictable way", p. 6). Essa exclusão não é feita pela condição sorteada (pesquisa/ordem de preferência), mas por um padrão de comportamento observado ao longo do próprio estudo — o equivalente, nesse desenho, a uma análise que não segue a atribuição (não é "intenção de tratar"): por isso 2.6 = N. Como o grupo B vota deterministicamente no candidato preferido (o que infla artificialmente a proporção de "voto no preferido" quando ele lidera e a proporção de voto "fiel" quando ele não lidera) e o grupo A vota quase ao acaso, excluir os dois é capaz de alterar substancialmente os percentuais relatados nas Fig. 5 e 6 em relação ao que se observaria com todos os sujeitos atribuídos — por isso 2.7 = S. Diferença de análise não alinhada à atribuição, com impacto provavelmente substancial: proponho `alto` para o domínio 2, o domínio que também determina o geral.

D3: o texto não relata perdas de participantes ou de instâncias de jogo; ao contrário, o desenho de coleta buscava garantir dados completos por combinação de parâmetros — "We collected at least 10 game instances for any combination of poll parameters" (p. 5) — o que é indício indireto forte, mas não uma declaração explícita de que não houve nenhuma perda a nível de sujeito/instância; por isso 3.1 = PS, não S. O fluxo (3.2 só se 3.1 = N/PN/SI) deixa 3.2-3.4 em NA. Proponho `baixo`.

D4: o desfecho (Fig. 5/6) é o próprio voto registrado pelo sistema — uma ação comportamental direta, não uma escala autorrelatada separada da ação —, medido do mesmo modo em todas as condições ("each participant to vote (only once) for one of the", p. 4; "For every instance of the game, a poll was generated using", p. 4), sustentando 4.1 = N e 4.2 = N. Isso aciona 4.3: o "avaliador" do desfecho é o próprio participante, que necessariamente vê sua própria pesquisa antes de votar ("presented in the voting bar to the left of each candidate", p. 4), portanto 4.3 = S, acionando 4.4. Seguindo a orientação do coordenador para desfecho autodeclarado/autoexecutado em experimento com vinheta (domínio 4: participante sabia da manipulação e desfecho suscetível a demanda do experimentador): como o pagamento do sujeito dependia diretamente do resultado da eleição e de sua própria estratégia diante da pesquisa que via ("The reward to the subject was determined solely by the winning", p. 5), há possibilidade de que o conhecimento da condição influencie a ação registrada (4.4 = PS). Quanto a 4.5, os próprios achados dos autores mostram desvios da expectativa teórica dos autores (ex.: sujeitos votando no candidato menos preferido, uma ação dominada) — "in contrast to our first hypothesis, about 5% of votes were cast" (p. 5) — o que indica que os sujeitos não estavam simplesmente adivinhando/atendendo a uma hipótese do experimentador, sustentando 4.5 = PN. O algoritmo (4.1/4.2 = N, 4.5 = PN) leva a `baixo`; note-se que, para um desfecho comportamental incentivado financeiramente (não uma escala de opinião), a "influência" de conhecer a própria condição é o próprio mecanismo em estudo (comportamento estratégico), não necessariamente um viés de mensuração — registro isso para o julgamento humano avaliar se concorda com essa distinção.

D5: o artigo (AAMAS 2015) não menciona qualquer plano de análise pré-registrado ou finalizado antes do acesso aos dados (SI, não presumo ausência; apenas não há informação), 5.1 = SI. Não há indício de seleção do desfecho entre medidas alternativas: os autores relatam explicitamente correlações não significativas e resultados "inconclusivos" em vez de omiti-los — "neither of these correlations was statistically significant, and thus the effect" (p. 6) — sustentando 5.2 = N. Também relatam de forma transparente que os padrões nas outras duas condições de n (103 e 10.007) foram similares aos de n = 1.009, sem indício de terem escolhido reportar apenas a condição mais favorável — "As for the sixth hypothesis, we observed very similar qualitative and" (p. 6) — sustentando 5.3 = N. Como 5.2 e 5.3 são N (nenhum indício direto de seleção), proponho `baixo` para o domínio, mesmo com 5.1 = SI, registrando que um avaliador humano pode divergir dado que a ausência de pré-registro, por si, é uma fragilidade da literatura de 2015 em geral.

Geral: o domínio 2 (`alto`, pela exclusão pós-atribuição dos grupos A e B de toda a análise relatada neste resultado, sem análise de sensibilidade incluindo-os) determina o julgamento geral proposto, `alto`, independentemente de D1 (`algumas_preocupacoes`) e dos demais domínios (`baixo`). `direcao_vies_proposta = imprevisivel`: o texto não permite prever se a exclusão dos grupos A/B infla ou reduz a proporção de "voto no líder"/"herding" relatada — depende da distribuição de cada grupo entre as condições de Fig. 5 e 6, que não é discriminada no texto.

O PDF de 9 páginas (Proceedings do AAMAS 2015) não traz material suplementar anexado; não há apêndice ou dados complementares fora do corpo do artigo. Os dois recortes de {RESULTADOS} (Fig. 5 e Fig. 6) foram ambos localizados, na Seção 5.1 ("Individual behavior under polls"), p. 6-7.
