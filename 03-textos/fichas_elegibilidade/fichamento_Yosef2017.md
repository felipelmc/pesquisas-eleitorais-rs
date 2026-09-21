---
citekey: Yosef2017
ficha_id: Yosef2017
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Yosef2017.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_136
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim, o título e o primeiro autor do documento batem com os metadados do registro (Haste Makes Waste: a Case to Favour Voting Bots; David Ben Yosef; 2017; DOI 10.1145/3106426.3106532 impresso na primeira página) — evidência: "Haste Makes Waste: a Case to Favour Voting Bots" (p. 1)
- **tipo_documento** — resposta: evento (artigo publicado nos anais da conferência WI '17, da ACM, realizada em Leipzig, Alemanha, em 2017) — evidência: "2017, Leipzig, Germany" (p. 2); "DOI: 10.1145/3106426.3106532" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, participantes humanos (estudantes) atuam como votantes que escolhem entre 5 candidatos, com preferências induzidas, em um jogo de votação on-line de laboratório cujo objetivo é um vencedor unânime antes do prazo — evidência: "a group of people (voters) is required to reach" (p. 1); "A total of 156 Voters played a total of 397 games." (p. 4)
- **c2_intervencao_estudada** — resposta: parcial, o resultado agregado corrente do jogo (score vector) é publicado a cada rodada e é a informação diante da qual os votantes decidem mudar o voto, mas não há manipulação nem variação identificada dessa exposição: o que varia entre condições é a composição de humanos e bots e a configuração do prazo — evidência: "Once the collection of score vectors are published, each voter" (p. 2)
- **c3_desfecho** — resposta: Sim, o desfecho é de voto: o estudo analisa se e quando os votantes mudam o voto, classificando a mudança em relação ao candidato com a maior pontuação corrente; não há comparecimento — evidência: "When and if do people change their vote?" (p. 1)
- **c4_desenho_elegivel** — resposta: Sim, experimento de laboratório on-line com participantes humanos, em duas fases com configurações distintas (7 e 8 votantes por partida, limite de partidas), mais partidas só de bots usadas como comparação — evidência: "We ran another experiment with a few changes" (p. 4); "We ran a set of bot-only games, 8 bots per game." (p. 5)
- **c5_estudo_primario** — resposta: Sim, é estudo primário: os autores construíram a plataforma, coletaram os dados das partidas e analisaram esses dados próprios — evidência: "We collected data that allows us to analyze human behavior" (p. 1)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação no documento — evidência: "Haste Makes Waste: a Case to Favour Voting Bots" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Dados próprios da plataforma CUD-Game, jogo de votação on-line com estudantes: Fase I com 160 estudantes, 156 votantes em 397 partidas (7 votantes, 5 candidatos, 10 rodadas); Fase II com 72 estudantes em 264 partidas (8 votantes por partida); e uma fase só de bots, com 10000 bots em 1250 partidas; o período da coleta não é informado — evidência: "A total of 72 students played a total of 264 games" (p. 5); "total of 10000 bots played 1250 games" (p. 5)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
Paginação: o PDF não traz numeração impressa em nenhuma das 6 páginas. A primeira página termina no bloco de copyright da ACM, sem número, e os cabeçalhos das páginas 2 a 6 trazem apenas o nome da conferência e o título ou os autores, também sem número. Conferi cabeçalho e rodapé de páginas distantes (folhas 1, 2, 4 e 5) antes de fechar a ficha. Por isso `paginacao: indice-do-PDF` e `offset_pagina: 0`: as páginas citadas são índices do PDF (1-based) e batem com a folha em que o trecho está.

c2 como parcial: o jogo exibe a cada rodada o placar agregado corrente, visível a todos, e é essa informação que orienta a mudança de voto analisada, o que a aproxima de uma pesquisa dentro de um jogo eleitoral de laboratório. Mas a exposição não é manipulada nem varia entre condições: todos os jogadores sempre veem o placar. As comparações do artigo são entre partidas com e sem ações irracionais, entre humanos, bots e partidas mistas, e entre as duas fases (número de votantes e limite de partidas). Fica a decisão do coordenador sobre se isso basta como exposição do protocolo.

c3 como Sim: a escolha de voto individual é medida e analisada (mudança de voto, e a classificação IRR1 e IRR2 define a mudança justamente em relação ao candidato com a maior pontuação corrente). Registro, porém, que os desfechos reportados nos gráficos são de nível de partida (percentual de convergência, pontos médios de recompensa, preço da anarquia e tempo de convergência), sem tabela de apoio por candidato à frente ou atrás. Pela convenção do projeto, a falta de dados numéricos utilizáveis não é motivo de Não.

c4 como Sim: o desenho é experimental (perfis de preferência sorteados uniformemente, duas fases com configurações definidas pelos autores, partidas contra bots sem que os humanos soubessem contra quem jogavam). Não há, contudo, braço que varie a informação agregada mostrada, o que é coerente com o parcial em c2.

outros_relatos_mesmo_estudo = 999: o documento cita um estudo anterior, de autoria em parte coincidente, que propôs o modelo teórico seguido aqui (referência [1]), mas esse trabalho é teórico e não é outro relato dos mesmos dados. Não há menção a versão anterior, tese, working paper ou relatório com os dados deste artigo.

registro_financiamento = 999: não há declaração de financiamento nem identificador de pré-registro no documento. Os 5 pontos de bônus em uma disciplina, oferecidos aos estudantes da Fase I, são incentivo à participação, não financiamento, e por isso não foram registrados aqui.
