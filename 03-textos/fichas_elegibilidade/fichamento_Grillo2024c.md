---
citekey: Grillo2024c
ficha_id: Grillo2024c
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Grillo2024c.pdf
paginacao: impressa
offset_pagina: 2
agente_fichador: elegib-opus5-031
data_fichamento: 2026-09-19
---

## Identificacao
- **texto_confere** — resposta: parcial; título e autores (Alberto Grillo e Eva Raiber) batem com o registro, mas o PDF é o working paper da AMSE (WP 2022-Nr 07) datado de 15 de março de 2022, outra versão do trabalho registrado como de 2024 (DOI 10.3917/reco.pr2.0188) — evidência: "Exit polls and voter turnout in the 2017 French elections" (p. 0); "March 15, 2022" (p. 0)
- **tipo_documento** — resposta: working_paper; a capa (sem número impresso, página 1 do PDF) traz 'Working Papers / Documents de travail' da Aix-Marseille School of Economics, 'WP 2022- Nr 07'; a folha de rosto é datada de 15/03/2022 e o apêndice é marcado como não destinado à publicação — evidência: "Online Appendix (not intended for publication)" (p. 15); "March 15, 2022" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim; unidades eleitorais agregadas (departamentos da França metropolitana) em eleição real, as presidenciais francesas de 2017, com 2012 e 2007 como comparação — evidência: "voter at the department level in 2017, 2012 and 2007" (p. 4)
- **c2_intervencao_estudada** — resposta: Sim; a exposição é a divulgação de pesquisas de boca de urna por mídia estrangeira (belga e suíça) antes do fechamento das urnas no 2º turno de 2017, com variação natural dada pela proibição francesa de divulgação e pelo horário da divulgação — evidência: "by exploiting the early release of exit polls by foreign media" (p. 1); "it is forbidden to publish exit polls before polling stations close" (p. 1)
- **c3_desfecho** — resposta: Sim; desfecho de comparecimento (turnout agregado por departamento às 12:00, 17:00 e no fechamento); não há desfecho de voto como variável dependente, o efeito sobre a margem de vitória é inferido pela heterogeneidade do comparecimento conforme o voto no 1º turno — evidência: "turnout is measured at 12:00, 17:00 and when polling stations closed" (p. 4)
- **c4_desenho_elegivel** — resposta: Sim; quase-experimento em diferenças em diferenças (antes e depois da divulgação, 2º turno contra 1º turno) e triplas diferenças com as eleições de 2012 e 2007, explorando o embargo e o horário da divulgação — evidência: "we use turnout rates at 12:00 as the pre-period" (p. 4); "we compare the results in 2017 to those in 2012 and 2007" (p. 6)
- **c5_estudo_primario** — resposta: Sim; estudo primário com análise própria de dados eleitorais oficiais por departamento — evidência: "Our dataset contains turnout rates, election results for each candidate" (p. 4)
- **c6_nao_retratado** — resposta: Sim; não há marca RETRACTED, nota ou página de retratação no documento — evidência: "Exit polls and voter turnout in the 2017 French elections" (p. 0)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Dados agregados do Ministério do Interior francês para os 96 departamentos da França metropolitana (comparecimento às 12:00, às 17:00 e no fechamento nos dois turnos das presidenciais de 2017, com 2012 e 2007 como comparação, resultados por candidato e eleitores registrados), mais chuva e temperatura máxima na capital do departamento; 576 observações na especificação base (Tabela 1, p. 11) e 1152 nas comparações com 2012 e 2007 (Tabela 2, p. 12) — evidência: "obtained from the French interior ministry" (p. 4); "all French mainland departments" (p. 11)
- **registro_financiamento** — resposta: ANR-17-EURE-0020 (French National Research Agency) e Excellence Initiative A*MIDEX da Aix-Marseille University; nenhum pré-registro citado — evidência: "French National Research Agency Grants ANR-17-EURE-0020" (p. 0)

## Notas do codificador
- Paginação e offset: a página 1 do PDF é a capa da série de working papers da AMSE e a página 2 é a folha de rosto com título, autores, data e resumo; nenhuma das duas tem número impresso. A numeração impressa começa em 1 na página 3 do PDF (Introdução). Conferido em três pontos: impressa 1 = PDF 3, impressa 11 = PDF 13 (Tabela 1), impressa 18 = PDF 20 (última página). Logo offset_pagina = 2. Pela fórmula (PDF = P + 2), a folha de rosto corresponde a p. 0 e a capa a p. -1; as citações da folha de rosto usam p. 0 e nenhuma citação usa a capa.
- texto_confere = parcial: o título e os autores coincidem com o registro, mas o documento é o working paper AMSE WP 2022-Nr 07, de 15/03/2022, enquanto o registro é de 2024 com DOI de periódico (Cairn). O documento não menciona a versão publicada.
- tipo_documento: a declaração 'Working Papers / Documents de travail' e 'WP 2022- Nr 07' está só na capa, sem número impresso; para não citar p. -1, a evidência usa a data da folha de rosto e o título do apêndice online ('not intended for publication'), que confirmam tratar-se de manuscrito não publicado.
- c2 e c4: a exposição (boca de urna divulgada por RTBF e outras mídias estrangeiras a partir de cerca de 16:00, com urnas abertas até 19:00 ou 20:00) é comum a todo o país no 2º turno; a identificação vem da comparação com o 1º turno (diferenças em diferenças) e com 2012 e 2007 (triplas diferenças). Os autores ressalvam que tendências semelhantes ocorreram em eleições anteriores, mas as triplas diferenças são significativas em parte das especificações. Há também heterogeneidade por proximidade da Bélgica e da Suíça (Tabela 3). O protocolo aceita diferenças em diferenças com variação por embargo ou calendário de divulgação, daí 'Sim'.
- c3: a variável dependente em todas as tabelas é o comparecimento; os votos por candidato no 1º turno entram só como moderadores (Tabela 4). O efeito 'underdog' sobre a margem de Macron é inferido, não estimado sobre o voto.
- fonte_dados_amostra: os números 96 departamentos, 576 e 1152 observações foram copiados das linhas Departments e Observations das Tabelas 1 e 2; como evidência usei trechos de texto corrido e da nota da Tabela 1, para não depender da ordem de extração das células.
- outros_relatos_mesmo_estudo = 999: o documento não menciona versão anterior, posterior ou outro relato com os mesmos dados. Morton et al. (2015) é outro estudo, sobre os territórios ultramarinos franceses.
- Evidências escolhidas sem palavras com ligaduras (effect, first, significant, difference, specification evitadas).
