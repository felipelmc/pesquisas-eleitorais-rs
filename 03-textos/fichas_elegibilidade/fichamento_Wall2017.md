---
citekey: Wall2017
ficha_id: Wall2017
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/Desktop/pesquisas-eleitorais-rs/03-textos/pdfs/Wall2017.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_e6b_14
data_fichamento: 2026-09-24
---

## Identificacao
- **texto_confere** — resposta: Sim. Título e autores (Matthew Wall, Rory Costello, Stephen Lindsay) batem com o registro; é o manuscrito aceito (versão do autor, repositório Cronfa) do artigo da Electoral Studies, DOI 10.1016/j.electstud.2017.01.003 — evidência: "The miracle of the markets: Identifying key campaign events in the Scottish" (p. 2)
- **tipo_documento** — resposta: artigo (manuscrito aceito de artigo de periódico, Electoral Studies) — evidência: "This is an author produced version of a paper published in" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: parcial. O contexto é o referendo de independência da Escócia de 2014, mas as unidades analisadas são preços de mercados de apostas on-line (probabilidade implícita do Sim), não eleitores nem unidades eleitorais; as pesquisas de intenção de voto entram só como variável — evidência: "This paper analyses campaign dynamics in the 2014 Scottish independence referendum" (p. 4)
- **c2_intervencao_estudada** — resposta: parcial. A divulgação de pesquisas é analisada como exposição ("poll shock", desvio da pesquisa em relação ao esperado pelo mercado, pelo horário de divulgação), mas o efeito estimado é sobre os preços de apostas, não sobre eleitores — evidência: "measure the extent to which the release of each new poll" (p. 4); "of poll shocks on daily changes in market prices" (p. 21)
- **c3_desfecho** — resposta: Não. A variável dependente é a variação diária da probabilidade implícita do Sim nos mercados de apostas (expectativa de quem vence); não há desfecho de voto nem de comparecimento como efeito da exposição a pesquisas — evidência: "the dependent variable in this analysis is the daily" (p. 19); "the market-adjusted implied probability" (p. 13)
- **c4_desenho_elegivel** — resposta: Não. Série temporal observacional agregada (regressão das variações diárias de preços em choques de pesquisa e dummies de eventos), sem variação identificada da exposição nem painel individual — evidência: "a multivariate time series analysis" (p. 4)
- **c5_estudo_primario** — resposta: Sim. Análise própria de preços de 17 mercados de apostas coletados por raspagem e de pesquisas publicadas — evidência: "we developed an automated page scraping program" (p. 12)
- **c6_nao_retratado** — resposta: Sim. Não há aviso de retratação no documento — evidência: "The miracle of the markets" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Versões anteriores apresentadas na conferência EPOP 2014 (Universidade de Edimburgo) e na conferência anual da PSAI 2014 (Galway), sem referência bibliográfica; o documento é a versão do autor do artigo publicado na Electoral Studies (registro Cronfa 31712) — evidência: "comments and suggestions on earlier drafts of this paper" (p. 28); "This is an author produced version of a paper published in" (p. 1)
- **fonte_dados_amostra** — resposta: Preços de 17 mercados de apostas on-line (via oddschecker.com), coletados a cada 15 minutos durante a campanha oficial do referendo escocês (a partir de 30 de maio de 2014 até a véspera da votação de 18/09/2014), agregados em 100 dias (N = 100 na Tabela 2), combinados com pesquisas divulgadas (whatscotlandthinks.org; 6 institutos mais Opinium; N = 30 na Tabela 3) — evidência: "Prices were collected in this way every 15 minutes" (p. 12); "from 17 online gambling markets" (p. 12); "the public opinion analysis site www.whatscotlandthinks.org" (p. 14)
- **registro_financiamento** — resposta: Arts and Humanities Research Council (Big Data Projects Call, tema Digital Transformations), projeto "What are the odds?", grant AH/L010011/1; sem pré-registro — evidência: "the grant reference is: AH/L010011/1" (p. 28)

## Notas do codificador
- Paginação: usei o índice do PDF (offset 0) porque a evidência de título e de tipo de documento está nas páginas de capa (p. 1, capa do repositório Cronfa; p. 2, folha "Accepted Manuscript"), que não têm número impresso. O corpo tem numeração impressa, com impressa P = PDF P + 3 (confirmado: impressa 1 = resumo na p. 4 do PDF; impressa 16 = p. 19 do PDF; impressa 25 = agradecimentos na p. 28 do PDF).
- Qualidade do PDF: as páginas 2 a 34 têm MediaBox reduzida (612 x 709), e o topo de cada página (cerca de 3 a 4 linhas) está cortado, também na camada de texto. A folha de rosto com o título (p. 3) aparece só a partir de "Rory Costello"; parte da introdução e do início de várias seções (por exemplo, a abertura da seção 4 e a legenda da Tabela 4) não está visível. O que falta não muda a elegibilidade: resumo, método, Tabelas 2 a 4 e conclusão estão legíveis.
- As letras da marca d'água "ACCEPTED MANUSCRIPT" se intercalam na camada de texto; as evidências foram escolhidas para evitar esses pontos e trechos com ligaduras (ff, fi).
- c1 e c2 como 'parcial': o estudo é de campanha de referendo e trata a divulgação de pesquisas como choque informacional, mas quem "responde" são os preços dos mercados de apostas (escolha de mercado/finanças), não eleitores. c3 e c4 são 'Não' sem ambiguidade: o desfecho é a probabilidade de vitória implícita nas apostas (expectativa de quem vence) e o desenho é série temporal agregada sem variação identificada. O estudo não mede efeito de pesquisas sobre voto ou comparecimento.
- Nenhuma variável com 999.
