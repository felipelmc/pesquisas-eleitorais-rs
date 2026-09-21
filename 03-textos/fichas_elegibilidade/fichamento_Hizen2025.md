---
citekey: Hizen2025
ficha_id: Hizen2025
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Hizen2025.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_161
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o título e os quatro autores batem com os metadados, mas o PDF é a versão preprint no arXiv (arXiv:2408.00265v2, datada de 19 de agosto de 2024), e não o artigo publicado em 2025 com o DOI informado — evidência: "Jumping on the bandwagon and off the Titanic" (p. 1)
- **tipo_documento** — resposta: preprint — evidência: "arXiv:2408.00265v2" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — participantes humanos jogam uma eleição de laboratório online entre dois candidatos (Orange e Green) com preferências induzidas, decidindo votar ou se abster — evidência: "Two candidates are labeled Orange and Green" (p. 7); "We conducted the experiment through 8 sessions, each with 21 human subjects" (p. 9)
- **c2_intervencao_estudada** — resposta: parcial — a exposição manipulada é a taxa de apoio aos candidatos exibida na tela de decisão, que informa ao sujeito se seu candidato está à frente ou atrás (status de maioria/minoria local e global), mas o documento nunca a descreve como resultado de pesquisa eleitoral divulgada: é parâmetro de conhecimento comum do jogo — evidência: "The decision screen showed the local support rates for the candidates" (p. 17)
- **c3_desfecho** — resposta: Sim — o desfecho é de comparecimento: a variável dependente é o comparecimento (turnout) do eleitor sob cada regra, medido pelo limiar de custo escolhido; não há medida de escolha de voto, já que votar no candidato menos preferido foi excluído do desenho — evidência: "Two dependent variables are employed, concerning the voter turnout" (p. 15)
- **c4_desenho_elegivel** — resposta: Sim — experimento controlado online (z-Tree Unleashed), com as 18 configurações de votação e as duas regras de agregação atribuídas dentro do sujeito e ordem de blocos contrabalanceada entre sessões, e custos de voto sorteados aleatoriamente — evidência: "We conducted an experiment on the voting game" (p. 7)
- **c5_estudo_primario** — resposta: Sim — estudo primário: os autores coletam dados experimentais próprios e os analisam com testes de Wilcoxon e regressões de efeitos aleatórios — evidência: "We report regression results to further investigate turnout behavior" (p. 15)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação em nenhuma das 22 páginas do documento — evidência: "Jumping on the bandwagon and off the Titanic" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Experimento eleitoral online com sujeitos do pool estudantil da Universidade de Osaka, em 8 sessões de 21 sujeitos humanos cada, realizadas em março e junho de 2021, com 36 rodadas de votação por sujeito — evidência: "The eight sessions took place in March and June 2021" (p. 10); "each with 21 human subjects" (p. 9)
- **registro_financiamento** — resposta: Sem identificador de pré-registro. Financiamento: Investissements d'Avenir, ANR-11-IDEX-0003/Labex Ecodec/ANR-11-LABX-0047; programa PHC Sakura, projeto número 45153XK (JPJSBP 120203208); Joint Usage/Research Center do ISER, Universidade de Osaka. Estudo aprovado pelo IRB da Universidade de Osaka — evidência: "PHC Sakura program, project number 45153XK (JPJSBP 120203208)" (p. 1)

## Notas do codificador

**Paginação.** A numeração impressa no rodapé coincide com o índice do PDF: o rodapé "1" está na folha 1 (folha de rosto), "11" na folha 11 (Tabela 4) e "22" na folha 22 (última página de referências), logo `offset_pagina: 0`. Todas as páginas citadas nas evidências (1, 7, 9, 10, 15, 17, 19) foram abertas e conferidas com a fórmula folha = página impressa + 0.

**texto_confere = parcial.** O documento é o preprint do arXiv (arXiv:2408.00265v2, "August 19, 2024"), sem qualquer indicação de periódico, volume ou DOI; o registro do coordenador aponta o artigo de 2025 no European Journal of Political Economy. Título e autores (Hizen, Kikuchi, Koriyama, Masuda) batem integralmente, então é outra versão do mesmo trabalho, não outro trabalho.

**c2 = parcial.** Esta é a decisão limítrofe da ficha. A informação que varia entre as 18 configurações e que define o status de maioria/minoria do sujeito é a taxa de apoio dos candidatos (p1, e as probabilidades de voto dos grupos automatizados), exibida na tela de decisão antes da escolha: funcionalmente, é a informação de "quem está à frente" cujo efeito sobre o comparecimento o artigo mede, e os autores nomeiam os achados justamente como efeito bandwagon comportamental e efeito Titanic, termos da literatura sobre pesquisas eleitorais. Por outro lado, o documento em momento algum apresenta essa informação como resultado de pesquisa eleitoral divulgada aos participantes: ela é parâmetro de conhecimento comum do jogo, e não há pesquisa (poll) liberada entre a formação das preferências e o voto. As menções a pesquisas de opinião no texto são a trabalhos de terceiros (Großer e Schram, 2010, citado na p. 5). Registrei parcial para que o coordenador decida se o desenho conta como manipulação de informação de pesquisa.

**c3.** O desfecho é apenas de comparecimento, não de escolha de voto: como votar no candidato menos preferido é estratégia dominada, o desenho omite essa escolha (nota de rodapé 7, p. 5), e o sujeito só decide o limiar de custo abaixo do qual vota. Não sinalizei isso como motivo de "Não", conforme a convenção do projeto, porque comparecimento entra na célula de mobilização.

**c4.** Trata-se de experimento controlado com atribuição das situações de votação dentro do sujeito (cada sujeito joga as 18 configurações uma vez sob cada regra), ordem de blocos alterada sessão a sessão para minimizar efeito de ordem (Tabela 3, p. 10) e custos de voto sorteados da distribuição uniforme. Os outros dois grupos do eleitorado são eleitores automatizados programados no equilíbrio, o que restringe a validade externa mas não retira o caráter experimental.

**outros_relatos_mesmo_estudo = 999.** O documento não menciona versão anterior, tese, working paper ou relatório técnico com os mesmos dados. A única remissão a material próprio é ao "Online Appendix" com as instruções experimentais e o questionário (nota de rodapé 11, p. 10), que é suplemento deste mesmo relato, não outro relato; por isso não o registrei como resposta. Kikuchi e Koriyama (2023) e Koriyama e Wang (2024), citados na p. 4, são estudos distintos, sem os mesmos dados.

**fonte_dados_amostra.** Não calculei o número total de sujeitos (o documento informa 8 sessões com 21 sujeitos cada, mas não escreve o total), nem transcrevi as 3.024 observações da Tabela 7 como tamanho de amostra, porque são observações sujeito-rodada por regra, e não o N de participantes.
