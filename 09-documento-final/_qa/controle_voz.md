# Leitura de controle do passe de voz (30/09/2026)

Leitor independente, que não escreveu nenhum dos textos. Prompt: `09-documento-final/prompts_final/prompt_leitura_controle_voz.md`. Pasta VOZ: o *scratchpad* da sessão (`…/scratchpad/voz`).

## Resumo

- **Base da comparação.** As cópias "antes" de `VOZ/antes/` são idênticas aos arquivos do commit `5f32e6c` (HEAD). O `_esqueleto_revisao_final.qmd` atual é igual à junção dos blocos de VOZ (`cabeca`, A, B, C1, C2, D, `cauda`), e o `revisao_final.qmd` e o `suplemento.qmd` montados (22:47) já trazem as mudanças do coordenador.
- **Pares lidos.** Li por *diff* de palavras os 16 pares do prompt: artigo, apêndices, `lacunas.yml`, linguagem simples, `legendas.yml`, `textos.yml`, `README.md`, `LEIA.md`, as três listas de conferência, `hipoteses.yml`, `oqf_principal.yml`, `transferibilidade.yml` e `montar_suplemento.py`. Li também as edições do coordenador em `montar_revisao_final.py` e `verificar_figuras.py`. Depois li o artigo inteiro, como ficou.
- **Sentido.** Nenhum número, chave, enunciado, certeza ou ID de pendência mudou. Palavras de certeza ("provavelmente", "pode(m)", "parece", "tende a") têm a mesma contagem em todos os pares. Ficaram **4 erros**: (i) duas ambiguidades de antecedente que trocam o ator ou a fonte, no README e no Apêndice B; (ii) a linha "Relato" do Apêndice G, que não acompanhou o "aprovamos o conteúdo desta versão" do artigo; e (iii) a ordem do piloto nos Métodos, que sugere que conferimos o piloto antes da Emenda 2.
- **Atores.** A IA continua como ator de tudo o que fez, e nenhuma ação de IA virou "nós". Sobrou um "dos autores" narrando os próprios autores, numa linha de tabela do `LEIA.md`. A ressalva fica para o "o congelamos com *hash*", porque quem grava o *hash* é a ferramenta.
- **Honestidade.** Todos os fatos da lista seguem presentes, com o mesmo alcance. O artigo passou de "declararam ter conferido/revisto" para "conferimos/revimos" (o radical "declar" caiu de 19 para 16 ocorrências). O "em bloco", o "sem registro item a item" e a "declaração única, transcrita pelo coordenador" seguraram o alcance.
- **Estilo.** Restam **13 avisos**. Os principais são fórmulas que o passe criou: o "Já" contrastivo foi de 0 para 11 no artigo, "por nós" aparece 3 vezes numa só frase (duas vezes), há "no entanto" intercalado em série nos Resultados e um "Daí que" com subjuntivo. Há também uma cadeia de cinco verbos no Apêndice G, que agora passa 1 palavra do teto.
- **Travas.** `conferir_reestruturacao.py --extra linguagem_simples.qmd`: OK (0 falhas, 0 avisos), com corpo de 8.486 palavras (teto 8.500). Os 17 `conferir_numeros.py` saíram vazios.
- **Semelhança com o corpus.** Média de 3,5/5.
- **Efeito das correções no orçamento.** Todas as correções sugeridas abaixo juntas tiram 9 palavras do corpo do artigo (folga atual: 14) e levam o Apêndice G a 291 palavras (teto: 292).

## Divergências

### Erros (mudou sentido, ator ou fato)

**E1. `README.md`, "Como foi feita": o antecedente atribui o Claude Code a um de nós.**
- Atual: "A síntese foi conduzida com a *skill* `revisao-sistematica` para o Claude Code, que um de nós, Felipe Lamarca, desenvolveu com apoio de agentes de IA e que divide o trabalho entre pessoas, modelos de linguagem e *scripts*."
- Problema: o "que" cola em "Claude Code". No "antes", o feminino de "desenvolvida" prendia o verbo à *skill*.
- Correção (mesmo número de palavras): "A síntese foi conduzida com a *skill* `revisao-sistematica`, que um de nós, Felipe Lamarca, desenvolveu para o Claude Code com apoio de agentes de IA e que divide o trabalho entre pessoas, modelos de linguagem e *scripts*."

