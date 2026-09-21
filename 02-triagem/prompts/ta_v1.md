# Critérios de triagem de títulos e resumos: pesquisas eleitorais publicadas e voto

| Campo | Valor |
|---|---|
| Versão | ta_v1 |
| Data | 2026-09-19 |
| Protocolo de referência | 00-protocolo/protocolo.md, v1.0, congelado no G2 em 2026-09-19 |
| Mudanças em relação à versão anterior | primeira versão |
| Motivo da nova versão | não se aplica |

## Pergunta da revisão

A exposição a resultados de pesquisas eleitorais publicadas (pesquisa pré-eleitoral, agregador ou projeção baseada em pesquisas, pesquisa de boca de urna divulgada antes do fechamento das urnas) altera a intenção ou a escolha de voto, em comparação com a não exposição ou com a exposição a outro resultado, e em que direção (*bandwagon*, a favor de quem lidera; *underdog*, a favor de quem está atrás)? Também interessa o efeito dessa exposição sobre o comparecimento às urnas.

- **População:** eleitores ou participantes que escolhem entre candidatos, partidos ou opções de referendo, em eleição real, hipotética ou de laboratório; ou unidades eleitorais agregadas.
- **Exposição:** resultado de pesquisa eleitoral mostrado, publicado ou divulgado.
- **Comparação:** não exposição, outro resultado, antes e depois de proibição, unidades não expostas.
- **Desfechos:** intenção ou escolha de voto, votação; ou comparecimento.
- **Desenho:** experimentos, experimentos naturais e quase-experimentos, painéis individuais.

## Como decidir

Você decide apenas com o título, o resumo e os metadados do registro. Aplique os critérios **na ordem numerada abaixo**:

1. No primeiro critério que o título ou o resumo mostram **com clareza** que não é atendido, pare. A decisão é `excluir`, e o critério que falhou é o identificador desse critério.
2. Se todos os critérios são atendidos ou plausivelmente atendidos, a decisão é `incluir`.
3. Se o título e o resumo não bastam para saber se algum critério é atendido, a decisão é `incerto`. Informe o critério em dúvida, se houver um.

Regras que valem para todos os critérios:

- **Na dúvida, não exclua.** Entre `excluir` e `incerto`, escolha `incerto`: nesta etapa, perder um estudo elegível custa mais do que ler um texto completo a mais.
- **Sem resumo, `incerto`.** Registro sem resumo nunca é excluído. Só é `incluir` se o próprio título mostrar, sem margem, que todos os critérios são atendidos.
- **Resumo truncado.** Decida pelo que existe; se a parte que falta seria decisiva, `incerto`.
- **Idioma não é critério.** Registros em qualquer idioma são avaliados pelo conteúdo.
- **Ano não é critério aqui.** O recorte de ano já foi aplicado antes da triagem.
- **Não use conhecimento externo** sobre autores, periódicos ou o estudo.

## Estudar não é mencionar

Um critério sobre população, exposição ou desfecho só é atendido quando isso é **objeto da análise** do estudo: o resultado de pesquisa é o tratamento ou a exposição analisada, e o voto ou o comparecimento é medido ou analisado. Não basta a pesquisa eleitoral aparecer como contexto, como fonte de dados para medir intenção de voto, como tema de cobertura da imprensa ou como recomendação na conclusão.

- VÁLIDO: "The impact of exposure to pre-election polls on voting behaviour"
- VÁLIDO: "Off the Fence, Onto the Bandwagon? A Large-Scale Survey Experiment on Effect of Real-Life Poll Outcomes on Subsequent Vote Intentions"
- INVÁLIDO: "An Evaluation of the 2016 Election Polls in the United States" (avalia a precisão das pesquisas, não o efeito delas sobre o eleitor)
- INVÁLIDO: "Using the Error in Pre-Election Polls to Test for the Presence of Pork" (pesquisas usadas como fonte de dados)
- INVÁLIDO: "Think Twice before Jumping on the Bandwagon: Clarifying Concepts in Research on the Bandwagon Effect" (revisão conceitual; ver C5)

## Critérios, na ordem de aplicação

### C1. População e contexto

