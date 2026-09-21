---
citekey: Meffert2012a
ficha_id: Meffert2012a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Meffert2012a.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_174
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial. O título e os autores batem com o registro, mas o PDF é a versão working paper depositada no SSOAR (Mannheim, 2010), e não o capítulo publicado em 2012 com o DOI informado — evidência: "Experimental Triangulation of Coalition Signals: Varying Designs, Converging Results" (p. 1)
- **tipo_documento** — resposta: working_paper. A folha de rosto do repositório classifica o documento como working paper, embora o corpo do texto se refira a si mesmo como capítulo — evidência: "Arbeitspapier / working paper" (p. 0)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim. Os três estudos têm participantes que escolhem entre partidos: dois experimentos de laboratório (jogo eleitoral com preferências induzidas e campanhas estaduais alemãs reais) e um experimento embutido em pesquisa pré-eleitoral representativa na Áustria — evidência: "representative pre-election survey before the 2006 Austrian General Election" (p. 16)
- **c2_intervencao_estudada** — resposta: Sim. O resultado de pesquisa eleitoral é manipulado experimentalmente junto com o sinal de coalizão no experimento econômico (disponibilidade da pesquisa randomizada) e no experimento psicológico (desempenho da pequena legenda acima ou abaixo da cláusula de barreira, numa tela que simula pesquisa estadual divulgada) — evidência: "The poll manipulation varied the expected performance of the small party" (p. 12)
- **c3_desfecho** — resposta: Sim. Desfecho de voto: decisão de voto com prêmio monetário no experimento econômico, decisão hipotética de voto no experimento psicológico e intenção de voto no experimento de survey; não há medida de comparecimento — evidência: "The key dependent variable was a hypothetical vote decision" (p. 8)
- **c4_desenho_elegivel** — resposta: Sim. Experimentos aleatorizados (laboratório econômico, laboratório psicológico e survey experiment), com atribuição aleatória das manipulações de pesquisa eleitoral e de sinal de coalizão — evidência: "the visibility of the signal to participants was randomized with equal probability" (p. 11)
- **c5_estudo_primario** — resposta: Sim. Os autores relatam três experimentos próprios, com desenho, coleta e análise próprios — evidência: "we designed an economic experiment that presented participants with an abstract game" (p. 7)
- **c6_nao_retratado** — resposta: Sim. Não há marca, nota ou página de retratação no documento — evidência: "Experimental Triangulation of Coalition Signals:" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim. O experimento econômico remete a Meffert e Gschwend (2007), working paper SFB 504 nº 07-55 da Universidade de Mannheim, e o experimento psicológico remete a Meffert e Gschwend (no prelo), artigo do European Journal of Political Research — evidência: "(for details, see Meffert and Gschwend 2007)" (p. 9); "(see Meffert and Gschwend, forthcoming, for details)" (p. 12)
- **fonte_dados_amostra** — resposta: Três experimentos dos próprios autores: um experimento econômico de laboratório com jogo abstrato de quatro partidos e preferências induzidas (amostra de conveniência de estudantes), um experimento psicológico de laboratório embutido em duas campanhas eleitorais estaduais alemãs em janeiro de 2006 (amostra de conveniência de estudantes) e um experimento de survey dentro de uma pesquisa pré-eleitoral representativa antes da eleição geral austríaca de 2006; o documento não informa o N total de participantes de nenhum dos três — evidência: "embedded in two real, contemporaneous German state election campaigns in January 2006" (p. 11)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset: a folha 1 do PDF é a capa do repositório SSOAR, sem numeração impressa; a folha 2 traz o cabeçalho "Experimental Triangulation 1" e a folha 26 traz "25", de modo que impressa P → folha do PDF = P + 1. Confirmei o offset em páginas distantes (impressas 1, 7, 11, 16 e 25) e reconferi cada página citada pelo cabeçalho. A capa recebe página impressa 0, valor que satisfaz a fórmula.
- `texto_confere` = parcial porque o registro traz ano 2012 e DOI de capítulo (Palgrave), enquanto este PDF é a versão de working paper depositada no SSOAR e citada como Gschwend e Meffert (2010), Mannheim; título e autoria são os mesmos, só a ordem dos autores muda na capa do repositório.
- `tipo_documento` = working_paper por declaração da folha de rosto ("Arbeitspapier / working paper"). Registro a tensão: o próprio corpo do texto diz "In this chapter we will focus on one particular but striking advantage of experiments" (p. 1), e o registro aponta capítulo publicado. Mantive o que o documento declara na folha de rosto, conforme o prompt da variável.
- `c2` = Sim pela regra de que basta um estudo do documento atender: a pesquisa eleitoral é exposição manipulada e analisada no experimento econômico (a Tabela 2, p. 23, compara decisões ótimas nas condições "No Info", "Poll Only", "Signal Only" e "Poll & Signal") e no experimento psicológico (pesquisa manipulada acima/abaixo da cláusula de barreira, apresentada como resultado de pesquisa estadual real). No experimento de survey, a manipulação é apenas de sinal de coalizão, não de pesquisa.
- `c3`: o desfecho é de voto em todos os três estudos; não há medida de comparecimento, então não marquei a célula de mobilização.
- `registro_financiamento` = 999: o documento não traz seção de agradecimentos, financiamento ou pré-registro. O número "SFB 504 Working Paper No. 07-55" aparece apenas dentro de uma entrada da lista de referências (p. 21), referente a outro trabalho citado, e por isso não foi tomado como identificador de financiamento deste documento.
- Evidências escolhidas evitando palavras com ligaduras tipográficas sempre que havia alternativa; em `outros_relatos_mesmo_estudo` o sobrenome "Meffert" é inevitável para citar a referência mencionada.
