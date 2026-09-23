---
citekey: Meffert2011
ficha_id: Meffert2011#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Meffert2011.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Meffert2011-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 33
faixas_lidas: 1-20,21-33
---

## 00_Resultado
- **unidade_randomizacao** — resposta: individual — evidência: "were randomly assigned to one of three poll conditions" (p. 12)
- **resultado_avaliado** — resposta: apoio_ao_lider: Tabela 4, coluna "With perceptions", regressão logística, coeficiente de "Close poll (manipulation)" — evidência: "Close poll (manipulation)" (p. 26)
- **efeito_de_interesse** — resposta: atribuicao — evidência: (metadados fornecidos pelo coordenador)

## D1b_Recrutamento_cluster
- **d1b_q1_identificados_antes** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_q2_recrutamento_afetado** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_q3_desequilibrio_participantes** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)
- **d1b_julgamento_proposto** — resposta: NA_secao — evidência: (classificador: unidade_randomizacao=individual)

## D1_Randomizacao
- **d1_q1_sequencia_aleatoria** — resposta: PS — evidência: "were randomly assigned to one of three poll conditions" (p. 12)
- **d1_q2_ocultacao** — resposta: SI — evidência: 999
- **d1_q3_desequilibrio_base** — resposta: SI — evidência: 999
- **d1_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 1.1 a 1.3)

## D2_Desvios_atribuicao
- **d2_q1_participantes_cientes** — resposta: N — evidência: "were unobtrusively manipulated" (p. 3)
- **d2_q2_executores_cientes** — resposta: SI — evidência: 999
- **d2_q3_desvios_contexto** — resposta: SI — evidência: 999
- **d2_q4_desvios_afetam** — resposta: NA — evidência: (fluxo: 2.3 = SI)
- **d2_q5_desvios_equilibrados** — resposta: NA — evidência: (fluxo: 2.4 = NA)
- **d2_q6_analise_apropriada** — resposta: S — evidência: "Close poll (manipulation)" (p. 26)
- **d2_q7_impacto_analise** — resposta: NA — evidência: (fluxo: 2.6 = S)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: S — evidência: "the analyses, only the 200 participants who were eligible" (p. 9)
- **d3_q2_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 3.1 = S)
- **d3_q3_faltante_pode_depender** — resposta: NA — evidência: (fluxo: 3.2 = NA)
- **d3_q4_faltante_provavelmente_depende** — resposta: NA — evidência: (fluxo: 3.3 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: N — evidência: "vote for a party other than the one ranked highest" (p. 25)
- **d4_q2_medida_diferiu** — resposta: N — evidência: "After the information search ended, participants were asked to vote" (p. 16)
- **d4_q3_avaliadores_cientes** — resposta: S — evidência: "All participants encountered and read this page before continuing" (p. 13)
- **d4_q4_avaliacao_influenciavel** — resposta: PS — evidência: "were unobtrusively manipulated" (p. 3)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: N — evidência: "including the manipulated and unobtrusively embedded polls and coalition signals" (p. 10)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: N — evidência: "not possible to conduct further in-depth analyses of this group" (p. 25)
- **d5_q3_selecao_analises** — resposta: N — evidência: "the model is reported with and without the perceptions" (p. 25)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Desenho: experimento de laboratório computadorizado (280 recrutados, 200 elegíveis analisados), com duas manipulações independentes por sujeito (condição de pesquisa eleitoral em 3 níveis, com probabilidades 20/50/30%; sinal de coalizão em 2 níveis, probabilidade igual), atribuídas aleatoriamente ao nível do participante ("Next, participants were randomly assigned to one of three poll conditions", p. 12; "The two signal conditions were assigned randomly with even probability", p. 13). Por isso `unidade_randomizacao = individual` e o bloco D1b (cluster) não se aplica (NA_secao).

Domínio 1: o texto declara aleatorização mas não descreve o mecanismo de geração da sequência (motivo do PS em 1.1, não S) nem discute explicitamente ocultação da alocação até a inclusão dos participantes, nem testa desequilíbrio de linha de base entre condições (1.2 e 1.3 = SI, sem trecho para presumir). Proposta `algumas_preocupacoes` por essa incerteza combinada, não por evidência de problema concreto.

Domínio 2: os participantes não sabiam que os números da pesquisa e os sinais de coalizão eram manipulados ("unobtrusively manipulated", p. 3; "unobtrusively embedded", p. 10), o que reduz o risco de desvios motivados pelo conhecimento da alocação (2.1 = N). Não há informação sobre se os experimentadores/software souberam a condição de cada participante de forma que pudesse alterar a entrega (2.2 = SI), o que aciona o fluxo para 2.3 (também SI, nenhum desvio de contexto relatado). A variável analisada (`Close poll (manipulation)`) é a própria condição atribuída, não uma medida de adesão/percepção, o que sustenta 2.6 = S (efeito da atribuição estimado diretamente). Proponho `baixo` sobrepondo o peso de 2.2/2.3 = SI: dado que a entrega da informação é automatizada por software e idêntica para todos os participantes de uma condição, não há mecanismo plausível de desvio contextual diferencial, mesmo sem declaração explícita; um avaliador humano pode preferir `algumas_preocupacoes` dado o SI em 2.2.

Domínio 3: a amostra analítica (200 de 280) é definida por critérios de elegibilidade prévios ao desfecho (direito de voto na Alemanha, participação prévia no piloto, perda técnica de dados de 6 participantes — nota 3, p. 29), não por perda diferencial ligada ao resultado ou à condição; não há relato de dados faltantes do desfecho dentro dos 200 analisados (a tarefa de voto final era obrigatória para concluir o estudo). Não encontrei tabela de atrito por braço.

Domínio 4: o desfecho é autorrelatado (decisão de voto final); o "avaliador" é o próprio participante, que necessariamente conheceu o conteúdo mostrado a ele (4.3 = S). Como a manipulação foi deliberadamente discreta ("unobtrusively"), a probabilidade de efeito de demanda do experimentador sobre a resposta é baixa (4.5 = N), sustentando `baixo`.

Domínio 5: não há declaração de pré-registro do plano de análise para este estudo (5.1 = SI). Os autores relatam explicitamente as duas especificações (com e sem percepções) lado a lado, justificando a escolha por transparência ("the model is reported with and without the perceptions", p. 25) e justificam a troca do desfecho "voto estratégico" (N=10, insuficiente) para "voto insincero" por razões de tamanho de amostra, não por resultado favorável ("not possible to conduct further in-depth analyses of this group", p. 25). Isso sustenta 5.2 = N e 5.3 = N e a proposta `baixo`.

Geral: pior domínio = D1 (`algumas_preocupacoes`); nenhum domínio alto; não agravei para `alto` por concentração em apenas um domínio. `direcao_vies_proposta = imprevisivel`: a incerteza em D1 é sobre ocultação/desequilíbrio não relatados, sem indício de para que lado puxaria o efeito.

Todos os dois resultados de {RESULTADOS} do despacho para esta chave/ferramenta referem-se ao mesmo coeficiente (Tabela 4, "With perceptions", "Close poll (manipulation)"); há apenas um resultado listado no despacho para Meffert2011|rob2, então uma única ficha foi suficiente.
