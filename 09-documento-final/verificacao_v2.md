# Verificação independente do artigo v2 (etapa 5)

Feita em 24/09/2026 por um subagente Opus (`claude-opus-5-5`) que não escreveu nenhum dos textos, seguindo `prompts_v2/prompt_verificacao_v2.md`. Nenhum texto do artigo, do suplemento ou do resumo em linguagem simples foi alterado. Não abri PDFs de estudos nem rodei `rs.py`. Esta verificação é de IA e não valida nada: as 18 pendências humanas continuam abertas.

Objetos conferidos:

- `09-documento-final/revisao_final.qmd`, remontado do esqueleto para uma pasta temporária e comparado byte a byte com o arquivo atual (idênticos), com as figuras (`revista/figuras/legendas.yml`, `revista/figuras/dados/`) e as tabelas (`revista/tabelas/*.yml`);
- `09-documento-final/suplemento.qmd`;
- `09-documento-final/linguagem_simples.qmd`.

## Resultado

**4 erros, 17 avisos e 14 casos ok com ressalva.** A auditoria A1 a A36 está em `auditoria_final.md`: 13 cumpridos, 18 parciais e 5 não cumpridos.

Os erros são quatro:

- o artigo diz que S11 traz as listas de conferência, e S11 está vazio;
- o painel da caixa em S9 tem contagens de estudos e uma certeza que não batem com as células;
- a Discussão fala do "maior experimento de campo", mas só há um;
- o texto conta 17 casos limítrofes decididos pelo autor, e o *log* registra 16.

Nenhum número de célula, meta-análise, risco de viés, PRISMA ou sensibilidade do corpo do artigo diverge da fonte.

## O que foi checado e quanto

| Conferência | O que foi feito | Quanto | Resultado |
|---|---|---|---|
| 1. Números | Cada número do texto, das tabelas, das legendas, do resumo, do *abstract*, das mensagens e do resumo em linguagem simples, confrontado com a fonte da mesma afirmação. As fórmulas de `celulas.json` e `numeros_v2.json` foram refeitas: Clopper-Pearson e teste de sinal recalculados por programa, δ reconvertido de 2 p.p., percentuais da Tab. 1 e contagens de transferibilidade refeitas do *master* | cerca de 400 números conferidos um a um, além dos 1.770 que a trava `conferir_reestruturacao.py` confere por lista branca | 4 erros, 3 deles de contagem (E2, E3, E4); ressalva de arredondamento (R1) |
| 2. Certeza | Todo enunciado de efeito: certeza da célula certa e frase padrão (muito baixa, "a evidência é muito incerta"; baixa, "pode"; moderada, "provavelmente"); busca de "significativ", "Neutro", "sem efeito" e "não tem efeito" | 18 enunciados de célula, cerca de 40 frases de efeito fora dos enunciados, 7 figuras e 5 tabelas | 18 de 18 enunciados certos; avisos V3, V5 e V6; nenhum termo proibido (o "não tem efeito principal" da legenda de S4 é falso positivo) |
| 3. Leitura às cegas | Mensagens, Resumo, Discussão 4.1 e Conclusões reescritas com a direção invertida | 13 conclusões | 4 com enquadramento otimista ou confiança acima da certeza (V3 a V6) |
| 4. Marcações humanas | Caixas "Pendente de revisão humana" comparadas com `_revisao_final_v1_oqf.qmd`, apêndice comparado com `_pendencias_abertas.json`, marcadores do autor e papéis humanos comparados com `emendas.md` e `correcao_atribuicao.csv` | 11 caixas, 18 pendências, 4 marcadores, 9 atribuições humanas | 11 caixas com os mesmos conjuntos de IDs; 18 de 18 pendências; E4, V16, R5 |
| 5. Citações e revisões anteriores | Toda `@chave` em `revista/referencias.json`. Afirmações sobre Barnfield, Moy e Rinke, Hardmeier e Coşgun conferidas em `insumos/revisoes_anteriores.md`, sobre o Brasil em `insumos/contexto_brasil.md` e sobre revisões rápidas em `insumos/garritty_2024.md` | 88 chaves no artigo, 56 no suplemento; 11 afirmações sobre revisões anteriores; 14 sobre o Brasil; 9 citações literais de Garritty | Todas as chaves existem. Hardmeier aparece sempre como não verificada. Nenhum item "não confirmado" do contexto foi usado. As citações de Garritty são literais. Avisos V12 e V14; ressalva R4 |
| 6. Recomendações | Verbos das implicações comparados com a tabela R6.8 do livro | 9 frases de implicação (artigo e linguagem simples) | Nenhuma recomenda proibir ou liberar a divulgação. Com certeza muito baixa, o texto usa "a evidência não permite concluir" e remete a decisão a quem tem mandato |
| 7. Auditoria | Itens A1 a A36 de `insumos/livro_regras.md`, seção 8 | 36 itens | `auditoria_final.md` |

## Divergências

Cada divergência traz o trecho, o número ou a formulação do texto, o que diz a fonte, a correção em texto exato e o arquivo onde se corrige. As linhas citadas são de `revisao_final.qmd`, e o mesmo texto está no esqueleto.

### Erros

**E1. S11 anunciado e vazio.**

- **Trecho no texto:** §2.1 (L184), "com o PRISMA-trAIce só como lista de conferência ([S11](suplemento.html#s11-checklists) dá o local de cada item)". Informações adicionais (L696): "(S1 a S11: estratégias, atalhos, emendas, características, risco de viés, efeitos, efeitos fora da contagem, sensibilidades, caixa, estudos regionais e listas de conferência)".
- **Fonte:** `suplemento.qmd`, S11, diz "Em preparação. As listas de conferência [...] serão preenchidas depois da versão final do texto". Hoje, nenhuma lista do PRISMA 2020, do PRISMA-S, do SWiM ou do PRISMA-trAIce traz o local de cada item no artigo.
- **Correção preferida:** preencher S11 antes de publicar, com o local de cada item no artigo, e não no relatório técnico. `07-relatorio/checklist_prisma.csv` e `checklist_swim.csv` servem de ponto de partida.
- **Texto exato, enquanto S11 não existir:**
  - no §2.1: "com o PRISMA-trAIce só como lista de conferência (as listas preenchidas, com o local de cada item no artigo, entram em [S11](suplemento.html#s11-checklists) com a versão final)";
  - nas Informações adicionais: "(S1 a S10: estratégias, atalhos, emendas, características, risco de viés, efeitos, efeitos fora da contagem, sensibilidades, caixa e estudos regionais; S11, listas de conferência, em preparação)".
- **Onde:** `_esqueleto_revisao_final.qmd`. O preenchimento de S11 vai em `_esqueleto_suplemento.qmd` e `montar_suplemento.py`.

**E2. Painel da caixa em S9: estudos e certeza.**

- **Trecho no texto:** `suplemento.qmd`, S9, tabela `tbl-s9-painel`:
  - "| Pesquisa pré-eleitoral | Apoio | Inconclusivo | insuficiente | muito baixa | 2 |";
  - "| Boca de urna | Comparecimento | Inconclusivo | insuficiente | muito baixa | 1 |";
  - "| Pesquisa pré-eleitoral | Comparecimento | Inconclusivo | fraca | baixa | 5 |".
- **Fonte:** `revista/celulas.json` e `06-analise/certeza.csv`:
  - pesquisa pré-eleitoral × apoio tem 9 células e 16 estudos, como diz a própria Tab. 4 do artigo;
  - boca de urna × comparecimento tem 2 células e 3 estudos (@Morton2015a, @Chatterjee2019a e @Grillo2024c);
  - pesquisa pré-eleitoral × comparecimento tem 4 células e 7 estudos, e a maior certeza entre elas é **moderada** (C13, @Gerber2020a), não baixa. A regra do painel é "corpos com o mesmo rótulo; vale a maior certeza".
- **Causa:** `06-analise/caixa_ferramentas.csv`, saída do `rs caixa`, guarda uma linha de certeza por formato × desfecho × desenho. Por isso leu só 8 das 18 linhas de `certeza.csv`, as linhas 2, 3, 5, 6, 10, 15, 18 e 19. Ficaram de fora:
  - a célula de @Gerber2020a (linha 16) e a de @Klor2017a (17);
  - a de boca de urna com proibição no comparecimento (4);
  - a de @Stolwijk2016a (9);
  - seis das sete células randomizadas de pesquisa × apoio (7, 8 e 11 a 14).
