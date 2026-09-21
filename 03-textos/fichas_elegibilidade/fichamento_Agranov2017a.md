---
citekey: Agranov2017a
ficha_id: Agranov2017a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Agranov2017a.pdf
paginacao: impressa
offset_pagina: 3
agente_fichador: fichador_el_091
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o documento é o WZB Discussion Paper SP II 2016-206 (setembro de 2016), versão working paper do artigo de 2017 na JEEA (DOI 10.1093/jeea/jvx023); título e os quatro autores (Agranov, Goeree, Romero, Yariv) são os mesmos do registro — evidência: "What makes voters turn out" (p. 1); "Discussion Papers of the Research Area Markets and Choice 2016" (p. 41)
- **tipo_documento** — resposta: working_paper — evidência: "Discussion Papers of the Research Area Markets and Choice 2016" (p. 41)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores de laboratório com preferências induzidas (cor sorteada de uma urna) que escolhem entre duas alternativas por regra de maioria, em grupos de nove sujeitos — evidência: "each participated in a total of 440 elections" (p. 3); "Overall, 198 subjects participated" (p. 10)
- **c2_intervencao_estudada** — resposta: Sim — a informação de pesquisa é manipulada experimentalmente em três tratamentos (No Polls, Perfect Polls e Lab Polls, este último com pesquisa de intenção de voto realizada e divulgada aos sujeitos antes da votação) — evidência: "subjects participated in a poll reporting their voting intentions" (p. 3); "we had three types of sessions" (p. 9)
- **c3_desfecho** — resposta: Sim — desfecho de comparecimento e de voto: propensão a votar (turnout) por tratamento e crença, e a vantagem realizada de cada alternativa comparada à vantagem prevista pela pesquisa — evidência: "Table 3 contains the observed voting propensities" (p. 18); "realized leads surpass those suggested by the poll" (p. 34)
- **c4_desenho_elegivel** — resposta: Sim — experimento de laboratório com sujeitos aleatorizados em grupos e tratamentos informacionais atribuídos por sessão — evidência: "We use laboratory experiments to test for one of the foundations" (p. 1); "subjects are randomized into a group of nine subjects" (p. 8)
- **c5_estudo_primario** — resposta: Sim — relata experimentos próprios conduzidos pelos autores, com análise dos dados gerados neles — evidência: "we present the voting patterns observed in our data" (p. 17)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação em nenhuma parte do documento — evidência: "What makes voters turn out" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: menciona um apêndice online com as instruções completas do experimento, hospedado na página pessoal de uma das autoras (http://people.hss.caltech.edu/~lyariv/papers/OnlineAppendix.pdf); não há menção a versão publicada, tese ou relatório técnico do mesmo estudo — evidência: "The full instructions are available at" (p. 8)
- **fonte_dados_amostra** — resposta: experimento de laboratório na California Social Sciences Experimental Laboratory (CASSEL) da UCLA, com 198 sujeitos em 22 grupos de 9, que participaram de 440 eleições entre duas alternativas em três tratamentos informacionais; o período de coleta não é informado (documento de setembro de 2016) — evidência: "Overall, 198 subjects participated" (p. 10); "each participated in a total of 440 elections" (p. 3)
- **registro_financiamento** — resposta: European Research Council, ERC Advanced Investigator Grant ESEI-249433; National Science Foundation, SES 0963583; Henry and Betty Moore Foundation (sem número); não há identificador de pré-registro — evidência: "ERC Advanced Investigator Grant" (p. 1); "the National Science Foundation (SES 0963583)" (p. 1)

## Notas do codificador
- Paginação e offset: a numeração impressa do corpo começa em 2 na 5ª página do PDF e termina em 40 na 43ª página do PDF, de modo que *página impressa P → PDF 1-based = P + 3*. O offset foi confirmado em duas páginas distantes: impressa 2 (PDF 5, início da Introdução) e impressa 37 (PDF 40, início das Referências). A página de resumo do WZB (PDF 4) corresponde à página 1 dessa sequência, embora o número não seja impresso nela; as citações atribuídas a `p. 1` (título, resumo e nota de agradecimentos) estão nessa página. As três primeiras páginas do PDF (capa do EconStor, folha de rosto do WZB e ficha institucional) precedem a página 1 e não recebem número impresso, por isso não foram usadas como evidência.
- Evidência de `tipo_documento` e da versão: a declaração mais explícita do tipo está na capa não numerada ("Working Paper"; "WZB Discussion Paper, No. SP II 2016-206"; "Discussion Paper / SP II 2016–206 / September 2016"). Como essas páginas antecedem a página 1, a evidência citada é a listagem da série na página 41 (PDF 44), que traz este mesmo número de série e título entre os discussion papers do WZB de 2016.
- `texto_confere` = parcial porque o PDF é a versão WZB Discussion Paper (2016) do trabalho registrado como artigo de 2017 na *Journal of the European Economic Association*; é outra versão do mesmo trabalho, não outro trabalho.
- `registro_financiamento`: o número do projeto do ERC aparece na nota de agradecimentos da p. 1 como "ESEI-249433"; o traço usado ali é um glifo da fonte do template do WZB que pode não ser o hífen simples, por isso a evidência verbatim cita só "ERC Advanced Investigator Grant" e o identificador numérico ancorado literalmente é o da NSF, "(SES 0963583)", na mesma nota e na mesma página.
- As citações do título foram truncadas em "What makes voters turn out" (o título impresso completo é "What makes voters turn out: The effects of polls and beliefs") para evitar a palavra "effects", com ligadura tipográfica ff, que costuma quebrar a verificação automática. Pelo mesmo motivo foram preferidos trechos sem ff/fi/fl nas demais evidências.
- `c2`: o tratamento Perfect Polls informa perfeitamente a distribuição de preferências realizada e o Lab Polls roda uma pesquisa de intenção de voto entre os próprios sujeitos, cujo resultado agregado é divulgado antes da decisão de votar; ambos são exposições a resultado de pesquisa manipuladas no experimento, e não a pesquisa como simples contexto ou fonte de dados.
- `c3`: o desfecho principal é comparecimento (propensão a votar, com custo de 25 ou 50 centavos), mas o documento também analisa desfecho de voto agregado — a vantagem realizada de cada alternativa em função da vantagem prevista pelas pesquisas (efeitos bandwagon e underdog) e a probabilidade de a alternativa majoritária ser eleita.
- `outros_relatos_mesmo_estudo`: decisão limítrofe. Não há menção a outra versão, tese ou relatório do mesmo estudo; a única referência a outro documento do próprio estudo é o apêndice online com as instruções do experimento (nota de rodapé 10, p. 8). Registrei-o em vez de 999 por ser um documento do mesmo estudo útil para a ligação de relatos.
- `fonte_dados_amostra`: o documento não informa as datas de coleta das sessões; a resposta registra essa ausência em vez de inferir a partir da data do discussion paper.
