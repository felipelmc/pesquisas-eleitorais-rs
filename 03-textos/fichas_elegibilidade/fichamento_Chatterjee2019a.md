---
citekey: Chatterjee2019a
ficha_id: Chatterjee2019a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Chatterjee2019a.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: elegib-opus5-017
data_fichamento: 2026-09-19
---

## Identificacao
- **texto_confere** — resposta: Sim — evidência: "Voting for the Underdog or Jumping on the Bandwagon?" (p. 0)
- **tipo_documento** — resposta: working_paper — evidência: "We thank seminar participants at FLAME University for comments and feedback." (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, eleitores indianos em eleições reais, analisados em unidades eleitorais agregadas (distritos eleitorais de eleições estaduais e gerais) — evidência: "the dataset consists of 681 constituencies of four" (p. 13)
- **c2_intervencao_estudada** — resposta: Sim, a exposição é a divulgação de pesquisas de boca de urna entre as fases de eleições multifásicas, com variação natural identificada pela proibição de divulgação (Representation of the People (Amendment) Act 2009, em vigor em 2010) — evidência: "ban on exit polls by the ECI provides an excellent natural experiment" (p. 2); "but it has potential to affect multi-phase elections" (p. 17)
- **c3_desfecho** — resposta: Sim, ambos: voto (percentual de votos do vencedor, do segundo colocado e dos demais candidatos) e comparecimento (voter turnout), além de margem de vitória e decisões de candidatura — evidência: "outcomes such as vote share of winner, vote share of runner up" (p. 18); "Our final set of outcomes include voter turnout and winning margin." (p. 18)
- **c4_desenho_elegivel** — resposta: Sim, experimento natural com diferenças em diferenças: estados com eleições sempre multifásicas (tratamento) contra sempre monofásicas (controle), antes e depois da proibição — evidência: "we employ a double difference estimation framework" (p. 17)
- **c5_estudo_primario** — resposta: Sim, estudo primário com análise própria de dados administrativos da Election Commission of India — evidência: "We use administrative data from the statistical reports published by election" (p. 13)
- **c6_nao_retratado** — resposta: Sim, não há aviso de retratação no documento — evidência: "Voting for the Underdog or Jumping on the Bandwagon?" (p. 0)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Dados administrativos dos relatórios estatísticos da Election Commission of India: 5 eleições gerais (1998-2014; 1740 observações distrito-eleição nas regressões sem controles) e 2 eleições estaduais em cada um de 4 estados (Arunachal Pradesh, Bihar, Haryana, Maharashtra; 2004-2010; 681 distritos, 1352 observações) — evidência: "five general elections conducted between 1998 and 2014" (p. 13); "four states between 2004 and 2010" (p. 13); "the dataset consists of 681 constituencies of four" (p. 13); "1352" (p. 20); "1740" (p. 22)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação e offset: o PDF tem 33 páginas. A folha de rosto (PDF 1) e a primeira página da Introdução (PDF 2) trazem ambas o número impresso "1"; a partir da Introdução, impressa P = PDF P+1 (conferido em PDF 2 = p. 1, PDF 20 = p. 19, PDF 21 = p. 20 e PDF 33 = p. 32). Por isso `offset_pagina: 1`. Como a folha de rosto repete o "1", as evidências tiradas dela (título e nota de agradecimento) estão citadas como "p. 0", que pelo offset aponta para o PDF 1; citar "p. 1" levaria o verificador ao PDF 2, onde o título não aparece.
- texto_confere: o título na folha de rosto (Voting for the Underdog or Jumping on the Bandwagon? Evidence from India's Exit Poll Ban), os autores (Somdeep Chatterjee, Jai Kamal) e o ano (December 2019) batem com os metadados do registro.
- tipo_documento: o documento não se declara explicitamente como working paper; a classificação vem da ausência de cabeçalho de periódico ou nota de publicação, da data "December 2019" na folha de rosto e do agradecimento a participantes de seminário, compatível com a versão SSRN indicada no DOI do registro. Como o registro é a própria versão SSRN, texto_confere = Sim (e não "parcial").
- c2: a exposição são resultados de boca de urna divulgados ao fim de cada fase de eleições multifásicas, antes que os eleitores das fases seguintes votem (projeção divulgada antes do fechamento das urnas das fases posteriores); a proibição de 2009 e a diferença entre estados multifásicos e monofásicos dão a variação identificada. O estudo não observa diretamente o conteúdo das pesquisas divulgadas; a leitura de "underdog" é inferida do sinal dos coeficientes de diferenças em diferenças.
- c3: o desfecho de voto permite comparar o candidato à frente (vencedor, segundo colocado) com os que ficam em 3º lugar ou abaixo; o comparecimento também é analisado (Tabelas 7 e 8), então entra na célula de mobilização.
- fonte_dados_amostra: os números de observações vêm da linha "Obs" das Tabelas 3 (p. 20, eleições estaduais: 1352) e 4 (p. 22, eleições gerais: 1740 sem controles, 1737 com controles). O número de estados incluídos nas eleições gerais não é dado no texto, só no mapa da Figura 1.
- outros_relatos_mesmo_estudo = 999: o texto cita Ujhelyi, Chatterjee and Szabó (2019), "None of the above", trabalho de um dos autores sobre outro tema (candidatos que disputam eleições); não é relato do mesmo estudo. Não há menção a versão anterior, tese ou outro artigo com os mesmos dados.
- registro_financiamento = 999: a nota de agradecimento menciona apenas participantes de seminário na FLAME University; não há pré-registro nem financiamento citados.
