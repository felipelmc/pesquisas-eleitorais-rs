# Leitura crítica simulada por IA: L2, cientista político

Esta é uma leitura simulada por IA, feita por um subagente `claude-opus-5-5` em 24/09/2026 no papel de cientista político especialista em comportamento eleitoral e efeitos de pesquisas. Não é revisão por pares, não valida nada e não substitui a leitura do autor (P038).

Li `revisao_final.qmd` (com as figuras de `revista/figuras/saida/`), `suplemento.qmd`, `linguagem_simples.qmd` e `insumos/revisoes_anteriores.md`. Consultei também as fichas de extração de Agranov2017a, Farjam2020a, Tal2015a, Tyszler2015, Timotei2013a e Witsman2016a, em `05-decomposicao/fichas/`, só para conferir como o artigo descreve esses estudos. As referências clássicas sugeridas abaixo são de memória e precisam ser conferidas antes de entrar no texto.

## Avaliação geral

O artigo é prudente na linguagem de certeza e transparente sobre o que não foi validado. O contexto brasileiro está bem documentado (STF em 2006, projetos de lei de 2022, Meireles, Pereira e Nunes), e separar a precisão das pesquisas do efeito delas sobre o voto é útil para o debate público.

Para um leitor da ciência política, o problema central é conceitual. A célula principal chama de *bandwagon* toda direção a favor de quem aparece à frente. Em pelo menos três dos oito estudos das duas células que sustentam as mensagens principais, essa direção vem de coordenação estratégica ou de comparecimento diferencial, segundo os próprios autores. Ou seja, vem exatamente do que a definição de Barnfield, adotada na introdução, exclui do *bandwagon*.

Há ainda três problemas de leitura:

- **Validade externa.** Nenhum estudo da célula principal mede o efeito de pesquisa pré-eleitoral sobre o voto numa eleição real, porque Farjam2020a é uma votação experimental sobre doações. A evidência mais próxima de uma campanha real (experimentos de *survey* com partidos reais, nas células de *momentum* e viabilidade) mostra efeitos pequenos, e o texto não explora esse contraste.
- **Comparecimento.** A seção não tem uma teoria do sinal: faltam pivotalidade, efeito Titanic e mobilização de quem está atrás. Sem isso, as células "ver × não ver" ficam sem direção prevista.
- **Brasil.** A seção omite as regras do dia da eleição, que são justamente o que a evidência de boca de urna e de apuração parcial informa. A "lacuna brasileira" precisa ser apresentada como lacuna desta busca.

A frase-síntese sobre regulação tem boa intenção, mas é simétrica de um modo que ignora o ônus da prova. Quase todas as correções são de texto, e as reclassificações exigem decisão do autor. Na minha leitura, os comentários graves 1 a 7 precisam ser resolvidos antes de qualquer divulgação pública, sobretudo a forma como a direção dos achados é nomeada nas mensagens principais e no resumo em linguagem simples.

## Comentários

### Graves

**1. A direção "*bandwagon*" da célula principal mistura *bandwagon*, coordenação estratégica e comparecimento diferencial. (grave)**

*Onde:*
- @sec-como-agiria;
- Mensagens principais, 1º item;
- Resumo e *Abstract*, em Resultados;
- Resumo executivo, 4º parágrafo;
- @sec-apoio;
- @tbl-sof, C01 e C02;
- @sec-mecanismo, parágrafo do voto estratégico;
- @tbl-hipoteses, linha E2;
- @sec-achados;
- Conclusões.

*Problema.* O texto adota Barnfield: o *bandwagon* é a mudança motivada pela popularidade, e o voto estratégico "pode ser confundido" com ele. Mas o alvo do efeito só separa o voto estratégico quando a deserção vai para um segundo colocado viável. Quando a opção viável é o próprio líder, a deserção estratégica cai na célula principal. O próprio modelo lógico diz que o E2 leva "a *bandwagon* ou migração para o segundo colocado competitivo".

Nas duas células das mensagens principais:

