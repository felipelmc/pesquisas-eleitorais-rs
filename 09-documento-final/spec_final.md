# Especificação do artigo final (versão de entrega, Emenda 7)

Escrita em 30/09/2026 por subagente de IA (`claude-opus-5-5`, papel de arquiteto). É o contrato dos três redatores (seção 4), do coordenador (seção 6) e da verificação. A análise não muda (sentinela na seção 10). Onde esta especificação não diz nada, vale a `spec_v2.md`: seção 0 (notação das fontes de número), seção 4 (enunciados literais das células) e seção 6 (proibições). Deixa de valer tudo o que ela diz sobre aviso de rascunho, callouts, caixa OQF, suplemento, Apêndice A e **[A confirmar pelo autor]**.

**Texto de partida.** `esq:Lnnn` é a linha nnn do esqueleto atual. Antes da redação, o coordenador copia o esqueleto para `_esqueleto_v2_2409.qmd`, com as mesmas linhas. "Sem mudança" quer dizer que o parágrafo fica, apenas com os ajustes da seção 1: nome do produto, remissão aos apêndices e nenhuma pendência no texto.

**Leituras feitas:**

- `CLAUDE.md`, `spec_v2.md`, o esqueleto atual e o do suplemento;
- `montar_suplemento.py`, `montar_revisao_final.py` e `conferir_reestruturacao.py`, com o modo `final` ainda não commitado;
- `revista/rotulos.yml`, `celulas.json`, `numeros_v2.json`, `_revista.yml`, `figuras/legendas.yml` e `tabelas/transferibilidade.yml`;
- `06-analise/certeza.csv`;
- `prompts_v2/prompt_redator_v2.md`;
- `07-relatorio/declaracao_uso_ia.md` e `declaracao_uso_ia_texto.md`;
- `declaracao_ia_v2.md`;
- Emenda 7 e `declaracao_autor_2026-09-30.md`;
- `livro_regras.md`, seções 1 e 7;
- `garritty_2024.md`, seção 4;
- `linguagem_simples.qmd`;
- `ferramentas/publicar.sh` e `juntar_pdf.py`.

## 0. Decisões

- **Tamanho do corpo.** De Introdução a Conclusões, 7.820 palavras de prosa, na faixa de 7.500 a 8.500. Hoje são cerca de 11.000.
- **O que sai do artigo:**
  - o aviso de rascunho, o resumo executivo e os 11 callouts;
  - a seção 3.11 (percepção, implementação e custo);
  - a caixa OQF (5.1 e Tab. 4);
  - a Tab. 5 (transferibilidade), que vira um parágrafo em 5.1;
  - a Fig. 4 (proporção por célula);
  - o Apêndice A de pendências;
  - os links para `suplemento.html` e todo "[A confirmar pelo autor]".
- **O que fica:** as Figs. 1, 2, 3, 5, 6 e 7, renumeradas de 1 a 6; as Tabs. 1, 2 e 3; os Quadros 1 e 2.
- **Apêndices.** Seções A a G, no pipeline do suplemento, com uma tabela nova de lacunas no G. S9, S10 e S11 vão para o pacote de replicação.
- **Redação.** Três blocos: (1) abertura, Introdução e Métodos; (2) Resultados e linguagem simples; (3) da Discussão ao fim, com as Informações adicionais e os apêndices.

## 1. Regras para os redatores

### 1.1 Números

- **Fontes permitidas.** São as da lista branca de `conferir_reestruturacao.py`:
  - os números do v1 (`_revisao_final_v1_oqf.qmd`);
  - as folhas de `07-relatorio/prisma_contagens.json`, `06-analise/swim_*/swim_resumo.json`, `06-analise/meta_*/meta_resumo.json`, `insumos/tabelas/numeros.json`, `revista/celulas.json`, `revista/numeros_v2.json` e `07-relatorio/_pendencias_abertas.json`;
  - os números das justificativas de `06-analise/certeza*.csv`.

  Um número que já está no esqueleto atual, com o mesmo sentido, passou pela trava e pode ser reusado.
- **Nada calculado.** Nenhuma soma, diferença, porcentagem ou contagem nova. Número derivado novo só entra por `revista/gerar_numeros_v2.py`, e quem o cria é o coordenador.
- **Números que não entram:**
  - a partição dos 145 pares da deduplicação (66, 56 e 23);
  - a simulação da deduplicação da Emenda 7 (58, 44, 91, 17, 1.533, 1.050, 521, 337);
  - métricas da declaração do *log* fora da lista branca (2.785 decisões, 117 eventos, estabilidade da triagem, concordância de risco de viés por domínio);
  - a mediana de p0;
  - *hashes*.
- **Anos** só se estiverem no v1, nos `.bib` ou em `incluidos.csv`.
- **Formato.** Negativo com U+2212; intervalo com "a"; vírgula decimal; ponto de milhar.

### 1.2 Enunciados de célula

- Cada uma das 18 células (C01 a C18) tem ao menos um span `[<enunciado>]{.enunciado cel="Cxx"}` com o texto literal de `celulas.json` (lista na `spec_v2.md`, seção 4). O texto não muda em nenhuma vírgula. Todos os spans ficam nos Resultados (Bloco 2), um por parágrafo de célula.
- O parágrafo do span traz "certeza <nível>" (o span já traz) e o k, em algarismo ou por extenso. Em três células o k fica fora do span: C08 ("dois experimentos"), C12 ("três estudos") e C17 ("dois experimentos naturais").
- Fora do span, no mesmo parágrafo:
  - "x de y" só com y = k (ou estudos com direção) e x = contagem de direção da célula. Um subconjunto vai por extenso. "x de y efeitos" é livre.
  - "p = ..." e "IC 95% a a b" que não venham depois de g, EP ou β só com os valores da célula.
  - Nenhuma "certeza <nível>" de outra célula.
- Metas, agrupamento amplo e sensibilidades ficam em parágrafos sem span. O enunciado literal nunca aparece fora de um span.

### 1.3 Figuras, tabelas, quadros, seções e apêndices

- **Marcadores.** Figuras e tabelas só por marcador em linha própria, com linha em branco antes e depois: `@@FIGURA modelo_logico|prisma|rob|direcao|metas|realismo@@` e `@@TABELA caracteristicas|sof|hipoteses@@`. Cada um é chamado no texto por `@fig-`/`@tbl-` antes do marcador ou logo depois.
- **Quadros.** `qdr-glossario` e `qdr-picoc` são escritos pelo redator, como em `esq:L143` e `esq:L192`.
- **Remissão a seções.** `@sec-` só para seção numerada (seção 2.11). Seção sem número vai por link: `[Informações adicionais](#informacoes-adicionais)`.
- **Apêndices.** Só por texto ("Apêndice C"), sem link e sem `@tbl-s...`.
- Nada de `column-*` nem de `../`.

### 1.4 Proibições que a trava reprova

- Termos: "Neutro"; "sem efeito"; "benéfic"; "danos"; "significativ"; "revisão/revisado por pares". No *Abstract*: *significant*, *beneficial*, *harmful*, *no effect*.
- Travessão (U+2014), inclusive como célula vazia (use "nenhuma" ou "n.a.").
- Caminho de arquivo em texto corrido (`06-analise/...`) e nomes internos (`FORA`, `celula_alvo`, `revisor_humano_1`).
- Verbo de conclusão em frase que cita @Hardmeier2008 ("conclui", "mostra", "encontra", "aponta", "indica", "sugere", "revela").
- Modo `final`:
  - nenhum callout "Pendente de revisão humana";
  - nenhum "[A confirmar pelo autor]";
  - nenhuma ocorrência de "suplemento" no artigo;
  - "RASCUNHO NÃO VALIDADO" exatamente uma vez no artigo e nenhuma nos apêndices.

### 1.5 Datas

A trava aceita as datas do v1 e do protocolo, mais 24/09/2026, 25/09/2026, 30/09/2026 e 01/10/2026. Use só estas:

| Data | Para quê |
|---|---|
| 01/01/2010 | corte |
| 19/09/2026 | G1, G2, busca nas bases, checagem de revisões anteriores |
| 20/09/2026 | busca por citação; Emendas 1 e 2 |
| 23/09/2026 | Emendas 3 a 6; pré-revisão PRESS |
| 24/09/2026 | GRADE; consulta aos projetos de lei; versão anterior |
| 30/09/2026 | declaração do autor; Emenda 7 |
| 01/10/2026 | esta versão |

### 1.6 Direção e certeza

