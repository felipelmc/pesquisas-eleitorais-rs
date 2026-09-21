---
citekey: Fairstein2019a
ficha_id: Fairstein2019a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Fairstein2019a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: elegib-opus5-018
data_fichamento: 2026-09-19
---

## Identificacao
- **texto_confere** — resposta: Sim. O título e os autores do documento (Roy Fairstein, Adam Lauz, Reshef Meir, Kobi Gal; 2019) batem com o registro; o PDF é a cópia do arXiv (1909.10492v1) do artigo dos anais da AAMAS 2019, com a nota de publicação dos anais. — evidência: "Modeling People's Voting Behavior with Poll Information" (p. 1)
- **tipo_documento** — resposta: evento — evidência: "Proc. of the 18th International Conference on Autonomous Agents and Multiagent Systems" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim. Participantes humanos em jogos eleitorais controlados (online e de laboratório) escolhem entre três candidatos com preferências induzidas, depois de ver uma pesquisa não vinculante. — evidência: "where people vote after observing non-binding poll information" (p. 1)
- **c2_intervencao_estudada** — resposta: Sim. A informação de pesquisa é a exposição manipulada pelo experimentador: cada rodada apresenta ao participante uma pesquisa diferente, e os modelos de decisão preveem o voto em função dos escores da pesquisa. — evidência: "the participants with a different poll each time" (p. 5)
- **c3_desfecho** — resposta: Sim. O desfecho é de voto: a escolha individual de candidato em cada rodada (incluindo voto no líder da pesquisa, voto estratégico e voto sincero); não há desfecho de comparecimento. — evidência: "The goal of the paper is to study strategic choices" (p. 1); "and then votes once" (p. 4)
- **c4_desenho_elegivel** — resposta: parcial. São experimentos controlados (online no Mechanical Turk e de laboratório) com pesquisa variada a cada rodada, mas o texto não diz que as pesquisas foram sorteadas e a análise compara a capacidade preditiva de modelos de decisão (validação cruzada), sem comparar o voto entre níveis de exposição. — evidência: "from controlled experiments in which human voters either faced a" (p. 1); "We used a ten-fold cross validation method" (p. 5)
- **c5_estudo_primario** — resposta: Sim. Estudo primário que coleta dados próprios de experimentos de votação e os analisa, junto com dois conjuntos de dados de outros autores. — evidência: "We collect the strategic decisions of 520 people in voting" (p. 2)
- **c6_nao_retratado** — resposta: Sim. Não há aviso de retratação no documento. — evidência: "Modeling People's Voting Behavior with Poll Information" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Não menciona versão anterior deste trabalho. Reanalisa dados publicados em outros artigos: o dataset TMG15, coletado no ambiente de Tal et al. [28] (AAMAS 2015), e o dataset TS16, de Tyszler e Schram [30] (Experimental Economics, 2016); os datasets D32 e D36, coletados pelos autores no ambiente de Tal et al., são próprios. — evidência: "Tal et al. [28] and Tyszler and Schram [30]" (p. 2); "Three of the datasets (D32, D36 and TMG15) were collected using" (p. 4)
- **fonte_dados_amostra** — resposta: Experimentos online próprios (Amazon Mechanical Turk, datasets D32 e D36) com 520 pessoas, três candidatos, até 36 rodadas por participante e mais de 14.000 decisões, mais os datasets reanalisados TMG15 (Tal et al.) e TS16 (laboratório de Tyszler e Schram); o período da coleta não é informado. — evidência: "We collect the strategic decisions of 520 people in voting" (p. 2); "more than 14,000 decisions in total" (p. 2); "were recruited via the Amazon Mechanical Turk" (p. 5)
- **registro_financiamento** — resposta: Israeli Science Foundation, grant nº 773/16; não há pré-registro citado. — evidência: "grant number 773/16" (p. 9)

## Notas do codificador
- Paginação: o PDF (9 páginas) não tem numeração impressa nos cabeçalhos nem nos rodapés; usei o índice do PDF (offset 0). Conferi as páginas 1, 5 e 9: nenhuma traz número impresso.
- texto_confere / tipo_documento: o documento tem o carimbo lateral do arXiv (1909.10492v1, 23 Sep 2019), mas o conteúdo é o artigo dos anais da AAMAS 2019, com a nota de rodapé e o "ACM Reference Format" dos anais. Por isso classifiquei como evento e respondi Sim em texto_confere. Se o coordenador tratar a cópia do arXiv como outra versão do registro, a resposta passaria a parcial.
- c2 e c4: a pesquisa varia de rodada a rodada (within-subject) nos datasets D32 e D36 (o participante vê uma pesquisa ruidosa, p. 4), mas o artigo não descreve como as pesquisas foram geradas nem diz que foram sorteadas. A análise ajusta modelos de decisão individuais (KP, CV, LD, LDLB, AT, AU) e compara o erro de previsão; não estima o efeito da pesquisa sobre o voto comparando níveis de exposição. A Tabela 1 (p. 6) dá o erro do modelo AU por tipo de pesquisa (ordem dos candidatos), não a votação. Marquei c4 como parcial para arbitragem humana. No TS16, a "pesquisa" são as preferências verdadeiras dos outros 11 votantes (p. 5), e não uma pesquisa eleitoral propriamente dita.
- c3: o desfecho é a escolha individual de voto, e os dados permitiriam comparar o voto no líder com o voto no candidato atrás da pesquisa (modelo LDLB, viés de líder). O artigo, porém, só reporta erros de previsão, e a falta de números utilizáveis não é motivo de exclusão.
- Tamanhos de amostra da tabela da p. 4 (não citados como evidência verbatim por ser célula de tabela): participantes D32 = 187, D36 = 335, TMG15 = 437, TS16 = 144; instâncias 4886, 9478, 8011 e 5760. D32 + D36 somam 522, e o texto diz 520 pessoas (p. 2); registro os dois números como aparecem.
- Nenhuma variável com 999.
