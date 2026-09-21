---
citekey: Stoetzer2024
ficha_id: Stoetzer2024
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Stoetzer2024.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_148
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o documento é o manuscrito aceito pelo autor (Author's Accepted Manuscript, datado de 20 de outubro de 2023, depositado no WRAP/University of Warwick) do mesmo trabalho registrado; o título bate com o do registro ("Voters' Expectations in Constituency Elections without Local Polls") e os autores que o documento traz são Lukas F. Stoetzer, Mark A. Kayser, Arndt Leininger e Andreas Murr — ou seja, o terceiro autor do registro ("Kayser, Mark Andreas Lindst Auml Dt") corresponde, no documento, a "Mark A. Kayser", segundo autor, sem o sufixo corrompido — evidência: "expectations in constituency" (p. 2); "elections without local polls" (p. 2)
- **tipo_documento** — resposta: artigo — research note de periódico, nesta versão de manuscrito aceito — evidência: "In this research note, we evaluate whether voters can rely" (p. 3); "published version or Version of Record" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores alemães entrevistados em survey pré-eleitoral nos 299 distritos, antes da eleição federal de 26 de setembro de 2021, que escolhem/avaliam candidatos de distrito — evidência: "we sampled at least 20 respondents" (p. 6); "the sample contains 6448 respondents" (p. 6)
- **c2_intervencao_estudada** — resposta: Sim — o resultado de uma pesquisa eleitoral nacional (Sonntagsfrage, a pesquisa mais recente sobre apoio partidário) é exibido de forma aleatorizada como tratamento, isolado ou combinado com o resultado do distrito na eleição anterior — evidência: "randomly displaying national election polls" (p. 4); "the most recent national poll about party support" (p. 7)
- **c3_desfecho** — resposta: Não — o único desfecho é a acurácia da expectativa do eleitor sobre o resultado do distrito (quem vence e qual a participação de votos esperada de cada candidato), medida por erro absoluto médio; não há medida de intenção/escolha de voto do próprio respondente nem de comparecimento — evidência: "expected vote share of the candidates as a percentage" (p. 6); "the average expected and final vote share of constituency candidates" (p. 8)
- **c4_desenho_elegivel** — resposta: Sim — experimento aleatorizado embutido em survey, com desenho intraindividual pré-teste/pós-teste e três grupos de tratamento informacional — evidência: "The survey included a within subject pretest-posttest" (p. 3); "This creates three experimental groups" (p. 7)
- **c5_estudo_primario** — resposta: Sim — estudo primário com survey próprio e análise própria dos dados coletados pelos autores — evidência: "The respondents in our survey were recruited from an online-access-panel provider" (p. 5)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação em nenhuma das 44 folhas do PDF — evidência: "elections without local polls" (p. 2)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim — o documento cita o plano de pré-análise do mesmo estudo (Stoetzer, 2021, "Pre-analysis Plan Citizen forecasting of the German Federal Elections 2021", OSF) e declara ser o manuscrito aceito, que pode diferir da versão publicada (Version of Record) — evidência: "were pre-registered (Stoetzer, 2021)" (p. 6); "Citizen forecasting of the German Federal Elections 2021" (p. 15)
- **fonte_dados_amostra** — resposta: Survey online pré-eleitoral com experimento intraindividual pré/pós-teste, painel online (Respondi), com ao menos 20 respondentes em cada um dos 299 distritos alemães, 6448 respondentes no total, em campo de 3 a 22 de setembro de 2021, antes da eleição federal alemã de 26 de setembro de 2021 — evidência: "the sample contains 6448 respondents" (p. 6); "The field time covered the last three weeks" (p. 6)
- **registro_financiamento** — resposta: Pré-registro na OSF, plano de pré-análise em http://osf.io/4e96d; o documento não traz número de processo, edital ou qualquer menção a financiamento — evidência: "http://osf.io/4e96d" (p. 15)

## Notas do codificador

**Paginação.** O PDF tem duas numerações impressas independentes: o corpo do artigo numera 1 a 13 nas folhas 3 a 15 do PDF (offset +2), e os Supplementary Materials reiniciam em 1 na folha 18 e vão até 27 na folha 44 (offset +17). As folhas 1 (capa do repositório WRAP), 2 (folha de rosto), 16 (rosto dos Supplementary Materials) e 17 (sumário dos SM) não têm numeração impressa. Como não existe offset único válido para o documento inteiro, declarei `paginacao: indice-do-PDF` com `offset_pagina: 0`: todos os números de página citados nas evidências são o índice da folha do PDF (1-based), de modo que `folha_do_PDF = pagina_anotada + 0`. Conferi cada citação na folha indicada pela fórmula: p. 1 = capa WRAP; p. 2 = folha de rosto com o título; p. 3 = impressa 1; p. 4 = impressa 2; p. 5 = impressa 3; p. 6 = impressa 4; p. 7 = impressa 5; p. 8 = impressa 6; p. 12 = impressa 10; p. 15 = impressa 13.

**texto_confere = parcial.** O conteúdo é o mesmo trabalho do registro (mesmo título, mesmos quatro autores, mesmo estudo), mas a folha 1 declara explicitamente que esta é a versão de manuscrito aceito depositada no WRAP e que pode diferir da versão publicada. Por isso `parcial` (outra versão do mesmo trabalho), e não `Sim`. Sobre o metadado corrompido: o documento traz, nas folhas 2 e 16, os autores como Lukas F. Stoetzer, Mark A. Kayser, Arndt Leininger e Andreas Murr — não há no documento nenhuma forma parecida com "Mark Andreas Lindst Auml Dt"; o nome do segundo autor aparece sempre como "Mark A. Kayser". Não citei a linha de autores como evidência porque as instruções vedam usar a lista de autores como citação verbatim (e ela está em versalete, com marcadores de afiliação sobrescritos).

**c3_desfecho = Não.** Este é o critério decisivo para o texto. O desenho é um experimento legítimo de exposição a resultado de pesquisa eleitoral (c2 = Sim) com desenho elegível (c4 = Sim), mas a variável dependente é exclusivamente a acurácia da expectativa do eleitor sobre o resultado do distrito: o erro absoluto médio entre a participação de votos esperada e a final dos candidatos, e o acerto sobre qual candidato vence. O codebook lista "expectativa de quem vence" entre os desfechos que obrigam a resposta `Não`, e não há no documento nenhuma medida de intenção ou escolha de voto do próprio respondente, nem de comparecimento, nem em análise secundária — os próprios autores registram, na discussão (folha 12), que a nota não trata das consequências de expectativas imprecisas e que a influência sobre voto estratégico fica como agenda futura ("our research note does not speak to the potential consequences", p. 12). Não apliquei `parcial` porque não há parte alguma da amostra ou análise com desfecho de voto ou comparecimento.

**c6_nao_retratado.** Li as 44 folhas do PDF em três faixas (1-20, 21-40, 41-44) e não encontrei marca "RETRACTED", nota ou página de retratação. A checagem externa em OpenAlex/Crossref não é minha, conforme o prompt da variável.

**registro_financiamento.** O pré-registro está identificado (OSF, http://osf.io/4e96d, citado na folha 6 como "pre-registered (Stoetzer, 2021)" e detalhado na referência da folha 15). Não há seção de agradecimentos nem qualquer menção a financiamento, número de processo ou edital no corpo, nas notas de rodapé ou nos Supplementary Materials — por isso a resposta registra apenas o pré-registro, sem `999` para a variável como um todo.

**Nenhuma variável recebeu 999 e nenhuma recebeu NA_secao** (o projeto não usa classificador nem seções condicionais; ficha única).

**Escolha das citações.** Preferi trechos curtos, contíguos dentro de uma mesma linha impressa e sem palavras com ligaduras tipográficas (ff, fi, fl, ffi, ffl) — por isso evitei, por exemplo, "party affiliation", "differ" e "The difference in these effects", que aparecem nas mesmas passagens. Também evitei o apóstrofo tipográfico de "Voters'" no título, citando o título em dois fragmentos contíguos da folha 2.