**E2. `_esqueleto_suplemento.qmd`, Apêndice B (atalhos): o juízo de IA passa a poder ser lido como de @Garritty2024Rapid.**
- Atual: "As tabelas abaixo cruzam cada atalho declarado no protocolo (A1 a A5) com o que @Garritty2024Rapid recomendam para revisões rápidas de efetividade e apontam a consequência provável de cada atalho para os resultados."
- Problema: o "apontam", no plural, vem logo depois de "@Garritty2024Rapid recomendam" e se lê como verbo de Garritty. A consequência provável, porém, é inferência de IA ("Consequência provável de cada atalho, inferida e não medida").
- Correção (−4 palavras): "Para cada atalho declarado no protocolo (A1 a A5), as tabelas abaixo trazem o que @Garritty2024Rapid recomendam para revisões rápidas de efetividade e a consequência provável para os resultados."

**E3. `lacunas.yml`, linha "Relato" (Apêndice G): o alcance da aprovação é maior que o do artigo.**
- Atual: "Em bloco, na versão de 24/09/2026 (declaração de 30/09/2026); antes da entrega, aprovamos esta versão, que a reescreve sem mudar a análise, já com a Emenda 8, que pedimos (G9)"
- Problema: o coordenador restringiu o artigo a "aprovamos o conteúdo desta versão" (Métodos e Limitações), porque o passe de voz veio depois da aprovação. O Apêndice G ainda diz que aprovamos a versão inteira.
- Correção (+2 palavras): "Em bloco, na versão de 24/09/2026 (declaração de 30/09/2026); antes da entrega, aprovamos o conteúdo desta versão, que a reescreve sem mudar a análise, já com a Emenda 8, que pedimos (G9)"
- Ajuste opcional: o comentário das linhas 11 e 12 ("A linha 'Relato' já diz que os autores aprovaram esta versão…").

**E4. `_esqueleto_revisao_final.qmd`, Métodos, Extração, 1º parágrafo: a cronologia e o ator do piloto.**
- Atual: "O piloto com três estudos [@Meer2015a; @Klor2017a; @Araujo2021a], que conferimos em bloco, levou à Emenda 2."
- Problema: a relativa intercalada sugere que conferimos o piloto antes da Emenda 2, como se a nossa conferência tivesse levado a ela. Na verdade, a Emenda 2 foi decidida pelo coordenador de IA depois do piloto (20/09) e endossada depois. A conferência em bloco é de 30/09 (`declaracao_autor_2026-09-30.md`). O "antes" separava os dois fatos ("levou à Emenda 2, e os autores o conferiram em bloco").
- Correção (+1 palavra): "O piloto com três estudos [@Meer2015a; @Klor2017a; @Araujo2021a] levou à Emenda 2, e o conferimos em bloco."

### Avisos (marca de IA, excesso de fórmula, estilo destoante)

Os trechos A1 a A12 são as piores marcas que sobraram. Cada correção mantém palavras, números e chaves e não aumenta o número de palavras.

**A1. Artigo, Métodos, Seleção, 4º parágrafo: "por nós" três vezes na mesma frase.**
- Atual: "Os 184 relatos avaliados somam 165 propostas da IA (47 inclusões e 118 exclusões), conferidas em bloco e mantidas por nós, 16 casos limítrofes decididos por nós (8 inclusões e 8 exclusões) e 3 exclusões em que a IA estendeu uma regra nossa a caso novo, endossadas por nós (Emenda 7)."
- Correção (−3): "Os 184 relatos avaliados somam 165 propostas da IA (47 inclusões e 118 exclusões), que conferimos em bloco e mantivemos, 16 casos limítrofes que decidimos (8 inclusões e 8 exclusões) e 3 exclusões em que a IA estendeu uma regra nossa a caso novo, que endossamos (Emenda 7)."

**A2. Artigo, Métodos, Risco de viés: "por nós por custo".**
- Atual: "um árbitro de IA do mesmo modelo de A, escolhido por nós por custo, decidiu os desacordos."
- Correção (−1): "um árbitro de IA do mesmo modelo de A, que escolhemos por custo, decidiu os desacordos."

