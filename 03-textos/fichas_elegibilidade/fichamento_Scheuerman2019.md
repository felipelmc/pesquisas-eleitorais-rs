---
citekey: Scheuerman2019
ficha_id: Scheuerman2019
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Scheuerman2019.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_101
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — o título e o primeiro autor impressos no documento batem com os metadados do registro (Heuristics in Multi-Winner Approval Voting; Jaelle Scheuerman; 2019) — evidência: "Heuristics in Multi-Winner Approval Voting" (p. 1)
- **tipo_documento** — resposta: preprint — o documento se declara como versão depositada no arXiv (1905.12104v2, cs.GT, 30 May 2019), sem nota de publicação em periódico ou anais — evidência: "arXiv:1905.12104v2" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — participantes humanos escolhem entre candidatos em eleições hipotéticas de laboratório por voto por aprovação, com preferências induzidas (utilidades apresentadas como representações monetárias) — evidência: "129 undergraduate students completed the study" (p. 7); "Each scenario includes a set of five candidates" (p. 5)
- **c2_intervencao_estudada** — resposta: parcial — a informação manipulada é o total de votos de cada candidato exibido ao participante antes do voto, que os autores aproximam explicitamente de pesquisas pré-eleitorais, mas nenhum resultado de pesquisa eleitoral (pesquisa publicada, agregador, projeção ou boca de urna) é apresentado como tal: os números são votos já depositados na própria eleição hipotética — evidência: "the total votes for each candidate so far" (p. 5); "the vote totals provided, as is the case with pre-election polls" (p. 8)
- **c3_desfecho** — resposta: Sim — o desfecho é de voto: mede-se o perfil de aprovação escolhido por cada participante entre os cinco candidatos (votar sinceramente, no líder ou nos de maior utilidade) e a frequência de voto em cada candidato; não há medida de comparecimento — evidência: "subjects could choose to vote truthfully" (p. 7); "the largest proportion of participants voting for Candidate E" (p. 8)
- **c4_desenho_elegivel** — resposta: Sim — experimento de laboratório com cenários manipulados intra-sujeito e condições de dois ou três vencedores entre sujeitos (Estudo 1); o Estudo 2 é simulação, sem participantes — evidência: "the design of two experiments aimed at studying the role" (p. 5); "The study was a 1 within (scenario) X 2 between" (p. 7)
- **c5_estudo_primario** — resposta: Sim — relata estudo primário com coleta e análise próprias (experimento com 129 estudantes e simulações computacionais dos mesmos cenários) — evidência: "through an experimental study and simulations" (p. 1)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação em nenhuma das 17 páginas do documento — evidência: "Heuristics in Multi-Winner Approval Voting" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Experimento de laboratório com 129 estudantes de graduação de duas universidades (66 na condição de dois vencedores e 63 na de três), cada um respondendo a quatro cenários hipotéticos de votação por aprovação multivencedor; período de coleta não informado — evidência: "129 undergraduate students completed the study" (p. 7); "with 66 subjects in the 2-winner condition and 63" (p. 7)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset de página: o cabeçalho corrido traz o número impresso a partir da segunda página; conferi a página 2 do PDF (cabeçalho "2"), a página 9 (cabeçalho "9", seção 5.1.2) e a página 17 (cabeçalho "17", referências finais). A página de rosto é a 1 do PDF e a numeração impressa coincide com o índice do PDF, logo `offset_pagina: 0` e `paginacao: impressa`.
- c2 como `parcial`: a exposição manipulada é informação sobre a posição dos candidatos (total de votos de cada um) mostrada ao participante antes de ele votar, e o heurístico central do artigo ("follow the leader") depende dessa informação, o que a aproxima de um jogo eleitoral de laboratório com informação de pesquisa. Contra isso: o documento nunca chama essa informação de pesquisa eleitoral; o participante é o último votante e os números são votos já depositados, com informação completa; as pesquisas pré-eleitorais aparecem como analogia ao discutir incerteza (p. 8) e como motivação na introdução, e a introdução de margens de erro nos totais de votos é apenas cogitada, não realizada (o Estudo 2 trata só do desempate e dos votos futuros desconhecidos). Registrei `parcial` em vez de `Não` por ser um caso-limite de exposição informacional pré-voto, e deixo a arbitragem para o coordenador.
- c4: o documento descreve manipulação de cenários intra-sujeito e duas condições entre sujeitos, mas não afirma em nenhum ponto que a alocação às condições de dois ou três vencedores foi aleatória. Respondi `Sim` por se tratar de experimento com exposição manipulada pelos pesquisadores, anotando essa lacuna.
- outros_relatos_mesmo_estudo como 999: não há menção, no corpo do texto, a versão anterior, tese, working paper ou relatório com os mesmos dados, nem seção de agradecimentos. O carimbo do arXiv indica "v2", o que sugere uma versão anterior do mesmo depósito, mas isso é inferência a partir do identificador e não uma menção do documento a outro relato; deixo o registro aqui para o coordenador, sem usá-lo como resposta.
- registro_financiamento como 999: o documento não tem seção de agradecimentos, financiamento, aprovação ética ou pré-registro; os únicos identificadores presentes são o do arXiv e a URL do Center for Election Science em nota de rodapé (p. 3), que não é registro nem financiamento do estudo.
- Li as 17 páginas do PDF (faixa 1-17), incluindo as figuras 1 a 11 e as referências.
