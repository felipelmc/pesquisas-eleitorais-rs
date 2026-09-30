# Verificação independente da versão de entrega (Emenda 7)

Feita em 30/09/2026 por um subagente de IA (`claude-opus-5-5`) que não escreveu nenhum dos textos, seguindo `prompts_final/prompt_verificacao_entrega.md` à risca. O contrato é `spec_final.md`. Não alterei nenhum texto, não abri PDF de estudo, não rodei `rs.py` nem nada em segundo plano. Esta verificação é de IA e não valida nada.

Objetos conferidos, todos montados às 14:03:35, depois da última mudança de qualquer fonte (esqueletos, `legendas.yml`, `lacunas.yml`, `rotulos.yml`, `montar_*.py`); por isso não remontei:

- `09-documento-final/revisao_final.qmd` (artigo, com figuras, tabelas e quadros);
- `09-documento-final/suplemento.qmd` (Apêndices A a G, com `revista/tabelas/lacunas.yml`);
- `09-documento-final/linguagem_simples.qmd`.

A sentinela da `spec_final.md` (seção 10) bate nos sete arquivos: `certeza.csv`, `certeza_agrupamento_amplo.csv`, `swim_principal/swim_resumo.json`, os dois `meta_resumo.json`, `prisma_contagens.json` e `_pendencias_abertas.json` têm o mesmo *hash* de 30/09/2026. A análise não mudou.

## Resultado

**2 erros, 8 avisos e 14 casos ok com ressalva.**

- Nenhum número de célula, PRISMA, meta-análise, risco de viés, sensibilidade, Tab. 1, Tab. 2 ou efeito do Apêndice E diverge da fonte (160 conferências por programa, 0 divergências; 70 linhas do Apêndice E e 26 n da Tab. 2 sem divergência).
- Os 18 enunciados são literais de `certeza.csv`, com a certeza e a frase padrão certas. O g das metas não aparece nas Mensagens, no Resumo, no *Abstract* nem nas Conclusões.
- "RASCUNHO NÃO VALIDADO" aparece uma vez, na abertura da declaração de IA, com as 8 pendências certas. A tabela do Apêndice G é idêntica, célula a célula e na legenda, à da `spec_final.md` e bate com a Emenda 7 e com `_pendencias_abertas.json` menos a P038.
- **Os dois erros são de atribuição e de nome.** (E1) A legenda do fluxograma PRISMA chama o produto de "esta revisão". (E2) A seção 3.9 e a legenda da Tab. 3 dizem que o fichamento de mecanismos foi "conferido em bloco pelo autor"; a declaração dele cobre os 560 efeitos, o piloto e as 259 divergências da recodificação de 10 estudos, e não a codificação de mecanismos dos 41 estudos. A redação veio da `spec_final.md` (item 3.9 da seção 2.4 e `t_hipoteses` da seção 3.4), que foi além da declaração.
- A trava passa com 0 falhas e 1 aviso (8.588 palavras de corpo, alvo de 7.500 a 8.500).

## O que foi checado e quanto

| Conferência | O que foi feito | Quanto | Resultado |
|---|---|---|---|
| 1. Números | Cada número do texto, das tabelas, das legendas, das Mensagens, do Resumo, do *Abstract* e do resumo em linguagem simples contra `prisma_contagens.json`, `swim_*/swim_resumo.json` (principal e 7 sensibilidades), `meta_*/meta_resumo.json` e as tabelas de *leave-one-out*, `certeza*.csv`, `_delta_celula.txt`, `celulas.json`, `numeros_v2.json`, `insumos/tabelas/numeros.json`, `_pendencias_abertas.json`, `declaracao_uso_ia.md`, `04-qualidade/rob_*` (geral e 3 consensos), `emendas.md`, `correcoes_sessao_2026-09-23.csv` e `arbitragem_humana.csv`. Teste de sinal e Clopper-Pearson refeitos. Mesma afirmação comparada entre artigo, apêndices e resumo em linguagem simples | 160 conferências em `verif_entrega.py`, 70 linhas do Apêndice E, 26 n da Tab. 2 e leitura inteira dos três textos; a trava conferiu 1.472 números contra a lista branca | 0 divergências de número. Ressalvas de precisão em A5 (δ da célula) e R10 |
| 2. Certeza e direção | Certeza da célula certa e frase padrão em toda afirmação de efeito; direção por significância; força das recomendações; g das metas nos quatro blocos proibidos | 18 enunciados; todas as frases de efeito fora dos spans (Resultados, Discussão, seção 5, Conclusões, Tab. 3, legendas e linguagem simples) | 18 de 18 certos; 1 frase sem o verbo padrão (A4); nenhuma direção por significância; nenhum "deve" ou "recomendamos"; g das metas ausente dos quatro blocos |
| 3. Leitura às cegas | Direção invertida em Mensagens, Resumo, *Abstract*, Discussão 4.1 e Conclusões | 26 afirmações | Nenhuma soa igualmente confiante invertida sem o qualificador de certeza. Ressalvas de enquadramento em R2 a R4 |
| 4. Atribuição humana | Toda menção ao autor comparada com `declaracao_autor_2026-09-30.md`, Emenda 7 (7a a 7c), Emenda 6a (o que ele confirmou antes), Emenda 3, Emenda 4 e `elegibilidade_tc_final.csv` (quem decidiu cada excluído) | Cerca de 70 menções nos três textos, nas legendas e nas tabelas; 13 excluídos da tabela C | 1 erro (E2), 2 avisos (A2 e A3). Nenhuma frase atribui ao autor o risco de viés, o GRADE ou a triagem cega; todas as seções que relatam risco de viés ou certeza dizem que foram só de IA. Nome do produto errado uma vez (E1). Os 3 excluídos por extensão de regra são RS4220, RS4361 e RS4487 (Bischoff2012, Corbetta2013, Hizen2025), como na tabela C |
| 5. Autocontido | Um leitor só com o PDF entende pergunta, critérios, busca, seleção, extração, risco de viés, síntese, certeza, resultados por célula e limitações? Cada remissão por letra aponta para o apêndice certo? | 24 remissões (20 no artigo e 4 nos apêndices) | 24 de 24 certas. Faltas em A5 (conversão do δ), A7 (portões) e R12 |
| 6. Citações e revisões anteriores | Toda `@chave` em `revista/referencias.json`; chaves dos apêndices no `nocite` do artigo; revisões anteriores contra `revisoes_anteriores.md`; Brasil contra `contexto_brasil.md` e `pergunta.md`, seção 4; revisões rápidas contra `garritty_2024.md` | 89 chaves no artigo, 69 nos apêndices e 69 no `nocite`; 9 afirmações sobre Barnfield, Moy e Rinke, Hardmeier e Coşgun; 12 sobre o Brasil; 5 citações literais de Garritty e 4 classificações de recomendação | Todas as chaves existem, e todas as dos apêndices entram na lista de referências do artigo. Hardmeier é sempre "não verificada". Citações de Garritty literais. Ressalva R11 sobre a "brecha" de 2018 |
| 7. Declarações do autor | Informações adicionais contra a declaração do autor, a Emenda 7 e o ambiente (`Rscript`, `quarto`) | 5 itens | Todos presentes: sem conflito nem relação com a Anthropic; CRediT todo do autor, agentes fora da autoria; R 4.5.2, metafor 5.0.1, clubSandwich 0.7.0, Quarto 1.9.35 e Typst 0.14.2 conferidos no ambiente; repositório privado com acesso sob pedido; pacote público com MIT e CC BY 4.0; 0 marcadores "[A confirmar pelo autor]" |
| 8. Travas | `python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd` | 1 rodada | **OK, 0 falhas e 1 aviso**: 8.588 palavras de Introdução a Conclusões (A1). Datas, 1.472 números, 18 células, callouts, apêndice (8 pendências, sem a P038), citações, 19 referências cruzadas, proibições e revisões anteriores: OK |

## Divergências

Cada item traz o trecho, a fonte, a correção em texto exato e o arquivo onde se corrige. As linhas são de `revisao_final.qmd` (montado) e, entre parênteses, do esqueleto de origem.

### Erros

**E1. A legenda do fluxograma PRISMA chama o produto de "revisão".**

- **Trecho:** legenda da `@fig-prisma`, L242 (`legendas.yml`, L56): "As caixas do modelo PRISMA que não se aplicam a esta revisão (n = 0) foram omitidas."
- **Fonte:** Emenda 7c e `spec_final.md`, seção 1.7: o nome é "síntese sistemática de evidências conduzida com agentes de IA", ou "esta síntese"; nunca "esta revisão". É a única ocorrência nos três objetos. A trava não a pega porque procura "revisão sistemática".
- **Correção:** "As caixas do modelo PRISMA que não se aplicam a esta síntese (n = 0) foram omitidas."
- **Onde:** `revista/figuras/legendas.yml` (entrada `prisma`).

**E2. O fichamento de mecanismos aparece como "conferido em bloco pelo autor".**

