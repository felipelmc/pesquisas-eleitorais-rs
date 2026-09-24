---
citekey: Pekar2021
ficha_id: Pekar2021
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/Desktop/pesquisas-eleitorais-rs/03-textos/pdfs/Pekar2021.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_e6b_09
data_fichamento: 2026-09-24
---

## Identificacao
- **texto_confere** — resposta: Sim (título e primeiro autor batem com o registro; é a versão revisada por pares do artigo, com o mesmo DOI, depositada no repositório da University of Birmingham) — evidência: "Voting Intentions on Social Media and Political Opinion Polls" (p. 1)
- **tipo_documento** — resposta: artigo — evidência: "Peer reviewed version" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, eleitores da eleição presidencial dos EUA de 2016 (intenções de voto em tweets e em pesquisas nacionais para Clinton e Trump). — evidência: "we analyze data from the 2016 US presidential election" (p. 1)
- **c2_intervencao_estudada** — resposta: Não, as pesquisas eleitorais são a variável prevista (alvo do modelo de previsão), e a exposição/preditor é uma métrica de rede social (índice de intenção de voto no Twitter); não há exposição a pesquisas publicadas. — evidência: "we use the detected voting intentions as a predictor" (p. 5); "we address the task of using social media data to forecast daily opinion polls" (p. 5)
- **c3_desfecho** — resposta: Sim, desfecho de voto: a participação de Clinton/Trump nas intenções de voto das pesquisas nacionais diárias é a variável-alvo da previsão (não há desfecho de comparecimento). — evidência: "we used the 2016 US presidential elections polls data" (p. 26); "is the share of the vote from opinion polls at day" (p. 19)
- **c4_desenho_elegivel** — resposta: Não, estudo observacional agregado de séries temporais (modelos autorregressivos e de aprendizado de máquina para prever pesquisas), sem variação identificada da exposição a pesquisas. — evidência: "We use conventional autoregressive models that include past observations of polls" (p. 19)
- **c5_estudo_primario** — resposta: Sim, estudo primário com coleta e análise própria de tweets e de dados de pesquisas. — evidência: "A collection of about 386 million election-related tweets were continuously collected" (p. 15)
- **c6_nao_retratado** — resposta: Sim, não há aviso de retratação no documento. — evidência: "Voting Intentions on Social Media and Political Opinion Polls" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Cerca de 386 milhões de tweets sobre a eleição presidencial dos EUA coletados de dezembro de 2015 a novembro de 2016 (48.881 tweets de 41.029 autores no índice final de intenção de voto), combinados com 1.106 pesquisas nacionais de 54 institutos (dados do FiveThirtyEight, 340 observações diárias). — evidência: "A collection of about 386 million election-related tweets were continuously collected" (p. 15); "produced 48,881 tweets written by 41,029 unique authors" (p. 19); "used data from 1106 nationwide surveys conducted by 54 pollsters" (p. 27)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação e offset: a página 1 do PDF é a capa do repositório da University of Birmingham (sem número impresso); a página 2 do PDF traz o número impresso 1 (título e resumo) e a página 52 do PDF traz o número impresso 51 (fim das referências). Logo, impressa P → PDF = P + 1 (offset 1), conferido também nas páginas impressas 15, 19, 26 e 27. A capa (PDF 1) corresponde a p. 0 por esse offset; é ali que está a evidência de tipo_documento.
- texto_confere: o documento é o manuscrito aceito ("Peer reviewed version") do artigo publicado em Government Information Quarterly, com o mesmo DOI (10.1016/j.giq.2021.101658) do registro. A capa lista seis autores (Pekar, Najafi, Binner, Swanson, Rickard, Fry); os metadados do registro trazem os quatro primeiros, na mesma ordem. Tratei como Sim (mesmo trabalho, versão revisada por pares), e não como 'parcial', porque não é preprint nem working paper; o coordenador pode reclassificar se a convenção do projeto tratar o manuscrito aceito como outra versão.
- c2 e c4 decidem a exclusão: as pesquisas eleitorais aparecem só como alvo de previsão (e como contexto na introdução, que cita efeitos das pesquisas sobre o voto na literatura), e o preditor é uma métrica de rede social, que o protocolo exclui como exposição. O desenho é previsão de séries temporais agregadas, sem variação identificada da exposição.
- c3 respondido Sim porque o estudo analisa intenção de voto agregada por candidato (participação nas pesquisas), embora não como resposta à exposição a pesquisas.
- Não há seção de financiamento nem menção a pré-registro; os agradecimentos (p. 41) citam só pareceristas. Não há menção a outros relatos do mesmo estudo (Pekar 2020, citado na p. 13, é sobre intenção de compra, outro estudo).
