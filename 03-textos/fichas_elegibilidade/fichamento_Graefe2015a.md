---
citekey: Graefe2015a
ficha_id: Graefe2015a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Graefe2015a.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: elegib-opus5-058
data_fichamento: 2026-09-19
---

## Identificacao
- **texto_confere** — resposta: parcial; título e autor idênticos aos do registro, mas o PDF é o manuscrito do autor, sem diagramação nem dados de periódico (outra versão do mesmo trabalho) — evidência: "Improving forecasts using equally weighted predictors" (p. 1)
- **tipo_documento** — resposta: preprint; manuscrito do autor sem cabeçalho de periódico nem nota de publicação, com rodapé N of 20 — evidência: "1 of 20" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, unidades eleitorais agregadas: resultado nacional das eleições presidenciais dos EUA (1976 a 2012). — evidência: "Forecast accuracy was analyzed across the ten U.S. presidential elections from 1976" (p. 9)
- **c2_intervencao_estudada** — resposta: Não, pesquisas de opinião (popularidade presidencial) entram só como variáveis preditoras de modelos de previsão; o objeto é a precisão de pesos iguais versus pesos de regressão. — evidência: "public opinion polls are major predictors in election forecasting models" (p. 7); "tests the predictive performance of equal and regression weights" (p. 7)
- **c3_desfecho** — resposta: Sim, desfecho de voto: participação do candidato do partido incumbente no voto popular bipartidário, como variável dependente e alvo de previsão (não há desfecho de comparecimento). — evidência: "The dependent variable was the two-party popular vote received by the candidate" (p. 8)
- **c4_desenho_elegivel** — resposta: Não, estudo observacional agregado de previsão eleitoral (modelos de regressão e de pesos iguais com previsões pseudo ex ante), sem variação identificada da exposição a pesquisas. — evidência: "calculated as one-election-ahead predictions" (p. 8); "Each of these models is estimated using multiple regression analysis" (p. 6)
- **c5_estudo_primario** — resposta: Sim, estudo primário com análise própria dos dados de nove modelos de previsão, além de uma revisão de literatura introdutória. — evidência: "This study uses data from nine established U.S. election-forecasting models" (p. 1)
- **c6_nao_retratado** — resposta: Sim, não há aviso de retratação no documento. — evidência: "Improving forecasts using equally weighted predictors" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Dados de nove modelos de previsão da eleição presidencial dos EUA (seis obtidos de Montgomery, Hollenbach e Ward 2012, um de Lockerbie 2012, dois cedidos por Cuzán e Holbrook), com previsões pseudo ex ante para as dez eleições de 1976 a 2012; o modelo índice soma 27 variáveis e é estimado com dados a partir de 1952. — evidência: "The present study analyses forecasts from the nine models" (p. 8); "Forecast accuracy was analyzed across the ten U.S. presidential elections from 1976" (p. 9)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: o rodapé impresso "N of 20" coincide com o índice do PDF (p. 1 → PDF 1; p. 9 → PDF 9; p. 16 → PDF 16), logo offset_pagina = 0. O PDF tem 16 páginas, embora o rodapé indique 20: as páginas com as Tabelas 1 a 3 e as Figuras 1 e 2 (provavelmente p. 17 a 20) não estão no arquivo. Documento lido por inteiro (p. 1 a 16).
- texto_confere / tipo_documento: título e autor batem exatamente com o registro, mas o arquivo é um manuscrito em formato de submissão (espaço duplo, sem cabeçalho do Journal of Business Research, sem DOI, ano ou volume). Por isso 'parcial' e 'preprint'; se o coordenador tratar o manuscrito aceito do autor como a mesma versão do artigo, texto_confere passa a 'Sim' e tipo_documento a 'artigo'. Nada disso afeta o resultado da elegibilidade.
- c1: tratei o resultado nacional das eleições presidenciais como unidade eleitoral agregada; não há eleitores individuais.
- c2 e c4 (motivos decisivos de exclusão): as pesquisas aparecem só como insumo de modelos de previsão (popularidade presidencial e outras medidas de opinião pública) e o estudo avalia a precisão das previsões; não há exposição de eleitores a resultados de pesquisa, manipulada ou identificada.
- c3: o desfecho é voto agregado (participação do incumbente no voto bipartidário), usado como alvo de previsão; o estudo não compara o apoio a quem a pesquisa mostra à frente com o apoio a quem mostra atrás, mas o critério de desfecho em si é de voto.
- outros_relatos_mesmo_estudo: o texto diz que estende Cuzán e Bundrick (2009) e usa dados de Montgomery, Hollenbach e Ward (2012) e de Lockerbie (2012), mas esses são estudos distintos, de outros autores, e não relatos do mesmo estudo. Os dados e cálculos estão em "tinyurl.com/equalweights" (p. 8), o que também não é outro relato. Por isso, 999.
- registro_financiamento: os agradecimentos só mencionam comentários de J. Scott Armstrong e Alfred Cuzán; não há número de processo nem pré-registro.
