---
citekey: Boudreau2010
ficha_id: Boudreau2010
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Boudreau2010.pdf
paginacao: impressa
offset_pagina: -512
agente_fichador: fichador_el_140
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim, o título, os dois autores (Cheryl Boudreau e Mathew D. McCubbins), o ano (2010) e o DOI impresso (doi:10.1017/S0022381609990946) batem com os metadados do registro — evidência: "The Blind Leading the Blind: Who Gets Polling" (p. 513)
- **tipo_documento** — resposta: artigo — evidência: "The Journal of Politics, Vol. 72, No. 2" (p. 513)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Não, os participantes são estudantes de graduação que escolhem entre as alternativas 'a' e 'b' de problemas de matemática do SAT, e não entre candidatos, partidos ou opções de referendo, em eleição real, hipotética ou de laboratório — evidência: "We ask subjects to make choices about math problems" (p. 515); "A total of 236 adults who were enrolled in undergraduate classes participated" (p. 520)
- **c2_intervencao_estudada** — resposta: Não, a exposição manipulada é o resultado de uma consulta feita pelos autores a 66 estudantes de graduação sobre a resposta correta de problemas de matemática, e não uma pesquisa eleitoral, agregador, projeção ou boca de urna — evidência: "before running our experiments, we polled 66 college undergraduates" (p. 515); "choose to receive the results of polls" (p. 515)
- **c3_desfecho** — resposta: Não, os desfechos são a decisão de receber ou não o resultado da consulta e o dinheiro ganho em cada problema, sem intenção de voto, escolha de voto, votação agregada nem comparecimento — evidência: "whether a subject chooses to receive a poll on each problem" (p. 520); "the amount of money that a subject earns on each problem" (p. 521)
- **c4_desenho_elegivel** — resposta: Sim, é experimento de laboratório com designação aleatória a quatro grupos de tratamento e a um grupo de controle, desenho aceito no protocolo (a inadequação deste texto está na exposição e no desfecho, não no desenho) — evidência: "we randomly assign subjects to either a control group" (p. 515); "we conducted laboratory experiments at a large public university" (p. 520)
- **c5_estudo_primario** — resposta: Sim, é estudo primário com dados próprios gerados e analisados pelos autores nos experimentos que conduziram — evidência: "A total of 236 adults who were enrolled in undergraduate classes participated" (p. 520); "We estimate the above model using a logistic regression" (p. 520)
- **c6_nao_retratado** — resposta: Sim, não há marca 'RETRACTED', nota nem página de retratação em nenhuma das 15 folhas do PDF — evidência: "The Blind Leading the Blind: Who Gets Polling" (p. 513)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: O documento remete a um apêndice online, hospedado na página da primeira autora, com resultados adicionais dos mesmos experimentos (é material suplementar deste artigo, não outro relato publicado); nenhuma versão anterior, tese, working paper ou artigo com os mesmos dados é mencionado — evidência: "The online appendix can be found at" (p. 524)
- **fonte_dados_amostra** — resposta: Experimentos de laboratório numa grande universidade pública, com 236 estudantes de graduação designados aleatoriamente a quatro grupos de tratamento (42, 49, 37 e 42) e ao controle (66), cada um decidindo sobre 10 a 18 problemas de matemática do SAT, totalizando 2.327 escolhas sobre receber a consulta (170 sujeitos) e 3.191 decisões (218 sujeitos); o período de coleta não é informado (manuscrito submetido em 5 de fevereiro de 2008) — evidência: "A total of 236 adults who were enrolled in undergraduate classes participated" (p. 520); "for a total of 2,327 choices" (p. 521)
- **registro_financiamento** — resposta: Financiamento da National Science Foundation, processo #SES-0616904, e do Kavli Institute for Brain and Mind; não há identificador de pré-registro (OSF, AEA RCT Registry, RIDIE ou EGAP) no documento — evidência: "the National Science Foundation (Grant #SES-0616904)" (p. 526)

## Notas do codificador

**Paginação.** A numeração impressa vai de 513 (primeira folha) a 527 (última), e o PDF tem 15 folhas, logo `folha_do_PDF = pagina_anotada - 512`. Confirmei a fórmula abrindo individualmente as folhas que cito: 513→1 (rodapé da abertura), 515→3, 520→8, 521→9, 524→12 e 526→14, cada uma com o número impresso no cabeçalho ou rodapé da própria página.

**C1, C2 e C3 (as três negativas).** O texto é um experimento sobre pesquisas de opinião, mas nenhum dos três elementos do protocolo aparece. (i) População: os sujeitos resolvem problemas binários de matemática do SAT, ganhando 50 centavos por acerto e perdendo 50 por erro; os autores explicitam que pediram escolhas sobre problemas de matemática justamente em vez de pedir voto em candidatos ou políticas fictícias, de modo que não há eleição real, hipotética nem de laboratório, nem opção de referendo, nem unidade eleitoral agregada. (ii) Intervenção: o tratamento é o resultado de uma consulta prévia a 66 estudantes de graduação sobre qual é a resposta correta de cada problema, variando em custo (grátis ou 10 centavos) e credibilidade; é uma pesquisa de opinião, mas não uma pesquisa eleitoral, agregador, projeção ou boca de urna. (iii) Desfecho: as variáveis dependentes são `ReceivePoll` (receber ou não a consulta) e `MoneyEarned` (qualidade da decisão em dinheiro), nenhuma delas de voto ou comparecimento.

Considerei responder 'parcial' nesses três critérios, porque os autores dedicam uma seção inteira à validade externa argumentando que decisões sobre problemas de matemática mapeiam decisões políticas (votar 'sim' ou 'não' numa iniciativa) e que suas consultas são análogas a pesquisas reais sobre fatos objetivos. Preferi 'Não' porque a analogia é argumento dos autores, não característica da amostra, da exposição ou do desfecho efetivamente medidos: o documento descreve sem ambiguidade o que os sujeitos fazem e o que é medido, e nada disso é eleitoral. A ressalva do protocolo que admite jogos eleitorais de laboratório com informação de pesquisa, qualquer que seja o tamanho do grupo, não alcança este desenho, porque aqui não há jogo eleitoral nenhum.

**C4.** Respondi 'Sim' porque o critério pergunta pelo desenho, e o desenho (experimento aleatorizado de laboratório, com designação aleatória a grupos de tratamento e controle) está entre os aceitos. A incompatibilidade deste texto com o protocolo está em C1, C2 e C3, não em C4.

**C6.** Li as 15 folhas do PDF e não há marca de retratação; usei o título da primeira página como evidência, conforme o prompt da variável. A checagem externa em OpenAlex e Crossref não é minha.

**outros_relatos_mesmo_estudo.** Não usei 999 porque há menção explícita a um documento com resultados dos mesmos experimentos (o apêndice online citado na nota 22, remetido também no corpo do texto na p. 524). Cito apenas o começo da frase da nota porque a URL se quebra no fim da linha do PDF. Nenhum outro relato (versão anterior, tese, working paper, relatório) é mencionado.

**fonte_dados_amostra.** Os números de sujeitos por grupo e de observações vêm da p. 520 e da nota 18 da p. 521, transcritos como impressos; não somei nem derivei nada. O documento não informa as datas de coleta, por isso registrei apenas a data de submissão do manuscrito, que consta da p. 526.
