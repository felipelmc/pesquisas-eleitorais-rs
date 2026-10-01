# Amostras de voz, versão 2: guia e trechos de textos do primeiro autor

Base do passe de voz de 30/09/2026 (`prompts_final/prompt_voz_autor.md`). Substitui `amostras_voz.md`, que usava listas do Survey-Research e textos do site. Os trechos são de textos de Felipe Lamarca escritos sem IA, citados para mostrar o ritmo. Não reaproveite o conteúdo deles. Erros de digitação do original foram mantidos e não devem ser imitados.

Fontes:
- **[M]** Lamarca, Felipe Marques Esteves. 2021. "As relações Executivo-Legislativo na Primeira República: uma análise das mensagens presidenciais ao Congresso (1910-1920)." *Mosaico* 13(20): 525–546. doi:10.12660/rm.v13n20.2021.82665.
- **[IL]** `felipelmc/Intro-Legislative-Studies`, `midterm/midterm.qmd` (mai. 2025) e notas de aula (ago. a nov. 2025). Não há commits de polimento.
- **[LG]** `felipelmc/Lego-I`, listas e aulas no commit `69a581e` (22/06/2025), anterior ao polimento por IA de set. 2026. Ficam fora o resumo e os parágrafos de inferência randomizada e DAG da lista 3, e os blocos de intervalo de confiança (aula 7), "Importante" (aula 11) e ANOVA (aula 13).

## 1. Guia de voz (registro formal: o *midterm* e o artigo da Mosaico)

**Ritmo.**
- Frases longas e encadeadas por subordinação: média de cerca de 28 palavras no *midterm* e mediana de 32 na Mosaico.
- Parágrafos de 2 a 4 frases. Uma frase curta e seca de vez em quando, para fechar um raciocínio.
- Nada de sequências de frases curtas do mesmo tamanho nem de parágrafos de uma frase só em série.

**Conectivos que ele usa** (variar, sem mecanizar):
- "trata-se de" (para classificar um resultado ou uma decisão);
- "de fato" (abre frase para confirmar ou aprofundar, nunca para contrastar);
- "isto é" (sempre em minúscula, depois de vírgula ou de ` -- `);
- "no entanto" no meio da frase, entre vírgulas ("Isso, no entanto, não se verifica…");
- "portanto" em minúscula, no meio da frase;
- "em outras palavras", "dito de outra forma" (para reformular no fim de um raciocínio);
- "em particular", "por sua vez", "daí", "afinal", "a despeito de", "em geral", "sobretudo", "aliás", "ou melhor";
- "Já X…" para contrastar com o que veio antes ("Já as teorias partidárias partem de um pressuposto distinto: …");
- "Note, no entanto, que…" para fechar com ressalva;
- "é claro" intercalado ("Esperamos, é claro, …");
- "Ora," e "No mínimo," (Mosaico), "Explico:" (Mosaico) e dois-pontos explicativos ("a questão é: …", "Trata-se de um resultado lógico: …").

**O que ele não usa:**
- "Contudo", "Entretanto", "Todavia", "Porém", "Ademais", "Em suma", "Dessa forma", "Destarte";
- "Assim," e "Logo," em início de frase;
- "Segundo X (ano)" e "De acordo com X" para apresentar autor.

**Citação.**
- O autor citado é o sujeito da frase: "@X mostra que…", "@X fazem uma análise…", "O que @X defende é que…", "na formulação de @X", "A figura do legislador em @X é…", "A principal questão de @X pode ser resumida da seguinte maneira: …".
- Citação entre parênteses no fim da frase quando a fonte só sustenta o fato.

**Pessoa.**
- Neste artigo: primeira do plural para tudo o que os autores fizeram, decidiram ou conferiram ("aprovamos", "conferimos em bloco", "decidimos").
- Impessoal com "-se" onde soar natural ("optou-se", "limitou-se", "impõe-se", "torna-se plausível").
- Os agentes de IA e o coordenador de IA ficam em terceira pessoa, como atores distintos.
- "Os autores" só para autores de estudos citados.

**Ressalvas.**
- "em certa medida", "pelo menos", "provavelmente", "parece", "mais ou menos", "em geral", "não necessariamente", "ao que tudo indica".
- Sequência expectativa e confirmação: "Esperamos, é claro, … De fato, observamos …".
- Nas frases de certeza do GRADE, as palavras padronizadas mandam (ver o *prompt*).

