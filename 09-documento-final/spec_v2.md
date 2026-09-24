# Especificação do artigo v2 (etapa 1)

Escrita em 24/09/2026 por subagente de IA (Opus, papel de editor-arquiteto) a partir de `09-documento-final/prompts_v2/prompt_arquiteto.md`. É o contrato do redator do corpo (etapa 3), do redator da abertura (etapa 4), da verificação (etapa 5) e dos passes de estilo (etapa 7). Não muda nada do plano aprovado (`/Users/felipelmc/.claude/plans/veja-acredito-que-na-delegated-ripple.md`): estrutura, figuras, tabelas, quadros e callouts estão congelados ali, e aqui só são detalhados.

Leituras feitas para escrever esta especificação, todas inteiras: o plano; `insumos/livro_regras.md`; `insumos/exemplares_movimentos.md`; `insumos/garritty_2024.md`; `insumos/revisoes_anteriores.md`; `_esqueleto_v1_oqf.qmd` (e a versão montada `_revisao_final_v1_oqf.qmd`); `verificacao.md`; `revista/rotulos.yml`; `revista/celulas.json`; `revista/numeros_v2.json`; `insumos/tabelas/numeros.json`; `insumos/contexto_brasil.md`; `insumos/mecanismos_moderadores.md`; `07-relatorio/relatorio.qmd`; `00-protocolo/protocolo.md`, `pergunta.md`, `teoria_programa.md`, `emendas.md` e `dag_v1.mmd`; `07-relatorio/_pendencias_abertas.json`; `08-revisao-humana/README.md`; `08-revisao-humana/efeitos/pontos_para_o_revisor.md`; `/Users/felipelmc/.claude/commands/my-voice.md`. Li também a trava `conferir_reestruturacao.py`, os prompts das etapas 2, 3 e 4 e o template Typst, para que a especificação não peça nada que a trava reprove.

## 0. Como ler esta especificação

**Identificadores de parágrafo.** Cada parágrafo tem um ID: `MP-1` (Mensagens), `RE-1` (Resumo executivo), `RS-1` (Resumo), `AB-1` (*Abstract*), `1.1-P1` (seção 1.1, parágrafo 1), `IA-1` (Informações adicionais), `AP-P1` (Apêndice A). Callouts são `CO-...`; quadros, `Q1` e `Q2`; o aviso de rascunho, `AV`. Os IDs são só desta especificação e nunca aparecem no texto.

**Notação das fontes de número.** O redator não digita número que não esteja numa destas fontes, e a especificação dá cada número só pela referência:

| Sigla | Arquivo (da raiz) | Exemplo |
|---|---|---|
| `cel:Cxx.campo` | `09-documento-final/revista/celulas.json`, célula Cxx | `cel:C01.k`, `cel:C01.ic_proporcao`, `cel:C01.p_sinal`, `cel:C02.delta` |
| `n2:chave` | `09-documento-final/revista/numeros_v2.json`, campo `valor` | `n2:relatos_nao_recuperados_total` (342) |
| `n1:chave` | `09-documento-final/insumos/tabelas/numeros.json` | `n1:meta.g`, `n1:rob_por_ferr.rob2.alto` |
| `pr:caminho` | `07-relatorio/prisma_contagens.json` | `pr:bases.identificados.por_fonte.openalex` |
| `mA:campo` / `mB:campo` | `06-analise/meta_exploratoria/meta_resumo.json` e `06-analise/meta_mesmo_candidato/meta_resumo.json`, `grupos[0].resultado` | `mA:tau` (0,197 → 0,20) |
| `pend:ID.n` | `07-relatorio/_pendencias_abertas.json` | `pend:P039.n` (560) |
| `cer:Cxx` | `06-analise/certeza.csv`, linha da célula Cxx, campos `justificativa` e `enunciado` | `cer:C10` (10.643 respondentes) |
| `v1:Lnnn` | número já escrito na linha nnn de `_esqueleto_v1_oqf.qmd` e conferido na `verificacao.md` | `v1:L332` (0,97; κ 0,90; PABAK 0,94) |

Os números das justificativas de `certeza.csv` e os do v1 estão na lista branca da trava. Números dos dossiês (`contexto_brasil.md`, `mecanismos_moderadores.md`), de `efeitos.csv` ou de `pontos_para_o_revisor.md` só entram se já estiverem numa das fontes acima. Se o redator precisar de um número derivado novo, ele não o calcula: pede ao coordenador uma entrada em `numeros_v2.json`, que é a única porta de entrada de número derivado.

**Orçamento de palavras.** Conta só a prosa corrida da seção: ficam fora os callouts, os quadros, as tabelas, os marcadores `@@...@@` e as legendas. A tolerância é de ±10% por seção de nível 1 e por subseção. As Mensagens principais (200) e o Resumo e o *Abstract* (250 cada) são limites duros.

**Frases canônicas (FC).** O mesmo achado usa as mesmas palavras em todos os produtos (livro R2.9). As frases abaixo são usadas assim, com variação só de concordância, nas Mensagens, no Resumo executivo, no Resumo, nas Conclusões, no resumo em linguagem simples e onde a especificação indicar. No *Abstract* vale a versão em inglês ao lado.

| ID | Frase canônica | *Abstract* |
|---|---|---|
| FC-apoio | A evidência é muito incerta sobre se ver uma pesquisa aumenta o apoio a quem ela mostra à frente (8 experimentos em duas células, cada uma com certeza muito baixa; quase todos em laboratório ou com vinheta hipotética). | *We are very uncertain whether seeing a poll increases support for whoever it shows ahead (8 experiments in two cells, each with very low certainty; almost all in the laboratory or with hypothetical vignettes).* |
| FC-apertada | Receber pesquisa que mostra disputa apertada, em vez de folgada, provavelmente não muda o comparecimento além de 2 pontos percentuais para mais ou para menos (1 experimento de campo; certeza moderada). | *Receiving a poll showing a close rather than a lopsided race probably does not change turnout by more than 2 percentage points either way (1 field experiment; moderate certainty).* |
| FC-divulgação | Ter visto a divulgação de pesquisas pode aumentar a intenção de votar ou o comparecimento (2 estudos não randomizados em eleições reais; certeza baixa). | *Having seen poll releases may increase turnout intention or turnout (2 non-randomised studies in real elections; low certainty).* |
| FC-projeção | Ver projeções que mostram probabilidade de vitória mais distante de 50:50 pode reduzir a decisão de votar (1 jogo *online*; certeza baixa). | *Seeing forecasts with a win probability further from 50:50 may reduce the decision to vote (1 online game; low certainty).* |
| FC-boca | A evidência é muito incerta sobre se divulgar boca de urna antes do fechamento das urnas muda o apoio ao líder (2 experimentos naturais, em direções opostas) ou reduz o comparecimento (3 experimentos naturais em duas células), com certeza muito baixa em todas as células. | *We are very uncertain whether releasing exit polls before polls close changes support for the leader (2 natural experiments pointing in opposite directions) or reduces turnout (3 natural experiments in two cells), with very low certainty in every cell.* |
| FC-Brasil | O único estudo com dados só do Brasil [@Araujo2021a] trata da divulgação oficial da apuração parcial com a votação ainda em curso, e não de pesquisa eleitoral. Nenhum estudo incluído estima, com dados só do Brasil, o efeito de pesquisas pré-eleitorais publicadas; o país aparece apenas entre os 46 do corte transversal de @Lago2015, que ficou fora da contagem principal. | *The only study with data from Brazil alone concerns the official release of partial counts while voting was still under way, not polls. No included study estimates the effect of published pre-election polls with data from Brazil alone; the country appears only among the 46 in a cross-national study that was left out of the main count.* |
| FC-metas | Duas meta-análises exploratórias, com 3 estudos cada, deram estimativas positivas com intervalos de confiança que cruzam zero e inferência robusta não confiável. | *Two exploratory meta-analyses, with 3 studies each, gave positive estimates with confidence intervals crossing zero and unreliable robust inference.* |
| FC-não-diz | A evidência não diz de quanto é o efeito das pesquisas sobre o voto, e tampouco permite afirmar que elas não têm efeito. | *The evidence does not tell how large the effect of polls on voting is, nor does it allow us to say that they have none.* |
| FC-regulação | Sozinha, a evidência não sustenta nem a restrição nem a manutenção das regras atuais de divulgação. | *On its own, the evidence supports neither restricting nor keeping the current rules on poll publication.* |
| FC-rascunho | Todas as etapas depois do protocolo foram conduzidas por agentes de IA, sem validação humana, e há 18 pendências humanas abertas. | *Every stage after the protocol was carried out by AI agents without human validation, and 18 human validation tasks remain open.* |

Números das FC: 8 (`v1:L41`); 2 pontos percentuais (δ do protocolo, `v1:L169`); 46 (`v1:L275`); 3 (`n1:meta.k_estudos`); 18 (`n2:pendencias_abertas`); os k das células vêm de `cel:`.

**Selo de certeza.** Nas Mensagens, no Resumo e no *Abstract*, a certeza vem com o selo `[⊕◯◯◯]{.grade}` e a palavra: muito baixa ⊕◯◯◯, baixa ⊕⊕◯◯, moderada ⊕⊕⊕◯, alta ⊕⊕⊕⊕ (U+2295 e U+25EF). No corpo, a palavra basta; o selo aparece na Tab. 2.

**Códigos de movimento.** M01 a M15, com dois dígitos, são os movimentos da rubrica dos exemplares (`insumos/exemplares_movimentos.md`); E1 a E7 são os exemplares; R1.1 a R7.30 e A1 a A36 são regras e itens de auditoria do livro (`insumos/livro_regras.md`); "frase-modelo M1" a "frase-modelo M18", com um dígito, são as frases-modelo do livro (seção 9 de `livro_regras.md`). E1 a E8, quando ligados a canais ("os canais E2 a E4"), são os elos do modelo lógico do protocolo; o contexto desfaz a ambiguidade, e no texto do artigo só os elos aparecem.

**Verbos pela certeza** (livro R5.36 e R5.37; rubrica M07). Alta: afirmação direta. Moderada: "provavelmente". Baixa: "pode". Muito baixa: "a evidência é muito incerta sobre...". Nulo ou trivial com certeza moderada: "provavelmente não muda... além de ±δ". Em inglês: *probably*, *may*, *we are very uncertain whether*. Tamanho de efeito, se aparecer, usa "efeito médio", nunca "efeito moderado". Cada conclusão é lida às cegas, com a direção invertida, antes de ficar (livro R5.39).

---

## 1. Público e tom

**Quem lê.** Em primeiro lugar, cientistas políticos que estudam comportamento eleitoral, opinião pública e campanhas e que leem revisões em revistas como *APSR*, *JOP* ou *BJPolS*. Em segundo, editores de método de revisões sistemáticas (Campbell, Cochrane), que vão procurar PRISMA 2020, SWiM, GRADE, risco de viés e desvios do protocolo. Em terceiro, quem participa do debate brasileiro sobre divulgação de pesquisas: assessorias do Congresso, a Justiça Eleitoral, jornalistas e institutos. Por último, o próprio autor, que ainda vai ler e validar o texto (P038). O texto é escrito para o primeiro leitor, com o rigor que o segundo cobra e a clareza de que o terceiro precisa.

**O que o leitor precisa sair sabendo.** Cinco coisas, nesta ordem:

1. a resposta, com a certeza: nos experimentos, a direção é *bandwagon*, com certeza muito baixa e sem estimativa de tamanho; no comparecimento, o quadro é misto, e o único achado com certeza moderada é um nulo por ±δ;
2. o que a evidência não diz: o tamanho do efeito, o efeito de pesquisas sobre eleitores brasileiros, o efeito de um embargo como o que o STF derrubou em 2006;
3. o que foi feito e por quem: uma revisão sistemática rápida, com protocolo congelado, feita de ponta a ponta por agentes de IA e ainda sem validação humana;
4. por que a regularidade *bandwagon* depende do tipo de desenho (laboratório e vinheta) e o que muda quando se olha só para eleições reais;
5. o que fica em aberto, com a pendência que decide cada ponto.

**Registro.** Artigo de revisão em revista de ciência política, em português do Brasil, com *abstract* em inglês. Primeira pessoa do plural como voz do texto, mas nunca para atribuir ao autor uma etapa que o registro atribui à IA: nos Métodos, cada etapa diz quem a fez (agente e modelo, ou o autor). Métodos no passado, dizendo o que esta revisão fez, sem explicação didática (livro R4.1, R4.2 e A13). Resultados com a observação antes da interpretação. Voz do autor pelas regras de `my-voice.md`: frases curtas misturadas com longas; listas no texto como "(i) ...; e (ii) ..."; termos em inglês em itálico (*bandwagon*, *underdog*, *momentum*, *survey*, *online*, *leave-one-out*); títulos em caixa de frase; negrito só no rótulo das Mensagens, nos subtítulos do Resumo e do *Abstract*, nos itens das Informações adicionais e no marcador **[A confirmar pelo autor]**. Nada de negrito como rótulo de parágrafo no corpo (diagnóstico 6 do plano): no lugar, uma frase de tópico ("Quanto ao realismo, ..."). Nenhum parágrafo abre com "Além disso", "Portanto", "Assim" ou "Consequentemente".

**Movimentos da rubrica que o texto cumpre** (`insumos/exemplares_movimentos.md`) e onde:

| Movimento | Onde se cumpre |
|---|---|
| M01 Resposta primeiro | MP, RE-2, RS-4/RS-6, 1.4-P2 (fim da introdução, antes dos Métodos) |
| M02 Contribuições explícitas | 1.3-P2 (numeradas) e 4.1-P3 (retomadas) |
| M03 Teoria antes da evidência | 1.2-P2 e 1.2-P3 com a Fig. 1; veredito por previsão em cada parágrafo de célula (3.4 a 3.7) e em 3.10-P2 com a Tab. 3 |
| M04 Métrica e direção antes dos resultados | Q1, 2.7-P2 e 2.7-P3 |
| M05 Unidades simples | pontos percentuais e "x de y estudos" nas Mensagens, no Resumo e nos parágrafos de célula; "2 em cada 100 eleitores" no Q1 |
| M06 Estudos nomeados em cada achado | todo parágrafo de célula (3.4 a 3.7) e a Tab. 2 |
| M07 Certeza ligada ao verbo | todo enunciado; verbos da seção 0 |
| M08 Causal separado de correlacional | 2.7-P1; ordem randomizado → não randomizado em 3.4 a 3.7; convergência das classes em 4.1-P1 |
| M09 Ausência de evidência não é evidência de ausência | Q1 (nulo por ±δ), 2.7-P3, 3.3-P3, 3.7-P2, 5.1-P2 |
| M10 O que a evidência não permite responder | MP-5, RE-2, 4.3-P3 |
| M11 Tabela e figura na ordem do texto | Tab. 2 e Figs. 4 e 5 em 3.3; ordem C01 a C18 em 3.4 a 3.7 |
| M12 Desvios com motivo, momento e direção | 2.1-P3, 3.8-P6, IA-1 |
| M13 Processo separado de evidência | 4.3 × 4.4 |
| M14 Revisões anteriores | 1.3-P1 e 4.2 |
| M15 Prática separada de pesquisa | 5.2 × 5.3 |

---

## 2. YAML exato do esqueleto

```yaml
---
title: "Pesquisas eleitorais publicadas mudam o voto?"
subtitle: "Revisão sistemática rápida sobre os efeitos *bandwagon* e *underdog* e o comparecimento"
date: 2026-09-25
keywords:
  - pesquisas eleitorais
  - efeito bandwagon
  - efeito underdog
  - comparecimento eleitoral
  - revisão sistemática rápida
  - síntese sem meta-análise
  - GRADE
  - Brasil
metadata-files: [revista/_revista.yml]
bibliography: revista/referencias.json
format:
  html:
    toc: true
    toc-location: left
    toc-depth: 2
    toc-title: "Sumário"
    number-sections: true
  typst: default
  docx:
    toc: true
    toc-depth: 2
    number-sections: true
---
```

Notas:

- Autor, afiliação, `lang`, `csl`, `crossref` (quadros), `rascunho`, a nota de autoria por IA e a data da última busca vêm de `revista/_revista.yml`; não repita nada disso no esqueleto.
- `typst: default` herda todas as opções do `_revista.yml`. Se o render Typst perder as opções com `default`, troque por `typst: {}`; não copie as opções para o esqueleto.
- Logo abaixo do YAML, um comentário HTML curto (sem caminhos de arquivo no texto renderizado) diz que o esqueleto é a fonte e que `montar_revisao_final.py` gera o `revisao_final.qmd`.
- Os cabeçalhos sem número são todos de nível 1, para o sumário ficar plano: `# Mensagens principais {#mensagens-principais .unnumbered}` (dentro da Div), `# Resumo executivo {#resumo-executivo .unnumbered}`, `# Resumo {#resumo .unnumbered}` (dentro da Div), `# Abstract {#abstract .unnumbered}` (dentro da Div `lang="en"`), `# Informações adicionais {#informacoes-adicionais .unnumbered}`, `# Referências {#referencias .unnumbered}` e `# Apêndice A: pendências humanas abertas {#sec-pendencias .unnumbered}`. O prompt do redator fala em `##` para as Mensagens; vale o nível 1 desta especificação. O template Typst reestiliza qualquer nível dentro das caixas.

---

## 3. Seção a seção

### 3.0 Visão geral

| Ordem | Seção | ID | Orçamento | Marcadores e quadros | Callouts (IDs exatos) |
|---|---|---|---|---|---|
| 0 | Aviso de rascunho | (callout-warning) | 60 | – | – |
| 1 | Mensagens principais | `mensagens-principais` | ≤ 200 (duro) | – | CO-P038 logo depois: {P038} |
| 2 | Resumo executivo | `resumo-executivo` | 700 (500 a 800) | – | – |
| 3 | Resumo | `resumo` | ≤ 250 (duro) | – | – |
| 4 | *Abstract* | `abstract` | ≤ 250 (duro) | – | – |
| 5 | 1 Introdução | `sec-introducao` | 1.100 | Fig. 1, Q1 | – |
| 5.1 | 1.1 O problema e o debate brasileiro | `sec-problema` | 400 | – | – |
| 5.2 | 1.2 Como a exposição poderia agir | `sec-como-agiria` | 320 | `@@FIGURA modelo_logico@@`, Q1 | – |
| 5.3 | 1.3 Por que esta revisão | `sec-por-que` | 240 | – | – |
| 5.4 | 1.4 Objetivos | `sec-objetivos` | 140 | – | – |
| 6 | 2 Métodos | `sec-metodos` | 2.150 | Q2 | 4 |
| 6.1 | 2.1 Protocolo, tipo de revisão e desvios | `sec-protocolo` | 330 | – | – |
| 6.2 | 2.2 Critérios de elegibilidade | `sec-elegibilidade` | 130 | Q2 | – |
| 6.3 | 2.3 Fontes e busca | `sec-busca` | 250 | – | CO-busca {P001, P004} |
| 6.4 | 2.4 Seleção dos estudos | `sec-selecao` | 260 | – | CO-selecao {P006, P007, P008, P019, P020, P023, P041} |
| 6.5 | 2.5 Extração | `sec-extracao` | 250 | – | CO-extracao {P025, P026, P037, P039} |
| 6.6 | 2.6 Risco de viés | `sec-rob-metodos` | 170 | – | – |
| 6.7 | 2.7 Síntese | `sec-sintese` | 370 | – | – |
| 6.8 | 2.8 Certeza da evidência | `sec-certeza` | 210 | – | CO-certeza {P035, P036, P042} |
| 6.9 | 2.9 Uso de IA e supervisão humana | `sec-ia` | 180 | – | – |
| 7 | 3 Resultados | `sec-resultados` | 3.480 | Figs. 2 a 7, Tabs. 1 a 3 | 4 |
| 7.1 | 3.1 Estudos incluídos | `sec-incluidos` | 350 | `@@FIGURA prisma@@`, `@@TABELA caracteristicas@@` | – |
| 7.2 | 3.2 Risco de viés nos estudos | `sec-rob` | 200 | `@@FIGURA rob@@` | CO-rob {P033} |
| 7.3 | 3.3 Visão geral da síntese | `sec-efeito` | 260 | `@@TABELA sof@@`, `@@FIGURA celulas@@`, `@@FIGURA direcao@@` | – |
| 7.4 | 3.4 Apoio a quem aparece à frente | `sec-apoio` | 680 | `@@FIGURA metas@@` | – |
| 7.5 | 3.5 Viabilidade e voto estratégico | `sec-viabilidade` | 180 | – | – |
| 7.6 | 3.6 *Momentum* | `sec-momentum` | 160 | – | – |
| 7.7 | 3.7 Comparecimento | `sec-comparecimento` | 430 | – | – |
| 7.8 | 3.8 Sensibilidades e viés de relato | `sec-sensibilidades` | 330 | – | CO-efeito {P033, P036, P037, P039, P042} |
| 7.9 | 3.9 Mecanismos | `sec-mecanismo` | 360 | – | CO-mecanismo {P037, P039} |
| 7.10 | 3.10 Moderadores | `sec-moderadores` | 440 | `@@TABELA hipoteses@@`, `@@FIGURA realismo@@` | CO-moderadores {P037, P039} |
| 7.11 | 3.11 Percepção, implementação e custo | `sec-percepcao` | 90 | – | – |
| 8 | 4 Discussão | `sec-discussao` | 1.600 | – | – |
| 8.1 | 4.1 Resumo dos achados | `sec-achados` | 300 | – | – |
| 8.2 | 4.2 Relação com revisões anteriores | `sec-revisoes-anteriores` | 300 | – | – |
| 8.3 | 4.3 Completude, aplicabilidade e limitações da evidência | `sec-limitacoes-evidencia` | 400 | – | – |
| 8.4 | 4.4 Limitações do processo e da síntese | `sec-limitacoes-processo` | 600 | – | – |
| 9 | 5 Da evidência à prática: implicações | `sec-pratica` | 900 | Tabs. 4 e 5 | 2 |
| 9.1 | 5.1 Caixa de ferramentas | `sec-caixa` | 280 | `@@TABELA oqf_principal@@` | CO-caixa {P035, P036, P042} |
| 9.2 | 5.2 O que isso significa para o debate brasileiro | `sec-brasil` | 420 | `@@TABELA transferibilidade@@` | CO-brasil {P036, P039, P042} |
| 9.3 | 5.3 Implicações para a pesquisa | `sec-pesquisa-futura` | 200 | – | – |
| 10 | 6 Conclusões | `sec-conclusoes` | 200 | – | – |
| 11 | Informações adicionais | `informacoes-adicionais` | 850 | – | – |
| 12 | Referências | `referencias` | – | `::: {#refs}` `:::` | – |
| 13 | Apêndice A: pendências humanas abertas | `sec-pendencias` | 80 | `@@TABELA pendencias@@` | – |

Corpo (1 a 6): cerca de 9.430 palavras. Os títulos numerados em caixa de frase, como na coluna "Seção", com o ID entre chaves: `# Introdução {#sec-introducao}`, `## O problema e o debate brasileiro {#sec-problema}` e assim por diante (o número é do Quarto, não se digita). O título da seção 5 é "Da evidência à prática: implicações" (livro R1.9).

**Ordem das figuras e das tabelas no texto** (livro A20): Fig. 1 (1.2), Q1 (1.2), Q2 (2.2), Fig. 2 e Tab. 1 (3.1), Fig. 3 (3.2), Tab. 2 e Figs. 4 e 5 (3.3), Fig. 6 (3.4), Tab. 3 e Fig. 7 (3.10), Tab. 4 (5.1), Tab. 5 (5.2). A abertura (Mensagens, Resumo executivo, Resumo, *Abstract*) não chama figura nem tabela; pode remeter a seções numeradas com `@sec-`. Todo marcador `@@...@@` fica em linha própria, com linha em branco antes e depois, e é chamado no texto antes ou logo depois (`@fig-...`, `@tbl-...`, `@qdr-...`).

**Convenção dos callouts.** Cada um é `::: {.callout-important}` com `## Pendente de revisão humana` na primeira linha e 1 ou 2 frases. O conjunto de IDs P0xx dentro de cada caixa é exatamente o da tabela acima: nenhum ID a mais, nenhum a menos (a trava compara o multiconjunto com o v1). Os 18 IDs abertos aparecem todos fora do apêndice por meio dessas caixas. Texto sem caminho de arquivo e sem nome interno (`FORA`, `pontos_para_o_revisor.md`).

