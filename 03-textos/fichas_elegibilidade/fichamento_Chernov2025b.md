---
citekey: Chernov2025b
ficha_id: Chernov2025b
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Chernov2025b.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: elegib-opus5-078
data_fichamento: 2026-09-19
---

## Identificacao
- **texto_confere** — resposta: Sim. Título, autores (Chernov, Elenev, Song) e ano (janeiro de 2025) do documento batem com o registro; o documento é o NBER Working Paper 33339. — evidência: "The Comovement of Voter Preferences: Insights from U.S. Presidential Election Prediction" (p. 1)
- **tipo_documento** — resposta: working_paper — evidência: "NBER Working Paper No. 33339" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim. Analisa as preferências de voto entre os candidatos democrata e republicano, agregadas por estado (10 estados competitivos), na eleição presidencial dos EUA de 2024. — evidência: "Our model estimates the joint dynamics of voter preferences across states." (p. 1); "Applying our approach to the 2024 Presidential Election" (p. 1)
- **c2_intervencao_estudada** — resposta: Não. As médias de pesquisas (agregadores) são só insumo para medir a preferência de voto num modelo de previsão, junto com preços de mercados de predição; não há exposição a resultado de pesquisa analisada. — evidência: "A key data input into these models are polls" (p. 3); "we use averages constructed by polling aggregators" (p. 9)
- **c3_desfecho** — resposta: Sim. Desfecho de voto: margem líquida de preferência (democrata menos republicano) por estado, estimada ao longo da campanha e simulada para o dia da eleição. — evidência: "representing the net margin for the Democratic presidential candidate" (p. 11); "to estimate voter preferences across U.S. states for the 2024 Presidential Election" (p. 32)
- **c4_desenho_elegivel** — resposta: Não. Modelo econométrico de séries temporais (espaço de estados) para previsão eleitoral, observacional agregado, sem variação identificada da exposição a pesquisas. — evidência: "we propose a time-series econometric framework" (p. 3); "We set up the problem using state space representation." (p. 4)
- **c5_estudo_primario** — resposta: Sim. Análise própria de dados de pesquisas, preços da Polymarket e fundamentos macroeconômicos de 2024. — evidência: "Political prediction market prices are taken at daily frequency from Polymarket." (p. 9)
- **c6_nao_retratado** — resposta: Sim. Não há aviso de retratação no documento. — evidência: "The Comovement of Voter Preferences: Insights from U.S. Presidential Election Prediction" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Menciona uma versão anterior do mesmo trabalho, de outubro de 2024, no SSRN (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4998858), que introduziu o modelo e produziu previsões em tempo real; o próprio documento é o NBER Working Paper 33339 (janeiro de 2025). — evidência: "The October 2024 version of our paper introduced this forecasting model" (p. 8); "This version is available at" (p. 8)
- **fonte_dados_amostra** — resposta: Painel estado-dia de médias diárias de pesquisas (FiveThirtyEight e Silver Bulletin), preços diários de contratos estaduais da Polymarket e três séries nacionais de fundamentos, para 10 estados competitivos na eleição presidencial dos EUA de 2024; amostra de estimação de 1º de junho a 25 de outubro de 2024. — evidência: "Our main data sources are FiveThirtyEight and the Silver Bulletin." (p. 9); "As a result, we focus our analysis on the 10" (p. 10); "we restrict our estimation sample to the period from June 1," (p. 10)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset de página: a numeração impressa começa em "2" na página 3 do PDF (Introdução) e segue até "37" na página 38 do PDF (referências); conferido também em impressa 19 = PDF 20 e impressa 32 = PDF 33. Logo offset_pagina = 1. A capa (PDF 1) e a página de título com resumo (PDF 2) não têm número impresso; pelo offset, a página de título com resumo corresponde a p. 1, que é como foi citada. O apêndice usa numeração própria (A-1 a A-9, PDF 39 a 47) e não foi citado. Documento lido por inteiro (PDF 1 a 47).
- texto_confere: título, os três autores e o ano batem com os metadados. O registro traz DOI do SSRN (10.2139/ssrn.5099876) e o PDF é o NBER Working Paper 33339 de janeiro de 2025; o documento cita uma versão anterior no SSRN com outro identificador (abstract_id=4998858, outubro de 2024), o que sugere que o registro é a versão de janeiro de 2025. Não há como confirmar pelo documento que o id 5099876 é exatamente esta versão, mas título, autores e ano coincidem, por isso "Sim".
- c6: a regra pede o título na primeira página; a capa (PDF 1) traz o título em caixa-alta, mas não tem número impresso e ficaria como p. 0 pelo offset, então citei o título da página de título com resumo (PDF 2, p. 1), que é a primeira página do trabalho com texto. Nenhum aviso de retratação em nenhuma página.
- c2 e c4: o artigo combina pesquisas e preços de mercados de predição para estimar preferências latentes e prever a eleição; pesquisas aparecem como fonte de dados para medir intenção de voto (motivo de "Não" no protocolo), e mercados de predição também não são exposição aceita. Não há experimento, variação natural nem painel individual.
- c3: "Sim" porque o estudo analisa a margem de preferência de voto por estado (e compara as previsões com o resultado final), embora essa medida seja estimada a partir das próprias pesquisas e preços, não como desfecho de uma exposição.
- registro_financiamento: só há agradecimento a um comentarista; nenhum número de financiamento ou pré-registro.
