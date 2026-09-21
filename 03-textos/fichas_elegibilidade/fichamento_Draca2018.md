---
citekey: Draca2018
ficha_id: Draca2018
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Draca2018.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_099
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — evidência: "How Polarized are Citizens?" (p. 1)
- **tipo_documento** — resposta: working_paper — evidência: "WORKING PAPER SERIES" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Não — a amostra é de respondentes do World Values Survey/European Values Study em 17 países, analisados como público geral por suas posições em temas (aborto, imigração, confiança em instituições), sem escolha entre candidatos, partidos ou opções de referendo e sem unidades eleitorais agregadas. — evidência: "develop a set of 17 countries in Europe and North America" (p. 7); "beliefs amongst the general public" (p. 3)
- **c2_intervencao_estudada** — resposta: Não — não há resultado de pesquisa eleitoral como exposição; o objeto empírico são as respostas de survey de valores tratadas como "issue-positions" e modeladas por aprendizado não supervisionado, sem manipulação, variação natural identificada ou medida individual de exposição a pesquisa. — evidência: "polarisation using unsupervised machine learning tools as applied to" (p. 2); "the main objects of analysis in our application" (p. 3)
- **c3_desfecho** — resposta: Não — os desfechos são as participações latentes de tipos ideológicos, o "citizen slant" (concentração Gini intrapessoal) e a medida de polarização de Esteban-Ray; não há intenção de voto, escolha de voto, votação agregada nem comparecimento. — evidência: "the type shares for one of the 4 types created by LDA" (p. 46); "We calculate the polarization measure separately for each country and wave" (p. 25)
- **c4_desenho_elegivel** — resposta: Não — o desenho é observacional, com cortes transversais repetidos do WVS/EVS, modelo LDA não supervisionado e regressões descritivas com efeitos fixos de país e dummies de onda, sem aleatorização, sem variação identificada de exposição e sem painel individual. — evidência: "we run some simple regressions of the type shares on individual" (p. 19); "Each column reports the regression results for individual level regression" (p. 46)
- **c5_estudo_primario** — resposta: Sim — estudo primário: os autores estimam seus próprios modelos e regressões sobre os microdados do WVS/EVS. — evidência: "For our main analysis, we use data from the World Values Survey" (p. 7); "to represent the answers to the survey questions as discrete" (p. 7)
- **c6_nao_retratado** — resposta: Sim — não há marca "RETRACTED", nota ou página de retratação em nenhuma parte do documento. — evidência: "How Polarized are Citizens?" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Integrated Values Survey (World Values Survey combinado com o European Values Study), 17 países da Europa e da América do Norte, 29 questões recodificadas em 58 posições, 82,338 observações em 3 ondas entre 1989 e 2010. — evidência: "82,338 observations over 3 waves spanning the years from 1989 to 2010" (p. 7)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador

Leitura: o documento tem 74 páginas no PDF e foi lido por inteiro, em faixas de 20 páginas (1-20, 21-40, 41-60, 61-74). A regra de leitura parcial para documentos com mais de 300 páginas não se aplica.

Paginação e offset. A página 1 do PDF é a capa da série de working papers do CAGE/Warwick, sem numeração impressa; a numeração impressa do corpo começa na página 2 do PDF. Offset confirmado em três páginas distantes: PDF 2 = impressa 1 (título e resumo), PDF 20 = impressa 19 (seção 4.4) e PDF 48 = impressa 47 (Tabela 5). Logo, impressa P = PDF P+1, `offset_pagina: 1`. Atenção do coordenador: os apêndices reiniciam a numeração impressa em 1 (PDF 50 = apêndice impressa 1, offset 49 nessa parte). Para evitar ambiguidade, todas as evidências desta ficha vêm do corpo do texto (impressas 1 a 48), onde vale o offset 1.

Citação da capa em `tipo_documento`. A única declaração do tipo de documento está na folha de rosto, que não tem número impresso. Aplicando a convenção de offset (impressa P -> PDF P+1), a capa corresponde a P = 0, e foi assim que a registrei; a citação "WORKING PAPER SERIES" está na página 1 do PDF. Se o gate não aceitar página 0, o trecho equivalente é o índice 1 do PDF.

texto_confere. Título ("How Polarized are Citizens? Measuring Ideology from the Ground-Up") e autores ("Mirko Draca and Carlo Schwarz") batem com os metadados do registro, e a data impressa na página de rosto do artigo é "April 2, 2018", compatível com o ano 2018 do registro. Registro para o coordenador: a capa da série traz "Jul 2019" e "No.432", isto é, o arquivo é a versão distribuída como CAGE Working Paper, enquanto o registro aponta um preprint de SSRN de 2018 com o mesmo título, autores e data interna. Por isso respondi "Sim" (mesmo trabalho, mesma data interna) e não "parcial"; se o protocolo do projeto tratar capa de série como versão distinta, o valor viraria "parcial".

c1 a c4 = Não. O texto mede ideologia latente a partir de respostas a 29 questões de valores (aborto, prostituição, imigração, papel do governo, confiança em instituições) e não a partir de escolha entre candidatos, partidos ou opções de referendo; não há pesquisa eleitoral como exposição em nenhum momento (as pesquisas do WVS/EVS são a fonte de dados, não o tratamento); os desfechos são participações de tipos ideológicos, concentração intrapessoal ("citizen slant") e polarização; e o desenho é observacional agregado/individual sem variação identificada da exposição, o que o coloca fora da lista de desenhos aceitos. Nenhum dos quatro casos é ambíguo o bastante para "parcial": não há, em nenhuma parte do documento, um estudo ou análise secundária que envolva pesquisa eleitoral ou voto.

c5 = Sim mesmo com c1 a c4 = Não, conforme a convenção do projeto de responder cada critério isoladamente: o documento traz análise própria de microdados (modelos LDA por onda, regressões das participações de tipos e do Gini intrapessoal, medida de polarização calculada pelos autores).

999. `outros_relatos_mesmo_estudo`: o documento não menciona versão anterior, tese, relatório técnico ou artigo irmão com os mesmos dados; as autorreferências dos autores não aparecem. `registro_financiamento`: não há número de pré-registro (OSF, AEA, RIDIE, EGAP) nem número de processo ou edital no texto; a capa exibe apenas os logotipos do CAGE e do ESRC, sem identificador escrito, e as notas de rodapé da primeira página trazem só as afiliações.

Escolha das citações. Preferi trechos curtos, contíguos e sem ligaduras tipográficas (ff, fi, fl); por isso evitei, por exemplo, "we offer a new approach" (ff) e "the Gini Coefficient of the individual type shares" (ffi), substituindo-os por trechos equivalentes das mesmas passagens. Todas as páginas citadas foram reabertas e conferidas na numeração impressa.