- A direção vem do estimador pontual, nunca da significância. Com 4 de 4, p = 0,125, e isso não indica ausência de efeito.
- A certeza qualifica a direção, e não a magnitude. Os verbos são "provavelmente" (moderada), "pode" (baixa) e "a evidência é muito incerta sobre" (muito baixa). No nulo por ±δ: "provavelmente não muda ... além de 2 pontos percentuais".
- Nenhuma recomendação acima da certeza: nada de "deve" nem "recomendamos".
- O g das metas nunca aparece nas Mensagens, no Resumo, no *Abstract* nem nas Conclusões.

### 1.7 Marcas da versão de entrega

- **Nome do produto.** "Síntese sistemática de evidências conduzida com agentes de IA", ou "esta síntese" (regra R7.28 do livro). Nunca "esta revisão" nem "revisão sistemática" para o próprio trabalho. "Revisão" continua valendo para outros trabalhos e para nomes de método ("variante rápida", "diretriz de revisões rápidas").
- **Marca de rascunho.** "RASCUNHO NÃO VALIDADO" só na abertura da declaração de uso de IA (IA-7). A palavra "rascunho" não aparece em nenhum outro lugar do artigo nem dos apêndices. No lugar dela, use "julgado só por IA, sem validação humana" ou "proposto por IA".
- **IDs de pendência.** P0xx só na abertura de IA-7 e na tabela do Apêndice G. No corpo, o texto remete ao Apêndice G.
- **Decisões de julgamento.** Nada de "decisão pendente", "se o autor decidir" nem "o autor ainda não leu". O autor manteve os pontos de julgamento dos efeitos (Emenda 7), e o texto os apresenta como leituras alternativas não adotadas. As escolhas do GRADE aparecem como juízos de IA não validados.
- **Forma.**
  - Sem códigos de regra (R7.28, A13): a trava lê "7.28" como número.
  - Modelos entre crases (`claude-opus-5-5`).
  - "*hash*", e não "SHA256".

### 1.8 Voz e forma

- **Guia.** `/Users/felipelmc/.claude/commands/my-voice.md`.
- **Voz e tempo.** Primeira pessoa do plural, sem atribuir ao autor o que a IA fez. Métodos no passado.
- **Títulos e itálico.** Títulos em caixa de frase. Termos em inglês em itálico.
- **Listas e negrito.** Listas no texto como "(i) ...; e (ii) ...". Negrito só nos rótulos das Mensagens, do Resumo, do *Abstract* e das Informações adicionais.
- **Aberturas proibidas.** Nenhum parágrafo começa com "Além disso", "Portanto", "Assim" ou "Consequentemente".
- **Estudos.** O estudo é nomeado em cada achado.

### 1.9 Orçamento e contagem

- **O que conta.** Só a prosa. Ficam fora tabelas, linhas `:::`, marcadores, legendas e títulos.
- **Tolerância.** ±10% por subseção, com o total de prosa das seções 1 a 6 entre 7.500 e 8.500.
- **Limites duros.** Mensagens até 170 palavras; Resumo e *Abstract* até 250 cada.
- **Contagem.** Este comando conta as palavras por seção:

```bash
python3 - _blocos/bloco2.qmd <<'EOF'
import re, sys
t = re.sub(r"<!--.*?-->", "", open(sys.argv[1], encoding="utf-8").read(), flags=re.S)
cab, n, ordem = None, {}, []
for l in t.split("\n"):
    m = re.match(r"^#+\s+(.*)", l)
    if m:
        cab = m.group(1); ordem.append(cab); n[cab] = 0; continue
    if cab and not re.match(r"^\s*(\||:::|@@|: )", l):
        n[cab] += len(re.findall(r"\S+", re.sub(r"\{[#.][^}]*\}", "", l)))
for k in ordem: print(n[k], k)
print(sum(n.values()), "TOTAL")
EOF
```

### 1.10 Frases canônicas (FC)

Estas frases são usadas nas Mensagens, no Resumo, nas Conclusões e no resumo em linguagem simples, com variação só de concordância. O *Abstract* as traduz com *we are very uncertain whether/about*, *probably* e *may*.

- **FC-apoio.** Nos experimentos, quase todos de laboratório ou vinheta, as estimativas apontaram a favor de quem aparece à frente, mas a evidência é muito incerta sobre o efeito de ver uma pesquisa no apoio ao líder (8 experimentos em duas células, cada uma com certeza muito baixa).
- **FC-apertada.** Receber, por carta, pesquisa que mostra disputa apertada, em vez de folgada, provavelmente não muda o comparecimento além de 2 pontos percentuais para mais ou para menos (1 experimento de campo; certeza moderada).
- **FC-divulgação.** Ter visto a divulgação de pesquisas pode aumentar a intenção de votar ou o comparecimento (2 estudos observacionais na Europa; certeza baixa).
- **FC-projeção.** Ver projeções que mostram probabilidade de vitória mais distante de 50:50 pode reduzir a decisão de votar (1 jogo *online*; certeza baixa).
- **FC-boca.** A evidência sobre a pesquisa de boca de urna divulgada antes do fechamento das urnas é muito incerta.
- **FC-metas.** As duas meta-análises exploratórias, com 3 estudos cada e menos de 4 graus de liberdade, têm intervalos que cruzam zero e não informam o tamanho do efeito.
- **FC-Brasil.** Nesta busca, que não incluiu a SciELO, o único estudo com dados só do Brasil [@Araujo2021a] trata da divulgação oficial da apuração parcial com a votação em curso, e não de pesquisa eleitoral.
- **FC-não-diz.** A evidência não diz de quanto é o efeito das pesquisas sobre o voto, e tampouco permite afirmar que elas não têm efeito.
- **FC-regulação.** Sozinha, a evidência não demonstra que a divulgação de pesquisas muda votos, nem que é inócua.
- **FC-IA.** Agentes de IA conduziram as etapas depois do protocolo. O autor conferiu em bloco a busca, a seleção e a extração, e o risco de viés e a certeza da evidência foram julgados só por IA, sem validação humana.

## 2. Estrutura do artigo

### 2.0 YAML e visão geral

O YAML é o de `esq:L1-28`, com quatro mudanças:

- `subtitle: "Síntese sistemática de evidências, conduzida com agentes de IA, sobre os efeitos *bandwagon* e *underdog* e o comparecimento"`;
- `date: 2026-10-01`;
- a palavra-chave "revisão sistemática rápida" vira "síntese sistemática de evidências";
- o formato `docx` sai.

Afiliação (MAPE/IESP-UERJ, só ali), `estado: final` e a nota de IA vêm de `_revista.yml`. O comentário de `esq:L35` sai.

| Seção (ID) | Palavras | Marcadores | Spans | Bloco |
|---|---|---|---|---|
| Mensagens principais (`mensagens-principais`) | ≤ 170 | – | – | 1 |
| Resumo (`resumo`); *Abstract* (`abstract`) | ≤ 250 cada | – | – | 1 |
| 1.1 O problema e o debate brasileiro (`sec-problema`) | 270 | – | – | 1 |
| 1.2 Como a exposição poderia agir (`sec-como-agiria`) | 290 | Fig. 1, Q1 | – | 1 |
| 1.3 Por que esta síntese (`sec-por-que`) | 140 | – | – | 1 |
| 1.4 Objetivos (`sec-objetivos`) | 120 | – | – | 1 |
| 2.1 Protocolo, tipo de síntese e desvios (`sec-protocolo`) | 230 | – | – | 1 |
| 2.2 Critérios de elegibilidade (`sec-elegibilidade`) | 120 | Q2 | – | 1 |
| 2.3 Fontes e busca (`sec-busca`) | 190 | – | – | 1 |
| 2.4 Seleção dos estudos (`sec-selecao`) | 260 | – | – | 1 |
| 2.5 Extração (`sec-extracao`) | 250 | – | – | 1 |
| 2.6 Risco de viés (`sec-rob-metodos`) | 110 | – | – | 1 |
| 2.7 Métodos de síntese (`sec-sintese`) | 420 | – | – | 1 |
| 2.8 Certeza da evidência (`sec-certeza`) | 140 | – | – | 1 |
| 2.9 Uso de IA e conferência humana (`sec-ia`) | 280 | – | – | 1 |
| 3.1 Estudos incluídos (`sec-incluidos`) | 320 | Fig. 2, Tab. 1 | – | 2 |
| 3.2 Risco de viés nos estudos (`sec-rob`) | 140 | Fig. 3 | – | 2 |
| 3.3 Visão geral da síntese (`sec-efeito`) | 160 | Tab. 2, Fig. 4 | – | 2 |
| 3.4 Apoio a quem aparece à frente (`sec-apoio`) | 780 | Fig. 5 | C01 a C06 | 2 |
| 3.5 Viabilidade e voto estratégico (`sec-viabilidade`) | 180 | – | C07, C08 | 2 |
| 3.6 *Momentum* (`sec-momentum`) | 180 | – | C09 a C11 | 2 |
| 3.7 Comparecimento (`sec-comparecimento`) | 630 | – | C12 a C18 | 2 |
| 3.8 Sensibilidades e viés de relato (`sec-sensibilidades`) | 320 | – | – | 2 |
| 3.9 Mecanismos (`sec-mecanismo`) | 180 | Tab. 3 | – | 2 |
| 3.10 Moderadores (`sec-moderadores`) | 270 | Fig. 6 | – | 2 |
| 4.1 Resumo dos achados (`sec-achados`) | 290 | – | – | 3 |
| 4.2 Relação com revisões anteriores (`sec-revisoes-anteriores`) | 170 | – | – | 3 |
| 4.3 Completude, aplicabilidade e limitações da evidência (`sec-limitacoes-evidencia`) | 240 | – | – | 3 |
| 4.4 Limitações do processo e da síntese (`sec-limitacoes-processo`) | 500 | – | – | 3 |
| 5.1 O que isso significa para o debate brasileiro (`sec-brasil`) | 340 | – | – | 3 |
| 5.2 Implicações para a pesquisa (`sec-pesquisa-futura`) | 130 | – | – | 3 |
| 6 Conclusões (`sec-conclusoes`) | 170 | – | – | 3 |
| Informações adicionais (`informacoes-adicionais`) | cerca de 930 (fora do corpo) | – | – | 3 |

