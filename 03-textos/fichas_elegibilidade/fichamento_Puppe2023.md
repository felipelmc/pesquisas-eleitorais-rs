---
citekey: Puppe2023
ficha_id: Puppe2023
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Puppe2023.pdf
paginacao: impressa
offset_pagina: 2
agente_fichador: fichador_el_171
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial, é o working paper do KIT nº 155 (fevereiro de 2022) do mesmo trabalho registrado como capítulo de 2023 (DOI 10.1007/978-3-031-21696-1_21), com o mesmo título e os mesmos autores (Clemens Puppe e Jana Rollmann) — evidência: "Participation in Voting over Budget Allocations." (p. 1)
- **tipo_documento** — resposta: working_paper — evidência: "Working Paper Series in Economics" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: parcial, são estudantes do KIT votando de verdade sobre a alocação de uma doação entre dois projetos do campus, isto é, um eleitorado real com decisão de comparecer, mas as opções são valores de orçamento e não candidatos, partidos ou pergunta de referendo ou plebiscito — evidência: "We invited 510 subjects to participate in a vote over the allocation" (p. 12)
- **c2_intervencao_estudada** — resposta: Não, a exposição analisada é a regra de agregação dos votos (média contra mediana), não resultado de pesquisa eleitoral; o documento não trata de pesquisa pré-eleitoral, agregador, projeção ou boca de urna — evidência: "The treatment variable was the collective decision rule employed." (p. 1)
- **c3_desfecho** — resposta: Sim, desfecho de comparecimento: a taxa de participação (voter turnout) dos convidados sob cada regra de votação, sem medida de voto em candidato ou partido — evidência: "Our main focus are the participation rate and the role" (p. 12)
- **c4_desenho_elegivel** — resposta: Sim, experimento de campo aleatorizado, com designação ao acaso dos convidados às duas regras de votação — evidência: "assigned to the mean rule, and 255 to the median rule." (p. 13)
- **c5_estudo_primario** — resposta: Sim, estudo primário com dados próprios coletados em experimento de campo conduzido pelos autores — evidência: "The field experiment went on for one week in July 2017" (p. 12)
- **c6_nao_retratado** — resposta: Sim, não há marca 'RETRACTED', nota nem página de retratação em nenhuma das 42 folhas do PDF — evidência: "Participation in Voting over Budget Allocations." (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim, o texto declara basear-se em dois capítulos da tese de doutorado da segunda autora, referenciada como Rollmann, J. (2020), Voting over Resource Allocation: Nash Equilibria and Costly Participation, PhD thesis, Karlsruhe Institute of Technology (KIT) — evidência: "This work is based on Chapters 2 and 3 of the second" (p. 1)
- **fonte_dados_amostra** — resposta: Experimento de campo no Karlsruhe Institute of Technology, uma semana de julho de 2017, com 510 estudantes convidados divididos em 30 grupos de 17 membros, dos quais 140 votaram (74 sob a regra da média e 66 sob a da mediana) sobre a alocação de 100 Euros entre a oficina de bicicletas e a horta do campus — evidência: "510 subjects which were divided into 30 groups of 17 members each." (p. 13)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
Offset. A folha 3 do PDF traz o número impresso 1 (página de rosto do corpo, com título, autores e resumo) e a folha 41 traz o número impresso 39 (última figura do apêndice): em ambos os casos folha do PDF = página impressa + 2, de modo que `offset_pagina: 2`. Conferi a fórmula contra cada citação desta ficha: p. 1 → folha 3, p. 12 → folha 14, p. 13 → folha 15. As três folhas de capa e contracapa do KIT (folhas 1, 2 e 42) não têm numeração impressa; pela fórmula elas correspondem às páginas -1, 0 e 40, e a evidência de `tipo_documento` foi anotada como p. 0 (folha 2, o Impressum), conforme a instrução de usar o número que satisfaz a fórmula mesmo quando for zero ou negativo. O documento tem 42 folhas e foi lido por inteiro (folhas 1 a 42), em três faixas.

texto_confere. O registro descreve o capítulo de livro de 2023 (Springer, DOI 10.1007/978-3-031-21696-1_21); o PDF baixado é a versão prévia do mesmo trabalho na série de working papers do KIT, nº 155, de fevereiro de 2022. Título e autoria coincidem, o ano e o veículo não, daí `parcial` e não `Sim`. Pela mesma razão `tipo_documento` foi codificado pelo que o próprio documento declara (working_paper), e não pelo tipo do registro.

c1. Decisão limítrofe. A favor de atender: é um pleito real, com convite por e-mail a 510 eleitores, decisão voluntária de comparecer e apuração coletiva, e não uma escolha de consumo, de mercado ou de finanças (o texto é explícito em que não há pagamento individual), nem votação de órgão deliberativo real. Contra: o objeto da votação é a repartição de 100 Euros entre dois projetos de campus, isto é, uma alocação contínua de orçamento, e não candidatos, partidos ou uma pergunta de referendo ou plebiscito. Como a ambiguidade é sobre o próprio objeto da escolha, registrei `parcial` em vez de forçar `Sim` ou `Não`.

c2. É o critério que exclui o texto sem margem de dúvida: nenhum resultado de pesquisa eleitoral é manipulado, explorado como variação natural ou medido no indivíduo. O tratamento é a regra de agregação (média contra mediana). As crenças que o estudo elicita são sobre o próprio impacto do voto, sobre o resultado da alocação e sobre o número de participantes do grupo, todas colhidas em questionário posterior ao voto, e não exposição a divulgação de pesquisa.

c3. Respondi `Sim` porque o desfecho principal do estudo é a taxa de participação, que o próprio texto chama de voter turnout e analisa em regressão da variável dicotômica de participação. Não há desfecho de voto em candidato, partido ou opção de referendo: a variável de voto analisada é o valor alocado à oficina de bicicletas.

c4. O desenho, isolado, está entre os aceitos (experimento aleatorizado de campo). O critério trata do desenho, não do conteúdo da exposição, que é o que falha em c2.

registro_financiamento. A nota de rodapé de agradecimentos da p. 1 lista apresentações em congressos e seminários e agradece pessoas nomeadas, mas não traz número de processo, edital, financiador nem identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP); o restante do texto e o apêndice também não. Daí 999, e não ausência por omissão minha.
