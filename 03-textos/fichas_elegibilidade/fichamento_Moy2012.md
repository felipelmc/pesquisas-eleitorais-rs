---
citekey: Moy2012
ficha_id: Moy2012
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Moy2012.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_095
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial, o título e o primeiro autor batem com os metadados do registro, mas este PDF é a versão pre-print do capítulo publicado (mesmo trabalho, outra versão) — evidência: "Attitudinal and Behavioral Consequences of Published Opinion Polls" (p. 2); "Pre-print version" (p. 1)
- **tipo_documento** — resposta: capitulo, o texto se declara capítulo e a nota de publicação da folha de rosto o situa em livro organizado (Palgrave Macmillan, 2012) — evidência: "This chapter explores the attitudinal and behavioral consequences" (p. 2)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, o capítulo trata de cidadãos e eleitores em contextos eleitorais (apoio a candidatos, partidos e opções de referendo), embora também cubra efeitos fora do contexto eleitoral — evidência: "what do citizens believe to be the electoral utility of voting" (p. 6); "polls lead people to support a trailing party, candidate or policy" (p. 7)
- **c2_intervencao_estudada** — resposta: Sim, a exposição de interesse do capítulo é o resultado de pesquisa eleitoral publicada (trial heat, tracking e boca de urna), e não a pesquisa como contexto, motivação ou fonte de dados, ainda que a análise seja de literatura e não empírica própria — evidência: "consequences of public opinion polls portrayed in the media" (p. 2); "Three types of election polls provide much of the fodder" (p. 4)
- **c3_desfecho** — resposta: Sim, o desfecho é de ambos: comparecimento (mobilização e desmobilização) e apoio ou intenção de voto em candidato, partido ou opção (bandwagon, underdog, voto estratégico) — evidência: "on turnout among citizens can be classified simply as either mobilizing" (p. 6); "an increase of support given to a party, candidate, or policy position" (p. 8)
- **c4_desenho_elegivel** — resposta: Não, é revisão narrativa e discussão teórica da literatura, sem experimento, sem variação identificada da exposição e sem painel individual próprio — evidência: "We begin with a review of the types of information" (p. 2)
- **c5_estudo_primario** — resposta: Não, revisão: usar na bola de neve; o capítulo sintetiza a literatura sobre efeitos de pesquisas publicadas e não analisa dados próprios — evidência: "The literature provides evidence for both possible consequences." (p. 6)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação em nenhuma parte do documento — evidência: "Attitudinal and Behavioral Consequences of Published Opinion Polls" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim, a folha de rosto declara a versão publicada deste mesmo texto: Moy, Patricia, and Eike Mark Rinke. 2012. "Attitudinal and Behavioral Consequences of Published Opinion Polls." In Opinion Polls and the Media: Reflecting and Shaping Public Opinion, ed. Jesper Strömbäck e Christina Holtz-Bacha, 225-45, Basingstoke, UK: Palgrave Macmillan, DOI 10.1057/9780230374959_11 — evidência: "Published as:" (p. 1); "Basingstoke, UK: Palgrave" (p. 1)
- **fonte_dados_amostra** — resposta: 999 — evidência: 999
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: o PDF não traz numeração impressa em nenhuma página (não há cabeçalho nem rodapé com número nas 32 páginas). Conferi a folha de rosto (página 1 do PDF, "Published as:"), a página de abertura do corpo (página 2, título e autores) e páginas distantes, como a de início das referências (página 26, "References") e a última (página 32, entrada "Zech, C. E. (1975)"): nenhuma exibe número impresso. Por isso `paginacao: indice-do-PDF` e `offset_pagina: 0`; todas as páginas citadas são o índice 1-based do PDF.
- `texto_confere` = parcial (e não Sim) porque o documento é explicitamente a versão pre-print do capítulo que consta do registro: título, autores, ano e DOI conferem, mas o arquivo não é a versão editorada (páginas 225-45 do livro).
- `tipo_documento` = capitulo: o documento se declara capítulo no corpo e a nota de publicação da folha de rosto o identifica como capítulo de livro organizado. A condição de pre-print está registrada em `texto_confere`, não aqui.
- c1 a c4 foram respondidos pelo conteúdo do capítulo, conforme a convenção do projeto de que revisões podem ter os critérios anteriores respondidos normalmente. c1 = Sim porque ao menos a parte eleitoral do capítulo trata de eleitores e cidadãos escolhendo entre candidatos, partidos e opções de referendo; a outra parte ("Non-electoral effects") trata de confiança política, engajamento e expressão de opinião, o que não descaracteriza o critério.
- c2 = Sim: a exposição de interesse é o resultado de pesquisa eleitoral divulgada, não a pesquisa como contexto, motivação ou fonte de dados de intenção de voto. Não há, porém, análise empírica própria, o que é tratado em c4 e c5.
- c4 = Não (e não 999): o documento não deixa de descrever um método por omissão; ele não tem desenho empírico porque é revisão narrativa e discussão teórica, categoria que o próprio prompt manda classificar como Não.
- `fonte_dados_amostra` = 999 porque o capítulo não coleta nem analisa dados próprios: não há fonte de dados, período ou tamanho de amostra a registrar. `registro_financiamento` = 999 porque o documento não traz identificador de pré-registro (OSF, AEA, RIDIE, EGAP) nem número de processo ou edital em nenhuma página, inclusive na folha de rosto e ao fim do texto.
- Nas evidências preferi trechos sem palavras com ligaduras tipográficas (ff, fi, fl), o que explica a escolha de citações que não usam a palavra "effects", abundante no texto.
- Li o documento inteiro (páginas 1 a 32 do PDF), em duas faixas de 16 páginas; as páginas 26 a 32 são a lista de referências.