- **Trechos:**
  - seção 3.9, L538 (esqueleto L328): "Nenhuma célula permitiu síntese formal de mecanismos, e o que segue, tirado do fichamento por IA conferido em bloco pelo autor, é descritivo (@tbl-hipoteses).";
  - legenda da Tab. 3, L562: "Síntese descritiva a partir do fichamento por IA, conferido em bloco pelo autor (Emenda 7)."
- **Fonte:** na declaração do autor, o bloco de extração cobre "os 560 efeitos conferidos na página do PDF; as 259 divergências da recodificação da extração; o piloto de 3 estudos". A Emenda 7a repete essa lista. A codificação de mecanismos (`mecanismo_testado`, `mecanismo_tipo_evidencia`, `mecanismo_descricao`) dos 41 estudos não está nela. Ela só entrou pelas 20 divergências dessas variáveis na recodificação cega, que cobriu 10 estudos (`arbitragem_humana.csv`). A frase atribui ao autor a conferência de um conjunto que a declaração não cobre. A `spec_final.md` pediu essa redação, e a correção vale também para ela.
- **Correção na 3.9:** "Nenhuma célula permitiu síntese formal de mecanismos, e o que segue, tirado do fichamento por IA, é descritivo (@tbl-hipoteses). Da codificação de mecanismos, o autor conferiu em bloco só as divergências da recodificação cega de 10 estudos, mantendo o valor original."
- **Correção na legenda:** "Síntese descritiva a partir do fichamento por IA; da codificação de mecanismos, o autor conferiu em bloco só as divergências da recodificação cega de 10 estudos (Emenda 7)."
- **Onde:** `_esqueleto_revisao_final.qmd` (3.9). A legenda da Tab. 3 é gerada em `montar_revisao_final.py`, L700 (código, do coordenador).

### Avisos

**A1. Tamanho do corpo acima do alvo (aviso da trava).**

- **Trecho:** de Introdução a Conclusões, 8.588 palavras pela trava (8.508 pelo comando da `spec_final.md`, seção 1.9), para um alvo de 7.500 a 8.500.
- **Fonte:** `spec_final.md`, seções 0 e 1.9 (tolerância de ±10% por subseção). Passam da tolerância: 3.1 (359 contra 320, +12%), 3.3 (185 contra 160, +16%) e Conclusões (236 contra 170, +39%). As Conclusões só levam frases canônicas, e o excesso delas é da própria especificação.
- **Correção possível, com cerca de 95 palavras a menos e nenhuma informação perdida (tudo está repetido em outro lugar):**
  1. 3.3 (esqueleto L250): apagar "A @tbl-sof as reúne numa só tabela, e não numa por comparação, desvio de formato que declaramos." e acrescentar o desvio em Informações adicionais, item (ix): "(ix) outros, como a tabela de resumo única para todas as comparações, a meta do mesmo candidato atrás, rodada depois do GRADE, e análises planejadas e não feitas".
  2. 3.3 (L250): apagar "O agrupamento amplo, decidido depois de ver os dados, está no Apêndice F." A legenda da Tab. 2 e a 3.8 já dizem isso.
  3. 3.6 (L288): apagar "*Momentum* é a pesquisa que mostra um partido ganhando apoio sem mostrar sua posição." (definido no Q1) e começar o parágrafo por "A célula de *momentum* veio da Emenda 4b, ...".
  4. 3.7 (L312): apagar o parágrafo "O contraste entre boca de urna e projeções, na direção de desmobilização, e pesquisas pré-eleitorais, na de mobilização, foi notado depois de ver os dados e se confunde com o desenho." e, na 3.10 (L342), trocar "(@fig-realismo; comparação descritiva, sem teste)" por "(@fig-realismo; comparação descritiva, *post hoc* e sem teste)".
  5. 3.10 (L342): trocar "e nenhum dos 3 não randomizados em eleição real mede pesquisa pré-eleitoral: tratam do dia da votação, com 2 *bandwagon* e 1 *underdog*" por "e os não randomizados em eleição real tratam do dia da votação" (a contagem está na 3.8).
  6. 4.3 (L372): trocar "Os 41 estudos vêm, na maioria, dos Estados Unidos e da Europa, e, dos 9 experimentos de apoio do agrupamento amplo, 8 usaram laboratório ou vinheta." por "Dos 9 experimentos de apoio do agrupamento amplo, 8 usaram laboratório ou vinheta." (a origem está na 3.1).
- **Onde:** `_esqueleto_revisao_final.qmd`.

**A2. "Aprovado ... o relato" sem dizer qual versão.**

- **Trecho:** 2.9, P2, L230 (L222): "... (vi) as 259 divergências da recodificação, mantido o valor original; e (vii) o relato."
- **Fonte:** a declaração cobre a "leitura do artigo, do suplemento e do relatório técnico" da versão de 24/09/2026; a P038 (aprovação do G9) segue aberta em `_pendencias_abertas.json`; a 4.4 e o Apêndice G dizem "a versão de 24/09/2026". Como está, o leitor entende que o autor aprovou este texto, o que ainda não aconteceu.
- **Correção:** "... (vi) as 259 divergências da recodificação, mantido o valor original; e (vii) o relato, na versão de 24/09/2026."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**A3. A frase canônica de IA atribui ao autor etapas inteiras.**

- **Trechos:** Mensagens, "Como foi feita", L42 (L38), e declaração de IA, L656 (L428): "O autor conferiu em bloco a busca, a seleção e a extração"; Resumo, L53 (L49): "o autor conferiu em bloco busca, seleção e extração"; *Abstract*, L74 (L70): "the author checked search, selection and extraction en bloc"; linguagem simples, L18: "O autor conferiu a busca, a seleção e os dados de cada estudo." e L47: "conferiu a busca, a seleção e os dados".
- **Fonte:** a declaração cobre, na seleção, as 81 divergências da triagem, as 165 propostas de elegibilidade, as 3 extensões de regra e os 145 pares de deduplicação. As 2.101 exclusões concordantes dos triadores de IA (1.314 e 787) e as 156 da Emenda 6b não passaram por pessoa, e é isso que a validação cega não feita deixa aberto. Na extração, a declaração cobre os efeitos, o piloto e as divergências da recodificação, e não os "dados de cada estudo" (características, contexto, mecanismos). Nas Mensagens, a frase não diz que a triagem ficou sem validação cega, e o leitor pode entender que a seleção foi conferida por inteiro.
- **Correção (frase canônica FC-IA, seção 1.10 da especificação):**
  - Mensagens e declaração de IA: "O autor conferiu em bloco partes da busca, da seleção e da extração (Apêndice G), e o risco de viés e a certeza da evidência foram julgados só por IA, sem validação humana." Na declaração de IA, manter "(@sec-ia)" no lugar de "(Apêndice G)".
  - Resumo: "o autor conferiu em bloco partes de busca, seleção e extração." Para ficar em 250 palavras, trocar também "Pesquisa apertada, em vez de folgada," por "Pesquisa apertada, e não folgada," e "além de ±2 pontos percentuais" por "além de ±2 p.p.".
  - *Abstract*: "the author checked parts of search, selection and extraction en bloc." Para compensar: "by more than 2 percentage points" vira "by over 2 percentage points", e "mostly laboratory or vignette studies" vira "mostly laboratory or vignette".
  - Linguagem simples, L18: "O autor conferiu partes da busca e da seleção e os números tirados de cada estudo." L47: "O autor aprovou o plano e conferiu partes da busca e da seleção e os números tirados dos estudos, mas o julgamento da qualidade dos estudos e da confiança na evidência não passou por uma pessoa."
- **Onde:** `_esqueleto_revisao_final.qmd` e `linguagem_simples.qmd` (e FC-IA na `spec_final.md`).

**A4. Afirmação de efeito com certeza baixa sem o verbo padrão.**

- **Trecho:** 4.1, P2, L584 (L356): "O jogo *online* de @Westwood2020a, que manipula a mesma proximidade percebida, acha desmobilização quando a projeção se afasta de 50:50 (certeza baixa), padrão que a teoria rival do artefato prevê, sem testá-la."
- **Fonte:** `spec_final.md`, seção 1.6: certeza baixa usa "pode". O enunciado de C14 diz "pode reduzir a decisão de votar".
- **Correção:** "No jogo *online* de @Westwood2020a, que manipula a mesma proximidade percebida, projeções mais distantes de 50:50 podem reduzir a decisão de votar (certeza baixa), padrão que a teoria rival do artefato prevê, sem testá-la."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**A5. O δ de 0,0573 é atribuído a uma célula ambígua, e a conversão não está descrita.**

- **Trechos:**
  - 2.7, L214 (L206): "O δ de 2 pontos percentuais, fixado no protocolo sem *benchmark*, virou g de 0,044 no apoio, 0,046 no comparecimento e 0,0573 na célula de pesquisa frente a nenhuma pesquisa.";
  - Q1, linha "δ e nulo por ±δ", L131 (L123): "0,0573 na célula de pesquisa frente a nenhuma pesquisa".