- **Tyszler2015**, cujo título é "Information and Strategic Voting". Os autores leem a pesquisa como "coordination device" numa eleição de pluralidade com três opções, e o desfecho é a fração de eleições vencidas pelo candidato majoritário.
- **Witsman2016a.** A autora conclui que os participantes "are indeed voting strategically in a three party election".
- **Agranov2017a.** É um jogo de comparecimento com duas cores e preferências induzidas. O "apoio" (E13, de 74% a 91%) é a taxa de vitória da maioria, que sobe porque, com pesquisa, a maioria vota mais e a minoria menos, como o próprio artigo diz na @sec-mecanismo. É mobilização diferencial e, do lado da minoria, o efeito Titanic, que a @sec-como-agiria diz não ser *bandwagon*. O mesmo experimento também conta na C12, de comparecimento.
- **Tal2015a** mistura o compromisso estratégico pelo segundo preferido com o voto no líder como atalho (*herding*).

O texto mostra a contradição. A @sec-achados diz que o voto estratégico tem "poucos estudos", e a @sec-mecanismo diz que ele é o canal com mais estudos (25) e com os testes mais diretos. Esses testes são Tyszler2015 e Tal2015a, contados como *bandwagon*. Na @tbl-hipoteses, a certeza do E2 é atribuída às células de viabilidade, onde esses testes não estão.

Há ainda um problema de desenho. Nos jogos com preferências induzidas, votar em quem está atrás custa dinheiro e não traz benefício expressivo, então o E5 (simpatia pelo azarão) não tem como operar. Nesses estudos, a ausência de *underdog* é em parte construção do desenho, e não evidência contra o *underdog*.

*Correção.*

(a) Sem mudar célula:
- chamar a direção de "a favor de quem aparece à frente" nas mensagens, nos resumos, na @tbl-sof, na @fig-celulas e nas conclusões, reservando "*bandwagon*" para a teoria;
- dizer uma vez, na @sec-como-agiria e na @sec-apoio, que essa direção é compatível com *bandwagon* (E3 e E4) e com coordenação estratégica (E2), e que a revisão não separa as duas quando o estudo não tem alvo de viabilidade;
- dar, estudo a estudo, o mecanismo que os autores atribuem;
- declarar que o E5 não opera em jogos com preferências induzidas;
- corrigir a contribuição (ii) na @sec-por-que e na @sec-achados, que hoje diz que as células distinguem *bandwagon* de voto estratégico;
- alinhar a linha E2 da @tbl-hipoteses;
- apontar, de forma descritiva, os estudos com dois competidores, em que não há deserção estratégica, como o teste mais limpo de *bandwagon* não estratégico.

(b) Tirar da contagem o efeito de apoio de Agranov2017a, ou levá-lo à mobilização, e mandar Tyszler2015, Tal2015a e Witsman2016a para uma célula de coordenação ou de viabilidade **exige decisão do autor**.

**2. Validade externa: Farjam2020a não é eleição real, e "rareia em eleições reais" lê mais do que os dados dizem. (grave)**

*Onde:*
- Resumo executivo, 4º parágrafo;
- @sec-sensibilidades, 2º parágrafo;
- @sec-moderadores, parágrafo do realismo, e @fig-realismo;
- @tbl-hipoteses, linha R3;
- @tbl-oqf, linha Moderador;
- @sec-achados;
- @sec-revisoes-anteriores, parágrafo de Barnfield.

*Problema.*

(i) **Farjam2020a não é eleição real.** É uma votação *online* em que US$ 200 iam para a organização política real mais votada, sem eleição em curso. A ficha registra "e não numa eleição real". A @tbl-oqf diz que "só um experimento de pesquisa usou eleição real (@Farjam2020a)", e a @sec-moderadores o conta entre "os 4 em eleição real". Corrigido isso, nenhum experimento randomizado da célula principal ocorreu em eleição real. Nenhum estudo da célula principal mede o efeito de pesquisa pré-eleitoral sobre o voto numa eleição real: os três não randomizados em contexto real tratam de informação do dia da votação (boca de urna e apuração parcial).

