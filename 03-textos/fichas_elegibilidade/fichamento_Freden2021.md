---
citekey: Freden2021
ficha_id: Freden2021
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Freden2021.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_109
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — evidência: "How Polling Trends Influence Compensational Coalition-Voting" (p. 1)
- **tipo_documento** — resposta: artigo — evidência: "This article develops the idea of compensational voting" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores suecos escolhendo entre partidos em oito eleições gerais reais (1988–2014), com base em amostra representativa do eleitorado. — evidência: "It consists of a representative sample of the Swedish electorate" (p. 4)
- **c2_intervencao_estudada** — resposta: parcial — o resultado de pesquisa eleitoral publicada (média das pesquisas do Sifo na campanha, comparada à votação anterior, formando a "polling trend") é a exposição analisada, mas é uma medida agregada observacional por partido-ano, sem manipulação experimental, sem variação natural identificada e sem medida individual em painel. — evidência: "The central measure for this analysis" (p. 4); "is the average of polls that were presented about a month" (p. 4)
- **c3_desfecho** — resposta: Sim — desfecho de voto: a variável dependente é a escolha de partido (voto) relatada pelo eleitor, sem medida de comparecimento. — evidência: "The outcome variable in the model is party choice (vote)." (p. 5)
- **c4_desenho_elegivel** — resposta: Não — estudo observacional que compara a tendência das pesquisas com o resultado da eleição anterior num logit misto sobre surveys pós-eleitorais repetidos, sem aleatorização, sem variação identificada da exposição e sem painel individual. — evidência: "a mixed logit model has been chosen" (p. 5); "conducted shortly after the general elections" (p. 4)
- **c5_estudo_primario** — resposta: Sim — estudo primário, com análise própria de dados de manifestos, pesquisas e survey. — evidência: "Publicly available datasets were analyzed in this study." (p. 9)
- **c6_nao_retratado** — resposta: Sim — evidência: "How Polling Trends Influence Compensational Coalition-Voting" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Combina manifestos eleitorais codificados pelo projeto do JMG, médias das pesquisas de campanha do instituto Sifo cerca de um mês antes da eleição e o National SOM Survey Cumulative Dataset (survey postal representativo do eleitorado sueco, oito eleições gerais de 1988 a 2014), com mais de 9.000 indivíduos avaliando sete partidos e mais de 64.000 observações. — evidência: "The data on party preference comes from the National SOM Survey" (p. 4); "generating more than 64,000 observations in total" (p. 5)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset: o rodapé da p. 1 do PDF traz "1" e o rodapé da última página traz "10"; conferi também a página de resultados (rodapé "7" na sétima página do PDF). Numeração impressa == índice do PDF, logo `offset_pagina: 0` e `paginacao: impressa`.
- c2 = parcial: a pesquisa eleitoral não aparece como mero contexto — a "polling trend" (média das pesquisas de campanha do Sifo menos a votação do partido na eleição anterior) é a variável explicativa central, inclusive nas interações de dois e três termos do modelo. Mas nenhum dos três modos qualificadores do critério se verifica: não há manipulação experimental, não há variação natural identificada (proibição, fuso, calendário) e a exposição é medida no nível partido-ano, não no indivíduo em painel. Por isso "parcial" e não "Sim".
- c4 = Não: o desenho é exatamente o caso excluído pelo protocolo (tendência das pesquisas comparada ao resultado anterior, em análise observacional agregada quanto à exposição). O survey SOM é uma série de cortes transversais aplicados logo após cada eleição, não um painel com exposição medida antes do desfecho.
- c3: o texto mede escolha de partido declarada; não há desfecho de comparecimento.
- outros_relatos_mesmo_estudo = 999: o documento cita Fredén (2014) e outros trabalhos da autora apenas como literatura prévia sobre o caso sueco, e cita o projeto do JMG e o SOM como fontes de dados; não há menção a versão anterior, tese, working paper ou relatório do mesmo estudo.
- registro_financiamento = 999: não há identificador de pré-registro nem número de processo/edital. A seção de financiamento traz apenas "All sources of funding for the research has been submitted." (p. 9), sem identificador; o link da seção de disponibilidade de dados (catálogo SND) é repositório de dados, não pré-registro.
- Documento de 10 páginas, lido por inteiro (pp. 1–10).