**A3. Artigo, Informações adicionais, desvio (v): "por nós por custo" de novo.**
- Atual: "registrou a troca do árbitro, decidida por nós por custo;"
- Correção (−1, a mesma forma do Apêndice B): "registrou a troca do árbitro, decisão nossa, por custo;"

**A4. Artigo: o "Já" contrastivo foi de 0 para 11** (os dois "já com a Emenda 8" do "antes" são temporais). Cinco deles estão nos Resultados. Onde o contraste é fraco, ele vira tique. Sugestão: tirar dois.
- "Já @Barnfield2019 é uma revisão conceitual, e @Cosgun2026, …" → "@Barnfield2019 é uma revisão conceitual, e @Cosgun2026, …" (−1)
- "Já a célula não randomizada de projeções frente a nenhuma pesquisa no comparecimento ficou vazia…" → "A célula não randomizada de projeções frente a nenhuma pesquisa no comparecimento ficou vazia…" (−1)

**A5. Artigo, Resultados: "X, no entanto," em série.** São quatro nos Resultados (C01, C06, C14 e C18). Em C06 e C14, o "antes" não tinha o conectivo, e o contraste já está na frase.
- "O desfecho, no entanto, é a parcela do candidato em toda a urna, e não só nos votos dados depois dela." → "O desfecho é a parcela do candidato em toda a urna, e não só nos votos dados depois dela." (−2)
- "A extração, no entanto, não registra se o EP corrige o agrupamento das decisões por participante…" → "A extração não registra se o EP corrige o agrupamento das decisões por participante…" (−2)

**A6. Artigo, "O que isso significa para o debate brasileiro": "Daí que" com subjuntivo.** A construção é lusitana, não está no corpus e soa forçada.
- Atual: "Daí que a consequência prática dessa incerteza dependa de quem carrega o ônus da prova -- isto é, de uma escolha jurídica e normativa."
- Correção (=): "Por isso, a consequência prática dessa incerteza depende de quem carrega o ônus da prova -- isto é, de uma escolha jurídica e normativa."

**A7. Artigo, Métodos, Extração, 2º parágrafo: gerúndio no fim da frase.** O bloco C2 corrigiu o mesmo gerúndio em Mecanismos, e as Limitações dizem "resolvidas pelo valor original".
- Atual: "…não foi acionada, e resolvemos as 259 divergências mantendo o valor original."
- Correção (−1): "…não foi acionada, e resolvemos as 259 divergências pelo valor original."

**A8. `_esqueleto_suplemento.qmd`, Apêndice G, última frase: cadeia de cinco verbos, com "revisaram… revisaram".** O apêndice também passou do teto: tem 293 palavras, e o teto (+5%) é 292.
- Atual: "Na noite de 30/09/2026, com a Emenda 8, outros agentes de IA revisaram o projeto, corrigiram a ferramenta de revisão, conferiram de novo o texto, revisaram o PDF, ajustaram o texto à nossa coautoria e o estilo à voz do primeiro autor, a partir de textos dele escritos sem IA, também sem ler PDF de estudo nem fazer análise nova."
- Correção (−2, apêndice com 291): "Na noite de 30/09/2026, com a Emenda 8, outros agentes, também sem ler PDF de estudo nem fazer análise nova, revisaram o projeto e o PDF, corrigiram a ferramenta de revisão, conferiram de novo o texto e o ajustaram à nossa coautoria e, no estilo, à voz do primeiro autor, a partir de textos dele escritos sem IA."
- O "de IA" pode sair porque as frases anteriores já dizem "agentes de IA".

**A9. `_esqueleto_suplemento.qmd`: as aberturas dos apêndices se repetem.** São "As estratégias abaixo…", "As tabelas abaixo…", "A tabela traz…" (B), "A tabela traz…" (E), "Os efeitos principais abaixo…" e "A tabela abaixo mostra…".
- Apêndice E, atual: "A tabela traz os efeitos principais de cada estudo, com a célula em que entram e a situação na contagem da síntese principal."
- Correção (−1): "Cada estudo aparece com seus efeitos principais, a célula em que entram e a situação na contagem da síntese principal."

