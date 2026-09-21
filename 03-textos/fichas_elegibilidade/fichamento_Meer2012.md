---
citekey: Meer2012
ficha_id: Meer2012
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Meer2012.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_124
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o título e o primeiro autor batem com os metadados, mas o arquivo é a versão de manuscrito do autor (tabelas e figuras ao final, marcas "[Table 1 approximately here]", sem a paginação do periódico), não a versão publicada em Acta Politica — evidência: "A panel study on the structure of changing vote intentions" (p. 1)
- **tipo_documento** — resposta: artigo — manuscrito de artigo de periódico, cuja publicação o próprio documento anuncia — evidência: "will be made publicly available upon publication of this paper" (p. 14)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores neerlandeses elegíveis a votar, acompanhados em painel sobre em qual partido votariam nas eleições parlamentares entre 2006 e 2010 — evidência: "we restricted the sample to respondents eligible to cast a vote" (p. 11)
- **c2_intervencao_estudada** — resposta: Não — o resultado de pesquisa eleitoral não é a exposição analisada; o painel de opinião é apenas a fonte de dados para medir intenção de voto, e o objeto é a estrutura ideológica das mudanças de voto, sem exposição manipulada, com variação natural identificada ou medida no indivíduo — evidência: "whether and how changes in voting behaviour are structured" (p. 3)
- **c3_desfecho** — resposta: Sim — mede intenção de voto em cada onda e o voto autorrelatado de 2006 e 2010; desfecho de voto (não há medida de comparecimento) — evidência: "Which party would you vote for if parliamentary elections were held today?" (p. 12)
- **c4_desenho_elegivel** — resposta: Não — painel individual descritivo analisado por tabulações cruzadas e por unfolding multidimensional indutivo, sem exposição a pesquisa eleitoral medida antes do desfecho nem variação identificada de exposição — evidência: "multidimensional unfolding does not provide a statistical test" (p. 14)
- **c5_estudo_primario** — resposta: Sim — estudo primário, com análise própria dos dados do painel 1VOP coletado pelos autores — evidência: "We test these theories using the 1Vandaag Opinion Panel data set" (p. 1)
- **c6_nao_retratado** — resposta: Sim — não há marca "RETRACTED", nota ou página de retratação no documento — evidência: "Bounded volatility in the Dutch electoral" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim — a folha de rosto cita a versão publicada do mesmo trabalho em Acta Politica (2012), v. 4, p. 333-355; os apêndices são remetidos a uma página online do primeiro autor — evidência: "Acta Politica 4, 333-355" (p. 1)
- **fonte_dados_amostra** — resposta: Painel de opinião online 1Vandaag (1VOP), 53 ondas de entrevista entre janeiro de 2007 e junho de 2010, com 54.763 respondentes elegíveis a votar que participaram de ao menos duas ondas, mais o voto autorrelatado nas eleições parlamentares de 2006 e 2010 — evidência: "The data set covers 53 waves of interview conducted" (p. 10); "who participated in at least two waves (N= 54,763)" (p. 11)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: o documento não traz numeração impressa em nenhuma página (não há cabeçalho nem rodapé numerado); conferi nas páginas distantes 1, 11, 21 e 31 do PDF. Por isso `paginacao: indice-do-PDF` e `offset_pagina: 0`; todas as páginas citadas são índices 1-based do PDF.
- Leitura: documento de 31 páginas, lido por inteiro em duas faixas (1-20 e 21-31), incluindo notas de fim (p. 23-25), referências (p. 26-27), Tabelas 1 e 2 (p. 28-29) e Figuras 1a-1c e 2 (p. 30-31).
- `texto_confere` = parcial: título ("Bounded volatility in the Dutch electoral battlefield") e primeiro autor (Tom van der Meer) coincidem com os metadados, assim como o ano (2012), mas trata-se do manuscrito aceito/pré-publicação, e não da versão paginada do periódico. O subtítulo da folha de rosto ("A panel study on changing vote intentions in a changing party system") difere ligeiramente do "Full title" ("A panel study on the structure of changing vote intentions"), que é o que consta dos metadados do registro.
- `c2` = Não: as pesquisas de opinião (1VOP, e as de Peil.nl, TNS/Nipo e Synovate citadas só para comparação de tendências) entram como fonte de dados e como referência de validade externa, nunca como tratamento ou exposição cujo efeito se estime. O artigo estima a estrutura dimensional das trocas de voto entre partidos, não o efeito de divulgar um resultado de pesquisa.
- `c4` = Não decorre de `c2`: embora o desenho seja um painel individual com muitas ondas (o que satisfaz a parte "painel" do protocolo), não há exposição a resultado de pesquisa medida antes do desfecho nem comparação entre níveis de exposição; as análises são tabulações cruzadas descritivas e um modelo de unfolding multidimensional explicitamente indutivo.
- `registro_financiamento` = 999: o documento agradece financiamento do programa de pesquisa "Adrift or adroit? On the sources of electoral volatility in the Netherlands, 2006-2010", financiado pela Netherlands Organisation for Scientific Research (NWO) (p. 1), mas não informa número de processo, de edital nem identificador de pré-registro; como a variável pede identificadores, registrei 999.
- Evidências escolhidas preferindo trechos sem ligaduras tipográficas (ff, fi, fl); por isso a citação do título em `c6_nao_retratado` foi cortada antes da palavra "battlefield".
