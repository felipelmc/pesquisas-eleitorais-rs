---
citekey: Houser2011
ficha_id: Houser2011
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Houser2011.pdf
paginacao: impressa
offset_pagina: 3
agente_fichador: fichador_el_130
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o documento é o Discussion Paper do Interdisciplinary Center for Economic Science (George Mason University), datado de julho de 2008, com o título "Turned Off or Turned Out? Campaign Advertising, Information, and Voting" e os mesmos autores do registro (Daniel Houser, Rebecca Morton, Thomas Stratmann); é outra versão do trabalho registrado como "Turned on or turned out? Campaign advertising, information and voting" (2011). — evidência: "Advertising, Information, and Voting" (p. -2)
- **tipo_documento** — resposta: working_paper — a folha de rosto do documento o declara como "Discussion Paper" da série do Interdisciplinary Center for Economic Science / George Mason University. — evidência: "Discussion Paper" (p. -2)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — participantes de eleições de laboratório com preferências induzidas escolhem entre dois candidatos (partidos Circle e Triangle) ou se abstêm, em 70 sujeitos distribuídos em três sessões. — evidência: "voted for one of the candidates or abstained" (p. 15)
- **c2_intervencao_estudada** — resposta: Não — a exposição analisada é a propaganda de campanha comprada endogenamente pelos candidatos (tratamentos Red Token e Blue Token), e não resultado de pesquisa eleitoral; nenhuma pesquisa pré-eleitoral, agregador, projeção ou boca de urna é manipulada, identificada ou medida no documento. — evidência: "We used two campaign advertisement treatments" (p. 16)
- **c3_desfecho** — resposta: Sim — o estudo mede tanto a escolha de voto (voto no candidato Striped, no candidato do próprio partido ou do outro partido) quanto o comparecimento (decisão de participar ou se abster); desfecho de voto e de comparecimento, ambos. — evidência: "multinomial logistic regression with non-candidate vote choice" (p. 22); "Participation Decisions of Non-Candidate Voters" (p. 20)
- **c4_desenho_elegivel** — resposta: Sim — experimento de laboratório controlado, com desenho intrassujeitos em que os tratamentos de propaganda variam por período segundo padrão predeterminado e os papéis de candidato, partido e tipo são sorteados a cada período. — evidência: "within subjects design; that is, campaign advertising treatments varied by period" (p. 17)
- **c5_estudo_primario** — resposta: Sim — relata experimento próprio conduzido pelos autores, com dados coletados em três sessões de laboratório e análise estatística própria. — evidência: "We conducted three experimental sessions" (p. 15)
- **c6_nao_retratado** — resposta: Sim — não há marca "RETRACTED", nota ou página de retratação em nenhuma folha do documento; a primeira página traz apenas o título, os autores, a data e a identificação da série. — evidência: "Advertising, Information, and Voting" (p. -2)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: O documento remete a Houser e Stratmann (2008), "Selling favors in the lab: experiments on campaign finance reform" (Public Choice, 136, 1-2, julho, pp. 215-239), que relata experimentos semelhantes com voto obrigatório e cujos resultados são comparados na Tabela 8. — evidência: "Houser and Stratmann (2008) report on similar experiments" (p. 25)
- **fonte_dados_amostra** — resposta: Experimento de laboratório em computadores, com sujeitos recrutados na George Mason University, em três sessões (24, 24 e 22 sujeitos, total de 70), 16 períodos por sessão, 48 campanhas e eleições e 1.120 decisões de voto; o documento é datado de julho de 2008 e não informa a data de realização das sessões. — evidência: "Session Three 22 subjects participated for a total of 70 subjects" (p. 15); "a total of 48 campaigns and elections" (p. 15)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- **Offset de página.** A numeração impressa começa na quarta folha do PDF, que traz "1" no rodapé: 1 + 3 = 4. Confirmei em duas folhas distantes: a folha 21 traz o impresso 18 (18 + 3 = 21) e a última folha, a 46, traz o impresso 43 (43 + 3 = 46). Logo `offset_pagina: 3`. As três primeiras folhas não têm numeração impressa; pela conta `folha = página + offset`, a capa (folha 1) corresponde a -2, a folha de rosto (folha 2) a -1 e a página do resumo (folha 3) a 0. As evidências de `texto_confere` e `c6_nao_retratado` estão na capa, por isso registradas como (p. -2).
- **texto_confere.** Seguindo a nota do coordenador, a divergência de título entre o registro ("Turned on or turned out?") e o documento ("Turned Off or Turned Out?") é variante entre versões, já conferida; autores e subtítulo batem, e o documento é a versão Discussion Paper (ICES/George Mason, julho de 2008) do artigo registrado com DOI de 2011. Por ser outra versão do mesmo trabalho, a resposta é `parcial`, e não `Sim`.
- **tipo_documento.** O documento se declara "Discussion Paper" de uma série de centro de pesquisa; classifiquei como `working_paper` por ser a categoria do codebook que cobre esse formato (não é preprint de artigo submetido declarado como tal, nem relatório técnico).
- **c2 é o critério que decide a exclusão.** A exposição estudada é a propaganda de campanha comprada pelos próprios candidatos no experimento (tokens vermelhos e azuis, que diferenciam propaganda sem custo e propaganda que reduz o payoff dos eleitores). Não há pesquisa eleitoral, agregador, projeção ou boca de urna em nenhum papel: nem como tratamento, nem como variação natural, nem como medida individual em painel. Por isso `Não`, mesmo com c1, c3, c4 e c5 atendidos.
- **c4.** Respondi `Sim` porque o desenho em si (experimento de laboratório aleatorizado, intrassujeitos) está entre os aceitos pelo protocolo; a inadequação do texto está no objeto da exposição (c2), não no método.
- **registro_financiamento = 999.** O documento agradece apoio da International Foundation for Research in Experimental Economics em nota de rodapé na folha de rosto, mas não informa nenhum identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP) nem número de processo ou edital. Como o prompt da variável pede identificadores (número de processo ou edital), e nenhum número consta do documento, registrei 999 em vez de transcrever apenas o nome do financiador.
- **Escolha das evidências.** Segui a orientação do coordenador sobre ligaduras: todas as citações foram escolhidas sem palavras com ff, fi, fl, ffi ou ffl. Isso motivou, por exemplo, citar só o segundo segmento do título ("Advertising, Information, and Voting", sem "Off") e evitar trechos de método com "first" e "specifically".
- **Cobertura da leitura.** O documento tem 46 folhas (43 páginas impressas) e foi lido por inteiro, em três faixas (folhas 1-20, 21-40 e 41-46); a regra de leitura parcial para documentos com mais de 300 páginas não se aplica.
