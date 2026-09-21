---
citekey: Tyszler2015
ficha_id: Tyszler2015
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Tyszler2015.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_119
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — título e primeiro autor batem com o registro, mas o PDF é a versão de manuscrito do mesmo trabalho (sem identificação de periódico, com marcadores de diagramação do tipo "[FIGURE 1 HERE]" e figuras/tabelas no fim) — evidência: "Information and Strategic Voting" (p. 0)
- **tipo_documento** — resposta: preprint — manuscrito do artigo, sem folha de rosto ou nota de publicação em periódico — evidência: "comments on an earlier draft of this manuscript" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — participantes com preferências induzidas votam entre três opções (A, B, C) em eleitorados de laboratório de 12 votantes — evidência: "288 student subjects participated in 24 independent electorates" (p. 13)
- **c2_intervencao_estudada** — resposta: Sim — a informação sobre a distribuição de preferências do eleitorado é manipulada entre tratamentos (informado vs. não informado) e é declaradamente uma pesquisa pré-eleitoral sem ruído — evidência: "possible publication of (noiseless) pre-election polls" (p. 6); "situation in which an opinion poll truthfully reveals" (p. 3)
- **c3_desfecho** — resposta: Sim — desfecho de voto: a escolha de voto de cada participante entre A, B e C (sincero, estratégico ou dominado) e a distribuição de votos por tratamento; não há desfecho de comparecimento porque o voto é obrigatório no desenho — evidência: "required to cast one vote for A, B or C" (p. 14); "table 2 shows for each treatment the distribution of votes" (p. 15)
- **c4_desenho_elegivel** — resposta: Sim — experimento de laboratório com desenho fatorial 2x2 entre sujeitos e preferências sorteadas com igual probabilidade — evidência: "design therefore requires four treatments" (p. 13); "which are assigned with equal probability to each subject" (p. 13)
- **c5_estudo_primario** — resposta: Sim — estudo primário, com análise dos próprios dados experimentais — evidência: "We use laboratory experiments for our empirical analysis of strategic voting." (p. 3)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento — evidência: "Information and Strategic Voting" (p. 0)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: menciona, em nota de rodapé, o artigo dos mesmos autores Tyszler and Schram (2013), "Voting in Heterogeneous Electorates: An Experimental Study", Games 4: 624-647, citado para robustez a heterogeneidade; o documento não afirma que esse artigo relate o mesmo estudo nem que use os mesmos dados — evidência: "Our results are robust to heterogeneity in" (p. 5)
- **fonte_dados_amostra** — resposta: experimento de laboratório no CREED, Universidade de Amsterdã, em novembro-dezembro de 2008, com 12 sessões, 288 estudantes e 24 eleitorados independentes de 12 votantes, cada eleitorado em 40 eleições; mais duas sessões-piloto na Fundação Getúlio Vargas, São Paulo, em agosto de 2007 — evidência: "sessions were run at the CREED laboratory at the University of Amsterdam" (p. 13); "pilot sessions were run at Fundação Getúlio Vargas, São Paulo, Brazil" (p. 14)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset de página: a primeira página do PDF é a folha de rosto, sem número impresso; o número impresso "1" está no rodapé da segunda página do PDF (início da Introdução) e o número impresso "31" está no rodapé da 32ª página do PDF (Table 3). Logo, página impressa P → página do PDF = P + 1, isto é, `offset_pagina: 1`. As duas conferências foram feitas em páginas distantes (impressa 1 e impressa 31).
- Folha de rosto sem número impresso: como o codebook exige o título da primeira página como evidência em `texto_confere` e `c6_nao_retratado`, essas citações foram registradas como (p. 0), que é o valor coerente com o offset declarado (0 + 1 = primeira página do PDF).
- `texto_confere` = parcial porque o PDF é claramente a versão de manuscrito do mesmo trabalho: título ("Information and Strategic Voting") e autores (Marcelo Tyszler e Arthur Schram) batem com o registro, mas não há cabeçalho de periódico, volume, DOI ou paginação de revista; o texto traz marcadores "[FIGURE 1 HERE]", "[TABLE 1 HERE]" e reúne figuras e tabelas depois das referências. Pela mesma razão, `tipo_documento` = preprint, e não artigo.
- `c2`: o tratamento manipulado é a informação sobre a distribuição das preferências do eleitorado, que os autores apresentam explicitamente como a publicação de uma pesquisa pré-eleitoral sem ruído ("noiseless" pre-election poll) e operacionalizam informando aos participantes, antes do voto, quantos votantes foram designados a cada ordenação de preferências. Enquadra-se na convenção do projeto para jogos eleitorais de laboratório com informação de pesquisa.
- `c3`: o desenho impõe voto obrigatório, então não há desfecho de comparecimento; o desfecho analisado é a escolha de voto (sincero, estratégico ou pela opção dominada) e o vencedor da eleição, inclusive com comparação entre quem apoia o candidato à frente e quem apoia os que estão atrás nas "sincere polls" (Rank 1st, 2nd, 3rd).
- `registro_financiamento` = 999: nos agradecimentos há menção a apoio financeiro (Antoni Serra Ramoneda UAB - Caixa Catalunya Research Chair, Department of Business studies e Research Priority Area Behavioral Economics da Universidade de Amsterdã), mas sem número de processo, edital ou identificador de pré-registro; o documento também não cita registro em OSF, AEA RCT Registry, RIDIE ou EGAP. Como a variável pede identificadores, e eles não existem no texto, a resposta é 999 (informação ausente), não os nomes dos financiadores.
- Nas citações, foram preferidos trechos sem ligaduras tipográficas (ff, fi, fl) e contidos em uma única linha do PDF.
