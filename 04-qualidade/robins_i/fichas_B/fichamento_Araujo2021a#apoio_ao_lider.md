---
citekey: Araujo2021a
ficha_id: Araujo2021a#apoio_ao_lider
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Araujo2021a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Araujo2021a-robins_i
data_fichamento: 2026-09-23
ferramenta: robins_i
paginas_pdf: 20
faixas_lidas: 1-20
---

## 00_Resultado_e_preliminares
- **variante_d1** — resposta: a — evidência: "Treatment is a dummy that takes a value of 1" (p. 11)
- **resultado_avaliado** — resposta: apoio_ao_lider: Figura 2, Modelo 1 (frontrunner), OLS, primeiro turno; Figura 3, Modelo 1 (frontrunner), OLS, segundo turno — evidência: "support for the announced frontrunner is 5.69 pp higher" (p. 12); "Bolsonaro’s vote share increases by 11.76 pp in voting" (p. 14)
- **desenho_resultado** — resposta: experimento_natural — evidência: "in natural experiments, it is possible that certain" (p. 14); "Treatment is a dummy that takes a value of 1" (p. 11)
- **confundidores_controlados** — resposta: apoio_latente: nao_controlado — sem covariável de popularidade/apoio prévio na regressão principal, apenas verificação indireta com dados de 2014 ; interesse_politico: nao_controlado — sem variável de engajamento ou interesse político entre as covariáveis ; preferencia_previa_partidarismo: nao_controlado — sem covariável de partidarismo na regressão principal, apenas verificação indireta com votos de 2014 — evidência: "control for the characteristics of voters registered to cast ballots" (p. 12); "examine the electoral preferences of treated and untreated units" (p. 15)

## B_Triagem
- **b1_tentou_controlar** — resposta: Y — evidência: "control for the characteristics of voters registered to cast ballots" (p. 12)
- **b2_confundimento_descarta** — resposta: NA — evidência: (fluxo: b1 = Y)
- **b3_medida_inadequada** — resposta: N — evidência: "data are available for each round of the election for all" (p. 10)

## D1a_Confundimento_linha_de_base
- **d1a_q1_controlou_importantes** — resposta: WN — evidência: "there is no reason to believe that the occurrence of technical" (p. 11); "examine the electoral preferences of treated and untreated units" (p. 15)
- **d1a_q2_medidos_validamente** — resposta: Y — evidência: "control for the characteristics of voters registered to cast ballots" (p. 12)
- **d1a_q3_controlou_pos_intervencao** — resposta: PY — evidência: "we account for this by controlling for turnout rates" (p. 9)
- **d1a_q4_controles_negativos** — resposta: N — evidência: "our placebo treatment shows no indication of a bandwagon effect" (p. 16)

## D1b_Confundimento_variavel_no_tempo
- **d1b_q1_metodo_g** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q2_controlou_importantes** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q3_medidos_validamente** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q4_controle_inadequado** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)
- **d1b_q5_controles_negativos** — resposta: NA_secao — evidência: (fluxo: variante_d1 = a)

## D1_Quase_experimento
- **qe_testes_pressupostos** — resposta: Estudo trata o limiar de 19h como quase-aleatório entre máquinas de votação; não há teste formal de balanceamento de covariáveis no texto principal (remetido a apêndices online não disponíveis), mas há: (i) argumento de que a ocorrência de falhas técnicas é independente de atributos do eleitorado; (ii) teste de falsificação com a eleição de 2014, mostrando que as unidades tratadas em 2018 não eram previamente mais propensas a apoiar o líder; (iii) testes de placebo com unidades atrasadas mas não expostas à informação, sem efeito bandwagon; (iv) robustez a exclusão do Acre (sempre tratado) e a subamostras por tamanho de seção. — evidência: "in natural experiments, it is possible that certain" (p. 14); "examine the electoral preferences of treated and untreated units" (p. 15); "our placebo treatment shows no indication of a bandwagon effect" (p. 16); "The only difference comes from our analyses of the first" (p. 14)
- **qe_pressupostos_crediveis_proposta** — resposta: proposta_parcial — evidência: (derivado de qe_testes_pressupostos)
- **d1_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 1.1 a 1.4 e qe_*)

