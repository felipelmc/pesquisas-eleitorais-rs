---
citekey: Fairstein2018a
ficha_id: Fairstein2018a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Fairstein2018a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: elegib-opus5-020
data_fichamento: 2026-09-19
---

## Identificacao
- **texto_confere** — resposta: Sim. O título e o primeiro autor (Roy Fairstein) no documento batem com o registro; é o preprint arXiv 1805.07606 (v1, 19 maio 2018), a mesma versão do DOI 10.48550/arxiv.1805.07606. — evidência: "Predicting Strategic Voting Behavior with Poll Information" (p. 1)
- **tipo_documento** — resposta: preprint — evidência: "arXiv:1805.07606v1" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim. Sujeitos humanos com preferências induzidas (ditadas) votam por regra de pluralidade entre 3 candidatos num jogo eleitoral experimental online com informação de pesquisa. — evidência: "human subjects with dictated preferences are exposed to a poll" (p. 2)
- **c2_intervencao_estudada** — resposta: Sim. A informação de pesquisa (poll) exibida antes do voto varia de rodada a rodada no experimento de origem, e o artigo modela a decisão de voto em função dela; os resultados são separados por cenário, definido pela ordem dos candidatos na pesquisa. — evidência: "each time with different preferences and poll information" (p. 7); "This work focuses on modeling strategic voting behavior under poll information" (p. 1)
- **c3_desfecho** — resposta: Sim. Desfecho de voto: a escolha individual entre Q, Q' e Q'' em cada rodada, analisada por cenário da pesquisa. Não há desfecho de comparecimento. — evidência: "make a single voting decision under the Plurality rule" (p. 2)
- **c4_desenho_elegivel** — resposta: parcial. Os dados vêm de experimentos controlados em que a pesquisa varia entre rodadas (desenho aceito), mas o documento não descreve aleatorização. A análise própria é o ajuste preditivo (leave-one-out) de modelos de decisão, e não uma comparação de efeito entre níveis de exposição. — evidência: "voting scenarios in controlled experiments involving humans" (p. 7); "The prediction was performed using leave-one-out method" (p. 8)
- **c5_estudo_primario** — resposta: Sim. Estudo empírico com análise própria (reanálise e modelagem) de dados de experimento coletados por Tal et al.; não é revisão. — evidência: "We evaluated the different models on data obtained from Tal et al." (p. 7)
- **c6_nao_retratado** — resposta: Sim. Não há aviso de retratação no documento. — evidência: "Predicting Strategic Voting Behavior with Poll Information" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim. Os dados são os do experimento de Tal, Meir e Gal, "A study of human behavior in online voting" (AAMAS 2015, pp. 665–673, versão completa em tinyurl.com/yczxugoj): é um artigo com os mesmos dados. — evidência: "We use the data of Tal et al." (p. 2); "A study of human behavior in online voting" (p. 13)
- **fonte_dados_amostra** — resposta: Dados de experimentos controlados de votação online de Tal et al. (parte disponível em votelib.org): 595 sujeitos, cada um com até 20 rodadas de votação com 3 candidatos. Período de coleta não informado. — evidência: "The data was obtained from 595 distinct subjects" (p. 7); "Each subject played up to 20 rounds of voting with 3 candidates" (p. 7)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: o PDF (preprint arXiv, 17 páginas) não tem numeração impressa em nenhuma página. Conferi as páginas 1, 2, 7, 8 e 13, e as demais na leitura integral. Por isso uso o índice do PDF, com offset 0.
- texto_confere: o registro aponta para o DOI do próprio arXiv (10.48550/arxiv.1805.07606), então o documento é a versão registrada ("Sim" e não "parcial"). Autores no documento: Roy Fairstein, Adam Lauz, Kobi Gal, Reshef Meir.
- c2: a pesquisa aqui é uma pesquisa simulada de laboratório ("The poll provided a noisy indication of the results of the voting", p. 7), manipulada pelo experimento de origem. O artigo a trata como a informação central da decisão, e as tabelas de resultados são separadas pelos seis cenários de ordem na pesquisa (Tabela 2, p. 9; matrizes de confusão por cenário, Figura 4, p. 10). Marquei "Sim" com base na convenção de jogos eleitorais de laboratório com informação de pesquisa. O limite do caso é que o artigo não estima o efeito da pesquisa sobre o voto: ele mede a acurácia preditiva de modelos.
- c3: a variável analisada é a ação de voto do sujeito em cada rodada (as linhas das matrizes de confusão são "the action of the subject", p. 10). Isso permite, em princípio, comparar o voto em Q quando a pesquisa o põe à frente (cenário A) e atrás (cenários E e F). O documento não traz essas proporções prontas, mas a falta de dados numéricos utilizáveis não é motivo de exclusão.
- c4: marquei "parcial" por dois motivos. (1) O documento fala em "controlled experiments" (p. 2 e p. 7), com variação da pesquisa dentro do sujeito entre rodadas, mas não diz se a atribuição dos cenários foi aleatória. (2) A análise própria do artigo é um ajuste preditivo de modelos de decisão (f-measure, leave-one-out), não uma comparação de desfecho entre níveis de exposição. O desenho que gerou os dados (experimento) está entre os aceitos. Fica para arbitragem decidir se basta o desenho de origem ou se vale a análise deste relato.
- c5: os dados foram coletados por outro grupo (Tal et al. [16], com Meir e Gal também coautores deste artigo), mas o artigo faz análise própria. Por isso "Sim", e não revisão.
- Incentivo monetário do experimento de origem: 10¢ por rodada em que Q (o preferido) é eleito, 5¢ para Q' e 0¢ para Q'' (p. 7).
- registro_financiamento: não há agradecimentos, nota de financiamento nem pré-registro no documento.
