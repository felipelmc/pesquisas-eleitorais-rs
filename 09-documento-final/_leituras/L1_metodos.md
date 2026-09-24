# Leitura crítica simulada: L1, editor de métodos

Leitura simulada por IA (subagente Opus, papel L1, 24/09/2026). Não é revisão por pares, não valida nenhuma etapa e não substitui a leitura do autor (P038).

Li `revisao_final.qmd`, as figuras em `revista/figuras/saida/`, `suplemento.qmd` e `linguagem_simples.qmd`. Conferi o texto contra o PRISMA 2020 (27 itens e os 12 do resumo), o SWiM (itens 1 a 9), o GRADE e a tabela de resumo dos achados, a orientação de Garritty et al. (2024) para revisões rápidas e as regras do livro (`insumos/livro_regras.md`). Os IDs de célula (C01 a C18) são os do atributo `cel` dos enunciados e seguem a ordem das linhas da Tabela 2.

## Avaliação geral

O rascunho é mais transparente do que a média das revisões publicadas. Ele declara que as etapas depois do protocolo foram feitas por agentes, lista as 18 pendências e nunca junta randomizados com não randomizados. A direção sai da estimativa pontual, a proporção vem com IC de Clopper-Pearson e o teste de sinal traz a ressalva. A certeza é julgada por célula, com frases padronizadas, e as limitações seguem as etapas. As contas que conferi fecham: fluxo (1.767 e 1.706; 1.573 e 1.054; 259 + 267 = 526; 42 + 13 = 55), 27 estudos em 18 células, contagens de risco de viés em S5 e 70 efeitos principais de 37 estudos em S6. Os problemas estão em cinco lugares:

1. O título chama de revisão sistemática um produto que, pela regra do livro que o texto cita, não conta como tal.
2. O dado que move toda a síntese, a direção de cada estudo, teve 50% de concordância na validação cega, e o texto relata o número sem dizer que a validação não aprovou a extração.
3. As três células acima de certeza muito baixa, que alimentam as mensagens principais (C13, C14 e C18), têm problemas de estimando, de unidade de análise e de rebaixamento por risco de viés. Corrigidos, podem baixar a certeza de pelo menos uma delas.
4. A leitura de que a regularidade *bandwagon* "depende" do laboratório vai além das contagens.
5. Faltam os checklists e partes dos itens 16a, 24b e 27 do PRISMA. O protocolo, que sustenta toda afirmação de "decidido antes ou depois de ver os dados", não está acessível ao leitor.

A maior parte das correções é de texto. Cerca de metade exige decisão do autor.

## Comentários graves

### 1. grave: o título promete mais do que a regra do livro permite

- **Local:** título e subtítulo; 2.1 Protocolo; 2.9 Uso de IA, último parágrafo.
- **Problema:** o subtítulo apresenta o texto como "Revisão sistemática rápida". A 2.9 parafraseia o livro assim: um produto executado de ponta a ponta por agentes "não conta como revisão sistemática concluída". Essa é a regra mais branda (R7.24). A regra que se aplica aqui é a R7.28: agentes que executam a revisão de ponta a ponta "não são uso aceitável", e "Nenhum produto desse tipo conta como revisão sistemática". A R7.27 também limita o LLM à estrutura e às seções descritivas, e aqui agentes redigiram a interpretação. O quadro de rascunho não resolve a contradição, porque é o título que circula (R2.11).
- **Correção proposta:** citar a R7.28 literalmente na 2.9. No título ou no subtítulo, marcar o estatuto (por exemplo, "rascunho de revisão sistemática rápida conduzido por agentes de IA, não validado"), mantendo a identificação que o item 1 do PRISMA pede. Outra saída é justificar por escrito por que a R7.28 não se aplica. Exige decisão do autor.

### 2. grave: a validação da extração por IA falhou, e o texto não diz isso

- **Local:** 2.5 Extração; 4.4 Limitações do processo, parágrafo da extração; declaração de uso de IA.
- **Problema:** a síntese inteira é uma contagem de direções. Na recodificação cega de 10 estudos, a concordância foi de 58,5%, com 37 variáveis abaixo do limiar. O κ foi 0,38 em alvo e comparador e 0,15 no estimando, e a direção da estimativa principal concordou em 50%. Na reextração cega, 6 dos 56 efeitos principais tinham outro sinal e 12 tinham outro valor. O texto dá esses números, mas não diz o que eles significam pela regra do protocolo: a validação não aprovou a extração por IA. A R7.25 pede exatamente isso ("Relato honesto de não aprovação é resultado metodológico"). Também faltam cinco informações:
  - o limiar do protocolo;
  - por que os efeitos principais passaram de 56, na reextração, para 70, na versão final;
  - quais arbitragens foram afetadas pelo erro de *prompt* que levou a barrar 40 correções;
  - se as 240 correções estendidas sem arbitragem tocam efeitos principais;
  - se algum dos 8 estudos das duas células das mensagens principais, ou os de C13, C14 e C18, teve o sinal trocado ou decidido só pelo árbitro, que é do mesmo modelo do reextrator.
