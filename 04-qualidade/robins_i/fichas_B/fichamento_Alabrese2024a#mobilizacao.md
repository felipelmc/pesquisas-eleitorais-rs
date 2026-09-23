---
citekey: Alabrese2024a
ficha_id: Alabrese2024a#mobilizacao
n_fichas_do_texto: 2
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Alabrese2024a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Alabrese2024a-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 69
faixas_lidas: 1-20,21-40,41-60,61-69
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: (classificação do avaliador: o modelo é uma especificação única por eleição/constituência, sem reclassificação de exposição ou modelagem de desvios de protocolo durante o seguimento; ver Notas)
- **resultado_avaliado** — resposta: Tabela 2; coluna 2: interação NationalPollmarginw1 × LocalSafetyt−1; EF distrito + EF região×ano; EP cluster distrito — evidência: "Table 2: The effect of national opinion poll margins interacted" (p. 30)
- **desenho_resultado** — resposta: painel_unidades_com_efeitos_fixos — evidência: "includes controls that vary by specification, such as constituency" (p. 23)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — os autores reconhecem que a especificação pode não excluir choques específicos de uma constituência numa dada eleição, mitigado só por evidência convergente de outros níveis de análise, não por controle direto ; interesse_politico: sem_informacao — nenhuma medida ou controle de interesse político é descrito no modelo agregado de turnout ; preferencia_previa: controlado — via LocalSafetyt−1 (margem eleitoral defasada entre Conservadores e Trabalhistas na constituência) e efeitos fixos de constituência, que absorvem o alinhamento partidário persistente da localidade — evidência: "specification may not entirely rule out the possibility that aggregate" (p. 24); "includes controls that vary by specification, such as constituency" (p. 23)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "includes controls that vary by specification, such as constituency" (p. 23)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: b1=Y)
- **b3_medida_inadequada** — resposta: N — evidência: "Turnout is the ratio between the total number of" (p. 30)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: WN — evidência: "specification may not entirely rule out the possibility that aggregate" (p. 24)
- **d1a_q2_medidos_validamente** — resposta: Y — evidência: "Data come from different sources. Electoral results" (p. 18)
- **d1a_q3_controlou_pos_intervencao** — resposta: N — evidência: "includes controls that vary by specification, such as constituency" (p. 23)
- **d1a_q4_controles_negativos** — resposta: N — evidência: (nenhum controle negativo ou análise de viés quantitativa reportada no texto)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1=a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Painel com efeitos fixos de constituência e ano/região×ano. Autores reportam robustez a diferentes combinações de EF ("coefficients remain largely unchanged"), mas nenhum teste formal de tendências prévias, balanceamento de covariáveis ou suporte comum é relatado. Ordem temporal (pesquisa e segurança local medidas antes do resultado) é usada como argumento contra causalidade reversa. — evidência: "coefficients remain largely unchanged when different fixed" (p. 29); "both national and local margins are measured before the vote" (p. 23)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 1.1 a 1.4 e qe_testes_pressupostos)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "both national and local margins are measured before the vote" (p. 23)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1=Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.1=Y)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "both national and local margins are measured before the vote" (p. 23)
- **d2_q5_outros_erros** — resposta: PY — evidência: "Take the example of Rasmussen, results suggest this polling" (p. 61)
- **d2_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: Y — evidência: "both national and local margins are measured before the vote" (p. 23)
- **d3_q2_eventos_excluidos** — resposta: N — evidência: (nenhuma exclusão de eventos iniciais após o início das estratégias é mencionada no texto)
- **d3_q3_selecao_pos_inicio** — resposta: PY — evidência: "where both a Conservative and a Labour candidate competed" (p. 13)
- **d3_q4_associadas_intervencao** — resposta: PY — evidência: "eliminates the constituencies of Northern Ireland (60 percent of" (p. 13)
- **d3_q5_influenciadas_outcome** — resposta: PN — evidência: "where both a Conservative and a Labour candidate competed" (p. 13)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1≠SN e 3.5≠Y/PY)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6=NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7=NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: PN — evidência: "5,599" (p. 28); "4,676" (p. 30)
- **d4_q2_outcome_completo** — resposta: PY — evidência: "Data come from different sources. Electoral results" (p. 18)
- **d4_q3_confundidores_completos** — resposta: PN — evidência: "5,599" (p. 28); "4,676" (p. 30)
- **d4_q4_casos_completos** — resposta: Y — evidência: (nenhuma menção a imputação; amostra reduzida indica análise de casos completos)
- **d4_q5_exclusao_relacionada** — resposta: PN — evidência: "Under the assumption that constituencies retaining the same name over" (p. 12)
- **d4_q6_explicada_modelo** — resposta: NA — evidência: (fluxo: 4.5≠Y/PY/NI)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4≠N/PN)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7=NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8=NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7≠N/PN/NI)
- **d4_q11_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: condição composta de 4.5/4.9/4.10 não satisfeita)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: N — evidência: "Turnout is the ratio between the total number of" (p. 30)
- **d5_q2_avaliadores_cientes** — resposta: PN — evidência: "Data come from different sources. Electoral results" (p. 18)
- **d5_q3_influenciada** — resposta: NA — evidência: (fluxo: 5.2≠Y/PY/NI)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: N — evidência: "Turnout is the ratio between the total number of" (p. 30)
- **d6_q3_selecao_analises** — resposta: PY — evidência: "results suggest that effects are particularly relevant to the" (p. 30)
- **d6_q4_selecao_subgrupos** — resposta: N — evidência: "Table 2: The effect of national opinion poll margins interacted" (p. 30)
- **d6_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado dos domínios 1 e 6, os piores; nenhum domínio grave ou crítico)
- **direcao_vies_proposta** — resposta: imprevisivel — evidência: (o texto não permite prever a direção do confundimento residual reconhecido na p. 24)

