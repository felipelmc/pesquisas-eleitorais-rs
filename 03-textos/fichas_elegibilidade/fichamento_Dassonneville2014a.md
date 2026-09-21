---
citekey: Dassonneville2014a
ficha_id: Dassonneville2014a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Dassonneville2014a.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_132
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — o título e a primeira autora do documento batem com os metadados do registro (Dassonneville, 2014); o documento é o paper de congresso com o mesmo título e subtítulo do registro — evidência: "How Partisanship is Strengthened in Election Times:" (p. 0)
- **tipo_documento** — resposta: evento — paper apresentado em congresso (13th Belgian Dutch Political Science Conference, Maastricht, 12-13 June 2014) — evidência: "Paper presented at the" (p. 0); "13th Belgian Dutch Political Science Conference" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitorado alemão adulto (respondentes do painel SOEP residentes nos estados da antiga Alemanha Ocidental) em contexto de eleições federais reais — evidência: "we focus on respondents living in former West German" (p. 7)
- **c2_intervencao_estudada** — resposta: Não — a exposição analisada é o período eleitoral (janela de 60 dias antes e depois da eleição) e a sofisticação política; resultado de pesquisa eleitoral não entra como tratamento nem como exposição medida — evidência: "The main independent variables in our analyses are election periods" (p. 9)
- **c3_desfecho** — resposta: Não — o desfecho é a identificação partidária (ter e força do vínculo com um partido), sem medida de intenção de voto, escolha de voto, votação agregada nem comparecimento — evidência: "The dependent variable party identification" (p. 8)
- **c4_desenho_elegivel** — resposta: parcial — painel individual longitudinal com comparação entre níveis de exposição (tempo eleitoral vs. não eleitoral) estimado por logit ordinal de efeitos mistos, mas observacional, com a exposição medida na mesma onda do desfecho e sem variação identificada da exposição prevista no protocolo — evidência: "Taking into account the longitudinal data structure we applied a mixed" (p. 12); "Due to panel attrition and refreshments the panel is unbalanced" (p. 8)
- **c5_estudo_primario** — resposta: Sim — estudo primário com análise própria dos dados do painel SOEP v29 — evidência: "Therefore, we made use of the German Socio-Economic Panel" (p. 7)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento; a primeira página traz apenas título, autoras, filiação e o congresso — evidência: "A Longitudinal Analysis using the German Socio-Economic Panel, 1984-2012" (p. 0)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Painel domiciliar German Socio-Economic Panel (SOEP v29), respondentes dos estados da antiga Alemanha Ocidental, 29 anos (1984-2012) com sete eleições federais, N=25,111 respondentes e N=210,702 observações — evidência: "Therefore, we made use of the German Socio-Economic Panel" (p. 7); "in Germany over 29 years (1984-2012)" (p. 7); "with a sample of N=25,111 respondents and N=210,702 observations" (p. 8)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação e offset: a folha de rosto do PDF (folha 1) não tem número impresso e foi anotada como p. 0, de modo que `folha_do_PDF = pagina_anotada + offset_pagina` (0 + 1 = 1). O offset foi conferido em duas páginas distantes: a folha 2 do PDF traz "1" impresso no rodapé (início da Introdução) e a folha 29 traz "28" (Table 5, no apêndice), ambas compatíveis com offset 1.
- c1: respondi Sim porque a amostra é o eleitorado alemão adulto acompanhado ao longo de sete eleições federais reais, contexto eleitoral real e não escolha de consumo, mercado ou órgão deliberativo. O fato de o desfecho não ser voto é tratado em c3, não em c1.
- c4: caso limítrofe. O desenho é um painel individual com comparação explícita entre níveis de exposição (períodos eleitorais vs. não eleitorais), o que se aproxima da terceira categoria aceita pelo protocolo; por outro lado, a exposição (ser entrevistado dentro da janela de 60 dias em torno da eleição) é medida na mesma onda do desfecho, não antes dele, e não há variação identificada da exposição do protocolo (resultado de pesquisa eleitoral). Por isso `parcial`, e não Sim nem Não.
- `outros_relatos_mesmo_estudo` = 999: o documento não menciona versão anterior, tese, working paper ou relatório que o origine. Há referência a Dassonneville (2014) sobre troca de intenção de voto e a Dassonneville et al. (2012), mas são trabalhos distintos citados na literatura, não outros relatos deste estudo; não deduzi ligação a partir do nome da autora.
- `registro_financiamento` = 999: não há identificador de pré-registro (OSF, AEA, RIDIE, EGAP) nem número de processo ou edital em nenhuma página, incluindo as notas de rodapé e a seção "References and Notes".
- Evidências escolhidas preferindo trechos sem ligaduras tipográficas e interrompidas antes de marcadores de nota de rodapé sobrescritos (ex.: na p. 7, o trecho para antes de "states1"; na p. 8, antes de "identification2").
- A citação da p. 8 reproduz o texto impresso tal como está, inclusive o aparente erro de digitação "as" no lugar de "us" na frase de origem.
