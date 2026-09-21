---
citekey: Unkelbach2022a
ficha_id: Unkelbach2022a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Unkelbach2022a.pdf
paginacao: impressa
offset_pagina: -50
agente_fichador: elegib-opus5-070
data_fichamento: 2026-09-19
---

## Identificacao
- **texto_confere** — resposta: Sim; título e primeiro autor (Fabienne Unkelbach) batem com o registro; publicado online em 10/08/2022 (volume impresso de 2023) — evidência: "Jumping on the Bandwagon" (p. 51); "Poll Effects in the Context of the 2021 German Federal Election" (p. 51)
- **tipo_documento** — resposta: artigo (Politische Vierteljahresschrift, 64:51-78, seção Critical Paper) — evidência: "Accepted: 4 July 2022" (p. 51)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim; eleitores alemães aptos a votar na eleição federal de 2021, entrevistados no GLES Rolling Cross-Section, com intenção de voto nos seis partidos do Bundestag — evidência: "were eligible to vote in the federal election of 2021" (p. 58)
- **c2_intervencao_estudada** — resposta: Sim; a exposição analisada é o resultado de pesquisas pré-eleitorais publicadas (intenção de voto majoritária, CMVI), casado a cada dia de campo pelo calendário de publicação, além da percepção autodeclarada de ter visto pesquisas na última semana — evidência: "we combined the RCS data with results of published preelection polls" (p. 59)
- **c3_desfecho** — resposta: Sim; desfecho de voto (intenção de voto individual, uma dummy por partido); não há desfecho de comparecimento — evidência: "The outcome, voting intention, was operationalized through a dummy variable" (p. 64)
- **c4_desenho_elegivel** — resposta: parcial; rolling cross-section individual casado com as pesquisas publicadas no dia anterior (variação diária pelo calendário de divulgação, com checagem t-1 vs t+1), mas sem experimento nem painel, e os autores admitem que o desenho só permite examinar correlações — evidência: "a lag of 1 day was chosen" (p. 59); "One could argue that our study design only allows examination of correlations" (p. 59); "we used multilevel logistic regressions" (p. 63)
- **c5_estudo_primario** — resposta: Sim; estudo primário com análise própria dos microdados do GLES RCS 2021 combinados com pesquisas publicadas — evidência: "The RCS is a large-scale, cross-sectional survey based on phone interviews" (p. 58); "the analysis dataset consisted of 5291 respondents" (p. 67)
- **c6_nao_retratado** — resposta: Sim; não há aviso de retratação no documento — evidência: "Jumping on the Bandwagon" (p. 51)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: GLES Rolling Cross-Section 2021 (entrevistas telefônicas pré-eleitorais de 2/8/2021 a 25/9/2021, 55 dias de campo, 7068 respondentes; 5291 na análise) combinado com as pesquisas de oito institutos obtidas no Wahlrecht.de — evidência: "between August 2, 2021, and September 25, 2021" (p. 59); "This resulted in a total sample size of 7068 respondents" (p. 59); "the analysis dataset consisted of 5291 respondents" (p. 67)
- **registro_financiamento** — resposta: Pré-registro no OSF (https://osf.io/g6r7v/); financiamento declarado só para o acesso aberto (Projekt DEAL), sem número de processo — evidência: "The preregistration can be accessed on osf.io" (p. 58); "Open Access funding enabled and organized by Projekt DEAL" (p. 75)

## Notas do codificador
- Paginação: o artigo ocupa as páginas impressas 51 a 78 do volume 64 (2023) da Politische Vierteljahresschrift. A página 1 do PDF é a impressa 51 (o cabeçalho traz 64:51-78); conferi a impressa 52 na p. 2 do PDF, a 67 na p. 17 e a 78 na p. 28. Logo offset_pagina = -50 (impressa P → PDF = P - 50).
- texto_confere: o registro dá 2022 e o documento traz "Published online: 10 August 2022" com volume impresso de 2023; é o mesmo trabalho, por isso Sim. Evitei na evidência o trecho do título com o apóstrofo tipográfico (Voters’).
- c2: as pesquisas publicadas são o preditor central (CMVI, nível 2), com variação entre dias de campo segundo a data de publicação; não aparecem só como contexto. Também há um item de percepção (ter lido ou visto pesquisas na última semana, p. 61), usado numa checagem de robustez.
- c4 (decisão limítrofe, marcada como parcial): o desenho usa a variação diária das pesquisas publicadas (calendário de divulgação) em dados individuais de rolling cross-section, com defasagem de 1 dia, defasagens de 0 e 2 dias como análises exploratórias e comparação com as pesquisas publicadas no dia seguinte (t-1 vs t+1) como teste de direção causal. Não é experimento nem painel individual, e a variação da exposição não vem de embargo nem de fuso horário. Os próprios autores dizem que o desenho só permite examinar correlações (p. 59) e que não houve evidência da direção causal (p. 73). Não é uma simples tendência de pesquisas comparada ao resultado, mas também não é um quase-experimento claramente identificado; fica para arbitragem humana.
- c3: a categoria de referência da dummy de voto junta outros partidos, indecisos, quem não votaria e voto nulo (p. 60); não há desfecho de comparecimento analisado.
- outros_relatos_mesmo_estudo = 999: o documento não menciona versão anterior, tese, working paper nem outro artigo com os mesmos dados. Menciona só o pré-registro e o suplemento online no OSF (p. 58 e nota 17, p. 67), que são material do próprio artigo e estão registrados em registro_financiamento. Faas et al. (2008) e Hoffmann e Klein (2013) usam RCS de outras eleições (2005 e 2009), não estes dados.
- Documento lido por inteiro (PDF 1-28, impressas 51-78).
