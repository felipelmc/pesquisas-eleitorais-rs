---
citekey: Scheuerman2021
ficha_id: Scheuerman2021
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Scheuerman2021.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_104
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial, o titulo e os autores batem com os metadados (K. Brent Venable corresponde a Kristen Brent Venable), mas o arquivo e a versao arXiv do mesmo trabalho (arXiv:2012.02811v1, 4 Dec 2020), enquanto o registro aponta a versao publicada na AAAI (DOI 10.1609/aaai.v35i6.16716) — evidência: "Modeling Voters in Multi-Winner Approval Voting" (p. 1)
- **tipo_documento** — resposta: preprint, o proprio documento traz na primeira pagina o carimbo de deposito no arXiv, e a Ethics Statement (p. 8) indica que ainda havera uma versao final do texto — evidência: "arXiv:2012.02811v1 [cs.GT] 4 Dec 2020" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, participantes votam em candidatos em eleicoes hipoteticas de laboratorio online (Mechanical Turk) com preferencias induzidas por pagamento monetario — evidência: "included 104 participants recruited through Mechanical Turk" (p. 6)
- **c2_intervencao_estudada** — resposta: parcial, a exposicao manipulada e a informacao parcial sobre a contagem corrente de votos no jogo eleitoral (numero de cedulas faltantes, isto e, o grau de incerteza sobre o placar), tratada pela literatura de AV como poll information, mas o documento nunca a descreve como resultado de pesquisa eleitoral divulgada — evidência: "uncertainty that is represented, in our case, as missing ballots" (p. 1)
- **c3_desfecho** — resposta: Sim, o desfecho e de voto (a cedula de aprovacao efetivamente marcada pelo participante na eleicao hipotetica, e quais candidatos ele aprova), nao ha desfecho de comparecimento — evidência: "Participants were asked to cast ballots in a voting game" (p. 6)
- **c4_desenho_elegivel** — resposta: Sim, experimento comportamental online aleatorizado, com alocacao aleatoria entre eleicoes de 2 e de 3 vencedores e variacao intra sujeito do numero de cedulas faltantes — evidência: "Participants were then randomly assigned to be part of a 2-winner" (p. 6)
- **c5_estudo_primario** — resposta: Sim, estudo primario com dados experimentais proprios coletados pelos autores e analise propria — evidência: "Our behavioral study aimed at investigating approval voting heuristics" (p. 6)
- **c6_nao_retratado** — resposta: Sim, nao ha marca, nota ou pagina de retratacao no documento — evidência: "Modeling Voters in Multi-Winner Approval Voting" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim, o texto remete a um Technical Appendix com mais informacoes sobre o mesmo estudo (nao incluido neste PDF, que termina nas referencias); a Ethics Statement (p. 8) tambem anuncia uma versao final do proprio trabalho, que corresponde a versao AAAI do registro; nenhuma tese, dissertacao ou working paper anterior e mencionado — evidência: "More information about this study can be found in the Technical Appendix." (p. 6)
- **fonte_dados_amostra** — resposta: experimento comportamental online no Amazon Mechanical Turk com 104 participantes votando em cenarios hipoteticos de aprovacao (todos no cenario de vencedor unico, n=104; depois alocados a 2 vencedores, n=50, ou 3 vencedores, n=54), com cenarios A e B em 9 condicoes (1, 2 ou 3 vencedores por 0, 1 ou 3 cedulas faltantes); o periodo de coleta nao e informado no documento — evidência: "All participants voted in the single winner scenarios (n=104)" (p. 6)
- **registro_financiamento** — resposta: NSF Award IIS-2007955 (financiamento); nao ha identificador de pre registro e o numero do IRB nao e informado — evidência: "supported by NSF Award IIS-2007955" (p. 8)

## Notas do codificador
- Paginacao e offset: o rodape das paginas do corpo traz a numeracao impressa igual ao indice do PDF; conferi em duas paginas distantes (pagina 2 do PDF traz "2" no rodape e pagina 8 do PDF traz "8"), logo offset_pagina = 0 e as citacoes usam a numeracao impressa. A primeira pagina nao traz numero impresso, mas e a pagina 1 do PDF na mesma sequencia.
- texto_confere = parcial porque o arquivo e a versao depositada no arXiv (carimbo arXiv:2012.02811v1, 4 Dec 2020) de um trabalho cujo registro traz o DOI das atas da AAAI; o titulo e os quatro autores sao os mesmos. A propria Ethics Statement da p. 8 indica que esta nao e a versao final, ao dizer que o numero do IRB sera acrescentado na versao final. Pela mesma razao, tipo_documento = preprint, embora a nota de rodape da primeira pagina ja traga o copyright da AAAI de 2021.
- c2 = parcial e o ponto limitrofe desta ficha. O que e manipulado e apresentado aos participantes e a contagem corrente de votos de cada candidato (linha "# Votes" das Tabelas 3 e 4) com 0, 1 ou 3 cedulas faltantes, ou seja, informacao parcial e incerta sobre o placar da eleicao. Na literatura de voto iterativo e de aprovacao isso e chamado de poll information, e o proprio artigo se apoia nesse arcabouco (Fairstein et al. 2019, Reijngoud e Endriss 2012), mas em nenhum momento o documento descreve a exposicao como pesquisa eleitoral publicada, agregador, projecao ou boca de urna: trata-se de contagem parcial de votos dentro do jogo. Deixo a decisao final para o coordenador.
- O foco analitico do artigo e comparar modelos de heuristica (Complete, Take X Best, AU, AUT) quanto a acuracia de predicao da cedula, e nao estimar o efeito causal da informacao sobre o voto; ainda assim o desfecho medido e a cedula de voto e ha manipulacao experimental, o que sustenta c3 e c4 como Sim. Pela convencao do projeto, a ausencia de estimativa de efeito utilizavel nao e motivo de Nao.
- Nenhuma variavel ficou com 999.