(ii) **A leitura vai além da contagem.** As frases "a regularidade rareia quando se olha só para eleições reais" e "disso segue que a regularidade *bandwagon* depende dos experimentos de laboratório e com vinheta" não se sustentam. Nos estudos que o artigo classifica como de contexto real, 3 de 4 vão a favor de quem aparece à frente. O que some é o número de estudos e a randomização, e não a direção. A teoria rival do artefato (R3) prevê efeito *maior* em contexto hipotético, e essa é uma previsão de magnitude que a contagem por direção não testa.

(iii) **A evidência mais realista está fora da célula principal.** Os experimentos de *survey* com partidos reais estão nas células de *momentum* e viabilidade:
- Dahlgaard2016a: +3,4 p.p., g = 0,12;
- Meer2015a: g = 0,13;
- Cornejo2023a: g = 0,19;
- Freden2024a: misto.

Os efeitos são pequenos, com IC que cruzam zero. Nos jogos e vinhetas, as diferenças são de 15 a 30 pontos: Agranov2017a, de 74% a 91%; Witsman2016a, de 55% a 86%; Tal2015a, de 70% a 92%. É esse contraste que um cientista político leria primeiro: o artefato inflaria a magnitude, e a direção poderia persistir. Ele não aparece no texto.

(iv) **Realismo e formato se confundem.** No comparecimento, a frase "a direção majoritária muda com o realismo" (R3) mistura realismo com formato de exposição. Os estudos reais de desmobilização são de boca de urna e de proibição, como a própria @sec-comparecimento reconhece.

*Correção.*
- Descrever Farjam2020a como "organizações políticas reais numa votação experimental, sem eleição".
- Trocar "rareia" e "depende" por algo como "em eleições reais, a evidência é escassa, não randomizada e restrita a informação do dia da votação; os poucos estudos não contrariam a direção, mas não distinguem um efeito real menor de um artefato".
- Acrescentar à Discussão o contraste descritivo de magnitude entre experimentos com partidos reais e jogos ou vinhetas, com a ressalva das unidades diferentes.
- Na comparação com Barnfield, dizer que o achado é compatível com a advertência dele, sem confirmá-la.
- Na linha R3, registrar a confusão com o formato.

Reclassificar o realismo de Farjam2020a **exige decisão do autor**, porque muda a @fig-realismo, a sensibilidade "só contexto real" e a @tbl-oqf.

**3. Comparecimento sem teoria do sinal: faltam pivotalidade, efeito Titanic e mobilização de quem está atrás. (grave)**

*Onde:*
- @sec-como-agiria e @fig-modelo-logico;
- @qdr-glossario, linha "Mobilização e desmobilização";
- @sec-comparecimento;
- @tbl-hipoteses, linha E7;
- Mensagens principais, 2º item;
- Resumo executivo, 5º parágrafo;
- Conclusões.

*Problema.* O modelo lógico tem um só canal para o comparecimento, a complacência (E7). Faltam os canais que a literatura de comparecimento usa para prever o sinal:
- a pivotalidade (Downs; Riker e Ordeshook): disputa apertada mobiliza, e disputa folgada desmobiliza;
- o efeito Titanic, em que quem apoia o lado que está atrás desiste. A @sec-como-agiria o cita, mas ele não está no modelo;
- a mobilização de quem está atrás.

Esses canais têm sinais opostos, conforme o que a pesquisa mostra e o lado do eleitor. Como o sinal "positivo = mobilização" soma apoiadores de quem lidera e de quem está atrás, as células "ver × não ver" (C12, C15 e C18) não têm direção prevista: o sinal líquido depende do conteúdo das pesquisas vistas. Chamar a desmobilização de "o efeito indesejado previsto pela teoria", como faz o glossário, é impreciso, porque a teoria prevê os dois sinais.

Isso tem três consequências para a leitura:

- **A C18.** A mensagem "ter visto pesquisas divulgadas pode aumentá-lo" soa como efeito genérico da divulgação. Na verdade, é o efeito líquido de pesquisas específicas em dois contextos europeus. Stolwijk2019b é um painel com exposição autosselecionada, em que o interesse político, confundidor do próprio modelo, move tanto o consumo de notícias de pesquisas quanto o comparecimento. A certeza baixa depende de rebaixar só um nível, decisão ainda pendente.
- **A C13 e a C14.** Gerber2020a (nulo em campo) e Westwood2020a (desmobilização num jogo *online* com preferências induzidas) manipulam a mesma coisa, a proximidade percebida, e aparecem em mensagens separadas. Lidas juntas, o único teste de campo acha efeito abaixo de 2 p.p., e o jogo acha efeito. É o padrão previsto pela teoria rival R3, e o texto não o aponta.
- **A linha E7 da @tbl-hipoteses.** Ela começa por "a disputa apertada, na [direção] de mobilização", com base em interações fora da contagem. Só depois diz que, no desenho mais forte, a crença de proximidade não muda o comparecimento.

