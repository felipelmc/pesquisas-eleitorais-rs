---
citekey: Brugarolas2021
ficha_id: Brugarolas2021#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Brugarolas2021.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Brugarolas2021-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 8
faixas_lidas: 1-8
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "we cannot test this assumption empirically and our estimates could be" (p. 4); "intention to treat (ITT)" (p. 4)
- **resultado_avaliado** — resposta: mobilizacao: Seção 3.2 Main Result, diferença de médias da intenção de comparecer entre entrevistados depois (tratados) e antes (controles) da divulgação do Poll 1 na janela [-0.8, 0.8] dias; ATE = 5,1 pontos (IC [2.0, 9.0]) — evidência: "turnout intention by 5.1% (CI: [2.0,9.0])." (p. 6); "we select the window [-0.8, 0.8] for our main analysis" (p. 4)
- **desenho_resultado** — resposta: regressao_descontinua — evidência: "We impose a sharp RD design" (p. 2); "use a local randomization approach to regression discontinuity" (p. 2)
- **confundidores_controlados** — resposta: apoio_latente: controlado pelo desenho, janela estreita de 0,8 dia de cada lado do corte, anterior ao início da campanha, e cortes placebo sem efeito, embora não haja medida direta ; interesse_politico: nao_controlado, balanço testado só em sexo, idade e tamanho do município (variáveis de cota) ; preferencia_previa / partidarismo: nao_controlado, não entra nos testes de balanço nem no ajuste — evidência: "our predetermined covariates (gender, age, and town size) are balanced in" (p. 4); "gender, age, and town size quotas" (p. 2); "for any of the possible windows for any of the three placebos" (p. 6)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "use a local randomization approach to regression discontinuity" (p. 2); "the selection of the control and treatment groups was not random" (p. 2)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: B1 = Y)
- **b3_medida_inadequada** — resposta: PN — evidência: "turnout intention, defined as the proportion of people who said they" (p. 2); "turnout intention measured using a survey item in a" (p. 2)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: WN — evidência: "our predetermined covariates (gender, age, and town size) are balanced in" (p. 4); "the selection of the control and treatment groups was not random" (p. 2)
- **d1a_q2_medidos_validamente** — resposta: PY — evidência: "gender, age, and town size quotas" (p. 2)
- **d1a_q3_controlou_pos_intervencao** — resposta: N — evidência: "average observed outcomes of all units in the treatment and control" (p. 3)
- **d1a_q4_controles_negativos** — resposta: N — evidência: "for any of the possible windows for any of the three placebos" (p. 6); "on the outcome variable is not significant for any window" (p. 6)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: RDD de randomização local com variável de corrida discreta (dia e faixa horária da entrevista). Valores de cada lado do corte: 4 pontos de massa de cada lado na janela principal. Continuidade de covariáveis: testes de balanço (Hotelling) em sexo, idade e tamanho do município, com p > 0,05 em todas as janelas menores que [-1, 1]; a janela [-0.8, 0.8] foi escolhida por procedimento automático de seleção de janela. Forma funcional: diferença de médias dentro da janela (funções planas). Banda: sensibilidade em 13 janelas, ATE de 3,4% a 5,1%. Donut: exclusão da faixa 12:05-14:00 do dia da divulgação; exclusão do dia inteiro no SI (Tabela A6, não anexada ao PDF). Cortes placebo (26/3, 2/4, 10/4) sem efeito. Teste de manipulação ou densidade no corte: não relatado. Balanço em interesse político ou partidarismo: não relatado — evidência: "is above 0.05 for all windows smaller than [-1, 1]" (p. 4); "four time intervals (mass points) before and" (p. 4); "the ATE in the 13 windows reported in Table A2" (p. 6); "We removed all observations from this interval following the" (p. 3)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "the treatment status changes on 9 April at 2:05 p.m." (p. 3)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "the day and time of the interview define" (p. 2)
- **d2_q5_outros_erros** — resposta: PN — evidência: "We removed all observations from this interval following the" (p. 3); "we cannot test this assumption empirically and our estimates could be" (p. 4)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: PY — evidência: "compare the responses of people who participated in" (p. 2)
- **d3_q2_eventos_excluidos** — resposta: Y — evidência: "We removed all observations from this interval following the" (p. 3)
- **d3_q3_selecao_pos_inicio** — resposta: PN — evidência: "was generated through randomly-chosen sampling" (p. 2)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = PN)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = PY e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: PY — evidência: "the variation in the time at which each interview was conducted" (p. 3)
- **d4_q2_outcome_completo** — resposta: PY — evidência: "turnout intention, defined as the proportion of people who said they" (p. 2)
- **d4_q3_confundidores_completos** — resposta: PY — evidência: "gender, age, and town size quotas" (p. 2)
- **d4_q4_casos_completos** — resposta: NA — evidência: (fluxo: 4.1, 4.2 e 4.3 = PY)
- **d4_q5_exclusao_relacionada** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q6_explicada_modelo** — resposta: NA — evidência: (fluxo: 4.5 = NA)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = NA)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 4.1, 4.2 e 4.3 = PY)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: PN — evidência: "turnout intention measured using a survey item in a" (p. 2)
- **d5_q2_avaliadores_cientes** — resposta: PY — evidência: "suggests that most people interviewed in" (p. 4); "were aware of the national election forecast" (p. 4)
- **d5_q3_influenciada** — resposta: WY — evidência: "the social desirability of turnout intention questions increases." (p. 6)
- **d5_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: PN — evidência: "Our outcome variable is turnout intention" (p. 2)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "we used the automatic data-driven window selection procedure" (p. 4); "the ATE in the 13 windows reported in Table A2" (p. 6)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "average observed outcomes of all units in the treatment and control" (p. 3)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (derivado dos domínios)