**A10. `montar_suplemento.py`, `s6_efeitos()` (legenda da tbl-s6-efeitos): "estes entre eles" ficou pendurado no fim.**
- Atual: "Conferimos em bloco, na página do texto, os 560 efeitos extraídos, estes entre eles (Emenda 7)."
- Correção (=): "Conferimos em bloco, na página do texto, os 560 efeitos extraídos, entre eles estes (Emenda 7)."

**A11. `textos.yml`, `como_foi_feita` (1º parágrafo): pelo antecedente, quem divide o trabalho passa a ser o Claude Code.**
- Atual: "Um de nós, Felipe Lamarca, desenvolveu, com apoio de agentes de IA, a *skill* `revisao-sistematica` para o Claude Code, que divide o trabalho entre pessoas, modelos de linguagem e *scripts*."
- Correção (=): "Um de nós, Felipe Lamarca, desenvolveu para o Claude Code, com apoio de agentes de IA, a *skill* `revisao-sistematica`, que divide o trabalho entre pessoas, modelos de linguagem e *scripts*."

**A12. `LEIA.md`: o "e" junta dois fatos sem relação.**
- Atual: "Estamos revendo o risco de viés e o GRADE, e a lista das pendências abertas está em `07-relatorio/_pendencias_abertas.json`."
- Correção (=): "Estamos revendo o risco de viés e o GRADE. A lista das pendências abertas está em `07-relatorio/_pendencias_abertas.json`."

**A13. `LEIA.md`, linha da tabela de `08-revisao-humana/`: "dos autores" narra os próprios autores.** Nenhuma trava confere essa linha, e só os números contam.
- Atual: "| `08-revisao-humana/` | declarações dos autores (conferência em bloco, deduplicação e coautoria) e as decisões de deduplicação dos pares (sem resumos) |"
- Correção (−1): "| `08-revisao-humana/` | nossas declarações (conferência em bloco, deduplicação e coautoria) e as decisões de deduplicação dos pares (sem resumos) |"

### Ok com ressalva

- **O1. "o congelamos com *hash* no *log*"** (artigo, Métodos e "Registro e protocolo").
  - Quem grava o *hash* é a ferramenta, quando aprovamos o G2.
  - A forma segue o exemplo do prompt. Se o coordenador quiser o ator exato: "Aprovamos o protocolo no portão G2, em 19/09/2026, e a ferramenta o congelou com *hash* no *log*" (+2 palavras; o corpo tem folga).
- **O2. "declararam ter conferido/revisto" → "conferimos/revimos"** (artigo: Métodos, Limitações, Mensagens, Resumo).
  - O alcance continua o mesmo: "em bloco", "sem registro item a item" e "Registramos essa revisão numa declaração única, transcrita pelo coordenador de IA, sem preencher as planilhas item a item".
  - O Apêndice G, o `lacunas.yml`, o README e o `montar_suplemento.py` mantêm "declaramos".
- **O3. Métodos, "Uso de IA e conferência humana": "e ajustaram seu estilo à voz do primeiro autor".**
  - É fato verdadeiro, mas o prompt só autorizava acréscimo no bloco D.
  - "seu" fica ambíguo (o texto ou os agentes?). Correção (=): "e ajustaram o estilo à voz do primeiro autor".
  - Também se pode tirar a frase, porque a declaração de IA já a traz.
- **O4. "Aprovamos também o conteúdo desta versão" e "aprovamos o conteúdo desta"** (mudança do coordenador).
  - As duas só continuam verdadeiras se o passe não tiver mudado sentido nenhum.
  - Corrigidos E1 a E4, a afirmação se sustenta. Se lermos e aprovarmos o PDF reescrito, a forma pode voltar a "esta versão" (e então o E3 também).
- **O5. Fichnova2015a (Resultados, "Risco de viés nos estudos"): "foi julgado baixo, mesmo com 17 dos 37 respondentes eslovacos fora das tabelas".**
  - O "mesmo com" explicita a tensão que a arbitragem apontou (na v2, era um caso "para essa revisão", num *callout*).
  - Só que a `spec_final.md` 3.2 manda o caso entrar "como fato". Para a forma factual, volta o "antes" (+1): "Em @Fichnova2015a, 17 dos 37 respondentes eslovacos não aparecem nas tabelas, e o domínio de dados faltantes foi julgado baixo (@fig-rob; domínio a domínio no Apêndice D)."
