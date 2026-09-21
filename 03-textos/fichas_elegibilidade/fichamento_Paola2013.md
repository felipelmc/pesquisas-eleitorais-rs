---
citekey: Paola2013
ficha_id: Paola2013
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Paola2013.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_123
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — mesmos autores, mesmo estudo e mesmos dados do registro, mas em versão de working paper da Università della Calabria, com "Dual Ballot System" no título em vez de "double ballot system" — evidência: "Exploiting the Italian Dual Ballot System" (p. 1)
- **tipo_documento** — resposta: working_paper — evidência: "Working Paper n. 03" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, analisa unidades eleitorais agregadas (municípios italianos em eleições municipais reais de prefeito, com primeiro e segundo turnos) — evidência: "about 1,400 electoral competitions at the municipal level" (p. 2)
- **c2_intervencao_estudada** — resposta: Não, a exposição analisada é a margem eleitoral do primeiro turno (resultado de eleição efetiva usado como proxy da disputa esperada no segundo turno), não resultado de pesquisa eleitoral; pesquisas de opinião só aparecem na discussão da literatura como medida alternativa usada por outros autores — evidência: "Electoral Margin represents an inverse measure of expected electoral closeness" (p. 6); "between the number of votes obtained by the two leading candidates" (p. 6)
- **c3_desfecho** — resposta: Sim, o desfecho é de comparecimento: a variável dependente é a razão entre votos válidos do segundo turno e eleitores aptos, com análises adicionais de votos brancos e nulos — evidência: "the ratio between the number of valid ballots at the second round" (p. 6)
- **c4_desenho_elegivel** — resposta: parcial, é painel agregado observacional de municípios estimado por MQO com efeitos fixos municipais, correção de seleção de Heckman e logit fracionário, apresentado pelos autores como exploração de um traço institucional (sistema de dois turnos) para medir a disputa esperada ex ante, mas sem choque exógeno identificado na exposição nem desenho de descontinuidade, diferenças em diferenças ou série interrompida — evidência: "we estimate an OLS model to analyze whether electoral closeness" (p. 8); "we use the two-step Heckman selection model" (p. 11)
- **c5_estudo_primario** — resposta: Sim, é estudo primário com análise própria de um painel de eleições municipais montado a partir de dados do Ministério do Interior italiano e dos Censos — evidência: "We base our analysis on a panel dataset" (p. 6)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação no documento — evidência: "The Causal Impact of Closeness on Electoral Participation" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: painel agregado de 1.410 eleições municipais italianas realizadas entre 1993 e 2011 em 632 municípios com mais de 15.000 habitantes, com dados do Ministério do Interior italiano e dos Censos de População — evidência: "Using data from Italian municipal elections from 1993 to 2011" (p. 1); "1,410 municipal elections held over the period" (p. 6); "in 632 municipalities with more than 15,000 inhabitants" (p. 6)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset de página: a numeração impressa começa na primeira página do texto (título e resumo), que é a página 2 do PDF; a página 1 do PDF é a folha de rosto da série de working papers e não traz número impresso. Confirmei em duas páginas distantes: o rodapé "1" aparece na página 2 do PDF e o rodapé "17" na página 18 do PDF, de modo que impressa P → PDF = P + 1. Para a folha de rosto, única fonte da declaração de tipo de documento (`tipo_documento`), registrei `p. 0`, que preserva a mesma fórmula (0 + 1 = página 1 do PDF).
- `texto_confere` = parcial pela regra do codebook para outra versão do mesmo trabalho: o documento é o Working Paper n. 03-2012 do Dipartimento di Economia e Statistica da Università della Calabria, datado "This version: 23 February 2012" (p. 1), com os mesmos autores (Maria De Paola e Vincenzo Scoppa) e o mesmo estudo do registro de 2013.
- `c2` = Não é a decisão central da ficha. O tratamento é a variável Electoral Margin, construída com a diferença absoluta de votos entre os dois candidatos mais votados no primeiro turno, dividida pelos eleitores aptos: é resultado de eleição efetiva, não pesquisa pré-eleitoral, agregador, projeção ou boca de urna. Pesquisas de opinião aparecem no documento apenas na revisão da literatura, como medida alternativa de competição usada por outros trabalhos e descartada pelos autores ("opinion polls may not reflect the effective electoral choices", p. 4), sem entrar no desenho empírico.
- `c4` = parcial por decisão limítrofe: o título e o texto reivindicam identificação causal ao explorar o sistema de dois turnos, e a exposição é medida antes do desfecho (margem do primeiro turno → comparecimento do segundo turno, duas semanas depois), o que se aproxima da lógica de painel com exposição anterior ao desfecho; por outro lado, a unidade é agregada (município), não individual, e a variação da margem não vem de proibição, embargo, fuso horário, calendário de divulgação, descontinuidade, diferenças em diferenças ou série interrompida, mas de variação natural entre eleições, tratada com efeitos fixos e correção de seleção. Não sendo possível encaixá-lo com segurança nem entre os desenhos aceitos nem entre os recusados, preferi `parcial`.
- `outros_relatos_mesmo_estudo` = 999: o documento traz "This version: 23 February 2012" (p. 1) e agradece comentários recebidos no 1st Workshop on Economics and Politics (Bologna, outubro de 2011), mas não menciona nem referencia nenhum outro relato do mesmo estudo (versão anterior, tese, relatório ou artigo com os mesmos dados). Deduzir a existência de outra versão a partir de "This version" seria inferência, vedada pelas regras.
- `registro_financiamento` = 999: a nota de rodapé de agradecimentos (p. 1) cita o Ministero dell'Interno pela cessão de dados e nomes de colegas, sem número de processo, edital ou identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP).
- Documento de 18 páginas, lido por inteiro (páginas 1 a 18 do PDF, isto é, folha de rosto e páginas impressas 1 a 17).
