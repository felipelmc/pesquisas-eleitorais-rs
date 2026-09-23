---
citekey: Unkelbach2022a
ficha_id: Unkelbach2022a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Unkelbach2022a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Unkelbach2022a-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 28
faixas_lidas: 1-20,21-28
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "RCS is a large-scale, cross-sectional survey based on phone" (p. 8)
- **resultado_avaliado** — resposta: Tabela 2 (p. 69 impressa), coluna SPD, modelo multinível principal (defasagem de 1 dia): CMVI (nível 2) e SES objetiva (nível 1) como preditores de intenção de voto, com interação CMVI×SES; mesma estimativa relatada no texto (p. 67 impressa) — evidência: "For the SPD, CMVI was positively associated with voting intention" (p. 17)
- **desenho_resultado** — resposta: experimento_natural — evidência: "the RCS data were matched with external data, namely" (p. 12)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — o modelo principal (Tabela 2) só inclui CMVI, SES objetiva e a interação entre os dois, sem qualquer ajuste para tendência de opinião compartilhada ; interesse_politico: nao_controlado — não entra no modelo principal; só é incluído numa checagem de robustez separada com covariáveis (que não é o resultado aqui avaliado) ; preferencia_previa/partidarismo: nao_controlado — idem, a identificação partidária só entra na checagem de robustez separada com covariáveis — evidência: "we included CMVI as a level 2 predictor and the index" (p. 14); "we included covariates (gender, age, general interest in politics" (p. 20)

## B_Triagem
- **b1_tentou_controlar** — resposta: N — evidência: "we included CMVI as a level 2 predictor and the index" (p. 14)
- **b2_confundimento_descarta** — resposta: PY — evidência: "voting intention was also associated with poll results published the day after" (p. 23)
- **b3_medida_inadequada** — resposta: N — evidência: "Individuals' voting intention was assessed by the single item" (p. 10)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: N — evidência: "we included CMVI as a level 2 predictor and the index" (p. 14)
- **d1a_q2_medidos_validamente** — resposta: NA — evidência: (fluxo: 1.1 = N)
- **d1a_q3_controlou_pos_intervencao** — resposta: NA — evidência: (fluxo: 1.1 = N)
- **d1a_q4_controles_negativos** — resposta: PY — evidência: "we did not find evidence for the assumed causality direction of a" (p. 23)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Não há teste formal de exogeneidade. Os autores só argumentam narrativamente que confundidores externos (eventos não medidos que afetassem simultaneamente os resultados de pesquisa e a intenção de voto) são pouco prováveis, com base em como os institutos coletam e publicam os dados em dias diferentes, e apresentam um DAG (Fig. 1) só para completude, sem testar seus pressupostos. A checagem de direção causal (comparando o efeito em t-1 e em t+1) não sustentou a direção temporal esperada para o bandwagon. — evidência: "unobserved confounders such as external events during the investigated time span could" (p. 9); "we did not find evidence for the assumed causality direction of a" (p. 23)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_critico — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "We matched each field day's RCS data with the results of" (p. 9)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = NA)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "We used data from the eight leading polling institutes in Germany" (p. 9)
- **d2_q5_outros_erros** — resposta: PY — evidência: "The published poll results, however, are not raw marginals." (p. 13)
- **d2_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: PY — evidência: "RCS is a large-scale, cross-sectional survey based on phone" (p. 8)
- **d3_q2_eventos_excluidos** — resposta: NI — evidência: 999
- **d3_q3_selecao_pos_inicio** — resposta: N — evidência: "We excluded participants whose postal codes indicated that they cast" (p. 13)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = N)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 ≠ SN e 3.5 ≠ Y/PY)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: Y — evidência: "In the event that no new polls were published on a" (p. 9)
- **d4_q2_outcome_completo** — resposta: Y — evidência: "we listwise excluded all cases with missing data on the" (p. 9)
- **d4_q3_confundidores_completos** — resposta: NI — evidência: 999
- **d4_q4_casos_completos** — resposta: Y — evidência: "We did not impute incomplete or missing data and instead used" (p. 13)
- **d4_q5_exclusao_relacionada** — resposta: PN — evidência: "reference category was defined as the voting intention for another political party" (p. 10)
- **d4_q6_explicada_modelo** — resposta: NA — evidência: (fluxo: 4.5 = PN)
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = Y)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: NA — evidência: (fluxo: 4.5 ≠ Y/PY/NI e 4.9/4.10 = NA)
- **d4_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: N — evidência: "Individuals' voting intention was assessed by the single item" (p. 10)
- **d5_q2_avaliadores_cientes** — resposta: Y — evidência: "the proportion of people who reported to have paid attention to such" (p. 2)
- **d5_q3_influenciada** — resposta: WY — evidência: "leads to individuals evaluating this attitude or object more positively" (p. 4)
- **d5_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: Y — evidência: "We preregistered all our analyses on the open science framework" (p. 8)
- **d6_q2_selecao_medidas** — resposta: N — evidência: "We preregistered all our analyses on the open science framework" (p. 8)
- **d6_q3_selecao_analises** — resposta: N — evidência: "We preregistered all our analyses on the open science framework" (p. 8)
- **d6_q4_selecao_subgrupos** — resposta: N — evidência: "We preregistered all our analyses on the open science framework" (p. 8)
- **d6_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_critico — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: afastado_do_nulo — evidência: (derivado dos domínios)

