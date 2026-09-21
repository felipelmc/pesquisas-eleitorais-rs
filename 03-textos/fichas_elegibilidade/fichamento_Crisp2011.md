---
citekey: Crisp2011
ficha_id: Crisp2011
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Crisp2011.pdf
paginacao: impressa
offset_pagina: -142
agente_fichador: fichador_el_175
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim, o título e o primeiro autor do documento batem com o registro (título "Electoral contexts that impede voter coordination"; Brian F. Crisp, Santiago Olivella, Joshua D. Potter); o DOI impresso é doi:10.1016/j.electstud.2011.09.006 e o artigo saiu no fascículo Electoral Studies 31 (2012) 143–158, aceito em 29 de setembro de 2011 — evidência: "Electoral contexts that impede voter coordination" (p. 143)
- **tipo_documento** — resposta: artigo — evidência: "Contents lists available at SciVerse ScienceDirect" (p. 143)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, o estudo analisa unidades eleitorais agregadas (distritos) de eleições reais de câmara baixa em 21 países, com a distribuição dos votos dos eleitores entre partidos viáveis e inviáveis — evidência: "coordination failure in 2007 districts in 183 lower chamber elections" (p. 144)
- **c2_intervencao_estudada** — resposta: Não, a exposição analisada são características do contexto eleitoral (experiência com as regras eleitorais, entrada de novos partidos, volatilidade passada e magnitude distrital), e não resultado de pesquisa eleitoral; a disponibilidade de pesquisas é citada apenas como fator não incorporado aos testes empíricos — evidência: "We focus on four aspects of the electoral context" (p. 146)
- **c3_desfecho** — resposta: Sim, desfecho de voto: votação agregada por distrito, medida como parcela de votos dados a partidos perdedores ("hopeless votes"), razão SF e "coordination product"; não há medida de comparecimento — evidência: "percentage of votes cast that went to the second largest losing party" (p. 149)
- **c4_desenho_elegivel** — resposta: Não, é estudo observacional agregado (modelos multiníveis com efeitos aninhados de país e distrito sobre dados distritais de retornos eleitorais), sem aleatorização, experimento natural ou painel individual com variação identificada de exposição a pesquisas eleitorais — evidência: "we will use multilevel models with random nested" (p. 151)
- **c5_estudo_primario** — resposta: Sim, é estudo primário com análise própria de dados distritais extraídos do CLE Dataset e do CLEA — evidência: "we have obtained a total of 10,764 observations" (p. 147)
- **c6_nao_retratado** — resposta: Sim, não há marca, nota ou página de retratação em nenhuma das 16 folhas do PDF — evidência: "Electoral contexts that impede voter coordination" (p. 143)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: O documento menciona uma versão anterior do projeto, apresentada no Summer Speakers Series do Departamento de Ciência Política da University of Illinois, mas sem referência bibliográfica a esse relato anterior — evidência: "An earlier version of this project received constructive criticism" (p. 143)
- **fonte_dados_amostra** — resposta: Dados agregados de retornos eleitorais distritais do Constituency Level Election (CLE) Dataset (Brancati, 2007) e do Constituency Level Elections Archive (CLEA) (Kollman et al., 2010), com 10.764 observações de distritos-eleição, 2007 distritos e 21 países em 183 eleições de câmara baixa, cujos anos por país estão listados na Tabela 1 (p. 145) — evidência: "From the Constituency Level Election (CLE) Dataset" (p. 147)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- **Paginação e offset.** A numeração impressa começa em 143 (o artigo ocupa Electoral Studies 31 (2012) 143–158) e a folha 1 do PDF é a página impressa 143, logo `folha_do_PDF = pagina_anotada + (-142)`. O offset foi conferido nos cabeçalhos impressos de folhas distantes: folha 2 = "144", folha 4 = "146", folha 5 = "147", folha 7 = "149", folha 9 = "151" e folha 15 = "157". Cada citação desta ficha foi relida na folha que a fórmula indica (143→1, 144→2, 146→4, 147→5, 149→7, 151→9). A folha 1 não traz o número impresso no rodapé; anotei 143 porque é o valor que satisfaz a fórmula e é o início do intervalo de páginas declarado no cabeçalho do fascículo.
- **texto_confere.** Respondi "Sim" e não "parcial" porque é a versão publicada final do mesmo trabalho: título e autoria batem com o registro. A única divergência é de metadado, não de versão — o registro traz ano 2011 (data de aceite e de copyright impressos no documento: "Accepted 29 September 2011", "© 2011 Elsevier Ltd.") enquanto o fascículo é de 2012.
- **c2.** Este é o critério que reprova o texto. A exposição do protocolo (resultado de pesquisa eleitoral divulgada) não é manipulada, nem identificada por variação natural, nem medida no indivíduo: as variáveis explicativas são experiência prévia com as regras, novos partidos como parcela da magnitude, volatilidade defasada e magnitude distrital (logada). Pesquisas eleitorais só aparecem (i) na revisão, ao descrever trabalhos que usam a percepção do eleitor sobre quem está perdendo "in the polls" (p. 145), e (ii) na nota 5 (p. 146), que lista a disponibilidade de dados de pesquisa entre os fatores explicitamente deixados fora dos testes empíricos.
- **c3.** Respondi "Sim" porque os três desfechos são votação agregada por partido no distrito, construídos justamente pela comparação entre o apoio aos partidos viáveis e o apoio aos perdedores; é desfecho de voto, sem comparecimento. A resposta "Sim" aqui não conflita com o "Não" de c2: o desfecho é elegível, a exposição não.
- **c4.** O próprio texto descreve o desenho como teste multivariado observacional de dados distritais, com efeitos aleatórios de país e distrito para lidar com a estrutura aninhada — não há proibição/embargo, fuso horário, calendário de divulgação, descontinuidade, série interrompida nem painel individual.
- **registro_financiamento = 999.** Não há identificador de pré-registro (OSF, AEA, RIDIE, EGAP) nem número de processo ou edital em nenhuma parte do documento. Há apenas o agradecimento de apoio institucional, sem número, na nota de rodapé da primeira página (Weidenbaum Center on the Economy, Government, and Public Policy, Washington University in St. Louis). Como o prompt da variável pede a transcrição de identificadores, e identificador não existe no texto, registrei 999 em vez de transcrever o agradecimento.
- **Escolha das citações.** Evitei trechos com ligaduras tipográficas (ff, fi, fl) quando havia alternativa — por isso, por exemplo, a evidência de c4 para em "random nested", sem incluir "effects", que vem logo em seguida na mesma frase.
- **Leitura.** Documento curto (16 folhas); li todas as folhas por inteiro, incluindo notas de rodapé, o apêndice com a Tabela A1 (p. 157) e as referências (p. 158).