*Correção.*
- Na @sec-como-agiria, descrever como teoria os canais de pivotalidade, Titanic e mobilização de quem está atrás, declarando como limitação que o modelo do protocolo não os tem.
- No glossário, trocar "o efeito indesejado previsto pela teoria" por uma definição neutra.
- Nas células "ver × não ver", dizer o que as pesquisas mostravam (disputa apertada ou folgada) e para quem.
- Reescrever a mensagem da C18 como associação observacional em dois contextos europeus.
- Juntar a C13 e a C14 na Discussão e nas mensagens, com a leitura pela R3.
- Na linha E7, começar pelo desenho mais forte.

Separar as células pelo conteúdo da pesquisa ou pelo lado do eleitor, ou mudar o GRADE da C18, **exige decisão do autor**. Tirar a C14 e a C18 das mensagens principais é decisão editorial.

**4. δ de 2 p.p. e "nulo ou trivial" não servem ao contexto brasileiro. (grave)**

*Onde:*
- @qdr-glossario, linha δ;
- @sec-sintese;
- @sec-comparecimento e @tbl-sof, C13;
- Mensagens principais;
- Resumo executivo, 5º parágrafo;
- @sec-brasil.

*Problema.* O artigo diz que δ = 2 p.p. é "convenção do protocolo sem *benchmark* de campo", mas usa o valor para chamar efeitos de "nulos ou triviais". No debate brasileiro, 2 pontos não são triviais: a diferença no segundo turno presidencial de 2022 foi de 1,8 ponto (50,90% a 49,10%).

No comparecimento, 2 p.p. é mais do que se esperaria de um envio de correspondência como o de Gerber2020a. A margem de equivalência, portanto, é folgada perto do que o tratamento poderia produzir. Os IC do próprio estudo, bem mais estreitos, não aparecem em pontos percentuais. "Trivial" é juízo normativo que o protocolo não sustenta, e o leitor tende a entender "nulo ou trivial" como "irrelevante" até para eleições apertadas.

*Correção.*
- Tirar "trivial" de todas as ocorrências, ou dizer "menor que 2 p.p.".
- Relatar em pontos percentuais o IC 95% de Gerber2020a.
- Dizer que efeitos abaixo de δ podem decidir eleições apertadas e que a classificação não diz nada sobre eles.

Mudar o valor de δ **exige decisão do autor**.

**5. A "lacuna brasileira" é, em parte, uma lacuna da busca. (grave)**

*Onde:*
- Resumo executivo, 2º e 6º parágrafos ("Sobre o Brasil, a principal mensagem é a lacuna");
- Mensagens principais, item Brasil;
- @sec-limitacoes-evidencia;
- @sec-brasil;
- @sec-achados, contribuição (iii);
- `linguagem_simples.qmd`.

*Problema.* A afirmação de que nenhum estudo com dados só do Brasil mede o efeito de pesquisas pré-eleitorais vem de uma busca com várias limitações:
- não incluiu a SciELO;
- não teve âncoras em português nem em espanhol;
- usou na BDTD uma estratégia sem termos de comparecimento;
- não folheou periódicos brasileiros da área, como *Opinião Pública*, *Dados*, *RBCS*, *Revista Brasileira de Ciência Política* e *Revista de Sociologia e Política*;
- não cobriu anais da ANPOCS e da ABCP;
- não consultou especialistas;
- não recuperou 342 dos 526 relatos buscados.

O S2 reconhece que a falta da SciELO "pesa mais na seção regional". Mas as mensagens principais apresentam a lacuna sem essa ressalva. Na área, é plausível que existam experimentos de *survey* ou dissertações brasileiras sobre pesquisas e voto útil que essa busca não alcançaria.

