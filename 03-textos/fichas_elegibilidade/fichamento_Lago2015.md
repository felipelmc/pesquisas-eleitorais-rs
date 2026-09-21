---
citekey: Lago2015
ficha_id: Lago2015
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Lago2015.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_155
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o título e os três autores batem com o registro (Regulating Disinformation; Lago, Guinjoan, Bermúdez), mas o PDF é a versão de manuscrito do trabalho (contagem de palavras, running header, marcadores "[INSERT TABLE ... ABOUT HERE]", tabelas e figuras ao final), não o artigo diagramado do periódico indicado pelo DOI — evidência: "REGULATING DISINFORMATION:" (p. 1)
- **tipo_documento** — resposta: artigo — evidência: "This article examines the political consequences" (p. 4)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, analisa eleitores em eleições reais (surveys de painel em Barcelona, Madri e Quebec) e unidades eleitorais agregadas (eleições nacionais em 46 democracias) — evidência: "we rely on Internet panel surveys conducted by the" (p. 17); "held in a sample of 46 democracies" (p. 11)
- **c2_intervencao_estudada** — resposta: Sim, a exposição analisada é a restrição legal à divulgação de pesquisas (número de dias de embargo antes da eleição, no nível agregado, e o período de embargo no nível individual) — evidência: "The key independent variables are poll embargo and party-system" (p. 13); "Pre-Election Day poll restriction has been operationalized as the Number" (p. 13)
- **c3_desfecho** — resposta: Sim, desfecho de voto: a análise agregada tem como variável dependente o percentual de votos desperdiçados (votação agregada em partidos sem representação) na última eleição legislativa de cada país; o desfecho da análise individual é a acurácia das expectativas sobre as chances dos partidos, que não conta — evidência: "The dependent variable is the percentage of wasted votes" (p. 12)
- **c4_desenho_elegivel** — resposta: Sim, pelo menos uma análise usa variação identificada da exposição: no nível individual compara os respondentes entrevistados nos dias de embargo legal com os entrevistados quando a publicação é permitida, em três eleições (Barcelona, Madri e Quebec, esta última como caso sem embargo); a análise agregada, porém, é observacional de corte transversal estimada por MQO, sem variação identificada — evidência: "In Barcelona and Madrid, we have created a dummy" (p. 19); "Estimation is by OLS with robust standard errors" (p. 14)
- **c5_estudo_primario** — resposta: Sim, é estudo primário com análise própria de dados agregados de 46 democracias e de dados individuais de surveys de painel — evidência: "Relying on aggregated data from the most recent Lower House elections" (p. 6)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação no documento — evidência: "POLL EMBARGO AND ELECTORAL COORDINATION" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Duas fontes: dados agregados da eleição legislativa mais recente em 46 democracias (Tabela A1, eleições de 2009 a 2013) e surveys de painel pela internet do Making Electoral Democracy Work Project, com 773 entrevistados em Barcelona e 976 em Madri na eleição nacional espanhola de 2011 e 990 entrevistados na eleição provincial de Quebec de 2012 — evidência: "the last Lower-House election held in a sample of 46 democracies" (p. 11); "Two representative samples of 773 and 976 individuals were respectively interviewed" (p. 17); "The representative sample includes 990 interviewees" (p. 17)
- **registro_financiamento** — resposta: Projeto de pesquisa CSO2010-1639 do Ministério da Ciência e Inovação da Espanha; o estudo integra o Making Electoral Democracy Work project. Não há identificador de pré-registro no documento — evidência: "research project CSO2010-1639" (p. 3)

## Notas do codificador
- **Paginação e offset.** A numeração impressa aparece no canto superior direito de todas as folhas e coincide com o índice do PDF: folha 1 traz "1", folha 20 traz "20", folha 39 traz "39" e folha 40 traz "40". Logo `offset_pagina: 0` e `paginacao: impressa`. Validei a fórmula `folha_do_PDF = pagina_anotada + offset_pagina` contra todas as páginas citadas nesta ficha (1, 3, 4, 6, 11, 12, 13, 14, 17 e 19): em cada uma o número impresso no topo é igual ao índice da folha lida, e cada trecho citado está na folha que a fórmula indica.
- **texto_confere = parcial.** Não é discrepância de trabalho: título e autoria batem com os metadados. O arquivo é a versão de manuscrito (p. 1 sem periódico, p. 2 com "[Word count: 6286]" e "Running header", marcadores "[INSERT TABLE 1 ABOUT HERE]" no corpo, tabelas e figuras agrupadas ao final, p. 31 a 40). Por isso as páginas citadas aqui não correspondem à paginação do artigo publicado sob o DOI do registro.
- **tipo_documento.** Classifiquei como `artigo` porque é assim que o próprio documento se declara ("This article", p. 4; "In this paper", p. 5) e porque não há folha de rosto de série de working papers nem nota de preprint. O formato de manuscrito está registrado na nota acima.
- **c3.** O documento tem dois desfechos. O agregado, percentual de votos desperdiçados, é votação agregada em partidos (os que não obtêm representação) e atende ao critério. O individual, acurácia das percepções sobre as chances de vitória dos partidos, é expectativa de quem vence e, sozinho, não atenderia. Pela convenção do projeto (basta uma análise atender), respondi Sim.
- **c4.** Decisão limítrofe. A análise agregada é exatamente o caso que o prompt manda excluir: corte transversal observacional de 46 países, por MQO com erros robustos, sem variação identificada da exposição. A análise individual, ao contrário, usa a proibição legal de divulgação (cinco dias na Espanha, só o dia da eleição em Quebec) como variação identificada, com dummy para os dias de embargo e Quebec funcionando como caso de comparação sem embargo (p. 17 a 19). Apliquei a convenção "basta uma análise atender" e respondi Sim, mas registro para o coordenador que o desenho elegível (c4) e o desfecho elegível (c3) estão em análises diferentes do mesmo documento: a parte com variação identificada mede expectativas, não voto.
- **outros_relatos_mesmo_estudo = 999.** O documento não menciona versão anterior, tese, working paper ou relatório do mesmo estudo. Cita Guinjoan et al. (2014) como pesquisa prévia (p. 9 e p. 29) e o Making Electoral Democracy Work Project como origem dos surveys, mas em nenhum momento afirma que aquele artigo usa os mesmos dados; concluir isso seria inferência, então marquei 999.
- Li o PDF inteiro, em duas faixas (folhas 1 a 20 e 21 a 40).
