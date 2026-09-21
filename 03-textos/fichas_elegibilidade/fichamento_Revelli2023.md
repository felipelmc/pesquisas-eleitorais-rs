---
citekey: Revelli2023
ficha_id: Revelli2023
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Revelli2023.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_153
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — é o mesmo trabalho ("Ties", primeiro autor Revelli), mas em versão preprint de maio de 2019 depositada no repositório da Universidade de Torino, com dois autores (Revelli e Tsai) e sem o terceiro autor do registro (Wu); a folha de rosto declara ser o preprint do artigo publicado com o DOI 10.1007/s00355-023-01476-0 — evidência: "Ties" (p. 0); "This is a pre print version of the following article:" (p. 0)
- **tipo_documento** — resposta: preprint — evidência: "This is a pre print version of the following article:" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores e unidades eleitorais agregadas (municípios italianos) em eleições municipais reais para prefeito, entre 2001 e 2017 — evidência: "We perform the empirical analysis on a panel dataset" (p. 16); "all Italian municipalities have direct election of the mayor" (p. 17)
- **c2_intervencao_estudada** — resposta: Não — a exposição analisada é a informação sobre o resultado de uma eleição municipal vizinha que terminou empatada ou foi decidida por um voto, isto é, resultado de eleição passada, e não resultado de pesquisa eleitoral (pesquisas eleitorais não aparecem como tratamento, exposição ou objeto do estudo) — evidência: "It is the informational consequences of these rare events" (p. 4); "on voter turnout rates of exposure for geographical reasons to spill-overs" (p. 1)
- **c3_desfecho** — resposta: Sim — o desfecho é de comparecimento: a taxa de comparecimento eleitoral agregada por município nas eleições subsequentes (e a variação do comparecimento entre os dois turnos); não há medida de intenção ou escolha de voto em candidato — evidência: "we regress the change in turnout in percentage points" (p. 22)
- **c4_desenho_elegivel** — resposta: Sim — quase-experimento com variação identificada da exposição, explorando o calendário eleitoral municipal escalonado e a ocorrência de empates e resultados decididos por um voto, estimado em painel de municípios — evidência: "the quasi-experimental conditions created by the staggered municipal electoral calendar" (p. 1)
- **c5_estudo_primario** — resposta: Sim — estudo primário: modelo teórico próprio e análise econométrica própria de um painel de eleições municipais italianas coletado pelos autores — evidência: "Table 3 reports the 42 cases of elections ending in a tie" (p. 21)
- **c6_nao_retratado** — resposta: Sim — não há marca "RETRACTED", nota ou página de retratação no documento — evidência: "Ties" (p. 0)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim — a folha de rosto do repositório AperTO declara que este arquivo é a versão preprint do artigo publicado, cujo DOI é 10.1007/s00355-023-01476-0 — evidência: "This is a pre print version of the following article:" (p. 0)
- **fonte_dados_amostra** — resposta: Painel de eleições municipais italianas cobrindo 2001 a 2017, restrito aos cerca de 7.000 municípios das quinze regiões de estatuto ordinário da Itália continental — evidência: "spanning through almost twenty years (2001 to 2017)" (p. 16); "we focus on the around 7,000 localities" (p. 16)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação e offset: o PDF tem 35 folhas; a folha 1 é a capa do repositório institucional AperTO (Università di Torino), sem numeração impressa, e a folha 2 traz a página impressa 1 (título "Ties"). A fórmula folha = página impressa + 1 foi conferida em quatro pontos distantes: página impressa 1 (título e resumo) na folha 2; página impressa 16 (Tabela 1 e início da seção 3) na folha 17; página impressa 21 (seção 4.1) na folha 22; página impressa 34 (última página de referências) na folha 35. A capa, por não ter número impresso, foi anotada como p. 0, valor que satisfaz a fórmula.
- Todas as citações foram retiradas de páginas efetivamente reabertas e conferidas na numeração impressa; foram escolhidos trechos curtos e sem palavras com ligaduras tipográficas (ff, fi, fl).
- `texto_confere` = parcial (e não Sim) porque o documento é o preprint de maio de 2019, assinado por dois autores, enquanto o registro descreve o artigo publicado em 2023 com três autores (Revelli, Tsai e Wu). O título e o primeiro autor coincidem, e a própria capa do repositório liga esta versão ao DOI do registro.
- `c2_intervencao_estudada` = Não é o motivo decisivo de exclusão: a exposição estudada é o resultado (empate ou diferença de um voto) de uma eleição municipal anterior em localidade vizinha, expressamente listado no codebook entre as exposições que levam a "Não" ("resultados de eleições passadas"). Não há pesquisa pré-eleitoral, agregador, projeção ou boca de urna como tratamento; o texto sequer usa pesquisas como fonte de dados. A menção a pesquisas pré-eleitorais no texto (por exemplo, a discussão de Bursztyn et al., 2018, na introdução) é apenas revisão de literatura, não objeto empírico.
- `c4_desenho_elegivel` = Sim considera apenas a forma do desenho, que é elegível pelo protocolo (quase-experimento com variação identificada, calendário escalonado, painel com efeitos fixos); a inadequação do estudo está na exposição (C2), não no desenho.
- `c3_desfecho` = Sim pela alínea (b) do critério: o desfecho é comparecimento agregado, que entra na célula de mobilização. Não há desfecho de voto em candidato, partido ou opção.
- `registro_financiamento` = 999: os agradecimentos (p. 32) citam apenas participantes de seminários e assistência de pesquisa, sem número de processo, edital ou identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP).
- Para referência do coordenador, o texto relata 42 empates e 67 eleições decididas por um voto no período (pp. 4 e 21), e as regressões de comparecimento usam 20.937 observações (Tabelas 5 e 6, pp. 23-24).