- **Efeito no rótulo:** recalculado à mão, célula a célula, o rótulo continua Inconclusivo em todas.
- **Correção:** gerar o painel a partir de `revista/celulas.json`, com os estudos da união das células e a certeza pela maior entre elas, ou rodar a caixa por célula (P042). Linhas corrigidas:
  - "| Pesquisa pré-eleitoral | Apoio | Inconclusivo | insuficiente | muito baixa | 16 |";
  - "| Boca de urna | Comparecimento | Inconclusivo | insuficiente | muito baixa | 3 |";
  - "| Pesquisa pré-eleitoral | Comparecimento | Inconclusivo | [força que a regra caixa-3 dá à certeza moderada] | moderada | 7 |".
- **Na legenda, acrescentar:** "O *script* da caixa leu uma célula por formato × desfecho × desenho; estudos e certeza desta tabela foram refeitos com todas as células."
- **Onde:** `montar_suplemento.py`, bloco do painel de S9. Não está entre os quatro arquivos de texto.

**E3. "O maior experimento de campo".**

- **Trecho no texto:** Discussão 4.1 (L577), "O maior experimento de campo permite descartar, com certeza moderada, efeitos de pesquisa apertada, frente a folgada, maiores que 2 pontos percentuais."
- **Fonte:** há 1 experimento de campo (Tab. 1; `insumos/tabelas/numeros.json`, `desenho.experimento_campo = 1`). O Resumo executivo diz "único experimento de campo". "Permite descartar" é mais forte que a frase padrão da certeza moderada.
- **Correção:** "O único experimento de campo indica que pesquisa apertada, frente a folgada, provavelmente não muda o comparecimento além de 2 pontos percentuais para mais ou para menos (certeza moderada)."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**E4. 17 casos limítrofes decididos pelo autor.**

- **Trecho no texto:**
  - §2.2 (L226): "O autor decidiu 17 casos limítrofes";
  - §2.7 (L278): "decidiu as Emendas 1, 4 (itens 4a a 4c) e 6b e 17 casos limítrofes de elegibilidade";
  - S2: "Os incertos residuais foram ao humano: 17 casos."
- **Fonte:** `00-protocolo/correcao_atribuicao.csv` tem 17 linhas mantidas como humanas na etapa 07, e uma delas é linha de teste (seq 557, substituída pela 558 com a mesma decisão). São 16 registros distintos:
  - 8 inclusões: Unkelbach2022a, Stolwijk2019b, Fairstein2018a, Fairstein2019a, Yang2023d, Schlegel2023, Araujo2021 e Araujo2021a;
  - 8 exclusões: Kim2018b, Kim2025a, Reveco2026, Scheuerman2019, Scheuerman2020, Scheuerman2021, Yosef2017 e Mavridis2016a.
- **Origem do 17:** a Emenda 6a e o `relatorio.qmd` escrevem "17 decisões" contando a linha de teste.
- **Correção:**
  - §2.2: "O autor decidiu 16 casos limítrofes (17 registros no *log*, um deles de teste)";
  - §2.7: "decidiu as Emendas 1, 4 (itens 4a a 4c) e 6b e 16 casos limítrofes de elegibilidade";
  - S2: "Os incertos residuais foram ao humano: 16 casos."
- **Onde:** `_esqueleto_revisao_final.qmd` e `insumos/garritty_2024.md`, que é a fonte de S2. Para alinhar o resto, `00-protocolo/emendas.md` (6a) e `07-relatorio/relatorio.qmd`.

### Avisos

**V1. A caixa não leu a tabela de achados inteira.**

- **Trecho no texto:** §2.6 (L268), "A caixa de ferramentas aplica por *script* a regra caixa-3 [...] à mesma tabela de achados". §4.1 (L619): "Ela foi gerada pela regra caixa-3 (@sec-certeza) a partir da mesma tabela de achados que alimenta a @tbl-sof."
- **Fonte:** E2. O *script* usou 8 das 18 células, e o rótulo por célula não se reproduz a partir do arquivo (A4).
- **Correção:**
  - no fim do parágrafo da §2.6, acrescentar: "O *script* guarda uma linha de certeza por formato × desfecho × desenho e, por isso, leu só 8 das 18 células. Refeito célula a célula, o rótulo continua Inconclusivo em todas, mas o painel de pesquisa pré-eleitoral × comparecimento passa a certeza moderada. A correção do *script* é parte da P042.";
  - na §4.1: "Ela foi gerada pela regra caixa-3 (@sec-certeza), aplicada a uma célula por formato × desfecho × desenho da mesma tabela de achados que alimenta a @tbl-sof; o recálculo célula a célula não muda nenhum rótulo."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V2. Emenda 4 fora da lista das decididas depois de ver os dados.**

- **Trecho no texto:** §2.1 (L188), "As contingências E001 e E002 foram acionadas antes da triagem, as Emendas 3 e 4 fixaram convenções antes de qualquer análise de efeito, e as Emendas 1, 2, 5 e 6b vieram depois de ver dados."
- **Fonte:** `00-protocolo/emendas.md` dá à Emenda 4 o tipo C, emenda depois de ver dados, decidida "depois da extração, antes de qualquer análise de efeito". S3 diz "depois de ver os dados". A frase do artigo tira a Emenda 4 da lista (R7.4).
- **Correção:** "As contingências E001 e E002 foram acionadas antes da triagem, e a Emenda 3 corrigiu uma omissão antes de qualquer avaliação de risco de viés. As Emendas 1, 2, 4, 5 e 6b vieram depois de ver dados; a 4, depois da extração e antes de qualquer análise de efeito."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V3. Discussão 4.1: células não randomizadas sem certeza.**

- **Trecho no texto:** L575, "Nas três células não randomizadas, o quadro é mais dividido: duas vão na direção *bandwagon*, e a de boca de urna tem um estudo em cada direção. As classes não se contradizem, mas a não randomizada é mais fraca e mais dividida."
- **Fonte:** C04, C05 e C06 têm certeza muito baixa (`certeza.csv`), e a frase não diz isso (A3). "As classes não se contradizem" é comparação não testada e, invertida, soaria igualmente confiante.
- **Correção:** "Nas três células não randomizadas, com 1 ou 2 estudos cada e certeza muito baixa em todas, o quadro é mais dividido: duas vão na direção *bandwagon*, e a de boca de urna tem um estudo em cada direção. A comparação entre as classes é descritiva e não foi testada."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V4. Discussão 4.1: contribuições "se confirmam".**

- **Trecho no texto:** L579, "As três contribuições anunciadas na introdução se confirmam em termos modestos: [...] (ii) a separação por células mostra que a regularidade *bandwagon* vem de um tipo de desenho".
- **Fonte:** o padrão vem da sensibilidade só com contexto real, feita no agrupamento amplo decidido depois de ver os dados, sem GRADE próprio (S8). Tudo espera validação humana. Invertida, a frase soaria igualmente confiante: há enquadramento otimista (A23).
- **Correção:** "As três contribuições anunciadas na introdução ficam de pé em termos modestos, e todas dependem da validação humana: (i) [...]; (ii) a separação por células sugere, numa comparação descritiva e *post hoc*, que a regularidade *bandwagon* depende de laboratório e vinheta, e mostra que voto estratégico e *momentum* têm poucos estudos; e (iii) [...]"
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V5. Nulo de certeza moderada dito sem a frase padrão e sem o contexto.**

- **Trecho no texto:**
  - Resumo executivo (L72): "É evidência de que o efeito, se houver, é menor que isso, e não ausência de evidência.";
  - §3.7 (L465): "é evidência de que o efeito, se houver, é menor que 2 pontos percentuais, e não ausência de evidência."
- **Fonte:** C13 tem certeza moderada, e a frase padrão pede "provavelmente" (R5.36). O estudo é de eleições para governador nos Estados Unidos, e "o efeito", dito sem contexto, generaliza para além dele.
- **Correção:**
  - L72: "Com certeza moderada, o efeito, se houver, provavelmente é menor que isso nesse contexto (eleições para governador nos Estados Unidos), o que é diferente de ausência de evidência.";
  - L465: "A certeza moderada qualifica a classificação como nulo ou trivial: o efeito, se houver, provavelmente é menor que 2 pontos percentuais nesse contexto, o que é diferente de ausência de evidência."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V6. Resumo em linguagem simples, "A revisão em resumo".**