- **Fonte:** cinco células comparam pesquisa com nenhuma pesquisa (C01, C07, C09, C12 e C15). Em `certeza.csv`, só a C01, de apoio ao líder com randomizados, tem δ = 0,0573; C07 e C09 têm 0,044, e C12 e C15, 0,046. O protocolo (seção 8) converte 2 p.p. em g pela razão de chances, com a proporção de referência (padrão, na falta de outra). A Emenda 5 (item 7) e a nota de 24/09/2026 usam, na C01, a mediana da proporção do grupo de comparação. Nas demais células ficou a referência padrão (Emenda 5, item 8), embora o protocolo peça a mediana de cada célula binária; isso é questão de análise, fora do escopo desta verificação, e fica registrado aqui só para o autor. Sem essa informação, o leitor do PDF não sabe por que uma célula tem outro δ. A correção não traz número novo.
- **Correção na 2.7:** "O δ de 2 pontos percentuais, fixado no protocolo sem *benchmark*, virou g pela razão de chances: 0,044 no apoio e 0,046 no comparecimento, com a proporção de referência padrão do protocolo, e 0,0573 na célula principal de apoio com pesquisa frente a nenhuma pesquisa (randomizados), com a mediana da proporção do grupo de comparação dos seus estudos."
- **Correção no Q1:** "0,0573 na célula principal de apoio com pesquisa frente a nenhuma pesquisa (randomizados)". A `spec_final.md` (seção 2.2) pede essa linha literal, e a decisão de mudá-la é do coordenador.
- **Onde:** `_esqueleto_revisao_final.qmd`.

**A6. @Farjam2020a aparece como "fora do laboratório", e os Apêndices o classificam como laboratório.**

- **Trecho:** 3.4, P1, L466 (L260): "@Farjam2020a, o único fora do laboratório e da vinheta, é uma votação *online* sobre organizações políticas reais, sem eleição em curso."
- **Fonte:** Apêndice C e Tab. 1: o desenho de @Farjam2020a é "laboratório, candidatos reais", e o contexto é "real". O enunciado de C01 ("3 deles de laboratório ou vinheta") e a justificativa GRADE se referem ao realismo do contexto ("só Farjam2020a usa organizações reais").
- **Correção:** "@Farjam2020a, o único em contexto real, é uma votação *online* sobre organizações políticas reais, sem eleição em curso."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**A7. Os portões não são definidos no artigo nem nos apêndices.**

- **Trecho:** 2.9, P1, L228 (L220): "Os portões G3 a G9 foram aprovados em autopiloto." G1 a G9 aparecem também em 1.2, 2.1, na legenda da Fig. 1, nas Informações adicionais e na tabela de emendas do Apêndice B.
- **Fonte:** critério 5 (autocontido). O PDF não diz o que é um portão nem a que etapa corresponde cada um, e é nessa frase que o leitor fica sabendo que a aprovação das etapas foi automática. A ordem sai de `declaracao_uso_ia.md`: G3 busca, G4 triagem, G5 elegibilidade, G6 piloto, G7 extração e risco de viés, G8 síntese e G9 relato.
- **Correção:** "Os portões G3 a G9, pontos de aprovação previstos no protocolo ao fim de cada etapa, da busca ao relato, foram aprovados em autopiloto, sem decisão humana."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**A8. O parágrafo "Agentes desta versão" não bate com o que rodou nem com o pacote.**

- **Trecho:** Apêndice G, L485 (esqueleto dos apêndices, L84): "Esta versão a reescreve, sem mudar a análise, com um arquiteto, três redatores, uma verificação e passes de estilo, todos agentes de IA. [...] A tabela com *prompt*, papel, modelo e início do *hash* de cada agente está no pacote de replicação."
- **Fonte:**
  - `prompts_final/` tem só `prompt_redator_final.md`, `prompt_checklists_entrega.md` e este `prompt_verificacao_entrega.md`. Não há *prompt* de passe de estilo, e o agente das listas de conferência, que refez `insumos/tabelas/checklist_*.md` às 14:06 e 14:07, não é mencionado. A `spec_final.md` (seção 3.3) manda o coordenador ajustar o parágrafo ao que rodou.
  - O pacote (`ferramentas/montar_pacote.py`) leva só `declaracao_ia_v2.md`, a tabela dos agentes da versão de 24/09/2026. Não há tabela dos agentes desta versão.
  - Esse arquivo, que é público, abre com "RASCUNHO NÃO VALIDADO: 18 pendências humanas abertas" e fecha com "o autor, que ainda não revisou este texto (P038)", em contradição com o artigo. A `spec_final.md`, seção 3.4, pedia a correção dessas marcas se o texto fosse reusado no pacote.
- **Correção:** "A declaração gerada do *log* não registra os agentes que prepararam o texto, porque eles não rodaram comandos da ferramenta de revisão. A versão de 24/09/2026 foi preparada por agentes coordenados por `claude-opus-5-5`, quase todos `claude-opus-5-5`, com `claude-sonnet-5` nas referências de método e na revisão visual, e a tabela com *prompt*, papel, modelo e início do *hash* de cada um está no pacote de replicação. Esta versão a reescreve, sem mudar a análise, com um arquiteto, três redatores, um agente das listas de conferência e uma verificação, todos agentes de IA, cujos *prompts* ficam no repositório do projeto. Nenhum desses agentes leu PDF de estudo incluído nem fez análise nova." Se os passes de estilo rodarem, o coordenador os acrescenta. Ele também acrescenta ao pacote a tabela desta versão e uma nota no topo de `declaracao_ia_v2.md` ("versão de 24/09/2026; o estado atual das pendências está no Apêndice G do artigo").
- **Onde:** `_esqueleto_suplemento.qmd` e, para o pacote, `ferramentas/montar_pacote.py` (coordenador).

### Ok com ressalva

**R1. Mensagens, Resumo e *Abstract* no limite de palavras.** Pelo comando da `spec_final.md` (seção 1.9), somam 170, 250 e 250, exatamente nos limites. A trava mede 254 no Resumo e 252 no *Abstract*, porque conta a linha de palavras-chave. Qualquer correção que acrescente palavra a esses blocos (A3, R3 e R4) precisa tirar outra. Onde se corrige: `_esqueleto_revisao_final.qmd`.

**R2. "Regularidade *bandwagon*" em seções de conclusão.** Na 3.8, L528 (L318), e na 4.1, L582 e L588 (L354 e L360), "regularidade" trata como padrão estabelecido uma direção de certeza muito baixa. Na leitura às cegas, "a regularidade *underdog* repousa sobretudo em laboratório" soaria igualmente firme. As frases vêm logo qualificadas, por isso não é aviso. Onde se corrige: `_esqueleto_revisao_final.qmd`.
- Na 3.8: "O padrão na direção *bandwagon* repousa, assim, sobretudo em laboratório e vinheta."
- Na 4.1, P1: "Em parte dos experimentos, esse padrão é compatível com coordenação estratégica ou com comparecimento diferencial."
- Na 4.1, P4: "e o padrão na direção *bandwagon* repousa sobretudo em laboratório e vinheta".

**R3. O Resumo e o *Abstract* estendem C14 do jogo ao comparecimento.** Resumo, L55 (L51): "projeções longe de 50:50 podem reduzi-lo"; *Abstract*, L76 (L72): "forecasts far from 50:50 may reduce it". A célula é um jogo *online* com preferências induzidas, e o enunciado fala em "decisão de votar". A frase-padrão e a certeza estão certas. Onde se corrige: `_esqueleto_revisao_final.qmd`, compensando as palavras como em A3.
- Resumo: "Ter visto pesquisas pode aumentá-lo; num jogo *online*, projeções longe de 50:50 podem reduzi-lo".
- *Abstract*: "and, in an online game, forecasts far from 50:50 may reduce it".

**R4. As Mensagens não dizem que os 8 experimentos são quase todos de laboratório ou vinheta.** Trecho: L38 (L34), "Nas duas maiores células, os 8 experimentos apontaram a favor de quem lidera". O Resumo põe essa ressalva nas Limitações, e as Conclusões, na FC-apoio. A certeza muito baixa está na frase. Onde se corrige: `_esqueleto_revisao_final.qmd`, compensando as palavras.
- Correção: "Os 8 experimentos das duas maiores células, quase todos de laboratório ou vinheta, apontaram a favor de quem lidera, mas a evidência é muito incerta ([⊕◯◯◯]{.grade} certeza muito baixa)."

**R5. "Esta" sem substantivo, ao lado de "revisões rápidas".** Na 2.1, L158 (L150), "e esta foi conduzida por agentes" pode ser lido como "esta revisão rápida". Onde se corrige: `_esqueleto_revisao_final.qmd`.
- Correção: "e esta síntese foi conduzida por agentes".

