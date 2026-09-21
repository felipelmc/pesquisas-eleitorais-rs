---
citekey: Granzier2019
ficha_id: Granzier2019
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Granzier2019.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_103
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — título, autores e ano do documento batem com os metadados do registro (NBER Working Paper 26599, DOI 10.3386/w26599); o arquivo é a versão revista em janeiro de 2023 do mesmo working paper — evidência: "HOW PAST RANKINGS SHAPE THE BEHAVIOR OF VOTERS AND CANDIDATES" (p. 1)
- **tipo_documento** — resposta: working_paper — evidência: "NBER WORKING PAPER SERIES" (p. 2)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — analisa eleitores e candidatos em eleições reais francesas (locais e parlamentares) e unidades eleitorais agregadas (distritos, cantões, seções e municípios), com replicação em 19 outros países — evidência: "races in 26 French local and parliamentary elections from 1958 to 2017" (p. 4)
- **c2_intervencao_estudada** — resposta: Não — a exposição analisada é a colocação (ranking) do candidato no primeiro turno, ou seja, um resultado eleitoral anterior, e não o resultado de uma pesquisa eleitoral; pesquisas de opinião aparecem apenas como motivação e como fonte de coordenação mencionada na introdução — evidência: "a dummy equal to 1 if the candidate had a higher rank" (p. 16); "This paper shows that candidate rankings in past contests" (p. 47)
- **c3_desfecho** — resposta: Sim — mede votação agregada no segundo turno (parcela de votos do candidato e probabilidade de vencer), além da decisão de permanecer na disputa; o desfecho é de voto (comparecimento entra apenas como checagem descritiva e como teste de mobilização de não votantes) — evidência: "an increased vote share and likelihood of winning conditional on staying" (p. 23)
- **c4_desenho_elegivel** — resposta: Sim — quase-experimento de regressão descontínua (RDD) em eleições de dois turnos, comparando candidatos com votações quase idênticas no primeiro turno e ranqueados logo acima ou logo abaixo um do outro — evidência: "we use a regression discontinuity design (RDD) and compare the likelihood" (p. 5)
- **c5_estudo_primario** — resposta: Sim — estudo primário com coleta e análise próprias de resultados eleitorais oficiais, inclusive digitação de resultados de boletins impressos, gastos de campanha e artigos de jornal — evidência: "digitized results from printed booklets for the 1958 to 1988 parliamentary" (p. 13)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento — evidência: "COORDINATION AND BANDWAGON EFFECTS:" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim — o documento registra que circulou antes com outro título (The Large Effects of a Small Win: How Past Rankings Shape the Behavior of Voters and Candidates) e cita Pons e Tricaud (2018), Expressive Voting and Its Cost: Evidence from Runoffs with Two or Three Candidates, Econometrica, que usa um subconjunto das mesmas eleições francesas de dois turnos — evidência: "Previously circulated as" (p. 2); "a subset of French two-round elections used in the present paper" (p. 9)
- **fonte_dados_amostra** — resposta: Resultados eleitorais oficiais do Ministério do Interior francês e boletins impressos digitalizados de 26 eleições locais e parlamentares francesas de 1958 a 2017, com 22.557 disputas (16.222 locais e 6.335 parlamentares), mais uma amostra externa de 72 eleições parlamentares em 19 países desde 1850 (4.075 disputas); a análise por sub-distrito usa 475.501 resultados de seções ou municípios e a análise de imprensa, 76.679 artigos — evidência: "our sample comprises 16,222 races from local elections and 6,335 races" (p. 13); "a separate sample of 72 parliamentary elections in 19 countries since 1850" (p. 8)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador

**Paginação e offset.** O documento tem duas numerações impressas independentes, o que impede um único offset para toda a obra: o corpo do artigo é numerado de 1 a 52 nas páginas 4 a 55 do PDF (offset 3) e o Online Appendix recomeça em 1, indo até 102, nas páginas 56 a 157 do PDF (offset 55). Além disso, a capa, a folha de rosto da NBER e a página do resumo (páginas 1 a 3 do PDF) não têm número impresso, e o prompt de `c6_nao_retratado` exige como evidência o título na primeira página do documento. Por isso registrei `paginacao: indice-do-PDF` com `offset_pagina: 0` e todas as evidências citam o índice do PDF (1-based). As duas correspondências foram confirmadas em páginas distantes: a página do PDF 4 traz o número impresso 1 e a página do PDF 47 traz o número impresso 44 (corpo, offset 3); a página do PDF 56 traz o número impresso 1 do Online Appendix e a página do PDF 157 traz o número impresso 102 (apêndice, offset 55).

**Leitura.** Documento de 157 páginas, abaixo do limite de 300; foi lido por inteiro, em faixas de 20 páginas (1-20, 21-40, 41-60, 61-80, 81-100, 101-120, 121-140, 141-157).

**c2 (decisão limítrofe, a mais importante desta ficha).** O resumo e a introdução falam de colocações "in polls, previous elections, or a previous round of the same election", mas nenhuma análise empírica usa resultado de pesquisa eleitoral como exposição. A variável de tratamento é sempre a colocação do candidato no primeiro turno de uma eleição real de dois turnos, isto é, um resultado eleitoral anterior, que a convenção do protocolo manda classificar como `Não` ("também 'Não' para resultados de eleições passadas"). Os autores inclusive registram que pesquisas por distrito são raras nas eleições parlamentares francesas e inexistentes nas locais, o que reforça que pesquisa eleitoral não é a exposição analisada. As pesquisas aparecem apenas como motivação teórica, como referência a experimentos de laboratório de terceiros e na discussão de implicações para a regulação do setor de pesquisas.

**c3.** Os desfechos principais são a probabilidade de permanecer na disputa, a probabilidade de vencer e a parcela de votos no segundo turno, medidos no nível do candidato a partir de resultados agregados. O comparecimento aparece como gráfico descritivo (Figura A1) e no teste sobre mobilização de não votantes, mas não é desfecho de tratamento do estudo, por isso classifiquei o desfecho como de voto e não como ambos.

**c4.** O desenho é RDD com bandwidths MSERD, testes de placebo, teste de McCrary e testes de robustez, o que se encaixa em "quase-experimento com variação identificada da exposição (descontinuidade)" do protocolo. Note-se que a elegibilidade final do texto depende de `c2`, não de `c4`.

**texto_confere.** Respondi `Sim` e não `parcial` porque o registro é o próprio NBER Working Paper 26599 (DOI 10.3386/w26599): o PDF é esse working paper, apenas em sua revisão de janeiro de 2023. O título anterior de circulação ("The Large Effects of a Small Win") está registrado em `outros_relatos_mesmo_estudo`.

**registro_financiamento = 999.** Os agradecimentos da folha de rosto listam apenas pessoas, seminários e conferências, e trazem a ressalva usual da NBER; não há número de processo, edital, nem identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP) em nenhuma parte do documento, inclusive nos apêndices.

**Evidências.** Preferi trechos sem palavras com ligaduras tipográficas (ff, fi, fl), o que excluiu as formulações mais óbvias do texto, que usam "first", "effects", "difference", "official" e "qualify". Onde isso obrigou a um trecho menos direto, usei duas evidências curtas em vez de uma longa.
