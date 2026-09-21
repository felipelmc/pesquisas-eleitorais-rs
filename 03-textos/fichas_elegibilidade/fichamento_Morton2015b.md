---
citekey: Morton2015b
ficha_id: Morton2015b
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Morton2015b.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_122
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o título, os autores e o ano batem com os metadados, mas o PDF é a versão em manuscrito (datada de 9 de abril de 2015, espaçamento duplo, paginação própria 1-47, sem identificação do periódico), não o artigo diagramado do DOI informado — evidência: "What motivates bandwagon voting behavior: Altruism or a desire to win?" (p. 1)
- **tipo_documento** — resposta: artigo — manuscrito de artigo de periódico: traz resumo, JEL classification, keywords e agradece ao editor e a dois pareceristas anônimos — evidência: "grateful to the editor Heinrich Ursprung and two anonymous referees" (p. 37)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — participantes de um jogo eleitoral de laboratório, com preferências induzidas, que escolhem entre o partido A, o partido B ou a abstenção — evidência: "we study a simple voting game in which there are 10 voters" (p. 18); "A total of 120 subjects from the undergraduate student population participated" (p. 22)
- **c2_intervencao_estudada** — resposta: Não — a exposição manipulada é a divulgação da distribuição de votos das eleições anteriores do próprio experimento (e a publicidade do voto), isto é, resultado de eleição passada, e não resultado de pesquisa eleitoral — evidência: "revealing vote distributions after each election" (p. 24); "information about previous voting behavior in prior elections" (p. 24)
- **c3_desfecho** — resposta: Sim — o desfecho é de voto e de comparecimento: voto no outro partido (bandwagon vote choices) e taxa de abstenção por tipo de eleitor — evidência: "We measure the percentage of abstention on the vertical axis" (p. 27); "summarizes other party voting by voter type and privacy treatment" (p. 31)
- **c4_desenho_elegivel** — resposta: Sim — experimento de laboratório com alocação aleatória de papéis e tratamentos de privacidade (voto secreto, voto secreto com informação, voto público) cruzados com duas regras de votação — evidência: "The experiment was conducted at NYU" (p. 22); "subjects were randomly given the sealed envelopes" (p. 23); "summarizes the treatments, parameters, number of subjects and sessions" (p. 27)
- **c5_estudo_primario** — resposta: Sim — estudo primário: os autores conduzem um experimento próprio e analisam os dados gerados por ele — evidência: "In this paper we present an experiment designed to evaluate the extent" (p. 4); "A total of 120 subjects from the undergraduate student population participated" (p. 22)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação em nenhuma parte do documento — evidência: "What motivates bandwagon voting behavior" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: experimento de votação em laboratório no Center for Experimental Social Science da NYU, com 120 estudantes de graduação recrutados em um subject pool, 6 a 8 períodos por sessão e, segundo a Tabela 3, 2 sessões e 20 sujeitos por célula de tratamento; o documento não informa o período (datas) de coleta — evidência: "A total of 120 subjects from the undergraduate student population participated" (p. 22); "Subjects were recruited via a subject pool" (p. 22)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: a numeração impressa coincide com o índice do PDF. Confirmei em páginas distantes: a página 1 do PDF traz "1" no rodapé (folha de rosto), a página 22 do PDF traz "22" (seção 3.4, "Subjects and basic procedures") e a página 47 do PDF traz "47" (fim das referências). Logo, `offset_pagina: 0` e as citações usam a numeração impressa.
- Li o documento inteiro (páginas 1-47), em três faixas de leitura pela ferramenta Read.
- `texto_confere` = parcial: título ("What motivates bandwagon voting behavior: Altruism or a desire to win?"), autores (Rebecca B. Morton; Kai Ou) e ano (2015) batem exatamente com os metadados do registro. Codifiquei "parcial" porque o arquivo é outra versão do mesmo trabalho: manuscrito datado de 9 de abril de 2015, sem cabeçalho, volume ou paginação de periódico, com numeração própria de 1 a 47. Os agradecimentos ao editor e a dois pareceristas anônimos (p. 37) indicam que é o manuscrito aceito do artigo correspondente ao DOI. É o texto certo, mas as páginas citadas nesta ficha são as do manuscrito, não as do artigo publicado.
- `tipo_documento` = artigo: o documento não se declara working paper nem preprint em nenhum lugar; a estrutura (resumo, JEL classification, keywords) e os agradecimentos ao editor e aos pareceristas indicam artigo de periódico. Ver a nota acima sobre a versão.
- `c2_intervencao_estudada` = Não, e é a decisão limítrofe desta ficha. O experimento manipula (a) a privacidade do voto (voto secreto, voto secreto com informação, voto público) e (b) a regra de votação (Regra 1, com maioria de tipo A; Regra 2, com grupos iguais e vantagem institucional de A). A única informação sobre escolhas alheias que os sujeitos recebem é a distribuição de votos revelada *depois* de cada eleição, isto é, o resultado das rodadas anteriores do próprio jogo (pp. 24 e 29). Não há pesquisa pré-eleitoral, agregador, projeção nem boca de urna no desenho: o protocolo trata resultado de eleição passada como exposição não elegível, por isso "Não". Pesquisas eleitorais aparecem no texto apenas como literatura e motivação (p. ex. a discussão de Agranov et al. 2013, p. 15, e a menção a controles sobre pesquisas nas implicações, p. 36), o que também é caso de "Não" pelo prompt da variável. Se o coordenador entender que a revelação da distribuição de votos das rodadas anteriores em jogo de laboratório equivale a "informação de pesquisa", a resposta viraria "Sim"; registro a alternativa para arbitragem.
- `c3` e `c4` foram respondidos sobre o desenho e os desfechos do estudo, independentemente do resultado de `c2`: os desfechos (abstenção e voto no outro partido) e o desenho (experimento aleatorizado de laboratório) são elegíveis pelo protocolo.
- `outros_relatos_mesmo_estudo` = 999: o documento cita trabalhos próprios relacionados (Morton e Ou 2013, "The secret ballot and other-regarding voting"; Morton e Ou 2014, "The secret ballot in the laboratory"; Morton et al. 2014, sobre boca de urna), mas em nenhum momento os apresenta como outro relato deste mesmo experimento — são citados como literatura anterior. Não infiro ligação de estudo a partir da coautoria.
- `registro_financiamento` = 999: há agradecimento genérico de apoio institucional nos Acknowledgements (p. 37, apoio da New York University), mas nenhum identificador de pré-registro (OSF, AEA, RIDIE, EGAP) nem número de processo ou edital, que é o que a variável pede transcrever.