**R6. A remissão aos modelos por etapa é circular.** A 2.9, L228 (L220), diz "cujos modelos por etapa estão nos Métodos", e a declaração de IA, L656 (L428), diz "nos Métodos (@sec-ia)". Os modelos estão nas seções 2.4 a 2.8, e a 2.9 não os lista. Onde se corrige: `_esqueleto_revisao_final.qmd`.
- Na 2.9: "cujos modelos por etapa estão nas seções de @sec-selecao a @sec-certeza e no Apêndice G".
- Na declaração: "com o modelo de cada etapa nos Métodos (@sec-selecao a @sec-certeza) e no Apêndice G".

**R7. "Tabela 1" ambígua no Apêndice B.** Na linha A5 da tabela de atalhos, "os itens sem número da Tabela 1" é a tabela de Garritty, e não a do artigo. O texto sai de `montar_suplemento.py` e de `garritty_2024.md` (código, do coordenador).
- Correção: "As 24 recomendações e os itens sem número da Tabela 1 de @Garritty2024Rapid não tratam de contato com autores."

**R8. O rótulo do atalho A2 ficou como no protocolo.** Na tabela de consequências do Apêndice B, o título é "Triagem, elegibilidade, extração, risco de viés e certeza por subagentes de IA, sem validação humana". A célula ao lado já registra a conferência em bloco da elegibilidade. O texto vem de `montar_suplemento.py` (código, do coordenador).
- Correção: "Triagem, elegibilidade, extração, risco de viés e certeza por subagentes de IA, sem validação humana (atalho como declarado no protocolo; conferência em bloco depois, Emenda 7)".

**R9. Leitura do valor de p no Apêndice F.** Na abertura, L404 (esqueleto dos apêndices, L72), "indicam só que a proporção numa direção difere de metade" é falso para p = 1, que aparece em várias linhas da tabela. Onde se corrige: `_esqueleto_suplemento.qmd`.
- Correção: "medem só o quanto a proporção numa direção se afasta de metade".

**R10. Voto obrigatório.** A 5.1, L628 (L400), diz "Nenhum dos 11 estudos de comparecimento da síntese tem voto obrigatório codificado." A 3.10 diz "codificado como sim". Dois dos 11 (@Gerber2020a e @Grillo2024c) têm a variável codificada como "não" (`numeros_v2.json`, `transf_voto_obrigatorio_informado`). Onde se corrige: `_esqueleto_revisao_final.qmd`.
- Correção: "Nenhum dos 11 estudos de comparecimento da síntese tem voto obrigatório codificado como sim."

**R11. "Brecha dessa regra".** A 5.1, L626 (L398), diz "@Araujo2021a trata de uma brecha dessa regra em 2018". A regra da frase anterior é a das 17h para levantamentos do dia. O estudo trata da divulgação oficial da apuração, que em 2018 começou às 19h, com seções ainda votando (`contexto_brasil.md`, 7.3; Emenda 1). Onde se corrige: `_esqueleto_revisao_final.qmd`.
- Correção: "@Araujo2021a trata de uma brecha, em 2018, da regra de só divulgar resultados depois do fechamento das urnas: o voto de quem ainda estava na fila quando a apuração começou a ser divulgada."

**R12. Faltas menores para um leitor só com o PDF.**
- As sementes da busca por citação (38, 12 e 3) ficam só no repositório privado, e o Apêndice A remete a "arquivos da busca por citação do projeto".
- As variáveis do *codebook* de extração não estão listadas. O PRISMA 2020, item 10b, pede a lista, que está no pacote.
- A sigla PRESS não é desdobrada.
- Onde se corrige: `_esqueleto_suplemento.qmd`, Apêndice A: "As sementes da busca por citação ficam no repositório do projeto, que é privado, com acesso sob pedido ao autor, e o pacote de replicação leva só as estratégias ativas, o registro das buscas e os *codebooks*."

**R13. Pendência da linha "Relato" do Apêndice G.** A coluna diz "nenhuma", mas a P038 segue aberta em `_pendencias_abertas.json`. O contrato manda tirar a P038 (`spec_final.md`, seção 3.3), com a condição de fechá-la com a aprovação do autor a esta versão. Se a publicação sair antes disso, a coluna deve trazer a P038. Onde se corrige: `revista/tabelas/lacunas.yml`.
- Enquanto a P038 estiver aberta: "P038".
- Depois de fechada: conferência "Em bloco pelo autor, nesta versão" e pendência "nenhuma".

**R14. Tamanho do resumo em linguagem simples.** Tem 743 palavras de prosa, sem títulos, ou 792 pela trava, que conta os títulos. A `spec_final.md` fala em "cerca de 700", e o livro, em até 750 (R2.2). Fica dentro pela contagem de prosa. Se A3 for aplicada (+4 palavras), continua dentro. Onde se corrige: `linguagem_simples.qmd`, só se o autor quiser folga.

## Leitura às cegas

Inverti a direção de cada conclusão e perguntei se o texto soaria igualmente confiante sem a certeza.

| Bloco | Afirmações | Resultado |
|---|---|---|
| Mensagens | 5 itens | Apoio ao líder e comparecimento trazem a certeza e a frase padrão; invertidos, continuam cautelosos. Ressalva R4 (laboratório e vinheta) |
| Resumo e *Abstract* | 5 frases de Resultados e as Conclusões, nas duas línguas | Cautelosos, com certeza por frase; "Não se sabe se pesquisas mudam o voto, nem em quanto". Ressalva R3 |
| Discussão 4.1 | 4 parágrafos | P1 e P2 trazem "muito incerta", "provavelmente" e "pode", com uma exceção (A4). P3 usa a FC-metas. P4 condiciona as contribuições à falta de validação humana. Ressalva R2 ("regularidade") |
| Conclusões | 2 parágrafos, 8 frases canônicas | Frases canônicas literais; a última lembra que risco de viés e certeza foram só de IA. Nenhuma soa firme quando invertida |
| Linguagem simples | Título, "A síntese em resumo" e "O que encontramos?" | Igual às Conclusões; o título tem "a evidência é muito incerta" |

## Conferências que passaram sem divergência

- **PRISMA** (2.3, 2.4, 3.1, legenda da Fig. 2, Resumo, *Abstract*, 4.4, Apêndices A, B e G e linguagem simples):
  - 1.767 e 1.706 identificados; 1.438, 118, 131 e 80 por estratégia; 1.189, 411 e 106 por rodada de citação; 1.235 da B01 fora;
  - 46 e 4 duplicados; 148 e 648 pelo filtro de ano; 1.573 e 1.054 triados; 1.314 e 787 excluídos;
  - 158 de 259 e 184 de 267 não recuperados (342 de 526); 101 e 83 avaliados; 59 e 70 excluídos (39 e 50 por C2); 42 e 13 relatos; 41 estudos e 55 relatos;
  - 184 = 165 + 16 + 3; 55 = 47 + 8; 129 = 118 + 8 + 3; 336 = 156 + 180; 180 = 15 + 165.
- **Células**:
  - as contagens de `celulas.json` batem com `swim_principal`, e certeza e enunciado batem com `certeza.csv`, nas 18;
  - proporção, IC e "x de y" da Tab. 2 e dos parágrafos batem;
  - p = 0,125, 1 e 0,5 nos textos, e 9 de 9 (p = 0,004), 10 de 11 (0,012), 8 de 8 (0,008) e 2 de 2 (0,5) nas sensibilidades, refeitos por teste binomial;
  - 15, 2 e 1 células com certeza muito baixa, baixa e moderada;
  - as notas a–h da Tab. 2 são coerentes com as justificativas;
  - o arredondamento de 0,975 → 0,98 e de 0,025 → 0,03 é comercial e consistente em toda parte.
- **Metas** (3.4, 4.1, legenda da Fig. 5):
  - g 0,48 e 0,62, com IC, p, gl (1,25 e 1,46), I² (15% e 94%), τ² (0,04 e 0,41) e IP (−3,55 a 4,51; −7,82 a 9,05);
  - ρ e ICC: de 0,47 a 0,51 e de 0,61 a 0,62;
  - *leave-one-out*: só sem @Timotei2013a (0,40 a 0,98) e sem @Lammers2022a (0,85 a 0,94) o IC deixa de cruzar zero.
- **Sensibilidades** (3.8 e Apêndice F): todas as linhas do Apêndice F batem com os sete `swim_resumo.json` de sensibilidade; o ICC de 0,20 não muda contagem; o GRADE do agrupamento amplo bate com `certeza_agrupamento_amplo.csv`.
- **Risco de viés** (Tab. 1, 3.2, Apêndice D, Apêndice B e Apêndice G), refeito de `04-qualidade/`:
  - 43 resultados de 37 estudos;
  - RoB 2 com 17 e 6, ROBINS-I V2 com 2, 8 e 3, EPOC com 6 e 1;
  - D5 em 21 de 23 e D1 grave ou crítico em 11 de 13;
  - 171 domínios concordantes e 88 arbitrados; o árbitro seguiu A em 79; nenhum domínio resolvido por humano; `validado_humano = 0` em todo o RoB e em todo `certeza.csv`.
