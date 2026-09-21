---
citekey: Dassonneville2017
ficha_id: Dassonneville2017
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Dassonneville2017.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_096
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — é o mesmo trabalho (mesmo título, mesmos autores, 2017), mas na versão de manuscrito aceito ("accepted"), sem paginação de periódico, e não na versão publicada em Acta Politica — evidência: "Electoral Volatility in Belgium (2009-2014)" (p. 1); "Acta Politica, 2017, accepted." (p. 1)
- **tipo_documento** — resposta: artigo — artigo de periódico (Acta Politica), na versão de manuscrito aceito — evidência: "Acta Politica, 2017, accepted." (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, eleitores belgas de Flandres e Valônia entrevistados em painel de amostra aleatória, que escolhem entre partidos nas eleições regionais reais de 2009 e 2014 — evidência: "among a random sample of respondents drawn from the Belgian National Register" (p. 10)
- **c2_intervencao_estudada** — resposta: Não, a exposição analisada são atributos do eleitor e dos partidos (força da identificação partidária, distância ideológica, avaliação do líder, avaliação econômica), e resultado de pesquisa eleitoral não é manipulado, nem tem variação identificada, nem é medido no indivíduo — evidência: "We test for the impact of partisanship, ideological distance," (p. 17)
- **c3_desfecho** — resposta: Sim, o desfecho é de voto: escolha de voto declarada nas eleições regionais de 2014 (e troca de partido entre 2009 e 2014); não há desfecho de comparecimento, pois o estudo exclui a mudança de e para abstenção — evidência: "we present the distribution of the reported vote choices" (p. 16); "Vote (dependent)" (p. 35)
- **c4_desenho_elegivel** — resposta: Não, painel individual analisado por regressões logísticas e logit condicional de efeitos fixos, sem exposição a pesquisa eleitoral medida antes do desfecho e sem variação identificada dessa exposição — evidência: "estimate a conditional logit model for explaining the vote choice" (p. 12)
- **c5_estudo_primario** — resposta: Sim, estudo primário com análise própria dos dados do Belgian Election Panel (2009-2014) — evidência: "we make use of the data from the Belgian" (p. 10)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação em nenhuma parte do documento — evidência: "Electoral Volatility in Belgium (2009-2014)" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim, o documento cita o relatório técnico do painel usado: Dassonneville, Falk Pedersen, Grieb e Hooghe (2014), "Belgian Election Panel 2009-2014. Technical Report", Leuven: University of Leuven; não há menção a tese, dissertação ou versão anterior deste artigo — evidência: "Technical Report. Leuven: University of Leuven." (p. 27)
- **fonte_dados_amostra** — resposta: Belgian Election Panel (2009-2014), painel representativo de cinco ondas com amostra aleatória do Registro Nacional belga em Flandres e Valônia (2.331 entrevistados na primeira onda de 2009, 1.542 questionários válidos na pré-eleitoral de 2014 e 707 entrevistados na pós-eleitoral de 2014), com 354 respondentes nos modelos logísticos de volatilidade e 1.019 e 656 observações nos logits condicionais de eleitores estáveis e voláteis — evidência: "This representative panel study consists of five waves of surveys" (p. 10); "707 respondents were interviewed by phone" (p. 10)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
Offset de página: a numeração impressa coincide com o índice do PDF. Conferido no rodapé de páginas distantes: a primeira página traz "1", a página da Tabela 1 traz "19" e a última traz "49"; logo `offset_pagina: 0` e `paginacao: impressa`. Documento de 49 páginas, lido por inteiro (não se aplica a regra de documentos com mais de 300 páginas).

`texto_confere` = parcial, e não Sim, porque título, autores e ano batem com os metadados, mas o documento é o manuscrito aceito ("Acta Politica, 2017, accepted."), sem volume, número nem paginação do periódico, isto é, outra versão do mesmo trabalho registrado pelo DOI 10.1057/s41269-016-0038-5. `tipo_documento` foi registrado como artigo porque é o que o próprio documento declara na folha de rosto (periódico Acta Politica, com nota de copyright do periódico), embora nessa versão de manuscrito aceito.

C2 = Não: o artigo usa o painel eleitoral belga apenas como fonte de dados de intenção e de escolha de voto; resultado de pesquisa eleitoral divulgada (pesquisa pré-eleitoral, agregador, projeção ou boca de urna) não aparece como tratamento, exposição natural nem variável medida no indivíduo. As exposições analisadas são identificação partidária, distância ideológica, avaliação do líder e avaliação retrospectiva da economia.

C4 = Não como consequência de C2: o desenho é um painel individual, mas não há exposição a pesquisa eleitoral medida antes do desfecho nem variação identificada dela (não há aleatorização, embargo, fuso horário, calendário de divulgação, diferenças em diferenças, descontinuidade ou série interrompida). O documento descreve o método como regressões logísticas binárias para a troca de partido e logit condicional de efeitos fixos para a escolha de voto.

C3 = Sim apenas na célula de voto: o desfecho é a escolha de partido declarada na onda pós-eleitoral de 2014 e a troca de partido entre 2009 e 2014. Comparecimento não entra, porque os autores registram que o foco na Bélgica, de voto obrigatório, impede analisar a mudança de e para a abstenção.

`registro_financiamento` = 999: o documento não traz agradecimentos, nota de financiamento, número de processo nem identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP) em nenhuma seção, incluindo a folha de rosto, as notas (p. 25) e os apêndices.

Em `outros_relatos_mesmo_estudo` foi registrado o relatório técnico do painel, que é o relato metodológico da mesma fonte de dados. O documento também cita Dassonneville (2012), sobre as eleições regionais belgas de 2009, e Dassonneville (2016), sobre o caso britânico, mas o primeiro trata de outra onda e outro objeto e o segundo usa outros dados, de modo que nenhum dos dois é apresentado como relato do mesmo estudo.