Por seção de nível 1: Introdução 820, Métodos 2.000, Resultados 3.160, Discussão 1.200, "Da evidência à prática: implicações" (`sec-pratica`) 470 e Conclusões 170, somando 7.820. Nenhuma seção de nível 1 tem parágrafo antes da primeira subseção. A ordem no PDF é: Mensagens, Resumo, *Abstract*, seções 1 a 6, Informações adicionais, Referências e, depois, os apêndices.

### 2.1 Abertura (Bloco 1)

- **Mensagens principais** (`::: {.mensagens-principais}` com `# Mensagens principais {#mensagens-principais .unnumbered}`). São 5 itens com rótulo em negrito e selo `[⊕◯◯◯]{.grade}` antes da palavra da certeza:
  - **Apoio ao líder**, a partir de `esq:L46`;
  - **Comparecimento**, a partir de `esq:L47`, com FC-apertada;
  - **Brasil**, a partir de `esq:L48` (não copie o enunciado literal de C06);
  - **O que não se sabe**, com FC-não-diz e FC-regulação;
  - **Como foi feita**, com FC-IA.
- **Resumo** (`::: {.resumo}`). Parte de `esq:L78-92`, com os mesmos subtítulos. Muda:
  - em Métodos, a última frase vira "Agentes de IA conduziram as etapas pós-protocolo; o autor conferiu em bloco busca, seleção e extração";
  - em Resultados, sai "em revisão";
  - Limitações: "De 1 a 4 estudos por célula, quase só de laboratório e vinheta, todos os experimentos com algumas preocupações ou risco alto de viés; risco de viés e certeza julgados só por IA, e triagem sem validação cega; 342 de 526 relatos não recuperados.";
  - as palavras-chave são as do YAML.
- ***Abstract*** (`::: {.resumo lang="en"}`). É a tradução do Resumo, a partir de `esq:L99-113`. Muda:
  - *rapid systematic review* vira *systematic evidence synthesis*;
  - sai *under review*;
  - em *Limitations*: *risk of bias and certainty judged by AI alone; screening without blind validation*.

### 2.2 Introdução (Bloco 1)

- **1.1** (`esq:L121-129`) não muda o conteúdo, só encolhe. A frase da ESOMAR/WAPOR é opcional. "Em 24/09/2026, nenhum dos dois tinha sido votado em plenário" fica.
- **1.2** (`esq:L133-164`):
  - encurte P1 (Barnfield);
  - em P2, a última frase vira "O modelo foi proposto por IA e aprovado pelo autor no portão G2";
  - `@@FIGURA modelo_logico@@` fica depois de P2, e P3 e P4 não mudam.
- **Q1** (glossário):
  - o cabeçalho vira "Como é usado nesta síntese";
  - a linha "Como ler" começa "A síntese não estima...";
  - na linha "Fora da contagem", o link [S7] vira "(Apêndice E)";
  - a linha "Inconclusivo" sai;
  - a legenda vira "Glossário e como ler esta síntese.";
  - a linha do δ (0,044; 0,046; 0,0573) e a linha "Célula" ficam literais.
- **1.3** (`esq:L168-170`):
  - sai a frase sobre a meta-análise de Hardmeier e Roth;
  - a última frase vira "Foi conduzida com agentes de IA, e o risco de viés e a certeza não tiveram validação humana (@sec-ia)."
- **1.4** (`esq:L174-176`): a pergunta literal e as perguntas secundárias. Depois, a resposta adiantada com FC-apoio, FC-apertada e FC-Brasil em forma curta.

### 2.3 Métodos (Bloco 1)

