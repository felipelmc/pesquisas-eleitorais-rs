---
citekey: Morton2013a
ficha_id: Morton2013a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Morton2013a.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_116
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim. O título na folha de rosto ("Exit Polls, Turnout, and Bandwagon Voting: Evidence from a Natural Experiment"), os quatro autores (Rebecca B. Morton, Daniel Müller, Lionel Page, Benno Torgler) e a data (February 5, 2013) batem com os metadados do registro. — evidência: "Exit Polls, Turnout, and Bandwagon Voting:" (p. 1)
- **tipo_documento** — resposta: working_paper. O documento traz apenas título, autores, data e nota de rodapé com afiliações e agradecimentos, sem nota de publicação, periódico, volume ou DOI, e refere-se a si mesmo como "paper". — evidência: "In this paper, we make use of a unique natural experiment" (p. 5)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, eleitores em eleições presidenciais reais na França, analisados em unidades eleitorais agregadas (departamentos e subdivisões de ultramar). — evidência: "Voters in overseas territories west of mainland France" (p. 13); "Our primary data set comprises French presidential election results" (p. 16)
- **c2_intervencao_estudada** — resposta: Sim, a exposição analisada é a informação de boca de urna divulgada antes do fechamento das urnas, com variação natural identificada pela reforma eleitoral francesa de 2005 (que mudou a ordem de votação dos territórios a oeste da metrópole). — evidência: "the causal effect of exit poll information on turnout" (p. 5); "This reform creates an exogenous variation in information" (p. 5)
- **c3_desfecho** — resposta: Sim, o desfecho é de comparecimento e de voto (ambos): turnout como variável dependente nas estimativas de diferenças em diferenças e a diferença de votos entre o candidato líder e o segundo colocado (voto de bandwagon) na segunda parte. — evidência: "decreases voter turnout by about 12 percentage points" (p. 1); "the candidate ahead in mainland France was more likely to win" (p. 32)
- **c4_desenho_elegivel** — resposta: Sim, experimento natural / quase-experimento com variação identificada da exposição (reforma de 2005), estimado por diferenças em diferenças com tendências temporais específicas por território e checagens de robustez com eleições parlamentares. — evidência: "To assess the impact of knowing the election outcome on voter turnout" (p. 17); "We take advantage of a unique natural experiment from 2005" (p. 34)
- **c5_estudo_primario** — resposta: Sim, estudo primário com análise própria de dados oficiais de comparecimento e resultados eleitorais franceses. — evidência: "Our primary data set comprises French presidential election results" (p. 16)
- **c6_nao_retratado** — resposta: Sim, não há marca "RETRACTED", nota nem página de retratação em nenhuma das 38 páginas do documento. — evidência: "Exit Polls, Turnout, and Bandwagon Voting:" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Dados agregados oficiais de comparecimento e resultados das eleições presidenciais francesas, por departamento/subdivisão (105 subdivisões: 96 departamentos da metrópole mais as de ultramar), nos dois turnos de seis eleições, de 1981 a 2012; para robustez, eleições parlamentares francesas de 1997 a 2012. — evidência: "election rounds from 1981 onwards" (p. 16); "105 such subdivisions in France" (p. 17)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset de página: a numeração impressa no rodapé coincide com o índice do PDF (1-based) nas duas pontas verificadas — a p. 1 do PDF traz "1" no rodapé e a última página do PDF (38ª) traz "38"; conferi também páginas intermediárias distantes entre si (p. 16 do PDF traz "16" e p. 32 traz "32"). Logo, `offset_pagina: 0` e `paginacao: impressa`.
- `tipo_documento`: o documento não declara nenhuma nota de publicação (não há periódico, série numerada, volume, páginas nem DOI); traz só título, autores, data "February 5, 2013", resumo e nota de rodapé com afiliações e agradecimentos a um congresso. Classifiquei como `working_paper` por essa ausência de nota de publicação somada à autodescrição como "paper"; a alternativa `preprint` foi descartada porque o documento não declara repositório de preprints. Pela mesma razão, `texto_confere` foi respondido como "Sim" (e não "parcial"): o registro do coordenador é de 2013 e sem DOI, ou seja, aponta para esta mesma versão.
- `c3_desfecho`: o texto tem dois desfechos elegíveis. O comparecimento é a variável dependente das Tabelas 3 a 7; o voto entra na Seção 6, em que a variável dependente é a diferença normalizada de votos entre o candidato mais votado e o segundo colocado nos territórios tratados (Tabela 8), o que permite comparar o apoio a quem a estimativa de boca de urna mostrava à frente. Por isso a resposta registra "ambos".
- `c4_desenho_elegivel`: a variação da exposição vem da reforma de 2005, que passou os territórios a oeste da metrópole a votar no sábado, antes da metrópole; antes disso esses eleitores votavam já sabendo o resultado divulgado às 20h na França continental. É variação natural identificada, não tendência agregada de pesquisas, e por isso "Sim" sem ressalva.
- `outros_relatos_mesmo_estudo` = 999: percorri folha de rosto, nota de rodapé de autoria, introdução, seções de dados e método, conclusão e lista de referências e não há menção a versão anterior, tese, relatório técnico ou outro relato com os mesmos dados. Os trabalhos de Morton e Williams (1999, 2001) e Battaglini, Morton e Palfrey (2007) citados no texto são estudos distintos, de laboratório, não relatos deste mesmo estudo.
- `registro_financiamento` = 999: a nota de rodapé da primeira página traz apenas agradecimentos nominais e menção ao 5th Australasian Public Choice Conference, sem número de processo, edital ou identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP).
- Na escolha das evidências evitei, quando havia alternativa, trechos com "difference", "coefficient", "first" e "Affairs", por causa das ligaduras tipográficas (ff, fi, ffi) na camada de texto deste PDF.