- **O6. Linguagem simples, quadro e "Quais são os limites?": "Conferimos partes da busca e da seleção e os números tirados de cada estudo".**
  - Falta "em bloco", tanto no "antes" quanto no "depois", então não é efeito do passe.
  - Na primeira pessoa, "de cada estudo" pode soar como conferência item a item. Se couber (+2): "Conferimos em bloco partes da busca…".
- **O7. Informações adicionais, Disponibilidade: "a nossa declaração".**
  - O pacote traz três declarações (conferência em bloco, deduplicação e coautoria; ver `LEIA.md`). O singular vem do "antes".
  - Correção (=): "as nossas declarações".
- **O8. Métodos, "Os portões G3 a G9 foram aprovados em autopiloto, sem decisão humana, e só depois confirmamos quatro deles."**
  - Bate com "Como esta síntese foi feita" (G3, G5, G6 e G9) e com a declaração: P001/P004 (busca), P020/P041/P023 (elegibilidade), P025/P026 (piloto) e P038 (relato). G4, G7 e G8 seguem sem confirmação.
  - Saiu a glosa "pontos de aprovação previstos no protocolo ao fim de cada etapa, da busca ao relato", que repetia a seção de abertura. Ok.
- **O9. Mecanismos: o 60% e o 40% agora vêm atribuídos à "recodificação cega de 10 estudos".**
  - Conferi em `05-decomposicao/validacao_extracao/concordancia/concordancia.csv`: `mecanismo_testado` concorda em 6 de 10 estudos, e `mecanismo_tipo_evidencia`, em 4 de 10. A atribuição está certa.
- **O10. Métodos e Resultados: o "nós" autoral cobre passos executados por agentes ou *scripts*** ("Usamos", "Convertemos", "imputamos", "calculamos", "Inferimos", "Examinamos a transferibilidade").
  - Isso vem do "antes" e não foi criado pelo passe. É convenção de seção de método, porque somos responsáveis pelas escolhas.

## "Os autores", "dos autores", "pelos autores" e "aos autores" nos arquivos "depois"

| Arquivo | Linha | Trecho | Classificação |
|---|---|---|---|
| `_esqueleto_revisao_final.qmd` | 297 | "o que os autores leem como voto de seguro" (@Freden2024a) | ok (estudo citado) |
| `lacunas.yml` | 6 | comentário YAML: "da declaração dos autores de 30/09/2026" | ok (comentário interno, não publicado) |
| `lacunas.yml` | 11 | comentário YAML: "já diz que os autores aprovaram esta versão" | ok (comentário, não publicado); ajustar com o E3 |
| `lacunas.yml` | 12 | comentário YAML: "Se os autores não aprovarem" | ok (comentário, não publicado) |
| `LEIA.md` | 40 | "declarações dos autores (conferência em bloco, deduplicação e coautoria)" | corrigir (A13) |
| `checklist_prisma2020.md` | 43 | "**26** Conflitos de interesse dos autores." | ok (texto do item PRISMA 2020) |
| `hipoteses.yml` | 9 | comentário: "só interpretação dos autores" | ok (autores dos estudos; comentário) |
| `montar_suplemento.py` | 291 | comentário de código: "as conferências foram dos dois autores" | ok (comentário, não publicado) |

Não sobrou nenhum "aos autores". Outras formas, todas ok:
- "sem contato com autores (A5)" (artigo, PRISMA 9 e PRISMA-S 6): autores dos estudos.
- "e não são autores" (CRediT): sobre os agentes.
- "primeiro autor": declaração de IA, Métodos, Apêndice G e linguagem simples.
- "com a licença do autor da *skill*" (`LEIA.md`, linha 42): papel, não narração. Ficaria opcionalmente "com a licença da *skill*".

## Honestidade

