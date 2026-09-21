---
citekey: Gschwend2016
ficha_id: Gschwend2016
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Gschwend2016.pdf
paginacao: impressa
offset_pagina: -292
agente_fichador: fichador_el_129
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim, o título, o primeiro autor (Thomas Gschwend), o ano (2016) e o DOI impressos no documento batem com os metadados do registro — evidência: "What drives rental votes? How coalitions signals facilitate strategic coalition voting" (p. 293)
- **tipo_documento** — resposta: artigo, publicado no periódico Electoral Studies 44 (2016), páginas 293 a 306, com histórico de submissão e nota de copyright da Elsevier — evidência: "Contents lists available at ScienceDirect" (p. 293)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, analisa eleitores alemães aptos a votar (apoiadores da CDU) escolhendo entre partidos na eleição estadual da Baixa Saxônia e na eleição federal alemã de 2013 — evidência: "The target population was in both cases German citizens eligible to vote" (p. 299)
- **c2_intervencao_estudada** — resposta: Não, a exposição analisada são os sinais de coalizão emitidos pelos partidos na campanha (e, no nível individual, preferência de coalizão e expectativa sobre a FDP ultrapassar a cláusula de barreira); resultados de pesquisas eleitorais aparecem apenas como contexto descritivo da disputa, sem manipulação, variação natural identificada nem medida de exposição a pesquisas em painel — evidência: "Do coalition signals influence rental voting behavior?" (p. 295); "polling at around 40 percent in both cases" (p. 296)
- **c3_desfecho** — resposta: Sim, o desfecho é de voto: intenção/escolha de voto individual entre FDP, CDU e outros partidos, além dos resultados agregados das duas eleições; não há desfecho de comparecimento — evidência: "21 percent of CDU supporters intended to vote for the FDP" (p. 299); "on the probability to vote FDP rather than CDU" (p. 298)
- **c4_desenho_elegivel** — resposta: parcial, é uma comparação de dois casos em desenho de sistemas mais semelhantes ("qualitative identification strategy") combinada com modelo logit condicional sobre dois surveys transversais; não há aleatorização, painel individual nem variação exógena identificada da exposição nos moldes do protocolo (proibição, fuso, calendário, DiD, descontinuidade, série interrompida) — evidência: "Such a strategy is commonly known as a most-similar-systems design." (p. 295); "The data comes from an online survey conducted by Harris/Decima" (p. 299)
- **c5_estudo_primario** — resposta: Sim, estudo primário com análise própria de dados de survey do projeto Making Electoral Democracy Work — evidência: "Our data is taken from the Making Electoral Democracy Work" (p. 299)
- **c6_nao_retratado** — resposta: Sim, não há marca "RETRACTED", nota ou página de retratação no documento; a primeira página traz apenas o título, a filiação e a nota de copyright — evidência: "How coalitions signals facilitate strategic coalition voting" (p. 293)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Não cita versão anterior, tese, working paper, relatório técnico ou outro artigo com os mesmos dados; menciona apenas o apêndice suplementar online do próprio artigo (no DOI) e, nos agradecimentos, a apresentação do trabalho em encontros de 2014 — evidência: "An Appendix including descriptive statistics and further robustness checks" (p. 305)
- **fonte_dados_amostra** — resposta: Survey online do projeto Making Electoral Democracy Work (MEDW), aplicado pela Harris/Decima duas semanas antes de cada pleito a cidadãos alemães aptos a votar na Baixa Saxônia, com 1023 respondentes na eleição estadual da Baixa Saxônia (janeiro de 2013) e 1211 na eleição federal alemã (setembro de 2013) — evidência: "The sample for the state election contains 1023 respondents and 1211 respondents" (p. 299)
- **registro_financiamento** — resposta: Não há identificador de pré-registro (OSF, AEA, RIDIE, EGAP) nem número de processo ou edital; o documento apenas reconhece apoio financeiro do Social Sciences and Humanities Research Council of Canada, sem número — evidência: "from the Social Sciences and Humanities Research Council of Canada" (p. 305)

## Notas do codificador

**Paginação e offset.** O artigo é um separata de periódico com numeração impressa contínua de 293 a 306 em 14 páginas de PDF, logo `offset_pagina: -292` (impressa P → PDF 1-based = P − 292). Confirmado em páginas distantes: PDF 3 traz "295" no cabeçalho, PDF 7 traz "299", PDF 13 traz "305" e PDF 14 traz "306".

**Sobre a convenção (p. 0) informada pelo coordenador.** Ela não se aplica aqui e não foi usada. A primeira folha do PDF não é capa nem folha de rosto sem numeração: é a própria página impressa 293 do periódico (o cabeçalho traz "Electoral Studies 44 (2016) 293–306" e a página seguinte está numerada 294), de modo que título, resumo e nota de copyright têm número impresso. Além disso, com `offset_pagina: -292` a anotação (p. 0) apontaria para a página −292 do PDF, e não para a primeira folha, contrariando a própria finalidade da convenção e a regra de citar a numeração impressa verificada no cabeçalho. As evidências da primeira folha foram anotadas como (p. 293).

**c2 (Não).** O objeto empírico do artigo é o contraste entre sinais de coalizão consistentes (eleição estadual da Baixa Saxônia, janeiro de 2013) e inconsistentes (eleição federal, setembro de 2013) com a lógica do voto de aluguel, mais a preferência de coalizão CDU-FDP e a incerteza do eleitor quanto à FDP superar a cláusula de 5%. Pesquisas eleitorais aparecem só como pano de fundo (a FDP oscilando em torno dos 5%, a CDU em torno de 40%) e como relatório pós-eleitoral da Forschungsgruppe Wahlen (p. 296): não são manipuladas, não têm variação natural identificada e não são medidas como exposição individual em painel. A expectativa autorrelatada sobre a FDP entrar no parlamento é medida de viabilidade percebida em escala de 11 pontos, não exposição a um resultado de pesquisa.

**c4 (parcial).** Os autores chamam o desenho de "qualitative identification strategy" com seleção de casos em sistemas mais semelhantes, combinada a um modelo estatístico individual (logit condicional) sobre dois surveys transversais independentes (1023 e 1211 respondentes). Fica entre as categorias do protocolo: tem comparação de casos deliberadamente construída, mas sem aleatorização, sem painel individual e sem choque exógeno identificado sobre a exposição; por isso `parcial`, e não `Sim` nem `Não`. A decisão de elegibilidade final não depende dessa margem, já que c2 é `Não`.

**Sem 999.** Todas as variáveis foram respondidas a partir do documento; em `registro_financiamento` o que falta é o identificador numérico, mas o financiador está impresso e foi citado, então não se usou 999.
