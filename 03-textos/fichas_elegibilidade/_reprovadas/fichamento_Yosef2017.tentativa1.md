---
citekey: Yosef2017
ficha_id: Yosef2017
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Yosef2017.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_134
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — o título, o primeiro autor (David Ben Yosef), o ano (2017) e o DOI (10.1145/3106426.3106532) impressos no documento batem com os metadados do registro — evidência: "Haste Makes Waste: a Case to Favour Voting Bots" (p. 1)
- **tipo_documento** — resposta: evento — trabalho publicado nos anais de conferência (WI '17, ACM), identificado no cabeçalho corrente de todas as páginas e no bloco de copyright da primeira página — evidência: "2017, Leipzig, Germany" (p. 2)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — estudantes participam, como eleitores com preferências induzidas sorteadas, de jogos eleitorais on-line em que escolhem entre candidatos por voto de pluralidade — evidência: "A total of 72 students played a total of 264 games" (p. 5); "7 voters per game, 5 candidates" (p. 4)
- **c2_intervencao_estudada** — resposta: parcial — o placar agregado corrente é público e visível a todos os eleitores a cada rodada, funcionando como informação de pesquisa dentro do jogo, mas não é manipulado nem tem variação identificada: o que o estudo manipula e compara é o prazo (deadline) e a composição da partida (só humanos, só bots ou mista) — evidência: "this paper is to examine how the deadline" (p. 1); "The collection of score vectors is public" (p. 2)
- **c3_desfecho** — resposta: Sim — desfecho de voto: a escolha de voto e as mudanças de voto a cada rodada são medidas e classificadas em relação ao candidato com a maior pontuação corrente (IRR1/IRR2); não há medida de comparecimento — evidência: "each voter may ask to change his selection" (p. 3); "a voter who opts to change his vote" (p. 3)
- **c4_desenho_elegivel** — resposta: Sim — experimento de laboratório on-line com estudantes, com perfis de preferência sorteados e participantes cegos quanto a jogar contra humanos ou contra bots; parte das comparações (jogos racionais vs. irracionais) é post hoc — evidência: "We set out to examine human behavior in an iterative voting" (p. 3); "Note that the students had no idea whether they were" (p. 5)
- **c5_estudo_primario** — resposta: Sim — estudo primário, com coleta própria dos dados dos jogos e análise própria — evidência: "A total of 156 Voters played a total of 397 games" (p. 4)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento — evidência: "Haste Makes Waste: a Case to Favour Voting Bots" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Experimento on-line (plataforma CUD-Game) com estudantes, em duas fases — Fase I: 156 votantes em 397 jogos, com 7 votantes, 5 candidatos e 10 rodadas por jogo; Fase II: 72 estudantes em 264 jogos, com 8 votantes por jogo, contra humanos ou contra bots — mais uma fase só de bots, com 10000 bots em 1250 jogos; o período da coleta não é informado — evidência: "A total of 156 Voters played a total of 397 games" (p. 4); "total of 10000 bots played 1250 games" (p. 5)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador

**Paginação.** O documento não tem numeração impressa em nenhuma folha: o cabeçalho corrente traz apenas o nome da conferência e o título curto/autor ("WI '17, August 23-26, 2017, Leipzig, Germany" / "Ben Yosef et al."), e a primeira e a última folha não têm rodapé com número. Conferi as folhas 1, 2 e 6 (distantes entre si) antes de fechar a ficha. Por isso `paginacao: indice-do-PDF` e `offset_pagina: 0`: as páginas anotadas nas evidências são o índice 1-based da folha do PDF, de modo que folha_do_PDF = pagina_anotada + 0.

**c2 (decisão limítrofe, a que mais pede arbitragem).** Respondi `parcial`. A favor de `Sim`: o vetor de pontuação agregado é divulgado a cada rodada, é público e visível a todos, e é exatamente a informação sobre a posição relativa dos candidatos a que os eleitores reagem ao mudar o voto — é o análogo, dentro do jogo, da informação de pesquisa, e a regra de C1 do protocolo diz que jogos eleitorais de laboratório com informação de pesquisa estão no escopo. Contra: essa informação é constante em todas as condições, não há braço sem placar nem variação do seu conteúdo, e o texto nunca a chama de *poll* no próprio desenho (só ao descrever trabalhos alheios). A exposição efetivamente manipulada e comparada é o prazo e a composição da partida (humanos, bots, mista), não o resultado da pesquisa. Numa leitura estrita de "manipulada em experimento, com variação natural identificada ou medida no indivíduo em painel", a resposta seria `Não`.

**c3.** Os desfechos reportados nas figuras são de qualidade do processo coletivo (percentual de convergência, pontos médios de recompensa, PoA, tempo de convergência). O desfecho de voto está na classificação das ações dos eleitores: IRR1 e IRR2 definem mudança de voto para candidato pior ranqueado que o de maior pontuação corrente, isto é, a escolha de voto medida em relação a quem está à frente no placar. Essa medida de voto serve, no artigo, como variável de agrupamento dos jogos (racionais vs. irracionais), não como variável dependente das comparações principais — mas há medida de escolha de voto, e a ausência de dados numéricos utilizáveis não é motivo de `Não` pela convenção do projeto.

**c4.** Há aleatorização dos perfis de preferência e os participantes eram cegos quanto a enfrentar humanos ou bots, o que caracteriza experimento de laboratório on-line. Ressalvas: as duas fases diferem em vários parâmetros ao mesmo tempo (7 vs. 8 votantes, limite de jogos por participante), e a comparação entre jogos com e sem ações irracionais é post hoc; os jogos só de bots são simulação.

**outros_relatos_mesmo_estudo = 999.** O texto se apoia num estudo anterior da mesma equipe (referência [1], Bannikova et al., que propôs o modelo teórico), mas é outro trabalho, teórico e sem os mesmos dados; não é outro relato deste estudo empírico. Não há menção a versão anterior, tese, working paper ou relatório com os mesmos dados.

**registro_financiamento = 999.** Não há seção de agradecimentos, de financiamento, nem identificador de pré-registro em nenhuma das 6 folhas.

**Escolha das evidências.** Preferi trechos sem palavras com ligaduras tipográficas (ff, fi, fl): por isso evitei, por exemplo, "affects" na frase do resumo sobre o prazo, "first experiment" e "configuration" na seção de coleta de dados, e "profile"/"pre-defined" na descrição das preferências sorteadas, embora fossem trechos mais diretos. Cada citação foi tomada de um fragmento contíguo dentro de uma linha impressa.