| Fato | Onde está, depois | Situação |
|---|---|---|
| Conferências em bloco, sem dupla independente, sem registro item a item | Mensagens; Resumo; *Abstract*; Métodos (Busca, Seleção, Extração, Uso de IA); Limitações; Declaração de IA ("por nós dois, em bloco, sem dupla independente"); Apêndice G; `lacunas.yml`; listas; README; LEIA; vitrine | presente, mesmo alcance; "partes da busca" continua "partes" |
| Risco de viés e certeza só por IA, sem validação humana | Mensagens, Resumo, Métodos, Resultados, Limitações, Conclusões, Declaração de IA, Apêndices D, F e G, linguagem simples ("ninguém conferiu como a IA julgou…") | presente |
| Validação cega da triagem não feita | Métodos ("A validação cega da triagem, por sua vez, não foi feita"), Limitações, Declaração de IA, Apêndice G, README ("que não foi feita"), LEIA, vitrine | presente |
| PRESS por IA não equivale a revisão independente | Métodos (Busca e Uso de IA), Limitações, Apêndice G, PRISMA-S 14, `montar_suplemento.py` | presente |
| "Concordar com a IA depois de ver as decisões não vale como codificação cega" | Limitações do processo | presente, literal |
| Pendências abertas | Declaração de IA (P033, P035, P036, P042; P006, P007, P008); `tbl-lacunas` (a trava confere as 7) | presente |
| "RASCUNHO NÃO VALIDADO" uma vez | `revisao_final.qmd`: 1; `suplemento.qmd`: 0 | ok |
| Agentes redigiram o texto e ajustaram o estilo à voz do primeiro autor | Declaração de IA: "…redigiu este texto…" e "Agentes de IA também ajustaram o estilo do texto à voz do primeiro autor, a partir de textos escritos por ele sem IA, sem mudar números, enunciados nem conclusões." Também nos Métodos (O3), no Apêndice G e na linguagem simples | presente |

Contagens antes → depois:
- "em bloco": igual em todos os pares, salvo `textos.yml` (3 → 4, porque "a conferência dos autores (Emenda 7)" virou "a nossa conferência em bloco (Emenda 7)", que qualifica sem reforçar).
- "não foi feita": igual, salvo o README (0 → 1, acréscimo verdadeiro).
- "sem dupla", "item a item", "só por/de IA" e "sem validação humana": iguais.

## Mudanças do coordenador

1. **Métodos: "Os portões G3 a G9 foram aprovados em autopiloto, sem decisão humana, e só depois confirmamos quatro deles."** Correta e coerente com a abertura e com a declaração (O8).
2. **Métodos e Limitações: "aprovamos o conteúdo desta [versão], já com a Emenda 8".** Correta, mas o Apêndice G (`lacunas.yml`) não acompanhou (E3). Ver também O4.
3. **Legenda do PRISMA e `verificar_figuras.py`: "decididos por nós".** As duas batem, e `verificar_figuras.py` dá OK. Na legenda, "que conferimos em bloco (Emenda 7), exceto 16 casos limítrofes decididos por nós" se lê bem nas duas ligações possíveis do "exceto".
4. **`montar_revisao_final.py`, `t_hipoteses`: "conferimos em bloco só as divergências da recodificação cega de 10 estudos (Emenda 7)".** Coerente com Mecanismos e presente no `revisao_final.qmd` montado.
5. **Apêndice G: menção ao ajuste de estilo.** Presente e verdadeira, mas alonga a cadeia de verbos e põe o apêndice em 293 palavras, 1 acima do teto de 292 (A8).

## Semelhança com o corpus (`amostras_voz_v2.md`)

| # | Parágrafo | Nota | Justificativa (trecho mais parecido) |
|---|---|---|---|
| 1 | "Como esta síntese foi feita", 2º parágrafo ("A *skill* divide o trabalho…") | 4 | Subordinação, glosa "-- isto é, … --," e "Já o que pede julgamento humano…" como nos trechos 6 e 14; a frase do *log* fica no fim como apêndice solto. |
| 2 | Introdução, "No comparecimento, o modelo tem só a complacência…" | 4 | Enumeração (i) a (iii) e o fecho "Trata-se de uma limitação do modelo e, portanto, desta síntese" lembram o trecho 6 ("e, portanto, trata-se de um mecanismo supramajoritário"). |
| 3 | Resultados, "Há, no entanto, outra leitura para @Tyszler2015 e @Agranov2017a…" | 4 | Abre como o trecho 16 ("Há, no entanto, um salto conceitual…") e fecha com ressalva "em parte" no tom do trecho 8. |
| 4 | Resultados, @Gerber2020a ("No experimento de campo de @Gerber2020a…") | 3 | "O estimando, portanto, é…" segue o guia, mas são cinco frases de relatório, densas de números e do mesmo comprimento; o mais próximo é o trecho 18. |
| 5 | Da evidência à prática, "Sobre a restrição à divulgação…" | 3 | A glosa "-- isto é, de uma escolha jurídica e normativa" é do trecho 6, mas a abertura é uma enumeração longa sem conectivo dele, e "Daí que… dependa" foge do corpus (o mais perto é o "Dito de outra forma" do trecho 30). |
| 6 | Linguagem simples, "Os achados sobre o comparecimento variam…" | 3 | "Note, no entanto, que…" é literalmente o trecho 25, mas as frases seguintes abrem todas por adjunto de lugar ("Em dois estudos…", "Num jogo…", "Sobre a pesquisa…") e o ritmo continua telegráfico. |

