---
citekey: Gasperoni2015a
ficha_id: Gasperoni2015a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Gasperoni2015a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_094
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — é o mesmo trabalho do registro (título, primeiro autor Gasperoni e ano 2015 batem), mas o arquivo é o manuscrito aceito depositado no repositório IRIS da Universidade de Bolonha, e não a versão publicada com o DOI 10.1017/ipo.2015.3 — evidência: "The Impact of Exposure to Pre-Election Polls on Voting Behaviour" (p. 1); "This is the final peer-reviewed accepted manuscript of:" (p. 1)
- **tipo_documento** — resposta: artigo — artigo de periódico (Italian Political Science Review/Rivista Italiana di Scienza Politica, vol. XLV, n. 1, 2015), aqui na versão de manuscrito aceito — evidência: "(ISSN 0048-8402), XLV, n. 1, 2015, pp. 1-23" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — cerca de 900 eleitores italianos participam de uma campanha eleitoral municipal simulada online e escolhem entre quatro candidatos — evidência: "900 voters were asked to participate in an online simulated election campaign" (p. 2)
- **c2_intervencao_estudada** — resposta: Sim — resultados de pesquisas pré-eleitorais manipulados e exibidos de forma forçada (timed items) aos participantes dos Grupos 1 e 2 são a exposição analisada — evidência: "whether voters actually shift preferences after being exposed to poll results" (p. 19)
- **c3_desfecho** — resposta: Sim — desfecho de voto: a escolha de voto ao fim da campanha simulada e a troca do candidato mais preferido para o segundo preferido após a exposição às pesquisas; não há desfecho de comparecimento — evidência: "19 voters (10% of the total) voted for the second preferred candidate" (p. 20)
- **c4_desenho_elegivel** — resposta: Sim — experimento online: participantes alocados aleatoriamente a grupos de campanha dentro de cada unidade de pesquisa, com exposição manipulada a duas pesquisas desfavoráveis ao candidato preferido nos Grupos 1 e 2, após registro da preferência no nono minuto — evidência: "participants were randomly assigned" (p. 9); "the campaign was suspended after nine minutes" (p. 19)
- **c5_estudo_primario** — resposta: Sim — relata análise própria de dados coletados na simulação de campanha com 895 participantes — evidência: "The final sample comprises 895 participants" (p. 9)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento — evidência: "The Impact of Exposure to Pre-Election Polls on Voting Behaviour" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim — versões preliminares do artigo foram apresentadas na 65th World Association for Public Opinion Research Annual Conference (Hong Kong, junho de 2012) e na 26th Italian Political Science Society Annual Conference (Roma, setembro de 2012); o texto remete a outros relatos do mesmo projeto: Corbetta and Colloca 2013 (descrição do projeto), Russo and Roccato 2013 e Corbetta and Colloca 2014 (heurísticas não relacionadas a pesquisas) — evidência: "Preliminary versions of this article were delivered as papers" (p. 3); "see Corbetta and Colloca 2013" (p. 10)
- **fonte_dados_amostra** — resposta: Simulação online de campanha eleitoral municipal em dynamic process-tracing environment, com 895 participantes recrutados por cotas em seis unidades de pesquisa em diferentes áreas da Itália e trabalho de campo de março a dezembro de 2011; a parte de exposição forçada a pesquisas pré-eleitorais analisa 188 casos dos Grupos 1 e 2 — evidência: "carried out in the period stretching from March to December 2011" (p. 9)
- **registro_financiamento** — resposta: Não há identificador de pré-registro; há financiamento: projeto "Electoral Choice: Voters' Heuristic Strategies and Information Processing", iniciativa PRIN 2008 do Ministério italiano da Universidade e da Pesquisa, processo 2008XZR2TT — evidência: "funded by the Italian University and Research Ministry [grant no. 2008XZR2TT]" (p. 3)

## Notas do codificador
Paginação: o arquivo é o manuscrito aceito depositado no IRIS e não traz numeração impressa em cabeçalho ou rodapé em nenhuma das páginas conferidas (capa p. 1, resumo p. 2, abertura do corpo p. 3, método p. 9-10, resultados p. 19-21, referências e tabelas ao fim). A única marca numérica do documento é um "1" solto no canto superior direito da folha 39 do PDF (a da Tabela A1), que não forma numeração contínua. Por isso registrei `paginacao: indice-do-PDF` e `offset_pagina: 0`, e todas as páginas citadas nas evidências são folhas do PDF (1-based). A capa informa que a versão publicada ocupa as pp. 1-23 do periódico, numeração que não existe neste arquivo; quem for conferir contra a versão publicada precisa refazer o mapeamento.

texto_confere = parcial, e não Sim, porque o documento é outra versão do mesmo trabalho: o próprio arquivo declara ser o manuscrito aceito e remete à versão publicada ("The final published version is available online at: doi.org/10.1017/ipo.2015.3", p. 1). Título, primeiro autor e ano coincidem com os metadados do registro.

c4 = Sim: os participantes foram alocados aleatoriamente aos grupos de campanha dentro de cada unidade de pesquisa e, nos Grupos 1 e 2 (unidades E e F), a exposição às pesquisas pré-eleitorais foi manipulada pelos pesquisadores em timed items, com a preferência registrada antes da exposição e o voto ao final. Registro a ressalva de que, para o desfecho de voto, os autores dizem em nota que não há grupo de controle com intenção de voto registrada no mesmo marco de nove minutos (nota 10, p. 21); a comparação disponível é a preferência do próprio eleitor antes e depois e o contraste entre os Grupos 1 e 2 (9% contra 11% de troca). Considerei isso questão de risco de viés e de dado utilizável, não de categoria de desenho, e pela convenção do projeto falta de dado utilizável não é motivo de Não.

c3: o desfecho é só de voto (escolha e troca de voto na eleição simulada); não há medida de comparecimento, então o texto não entra na célula de mobilização.

Nenhuma variável ficou com 999.
