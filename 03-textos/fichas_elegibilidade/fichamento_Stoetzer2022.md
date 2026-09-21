---
citekey: Stoetzer2022
ficha_id: Stoetzer2022
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Stoetzer2022.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_111
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — evidência: "Learning from Polls During Electoral Campaigns" (p. 1)
- **tipo_documento** — resposta: artigo — evidência: "ORIGINAL PAPER" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — respondentes adultos dos EUA recrutados no MTurk, colocados numa eleição hipotética entre dois partidos (estudo I) e numa disputa entre candidato democrata e republicano às vésperas da eleição presidencial de 2020 (estudo II), com identificação partidária medida. — evidência: "presents a hypothetical election environment where party A and party B" (p. 11); "Our sample consists of 2000 respondents that we recruited via Amazon MTurk" (p. 15)
- **c2_intervencao_estudada** — resposta: Sim — o resultado de pesquisa eleitoral é a exposição manipulada: os respondentes recebem sequências de três resultados de pesquisa, com variação experimental da direção da sequência e, no estudo II, da fonte (MSNBC/Fox) e do candidato à frente. — evidência: "sequentially present respondents with three sets of changing polling results" (p. 3); "we vary the source (MSNBC, Fox) and the candidate that is winning" (p. 15)
- **c3_desfecho** — resposta: Não — o desfecho é a crença/expectativa sobre a parcela de votos dos partidos ou candidatos e sobre as chances de vitória, elicitada pelas questões de Manski; não há intenção de voto, escolha de voto, votação agregada nem comparecimento. — evidência: "based on which respondents can infer the winning chances of party A" (p. 11); "We again elicit beliefs about the vote share of the winning candidate" (p. 15)
- **c4_desenho_elegivel** — resposta: Sim — dois survey experiments com aleatorização das condições (crenças prévias instiladas, sequência ascendente/descendente de pesquisas, fonte e candidato vencedor). — evidência: "we conduct two survey experiments to evaluate the Bayesian learning model" (p. 10); "Respondents are further randomized into two conditions" (p. 12)
- **c5_estudo_primario** — resposta: Sim — estudo primário com dados próprios coletados em dois experimentos de survey no MTurk e análise própria por um modelo bayesiano dinâmico. — evidência: "We recruited 1388 respondents from the crowdsourcing platform Amazon" (p. 13)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento. — evidência: "Learning from Polls During Electoral Campaigns" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim — a nota de agradecimentos informa que uma versão anterior do trabalho foi apresentada em conferências e workshops (EPSA 2019, SVPW 2021, Berlin Political Behaviour Workshop 2021, workshop da cátedra de metodologia política da Universidade de Zurique em Villa Garbald, 2019); não há menção a tese, dissertação, working paper ou artigo com os mesmos dados. — evidência: "Earlier version was presented at the EPSA annual conference in Belfast 2019" (p. 1)
- **fonte_dados_amostra** — resposta: Dois survey experiments online no Amazon MTurk (EUA) com resultados fictícios de pesquisa eleitoral: estudo I com 1388 respondentes no início de abril de 2020 e estudo II com 2000 respondentes entre 28 de setembro e 20 de outubro de 2020, antes da eleição presidencial. — evidência: "We recruited 1388 respondents from the crowdsourcing platform Amazon" (p. 13); "Our sample consists of 2000 respondents that we recruited via Amazon MTurk" (p. 15)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: o PDF é a versão Springer com "Published online: 08 December 2022" e não traz numeração impressa em nenhuma página (conferi cabeçalho e rodapé da p. 1, da p. 11 e da p. 22, isto é, as duas extremidades e o meio do documento: o cabeçalho traz só "Political Behavior" e o rodapé só a marca da Springer). Por isso `paginacao: indice-do-PDF` e `offset_pagina: 0`; todas as páginas citadas são o índice 1-based do PDF.
- c1: respondi Sim porque a população são eleitores dos EUA num contexto eleitoral (disputa hipotética entre dois partidos no estudo I; disputa entre candidato democrata e republicano, com partidarismo medido, no estudo II), e o protocolo aceita eleição hipotética ou de laboratório. Registro, porém, a ressalva de que os participantes não chegam a escolher entre os candidatos: só declaram crenças sobre a parcela de votos. Essa ausência de escolha é o que faz o texto falhar em c3, não em c1.
- c3: respondi Não porque o único desfecho medido é a crença sobre a parcela de votos e sobre quem vence a disputa (expectativa de vitória), justamente o caso que o prompt manda excluir. Não há medida de intenção de voto, escolha de voto, votação agregada nem comparecimento em nenhum dos dois experimentos; o texto só menciona consequências para o comportamento eleitoral como implicação na discussão. Não é caso de "falta de dados numéricos utilizáveis".
- registro_financiamento: 999 porque o documento não traz identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP) nem número de processo ou edital. O que existe, e não atende ao que o prompt pede, é uma nota de financiamento sem número ("Open Access funding enabled and organized by Projekt DEAL", p. 20) e um DOI de materiais de replicação no Dataverse (10.7910/DVN/IW4FP8, nota de rodapé 11, p. 11), que registro aqui para o coordenador.
- Li o documento inteiro (p. 1 a 22) em duas faixas, com a ferramenta Read. O material suplementar (SM A–E) é citado várias vezes no texto, mas não está no PDF; nenhuma resposta depende dele.
- Nas evidências evitei trechos com ligaduras tipográficas (ff, fi, fl) e com apóstrofos, e não usei fragmentos quebrados por hifenização de fim de linha.
