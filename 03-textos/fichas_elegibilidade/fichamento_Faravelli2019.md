---
citekey: Faravelli2019
ficha_id: Faravelli2019
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Faravelli2019.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_097
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial: mesmo trabalho em outra versão, o working paper da UNSW Business School (No. 2017 ECON 16, datado de 24 de agosto de 2017), com o mesmo título e os mesmos autores (Faravelli, Kalayci, Pimienta) do registro de 2019 com DOI 10.1007/s10683-019-09620-3 — evidência: "A LARGE-SCALE REAL EFFORT EXPERIMENT" (p. 1)
- **tipo_documento** — resposta: working_paper — evidência: "UNSW Business School Research Paper No. 2017 ECON 16" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, participantes de um jogo eleitoral com dois partidos (A e B) e preferências induzidas, que decidem votar no próprio partido ou se abster, com 1.200 trabalhadores do Amazon Mechanical Turk nos EUA — evidência: "Every agent independently chooses whether to vote for her own party" (p. 6); "A total of 1,200 subjects took part in the experiment" (p. 6)
- **c2_intervencao_estudada** — resposta: Não, a exposição manipulada é o tamanho do eleitorado (30 vs 300) e a probabilidade ex ante de pertencer a cada grupo (eleição apertada vs desigual), não resultado de pesquisa eleitoral; nenhuma pesquisa, agregador ou boca de urna entra como tratamento ou exposição — evidência: "the electorate size (30 vs 300) and the probability of being assigned" (p. 3)
- **c3_desfecho** — resposta: Sim, desfecho de comparecimento: a taxa de comparecimento (proporção de participantes que completa o Estágio 2, equivalente a votar) é a variável dependente; não há medida de escolha entre candidatos — evidência: "Stage 2 constitutes the turnout rate for that treatment" (p. 8)
- **c4_desenho_elegivel** — resposta: Sim, experimento aleatorizado (artefactual field experiment online) com desenho 2 x 2 entre sujeitos e alocação aleatória dos participantes aos quatro tratamentos — evidência: "Workers were randomly assigned to the four treatments" (p. 8)
- **c5_estudo_primario** — resposta: Sim, estudo primário com dados próprios coletados no experimento e análise estatística própria (estatísticas descritivas, testes de Mann-Whitney e regressões) — evidência: "We start our analysis by reporting the descriptive statistics of our sample" (p. 10)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação no documento — evidência: "A LARGE-SCALE REAL EFFORT EXPERIMENT" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Experimento de esforço real conduzido online (Qualtrics) com 1.200 trabalhadores do Amazon Mechanical Turk baseados nos EUA, 300 por tratamento num desenho 2 x 2, iniciado às 16h EDT de 18 de julho de 2016 e com duração aproximada de 24 horas — evidência: "The experiment started at 4pm EDT on 18 July 2016" (p. 8)
- **registro_financiamento** — resposta: Australian Research Council, Discovery Projects, processo DP140102426 (Marco Faravelli e Carlos Pimienta) e Australian Research Council Grant DE160101242 (Kenan Kalayci); não há identificador de pré-registro no documento — evidência: "Discovery Projects funding scheme (project number DP140102426)" (p. 1)

## Notas do codificador
- Offset: a capa (folha de rosto do working paper da UNSW) é a página 1 do PDF e não traz numeração impressa; a página impressa 1 (título, resumo, rodapé com data e financiamento) é a página 2 do PDF e a página impressa 32 (última das referências) é a página 33 do PDF. Logo, impressa P -> PDF = P + 1, offset_pagina: 1. Conferido em duas páginas distantes (impressas 1 e 32). A evidência de `tipo_documento` está na capa, que por essa convenção corresponde à página impressa 0 (página 1 do PDF); registrei "(p. 0)" para manter a regra impressa P -> PDF P+1.
- `texto_confere` = parcial porque o PDF é a versão working paper (UNSW Business School Research Paper No. 2017 ECON 16, "Date: August 24, 2017"), e não o artigo de 2019 na Experimental Economics indicado pelo DOI do registro; título, autores e desenho batem.
- `c1` = Sim: trata-se de um jogo eleitoral com preferências induzidas (cada participante é sorteado para o partido A ou B e recebe prêmio se o seu partido ganha a eleição), que o protocolo aceita em qualquer tamanho de grupo ou sessão. A ressalva é que as instruções aos participantes usam linguagem neutra e não mencionam voto ou eleição ("The rules of the participation game are explained in neutral language", p. 3); a moldura eleitoral está no modelo e na análise dos autores, não no enunciado dado aos sujeitos. Ainda assim, a população e o contexto analisados são de escolha eleitoral com preferências induzidas.
- `c2` = Não: a única informação de agregado dada aos participantes é a probabilidade ex ante γ de pertencer a cada grupo, apresentada em gráfico de pizza, que é parâmetro induzido pelo desenho e não resultado de pesquisa eleitoral (pesquisa pré-eleitoral, agregador, projeção ou boca de urna). O artigo cita literatura sobre pesquisas (p. ex. Agranov, Goeree, Romero e Yariv, 2012), mas não usa resultado de pesquisa como exposição. Como C2 falha, o texto é candidato a exclusão mesmo atendendo a C1, C3, C4, C5 e C6.
- `c3` = Sim apenas na célula de mobilização: o desfecho é comparecimento (decisão de arcar com o custo e "votar"), medido por tratamento e por grupo (Tabelas 3 e 5); não há medida de intenção ou escolha de voto entre candidatos, já que votar no outro grupo não é permitido.
- `outros_relatos_mesmo_estudo` = 999: o documento não menciona versão anterior, tese, relatório ou outro artigo com os mesmos dados. A referência da capa ("UNSW Business School Research Paper No. 2017 ECON 16" e o link do SSRN) identifica o próprio documento, não outro relato; o artigo publicado de 2019 não é citado no texto.