- **Trecho no texto:** "Nos experimentos, ver uma pesquisa tende a favorecer quem aparece à frente, mas a evidência é muito incerta. Uma pesquisa de disputa apertada provavelmente não muda o comparecimento em mais de 2 em cada 100 eleitores."
- **Fonte:**
  - "tende a favorecer" afirma efeito com certeza muito baixa. As células só dizem para que lado apontam as estimativas, e a frase invertida soaria igualmente confiante;
  - a segunda frase perde o comparador. O achado é pesquisa apertada **em vez de folgada** (C13), e, sem o comparador, o leitor entende "frente a nenhuma pesquisa" (R2.9).
- **Correção** (49 palavras): "Nos experimentos, as estimativas apontam a favor de quem aparece à frente, mas a evidência é muito incerta. Pesquisa de disputa apertada, em vez de folgada, provavelmente não muda o comparecimento em mais de 2 em cada 100 eleitores. Não há estudo de pesquisas com dados só do Brasil."
- **Onde:** `linguagem_simples.qmd`.

**V7. "Efeitos grandes" sem número nem faixa declarada.**

- **Trecho no texto:** §3.8 (L553), "As exposições do dia da votação (boca de urna e apuração parcial) têm efeitos grandes, mas são as únicas de variação natural em eleição real, e o momento se confunde com o desenho."
- **Fonte:** o protocolo não fixou *benchmark* de magnitude ("δ [...] sem *benchmark* de campo", §2.5). Sem faixa declarada, rótulos como "grande" não aparecem (R4.14, R5.52, A16).
- **Correção:** "Nas exposições do dia da votação (boca de urna e apuração parcial), as estimativas chegam a +11,76 pontos percentuais no apoio (@Araujo2021a) e a −11 pontos no comparecimento (@Morton2015a), mas essas são as únicas de variação natural em eleição real, e o momento se confunde com o desenho."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V8. Valores de p de teste de sinal sem a ressalva ao lado.**

- **Trecho no texto:**
  - §3.9 (L481): "9 de 9 experimentos foram na direção *bandwagon* (proporção 1,00; IC 95% 0,66 a 1,00; p = 0,004)";
  - L487: "(@Gandhi2019 contra; p = 0,012)" e "(p = 0,008)";
  - legenda de `tbl-s8-sensibilidades`.
- **Fonte:** R5.18 e A25 pedem a ressalva junto de todo resultado de teste combinado. A ressalva está só na §2.5 e, parafraseada, porque o texto literal do livro contém "significativo", que as travas do projeto proíbem. A paráfrase é fiel. O que falta é a ressalva ao lado desses três valores de p, os únicos abaixo de 0,05.
- **Correção:**
  - no fim do parágrafo da L487, acrescentar: "Esses valores de p vêm de teste de sinal em agrupamentos *post hoc*: indicam só que a proporção numa direção difere de metade, não informam a magnitude nem distinguem estudos grandes de pequenos, e não definem rótulo.";
  - na legenda de S8, acrescentar a mesma frase.
- **Onde:** `_esqueleto_revisao_final.qmd` e `montar_suplemento.py` (legenda de S8).

**V9. Numeração de figuras e tabelas fora da ordem de chamada.**

- **Trecho no texto:**
  - §2.5 (L262) chama @fig-celulas e @fig-direcao, as Figs. 4 e 5, antes da primeira chamada das Figs. 2 e 3;
  - §2.6 (L266) chama @tbl-sof, a Tab. 2, antes da Tab. 1 (L298).
- **Fonte:** A20 e R5.24 pedem numeração na ordem de aparição e conferência de cada chamada.
- **Correção:**
  - L262: "Os gráficos, nos Resultados, são a proporção por célula, a direção por estudo, ordenada por célula, desenho e risco de viés, com símbolo de tamanho constante porque os n estão em unidades diferentes (desvio declarado do *effect direction plot*), e *forest plots* sem intervalo de predição.";
  - L266: "(notas da tabela de resumo dos achados, nos Resultados)".
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V10. *Forest plots* em ordem alfabética, sem a ordem declarada nem o risco de viés.**

- **Trecho:** @fig-metas. `dados_metas.csv` põe os estudos em ordem alfabética (Agranov, Timotei, Tyszler; Fichnova, Lammers, Witsman). A legenda não declara a ordem nem mostra o risco de viés por estudo.
- **Fonte:** R5.25 pede ordem por característica, não alfabética, declarada. R5.9 pede o julgamento de risco de viés ao lado de cada estudo (A5).
- **Correção:** ordenar por precisão em `preparar_dados_figuras.py` e acrescentar à legenda: "Em cada painel, os efeitos estão ordenados por precisão, do menor ao maior erro-padrão. Todos os efeitos do painel **a** estão em algumas preocupações de risco de viés, e todos os do painel **b**, em risco alto."
- **Onde:** `revista/figuras/legendas.yml`, `revista/figuras/preparar_dados_figuras.py` e `gerar_figuras.R`.

**V11. Fluxograma PRISMA.**

- **Trecho:** @fig-prisma e sua legenda, "a triagem de títulos e resumos e a avaliação dos textos completos foram feitas por agentes de IA".
- **Fonte:**
  - o diagrama mantém caixas zeradas que não se aplicam: "registros de estudos (n = 0)", "sites e organizações (n = 0)", "outros (n = 0)" e "outros motivos (n = 0)" nos dois ramos. R5.5 manda tirá-las;
  - no texto completo, 16 casos foram decididos pelo autor (8 inclusões e 8 exclusões; E4), e o diagrama não separa humano de automação (R5.2, A1).
- **Correção:**
  - tirar as caixas zeradas em `preparar_dados_figuras.py`;
  - na legenda, trocar o trecho por "a triagem de títulos e resumos foi feita por agentes de IA, e a avaliação dos textos completos também, exceto 16 casos limítrofes decididos pelo autor (8 inclusões e 8 exclusões); o fluxo inclui a triagem complementar da Emenda 6b".
- **Onde:** `revista/figuras/legendas.yml` e `revista/figuras/preparar_dados_figuras.py`.

**V12. Estudos excluídos citados por autor e ano, sem referência.**

- **Trecho no texto:** §3.1 (L296), "(Scheuerman 2019, 2020 e 2021; Yosef 2017; Bischoff 2012; Hizen 2025; Morton 2015b; C2)", "(Reveco 2026 [...])", "(Corbetta 2013 [...])", "(Kim 2018b; C3)", "(Kim 2025a; C1)" e "(Freden 2021; Mavridis 2016a; C4)".
- **Fonte:** nenhuma dessas chamadas tem referência em `revista/referencias.json`. As letras "b" e "a" vêm das chaves internas e não correspondem a nada que o leitor veja. A8 pede que toda chamada corresponda a uma referência, e o PRISMA 16b pede a citação dos excluídos limítrofes.
- **Correção:** acrescentar as 14 referências e citar por `@chave` ou, se o artigo não as quiser na lista, mover a lista para uma tabela do suplemento com referência completa e motivo, e escrever no §3.1 "(lista com referências e motivos no suplemento)".
- **Onde:** `_esqueleto_revisao_final.qmd`, um `.bib` de referências e `montar_suplemento.py`.

**V13. O Resumo não traz as limitações da evidência.**

- **Trecho no texto:** "**Limitações.** Sem validação humana (18 pendências); 342 de 526 relatos não recuperados."
- **Fonte:** R2.1 e A11 pedem as limitações **da evidência** entre os 12 itens do resumo, e as duas listadas são do processo.
- **Correção**, que leva o Resumo a 250 palavras:
  - Resumo: "**Limitações.** De 1 a 4 estudos por célula, quase só de laboratório e vinheta; sem validação humana (18 pendências); 342 de 526 relatos não recuperados.";
  - *Abstract*: "**Limitations.** One to four studies per cell, mostly laboratory or vignette studies; no human validation (18 open tasks); 342 of 526 reports were not retrieved."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V14. O relatório técnico ainda chama Hardmeier (2008) de meta-análise.**

- **Trecho:** `07-relatorio/relatorio.qmd`:
  - L51: "é a de @Hardmeier2008, uma síntese com meta-análise cujo último ano de busca não foi verificado";
  - L619: "@Hardmeier2008 fez uma meta-análise cujos números e período não foram verificados nesta revisão".
