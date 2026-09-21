---
citekey: Leontiou2023
ficha_id: Leontiou2023
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Leontiou2023.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_113
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o título e os três autores batem com os metadados do registro, mas o arquivo é a versão aceita ("peer reviewed version") depositada no Edinburgh Research Explorer, com paginação própria 1–45, e não a versão publicada no periódico (pp. 471–490). — evidência: "Bandwagons in Costly Elections: The Role of" (p. 1)
- **tipo_documento** — resposta: artigo — o próprio texto se declara "paper", e a folha de rosto do repositório registra a publicação no Journal of Economic Behavior and Organization. — evidência: "The current paper attempts to provide the missing link between theoretical studies" (p. 31)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: parcial — o objeto são eleitores que escolhem entre dois partidos (A e B) ou abstenção numa eleição majoritária, mas são agentes de um modelo formal, sem amostra empírica nem participantes de laboratório. — evidência: "citizens have to choose to vote for party A, party B" (p. 8)
- **c2_intervencao_estudada** — resposta: Não — a pesquisa eleitoral aparece apenas como motivação na introdução; a exposição analisada é a aversão à perda com pontos de referência endógenos (expectativas de equilíbrio), não a divulgação de um resultado de pesquisa. — evidência: "We introduce loss aversion with respect to the expected equilibrium payoffs" (p. 3)
- **c3_desfecho** — resposta: parcial — o desfecho analisado é de comparecimento (taxas de participação/abstenção dos apoiadores do vencedor esperado e do perdedor esperado), mas medido apenas como probabilidade de equilíbrio no modelo e em simulações, sem dado real, validado ou agregado. — evidência: "the supporters of the expected winner are less likely to abstain" (p. 18)
- **c4_desenho_elegivel** — resposta: Não — é modelo teórico de voto custoso (teoria dos jogos, equilíbrio de Poisson) com simulações numéricas, sem experimento, variação identificada de exposição ou painel individual. — evidência: "We study a costly voting model under population uncertainty" (p. 8); "we employ numerical simulations to confirm that the assumption" (p. 26)
- **c5_estudo_primario** — resposta: Não — não há análise própria de dados empíricos: o trabalho é formal/teórico, com simulações numéricas; não é revisão de literatura nem meta-análise. — evidência: "this is the first formal study that explains bandwagons in large elections" (p. 1)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação em nenhuma página do documento. — evidência: "Bandwagons in Costly Elections: The Role of" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Sem dados empíricos: modelo teórico de voto custoso; as únicas "observações" são simulações numéricas com população fixa de N = 20 e parâmetros de aversão à perda η ∈ {0.5, 1} e λ ∈ {1.5, 1.9}, sem período nem amostra de eleitores. — evidência: "we present numerical simulations for a population of fixed size" (p. 28)
- **registro_financiamento** — resposta: Sem identificador de pré-registro; financiamento declarado: grant interno IMVASY da University of Cyprus (Xefteris) e bolsa HFRI PhD Fellowship nº 337 (Leontiou). — evidência: "the University of Cyprus internal grant IMVASY" (p. 1); "PhD Fellowship grant (Fellowship Number: 337)" (p. 1)

## Notas do codificador
- **Offset de página.** O PDF tem 46 páginas: a 1ª é a folha de rosto do repositório (Edinburgh Research Explorer), sem numeração impressa, e as 45 seguintes trazem numeração impressa de 1 a 45. Confirmei em páginas distantes: PDF 2 = impressa "1" (título/abstract), PDF 32 = impressa "31" (Conclusion), PDF 46 = impressa "45" (última do apêndice). Logo, impressa P → PDF = P + 1, e `offset_pagina: 1`. Todas as evidências usam a numeração impressa.
- **texto_confere = parcial.** Título, três autores e ano conferem com o registro, e a folha de rosto do repositório cita o mesmo DOI. Marquei "parcial" porque o arquivo é a versão aceita/revisada por pares depositada em repositório, não a versão publicada: a paginação do documento (1–45) não corresponde à do periódico (vol. 209, pp. 471–490), o que importa para citar páginas em fases posteriores.
- **tipo_documento = artigo.** A declaração mais forte está na folha de rosto do repositório ("Published In: Journal of Economic Behavior and Organization"; "Document Version: Peer reviewed version"), mas essa página não tem numeração impressa e, por isso, não é citável no formato "(p. N)" desta ficha. Usei como evidência a autodeclaração "The current paper" no corpo numerado.
- **outros_relatos_mesmo_estudo = 999.** Nas páginas numeradas (1–45) não há menção a outra versão, working paper, tese ou relatório do mesmo estudo. A folha de rosto não numerada do repositório traz a citação da versão publicada (Journal of Economic Behavior and Organization, vol. 209, pp. 471–490, DOI 10.1016/j.jebo.2023.03.011), que é o mesmo trabalho em outra versão, mas por não ter página impressa não pude ancorá-la; registro o dado aqui.
- **c1 e c3 = parcial.** O conteúdo é eleitoral (eleitores escolhendo entre dois partidos; comparecimento/abstenção como variável de interesse), mas tudo é derivado em equilíbrio teórico e em simulações; não há eleitores reais, hipotéticos ou de laboratório, nem medida empírica de comparecimento. Preferi "parcial" a "Não" para não esconder que a população e o desfecho do protocolo são, em substância, os do modelo.
- **c2 = Não.** A pesquisa eleitoral só aparece como motivação na introdução (candidatos divulgam resultados de pesquisas quando lhes são favoráveis). No modelo, o que gera o efeito é a expectativa de equilíbrio sobre quem vence (ponto de referência endógeno à la Kőszegi e Rabin), não a exposição a um resultado de pesquisa divulgado.
- **c5 = Não sem a marca de revisão.** O documento não é revisão de literatura, revisão sistemática, meta-análise, editorial ou comentário; portanto NÃO escrevi "revisão: usar na bola de neve". Respondi "Não" porque não há análise própria de dados: é estudo formal com simulações numéricas. A seção 2 (Literature review) lista estudos empíricos de bandwagon/underdog (Irwin e Van Holsteyn 2000; Klor e Winter 2007; Großer e Schram 2010; Morton et al. 2015; Agranov et al. 2018; Faravelli et al. 2020) e pode ser útil ao coordenador como fonte de bola de neve, ainda que o texto não seja revisão.
- **Escolha das citações.** Preferi trechos curtos e contíguos dentro de uma mesma linha impressa e evitei palavras com ligaduras tipográficas (ff, fi, fl) e apóstrofos, que costumam quebrar na camada de texto deste PDF (ex.: evitei "financial support" e "citizen's expectations" nas evidências).
- **Cobertura da leitura.** Documento com 46 páginas de PDF: li todas, em faixas de 20 (PDF 1–20, 21–40, 41–46), incluindo abstract, introdução, revisão, modelo, análise, discussão, conclusão, referências e apêndice.