- **Correção proposta:**
  1. Declarar na 2.5 o limiar do protocolo e que ele não foi atingido.
  2. Acrescentar ao suplemento uma tabela, estudo a estudo, para C01, C02, C13, C14 e C18: direção na extração original, direção na reextração cega, se houve arbitragem e o que ela decidiu.
  3. Explicar a passagem de 56 para 70 efeitos principais.

  O item 2 é tabulação nova de arquivos que já existem. Exige decisão do autor.

### 3. grave: o enquadramento do achado principal vai além das contagens

- **Local:** mensagens principais (1º item); resumo executivo (2º e 3º parágrafos); 1.4 Objetivos (2º parágrafo); 3.8 Sensibilidades (2º parágrafo); 4.1 Resumo dos achados; 4.2 Relação com revisões anteriores (1º parágrafo); 5.2 Brasil, item (i); 6 Conclusões.
- **Problema:**
  - **(a) A direção vira achado.** "Nos experimentos, a direção é *bandwagon*" (Conclusões) e "a direção dominante é *bandwagon*, com certeza muito baixa" (resumo executivo, 5.2) enunciam a direção como achado e só depois anexam a certeza. Com certeza muito baixa, a frase padrão é "a evidência é muito incerta sobre..." (R5.36). Sem certeza, só se pode fazer uma descrição, como "os 8 experimentos das duas células apontaram na direção *bandwagon*".
  - **(b) "Depende do laboratório" não sai dos dados.** A 3.8 diz "Disso segue que a regularidade *bandwagon* depende dos experimentos de laboratório e com vinheta", e o resumo executivo, a 4.1 e a 4.2 dizem que a regularidade "rareia" em eleições reais. Os dados da própria revisão não mostram isso. No alvo principal, 3 dos 4 estudos em contexto real foram *bandwagon* (3.10, parágrafo do realismo), e só um deles é de pesquisa pré-eleitoral (@Farjam2020a); os outros tratam de boca de urna e de apuração parcial. Na viabilidade e no *momentum*, os 5 estudos em eleição real foram a favor ou mistos. Os dados mostram que há poucos estudos em contexto real e que não se sabe se o padrão se mantém neles. Não mostram que o padrão depende do laboratório. A comparação é *post hoc*, não tem teste e soma classes de desenho. A frase "em linha com" @Barnfield2019 herda o mesmo excesso.
  - **(c) As células não isolam o mecanismo.** A contribuição (ii) diz que as células distinguem *bandwagon* de voto estratégico. Nas células de alvo principal, quem aparece à frente é também a opção viável. Dois dos oito estudos das células das mensagens (@Tyszler2015 e @Tal2015a) testam coordenação estratégica em laboratório com incentivos, como a própria 3.9 diz. Os autores de @Witsman2016a leem o contraste do estudo como voto estratégico. "Direção *bandwagon*" é, aqui, um rótulo operacional para "mais apoio a quem aparece à frente", que não isola o mecanismo.
- **Correção proposta:**
  - (a) reescrever como descrição da contagem, seguida da frase GRADE.
  - (b) trocar por: "a regularidade repousa sobretudo em estudos de laboratório e vinheta; em contexto real, há 4 estudos de apoio ao líder, 3 na mesma direção e só 1 de pesquisa pré-eleitoral, e não se sabe se o padrão se mantém".
  - (c) dizer no glossário e na 2.7 que "*bandwagon*" nomeia a direção do apoio a quem aparece à frente, compatível com *bandwagon* e com voto estratégico, e limitar a contribuição (ii) ao que as células de viabilidade e de *momentum* de fato separam.

  São mudanças de texto, sem análise nova.

### 4. grave: a certeza baixa de C18 contraria a regra aplicada às outras células e está nas mensagens principais