- **Fonte:** `insumos/revisoes_anteriores.md`, seção 2, diz que a meta-análise é de Hardmeier e Roth (2003) e que o capítulo de 2008 não foi verificado. O artigo já corrigiu isso ("O que mudou", iii), mas remete ao relatório técnico para a declaração de IA, e os dois produtos se contradizem (R2.9).
- **Correção:**
  - L51: "é a de @Hardmeier2008, capítulo de síntese sem texto aberto, cujo conteúdo e período não foram verificados";
  - L619: "@Hardmeier2008 é um capítulo de síntese cujo conteúdo não foi verificado (sem texto aberto)".
- **Onde:** `07-relatorio/relatorio.qmd`, fora dos objetos desta verificação, mas publicado junto com eles.

**V15. Saídas do artigo desatualizadas e PDF reprovado na trava de mancha.**

- **Trecho:** `revisao_final.html` e `revisao_final.docx` são de 14:37 e o `.qmd` é de 15:01. Cerca de 25% das frases do `.qmd` (124 de 496) não aparecem no HTML. `revista/verificar_pdf.py revisao_final.pdf --artigo` reprova 5 páginas por texto fora da mancha: pp. 5, 12, 14, 19 e 25, até 190,5 mm.
- **Fonte:** A2 pede os mesmos números nos derivados. `ferramentas/publicar.sh` roda o `verificar_pdf.py` e pararia na publicação.
- **Correção:** renderizar de novo HTML e `.docx` a partir do `.qmd` atual e ajustar a composição dessas cinco linhas no tema Typst (hifenização ou quebra) antes de publicar. Não é mudança de texto.
- **Onde:** renderização e `revista/typst-template.typ`.

**V16. Declaração de conflito atribuída ao autor além do que ele declarou.**

- **Trecho no texto:** Informações adicionais (L692), "**Conflitos de interesse.** Nenhum, por declaração do autor, inclusive com o provedor das ferramentas de IA."
- **Fonte:** o protocolo, linha 27, registra só "nenhum declarado pelo `revisor_humano_1`". O "inclusive com o provedor" vem da declaração de IA redigida por agente (`07-relatorio/declaracao_uso_ia_texto.md`), e não há registro de o autor ter declarado isso. A regra do projeto é que nenhum papel humano seja atribuído sem declaração do autor.
- **Correção:** "**Conflitos de interesse.** Nenhum, por declaração do autor no protocolo. Relação com o provedor das ferramentas de IA: **[A confirmar pelo autor]**."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V17. Versões de *software* incompletas nos métodos.**

- **Trecho no texto:** §2.5 (L260), "Os pacotes foram o metafor 5.0.1 [@Viechtbauer2010Metafor] e o clubSandwich [@Pustejovsky2026ClubSandwich]."
- **Fonte:** R4.5 (iv) e A15 pedem o *software* com versão. Faltam a versão do R e a da ferramenta de revisão (`rs.py`, `swim.R`, `efeitos.R`), e a do clubSandwich (0.7.0) só aparece na disponibilidade de dados. Na máquina de trabalho, hoje, estão o R 4.5.2, o metafor 5.0.1 e o clubSandwich 0.7.0.
- **Correção:** "Os pacotes foram o metafor 5.0.1 [@Viechtbauer2010Metafor] e o clubSandwich 0.7.0 [@Pustejovsky2026ClubSandwich], no R [versão registrada no *log*], chamados pelos *scripts* da ferramenta de revisão (versão [a registrar])."
- **Onde:** `_esqueleto_revisao_final.qmd`.

### Ok com ressalva

**R1. Arredondamento assimétrico do IC de uma célula com 1 estudo.**

- O limite inferior 0,025 aparece como "0,03", e o superior 0,975, como "0,97". Arredondando meio para cima, que é o que dá 0,03, o superior é 0,98. O 0,97 é artefato do ponto flutuante: `round(0.975, 2)` dá 0,97.
- Aparece em C14, C16 e C17 (Tab. 2 e S8), na §3.7 (L473, "0,00 a 0,97") e na §4.3 (L593, "0,00 a 0,97").
- **Correção:** "0,00 a 0,98" em todos os lugares, com o formatador corrigido em `revista/gerar_celulas.py` e nos montadores (arredondamento por `Decimal`, meio para cima), e o texto do esqueleto nas duas linhas.

**R2. Datas.**

- O artigo e o resumo em linguagem simples estão datados de 25/09/2026, e a declaração de IA diz "entre 19/09/2026 e 25/09/2026". Esta verificação foi feita em 24/09/2026.
- O suplemento está datado de 24/09/2026, e S2 diz "a revisão rodou de 19/09 a 24/09/2026".
- **Correção:** usar a data real da publicação nos três documentos e em S2 (`insumos/garritty_2024.md`, linha 233) e confirmar a última data de uso de IA na publicação.

**R3. "Feito sob voto obrigatório".**

- Resumo executivo (L74), §4.3 (L595) e Tab. 5 dizem "nenhum estudo de comparecimento da síntese foi feito sob voto obrigatório". A codificação diz 2 "não" e 9 "não informado" (`numeros_v2.json`; o texto da §3.8, L559, diz isso certo).
- **Correção:** "nenhum estudo de comparecimento da síntese tem voto obrigatório codificado (2 sem voto obrigatório e 9 sem a informação)".
- **Onde:** `_esqueleto_revisao_final.qmd` e `revista/tabelas/transferibilidade.yml`.

**R4. Tramitação do PL 2.567/2022.**

- §1.1 (L128): "tramitava apensado ao PL nº 96/2011". Segundo `insumos/contexto_brasil.md`, ele está apensado ao PL 1.764/2022, que tramita apensado ao PL 96/2011.
- **Correção:** "tramitava apensado ao PL nº 1.764/2022, por sua vez apensado ao PL nº 96/2011, pronto para pauta".

**R5. Emenda 4 e escolha do árbitro atribuídas ao autor.**

- §2.7 atribui ao autor a Emenda 4 (4a a 4c) e a escolha do árbitro por custo. As duas se apoiam no texto de `emendas.md` ("por questionário"; "por decisão de custo do revisor humano"), mas não estão na lista que o autor confirmou na Emenda 6a (G1, G2, Emenda 1 e os casos limítrofes).
- Não há contradição, mas vale incluir as duas na confirmação que a CRediT já pede ("nas demais escolhas de método, [A confirmar pelo autor]").

**R6. Etapas ainda não concluídas descritas como feitas.**

- §2.7 (L280) descreve "a verificação independente, uma rubrica cega e duas leituras críticas simuladas". No momento desta verificação, a rubrica e a leitura L2 existiam, e a L1 não.
- O comentário `<!-- coordenador: conferir ao fim da etapa 7 [...] -->` já prevê a conferência. Manter o texto só se as três tiverem sido concluídas.

**R7. Emenda 3 em S3.**

- A linha da Emenda 3 diz "correção de registro ou de omissão, sem nova decisão de método". A mesma emenda registrou a troca do árbitro previsto no protocolo, que é desvio de método decidido pelo autor antes da avaliação.
- **Correção**, no objeto: "codebooks de risco de viés copiados para o protocolo; troca do árbitro do RoB (decisão de custo do autor, antes de qualquer avaliação)".
- **Onde:** `montar_suplemento.py`, dicionário de tipos, linha 215, ou a fonte da tabela.

**R8. Tab. 3 com formulação definitiva para achado descritivo ou de certeza moderada.**

- Linha E7: "a crença de proximidade isolada não muda o comparecimento". Linha R2: "move a crença sobre a proximidade, mas não o comparecimento".
- **Correção:**
  - E7: "a crença de proximidade isolada não mostrou efeito sobre o comparecimento no único teste (@Gerber2020a)";
  - R2: "move a crença sobre a proximidade, mas provavelmente não o comparecimento além de ±2 p.p.".
- **Onde:** `revista/tabelas/hipoteses.yml`.

**R9. Número de competidores.**

- §3.8 (L549): "O número de competidores não muda a direção".
- **Correção:** "A direção não variou com o número de competidores nestes estudos".

**R10. Estudos por nível de moderador.**

- §2.5 (L262): "Nenhuma célula teve 3 estudos por nível de moderador". A C02 tem 3 estudos hipotéticos (um só nível).
- **Correção:** "Nenhuma célula teve 3 estudos em cada nível de um moderador".