## D2_Classificacao_intervencoes
- **d2_q1_distinguiveis_inicio** — resposta: Y — evidência: "data also include the time of actual closure of each" (p. 11)
- **d2_q2_eventos_depois** — resposta: NA — evidência: (fluxo: 2.1 = Y)
- **d2_q3_analise_evitou** — resposta: NA — evidência: (fluxo: 2.2 = NA)
- **d2_q4_classificacao_influenciada** — resposta: N — evidência: "machines that remained open after preliminary results started being announced" (p. 11)
- **d2_q5_outros_erros** — resposta: PY — evidência: "it is virtually impossible to know whether the release" (p. 15)
- **d2_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 2.1 a 2.5)

## D3_Selecao_participantes
- **d3_q1_seguimento_inicio** — resposta: Y — evidência: "data are available for each round of the election for all" (p. 10)
- **d3_q2_eventos_excluidos** — resposta: N — evidência: "we code five different outcome variables" (p. 10)
- **d3_q3_selecao_pos_inicio** — resposta: PN — evidência: "Not all voting machines contained ballots cast for our five outcome variables" (p. 10)
- **d3_q4_associadas_intervencao** — resposta: NA — evidência: (fluxo: 3.3 = PN)
- **d3_q5_influenciadas_outcome** — resposta: NA — evidência: (fluxo: 3.4 = NA)
- **d3_q6_analise_corrigiu** — resposta: NA — evidência: (fluxo: 3.1 = Y e 3.5 = NA)
- **d3_q7_sensibilidade** — resposta: NA — evidência: (fluxo: 3.6 = NA)
- **d3_q8_graves_para_excluir** — resposta: NA — evidência: (fluxo: 3.7 = NA)
- **d3_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 3.1 a 3.8)

## D4_Dados_faltantes
- **d4_q1_intervencao_completa** — resposta: Y — evidência: "data are available for each round of the election for all" (p. 10)
- **d4_q2_outcome_completo** — resposta: PN — evidência: "Not all voting machines contained ballots cast for our five outcome variables" (p. 10)
- **d4_q3_confundidores_completos** — resposta: PY — evidência: "control for the characteristics of voters registered to cast ballots" (p. 12)
- **d4_q4_casos_completos** — resposta: Y — evidência: "hence the varying number of observations" (p. 10)
- **d4_q5_exclusao_relacionada** — resposta: NI — evidência: 999
- **d4_q6_explicada_modelo** — resposta: NI — evidência: 999
- **d4_q7_imputacao** — resposta: NA — evidência: (fluxo: 4.4 = Y)
- **d4_q8_mar_mcar** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q9_imputacao_apropriada** — resposta: NA — evidência: (fluxo: 4.8 = NA)
- **d4_q10_metodo_alternativo** — resposta: NA — evidência: (fluxo: 4.7 = NA)
- **d4_q11_evidencia_sem_vies** — resposta: NI — evidência: 999
- **d4_julgamento_proposto** — resposta: proposta_moderado — evidência: (derivado de 4.1 a 4.11)

## D5_Mensuracao_outcome
- **d5_q1_medida_diferiu** — resposta: N — evidência: "electronic voting machines means that electoral results are calculated speedily" (p. 7)
- **d5_q2_avaliadores_cientes** — resposta: N — evidência: "electronic voting machines means that electoral results are calculated speedily" (p. 7)
- **d5_q3_influenciada** — resposta: NA — evidência: (fluxo: 5.2 = N)
- **d5_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 5.1 a 5.3)

## D6_Resultado_relatado
- **d6_q1_plano_previo** — resposta: NI — evidência: 999
- **d6_q2_selecao_medidas** — resposta: N — evidência: "we code five different outcome variables" (p. 10)
- **d6_q3_selecao_analises** — resposta: PN — evidência: "Our results also remain stable in a series of robustness checks" (p. 14)
- **d6_q4_selecao_subgrupos** — resposta: PN — evidência: "The only difference comes from our analyses of the first" (p. 14)
- **d6_julgamento_proposto** — resposta: proposta_baixo — evidência: (derivado de 6.1 a 6.4)

## D9_Geral
- **geral_julgamento_proposto** — resposta: proposta_grave — evidência: (derivado dos domínios)
- **direcao_vies_proposta** — resposta: para_o_nulo — evidência: (derivado de 2.5 e confundidores_controlados)

## Notas do codificador
Desenho: experimento natural (falha técnica biométrica como fonte de variação quase-aleatória na exposição à informação eleitoral), com ajuste por covariáveis (OLS), não painel/efeitos fixos, não RDD, não IV/pareamento formal. Classifiquei `variante_d1 = a` porque o tratamento é definido de forma estática (fechamento da urna antes/depois de 19h), sem modelagem de mudanças de protocolo durante o seguimento; por isso D1b recebeu `NA_secao` inteiro.

