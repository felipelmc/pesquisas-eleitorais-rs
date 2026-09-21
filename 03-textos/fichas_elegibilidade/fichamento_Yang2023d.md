---
citekey: Yang2023d
ficha_id: Yang2023d
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Yang2023d.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_115
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — título e autores do documento batem com os metadados do registro (mesmo título, primeiro autor Fumeng Yang, estudo sobre as midterms de 2022); trata-se do preprint/manuscrito aceito, que é a versão registrada pelo DOI do OSF — evidência: "Swaying the Public? Impacts of Election Forecast Visualizations" (p. 1)
- **tipo_documento** — resposta: preprint — evidência: "Our preprint and supplements are available at" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores dos EUA (1.327 participantes recrutados em 15 estados com eleição para governador em 2022), respondendo sobre a disputa real do próprio estado — evidência: "involving 1,327 participants from 15 states" (p. 1); "reported that they registered to vote" (p. 6)
- **c2_intervencao_estudada** — resposta: Sim — a exposição é a previsão eleitoral baseada em pesquisas (modelo próprio sobre as polls do FiveThirtyEight), exibida em quatro visualizações de incerteza atribuídas aleatoriamente e analisada também segundo quem a previsão aponta como vencedor — evidência: "deployed four uncertainty visualizations for the election forecasts" (p. 1); "We use the polls collected and maintained by FiveThirtyEight" (p. 3)
- **c3_desfecho** — resposta: Sim — desfecho de comparecimento: intenção autodeclarada de votar (e percepção da intenção dos pares), medida nas ondas 2 e 3; não há medida de escolha de voto entre candidatos — evidência: "We evaluate two costly activities: voting and campaign contributions" (p. 5); "does this forecast make you more or less likely to vote" (p. 5)
- **c4_desenho_elegivel** — resposta: Sim — experimento online aleatorizado em painel longitudinal de três ondas, com a visualização da previsão sorteada por participante e desfechos medidos após a exposição — evidência: "We use a three-wave panel design and invite participants" (p. 5); "The visualization is randomly assigned on the" (p. 4)
- **c5_estudo_primario** — resposta: Sim — estudo primário, com coleta e análise próprias de dados quantitativos e qualitativos nas três ondas — evidência: "We conducted a longitudinal study during the 2022 U.S. midterm elections" (p. 1)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento — evidência: "Swaying the Public? Impacts of Election Forecast Visualizations" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: O documento remete ao próprio preprint e aos suplementos depositados no OSF (https://doi.org/osf.io/ajq8f), onde estão documentados os estudos preliminares, o pré-registro, dados e código; não menciona tese, dissertação, working paper anterior nem outro artigo com os mesmos dados — evidência: "Our preprint and supplements are available at" (p. 1); "The authors provide the following materials at" (p. 10)
- **fonte_dados_amostra** — resposta: Experimento online longitudinal de três ondas (Qualtrics + site de previsão próprio), de 18/10/2022 a 23/11/2022, com participantes recrutados na Prolific em 15 estados dos EUA com eleição para governador: 1.327 respostas na onda 1 (1.293 elegíveis), 1.020 na onda 2 e 884 na onda 3 — evidência: "running from Oct. 18, 2022 to Nov. 23, 2022" (p. 2); "In total, we collected 1,327 responses from 1,327 participants" (p. 6)
- **registro_financiamento** — resposta: Financiamento: NSF IIS-2107490, NSF IIS-1901485, NSF IIS-2126598 e NSF 2127309 (Computing Research Association, CIFellows Project). Há pré-registro das análises quantitativas, depositado nos suplementos do OSF (https://doi.org/osf.io/ajq8f), mas o documento não transcreve um identificador próprio de registro — evidência: "This research is supported by NSF IIS-2107490, NSF IIS-1901485" (p. 10); "The pilot data were used in pre-registration" (p. 6)

## Notas do codificador
- Paginação: o PDF tem 11 páginas e não traz numeração impressa em cabeçalho ou rodapé (conferido abrindo as páginas 1, 5 e 6). A numeração interna do próprio documento coincide com o índice do PDF, como mostram os retrolinks das referências (a ref. [86] remete às páginas 1, 2 e 8 e, de fato, é citada nessas três páginas do PDF; a ref. [24] remete à página 6, onde aparece o alfa de Cronbach). Por isso, `paginacao: indice-do-PDF` e `offset_pagina: 0`, com as duas páginas distantes exigidas conferidas (1 e 8).
- Documento com 11 páginas: lido por inteiro (páginas 1 a 11).
- `texto_confere` = Sim (e não "parcial"): título e lista de autores coincidem exatamente com os metadados do registro, e o registro é justamente o preprint no OSF (DOI 10.31219/osf.io/qpyna). O PDF é a versão de autor do manuscrito aceito na IEEE TVCG (os campos de publicação ainda estão como gabarito: "Manuscript received xx xxx. 201x"), e o próprio texto se apresenta como preprint, daí `tipo_documento` = preprint. O identificador do OSF citado no texto (ajq8f) é o do projeto com preprint e suplementos, distinto do DOI do registro.
- `c2`: a aleatorização é entre quatro formatos de visualização da mesma previsão, não entre previsão e ausência de previsão (não há grupo sem previsão). Ainda assim a exposição analisada é o resultado da previsão baseada em pesquisas: o modelo é descrito como meta-análise bayesiana de pesquisas, e as estimativas incluem a probabilidade de vitória, o vencedor previsto e a correção da previsão, com comparação explícita entre "D is predicted to win" e "R is predicted to win". Registro a ressalva aqui por afetar a comparabilidade, não a elegibilidade.
- `c3`: o desfecho elegível é só o de comparecimento (intenção de votar, própria e percebida nos pares). Emoções e confiança na previsão não são desfechos do protocolo, e o texto afirma que o experimento não intervém diretamente na decisão de voto ("Our experiment does not directly intervene in voting decisions", p. 2). Não há medida de escolha entre candidatos, então a célula de escolha de voto fica vazia para este relato.
- `c4`: além da aleatorização da visualização, o desenho é de painel individual com exposição medida antes do desfecho (onda 1 como linha de base, ondas 2 e 3 após a exposição), o que atende ao critério por dois caminhos.
- Nenhuma variável ficou em 999 e não há seções condicionais neste codebook (nenhum `NA_secao`).