**R11. "Efeito médio" no sentido de média.**

- L136, L258 e a linha R1 da Tab. 3 usam "efeito médio" no sentido de efeito na média. A adaptação brasileira do GRADE reserva "efeito médio" para o tamanho intermediário (R5.37, A17).
- **Correção:** "efeito na média".
- **Onde:** esqueleto e `hipoteses.yml`.

**R12. "O que mudou" no fim.**

- "O que mudou desde 24/09/2026" está nas Informações adicionais. R2.17 pede que a versão atualizada abra com o que mudou.
- **Correção:** uma frase no aviso inicial, "Esta versão reestrutura o texto como artigo, sem mudar a análise (ver O que mudou, nas Informações adicionais)."

**R13. Declaração de IA do artigo.**

- Faltam a justificativa do uso de IA, quem pagou o acesso e os termos de tratamento dos dados pelo provedor (R7.15, R7.19). O relatório técnico registra os dois últimos como "não registrado".
- **Correção:** acrescentar "O uso de IA em todas as etapas depois do protocolo foi escolha do autor para uma revisão rápida; quem pagou o acesso e os termos de retenção dos dados não estão registrados no projeto."

**R14. Tab. 2 junta 18 comparações numa só tabela.**

- R5.44 e R5.45 pedem até sete desfechos por tabela e uma tabela por comparação. A divisão em quatro blocos atenua o problema. É escolha de formato, a declarar ou dividir numa revisão futura.

## Leitura às cegas

Cada conclusão foi relida com a direção invertida. "Sim" quer dizer que o texto invertido soaria igualmente confiante sem que a certeza o sustentasse, e isso é registrado como aviso.

| Local | Conclusão | Invertida soaria igual? | Registro |
|---|---|---|---|
| Mensagens, 1 | 4 de 4 *bandwagon* nas duas células; "a evidência é muito incerta" | Não: a frase padrão da certeza muito baixa vem logo depois | ok |
| Mensagens, 2 | Apertada × folgada "provavelmente não muda"; "pode aumentá-lo"; "podem reduzi-lo" | Não: frases padrão por certeza | ok |
| Mensagens, 3 | Brasil: "a evidência é muito incerta" | Não | ok |
| Mensagens, 4 | "Sozinha, a evidência não sustenta nem a restrição nem a manutenção" | Não: simétrica | ok |
| Resumo, Resultados e Conclusões | "certeza muito baixa, e não se sabe o tamanho do efeito, nem se ele existe" | Não | ok |
| Resumo executivo, § 5 | "É evidência de que o efeito, se houver, é menor que isso" | Sim: afirma sem "provavelmente" e sem contexto | aviso V5 |
| Discussão 4.1, § 1 | "As classes não se contradizem"; células não randomizadas sem certeza | Sim | aviso V3 |
| Discussão 4.1, § 2 | "O maior experimento de campo permite descartar, com certeza moderada" | Sim: "descartar" vai além de "provavelmente" | erro E3 |
| Discussão 4.1, § 3 | "As três contribuições [...] se confirmam"; "mostra que a regularidade *bandwagon* vem de um tipo de desenho" | Sim: enquadramento otimista sobre a própria revisão, com base *post hoc* | aviso V4 |
| Conclusões, § 1 | Direção *bandwagon* com "a evidência é muito incerta"; "provavelmente"; "pode"; boca de urna muito incerta | Não | ok |
| Conclusões, § 2 | "não diz de quanto é o efeito [...] nem permite afirmar que elas não têm efeito" | Não: simétrica | ok |
| Linguagem simples, "A revisão em resumo" | "ver uma pesquisa tende a favorecer quem aparece à frente" | Sim: afirma tendência de efeito com certeza muito baixa | aviso V6 |
| Linguagem simples, "O que isso significa?" | "não permite dizer que as pesquisas mudam o resultado das eleições, nem que não mudam" | Não | ok |

## Conferências que passaram sem divergência

- **PRISMA** (`07-relatorio/prisma_contagens.json`):
  - identificação: 1.767 (1.687 + 80); 1.706 = 1.189 + 411 + 106; 1.687 = 1.438 + 118 + 131;
  - antes da triagem: 46 e 4 duplicados; 148 e 648 pelo filtro de ano (796);
  - triagem: 1.573 e 1.054 triados; 1.314 e 787 excluídos;
  - texto completo: 259 e 267 buscados (526); 158 e 184 não recuperados (342); 101 e 83 avaliados; 59 e 70 excluídos, com os motivos 39/50, 8/13, 10/4 e 2/3;
  - inclusão: 41 estudos e 55 relatos (42 + 13); 1.235 registros da B01 fora; invariantes fechadas.
- **Células:** as 18 células de `celulas.json` batem com `swim_principal/swim_resumo.json` e `certeza.csv` em k, x de y, mistos, nulos, IC de Clopper-Pearson e p do teste de sinal, recalculados por programa. As certezas batem, 15 muito baixa, 2 baixa e 1 moderada, e o mesmo vale para os 27 estudos, as 18 células com estudo, a célula vazia (@Kaplan2019a) e as notas a a h da Tab. 2.
- **Metas** (`meta_*/meta_resumo.json`):
  - célula sem pesquisa: g 0,48 (IC −1,51 a 2,47; p 0,263; gl 1,25; τ² 0,04; τ 0,20; I² 15%; PI −3,55 a 4,51); ρ 0,49, 0,48 e 0,47; *leave-one-out* de 0,19 a 0,69, e sem @Timotei2013a, 0,40 a 0,98; com ICC 0,20, 0,51 (−0,97 a 1,98);
  - célula do mesmo candidato: g 0,62 (−0,48 a 1,72; p 0,111; gl 1,46; τ² 0,41; τ 0,64; I² 94%; PI −7,82 a 9,05); ρ 0,61, 0,62 e 0,62; *leave-one-out* de 0,55 a 0,90, e sem @Lammers2022a, 0,85 a 0,94.
- **Sensibilidades** (`swim_sens_*`):
  - 9 de 9 (0,66 a 1,00; p 0,004); só com contexto real, 1 de 1, 2 a 1, 1 desmobilização e 1 nulo, 2 a 2 com 1 misto;
  - com críticos: @Kaplan2019a e @Unkelbach2022a, e *momentum* não randomizado com 2 de 2 (0,16 a 1,00; p 0,5);
  - com os efeitos fora da contagem: 10 de 11 (p 0,012) e 4 a 4 com 1 misto; sem dados anteriores a 2010: 8 de 8 (p 0,008); sem @Araujo2021a: 2 de 3;
  - com ICC 0,20, nenhuma contagem muda.
- **δ:** 2 p.p. dá g 0,0441 com p0 0,50, 0,0464 com p0 0,60 e 0,0573 com p0 0,73 (`_delta_celula.txt`).
- **Risco de viés** (`04-qualidade/rob_*`): 43 resultados de 37 estudos; RoB 2 17/6, ROBINS-I 2/8/3 e EPOC 6/1; 21 de 23 no D5; 11 de 13 com confundimento grave ou crítico; 259 domínios, 171 com consenso automático e 88 arbitrados, com o árbitro seguindo A em 79, B em 7 e dando terceiro valor em 2. Os estudos das células C01 e C02 estão em algumas preocupações e em risco alto, respectivamente.
- **Tab. 1:** as 35 porcentagens foram refeitas, todas certas com uma casa, e as faixas de ano (5, 19 e 17) foram refeitas de S4.
- **Transferibilidade:** 3 estudos com voto obrigatório e 10 com o dado informado; 11 estudos de comparecimento na síntese, 2 "não" e 9 não informados; 4 em dois turnos; 3 com regra de divulgação, 2 deles na síntese; 1 com confiança nas pesquisas.
- **Processo** (`relatorio.qmd`, `emendas.md`, `correcoes_sessao_2026-09-23.csv`):
  - triagem: 81 divergências; 0,97 (κ 0,90; PABAK 0,94); amostras de 141 e 300;
  - Emenda 6b: 336 registros, 172 com resumo recuperado, 156 exclusões, 180 ao texto completo, 15 recuperados e excluídos, 165 não recuperados;
  - elegibilidade: 165 decisões propostas (47 inclusões e 118 exclusões);
  - extração: 560 efeitos de 40 estudos, 70 principais; recodificação cega de 10 estudos com 58,5% em 560 comparações e 37 variáveis abaixo do limiar (κ 0,38, 0,38 e 0,15);
  - reextração: 56 efeitos principais (15 concordantes, 23 com mesmo valor e outra classificação, 12 com outro valor, 6 com outro sinal); 28 estudos arbitrados; 772 correções, 240 estendidas, 40 barradas;
  - busca: 19 âncoras, 15 de 19 na v4 e 19 de 19 na v5.