- **Efeitos citados:** Lammers (1,25, 1,03, −0,39 e 0,06), Chatterjee (−0,29 e −0,42), Araujo (+5,69 e +11,76 p.p.), Cornejo (0,19, EP 0,105; 0,33 e 0,09 por subgrupo), Freden (−0,41), Feltovich (0,25 e 0,44), Dahlgaard (+3,40 p.p.; 0,12, EP 0,080), Meer (0,13, EP 0,072), Gerber (0,29 p.p. e 0,08; 126.126), Westwood (−0,10, EP 0,023; 5.845), Morton (−11 p.p.), Schlegel (+11 e +17 p.p.) e Fichnova (17 de 37) batem com `numeros_v2.json`, o Apêndice E e `certeza.csv`. As 70 linhas do Apêndice E batem com `efeitos_principais_valores`.
- **Extração e IA:**
  - 560 efeitos de 40 estudos, 37 com efeito principal;
  - 56 efeitos principais de então (15, 23, 12 e 6) e 28 estudos arbitrados;
  - 772 correções, 240 estendidas (`correcoes_sessao_2026-09-23.csv`: 772 linhas, 240 de extensão; o CLAUDE.md diz 771, e a fonte dá 772);
  - 58,5% em 560 comparações, 37 variáveis abaixo do limiar e κ 0,38, 0,38 e 0,15 (`notas_extracao_completa.md`);
  - 259 divergências; 0,97 (κ 0,90; PABAK 0,94); 141 e 300.
- **Síntese:** 27 estudos na principal e 14 fora (3 críticos, 7 só fora da contagem e 4 sem efeito principal); 11 estudos de comparecimento na síntese e 17 no total; 34 com mecanismo, 3 por mediação e 25 no voto estratégico; 60% e 40% de concordância nas variáveis de mecanismo.
- **Emendas** (2.1, 2.9, Informações adicionais e Apêndice B):
  - datas, tipos, momento (antes ou depois de ver os dados) e autoria de E001, E002 e das Emendas 1 a 7 conferem com `emendas.md`;
  - Emenda 2 decidida pela IA e endossada pelo autor;
  - árbitro escolhido pelo autor por custo (Emenda 3);
  - 4a a 4c por questionário do autor; 4d substituída pela 6a;
  - 16 casos limítrofes (17 linhas no *log*, uma de teste) confirmados na 6a;
  - 6b decidida pelo autor, com a conferência dispensada.
- **Pendências:** P006, P007, P008, P019, P033, P035, P036 e P042 aparecem só na abertura da declaração de IA e na tabela do Apêndice G, e nenhum outro ID aparece. A tabela do Apêndice G é igual à da `spec_final.md` em todas as células e na legenda.
- **Nome e marcas:**
  - "síntese sistemática de evidências conduzida com agentes de IA" no subtítulo, nas palavras-chave, no título dos apêndices e na citação;
  - "rascunho" só em "RASCUNHO NÃO VALIDADO";
  - nenhum "suplemento", "S1" a "S11", "relatório técnico", "18 pendências", "decisão pendente" ou "[A confirmar pelo autor]";
  - o YAML do artigo não liga `rascunho`, e o *template* não imprime marca-d'água nem o campo `pendencias-abertas`.
- **Brasil:**
  - Lei nº 9.504/1997 (registro cinco dias antes e crime de pesquisa fraudulenta);
  - embargo de 2006 e o fundamento da ADI 3.741;
  - 17h em 2022 e 19h em 2018;
  - PLs nº 2.567/2022 e nº 2.558/2022, não votados em 24/09/2026;
  - Meireles e Russo (mais de 2 mil pesquisas, de 2012 a 2020);
  - Pereira e Nunes;
  - na linguagem simples, "outubro de 2022" e "15 dias".
- **Revisões anteriores e Garritty:**
  - Barnfield: revisão conceitual; "only ten discuss mobilisation"; experimentos com a pesquisa como único estímulo; identificação partidária atenua o efeito;
  - Moy e Rinke: revisão narrativa, sem método de seleção; "can hardly conclude";
  - Coşgun: revisão sistemática, uma base, só em inglês; afirmações causais em laboratório e *survey*, concentradas nos EUA;
  - Hardmeier: "não verificada", sem verbo de conclusão;
  - a checagem de 19/09/2026 em OpenAlex, OSF e BDTD (`pergunta.md`, seção 4);
  - Garritty: "led only by experienced systematic reviewers", "no longer than six months", "carefully considered", "at a minimum..." e "the absence of peer review..." literais; recomendações 5, 6, 9, 16 e 23 classificadas como no insumo.

## Scripts usados

Todos só leem. Ficaram na pasta de rascunho da sessão (`/private/tmp/claude-501/.../scratchpad/`) e estão transcritos abaixo.

| Script | O que faz | Resultado |
|---|---|---|
| `conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd` (do projeto) | A trava da versão final | OK, 0 falhas e 1 aviso |
| `shasum -a 256` nos sete arquivos da sentinela | Sentinela da `spec_final.md`, seção 10 | Os sete iguais |
| `verif_entrega.py` | Números do PRISMA, células, Tab. 2, parágrafos de célula, teste de sinal, metas e *leave-one-out*, g fora dos blocos proibidos, risco de viés refeito de `04-qualidade/`, pendências e Apêndice G, marca de rascunho, correções, recodificação e contagens da síntese | 160 OK, 0 divergências |
| `swim_resumo.py` | Resume os grupos da SWiM principal e das 7 sensibilidades, para conferir a 3.8 e o Apêndice F | Tudo bate |
| `conferir_apendice_e.py` | g, EP, p.p., p0, p1 e β das 70 linhas do Apêndice E contra `numeros_v2.json` | 70 sem divergência |
| `conferir_citacoes.py` | `@chaves` dos três textos e o `nocite` contra `referencias.json` | Nenhuma chave ausente |
| `varrer_termos.py` | Varre os três textos, as legendas, `lacunas.yml` e `hipoteses.yml` por nome do produto, "rascunho", "suplemento", IDs de pendência, atribuições ao autor, validação, significância e recomendação | Base de E1, E2, A2, A3 e da tabela de atribuição |
| `contar_palavras.py` | Palavras de prosa por seção, pela regra da `spec_final.md`, seção 1.9 | Base de A1, R1 e R14 |
| Trechos em linha de comando | `Rscript`, `quarto --version` e `quarto typst --version` para as versões; leitura de `elegibilidade_tc_final.csv` para os 13 excluídos; tabelas de *leave-one-out*; `montar_pacote.py` e `declaracao_ia_v2.md` para A8 | Descritos nos itens |

### Transcrição de `verif_entrega.py`