- **Local:** Tabela 2, linha C18 (pesquisa pré-eleitoral, unidades expostas × não expostas, comparecimento); mensagens principais (2º item); resumo; *abstract*; resumo executivo; 6 Conclusões; 3.7 Comparecimento (penúltimo parágrafo); 3.8, item (v); S7 (@Geers2018).
- **Problema:**
  - **Rebaixamento por risco de viés.** Nas outras células não randomizadas, resultado ROBINS-I em risco grave rebaixou dois níveis: C04, C06 e C11 têm a nota *b*. Em C18, @Stolwijk2019b está em risco grave e a célula caiu só um nível (nota *a*). O texto deixa a questão ao autor (decisão ii da 4.4), mas as mensagens principais e o resumo apresentam "certeza baixa" sem ressalva.
  - **Entrada de @Stolwijk2019b.** O estudo entra só pelo sinal de p1 − p0, num painel com exposição autorrelatada e confundimento grave.
  - **Imprecisão.** C18 caiu um nível com 2 estudos, um deles sem n relatado, e IC da proporção de 0,16 a 1,00. As células de 1 estudo com IC que cruza zero caíram dois.
  - **@Geers2018.** Este painel de comparecimento aponta para desmobilização e ficou fora da contagem por "conferência humana pendente". Esse motivo vale para os 560 efeitos (P039), mas foi aplicado a um único estudo, e justamente a um que contraria a direção da célula. A 3.8, item (v), não diz em que célula ele entraria. Se for em C18, a célula fica 2 de 3, com inconsistência.
- **Correção proposta:** aplicar a C18 a regra das demais (risco grave, dois níveis) ou justificar a exceção na nota da célula. Enquanto a decisão estiver aberta, tirar C18 das mensagens principais e do resumo ou pôr a ressalva nos dois. Tratar @Geers2018 como os demais efeitos não conferidos (dentro, pela direção) ou declarar um critério geral que o exclua. Dizer em que célula ele entraria. Muda célula e GRADE. Exige decisão do autor.

### 5. grave: o único achado de certeza moderada (C13) tem problemas de base

- **Local:** Tabela 2, linha C13; 3.7 Comparecimento (2º parágrafo); 3.9 Mecanismos (3º parágrafo); S6 (@Gerber2020a, E12 e E31); mensagens principais (2º item); resumo executivo; 4.1 Resumo dos achados.
- **Problema:**
  - **(a) E12 não estima o contraste da exposição.** Pelo próprio texto, E12 é o efeito de variável instrumental: "1 ponto percentual a mais de crença muda o comparecimento em 0,08 ponto" (3.9) corresponde aos 0,08 p.p. de E12 em S6, e a 3.8 fala do "efeito de variável instrumental". Esse coeficiente está em outra escala (p.p. de comparecimento por p.p. de crença) e não estima o contraste da exposição. Pela regra da Emenda 5, a mesma que tirou @Klor2017a E01 da contagem por não ser contraste de exposição, ele deveria ficar fora. Compará-lo com ±δ não diz nada sobre o efeito de receber a pesquisa. A frase "As duas estimativas tiveram IC 95% inteiro dentro de ±δ" fica errada, embora E31 sozinho sustente o nulo (0,29 p.p.; IC de g de cerca de −0,002 a 0,022).
  - **(b) O estimando é mais estreito do que as frases derivadas.** O que se estima é o efeito de receber uma carta com a pesquisa, sem saber quem a leu (intenção de tratar), em eleições para governador nos Estados Unidos, comparando disputa apertada com folgada. A Tabela 2 diz "Receber pesquisa...". As mensagens principais, o resumo e a 4.1 encurtam para "Pesquisa apertada, frente a folgada", e a 4.1 diz que o experimento "permite descartar" efeitos maiores que 2 p.p., o que é mais forte que "provavelmente". A célula não foi rebaixada por indireção nem há justificativa para não rebaixar.
  - **(c) O limiar do nulo é convenção e veio depois.** O δ de 2 p.p. é convenção do protocolo, sem âncora. A regra de classificar como nulo por ±δ veio da Emenda 5, depois de ver os dados. É plausível que os efeitos que interessam ao debate sejam menores que 2 p.p., e então "nulo ou trivial" frente a ±2 p.p. informa pouco a quem decide.
- **Correção proposta:**
  - Mover E12 para os efeitos fora da contagem, mantendo-o na sensibilidade, e reescrever a frase sobre "as duas estimativas".
  - Manter "receber, por carta," em todos os produtos (R2.9) e trocar "permite descartar" pela frase padrão, "provavelmente resulta em pouca ou nenhuma diferença" (R5.36).
  - Registrar na nota da célula a indireção do estimando e rebaixar ou justificar por que não.
  - Mostrar como sensibilidade a classificação com δ de 1 p.p. e declarar que o nulo depende de uma regra decidida depois de ver os dados.

  Muda célula e, possivelmente, GRADE. Exige decisão do autor.

### 6. grave: lacunas conhecidas da busca, que atingem justamente os desenhos da pergunta regulatória, não foram corrigidas

