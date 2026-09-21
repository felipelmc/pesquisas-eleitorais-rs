---
citekey: Dahlgaard2015b
ficha_id: Dahlgaard2015b
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Dahlgaard2015b.pdf
paginacao: impressa
offset_pagina: -4
agente_fichador: fichador_el_110
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — o título e os autores do documento batem com os metadados do registro (o documento grafa o segundo autor como "Jonas H. Hansen", e o registro como "Jonas Hedegaard Hansen"); é o artigo publicado em politica, 47(1), 2015, p. 5-23 — evidência: "på danskernes stemmeadfærd og sympati for partierne" (p. 5)
- **tipo_documento** — resposta: artigo — evidência: "I denne artikel undersøger vi, om meningsmålingerne påvirker vælgerne" (p. 5)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, a amostra é de eleitores dinamarqueses de 18 a 74 anos, questionados sobre em que partido votariam — evidência: "e-mailinvitationer til danske statsborgere mellem 18-74 år" (p. 9); "udsnit af vælgerne mellem 18 og 74 år" (p. 9)
- **c2_intervencao_estudada** — resposta: Sim, o resultado de pesquisa eleitoral é manipulado experimentalmente em notícias fictícias que mostram o partido subindo ou caindo pontos percentuais na medição — evidência: "Socialdemokraterne gået 5 procentpoint frem i artiklen" (p. 11); "Respondenterne er tilfældigt blevet inddelt i fem grupper" (p. 9)
- **c3_desfecho** — resposta: Sim, desfecho de voto (intenção de voto no partido, além de simpatia e probabilidade de votar no partido); não há medida de comparecimento — evidência: "hvilket parti de ville stemme på, hvis der var valg i morgen" (p. 10)
- **c4_desenho_elegivel** — resposta: Sim, survey experiment online com alocação aleatória a quatro grupos de estímulo e um grupo de controle, analisado por comparação entre os grupos experimentais — evidência: "Konkret anvender vi et survey-eksperiment med 3.011 respondenter" (p. 6); "Analysen er en række simple sammenligninger af de eksperimentelle grupper" (p. 12)
- **c5_estudo_primario** — resposta: Sim, é estudo primário: os autores coletaram e analisaram os próprios dados do experimento de janeiro de 2014 — evidência: "blev gennemført i perioden 10.-28. januar 2014" (p. 9)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação no documento — evidência: "danskernes stemmeadfærd og sympati for partierne" (p. 5)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim, o documento informa que os dados já haviam sido usados no working paper/relatório Dahlgaard, Hansen, Hansen e Larsen (2014), "Hvordan påvirkes vælgerne af meningsmålinger?: Rapport om effekten af meningsmålinger på danskernes stemmeadfærd og sympati for partierne", Institut for Statskundskab, Københavns Universitet — evidência: "Data er tidligere anvendt i arbejdspapiret Dahlgaard et al. (2014)" (p. 22)
- **fonte_dados_amostra** — resposta: Survey experiment online no painel de internet da YouGov com eleitores dinamarqueses de 18 a 74 anos, campo de 10 a 28 de janeiro de 2014, com 3.011 respondentes que completaram o questionário — evidência: "onlinesurvey i YouGovs internetpanel" (p. 9); "hvoraf 3.011 respondenter har gennemført hele undersøgelsen" (p. 9)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: o PDF tem 19 páginas e reproduz as páginas impressas 5 a 23 do periódico. O offset foi confirmado em duas páginas distantes: a página 1 do PDF traz o rodapé impresso "5" e o cabeçalho "politica, 47. årg. nr. 1 2015, 5-23", e a página 18 do PDF traz o rodapé impresso "22". Logo, impressa P → PDF (1-based) = P − 4, ou seja, offset_pagina = -4. Todas as evidências usam a numeração impressa.
- texto_confere = Sim (e não "parcial"): título, quatro autores e ano conferem com o registro; a única diferença é a abreviação do nome do segundo autor no documento. O trabalho de 2014 citado como relato anterior é outro documento (relatório), não este.
- c2: a exposição manipulada é o resultado da pesquisa eleitoral dentro de uma notícia fictícia (Socialdemokratiet ±5 pontos, Konservative ±2 pontos), com grupo de controle sem artigo; não é pesquisa usada apenas como contexto ou fonte de dados.
- c3: além do voto, o artigo mede simpatia pelo partido e probabilidade de votar; como há medida de intenção de voto, o critério é atendido pela célula de voto. Não há desfecho de comparecimento.
- registro_financiamento = 999 porque o documento não traz identificador de pré-registro (OSF, AEA, RIDIE, EGAP) nem número de processo ou edital. Há apenas agradecimento de financiamento sem identificador, no Taksigelse da p. 21 ("Tak til Danmarks Radio for finansiering af dataindsamlingen"), e a menção, na nota 4 da p. 21, a um projeto de pesquisa do Institut for Statskundskab da Universidade de Copenhague, também sem número.
- Preferi trechos sem ligaduras tipográficas (ff, fi, fl) nas evidências; por isso evitei citar frases com "effekten" e "fiktive", que são as formulações mais diretas do desenho no texto.
- Documento com menos de 300 páginas: lido por inteiro (páginas 1 a 19 do PDF, impressas 5 a 23).
