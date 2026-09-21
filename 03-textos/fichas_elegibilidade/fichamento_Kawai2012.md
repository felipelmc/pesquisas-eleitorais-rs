---
citekey: Kawai2012
ficha_id: Kawai2012
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Kawai2012.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_173
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial; o título e os dois autores batem com o registro, mas o próprio documento é um manuscrito datado de maio de 2009, enquanto o registro traz ano 2012 (depósito no SSRN): trata-se da versão de working paper do mesmo trabalho — evidência: "Inferring Strategic Voting" (p. 1); "May 2009" (p. 1)
- **tipo_documento** — resposta: working_paper; a folha de rosto traz apenas título, autores, afiliação universitária e data, sem periódico, volume ou nota de publicação — evidência: "May 2009" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim; analisa eleitores japoneses que escolhem entre candidatos em eleição real, com unidades eleitorais agregadas (municípios dentro de distritos) como observação — evidência: "We use data from the Japanese House of Representatives election" (p. 12)
- **c2_intervencao_estudada** — resposta: Não; a exposição analisada é a estrutura de preferências e crenças num modelo de voto estratégico estimado a partir de votos agregados, não um resultado de pesquisa eleitoral; pesquisas aparecem só como menção de contexto sobre de onde vêm as crenças dos eleitores — evidência: "we study how to identify and estimate a model of strategic voting" (p. 2); "information regarding the expected outcome of the election is widely available" (p. 8)
- **c3_desfecho** — resposta: Sim; o desfecho é de voto: a votação agregada (vote share) de cada candidato e partido por município, sem qualquer medida de comparecimento — evidência: "We use municipality-level aggregate data for our estimation" (p. 23); "descriptive statistics of electoral district vote shares in Table 2" (p. 13)
- **c4_desenho_elegivel** — resposta: Não; é estimação estrutural em dados observacionais agregados de uma única eleição, com identificação vinda da multiplicidade de equilíbrios e de desigualdades de momentos, sem aleatorização, sem variação exógena identificada de exposição a pesquisa e sem painel individual — evidência: "We estimate the model using inequality-based estimator developed by Pakes" (p. 22)
- **c5_estudo_primario** — resposta: Sim; estudo primário, com dados próprios coletados e estimação própria do modelo — evidência: "The data on the vote share and candidate characteristics were collected by" (p. 13)
- **c6_nao_retratado** — resposta: Sim; não há marca, nota ou página de retratação em nenhuma das 42 páginas — evidência: "Inferring Strategic Voting" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Dados agregados por município da eleição da Câmara dos Representantes do Japão de 2005, com votos e características dos candidatos do CD-ROM do Yomiuri Shimbun e demografia do Statistics Bureau, na amostra de 175 distritos eleitorais que satisfazem os três critérios de seleção — evidência: "data from the Japanese House of Representatives election held on September" (p. 12); "Yomiuri Shimbun (2005) Shugiin-Senkyo 2005 CD-ROM" (p. 35); "We are left with 175 electoral districts that satisfy the three criteria" (p. 13)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador

Paginação e offset. A numeração impressa coincide com a folha do PDF em todo o documento: a folha 1 traz "1", a folha 12 traz "12", a folha 22 traz "22", a folha 35 traz "35" e a folha 42 traz "42". Logo `folha_do_PDF = pagina_anotada + 0` e `offset_pagina: 0`. Todas as páginas citadas (1, 2, 8, 12, 13, 22, 23, 35) foram abertas diretamente e o número impresso foi conferido no rodapé de cada uma.

texto_confere. Título e autores batem literalmente com o registro ("Inferring Strategic Voting"; Kei Kawai e Yasutora Watanabe, ambos da Northwestern University, p. 1). A única divergência é o ano: o documento se declara de maio de 2009, e o registro traz 2012 (ano do depósito no SSRN, DOI 10.2139/ssrn.2188562). Registrei `parcial` por ser uma versão do mesmo trabalho, e não uma correspondência exata de metadados. Não consultei o outro arquivo mencionado pelo coordenador: a ficha se apoia apenas neste PDF.

tipo_documento. O documento não traz nota de publicação, periódico, volume nem indicação de anais. A folha de rosto tem só título, autores com afiliação universitária, data e abstract, e o rodapé de agradecimentos é o de um manuscrito em circulação; por isso `working_paper`. A evidência possível é a linha de data, que é o que ocupa o lugar da nota de publicação, já que não há nenhuma declaração explícita do tipo.

c2. As pesquisas eleitorais aparecem uma única vez no corpo do texto, na justificativa da hipótese de crenças comuns (p. 8), como exemplo de informação disponível publicamente, e nunca como tratamento, exposição medida ou variável do modelo. O objeto empírico é a fração de eleitores estratégicos e o voto desalinhado, recuperados de dados agregados de votação. Daí `Não`.

c3. Respondi `Sim` porque o desfecho analisado é votação agregada de candidato e partido, que é a alternativa (a) do critério. Registro, porém, que a comparação entre o apoio ao candidato à frente e ao candidato atrás nas pesquisas não é feita no documento, simplesmente porque não há exposição a pesquisa nenhuma (ver c2). O texto afirma explicitamente que comparecimento ficou de fora do artigo, então não há desfecho de mobilização.

c4. O desenho é observacional agregado, de corte transversal de uma eleição, com identificação parcial obtida da multiplicidade de equilíbrios e de restrições de desigualdade. Não há aleatorização, embargo, fuso horário, calendário de divulgação nem painel individual: nenhuma das variações identificadas aceitas no protocolo.

999. `outros_relatos_mesmo_estudo`: o documento não menciona versão anterior, tese, relatório ou artigo irmão; o "Supplementary Material" citado é a própria seção 7.4 deste PDF, não outro relato. `registro_financiamento`: o rodapé de agradecimentos (p. 1) traz apenas nomes de colegas, sem número de processo, edital ou identificador de pré-registro, e não há seção de financiamento em nenhuma página.