*Correção.* Qualificar a lacuna nas mensagens, no resumo executivo, na @sec-brasil e no resumo em linguagem simples, com algo como "nesta busca, que não incluiu a SciELO nem periódicos e anais brasileiros". Uma busca suplementar nessas fontes **exige decisão do autor**, porque é análise nova.

**6. O contexto regulatório omite as regras do dia da eleição, que são o que a evidência de boca de urna e de apuração parcial informa. (grave)**

*Onde:*
- @sec-problema;
- @tbl-transferibilidade, linha "Regulação da divulgação";
- @sec-brasil, 2º parágrafo e parágrafo sobre Araujo2021a;
- uso do termo "boca de urna" em todo o texto.

*Problema.* O texto diz que "não há período de silêncio" e trata a evidência de proibição de boca de urna (França e Índia) como a evidência direta sobre restrição à divulgação. Faltam dois dados, a conferir:

- **Divulgação no dia da eleição.** A Res.-TSE nº 23.600/2019, que o artigo já cita, regula a divulgação de levantamentos feitos no dia da eleição, que só pode ocorrer depois do encerramento da votação. Se isso se confirmar, as proibições estudadas na França e na Índia tratam de uma restrição que o Brasil já tem, e não do embargo pré-eleitoral que o STF derrubou.
- **Horário unificado.** Em 2022, o TSE unificou o horário de votação pelo horário de Brasília. Isso muda a exposição que Araujo2021a estudou em 2018, quando parte do eleitorado ainda votava depois de a apuração oficial começar a ser divulgada. Deve entrar na transferibilidade da C06.

Há ainda um problema de termo. No direito eleitoral brasileiro, "boca de urna" também nomeia o crime de propaganda no dia da eleição (Lei nº 9.504/1997, art. 39, § 5º, II), e o leitor brasileiro pode confundir as duas coisas.

*Correção.*
- Conferir as duas normas e incluí-las na @sec-problema e na linha de regulação da @tbl-transferibilidade.
- Na @sec-brasil, dizer que a evidência de boca de urna informa sobre uma regra que o Brasil já aplica, e que Araujo2021a informa sobre a brecha dessa regra, que é o voto em fila depois da divulgação.
- Usar "pesquisa de boca de urna" na primeira ocorrência e no glossário.

**7. A frase-síntese sobre regulação é simétrica demais e ignora o ônus da prova. (grave)**

*Onde:*
- Mensagens principais, último item;
- Resumo executivo, 6º parágrafo;
- @sec-brasil, 2º parágrafo;
- Conclusões;
- `linguagem_simples.qmd`, seção "O que isso significa?".

*Problema.* "Sozinha, a evidência não sustenta nem a restrição nem a manutenção das regras atuais de divulgação" põe no mesmo plano uma medida que restringe um direito e a regra vigente. A regra vigente foi fixada por decisão constitucional com base no direito à informação, que não depende de prova de efeito. O texto reconhece isso logo depois ("o fundamento de 2006 [...] não depende desta evidência"), mas a frase-síntese diz outra coisa.

Além disso, as "regras atuais" de registro prévio não se baseiam em efeito sobre o voto: elas miram a fraude, o que corresponde ao canal E8. O que a evidência permite dizer é factual e simétrico: ela não mostra que a divulgação muda votos a ponto de justificar restrição, e também não mostra que a divulgação é inócua.

*Correção.* Reescrever a frase nos cinco lugares, por exemplo: "Sozinha, a evidência não demonstra que a divulgação de pesquisas muda votos, nem que é inócua". Acrescentar, na @sec-brasil, que a consequência prática dessa incerteza depende de quem carrega o ônus da prova, que é uma escolha jurídica e normativa, e que o STF o pôs sobre a restrição.

### Menores

**8. A base teórica é estreita para o leitor da área. (menor)**

*Onde:* @sec-como-agiria, @qdr-glossario e @fig-modelo-logico.

