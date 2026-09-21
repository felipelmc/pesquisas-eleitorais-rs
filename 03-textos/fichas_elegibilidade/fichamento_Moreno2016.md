---
citekey: Moreno2016
ficha_id: Moreno2016
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Moreno2016.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_128
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim. O título e os autores impressos no documento batem com os metadados do registro (Moreno, Ramos-Sosa e Rodríguez-Lara, 2016); o PDF é a versão da série de working papers da Universidad de Málaga, enquanto o DOI do registro é do SSRN. — evidência: "Conformity, information and truthful voting" (p. 1)
- **tipo_documento** — resposta: working_paper. O documento é o número WP 2016-1 (fevereiro de 2016) da série de working papers do Málaga Economic Theory Research Center, do Departamento de Teoría e Historia Económica da Universidad de Málaga. — evidência: "Málaga Economic Theory Research Center Working Papers" (p. 0); "WP 2016-1" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: parcial. Participantes de laboratório com preferências induzidas votam entre duas opções, o que a definição admite, mas as opções são A e B genéricas, sem candidatos, partidos nem consulta popular, e o cenário modelado é o de um colegiado de cinco membros com quórum (conselho, senado, Suprema Corte), não o de um eleitorado. — evidência: "they were asked to vote between option A and option B" (p. 10); "students from the undergraduate population of the Universidad de Valencia" (p. 10)
- **c2_intervencao_estudada** — resposta: Não. A exposição manipulada é o incentivo monetário à conformidade e a informação de que dois agentes votarão conforme seu tipo; não há resultado de pesquisa eleitoral (pesquisa pré-eleitoral, agregador, projeção ou boca de urna) em nenhum ponto do desenho. — evidência: "In our treatment with conformity, the additional payoff is received only if" (p. 3); "a binary-decision voting game in which agents are heterogeneous" (p. 21)
- **c3_desfecho** — resposta: Sim. O desfecho é de voto: a escolha entre as opções A e B em cada rodada, operacionalizada como a probabilidade de votar conforme o próprio tipo (voting truthfully); o documento não mede comparecimento. — evidência: "we estimate a logit model for the likelihood of voting truthfully" (p. 15)
- **c4_desenho_elegivel** — resposta: Sim. Experimento aleatorizado de laboratório, com atribuição aleatória de tipo e comparação entre sujeitos dos tratamentos de conformidade e de informação. — evidência: "subjects were randomly assigned a type (Player A or Player B)" (p. 10); "Our experiment relies on a between-subject design" (p. 11)
- **c5_estudo_primario** — resposta: Sim. Estudo primário: os autores conduzem o próprio experimento e analisam os dados que coletaram, além do modelo teórico. — evidência: "This section presents our experimental evidence" (p. 13)
- **c6_nao_retratado** — resposta: Sim. Não há marca 'RETRACTED', nota nem página de retratação em nenhuma parte do documento, da capa da série às tabelas do apêndice. — evidência: "Conformity, information and truthful voting" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: 999 — evidência: 999
- **fonte_dados_amostra** — resposta: Experimento de votação em laboratório com 390 estudantes de graduação em Economia ou Administração da Universidad de Valencia, em sessões computadorizadas; o documento não informa as datas da coleta. — evidência: "390 subjects were recruited to participate in our computerized sessions" (p. 10); "students from the undergraduate population of the Universidad de Valencia" (p. 10)
- **registro_financiamento** — resposta: Não há identificador de pré-registro no documento. Financiamento declarado: Junta de Andalucía, processos SEJ-5980 e P09-SEJ-4941REC, e Ministério espanhol de Ciência e Tecnologia, processos ECO2014-53767-P e ECO2014-58297-R. — evidência: "financial support from Junta de Andalucía (SEJ-5980 and P09-SEJ-4941REC)" (p. 1)

## Notas do codificador