- **Mecanismos e moderadores** (`insumos/mecanismos_moderadores.md`):
  - mecanismos: 34 de 41 estudos com mecanismo testado, 3 por mediação; concordância de 60% e 40%; 25 estudos marcam o voto estratégico; 0,08 p.p. em @Gerber2020a;
  - realismo e competidores: 4 hipotéticos, 5 induzidos e 4 reais (3 e 1) no apoio; 3 de 4 e 2/3/1/1 no comparecimento; 5 de 5 e 7 de 8 por número de competidores; 8 de 13 com regra do experimento;
  - subgrupos e contexto: 11 de 41 com os dias até a eleição; @Cornejo2023a com 0,33, 0,09 e −0,05; 6 estudos com subgrupos de sinais opostos, 2 deles entre eleitores. A tabela de realismo da figura (`dados_realismo.csv`) bate com o texto.
- **Efeitos citados:** conferidos em `06-analise/efeitos.csv` com o IC recalculado:
  - @Lammers2022a: 1,25, 1,03, −0,39 e 0,06;
  - @Feltovich2022: 0,25 e 0,44;
  - @Chatterjee2019a: −0,29 e −0,42;
  - @Araujo2021a: +5,69 e +11,76 p.p.;
  - @Cornejo2023a: 0,19 (EP 0,105);
  - @Freden2024a: −0,41;
  - @Dahlgaard2016a: 0,12 (EP 0,080), IC cruzando zero;
  - @Meer2015a: 0,13 (EP 0,072), IC cruzando zero;
  - @Gerber2020a: os dois IC dentro de ±0,046;
  - @Westwood2020a: −0,10 (EP 0,023), IC de −0,140 a −0,051, abaixo de −δ;
  - @Grillo2024c: IC cruzando zero;
  - @Morton2015a: −11 p.p.
- **Brasil:** Lei 9.504/1997, Resolução 23.600/2019 (PesqEle, multa de R$ 53.205,00 a R$ 106.410,00), ADIs 3.741, 3.742 e 3.743, PLs 2.567 e 2.558/2022, 30 assinaturas da CPI (sem afirmar instalação), ESOMAR/WAPOR (América Latina, mediana de 7 dias, Brasil citado), @Meireles2022 (mais de 2 mil pesquisas, 2012 a 2020) e @PereiraNunes2024 (de cerca de 10 para 7,4 a 7,9 pontos). Todos batem com `contexto_brasil.md`, sem uso de itens não confirmados (única ressalva: R4).
- **Revisões anteriores:**
  - @Barnfield2019: conceitual, não meta-análise nem RS; tipologia estático × dinâmico e conversão × mobilização; efeito "Titanic"; advertência sobre experimentos;
  - @MoyRinke2012: narrativa, sem método descrito; não dá para dizer qual efeito é mais comum; mobilização e desmobilização; dependência de contexto;
  - @Hardmeier2008: sempre "não verificada", sem conteúdo atribuído;
  - @Cosgun2026: uma base, só inglês, pesquisas como uma linha teórica, afirmações causais mais fortes em laboratório e *survey*.
- **Revisões rápidas:** as citações literais das recomendações 5, 6, 7 e 16, o item de registro e a frase sobre PRESS estão em `garritty_2024.md`, e a leitura dentro, fora ou no limite de cada atalho coincide.
- **Marcações humanas:** 11 caixas com os mesmos conjuntos de IDs do v1 e nas seções correspondentes; o apêndice com as 18 pendências de `_pendencias_abertas.json`; 4 marcadores "[A confirmar pelo autor]", 2 na CRediT e 2 na disponibilidade (condições de acesso e licença); declaração de IA abrindo com "RASCUNHO NÃO VALIDADO".
- **Palavras** (limites do livro):
  - Resumo: 238, até 250;
  - Resumo em linguagem simples: 699, de 600 a 750;
  - "A revisão em resumo": 49, até 50.
- **Remontagem:** `montar_revisao_final.py` gerou um `.qmd` idêntico ao atual, e `montar_suplemento.py` regravou `suplemento.qmd` sem diferença (`git diff` vazio). `verificar_figuras.py` passou nas 7 figuras.

## Scripts usados

Rodados da raiz do projeto, com `python3 -B`:

1. `python3 -B 09-documento-final/montar_revisao_final.py --saida <scratchpad>/rf_montado.qmd`, seguido de `diff` com `revisao_final.qmd`: idênticos.
2. `python3 -B 09-documento-final/montar_suplemento.py`: regravou `suplemento.qmd`, com `git diff` vazio.
3. `python3 -B 09-documento-final/conferir_reestruturacao.py`: 0 falhas e 0 avisos, com 1.770 números por lista branca, 18 enunciados, 11 caixas, 18 pendências, chaves, rótulos e proibições.
4. `python3 -B 09-documento-final/revista/figuras/verificar_figuras.py`: OK nas 7 figuras.
5. `python3 -B 09-documento-final/revista/verificar_pdf.py 09-documento-final/revisao_final.pdf --artigo`: 5 falhas de mancha (V15).
6. `verif_fontes.py`, escrito para esta verificação e transcrito abaixo. Refaz, dos arquivos primários:
   - o PRISMA;
   - as 18 células, com Clopper-Pearson e teste de sinal próprios;
   - a caixa contra `certeza.csv` e o painel contra as células;
   - as metas, o risco de viés, as decisões limítrofes, as correções, o realismo e o δ;
   - as contagens de palavras, a ordem de numeração de figuras e tabelas, as chaves de citação, as caixas e o apêndice, os termos proibidos e as duas contradições textuais (S11; experimento de campo).

   Resultado da execução em 24/09/2026:
   - 41 verificações de fonte OK e 4 divergências: a caixa leu 8 de 18 linhas e três linhas do painel divergem (E2, V1);
   - 5 divergências de texto: numeração de figuras e de tabelas (V9, duas linhas), S11 (E1), "maior experimento de campo" (E3) e o falso positivo "não tem efeito principal" em S4;
   - 1 INFO: 17 linhas e 16 registros de decisões limítrofes (E4).
7. Consultas avulsas no terminal:
   - `efeitos.csv`, para os IC dos efeitos citados;
   - `elegibilidade_tc_final.csv`, para os motivos dos excluídos limítrofes e os registros das decisões do autor;
   - `fichamentos_master.csv`, para o sistema eleitoral e o voto obrigatório;
   - comparação do HTML de 14:37 com o `.qmd` atual (V15);
   - `callouts.py`, para comparar as caixas com o v1.

### Transcrição de `verif_fontes.py`

O *script* foi rodado de uma pasta temporária e não fica no projeto. Para refazer a verificação, basta copiar o bloco abaixo e rodá-lo com `python3 -B`.