**Parágrafos com enunciado de célula.** Cada parágrafo que contém um `[...]{.enunciado cel="Cxx"}` é conferido pela trava como uma unidade. Nele:
- "x de y" com algarismos só se referir à própria célula (y = k ou estudos com direção; x = contagem de direção); subconjuntos vão por extenso ("três dos quatro"), senão viram AVISO ou FALHA; "x de y efeitos" é livre;
- "p = ..." e "IC 95% ... a ..." fora de um g, EP ou β só com os valores da célula (`cel:Cxx.p_sinal`, `cel:Cxx.ic_proporcao`);
- nenhuma outra frase "certeza <nível>" de outra célula;
- o k da célula aparece fora do span quando o enunciado não o traz (C12 e C17; ver seção 4).
Por isso, metas, agrupamento amplo e sensibilidades ficam em parágrafos sem span.

### 3.1 Aviso de rascunho (AV), antes das Mensagens

`::: {.callout-warning}` com `## RASCUNHO NÃO VALIDADO: 18 pendências humanas abertas`. Três ou quatro frases, cerca de 60 palavras:
- FC-rascunho, com a consequência: os achados não devem ser citados como finais;
- a nota de autoria, literal de `revista/_revista.yml:revista.nota-ia`: "Rascunho redigido por IA a partir dos arquivos do projeto e ajustado ao estilo do autor; não revisado pelo autor (P038)." (no PDF o bloco de título também a imprime; a repetição é aceita, porque HTML e .docx não têm esse bloco);
- a última busca: 19/09/2026 nas bases e 20/09/2026 na busca por citação;
- remissão ao [Apêndice A](#sec-pendencias).
Fonte: `v1:L30`; plano, "Honestidade sobre a autoria". Este callout não conta entre os 11 (o título não é "Pendente de revisão humana").

### 3.2 Mensagens principais (etapa 4)

Estrutura: `::: {.mensagens-principais}` → `# Mensagens principais {#mensagens-principais .unnumbered}` → lista de 5 itens → `:::`. Cada item começa com um rótulo curto em negrito e traz direção, k, selo e frase padrão. Até 200 palavras no total. O agrupamento amplo *post hoc* (9 de 9) não aparece. Nenhum g, nenhum p.

- **MP-1 Apoio a quem aparece à frente** (cerca de 55 palavras). Função: resposta à pergunta principal (M01). Conteúdo: nas duas células com mais estudos, os 4 experimentos de cada uma foram na direção *bandwagon*; uma compara mostrar pesquisa com não mostrar, a outra o mesmo candidato à frente ou atrás; FC-apoio, com o selo ⊕◯◯◯; a ressalva: uma decisão pendente sobre um efeito de @Witsman2016a, que o autor do estudo lê como voto estratégico, pode tirar um experimento da segunda célula. Números: `cel:C01.k`, `cel:C01.n_beneficos`, `cel:C02.k`, `cel:C02.n_beneficos`, 8 (`v1:L41`). Movimentos: M01, M05, M07; livro R2.7.
- **MP-2 Comparecimento** (cerca de 55). FC-apertada com ⊕⊕⊕◯; FC-divulgação com ⊕⊕◯◯; FC-projeção com ⊕⊕◯◯. Números: `cel:C13.k`, `cel:C18.k`, `cel:C14.k`. Movimentos: M01, M05, M07, M09.
- **MP-3 Boca de urna** (cerca de 30). FC-boca com ⊕◯◯◯. Números: `cel:C05.k`, `cel:C16.k` + `cel:C17.k`. Movimento: M07.
- **MP-4 Brasil** (cerca de 40). FC-Brasil encurtada (pode omitir a segunda frase se passar do limite, mas nunca dizer "nenhum estudo sobre o Brasil" sem a qualificação "com dados só do Brasil"); a certeza do estudo brasileiro: "a evidência é muito incerta sobre se essa divulgação aumenta a votação de quem aparece à frente (1 experimento natural; ⊕◯◯◯ certeza muito baixa)". Fonte: `cel:C06`. Movimentos: M10; livro R2.14.
- **MP-5 O que a evidência não permite dizer** (cerca de 20). FC-não-diz + FC-regulação. Movimento: M10.

Logo depois da Div: **CO-P038** {P038}. Texto: "Todo o documento depende da P038: o autor ainda não leu nem confirmou o relato que o autopiloto aprovou no portão G9. As demais pendências estão no [Apêndice A](#sec-pendencias), e cada seção indica as que a afetam." Fonte: `v1:L64`.

### 3.3 Resumo executivo (etapa 4)

`# Resumo executivo {#resumo-executivo .unnumbered}`. Pirâmide invertida, começando pelo problema de política (livro §11.1, R2.6 e R2.15). Só prosa, sem listas, sem figura, sem tabela. Cerca de 700 palavras em 7 parágrafos.

- **RE-1 Problema** (cerca de 100). Função: abrir pela política, não pela revisão. Conteúdo: pesquisas voltam ao centro do debate a cada eleição em que as urnas se afastam das estimativas; depois do primeiro turno de 2022, projetos de lei propuseram punir institutos cujas pesquisas divergissem do resultado [@BrasilCamara2022PL2567; @BrasilSenado2022PL2558]; a decisão do STF de 2006 que derrubou o embargo de 15 dias se apoiou no direito à informação, e não em evidência sobre efeitos [@STF2006ADI3741]; a pergunta de fundo, raramente respondida com dados, é se ver uma pesquisa muda o voto de quem a vê. Números: 2022, 2006, 15 (`v1:L57`, `v1:L99`). Movimentos: E4 (pergunta controversa), livro R2.15.
- **RE-2 A resposta curta** (cerca de 100). Função: tese antes do detalhe (M01; E6). Conteúdo: nos experimentos, a direção dominante é *bandwagon*, com certeza muito baixa; a revisão não estima o tamanho do efeito; no comparecimento, o quadro é misto; sobre o Brasil, a principal mensagem é a lacuna; FC-não-diz. Movimentos: M01, M10.
- **RE-3 O que foi feito** (cerca de 110). Função: bloco "o que foi feito" (livro R2.12 e R2.13). Conteúdo: busca no OpenAlex em inglês, português e espanhol e na BDTD em 19/09/2026, com busca por citação até 20/09/2026; 41 estudos (55 relatos) publicados de 2010 a 2024, a maioria dos Estados Unidos e da Europa; experimentos de *survey* e de laboratório, um experimento de campo, experimentos naturais e painéis; evidência separada em células, contagem da direção das estimativas e certeza GRADE por célula; todas as etapas depois do protocolo feitas por agentes de IA, sem validação humana. Números: `n1:estudos`, `n1:relatos`, `n1:ano_min`, `n1:ano_max`. Movimentos: livro R2.12, M06 (parcial).
- **RE-4 Apoio a quem aparece à frente** (cerca de 110). Conteúdo: nas duas células com mais estudos, todos os experimentos apontam para mais apoio a quem a pesquisa mostra à frente; são poucos, pequenos e quase todos de laboratório ou com candidatos hipotéticos, e a certeza é muito baixa; FC-metas; não se sabe o tamanho do efeito nem se ele aparece fora do laboratório; viabilidade e *momentum* têm 1 ou 2 estudos por célula, todos com certeza muito baixa. Fonte: `v1:L53`; `cel:C01`, `cel:C02`, `cel:C07` a `cel:C11`. Movimentos: M07, M08.
- **RE-5 Comparecimento** (cerca de 100). Conteúdo: FC-apertada (o maior experimento de campo, nos Estados Unidos); FC-divulgação; FC-projeção; FC-boca na parte de comparecimento. Fonte: `v1:L55`. Movimentos: M07, M09.
- **RE-6 Brasil** (cerca de 110). Conteúdo: FC-Brasil; não há estudo sobre como o voto obrigatório, os dois turnos ou a confiança nas pesquisas alteram o efeito; o fundamento do STF em 2006 não depende desta evidência; FC-regulação; a decisão cabe a quem tem mandato para tomá-la (livro R6.10). Fonte: `v1:L57` corrigido. Movimentos: M10, livro R2.14 e R6.10.
- **RE-7 Estado do documento** (cerca de 70). Conteúdo: FC-rascunho; a validação pode mudar a composição das células e, com ela, as mensagens; algumas decisões de julgamento ficaram em aberto para o autor (@sec-limitacoes-processo); lista no [Apêndice A](#sec-pendencias). Fonte: `v1:L59`. Movimento: livro R7.24.

### 3.4 Resumo (etapa 4)

`::: {.resumo}` → `# Resumo {#resumo .unnumbered}` → parágrafos com subtítulo em negrito na mesma linha → `**Palavras-chave:** ...` → `:::`. Até 250 palavras, sem contar a linha de palavras-chave. Cobre os 12 itens do resumo PRISMA 2020 (livro R2.1): o título (item 1) já identifica a revisão sistemática.

- **RS-1 Contexto** (cerca de 25). O debate sobre restringir ou punir a divulgação de pesquisas depende de saber se ver uma pesquisa muda o voto.
- **RS-2 Objetivos** (cerca de 25; item 2). Avaliar se a exposição a resultados de pesquisas eleitorais publicadas altera a intenção ou a escolha de voto, em que direção (*bandwagon* ou *underdog*) e se altera o comparecimento. Fonte: `v1:L71`.
- **RS-3 Métodos** (cerca de 75; itens 3 a 6). Critérios (experimentos, experimentos naturais, quase-experimentos e painéis publicados desde 2010, em qualquer idioma, sobre pesquisa pré-eleitoral, agregador ou projeção, boca de urna e, por emenda, apuração parcial oficial); fontes e datas (OpenAlex e BDTD em 19/09/2026; busca por citação até 20/09/2026); risco de viés (RoB 2, ROBINS-I V2, EPOC); síntese (contagem da direção das estimativas por célula, SWiM, com teste de sinal e intervalo de Clopper-Pearson); certeza (GRADE); todas as etapas depois do protocolo por agentes de IA. Fonte: `v1:L73`.
- **RS-4 Resultados** (cerca de 80; itens 7 e 8). 41 estudos (55 relatos); os tamanhos de amostra estão em unidades diferentes e não foram somados; 27 na síntese principal, em 18 células; nas duas células com mais estudos, 4 de 4 experimentos na direção *bandwagon* (proporção 1,00; IC 95% 0,40 a 1,00), com certeza muito baixa ⊕◯◯◯; FC-metas, numa só oração e sem g; FC-apertada com ⊕⊕⊕◯; FC-divulgação e FC-projeção com ⊕⊕◯◯; boca de urna com certeza muito baixa; FC-Brasil na forma curta. Números: `n1:estudos`, `n1:relatos`, `n1:n_swim_principal_estudos`, `n1:swim_principal_celulas_com_estudo`, `cel:C01.k`, `cel:C01.proporcao`, `cel:C01.ic_proporcao`.
- **RS-5 Limitações** (cerca de 30; item 9). IA sem validação humana (18 pendências); 342 de 526 relatos buscados não foram recuperados; poucos estudos por célula e, no apoio a quem lidera, quase todos de laboratório ou vinheta; fontes restritas a duas bases e busca por citação. Números: `n2:pendencias_abertas`, `n2:relatos_nao_recuperados_total`, `n2:relatos_buscados_total`.
- **RS-6 Conclusões** (cerca de 30; item 10). A direção dominante nos experimentos é *bandwagon*, com certeza muito baixa e sem estimativa de tamanho; FC-não-diz; nenhum estudo sobre pesquisas com dados só do Brasil.
- **RS-7 Registro e financiamento** (cerca de 15; itens 11 e 12). Não registrado; protocolo congelado com sha256 no *log*; sem financiamento. Fonte: `v1:L79`.
- **Palavras-chave:** as do YAML.

### 3.5 *Abstract* (etapa 4)

`::: {.resumo lang="en"}` → `# Abstract {#abstract .unnumbered}` → **Background.** **Objectives.** **Methods.** **Results.** **Limitations.** **Conclusions.** **Registration and funding.** → `**Keywords:** election polls; bandwagon effect; underdog effect; voter turnout; rapid systematic review; synthesis without meta-analysis; GRADE; Brazil.` → `:::`. Parágrafos AB-1 a AB-7, com o mesmo conteúdo de RS-1 a RS-7, em inglês acadêmico natural, não traduzido palavra por palavra (livro §11.4; `references/ingles.md` da skill tirar-cara-de-ia no passe de estilo). Ponto decimal (1.00; 0.40), sem itálico no bloco inteiro (a v1 punha tudo em itálico; não repetir). Frases GRADE com as versões em inglês das FC. Proibido: *significant*, *beneficial*, *harmful*, *no effect*, *peer review*. Até 250 palavras sem a linha de *keywords*.

### 3.6 Seção 1: Introdução `{#sec-introducao}` (cerca de 1.100)

#### 1.1 O problema e o debate brasileiro `{#sec-problema}` (cerca de 400)

- **1.1-P1** (cerca de 90). Função: gancho com a pergunta controversa (E4; E6, "debate dividido"). Conteúdo: pesquisas eleitorais estão entre as informações mais difundidas de uma campanha e, no Brasil, voltam ao centro do debate a cada eleição em que o resultado se afasta das estimativas; o debate sobre regular a divulgação depende de duas perguntas empíricas, se ver uma pesquisa muda o voto e em que direção (a favor de quem lidera ou de quem está atrás); a pergunta é antiga e a resposta, disputada. Fontes: `v1:L49`; protocolo [6]; para "antiga e disputada", `revisoes_anteriores.md` §1 e §3 (Barnfield classifica estudos desde a década de 1940; Moy e Rinke: a literatura "can hardly conclude"), sem escrever ano nem número. Movimentos: E4, livro R6.13 (prioridade do problema). Sem números.
- **1.1-P2** (cerca de 110). Função: marco normativo. Conteúdo: a Lei das Eleições obriga as entidades e empresas que realizam pesquisas eleitorais para conhecimento público a registrá-las na Justiça Eleitoral até cinco dias antes da divulgação, com contratante, valor, metodologia, plano amostral, margem de erro e questionário; divulgação sem registro é punida com multa, e a de pesquisa fraudulenta é crime [@Brasil1997Lei9504]; a Resolução-TSE nº 23.600/2019 organiza o registro no PesqEle, exige a assinatura do estatístico e fixa a multa entre R$ 53.205,00 e R$ 106.410,00 [@TSE2019Res23600]; não há período de silêncio: o art. 35-A, incluído pela Lei nº 11.300/2006, vedava a divulgação do décimo quinto dia anterior até as 18 horas do dia da eleição, e o STF, nas ADIs 3.741, 3.742 e 3.743, declarou-o inconstitucional por restringir o direito do eleitor à informação; o efeito das pesquisas sobre o voto não entrou nesse fundamento [@STF2006ADI3741]. Fonte: `v1:L97`, `v1:L99` (com a correção 7 da verificação: "entidades e empresas que realizam"). Movimento: livro R6.20 (marco normativo).
- **1.1-P3** (cerca de 110). Função: o debate recente. Conteúdo: depois do primeiro turno de 2022, o PL nº 2.567/2022 (Câmara) propôs tipificar como crime a publicação de pesquisa que diverge do resultado além da margem de erro [@BrasilCamara2022PL2567], e o PL nº 2.558/2022 (Senado) propôs punir as empresas [@BrasilSenado2022PL2558]; em 24/09/2026, o primeiro tramitava apensado ao PL nº 96/2011, pronto para pauta, com a nota de rodapé do v1 (URL da Câmara), e o segundo aguardava relator; um requerimento de CPI reuniu 30 assinaturas [@SenadoNoticias2022CPIPesquisas] (não dizer que foi instalada); o levantamento da ESOMAR e da WAPOR cita o Brasil entre os países em que lideranças cogitaram multar ou prender responsáveis por pesquisas que não batessem com as urnas, e mostra a América Latina como a região com maior proporção de países com embargo, de sete dias na mediana [@ESOMARWAPOR2022]. Fonte: `v1:L101` (com a correção 8 da verificação). Números: `v1:L101`.
- **1.1-P4** (cerca de 90). Função: delimitar a pergunta desta revisão contra as duas que o debate mistura. Conteúdo: a precisão [@Meireles2022: mais de 2 mil pesquisas registradas em cinco eleições de 2012 a 2020; precisão melhora perto da eleição e com amostras maiores; desempenho comparável ao de outros países] e a mudança real de opinião na reta final [@PereiraNunes2024: voto estratégico e decisão tardia; nos cenários de realocação, a diferença de cerca de 10 pontos cai para 7,4 a 7,9]; fecho: nenhuma das duas é a pergunta desta revisão, que é se ver uma pesquisa muda o voto de quem a vê. Fonte: `v1:L103`. Números: `v1:L103`.

#### 1.2 Como a exposição poderia agir `{#sec-como-agiria}` (cerca de 320)

- **1.2-P1** (cerca de 110). Função: conceitos (M03, M04). Conteúdo, só com o que `revisoes_anteriores.md` marca como verificado em @Barnfield2019: *bandwagon* como mudança individual da escolha de voto ou da decisão de comparecer na direção de quem está mais popular ou ganhando popularidade, motivada por essa popularidade; *underdog* como o padrão oposto; o voto estratégico, que pode ser confundido com *bandwagon* sem que a popularidade atraia o eleitor; *bandwagon* estático (nível) e dinâmico (variação); conversão (preferência) e mobilização (comparecer); e a distinção, que Barnfield retoma de outros autores, entre *bandwagon* e o efeito "Titanic": deixar de votar porque o próprio partido não tem chance não é *bandwagon*, e por isso a desmobilização tem célula própria aqui. Fonte: `v1:L107`; `revisoes_anteriores.md` §1. Movimento: M03.
- **1.2-P2** (cerca de 120). Função: modelo lógico antes da evidência (M03; E2; SWiM item 1a). Conteúdo, fiel ao `dag_v1.mmd` (correção da v1, que punha todos os canais depois da viabilidade): ver a pesquisa atualiza a percepção de viabilidade (E1), e só o cálculo estratégico (E2) passa por ela; a heurística de consenso (E3), a conformidade ou desejo de estar com quem vence (E4), a simpatia pelo azarão (E5) e as emoções (E6) saem direto da exposição; E2 a E4 levam ao *bandwagon*, E5 ao *underdog*, e E6 tem direção ambígua; há dois efeitos não intencionais, tracejados na figura: a complacência que reduz o comparecimento (E7) e a divulgação de pesquisas enviesadas por atores interessados (E8), que age sobre o conteúdo da pesquisa; nos desenhos observacionais, o apoio latente move a pesquisa e o voto, e o interesse político e a preferência prévia movem a exposição e o voto (confundidores que o risco de viés examina); permanecer no painel é um colisor; e o apoio de hoje alimenta a pesquisa seguinte; como os canais têm sinais opostos, um efeito médio perto de zero não significa que ninguém mude de voto; o modelo é rascunho de IA aprovado no portão G2, e nenhuma seta foi conferida em texto completo. Depois do parágrafo: `@@FIGURA modelo_logico@@` (chamada `@fig-modelo-logico`). Fontes: `teoria_programa.md` §1 a §3 e §5; `dag_v1.mmd`; `v1:L131`. Movimentos: M03, E2, livro R6.13 (efeitos indesejáveis do DAG).
- **1.2-P3** (cerca de 90). Função: previsões rivais e a célula em que cada uma apareceria (M03, M04; E6, tabela de previsões; E7, direção prevista codificada antes). Conteúdo: *bandwagon* → estimativa positiva na célula principal (quem a pesquisa mostra à frente); *underdog* → negativa na célula principal; voto estratégico → célula de viabilidade (deserção para a opção mostrada como viável); *bandwagon* dinâmico → célula de *momentum*; complacência → negativa na célula de comparecimento; teorias rivais do protocolo: efeitos que se anulam no agregado, efeito só sobre a expectativa (a pesquisa muda o que o eleitor espera, não o que faz) e efeito artefatual (maior em laboratório e vinheta que em eleição real); o @qdr-glossario resume os termos e diz como ler a revisão. Depois do parágrafo: Q1. Fontes: `v1:L109`; protocolo §2 (regras de sinal e alvo); `teoria_programa.md` §5; Emendas 4b e 5. Movimentos: M03, M04.
- **Q1** `::: {#qdr-glossario}` com tabela de duas colunas ("Termo", "Como é usado nesta revisão") e a legenda como último parágrafo: "Glossário e como ler esta revisão." `tbl-colwidths="[24,76]"`. Linhas, nesta ordem:
  1. Como ler: a revisão não estima o tamanho do efeito; conta em que direção apontam os estudos de cada célula, e a certeza GRADE qualifica essa direção, não a magnitude (conteúdo de `v1:L36`).
  2. Exposição: contato com resultado de pesquisa eleitoral em quatro formatos: pesquisa pré-eleitoral; agregador ou projeção; boca de urna divulgada antes do fechamento das urnas; e, pela Emenda 1, apuração parcial oficial divulgada com a votação em curso.
  3. *Bandwagon* e *underdog*: estimativa positiva ou negativa no apoio a quem a pesquisa mostra à frente (célula principal).
  4. Viabilidade: efeito sobre opções mostradas como viáveis ou inviáveis (segundo colocado viável, terceiro sem chance, partido perto da cláusula de barreira); positivo = deserção para a opção viável.
  5. *Momentum*: pesquisa que mostra um partido ganhando ou perdendo apoio sem mostrar sua posição (Emenda 4b); positivo = a favor de quem ganha apoio.
  6. Mobilização e desmobilização: efeito sobre o comparecimento ou a intenção de comparecer; negativo = desmobilização, o efeito indesejado previsto pela teoria.
  7. Célula: formato de exposição × desfecho × comparador × alvo × classe de desenho; estudos randomizados e não randomizados nunca se juntam.
  8. Direção e "x de y": x estudos na direção positiva entre os y com direção definida; estudos nulos e mistos ficam fora do denominador; a direção vem da estimativa pontual, nunca da significância; um estudo com vários efeitos tem direção quando 70% deles apontam para o mesmo lado, e senão é misto.
  9. δ e nulo por ±δ: 2 pontos percentuais, isto é, 2 em cada 100 eleitores, convertidos em g (0,044 no apoio, 0,046 no comparecimento, 0,0573 na célula de pesquisa frente a nenhuma pesquisa); efeito com IC 95% inteiro dentro de ±δ é nulo ou trivial. Números: `v1:L376`; "2 em cada 100" é a tradução que o resumo em linguagem simples reusa.
  10. Fora da contagem: efeitos principais que não estimam o contraste da exposição (interações com moderadores contínuos, contrastes de formato da mesma previsão, alvos opostos somados) ou que aguardam conferência; entram só na narrativa e numa sensibilidade (S7).
  11. Certeza (GRADE): ⊕⊕⊕⊕ alta, ⊕⊕⊕◯ moderada, ⊕⊕◯◯ baixa, ⊕◯◯◯ muito baixa, com as frases "provavelmente", "pode" e "a evidência é muito incerta sobre".
  12. Inconclusivo: rótulo da caixa de ferramentas (regra caixa-3) para certeza muito baixa ou estudos insuficientes; não quer dizer que as pesquisas não têm efeito.
  13. Estudo e relato: um estudo pode ter vários relatos (artigo, *working paper*, tese).

#### 1.3 Por que esta revisão `{#sec-por-que}` (cerca de 240)

- **1.3-P1** (cerca de 140). Função: revisões anteriores e a lacuna (M14 no início; E2, "no systematic review has assessed"). Conteúdo: @Hardmeier2008 é um capítulo de síntese sobre efeitos de pesquisas publicadas, no *SAGE Handbook of Public Opinion Research*; sem texto aberto, não verificamos seu conteúdo, e ele serve aqui só como marco do recorte de 2010 (nenhum verbo de conclusão na frase: nada de "mostra", "conclui", "indica", "aponta", "sugere", "encontra", "revela"; nunca chamá-lo de meta-análise; a frase sobre Hardmeier termina antes das frases sobre as outras revisões, para que nenhum verbo de conclusão caia na mesma frase); @MoyRinke2012, revisão narrativa, sem método de seleção descrito, organiza os efeitos em comparecimento (mobilizador ou desmobilizador) e preferência (*bandwagon*, *underdog* e voto estratégico) e conclui que a literatura não permitia dizer qual dos dois efeitos era mais comum; @Barnfield2019, revisão conceitual, que declara não ser meta-análise nem revisão sistemática; @Cosgun2026, revisão sistemática sobre campanhas e comportamento do eleitor, numa só base e só em inglês, em que as pesquisas são uma entre várias linhas teóricas e nenhum efeito é estimado; a checagem de 19/09/2026 (OpenAlex, OSF Registries e BDTD) não achou síntese sobre o efeito de pesquisas publicadas no voto posterior a 2008 nem revisão registrada em andamento, e listou a revisão de campanhas como periférica. Fontes: `revisoes_anteriores.md` §1 a §4 (só o marcado como verificado); protocolo, tabela de revisões existentes; `pergunta.md` §4. Movimentos: M14, E2, E4 ("extant reviews did not...").
- **1.3-P2** (cerca de 100). Função: contribuições numeradas (M02; E7). Conteúdo: "Esta revisão faz três contribuições": (i) a primeira síntese com protocolo congelado e busca documentada da evidência causal publicada desde 2010; (ii) a separação da evidência em células, que distingue *bandwagon* de voto estratégico e de *momentum* e nunca junta sorteio com observação, com risco de viés por desenho e certeza por célula; e (iii) uma leitura dirigida ao debate brasileiro, com os fatores de transferibilidade fixados no protocolo; uma frase final honesta: é também um rascunho produzido por agentes de IA, e tudo o que vem depois do protocolo espera validação humana. Movimento: M02.

#### 1.4 Objetivos `{#sec-objetivos}` (cerca de 140)

- **1.4-P1** (cerca de 70). Função: objetivo explícito (PRISMA item 4). Conteúdo: a pergunta principal, literal do protocolo [7] ("A exposição a resultados de pesquisas eleitorais publicadas altera a intenção ou a escolha de voto do eleitorado, em comparação com a não exposição ou com a exposição a outro resultado, e em que direção (*bandwagon* ou *underdog*)?"); perguntas secundárias: se reduz o comparecimento (o efeito indesejado, a desmobilização), por quais mecanismos, para quem, onde e quando, e se os achados diferem entre Brasil e América Latina e as demais regiões; é avaliação *ex post* de um fenômeno, não de um programa. Fontes: protocolo [7]; `v1:L113`. Movimento: livro R1.7 (item 4).
- **1.4-P2** (cerca de 70). Função: a resposta no fim da introdução, antes dos Métodos (M01, critério b), e o roteiro (voz do autor). Conteúdo: "De forma antecipada, ..." nos experimentos, a direção é *bandwagon*, com certeza muito baixa e sem estimativa de tamanho; no comparecimento, uma pesquisa apertada, frente a uma folgada, provavelmente não muda o comparecimento além de ±2 pontos percentuais (certeza moderada), e os demais achados são de certeza baixa ou muito baixa; não há estudo de pesquisas com dados só do Brasil; roteiro: métodos (@sec-metodos), resultados (@sec-resultados), discussão (@sec-discussao), implicações (@sec-pratica) e conclusões (@sec-conclusoes). Movimento: M01.

### 3.7 Seção 2: Métodos `{#sec-metodos}` (cerca de 2.150)

Regra da seção: passado, o que esta revisão fez, com os parâmetros de cada etapa (quem, quantos, com que concordância, com que ferramenta e versão; livro R4.3 e A15). Nada de explicação didática do método.

#### 2.1 Protocolo, tipo de revisão e desvios `{#sec-protocolo}` (cerca de 330)

- **2.1-P1** (cerca de 100). Função: conformidade e tipo (livro R1.1 a R1.3; frase-modelo M1). Conteúdo: o protocolo foi aprovado pelo autor no portão G2 em 19/09/2026 e congelado com sha256 no *log* do projeto, sem registro; revisão sistemática de efetividade com síntese sem meta-análise (SWiM), na variante rápida; relato pelo PRISMA 2020 [@Page2021PRISMA; @Page2021PRISMAEE], pelo PRISMA-S na busca [@Rethlefsen2021PRISMAS] e pelo SWiM nas sínteses [@Campbell2020SWiM], com o PRISMA-trAIce só como lista de conferência; checklists com o local de cada item em [S11](suplemento.html#s11-checklists); estrutura de relato OQF [@Schaefer2025OQF; @Lamarca2026Livro], acrescida da Discussão das revisões Campbell e Cochrane (acréscimo declarado); a variante rápida foi escolha do autor para cortar etapas: não houve prazo externo nem consulta a *stakeholders*, que a diretriz de revisões rápidas associa a esse tipo de revisão [@Garritty2024Rapid]. Fontes: `v1:L303`; protocolo [1a], [2]; `garritty_2024.md` §5. Movimentos: frase-modelo M1; livro R1.1, R1.3; Garritty rec. 24.
- **2.1-P2** (cerca de 150). Função: cada atalho com a recomendação literal de Garritty et al. (plano; M12). Conteúdo, citando as recomendações em inglês, entre aspas, com o número (`garritty_2024.md` §3 e §4):
  - A1, fontes restritas a OpenAlex e BDTD, mais busca por citação: recomendação 5, "Select a small number (but at least two) bibliographic databases that are likely to contain relevant literature", atendida no limite, porque a BDTD é catálogo de teses; recomendação 7, "Assess the need for grey literature and supplemental searching. Justify the sources to be searched", atendida;
  - A2, triagem, elegibilidade, extração, risco de viés e certeza por agentes de IA, sem validação humana: as recomendações 9, 12, 16 e 23 pedem uma segunda pessoa (por exemplo, a 16, "Have one person perform the risk of bias assessment, with a second person verifying the judgements"); o A2 não corresponde a nenhum atalho aceito pela diretriz;
  - A3, âncoras de validação montadas por subagente isolado: nenhuma recomendação correspondente;
  - A4, PRESS só por subagente: recomendação 6, "Use the PRESS checklist to peer review the primary search strategy", atendida só na forma mínima que a própria recomendação admite; a recomendação 4, de envolver um especialista em informação, não foi seguida nem declarada como atalho;
  - A5, sem contato com autores: nenhuma recomendação correspondente.

  Escrever em prosa com "(i) ... (v)", não em lista. Cruzamento completo, com a consequência provável de cada atalho, em [S2](suplemento.html#s2-atalhos). Não citar a versão da recomendação 9 com percentual e κ (números fora da lista branca).
- **2.1-P3** (cerca de 80). Função: desvios com o momento (M12; SWiM item 1b; E2, "without consideration of study results"). Conteúdo: duas contingências previstas (E001 e E002) antes da triagem; convenções fixadas antes de qualquer análise de efeito (Emendas 3 e 4); decisões tomadas depois de ver dados (Emendas 1, 2, 5 e 6b); em particular, a estrutura de células que organiza os resultados, com o alvo do efeito como quinta dimensão, e a lista de efeitos fora da contagem foram fixadas pela Emenda 5, depois de ver a primeira síntese, e por isso o agrupamento amplo é só descritivo; detalhes em [Informações adicionais](#informacoes-adicionais) e em [S3](suplemento.html#s3-emendas). Fonte: `emendas.md` (tabela-resumo); `v1:L305` a `v1:L312`.

#### 2.2 Critérios de elegibilidade `{#sec-elegibilidade}` (cerca de 130)

- **2.2-P1** (cerca de 130). Função: critérios completos (PRISMA item 5). Conteúdo: os critérios C1 a C6 (população e contexto; exposição estudada como objeto empírico; desfecho de voto ou de comparecimento; desenho experimental, experimento natural, quase-experimento com variação identificada ou painel individual com exposição medida antes do desfecho; estudo primário; sem retratação), resumidos no @qdr-picoc; ficaram de fora a percepção autodeclarada de influência, simulações, estudos agregados sem variação identificada e estudos que usam a pesquisa só como fonte de dados; relatos publicados desde 01/01/2010 (ano de publicação do OpenAlex; ano de defesa na BDTD), justificado pela mudança do ambiente informacional; sem restrição de idioma nem de status de publicação; texto não obtido ficou como não recuperado, nunca como excluído; a Emenda 1 acrescentou a apuração parcial oficial depois de conhecer o estudo brasileiro; o agrupamento das sínteses está em @sec-sintese. Fonte: `v1:L316`; protocolo §4. Depois do parágrafo: Q2.
- **Q2** `::: {#qdr-picoc}` com a tabela de `v1:L115` a `v1:L121` (População; Exposição; Comparador; Desfechos; Contexto), legenda como último parágrafo: "Pergunta e critérios no formato PICOC (protocolo, seções 2 e 4)." `tbl-colwidths="[18,82]"`. Sem caminho de arquivo na legenda.

#### 2.3 Fontes e busca `{#sec-busca}` (cerca de 250)

- **2.3-P1** (cerca de 140). Função: fontes, datas, filtros e deduplicação (PRISMA itens 6 e 7; PRISMA-S 8, 13, 15 e 16; livro R4.4). Conteúdo: OpenAlex, título e resumo: inglês (B05, 1.438 registros), português (B02, 118) e espanhol (B03, 131); BDTD, todos os campos (B04, 80); todas em 19/09/2026; quatro fios unidos por OR (pesquisa ou projeção com efeito nomeado; *survey* eleitoral com efeito nomeado; exposição a resultado de pesquisa com desfecho de voto; exposição com comparecimento); no OpenAlex, filtro de ano de 2008 a 2026, com o corte de 2010 aplicado depois por *script*; busca por citação para trás e para frente no OpenAlex em três rodadas: SN1 (38 sementes, 1.189 registros, 19/09/2026), SN2 (12, 411, 20/09/2026) e SN3 (3, 106, 20/09/2026), com os incluídos e as revisões achadas como sementes; a busca B01 foi substituída pela B05 (E002) e seus 1.235 registros ficaram fora dos identificados; sem Web of Science, Scopus, SciELO, sites de literatura cinzenta nem contato com autores; deduplicação por *script* da ferramenta da revisão, com os pares incertos deixados sem decisão; estratégias completas, como executadas, em [S1](suplemento.html#s1-busca). Números: `v1:L320`, `v1:L342`. Movimento: livro R4.4.
- **2.3-P2** (cerca de 110). Função: validação da busca e lacunas conhecidas. Conteúdo: 19 âncoras montadas por subagente isolado (A3): 15 de 19 recuperadas na versão v4 e 19 de 19 na v5; como as 4 perdidas orientaram a correção, o *recall* final não é evidência independente; não houve âncora em português ou espanhol; uma pré-revisão por IA da estratégia ativa, em 23/09/2026, apontou lacunas: não há termos de proibição ou embargo de divulgação nem de apuração parcial (@Lago2015 e @Araujo2021a só vieram pela busca por citação), o fio de comparecimento é estreito, e a BDTD não tem termo de comparecimento. Fonte: `v1:L322`; relatório técnico, seção 23c (`07-relatorio/relatorio.qmd`, "Âncoras e PRESS"). Números: `v1:L322`.
- **CO-busca** {P001, P004}: "A estratégia de busca não teve revisão PRESS humana (P001), e o portão G3, que aprovou a busca, espera confirmação (P004). Uma busca suplementar com os termos que faltam pode mudar o conjunto de estudos incluídos." Fonte: `v1:L327`.

#### 2.4 Seleção dos estudos `{#sec-selecao}` (cerca de 260)

- **2.4-P1** (cerca de 110). Função: automação separada da triagem por IA (livro R5.2 e R7.20; PRISMA item 8). Conteúdo: antes da triagem, *scripts* removeram duplicados (46 nas bases e 4 nos outros métodos) e os relatos publicados antes de 2010 (148 e 648; 796 no total), exclusão determinística por metadado prevista no protocolo; na triagem de títulos e resumos, dois triadores de IA independentes (A = `claude-sonnet-5`; B = `claude-opus-5`) aplicaram critérios versionados, pela regra liberal (bastava um incluir ou marcar incerto para o registro seguir); nenhuma pessoa triou; as 81 divergências ficaram na fila humana, sem arbitragem; concordância A × B na primeira onda de 0,97 (κ 0,90; PABAK 0,94), que mede consistência entre agentes, não acurácia; o *recall* não foi calculado, porque as amostras de validação (141 registros) e de elusão (300) não foram codificadas por humanos. Números: `pr:bases.removidos_antes_triagem.duplicatas`, `pr:outros_metodos.removidos_antes_triagem.duplicatas`, `n2:excluidos_filtro_ano_bases`, `n2:excluidos_filtro_ano_outros_metodos`, `n2:excluidos_filtro_ano_total`, `v1:L332`, `pend:P006.n`, `pend:P007.n`, `pend:P020.n`.
- **2.4-P2** (cerca de 70). Função: a triagem complementar (Emenda 6b). Conteúdo: os 336 registros sem resumo, antes excluídos pelo título sem conferência do autor, foram triados de novo por dois triadores de IA (A = `claude-sonnet-5`; B = `claude-opus-5-5`), com o resumo recuperado em fontes legítimas para 172; um registro só era excluído se os dois excluíssem, com trecho literal do resumo; 156 exclusões e 180 registros ao texto completo; dos 180, 15 foram recuperados e avaliados, e os 15 foram excluídos; os outros 165 ficaram como não recuperados; o autor dispensou a conferência humana dessa etapa. Números: `v1:L334`.
- **2.4-P3** (cerca de 80). Função: texto completo. Conteúdo: um subagente de IA por PDF propôs a elegibilidade com trecho literal e página, conferidos por *script*, e ficha reprovada foi refeita por outro subagente; o autor decidiu 17 casos limítrofes; em 3 casos a IA estendeu a caso novo uma regra que ele tinha decidido para outro grupo; as 165 decisões propostas a partir das fichas (47 de inclusão e 118 de exclusão) aguardam conferência; relatos do mesmo estudo foram ligados antes da extração e as retratações checadas; PDFs só de fontes legítimas: nenhum por Sci-Hub ou fonte não autorizada. Números: `v1:L336`, `pend:P041.n`.
- **CO-selecao** {P006, P007, P008, P019, P020, P023, P041}: "A seleção não tem validação humana: faltam revisar os 145 pares candidatos de duplicata (P019), resolver as 81 divergências da triagem (P020), codificar às cegas as amostras de validação e de elusão (P006 e P007), conferir as 165 decisões de elegibilidade (P041) e confirmar os portões G4 e G5 (P008 e P023). Qualquer uma pode mudar o conjunto de incluídos." Fonte: `v1:L347`.

#### 2.5 Extração `{#sec-extracao}` (cerca de 250)

- **2.5-P1** (cerca de 90). Função: quem extraiu e como (PRISMA itens 9 e 10). Conteúdo: *codebook* com variáveis próprias desta literatura (realismo do contexto, comparador, alvo do efeito, sistema eleitoral, voto obrigatório, região, ano da eleição); piloto com três estudos [@Meer2015a; @Klor2017a; @Araujo2021a], que levou à Emenda 2, decidida pelo coordenador de IA; na rodada completa, um subagente `claude-opus-5` por texto, com trecho literal e página por variável, conferidos por *script*; 560 efeitos de 40 estudos, 70 deles principais; regra de modelo principal escrita antes da extração: o declarado pelos autores; na falta, o usado na interpretação; por último, a regra do protocolo; nunca o de menor valor-p; um segundo subagente (`claude-sonnet-5`) recodificou às cegas 10 estudos sorteados, com 58,5% de concordância em 560 comparações e 37 variáveis abaixo do limiar do protocolo; não houve contato com autores (A5). Números: `v1:L352`, `n1:efeitos`, `n1:estudos_com_efeitos`, `n1:efeitos_principais`.
- **2.5-P2** (cerca de 80). Função: conversões e pressupostos (SWiM item 2; livro R4.5 ii; plano: "conversões, ICC 0,05 imputado, efeitos lidos de figura"). Conteúdo: g de Hedges; proporções, pontos percentuais e razões de chances convertidos pelo log da razão de chances com a proporção do grupo de comparação (d = ln(OR)·√3/π), com as conversões aproximadas marcadas; logit que não relatou efeito marginal convertido por OR = exp(β); probit que não o relatou, só na direção; estudos sem t, β ou r receberam o sinal pelos pontos percentuais, por p1 − p0 ou por ln(OR), só para a direção; desenhos com conglomerado sem ICC relatado: variância multiplicada pelo efeito de desenho, com ICC imputado de 0,05 (Emenda 4c) e sensibilidade em 0,20; os dois efeitos principais de @Tyszler2015 foram lidos de figura, assim como a proporção de referência de @Brugarolas2021; o n por célula foi derivado em @Lammers2022a e @Meffert2011, e o efeito de @Kaplan2019a é valor derivado. Fontes: `07-relatorio/relatorio.qmd` itens 10b, 12 e 13b; `v1:L376`, `v1:L402`.
- **2.5-P3** (cerca de 80). Função: reextração cega e arbitragem. Conteúdo: antes da síntese, um subagente `claude-opus-5-5` reextraiu às cegas os efeitos do modelo principal dos 40 estudos com dados; nos 56 efeitos principais originais, 15 concordaram, 23 tinham o mesmo valor com classificação diferente, 12 tinham outro valor e 6 tinham sinal diferente; nos 28 estudos com divergência, um árbitro de IA do mesmo modelo, um PDF por agente, decidiu pelo texto, com trecho e página; o coordenador aplicou 772 correções, 240 delas estendidas a linhas análogas sem nova arbitragem, e barrou 40 que dependiam de um erro dele no *prompt* do árbitro. Números: `v1:L354`, `v1:L432`. Usar 772 (verificado contra o arquivo de correções), não 771.
- **CO-extracao** {P025, P026, P037, P039}: "Nenhum dos 560 efeitos foi conferido por humano na página do texto completo (P039). Faltam arbitrar as 259 divergências da recodificação cega (P037), conferir o piloto (P025) e confirmar o portão G6 (P026)." Fonte: `v1:L359`.

#### 2.6 Risco de viés `{#sec-rob-metodos}` (cerca de 170)

- **2.6-P1** (cerca de 170). Função: relato mínimo do risco de viés (livro R4.15 e R4.16; PRISMA item 11). Conteúdo: RoB 2 para experimentos aleatorizados, com a variante por conglomerado [@Sterne2019RoB2]; ROBINS-I V2, versão ainda em rascunho, para experimentos naturais, quase-experimentos com dados individuais e painéis [@Sterne2016ROBINSI; @Sterne2025ROBINSIV2]; para exposição não atribuída, a ferramenta canônica seria o ROBINS-E, que a ferramenta da revisão não tinha, e isso fica como limitação; critérios EPOC para proibições e embargos com unidades agregadas [@EPOC2017RoB], com sequência e ocultação fora do julgamento geral (Emenda 4a); *codebooks* copiados para o protocolo antes de qualquer avaliação, com os confundidores do modelo lógico (Emenda 3); dois avaliadores de IA independentes (A = `claude-opus-5-5`; B = `claude-sonnet-5`), com trecho literal e página; concordância → consenso automático; desacordo → árbitro de IA do mesmo modelo do avaliador A, em contexto novo, escolhido pelo autor por custo no lugar do previsto no protocolo (Emenda 3); nenhum julgamento foi validado por humano; resultados em risco crítico ficaram fora da análise principal e entraram numa sensibilidade, e o risco de viés entrou no domínio correspondente do GRADE. Fontes: `v1:L364` (parte de método); relatório técnico, item 11; protocolo §7. Movimento: livro R4.15. A frase-modelo M16 do livro ("todos os julgamentos foram humanos") não se aplica e não aparece.

#### 2.7 Síntese `{#sec-sintese}` (cerca de 370)

- **2.7-P1** (cerca de 70). Função: agrupamento (SWiM item 1a; livro R4.11; frase-modelo M13). Conteúdo: célula = formato de exposição × desfecho × comparador × alvo (principal, viabilidade, *momentum*, mobilização) × classe de desenho; randomizados e não randomizados nunca juntos; contrastes antes e depois no mesmo sujeito na classe não randomizada (Emenda 5); o alvo separa *bandwagon*, voto estratégico e *momentum*, como prevê o modelo lógico (@sec-como-agiria); a estrutura foi fixada depois de ver a primeira síntese, e o agrupamento amplo (desfecho × alvo × classe) é só descritivo. Fonte: `v1:L374`; Emenda 5, itens 1 e 6.
- **2.7-P2** (cerca de 60). Função: métrica e sinal (SWiM item 2; M04). Conteúdo: g de Hedges alinhado à convenção de cada alvo: na célula principal, positivo = *bandwagon* e negativo = *underdog*; na viabilidade, positivo = mais apoio à opção mostrada como viável ou menos à mostrada como inviável; no *momentum*, positivo = a favor do partido mostrado ganhando apoio; no comparecimento, positivo = mobilização; nos desenhos de proibição [@Chatterjee2019a; @Morton2015a], o efeito da proibição foi reorientado para o da exposição; a convenção é técnica, sem juízo normativo. Fonte: `v1:L374`; relatório técnico, item 12.
- **2.7-P3** (cerca de 140). Função: método, o que ele responde e a ressalva do teste de sinal (SWiM itens 3 e 4; livro R4.6, R4.8, R4.9, R5.16, R5.18 e A25; E1 item 9). Conteúdo: contagem pela direção da estimativa pontual, nunca pela significância [@Boon2021EffectDirection]; regra de 70% para dar direção a um estudo com vários efeitos; proporção de estudos na direção positiva, com IC 95% exato de Clopper-Pearson [@Clopper1934IC], e teste de sinal binomial exato bilateral [@Nikolakopoulos2020SignTest]; a pergunta que o método responde é se há evidência de efeito numa direção, e não qual é o efeito médio [@Campbell2020SWiM]; limiar de relevância δ = 2 pontos percentuais, convenção do protocolo sem *benchmark* de campo, convertido em g: 0,044 no apoio (referência 0,50), 0,046 no comparecimento (referência 0,60) e 0,0573 na célula de pesquisa frente a nenhuma pesquisa (mediana das proporções de comparação da célula; não escrever o valor da mediana, que não está na lista branca); efeito com IC 95% inteiro dentro de ±δ foi classificado como nulo; prioridade (SWiM item 4): a análise principal excluiu os resultados em risco crítico, como previa o protocolo, e os efeitos principais que não estimam o contraste da exposição ou aguardam conferência, decisão da Emenda 5, tomada depois de ver os dados (lista com o motivo em [S7](suplemento.html#s7-fora-da-contagem)); por fim, a ressalva do teste de sinal, adaptada do livro sem as palavras proibidas: o teste combina direções e não informa a magnitude; não distingue estudos grandes com efeitos pequenos de estudos pequenos com efeitos grandes; com p < 0,05, indicaria apenas que a proporção de estudos numa direção difere de metade; com poucos estudos pequenos, p acima de 0,05 não indica ausência de efeito; é análise secundária e não define rótulo. Números: `v1:L376`; `parametros.delta` dos dois `meta_resumo.json` (0,0573 e 0,044).
- **2.7-P4** (cerca de 60). Função: metas exploratórias (livro R4.5 iii e iv, R5.26 a R5.30, A26). Conteúdo: nas duas células com 3 estudos com g, meta-análise exploratória por modelo CHE (REML) com variância robusta CR2 e graus de liberdade de Satterthwaite, ρ = 0,6 com sensibilidade em 0,2, 0,5 e 0,8, e graus de liberdade abaixo de 4 lidos como inferência não confiável [@Pustejovsky2022CHE]; metafor 5.0.1 [@Viechtbauer2010Metafor] e clubSandwich [@Pustejovsky2026ClubSandwich]; τ², τ, I² e intervalo de predição relatados, mas não interpretados com k < 5; frase literal: "Com menos de dez estudos por célula, não testamos assimetria."; a certeza de cada meta é a da célula. Números: `v1:L378`, `n1:meta.rho`; `parametros.pacotes.metafor` do `meta_resumo.json`.
- **2.7-P5** (cerca de 40). Função: heterogeneidade, sensibilidade e gráficos (SWiM itens 5 e 7; livro R5.24). Conteúdo: moderadores pré-especificados, mas nenhuma célula teve 3 estudos por nível, e a comparação ficou descritiva, sem teste; sensibilidades: com os críticos e com ICC de 0,20 (células do protocolo); só contexto real, sem dados anteriores a 2010, sem @Araujo2021a e com os efeitos fora da contagem (agrupamento amplo, *post hoc*); nas metas, *leave-one-out*, ρ e ICC; gráficos: proporção por célula (@fig-celulas), direção por estudo ordenada por célula, desenho e risco de viés, com símbolo de tamanho constante porque os n estão em unidades diferentes, desvio declarado do *effect direction plot*, e *forest plots* sem diamante de predição.

#### 2.8 Certeza da evidência `{#sec-certeza}` (cerca de 210)

- **2.8-P1** (cerca de 150). Função: métodos de certeza (livro R4.19 a R4.22; frase-modelo M11). Conteúdo: GRADE por célula [@Guyatt2008GRADE], com randomizados e não randomizados em corpos separados e os domínios adaptados para síntese sem meta-análise [@Murad2017GRADE]; pontos de partida: randomizados em alta; não randomizados avaliados com ROBINS-I V2 em alta, com rebaixamento por risco de viés; corpos avaliados só com EPOC em baixa; célula com as duas ferramentas em baixa; indireção pelo contexto eleitoral, pelo realismo e pelo estimando; inconsistência pela coerência das direções; imprecisão pelo número de estudos e de participantes e pela largura do IC da proporção, frente a δ; viés de publicação pela limitação de fontes, pela triagem complementar só por IA, pela ausência de nulos e pelo tamanho dos estudos; um subagente (`claude-opus-5-5`) rascunhou os juízos em 24/09/2026, sem segundo avaliador, com cada rebaixamento justificado por escrito (notas da Tab. 2); a certeza qualifica a direção, não a magnitude, e na célula com efeito nulo por ±δ qualifica a classificação como nulo ou trivial; enunciados pelas frases padronizadas [@Santesso2020GRADE]. Fonte: `v1:L382`; relatório técnico, item 15.
- **2.8-P2** (cerca de 60). Função: regra de rótulos versionada (livro R5.49 a R5.51; frase-modelo M4). Conteúdo: a caixa de ferramentas usa a regra caixa-3 [@Schaefer2025OQF; @Lamarca2026Livro], aplicada por *script* à mesma tabela de achados, nesta ordem: Pendente (sem certeza); Inconclusivo (certeza muito baixa); Misto (só com meta-análise de pelo menos 5 estudos, intervalo de predição além de ±δ dos dois lados e explicação com certeza própria); Positivo ou Negativo (com meta-análise, IC inteiro de um lado de zero e certeza pelo menos baixa; sem meta-análise, teste de sinal com p < 0,05, pelo menos 5 estudos, pelo menos 70% numa direção, não só estudos em risco alto e certeza pelo menos baixa); Nulo (meta-análise com IC inteiro dentro de ±δ e certeza pelo menos moderada); Inconclusivo nos demais casos; a "Força" da caixa é a certeza, não o tamanho. Fonte: `v1:L255` a `v1:L261`.
- **CO-certeza** {P035, P036, P042}: "Nenhum juízo GRADE foi validado por humano (P036 e P042), e o portão G8 espera confirmação (P035). O rascunho deixou três decisões para o autor, descritas na @sec-limitacoes-processo." Fonte: `v1:L387`.

#### 2.9 Uso de IA e supervisão humana `{#sec-ia}` (cerca de 180)

- **2.9-P1** (cerca de 100). Função: plano e papéis (livro R7.17, R7.20). Conteúdo: um coordenador de IA, o Claude Opus 5.5 (`claude-opus-5-5`), executou os *scripts* da ferramenta de revisão sistemática no Claude Code e distribuiu o trabalho entre subagentes, com os modelos por etapa dados em 2.4 a 2.8; o único humano, o autor, aprovou a pergunta e o protocolo (portões G1 e G2), decidiu as Emendas 1, 4 (itens 4a a 4c) e 6b e 17 casos limítrofes de elegibilidade, e escolheu por custo o árbitro do risco de viés (Emenda 3); os portões G3 a G9 foram aprovados em autopiloto quando as checagens do *script* passaram, e cada aprovação abriu uma pendência humana; em 23/09/2026, o autor declarou que não tinha conferido decisões que o *log* registrava como dele, e a Emenda 6a corrigiu a atribuição. Fonte: `v1:L392`; `emendas.md`, Emenda 6a.
- **2.9-P2** (cerca de 80). Função: agentes desta versão e o estatuto do produto (livro R7.18, R7.24, R7.28). Conteúdo: a reescrita de 24/09/2026 e 25/09/2026 usou subagentes Opus (`claude-opus-5-5`) para ler as regras do livro, as revisões exemplares, a diretriz de revisões rápidas e as revisões anteriores, só em textos abertos e legítimos, e para escrever a especificação, o corpo, a abertura, as figuras e as tabelas; um subagente Sonnet conferiu as referências de método no Crossref; subagentes Opus fizeram a verificação independente, uma rubrica cega e duas leituras críticas simuladas (editor de métodos e cientista político), que não substituem a leitura do autor nem validam nada; os números foram conferidos por programas contra os arquivos; pelo critério do livro que orienta esta revisão, um produto executado de ponta a ponta por agentes não conta como revisão sistemática concluída, e por isso este texto sai como rascunho. Acrescentar logo depois do parágrafo o comentário `<!-- coordenador: conferir ao fim da etapa 7 os agentes e as etapas efetivamente rodados -->`. Fontes: plano, "Etapas"; cabeçalhos dos insumos da etapa 0b. Não dar versão ao Sonnet (não registrada).

### 3.8 Seção 3: Resultados `{#sec-resultados}` (cerca de 3.480)

Regra da seção: observação antes da interpretação; em cada célula, os estudos que contribuem com desenho e risco de viés, o achado em linguagem coerente com a pergunta e a certeza (SWiM item 8; M06). A ordem de 3.4 a 3.7 é C01 a C18, a mesma da Tab. 2 e da Fig. 4 (SWiM item 7): se a tabela montada vier em outra ordem, o redator avisa o coordenador e não reordena o texto.

#### 3.1 Estudos incluídos `{#sec-incluidos}` (cerca de 350)

- **3.1-P1** (cerca de 140). Função: fluxo (PRISMA item 16a; livro A1; frase-modelo M2). Conteúdo, pelos números do `prisma_contagens.json`: a busca identificou 1.767 registros nas bases (1.687 no OpenAlex e 80 na BDTD) e 1.706 por busca de citação; antes da triagem, foram removidos 46 e 4 duplicados e 148 e 648 relatos pelo filtro de ano; os triadores de IA triaram 1.573 e 1.054 registros e excluíram 1.314 e 787; buscamos o texto completo de 259 e 267 relatos, não recuperamos 158 e 184 (342 de 526), avaliamos 101 e 83 e excluímos 59 e 70, a maior parte por exposição fora do critério C2 (39 e 50), seguida de população ou contexto (8 e 13), desenho (10 e 4) e desfecho (2 e 3); incluímos 41 estudos em 55 relatos (42 das bases e 13 dos outros métodos); os 1.235 registros da busca substituída ficaram fora; na triagem complementar, os 15 registros recuperados foram excluídos e 165 ficaram como não recuperados (@fig-prisma). Depois do parágrafo: `@@FIGURA prisma@@`. Números: `pr:bases.*`, `pr:outros_metodos.*`, `pr:incluidos.*`, `pr:buscas_inativas.n_registros`, `n2:relatos_nao_recuperados_total`, `n2:relatos_buscados_total`, `v1:L334`.
- **3.1-P2** (cerca de 70). Função: estudos que pareciam elegíveis e foram excluídos (PRISMA item 16b). Conteúdo, por sobrenome e ano, sem `@` (não estão nas referências porque foram excluídos): experimentos de laboratório em que o participante vê a contagem de votos ou o placar do próprio jogo, e não uma pesquisa (Scheuerman 2019, 2020 e 2021; Yosef 2017; Bischoff 2012; Hizen 2025; Morton 2015b; C2); um experimento natural no Peru em que a divulgação juntava boca de urna e contagem parcial oficial, sem separar as fontes (Reveco 2026; C2, decisão do autor); um artigo que não analisa o experimento de exposição que menciona (Corbetta 2013; C2); um estudo de efeito de terceira pessoa (Kim 2018b; C3); jogos em equipe sem escolha eleitoral (Kim 2025a; C1); e estudos com a pesquisa como medida agregada, sem variação identificada (Freden 2021; Mavridis 2016a; C4). Fonte: `07-relatorio/relatorio.qmd`, "Seleção dos estudos", terceiro parágrafo.
- **3.1-P3** (cerca de 90). Função: características (PRISMA item 17). Conteúdo: publicados de 2010 a 2024; 14 experimentos de *survey*, 9 de laboratório com preferências induzidas, 3 de laboratório com candidatos reais, 1 experimento de campo, 6 experimentos naturais, 3 painéis individuais e 5 outros desenhos; exposição: pesquisa pré-eleitoral em 33, agregador ou projeção em 4, boca de urna em 3 e apuração parcial em 1; contexto real em 25, induzido em 9 e hipotético em 7; 32 eleições com candidatos ou partidos, 8 simuladas e 1 referendo; só apoio em 24, só comparecimento em 10 e os dois em 7; quanto à região, 1 estudo do Brasil, 1 do México, 1 multinacional que inclui o Brasil, 1 sem região informada e 37 de outras regiões, sobretudo Estados Unidos e Europa (@tbl-caracteristicas; estudo a estudo em [S4](suplemento.html#s4-caracteristicas)). Depois do parágrafo: `@@TABELA caracteristicas@@`. Números: `n1:ano_min`, `n1:ano_max`, `n1:desenho.*`, `n1:familia.*`, `n1:realismo.*`, `n1:eleicao.*`, `n1:construto.*`, `n1:regiao.*`.
- **3.1-P4** (cerca de 50). Função: destino de cada estudo e os que não contribuem, com nome (plano; livro R5.8). Conteúdo: 27 entram na síntese principal; 14 não contribuem para a contagem: 3 em risco de viés crítico [@Gasperoni2015a, também fora da contagem; @Kaplan2019a; @Unkelbach2022a], 7 com todos os efeitos principais fora da contagem [@Alabrese2024a; @Bursztyn2023a; @Gandhi2019; @Geers2018; @Lago2015; @Meffert2011; @Urminsky2019] e 4 que não têm efeito principal extraído [@Freden2016b, cujo PDF é só o capítulo introdutório da tese; @Meffert2012a; @Tyszler2013; @Yang2023d]; eles entram na leitura de mecanismos e moderadores e nas sensibilidades. Números: `n1:n_swim_principal_estudos`, `n2:estudos_fora_da_sintese_principal`, `n2:estudos_risco_critico`, `n2:estudos_so_fora_da_contagem`, `n2:estudos_sem_efeito_principal`. Escrever "não têm efeito principal extraído", nunca a sequência proibida "sem efeito".

#### 3.2 Risco de viés nos estudos `{#sec-rob}` (cerca de 200)

- **3.2-P1** (cerca de 200). Função: risco de viés por estudo e por síntese (PRISMA item 18; livro R5.8, R5.11, frase-modelo M15). Conteúdo: 43 resultados de 37 estudos: 23 com RoB 2 (17 com algumas preocupações e 6 em risco alto), 13 com ROBINS-I V2 (2 moderado, 8 grave e 3 crítico) e 7 com EPOC (6 alto e 1 baixo), somando o total avaliado; nenhum resultado randomizado ficou em risco baixo; o domínio de relato seletivo teve algumas preocupações em 21 dos 23 resultados do RoB 2; nos não randomizados, o confundimento foi grave ou crítico em 11 dos 13; por síntese: os 4 estudos da célula do mesmo candidato atrás estão em risco alto, e os 4 da célula sem pesquisa, em algumas preocupações; dos 259 domínios julgados, 171 tiveram consenso automático e 88 foram arbitrados; o árbitro seguiu o avaliador A em 79, B em 7 e propôs terceiro valor em 2, e como A e o árbitro são o mesmo modelo, pode haver viés de afinidade (@fig-rob; domínio a domínio em [S5](suplemento.html#s5-risco-de-vies)). Depois do parágrafo: `@@FIGURA rob@@`. Números: `n1:rob_resultados`, `n1:rob_estudos`, `n1:rob_por_ferr.*`, `n1:rob2_D5_algumas`, `n1:robins_D1_grave_critico`, `n1:rob_dominios.*`, `n1:arbitro_segue.*`, `cel:C01.k`, `cel:C02.k`. Parágrafo sem span de célula.
- **CO-rob** {P033}: "Nenhum dos 259 julgamentos de risco de viés foi validado por humano, e o portão G7 espera confirmação (P033). A arbitragem dos efeitos apontou um caso para essa revisão: em @Fichnova2015a, 17 dos 37 respondentes eslovacos não aparecem nas tabelas, e o domínio de dados faltantes foi julgado baixo." Fonte: `v1:L369`.

#### 3.3 Visão geral da síntese `{#sec-efeito}` (cerca de 260)

- **3.3-P1** (cerca de 110). Função: mapa da evidência (M11). Conteúdo: dos 41 estudos, 40 têm efeitos extraídos (560) e 37 têm ao menos um efeito principal; a síntese principal reúne 27 estudos em 18 células com estudo; uma 19.ª célula (projeção × comparecimento × sem pesquisa × não randomizado) ficou vazia depois da exclusão de @Kaplan2019a, em risco crítico; nenhuma célula tem mais de 4 estudos; das 18, 15 ficaram com certeza muito baixa, 2 com baixa e 1 com moderada; a @tbl-sof dá, por célula, a comparação, os estudos, a direção (x de y, com o IC), a certeza e o enunciado; o agrupamento amplo, decidido depois de ver os dados, ficou fora dela (@sec-sensibilidades e [S8](suplemento.html#s8-sensibilidades)). Depois do parágrafo: `@@TABELA sof@@`. Números: `v1:L135`, `n1:swim_principal_grupos`, `n1:swim_principal_celulas_com_estudo`, `n1:certeza_contagem.*`. Parágrafo sem span. Escrever "19.ª" ou "a célula restante"; evitar "x de y".
- **3.3-P2** (cerca de 90). Função: ler as figuras (livro R5.24; "Note que"). Conteúdo: a @fig-celulas mostra, por célula, a proporção de estudos na direção positiva com o IC de Clopper-Pearson e a certeza; células só com nulos ganham marca própria ("nulo por ±δ"); a @fig-direcao mostra a direção de cada estudo, ordenada por célula, desenho e risco de viés, com um painel à parte, *post hoc*, para os efeitos fora da contagem (os efeitos individuais estão em [S6](suplemento.html#s6-efeitos)); note que a proporção conta estudos, não participantes, e que o tamanho do símbolo é constante. Depois do parágrafo: `@@FIGURA celulas@@` e `@@FIGURA direcao@@`, cada um em linha própria.
- **3.3-P3** (cerca de 60). Função: a ressalva do teste de sinal aplicada aos números (livro R5.18 e A25; M09). Conteúdo: remeter à ressalva de @sec-sintese e aplicá-la: nas células com 4 estudos, mesmo 4 de 4 dão p = 0,125, e p < 0,05 exigiria pelo menos 6 estudos na mesma direção; por isso, p acima de 0,05 nestas células não indica ausência de efeito, e o teste não define nenhum rótulo. Números: `cel:C01.p_sinal`, `v1:L263` (6). Parágrafo sem span.

#### 3.4 Apoio a quem aparece à frente `{#sec-apoio}` (cerca de 680)

- **3.4-P1: C01** (cerca de 110). Função: achado da célula randomizada com mais estudos (SWiM item 8; M06; M03). Conteúdo: quatro experimentos [@Agranov2017a; @Farjam2020a; @Timotei2013a; @Tyszler2015], todos com algumas preocupações de risco de viés; três dos quatro em laboratório com preferências induzidas ou vinheta hipotética, e só @Farjam2020a com partidos e organizações reais; em @Agranov2017a e @Tyszler2015 o desfecho é o resultado da eleição do grupo, não o voto individual; 4 de 4 na direção *bandwagon* (proporção 1,00; IC 95% 0,40 a 1,00; p = 0,125); é a direção que os canais E2 a E4 preveem, e não a do E5; span C01. Números: `cel:C01.*`. Escrever "três dos quatro" por extenso.
- **3.4-P2: meta A** (cerca de 120, sem span). Função: estimativa exploratória com heterogeneidade no texto (livro R2.5, R5.25 a R5.29 e frase-modelo M14). Conteúdo: os três estudos com g [@Agranov2017a; @Timotei2013a; @Tyszler2015], com 4 efeitos, por CHE (REML) com RVE (CR2), ρ = 0,6: g = 0,48 (IC 95% −1,51 a 2,47; p = 0,263), com 1,25 grau de liberdade, abaixo de 4, e portanto inferência robusta não confiável; o IC cruza zero e ±δ (0,0573); τ² = 0,04 (τ = 0,20) e I² = 15%, com intervalo de predição de −3,55 a 4,51, não interpretados com k = 3; com ρ de 0,2, 0,5 e 0,8, a estimativa foi 0,49, 0,48 e 0,47, com IC cruzando zero; com ICC de 0,20, g = 0,51 (IC 95% −0,97 a 1,98); no *leave-one-out*, de 0,19 a 0,69, e o IC só deixou de cruzar zero sem @Timotei2013a (0,40 a 0,98); os dois efeitos de @Tyszler2015 foram lidos de figura; é exploratória, e sua certeza é a da célula (muito baixa). Números: `n1:meta.*`, `n1:meta_icc020.*`, `n1:meta_loo`, `mA:tau`, `v1:L143`.
- **3.4-P3: C02** (cerca de 110). Função: segunda célula randomizada. Conteúdo: quatro experimentos [@Tal2015a; @Lammers2022a; @Fichnova2015a; @Witsman2016a], todos em risco alto e todos em laboratório com preferências induzidas ou vinheta hipotética; 4 de 4 na direção *bandwagon* (proporção 1,00; IC 95% 0,40 a 1,00; p = 0,125); dentro de @Lammers2022a, os sinais se opõem conforme o modo de raciocínio induzido (g = 1,25 e 1,03 no modo heurístico; −0,39 e 0,06 no modo moral), e o estudo recebeu a direção *bandwagon* pela regra de 70% (3 de 4 efeitos); a condição moral é compatível, dentro do estudo, com o canal de equidade (E5); span C02. Números: `cel:C02.*`, `v1:L147`.
- **3.4-P4: meta B** (cerca de 110, sem span). Conteúdo: 3 estudos e 6 efeitos [@Fichnova2015a; @Lammers2022a; @Witsman2016a], mesmo modelo, δ = 0,044: g = 0,62 (IC 95% −0,48 a 1,72; p = 0,111), 1,46 grau de liberdade; IC que cruza zero e ±δ; comparabilidade limitada: posto num *ranking* de 7 candidatos, probabilidade autodeclarada numa escala de 1 a 7 e proporção de voto; τ² = 0,41 (τ = 0,64) e I² = 94%, com intervalo de predição de −7,82 a 9,05, não interpretados; com ρ de 0,2, 0,5 e 0,8, 0,61, 0,62 e 0,62; no *leave-one-out*, de 0,55 a 0,90, e o IC só deixou de cruzar zero sem @Lammers2022a (0,85 a 0,94); a sensibilidade sem risco alto não pôde ser rodada, porque todos os efeitos estão em risco alto; foi rodada depois do GRADE, que não a considerou; "Com menos de dez estudos, não testamos assimetria."; a ressalva: o autor de @Witsman2016a lê o contraste entre o candidato mostrado bem à frente e bem atrás como voto estratégico, e, se o alvo passar a viabilidade, o estudo sai desta célula e desta meta (sem os percentuais do contraste, fora da lista branca). Depois do parágrafo: `@@FIGURA metas@@` (chamada `@fig-metas` no parágrafo). Números: `n1:meta_mesmo_candidato.*`, `mB:tau`, `v1:L149`.
- **3.4-P5: C03** (cerca de 60). Conteúdo: um experimento de laboratório com preferências induzidas [@Boukouras2020a], com algumas preocupações de risco de viés, em que o grupo de comparação também viu pesquisas reais da mesma eleição e só o conjunto revelado mudou; 3 de 3 efeitos positivos; o desfecho é a taxa de vitória do candidato, medida de grupo; span C03; k por extenso ("um experimento"). Números: `cel:C03.*`; `cer:C03`.
- **3.4-P6: C04** (cerca de 55). Conteúdo: na classe não randomizada, um estudo de laboratório [@Feltovich2022], com contraste não sorteado e risco grave, na direção *bandwagon* (efeitos marginais de 0,25 e 0,44); span C04; a decisão pendente: a parcela do incumbente na prévia se confunde com o sinal de desempenho que todos recebem, e, se os efeitos forem para fora da contagem, a célula fica vazia. Números: `cel:C04.*`; `cer:C04` (0,25 e 0,44).
- **3.4-P7: C05** (cerca de 80). Conteúdo: dois experimentos naturais sobre proibição de boca de urna, ambos em risco alto no EPOC: @Morton2015a (territórios franceses de ultramar) na direção *bandwagon* e @Chatterjee2019a (Índia) na direção *underdog*, com dois efeitos principais (g −0,29 e −0,42); efeitos reorientados da proibição para a exposição; proporção 0,50 (IC 95% 0,01 a 0,99; p = 1); span C05. Números: `cel:C05.*`; `cer:C05` (−0,29 e −0,42).
- **3.4-P8: C06** (cerca de 70). Conteúdo: no Brasil, as urnas que continuaram recebendo votos depois da divulgação oficial da apuração parcial deram mais votos ao candidato mostrado à frente nos dois turnos da eleição presidencial de 2018 (+5,69 e +11,76 pontos percentuais) [@Araujo2021a]; o estudo está em risco grave, puxado pelo confundimento; entrou pela Emenda 1, decidida depois de conhecê-lo, e forma célula própria, porque não trata de pesquisa; span C06. Números: `cel:C06.*`; `v1:L155`.

#### 3.5 Viabilidade e voto estratégico `{#sec-viabilidade}` (cerca de 180)

- **3.5-P1: C07** (cerca de 70). Conteúdo: com nenhuma pesquisa como comparador, um experimento de *survey* no México [@Cornejo2023a], com 545 respondentes e algumas preocupações de risco de viés, foi na direção de viabilidade (g = 0,19, EP 0,105), com o candidato de oposição mostrado como segundo colocado viável; é o único estudo latino-americano sobre pesquisa pré-eleitoral na análise principal; span C07. Números: `cel:C07.*`, `cer:C07` (545), `v1:L161`.
- **3.5-P2: C08** (cerca de 110). Conteúdo: com outro resultado de pesquisa como comparador, dois experimentos: @Schlegel2023 (Reino Unido, vinheta hipotética) na direção da deserção para a opção viável (+11 e +17 pontos percentuais), com o contraste principal misturando a precisão da pesquisa com a retirada de carga cognitiva (decisão pendente); @Freden2024a (Suécia, eleição real) misto, com 2 de 3 efeitos contrários: mostrar uma legenda pequena abaixo da cláusula de 4% aumentou o voto nela (g = −0,41 na convenção da célula), o que os autores leem como voto de seguro; um estudo compatível com a previsão de voto estratégico e o outro contrário a ela; span C08; os efeitos de viabilidade de @Lago2015 e @Alabrese2024a ficaram fora da contagem, por serem interações com moderadores contínuos. Números: `cel:C08.*`, `v1:L161`. Escrever "dois experimentos" por extenso ou "2 experimentos" (k = 2).

#### 3.6 *Momentum* `{#sec-momentum}` (cerca de 160)

- **3.6-P1** (cerca de 40, sem span). Função: ressalva da Emenda 4b. Conteúdo: *momentum* é a pesquisa que mostra um partido ganhando apoio sem mostrar sua posição; a célula própria foi fixada pela Emenda 4b antes de qualquer análise de efeito, mas três dos quatro estudos de *momentum* (um deles em risco crítico) foram reclassificados para ela pelos árbitros de IA em 23/09/2026, depois de ver os dados; a pergunta é outra que a da célula principal.
- **3.6-P2: C09** (cerca de 45). Conteúdo: @Dahlgaard2016a, experimento de *survey* na Dinamarca com 1.700 respondentes, frente a nenhuma pesquisa: +3,40 pontos percentuais (g = 0,12, EP 0,080), com IC que cruza zero; algumas preocupações de risco de viés; span C09. Números: `cel:C09.*`, `cer:C09`, `v1:L165`.
- **3.6-P3: C10** (cerca de 40). Conteúdo: @Meer2015a, experimento de *survey* nos Países Baixos com 10.643 respondentes, pesquisa com ponto de referência de crescimento frente ao resultado sem esse enquadramento: g = 0,13 (EP 0,072), com IC que cruza zero; span C10. Números: `cel:C10.*`, `cer:C10`, `v1:L165`.
- **3.6-P4: C11** (cerca de 40). Conteúdo: @Stolwijk2016a, painel na Alemanha com a valência da cobertura de pesquisas, em risco grave, a favor do partido com cobertura favorável; @Unkelbach2022a, também de *momentum*, ficou fora por risco crítico; span C11. Números: `cel:C11.*`.

#### 3.7 Comparecimento `{#sec-comparecimento}` (cerca de 430)

- **3.7-P1: C12** (cerca de 80). Conteúdo: nos randomizados que comparam ver pesquisa com não ver, três estudos: dois de laboratório na direção de mobilização [@Agranov2017a; @Groer2010a] e um com candidatos reais, em risco alto, na de desmobilização [@Erlich2023]; proporção 0,67 (IC 95% 0,09 a 0,99; p = 1); a complacência prevista pelo E7 aparece só no estudo com candidatos reais; span C12. Números: `cel:C12.*`. O enunciado não traz o k: escrever "três estudos" fora do span.
- **3.7-P2: C13** (cerca de 80). Conteúdo: no experimento de campo de @Gerber2020a, em eleições para governador nos Estados Unidos, 126.126 eleitores receberam cartas com uma pesquisa de disputa apertada ou folgada, e o comparecimento foi medido em registros administrativos; as duas estimativas tiveram IC 95% inteiro dentro de ±δ (0,046); a certeza moderada qualifica a classificação como nulo ou trivial: é evidência de que o efeito, se houver, é menor que 2 pontos percentuais, e não ausência de evidência (M09); span C13. Números: `cel:C13.*`, `cer:C13` (126.126), `v1:L169`.
- **3.7-P3: C14** (cerca de 60). Conteúdo: num jogo *online* com preferências induzidas e 5.845 decisões [@Westwood2020a], a decisão de votar caiu quando a probabilidade de vitória exibida se afastava de 50:50 (g = −0,10, EP 0,023, com IC 95% inteiro abaixo de −δ); é a direção que a complacência e a pivotalidade preveem; span C14. Números: `cel:C14.*`, `v1:L175`.
- **3.7-P4: C15** (cerca de 50). Conteúdo: no contraste antes e depois no mesmo sujeito de @Klor2017a (laboratório; classe não randomizada pela Emenda 5; risco moderado), revelar a distribuição de preferências foi na direção de mobilização; span C15. Números: `cel:C15.*`.
- **3.7-P5: C16** (cerca de 50). Conteúdo: @Grillo2024c (França) compara momentos de divulgação de boca de urna, porque o turno de comparação também teve boca de urna da mídia estrangeira, divulgada mais tarde; direção de desmobilização com IC que cruza zero; risco alto no EPOC; o comparador é decisão pendente; span C16. Números: `cel:C16.*`.
- **3.7-P6: C17** (cerca de 60). Conteúdo: nos dois experimentos naturais de proibição de boca de urna, @Morton2015a foi na direção de desmobilização (−11 pontos percentuais) e @Chatterjee2019a ficou misto; proporção 0,00 (IC 95% 0,00 a 0,97; p = 1); span C17. Números: `cel:C17.*`, `v1:L177`. O enunciado não traz o k: escrever "dois experimentos naturais" fora do span. Usar a mesma casa decimal do limite superior que a Tab. 2 e a Fig. 4 usarem (a v1 escreveu 0,97); se divergirem, avisar o coordenador.
- **3.7-P7: C18** (cerca de 60). Conteúdo: dois estudos não randomizados em eleições reais, @Stolwijk2019b (painel na eleição para o Parlamento Europeu, risco grave) e @Brugarolas2021 (descontinuidade no horário de divulgação na Espanha, risco moderado), foram na direção de mobilização: 2 de 2 (IC 95% 0,16 a 1,00; p = 0,5); o rebaixamento por risco de viés foi de um nível, e não dois, decisão que o rascunho do GRADE deixou ao autor; span C18. Números: `cel:C18.*`. Não escrever o ano da eleição europeia (fora da lista branca).
- **3.7-P8** (cerca de 40, sem span). Conteúdo: o contraste entre boca de urna e projeções, na direção de desmobilização, e pesquisas pré-eleitorais, na de mobilização, foi notado depois de ver os dados e não foi testado; ele se confunde com o desenho, porque toda boca de urna aqui é experimento natural em eleição real. Fonte: `v1:L179`.

#### 3.8 Sensibilidades e viés de relato `{#sec-sensibilidades}` (cerca de 330)

Nenhum parágrafo desta seção tem span de célula.

- **3.8-P1** (cerca de 80). Função: o agrupamento amplo, *post hoc*, fora das manchetes (plano, "Riscos"). Conteúdo: juntando formatos e comparadores, num agrupamento decidido depois de ver os dados, 9 de 9 experimentos foram na direção *bandwagon* (proporção 1,00; IC 95% 0,66 a 1,00; p = 0,004), mas só @Farjam2020a tem contexto real; a certeza é muito baixa no rascunho do GRADE, que rebaixou esse corpo por viés de publicação (estudos pequenos, todos positivos, busca limitada); sem esse rebaixamento, a certeza seria baixa, e a decisão é do autor. Números: `v1:L157`, `n1:certeza_amplo_contagem`.
- **3.8-P2** (cerca de 60). Função: a sensibilidade que mais pesa. Conteúdo: só contexto real: no agrupamento amplo, os experimentos de apoio ficam reduzidos a @Farjam2020a (1 de 1), os não randomizados ficam com 2 estudos *bandwagon* e 1 *underdog*; na mobilização, os randomizados ficam com 1 estudo na direção de desmobilização e 1 nulo, e os não randomizados se dividem, 2 a 2, com 1 misto; disso segue que a regularidade *bandwagon* depende dos experimentos de laboratório e com vinheta. Números: `v1:L183`.
- **3.8-P3** (cerca de 50). Conteúdo: com os estudos em risco crítico, duas células mudam: a de projeções frente a nenhuma pesquisa recebe @Kaplan2019a, na direção de desmobilização, e a de *momentum* não randomizado recebe @Unkelbach2022a, a favor, e fica com 2 de 2 (IC 95% 0,16 a 1,00; p = 0,5); @Gasperoni2015a não entra em nenhuma célula, porque também está fora da contagem. Números: `v1:L185`.
- **3.8-P4** (cerca de 60). Conteúdo: o ICC de 0,20 não mudou nenhuma contagem; com os efeitos fora da contagem, os randomizados de apoio passam a 10 de 11 (@Gandhi2019 contra; p = 0,012), e a mobilização não randomizada fica 4 a 4, com 1 misto; sem dados anteriores a 2010, os randomizados de apoio ficam com 8 de 8 (p = 0,008), porque @Tyszler2015 sai pelo ano da coleta, numa regra de ano ainda inconsistente nos experimentos de laboratório; sem @Araujo2021a, os não randomizados de apoio ficam com 2 de 3; nenhuma dessas análises tem GRADE próprio; tabela completa em [S8](suplemento.html#s8-sensibilidades) (livro R5.33). Números: `v1:L187`, `n1:icc020_igual_principal`.
- **3.8-P5** (cerca de 50). Função: viés de relato (PRISMA item 21; livro R5.30; E4, "poucos nulos"). Conteúdo: nenhuma célula teve 10 ou mais estudos, e não houve funil, teste de Egger nem modelo de seleção; o GRADE rebaixou por viés de publicação as duas células randomizadas de apoio e o agrupamento amplo randomizado, em que todos os estudos são pequenos e positivos, sem nenhum nulo; nas demais células não houve rebaixamento, porque há resultado nulo ou contrário ou um só estudo, mas a suspeita fica em aberto pela limitação de fontes; não houve avaliação separada de evidência faltante por célula. Fonte: relatório técnico, item 21.
- **3.8-P6** (cerca de 30 + a enumeração, cerca de 70). Função: decisões pendentes que mudariam células, com a direção provável (M12; livro R6.4). Conteúdo, em prosa com "(i) ... (viii)": (i) se o alvo do efeito principal de @Witsman2016a passar a viabilidade, a célula do mesmo candidato atrás fica com 3 estudos, e a meta B muda; (ii) se os efeitos de @Feltovich2022 forem para fora da contagem, a célula não randomizada de outro resultado fica vazia; (iii) se o contraste de @Schlegel2023 for para fora, a célula de viabilidade com outro resultado fica só com @Freden2024a; (iv) se o efeito de @Klor2017a hoje fora da contagem voltar, a célula do mesmo candidato atrás ganha um estudo; (v) se os efeitos de @Geers2018 voltarem pela direção, o comparecimento não randomizado ganha um estudo na direção de desmobilização; (vi) se o efeito de variável instrumental de @Gerber2020a for para fora, a célula de pesquisa apertada muda de composição, mas não de direção; (vii) se o comparador de @Grillo2024c passar a unidades não expostas, o estudo muda de célula; e (viii) a regra de ano da eleição nos experimentos de laboratório muda a sensibilidade sem dados anteriores a 2010; nenhuma dessas mudanças levaria uma célula a 6 estudos numa só direção, o mínimo para p < 0,05 no teste de sinal. Fontes: `pontos_para_o_revisor.md`; `v1:L192`; `mecanismos_moderadores.md` §6. Números: `v1:L263` (6).
- **CO-efeito** {P033, P036, P037, P039, P042}: "Os achados de @sec-efeito a @sec-sensibilidades dependem da conferência dos 560 efeitos na página do texto completo (P039), da arbitragem da recodificação cega (P037), da validação do risco de viés (P033) e da validação do GRADE (P036 e P042). As decisões de julgamento que podem mudar as células estão no último parágrafo desta seção." Fonte: `v1:L192`.

#### 3.9 Mecanismos `{#sec-mecanismo}` (cerca de 360)

Regra da subseção: descritiva; certeza só quando a afirmação coincide com uma célula; nos demais casos, "sem GRADE (descritivo)" (livro R5.47: moderador ou mecanismo de credibilidade baixa aparece como hipótese).

- **3.9-P1** (cerca de 40). Conteúdo: nenhuma célula teve estudos suficientes para síntese formal de mecanismos; o que segue vem do fichamento por IA, não conferido por humano, e compara estudos ou relata o que cada estudo testou. Fonte: `v1:L197`, sem o caminho de arquivo.
- **3.9-P2** (cerca de 50). Conteúdo: dos 41 estudos, 34 marcam algum mecanismo como testado, mas só 3 o fazem por mediação estatística; nos demais, o canal é inferido de um contraste, relatado pelos participantes ou só hipotetizado; os dois codificadores de IA concordaram em 60% dos casos sobre qual mecanismo foi testado e em 40% sobre o tipo de evidência, abaixo do limiar do protocolo. Números: `v1:L199`.
- **3.9-P3** (cerca de 60). Função: teoria rival 2, efeito só de expectativa. Conteúdo: só @Gerber2020a testa formalmente se a expectativa de quem vence transmite o efeito ao comportamento: a pesquisa apertada move a crença sobre a proximidade da disputa, mas 1 ponto percentual a mais de crença muda o comparecimento em 0,08 ponto; é o padrão da teoria rival do protocolo, em que a pesquisa muda o que o eleitor espera, e não o que ele faz; o nulo da exposição tem certeza moderada, mas a leitura como mediação é descritiva, e nenhum estudo testou essa mediação no apoio a quem aparece à frente. Números: `v1:L201`.
- **3.9-P4** (cerca de 80). Função: heurística, conformidade, simpatia e emoções (E3 a E6). Conteúdo: o único estudo que manipula o modo de processamento, @Lammers2022a, acha *bandwagon* sob raciocínio heurístico e *underdog* ou efeito perto de zero sob o motivo moral de igualdade, em vinheta e risco alto; em @Meer2015a, a ênfase sobre quem está ganhando importa mais que o número; nenhum estudo isola a conformidade; em @Agranov2017a, a maioria vota mais e a minoria menos quando há pesquisa, padrão que os autores atribuem, pelo menos em parte, ao desejo de votar no vencedor; em @Stolwijk2016a, os efeitos indiretos da cobertura de pesquisas passam mais pelo entusiasmo que pela ansiedade, numa mediação observacional em risco grave; tudo isso é descritivo ou está em células de certeza muito baixa. Fonte: `v1:L203`, `v1:L207`.
- **3.9-P5** (cerca de 70). Função: voto estratégico (E2). Conteúdo: é o canal com mais estudos (25 o marcam) e com os testes mais diretos, em laboratório com incentivos; neles, a informação sobre a distribuição de preferências aparece associada a mais deserção para a opção viável [@Tyszler2015; @Tyszler2013; @Tal2015a], achado descritivo: os dois primeiros estão em células de apoio principal com certeza muito baixa, e @Tyszler2013 não entra em nenhuma célula; fora do laboratório, @Cornejo2023a acha a direção de viabilidade no México e @Freden2024a acha o contrário na Suécia; @Araujo2021a testou e descartou o voto estratégico como explicação do caso brasileiro, porque o efeito aparece maior no segundo turno, com dois candidatos. Fonte: `v1:L205`.
- **3.9-P6** (cerca de 60). Função: pivotalidade e complacência (E7). Conteúdo: ver projeções longe de 50:50 pode reduzir a decisão de votar (certeza baixa), e a evidência é muito incerta sobre se a boca de urna divulgada antes do fechamento reduz o comparecimento (certeza muito baixa) [@Westwood2020a; @Morton2015a; @Grillo2024c]; em @Klor2017a, revelar a distribuição de preferências aparece associado a mais comparecimento só em eleitorados quase divididos, achado dentro do estudo, descritivo, numa célula de certeza muito baixa. Fonte: `v1:L207` (com as correções 3 da verificação).
- **CO-mecanismo** {P037, P039}: "Mecanismos e tipos de evidência vêm do fichamento por IA, com concordância abaixo do limiar entre os dois codificadores (P037), e os valores citados aguardam a conferência na página do texto (P039). As leituras de @Lammers2022a (n por célula derivado) e do efeito de variável instrumental de @Gerber2020a são as que mais dependem dessa conferência." Fonte: `v1:L212`.

#### 3.10 Moderadores `{#sec-moderadores}` (cerca de 440)

- **3.10-P1** (cerca de 45). Conteúdo: também descritiva; o protocolo só permite estimativa por subgrupo com pelo menos 3 estudos por nível e teste com pelo menos 4, e nenhuma célula chegou lá; o que segue compara a direção de estudos que diferem num moderador, uma comparação mais fraca, ou relata subgrupos estimados dentro de um estudo, lado a lado e sem teste (livro R5.34). Fonte: `v1:L217`.
- **3.10-P2** (cerca de 75). Função: veredito por previsão (M03; E7, "veredito para cada previsão"). Conteúdo: a @tbl-hipoteses põe cada elo do modelo lógico e cada teoria rival ao lado do que a evidência diz, com a certeza só onde a afirmação coincide com uma célula; em resumo, a direção prevista pelos canais E2 a E4 domina os experimentos (certeza muito baixa); a direção *underdog*, prevista pelo E5, aparece só na condição moral de @Lammers2022a e numa proibição de boca de urna [@Chatterjee2019a], que os autores leem como voto no azarão ou de protesto; a teoria rival do efeito só de expectativa é compatível com @Gerber2020a; a de efeitos que se anulam ficou sem teste; e a do efeito artefatual é compatível com o padrão de realismo descrito a seguir, sem teste formal. Depois do parágrafo: `@@TABELA hipoteses@@`.
- **3.10-P3** (cerca de 70). Conteúdo: quanto ao realismo, na célula principal de apoio, os 4 estudos com vinheta hipotética e os 5 com preferências induzidas foram todos na direção *bandwagon*, e dos 4 em eleição real, 3 foram *bandwagon* e 1 *underdog* [@Chatterjee2019a]; no comparecimento, 3 de 4 estudos com preferências induzidas foram na direção de mobilização, e entre os 7 em eleição real houve 2 na de mobilização, 3 na de desmobilização, 1 misto e 1 nulo; o realismo foi o principal motivo de rebaixamento por indireção nas células de apoio (@fig-realismo; comparação descritiva, sem teste). Depois do parágrafo: `@@FIGURA realismo@@`. Números: `v1:L219`.
- **3.10-P4** (cerca de 45). Conteúdo: o número de competidores não muda a direção: 5 de 5 estudos com dois competidores e 7 de 8 com três ou mais foram *bandwagon*; 8 dos 13 estudos da célula principal usam a regra do próprio experimento como sistema eleitoral, e sem estimativa de tamanho a hipótese de efeito maior com pluralidade não pode ser avaliada. Números: `v1:L221`.
- **3.10-P5** (cerca de 55). Conteúdo: nos estudos que variam a proximidade, a disputa apertada aparece com mais comparecimento e a decidida com menos [@Bursztyn2023a; @Klor2017a; @Alabrese2024a]; no desenho mais forte [@Gerber2020a], receber pesquisa apertada, em vez de folgada, provavelmente não muda o comparecimento além de ±2 pontos percentuais (certeza moderada); a mobilização do lado que está atrás, prevista pela teoria, aparece como padrão de comparecimento em @Bursztyn2023a, mas o efeito na parcela de votos é nulo por ±δ. Fonte: `v1:L223`.
- **3.10-P6** (cerca de 40). Conteúdo: os dias até a eleição só estão informados em 11 dos 41 estudos; as exposições no dia da votação (boca de urna e apuração parcial) têm efeitos grandes, mas são também as únicas de variação natural em eleição real, e o momento se confunde com o desenho; só um estudo é de referendo [@Bursztyn2023a], e a hipótese de efeito maior em referendos não pôde ser examinada. Números: `v1:L225`.
- **3.10-P7** (cerca de 55). Conteúdo: em @Cornejo2023a, com heterogeneidade pré-especificada, o efeito na direção de viabilidade foi maior entre partidários (g = 0,33) que entre independentes (0,09), ao contrário do esperado, e ficou perto de zero, com sinal oposto, entre quem prefere o PRI (−0,05); @Meer2015a não achou interação com preferência prévia, volatilidade ou escolaridade; quanto à sofisticação, as duas teorias rivais do protocolo têm algum apoio: os menos informados atualizam mais as crenças e respondem mais à heurística induzida [@Gerber2020a; @Lammers2022a], enquanto em @Gasperoni2015a, em risco crítico, quem trocou de voto era mais interessado; nenhum estudo testa as duas no mesmo desenho. Números: `v1:L227`.
- **3.10-P8** (cerca de 50). Conteúdo: a hipótese de efeitos que se anulam exige pelo menos 3 estudos com subgrupos de eleitores de sinais opostos, e só 2 os têm [@Cornejo2023a; @Lammers2022a], de modo que fica sem teste; quanto à equidade, dos três estudos que testaram a escolaridade, dois não acharam diferença [@Dahlgaard2016a; @Meer2015a] e um achou a direção prevista para um único partido [@Unkelbach2022a, em risco crítico], e o único teste de classe social não achou moderação; a hipótese de *bandwagon* maior entre os de menor escolaridade ou classe não encontra apoio consistente. Fonte: `v1:L229`, `v1:L231`.
- **3.10-P9** (cerca de 30). Conteúdo: nenhum dos 11 estudos de comparecimento da síntese principal tem voto obrigatório codificado como sim; 2 estão como não e 9 como não informado; a hipótese de que o voto obrigatório elimina o canal da desmobilização não pode ser examinada. Números: `v1:L233` (corrigidos pela verificação: 11, 2 e 9).
- **CO-moderadores** {P037, P039}: "Os moderadores relatados, a margem mostrada, os dias até a eleição e o voto obrigatório tiveram concordância abaixo do limiar entre os codificadores de IA (P037), e as estimativas por subgrupo aguardam a conferência dos efeitos (P039). As decisões sobre @Feltovich2022 e @Witsman2016a mudariam as contagens de realismo e de número de competidores." Fonte: `v1:L238`.

#### 3.11 Percepção, implementação e custo `{#sec-percepcao}` (cerca de 90)

- **3.11-P1** (cerca de 90). Função: o "não se aplica" do OQF (livro R1.6, R1.8; EtD R6.13). Conteúdo: o formato OQF avalia também como os envolvidos percebem uma política, o que a implementação exige e quanto custa; aqui essas dimensões não se aplicam: a exposição a pesquisas é um fenômeno de informação, sem gestor que a implemente, e chega ao eleitor por escolha, por acaso ou por manipulação experimental; não há fidelidade de implementação nem custo por beneficiário a calcular, e a revisão, restrita ao efeito, não sintetizou achados qualitativos (sem GRADE-CERQual); a caixa gerada pelo *script* marca implementação como "Não avaliada" e custo como "Pendente", e o texto as trata como "não se aplica"; estudos de percepção e de custo regulatório entram na agenda de pesquisa (@sec-pesquisa-futura). Fonte: `v1:L243`.

### 3.9 Seção 4: Discussão `{#sec-discussao}` (cerca de 1.600)

#### 4.1 Resumo dos achados `{#sec-achados}` (cerca de 300)

- **4.1-P1** (cerca de 120). Função: resposta com a certeza e a convergência das classes de desenho (M01, M07, M08; E4, convergência). Conteúdo: nas três células randomizadas de apoio, todos os estudos foram na direção *bandwagon*, com certeza muito baixa em cada uma e sem estimativa de tamanho (FC-metas); nas três não randomizadas, o quadro é mais dividido: duas vão na direção *bandwagon* e a de boca de urna tem um estudo em cada direção; as classes não se contradizem, mas a não randomizada é mais fraca e mais dividida; a regularidade repousa em laboratório e vinheta (@sec-sensibilidades). Números: `cel:C01` a `cel:C06` (sem "x de y" com algarismos). Movimentos: M01, M08.
- **4.1-P2** (cerca de 100). Função: comparecimento e o que se pode descartar (M09; E7, "we can rule out"). Conteúdo: o quadro é misto; o achado de maior certeza é um nulo: o maior experimento de campo permite descartar, com certeza moderada, efeitos de pesquisa apertada, frente a folgada, maiores que 2 pontos percentuais; ter visto a divulgação de pesquisas pode aumentar a participação, e projeções longe de 50:50 podem reduzi-la (certeza baixa nos dois casos); a boca de urna tem certeza muito baixa; a diferença entre formatos foi notada depois de ver os dados.
- **4.1-P3** (cerca de 80). Função: as contribuições retomadas (M02). Conteúdo: retomar as três contribuições de 1.3-P2 com o que cada uma mostrou: (i) o inventário com protocolo desde 2010 existe, com risco de viés e certeza por célula; (ii) a separação por células mostra que a regularidade *bandwagon* vem de um tipo de desenho e que voto estratégico e *momentum* têm poucos estudos; e (iii) o mapa brasileiro é sobretudo de lacunas.

#### 4.2 Relação com revisões anteriores `{#sec-revisoes-anteriores}` (cerca de 300)

Só conteúdo marcado como verificado em `revisoes_anteriores.md`. Frases com @Hardmeier2008 nunca têm verbo de conclusão.

- **4.2-P1** (cerca de 110). Conteúdo: @Barnfield2019 argumenta que experimentos que apresentam a pesquisa como único estímulo tendem a achar efeito, com pouco a ensinar por falta de realismo, e que pistas de contexto, como a identificação partidária, atenuam o efeito da pesquisa; o achado de que a regularidade *bandwagon* desta revisão repousa em laboratório e vinheta e rareia em eleições reais está em linha com essa advertência; a separação entre conversão e mobilização, e entre *bandwagon* e desmobilização de quem vê o próprio partido afundar, também está nas células desta revisão. Fonte: `revisoes_anteriores.md` §1 ("Being conservative in experimental study"; "Bandwagon conversion and mobilisation effects"). Movimento: M14.
- **4.2-P2** (cerca de 100). Conteúdo: @MoyRinke2012 concluíram que a literatura não permitia dizer se o *bandwagon* ou o *underdog* era mais comum, por inconsistências teóricas e operacionais, que havia evidência de efeitos mobilizadores e desmobilizadores no comparecimento e que os efeitos dependem do contexto político e midiático; esta revisão não fecha essa questão: nas células randomizadas, a direção pende para o *bandwagon*, mas com certeza muito baixa; no comparecimento, o quadro segue misto; e a dependência do contexto reaparece no padrão de realismo e na transferibilidade; a diferença de método (protocolo, células, risco de viés, GRADE, só evidência desde 2010) explica por que a comparação é de enquadramento, e não de estimativas. Fonte: `revisoes_anteriores.md` §3.
- **4.2-P3** (cerca de 90). Conteúdo: @Cosgun2026, revisão sistemática sobre campanhas numa só base e só em inglês, registra que as afirmações causais mais fortes da área vêm de laboratório e de experimentos de *survey*, concentrados nos Estados Unidos e em painéis de conveniência, o que coincide com a composição dos estudos incluídos aqui; a sobreposição com esta revisão é pequena; sobre @Hardmeier2008, sem texto aberto, não há como comparar conclusões, e esta revisão atualiza a evidência, não um resultado verificado daquele capítulo. Fonte: `revisoes_anteriores.md` §2 e §4.1.

#### 4.3 Completude, aplicabilidade e limitações da evidência `{#sec-limitacoes-evidencia}` (cerca de 400)

- **4.3-P1** (cerca de 110). Função: completude e aplicabilidade (PRISMA 23b; Campbell 7c; E4, cautela na generalização). Conteúdo: os 41 estudos vêm, na maioria, dos Estados Unidos e da Europa; dos 9 experimentos de apoio do agrupamento amplo, 8 usaram laboratório com preferências induzidas ou vinheta hipotética, e com contexto real sobra 1; FC-Brasil; os fatores de transferibilidade ficam sem estudo (@sec-brasil). Números: `v1:L398`, `v1:L412`.
- **4.3-P2** (cerca de 150). Função: qualidade da evidência. Conteúdo: cada célula tem de 1 a 4 estudos, abaixo do necessário para teste de sinal com poder, análise de moderadores ou avaliação de viés de publicação; nas células de 1 estudo, o IC 95% da proporção vai de 0,03 a 1,00 ou de 0,00 a 0,97; efeitos lidos de figura e medidas indiretas (@Tyszler2015; @Agranov2017a e @Tyszler2015 medem quem vence a eleição do grupo; n derivado em @Lammers2022a e @Meffert2011; valor derivado em @Kaplan2019a); sem meta-análise principal, não há tamanho do efeito, e as duas metas misturam medidas, têm menos de 4 graus de liberdade e dependem de um estudo cada no *leave-one-out*; nenhum resultado randomizado em risco baixo, os 4 experimentos da célula do mesmo candidato atrás em risco alto e o confundimento grave ou crítico na maioria dos não randomizados; contrastes e estimandos heterogêneos, e 7 estudos só com efeitos fora da contagem; alguns estudos publicados depois de 2010 usam eleições ou coletas anteriores [@Morton2015a; @Chatterjee2019a; @Tyszler2015; @Klor2017a]. Números: `v1:L400` a `v1:L410`.
- **4.3-P3** (cerca de 140). Função: o que a evidência não permite responder (M10; E6, "our evidence is silent"). Conteúdo: "A evidência nada diz sobre" (i) o tamanho do efeito das pesquisas sobre o voto; (ii) o efeito de pesquisas pré-eleitorais publicadas sobre eleitores brasileiros; (iii) um embargo de pesquisas pré-eleitorais como o que o STF derrubou em 2006, que só @Lago2015 aborda, fora da contagem; (iv) se o voto obrigatório fecha o canal da desmobilização; (v) se a confiança nas pesquisas modera o efeito (relatada por um só estudo); (vi) o efeito de agregadores e projeções sobre a escolha de voto, porque os estudos desse formato mediram só o comparecimento; (vii) referendos, com um só estudo; e (viii) os mecanismos, além do teste de expectativa de @Gerber2020a; para cada item, o motivo (sem estudo, desenho fraco, desfecho não medido). Fontes: `mecanismos_moderadores.md` §3.7 (agregador sem estudo no apoio) e §3.4; `v1:L285`; `n1:familia`.

#### 4.4 Limitações do processo e da síntese `{#sec-limitacoes-processo}` (cerca de 600)

Regra: um parágrafo por etapa, com (a) o que houve, (b) a direção provável do viés, dita como inferência, e (c) a pendência que resolve (PRISMA 23c; SWiM item 9; M13; Garritty rec. 24; livro R6.3 a R6.5). Frase de tópico no início de cada parágrafo, sem negrito. A direção provável vem de `garritty_2024.md` §4 ("Consequência provável").

- **4.4-P1** (cerca de 30). Abertura: as limitações seguem as etapas; a direção do viés é inferência, não medida; pelo critério do livro, nada disso é compensado pela concordância entre agentes.
- **4.4-P2 Busca** (cerca de 75). (a) Fontes restritas (A1), sem Web of Science, Scopus, SciELO nem literatura cinzenta; âncoras por IA, com *recall* final não independente (A3); PRESS só por IA, com lacunas conhecidas (A4); três idiomas; o recorte de 2010 deixa de fora o intervalo entre o fim da cobertura de @Hardmeier2008, não verificado, e 2009. (b) Estudos perdidos, se forem mais vezes nulos e não publicados, inflariam a proporção na direção dominante; proibições, embargos e comparecimento tendem a ficar sub-representados; o sinal *bandwagon* × *underdog* é indeterminado. (c) P001 e P004. Fontes: `v1:L416`, `v1:L426`, `v1:L442`.
- **4.4-P3 Seleção** (cerca de 95). (a) Triagem só por IA (A2), sem *recall*; 81 divergências e 145 pares de duplicata sem decisão; a triagem complementar dos 336 registros sem resumo foi só por IA, sem estimativa de quantos elegíveis se perderam nas 156 exclusões; o comando que registrou essas decisões grava o ator como humano, embora sejam de IA; 165 decisões de elegibilidade sem conferência; 342 de 526 relatos não recuperados, sem contato com autores (A5), parte de acesso aberto bloqueada por desafio antirrobô, que não foi contornado; em @Freden2016b o PDF não traz o artigo empírico. (b) A regra liberal reduz exclusões erradas, mas exclusões concordantes e erradas dos dois agentes não aparecem na concordância; se os não recuperados forem mais vezes nulos, a direção dominante fica superestimada. (c) P006, P007, P019, P020, P041, P008 e P023. Fontes: `v1:L418`, `v1:L422`, `v1:L424`, `v1:L436`.
- **4.4-P4 Extração** (cerca de 80). (a) Concordância de 58,5% na recodificação cega, com alvo e comparador em κ 0,38 e estimando em κ 0,15, e a direção da estimativa principal em 50%; reextração e arbitragem pelo mesmo modelo; 772 correções aplicadas pelo coordenador de IA, 240 estendidas sem nova arbitragem; 40 barradas por erro do coordenador. (b) Erros aleatórios de sinal aproximam as contagens de metade e atenuam a direção dominante; erros sistemáticos do mesmo modelo têm direção imprevisível. (c) P039, P037, P025 e P026. Fonte: `v1:L430`, `v1:L432`.
- **4.4-P5 Risco de viés** (cerca de 60). (a) Julgamentos só de IA; árbitro do mesmo modelo do avaliador A, que ele seguiu em 79 de 88 domínios; a confirmação em bloco registrada na Emenda 4d não aconteceu (Emenda 6a); ROBINS-I V2 no lugar do ROBINS-E; classificadores de desenho em desacordo fixados pelo coordenador. (b) Afeta a certeza e a exclusão por risco crítico (3 estudos), não o sinal dos efeitos. (c) P033. Fontes: `v1:L420`, `v1:L428`, `v1:L438`; relatório técnico, "Outras informações".
- **4.4-P6 Síntese** (cerca de 110). (a) A estrutura de células, o sinal por alvo, a lista de efeitos fora da contagem, a classe de desenho de dois estudos, os nulos por ±δ e o sinal por *proxy* foram decididos depois de ver os dados (Emenda 5), assim como as reclassificações de alvo e comparador dos árbitros; o agrupamento amplo é descritivo; a contagem por direção responde se há evidência numa direção, não o tamanho, e ignora a precisão dos estudos; as metas misturam medidas e têm menos de 4 graus de liberdade; a meta do mesmo candidato atrás foi rodada depois do GRADE; análises planejadas e não feitas: moderadores e subgrupos (k insuficiente), fatores de equidade, avaliação separada de evidência faltante, artigo como conglomerado e modelo de seleção. (b) As decisões pendentes de @sec-sensibilidades podem mover estudos entre células, mas nenhuma levaria uma célula a outro rótulo. (c) P035, P036 e P039. Fontes: `v1:L440`, `v1:L442`; SWiM item 9.
- **4.4-P7 Certeza** (cerca de 70). (a) GRADE rascunhado por um só subagente, sem segundo avaliador; três decisões ficaram para o autor: (i) não rebaixar os corpos cuja única preocupação de risco de viés é o relato seletivo [@Westwood2020a; @Meer2015a; @Boukouras2020a; @Gerber2020a], e se forem rebaixados, as células de @Westwood2020a e @Gerber2020a descem um nível; (ii) rebaixar só um nível a célula de @Stolwijk2019b e @Brugarolas2021; e (iii) rebaixar por viés de publicação o agrupamento amplo de apoio randomizado, que sem isso teria certeza baixa. (b) Nenhuma dessas decisões dá a uma célula estudos suficientes para outro rótulo da caixa. (c) P036, P042 e P035. Fontes: `v1:L387`, `v1:L268`; relatório técnico, item 22.
- **4.4-P8 Relato e questões transversais** (cerca de 80). (a) Este texto foi redigido por agentes de IA a partir dos arquivos e ajustado ao estilo do autor, que ainda não o leu; todos os modelos são do mesmo provedor, e erros correlacionados não aparecem na concordância entre eles; dois defeitos da ferramenta de revisão: o conferidor de trechos literais removia o travessão sem inserir espaço e recusou citações corretas de dois triadores, e o classificador de respostas tratava como inconclusiva qualquer resposta com a sequência "incert"; não houve consulta a *stakeholders*. (b) Os dois primeiros podem reforçar erros sem sinal; os defeitos da ferramenta afetaram registros de triagem, não efeitos. (c) P038. Fontes: `v1:L428`, `v1:L434`, `v1:L442`.

### 3.10 Seção 5: Da evidência à prática: implicações `{#sec-pratica}` (cerca de 900)

#### 5.1 Caixa de ferramentas `{#sec-caixa}` (cerca de 280)

- **5.1-P1** (cerca de 90). Função: a caixa e a regra (livro R5.48 a R5.53; frase-modelo M4). Conteúdo: a @tbl-oqf traz a caixa no formato OQF para a pergunta principal (pesquisa pré-eleitoral e apoio a quem aparece à frente), gerada pela regra caixa-3 (@sec-certeza) a partir da mesma tabela de achados que alimenta a @tbl-sof; cada linha informa a certeza, e a "Força" é a certeza, não o tamanho; a caixa célula a célula e o painel ficam em [S9](suplemento.html#s9-caixa). Depois do parágrafo: `@@TABELA oqf_principal@@`. Fonte: `v1:L249`, `v1:L255`.
- **5.1-P2** (cerca de 130). Função: por que tudo é Inconclusivo (M09). Conteúdo: 15 das 18 células têm certeza muito baixa, o que leva direto a Inconclusivo; as outras três não têm meta-análise nem estudos suficientes para o teste de sinal: com o teste binomial exato bilateral, p < 0,05 exige pelo menos 6 estudos na mesma direção, e nenhuma célula tem mais de 4; a célula de @Gerber2020a, nula por ±δ e com certeza moderada, também fica Inconclusivo, porque a regra só dá Nulo a uma meta-análise, e o rótulo é calculado no nível formato × desfecho × desenho e repetido nas células; Inconclusivo não quer dizer que as pesquisas não têm efeito, e sim que a evidência não permite afirmar direção e tamanho com a confiança que a regra exige. Números: `v1:L263`; `n1:certeza_contagem`.
- **5.1-P3** (cerca de 60). Conteúdo: as linhas de percepção, implementação e custo não se aplicam (@sec-percepcao); os rótulos seguem a regra versionada, aplicada à tabela de achados, e nenhuma implicação desta seção é mais forte que a certeza que a sustenta (frase-modelo M4 do livro, adaptada).
- **CO-caixa** {P035, P036, P042}: "Os rótulos e a força dependem das certezas GRADE, rascunhadas por IA e não validadas (P036 e P042), e da confirmação do portão G8 (P035). Nenhuma das decisões em aberto dá a uma célula estudos suficientes para outro rótulo que não Inconclusivo." Fonte: `v1:L268`.

#### 5.2 O que isso significa para o debate brasileiro `{#sec-brasil}` (cerca de 420)

- **5.2-P1** (cerca de 90). Função: o que a evidência permite dizer (livro R6.8, linha "muito baixa"). Conteúdo: a evidência permite dizer pouco: (i) nos experimentos que isolam a informação da pesquisa, a direção dominante é *bandwagon*, com certeza muito baixa; (ii) uma pesquisa apertada, frente a uma folgada, provavelmente não muda o comparecimento além de 2 pontos percentuais, num país de voto facultativo; e (iii) FC-Brasil; a evidência não permite afirmar que as pesquisas mudam o resultado das eleições, nem de quanto, nem que não têm efeito, e não trata da precisão das pesquisas, que é o objeto dos projetos de lei de 2022. Fonte: `v1:L273`, com a frase do Brasil corrigida.
- **5.2-P2** (cerca de 90). Função: restrição à divulgação, com verbo proporcional (livro R6.8 a R6.10, R6.20). Conteúdo: a evidência direta sobre restrições vem de proibições de boca de urna na França e na Índia, em direções opostas no apoio ao líder e com certeza muito baixa, e de um corte transversal de 46 países que ficou fora da contagem [@Lago2015]; nenhum estudo da síntese principal avalia um embargo de pesquisas pré-eleitorais como o que o STF derrubou em 2006; com certeza muito baixa, a evidência não permite concluir, e não cabe implicação de adoção nem de revogação baseada em efeito; FC-regulação; o fundamento de 2006, o direito à informação, não depende desta evidência, e a decisão cabe a quem tem mandato para tomá-la. Fonte: `v1:L275`.
- **5.2-P3** (cerca de 80). Função: transferibilidade julgada, não presumida (livro R6.14 a R6.17). Conteúdo: os quatro fatores fixados no protocolo antes dos dados (voto obrigatório; dois turnos nas eleições executivas; regulação da divulgação; confiança nas pesquisas); a @tbl-transferibilidade diz, para cada um, como é o Brasil, quantos estudos incluídos têm a condição e o que se pode dizer; o julgamento é por fator e não gera um segundo rebaixamento, porque a diferença de contexto e de realismo já entrou na indireção do GRADE; em síntese, nenhum estudo de comparecimento da síntese principal tem voto obrigatório codificado, só o estudo brasileiro mede os dois turnos da mesma eleição, os experimentos de viabilidade vêm de sistemas de pluralidade ou proporcionais, a evidência sobre regulação vem de outros países e a confiança nas pesquisas foi relatada por um só estudo (as contagens por fator estão na tabela, não no texto). Depois do parágrafo: `@@TABELA transferibilidade@@`. Fontes: protocolo §9; `v1:L277` a `v1:L285`.
- **5.2-P4** (cerca de 70). Conteúdo: em @Araujo2021a, falhas da identificação biométrica deixaram eleitores votando depois das 19:00 na eleição presidencial de 2018, quando a apuração parcial oficial já mostrava Bolsonaro à frente; o estudo entrou pela Emenda 1, decidida depois de conhecê-lo, e forma célula própria; @Cornejo2023a é o único estudo latino-americano sobre pesquisa pré-eleitoral na análise principal, e @Lago2015 ficou fora da contagem; a tabela regional está em [S10](suplemento.html#s10-regional). Fonte: `v1:L289`.
- **5.2-P5** (cerca de 90). Função: implicações por ator, separadas das de pesquisa (M15; livro R6.12, R6.21). Conteúdo: para o Congresso e a Justiça Eleitoral, qualquer argumento sobre efeito de pesquisas no voto, a favor ou contra restrições, precisa dizer que a certeza é muito baixa ou baixa na maior parte das células e que não há evidência sobre pesquisas com dados só do Brasil; se as regras de divulgação mudarem, a mudança pode ser desenhada de modo a permitir avaliação (implicação de desenho de avaliação, a única admissível com certeza muito baixa); para a imprensa e os institutos, a revisão não dá base para afirmar que a divulgação move votos, nem que é inócua. Sem "deve", "recomendamos" ou verbo mais forte que "pode". Movimento: M15.
- **CO-brasil** {P036, P039, P042}: "As implicações acompanham certezas ainda não validadas (P036 e P042) e efeitos ainda não conferidos (P039). Se o autor mudar o alvo do efeito principal de @Witsman2016a ou a lista de efeitos fora da contagem, a primeira mensagem principal precisa ser revista." Fonte: `v1:L296`.

#### 5.3 Implicações para a pesquisa `{#sec-pesquisa-futura}` (cerca de 200)

- **5.3-P1** (cerca de 200). Função: implicações que saem dos domínios que rebaixaram a certeza (livro R6.11; M15; E2 e E6). Conteúdo, em prosa com "(i) ... (vii)": (i) indireção: estudos com eleições reais no Brasil, sejam experimentos de *survey* com pesquisas verdadeiras em campanhas em curso, sejam experimentos naturais que aproveitem variações no calendário ou no alcance da divulgação; (ii) comparador sem pesquisa, porque é esse contraste que responde à pergunta regulatória; (iii) risco de viés: pré-registro e relato completo, que reduziriam a preocupação mais comum nos experimentos (o relato seletivo); (iv) imprecisão: estudos maiores, com o efeito relatado em pontos percentuais e erro-padrão; (v) medir no mesmo desenho o apoio a quem lidera, a deserção estratégica e o comparecimento; (vi) estimativas por subgrupo de eleitores que permitam testar a hipótese de efeitos que se anulam, e a confiança nas pesquisas e o voto obrigatório como moderadores; e (vii) estudos sobre a percepção das pesquisas pelos eleitores e sobre o custo regulatório de restrições à divulgação, que são avaliação da regulação, e não da exposição; uma atualização desta revisão deveria incluir outras bases e revisão PRESS humana. Fontes: `v1:L291`, `v1:L245`.

### 3.11 Seção 6: Conclusões `{#sec-conclusoes}` (cerca de 200)

- **6-P1** (cerca de 110). Função: a resposta, pela última vez, com a certeza em cada frase (livro R1.8). Conteúdo: nos experimentos, a direção é *bandwagon*, com certeza muito baixa e sem tamanho; FC-apertada; FC-divulgação; FC-projeção; FC-boca (parte de comparecimento).
- **6-P2** (cerca de 90). Função: o que não se sabe e o estado do texto. Conteúdo: FC-não-diz; FC-Brasil (forma curta); FC-regulação; FC-rascunho, com a consequência: a validação pode mudar a composição das células e, com ela, estas conclusões.

### 3.12 Informações adicionais `{#informacoes-adicionais}` (cerca de 850)

Parágrafos IA-1 a IA-9, detalhados na seção 8 desta especificação. Rótulo em negrito no início de cada um (PRISMA 24 a 27). Sem lista com marcadores.

### 3.13 Referências `{#referencias}`

`# Referências {#referencias .unnumbered}` seguido de `::: {#refs}` e `:::`. Toda `@chave` citada existe em `revista/referencias.json` (gerado de `07-relatorio/references.bib`, `referencias_contexto.bib` e `referencias_metodo.bib`).

### 3.14 Apêndice A `{#sec-pendencias}` (cerca de 80)

- **AP-P1** (cerca de 80). Conteúdo: estas são as 18 pendências abertas; todas exigem decisão humana; a IA não fecha nenhuma, e nenhuma sugestão de IA preparada nos pacotes conta como validação; a ordem segue as etapas, porque decisões de busca e de triagem podem mudar o conjunto de incluídos e tudo o que vem depois; os marcadores **[A confirmar pelo autor]** do texto são contados à parte e não são pendências; o guia da revisão humana está em <https://felipelamarca.com/pesquisas-eleitorais-rs/revisao-humana.html>. Depois do parágrafo: `@@TABELA pendencias@@`. Fonte: `v1:L465`; plano, "São 11 callouts...".

### 3.15 Mapa PRISMA 2020, PRISMA-S e SWiM → texto novo

Para o S11 e para a auditoria (livro A11). Item → onde:

| Item | Onde |
|---|---|
| 1 Título | título e subtítulo |
| 2 Resumo (12 itens) | RS-1 a RS-7 |
| 3 Justificativa | 1.1, 1.3 |
| 4 Objetivos | 1.4-P1 |
| 5 Elegibilidade | 2.2, Q2, 2.7-P1 |
| 6 Fontes | 2.3-P1 |
| 7 Estratégia | 2.3-P1, S1 |
| 8 Seleção | 2.4 |
| 9 Coleta | 2.5-P1, 2.5-P3 |
| 10a/10b Itens | Q2, 2.5-P1, 2.5-P2 |
| 11 Risco de viés | 2.6 |
| 12 Medidas de efeito | 2.7-P2, 2.5-P2 |
| 13a a 13f Síntese | 2.7 |
| 14 Viés de relato | 2.7-P4, 2.8-P1 |
| 15 Certeza | 2.8 |
| 16a Fluxo | 3.1-P1, Fig. 2 |
| 16b Excluídos | 3.1-P2 |
| 17 Características | 3.1-P3, Tab. 1, S4 |
| 18 Risco de viés nos estudos | 3.2, Fig. 3, S5 |
| 19 Resultados individuais | Fig. 5, S6 |
| 20a a 20d Sínteses | 3.3 a 3.8, Tab. 2, Figs. 4 e 6, S8 |
| 21 Viés de relato | 3.8-P5 |
| 22 Certeza | Tab. 2 e cada parágrafo de célula |
| 23a a 23d Discussão | 4.1 e 4.2; 4.3; 4.4; 5 |
| 24a a 24c Registro, protocolo, emendas | IA-1, IA-2, 2.1 |
| 25 Financiamento | IA-3 |
| 26 Conflitos | IA-4 |
| 27 Dados e código | IA-6 |
| PRISMA-S 8, 13, 15, 16 | S1; 2.3-P1 |
| SWiM 1a e 1b | 2.7-P1, 2.1-P3 |
| SWiM 2 | 2.7-P2, 2.5-P2 |
| SWiM 3 e 4 | 2.7-P3 |
| SWiM 5 | 2.7-P5, 3.10 |
| SWiM 6 | 2.8 |
| SWiM 7 | 2.7-P5, 3.3-P2 |
| SWiM 8 | 3.4 a 3.7 |
| SWiM 9 | 4.4-P6 |

---

## 4. Enunciados C01 a C18

Regra: cada célula tem ao menos um span `[<enunciado literal>]{.enunciado cel="Cxx"}` em prosa, no parágrafo indicado; o texto do span é copiado de `revista/celulas.json` sem mudar uma vírgula (a lista abaixo foi gerada por programa a partir desse arquivo). A frase de certeza já está dentro do span; o k tem de aparecer no mesmo parágrafo, dentro ou fora do span. A Tab. 2 (SoF) tem outro span por célula, gerado pelo programador. Nenhuma Mensagem, nenhum Resumo e nenhum parágrafo sem célula leva span. As mensagens que juntam duas células (MP-1, FC-apoio) dizem "cada uma com certeza muito baixa".

| Célula | Bloco | Parágrafo | k fora do span? | Estudos que o parágrafo nomeia | Cuidados |
|---|---|---|---|---|---|
| C01 | apoio principal | 3.4-P1 | já no span ("4 de 4") | @Agranov2017a, @Farjam2020a, @Timotei2013a, @Tyszler2015 | "três dos quatro" por extenso; meta A em parágrafo separado |
| C02 | apoio principal | 3.4-P3 | já no span | @Tal2015a, @Lammers2022a, @Fichnova2015a, @Witsman2016a | "3 de 4 efeitos" é livre; meta B em parágrafo separado |
| C03 | apoio principal | 3.4-P5 | já no span ("1 estudo") | @Boukouras2020a | – |
| C04 | apoio principal | 3.4-P6 | já no span | @Feltovich2022 | classe não randomizada dita no parágrafo |
| C05 | apoio principal | 3.4-P7 | já no span ("2 estudos") | @Morton2015a, @Chatterjee2019a | p = 1; IC 0,01 a 0,99 |
| C06 | apoio principal | 3.4-P8 | já no span | @Araujo2021a | – |
| C07 | viabilidade | 3.5-P1 | já no span | @Cornejo2023a | – |
| C08 | viabilidade | 3.5-P2 | escrever "dois experimentos" | @Schlegel2023, @Freden2024a | o span traz "2 de 3 efeitos" |
| C09 | *momentum* | 3.6-P2 | já no span | @Dahlgaard2016a | – |
| C10 | *momentum* | 3.6-P3 | já no span | @Meer2015a | – |
| C11 | *momentum* | 3.6-P4 | já no span | @Stolwijk2016a (e @Unkelbach2022a como excluído) | – |
| C12 | comparecimento | 3.7-P1 | **sim: "três estudos"** | @Agranov2017a, @Groer2010a, @Erlich2023 | proporção 0,67; IC 0,09 a 0,99; p = 1 |
| C13 | comparecimento | 3.7-P2 | já no span ("1 experimento") | @Gerber2020a | certeza moderada; nulo por ±δ |
| C14 | comparecimento | 3.7-P3 | já no span | @Westwood2020a | certeza baixa |
| C15 | comparecimento | 3.7-P4 | já no span | @Klor2017a | – |
| C16 | comparecimento | 3.7-P5 | já no span | @Grillo2024c | – |
| C17 | comparecimento | 3.7-P6 | **sim: "dois experimentos naturais"** | @Morton2015a, @Chatterjee2019a | proporção 0,00; p = 1 |
| C18 | comparecimento | 3.7-P7 | já no span ("2 estudos") | @Stolwijk2019b, @Brugarolas2021 | certeza baixa; p = 0,5 |

Enunciados literais e números de cada célula (de `revista/celulas.json`):

- **C01** (apoio principal; pesquisa pré-eleitoral × sem pesquisa × randomizado). k = 4; direção: 4 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,40 a 1,00); p do teste de sinal = 0,125; δ = 0,0573; certeza muito baixa; estudos: @Agranov2017a, @Farjam2020a, @Timotei2013a, @Tyszler2015.
  `[A evidência é muito incerta sobre se ver pesquisa que mostra quem está à frente, frente a não ver pesquisa, aumenta o apoio ao líder (4 de 4 estudos na direção bandwagon, 3 deles de laboratório ou vinheta; certeza muito baixa).]{.enunciado cel="C01"}`
- **C02** (apoio principal; pesquisa pré-eleitoral × mesmo candidato atrás × randomizado). k = 4; direção: 4 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,40 a 1,00); p do teste de sinal = 0,125; δ = 0,044; certeza muito baixa; estudos: @Tal2015a, @Lammers2022a, @Fichnova2015a, @Witsman2016a.
  `[A evidência é muito incerta sobre se ver o candidato à frente numa pesquisa, em vez de atrás, aumenta o apoio a ele (4 de 4 estudos na direção bandwagon, todos de laboratório ou vinheta e em risco de viés alto; certeza muito baixa).]{.enunciado cel="C02"}`
- **C03** (apoio principal; pesquisa pré-eleitoral × outro resultado × randomizado). k = 1; direção: 1 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,03 a 1,00); p do teste de sinal = 1; δ = 0,044; certeza muito baixa; estudos: @Boukouras2020a.
  `[A evidência é muito incerta sobre se revelar um conjunto de pesquisas diferente, da mesma eleição, aumenta a vitória do candidato à frente (1 estudo de laboratório, 3 de 3 efeitos na direção bandwagon; certeza muito baixa).]{.enunciado cel="C03"}`
- **C04** (apoio principal; pesquisa pré-eleitoral × outro resultado × não randomizado). k = 1; direção: 1 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,03 a 1,00); p do teste de sinal = 1; δ = 0,044; certeza muito baixa; estudos: @Feltovich2022.
  `[A evidência é muito incerta sobre se ver uma prévia com maior parcela do incumbente aumenta o voto nele (1 estudo de laboratório, com contraste não sorteado; certeza muito baixa).]{.enunciado cel="C04"}`
- **C05** (apoio principal; boca de urna × antes e depois da proibição × não randomizado). k = 2; direção: 1 a favor, 1 contra, 0 misto(s), 0 nulo(s); proporção 0,50 (IC 95% 0,01 a 0,99); p do teste de sinal = 1; δ = 0,044; certeza muito baixa; estudos: @Morton2015a, @Chatterjee2019a.
  `[A evidência é muito incerta sobre se a divulgação de boca de urna antes do fechamento das urnas aumenta ou reduz o apoio ao líder (2 estudos em direções opostas; certeza muito baixa).]{.enunciado cel="C05"}`
- **C06** (apoio principal; apuração parcial oficial × unidades não expostas × não randomizado). k = 1; direção: 1 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,03 a 1,00); p do teste de sinal = 1; δ = 0,044; certeza muito baixa; estudos: @Araujo2021a.
  `[A evidência é muito incerta sobre se a divulgação oficial de apuração parcial enquanto a votação continua aumenta o voto no candidato à frente (1 estudo brasileiro na direção bandwagon; certeza muito baixa).]{.enunciado cel="C06"}`
- **C07** (viabilidade; pesquisa pré-eleitoral × sem pesquisa × randomizado). k = 1; direção: 1 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,03 a 1,00); p do teste de sinal = 1; δ = 0,044; certeza muito baixa; estudos: @Cornejo2023a.
  `[A evidência é muito incerta sobre se ver pesquisa que mostra um candidato de oposição como segundo colocado viável aumenta o apoio a ele (1 estudo no México; certeza muito baixa).]{.enunciado cel="C07"}`
- **C08** (viabilidade; pesquisa pré-eleitoral × outro resultado × randomizado). k = 2; direção: 1 a favor, 0 contra, 1 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,03 a 1,00); p do teste de sinal = 1; δ = 0,044; certeza muito baixa; estudos: @Schlegel2023, @Freden2024a.
  `[A evidência é muito incerta sobre se pesquisas que mostram quais opções são viáveis levam eleitores a desertar para a opção viável (1 estudo a favor e 1 misto, com 2 de 3 efeitos contrários; certeza muito baixa).]{.enunciado cel="C08"}`
- **C09** (*momentum*; pesquisa pré-eleitoral × sem pesquisa × randomizado). k = 1; direção: 1 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,03 a 1,00); p do teste de sinal = 1; δ = 0,044; certeza muito baixa; estudos: @Dahlgaard2016a.
  `[A evidência é muito incerta sobre se ver pesquisa que mostra um partido ganhando apoio, frente a não ver pesquisa, aumenta o voto nele (momentum; 1 estudo; certeza muito baixa).]{.enunciado cel="C09"}`
- **C10** (*momentum*; pesquisa pré-eleitoral × outro × randomizado). k = 1; direção: 1 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,03 a 1,00); p do teste de sinal = 1; δ = 0,044; certeza muito baixa; estudos: @Meer2015a.
  `[A evidência é muito incerta sobre se ver pesquisa que mostra um partido ganhando apoio aumenta o voto nele (momentum; 1 estudo; certeza muito baixa).]{.enunciado cel="C10"}`
- **C11** (*momentum*; pesquisa pré-eleitoral × outro resultado × não randomizado). k = 1; direção: 1 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,03 a 1,00); p do teste de sinal = 1; δ = 0,044; certeza muito baixa; estudos: @Stolwijk2016a; excluído por risco crítico: @Unkelbach2022a.
  `[A evidência é muito incerta sobre se a cobertura de pesquisas favorável a um partido aumenta o voto nele (momentum; 1 estudo observacional; certeza muito baixa).]{.enunciado cel="C11"}`
- **C12** (comparecimento; pesquisa pré-eleitoral × sem pesquisa × randomizado). k = 3; direção: 2 a favor, 1 contra, 0 misto(s), 0 nulo(s); proporção 0,67 (IC 95% 0,09 a 0,99); p do teste de sinal = 1; δ = 0,046; certeza muito baixa; estudos: @Agranov2017a, @Groer2010a, @Erlich2023.
  `[A evidência é muito incerta sobre se ver pesquisa, frente a não ver, aumenta ou reduz o comparecimento (2 estudos de laboratório na direção de mobilização e 1 com candidatos reais na de desmobilização; certeza muito baixa).]{.enunciado cel="C12"}`
- **C13** (comparecimento; pesquisa pré-eleitoral × outro resultado × randomizado). k = 1; direção: 0 a favor, 0 contra, 0 misto(s), 1 nulo(s); proporção não se aplica (o único estudo é nulo por ±δ); p do teste de sinal = não se aplica; δ = 0,046; certeza moderada; estudos: @Gerber2020a.
  `[Receber pesquisa que mostra disputa apertada, em vez de folgada, provavelmente não muda o comparecimento além de 2 p.p. para mais ou para menos (efeito nulo ou trivial; 1 experimento de campo; certeza moderada).]{.enunciado cel="C13"}`
- **C14** (comparecimento; agregador ou projeção × outro resultado × randomizado). k = 1; direção: 0 a favor, 1 contra, 0 misto(s), 0 nulo(s); proporção 0,00 (IC 95% 0,00 a 0,97); p do teste de sinal = 1; δ = 0,046; certeza baixa; estudos: @Westwood2020a.
  `[Ver projeções de agregador que mostram probabilidade de vitória mais distante de 50:50 pode reduzir a decisão de votar (direção de desmobilização; 1 estudo; certeza baixa).]{.enunciado cel="C14"}`
- **C15** (comparecimento; pesquisa pré-eleitoral × sem pesquisa × não randomizado). k = 1; direção: 1 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,03 a 1,00); p do teste de sinal = 1; δ = 0,046; certeza muito baixa; estudos: @Klor2017a.
  `[A evidência é muito incerta sobre se revelar a distribuição de preferências do eleitorado aumenta o comparecimento (1 estudo de laboratório, antes e depois no mesmo sujeito; certeza muito baixa).]{.enunciado cel="C15"}`
- **C16** (comparecimento; boca de urna × outro resultado × não randomizado). k = 1; direção: 0 a favor, 1 contra, 0 misto(s), 0 nulo(s); proporção 0,00 (IC 95% 0,00 a 0,97); p do teste de sinal = 1; δ = 0,046; certeza muito baixa; estudos: @Grillo2024c.
  `[A evidência é muito incerta sobre se a boca de urna divulgada mais cedo durante a votação reduz o comparecimento (1 estudo na direção de desmobilização, com IC que cruza zero; certeza muito baixa).]{.enunciado cel="C16"}`
- **C17** (comparecimento; boca de urna × antes e depois da proibição × não randomizado). k = 2; direção: 0 a favor, 1 contra, 1 misto(s), 0 nulo(s); proporção 0,00 (IC 95% 0,00 a 0,97); p do teste de sinal = 1; δ = 0,046; certeza muito baixa; estudos: @Morton2015a, @Chatterjee2019a.
  `[A evidência é muito incerta sobre se a divulgação de boca de urna antes do fechamento das urnas reduz o comparecimento (1 estudo na direção de desmobilização e 1 misto; certeza muito baixa).]{.enunciado cel="C17"}`
- **C18** (comparecimento; pesquisa pré-eleitoral × unidades não expostas × não randomizado). k = 2; direção: 2 a favor, 0 contra, 0 misto(s), 0 nulo(s); proporção 1,00 (IC 95% 0,16 a 1,00); p do teste de sinal = 0,5; δ = 0,046; certeza baixa; estudos: @Stolwijk2019b, @Brugarolas2021.
  `[Ter visto a divulgação de pesquisas pode aumentar a intenção de votar ou o comparecimento (2 estudos observacionais em eleições reais, ambos na direção de mobilização; certeza baixa).]{.enunciado cel="C18"}`
- **Célula vazia** (agregador ou projeção × comparecimento × sem pesquisa × não randomizado): k = 0 na síntese principal, sem linha em `certeza.csv` e sem enunciado; @Kaplan2019a, o único estudo, ficou fora por risco crítico. Citada em 3.3-P1 e 3.8-P3, sem span.

---

## 5. Mapa do v1

Cada bloco de `_esqueleto_v1_oqf.qmd` (linha de início) → destino no texto novo, ou "descartado: motivo". Os títulos de seção não entram no mapa. Callouts e tabelas contam como um bloco.

| Linha v1 | Bloco | Destino |
|---|---|---|
| L1 | YAML (título OQF; bibliografia com `../`) | YAML novo (seção 2): título com "revisão sistemática", `revista/referencias.json`, sem `../` |
| L19 | comentário HTML de produção | descartado: nota interna da v1, com caminhos; o esqueleto novo tem seu próprio comentário |
| L30 | aviso de rascunho | AV (sem caminho de arquivo; com a nota de autoria por IA e a data da última busca) |
| L36 | caixa "Como ler este documento" | Q1, linhas 1 e 11; regra caixa-3 em 2.8-P2 |
| L41 | Mensagem: apoio | MP-1 (+ ressalva sobre @Witsman2016a) |
| L42 | Mensagem: comparecimento | MP-2 |
| L43 | Mensagem: boca de urna | MP-3 |
| L44 | Mensagem: Brasil | MP-4 (frase corrigida: FC-Brasil) |
| L45 | Mensagem: o que não permite dizer | MP-5 |
| L49 | RE: problema e pergunta | RE-1 e 1.1-P1 |
| L51 | RE: o que foi feito | RE-3 |
| L53 | RE: achado *bandwagon* e metas | RE-2 e RE-4 |
| L55 | RE: comparecimento | RE-5 |
| L57 | RE: Brasil e STF | RE-6 (frase corrigida) |
| L59 | RE: rascunho | RE-7 |
| L64 | callout P038 | CO-P038, movido para logo depois das Mensagens |
| L71 | Resumo: objetivos | RS-2 |
| L73 | Resumo: métodos | RS-3 |
| L75 | Resumo: resultados | RS-4 (metas numa oração, sem g) |
| L77 | Resumo: conclusões | RS-6 |
| L79 | Resumo: registro e financiamento | RS-7 |
| L83 | *Abstract*: objectives | AB-2 |
| L85 | *Abstract*: methods | AB-3 |
| L87 | *Abstract*: results | AB-4 |
| L89 | *Abstract*: conclusions | AB-6 |
| L91 | *Abstract*: registration and funding | AB-7 |
| L97 | regras brasileiras de registro | 1.1-P2 |
| L99 | art. 35-A e STF 2006 | 1.1-P2 |
| L101 | PLs de 2022, CPI, ESOMAR/WAPOR | 1.1-P3 |
| L103 | precisão × mudança de opinião | 1.1-P4 |
| L107 | conceitos de Barnfield | 1.2-P1 (+ efeito "Titanic", verificado) |
| L109 | distinções → células | 1.2-P3 e Q1 |
| L113 | pergunta no formato X → Y | 1.4-P1 |
| L115 | tabela PICOC, com a legenda em L123 | Q2 (quadro, legenda sem caminho) |
| L127 | revisões anteriores e o que esta acrescenta | 1.3-P1 e 1.3-P2; @Hardmeier2008 deixa de ser descrito como síntese com meta-análise (não verificado); a nota com o endereço do MAPE sai (decisão do usuário: MAPE só na afiliação); o formato OQF passa a 2.1-P1, citado por @Schaefer2025OQF |
| L131 | teoria da mudança | 1.2-P2 (corrigido pelo DAG: só o E2 passa pela viabilidade) e Fig. 1 |
| L135 | abertura da seção de efeito | 3.3-P1; os 14 estudos fora da síntese vão a 3.1-P4 |
| L137 | `@@TABELA swim@@` | substituída pela Tab. 2 (SoF) e pela Fig. 4 em 3.3; contagens por célula também em S8 |
| L141 | C01 | 3.4-P1 |
| L143 | meta A | 3.4-P2 (+ τ, intervalo de predição não interpretado, frase de assimetria) |
| L145 | figura *forest* da meta A | Fig. 6 (`fig-metas`), redesenhada |
| L147 | C02 | 3.4-P3 |
| L149 | meta B | 3.4-P4 (+ ressalva sobre @Witsman2016a) |
| L151 | figura *forest* da meta B | Fig. 6 (`fig-metas`), redesenhada |
| L153 | C03 e C04 | 3.4-P5 e 3.4-P6, separados por classe de desenho |
| L155 | C05 e C06 | 3.4-P7 e 3.4-P8 |
| L157 | leitura conjunta (agrupamento amplo) | 3.8-P1 (sai de 3.4 para não virar manchete) |
| L161 | viabilidade | 3.5-P1 e 3.5-P2 |
| L165 | *momentum* | 3.6-P1 a 3.6-P4 |
| L169 | C13 | 3.7-P2 |
| L171 | C18 | 3.7-P7 |
| L173 | C12 e C15 | 3.7-P1 e 3.7-P4 |
| L175 | C14 | 3.7-P3 |
| L177 | C17 e C16 | 3.7-P6 e 3.7-P5 |
| L179 | contraste *post hoc* entre formatos | 3.7-P8 |
| L183 | só contexto real | 3.8-P2 |
| L185 | com críticos | 3.8-P3 |
| L187 | outras sensibilidades | 3.8-P4 |
| L192 | callout do efeito | CO-efeito; os itens (i) a (vi) passam a 3.8-P6 e 4.4-P7 |
| L197 | mecanismo: caráter descritivo | 3.9-P1 (sem caminho de arquivo) |
| L199 | contagens de mecanismos | 3.9-P2 |
| L201 | expectativas | 3.9-P3 |
| L203 | heurística, conformidade, simpatia | 3.9-P4 |
| L205 | voto estratégico | 3.9-P5 |
| L207 | pivotalidade e emoções | 3.9-P6 (a parte de emoções vai a 3.9-P4) |
| L212 | callout de mecanismo | CO-mecanismo |
| L217 | moderadores: caráter descritivo | 3.10-P1 |
| L219 | realismo | 3.10-P3 e Fig. 7 |
| L221 | sistema e competidores | 3.10-P4 |
| L223 | proximidade | 3.10-P5 |
| L225 | momento e tipo de eleição | 3.10-P6 |
| L227 | partidarismo e sofisticação | 3.10-P7 |
| L229 | efeitos que se anulam | 3.10-P8 |
| L231 | equidade | 3.10-P8 |
| L233 | voto obrigatório | 3.10-P9 |
| L238 | callout de moderadores | CO-moderadores |
| L243 | percepção, implementação e custo | 3.11-P1 |
| L245 | estudo futuro de percepção e custo | 5.3-P1, item (vii) |
| L249 | introdução da caixa | 5.1-P1 |
| L251 | `@@TABELA oqf_principal@@` | Tab. 4 (5.1) |
| L253 | `@@TABELA caixa_celulas@@` | suplemento S9 (link em 5.1-P1) |
| L255 | legenda dos rótulos | 2.8-P2 e 5.1-P1 |
| L257 | rótulo Positivo ou Negativo | 2.8-P2 |
| L258 | rótulo Misto | 2.8-P2 |
| L259 | rótulo Nulo | 2.8-P2 |
| L260 | rótulo Inconclusivo | 2.8-P2 |
| L261 | rótulo Pendente | 2.8-P2 |
| L263 | por que tudo é Inconclusivo | 5.1-P2 |
| L268 | callout da caixa | CO-caixa |
| L273 | o que a evidência permite dizer | 5.2-P1 (frase do Brasil corrigida) |
| L275 | restrição à divulgação | 5.2-P2 |
| L277 | transferibilidade | 5.2-P3 |
| L279 | fator voto obrigatório | Tab. 5 e 5.2-P3 |
| L281 | fator dois turnos | Tab. 5 e 5.2-P3 |
| L283 | fator regulação | Tab. 5 e 5.2-P3 |
| L285 | fator confiança | Tab. 5, 5.2-P3 e 4.3-P3 |
| L287 | `@@TABELA regional@@` | suplemento S10 (link em 5.2-P4) |
| L289 | estudos da região | 5.2-P4 |
| L291 | implicações para a pesquisa | 5.3-P1 |
| L296 | callout do Brasil | CO-brasil |
| L303 | protocolo e atalhos | 2.1-P1 e 2.1-P2 |
| L305 | E001 | IA-1 e 2.1-P3 |
| L306 | E002 | IA-1 e 2.1-P3 |
| L307 | Emenda 1 | IA-1, 2.1-P3 e 2.2-P1 |
| L308 | Emenda 2 | IA-1 e 2.5-P1 |
| L309 | Emenda 3 | IA-1 e 2.6-P1 |
| L310 | Emenda 4 | IA-1 e 2.1-P3 |
| L311 | Emenda 5 | IA-1 e 2.1-P3 |
| L312 | Emenda 6 | IA-1 e 2.4-P2 |
| L316 | critérios de elegibilidade | 2.2-P1 |
| L320 | fontes, estratégias e datas | 2.3-P1 |
| L322 | âncoras e lacunas | 2.3-P2 |
| L327 | callout da busca | CO-busca |
| L332 | triagem de títulos e resumos | 2.4-P1 |
| L334 | Emenda 6b | 2.4-P2 e 3.1-P1 |
| L336 | texto completo | 2.4-P3 |
| L340 | figura PRISMA | Fig. 2 (3.1), redesenhada com as 18 pendências; a ressalva "17 das 18" deixa de ser necessária |
| L342 | fluxo PRISMA | 3.1-P1 |
| L347 | callout da seleção | CO-selecao (2.4) |
| L352 | extração | 2.5-P1 |
| L354 | reextração e arbitragem | 2.5-P3 |
| L359 | callout da extração | CO-extracao |
| L364 | risco de viés (método e contagens) | 2.6-P1 (método) e 3.2-P1 (contagens) |
| L369 | callout do risco de viés | CO-rob, movido para 3.2 (plano) |
| L374 | célula e sinal | 2.7-P1 e 2.7-P2 |
| L376 | SWiM, δ, fora da contagem, ICC | 2.7-P3, 2.5-P2 e Q1 |
| L378 | metas exploratórias | 2.7-P4 |
| L382 | GRADE | 2.8-P1 e 3.3-P1 |
| L387 | callout da certeza | CO-certeza; as três decisões passam a 4.4-P7 |
| L392 | uso de IA | 2.9-P1 |
| L398 | limitação: laboratório e vinheta | 4.3-P1 |
| L400 | limitação: poucos estudos | 4.3-P2 |
| L402 | limitação: dados de figura | 4.3-P2 e 2.5-P2 |
| L404 | limitação: sem meta principal | 4.3-P2 |
| L406 | limitação: risco de viés | 4.3-P2 |
| L408 | limitação: contrastes heterogêneos | 4.3-P2 |
| L410 | limitação: dados anteriores a 2010 | 4.3-P2 |
| L412 | limitação: Brasil | 4.3-P1 (FC-Brasil) e 4.3-P3 |
| L416 | processo: fontes restritas | 4.4-P2 |
| L418 | processo: IA sem validação | 4.4-P3 a 4.4-P5 |
| L420 | processo: correção de atribuição | 4.4-P5 e 2.9-P1 |
| L422 | processo: papel humano gravado | 4.4-P3 |
| L424 | processo: triagem complementar | 4.4-P3 |
| L426 | processo: âncoras e PRESS | 4.4-P2 |
| L428 | processo: mesmo provedor | 4.4-P8 (e 4.4-P4 e 4.4-P5) |
| L430 | processo: concordância da extração | 4.4-P4 |
| L432 | processo: correções por IA | 4.4-P4 |
| L434 | processo: defeitos da ferramenta | 4.4-P8 |
| L436 | processo: PDFs não recuperados | 4.4-P3 |
| L438 | processo: ROBINS-I × ROBINS-E | 4.4-P5 |
| L440 | processo: decisões depois dos dados | 4.4-P6 |
| L442 | processo: outras | 4.4-P2 (datas e idiomas), 4.4-P3 (duplicatas), 4.4-P6 (análises não feitas, meta B) e 4.4-P8 (redação por IA) |
| L446 | dados e código | IA-6 |
| L448 | relatório técnico completo | IA-6 |
| L450 | financiamento | IA-3 |
| L452 | conflitos | IA-4 |
| L454 | uso de IA | IA-7 |
| L456 | como citar | IA-8 (sem "formato O que funciona?"; com "não citar como final") |
| L460 | `::: {#refs}` | Referências |
| L465 | introdução do Apêndice A | AP-P1 |
| L467 | `@@TABELA pendencias@@` | Apêndice A (mesmo marcador) |

Correções de conteúdo que o mapa carrega (nenhum número verificado se perde): a frase do Brasil (L44, L57, L273, L412); Hardmeier (L127); o DAG (L131); o nome "dicionário `FORA`" vira "fora da contagem" em todo o texto; caminhos de arquivo saem de todos os blocos (L30, L123, L131, L192, L197, L243, L303, L376).

---

## 6. O que o redator NÃO faz

1. **Análise nova.** Nada de recalcular, reagrupar, recontar, reclassificar célula, alvo, comparador, lista de efeitos fora da contagem, certeza ou rótulo. Nada de médias, porcentagens ou somas que não estejam nas fontes da seção 0. Pedido de leitor que exija isso vira "decisão do autor" (seção 7).
2. **Número fora das fontes.** Só os das siglas da seção 0. Armadilhas já identificadas, que a trava reprovaria: a mediana de p0 da célula sem pesquisa (0,73); os percentuais do contraste de @Witsman2016a; o número de artigos de Barnfield; o ano de início do período coberto por Coşgun; a data da versão da ROBINS-I V2; datas de tramitação de 2025; o número de urnas de @Araujo2021a; os κ por domínio do risco de viés; o percentual e o κ da recomendação 9 de Garritty; qualquer *hash* sha256. Anos só se estiverem no v1, nos `.bib` ou em `incluidos.csv` (não servem, por exemplo, 2014, 2005, 2003, 2002 ou 1996). Datas dd/mm/aaaa só da lista da trava (v1, protocolo, 24/09/2026 e 25/09/2026).
3. **Conclusão atribuída a revisão não verificada.** Nenhuma frase com @Hardmeier2008 tem verbo de conclusão ("conclui", "mostra", "encontra", "aponta", "indica", "sugere", "revela", nem em inglês); ele nunca é chamado de meta-análise. A meta-análise de Hardmeier e Roth, citada por Moy e Rinke, não entra (não lida, sem referência e com ano fora da lista branca).
4. **Recomendação acima da certeza.** Com certeza muito baixa, só "a evidência não permite concluir" e implicações de pesquisa e de desenho de avaliação (livro R6.8). Nada de "deve", "recomendamos", "é preciso restringir" ou "é preciso manter".
5. **Caminhos de arquivo no texto**, inclusive nomes de arquivos e de variáveis internas (`FORA`, `celula_alvo`, `direcao_desejada`, `revisor_humano_1`, `nao_se_aplica`, `pontos_para_o_revisor.md`, `rs_log.jsonl`). Modelos de IA entre crases (`claude-opus-5-5`) são permitidos.
6. **`@sec` para seção sem número.** Para Mensagens, Resumo executivo, Resumo, *Abstract*, Informações adicionais, Referências e Apêndice A, só `[texto](#id)`.
7. **`column-*`** em qualquer lugar do `.qmd`. Tabela ou figura larga só pelas classes `.tabela-larga`/`.figura-larga`, que são do programador.
8. **`../`** em qualquer caminho ou link.
9. **Palavras e expressões proibidas:** "Neutro"; "sem efeito" (inclusive dentro de "sem efeito principal"); "não significativo" e qualquer forma de "significativ"; "benéfico", "benéfica", "danoso", "danos" (e, por prudência, "dano"); no *abstract*, *significant*, *beneficial*, *harmful*, *no effect*; "revisão por pares" ou "revisado por pares" (as leituras críticas da etapa 6 são "leituras críticas simuladas por IA"). A ressalva do teste de sinal do livro contém duas dessas palavras: usar a versão adaptada de 3.3-P3.
10. **Travessão** (—) e travessão curto usado como pausa. Negativos com o sinal de menos U+2212 (−0,41); intervalos com "a" ("0,40 a 1,00").
11. **Outros:** marcadores `@@...@@` fora de linha própria; figura ou tabela nova, fora do plano; lista com marcadores fora das Mensagens e dos quadros; negrito como rótulo de parágrafo no corpo; o agrupamento amplo nas Mensagens, no Resumo, no *Abstract* ou nas Conclusões; g pontual das metas no Resumo e no *Abstract*; "efeito médio" das metas como se fosse estimativa; o nome MAPE fora da afiliação (que já vem do `_revista.yml`); a mudança de qualquer vírgula de um `{.enunciado}`; os marcadores antigos `@@TABELA swim@@`, `@@TABELA caixa_celulas@@` e `@@TABELA regional@@` (substituídos ou movidos para o suplemento); conteúdo de `revista/figuras/`, `revista/tabelas/`, `montar_revisao_final.py` ou `vitrine/`, que são de outros agentes.

---

## 7. Decisões do autor que o texto apresenta como abertas

O texto diz que cada ponto está em aberto, diz o que muda se for decidido de um jeito ou de outro, quando a fonte permite, e não o resolve.

| # | Ponto em aberto | Pendência | Onde aparece |
|---|---|---|---|
| 1 | Alvo do efeito principal de @Witsman2016a (principal × viabilidade) | P039 | MP-1, 3.4-P4, 3.8-P6 (i), CO-brasil |
| 2 | Efeitos de @Feltovich2022 para fora da contagem (prévia como mecanismo de coordenação) | P039 | 3.4-P6, 3.8-P6 (ii), CO-moderadores |
| 3 | Contraste de @Schlegel2023 para fora da contagem ou só ressalva | P039 | 3.5-P2, 3.8-P6 (iii) |
| 4 | Volta à contagem do efeito de @Klor2017a hoje fora; análise de governadores como estudo à parte | P039 | 3.8-P6 (iv) |
| 5 | Volta de @Geers2018 à contagem, só pela direção | P039 | 3.8-P6 (v) |
| 6 | Efeito de variável instrumental de @Gerber2020a para fora da contagem | P039 | 3.8-P6 (vi), CO-mecanismo |
| 7 | Comparador de @Grillo2024c (outro resultado × unidades não expostas) | P039 | 3.7-P5, 3.8-P6 (vii) |
| 8 | Regra do ano da eleição nos experimentos de laboratório | P037 | 3.8-P4, 3.8-P6 (viii) |
| 9 | Desfecho de apoio de @Alabrese2024a (parcela de votos × probabilidade de vitória) | P039 | 4.4-P6 (reclassificações) |
| 10 | Domínio de dados faltantes de @Fichnova2015a | P033 | CO-rob |
| 11 | Não rebaixar corpos com preocupação só no relato seletivo | P036, P042 | 4.4-P7 (i), CO-certeza |
| 12 | Rebaixar um nível, e não dois, a célula de @Stolwijk2019b e @Brugarolas2021 | P036 | 3.7-P7, 4.4-P7 (ii) |
| 13 | Rebaixar por viés de publicação o agrupamento amplo randomizado (baixa × muito baixa) | P036 | 3.8-P1, 4.4-P7 (iii) |
| 14 | Meta do mesmo candidato atrás rodada depois do GRADE | P036 | 3.4-P4, 4.4-P6 |
| 15 | Busca suplementar com os termos que faltam (proibição, apuração parcial, comparecimento na BDTD) | P001, P004 | 2.3-P2, CO-busca, 4.4-P2 |
| 16 | Confirmação dos portões G3 a G9 | P004, P008, P023, P026, P033, P035, P038 | callouts de cada seção; CO-P038 |
| 17 | Papéis CRediT além de conceituação e protocolo | nenhuma (marcador **[A confirmar pelo autor]**) | IA-5 |
| 18 | Licença do material próprio e acesso ao repositório privado | nenhuma (marcador) | IA-6 |

As pendências P019, P020, P006, P007, P041, P025 e P037 (concordância em geral) são de validação, não de julgamento, e entram pelos callouts de Métodos e por 4.4.

---

## 8. Informações adicionais

`# Informações adicionais {#informacoes-adicionais .unnumbered}`. Nove parágrafos, cada um com o rótulo em negrito no início (livro R7.1 a R7.8; frases-modelo M5 a M9 adaptadas).

- **IA-1 Diferenças entre protocolo e revisão** (cerca de 220; PRISMA 24c; M12; livro R7.2 a R7.4). Em prosa, com "(i) ... (ix)", cada desvio com data, momento (antes ou depois de ver os dados) e efeito provável ou resultado da sensibilidade:
  (i) E001, 19/09/2026, contingência prevista, antes da busca definitiva: estratégia em inglês ampliada depois da pré-revisão PRESS por IA;
  (ii) E002, 19/09/2026, depois da busca e antes da triagem: B01 substituída pela B05 por perda de 4 âncoras, e o *recall* final deixou de ser independente;
  (iii) Emenda 1, 20/09/2026, depois de ver o estudo: apuração parcial oficial no critério C2; afeta só @Araujo2021a, em célula própria; sem ele, os não randomizados de apoio ficam com 2 de 3;
  (iv) Emenda 2, 20/09/2026, depois do piloto, decidida pelo coordenador de IA: três variáveis do *codebook* redefinidas, o que não mexe diretamente nas células;
  (v) Emenda 3, 23/09/2026, antes de qualquer avaliação de risco de viés: *codebooks* copiados para o protocolo, e o árbitro trocado por custo, por decisão do autor, por outro do mesmo modelo do avaliador A (possível viés de afinidade);
  (vi) Emenda 4, 23/09/2026, depois da extração e antes de qualquer análise de efeito: geral do EPOC, célula de *momentum* e ICC imputado; o ICC de 0,20 não mudou contagens; o item 4d foi substituído pela Emenda 6a;
  (vii) Emenda 5, 23/09/2026, depois de ver a primeira síntese: células com o alvo, sinal por alvo, efeitos fora da contagem, críticos fora, classe de dois estudos, metas exploratórias, nulos por ±δ, sinal por *proxy* e sensibilidades; as sensibilidades com os efeitos fora da contagem e com os críticos não inverteram a direção dominante no apoio randomizado;
  (viii) Emenda 6, 23/09/2026, depois do G9: correção da atribuição humana (6a) e nova triagem, por IA, dos 336 registros sem resumo (6b), sem novo incluído;
  (ix) outros desvios: classificadores de desenho em desacordo fixados pelo coordenador, e não pelo árbitro; a meta do mesmo candidato atrás rodada depois do GRADE; as metas usaram o modelo CHE com RVE que o protocolo prevê para efeitos dependentes, e não o estimador citado na Emenda 5; análises planejadas e não feitas (moderadores e subgrupos, fatores de equidade, evidência faltante por célula, artigo como conglomerado, modelo de seleção).
  Tabela completa em [S3](suplemento.html#s3-emendas). Fontes: `emendas.md`; relatório técnico, "Outras informações"; `verificacao.md`, item 17.
- **IA-2 Registro e protocolo** (cerca de 40; PRISMA 24a e 24b; frase-modelo M5). "A revisão não foi registrada, por decisão do autor em 19/09/2026. O protocolo foi aprovado no portão G2 em 19/09/2026 e congelado com sha256 no *log* do projeto; as emendas estão registradas com a mudança, o motivo e a etapa." Não imprimir o *hash*.
- **IA-3 Financiamento** (cerca de 15; PRISMA 25; frase-modelo M6). "Esta revisão não recebeu financiamento específico, por declaração do autor."
- **IA-4 Conflitos de interesse** (cerca de 20; PRISMA 26; frase-modelo M7). "Nenhum, por declaração do autor, inclusive com o provedor das ferramentas de IA."
- **IA-5 Contribuições (CRediT)** (cerca de 90). Conceituação: Felipe Lamarca (pergunta aprovada no portão G1). Metodologia: Felipe Lamarca, no protocolo aprovado no portão G2; nas demais escolhas de método, **[A confirmar pelo autor]**. Curadoria de dados, análise formal, investigação, *software*, visualização, administração do projeto, recursos, supervisão, validação e escrita (revisão e edição): **[A confirmar pelo autor]**. Escrita (rascunho original): agentes de IA, que não são autores (Declaração de uso de IA). Obtenção de financiamento: não se aplica. Uma frase: as decisões que o *log* registra como do autor estão em @sec-ia. Fonte: `emendas.md`, Emenda 6a (o que o autor confirmou como seu).
- **IA-6 Disponibilidade de dados, código e materiais** (cerca de 170; PRISMA 27; livro R7.7 a R7.14; frase-modelo M8). Material por material, dizendo o que é aberto e o que é fechado:
  - aberto, na página do projeto (<https://felipelamarca.com/pesquisas-eleitorais-rs/>): este artigo em HTML, PDF e .docx; o material suplementar (S1 a S11: estratégias completas, atalhos, emendas, características estudo a estudo, risco de viés por domínio, efeitos individuais, efeitos fora da contagem, sensibilidades, caixa célula a célula, estudos regionais e *checklists*); o resumo em linguagem simples; o relatório técnico no formato PRISMA 2020, com a declaração de IA gerada do *log* (<https://felipelamarca.com/pesquisas-eleitorais-rs/relatorio-tecnico.html>); o guia da revisão humana; e a página de entrada;
  - fechado, no repositório privado do GitHub `felipelmc/pesquisas-eleitorais-rs`: protocolo congelado e emendas, *log* de buscas e registros, registro das decisões, *codebooks*, fichas com trechos literais, efeitos extraídos e conversões, julgamentos de risco de viés, entradas e saídas das análises, *prompts* dos agentes, *log* auditável e pacotes de revisão humana; as condições de acesso: **[A confirmar pelo autor]**;
  - fora do repositório: o código de análise da ferramenta de revisão (os *scripts* em R de efeitos e de síntese que ela chama), que fica no ambiente do autor; versões registradas: metafor 5.0.1, clubSandwich 0.7.0, Quarto 1.9.35 e Typst 0.14.2;
  - não redistribuído: os PDFs dos estudos;
  - sem identificador persistente nem depósito em repositório aberto; licença do material próprio: **[A confirmar pelo autor]**.
  Escrever em prosa, com "(i) ... (v)". Fonte: `v1:L446`, `v1:L448`; plano, etapa 10; CLAUDE.md do projeto (scripts R fora do repositório).
- **IA-7 Declaração de uso de inteligência artificial** (cerca de 170; livro R7.18 a R7.26, A27; frase-modelo M17 adaptada). Primeira frase, literal: "RASCUNHO NÃO VALIDADO: 18 pendências humanas abertas ([Apêndice A](#sec-pendencias))." Depois: modelos da Anthropic, pelo Claude Code, entre 19/09/2026 e 25/09/2026, com o coordenador `claude-opus-5-5` e subagentes `claude-sonnet-5`, `claude-opus-5` e `claude-opus-5-5`, e, nesta versão, subagentes Opus e Sonnet (@sec-ia); a IA decidiu a triagem de títulos e resumos e a triagem complementar dos registros sem resumo, e propôs, sem validação humana, a elegibilidade, a extração, as correções dos efeitos, o risco de viés e a certeza; agentes redigiram este texto e o resumo em linguagem simples a partir dos arquivos, e os números foram conferidos por programas; resultados da validação: concordância A × B de 0,97 (κ 0,90) na triagem e de 58,5% na recodificação da extração, medidas de consistência e não de acurácia, e *recall* não calculado; limitações: um só provedor, árbitro do mesmo modelo do avaliador A, versões de modelo que mudam; a responsabilidade pelo conteúdo é humana, e o autor ainda não revisou este texto (P038); a declaração completa, gerada do *log*, está no relatório técnico. Fonte: `v1:L454`.
- **IA-8 Versão e citação** (cerca de 50). Primeira frase, literal: "Versão de trabalho de 25/09/2026; não citar como final." Depois: "Como citar esta versão: Lamarca, Felipe. 2026. *Pesquisas eleitorais publicadas mudam o voto? Revisão sistemática rápida sobre os efeitos* bandwagon *e* underdog *e o comparecimento*. Documento de trabalho, rascunho não validado, versão de 25/09/2026. <https://felipelamarca.com/pesquisas-eleitorais-rs/>." Fonte: `v1:L456` atualizado.
- **IA-9 O que mudou desde 24/09** (cerca de 130; livro R2.17). Em prosa, com "(i) ... (vi)": (i) estrutura de artigo de revisão: métodos antes dos resultados, Discussão nova, um só resumo mais o resumo executivo, título com "revisão sistemática" e resumo em linguagem simples como documento separado; (ii) tabelas e figuras novas (resumo dos achados, características, hipóteses, transferibilidade, modelo lógico, risco de viés, proporção por célula) e as antigas redesenhadas em português, com vírgula decimal; tabelas estudo a estudo no suplemento; (iii) três correções de texto: a frase sobre o Brasil (o corte transversal de 46 países inclui o Brasil), a descrição de Hardmeier (deixou de ser chamada de meta-análise, porque não foi verificada) e a descrição do modelo lógico; a comparação com revisões anteriores passou a usar só conteúdo verificado; (iv) referências de método e o cruzamento dos atalhos com a diretriz de revisões rápidas; (v) nada mudou na análise: as mesmas células, contagens, certezas, metas e as 18 pendências da versão de 24/09/2026; e (vi) novos formatos (PDF, .docx, suplemento e página de entrada).

---

## 9. Resumo em linguagem simples

Documento separado: `09-documento-final/linguagem_simples.qmd` (etapa 4). Publicado como `linguagem-simples.html` e na página de entrada. Fica fora do artigo.

**YAML:**

```yaml
---
title: "Não se sabe se pesquisas eleitorais mudam o voto: os poucos experimentos apontam a favor de quem lidera, e a evidência é muito incerta"
lang: pt-BR
date: 2026-09-25
format:
  html:
    embed-resources: true
---
```

O título é a própria mensagem (livro R3.2) e não promete mais do que a certeza permite (R2.11). Alternativa aceita, se o passe de estilo encurtar: "Pesquisas eleitorais e voto: experimentos apontam a favor de quem lidera, mas a evidência é muito incerta".

**Regras:** de 600 a 750 palavras (alvo 680); presente do indicativo; sem citações, sem notas e sem referências; achado enunciado diretamente, sem "a análise mostra" (R3.1); subtítulos em forma de pergunta; as mesmas palavras do artigo para o mesmo nível de certeza (FC em linguagem comum); números só em unidades simples e só se estiverem no corpo do artigo (o *script* da etapa 4 confere); desfecho importante sem dados é mencionado (R3.5); nenhuma recomendação de política, só o que os achados significam para a política e para a pesquisa (R3.8); quando o intervalo inclui as duas direções, dizer que se sabe muito pouco sobre o tamanho (R3.7); dizer que o trabalho foi feito por agentes de IA e que o autor ainda não o conferiu (R3.9, R2.12); proibições da seção 6 desta especificação.

**Estrutura e conteúdo:**

1. **A revisão em resumo** (até 50 palavras; R3.3): os dois desfechos principais: nos experimentos, ver uma pesquisa tende a favorecer quem aparece à frente, mas a evidência é muito incerta; uma pesquisa apertada provavelmente não muda o comparecimento além de 2 em cada 100 eleitores; não há estudo sobre pesquisas no Brasil com dados só do país.
2. **Quadro na primeira página** (R3.4): `::: {.callout-note}` com o título "O que esta revisão estudou": a pergunta; 41 estudos; busca até 19/09/2026 nas bases e 20/09/2026 na busca por citação; feita por agentes de IA, rascunho com 18 pendências.
3. **Do que trata esta revisão?** (cerca de 100): o debate brasileiro (projetos de 2022 e a decisão do STF de 2006), a pergunta, o que são os efeitos *bandwagon* e *underdog* e a desmobilização, em palavras comuns.
4. **Que estudos entraram?** (cerca de 100): 41 estudos publicados de 2010 a 2024, a maioria dos Estados Unidos e da Europa, muitos de laboratório ou com candidatos inventados; poucos estudos por comparação (de 1 a 4); um só estudo brasileiro, sobre a apuração parcial, e não sobre pesquisa.
5. **O que encontramos?** (cerca de 190): apoio a quem lidera (4 de 4 experimentos em cada uma das duas comparações com mais estudos; evidência muito incerta; não se sabe o tamanho do efeito, e as duas estimativas exploratórias vão de negativo a positivo, isto é, sabe-se muito pouco sobre o tamanho); comparecimento (apertada × folgada: provavelmente nada além de 2 em cada 100; ter visto pesquisas pode aumentar; projeções que mostram a eleição decidida podem reduzir; boca de urna muito incerta); voto estratégico e *momentum*: poucos estudos, muito incertos.
6. **O que isso significa?** (cerca de 100): a evidência não permite dizer que pesquisas mudam o resultado das eleições, nem que não mudam; sozinha, não sustenta nem restringir nem manter as regras atuais; o que falta estudar (eleições reais no Brasil, comparação com não ver pesquisa).
7. **Quais são os limites?** (cerca de 100): trabalho feito por agentes de IA, ainda sem conferência humana (18 pendências); só duas bases e busca por citação; 342 de 526 textos não foram obtidos; decisões pendentes podem mudar as comparações.
8. **Até quando vai a busca?** (cerca de 45): busca nas bases em 19/09/2026 e por citação até 20/09/2026; versão de trabalho de 25/09/2026 (R3.6).
9. Linha final, literal: "Rascunho não validado; 18 pendências de revisão humana." seguida do link `[Leia a revisão completa](revisao.html)`.

Movimentos: E2 e E3 (título-achado e perguntas), livro R3.1 a R3.9, A12.

---

## 10. Sentinela

SHA256 das fontes de síntese, calculado em 24/09/2026 com `shasum -a 256`, da raiz:

```
c075097a6f119c0551beab82619cf9b01a5cc6adff640a324633e0bfff83beea  06-analise/certeza.csv
a140b57602eb755e3ae68274c2db794151c3210aa537faae63d113bfa50a8a80  06-analise/swim_principal/swim_resumo.json
a40533e25689daf10dd94f5c5cb57e7fc88f21df9190fe3c38b990fdf69c15fb  06-analise/meta_exploratoria/meta_resumo.json
7ca65f2853153ce63b44bbf618d4bd18c105577d0fcd82a334c2181754f7dca7  06-analise/meta_mesmo_candidato/meta_resumo.json
679f3b3c997b440f3166f618c8c00a9ba939c6ed77959399f9d127909d02ea9d  07-relatorio/_pendencias_abertas.json
```

Os dois primeiros batem com os registrados em `revista/celulas.json` (campo `fontes`). Antes de cada etapa, rodar de novo o mesmo comando; se algum valor mudar, esta especificação deixa de valer para as seções abaixo, que precisam ser reescritas (e `celulas.json` e `numeros_v2.json` regenerados antes):

| Arquivo que mudou | Seções a reescrever |
|---|---|
| `certeza.csv` | todos os spans e a Tab. 2; 3.3 a 3.8; 3.9-P3 a P6; 4.1; 4.4-P7; 5.1; 5.2-P1 e P2; 6; Mensagens; Resumo executivo; Resumo; *Abstract*; resumo em linguagem simples; seção 4 desta especificação |
| `swim_resumo.json` | as mesmas de `certeza.csv`, mais 3.1-P4, 3.10-P3 e P4 e as Figs. 4 e 5 |
| `meta_exploratoria/meta_resumo.json` | 3.4-P2; 4.3-P2; Fig. 6; FC-metas onde aparece |
| `meta_mesmo_candidato/meta_resumo.json` | 3.4-P4; 4.3-P2; Fig. 6; FC-metas onde aparece |
| `_pendencias_abertas.json` | AV; os 11 callouts; Apêndice A; 4.4; seção 7 desta especificação; IA-7; o número 18 em todo lugar (FC-rascunho) |
