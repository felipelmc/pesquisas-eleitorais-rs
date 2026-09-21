---
citekey: Freden2021
ficha_id: Freden2021
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Freden2021.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_106
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim, o documento traz o mesmo titulo do registro (How Polling Trends Influence Compensational Coalition-Voting), a mesma autora (Annika Fredén), o mesmo ano (2021) e o mesmo doi (10.3389/fpos.2021.598771) — evidência: "Compensational Coalition-Voting" (p. 1)
- **tipo_documento** — resposta: artigo, publicado como artigo de pesquisa original na revista Frontiers in Political Science (vol. 3, artigo 598771) — evidência: "ORIGINAL RESEARCH" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, a analise usa eleitores suecos de amostra representativa do eleitorado, com escolha de voto entre os sete principais partidos em oito eleicoes gerais reais (1988-2014) — evidência: "It consists of a representative sample of the Swedish electorate" (p. 4)
- **c2_intervencao_estudada** — resposta: Sim, a tendencia de pesquisa eleitoral (polling trend), construida a partir das sondagens de campanha do instituto Sifo comparadas ao resultado da eleicao anterior, e a exposicao analisada e a variavel explicativa central do modelo, e nao mero contexto ou fonte para medir intencao de voto — evidência: "is compared with election campaign opinion poll levels in order to measure" (p. 3)
- **c3_desfecho** — resposta: Sim, o desfecho e de voto: a variavel dependente e a escolha de partido declarada pelo eleitor; nao ha desfecho de comparecimento — evidência: "The outcome variable in the model is party choice (vote)" (p. 5)
- **c4_desenho_elegivel** — resposta: Não, o desenho e observacional, sem variacao identificada da exposicao: um mixed logit sobre survey pos-eleitoral repetido (SOM), em que a tendencia de pesquisas do partido desde a eleicao anterior e cruzada com a escolha de voto relatada apos a eleicao, sem aleatorizacao, sem experimento natural e sem painel individual com exposicao medida antes do desfecho — evidência: "To test the hypotheses using real life data, a mixed logit model" (p. 5); "reported vote choices, conducted shortly after the general elections" (p. 4)
- **c5_estudo_primario** — resposta: Sim, e estudo primario com analise propria: a autora combina tres bases (manifestos eleitorais, sondagens Sifo e o survey SOM) e estima os modelos — evidência: "three unique datasets are combined" (p. 3)
- **c6_nao_retratado** — resposta: Sim, nao ha marca, nota ou pagina de retratacao em nenhuma das 10 paginas do documento — evidência: "Compensational Coalition-Voting" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Combinacao de tres fontes sobre oito eleicoes gerais suecas de 1988 a 2014: codificacao de manifestos eleitorais (projeto do JMG/Universidade de Gotemburgo), sondagens de campanha do instituto Sifo (media das ultimas pesquisas cerca de um mes antes da eleicao) e o National SOM Survey Cumulative Dataset (survey postal representativo do eleitorado sueco, com voto relatado logo apos cada eleicao); mais de 9.000 individuos avaliando sete partidos, 64.306 observacoes no modelo — evidência: "investigated over eight general elections in the PR system of Sweden" (p. 2); "generating more than 64,000 observations in total" (p. 5)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginacao: a numeracao impressa no rodape coincide com o indice do PDF. Conferi em duas paginas distantes: a primeira pagina do corpo traz 1 no rodape e a ultima traz 10 (rodape "Frontiers in Political Science | www.frontiersin.org ... February 2021 | Volume 3 | Article 598771"). Logo, offset_pagina: 0. Li o PDF inteiro (paginas 1 a 10).
- c2 limitrofe entre Sim e parcial. Optei por Sim porque o resultado de pesquisa eleitoral e de fato a exposicao analisada (a tendencia de pesquisa entra como variavel explicativa central e nas interacoes de dois e tres termos do modelo), e nenhuma das situacoes de exclusao do prompt se aplica (a pesquisa nao aparece so como contexto, motivacao, fonte para medir intencao de voto, objeto de analise de precisao ou tema de cobertura). A ressalva relevante e que a exposicao e medida no nivel do partido-eleicao e nao ha variacao identificada nem medida individual da exposicao, o que e um problema de desenho e foi registrado em c4, nao em c2.
- c4 = Não pelo caso nomeado no proprio protocolo: tendencia de pesquisas comparada ao resultado, em estudo observacional sem variacao identificada da exposicao. O survey SOM e pos-eleitoral e repetido no tempo (nao e painel individual com exposicao medida antes do desfecho) e a tendencia de pesquisa e um atributo do partido naquele ano eleitoral. A checagem de robustez descrita (retirar um ano eleitoral por vez) nao introduz variacao exogena.
- c3: o desfecho e so de voto (escolha de partido). Nao ha medida de comparecimento nem de intencao de comparecer.
- outros_relatos_mesmo_estudo = 999: o documento cita Fredén (2014) e o material suplementar do proprio artigo, mas nao menciona outro relato (versao anterior, tese, working paper) do mesmo estudo. Fredén (2014) e citado como trabalho anterior distinto, sobre a eleicao sueca de 2010, e nao como outra versao deste estudo.
- registro_financiamento = 999: a secao FUNDING (p. 9) nao traz numero de processo, edital nem identificador de pre-registro, e nao ha mencao a OSF, AEA RCT Registry, RIDIE ou EGAP. A secao de disponibilidade de dados indica um repositorio de dados (SND), que nao e identificador de pre-registro nem de financiamento, por isso nao foi transcrito aqui.
- Evidencias escolhidas com trechos curtos e, sempre que havia alternativa, sem palavras com ligaduras tipograficas (ff, fi, fl). Em texto_confere e c6 o proprio codebook manda usar o titulo da primeira pagina: citei a segunda linha do titulo, que e contigua e nao tem ligadura, enquanto a primeira linha contem "Influence".