- **Local:** 2.3 Fontes e busca; 2.1 Protocolo (2º parágrafo); S1; S2 (A1 e A4).
- **Problema:**
  - **Uma só base internacional.** Para a literatura internacional em periódicos houve uma só base bibliográfica, porque a BDTD é catálogo de teses. A recomendação 5 de Garritty et al. não admite isso na substância, e "no limite" é generoso.
  - **Sem SciELO.** A SciELO não foi buscada, embora a pergunta secundária seja sobre Brasil e América Latina.
  - **Lacunas apontadas e não corrigidas.** A pré-revisão por IA de 23/09 apontou três lacunas: faltam termos de proibição, embargo e apuração parcial; o fio de comparecimento é estreito; e a BDTD não tem termo de comparecimento. São os desenhos que mais pesam para o debate brasileiro (proibição, embargo e comparecimento), e o fato de @Lago2015 e @Araujo2021a só terem vindo pela busca por citação é sintoma disso.
  - **Validação e registros.** O *recall* de 19 em 19 não é independente, não há âncora em português nem em espanhol e não houve busca em registros.
  - A correção é barata e usa as mesmas ferramentas.
- **Correção proposta:** antes de circular, rodar três buscas suplementares, triadas pelas mesmas regras e registradas como nova emenda:
  - no OpenAlex, com os blocos que faltam (proibição, embargo ou *blackout*; apuração parcial ou *early returns*; comparecimento ampliado);
  - na SciELO, em português e espanhol;
  - na BDTD, com termo de comparecimento.

  Se não forem feitas, reclassificar a recomendação 5 como "fora" em S2 e dizer, na 5.2, que a evidência sobre proibições e comparecimento é a mais exposta às lacunas da busca. Exige decisão do autor.

### 7. grave: 65% de relatos não recuperados sem explicação, e o fluxo não fecha na etapa do texto completo

- **Local:** 2.4 Seleção (2º e 3º parágrafos); 3.1 Estudos incluídos (1º parágrafo); Figura 2 (PRISMA); resumo e *abstract*, campo Limitações.
- **Problema:** "342 de 526 relatos não recuperados" é a única limitação numérica do resumo, mas o texto não esclarece três coisas:
  - **(a) Onde entra a triagem complementar.** Não diz se os 165 não recuperados da triagem complementar (Emenda 6b) estão entre os 342. A Figura 2 não tem ramo para essa triagem, e a frase da 3.1 sobre ela é ambígua.
  - **(b) Por que não foram recuperados.** Os motivos (acesso pago, desafio antirrobô, não localizado, capítulo de livro) não são dados, além de "parte deles de acesso aberto bloqueado por desafio antirrobô".
  - **(c) Que registros são.** Muitos dos 165 não tinham resumo e nunca foram triados pelo conteúdo, então a taxa mistura registros de relevância desconhecida com relatos provavelmente elegíveis.

  Além disso, a conta do texto completo não fecha: foram avaliados 184 relatos (101 + 83), mas 165 decisões propostas pela IA e 17 do autor somam 182. Também não se sabe se os 15 relatos recuperados na Emenda 6b estão entre os 184. A R5.2 pede que o fluxo separe as exclusões humanas das automáticas, e a caixa de excluídos no texto completo junta as duas.
- **Correção proposta:**
  - Acrescentar à Figura 2, ou a uma tabela ao lado, o ramo da Emenda 6b: 336 registros, 156 excluídos, 180 buscados, 165 não recuperados e 15 excluídos.
  - Detalhar os não recuperados por origem, motivo e tipo de documento.
  - Reconciliar os 184 relatos do texto completo e separar, na caixa, as decisões do autor das da IA.
  - No resumo, dar a decomposição ("342 de 526, dos quais 165 da triagem complementar de registros sem resumo") ou a taxa na triagem regular.
  - Se houver meios legítimos (acesso institucional, empréstimo entre bibliotecas, contato com autores) para o subconjunto da triagem regular, usá-los.

  A última parte exige decisão do autor.

### 8. grave: o protocolo, os dados e o código não estão acessíveis ao leitor

- **Local:** Informações adicionais (Registro e protocolo; Disponibilidade de dados, código e materiais); 2.1 Protocolo.
- **Problema:** a revisão não foi registrada. Protocolo, emendas, *log* com o sha256, registro de decisões e efeitos extraídos estão num repositório privado, com condições de acesso "[A confirmar pelo autor]". O código em R da análise nem está no repositório ("no ambiente do autor").
  - O item 24b do PRISMA pede onde o protocolo pode ser acessado, e o item 27 pede o que é público e onde (R7.7 e R7.8).
  - O livro pede código que rode do zero e identificador persistente (R7.10 e R7.14; A30 e A36).
  - Toda afirmação de "decidido antes ou depois de ver os dados", que o artigo usa para defender suas escolhas, depende de um protocolo que o leitor não vê, e um sha256 num *log* privado não prova nada a quem está de fora.
- **Correção proposta:** depositar num repositório aberto com DOI (OSF ou Zenodo), sem os PDFs (R7.12):
  - o protocolo congelado no G2, com hash e data;
  - o *log* de emendas;
  - a tabela-fonte da Tabela 2, com a regra caixa-3;
  - os efeitos extraídos, com as conversões;
  - os *scripts* em R (`efeitos.R`, `swim.R`), com as versões, inclusive a do R.

  O que o autor decidir não abrir deve ser declarado item a item (R7.5). Exige decisão do autor.