## Notas do codificador
Mesmo desenho de base da ficha #apoio_ao_lider: painel repetido de constituências do Reino Unido (1983-2017), NationalPollmargin (nível nacional-semana) interagido com LocalSafenesst−1 (defasada, nível constituência), com efeitos fixos de constituência e ano ou região×ano (Tabela 2, colunas pares usam região×ano, conforme "the even-numbered columns replace year dummies with region-by-year fixed effects", p. 24). variante_d1=a pelo mesmo motivo: não há reclassificação de exposição nem desvio de protocolo modelado durante o seguimento.

Domínio 1: mesma ressalva dos autores sobre confundimento residual agregado (p. 24), mitigada por eles através da análise de nível de partido e da análise de survey com exposição quase-aleatória (não avaliadas nesta ficha, que trata do resultado agregado de turnout). Codifiquei 1.1=WN pela mesma lógica de triangulação da outra ficha; sinalizo a mesma ressalva para arbitragem humana (um WN vs SN é discutível na ausência de testes formais de pressupostos).

Domínio 2: idêntico à outra ficha — variação sistemática entre casas de pesquisa (Tabela A.12) que compõe o NationalPollmargin médio introduz possível erro de mensuração não diferencial (2.5=PY), mas a exposição é sempre pré-resultado (2.4=N).

Domínio 3: mesmo critério de amostra (constituências com competição Conservador-Trabalhista em algum momento 1983-2017, excluindo Irlanda do Norte) discutido na outra ficha; julguei estrutural e não causado pelo turnout da eleição específica avaliada (3.5=PN).

Domínio 4: para este resultado o N cai de 5.599 (Tabela 1, colunas sem LocalSafetyt−1) para 4.676 (Tabela 2, com LocalSafetyt−1), a mesma perda de ~17% por ausência de eleição anterior comparável (mudança de fronteira/nome de constituência, nota de rodapé 10, p. 12). Sem menção a imputação (4.4=Y, casos completos).

Domínio 5: turnout é a razão entre votos válidos e eleitores aptos ("Turnout is the ratio between the total number of votes and the number of eligible voters of a constituency", nota da Tabela 2, p. 30), medida administrativa objetiva; mensuração e avaliador não dependem do conhecimento da exposição (5.1=N; 5.2=PN).

Domínio 6: mesma ausência de menção a plano de análise pré-registrado (6.1=NI) e mesma nota de rodapé 22 (p. 30) sobre um modelo conjunto de todas as semanas cujos resultados completos são apenas "available on request" (6.3=PY). Diferente da outra ficha, aqui o desfecho (turnout) tem uma única definição usada em todo o artigo e a Tabela 2 é a amostra completa (não um subgrupo), então codifiquei 6.2=N e 6.4=N em vez de PN.

O resultado despachado para esta ficha (mobilizacao) foi localizado sem dificuldade na Tabela 2 (p. 30), coluna 2, conforme descrito no despacho.