## Notas do codificador
Resultado: o único resultado despachado (mobilizacao, Seção 3.2, janela [-0.8, 0.8]) foi localizado nas p. 5-6 do PDF (Figura 2 e texto do Main Result). O PDF tem 8 folhas (7 de artigo e 1 de aviso de copyright); o SI Appendix (Tabelas A2-A6, Seção 1) não está anexado, então o que se diz dele vem só do texto principal.

Variante do domínio 1: a. A comparação é entre entrevistados antes e depois da divulgação, sem desvios ou trocas durante o seguimento; os próprios autores leem a estimativa como efeito de intenção de tratar (exposição à divulgação não medida).

D1 (proposta_moderado): 1.1 = WN porque o balanço só foi testado em sexo, idade e tamanho do município, que são as variáveis de cota da amostra (e por isso tendem a sair balanceadas por construção); interesse político, partidarismo e a geografia do campo em cada dia (rotas aleatórias podem cobrir áreas diferentes em dias diferentes) não foram testados. Não marquei SN porque a janela é curta (8/4 14:05 a 10/4 12:00, antes da campanha), cobre os mesmos tipos de faixa horária dos dois lados e os três cortes placebo não mostram descontinuidade, o que torna improvável um confundimento substancial. 1.2 = PY (variáveis de cota registradas pelo CIS), 1.3 = N (diferença simples de médias, sem ajuste por variáveis pós-intervenção), 1.4 = N (placebos nulos). Pelo algoritmo, 1.1 = WN leva a moderado. Pressupostos do RDD: parcial, porque não há teste de manipulação/densidade no corte (a variável de corrida é o horário da entrevista, marcado pelo campo do CIS, o que limita manipulação pelo respondente, mas o texto não discute) nem balanço em covariáveis políticas. Ponto para os humanos: possível não resposta diferencial depois da divulgação (a notícia sobre o CIS pode ter mudado quem aceita responder); o texto não traz taxas de resposta.

D2 (proposta_baixo): status definido pelo horário da entrevista, anterior ao desfecho (2.4 = N). A faixa ambígua 12:05-14:00 do dia 9/4 foi excluída (donut). 2.5 = PN: a exposição efetiva à pesquisa não foi medida, mas isso muda a interpretação para ITT da divulgação, que é a exposição do protocolo (pesquisa publicada/divulgada), e não uma classificação errada do tratamento atribuído.

D3 (proposta_moderado): 3.2 = Y porque o donut exclui respostas dadas entre 12:30 e 14:00 do dia da divulgação, isto é, eventos logo após o início da intervenção. Apliquei o algoritmo (exclusão de eventos iniciais leva a moderado). Os humanos podem rebaixar para baixo: a exclusão é por ambiguidade do status, não por característica ligada ao desfecho, e o texto diz que a exclusão do dia inteiro (Tabela A6 do SI, não anexada) mantém os resultados. Se houver viés, o sentido provável é para o nulo, já que os autores dizem que o efeito decai com o tempo. 3.3 = PN: a amostra vem de pontos de amostragem aleatórios com cotas, e a restrição à janela é por horário de entrevista.

D4 (proposta_baixo): 4.2 = PY é inferência: o desfecho é definido como proporção dos entrevistados que disseram que votariam, o que sugere denominador com todos os entrevistados. O texto não informa como "não sabe/não responde" foi tratado; vale confirmar com os autores ou nos dados de replicação (Harvard Dataverse). Se houver perda relevante no item, 4.2 passaria a NI e o domínio a moderado.

D5 (proposta_moderado): desfecho autodeclarado (intenção de comparecer) medido pelo mesmo item do survey nos dois grupos (5.1 = PN). Quem avalia o desfecho é o próprio respondente, e os autores sustentam que a maioria dos entrevistados depois da divulgação conhecia a previsão (5.2 = PY). 5.3 = WY: a nota 8 levanta como explicação alternativa que, depois de ver a pesquisa, aumenta a desejabilidade social de declarar intenção de votar; isso afeta a declaração, não necessariamente a mobilização. Marquei WY e não SY porque os autores tratam isso como hipótese especulativa e não há como dimensionar pelo texto; os humanos podem preferir SY (grave). Os autores também admitem que efeitos sobre intenção tendem a ser maiores que sobre comparecimento real.

D6 (proposta_moderado): nenhum plano de análise prévio ou pré-registro é mencionado (6.1 = NI; pedir aos autores). Há um só desfecho (6.2 = PN). A janela principal foi escolhida por procedimento automático de balanço, e 13 janelas são relatadas no SI (6.3 = PN); nota: a estimativa principal (5,1%) coincide com o limite superior da faixa de 3,4% a 5,1%, o que os humanos podem pesar. Nenhum subgrupo é relatado (6.4 = PN). Pelo algoritmo, 6.1 NI com 6.2-6.4 N/PN leva a moderado.

Geral (proposta_grave): o pior domínio é moderado (D1, D3, D5, D6). A regra do codebook manda agravar para grave quando há vários moderados, e há quatro; apliquei a regra. Sobreposição que os humanos podem considerar: manter proposta_moderado, se julgarem que D3 é baixo (donut com robustez relatada) e que as preocupações de D1 e D6 são pequenas diante do desenho de RD com placebos nulos. Direção do viés: imprevisivel (D5 puxaria para longe do nulo, D3 para o nulo, D1 sem sentido previsível).