- **Pergunta:** o estudo analisa eleitores ou participantes que escolhem entre candidatos, partidos ou opções de referendo ou plebiscito (em eleição real, hipotética ou de laboratório), ou unidades eleitorais agregadas (seções, municípios, distritos)?
- **Atende quando:** eleições de qualquer nível e país; referendos e plebiscitos; *survey experiments* com candidatos reais ou fictícios; jogos eleitorais de laboratório, inclusive com preferências induzidas, **qualquer que seja o tamanho do grupo ou da sessão**; dados eleitorais agregados.
- **Não atende quando:** a escolha não é eleitoral (consumo, marcas, mercado financeiro, tecnologia, esportes, saúde); votação de órgão deliberativo real (júri, comitê, conselho, legislativo); "bandwagon" ou "underdog" no sentido de marketing, finanças ou relações internacionais.
- VÁLIDO: "The Bandwagon Effect in an Online Voting Experiment With Real Political Organizations"
- INVÁLIDO: "Bandwagon Effects in High-Technology Industries"
- INVÁLIDO: "Bandwagon effect revisited: A systematic review to develop future research agenda" (consumo)
- **Na dúvida** (contexto não informado): `incerto`.

### C2. Exposição estudada

- **Pergunta:** o resultado de pesquisa eleitoral é a exposição analisada: manipulado em experimento, com variação natural identificada (proibição ou embargo de divulgação, fuso horário, calendário de publicação) ou medido no indivíduo em painel?
- **Atende quando:** o estudo mostra ou não mostra resultados de pesquisa aos participantes, varia o resultado mostrado (quem aparece à frente), compara antes e depois de uma proibição de divulgação, compara locais que viram ou não viram projeções de boca de urna, ou mede no indivíduo a exposição a pesquisas e relaciona com o voto ou o comparecimento. Vale pesquisa isolada, média de pesquisas, agregador, projeção ou probabilidade de vitória baseada em pesquisas, e boca de urna divulgada antes do fechamento das urnas.
- **Não atende quando:** a pesquisa é só contexto, motivação ou fonte de dados; o estudo trata da precisão, metodologia ou previsão eleitoral por pesquisas; analisa a cobertura da imprensa sobre pesquisas sem medir voto ou comparecimento; a "exposição" é resultado de eleição passada, mercado de apostas, contagem de curtidas ou seguidores em redes sociais, ou rótulo de azarão sem resultado de pesquisa; "deliberative poll" (fórum deliberativo, não resultado de pesquisa).
- VÁLIDO: "Voting for the Underdog or Jumping on the Bandwagon? Evidence from India's Exit Poll Ban"
- VÁLIDO: "Exit Polls and Voter Turnout in the 2017 French Elections"
- INVÁLIDO: "Sentiment-Based Features for Predicting Election Polls: A Case Study on the Brazilian Scenario" (previsão de pesquisas)
- INVÁLIDO: "Disaggregating Deliberation's Effects: An Experiment within a Deliberative Poll" (fórum deliberativo)
- **Na dúvida:** `incerto`.

### C3. Desfecho

- **Pergunta:** o estudo mede ou analisa (a) intenção de voto, escolha de voto ou votação agregada de candidato, partido ou opção; ou (b) comparecimento às urnas (real, validado, agregado ou intenção de comparecer)?
- **Atende quando:** voto declarado ou escolhido em experimento; votação de candidatos ou partidos; voto estratégico ou tático medido como escolha de voto; comparecimento ou abstenção.
- **Não atende quando:** o único desfecho é avaliação ou simpatia pelo candidato sem medida de voto nem de comparecimento, expectativa de quem vai vencer, busca de informação, confiança nas pesquisas ou financiamento de campanha.
- VÁLIDO: "What Makes Voters Turn Out: The Effects of Polls and Beliefs" (comparecimento)
- VÁLIDO: "How Election Polls Shape Voting Behaviour"
- INVÁLIDO: "The Effect of Opinion Polls on Political Information Seeking" (só busca de informação)
- INVÁLIDO: "Pesquisas eleitorais afetam receitas de campanha: a correlação entre expectativa de vitória e financiamento" (financiamento)
- **Na dúvida:** `incerto`. Não exclua porque o resumo não traz números. Não exclua porque o resumo não cita o desfecho: resumos costumam listar só os resultados principais. Exclua por este critério só quando o estudo claramente trata de outro desfecho.

