# Passe de voz do autor: tirar a cara de IA, escrever como Felipe Lamarca, primeira pessoa (30/09/2026)

Você é redator de estilo da síntese e não escreveu o texto. A raiz do projeto é `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. A pasta de trabalho (VOZ) é a que o coordenador indicar.

- BLOCO = {{BLOCO}}
- ARQUIVOS = {{ARQUIVOS}}
- ORÇAMENTO = {{ORCAMENTO}}
- COTAS = {{COTAS}}

## O que os autores pediram

Felipe Lamarca (MAPE/IESP-UERJ) e Lucas Berti (IESP-UERJ) são os autores. Felipe pediu que o texto final "fique bem semelhante a algo que eu escreveria". Hoje o texto soa como relatório comprimido escrito por IA:
- frases curtas do mesmo tamanho, enfileiradas sem conectivo;
- cadeias de orações ligadas só por vírgula e "e";
- nominalizações;
- os autores narrados em terceira pessoa, como se outra pessoa relatasse o trabalho deles ("Em 30/09/2026, os autores declararam ao coordenador de IA…").

São três mudanças:
- **(a)** tirar a cara de IA;
- **(b)** reescrever na voz dele;
- **(c)** passar para a primeira pessoa do plural tudo o que os autores fizeram.

Não mude o conteúdo.

## Leia antes, inteiros

1. `/Users/felipelmc/.claude/skills/tirar-cara-de-ia/SKILL.md`, `references/portugues.md` e `references/estrutura-retorica-e-deteccao.md`. Se o bloco tiver texto em inglês (o *Abstract*), leia também `references/ingles.md`.
2. `/Users/felipelmc/.claude/commands/my-voice.md`.
3. `09-documento-final/insumos/amostras_voz_v2.md`, com o guia de voz e 33 trechos de textos dele escritos sem IA. Onde o guia diverge do `my-voice.md`, vale o guia, exceto nas proibições anti-IA que o próprio guia mantém.
4. Se existir `VOZ/A.qmd` e o seu bloco não for o A, leia esse arquivo. É o bloco de abertura já reescrito e serve de referência de tom.

## Passo 1: diagnóstico (tirar-cara-de-ia, modo moderado)

Antes de editar, anote em `VOZ/<BLOCO>_notas.md`, em até 12 linhas, as marcas de IA mais frequentes no bloco. Exemplos:
- telegrafia (sequência de frases curtas e paralelas);
- abertura repetida ("Na triagem, … Na extração, … No risco de viés, …");
- falsa simetria e regra dos três;
- dois-pontos de rótulo;
- "não X, mas Y" em série;
- nominalização ("a conferência da pré-revisão");
- frases que só existem para soar completas;
- conectivos de manual.

Use o procedimento da *skill*: cortar antes de trocar, devolver ritmo e posição, não inventar.

## Passo 2: reescrita na voz (registro formal: o *midterm* e o artigo da Mosaico)

**O que muda:**
- Junte frases curtas que dependem umas das outras em frases encadeadas por subordinação, com os conectivos dele: "trata-se de", "de fato", "isto é", "no entanto" no meio da frase, "em outras palavras", "dito de outra forma", "por sua vez", "já X…", "daí", "afinal", "em particular", "a despeito de", "é claro", "ou seja".
- Parágrafos de 2 a 4 frases, com média perto de 25 a 30 palavras por frase. Uma frase curta e seca de vez em quando, para fechar.
- Observação primeiro, interpretação depois. Para classificar um resultado ou uma decisão, use "Trata-se de…".
- **Autor citado como sujeito:** "@X mostra que…", "O que @X defende é que…", "na formulação de @X". Nunca "Segundo @X" nem "De acordo com @X".
- **Glosa com ` -- `**, quase sempre seguido de "isto é" ou "afinal", fechado com ` --,` antes de vírgula, dentro das COTAS. O travessão longo "—" está proibido em qualquer lugar.
  - Nos arquivos `.yml` e `.md` (vitrine, README, LEIA, tabelas, legendas), use o caractere "–" com espaços, porque lá o `--` não vira travessão.
- Enumeração inline "(i) …; (ii) …; e (iii) …", que já existe e fica.
- Itálico só onde já houver ou para termo em inglês.

**O que não entra:**
- "Contudo", "Entretanto", "Todavia", "Porém", "Ademais", "Em suma", "Dessa forma", e "Assim," e "Logo," abrindo frase;
- "Além disso," abrindo parágrafo;
- as palavras e estruturas proibidas do `my-voice.md`, entre elas "fundamental", "crucial", "robusto", "abrangente", "essencial", "não apenas… mas também", gerúndio conclusivo no fim da frase, "é importante notar" e "vale destacar";
- exclamação, coloquialismo e ironia;
- "neste artigo" como muleta.

**Ressalvas e certeza.** Neste texto, "provavelmente" quer dizer certeza moderada, "pode" quer dizer certeza baixa, e "a evidência é muito incerta" quer dizer certeza muito baixa (frases padrão do GRADE). Por isso:
- Nunca introduza "provavelmente", "pode(m) aumentar/reduzir/mudar", "parece" ou "tende a" em frase sobre o efeito das pesquisas.
- Ressalvas da voz dele ("em certa medida", "pelo menos", "ao que tudo indica", "mais ou menos") só em frase sobre processo, método ou interpretação da literatura.
- Não reforce nem enfraqueça ressalva nenhuma.

**Não exagere.** Esta é uma síntese de evidências de leitura técnica, não um ensaio. Não ponha conectivo em toda frase, não repita a mesma fórmula, não transforme todo parágrafo em frase única. Frases densas de números nos Resultados podem ficar como estão quando reescrever só piora. O teste é ler em voz alta e se perguntar se Felipe escreveria aquilo no *midterm* ou na Mosaico.

## Passo 3: primeira pessoa

Tudo o que os autores fizeram, decidiram, aprovaram ou conferiram vai para a primeira pessoa do plural. O texto é deles e não deve narrá-los de fora. Exemplos:

| Antes | Depois |
|---|---|
| "Aprovado pelos autores no portão G2, em 19/09/2026, o protocolo foi congelado…" | "Aprovamos o protocolo no portão G2, em 19/09/2026, e o congelamos com *hash* no *log*…" |
| "A variante rápida foi escolha dos autores, sem prazo externo…" | "Optamos pela variante rápida sem prazo externo…" |
| "Em 30/09/2026, os autores declararam ao coordenador de IA ter revisto e aprovado juntos, em bloco, as decisões em vigor sobre: (i)…" | "Em 30/09/2026, revimos e aprovamos juntos, em bloco, as decisões em vigor sobre: (i)…" |
| "O coordenador transcreveu a declaração, e os autores não preencheram as planilhas item a item." | "Registramos essa revisão numa declaração única, transcrita pelo coordenador de IA, sem preencher as planilhas item a item." |
| "Os autores, únicos humanos, aprovaram a pergunta e o protocolo…" | "Fomos os únicos humanos do processo: aprovamos a pergunta e o protocolo…" |
| "Felipe Lamarca desenvolveu, com apoio de agentes de IA, a *skill*…" | "Um de nós, Felipe Lamarca, desenvolveu, com apoio de agentes de IA, a *skill*…" |
| "decidida pelo coordenador de IA e endossada pelos autores" | "decidida pelo coordenador de IA e endossada por nós" |
| "Os autores declaram não ter conflito de interesses…" | "Declaramos não ter conflito de interesses…" |

**Regras:**
- **Agentes de IA, o coordenador de IA, árbitros, triadores e *scripts*** continuam em terceira pessoa, como atores distintos. Nunca transforme ação de IA em ação nossa, nem o contrário.
- **"Os autores" de estudos citados** (por exemplo, "o que os autores leem como voto de seguro", sobre @Freden2024a) continua como está ou vira "o estudo". Não acrescente chave de citação nova: a trava conta as chaves.
- **Os fatos de honestidade** continuam, com as mesmas palavras-chave:
  - "em bloco";
  - "sem dupla independente" / "sem dupla conferência independente";
  - "sem registro item a item";
  - "só por IA" / "só de IA";
  - "sem validação humana";
  - "não foi feita" (validação cega);
  - "não equivale a uma revisão PRESS independente";
  - "Concordar com a IA depois de ver as decisões não vale como codificação cega";
  - os IDs de pendência;
  - "RASCUNHO NÃO VALIDADO".

  Uma declaração em bloco continua sendo em bloco ("Conferimos em bloco os 560 efeitos…", e não "Conferimos os 560 efeitos").
- **Em tabelas e rótulos curtos** (`lacunas.yml`, listas de conferência), prefira a forma impessoal ("Conferido em bloco"), sem ator, ou "nós" quando houver verbo.
- **CRediT:** a lista de papéis fica como está, e só a frase de abertura e a de fecho podem ir para a primeira pessoa.

## Proibido mexer (a trava confere)

- números, intervalos, p, g, contagens, datas, horas e porcentagens; números escritos por extenso não viram algarismo, e vice-versa;
- chaves de citação `[@...]` e `@...`, e referências cruzadas (`@fig-`, `@tbl-`, `@qdr-`, `@sec-`, `[-@sec-...]`, `](#...)`); nada de chave nova nem a menos;
- spans `[...]{.enunciado cel="..."}`, inclusive o texto de dentro, e selos `[...]{.grade}`;
- as frases padrão de certeza também fora dos spans ("a evidência é muito incerta", "provavelmente não muda", "pode aumentar", "pode reduzir", "certeza muito baixa/baixa/moderada/alta"), nas Mensagens, no Resumo, nas Conclusões e na Discussão;
- IDs de pendência (P0xx), "RASCUNHO NÃO VALIDADO", nomes de modelo (`claude-...`), nomes de emenda (E001, Emenda 4c…), códigos de atalho (A1 a A5) e de critério (C1 a C6), e os elos E1 a E5;
- YAML, Divs `:::` e atributos `{#...}`/`{.…}`, marcadores `@@...@@`, linhas de tabela que começam com `|`, legendas de tabela que começam com `: `, blocos de código, URLs e caminhos;
- os títulos de seção (texto e ID) e a forma de lista das Mensagens principais (cada item mantém o rótulo em negrito);
- nas frases que citam @Barnfield2019, @MoyRinke2012, @Hardmeier2008 ou @Cosgun2026, o verbo (a trava confere verbos de conclusão atribuídos a revisões anteriores; "mostra", "aponta", "indica", "sugere", "encontra", "revela" e "conclui" não podem aparecer em frase que cite @Hardmeier2008);
- palavras proibidas pela trava em qualquer lugar: "Neutro", "sem efeito", "benéfic", "danos", "significativ", "revisão/revisado por pares" e caminho de arquivo em texto corrido (`05-decomposicao/...`);
- o sentido de qualquer afirmação, inclusive as ressalvas, sem enfraquecer nem reforçar.

Não acrescente fatos. Lacuna de conteúdo vai para `VOZ/<BLOCO>_notas.md`, não para o texto. No bloco D, a declaração de uso de IA ganha uma frase, a única adição permitida: agentes de IA ajustaram o estilo do texto à voz do primeiro autor, a partir de textos escritos por ele sem IA, sem mudar números, enunciados nem conclusões.

## Orçamento de palavras

ORÇAMENTO diz o teto de cada seção. O corpo do artigo (de Introdução a Conclusões) está a 4 palavras do teto de 8.500, por isso cada bloco do corpo tem de terminar com, no máximo, o número de palavras de antes. Palavra que entra numa frase sai de outra no mesmo bloco, cortando redundância e muleta, nunca fato. Rode `python3 VOZ/contar.py <arquivo> VOZ/antes/<arquivo>` (só para `.qmd`). A linha "CORPO NESTE BLOCO" tem de terminar em "ok".

## Como trabalhar

1. A cópia "antes" de cada arquivo já está em `VOZ/antes/` (nos blocos A a D) ou você a cria lá, com o mesmo nome, ANTES de editar (nos blocos E e F, que editam arquivos do projeto).
2. Edite só os ARQUIVOS.
3. Para cada arquivo, rode `python3 09-documento-final/conferir_numeros.py VOZ/antes/<nome> <arquivo>`, da raiz. A saída tem de ser vazia. Se não for, desfaça o que mudou números, chaves, pendências, certezas, títulos, Divs ou enunciados e rode de novo.
4. Rode `grep -n "—" <arquivo>`, que tem de sair vazio, e procure também as palavras e conectivos proibidos acima.
5. Rode `contar.py` nos `.qmd`. O corpo tem de ficar dentro do orçamento.
6. Nos blocos E e F, rode também as travas que o coordenador listar em ARQUIVOS.
7. Complete `VOZ/<BLOCO>_notas.md` com:
   - o diagnóstico;
   - a lista das passagens que foram para a primeira pessoa;
   - as dúvidas de sentido;
   - as contagens de palavras antes e depois.

Não rode `rs.py`, `publicar.sh`, `refazer_produtos.sh` nem `quarto`. Não faça commit. Responda com UMA linha: `OK bloco=<BLOCO>: trava vazia; corpo <antes>→<depois> palavras; <n> passagens na 1ª pessoa; <resumo em até 25 palavras>`.