```python
"""Verificação da versão de entrega (Emenda 7): números do texto contra as fontes. Só lê arquivos.

Uso: python3 verif_entrega.py   (da raiz do projeto ou de qualquer lugar)
Imprime OK / DIV / INFO por conferência e o total no fim.
"""
import csv, json, re
from math import comb
from pathlib import Path

R = Path("/Users/felipelmc/Desktop/pesquisas-eleitorais-rs")
D = R / "09-documento-final"
A = (D / "revisao_final.qmd").read_text(encoding="utf-8")
SUP = (D / "suplemento.qmd").read_text(encoding="utf-8")
LS = (D / "linguagem_simples.qmd").read_text(encoding="utf-8")
out = []
ok = lambda c, m: out.append(("OK   " if c else "DIV  ") + m)
info = lambda m: out.append("INFO " + m)
from decimal import Decimal, ROUND_HALF_UP
# arredondamento comercial (0,975 -> 0,98 e 0,025 -> 0,03), a convenção do texto
br = lambda x, casas=2: str(Decimal(repr(x)).quantize(Decimal(1).scaleb(-casas), rounding=ROUND_HALF_UP)).replace(".", ",").replace("-", "−")
milhar = lambda n: f"{n:,}".replace(",", ".")

# ------------------------------------------------------------------ 1. PRISMA (2.3, 2.4, 3.1, linguagem simples)
P = json.loads((R / "07-relatorio/prisma_contagens.json").read_text())
b, o = P["bases"], P["outros_metodos"]
esperado = [
    f"A busca identificou {milhar(b['identificados']['bases'])} registros nas bases e {milhar(o['identificados']['busca_citacoes'])} pela busca por citação",
    f"saíram {b['removidos_antes_triagem']['duplicatas']} e {o['removidos_antes_triagem']['duplicatas']} duplicados e {b['removidos_antes_triagem']['automacao']} e {o['removidos_antes_triagem']['automacao']} relatos pelo filtro de ano",
    f"Dos {milhar(b['triados'])} e {milhar(o['triados'])} registros triados, os triadores de IA excluíram {milhar(b['excluidos_triagem'])} e {o['excluidos_triagem']}",
    f"Não foram recuperados {b['nao_recuperados']} dos {b['buscados']} e {o['nao_recuperados']} dos {o['buscados']} relatos buscados ({b['nao_recuperados'] + o['nao_recuperados']} de {b['buscados'] + o['buscados']})",
    f"Dos {b['avaliados']} e {o['avaliados']} avaliados, {b['excluidos_elegibilidade']['total']} e {o['excluidos_elegibilidade']['total']} foram excluídos",
    f"fora do critério C2 ({b['excluidos_elegibilidade']['motivos']['c2_intervencao_estudada']} e {o['excluidos_elegibilidade']['motivos']['c2_intervencao_estudada']})",
    f"Foram incluídos {P['incluidos']['estudos']} estudos, em {P['incluidos']['relatos']} relatos ({b['incluidos_relatos']} das bases e {o['incluidos_relatos']} dos outros métodos)",
    f"os duplicados ({b['removidos_antes_triagem']['duplicatas']} nas bases e {o['removidos_antes_triagem']['duplicatas']} nos outros métodos) e os relatos publicados antes de 2010 ({b['removidos_antes_triagem']['automacao']} e {o['removidos_antes_triagem']['automacao']})",
    f"Os {b['avaliados'] + o['avaliados']} relatos avaliados",
]
for e in esperado:
    ok(e in A, f"PRISMA no artigo: «{e[:90]}…»")
nr, bu = b["nao_recuperados"] + o["nao_recuperados"], b["buscados"] + o["buscados"]
for nome, t in (("Resumo/Limitações", A), ("apêndices", SUP), ("linguagem simples", LS)):
    ok(f"{nr} de {bu}" in t or f"{nr} dos {bu}" in t or nome == "apêndices", f"{nr} de {bu} em {nome}")
ok(f"{b['nao_recuperados']} das bases e {o['nao_recuperados']} dos outros métodos" in SUP, "Apêndice B, A5: não recuperados por ramo")
# 184 = 165 + 16 + 3; inclusões 47 + 8 = 55; exclusões 118 + 8 + 3 = 129
ok(165 + 16 + 3 == b["avaliados"] + o["avaliados"], "2.4: 165 + 16 + 3 = relatos avaliados")
ok(47 + 8 == P["incluidos"]["relatos"], "2.4: 47 + 8 inclusões = relatos incluídos")
ok(118 + 8 + 3 == b["excluidos_elegibilidade"]["total"] + o["excluidos_elegibilidade"]["total"], "2.4: 118 + 8 + 3 = excluídos no texto completo")
ok(156 + 180 == 336 and 15 + 165 == 180, "2.4: Emenda 6b, 336 = 156 + 180 e 180 = 15 + 165")
por_fonte = b["identificados"]["por_fonte"]
ok(1438 + 118 + 131 == por_fonte["openalex"] and 80 == por_fonte["bdtd"], "2.3: B05 + B02 + B03 = OpenAlex; B04 = BDTD")
ok(1189 + 411 + 106 == o["identificados"]["busca_citacoes"], "2.3: SN1 + SN2 + SN3 = busca por citação")

# ------------------------------------------------------------------ 2. células: celulas.json × swim_resumo × Tab. 2 × texto
C = json.loads((D / "revista/celulas.json").read_text())["celulas"]
S = json.loads((R / "06-analise/swim_principal/swim_resumo.json").read_text())["grupos"]
cert = list(csv.DictReader(open(R / "06-analise/certeza.csv", encoding="utf-8")))
chave_g = lambda g: (g["familia_intervencao"], g["construto_outcome"], g["comparador_tipo"], g["celula_alvo"], g["classe_desenho"])
sw = {chave_g(g): g for g in S}
ct = {(x["familia_intervencao"], x["construto_outcome"], x["comparador_tipo"], x["celula_alvo"], x["classe_desenho"]): x for x in cert}
sof = A[A.index("| Comparação e desenho"):A.index("{#tbl-sof}")]
for c in C:
    k = chave_g(c)
    g, x = sw[k], ct[k]
    ok(g["k_estudos"] == c["k"] and g["n_beneficos"] == c["n_beneficos"] and g["n_danosos"] == c["n_danosos"]
       and g["n_mistos"] == c["n_mistos"] and g["n_nulos"] == c["n_nulos"] and sorted(g["estudos"]) == sorted(c["estudos"]),
       f"{c['id']}: contagens de celulas.json = swim_resumo")
    ok(x["certeza"] == c["certeza"] and x["enunciado"] == c["enunciado"], f"{c['id']}: certeza e enunciado = certeza.csv")
    linha = next(l for l in sof.split("\n") if f'cel="{c["id"]}"' in l)
    if c["proporcao"] is not None:
        ic = c["ic_proporcao"]
        alvo = f"(proporção {br(c['proporcao'])}; IC 95% {br(ic[0])} a {br(ic[1])})"
        ok(alvo in linha, f"{c['id']}: Tab. 2 traz {alvo}")
        ok(f"{c['n_beneficos']} de {c['n_estudos_com_direcao']}" in linha, f"{c['id']}: Tab. 2 traz {c['n_beneficos']} de {c['n_estudos_com_direcao']}")
    ok(c["certeza_texto"] in linha, f"{c['id']}: Tab. 2 traz certeza {c['certeza_texto']}")
    # parágrafo do span no texto: proporção, IC e p, quando citados
    par = next(p for p in A.split("\n\n") if f'cel="{c["id"]}"' in p and not p.startswith("|") and "+---" not in p)
    for m in re.finditer(r"proporção (?:ficou em )?([\d,]+) \(IC 95% ([\d,]+) a ([\d,]+); p = ([\d,]+)\)", par):
        pv = c["p_sinal"]
        pv_txt = "1" if pv == 1 else br(pv, 3 if pv < 0.2 else 1)
        ok(m.group(1) == br(c["proporcao"]) and m.group(2) == br(c["ic_proporcao"][0]) and m.group(3) == br(c["ic_proporcao"][1])
           and m.group(4) == pv_txt, f"{c['id']}: texto «{m.group(0)}»")
    for m in re.finditer(r"\(proporção ([\d,]+); IC 95% ([\d,]+) a ([\d,]+); p = ([\d,]+)\)", par):
        ok(m.group(1) == br(c["proporcao"]), f"{c['id']}: texto «{m.group(0)}»")
cont = {}
for c in C:
    cont[c["certeza"]] = cont.get(c["certeza"], 0) + 1
ok(cont == {"muito_baixa": 15, "baixa": 2, "moderada": 1}, f"certezas por célula {cont} = 15/2/1 do texto (2.8 e 3.3)")
ok(all(x["validado_humano"] in ("0", 0) for x in cert), "certeza.csv: validado_humano = 0 em todas as linhas")
# teste de sinal
p_sinal = lambda x, n: min(1.0, 2 * sum(comb(n, i) for i in range(min(x, n - x) + 1)) / 2 ** n)
for x, n, txt in ((4, 4, "0,125"), (9, 9, "0,004"), (10, 11, "0,012"), (8, 8, "0,008"), (2, 2, "0,5"), (6, 6, "0,031")):
    ok(br(p_sinal(x, n), 3).rstrip("0").rstrip(",") in (txt, txt.rstrip("0")), f"teste de sinal {x} de {n}: p = {p_sinal(x, n):.4f} ({txt})")

# ------------------------------------------------------------------ 3. metas
MA = json.loads((R / "06-analise/meta_exploratoria/meta_resumo.json").read_text())["grupos"][0]["resultado"]
MB = json.loads((R / "06-analise/meta_mesmo_candidato/meta_resumo.json").read_text())["grupos"][0]["resultado"]
for nome, m, d in (("A", MA, "0,0573"), ("B", MB, "0,044")):
    trecho = f"g = {br(m['estimativa'])} (IC 95% {br(m['ic'][0])} a {br(m['ic'][1])}; p = {br(m['p'], 3)}), com {br(m['gl'])} grau de liberdade e IC que cruza zero e ±δ ({d})"
    ok(trecho in A, f"meta {nome}: «{trecho}»")
    ok(f"I² ({round(m['I2'])}%)" in A, f"meta {nome}: I² {round(m['I2'])}%")
    ok(f"{br(m['pi'][0])} a {br(m['pi'][1])}" in A, f"meta {nome}: IP na legenda da Fig. 5")
ok(f"τ² ({br(MA['tau2'])} e {br(MB['tau2'])})" in A, "metas: τ² na legenda")
loo = lambda p: list(csv.DictReader(open(next((R / p).glob("loo_01_*.csv")))))
la = {r["estudo_removido"]: r for r in loo("06-analise/meta_exploratoria/tabelas")}
lb = {r["estudo_removido"]: r for r in loo("06-analise/meta_mesmo_candidato/tabelas")}
ok(la["ES1876"]["ic_exclui_zero"] == "TRUE" and f"sem @Timotei2013a ({br(float(la['ES1876']['ic_inf']))} a {br(float(la['ES1876']['ic_sup']))})" in A,
   "meta A: leave-one-out sem Timotei2013a (ES1876)")
ok(lb["ES1621"]["ic_exclui_zero"] == "TRUE" and f"sem @Lammers2022a ({br(float(lb['ES1621']['ic_inf']))} a {br(float(lb['ES1621']['ic_sup']))})" in A,
   "meta B: leave-one-out sem Lammers2022a (ES1621)")
ok(sum(r["ic_exclui_zero"] == "TRUE" for r in la.values()) == 1 and sum(r["ic_exclui_zero"] == "TRUE" for r in lb.values()) == 1,
   "metas: só um leave-one-out deixa de cruzar zero em cada")
rho_a = [s["estimativa"] for s in json.loads((R / "06-analise/meta_exploratoria/meta_resumo.json").read_text())["grupos"][0]["sensibilidade"]["rho"]]
icc_a = json.loads((R / "06-analise/meta_exploratoria_icc020/meta_resumo.json").read_text())["grupos"][0]["resultado"]["estimativa"]
ok(br(min(rho_a + [icc_a])) == "0,47" and br(max(rho_a + [icc_a])) == "0,51", "meta A: ρ de 0,2 a 0,8 e ICC 0,20 dão g de 0,47 a 0,51")
rho_b = [s["estimativa"] for s in json.loads((R / "06-analise/meta_mesmo_candidato/meta_resumo.json").read_text())["grupos"][0]["sensibilidade"]["rho"]]
ok(br(min(rho_b)) == "0,61" and br(max(rho_b)) == "0,62", "meta B: ρ dá g de 0,61 a 0,62")
for trecho in ("0,48", "0,62"):
    for nome, bloco in (("Mensagens", A[A.index("# Mensagens"):A.index("# Resumo")]),
                        ("Resumo e Abstract", A[A.index("# Resumo"):A.index("# Introdução")]),
                        ("Conclusões", A[A.index("# Conclusões"):A.index("# Informações adicionais")])):
        ok(trecho not in bloco, f"g da meta ({trecho}) ausente de {nome}")

# ------------------------------------------------------------------ 4. risco de viés (04-qualidade)
G = list(csv.DictReader(open(R / "04-qualidade/rob_geral.csv", encoding="utf-8")))
from collections import Counter
cg = Counter((x["ferramenta"], x["rob_geral"]) for x in G)
info(f"rob_geral: {dict(cg)}")
ok(len(G) == 43 and len({x["chave"] for x in G}) == 37, f"RoB: {len(G)} resultados de {len({x['chave'] for x in G})} estudos")
ok(cg[("rob2", "algumas_preocupacoes")] == 17 and cg[("rob2", "alto")] == 6, "RoB 2: 17 algumas preocupações e 6 alto")
ok(cg[("robins_i", "moderado")] == 2 and cg[("robins_i", "grave")] == 8 and cg[("robins_i", "critico")] == 3, "ROBINS-I: 2, 8 e 3")
ok(cg[("epoc", "alto")] == 6 and cg[("epoc", "baixo")] == 1, "EPOC: 6 alto e 1 baixo")
ok(all(x["validado_humano"] == "0" for x in G), "rob_geral: validado_humano = 0 em todas as linhas")
dom = []
for f in ("rob2", "robins_i", "epoc"):
    dom += list(csv.DictReader(open(R / f"04-qualidade/rob_{f}_consenso.csv", encoding="utf-8")))
aplic = [d for d in dom if d["julgamento_consenso"] not in ("", "nao_se_aplica", "na")]
arb = [d for d in aplic if d["resolvido_por"].startswith("arbitro")]
info(f"domínios com consenso: {len(aplic)}; arbitrados: {len(arb)}; resolvido_por: {Counter(d['resolvido_por'].split(':')[0] for d in aplic)}")
ok(len(arb) == 88, f"88 domínios arbitrados (achados {len(arb)})")
segue_a = sum(d["julgamento_consenso"] == d["julgamento_a"] for d in arb)
ok(segue_a == 79, f"árbitro seguiu A em 79 (achados {segue_a})")
ok(not any(d["resolvido_por"].startswith("revisor_humano") for d in dom), "nenhum domínio resolvido por humano")
d5 = sum(d["dominio"] == "D5" and d["julgamento_consenso"] == "algumas_preocupacoes" for d in dom if d["ferramenta"] == "rob2")
d1 = sum(d["dominio"] == "D1" and d["julgamento_consenso"] in ("grave", "critico") for d in dom if d["ferramenta"] == "robins_i")
ok(d5 == 21 and d1 == 11, f"RoB 2 D5 algumas preocupações = {d5} (21); ROBINS-I D1 grave ou crítico = {d1} (11)")

# ------------------------------------------------------------------ 5. pendências e Apêndice G
PA = json.loads((R / "07-relatorio/_pendencias_abertas.json").read_text())
ids = sorted(p["id"] for p in PA["pendencias"] if p.get("status") == "aberta")
ok(ids == ["P006", "P007", "P008", "P019", "P033", "P035", "P036", "P038", "P042"], f"pendências abertas: {ids}")
lac = SUP[SUP.index("# Apêndice G"):]
ok(sorted(set(re.findall(r"P0\d\d", lac))) == [i for i in ids if i != "P038"], "Apêndice G cita as abertas menos a P038")
ok(sorted(set(re.findall(r"P0\d\d", A))) == [i for i in ids if i != "P038"], "artigo cita as abertas menos a P038 (só em IA-7)")
ok(A.count("RASCUNHO NÃO VALIDADO") == 1 and "RASCUNHO" not in SUP and "ascunho" not in LS
   and not re.search(r"rascunho", A.replace("RASCUNHO NÃO VALIDADO", ""), re.I), "RASCUNHO NÃO VALIDADO uma vez; 'rascunho' em nenhum outro lugar")

# ------------------------------------------------------------------ 6. outros números citados
N2 = json.loads((D / "revista/numeros_v2.json").read_text())
ok(N2["transf_comparecimento_sintese"]["valor"] == 11 and N2["transf_voto_obrigatorio_sim_comparecimento"]["valor"] == 0,
   "11 estudos de comparecimento na síntese, nenhum com voto obrigatório = sim")
ok(N2["transf_comparecimento_estudos"]["valor"] == 17 and "aqui 17 estudos medem o comparecimento" in A, "17 estudos medem comparecimento (4.2)")
ok(N2["transf_confianca"]["valor"] == 1, "confiança nas pesquisas: 1 estudo (5.1)")
cor = list(csv.DictReader(open(R / "05-decomposicao/correcoes_sessao_2026-09-23.csv", encoding="utf-8")))
ext = sum(x["origem"].startswith("coordenador de IA, extensão") for x in cor)
ok(len(cor) == 772 and ext == 240, f"correções dos efeitos: {len(cor)} linhas, {ext} extensões (772 e 240 no texto)")
ok(A.count("772") == 2 and "772 correções" in SUP, "772 aparece em 2.5 e 4.4 e nos Apêndices B e G")
arb_h = list(csv.DictReader(open(R / "08-revisao-humana/P037_concordancia/arbitragem_humana.csv", encoding="utf-8")))
ok(len(arb_h) == 259, f"recodificação: {len(arb_h)} divergências (259)")
mec = sum(x["variavel"].startswith("mecanismo_") for x in arb_h)
info(f"divergências da recodificação em variáveis de mecanismo: {mec}, em {len({x['chave'] for x in arb_h})} estudos")
N1 = json.loads((D / "insumos/tabelas/numeros.json").read_text())
ok(N1["estudos_com_efeitos"] == 40 and N1["efeitos"] == 560 and N1["estudos_com_principal"] == 37,
   "40 estudos com efeitos, 560 efeitos, 37 com efeito principal (3.3)")
ok(N1["n_swim_principal_estudos"] == 27 and N2["estudos_fora_da_sintese_principal"]["valor"] == 14, "27 na síntese principal e 14 fora (3.1)")

print("\n".join(out))
print(f"\n{sum(l.startswith('DIV') for l in out)} divergências, {sum(l.startswith('OK') for l in out)} OK, "
      f"{sum(l.startswith('INFO') for l in out)} INFO")
```

