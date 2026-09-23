---
citekey: Boukouras2020a
ficha_id: Boukouras2020a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Boukouras2020a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Boukouras2020a-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 62
faixas_lidas: 1-20,21-40,41-60,61-62
---

## 00_Resultado
- **unidade_randomizacao** — resposta: cluster — evidência: "participants being randomly allocated between the two" (p. 16)
- **resultado_avaliado** — resposta: apoio_ao_lider: Tabela VI, número de eleições vencidas por K vs. J em cada condição (E1, E2 e E3), teste exato de Fisher unilateral — evidência: "Number of elections won for each party in each treatment" (p. 50)
- **efeito_de_interesse** — resposta: atribuicao — evidência: (metadados fornecidos pelo coordenador)

## D1b_Recrutamento_cluster
- **d1b_q1_identificados_antes** — resposta: S — evidência: "each experimental block (of 30 subjects) to achieve perfect randomisation" (p. 16)
- **d1b_q2_recrutamento_afetado** — resposta: NA — evidência: (fluxo: 1b.1 = S)
- **d1b_q3_desequilibrio_participantes** — resposta: SI — evidência: 999
- **d1b_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 1b.1 a 1b.3)

## D1_Randomizacao
- **d1_q1_sequencia_aleatoria** — resposta: PS — evidência: "participants being randomly allocated between the two" (p. 16)
- **d1_q2_ocultacao** — resposta: SI — evidência: 999
- **d1_q3_desequilibrio_base** — resposta: SI — evidência: 999
- **d1_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 1.1 a 1.3)

## D2_Desvios_atribuicao
- **d2_q1_participantes_cientes** — resposta: S — evidência: "All participants will observe the fraction of votes" (p. 32)
- **d2_q2_executores_cientes** — resposta: S — evidência: "We programmed the experiments using O-tree" (p. 16)
- **d2_q3_desvios_contexto** — resposta: S — evidência: "were the only sessions of their block" (p. 16)
- **d2_q4_desvios_afetam** — resposta: SI — evidência: 999
- **d2_q5_desvios_equilibrados** — resposta: N — evidência: "four control sessions and five treatment sessions" (p. 15)
- **d2_q6_analise_apropriada** — resposta: S — evidência: "number of rounds won in the treatment condition" (p. 50)
- **d2_q7_impacto_analise** — resposta: NA — evidência: (fluxo: 2.6 = S)
- **d2_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: S — evidência: "eight 15-subject sessions (four control sessions and four treatment sessions)" (p. 15)
- **d3_q2_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 3.1 = S)
- **d3_q3_faltante_pode_depender** — resposta: NA — evidência: (fluxo: 3.1 = S)
- **d3_q4_faltante_provavelmente_depende** — resposta: NA — evidência: (fluxo: 3.1 = S)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: N — evidência: "simple majority, with ties broken by a 50-50 coin toss" (p. 15)
- **d4_q2_medida_diferiu** — resposta: N — evidência: "simple majority, with ties broken by a 50-50 coin toss" (p. 15)
- **d4_q3_avaliadores_cientes** — resposta: S — evidência: "We programmed the experiments using O-tree" (p. 16)
- **d4_q4_avaliacao_influenciavel** — resposta: N — evidência: "simple majority, with ties broken by a 50-50 coin toss" (p. 15)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: NA — evidência: (fluxo: 4.4 = N)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: N — evidência: "in terms of average vote share, candidate K performed better" (p. 5)
- **d5_q3_selecao_analises** — resposta: N — evidência: "number of rounds won in the treatment condition" (p. 50)
- **d5_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador

**Desenho.** Experimento de laboratório com três réplicas (E1, E2, E3), 15 participantes por sessão, 15 rodadas de eleição por sessão. Cada bloco de 30 sujeitos foi dividido em uma sessão-controle e uma sessão-tratamento, com alocação aleatória dos participantes entre as duas ("participants being randomly allocated between the two", p. 16). Como a condição (quais e quantas pesquisas são reveladas) é entregue à sessão inteira, e todos os 15 participantes de uma sessão compartilham a mesma condição em todas as rodadas, classifiquei `unidade_randomizacao = cluster` (sessão = cluster), seguindo a orientação do coordenador para desenhos de laboratório em que a sessão é a unidade. O resultado avaliado (Tabela VI) é o número de eleições vencidas por K vs. J, comparado por teste exato de Fisher unilateral, separadamente em E1 (controle: revela as 5 pesquisas; tratamento: revela só as 2 mais favoráveis a K), E2 (controle: 2 pesquisas aleatórias; tratamento: as 2 mais favoráveis a K) e E3 (repete E1, mas o tratamento informa a priori a regra de seleção). Tratei os três experimentos como um único resultado porque o item de RESULTADOS despachado os agrupa em uma única linha (E1/E2/E3 do mesmo construto `apoio_ao_lider`, mesma tabela e mesmo teste).

