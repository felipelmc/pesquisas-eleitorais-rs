---
citekey: Araujo2021
ficha_id: Araujo2021
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Araujo2021.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_107
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — evidência: "Casting ballots when knowing results" (p. 1)
- **tipo_documento** — resposta: artigo — evidência: "In the current article, we exploit an unique source" (p. 3)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, eleitores de uma eleição presidencial real (Brasil, 2018), analisados em unidades eleitorais agregadas (urnas/seções eleitorais) — evidência: "In Brazil, citizens between the ages of 18 and 70" (p. 18); "323 voters are registered to cast ballots in each voting machine" (p. 18)
- **c2_intervencao_estudada** — resposta: parcial, a exposição analisada é a divulgação oficial de resultados parciais da própria eleição (totalização a partir das 19:00 BRT), com variação natural identificada por falhas técnicas da biometria, e não resultado de pesquisa eleitoral, agregador, boca de urna ou projeção baseada em pesquisas — evidência: "for voting machines that closed after the results started being released" (p. 20); "our results emerge from a situation of exposure to vote tallies" (p. 32)
- **c3_desfecho** — resposta: Sim, desfecho de voto: parcela de votos por candidato (primeiro, segundo e terceiro colocados) e de votos brancos e nulos por urna; comparecimento entra apenas como controle — evidência: "We estimate Ordinary Least Squares (OLS) models for each outcome variable" (p. 20); "support for the announced frontrunner is 5.69 pp higher in treated units" (p. 23)
- **c4_desenho_elegivel** — resposta: Sim, experimento natural com variação identificada da exposição (atrasos imprevistos por falhas técnicas da biometria definem urnas tratadas e de controle), estimado por MQO com testes de placebo — evidência: "the 2018 Brazilian election provides an unique natural experimental setting" (p. 8); "we identify our treatment and control units" (p. 19)
- **c5_estudo_primario** — resposta: Sim, estudo primário com análise própria de dados oficiais de urna do TSE — evidência: "Using timestamp data of the last vote cast in each voting machine" (p. 3)
- **c6_nao_retratado** — resposta: Sim, não há aviso ou marca de retratação no documento — evidência: "Casting ballots when knowing results" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Dados oficiais de urna (TSE) dos dois turnos da eleição presidencial brasileira de 2018, cobrindo as 454.490 urnas do país, com 8.548 urnas tratadas (1,6%) no primeiro turno e 1.084 (0,24%) no segundo — evidência: "data are available for each round of the election for all 454,490" (p. 18); "a total of 8,548 (1.6%) observations are in our treatment group" (p. 19)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
Paginação e offset: a numeração impressa do corpo do artigo coincide com o índice do PDF (offset 0), confirmado em páginas distantes: a p. 2 do PDF traz "2" no rodapé, a p. 13 traz "13", a p. 20 traz "20", a p. 25 traz "25" e a p. 37 traz "37". O documento tem, porém, DUAS sequências de numeração: o artigo (PDF 1-37, impressas 1-37) e o "Online Appendix", que reinicia a contagem (PDF 38 = impressa 1; offset 37 nessa parte). Para manter offset único, todas as evidências foram extraídas do corpo do artigo (pp. 1-37). A p. 1 é a folha de rosto, sem número impresso, citada como p. 1 pela posição na sequência.

texto_confere: título e primeiro autor do documento ("Casting ballots when knowing results"; Victor Araújo, com Malu A. C. Gatto) batem com os metadados do registro; ano 2021 compatível. Respondi Sim.

tipo_documento: o documento não traz folha de rosto de periódico, nota de publicação ou marca de preprint; a única autodeclaração é "In the current article" (p. 3), por isso classifiquei como artigo. Registro que o DOI informado pelo coordenador (10.33774/apsa-2021-5d090-v2) é de servidor de preprints e que a nota de agradecimento menciona "three anonymous reviewers and editor Robert Johns" (p. 1), o que sugere manuscrito submetido; como metadados do coordenador só valem para texto_confere, não usei essa pista para responder esta variável.

c2 (decisão limítrofe, sinalizada para arbitragem do coordenador): a exposição analisada NÃO é resultado de pesquisa eleitoral. É a divulgação oficial da apuração parcial da própria eleição, iniciada às 19:00 BRT, à qual ficaram expostos eleitores que ainda votavam por causa de atrasos causados pela biometria. Os próprios autores marcam a diferença: "our results emerge from a situation of exposure to vote tallies, not pre-electoral polls" (p. 32). Por outro lado, funcionalmente o caso é o da informação de resultado eleitoral difundida antes do encerramento efetivo da votação, família à qual o protocolo associa boca de urna e projeção divulgada antes do fechamento das urnas, e a variação é natural e identificada (falhas técnicas imprevisíveis), não sendo resultado de eleição passada nem mercado de apostas. Como o protocolo não decide o caso, respondi parcial.

c3: comparecimento (turnout) aparece apenas como controle nos modelos ("we also control for turnout rates", p. 21), não como desfecho; brancos e nulos são desfechos usados como indício de (des)mobilização. Por isso o desfecho registrado é de voto.

outros_relatos_mesmo_estudo: não há menção, no documento, a versão anterior, working paper, tese ou relatório com os mesmos dados. A nota de rodapé de agradecimentos cita seminários (King's College London, London School of Economics), que são apresentações, não relatos do estudo; por isso 999, e não uma referência inventada.

registro_financiamento: não há número de processo, edital ou identificador de pré-registro (OSF, AEA, RIDIE, EGAP) no documento. A nota de agradecimento menciona a Universidade de Zurique, mas sem qualquer identificador de projeto financiado; por isso 999.

Divergência numérica no próprio texto, registrada sem correção: o resumo dos resultados na p. 4 diz "1,024 (0.24%) of machines" no segundo turno, enquanto a seção de dados na p. 19 diz "In the second round, 1,084 (0.24%) of voting machines were treated." Usei o número da seção de dados (1.084) em fonte_dados_amostra.

Leitura: documento de 66 páginas lido por inteiro em faixas (PDF 1-20, 21-40, 41-60, 61-66), incluindo o Online Appendix (apêndices A-N).
