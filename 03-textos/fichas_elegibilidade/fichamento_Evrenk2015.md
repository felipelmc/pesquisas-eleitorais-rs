---
citekey: Evrenk2015
ficha_id: Evrenk2015
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Evrenk2015.pdf
paginacao: impressa
offset_pagina: 2
agente_fichador: fichador_el_160
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o título e os autores batem com o registro, mas o PDF é a versão estendida em working paper (MPRA Paper No. 62794) do artigo publicado em Public Choice com o DOI do registro — evidência: "Social interactions in voting behavior: distinguishing between" (p. 0); "This is an extended version of an article with the same name" (p. 0)
- **tipo_documento** — resposta: working_paper — evidência: "MPRA Paper No. 62794" (p. -1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores reais da eleição geral britânica de 2005 (amostra da Inglaterra do British Election Study), escolhendo entre Trabalhistas, Conservadores e Liberais Democratas — evidência: "we employ data obtained from the 2005 British Election Studies" (p. 2)
- **c2_intervencao_estudada** — resposta: Não — a exposição analisada é a expectativa subjetiva do próprio respondente sobre quem vence a disputa no seu distrito (pergunta de win-chance do survey), não resultado de pesquisa eleitoral divulgada; pesquisas pré-eleitorais aparecem apenas como o pressuposto de estudos anteriores que os autores rejeitam — evidência: "we use the subjective chance ranking elicited from voter responses" (p. 8); "rational expectations grounded in pre-election polls" (p. 4)
- **c3_desfecho** — resposta: Sim — desfecho de voto: a variável dependente é a escolha de voto entre os três partidos principais (não há medida de comparecimento; abstencionistas são excluídos da subamostra) — evidência: "The dependent variable is voting choice" (p. 23)
- **c4_desenho_elegivel** — resposta: parcial — é survey individual com expectativas medidas na onda pré-eleitoral e voto na onda pós-eleitoral, comparando níveis de expectativa num probit multinomial, mas sem aleatorização nem variação exógena identificada da exposição a pesquisas eleitorais — evidência: "The overall study comprised a series of linked surveys" (p. 5); "The model is estimated using multinomial probit, as opposed to multinomial logit" (p. 11)
- **c5_estudo_primario** — resposta: Sim — estudo primário com análise própria dos microdados do BES 2005 — evidência: "The primary data source for the present study is the dataset" (p. 5)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento — evidência: "Social interactions in voting behavior:" (p. -1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim — o documento se declara versão estendida do artigo homônimo publicado em Public Choice, vol. 162, p. 405-23, e versão revista de um capítulo da tese de doutorado do segundo autor (Sher 2012, Boston University) — evidência: "This is an extended version of an article with the same name" (p. 0); "This paper is a heavily revised version of a chapter" (p. 17)
- **fonte_dados_amostra** — resposta: Survey do British Election Study 2005 (ondas pré e pós-eleitoral ligadas), amostra da Inglaterra na eleição geral de 5 de maio de 2005, com N = 1.929 na amostra pré-eleitoral da Inglaterra e 1.147 observações na regressão principal (Tabela 5) — evidência: "In the England sample (N = 1,929) of the BES pre-election survey" (p. 9); "This election took place on 5 May 2005" (p. 2)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset: a capa do MPRA (folha 1 do PDF) e a folha de rosto com o resumo (folha 2) não têm numeração impressa; o corpo começa na folha 3 com o rodapé "1" e termina na folha 28 com o rodapé "26". Logo, folha do PDF = página impressa + 2 (offset_pagina: 2), confirmado em três pontos distantes: impressa 1 → folha 3, impressa 12 → folha 14 e impressa 26 → folha 28. Pelas páginas sem numeração impressa, a fórmula dá p. 0 para a folha de rosto e p. -1 para a capa do MPRA, e é assim que elas estão anotadas nas evidências.
- texto_confere = parcial (e não Sim) porque o PDF é o preprint/working paper do MPRA, explicitamente descrito como versão estendida do artigo com o mesmo nome publicado em Public Choice — o DOI do registro (10.1007/s11127-015-0241-3) aparece no documento como link para a publicação final, não como identificador deste arquivo.
- c2 = Não: o objeto empírico é a expectativa subjetiva individual sobre quem vence no distrito, elicitada pela pergunta de win-chance do BES, combinada com a percepção do peso do próprio voto (pergunta de impact). Nenhum resultado de pesquisa eleitoral divulgada é manipulado, embargado ou medido como exposição; a referência a pesquisas pré-eleitorais é feita para criticar o pressuposto de expectativas racionais de estudos anteriores. O "efeito manada" aqui é medido como propensão a votar no vencedor esperado pelo próprio respondente, não como reação à divulgação de uma pesquisa.
- c4 = parcial: o desenho tem o formato de painel individual (expectativas na onda pré-eleitoral, voto relatado na onda pós-eleitoral, comparação entre níveis de expectativa num probit multinomial com controles), o que não é o caso de exclusão por "observacional agregado" nem de "percepção autodeclarada sem comparação"; mas a exposição relevante para o protocolo (pesquisa eleitoral) não existe e não há variação identificada de exposição. Deixei em parcial para que a arbitragem humana decida se a ausência de exposição do protocolo já basta para reprovar por C2 isoladamente.
- registro_financiamento = 999: os Agradecimentos (p. 17) mencionam apenas colegas que comentaram o texto, sem número de processo, edital ou registro prévio (OSF, AEA, RIDIE, EGAP).
- Documento curto (28 folhas): lido por inteiro, nas faixas de folhas 1-14 e 15-28 do PDF.