**Domínio 1b (cluster).** Os 30 sujeitos de cada bloco já estavam recrutados e presentes na sessão de laboratório antes de saber a qual das duas sub-sessões (controle/tratamento) seriam alocados (1b.1 = S). Não há relato de desequilíbrio de características entre participantes das duas sub-sessões (1b.3 = SI, o artigo não reporta nenhuma tabela de balanceamento de covariáveis dos sujeitos).

**Domínio 1.** O texto afirma "randomisation" e "randomly allocated", mas não descreve o mecanismo exato (sorteio manual, RNG do software oTree) nem se a sequência ficou oculta até a alocação — por isso 1.1 = PS (e não S) e 1.2 = SI. Não há tabela de balanceamento de linha de base entre sessões-controle e sessões-tratamento, então 1.3 = SI também. Proponho `algumas_preocupacoes` porque, apesar do componente aleatório declarado, a ocultação da sequência e o balanceamento de linha de base ficam sem informação (nem N/PN, que aliviaria o domínio).

**Domínio 2.** Participantes e pesquisadores sabem, por desenho, qual informação é mostrada em cada sessão (o software revela diretamente 2 ou 5 pesquisas na tela). Um desvio genuíno do plano de blocos ocorreu por restrição prática: a nota de rodapé 14 relata que três sessões (E1_C2, E1_T2, E3_T5) ficaram "as only sessions of their block" por falta de sujeitos ou capacidade de laboratório, e a nota de rodapé 13 confirma que E3 terminou com 4 sessões-controle e 5 sessões-tratamento (desbalanceado). Não há discussão explícita de impacto desse desbalanceamento sobre o resultado do teste de Fisher (2.4 = SI), mas o desvio em si não foi equilibrado entre os grupos (2.5 = N, mais sessões de tratamento do que de controle em E3). A análise (Tabela VI) compara diretamente os resultados por condição designada, sem exclusões pós-alocação, o que é apropriado para o efeito da atribuição (2.6 = S). Proponho `algumas_preocupacoes` pelo desbalanceamento de sessões sem avaliação expressa de impacto.

**Domínio 3.** Os totais de eleições em cada célula da Tabela VI (60 = 4 sessões × 15 rodadas em cada braço de E1 e E2; 60 no controle e 75 = 5 × 15 no tratamento de E3) fecham exatamente com o número de sessões e rodadas declarado no desenho, sem evidência de sessões ou rodadas perdidas para este resultado. `baixo`.

**Domínio 4.** O resultado (vitória eleitoral) é apurado mecanicamente por maioria simples, com sorteio de 50/50 em caso de empate, igual em todas as condições — método objetivo, não sujeito a viés de aferição diferencial entre braços. `baixo`.

**Domínio 5.** Não encontrei menção a pré-registro, plano de análise fechado antes da coleta ou repositório de protocolo para os experimentos de laboratório (5.1 = SI). O artigo reporta de forma transparente tanto a contagem de eleições vencidas (Tabela VI) quanto a diferença de vote share (Figuras IV, V, VIII, IX, XII, XIII) como medidas complementares, não como escolha seletiva entre medidas concorrentes (5.2 = N); e o teste de Fisher unilateral de Table VI é uma análise única e simples, sem indício de múltiplas especificações testadas e só a significativa reportada (5.3 = N). Proponho `algumas_preocupacoes` pela ausência de informação sobre pré-especificação, mesmo com 5.2 e 5.3 favoráveis.

**Geral.** Três domínios (1, 2 e 5) receberam `algumas_preocupacoes`, nenhum `alto`. Considerei agravar para `alto` pela quantidade de domínios com preocupação, mas as preocupações são todas de natureza semelhante (ausência de detalhe procedimental sobre ocultação/balanceamento/pré-registro em um experimento de laboratório altamente controlado e automatizado por software, não indícios concretos de viés atuante), e o efeito é reportado de forma consistente e robusta nas três réplicas (E1, E2, E3) com o mesmo sinal. Por isso mantive `algumas_preocupacoes` no geral, pelo pior domínio e sem indício de que as preocupações combinadas comprometam substancialmente a confiança no resultado. Direção do viés: `imprevisivel`, pois as lacunas de informação (ocultação da sequência, balanceamento, pré-registro) não apontam para um sentido previsível de distorção a favor de um dos braços.

**Resultados de RESULTADOS não encontrados.** Nenhum: a Tabela VI (p. 50) contém as três réplicas (E1, E2, E3) do resultado `apoio_ao_lider` despachado.
