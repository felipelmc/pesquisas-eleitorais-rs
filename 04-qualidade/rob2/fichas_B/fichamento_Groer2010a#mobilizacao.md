---
citekey: Groer2010a
ficha_id: Groer2010a#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Groer2010a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Groer2010a-rob2
data_fichamento: 2026-09-23
ferramenta: rob2
paginas_pdf: 35
faixas_lidas: 1-20,21-35
---

## 00_Resultado
- **unidade_randomizacao** — resposta: cluster — evidência: "three sessions (six electorates) per cell" (p. 9)
- **resultado_avaliado** — resposta: mobilizacao: ER1, teste de Wilcoxon-Mann-Whitney no nível do eleitorado, comparações IF-UF (só flutuantes) e IM-UM (mistos), Figura 2 — evidência: "Polls increase turnout levels by 22-28%." (p. 16)
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
- **d2_q1_participantes_cientes** — resposta: S — evidência: "were announced at the beginning of each round" (p. 10)
- **d2_q2_executores_cientes** — resposta: PS — evidência: "the online appendix for the read-aloud instructions" (p. 9)
- **d2_q3_desvios_contexto** — resposta: S — evidência: "one session had to be stopped after 94 rounds" (p. 10)
- **d2_q4_desvios_afetam** — resposta: SI — evidência: 999
- **d2_q5_desvios_equilibrados** — resposta: N — evidência: "one session had to be stopped after 94 rounds" (p. 10)
- **d2_q6_analise_apropriada** — resposta: S — evidência: "We have observations from 6 independent electorates per treatment." (p. 11)
- **d2_q7_impacto_analise** — resposta: NA — evidência: (fluxo: 2.6 = S)
- **d2_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado de 2.1 a 2.7)

## D3_Dados_faltantes
- **d3_q1_dados_completos** — resposta: S — evidência: "We have observations from 6 independent electorates per treatment." (p. 11)
- **d3_q2_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 3.1 = S)
- **d3_q3_faltante_pode_depender** — resposta: NA — evidência: (fluxo: 3.2 = NA)
- **d3_q4_faltante_provavelmente_depende** — resposta: NA — evidência: (fluxo: 3.3 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.4)

## D4_Mensuracao
- **d4_q1_metodo_inadequado** — resposta: N — evidência: "Each voter individually and privately decides between voting" (p. 6)
- **d4_q2_medida_diferiu** — resposta: N — evidência: "The experimental software was programmed using RatImage" (p. 9)
- **d4_q3_avaliadores_cientes** — resposta: S — evidência: "and knew her or his type right from the start" (p. 9)
- **d4_q4_avaliacao_influenciavel** — resposta: N — evidência: "binary choice between voting (= 1) and abstaining (= 0)" (p. 19)
- **d4_q5_avaliacao_provavelmente_influenciada** — resposta: NA — evidência: (fluxo: 4.4 = N)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.5)

## D5_Resultado_relatado
- **d5_q1_plano_previo** — resposta: SI — evidência: 999
- **d5_q2_selecao_medidas** — resposta: N — evidência: "turnout rates averaged over blocks of 20 rounds each" (p. 15)
- **d5_q3_selecao_analises** — resposta: N — evidência: "Many of our statistical tests are based on nonparametric statistics" (p. 15)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_algumas_preocupacoes — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Desenho: experimento de laboratório (participation game de Palfrey e Rosenthal), 288 estudantes em 12 sessões de 24 sujeitos; cada sessão dividida em 2 eleitorados de E=12 e o desenho 2×2 between-subject usa 3 sessões (6 eleitorados) por célula, ou seja, o eleitorado/sessão inteiro recebe uma única combinação de tratamento (informado/não informado × flutuante/misto) — por isso `unidade_randomizacao = cluster`, conforme a orientação do coordenador para eleitorados de 7 a 24 participantes.

D1b e D1: o texto descreve em detalhe apenas a randomização da composição dos grupos dentro do eleitorado a cada rodada (Steps 1 e 2, p. 8), mas não descreve em nenhum trecho como as sessões/eleitorados foram alocados às quatro células de tratamento (se por sorteio, ordem fixa etc.), nem se há desequilíbrio de linha de base entre participantes ou eleitorados. Por isso todas as perguntas de sequência, ocultação, desequilíbrio e recrutamento ficaram SI. Proponho `algumas_preocupacoes` em ambos os domínios por ausência de informação, sem indício concreto de alocação não aleatória.

D2: os sujeitos sabem seu tipo (aliado/flutuante) e a condição informada/não informada desde o início de cada rodada (p. 9-10), e o script de leitura em voz alta (online appendix) implica que quem conduz a sessão sabe a alocação (por isso `PS`, não `S`, no d2_q2). Houve um desvio real do protocolo pretendido por causa do ambiente do estudo: uma sessão foi interrompida na rodada 94 de 100 por pane do computador (nota 13, p. 10). O texto não diz se isso afetou o resultado (SI em 2.4), mas, por definição, esse desvio atingiu só uma das 12 sessões, não as demais, portanto não foi equilibrado entre os grupos (N em 2.5). A análise usa todos os 6 eleitorados independentes por tratamento (Tabela 1, p. 11), sem exclusão por não cumprimento — 2.6 = S, 2.7 = NA. Proponho `algumas_preocupacoes` pelo desvio real de magnitude incerta.

D3: turnout é registrado automaticamente pelo software a cada rodada; os 6 eleitorados por tratamento aparecem na análise (p. 11), incluindo a sessão truncada em 94 rodadas, então dados praticamente completos — proponho `baixo`.

D4: o desfecho (votar/abster) é uma decisão binária registrada diretamente pelo sistema computadorizado (RatImage, nota 12, p. 9; Tabela 2, p. 19), idêntico nos quatro tratamentos, sem avaliador humano separado sujeito a viés de aferição — proponho `baixo`. Marquei d4_q3 = S porque o "avaliador" do desfecho autorrelatado é o próprio participante, que sabe sua condição (mesma lógica de D2), mas classifiquei d4_q4 = N porque o registro do voto é automático e idêntico entre braços, não uma avaliação subjetiva sujeita a distorção pós-hoc; documento essa sobreposição do algoritmo aqui.

D5: não há registro de protocolo/plano de análise pré-especificado citado no artigo (SI em 5.1; trabalho de 2002/2007, período anterior à prática comum de pré-registro em economia experimental). A medida de turnout é única e consistente (médias por blocos de 20 rodadas, Figura 2) e os testes não paramétricos ao nível do eleitorado são anunciados como método padrão do artigo (p. 15), não parecem escolhidos a posteriori por resultado — proponho `baixo` apesar do SI em 5.1.

Geral: nenhum domínio chegou a `alto`; as preocupações em D1b, D1 e D2 vêm principalmente de lacunas de informação (não de indícios claros de viés), por isso não agravei para `alto`. Direção do viés `imprevisivel`: não há como prever o sentido do efeito das lacunas de alocação nem do desvio da sessão truncada.

Os dois resultados de {RESULTADOS} (comparações IF-UF e IM-UM do ER1) foram ambos localizados no mesmo trecho do artigo (Figura 2 e o parágrafo SUPPORT de ER1, p. 15-16) e tratados numa única ficha, já que o item do despacho os agrupa como um resultado (mobilizacao) com duas comparações internas.