*Problema.* O enquadramento repousa só em Barnfield e num modelo lógico rascunhado por IA. Falta a literatura que o leitor da área espera encontrar, e que ajudaria a ler as células:
- Simon (1954), sobre *bandwagon*, *underdog* e a possibilidade de prever eleições;
- Downs (1957) e Riker e Ordeshook (1968), sobre pivotalidade e comparecimento;
- Cox (1997), sobre coordenação estratégica e a regra M+1, inclusive em dois turnos;
- Forsythe, Myerson, Rietz e Weber (1993), o paradigma de laboratório em que a pesquisa serve de dispositivo de coordenação, seguido por Tyszler2015 e Tal2015a e citado por Moy e Rinke;
- Mutz (1998), sobre influência impessoal, heurística de consenso e resposta cognitiva;
- Bartels (1988), sobre *momentum*;
- Noelle-Neumann, sobre a espiral do silêncio, que Timotei2013a invoca.

O modelo também põe só o E2 depois da "percepção de viabilidade". O E3 e o E4, porém, dependem da percepção de popularidade ou de consenso, e só nas disputas de dois candidatos as duas percepções coincidem.

*Correção.*
- Acrescentar essas referências, depois de conferidas, e um parágrafo que ligue cada célula à tipologia de Barnfield: principal como conversão estática, *momentum* como conversão dinâmica, mobilização como mobilização, e viabilidade como voto estratégico. Uma coluna no glossário resolve.
- Esclarecer no texto a diferença entre percepção de popularidade e percepção de viabilidade. Mudar o modelo do protocolo **exige decisão do autor**.

**9. A comparação com as revisões anteriores deixa de fora a única meta-análise conhecida e os achados de *underdog*. (menor)**

*Onde:* @sec-por-que e @sec-revisoes-anteriores.

*Problema.*
- **Hardmeier e Roth (2003).** Pela menção de Moy e Rinke, é a meta-análise anterior, com uma "preponderance of a medium bandwagon effect" e a ressalva de amostra concentrada nos Estados Unidos. É o comparador natural, e o artigo não a cita.
- **Achados de *underdog*.** Moy e Rinke relatam revisões e estudos antigos com *underdog* (Marsh, 1984; Lavrakas, Holley e Miller, 1991). A ausência de *underdog* aqui pode refletir os desenhos (ver o comentário 1), e o texto não discute isso.
- **Contradição.** "Quatro revisões tocam o tema", duas delas depois de 2008, convive com "não achou síntese posterior a 2008".
- **Exagero.** "A primeira síntese" é afirmação forte para uma busca com fontes restritas.
- **Contribuição não explorada.** Barnfield conta que só 10 dos 65 artigos que revisou discutem mobilização. Esta revisão tem 17 estudos com comparecimento, e essa é uma contribuição real que o texto não aproveita.

*Correção.*
- Citar Hardmeier e Roth (2003) pela menção de Moy e Rinke, dizendo que não foi lida.
- Discutir o contraste com os achados antigos de *underdog*.
- Escrever "nenhuma revisão sistemática ou meta-análise dedicada ao efeito" no lugar de "síntese".
- Trocar "a primeira" por "não achamos, na busca descrita".
- Registrar a contribuição sobre o comparecimento.

**10. O recorte de 2010 afeta a comparação com a literatura. (menor)**

*Onde:* @sec-elegibilidade, @sec-limitacoes-processo e @sec-revisoes-anteriores.

*Problema.*
- A "mudança do ambiente informacional" é afirmada, e não argumentada: faltam agregadores, redes sociais e a data de cada mudança.
- "O intervalo desde Hardmeier" não pode ser verificado, porque o capítulo não foi lido.
- O recorte deixa de fora a literatura experimental clássica citada por Barnfield (Fleitas, 1971; Goidel e Shields, 1994; Ansolabehere e Iyengar, 1994). Com isso, a revisão não pode dizer se a evidência posterior a 2010 difere da anterior, que seria o ganho substantivo do recorte.
- Pela justificativa dada, o recorte deveria ser pelo ano dos dados, e não pelo de publicação.

*Correção.* Argumentar a mudança do ambiente informacional ou declarar o recorte como pragmático. Dizer, na @sec-revisoes-anteriores, que a comparação com a literatura anterior a 2010 fica fora do alcance. Mudar o critério **exige decisão do autor**.

