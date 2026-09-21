---
citekey: Kawai2013
ficha_id: Kawai2013
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Kawai2013.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_162
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o título ("Inferring Strategic Voting") e os autores (Kei Kawai, New York University; Yasutora Watanabe, Northwestern University) batem com os metadados, mas o PDF é uma versão de manuscrito datada de abril de 2012, sem identificação de periódico, volume, páginas ou DOI da publicação na American Economic Review de 2013 registrada pelo coordenador — evidência: "Inferring Strategic Voting" (p. 1); "April 2012" (p. 1)
- **tipo_documento** — resposta: artigo — evidência: "In this paper, we only focus on the issue of strategic voting" (p. 31)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, analisa unidades eleitorais agregadas (municípios dentro de distritos eleitorais) de uma eleição real, a eleição geral da Câmara dos Representantes do Japão de 11 de setembro de 2005 — evidência: "data from the Japanese House of Representatives election held on September 11" (p. 13)
- **c2_intervencao_estudada** — resposta: parcial, as previsões pré-eleitorais distrito a distrito publicadas por dois semanários entram no modelo como medida da proximidade esperada da eleição (w) que condiciona a fração estimada de eleitores estratégicos, mas não há manipulação experimental, variação natural identificada da divulgação nem exposição medida no indivíduo em painel — evidência: "Data on pre-election forecasts are collected from two periodicals" (p. 13); "They have district-by-district election forecasts, which we use as a measure" (p. 13)
- **c3_desfecho** — resposta: Sim, o desfecho é de voto: a variável dependente é a votação agregada (vote share) de cada candidato por município e distrito, e o experimento contrafactual reporta também número de cadeiras; não há desfecho de comparecimento, explicitamente deixado fora do modelo — evidência: "Regress the vote share data of candidate k in each municipality" (p. 28); "breakdown of vote-share data is available by municipality" (p. 13)
- **c4_desenho_elegivel** — resposta: Não, é estudo observacional agregado de corte transversal: um modelo estrutural de voto estratégico estimado por desigualdades de momento com dados municipais de uma única eleição, sem aleatorização, proibição/embargo, fuso horário, calendário de divulgação, diferenças em diferenças, descontinuidade ou painel individual que identifique variação da exposição — evidência: "We estimate the model using an inequality-based estimator developed by Pakes" (p. 28); "We use municipality-level aggregate data for our estimation." (p. 41)
- **c5_estudo_primario** — resposta: Sim, é estudo primário com análise própria de dados eleitorais agregados, de survey de candidatos e demográficos da eleição japonesa de 2005 — evidência: "We obtained the data on the vote shares and candidate characteristics" (p. 13)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação no documento — evidência: "Inferring Strategic Voting" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Dados agregados da eleição geral da Câmara dos Representantes do Japão de 11 de setembro de 2005 — vote shares por município e características dos candidatos do Yomiuri Shimbun e do Asahi-Todai Elite Survey 2005, demografia municipal do Social and Demographic Statistics of Japan e previsões de proximidade dos semanários Shukan Asahi e Shukan Gendai —, com amostra final de 159 distritos eleitorais — evidência: "We are left with 159 electoral districts." (p. 14); "We obtained the data on the vote shares and candidate characteristics" (p. 13)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset: a numeração impressa coincide com o índice do PDF em todo o documento. Conferi a folha 1 do PDF (numeral impresso "1", folha de rosto), a folha 13 (numeral "13", início da seção "3 Data") e a folha 50 (numeral "50", última página do Supplementary Material B). Logo `folha_do_PDF = pagina_anotada + 0`, `paginacao: impressa`, `offset_pagina: 0`. Todas as citações desta ficha foram reabertas nas folhas indicadas pela fórmula.
- Documento de 50 páginas, lido por inteiro em três faixas (1-20, 21-40, 41-50); não se aplica a regra de leitura parcial de documentos com mais de 300 páginas.
- `texto_confere` = parcial: o trabalho é o mesmo (mesmo título, mesmos autores, mesmas afiliações), mas o arquivo é o manuscrito datado de abril de 2012, com seções próprias de "Supplementary Material A" e "Supplementary Material B" ao fim do corpo do texto (pp. 47-50) e sem qualquer marca de publicação em periódico. Por isso registrei parcial em vez de Sim, para que o coordenador saiba que a paginação e a estrutura não são as da versão publicada na AER (103(2), 2013).
- `tipo_documento` = artigo: o documento não traz nota de publicação, série de working paper nem cabeçalho de periódico; tem folha de rosto com título, autores, afiliações, data, resumo e palavras-chave, e se autodenomina "paper" no corpo do texto. Registrei artigo com base nessa autodescrição; a leitura alternativa seria working_paper, mas nenhuma série é declarada no documento.
- `c2_intervencao_estudada` = parcial (decisão limítrofe). A previsão pré-eleitoral não é mero contexto: ela é coletada como dado (Shukan Asahi e Shukan Gendai), vira a variável w de proximidade esperada, entra na distribuição Beta da fração de eleitores estratégicos e organiza os resultados da Tabela 6, que reporta a fração média de eleitores estratégicos por proximidade prevista (p. 34). Por outro lado, nenhum dos modos de exposição exigidos pelo protocolo está presente: não há manipulação experimental, não há variação natural identificada da divulgação (proibição, embargo, fuso, calendário) e não há medida individual em painel — a previsão é apenas uma covariável agregada num modelo estrutural. Daí parcial, e não Sim nem Não.
- `c4_desenho_elegivel` = Não: o desenho é um modelo estrutural de escolha discreta com identificação parcial, estimado por desigualdades de momento (Pakes, Porter, Ho e Ishii, 2007) sobre dados agregados municipais de uma única eleição; o "counterfactual policy experiment" do texto é uma simulação do modelo, não um desenho empírico com variação identificada da exposição.
- `outros_relatos_mesmo_estudo` = 999: o documento não menciona em nenhum ponto versão anterior, working paper, tese ou relatório técnico do mesmo estudo. Percorri a folha de rosto, a nota de agradecimentos (p. 1), as notas de rodapé e a lista completa de referências (pp. 38-41), que não contém autocitação de Kawai e/ou Watanabe. Em particular, a outra versão do trabalho existente no corpus não é citada no próprio texto, por isso não pôde ser registrada aqui.
- `registro_financiamento` = 999: a nota de agradecimentos (p. 1) agradece a pesquisadores nomeados, a um assistente de pesquisa e a participantes de seminários, sem número de processo, edital, agência financiadora ou identificador de pré-registro; nenhum identificador aparece em outro ponto do documento.