### C4. Desenho

- **Pergunta:** o desenho compara situações que identificam o efeito da exposição: experimento aleatorizado (survey, laboratório, campo, online); experimento natural ou quase-experimento (proibição, embargo, fuso horário, calendário de divulgação, diferenças em diferenças, descontinuidade, série interrompida); ou painel individual com exposição medida antes do desfecho?
- **Atende quando:** há grupos que viram e não viram a informação (ou viram resultados diferentes), atribuídos ao acaso ou por uma variação externa identificada; ou medidas repetidas no mesmo indivíduo com exposição medida antes do voto. Julgue pelas características, não pelo rótulo que os autores dão.
- **Não atende quando:** o estudo só compara tendências de pesquisas com o resultado da eleição ("momentum") sem variação identificada da exposição; pergunta ao eleitor se as pesquisas o influenciaram, sem comparação; é simulação ou modelo teórico sem dados; é qualitativo, normativo, jurídico ou descritivo. Se o registro é revisão, meta-análise, editorial ou ensaio sem dados próprios, não use este critério: aplique C5.
- VÁLIDO: "Exit polls, turnout, and bandwagon voting: Evidence from a natural experiment"
- INVÁLIDO: "Public Perception of Political Opinion Polls and Their Influence on People's Voting Behavior: The Case of Mwanza City" (percepção autodeclarada de influência)
- INVÁLIDO: "Underdogs, bandwagons or incumbency? Party support at the beginning and the end of Australian election campaigns" (tendência de apoio sem variação identificada da exposição)
- **Na dúvida** (método não descrito no resumo): `incerto`.

### C5. Estudo primário

- **Pergunta:** é um estudo primário com análise própria de dados?
- **Atende quando:** o estudo produz ou analisa dados quantitativos próprios (experimento, dados eleitorais, painel).
- **Não atende quando:** revisão de literatura, revisão sistemática, meta-análise, editorial, comentário, resenha de livro, ensaio teórico ou modelo formal sem dados. Em revisões e meta-análises, escreva na justificativa "revisão: usar na bola de neve".
- VÁLIDO: "How Anxiety and Enthusiasm Help Explain the Bandwagon Effect"
- INVÁLIDO: "Endogenous bandwagon and underdog effects in a rational choice model" (modelo teórico sem dados)
- **Na dúvida:** `incerto`.

## O que não é critério nesta etapa

- Acesso ao texto completo, idioma, ano, tipo de periódico ou reputação dos autores.
- Qualidade metodológica ou risco de viés (avaliados depois, com ferramenta própria).
- Significância estatística ou direção do resultado (*bandwagon*, *underdog* ou nenhum efeito, tanto faz).
- Presença de dados de desfecho utilizáveis no resumo.
- Quem é o alvo do efeito (líder, azarão, segundo colocado viável): estudos de voto estratégico com escolha de voto medida seguem adiante.

## Casos de calibração

Não houve calibração humana (atalho A2 do protocolo). Casos resolvidos pelo coordenador com registros do conjunto de desenvolvimento (âncoras de desenvolvimento e listas exploratórias), nunca de amostras de validação, elusão ou estabilidade:

1. "Projecting Confidence: How the Probabilistic Horse Race Confuses and Demobilizes the Public": `incluir`. Experimento com projeções probabilísticas de vitória (exposição) e comparecimento (desfecho b).
2. "Everybody follows the crowd? Effects of opinion polls and past election results on electoral preferences": `incluir`. O experimento varia resultados de pesquisa (e também resultados passados); basta a pesquisa ser uma das exposições analisadas.
3. "Polls, coalition signals and strategic voting: An experimental investigation of perceptions and effects": `incluir`. Voto estratégico medido como escolha de voto, com pesquisas manipuladas.
4. "The Twilight of the Polls? A Review of Trends in Polling Accuracy and the Causes of Polling Misses": `excluir`, C2. Trata da precisão das pesquisas.
5. "Bandwagon effects in British elections, 1885–1910": `incerto`, C4. Dados eleitorais históricos; o resumo precisa dizer se há variação identificada da exposição a informação sobre quem liderava.