Domínio 1 (D1a): nenhum dos três confundidores do protocolo (`apoio_latente`, `interesse_politico`, `preferencia_previa`/partidarismo) é medido ou incluído como covariável na regressão principal — os autores controlam apenas idade, escolaridade, % de mulheres, turnout, fuso horário, atraso de fechamento e % de erro de biometria. O argumento de identificação é de desenho (a ocorrência da falha técnica seria independente de atributos do eleitorado) mais um teste de falsificação com a eleição de 2014, que mostra as unidades tratadas em 2018 menos, e não mais, propensas ao candidato favorecido em 2018 — o que reduz a plausibilidade de confundimento por preferência política latente na direção do efeito encontrado. Por isso proponho `WN` em 1.1 (não controlado diretamente, mas o confundimento residual provavelmente não é substancial dada a verificação indireta) em vez de `SN`. Marquei `PY` em 1.3 porque a variável turnout, usada como covariável, é discutida pelos próprios autores como um canal potencialmente afetado pelo próprio tratamento (mecanismo de desmobilização, H1/H3), o que é uma preocupação de variável pós-intervenção/colisora, não de confundidor de linha de base puro. `d1_julgamento_proposto = moderado`: nem crítico, pois o teste de falsificação e os testes de placebo mitigam bastante a preocupação, nem baixo, pois os confundidores do protocolo seguem sem controle estatístico direto.

Domínio 2: a classificação do tratamento é objetiva (timestamp de fechamento da urna), então marquei `Y` em 2.1 e `N` em 2.4 (não há como o resultado do voto influenciar retroativamente o horário de fechamento da urna). Marquei `PY` em 2.5 porque os próprios autores reconhecem que não é possível saber se cada eleitor individual dentro de uma urna "tratada" de fato viu a informação antes de votar — há erro de classificação da exposição no nível individual dentro do nível de agregação (urna), provavelmente não diferencial.

Domínio 3: sem evidência de seleção de unidades com base em características pós-tratamento; a variação no N entre modelos (nota 13) decorre de urnas sem votos registrados para algum candidato/categoria, não de exclusão deliberada ligada ao tratamento.

Domínio 4: dados de tratamento (timestamp) parecem completos para as 454.490 urnas; dados de outcome têm N variável entre modelos (nota 13 do artigo), mas o texto não detalha se essa ausência se relaciona ao valor do outcome ou ao tratamento — por isso `NI` em 4.5, 4.6 e 4.11 em vez de arriscar um "não".

Domínio 5: outcome é a contagem oficial de votos por urna eletrônica, um registro administrativo automático e uniforme para unidades tratadas e não tratadas — sem avaliador humano sujeito a viés de expectativa.

Domínio 6: os cinco desfechos (Bolsonaro, Haddad, Gomes, brancos, nulos) são definidos a priori a partir das cinco hipóteses (H1–H5), não parecem escolhidos a posteriori. As checagens de robustez (exclusão do Acre, amostra restrita a urnas com falha registrada, subamostras por tamanho de seção) são reportadas de forma transparente, incluindo o único resultado discordante (Gomes ganhando votos nas menores seções no primeiro turno), o que reduz a suspeita de relato seletivo.

Direção do viés: propus `para_o_nulo` porque (i) o erro de classificação não diferencial da exposição individual (2.5) tende a atenuar o efeito estimado, e (ii) o teste de falsificação de 2014 indica que, se houvesse confundimento residual por preferência política latente, ele operaria contra o achado dos autores (unidades tratadas eram mais, não menos, favoráveis ao PT antes de 2018) — ambos os mecanismos apontam para uma possível subestimação, não sobrestimação, do efeito relatado.

Resultado de {RESULTADOS} localizado integralmente: Figura 2/Modelo 1 (primeiro turno, p. 12) e Figura 3/Modelo 1 (segundo turno, p. 14). Tratei os dois turnos como uma única ficha porque compartilham desenho, estratégia de identificação e covariáveis; se o consenso humano preferir fichas separadas por turno, a divisão é direta a partir desta ficha.

Todas as evidências foram confrontadas com o PDF extraído (pymupdf) página a página; evitei citar palavras com ligaduras tipográficas (ex.: "official", "efficient") quando havia alternativa no mesmo trecho.