### 9. grave: os checklists não existem, e o texto diz que existem

- **Local:** 2.1 Protocolo (1º parágrafo); S11.
- **Problema:** a 2.1 diz que "[S11] dá o local de cada item" do PRISMA 2020, do PRISMA-S, do SWiM e do PRISMA-trAIce, mas S11 está "Em preparação". Os checklists com o local de cada item são obrigatórios (R1.3; A11), e são eles que permitem ao leitor e ao editor julgar a completude (R1.4). Sem eles, a conformidade declarada com o PRISMA 2020 não pode ser verificada.
- **Correção proposta:** antes de circular, preencher S11 com a seção de cada item:
  - PRISMA 2020: 27 itens mais os 12 do resumo;
  - PRISMA-S: 16 itens;
  - SWiM: 9 itens;
  - PRISMA-trAIce, só como lista de conferência.

  Até lá, tirar a frase da 2.1. É mudança de texto, sem análise nova.

## Comentários menores

### 10. menor: resumo e *abstract* incompletos frente aos 12 itens

- **Local:** resumo e *abstract*.
- **Problema:**
  - Faltam dois dos 12 itens do PRISMA para resumos: o número de participantes (item 7; nem uma faixa) e as limitações da evidência (item 10: risco de viés, indireção, imprecisão). O campo "Limitações" traz só limitações do processo.
  - O risco de viés alto de todos os estudos de C02 some do resumo e das conclusões (R5.12).
  - O resumo em português dá "IC 95% da proporção, 0,40 a 1,00" sem a proporção, que o *abstract* dá.
  - "Agentes de IA fizeram tudo após o protocolo" não bate com as decisões do autor listadas na 2.9: Emendas 1, 4 e 6b e 17 casos limítrofes.
  - A apuração parcial aparece nos critérios sem a marca de que entrou por emenda decidida depois de ver o estudo brasileiro.
- **Correção proposta:**
  - Em Limitações, acrescentar "risco de viés alto ou algumas preocupações em todos os experimentos; quase todos em laboratório ou vinheta; de 1 a 4 estudos por célula". Acrescentar também a faixa de n.
  - Harmonizar resumo e *abstract*.
  - Trocar por "quase todas as etapas após o protocolo".
  - Os dois textos estão perto de 250 palavras. Para compensar, cortar em Resultados (por exemplo, a frase sobre boca de urna).

### 11. menor: falta justificar a abordagem rápida, e S2 dá "dentro" cedo demais

- **Local:** 2.1 Protocolo (1º e 2º parágrafos); S2.
- **Problema:**
  - Garritty et al. (p-11 e recomendação 24) pedem justificativa forte para a abordagem rápida. "Escolha do autor para cortar etapas" descreve a decisão, mas não a justifica.
  - S2 dá "Dentro" para o prazo de seis meses, mas a revisão não terminou: há 18 pendências.
  - S2 dá "Dentro" também para a recomendação 22 (limitar a certeza à comparação principal e aos desfechos críticos), mas o GRADE foi feito em 18 células e no agrupamento amplo, e a dimensão do alvo foi fixada depois dos dados.
  - Falta em S2 o item sem número "rapid reviews led only by experienced systematic reviewers", que pesa numa revisão conduzida por agentes.
  - A recomendação 1 (usuários do conhecimento) pesa mais do que o texto admite, porque a revisão se dirige a um debate regulatório com atores identificáveis (Congresso, TSE, institutos).
- **Correção proposta:**
  - Dar a justificativa ou dizer que não há outra além do custo.
  - Reclassificar em S2 o prazo como "ainda não se aplica" e a recomendação 22 como "em parte".
  - Acrescentar a linha do revisor experiente.

### 12. menor: as emendas são classificadas de modo diferente no texto e em S3

- **Local:** 2.1 Protocolo (3º parágrafo); 3.6 *Momentum* (1º parágrafo); Informações adicionais (diferenças entre protocolo e revisão); S3.
- **Problema:**
  - **(a) Emenda 4.** A 2.1 diz que "as Emendas 3 e 4 fixaram convenções antes de qualquer análise de efeito", e a 3.6 diz que a célula de *momentum* veio "antes de qualquer análise de efeito". S3, porém, marca a Emenda 4 como "depois de ver os dados" (tipo C), e ela veio depois da extração, com os efeitos já vistos.
  - **(b) Emenda 3.** S3 a classifica como correção de registro "sem nova decisão de método", mas o texto diz que ela registrou a troca do árbitro de risco de viés, feita por custo, o que é decisão de método.
  - **(c) Emenda 2.** Foi decidida pelo coordenador de IA, e S3 não diz isso.
  - **(d) Agrupamento amplo.** A frase "a estrutura de células [...] foram fixadas pela Emenda 5, depois da primeira síntese. Por isso, o agrupamento amplo é só descritivo" não se sustenta. O que veio depois dos dados foi a quinta dimensão (o alvo). O agrupamento amplo é descritivo porque junta o que o protocolo separa (S8). A Tabela 2 também não diz que a dimensão do alvo é *post hoc*.