### Transcrição de `swim_resumo.py`

```python
import json, sys, glob
for f in sorted(glob.glob('06-analise/swim_*/swim_resumo.json')):
    d=json.load(open(f))
    print("=====", f, "excl_critico:", d.get('n_excluidos_rob_critico'))
    for g in d['grupos']:
        ic = g.get('ic_proporcao')
        ic = None if ic is None else [round(x,3) for x in ic]
        sens = g.get('sensibilidade',{}).get('com_rob_critico',{})
        s = ''
        if sens.get('executado'):
            s = f" | +crit: {sens['n_beneficos']}/{sens['n_estudos']} p={sens['p_sinal']}"
        print(f"{g['grupo']:<95} k={g['k_estudos']} n={g['n_estudos']} +{g['n_beneficos']} -{g['n_danosos']} mix{g['n_mistos']} nul{g['n_nulos']} prop={g['proporcao_benefica']} ic={ic} p={g['p_sinal']} {g['estudos']} crit={g.get('excluidos_rob_critico',{}).get('estudos')}{s}")
```

### Transcrição de `conferir_apendice_e.py`

```python
"""Confere g, EP, p.p., p0 e p1 da tabela de efeitos principais (Apêndice E) contra numeros_v2.json. Só lê."""
import json, re
from pathlib import Path

R = Path("/Users/felipelmc/Desktop/pesquisas-eleitorais-rs/09-documento-final")
v = json.loads((R / "revista/numeros_v2.json").read_text(encoding="utf-8"))["efeitos_principais_valores"]["valores"]
t = (R / "suplemento.qmd").read_text(encoding="utf-8")
ini = t.index("## Efeitos principais por estudo")
fim = t.index("{#tbl-s6-efeitos")
num = lambda s: float(s.replace("−", "-").replace(".", "").replace(",", ".")) if s else None
n_ok = n_div = 0
for l in t[ini:fim].split("\n"):
    if not l.startswith("| @"):
        continue
    c = [x.strip() for x in l.strip("|").split("|")]
    chave, ef = c[0].lstrip("@"), c[1]
    ide = f"{chave}-{ef}"
    src = v.get(ide)
    if src is None:
        print("SEM FONTE", ide); n_div += 1; continue
    m = re.match(r"([−\d,]+) \(([\d,]+)\)", c[5])
    difs = []
    if m:
        g, ep = num(m.group(1)), num(m.group(2))
        casas = len(m.group(1).split(",")[1])
        if round(src.get("yi", 1e9), casas) != g:
            difs.append(f"g {m.group(1)} x {src.get('yi')}")
        if round(src.get("sei", 1e9), 3) != ep:
            difs.append(f"EP {m.group(2)} x {src.get('sei')}")
    elif c[5] != "NR":
        difs.append(f"g ilegível {c[5]}")
    elif "yi" in src:
        difs.append(f"g NR mas fonte tem yi={src['yi']}")
    for rot, campo, casas in (("p.p.", "efeito_pp", 2), ("p0 = ", "p0", 2), ("p1 = ", "p1", 2), ("β = ", "beta", 3)):
        mm = re.search((r"([−\d,]+) p\.p\." if rot == "p.p." else re.escape(rot) + r"([−\d,]+)"), c[6])
        if mm:
            val = num(mm.group(1))
            fonte = src.get(campo)
            if fonte is None or round(fonte, casas) != val:
                difs.append(f"{campo} {mm.group(1)} x {fonte}")
    if difs:
        n_div += 1; print("DIVERGE", ide, "; ".join(difs))
    else:
        n_ok += 1
print(f"linhas conferidas sem divergência: {n_ok}; com divergência: {n_div}")
```