**Pontuação e marcação.**
- ` -- ` para glosa ou explicação, quase sempre seguido de "isto é" ou "afinal", fechado com ` --,` antes de vírgula. Com moderação: no máximo um a cada dois parágrafos. O travessão longo nunca.
- Dois-pontos frequentes, para anunciar definição ou explicação.
- Ponto e vírgula moderado, sobretudo em enumeração "(i) …; e (ii) …".
- Parênteses para glosas rápidas.
- Itálico para termos em inglês e para conceitos da literatura.
- Sem negrito no meio da prosa e sem exclamação no registro formal.
- Uma pergunta retórica é possível quando abre um problema (Mosaico: "Será que as relações Executivo-Legislativo se tornaram mais complexas nesse período?"). No máximo uma ou duas no artigo inteiro.

**Vocabulário.** indícios, achados, empreitada, caráter, contraintuitivo, interpretação clássica, dar conta de, de saída, a respeito de, do ponto de vista de, "a questão é", "a ideia é".

**O que vale do `my-voice` mesmo contra o corpus.** As proibições anti-IA continuam:
- "fundamental", "robusto", "crucial", "significativo", "abrangente", "essencial";
- "não apenas X, mas também Y";
- gerúndio conclusivo no fim da frase;
- "Além disso," e "Assim," abrindo parágrafo;
- "é importante notar" e "vale destacar".

O corpus de graduação tem alguns desses traços, e eles não devem ser imitados.

## 2. Trechos

### Abrir um problema e situar o debate

1. "Novos estudos, entretanto, têm disputado essa narrativa e apontado que o poder representativo da Primeira República precisa ser revisitado sob uma perspectiva menos normativa." [M]
2. "As relações entre os poderes Executivo e Legislativo durante a Primeira República têm sido alvo de reflexão. De um lado, persiste uma interpretação clássica que prevê harmonia entre ambos [...]" [M]
3. "No objetivo de verificar se há indícios de conflito [entre] os Poderes Executivo e Legislativo, serão analisadas as mensagens presidenciais enviadas pelo presidente da República ao Congresso Nacional entre os anos de 1910 e 1920, na inauguração do ano legislativo." [M]
4. "A relação entre dinheiro e eleições é amplamente explorada na literatura [@mancuso2015], mas poucos trabalhos investiram em análises inferenciais ou preditivas sobre essa relação no nível municipal [@sampaio_filho_2019]." [LG lista 1]
5. "Isso impõe pelo menos uma questão para o campo dos estudos legislativos: num _policy space_ unidimensional, vence o mediano; mas na prática, nos legislativos efetivamente implementados no mundo, frequentemente precisamos considerar maiorias qualificadas e, nesse caso, o mediano é insuficiente para entender todo o processo que envolve a aprovação de uma _policy_." [IL midterm]

### Definir e glosar

6. "A cloture, no entanto, é uma medida que requer o apoio de pelo menos 60 senadores -- isto é, três quintos do Senado --, e, portanto, trata-se de um mecanismo supramajoritário." [IL midterm]
7. "Em outras palavras, a opção por iniciar ou não um filibuster é condicionada pela posição (no espaço unidimensional) do filibuster pivot, que tem o poder de decidir se a cloture será ou não aprovada." [IL midterm]
8. "Em certa medida, no caso particular deste problema de pesquisa, os conceitos e as variáveis operacionalizadas se confundem." [LG lista 1]
9. "A variável de sucesso eleitoral é operacionalizada a partir do resultado nas urnas -- ou (1) uma variável contínua que guarda o número de votos de um candidato nas urnas, ou (2) uma variável binária que indica se o candidato foi eleito ou não. Opto pela segunda abordagem." [LG lista 1]

### O autor citado como sujeito

10. "A figura do legislador em @Arnold1990LogicCongressionalAction é um indivíduo, antes de tudo, avesso ao risco." [IL midterm]
11. "A principal questão de @Arnold1990LogicCongressionalAction pode ser resumida da seguinte maneira: por que o Congresso (1) ora aprova propostas que atendem a interesses particulares, (2) ora aprovam medidas que atendem a interesses difusos? De fato, na formulação de @Mayhew2004ElectoralConnection, só haveria incentivo para ações do primeiro tipo, e nunca para o segundo." [IL midterm]
12. "Na perspectiva da competição eleitoral, Ricci e Zulini (2012; 2013) rebatem o argumento clássico relacionado à degola." [M]

### Objeção em dois tempos e contraste

