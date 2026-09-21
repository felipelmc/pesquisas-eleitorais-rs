---
citekey: Frenkel2012
ficha_id: Frenkel2012
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Frenkel2012.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_176
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — o título no documento é "Competence and Ambiguity in Electoral Competition" e o autor é Sivan Frenkel, com data de 5 de dezembro de 2012, batendo com título, autor e ano do registro; o documento não traz DOI em nenhuma página. — evidência: "Competence and Ambiguity in Electoral Competition" (p. 1)
- **tipo_documento** — resposta: preprint — manuscrito do próprio autor, datado na folha de rosto, com abstract, classificação JEL e palavras-chave, sem nota de publicação, veículo, número de série ou DOI, e com apêndice online hospedado na página pessoal do autor. — evidência: "December 5, 2012" (p. 1); "The online Appendix is available at" (p. 8)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: parcial — o contexto é eleitoral (um eleitor escolhendo entre dois candidatos numa eleição), mas existe apenas como agente analítico de um modelo formal, sem amostra empírica de eleitores nem participantes de laboratório. — evidência: "There is a single voter and two possible policies" (p. 8)
- **c2_intervencao_estudada** — resposta: Não — a exposição analisada é a declaração de campanha do candidato e seu grau de ambiguidade/compromisso, não resultado de pesquisa eleitoral; o documento não trata de divulgação de pesquisas, agregadores ou boca de urna. — evidência: "During the campaign, each candidate makes a declaration regarding the policy" (p. 9)
- **c3_desfecho** — resposta: parcial — o desfecho é de voto (a escolha do eleitor entre os dois candidatos e a probabilidade de eleição de cada um), mas é derivado analiticamente no equilíbrio, sem medida empírica e sem qualquer comparação com o que uma pesquisa mostraria à frente ou atrás. — evidência: "The voter elects with probability one the candidate he believes" (p. 12)
- **c4_desenho_elegivel** — resposta: Não — modelo teórico de teoria dos jogos (equilíbrio bayesiano perfeito, lemas e proposições com provas), sem dados, sem experimento, sem variação identificada de exposição e sem painel individual. — evidência: "We present a formal game-theoretic model" (p. 4)
- **c5_estudo_primario** — resposta: Não — o documento é um modelo formal sem dados nem análise empírica própria; revisão: usar na bola de neve, porque a seção de discussão cita trabalhos empíricos sobre ambiguidade e escolha do eleitor. — evidência: "The paper uses a simple model to analyze the connection" (p. 22)
- **c6_nao_retratado** — resposta: Sim — não há marca "RETRACTED", nota ou página de retratação em nenhuma das 28 páginas; a primeira página traz apenas título, autor e data. — evidência: "Competence and Ambiguity in Electoral Competition" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim — a nota de rodapé de autoria informa que o trabalho foi feito como parte da tese de doutorado do autor na Eitan Berglas School of Economics, Tel Aviv University; há também um Apêndice Online com as provas, hospedado na página pessoal do autor (p. 8). — evidência: "This work was done as part of my PhD thesis" (p. 1)
- **fonte_dados_amostra** — resposta: 999 — evidência: 999
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: a numeração impressa no rodapé coincide com o índice do PDF em todas as páginas conferidas (rodapé "1" na folha de rosto do PDF 1, "4" no PDF 4, "8" no PDF 8, "12" no PDF 12, "22" no PDF 22, "28" no PDF 28), logo `paginacao: impressa` e `offset_pagina: 0`. Todas as citações foram reabertas na página impressa correspondente.
- Documento lido por inteiro (PDF 1 a 28, em duas faixas de 14 páginas): corpo do artigo (p. 1 a 22), referências (p. 22 a 24) e Apêndice Online com as provas (p. 25 a 28).
- `texto_confere` = Sim: título e primeiro autor batem exatamente com os metadados, e a data do documento é de 2012. Não marquei "parcial" porque o registro não indica versão publicada com a qual contrastar; registro, ainda assim, que o documento não tem DOI, veículo nem nota de publicação, e que agradece a "two anonymous reviewers" (p. 1), o que é compatível com manuscrito submetido.
- `tipo_documento` = preprint: o documento não declara seu tipo em lugar nenhum. Classifiquei pelo que a folha de rosto mostra (manuscrito datado, sem veículo nem número de série de coleção de working papers) e pelo apêndice online na página pessoal do autor. Se o critério do projeto for exigir declaração explícita, este campo viraria 999.
- `c1` e `c3` = parcial: o texto é teoria pura. Há eleitor, candidatos e escolha de voto, mas como objetos de um modelo (um único eleitor representando o eleitor mediano, p. 8), não como amostra observada ou participantes de experimento; nenhum desfecho é medido. Marquei "parcial" em vez de "Sim" por isso, e em vez de "Não" porque o objeto modelado é de fato uma escolha eleitoral entre dois candidatos.
- `c2` = Não com segurança: pesquisa eleitoral (poll) não aparece como exposição nem como tema; a exposição do modelo é a clareza/ambiguidade da declaração de campanha como sinal de competência.
- `c5` = Não: o documento não é revisão nem meta-análise, mas também não tem dados próprios (é modelo formal), o que o enquadra na convenção do projeto para ensaios sem dados próprios; inseri a frase 'revisão: usar na bola de neve' porque a discussão (p. 20 a 21) cita estudos empíricos potencialmente elegíveis (Tomz e van Houweling 2009, Campbell 1983, Bartels 1986, Brady e Ansolabehere 1989).
- `fonte_dados_amostra` = 999 porque não há dados, período nem amostra no documento; `registro_financiamento` = 999 porque a nota de agradecimentos (p. 1) cita orientador e pareceristas, mas nenhum número de processo, edital ou identificador de pré-registro.