- **Correção proposta:**
  - Alinhar texto e S3: Emenda 4 depois de ver os dados; troca de árbitro da Emenda 3 como decisão de método; Emenda 2 marcada como decidida por IA.
  - Reescrever a frase do item (d).
  - Dizer na legenda da Tabela 2 que o alvo veio da Emenda 5.

### 13. menor: notas de rebaixamento genéricas e imprecisão julgada de modo desigual

- **Local:** Tabela 2 (notas *a* a *h*); 2.8 Certeza da evidência.
- **Problema:**
  - As notas são genéricas ("poucos estudos, IC da proporção largo ou efeitos frente a ±δ") e se repetem em todas as células. A R4.22 e a R5.45 pedem a justificativa de cada rebaixamento, e o leitor não consegue reconstruir o juízo.
  - Nas células de 1 estudo, a imprecisão foi julgada de modo desigual. C03, C07, C09, C10 e C16, cujo IC conhecido cruza zero, caíram dois níveis (*f*). C04, C11 e C15, sem g nem EP para julgar a precisão, caíram um (*e*). Quem não tem medida de precisão saiu melhor que quem tem IC largo.
  - O limiar de cada juízo não é dito célula a célula (R5.35): zero, para a direção; ±δ, para o nulo de C13.
  - A Tabela 2 reúne 18 linhas numa só tabela. O livro pede no máximo 7 desfechos por tabela e uma tabela por comparação (R5.44 e R5.45), além de uma coluna de população e cenário (R5.43).
  - A meta de C02 foi rodada depois do GRADE, que não considerou o I² de 94%.
- **Correção proposta:**
  - Escrever notas específicas por célula (por exemplo, "1 estudo; g sem EP; precisão não avaliável").
  - Adotar uma regra única para imprecisão sem medida de precisão.
  - Dizer o limiar na 2.8.
  - Dividir a Tabela 2 (apoio e comparecimento, ou por comparação) e acrescentar a coluna de cenário (laboratório, vinheta, eleição real).
  - Rever C02 à luz da meta.

  Nenhum rótulo muda, mas a regra de imprecisão pode mudar juízos. Nessa parte, exige decisão do autor.

### 14. menor: C14 está nas mensagens principais com base num único jogo e com unidade de análise incerta

- **Local:** Tabela 2, linha C14; mensagens principais (2º item); resumo; 3.7 Comparecimento (3º parágrafo).
- **Problema:**
  - C14 tem certeza baixa e vai às mensagens principais com base num único jogo *online* com preferências induzidas.
  - O n é dado em decisões (5.845), não em participantes. Se cada participante toma várias decisões, o EP de 0,023 só vale se o estudo corrigiu pelo agrupamento, e o texto não diz se corrigiu. O rebaixamento de um nível por imprecisão depende disso.
  - A indireção caiu um nível, como nos laboratórios da célula principal, mas aqui não há outro estudo que reduza a dependência de um só desenho induzido.
- **Correção proposta:**
  - Informar o número de participantes e se o EP é robusto ao agrupamento. Se não for, corrigir ou rebaixar a imprecisão.
  - Decidir se uma célula de um só jogo deve estar nas mensagens principais.

  Pode mudar o GRADE. Exige decisão do autor.

### 15. menor: frases de certeza fora do padrão

- **Local:** frases de certeza em todo o texto; resumo em linguagem simples.
- **Problema:**
  - **(a)** Em C13, a frase padrão para certeza moderada com efeito trivial é "provavelmente resulta em pouca ou nenhuma diferença" (R5.36). "Provavelmente não muda [...] além de 2 p.p." passa. "Permite descartar, com certeza moderada" (4.1) não passa.
  - **(b)** Muitas frases de certeza muito baixa embutem a direção ("muito incerta sobre se [...] aumenta o apoio ao líder"). A forma neutra de Santesso et al. é "muito incerta sobre o efeito de X em Y".
  - **(c)** O resumo em linguagem simples abre com "ver uma pesquisa tende a favorecer quem aparece à frente". A frase afirma um efeito que a certeza muito baixa não sustenta e só depois diz que a evidência é muito incerta. O título do mesmo resumo já tem a forma certa.
- **Correção proposta:** padronizar as frases. Trocar "tende a favorecer" por "os experimentos apontaram a favor de quem aparece à frente, mas não se sabe se ver uma pesquisa muda o voto".