13. "Parte da literatura prevê que esse comportamento levaria a uma alta instabilidade no processo decisório -- afinal, o incentivo ao particularismo faria com que não existisse, em geral, equilíbrio, a não ser sob distribuições de preferência extremamente específicas. Isso, no entanto, não se verifica empiricamente, porque o Congresso se estrutura de maneira que induz equilíbrio [@ShepsleWeingast1981StructureInduced]." [IL midterm]
14. "Já as teorias partidárias partem de um pressuposto distinto: o de que o Congresso não se organiza primordialmente para atender aos interesses individuais dos legisladores, mas para maximizar os objetivos coletivos dos partidos." [IL midterm]
15. "Na perspectiva informacional, por sua vez, o grande problema é a incerteza a respeito do resultado da _policy_ [@Krehbiel1992InformationLegislativeOrganization] -- algo desconsiderado pelas perspectivas anteriores. De fato, essa perspectiva assume que os legisladores precisam tomar decisões sobre temas altamente complexos, cujos resultados são mais ou menos desconhecidos." [IL midterm]
16. "Há, no entanto, um salto conceitual para afirmar que a distribuição observada é representativa." [IL aula 9]

### Classificar e interpretar resultados

17. "Trata-se de um resultado lógico: como o Congresso é organizado para facilitar e organizar o _logrolling_ e os ganhos mútuos da troca, as decisões a respeito da policy são tomadas pelos legisladores especialistas, e essas decisões serão referendadas pelos pares -- sob a garantia de que o mesmo ocorrerá quando outros temas de interesse forem votados." [IL midterm]
18. "Os números mostram que, em média, ocorreram ao menos duas intervenções federais nos estados por ano entre 1910 e 1920. Trata-se de resultados contraintuitivos na medida em que contestam empiricamente a interpretação clássica [...]" [M]
19. "O quadro sinaliza que as mensagens ficam mais longas na medida em que os anos passam, com exceção de 1915 e 1917. [...] Será que as relações Executivo-Legislativo se tornaram mais complexas nesse período?" [M]
20. "Esperamos, é claro, um resultado bastante desviante do parâmetro populacional -- afinal, estamos amostrando um número pequeno de indivíduos uma única vez." Logo depois: "De fato, observamos que a média obtida superestima a renda mensal…" [LG lista 3]

### Ressalvas e limites

21. "Essa análise provavelmente é, por si só, enviesada pela potencial concentração de programas de pós-graduação no Sudeste, assim como pela longevidade dos programas na região. Essa é apenas uma hipótese que, pelo menos nessa ocasião, não será testada." [LG lista 2]
22. "No mínimo, torna-se plausível pensar na hipótese de as intervenções federais terem sido mal interpretadas pelos clássicos, já que há indícios de que poderiam funcionar como mais um elemento do pacto oligárquico." [M]
23. "Ao que tudo indica, a literatura clássica não explorou a possibilidade de governadores dos estados requisitarem auxílio do governo federal [...]" [M]
24. "Também seria razoável utilizar a receita, sob o risco de superestimar o efeito do dinheiro." [LG lista 1]
25. "Note, no entanto, que a delegação de poder do mediano para as comissões implica uma perda distributiva -- isto é, o mediano está disposto a tomar uma decisão mais ou menos enviesada em relação ao seu ponto ideal em troca de ganho de informação a respeito do _outcome_ da policy." [IL midterm]
26. "Isto é, não é porque um efeito é estatisticamente diferente de zero que ele é relevante." [LG aula 11, trecho anterior ao bloco "Importante"]

### Justificar uma decisão de método

27. "Para efeito de iniciar essa empreitada, limitou-se o foco às mensagens presidenciais enviadas ao Congresso entre 1910 e 1920." [M]
28. "O problema dessa estratégia é ficar refém do discurso de terceiros e encampar versões parciais, perdendo o controle sobre outras narrativas concorrentes." [M]
29. "Ora, tratar os anos 1910-1920 como exceção, [...] significa, na prática, basear toda a tese da política dos governadores em meros 9 anos de vivência política. Impõe-se, no mínimo, compreender melhor o que se passou desde 1910 [...]" [M]
30. "Dito de outra forma, apoiando candidatos de situação, o coronel obtinha auxílio financeiro para si (CARVALHO, 2002; LEAL, 2012)." [M]

### Fechar e apontar agenda

31. "Afinal, se o pacto oligárquico realmente funcionou a pleno vapor durante todo o período da Primeira República, o presidente deveria ter total anuência do Congresso Nacional [...]. No entanto, as mensagens presidenciais dão indícios de que esse não era o caso." [M]
32. "Futuras pesquisas deveriam estender a análise para todo o período pós implementação do pacto oligárquico, isto é, 1900-1930." [M]
33. "Análises futuras deverão, é claro, analisar a relação em outros anos." [LG]