```python
"""Verificação independente (etapa 5): refaz, a partir dos arquivos primários, os números que o artigo usa.
Só lê arquivos. Uso: python3 -B verif_fontes.py
"""
import csv
import json
from collections import Counter, defaultdict
from math import comb
from pathlib import Path

R = Path("/Users/felipelmc/Desktop/pesquisas-eleitorais-rs")
D = R / "09-documento-final"
out = []


def ok(cond, msg):
    out.append(("OK  " if cond else "DIV ") + msg)


def lcsv(p):
    return list(csv.DictReader(open(p, encoding="utf-8-sig")))


def cp(x, n, a=0.05):
    """IC exato de Clopper-Pearson por bisseção (sem scipy)."""
    def cdf(k, n, p):
        return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))

    def bis(f, lo=0.0, hi=1.0):
        for _ in range(200):
            m = (lo + hi) / 2
            if f(m):
                lo = m
            else:
                hi = m
        return (lo + hi) / 2
    lo = 0.0 if x == 0 else bis(lambda p: 1 - cdf(x - 1, n, p) < a / 2)
    hi = 1.0 if x == n else bis(lambda p: cdf(x, n, p) > a / 2)
    return lo, hi


def psinal(x, n):
    if n == 0:
        return None
    k = min(x, n - x)
    return min(1.0, 2 * sum(comb(n, i) for i in range(0, k + 1)) / 2 ** n)


# 1. PRISMA
P = json.load(open(R / "07-relatorio/prisma_contagens.json"))
b, o = P["bases"], P["outros_metodos"]
ok(b["identificados"]["bases"] == 1767 and b["identificados"]["por_fonte"] == {"openalex": 1687, "bdtd": 80}, "PRISMA identificados 1.767 (1.687 + 80)")
ok(o["identificados"]["busca_citacoes"] == 1189 + 411 + 106 == 1706, "citação 1.706 = SN1 1.189 + SN2 411 + SN3 106")
ok(1438 + 118 + 131 == 1687, "OpenAlex 1.687 = B05 1.438 + B02 118 + B03 131")
ok(b["buscados"] + o["buscados"] == 526 and b["nao_recuperados"] + o["nao_recuperados"] == 342, "526 buscados, 342 não recuperados")
ok(b["removidos_antes_triagem"]["automacao"] + o["removidos_antes_triagem"]["automacao"] == 796, "796 pelo filtro de ano")
ok(all(i["ok"] for i in P["invariantes"]), "invariantes do PRISMA fecham")

# 2. SWiM principal x celulas.json x certeza.csv
S = json.load(open(R / "06-analise/swim_principal/swim_resumo.json"))
C = json.load(open(D / "revista/celulas.json"))
cert = lcsv(R / "06-analise/certeza.csv")
chave_cert = {(r["familia_intervencao"], r["construto_outcome"], r["comparador_tipo"], r["celula_alvo"], r["classe_desenho"]): r for r in cert}
grupos = {(g["familia_intervencao"], g["construto_outcome"], g["comparador_tipo"], g["celula_alvo"], g["classe_desenho"]): g for g in S["grupos"]}
for c in C["celulas"]:
    k = (c["familia_intervencao"], c["construto_outcome"], c["comparador_tipo"], c["celula_alvo"], c["classe_desenho"])
    g = grupos[k]
    x, n = g["n_beneficos"], g["n_estudos"]
    lo, hi = cp(x, n) if n else (None, None)
    p = psinal(x, n)
    iguais = (c["k"] == g["k_estudos"] and c["n_beneficos"] == x and c["n_estudos_com_direcao"] == n
              and c["n_mistos"] == g["n_mistos"] and c["n_nulos"] == g["n_nulos"]
              and (n == 0 or (abs(lo - c["ic_proporcao"][0]) < 1e-6 and abs(hi - c["ic_proporcao"][1]) < 1e-6))
              and (p is None or abs(p - c["p_sinal"]) < 1e-9)
              and chave_cert[k]["certeza"] == c["certeza"] and set(c["estudos"]) == set(g["estudos"]))
    ok(iguais, f"{c['id']} k={c['k']} {x}/{n} IC=({lo if lo is None else round(lo,4)}, {hi if hi is None else round(hi,4)}) p={p} certeza={c['certeza']}")
ok(Counter(r["certeza"] for r in cert) == Counter({"muito_baixa": 15, "baixa": 2, "moderada": 1}), "certeza: 15 muito baixa, 2 baixa, 1 moderada")
estudos_sintese = sorted({e for g in S["grupos"] for e in g["estudos"]})
ok(len(estudos_sintese) == 27, f"27 estudos na síntese principal ({len(estudos_sintese)})")
ok(sum(1 for g in S["grupos"] if g["k_estudos"] > 0) == 18 and len(S["grupos"]) == 19, "18 células com estudo, 19 grupos")

# arredondamento assimétrico de 0,025 e 0,975 (Clopper-Pearson com 1 estudo)
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
for v in ("0.025", "0.975"):
    out.append(f"INFO arredondamento de {v}: meio para cima = {Decimal(v).quantize(Decimal('0.01'), ROUND_HALF_UP)}, "
               f"meio para par = {Decimal(v).quantize(Decimal('0.01'), ROUND_HALF_EVEN)}, float round = {round(float(v), 2)}")

# 3. caixa: quantas linhas de certeza.csv a caixa leu
cx = lcsv(R / "06-analise/caixa_ferramentas.csv")
lidas = sorted({int(r["fontes"].split("linha ")[1]) for r in cx if r["fontes"].startswith("certeza.csv")})
ok(len(lidas) == len(cert), f"caixa leu {len(lidas)} de {len(cert)} linhas de certeza.csv (linhas {lidas})")
por_nivel = defaultdict(list)
for i, r in enumerate(cert, start=2):
    por_nivel[(r["familia_intervencao"], r["construto_outcome"], r["classe_desenho"])].append((i, r["certeza"], r["estudos"]))
for kk, v in sorted(por_nivel.items()):
    if len(v) > 1:
        usada = [i for i, _, _ in v if i in lidas]
        out.append(f"INFO nível {kk}: {len(v)} células em certeza.csv {[(i, c) for i, c, _ in v]}; a caixa usou a linha {usada}")
painel = [r for r in cx if r["dimensao"] == "efeito_painel"]
for r in painel:
    fam, con = r["familia_intervencao"], r["construto_outcome"]
    est = {e for c in C["celulas"] if c["familia_intervencao"] == fam and c["construto_outcome"] == con for e in c["estudos"]}
    certs = [c["certeza"] for c in C["celulas"] if c["familia_intervencao"] == fam and c["construto_outcome"] == con]
    ordem = ["muito_baixa", "baixa", "moderada", "alta"]
    maior = max(certs, key=ordem.index)
    ok(int(r["n_estudos"]) == len(est) and r["certeza"] == maior,
       f"painel {fam} × {con}: caixa n_estudos={r['n_estudos']}, certeza={r['certeza']}; nas células: {len(est)} estudos, maior certeza={maior}")

# 4. metas
for nome, pasta, esperado in [("sem pesquisa", "meta_exploratoria", (0.48, -1.51, 2.47, 0.263, 1.25, 0.04, 0.20, 15, -3.55, 4.51)),
                              ("mesmo candidato", "meta_mesmo_candidato", (0.62, -0.48, 1.72, 0.111, 1.46, 0.41, 0.64, 94, -7.82, 9.05))]:
    m = json.load(open(R / f"06-analise/{pasta}/meta_resumo.json"))["grupos"][0]["resultado"]
    obt = (round(m["estimativa"], 2), round(m["ic"][0], 2), round(m["ic"][1], 2), round(m["p"], 3), round(m["gl"], 2),
           round(m["tau2"], 2), round(m["tau"], 2), round(m["I2"]), round(m["pi"][0], 2), round(m["pi"][1], 2))
    ok(obt == esperado, f"meta {nome}: {obt}")

# 5. RoB
rg = lcsv(R / "04-qualidade/rob_geral.csv")
ok(len(rg) == 43 and len({r['chave'] for r in rg}) == 37, "RoB: 43 resultados de 37 estudos")
cont = Counter((r["ferramenta"], r["rob_geral"]) for r in rg)
ok(cont == Counter({("rob2", "algumas_preocupacoes"): 17, ("rob2", "alto"): 6, ("robins_i", "grave"): 8, ("robins_i", "critico"): 3,
                     ("robins_i", "moderado"): 2, ("epoc", "alto"): 6, ("epoc", "baixo"): 1}), f"RoB geral por ferramenta: {dict(cont)}")
tot = auto = 0
seg = Counter()
for f in ["rob_rob2_consenso.csv", "rob_robins_i_consenso.csv", "rob_epoc_consenso.csv"]:
    for r in lcsv(R / "04-qualidade" / f):
        tot += 1
        if r["julgamento_a"] == r["julgamento_b"]:
            auto += 1
        else:
            seg["A" if r["julgamento_consenso"] == r["julgamento_a"] else "B" if r["julgamento_consenso"] == r["julgamento_b"] else "outro"] += 1
ok((tot, auto, seg["A"], seg["B"], seg["outro"]) == (259, 171, 79, 7, 2), f"domínios {tot}, consenso automático {auto}, árbitro A/B/outro {seg['A']}/{seg['B']}/{seg['outro']}")

# 6. decisões humanas limítrofes
ca = lcsv(R / "00-protocolo/correcao_atribuicao.csv")
lim = [r for r in ca if r["classificacao"] == "mantida" and r["etapa"] == "07_textos_elegibilidade"]
reais = {r["objeto"].split()[0] for r in lim if "teste" not in r["observacao"]}
out.append(f"INFO decisões limítrofes do autor: {len(lim)} linhas no log, {len(reais)} registros distintos (1 linha de teste)")

# 7. correções dos efeitos
corr = lcsv(R / "05-decomposicao/correcoes_sessao_2026-09-23.csv")
ext = sum(1 for r in corr if r["origem"].startswith("coordenador de IA, extens"))
ok(len(corr) == 772 and ext == 240, f"correções: {len(corr)}, extensões {ext}")

# 8. realismo (figura) x texto
real = lcsv(D / "revista/figuras/dados/dados_realismo.csv")
ap = Counter((r["realismo"], r["direcao"]) for r in real if r["desfecho"] == "apoio_ao_lider" and r["excluido_critico"] == "0")
mo = Counter((r["realismo"], r["direcao"]) for r in real if r["desfecho"] == "mobilizacao" and r["excluido_critico"] == "0")
ok(ap == Counter({("hipotetico", "benefico"): 4, ("induzido", "benefico"): 5, ("real", "benefico"): 3, ("real", "danoso"): 1}), f"realismo apoio {dict(ap)}")
ok(mo == Counter({("induzido", "benefico"): 3, ("induzido", "danoso"): 1, ("real", "benefico"): 2, ("real", "danoso"): 3,
                  ("real", "misto"): 1, ("real", "nulo"): 1}), f"realismo comparecimento {dict(mo)}")

# 9. delta
import math
for p0, esp in [(0.50, 0.044), (0.60, 0.046), (0.73, 0.0573)]:
    p1 = p0 + 0.02
    d = math.log((p1 / (1 - p1)) / (p0 / (1 - p0))) * math.sqrt(3) / math.pi
    ok(abs(d - esp) < 0.0006, f"δ com p0 = {p0}: g = {d:.4f} (texto {esp})")

# 10. transferibilidade e Tab. 1 a partir do master
M = lcsv(R / "05-decomposicao/fichamentos_master.csv") if (R / "05-decomposicao/fichamentos_master.csv").exists() else []
if M:
    col = lambda nome: [r.get(nome, "") for r in M]
    out.append(f"INFO master: {len(M)} linhas; colunas voto_obrigatorio/sistema_eleitoral presentes: "
               f"{'voto_obrigatorio' in M[0]}/{'sistema_eleitoral' in M[0]}")
    vo = Counter(r.get("voto_obrigatorio", "")[:3].lower() for r in M)
    out.append(f"INFO voto_obrigatorio (3 primeiras letras): {dict(vo)}")
    se = Counter(r.get("sistema_eleitoral", "") for r in M)
    out.append(f"INFO sistema_eleitoral: {dict(se)}")

print("\n".join(out))
print(f"\n{sum(1 for l in out if l.startswith('DIV'))} divergências, {sum(1 for l in out if l.startswith('OK'))} OK")


# ---------------------------------------------------------------- 11. conferências de texto
import re
A = (D / "revisao_final.qmd").read_text(encoding="utf-8")
SUP = (D / "suplemento.qmd").read_text(encoding="utf-8")
LS = (D / "linguagem_simples.qmd").read_text(encoding="utf-8")
V1 = (D / "_revisao_final_v1_oqf.qmd").read_text(encoding="utf-8")
out2 = []


def palavras(t):
    t = re.sub(r"\[([^\]]*)\]\{[^}]*\}", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return len([w for w in t.replace("*", "").split() if re.search(r"\w", w)])


res = re.search(r"# Resumo \{#resumo.*?\n(.*?)\*\*Palavras-chave", A, re.S).group(1)
abs_ = re.search(r"# Abstract \{#abstract.*?\n(.*?)\*\*Keywords", A, re.S).group(1)
ls_corpo = re.sub(r"^#+ .*$|^:::.*$", "", LS.split("---", 2)[2], flags=re.M)
ls_res = re.search(r"## A revisão em resumo\n\n(.*?)\n\n:::", LS, re.S).group(1)
out2.append(f"INFO palavras: resumo {palavras(res)} (limite 250), abstract {palavras(abs_)}, "
            f"linguagem simples {palavras(ls_corpo)} (600 a 750), 'A revisão em resumo' {palavras(ls_res)} (até 50)")

# ordem de numeração de figuras e tabelas x primeira chamada
linhas = A.split("\n")
defs, prim = {}, {}
for i, l in enumerate(linhas, 1):
    for m in re.finditer(r"\{#((?:fig|tbl|qdr)-[\w-]+)", l):
        defs.setdefault(m.group(1), i)
    for m in re.finditer(r"@((?:fig|tbl|qdr)-[\w-]+)", l):
        prim.setdefault(m.group(1), i)
for tipo in ("fig", "tbl"):
    ks = sorted([k for k in defs if k.startswith(tipo)], key=defs.get)
    chamadas = sorted([k for k in ks if k in prim], key=prim.get)
    fora = [k for k in ks if k in prim][:len(chamadas)] != chamadas
    out2.append(("DIV " if fora else "OK  ") + f"{tipo}: numeração {[k for k in ks]} x ordem da 1ª chamada {chamadas}")

# chaves de citação
refs = {r["id"] for r in json.load(open(D / "revista/referencias.json"))}
for nome, t in (("artigo", A), ("suplemento", SUP)):
    ks = {k for k in re.findall(r"(?<![\w.])@([A-Za-z][\w:-]*\w)", re.sub(r"https?://\S+", "", t))
          if not k.startswith(("fig-", "tbl-", "sec-", "qdr-"))}
    falt = sorted(k for k in ks if k not in refs)
    out2.append(("OK  " if not falt else "DIV ") + f"{nome}: {len(ks)} chaves, ausentes em referencias.json: {falt}")
# citações autor-ano digitadas à mão (sem @)
maos = re.findall(r"\b([A-Z][a-zà-ü]+ (?:\d{4}[a-z]?(?:, \d{4})*(?: e \d{4})?))\b", A)
out2.append("INFO citações autor-ano sem @chave no artigo: " + "; ".join(sorted(set(m for m in maos if not m.startswith(("Lei", "Emenda", "Resolução"))))))

# callouts
def callouts(t):
    blocos = re.findall(r"## Pendente de revisão humana\n\n(.*?)\n:::", t, re.S)
    return Counter(tuple(sorted(set(re.findall(r"P0\d\d", b)))) for b in blocos)
ok_c = callouts(A) == callouts(V1) and sum(callouts(A).values()) == 11
out2.append(("OK  " if ok_c else "DIV ") + f"11 caixas 'Pendente de revisão humana' com os mesmos conjuntos de IDs do v1: {sum(callouts(A).values())}")
pend = json.load(open(R / "07-relatorio/_pendencias_abertas.json"))
ids = [p["id"] for p in pend["pendencias"] if p["status"] == "aberta"]
tab = re.findall(r"^\| (P0\d\d) \|", A, re.M)
out2.append(("OK  " if sorted(ids) == sorted(tab) and len(ids) == 18 else "DIV ") + f"apêndice A: {len(tab)} pendências; abertas no JSON: {len(ids)}")
out2.append(f"INFO marcadores [A confirmar pelo autor]: {A.count('[A confirmar pelo autor]')}")

# termos proibidos
for nome, t in (("artigo", A), ("suplemento", SUP), ("linguagem simples", LS)):
    achados = re.findall(r"(?i)significativ\w*|\bneutro\b|sem efeito|não tem efeito", t)
    out2.append(("OK  " if not achados else "DIV ") + f"{nome}: termos proibidos {achados}")

# S11 vazio x afirmação no artigo
s11 = re.search(r"# S11 .*?\n\n(.*?)\n\n#", SUP, re.S).group(1)
out2.append(("DIV " if "Em preparação" in s11 and "dá o local de cada item" in A else "OK  ")
            + "artigo diz que S11 'dá o local de cada item'; S11 diz: " + s11[:80])

# 'maior experimento de campo' x Tab. 1
out2.append(("DIV " if "O maior experimento de campo" in A and "único experimento de campo" in A else "OK  ")
            + "'O maior experimento de campo' (Discussão) x 'único experimento de campo' (Resumo executivo; Tab. 1: 1)")

print("\n".join(out2))
print(f"\n{sum(1 for l in out2 if l.startswith('DIV'))} divergências de texto")
```