**11. "Num país de voto facultativo" é ambíguo na seção sobre o Brasil. (menor)**

*Onde:* @sec-brasil, 1º parágrafo, item (ii).

*Problema.* No parágrafo sobre o Brasil, que tem voto obrigatório, a frase parece falar do Brasil.

*Correção.* Trocar por "num experimento de campo nos Estados Unidos, onde o voto é facultativo".

**12. A transferibilidade precisa de dados brasileiros que estão à mão. (menor)**

*Onde:* @tbl-transferibilidade e @sec-brasil.

*Problema.*

- **Voto obrigatório.** A linha diz que "o levantamento de contexto desta revisão não tratou deste fator". O dado é público:
  - o voto é obrigatório dos 18 aos 70 anos e facultativo para quem tem 16 ou 17 anos, mais de 70 ou é analfabeto (CF, art. 14, § 1º);
  - a abstenção ficou em torno de 20% nas eleições presidenciais recentes (TSE), com multa irrisória.

  Por isso, o canal de desmobilização provavelmente opera na margem, e a hipótese de que "o voto obrigatório elimina o canal" é fraca para o Brasil.
- **Dois turnos.** A coordenação estratégica no primeiro turno, o "voto útil", é central nas campanhas brasileiras. Pela lógica M+1 de Cox, até três candidatos podem ser viáveis no primeiro turno. Os experimentos de viabilidade em pluralidade são um *proxy* ruim para isso. Kiss e Simonovits (2014, *Public Choice*), sobre *bandwagon* em eleições de dois turnos com o resultado do primeiro turno como informação, ajuda aqui, mesmo que fique fora do C2.
- **Confiança nas pesquisas.** Há literatura sobre raciocínio motivado na credibilidade das pesquisas (Kuru, Pasek e Traugott, 2017; Madson e Hillygus, 2020) que sustenta o moderador. Depois dos ataques de 2022, a confiança provavelmente se polarizou por partido.

*Correção.* Preencher a linha do voto obrigatório com a Constituição e os dados de abstenção do TSE. Discutir o voto útil de primeiro turno e M+1. Citar a literatura de credibilidade, depois de conferida, e buscar, se existir, uma medida brasileira de confiança nas pesquisas.

**13. A descrição de Araujo2021a precisa de desfecho, magnitude e mecanismo mais claros. (menor)**

*Onde:* @sec-apoio, @sec-mecanismo e @sec-brasil.

*Problema.*
- **Desfecho.** O leitor não sabe se o +11,76 p.p. é a parcela do candidato em toda a seção ou nos votos dados depois da divulgação. Também não sabe que fração do eleitorado da seção votou depois disso. Sem esses dois dados, a magnitude parece implausível, porque exigiria efeitos individuais enormes.
- **Termo.** "Falhas da identificação biométrica" parece descrever filas causadas pela identificação biométrica, e não falhas.
- **Mecanismo.** O efeito maior no segundo turno, usado para descartar o voto estratégico, também é compatível com mudanças na composição de quem vota tarde.

*Correção.* Conferir no texto do estudo e explicitar o desfecho, a fração de votantes expostos e a ressalva sobre composição.

**14. A ligação dos achados com o debate brasileiro pode ser mais precisa. (menor)**

*Onde:* @sec-problema e @sec-brasil, parágrafo das implicações por ator.

*Problema.*

(a) **Os projetos de lei.** Os PLs de 2022 tratam da precisão das pesquisas. O artigo não diz se as justificativas deles invocam a influência sobre o eleitor, que é a premissa que tornaria a pergunta desta revisão relevante para eles.

(b) **O canal E8.** A divulgação de pesquisas enviesadas é justamente a preocupação brasileira. O único teste (Boukouras2020a: revelar só as pesquisas favoráveis aumentou vitórias mesmo com aviso ao eleitor) não aparece na @sec-brasil, e o registro prévio no PesqEle é uma regra voltada para esse canal.

(c) **A cobertura da imprensa.** A célula de *momentum* trata de como a imprensa enquadra o mesmo resultado (Meer2015a) e da valência da cobertura (Stolwijk2016a). Isso é prática jornalística, e não regulação de pesquisas.

