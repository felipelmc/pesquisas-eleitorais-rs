---
citekey: Gersbach2017
ficha_id: Gersbach2017
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Gersbach2017.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_098
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — o título e os autores impressos na folha de rosto batem com os metadados do registro (Assessment Voting in Large Electorates; Gersbach, Mamageishvili, Tejada), e a folha de rosto data esta versão em dezembro de 2017 — evidência: "Assessment Voting in Large Electorates" (p. 1); "This version: December 2017" (p. 1)
- **tipo_documento** — resposta: preprint — documento depositado em repositório, com datas de primeira versão e de versão corrente na folha de rosto e sem nota de publicação em periódico — evidência: "First version: October 2016" (p. 1); "This version: December 2017" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: parcial — o objeto são cidadãos que escolhem entre duas alternativas (A e B) em referendo ou eleição, mas são agentes de um modelo teórico, sem amostra empírica de eleitores nem eleição real, hipotética ou de laboratório — evidência: "citizens have a right to vote for one of two alternatives" (p. 6)
- **c2_intervencao_estudada** — resposta: Não — a exposição analisada é a divulgação da contagem de votos da primeira rodada do próprio procedimento Assessment Voting, não um resultado de pesquisa eleitoral; o texto contrasta explicitamente esse mecanismo com pesquisas pré-eleitorais — evidência: "The number of votes in favor of either alternative" (p. 3); "Because AV is based on actual votes and not on reported opinions" (p. 14)
- **c3_desfecho** — resposta: parcial — analisa comparecimento (nível endógeno de turnout de equilíbrio) e a alternativa escolhida, ou seja, desfecho de voto e de comparecimento, mas apenas como predição de equilíbrio de um modelo teórico, sem medida empírica — evidência: "which induces an endogenous level of turnout that yields socially desirable outcomes" (p. 4); "No citizen of the second voting round votes." (p. 12)
- **c4_desenho_elegivel** — resposta: Não — modelo teórico formal (jogo de Poisson) com teoremas e provas em apêndice, sem dados e sem variação identificada de exposição — evidência: "we consider a model of a society that needs to choose" (p. 4); "The proofs of the main body of the paper" (p. 6)
- **c5_estudo_primario** — resposta: parcial — trabalho teórico original, com análise própria (modelo formal, teoremas e provas), mas sem análise de dados empíricos; não é revisão de literatura, meta-análise, editorial nem comentário — evidência: "In this paper, we have advocated a new voting procedure" (p. 17)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento — evidência: "Assessment Voting in Large Electorates" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Menciona Gersbach (2015), "Assessment-Voting", Neue Zürcher Zeitung, descrição verbal da mesma proposta; a folha de rosto também registra uma versão anterior do próprio texto (outubro de 2016) — evidência: "For a verbal description, see Gersbach" (p. 3); "First version: October 2016" (p. 1)
- **fonte_dados_amostra** — resposta: 999 — evidência: 999
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset de página: a numeração impressa coincide com o índice do PDF. Confirmado em duas páginas distantes: a página 2 do PDF traz "2" no rodapé (primeira página do corpo, início da Introdução) e a página 33 do PDF traz "33" (última página do Apêndice B). A folha de rosto é a página impressa 1 (sem número impresso no rodapé), e as citações dela são registradas como (p. 1).
- Documento lido por inteiro (33 páginas, em duas faixas: 1-17 e 18-33). Não se aplica a regra de documentos com mais de 300 páginas.
- `texto_confere` = Sim: título, três autores e ano batem com os metadados. Registro: o PDF é a cópia depositada em repositório de preprints (carimbo lateral de arXiv na folha de rosto), enquanto o DOI do registro é de SSRN (10.2139/ssrn.3088530). Trata-se, pelo título, autores e data de versão, do mesmo working paper depositado em dois repositórios; por isso não usei "parcial". Fica como pendência para o coordenador, caso a convenção do projeto trate depósitos distintos como versões diferentes.
- `tipo_documento` = preprint: o documento não declara periódico nem número de série de working paper institucional no corpo do texto; o que declara são as datas de versão ("First version" / "This version") e o carimbo de repositório de preprints. Evitei citar o carimbo lateral como evidência porque é texto rotacionado na margem e a camada de texto pode extraí-lo com espaçamento irregular.
- `c1` = parcial: a "população" são cidadãos de um modelo (país ou jurisdição genérica, preferências privadas sorteadas de uma distribuição comum, número de cidadãos com distribuição de Poisson). O contexto é de referendo ou eleição binária, mas não há eleitores reais, participantes de laboratório nem unidades eleitorais agregadas observadas, então marquei ambiguidade em vez de "Sim".
- `c2` = Não: a exposição do modelo é a divulgação pública da contagem de votos da primeira rodada do Assessment Voting entre as duas rodadas de votação, e não o resultado de uma pesquisa eleitoral. Pesquisas pré-eleitorais aparecem apenas como contraste teórico e como referência à literatura de manipulação de pesquisas (p. 14).
- `c3` = parcial: os desfechos tratados são comparecimento e alternativa vencedora (ambos de interesse do protocolo), mas derivados analiticamente como propriedades de equilíbrio, sem qualquer medida. Não usei "Não" porque os desfechos são de voto e de comparecimento; não usei "Sim" porque não há medida nem análise de dados.
- `c5` = parcial: o prompt manda responder "Não" apenas para revisão, meta-análise, editorial ou comentário, que não é o caso; mas também não há análise própria de dados, já que o estudo é puramente teórico. Marquei ambiguidade e não escrevi a frase "revisão: usar na bola de neve", porque o texto não é revisão. A exclusão substantiva, se houver, vem de `c4`.
- `fonte_dados_amostra` = 999: o documento não relata fonte de dados, período nem tamanho de amostra, porque não usa dados empíricos. Não inferi nem descrevi ausência como resposta substantiva.
- `registro_financiamento` = 999: a nota de rodapé da folha de rosto traz apenas agradecimentos a colegas e a participantes de seminário, sem número de processo, edital ou identificador de pré-registro.
- Nas evidências, preferi trechos sem ligaduras tipográficas (ff, fi, fl). Por isso, em `c2`, citei "The number of votes in favor of either alternative" em vez do trecho seguinte, que contém "first".
