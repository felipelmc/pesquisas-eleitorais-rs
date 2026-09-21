---
citekey: Scheuerman2020
ficha_id: Scheuerman2020
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Scheuerman2020.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_105
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — o título e o primeiro autor do documento batem com os metadados, e a nota de publicação é do AAMAS 2020 (ano 2020) — evidência: "Heuristic Strategies in Uncertain Approval Voting Environments" (p. 1)
- **tipo_documento** — resposta: evento — o documento declara publicação nos anais de conferência (AAMAS 2020) — evidência: "19th International Conference on Autonomous Agents and Multiagent Systems" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — participantes recrutados no Mechanical Turk votam entre cinco candidatos em eleições hipotéticas de aprovação, com preferências induzidas por pagamento — evidência: "participants were asked to vote in a series of unrelated hypothetical elections" (p. 6); "104 participants were recruited through Mechanical Turk" (p. 6)
- **c2_intervencao_estudada** — resposta: parcial — a exposição manipulada é a informação sobre a posição dos candidatos exibida antes do voto (votos já computados e número de votos faltantes), equivalente funcional de uma pesquisa, mas o documento nunca a descreve como resultado de pesquisa eleitoral — evidência: "the number of votes cast for each candidate so far" (p. 6); "We manipulate two environmental features, including the number of winners" (p. 4)
- **c3_desfecho** — resposta: Sim — desfecho de voto: o voto de aprovação efetivamente emitido pelo participante em cada cenário (quais e quantos candidatos aprovou); não há medida de comparecimento — evidência: "subjects could vote for 0 or more (up to five)" (p. 6); "only 15.4% voted truthfully in the 1-winner election" (p. 6)
- **c4_desenho_elegivel** — resposta: Sim — experimento comportamental online, com cenários manipulados e alocação aleatória dos participantes entre a eleição de 2 e a de 3 vencedores — evidência: "In a behavioral experiment of 104 subjects on Mechanical Turk" (p. 2); "randomly assigned to be part of a 2-winner" (p. 6)
- **c5_estudo_primario** — resposta: Sim — relata análise própria dos dados do experimento comportamental conduzido pelos autores — evidência: "The results of the behavioral experiment described above showed unique patterns" (p. 6)
- **c6_nao_retratado** — resposta: Sim — não há aviso, marca ou página de retratação no documento — evidência: "Heuristic Strategies in Uncertain Approval Voting Environments" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Cita um estudo anterior dos mesmos quatro autores, referência [31] Scheuerman, Harman, Mattei e Venable (2019), "Heuristics in Multi-Winner Approval Voting", CoRR abs/1905.12104; o documento o trata como estudo prévio e não afirma que sejam o mesmo estudo ou os mesmos dados — evidência: "A recent study of voting behavior in multi-winner approval elections showed" (p. 1); "Heuristics in Multi-Winner Approval Voting. CoRR abs/1905.12104" (p. 9)
- **fonte_dados_amostra** — resposta: Experimento comportamental online no Mechanical Turk com 104 participantes (todos nos cenários de um vencedor; 50 alocados à eleição de 2 vencedores e 54 à de 3 vencedores), com pagamento de US$ 1,00 mais bônus; o documento não informa o período de coleta — evidência: "104 participants were recruited through Mechanical Turk" (p. 6); "All participants voted in the single winner scenarios (n=104)" (p. 6)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset de página: a numeração impressa coincide com o índice do PDF. Conferido em duas páginas distantes: o rodapé da página 2 do PDF traz "2" e o da página 9 traz "9" (a primeira página, de abertura do artigo, não exibe número, como é usual no formato ACM/AAMAS). Logo, `paginacao: impressa` e `offset_pagina: 0`.
- `texto_confere` = Sim: o arquivo é o depósito no arXiv (marca lateral "arXiv:1912.00011v1 [cs.GT] 29 Nov 2019" na p. 1), mas traz a nota de publicação e o copyright dos anais do AAMAS 2020, com o mesmo título e os mesmos autores do registro. O DOI do registro não aparece no documento, que imprime apenas o marcador "https://doi.org/doi"; por isso a conferência foi feita por título, primeiro autor e ano de publicação.
- `c2_intervencao_estudada` = parcial (decisão limítrofe). A exposição é manipulada experimentalmente e é informação sobre a posição relativa dos candidatos antes de o participante votar: cada cenário varia quem lidera e quantos votos ainda faltam. Funcionalmente é o mesmo conteúdo informacional de uma pesquisa pré-eleitoral, e o próprio artigo situa o trabalho na literatura sobre voto com informação de pesquisa (ele descreve, na seção de trabalhos relacionados, estudos em que os agentes recebem "poll information"). Mas o que é exibido ao participante são votos já emitidos na própria eleição em curso, e em nenhum momento o documento chama isso de pesquisa eleitoral, agregador ou boca de urna. Como a decisão depende de o protocolo aceitar, ou não, a informação de posicionamento em jogo eleitoral de laboratório como equivalente a resultado de pesquisa, marquei parcial em vez de decidir por conta própria entre Sim e Não.
- `c3_desfecho` = Sim, desfecho de voto. A variável dependente é a cédula de aprovação emitida (estratégia usada: truthful, take the X best, regret minimization, abstenção) e o número de candidatos aprovados, reportados em percentuais por cenário e condição. Não há medida de comparecimento.
- `registro_financiamento` = 999: o documento informa apenas a remuneração dos participantes (US$ 1,00 pela pesquisa e bônus de até US$ 8,00 conforme o resultado das eleições hipotéticas), o que não é identificador de pré-registro nem de projeto financiado. Não há seção de agradecimentos, número de processo, edital ou registro em OSF/AEA/RIDIE/EGAP.
- O documento não informa o período de coleta dos dados, nem o país dos participantes; por isso esses itens não constam de `fonte_dados_amostra`.
- Leitura: o PDF tem 9 páginas e foi lido por inteiro (pp. 1 a 9), incluindo tabelas de cenários e a seção de resultados.
