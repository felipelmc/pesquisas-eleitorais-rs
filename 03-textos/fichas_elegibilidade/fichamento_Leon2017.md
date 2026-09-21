---
citekey: Leon2017
ficha_id: Leon2017
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Leon2017.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_120
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o PDF é o working paper (Barcelona GSE WP 691, versão de novembro de 2015) do mesmo trabalho do registro (mesmo título e mesmo autor, León/Leon, Gianmarco), não a versão publicada de 2017 no periódico — evidência: "Turnout, Political Preferences and Information:" (p. 1)
- **tipo_documento** — resposta: working_paper — evidência: "Barcelona GSE Working Paper Series" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores reais em eleição real (eleição municipal peruana de outubro de 2010), amostrados em 29 povoados de 10 distritos da região de Lima — evidência: "voters in a sample of 29 villages in 10 districts" (p. 12)
- **c2_intervencao_estudada** — resposta: Não — a exposição analisada é informação sobre o novo valor da multa por abstenção (variação individual no custo de se abster), e não resultado de pesquisa eleitoral; pesquisa de opinião aparece apenas como instrumento de coleta de dados (baseline e follow-up) — evidência: "individual level variation in the cost of abstention" (p. 12)
- **c3_desfecho** — resposta: Sim — o desfecho é comparecimento: voto declarado e validado objetivamente pelo carimbo no documento de identidade na eleição municipal de 2010; não há medida de escolha de voto entre candidatos ou partidos — evidência: "whether or not each respondent voted in the municipal election" (p. 13)
- **c4_desenho_elegivel** — resposta: Sim — experimento de campo aleatorizado no indivíduo dentro do povoado, combinado com mudança legal exógena e estimação por variáveis instrumentais (2SLS) — evidência: "By stratifying the randomization at the village level" (p. 12)
- **c5_estudo_primario** — resposta: Sim — estudo primário com dados próprios coletados pelo autor em survey de linha de base e de acompanhamento ligado ao experimento de campo — evidência: "I have complete baseline information for 2,837 individuals" (p. 12)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação em nenhuma parte do documento — evidência: "Turnout, Political Preferences and Information:" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim — a folha de rosto registra que esta é a versão de novembro de 2015 de um working paper cuja versão anterior é de dezembro de 2014 (Barcelona GSE Working Paper Series, Working Paper no 691); nenhuma tese, relatório técnico ou artigo adicional com os mesmos dados é mencionado no texto — evidência: "This version: November 2015" (p. 0); "(December 2014)" (p. 0)
- **fonte_dados_amostra** — resposta: Experimento de campo com surveys de linha de base (uma a quatro semanas antes da eleição) e de acompanhamento (uma a três semanas depois) em 29 povoados de 10 distritos da região de Lima, em torno da eleição municipal peruana de 3 de outubro de 2010; 2.837 indivíduos de 1.911 domicílios no baseline e 1.732 indivíduos de 1.166 domicílios na amostra de análise — evidência: "we were able to track down 1,732 individuals from 1,166 households" (p. 16)
- **registro_financiamento** — resposta: Não há identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP) no documento; há financiamento do IBER, CEGA e IADB e do Ministério da Economia e Competitividade da Espanha, com os identificadores SEV-2011-0075 (Severo Ochoa) e ECO2014-55555-P — evidência: "(SEV-2011-0075) and grant ECO2014-55555-P" (p. 1)

## Notas do codificador
- Offset de página: a numeração impressa começa na folha de rosto interna do artigo, que é a página 2 do PDF (marcada "1" no rodapé), logo impressa P → PDF 1-based = P + 1. Confirmei em duas páginas distantes: a página impressa 1 (título e resumo) é a página 2 do PDF e a página impressa 40 (Table 1) é a página 41 do PDF.
- A capa institucional do Barcelona GSE (página 1 do PDF) não tem número impresso. Para manter a convenção `impressa P → PDF = P + offset`, ela está citada como "p. 0" (0 + 1 = página 1 do PDF) nas variáveis `tipo_documento` e `outros_relatos_mesmo_estudo`, que são as únicas informações que só existem nessa capa.
- `texto_confere` = parcial porque o PDF é o working paper (esta versão: novembro de 2015; folha de rosto interna datada de 10 de outubro de 2015), enquanto os metadados do registro apontam o artigo de 2017 com DOI 10.1016/j.jdeveco.2017.02.005. Título e autor batem; trata-se de outra versão do mesmo trabalho.
- `c2` = Não é o motivo central de inelegibilidade: o tratamento aleatorizado é a informação sobre o novo nível da multa por abstenção (Ley 28859), e a variação explorada é a mudança legal peruana de 2006 mais a atualização individual da multa percebida. Pesquisa eleitoral não é exposição em nenhuma das análises do documento; os surveys do autor são apenas fonte de dados. Também não há mercado de apostas, divulgação de projeção ou embargo de pesquisa como exposição.
- `c3` = Sim apenas pela célula de mobilização (comparecimento). O documento analisa ainda preferências de política, aquisição de informação política e compra de voto, mas nenhuma medida de intenção ou escolha de voto entre candidatos, partidos ou opções, de modo que não se pode comparar apoio a quem lidera contra quem está atrás.
- `c6` = Sim por inspeção do documento inteiro: não há marca "RETRACTED", nota ou página de retratação. A checagem externa (OpenAlex/Crossref) não foi feita, conforme o prompt.
- Nas evidências evitei, quando havia alternativa, trechos com palavras de ligadura tipográfica (fine, field, first, official), o que explica a escolha de trechos como "individual level variation in the cost of abstention" em vez do trecho que nomeia a multa.
- Li o PDF inteiro em três faixas de 20 páginas (PDF 1-20, 21-40, 41-60), o que cobre a capa e as páginas impressas 1 a 59, incluindo o apêndice.