### Transcrição de `conferir_citacoes.py`

```python
"""Confere as @chaves dos três objetos contra revista/referencias.json e o nocite do artigo. Só lê."""
import json, re
from pathlib import Path

R = Path("/Users/felipelmc/Desktop/pesquisas-eleitorais-rs/09-documento-final")
refs = json.loads((R / "revista/referencias.json").read_text(encoding="utf-8"))
ids = {r["id"] for r in refs} if isinstance(refs, list) else set(refs)
RX = re.compile(r"(?<![\w.])@([A-Za-z][\w:-]*[A-Za-z0-9])")
NAO_CHAVE = re.compile(r"^(fig|tbl|sec|qdr|eq)-")

def chaves(arq, sem_yaml=True):
    t = (R / arq).read_text(encoding="utf-8")
    yaml = re.match(r"(?s)^---.*?\n---\n", t)
    nocite = set()
    if yaml:
        m = re.search(r"nocite: \|\n\s+(.*)", yaml.group(0))
        if m:
            nocite = set(RX.findall(m.group(1)))
        if sem_yaml:
            t = t[yaml.end():]
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"`[^`]*`", "", t)
    t = re.sub(r"https?://\S+", "", t)
    ks = {k for k in RX.findall(t) if not NAO_CHAVE.match(k)}
    return ks, nocite

art, nocite = chaves("revisao_final.qmd")
sup, nocite_sup = chaves("suplemento.qmd")
ls, _ = chaves("linguagem_simples.qmd")
print("referências no JSON:", len(ids))
for nome, ks in (("artigo", art), ("apêndices", sup), ("linguagem simples", ls)):
    faltam = sorted(k for k in ks if k not in ids)
    print(f"{nome}: {len(ks)} chaves citadas; ausentes do referencias.json: {faltam}")
print("nocite do artigo:", len(nocite), "; ausentes do JSON:", sorted(k for k in nocite if k not in ids))
fora = sorted(k for k in sup if k not in art and k not in nocite)
print("chaves dos apêndices que não entram na lista do artigo (nem citadas nem nocite):", fora)
print("no JSON e nunca citadas nem no nocite:", sorted(k for k in ids if k not in art | sup | nocite))
```

### Transcrição de `varrer_termos.py`

```python
"""Varre os três objetos (e as legendas/tabelas de origem) por termos sensíveis da Emenda 7. Só lê."""
import re, sys
from pathlib import Path

R = Path("/Users/felipelmc/Desktop/pesquisas-eleitorais-rs/09-documento-final")
ARQS = ["revisao_final.qmd", "suplemento.qmd", "linguagem_simples.qmd",
        "revista/figuras/legendas.yml", "revista/tabelas/lacunas.yml", "revista/tabelas/hipoteses.yml"]
PADROES = {
    "rascunho": r"rascunho",
    "RASCUNHO NÃO VALIDADO": r"RASCUNHO NÃO VALIDADO",
    "revisão (produto)": r"\b(?:esta|nesta|desta|a|da|na|dessa|nessa|essa)\s+revisão\b",
    "revisão sistemática": r"revisão sistemática|revisões sistemáticas|systematic review",
    "suplemento": r"suplement",
    "P0xx": r"\bP0\d\d\b",
    "pendente/pendência": r"pendent|pendênci",
    "autor (atribuição)": r"(?:o autor|pelo autor|do autor|ao autor|autor declar|autor confer|autor conc|autor mant|autor resolv|autor decid|autor aprov|autor leu|autor endoss|autor escolh|autor dispens|por ele|decididos por ele|endossad)",
    "valida": r"validad|validação|validou|validar",
    "conferid": r"conferi|conferência",
    "significância": r"significa|signific",
    "deve/recomend": r"\bdeve\b|\bdevem\b|recomendamos|recomenda-se",
}

def linhas(arq):
    t = (R / arq).read_text(encoding="utf-8")
    t = re.sub(r"(?s)^---.*?\n---\n", lambda m: "\n" * m.group(0).count("\n"), t, count=1)  # sem YAML
    t = re.sub(r"(?s)<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), t)
    return t.split("\n")

alvo = sys.argv[1:] or list(PADROES)
for nome in alvo:
    rx = re.compile(PADROES[nome], re.I if nome not in ("RASCUNHO NÃO VALIDADO",) else 0)
    print(f"\n######## {nome}")
    for arq in ARQS:
        for i, l in enumerate(linhas(arq), 1):
            for m in rx.finditer(l):
                s = max(0, m.start() - 110); e = min(len(l), m.end() + 110)
                print(f"  {arq}:{i}: …{l[s:e]}…")
```

### Transcrição de `contar_palavras.py`

```python
"""Conta palavras de prosa por seção (regra da spec_final, seção 1.9) nos três objetos. Só lê."""
import re
from pathlib import Path

R = Path("/Users/felipelmc/Desktop/pesquisas-eleitorais-rs/09-documento-final")


def contar(arq, sem_palavras_chave=False):
    t = (R / arq).read_text(encoding="utf-8")
    t = re.sub(r"(?s)^---.*?\n---\n", "", t, count=1)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    cab, n, ordem = None, {}, []
    for l in t.split("\n"):
        m = re.match(r"^#+\s+(.*)", l)
        if m:
            cab = m.group(1); ordem.append(cab); n[cab] = 0; continue
        if sem_palavras_chave and l.startswith(("**Palavras-chave", "**Keywords")):
            continue
        if re.match(r"^\s*(\||:::|@@|: |!\[|\+-|\+=|```)", l):
            continue
        if cab is None:
            cab = "(antes do primeiro título)"; ordem.append(cab); n[cab] = 0
        n[cab] += len(re.findall(r"\S+", re.sub(r"\{[#.][^}]*\}", "", l)))
    return ordem, n


for arq, kw in (("revisao_final.qmd", True), ("linguagem_simples.qmd", False)):
    ordem, n = contar(arq, kw)
    print("==", arq, "(sem palavras-chave)" if kw else "")
    for k in ordem:
        print(f"  {n[k]:5d}  {k}")
    print(f"  {sum(n.values()):5d}  TOTAL")

# linguagem simples sem a linha do link final
t = (R / "linguagem_simples.qmd").read_text(encoding="utf-8")
t = re.sub(r"(?s)^---.*?\n---\n", "", t, count=1)
corpo = [l for l in t.split("\n") if not re.match(r"^\s*(#|:::|\[Leia)", l)]
print("linguagem simples, prosa sem títulos, sem ::: e sem o link final:", len(re.findall(r"\S+", "\n".join(corpo))))
```
