---
citekey: Fairstein2018a
ficha_id: Fairstein2018a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Fairstein2018a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: elegib-opus5-019
data_fichamento: 2026-09-19
---

## Identificacao
- **texto_confere** — resposta: Sim — evidência: "Predicting Strategic Voting Behavior with Poll Information" (p. 1)
- **tipo_documento** — resposta: preprint — evidência: "arXiv:1805.07606v1" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, participantes humanos de jogo eleitoral online controlado, com 3 candidatos, preferências induzidas, regra de pluralidade e informação de pesquisa (poll). — evidência: "Each subject played up to 20 rounds of voting with 3 candidates" (p. 7)
- **c2_intervencao_estudada** — resposta: Sim, a informação de pesquisa (poll) varia entre as rodadas dos experimentos controlados de Tal et al. e é a entrada analisada dos modelos de decisão de voto (análise secundária desses dados). — evidência: "that vary the number of voters, the poll information" (p. 2); "The poll provided a noisy indication of the results of the voting." (p. 7)
- **c3_desfecho** — resposta: Sim, desfecho de voto: a escolha de candidato em cada rodada (Q, Q' ou Q''), prevista pelos modelos; não há desfecho de comparecimento. — evidência: "make a single voting decision under the Plurality rule" (p. 2)
- **c4_desenho_elegivel** — resposta: parcial, análise secundária de dados de experimento online controlado com cenários de pesquisa variando entre rodadas, mas o artigo ajusta e compara modelos preditivos (leave-one-out) sem descrever aleatorização nem estimar o efeito da pesquisa por comparação entre níveis de exposição. — evidência: "several voting scenarios in controlled experiments involving humans" (p. 7); "The prediction was performed using leave-one-out method" (p. 8)
- **c5_estudo_primario** — resposta: Sim, estudo empírico com análise própria (ajuste e avaliação de modelos) de dados experimentais publicados por Tal et al. — evidência: "an extensive evaluation of various decision models on real-world data" (p. 2)
- **c6_nao_retratado** — resposta: Sim, não há aviso de retratação no documento. — evidência: "Predicting Strategic Voting Behavior with Poll Information" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Os dados vêm de outro relato do mesmo experimento: Tal, Meir e Gal, "A study of human behavior in online voting", AAMAS 2015 (versão completa em https://tinyurl.com/yczxugoj), que também identificou os tipos de eleitor usados no modelo TMG; nenhuma outra versão do próprio artigo é mencionada. — evidência: "We use the data of Tal et al." (p. 2); "A study of human behavior in online voting" (p. 14)
- **fonte_dados_amostra** — resposta: Experimento online controlado de votação de Tal et al. (parte dos dados pública em votelib.org), com 595 sujeitos que jogaram até 20 rodadas cada, com 3 candidatos; período de coleta não informado. — evidência: "The data was obtained from 595 distinct subjects." (p. 7)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: o PDF (preprint arXiv v1, 17 páginas) não tem numeração impressa em nenhuma página (conferido na p. 1, na p. 9 de resultados e na p. 15 do apêndice); por isso paginacao = indice-do-PDF e offset_pagina = 0.
- texto_confere = Sim: título e autores (Fairstein, Lauz, Gal, Meir) batem com o registro; o carimbo arXiv:1805.07606v1 de 19 May 2018 bate com o DOI 10.48550/arxiv.1805.07606 e o ano.
- c2 e c4: o artigo não conduz o experimento; reanalisa os dados de Tal et al. [16], em que a informação de pesquisa varia entre rodadas (seis cenários de ordem dos candidatos no poll, tamanhos de poll de n < 10 a n ≈ 10000). A pesquisa é central na análise (entrada de todos os modelos), por isso c2 = Sim. Em c4 marquei parcial porque o documento não descreve aleatorização da informação de pesquisa e o objetivo é ajuste preditivo de modelos de decisão (f-measure), não estimar o efeito da pesquisa sobre o voto por comparação entre níveis de exposição; a Tabela 2 e as matrizes de confusão (Figura 4) trazem, porém, as escolhas por cenário de pesquisa, o que pode permitir essa comparação. Decisão final fica para a arbitragem.
- c5 = Sim: análise própria de dados alheios (secundária), não uma revisão.
- registro_financiamento = 999: não há agradecimentos, número de projeto nem pré-registro no documento.