**Paginação e offset.** O PDF tem 36 folhas. A numeração impressa começa no corpo do artigo: a folha 3 do PDF traz "2" no rodapé e a folha 36 traz "35", duas páginas distantes que confirmam `offset_pagina: 1` (impressa P = folha P+1). A folha 1 é a capa da série de working papers, que não entra na numeração impressa; por isso, seguindo a convenção do coordenador, a evidência tirada só da capa está anotada como (p. 0), que o offset converte na primeira folha. A folha 2 (título, resumo, agradecimentos) é a página impressa 1: seu número é suprimido, como é usual na primeira página, mas ela ocupa a posição 1 da numeração, e anotá-la como (p. 0) mandaria a verificação para a capa, onde o resumo e os agradecimentos não estão. Registrei-a, portanto, como (p. 1), que é o que o offset resolve corretamente.

**Leitura.** Li o documento inteiro, nas faixas 1 a 20 e 21 a 36 do PDF (o item de documentos com mais de 300 páginas não se aplica).

**c1 limítrofe.** Codifiquei `parcial`, e não `Sim` nem `Não`, porque o caso fica entre duas cláusulas do critério. A favor de atender: é um jogo de votação de laboratório com preferências induzidas por pagamento, e o protocolo aceita esses jogos qualquer que seja o tamanho do grupo ou da sessão. Contra: os sujeitos escolhem entre "Option A" e "Option B" abstratas, sem candidato, partido ou pergunta de referendo, e a situação modelada é a de um colegiado de cinco membros com quórum de 3, 4 ou 5 votos, que o próprio texto motiva com conselhos de administração, parlamentares e a Suprema Corte dos Estados Unidos. A exclusão do protocolo é dirigida a votações de órgãos deliberativos reais, que não é o caso de um experimento de laboratório; daí `parcial` em vez de `Não`.

**c2 é o critério decisivo.** Não há pesquisa eleitoral em nenhuma forma no desenho: os tratamentos são o pagamento por conformidade (CON) e a informação comum de que dois participantes do tipo B estão obrigados a votar em B (INF). A informação sobre o comportamento dos outros vem da regra do experimento, não de pesquisa, agregador ou boca de urna divulgados. O texto cita literatura de bandwagon e de exit polls (Morton e Ou 2015; Morton et al. 2015) apenas como referência, para se distinguir dela.

**c3.** O desfecho é escolha de voto entre as duas opções, medida como votar conforme o próprio tipo. Não há medida de comparecimento porque, no desenho, cada sujeito vota em uma das duas opções em cada rodada. Não é possível comparar apoio a quem a pesquisa mostra à frente ou atrás, mas isso decorre da ausência de pesquisa (c2), não do desfecho.

**999.** Uma variável em 999: `outros_relatos_mesmo_estudo`. O documento não menciona versão anterior, tese ou relatório que o tenha originado. Cita "Moreno, B. & M.P. Ramos-Sosa (2015) Voting by Conformity. Universidad de Málaga, mimeo", de dois dos três autores, mas como trabalho teórico anterior e distinto, do qual empresta a definição lexicográfica de conformidade, não como outro relato deste estudo. Também não segui a menção, nas considerações finais, a um projeto mais amplo de testar funções de escolha social: é um plano de pesquisa, não um relato existente.

**Versão do texto.** Registro para o coordenador, sem alterar `texto_confere`: o PDF é o WP 2016-1 da Universidad de Málaga e o DOI do registro (10.2139/ssrn.2740364) é do SSRN. Título, autores e mês conferem, e a comparação pedida no codebook é de título, autores e ano, por isso `Sim`. Se a checagem externa do coordenador mostrar que o depósito do SSRN é uma versão diferente, isto vira `parcial`. Nota menor: na capa o terceiro autor aparece como "Rodríguez-Lara" e na folha de rosto como "Rodriguez-Lara", sem acento.

**Financiamento.** Os quatro processos estão na nota de agradecimentos da página impressa 1. A evidência cita apenas os dois primeiros porque o fim da frase quebra com hífen de fim de linha em "ECO2014-58297-R", e um fragmento que atravesse essa quebra é frágil na verificação. Os dois processos do Ministério estão transcritos na resposta.