## Notas do codificador
Domínio 1 (o mais importante aqui): variante_d1 = a porque a RCS é transversal (cada respondente é entrevistado uma única vez; não há "seguimento" nem mudança de status de exposição dentro do indivíduo), então o efeito estimado é do tipo "intenção de tratar", sem confundimento variável no tempo dentro do sujeito. O modelo principal (Tabela 2, coluna SPD) não ajusta nenhum dos três confundidores do protocolo (apoio_latente, interesse_politico, preferencia_previa/partidarismo) — só entram numa checagem de robustez à parte (Seção 5.2, covariáveis), que não é o resultado aqui avaliado. Além de não controlado (d1a_q1 = N), há evidência do tipo "controle negativo": os próprios autores mostram que a intenção de voto também se associa com resultados de pesquisas publicados no dia seguinte (direção temporal invertida), e concluem explicitamente que isso "pode indicar que não há efeito bandwagon e que ambas as medidas simplesmente refletem... oscilações gerais da opinião pública" — ou seja, o próprio artigo não descarta que a associação SPD seja inteiramente devida a uma tendência de opinião compartilhada (apoio_latente), não a um efeito causal do CMVI. Isso levou a d1a_q4 = PY e a b2 = PY, e propus julgamento crítico para o Domínio 1 e geral. O algoritmo de "vários domínios moderados/graves agravam o geral" não foi necessário aqui porque o Domínio 1 já é crítico isoladamente e B2 = PY também aponta para crítico.

Classifiquei desenho_resultado como experimento_natural porque a "exposição" (CMVI, o resultado publicado de pesquisas eleitorais no dia anterior) é uma variável de nível 2 (dia de campo) que varia por razões externas ao desenho da pesquisa (o ritmo de publicação das pesquisas eleitorais), combinada com dados de nível 1 de uma survey transversal repetida — não se encaixa bem em nenhuma das outras categorias do codebook (não é coorte/painel de indivíduos, não é painel de unidades com efeitos fixos, não é pareamento, RDD, IV nem DiD de indivíduos). É uma classificação interpretativa; um humano pode preferir "outro".

Domínio 2: a classificação da "intervenção" (CMVI) vem de dados externos e objetivos (institutos de pesquisa), então não pode ser influenciada pelo outcome individual (d2_q4 = N). Mas os próprios autores revelam, em nota de rodapé, que os institutos aplicam procedimentos de transformação dos dados brutos que não são divulgados publicamente, o que é uma fonte plausível de erro de classificação não relacionado ao outcome (d2_q5 = PY) — daí o julgamento moderado.

Domínio 3: várias perguntas (3.2 em diante) foram desenhadas para estudos de coorte com seguimento ao longo do tempo e não se aplicam com nitidez a uma survey transversal de corte único por respondente. Respondi d3_q1 de forma interpretativa (PY, com base na natureza transversal do desenho, sem "tempo imortal" possível) e marquei d3_q2 como NI por não haver texto que discuta diretamente exclusão de eventos iniciais num desenho sem janela de seguimento. Um humano deveria revisar se essas perguntas realmente se aplicam a este desenho.

Domínio 4: a exclusão de casos por dados faltantes (d1a) foi por características de linha de base (escolaridade, situação de emprego) e por indecisos/não-votantes tratados como categoria de referência (não excluídos), não pelo valor real do outcome — por isso d4_q5 = PN. d4_q3 (confundidores completos) recebeu NI porque os confundidores do protocolo simplesmente não entram no modelo principal, então o texto não discute sua completude nesse modelo específico.

Domínio 5: a medida do outcome é autorrelatada e idêntica para todos os respondentes (não difere por grupo de exposição, d5_q1 = N), mas o mecanismo teórico do próprio estudo (conformidade/bandwagon) implica que o autorrelato de intenção de voto pode ser influenciado pelo conhecimento da opinião majoritária percebida — isso é conceitualmente inseparável do efeito de interesse, por isso d5_q3 = WY (impacto provavelmente não substancial no sentido de invalidar a medida, mas presente) e julgamento moderado.

Domínio 6: pré-registro no OSF e relato transparente dos seis partidos (incluindo resultados nulos) não mostram sinal de seleção de medidas, análises ou subgrupos pelo resultado.

Resultado de {RESULTADOS}: o único resultado (apoio_ao_lider | Tabela 2, coluna SPD) foi localizado sem problemas no texto (Tabela 2, p. 69 impressa / folha 19 do PDF) e no texto corrido (p. 67 impressa / folha 17 do PDF); os dois números conferem.

Nenhuma pergunta ficou sem revisão; todas as evidências citadas foram conferidas literalmente nas páginas indicadas (índice do PDF) antes de gravar esta ficha.