*Correção.*
- Citar as justificativas dos PLs, ou reduzir o peso deles na motivação.
- Levar o E8 e Boukouras2020a à @sec-brasil, com certeza muito baixa.
- Na implicação "para a imprensa", mencionar o enquadramento.

**15. O contrafactual regulatório e o canal das elites. (menor)**

*Onde:* @sec-pesquisa-futura, item (ii), e @sec-limitacoes-evidencia.

*Problema.* "Desenhos com comparador sem pesquisa [...] é esse contraste que responde à pergunta regulatória" é impreciso por dois motivos.

- **O contrafactual do embargo.** Um embargo não produz eleitor sem informação: produz eleitor com pesquisas antigas e outras pistas. O braço "sem pesquisa" dos jogos, em que o participante não sabe nada da distribuição de preferências, não corresponde a nenhuma regra real. Já os PLs sobre precisão correspondem ao contraste "outro resultado de pesquisa".
- **O canal das elites.** O arcabouço de exposição individual não capta o efeito das pesquisas sobre doadores, cobertura, debates, alianças e desistência de candidatos. Uma restrição também agiria por esse canal, e só os estudos agregados de proibição o captam em parte.

*Correção.* Reescrever o item (ii), com o contrafactual de "pesquisa antiga" para embargos e o de "outro resultado" para os PLs sobre precisão. Declarar o canal das elites como limite de aplicabilidade.

**16. Gerber2020a mede a expectativa de proximidade, e não a de quem vence. (menor)**

*Onde:* @sec-mecanismo, 3º parágrafo; @tbl-hipoteses, linhas E1 e R2.

*Problema.* "Só @Gerber2020a testa se a expectativa de quem vence transmite o efeito ao comportamento": o estudo manipula a crença sobre a proximidade da disputa. Para o apoio ao líder, a expectativa que importa é a de quem vence; para o comparecimento, a de proximidade.

*Correção.* Escrever "a crença sobre a proximidade da disputa", deixando claro que a compatibilidade com a R2 vale só para o comparecimento.

**17. Clareza para o leitor da área. (menor)**

*Onde:* Mensagens principais, Resumo, @sec-resultados e @sec-percepcao.

*Problema.*
- O jargão de processo (célula, alvo, fora da contagem, caixa-3, OQF, portões, P0xx, Emenda 5) aparece nos Resultados sem tradução.
- A primeira mensagem principal termina com uma decisão pendente sobre Witsman2016a, que o leitor não tem como avaliar.
- "Dos 41 estudos incluídos (amostras em unidades diferentes)", no Resumo, é opaco.
- O g de Hedges é pouco familiar para desfechos de voto.
- A @sec-percepcao só diz que três dimensões não se aplicam.

*Correção.*
- Tirar das mensagens a frase sobre Witsman2016a, que já está na @sec-apoio.
- Tirar o parêntese do Resumo.
- Dar os pontos percentuais junto do g nos efeitos principais, com a ressalva de que alguns são taxas de vitória de grupo.
- Abrir os Resultados com um parágrafo que traduza os termos internos.
- Levar a @sec-percepcao ao suplemento, deixando uma frase no texto.

**18. O resumo em linguagem simples afirma uma tendência que a certeza não permite. (menor)**

*Onde:* `linguagem_simples.qmd`, título e primeira frase ("ver uma pesquisa tende a favorecer quem aparece à frente") e o parágrafo do comparecimento.

*Problema.*
- "Tende a favorecer" é afirmação causal para uma direção com certeza muito baixa, e parte dela vem de voto estratégico e de comparecimento diferencial (ver o comentário 1).
- É a frase com mais chance de ser citada no debate público.
- "Ter visto pesquisas divulgadas pode aumentar [...] o comparecimento" não diz que vem de dois estudos observacionais na Europa.

*Correção.* Algo como: "Nos experimentos, quem aparecia à frente na pesquisa recebeu mais votos, mas a evidência é muito incerta, e parte desse padrão pode vir de voto estratégico, e não da vontade de acompanhar a maioria". No comparecimento, acrescentar "em dois estudos na Europa, sem sorteio". Ajustar o título na mesma linha.