- **2.1** (`esq:L182-186`):
  - O protocolo foi aprovado no G2 em 19/09/2026 e congelado com *hash* no *log*, sem registro. Protocolo e emendas estão no pacote de replicação. Sem registro público anterior à busca, o leitor não confere quando cada decisão foi fixada.
  - Sai "na estrutura OQF". As listas de conferência ficam no pacote de replicação (seção 6, item 5).
  - Os atalhos vão ao Apêndice B.
  - A Emenda 2, decidida pelo coordenador de IA, foi endossada pelo autor, e a Emenda 7 entra entre as decididas depois de ver os dados. A remissão final vai às [Informações adicionais](#informacoes-adicionais) e ao Apêndice B.
- **2.2** (`esq:L190-204`) e o Q2 não mudam.
- **2.3** (`esq:L208-210`):
  - as estratégias ficam no Apêndice A;
  - a deduplicação sai daqui e vai para 2.4;
  - depois da pré-revisão PRESS, entra: "O autor conferiu essa pré-revisão e aceitou a v5 com as lacunas declaradas (Emenda 7), o que não equivale a uma revisão PRESS independente."
- **2.4** (`esq:L220-224`, reescrito):
  - P1 (60): *scripts* removeram duplicados (46 e 4) e relatos anteriores a 2010 (148 e 648). Nos 145 pares candidatos a duplicata, o autor concordou com as sugestões da IA, e as decisões foram gravadas sem aplicação: aplicá-las mudaria contagens do fluxo, e não os incluídos.
  - P2 (100):
    - dois triadores de IA independentes (A = `claude-sonnet-5`; B = `claude-opus-5`), pela regra liberal;
    - as 81 divergências seguiram ao texto completo, e o autor manteve esse estado;
    - concordância de 0,97 (κ 0,90; PABAK 0,94), que mede consistência, e não acurácia;
    - *recall* não calculado, porque as amostras de validação (141) e de elusão (300) não foram codificadas às cegas por humanos;
    - Emenda 6b: 336 registros sem resumo, 156 excluídos e 180 ao texto completo (15 excluídos e 165 não recuperados), com a conferência dispensada pelo autor.
  - P3 (100):
    - um subagente por PDF, com trecho conferido por *script*;
    - 184 relatos avaliados: 165 propostas da IA (47 inclusões e 118 exclusões), conferidas em bloco e mantidas pelo autor; 16 casos limítrofes decididos por ele (8 e 8); 3 exclusões em que a IA estendeu regra dele, endossadas pelo autor (Emenda 7);
    - relatos ligados por estudo;
    - nenhum PDF veio de Sci-Hub ou fonte não autorizada.
- **2.5** (`esq:L234-240`):
  - P1: o autor conferiu o piloto em bloco.
  - P2: depois do limiar, entra "A contingência prevista, redefinir e recodificar, não foi acionada, e o autor resolveu as 259 divergências mantendo o valor original"; "aguardam arbitragem humana" sai.
  - P3: sai "13 promovidos, 5 rebaixados, 6 linhas"; entra "O autor declarou ter conferido os 560 efeitos na página do PDF, em bloco (Emenda 7)".
  - P4: fica, com os efeitos individuais no Apêndice E.
- **2.6** (`esq:L250`): a última frase vira "Nenhum julgamento foi validado por humano, e o autor declarou esta etapa como feita só por IA nesta versão (Emenda 7). Os resultados em risco crítico saíram da análise principal."
- **2.7** (`esq:L254-262`, de 609 para 420 palavras). Itens obrigatórios:
  - a célula e o alvo (Emenda 5);
  - o estimando por classe de desenho (`esq:L256`, literal);
  - o sinal por alvo e as proibições reorientadas;
  - a direção pela estimativa pontual e a regra de 70%;
  - a proporção com Clopper-Pearson e o teste de sinal;
  - o δ convertido em g (0,044; 0,046; 0,0573);
  - o nulo por ±δ e os efeitos fora da contagem (Apêndice E);
  - uma frase só de ressalva do teste de sinal;
  - as metas: CHE, REML, CR2, Satterthwaite e ρ, com a ressalva de que menos de 4 graus de liberdade tornam a inferência robusta não confiável, sem Wald nem HKSJ, e com "R 4.5.2" no lugar do marcador do autor;
  - os moderadores descritivos, as sensibilidades e o viés de publicação dentro do GRADE;
  - a frase final: "Não houve síntese de percepção, implementação ou custo, dimensões que não se aplicam a um fenômeno de informação sem gestor que o implemente."
- **2.8** (`esq:L266`):
  - "rascunhou os juízos" vira "julgou a certeza em 24/09/2026, sem segundo avaliador, e o juízo não foi validado por humano (Emenda 7)";
  - o parágrafo da caixa (`esq:L268`) vira uma frase: "A caixa de ferramentas no formato *O que funciona?*, opcional neste tipo de síntese, não é relatada: com certeza muito baixa em 15 das 18 células e o GRADE não validado, nenhuma célula teria rótulo definido (Emenda 7)."
- **2.9 Uso de IA e conferência humana** (reescrito; fonte: Emenda 7 e declaração do autor):
  - P1 (90), a partir de `esq:L278`: o coordenador `claude-opus-5-5` e os subagentes, com os modelos por etapa nos Métodos e no Apêndice G. O que o autor fez: G1 e G2; as Emendas 1, 4 (4a a 4c) e 6b; os 16 casos limítrofes; a escolha do árbitro por custo. Os portões G3 a G9 foram aprovados em autopiloto. A Emenda 6a, de 23/09/2026, corrigiu atribuições.
  - P2 (110), quase literal: "Em 30/09/2026, o autor declarou ao coordenador de IA ter revisto e aprovado, em bloco, as decisões em vigor sobre: (i) a busca, pela conferência da pré-revisão PRESS feita por IA, que não é uma revisão PRESS independente; (ii) a triagem, com as 81 divergências mantidas no texto completo pela regra liberal; (iii) a elegibilidade, com as 165 propostas da IA e as 3 extensões de regra; (iv) o piloto de extração; (v) os 560 efeitos, contra a página do PDF; (vi) as 259 divergências da recodificação, mantido o valor original; e (vii) o relato. O coordenador transcreveu a declaração, e o autor não preencheu as planilhas item a item. Nenhuma decisão em vigor, dado de efeito ou contagem mudou (Emenda 7)."
  - P3 (80):
    - ficaram só com a IA, e assim são declarados, o risco de viés e a certeza;
    - a validação cega da triagem não foi feita, e a deduplicação foi decidida e não aplicada;
    - agentes redigiram o texto, inclusive a interpretação entre estudos, uso que o livro não admite [@Lamarca2026Livro];
    - pelo mesmo livro, "Nenhum produto desse tipo conta como revisão sistemática", daí o rótulo do título;
    - remissões ao Apêndice G e às Informações adicionais.

### 2.4 Resultados (Bloco 2)

- **3.1** (`esq:L288-298`):
  - `@@FIGURA prisma@@` depois de P1;
  - em P2, as 13 chaves de excluídos que pareciam elegíveis ficam todas (item 16b do PRISMA); o fecho vira "(lista com o critério e quem decidiu no Apêndice C)";
  - P3 cita o Apêndice C, com `@@TABELA caracteristicas@@` depois dele;
  - P4 não muda.
- **3.2** (`esq:L302`): sai "B em 7 e propôs terceiro valor em 2". O caso de @Fichnova2015a (`esq:L309`) entra como fato. O fecho vira "(@fig-rob; domínio a domínio no Apêndice D)", e `@@FIGURA rob@@` vem depois.
- **3.3** (`esq:L314`, `L318`, `L324`):
  - sai a `@fig-celulas`;
  - o agrupamento amplo vai ao Apêndice F, e os efeitos individuais ao Apêndice E;
  - a ordem é P1, `@@TABELA sof@@`, P2 (direção e p = 0,125), `@@FIGURA direcao@@`.
- **3.4** (`esq:L328-346`, na mesma ordem):
  - As metas A e B ficam com cerca de 100 palavras cada: g, IC, p, gl e o IC que cruza zero e ±δ; "τ², I² e intervalo de predição, na `@fig-metas`, não são interpretados"; ρ e ICC numa oração; o *leave-one-out* com o único IC que não cruza zero.
  - A meta B termina com FC-metas, e `@@FIGURA metas@@` vem depois dela.
  - No C02, a frase sobre @Witsman2016a vira "Lido como viabilidade, leitura possível e não adotada, o efeito sairia da célula e da meta".
- **3.5** (`esq:L350-352`): no C08, "a decisão sobre ele está pendente" vira "e o contraste ficou na contagem".
- **3.6** (`esq:L356-362`) não muda.
- **3.7** (`esq:L366-380`):
  - C13: "cai um nível se o autor rebaixar pelo relato seletivo" vira "não foi rebaixada pelo relato seletivo e, com esse rebaixamento, cairia um nível";
  - C16: "o comparador é decisão pendente" vira "o comparador foi codificado como outro resultado";
  - C18: "a decisão ficou com o autor" vira "escolha do julgamento por IA, não validado".
- **3.8** (`esq:L384-392`):
  - P1: "rascunho do GRADE" vira "julgamento de IA", e sai "decisão do autor";
  - P3 fecha com "(Apêndice F)";
  - a lista (i) a (x) vira uma frase: dez leituras alternativas, não adotadas, mudariam a composição de células, sobretudo o alvo de @Witsman2016a e a leitura de coordenação em @Agranov2017a, @Tyszler2015 e @Tal2015a; nenhuma levaria uma célula a 6 estudos numa só direção, o mínimo para p < 0,05.
- **3.9** (`esq:L402-408`):
  - "não conferido" vira "conferido em bloco pelo autor";
  - chame a `@tbl-hipoteses` em P1 e ponha `@@TABELA hipoteses@@` no fim;
  - encurte.
- **3.10** (`esq:L418-430`): quatro parágrafos (regra e veredito; realismo com `@fig-realismo` e o marcador depois; competidores, proximidade e momento; subgrupos e voto obrigatório).

### 2.5 Discussão (Bloco 3)

- **4.1** (`esq:L446-452`): em P3, entra FC-metas; em P4, "todas dependem da validação humana" vira "com a ressalva de que risco de viés e certeza não tiveram validação humana".
- **4.2** (`esq:L456-460`) só encolhe.
- **4.3** (`esq:L464-468`) só encolhe.
- **4.4** (`esq:L472-482`, reescrito com a Emenda 7):
  - **Busca.** A1, A3 e A4, e o fato de o autor ter conferido a pré-revisão PRESS por IA sem revisão independente.
  - **Seleção.**
    - triagem só por IA, sem *recall*;
    - validação cega não feita (concordar depois de ver as decisões não vale como codificação cega);
    - triagem complementar só por IA, com o ator gravado como humano;
    - 342 de 526 relatos não recuperados;
    - deduplicação decidida e não aplicada, que mudaria contagens do fluxo, e não os incluídos.
  - **Extração.**
    - recodificação abaixo do limiar, sem a contingência acionada;
    - divergências resolvidas pelo valor original;
    - reextração e arbitragem pelo mesmo modelo, com 240 das 772 correções estendidas;
    - a conferência dos 560 efeitos foi declarada em bloco e não tem registro item a item que o leitor possa verificar;
    - a direção provável dos erros.
  - **Risco de viés.** Só IA; árbitro do mesmo modelo de A (79 de 88); Emenda 4d substituída pela 6a. Afeta a certeza e a exclusão por risco crítico, e não o sinal.
  - **Síntese.** O que foi decidido depois de ver os dados e o que ficou planejado e não foi feito.
  - **Certeza.** As quatro escolhas de `esq:L480`, (i) a (iv), aparecem como juízos de IA que um avaliador humano pode rever, com as consequências.
  - **Relato.** Agentes redigiram o texto. O autor leu a versão de 24/09/2026, da qual esta deriva sem mudar a análise. Um só provedor; dois defeitos da ferramenta.

### 2.6 Da evidência à prática: implicações (Bloco 3)

- **5.1** (`esq:L502-510` e `transferibilidade.yml`), a seção curta sobre o Brasil que o protocolo pede:
  - P1 (90): o que a evidência permite dizer: FC-apoio curta, FC-apertada em contexto de voto facultativo e FC-Brasil. A precisão das pesquisas não foi examinada.
  - P2 (120): as proibições de boca de urna na França e na Índia, em direções opostas e com certeza muito baixa, e @Lago2015, fora da contagem. Elas correspondem à regra das 17h, e não ao embargo de 2006. @Araujo2021a trata da brecha de 2018. O parágrafo fecha com FC-regulação e o ônus da prova.
  - P3 (130): os quatro fatores do protocolo, em prosa, com os números `n2:transf_*`:
    - voto obrigatório: nenhum dos 11 estudos de comparecimento da síntese o tem codificado;
    - dois turnos: nenhum experimento de viabilidade trata de primeiro turno (@PereiraNunes2024);
    - regulação;
    - confiança nas pesquisas: um estudo.

    Não há segundo rebaixamento. A comparação entre Brasil e América Latina e as outras regiões, pedida pelo protocolo, não é possível (um estudo brasileiro sobre apuração parcial e @Cornejo2023a). Única implicação: se as regras mudarem, desenhá-las para permitir avaliação.
- **5.2** (`esq:L520`) encolhe. A atualização inclui a validação humana de risco de viés e certeza e a codificação cega da triagem.

### 2.7 Conclusões (Bloco 3)

Na ordem: FC-apoio, FC-apertada, FC-divulgação e FC-projeção, FC-boca, FC-não-diz, FC-Brasil e FC-regulação. Última frase: "Risco de viés e certeza foram julgados só por agentes de IA, e a validação humana dessas etapas pode mudar as certezas."

### 2.8 Informações adicionais (Bloco 3)

`# Informações adicionais {#informacoes-adicionais .unnumbered}`, com oito parágrafos, cada um aberto por rótulo em negrito:

- **IA-1 Diferenças entre protocolo e síntese** (200). Parte de `esq:L530`, itens (i) a (ix). O item (iv) passa a dizer "endossada pelo autor". Entra o item (x): Emenda 7, de 30/09/2026, decidida depois do G9 e de ver os dados. Ela:
  - registra a conferência em bloco;
  - declara como não validados o risco de viés, o GRADE e a validação cega;
  - adota o rótulo de síntese;
  - deixa a marca de rascunho só na declaração de IA, desvio parcial da seção 10 do protocolo;
  - tira a caixa;
  - transforma o suplemento em apêndices;
  - publica o pacote.

  Nenhum dado, decisão em vigor ou contagem mudou. A tabela está no Apêndice B.
- **IA-2 Registro e protocolo**: não registrada, por decisão do autor em 19/09/2026. O protocolo foi aprovado no G2 em 19/09/2026 e congelado com *hash* no *log*. Protocolo e emendas estão no pacote.
- **IA-3 Financiamento**: "Esta síntese não recebeu financiamento específico."
- **IA-4 Conflitos de interesse**: "O autor declara não ter conflito de interesses nem relação com a Anthropic, provedora dos modelos de IA usados."
- **IA-5 CRediT**: Felipe Lamarca em conceituação, curadoria de dados, análise formal, investigação, metodologia, administração do projeto, recursos, *software*, supervisão, validação, visualização, escrita (primeira redação) e escrita (revisão e edição). Obtenção de financiamento: não se aplica. Depois vem a frase: "Agentes de IA executaram, sob supervisão do autor, parte dessas tarefas, entre elas a primeira redação do texto, e não são autores."
- **IA-6 Disponibilidade** (200), com os itens (i) a (v):
  - (i) Públicos, na página do projeto (<https://felipelamarca.com/pesquisas-eleitorais-rs/>): este artigo com os apêndices, em PDF e HTML; o resumo em linguagem simples; a página interativa.
  - (ii) Público, no pacote de replicação (<https://felipelamarca.com/pesquisas-eleitorais-rs/pacote-replicacao.zip>), com licença MIT para o código e CC BY 4.0 para textos e dados, sem resumos nem e-mails de terceiros. O conteúdo segue o manifesto de `ferramentas/montar_pacote.py`:
    - protocolo, emendas, pergunta, teoria do programa e *codebooks*;
    - estratégias de busca ativas, registro das buscas e conferência do PRESS;
    - registros só com metadados bibliográficos;
    - decisões de deduplicação, de triagem e de texto completo;
    - contagens do PRISMA;
    - fichamento e efeitos extraídos;
    - risco de viés;
    - entradas, saídas e *scripts* da síntese;
    - a declaração de IA gerada do *log*, a tabela de agentes, a declaração do autor e as pendências abertas;
    - listas de conferência;
    - uma cópia da ferramenta de revisão (os *scripts* que rodam a síntese);
    - um manifesto com o *hash* de cada arquivo.
  - (iii) O que se reproduz. Com o pacote, refaz-se a síntese a partir dos efeitos extraídos (conversões, células, testes de sinal, metas, figuras e tabelas), com R 4.5.2, metafor 5.0.1, clubSandwich 0.7.0, Quarto 1.9.35 e Typst 0.14.2. Extração, elegibilidade e risco de viés dependem dos textos completos, que não são redistribuídos, e o pacote traz os identificadores para obtê-los.
  - (iv) Privados, no repositório GitHub `felipelmc/pesquisas-eleitorais-rs`, com acesso sob pedido ao autor: os *prompts* dos agentes, as fichas com trechos, os pacotes de revisão humana e o *log* completo.
  - (v) Não há identificador persistente.
- **IA-7 Declaração de uso de inteligência artificial** (280). O rótulo fica numa linha. O parágrafo seguinte começa literalmente assim: "**RASCUNHO NÃO VALIDADO.** Ficaram sem validação humana: (i) o risco de viés e a certeza da evidência, julgados só por agentes de IA (P033, P035, P036 e P042); (ii) a validação cega da triagem, que não foi feita (P006, P007 e P008); e (iii) a deduplicação, decidida pelo autor e não aplicada (P019)." Depois, em prosa:
  - **Ferramentas.** Modelos da Anthropic, pelo Claude Code, entre 19/09/2026 e 01/10/2026. O coordenador foi `claude-opus-5-5`, e os subagentes, `claude-sonnet-5`, `claude-opus-5` e `claude-opus-5-5`. O *log* não registra o modelo do coordenador.
  - **Finalidade.** A IA decidiu a triagem e a triagem complementar. Propôs a elegibilidade, a extração e as correções dos efeitos. Julgou o risco de viés e a certeza. Redigiu este texto, com a interpretação entre estudos, e o resumo em linguagem simples.
  - **Justificativa.** Foi escolha do autor, para a variante rápida, com um só revisor humano.
  - **Validação.** Só com métricas já na lista branca:
    - triagem: 0,97 (κ 0,90; PABAK 0,94), sem IC, e *recall* não calculado;
    - recodificação: 58,5%, abaixo do limiar;
    - risco de viés: o árbitro seguiu o avaliador A em 79 de 88 domínios;
    - conferência do autor em bloco (@sec-ia).

    A concordância entre agentes mede consistência, e não acurácia.
  - **Interesses.** Nenhum conflito. Custo de acesso e termos de retenção dos dados não registrados.
  - **Limitações.** Um só provedor; árbitro do mesmo modelo; versões de modelo que mudam.
  - **Responsabilidade.** É humana, inclusive pela decisão de usar IA. A declaração completa, gerada do *log*, está no pacote, e o quadro por etapa, no Apêndice G.
- **IA-8 Versão e citação**: "Versão de entrega de 01/10/2026. Reescreve a de 24/09/2026 como artigo único com apêndices, sem mudar células, contagens, certezas nem metas. Como citar: Lamarca, Felipe. 2026. *Pesquisas eleitorais publicadas mudam o voto? Síntese sistemática de evidências, conduzida com agentes de IA, sobre os efeitos* bandwagon *e* underdog *e o comparecimento*. Documento de trabalho, versão de 01/10/2026. <https://felipelamarca.com/pesquisas-eleitorais-rs/>."

Depois vêm `# Referências {#referencias .unnumbered}` e `::: {#refs}` / `:::`. A lista cobre também as chaves dos apêndices, que não têm lista própria.

### 2.9 Figuras e tabelas: o que fica e por quê

- **Ficam:**
  - Fig. 1 (modelo lógico): põe a teoria antes da evidência e poupa cerca de 110 palavras em 1.2.
  - Figs. 2 e 3 (PRISMA e risco de viés): obrigatórias.
  - Fig. 5 (direção), que vira Fig. 4: obrigatória.
  - Fig. 6 (metas), que vira Fig. 5: é o único lugar com os efeitos de estudo e seus IC nas duas maiores células. A legenda leva τ², o intervalo de predição, os gl e a ressalva de gl < 4, o que poupa cerca de 80 palavras em 3.4.
  - Fig. 7 (realismo), que vira Fig. 6: sustenta a ressalva central (a regularidade repousa em laboratório e vinheta) e poupa cerca de 120 palavras em 3.10.
  - Tabs. 1 e 2: obrigatórias.
  - Tab. 3 (hipóteses): responde à pergunta secundária de mecanismos e deixa 3.9 e 3.10 em 450 palavras, contra 900 hoje.
- **Saem:**
  - Fig. 4: repete a Tab. 2 e a figura de direção.
  - Tab. 4 (caixa): Emenda 7c.
  - Tab. 5: os quatro fatores cabem em 130 palavras. A legenda deixava o juízo de preocupação com o autor, e esta versão não faz esse juízo.

### 2.10 O que sai do texto atual

- `esq:L35-41` e `esq:L53-73`.
- Os 11 callouts: `esq:L53`, `L212`, `L226`, `L242`, `L270`, `L306`, `L394`, `L410`, `L432`, `L494` e `L512`.
- `esq:L268`, `L318`, `L320`, `L438-440`, `L486-498`, `L508`, `L546` e `L553-557`.
- Todo `suplemento.html#`, "S1" a "S11", "relatório técnico", "18 pendências", "rascunho", "[A confirmar pelo autor]", "decisão pendente" e "o autor ainda não leu".

### 2.11 Contrato de rótulos (`revista/rotulos.yml`, coordenador)

- **Figuras.** Sai `celulas`.
- **Tabelas.** Saem `oqf_principal`, `transferibilidade` e `pendencias`.
- **Seções.** Saem `sec-percepcao` e `sec-caixa`, e as outras 35 ficam.
- **Âncoras.** Saem `resumo-executivo` e `sec-pendencias`.
- **Chave `suplemento`.** Mantém o nome, porque a trava e o montador a leem, e passa a listar `ap-a-busca`, `ap-b-emendas`, `ap-c-estudos`, `ap-d-rob`, `ap-e-efeitos`, `ap-f-sensibilidades` e `ap-g-ia`.

## 3. Apêndices (Bloco 3; `_esqueleto_suplemento.qmd` reescrito)

### 3.1 YAML e convenções

```yaml
---
title: "Apêndices"
subtitle: "Pesquisas eleitorais publicadas mudam o voto? Síntese sistemática de evidências, conduzida com agentes de IA, sobre os efeitos *bandwagon* e *underdog* e o comparecimento"
date: 2026-10-01
keywords: [pesquisas eleitorais, apêndices, síntese sistemática de evidências]
paisagem: true
suppress-bibliography: true
metadata-files: [revista/_revista.yml]
bibliography: revista/referencias.json
number-sections: false
format:
  typst:
    number-sections: false
---
```

- Saem o callout de rascunho e as Referências. As chaves citadas nos apêndices já entram no `nocite` comum (`montar_revisao_final.chaves_apendices`).
- Títulos: `# Apêndice X. Título {#ap-x-... .unnumbered}`, com subseções `## Título {.unnumbered}`.
- Tabelas numeradas por apêndice (A1, B1, ...), para não colidir com as Tabelas 1 a 3 do artigo.
- Sem P0xx fora da tabela de lacunas, sem "suplemento" e sem "rascunho".

### 3.2 Seções

- **Apêndice A. Estratégias de busca** `{#ap-a-busca}`: o texto de S1. As sementes da busca por citação ficam no repositório do projeto (o pacote leva só as estratégias ativas e o registro das buscas). Marcador `@@TABELA s1_busca@@`.
- **Apêndice B. Atalhos da variante rápida e emendas ao protocolo** `{#ap-b-emendas}`:
  - `## Atalhos da variante rápida`: o texto de S2. "O cruzamento é julgamento de IA, não conferido por humano" vira "O cruzamento é julgamento de IA, lido pelo autor na conferência do relato (Emenda 7)". A frase do prazo de seis meses sai. Marcador `@@TABELA s2_atalhos@@`.
  - `## Emendas e desvios do protocolo`: o texto de S3, com uma ressalva a mais: "a Emenda 7 registra a conferência em bloco do autor e as etapas sem validação humana, sem mudar dados, decisões em vigor nem contagens". Marcador `@@TABELA s3_emendas@@`.
- **Apêndice C. Estudos incluídos e excluídos** `{#ap-c-estudos}`: o texto de S4, com "quem propôs e quem decidiu" na segunda tabela. Marcador `@@TABELA s4_caracteristicas@@`.
- **Apêndice D. Risco de viés por domínio** `{#ap-d-rob}`: "Todos são rascunho de IA" vira "Foram feitos só por agentes de IA (dois avaliadores independentes e um árbitro nos desacordos), sem validação humana (Apêndice G)". Marcador `@@TABELA s5_rob@@`.
- **Apêndice E. Efeitos principais e efeitos fora da contagem** `{#ap-e-efeitos}`: `## Efeitos principais por estudo`, com o texto de S6 e o marcador `@@TABELA s6_efeitos@@`, e `## Efeitos fora da contagem`, com o texto de S7 e o marcador `@@TABELA s7_fora@@`.
- **Apêndice F. Agrupamento amplo e análises de sensibilidade** `{#ap-f-sensibilidades}`: o texto de S8. Marcador `@@TABELA s8_sensibilidades@@`.
- **Apêndice G. Uso de IA e lacunas de validação humana** `{#ap-g-ia}`:
  - Três frases de introdução: por etapa, quem executou, a concordância entre agentes, a conferência humana e a pendência aberta. "Em bloco" é a declaração de 30/09/2026, transcrita pelo coordenador, sem registro item a item. A declaração completa, gerada do *log*, está no pacote.
  - Marcador `@@TABELA lacunas@@`.
  - Parágrafo "Agentes desta versão", descrito abaixo.

### 3.3 Tabela de lacunas (`revista/tabelas/lacunas.yml`, Bloco 3)

O formato é o que a função `lacunas()`, já escrita em `montar_suplemento.py`, lê:

- `colunas`: `[Etapa, Quem executou (modelo), Concordância entre agentes de IA, Conferência humana, Pendência aberta]`;
- `larguras`: `[13, 23, 23, 29, 12]`;
- `legenda`: o texto abaixo;
- `linhas`: uma lista de cinco células por linha, sem marcadores.

A função grava a legenda numa linha só, com `{#tbl-lacunas}`.

Legenda: "Uso de IA e conferência humana por etapa da síntese. Em bloco pelo autor: em 30/09/2026, o autor declarou ter revisto a etapa e concordado com as decisões em vigor, sem registrar a conferência item a item; a declaração foi transcrita pelo coordenador de IA (Emenda 7). A concordância entre agentes de IA mede consistência, e não acurácia, e não vale como validação. Pendência aberta: tarefa de validação humana registrada e não concluída."

| Etapa | Quem executou (modelo) | Concordância entre agentes de IA | Conferência humana | Pendência aberta |
|---|---|---|---|---|
| Busca | Coordenador de IA (`claude-opus-5-5`); âncoras por subagente isolado; pré-revisão PRESS da estratégia ativa por `claude-opus-5-5` | Não se aplica (um agente por tarefa). *Recall* das âncoras de 19 de 19 na versão final da estratégia em inglês, não independente | Em bloco pelo autor: conferência da pré-revisão PRESS por IA, com as lacunas declaradas; não é revisão PRESS independente | nenhuma |
| Deduplicação | *Script* da ferramenta de revisão (46 e 4 duplicatas removidas); sugestão por agente de IA nos 145 pares incertos | Não se aplica | Em bloco pelo autor: concordou com as sugestões da IA nos 145 pares (fundir, rejeitar ou ligar); decisões gravadas e não aplicadas; aplicá-las não mudaria os estudos incluídos | P019 |
| Triagem de títulos e resumos | `claude-sonnet-5` (A) e `claude-opus-5` (B), independentes, pela regra liberal; na triagem complementar dos 336 registros sem resumo (Emenda 6b), `claude-sonnet-5` (A) e `claude-opus-5-5` (B) | A × B na primeira onda: 0,97 (κ 0,90; PABAK 0,94), sem IC; *recall* não calculado | Em bloco pelo autor: 81 divergências mantidas no texto completo pela regra liberal. Validação cega não realizada (amostras de 141 e 300 registros). Triagem complementar: conferência dispensada pelo autor | P006, P007, P008 |
| Elegibilidade no texto completo | Um subagente por PDF (`claude-opus-5`; `claude-opus-5-5` depois da Emenda 6b), com trecho conferido por *script* | Sem dupla nem medida de concordância | Em bloco pelo autor: 165 propostas mantidas e 3 extensões de regra endossadas; item a item nos 16 casos limítrofes, decididos por ele | nenhuma |
| Extração e efeitos | Um subagente `claude-opus-5` por texto, depois de um piloto de 3 estudos; reextração cega e arbitragem dos efeitos principais por `claude-opus-5-5` | Nos 56 efeitos principais de então, 15 concordaram, 23 tinham o mesmo valor com outra classificação, 12 outro valor e 6 outro sinal; 772 correções, 240 estendidas sem nova arbitragem | Em bloco pelo autor: os 560 efeitos, conferidos na página do PDF, e o piloto, mantidos | nenhuma |
| Recodificação cega da extração | `claude-sonnet-5`, em 10 estudos sorteados | 58,5% em 560 comparações; 37 variáveis abaixo do limiar (κ ou PABAK de pelo menos 0,7 e 80%); contingência não acionada | Em bloco pelo autor: 259 divergências resolvidas com o valor original | nenhuma |
| Risco de viés | Avaliadores `claude-opus-5-5` (A) e `claude-sonnet-5` (B), independentes; árbitro `claude-opus-5-5`, escolhido pelo autor por custo | Consenso automático em 171 dos 259 domínios; nos 88 arbitrados, o árbitro seguiu A em 79 | Não realizada | P033 |
| Certeza da evidência (GRADE) | Um subagente `claude-opus-5-5`, sem segundo avaliador | Não se aplica (um só avaliador) | Não realizada | P035, P036, P042 |
| Relato | Subagentes `claude-opus-5-5` e `claude-sonnet-5`, com números conferidos por programa | Não se aplica; verificação e leituras críticas por IA não validam o conteúdo | Em bloco pelo autor, na versão de 24/09/2026 (declaração de 30/09/2026); esta versão a reescreve sem mudar a análise | nenhuma |

A trava exige na tabela exatamente as pendências abertas, menos a P038: P006, P007, P008, P019, P033, P035, P036 e P042. Nenhum outro ID entra. Se a P038 for fechada com a aprovação do autor a esta versão, a conferência do Relato passa a "Em bloco pelo autor, nesta versão".

**Agentes desta versão** (cerca de 100 palavras, depois da tabela). O parágrafo diz cinco coisas:

- a declaração do *log* não registra os agentes que prepararam o texto, porque eles não rodaram comandos da ferramenta de revisão;
- a versão de 24/09/2026 foi preparada por agentes coordenados por `claude-opus-5-5`, quase todos `claude-opus-5-5`, com `claude-sonnet-5` nas referências de método e na revisão visual;
- esta versão a reescreve, sem mudar a análise, com arquiteto, três redatores, verificação e passes de estilo (o coordenador ajusta ao que rodou);
- nenhum desses agentes leu PDF de estudo incluído nem fez análise nova;
- a tabela com *prompt*, papel, modelo e início do *hash* está no pacote.

### 3.4 Legendas e células que ficariam falsas (o coordenador corrige no código)

Em `montar_suplemento.py`:

- **Legenda de `tbl-s2-atalhos`.** "Julgamento de IA, não conferido por humano." vira "Julgamento de IA, lido pelo autor na conferência do relato (Emenda 7)."
- **Células de S2 vindas de `garritty_2024.md`.** Troque no montador, sem editar o insumo:
  - "Ficaram 165 decisões propostas sem conferência humana." vira "As 165 decisões propostas foram conferidas em bloco e mantidas pelo autor (Emenda 7)."
  - Linha "Extração: 11": "Dentro na forma; sem humano" vira "Dentro na forma", e "A conferência humana do piloto está pendente." vira "O autor conferiu o piloto em bloco e o manteve (Emenda 7)."
  - Linha "Extração: 12": "Fora" vira "Dentro, com ressalva", e "Nenhum dos 560 efeitos foi conferido por humano na página do PDF." vira "O autor declarou ter conferido os 560 efeitos na página do PDF, em bloco (Emenda 7)."
  - Linha "Certeza: 21": "Dentro, como rascunho" vira "Dentro, julgado só por IA".
  - Linha "Certeza: 23": a célula vira "Um só agente de IA julgou, sem segundo verificador nem validação humana."
  - Linha A4, recomendação 6: acrescente "O autor conferiu essa pré-revisão (Emenda 7), o que não equivale a revisão independente."
  - Consequências de A2: "**Texto completo:** exclusões erradas não são detectadas." vira "**Texto completo:** exclusões erradas só seriam vistas na conferência do autor, feita em bloco."
- **`s4_caracteristicas`.** "rascunho de IA não validado" vira "julgado só por IA, sem validação humana".
- **`s4_excluidos`.**
  - Legenda: "(...) aguardam conferência humana (P041)." vira "As exclusões propostas pela IA foram conferidas em bloco e mantidas pelo autor (Emenda 7)."
  - Coluna: "Quem decidiu" vira "Quem propôs e quem decidiu".
  - Valores: "IA, conferida em bloco pelo autor"; "IA, estendendo regra do autor, endossada por ele"; "autor (caso limítrofe)".
- **`s6_efeitos`.** "Nenhum efeito foi conferido por humano na página do texto (P039)." vira "Os 560 efeitos extraídos, estes entre eles, foram conferidos pelo autor na página do texto, em bloco (Emenda 7)."
- **`tbl-s8-sof-amplo`.** "(GRADE, rascunho de IA não validado)" vira "(GRADE julgado só por IA, sem validação humana)".
- **`s9_caixa`, `s10_regional`, `s11_checklists` e `declaracao_ia_v2()`.** Saem do esqueleto dos apêndices, mas as funções podem ficar. Se forem reusados no pacote, corrija "(P042)", "(P038)", "neste suplemento" e "no relatório técnico".

No artigo:

- **`legendas.yml`, `modelo_logico`.** "O modelo é um rascunho de IA aprovado no G2" vira "O modelo foi proposto por IA e aprovado pelo autor no G2".
- **`legendas.yml`, `prisma`.**
  - "(...) assim como a avaliação dos textos completos, exceto 16 casos limítrofes decididos pelo autor (8 inclusões e 8 exclusões)" vira "Os textos completos foram avaliados por agentes de IA, com conferência em bloco do autor, que decidiu 16 casos limítrofes (8 inclusões e 8 exclusões)".
  - O trecho de "O fluxo ainda é rascunho." até "[Apêndice A](#sec-pendencias)." vira "Os 145 pares candidatos a duplicata foram revistos pelo autor, e as decisões não foram aplicadas: aplicá-las mudaria contagens deste fluxo, e não os estudos incluídos (Apêndice G)."
- **`legendas.yml`, `celulas`.** Sai.
- **`montar_revisao_final.py`.**
  - `t_caracteristicas`: "Tabela estudo a estudo no suplemento, S4 e S5." vira "Estudo a estudo nos Apêndices C e D."
  - `t_sof`: "e é rascunho de IA não validado" vira "e foi julgada só por IA, sem validação humana", e "(suplemento, S8)" vira "(Apêndice F)".
  - `t_hipoteses`: "fichamento por IA, não conferido por humano" vira "fichamento por IA, conferido em bloco pelo autor (Emenda 7)".

## 4. Divisão em três blocos

Cada redator escreve só `09-documento-final/_blocos/blocoN.qmd`. O Bloco 2 escreve também `linguagem_simples.qmd`, e o Bloco 3, `_esqueleto_suplemento.qmd` e `revista/tabelas/lacunas.yml`. O coordenador junta 1 + 2 + 3 em `_esqueleto_revisao_final.qmd`, monta e roda a trava. Os redatores:

- não rodam `rs.py`;
- não abrem PDF;
- não mexem em código, figuras, `rotulos.yml` nem `numeros_v2.json`;
- entregam a contagem da seção 1.9.

A remissão entre blocos é feita só pelos IDs da seção 2.11. Cada achado usa a frase canônica da seção 1.10.

| Bloco | Fronteiras | Prosa | Lê, além desta especificação e de `my-voice.md` |
|---|---|---|---|
| 1 | Do YAML até o fim de `## Uso de IA e conferência humana {#sec-ia}`, isto é, tudo antes de `# Resultados {#sec-resultados}`. Inclui Mensagens, Resumo, *Abstract*, Q1 e Q2 | cerca de 3.490 (670 + 2.820) | `_esqueleto_v2_2409.qmd` `L1-282`; emendas (Resumo e Emenda 7); declaração do autor; `protocolo.md`, seções 2 a 8 e 10; `garritty_2024.md`, seção 4; `revisoes_anteriores.md`; `contexto_brasil.md`; `prisma_contagens.json`; `celulas.json`; `numeros_v2.json`; `livro_regras.md`, seções 1, 2, 4 e 7 |
| 2 | De `# Resultados {#sec-resultados}` até o fim de `## Moderadores {#sec-moderadores}`. Mais `linguagem_simples.qmd` | cerca de 3.860 (3.160 + 700) | `_esqueleto_v2_2409.qmd` `L284-436`; `spec_v2.md`, seção 4; `celulas.json`; `certeza.csv`; `swim_resumo.json` e os dois `meta_resumo.json`; `insumos/tabelas/numeros.json`; `numeros_v2.json`; `mecanismos_moderadores.md`; `revista/tabelas/previa_{sof,hipoteses,caracteristicas}.md`; `legendas.yml`; `referencias_excluidos.bib`; `08-revisao-humana/efeitos/pontos_para_o_revisor.md`, só para saber o que foi mantido; `livro_regras.md`, seções 3 e 5 |
| 3 | De `# Discussão {#sec-discussao}` até o fim (Referências). Mais os apêndices e `lacunas.yml` | cerca de 3.690 (1.840 + 930 + 920) | `_esqueleto_v2_2409.qmd` `L442-551`; `_esqueleto_suplemento.qmd`; `montar_suplemento.py`; `garritty_2024.md`, seção 4; `revisoes_anteriores.md`; `contexto_brasil.md`; `transferibilidade.yml`; `numeros_v2.json` (`transf_*`); `declaracao_uso_ia.md` regenerada e `declaracao_uso_ia_texto.md`; `declaracao_ia_v2.md`; emendas; declaração do autor; `_pendencias_abertas.json`; `livro_regras.md`, seções 6 e 7 |

## 5. Resumo em linguagem simples (Bloco 2; `linguagem_simples.qmd`, cerca de 700 palavras)

- **YAML.** `date: 2026-10-01`; o título fica.
- **Nome.** "Revisão" vira "síntese" (ou "este trabalho") em todo o texto e nos subtítulos. "A revisão em resumo" vira "A síntese em resumo".
- **Quadro "O que esta síntese estudou".** Leva a pergunta; 41 estudos; buscas até 20/09/2026; agentes de IA fizeram a maior parte do trabalho; o autor conferiu a busca, a seleção dos estudos e os dados tirados de cada um; a qualidade dos estudos e a confiança na evidência foram julgadas só pela IA, sem conferência humana. Sai "rascunho, com 18 pendências".
- **"O que encontramos?" e "O que isso significa?"** Ficam como estão.
- **"Quais são os limites?"** (cerca de 110 palavras), reescrito:
  - quem fez o quê;
  - o julgamento de qualidade e de confiança não passou por uma pessoa;
  - não se estimou quantos estudos a triagem por IA pode ter perdido;
  - só duas bases e as citações, sem a principal base latino-americana;
  - 342 dos 526 textos não foram obtidos;
  - a falta de estudos brasileiros é, em parte, lacuna da busca.

  Saem "O autor ainda não conferiu o trabalho", "18 pendências" e "Decisões ainda pendentes".
- **"Até quando vai a busca?"** As mesmas datas, mais "Esta é a versão de 01/10/2026".
- **Frase nova.** "Este resumo também foi redigido por agentes de IA, a partir do artigo."
- **Linha final.** Sai "Rascunho não validado; 18 pendências". Fica o link `[Leia a síntese completa, com os apêndices](revisao.pdf)`.
- **Restrições.** Nenhum número novo, nenhum "rascunho", e as proibições da seção 1.4 (a trava roda com `--extra linguagem_simples.qmd`).

## 6. Tarefas do coordenador

**Antes da redação:**

1. Copiar o esqueleto para `_esqueleto_v2_2409.qmd`.
2. Decidir se registra a Emenda 7 no *log* (`rs emenda`). Depois de qualquer comando que escreva no *log*, `rs declaracao-ia` vai por último. A declaração de hoje para no evento 833 e fala em 18 pendências. O Bloco 3 lê a regenerada, e ela também entra no pacote.

**Depois da junção:**

1. Aplicar as seções 2.11 e 3.4.
2. Tirar S9 a S11 do esqueleto dos apêndices; a função `lacunas` já está em `SECOES`.
3. Nos apêndices, ligar a numeração de tabela por apêndice. O `suppress-bibliography` e o `nocite` comum já estão encaminhados.
4. Corrigir `palavras_corpo` em `conferir_reestruturacao.py`. Hoje ela conta as linhas de figura (`![legenda](...)`, cerca de 890 palavras nas seis figuras) e os títulos `##`, embora o cabeçalho diga "sem legendas". Excluir `^!\[` e `^##`. Sem isso, a trava dá AVISO, com cerca de 8.900 palavras.
5. Pacote. O manifesto de `montar_pacote.py` leva `caixa_ferramentas.csv` (S9, dentro de `06-analise/`), mas ainda não leva:
   - as tabelas regionais de S10 (`insumos/tabelas/regional.md` e `viabilidade.md`);
   - as listas PRISMA-S e PRISMA-trAIce de S11 (`insumos/tabelas/checklist_*.md`).

   Também, `07-relatorio/checklist_prisma.csv` e `checklist_swim.csv` apontam para o relatório técnico, e não para este artigo. É preciso acrescentar esses arquivos e refazer as listas para o artigo novo, ou marcá-las como da versão de 24/09/2026 no `LEIA.md` do pacote. Os *prompts* não entram no pacote, e IA-6 os declara como privados. Conferir IA-6 contra o manifesto final.
6. Fechar a P038 só com a aprovação do autor a esta versão, e então ajustar a linha "Relato" do Apêndice G.
7. Rodar `montar_revisao_final.py`, `montar_suplemento.py`, `conferir_reestruturacao.py --modo final` e `bash ferramentas/publicar.sh`.

## 10. Sentinela

SHA256 das fontes da síntese, calculado em 30/09/2026 com `shasum -a 256`, da raiz. Os valores de `certeza.csv`, `swim_resumo.json` e dos dois `meta_resumo.json` são os de 24/09/2026 (`spec_v2.md`, seção 10). Os dois primeiros desses quatro batem com o campo `fontes` de `revista/celulas.json`.

```
c075097a6f119c0551beab82619cf9b01a5cc6adff640a324633e0bfff83beea  06-analise/certeza.csv
29878705b08a6fd1f7a3bea88327b1e28596ead4c0e3fb57562169c76e51e14e  06-analise/certeza_agrupamento_amplo.csv
a140b57602eb755e3ae68274c2db794151c3210aa537faae63d113bfa50a8a80  06-analise/swim_principal/swim_resumo.json
a40533e25689daf10dd94f5c5cb57e7fc88f21df9190fe3c38b990fdf69c15fb  06-analise/meta_exploratoria/meta_resumo.json
7ca65f2853153ce63b44bbf618d4bd18c105577d0fcd82a334c2181754f7dca7  06-analise/meta_mesmo_candidato/meta_resumo.json
c5291d5f7529627d2b505dd7e377cdb94b3a145e403c53fda244a3708baed105  07-relatorio/prisma_contagens.json
ecaded94a7bbcfe73af65815dc10890706395925cbb4d17b9be54ff69d23e103  07-relatorio/_pendencias_abertas.json
```

Antes de cada etapa, rode de novo o mesmo comando. Se um valor mudar, `celulas.json` e `numeros_v2.json` são regenerados, e as seções abaixo são reescritas:

| Arquivo que mudou | Seções a reescrever |
|---|---|
| `certeza.csv` | todos os spans e a Tab. 2; 2.8; 3.3 a 3.8; 3.10; 4.1; 4.4 (certeza); 5.1; 6; Mensagens; Resumo; *Abstract*; linguagem simples; seção 1.10 |
| `certeza_agrupamento_amplo.csv` | 3.8 (P1); Apêndice F |
| `swim_resumo.json` | as de `certeza.csv`, mais 3.1 (P4), 3.10 e as Figs. 4 e 6 |
| `meta_*/meta_resumo.json` | 3.4 (meta correspondente); 4.1 (P3); Fig. 5; FC-metas |
| `prisma_contagens.json` | 2.4; 3.1 (P1); Fig. 2; Resumo e *Abstract* (Limitações); 4.4 (seleção); linguagem simples |
| `_pendencias_abertas.json` | Se só a P038 fechar, só a linha "Relato" do Apêndice G muda. Se qualquer outra abrir ou fechar: abertura de IA-7; 2.9 (P3); 4.4; `lacunas.yml`; Mensagens (Como foi feita); Resumo e *Abstract*; Conclusões (última frase); linguagem simples |
