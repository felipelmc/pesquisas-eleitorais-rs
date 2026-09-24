---
citekey: HashemPesaran2024a
ficha_id: HashemPesaran2024a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/Desktop/pesquisas-eleitorais-rs/03-textos/pdfs/HashemPesaran2024a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_e6b_16
data_fichamento: 2026-09-24
---

## Identificacao
- **texto_confere** — resposta: Sim. O título e os autores no documento (M. Hashem Pesaran; Hayun Song, 2024) batem com os metadados (título "Forecasting 2024 US Presidential Election by States Using County Level Data: Too Close to Call"). — evidência: "Forecasting 2024 US Presidential Election by States" (p. 2)
- **tipo_documento** — resposta: working_paper (Cambridge Working Papers in Economics, CWPE 2464, publicado em 10 de outubro de 2024) — evidência: "CAMBRIDGE WORKING PAPERS IN ECONOMICS" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, unidades eleitorais agregadas (condados e estados dos EUA) na eleição presidencial norte-americana. — evidência: "a panel econometric model covering 3,107 counties over" (p. 3)
- **c2_intervencao_estudada** — resposta: Não, o estudo é de previsão eleitoral por regressão em painel com variáveis socioeconômicas e declara não usar dados de pesquisas; a pesquisa eleitoral aparece só como contexto, sem ser exposição analisada. — evidência: "We do not use poll data" (p. 3); "do not make use of any polling data" (p. 2)
- **c3_desfecho** — resposta: Sim, modela e prevê a votação agregada do Partido Republicano e o comparecimento por condado e estado (ambos: voto e comparecimento), embora sem relação com o que as pesquisas mostram. — evidência: "produce state level forecasts of voter turnout" (p. 3)
- **c4_desenho_elegivel** — resposta: Não, é um modelo de previsão por regressão em painel de condados com seleção de variáveis (Lasso, OCMT), sem variação identificada de exposição a pesquisas. — evidência: "We estimate two models: a pooled model and a heterogeneous model." (p. 7)
- **c5_estudo_primario** — resposta: Sim, estudo primário com análise própria de dados de condados atualizados até 2020. — evidência: "It updates the 3,107 county level data used by AP" (p. 2)
- **c6_nao_retratado** — resposta: Sim, não há aviso de retratação no documento. — evidência: "Forecasting 2024 US Presidential Election by" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: O documento é continuação de Ahmed e Pesaran (2020), CESifo Working Paper No. 8615, publicado como Ahmed e Pesaran (2022), International Journal of Forecasting 38(2), 662-687, cujos dados de condados são atualizados aqui. — evidência: "This document is a follow up to the paper by Ahmed and Pesaran" (p. 2); "CESifo Working Paper No. 8615" (p. 28)
- **fonte_dados_amostra** — resposta: Painel de 3.107 condados dos EUA em cinco ciclos de eleição presidencial (2004 a 2020; 15.535 observações na amostra 2000-2020), com votos por condado do MIT Election Data and Science Lab e variáveis socioeconômicas, usado para prever a eleição de 2024. — evidência: "3,107 counties over five election cycles" (p. 3); "County Presidential Election Returns" (p. 29)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: o PDF tem 37 páginas. A p. 1 do PDF é a capa da série CWPE e a p. 2 é a folha de rosto, ambas sem número. As p. 3 a 28 do PDF trazem a numeração impressa 1 a 26, e as p. 29 a 37 trazem a numeração do apêndice A.1 a A.9. Como a capa e a folha de rosto não têm número e o apêndice usa numeração alfanumérica, nenhum offset único cobre o documento; por isso usei `paginacao: indice-do-PDF` com `offset_pagina: 0`, e todas as páginas citadas são índices do PDF (1-based). Conferi: p. 3 do PDF = impressa 1 (Introduction); p. 7 do PDF = impressa 5; p. 28 do PDF = impressa 26 (References); p. 29 do PDF = A.1.
- c2 e c4: as pesquisas aparecem só na motivação (a introdução comenta que há muitas pesquisas e que as dos estados decisivos são instáveis). O objeto é a precisão de um modelo de previsão sem pesquisas; não há exposição a resultado de pesquisa manipulada, variação natural identificada nem painel individual.
- c3: marquei Sim porque as variáveis dependentes são a votação republicana (log-odds) e o comparecimento por condado; o texto não liga esses desfechos a nenhuma exposição a pesquisa.
- Na capa (p. 1), o resumo tem um caractere corrompido em "AP's"; evitei esse trecho nas evidências.
- Documento lido inteiro (p. 1 a 37).