### 16. menor: metas exploratórias pouco informativas e com peso demais no texto

- **Local:** 2.7 Síntese (parágrafo das metas); 3.4 Apoio (2º e 4º parágrafos); Figura 6; Tabela 4 (caixa, linha Escala); resumo executivo (4º parágrafo).
- **Problema:**
  - Com 3 estudos, o livro pede os IC de HKSJ e de Wald lado a lado (R5.26). Há só o CHE com RVE, que o próprio texto diz não ser confiável (1,25 e 1,46 graus de liberdade).
  - τ² sai sem IC (R5.29).
  - Na meta *b*, os desfechos se comparam mal: posto num *ranking* de 7, escala de 1 a 7 e proporção de voto. Na meta *a*, dois dos três estudos medem a eleição do grupo, e o outro, o voto individual.
  - Nos *forest plots*, os estudos estão em ordem alfabética (R5.25; A5).
  - Mesmo com as ressalvas, g = 0,48 e 0,62 aparecem no resumo executivo ("estimativas positivas") e na linha Escala da caixa. Sem faixa de magnitude declarada, essa linha não deveria trazer magnitude (R5.52).
- **Correção proposta:**
  - Acrescentar Wald e HKSJ como sensibilidade (análise nova; exige decisão do autor).
  - Ordenar os estudos por precisão ou por risco de viés.
  - Tirar os valores do resumo executivo e da linha Escala. Na Escala, deixar "não estimada; metas exploratórias não informativas (3.4)".

### 17. menor: números e vocabulário do painel da caixa não batem com o artigo

- **Local:** S9 (painel); Tabela 4; 5.1 Caixa de ferramentas (3º parágrafo).
- **Problema:**
  - No painel de S9, a coluna "Estudos" traz números que não batem com o artigo: 2 para pesquisa pré-eleitoral × apoio (o artigo conta 16 estudos em 9 células), 1 para boca de urna × comparecimento (são 3) e 5 para pesquisa pré-eleitoral × comparecimento (são 7).
  - A "Força" usa "fraca" e "insuficiente", enquanto o texto diz que Força é a certeza (R5.48).
  - A certeza "baixa" de pesquisa × comparecimento não corresponde a nenhum corpo GRADE: as células vão de muito baixa a moderada.
  - O rótulo é calculado no nível formato × desfecho × desenho, que junta comparadores que o protocolo separa, e essa agregação não está na regra relatada.
  - Falta avisar o leitor de que o agrupamento amplo de apoio randomizado (9 de 9, p = 0,004) só não recebe "Positivo" por dois motivos: não é unidade de rótulo, e um único juízo de IA o rebaixou por viés de publicação. A frase "nenhuma das decisões em aberto dá a uma célula estudos suficientes para outro rótulo" é verdadeira só para as células.
- **Correção proposta:**
  - Corrigir ou definir a coluna "Estudos".
  - Usar os níveis GRADE na Força.
  - Documentar a regra de agregação do painel e de onde vem a certeza de cada linha.
  - Acrescentar à 5.1 uma frase sobre o agrupamento amplo.

### 18. menor: o recorte de 2010 é justificado pela exposição e aplicado à publicação

- **Local:** 2.2 Critérios de elegibilidade; 3.8 Sensibilidades (4º parágrafo); S8.
- **Problema:**
  - O corte de 2010 é justificado pela mudança do ambiente informacional, que é atributo do momento da exposição, mas foi aplicado ao ano de publicação. Por isso entram eleições e coletas anteriores a 2010 (@Morton2015a, @Chatterjee2019a, @Tyszler2015, @Klor2017a).
  - A sensibilidade "sem dados anteriores a 2010" usa uma regra que o próprio texto chama de inconsistente nos experimentos de laboratório.
  - O intervalo de 2008 a 2009 fica descoberto, apoiado num capítulo (@Hardmeier2008) que não foi lido.
- **Correção proposta:**
  - Ou reescrever a justificativa como critério de publicação (atualizar a literatura), ou definir a sensibilidade pelo ano da coleta, com uma regra só, inclusive para o laboratório.
  - Declarar o intervalo de 2008 a 2009 como limitação da busca.

  A regra da sensibilidade exige decisão do autor.

### 19. menor: falta o método de avaliação do viés por resultados faltantes

- **Local:** 2.7 Síntese; 3.8 Sensibilidades (último parágrafo antes das decisões em aberto).
- **Problema:**
  - Não há parágrafo de métodos para o item 14 do PRISMA (risco de viés por resultados faltantes). O tema só aparece no GRADE e na meta.
  - Em ciência política, muitos experimentos são pré-registrados (AEA RCT Registry, OSF, EGAP). Comparar os registros com o que foi publicado é o jeito direto de achar resultados faltantes. Isso não foi feito nem declarado (PRISMA-S, item 3).
  - O rebaixamento por viés de publicação em C01, C02 e no agrupamento amplo se apoia em "estudos pequenos, todos positivos". Mas foi a lista de efeitos fora da contagem, decidida depois de ver os dados, que tirou o único randomizado contrário (@Gandhi2019).
