---
citekey: Gschwend2017
ficha_id: Gschwend2017
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Gschwend2017.pdf
paginacao: impressa
offset_pagina: -641
agente_fichador: fichador_el_131
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — título, autores e ano do documento batem com os metadados do registro (Gschwend, Meffert e Stoetzer, 2017, The Journal of Politics 79(2), DOI 10.1086/688678) — evidência: "Weighting Parties and Coalitions: How Coalition" (p. 642)
- **tipo_documento** — resposta: artigo — artigo publicado em periódico, com nota de publicação na primeira página — evidência: "The Journal of Politics, volume 79, number 2" (p. 642)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores em surveys representativos de população (estudo pré-eleitoral austríaco de 2006 e GLES alemão de 2009) que respondem perguntas de intenção de voto escolhendo entre partidos — evidência: "In this study participants were exposed to four coalition" (p. 646)
- **c2_intervencao_estudada** — resposta: Não — a exposição manipulada são sinais de coalizão (anúncios de partidos sobre coalizões pré-eleitorais) apresentados em vinhetas, e não resultado de pesquisa eleitoral; o próprio texto trata pesquisas pré-eleitorais como fonte de informação distinta dos sinais de coalizão e afirma que suas vinhetas isolam o efeito do sinal de coalizão do efeito de resultados de pesquisa — evidência: "to embed coalition signals as vignettes in a representative" (p. 646); "Besides preelection polls, coalition signals are the most" (p. 643)
- **c3_desfecho** — resposta: Sim — desfecho de voto: intenção de voto por partido, medida na decisão padrão e na decisão de vinheta, com modelagem das transições entre as duas escolhas; há ainda comparação descritiva de não votantes mobilizados, mas o desfecho analisado é de voto — evidência: "leading some voters to change their vote intention" (p. 642)
- **c4_desenho_elegivel** — resposta: Sim — experimentos de survey com vinhetas apresentadas em ordem aleatorizada, embutidas em dois surveys representativos (Áustria 2006 e GLES 2009) — evidência: "followed by four vignettes, in randomized order" (p. 646)
- **c5_estudo_primario** — resposta: Sim — estudo primário com análise própria dos dados dos dois experimentos de survey, estimando um modelo de escolha sequencial por inferência bayesiana — evidência: "obtained by MCMC sampling running two chains" (p. 649)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação em nenhuma das 14 folhas do PDF — evidência: "Weighting Parties and Coalitions: How Coalition" (p. 642)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Menciona apenas material do próprio artigo: um apêndice online com material suplementar e os dados depositados no JOP Dataverse; não há menção a versão anterior, working paper, tese ou dissertação que o tenha originado — evidência: "An online appendix with supplementary material is available" (p. 642)
- **fonte_dados_amostra** — resposta: Dois experimentos de vinhetas embutidos em surveys representativos: um survey pré-eleitoral da eleição geral austríaca de 2006 e o German Longitudinal Election Study (GLES Online Tracking T4), de 2009, cada um com quatro vinhetas de coalizão; o tamanho da amostra não é informado no texto principal (remetido ao apêndice) — evidência: "survey of the Austrian General Election 2006" (p. 646); "German Longitudinal Election Study (GLES Online Tracking" (p. 646)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- **Offset de página.** A numeração impressa do periódico vai de 642 a 655 e o PDF tem 14 folhas. Confirmei em duas folhas distantes: a folha 1 traz "642" no rodapé e a folha 8 traz o cabeçalho corrido "Volume 79 Number 2 April 2017 / 649". Logo, impressa P → folha do PDF = P − 641, isto é, `offset_pagina: -641` (642 − 641 = 1; 649 − 641 = 8; 655 − 641 = 14). Todas as páginas anotadas nas evidências são as impressas.
- **c2 (decisão de exclusão).** Este é o único critério em que o texto não atende. A exposição manipulada é o sinal de coalizão — declarações de partidos sobre com quem pretendem ou não governar —, não um resultado de pesquisa eleitoral. As vinhetas austríacas e alemãs transcritas nas p. 646–647 não apresentam número, percentual ou projeção de pesquisa: perguntam a intenção de voto condicionada ao anúncio de coalizão. O próprio artigo trata as duas coisas como fontes de informação distintas (p. 643) e critica, na p. 644, desenhos anteriores que combinam resultados de pesquisa com sinais de coalizão justamente por não conseguirem separar um efeito do outro. Por isso `Não`, e não `parcial`: nenhuma parte do documento usa resultado de pesquisa como exposição analisada.
- **c1, c3, c4 e c5 respondidos normalmente**, conforme a convenção do projeto de que os critérios anteriores podem ser respondidos mesmo quando outro critério falha.
- **c3.** A p. 652 menciona que mais não votantes austríacos e alemães passam a reportar intenção de voto depois das vinhetas e fala em potencial de aumentar o comparecimento, mas isso aparece como comparação descritiva das matrizes de transição, não como desfecho de comparecimento medido e analisado. Classifiquei o desfecho como de voto.
- **c6.** A checagem é apenas interna ao documento, como manda o prompt: li as 14 folhas e não há aviso de retratação. A verificação externa (OpenAlex/Crossref) é do coordenador.
- **outros_relatos_mesmo_estudo.** Optei por registrar o apêndice online e o depósito no JOP Dataverse em vez de 999, porque são registros companheiros do mesmo estudo, úteis para ligação; deixei explícito na resposta que não há menção a versão anterior, working paper ou tese. As referências a Meffert e Gschwend (2011, 2012) e Gschwend, Stoetzer e Zittlau (2016) são a estudos distintos, com outros dados, e não foram contadas aqui.
- **fonte_dados_amostra.** Fonte e período estão no texto principal; o tamanho da amostra dos dois estudos não é reportado no corpo do artigo (a nota 4, na p. 647, remete a estatísticas descritivas na tabela 1 e na tabela 9 do apêndice, que não integram este PDF). Não infiro N.
- **registro_financiamento = 999.** Os agradecimentos (p. 654) citam apenas comentários de colegas e a hospitalidade de Utrecht University, do Institute for Advanced Studies (Viena) e da Universidade de Mannheim, sem número de processo, edital ou identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP).
- **Escolha das citações.** Preferi trechos curtos, contidos numa única linha impressa e sem palavras com ligaduras tipográficas (ff, fi, fl) nem apóstrofos, para não quebrar o verificador; por isso evitei, por exemplo, "survey experiments in two different countries" e "The first survey experiment was implemented...".