**Média: 3,5/5.** A frase média do corpo do artigo foi de 24,5 para 25,5 palavras (mediana de 22 para 23), abaixo dos 28 a 32 do corpus. O passe aproximou o tom sem chegar ao ritmo dele.

## Travas

**`python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd`: RESULTADO: OK (0 falha(s), 0 aviso(s)).**
- Datas, 1.471 números contra a lista branca, 18 spans de célula, callouts, `tbl-lacunas` (7 pendências), citações, rótulos, proibições e revisões anteriores: OK.
- Revisões anteriores: 2 frases com verbo de conclusão, ambas sobre obras verificadas.

Palavras:

| Trecho | Palavras | Teto ou alvo |
|---|---|---|
| Corpo, Introdução a Conclusões | 8.486 | 7.500 a 8.500 (antes, 8.496) |
| Mensagens | 161 | 163 |
| Resumo | 253 | 255 |
| *Abstract* | 251 | 252 |
| "Como esta síntese foi feita" | 399 | 410 |
| Informações adicionais | 1.243 | 1.274 |
| Apêndice G | 293 | 292 (+5%; ver A8) |
| Linguagem simples | 824 | sem teto na trava (igual ao "antes") |

**`python3 09-documento-final/conferir_numeros.py <antes> <depois>`: saída vazia em todos os pares.**
- Artigo: a concatenação de `antes/cabeca.qmd`, A, B, C1, C2, D e `antes/cauda.qmd` (arquivo temporário no *scratchpad*), e também `antes/esqueleto_completo.qmd`, contra `_esqueleto_revisao_final.qmd`.
- Apêndices: `_esqueleto_suplemento.qmd`, e `suplemento_montado_antes.qmd` contra o `suplemento.qmd` montado.
- Tabelas e legendas: `lacunas.yml`, `legendas.yml`, `hipoteses.yml`, `oqf_principal.yml`, `transferibilidade.yml`.
- Textos avulsos: `linguagem_simples.qmd`, `textos.yml`, `README.md`, `LEIA.md`.
- Listas: `checklist_prisma2020.md`, `checklist_prisma_s.md`, `checklist_trAIce.md`.
- Código: `montar_suplemento.py`.

**Conferências extras, só de leitura:**
- `verificar_figuras.py`: OK (7 figuras).
- "RASCUNHO NÃO VALIDADO": 1 no artigo montado.
- Nenhum "—" novo; os que restam estão só em comentário ou constante dos `.py`.
- Nenhum conectivo proibido (Contudo, Entretanto, Todavia, Porém, Ademais, Em suma, Dessa forma, "Assim,"/"Logo," abrindo frase, "Além disso").
- Nenhuma palavra proibida do `my-voice` fora de termo técnico ("variância robusta", "erro-padrão robusto", "*bandwagon* dinâmico").
- `conferir_numeros.py` sobre o `revisao_final.qmd` montado (HEAD contra agora) acusa `[divs]` em dois parágrafos que vêm logo depois de figura ("No comparecimento, o modelo…" e "A direção não variou…"). É artefato da regex de Div (`^:{3,}\s*(…)`), cujo `\s*` atravessa a quebra de linha depois de um `:::` de fechamento. Os textos mudaram só no estilo (conferido acima). Essa trava não é a pedida pelo prompt, que compara esqueletos, mas vale trocar `\s*` por `[ \t]*` no `conferir_numeros.py`.