- **Correção proposta:**
  - Escrever um parágrafo de métodos para o item 14.
  - Buscar nos registros de pré-registro ou declarar que não houve essa busca.
  - Mencionar @Gandhi2019 na justificativa do rebaixamento.

  A busca exige decisão do autor.

### 20. menor: itens de relato incompletos

- **Local:** 3.1 Estudos incluídos (3º parágrafo); S1; 2.3; 2.6; 2.7; 2.9.
- **Problema:**
  - Os estudos excluídos que pareciam elegíveis (Scheuerman 2019, 2020 e 2021; Yosef 2017 e outros) aparecem sem referência. O item 16b do PRISMA pede que sejam citados.
  - As sementes da busca por citação estão só em "arquivos do projeto", que são privados (PRISMA-S, item 5).
  - O *software* de deduplicação não é nomeado (PRISMA-S, item 16).
  - Falta a versão do R, e a do clubSandwich só aparece nas informações adicionais (PRISMA, item 13d).
  - A ROBINS-I V2 é citada sem a data da versão usada (R4.16).
  - Os modelos aparecem pelo nome, sem data de acesso nem parâmetros (PRISMA, itens 8 e 9; RAISE).
- **Correção proposta:** completar cada item e citar os excluídos nas referências ou numa tabela do suplemento.

### 21. menor: a declaração de uso de IA tem lacunas e inconsistências

- **Local:** declaração de uso de IA; 2.9; resumo em linguagem simples; cabeçalhos dos documentos.
- **Problema:**
  - **(a)** O κ de 0,90 e os 58,5% vêm sem IC (R7.22).
  - **(b)** O texto não diz se os termos do provedor foram conferidos antes de enviar a ele PDFs de terceiros (R7.15).
  - **(c)** Falta justificar o uso de IA de ponta a ponta (RAISE, item de justificativa).
  - **(d)** O papel da IA aparece em três graduações: "quase todo o trabalho" (quadro do resumo em linguagem simples), "todo o trabalho depois do protocolo" (limites do mesmo resumo) e "tudo após o protocolo" (resumo). Nenhuma é exata, porque o autor decidiu emendas e 17 casos.
  - **(e)** O artigo tem data de 25/09/2026 e declara uso de IA "entre 19/09/2026 e 25/09/2026" e reescrita "em 24/09/2026 e 25/09/2026". Hoje é 24/09. O suplemento tem data de 24/09.
- **Correção proposta:**
  - Dar os IC e registrar a conferência dos termos.
  - Escrever uma frase de justificativa.
  - Usar uma só formulação: "as etapas depois do protocolo foram conduzidas por agentes de IA, com decisões pontuais do autor".
  - Usar datas que correspondam ao que já tiver sido feito quando o texto circular.

### 22. menor: "célula principal" tem dois sentidos, e as comparações descritivas somam classes de desenho

- **Local:** 3.10 Moderadores (parágrafos do realismo e do número de competidores); 2.7; glossário.
- **Problema:**
  - "Célula principal" nomeia duas coisas diferentes: o alvo principal (13 estudos em seis células e duas classes de desenho) e a célula de pesquisa frente a nenhuma pesquisa (a do δ de 0,0573).
  - As comparações de realismo e de número de competidores somam randomizados com não randomizados ("dos 4 em eleição real, 3 foram *bandwagon*") e comparadores diferentes, o que a regra da revisão proíbe. A Figura 7 separa as classes; o texto, não.
- **Correção proposta:** usar "alvo principal" para a dimensão e o nome da célula para C01. Relatar as contagens de realismo e de competidores por classe de desenho, como na figura.

### 23. menor: a tabela de transferibilidade não traz fonte primária nem juízo por fator

- **Local:** Tabela 5 (transferibilidade); 5.2 Brasil.
- **Problema:**
  - Na linha do voto obrigatório, a coluna "Como é no Brasil" diz que o levantamento de contexto "não tratou deste fator" e se apoia no estudo incluído. O fato é normativo (Constituição, art. 14, §1º) e pede fonte primária, como tiveram a Lei 9.504 e a resolução do TSE.
  - Na confiança nas pesquisas, falta checar se há medida publicada e, se não houver, dizer que não há.
  - A 5.2 diz que a transferibilidade "foi julgada", mas a tabela não traz o juízo por fator (preocupação séria, moderada ou nenhuma), como pede a R6.17.
- **Correção proposta:** citar a norma e acrescentar uma coluna com o juízo explícito de cada fator.
