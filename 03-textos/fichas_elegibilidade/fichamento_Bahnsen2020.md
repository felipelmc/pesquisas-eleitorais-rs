---
citekey: Bahnsen2020
ficha_id: Bahnsen2020
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Bahnsen2020.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_141
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial; o título e os três autores batem com os metadados do registro, mas o arquivo é a versão preprint submetida à Elsevier, e não a versão publicada em Electoral Studies — evidência: "How Do Coalition Signals Shape Voting Behavior?" (p. 1); "Preprint submitted to Elsevier" (p. 1)
- **tipo_documento** — resposta: preprint; o próprio rodapé de todas as páginas declara tratar-se de preprint submetido à editora — evidência: "Preprint submitted to Elsevier" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, são eleitores suecos respondendo a um survey experiment durante a campanha da eleição geral de 2018, que informam sua propensidade de voto nos partidos — evidência: "In total, 1,907 respondents participated in our survey experiment" (p. 7); "Swedish voters are familiar with coalition signals" (p. 6)
- **c2_intervencao_estudada** — resposta: Não, a exposição manipulada é uma vinheta de sinal de coalizão (declaração partidária sobre a coalizão que pretende formar), não um resultado de pesquisa eleitoral; as pesquisas de opinião aparecem apenas como contexto da eleição de 2018 — evidência: "respondents were exposed to the following coalition signal vignettes" (p. 7); "all major opinion polls suggested that neither the left nor" (p. 6)
- **c3_desfecho** — resposta: Sim, o desfecho é de voto: a propensidade declarada de votar em cada partido, medida em escala de 1 a 7 após a vinheta; não há medida de comparecimento — evidência: "the respondents indicated their propensity to vote" (p. 8); "How likely is it that you will vote for the following parties?" (p. 10)
- **c4_desenho_elegivel** — resposta: Sim, é um experimento aleatorizado embutido em survey, com quatro grupos de tratamento e um grupo de controle — evidência: "respondents were randomly assigned to one of four treatment groups" (p. 7)
- **c5_estudo_primario** — resposta: Sim, é estudo primário: os autores conduziram o próprio survey experiment e analisam os dados coletados — evidência: "We conducted a coalition vignette survey experiment" (p. 2)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação em nenhuma das 32 páginas do documento — evidência: "How Do Coalition Signals Shape Voting Behavior?" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: survey experiment online no painel do Laboratory of Opinion Research (LORE) da Universidade de Gotemburgo, aplicado durante a campanha da eleição geral sueca de 2018, entre 12 de junho e 6 de agosto, com 1.907 respondentes (em média 381 por grupo experimental) — evidência: "during the 2018 Swedish election campaign between June 12 and August 6" (p. 7); "In total, 1,907 respondents participated in our survey experiment" (p. 7)
- **registro_financiamento** — resposta: projeto financiado pela German Research Foundation (DFG), processo GS 17/8-1; apoio adicional do GESS (Universidade de Mannheim) e do MZES; nenhum identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP) é citado no documento — evidência: "a research project (grant GS 17/8-1)" (p. 1); "funded by the German Research Foundation (DFG)" (p. 1)

## Notas do codificador
- Paginação: o rodapé de todas as páginas traz "Page N of 32", com N igual ao índice da folha do PDF (conferido nas folhas 1, 6, 7, 8, 10, 17 e 32). Logo, `paginacao: impressa` e `offset_pagina: 0`; todas as citações foram reabertas na folha do PDF indicada pela fórmula folha = página anotada + 0.
- `texto_confere` = parcial, e não Sim, porque o PDF é a versão preprint submetida à Elsevier (rodapé em todas as páginas), enquanto o registro aponta para o artigo publicado em Electoral Studies (DOI 10.1016/j.electstud.2020.102166). Título e autoria coincidem.
- `c2` é o critério que falha. O tratamento é uma vinheta de sinal de coalizão atribuída ao acaso, cujo texto diz que "there is a high probability of this party joining a coalition government with [signaled coalition partners] after the election" (p. 7), atribuída a "political observers" e não a pesquisas eleitorais. Pesquisas de opinião aparecem só como pano de fundo da eleição de 2018 (p. 6) e, em nota de rodapé, como uma das fontes que informam expectativas de coalizão (p. 4) — em nenhum momento como exposição analisada. Os artigos de Fredén (2017) e Stoetzer e Orlowski (2019), que tratam de pesquisas eleitorais, são apenas referências citadas.
- `c1`, `c3`, `c4` e `c5` são atendidos: eleitores reais em campanha real, desfecho de propensidade de voto (PTV), desenho experimental aleatorizado (teste de aleatorização no Apêndice B, p. 20) e dados próprios. Mantidos como Sim por instrução do codebook, que manda responder os demais critérios normalmente mesmo quando um deles falha.
- `outros_relatos_mesmo_estudo` = 999: o documento não cita versão anterior, tese, working paper ou relatório técnico com os mesmos dados. A única pista de outra versão é o rodapé "Preprint submitted to Elsevier", já registrado em `tipo_documento` e em `texto_confere`; como não há referência a um relato identificável, não o tratei como menção, para não inferir.
- Documento lido por inteiro (folhas 1 a 32, incluindo os apêndices A a K), em duas faixas de 16 páginas.
