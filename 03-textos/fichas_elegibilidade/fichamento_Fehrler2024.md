---
citekey: Fehrler2024
ficha_id: Fehrler2024
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Fehrler2024.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_168
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim; o título e os três autores do documento batem com os metadados do registro (o documento traz a data "February 16, 2023", anterior ao ano 2024 do registro SSRN) — evidência: "Beliefs about Others:" (p. 1)
- **tipo_documento** — resposta: working_paper; manuscrito datado, com códigos JEL, palavras-chave e apêndices "for online publication", sem nota de publicação em periódico — evidência: "February 16, 2023" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Não; a amostra é de estudantes em laboratório que adivinham a cor da bola de outro participante sorteada de urnas, sem eleitores, candidatos, partidos ou opções de referendo — evidência: "In Treatment 1, 116 students (average age: 22 years old" (p. 13)
- **c2_intervencao_estudada** — resposta: Não; a exposição manipulada são intervenções para estimular o uso do próprio sinal (urnas físicas, sorteio sem reposição, elicitação de crenças e de estratégia), não resultado de pesquisa eleitoral — evidência: "We try to facilitate projection (rational updating) by three interventions each." (p. 11)
- **c3_desfecho** — resposta: Não; o desfecho é o palpite sobre a cor da bola do outro participante e as crenças probabilísticas declaradas, sem intenção de voto, voto agregado ou comparecimento — evidência: "how often the participants actually guess the same color signal" (p. 14)
- **c4_desenho_elegivel** — resposta: Sim; é experimento de laboratório com tratamentos e um experimento de controle adicional, desenho aceito pelo protocolo (ainda que a exposição não seja pesquisa eleitoral) — evidência: "In a laboratory experiment with three consecutively developed treatments" (p. 2)
- **c5_estudo_primario** — resposta: Sim; relata sessões experimentais próprias programadas e conduzidas pelos autores, com análise dos dados gerados — evidência: "We programed all treatments in z-Tree" (p. 13)
- **c6_nao_retratado** — resposta: Sim; não há marca, nota ou página de retratação no documento — evidência: "A Striking Example of Information Neglect" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Experimento de laboratório com oito sessões (116, 58 e 54 estudantes nos Tratamentos 1, 2 e 3), mais um tratamento de controle de agente único conduzido online em março de 2022 com 56 participantes de agente único e 54 de linha de base — evidência: "We conducted eight experimental sessions in total" (p. 13)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset: a numeração impressa no rodapé coincide com a folha do PDF (folha 2 traz "2"; folha 14 traz "14"; folha 36 traz "36"), logo `offset_pagina: 0`. Cada citação foi reaberta na folha indicada pela fórmula `folha = pagina_anotada + 0`: p. 1 (folha 1, rosto, sem numeração impressa), p. 2, p. 11, p. 13 e p. 14. A folha 1 não tem número impresso; anotei "1" porque é o valor que satisfaz a fórmula.
- `texto_confere` = Sim (e não "parcial") porque título, os três autores e a natureza do documento (manuscrito de trabalho) batem com o registro; a única divergência é a data do arquivo (16/02/2023) contra o ano do registro SSRN (2024), o que é comum quando o arquivo depositado é anterior à data de postagem. Se o coordenador preferir tratar versões datadas como distintas, este item viraria "parcial".
- `tipo_documento`: o documento não declara série nem editora; classifiquei como working_paper pelo formato (folha de rosto com afiliações e data, classificação JEL, palavras-chave, "Appendices (for online publication)") e ausência de nota de publicação. "preprint" seria a alternativa defensável, dado que o DOI do registro é de repositório SSRN.
- C1 a C3 = Não: o objeto é inferência bayesiana sobre o tipo de outro jogador num jogo de urnas e bolas (projeção versus negligência de informação). Não há eleição real, hipotética ou de laboratório, não há pesquisa eleitoral como exposição e não há desfecho de voto nem de comparecimento. As únicas menções a eleições são de literatura relacionada na introdução e em referências (por exemplo Agranov et al. e Goeree e Großer), não do desenho empírico.
- C4 = Sim isoladamente, porque o critério trata do tipo de desenho (experimento aleatorizado de laboratório) e não da exposição; a incompatibilidade com o protocolo está em C1, C2 e C3.
- `outros_relatos_mesmo_estudo` = 999: a nota de rodapé 19 (p. 13) menciona que participantes do Tratamento 1 também participaram de um tratamento-piloto "completely unrelated" de outro estudo, o que não é outro relato deste mesmo estudo; não há menção a versão anterior, tese ou relatório do próprio trabalho.
- `registro_financiamento` = 999: não há identificador de pré-registro nem número de processo ou edital. Os agradecimentos (p. 23) informam apenas apoio da "Foundation for Science and Research of the Canton Thurgau in Switzerland", sem número, o que não atende ao que o prompt pede para transcrever.
- Nas citações evitei trechos com ligaduras tipográficas (ff, fi, fl) sempre que havia alternativa.
