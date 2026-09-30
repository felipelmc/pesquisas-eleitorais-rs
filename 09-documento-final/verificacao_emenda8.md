# Verificação independente das mudanças de 30/09/2026, noite (Emenda 8)

Verificador independente (agente de IA, `claude-opus-5-5`), que não escreveu nenhum dos textos conferidos. Feita em 30/09/2026 sobre a árvore de trabalho da branch `ajustes-2026-09-30`: commit `aa31429`, mais `docs/`, `REPRODUZIR.md` e dois insumos modificados e ainda não commitados. O `docs/` foi gerado às 18h19, depois da última edição das fontes, e o PDF, o HTML e o pacote conferidos são os que estão lá. O prompt é `prompts_final/prompt_verificacao_emenda8.md`. Nenhum arquivo foi alterado além deste. Não rodei `rs.py`, `montar_*.py` nem `publicar.sh`, e não abri PDF de estudo.

**Mudanças feitas por outro processo durante a verificação.** Entre 18h34 e 18h38, fontes foram editadas e remontadas por outro processo, não por este verificador:

- `_esqueleto_revisao_final.qmd` e `revisao_final.qmd`;
- `montar_suplemento.py` e `suplemento.qmd`;
- `lacunas.yml` e `legendas.yml`;
- `preparar_dados_figuras.py`, as figuras e `montar_vitrine.py`;
- entre outros arquivos.

O `docs/` continua o de 18h19. Às 18h40, conferi de novo contra as fontes atuais os itens abaixo. Três mudaram:

- o E1 já está corrigido na fonte, mas não em `docs/`;
- a frase do δ (O1) foi reescrita;
- a frase da deduplicação na 4.4 (O3) foi reescrita.

As demais divergências seguem nas fontes atuais. Os números de linha citados são os das fontes às 18h40.

## Resumo

| # | Conferência | O que foi checado | Resultado |
|---|---|---|---|
| 1 | Números do fluxo | 17 contagens do PRISMA e 8 entradas `dedup_*` confrontadas com o Resumo, o *Abstract*, as seções 2.4, 3.1 e 4.4, a legenda e a figura do PRISMA, o Apêndice G, a linguagem simples, a Emenda 8, o README, o LEIA do pacote, o `08-revisao-humana/README.md`, os `textos.yml` e o `docs/index.html` (texto visível e JSON embutido). Também o `pdftotext` do `docs/revisao.pdf` (51 páginas), os três HTML e os `.md` do pacote (220 arquivos) | Nenhum dos oito números antigos da lista sobra no PDF. **Sobra o par antigo "158 das bases e 184 dos outros métodos"** no Apêndice B (E1), já corrigido na fonte às 18h38, mas não em `docs/`. O resto bate |
| 2 | Deduplicação | Todos os textos ativos, mais os `.md` e CSV do pacote | Artigo, apêndices, linguagem simples, legendas, vitrine, README, LEIA e o README da revisão humana estão corretos. **Duas listas de conferência do pacote dizem "não aplicada"** (E2). A regra descrita bate com a Emenda 8, a declaração e o log: verifiquei os 44 absorvidos um a um |
| 3 | Atribuição humana | Toda frase com "autor" + verbo de conferência, validação, aprovação ou decisão no artigo, nos apêndices, na linguagem simples, na vitrine, no README, nos dois LEIAs e nas listas de conferência do pacote | Nenhuma frase atribui ao autor RoB, GRADE ou validação cega. **Três listas de conferência dizem que ele conferiu "a triagem" ou "a busca, a seleção e a extração" inteiras** (E3). **"Leu e aprovou esta versão" já não é coberto por nenhuma declaração** (E4). "RASCUNHO NÃO VALIDADO" aparece uma só vez, com as 7 pendências certas. A vitrine diz que RoB e certeza "estão em revisão pelo autor", sem afirmar validação concluída: ok |
| 4 | δ | Protocolo (seção 8, "Limiar de relevância e magnitude"), Emenda 5 (itens 7 e 8, e nota de 24/09), `certeza.csv` e `_delta_celula.txt` | A frase é verdadeira, com uma ressalva de precisão (O1). Os valores 0,044 (10 linhas), 0,046 (7) e 0,0573 (1) de `certeza.csv` e o 0.0573 de `_delta_celula.txt` são iguais aos do texto, e `certeza.csv` não mudou desde a tag v3 |
| 5 | Datas | `grep` em todos os arquivos versionados e não ignorados, em `docs/*.html`, no PDF e no pacote extraído | Artigo, apêndices, linguagem simples, vitrine, README, `CITATION.cff` e PDF estão em 30/09/2026. **O pacote leva "01/10/2026"** em `09-documento-final/declaracao_ia_v2.md` (E5). A tag citada como a desta versão ainda não existe (A1) |
| 6 | Desvios | Lista (i) a (xi) das Informações adicionais × tabela Resumo de `emendas.md` × Apêndice B | Batem: 10 emendas (E001, E002, 1 a 8), com datas e momentos certos, mais o item (ix), "outros". Ficam ressalvas na tabela do Apêndice B (A3) e na redação do item (xi) (O5) |
| 7 | Declaração de IA gerada do log | Seções 6 e 7 de `07-relatorio/declaracao_uso_ia.md` × `rs_estado.json` (42 pendências, 7 abertas) e `rs_log.jsonl` (seq 1 a 874) | Corretas. Batem os seq de abertura e de fechamento e as cadeias de sucessão (P005 → P012 → P016 → P020; P027 → P032 → P039; P034 → P036), as contagens de RoB (23/13/7), os SHA e as contagens dos dois `certeza*.csv` (18/18 e 7/7), a caixa (22) e os portões. Ficam ressalvas de completude (O7) |
| 8 | Travas | `conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd`, rodada duas vezes | **OK, com 0 falhas e 0 avisos, nas duas rodadas.** O corpo (Introdução a Conclusões) tinha **8.498 palavras** nas fontes de 18h19 e **8.493** nas de 18h40, dentro da faixa de 7.500 a 8.500 e perto do teto (O8) |

**Total: 5 erros, 10 avisos e 10 itens ok com ressalva.** Os cinco erros estão em texto publicado em `docs/`: três no pacote de replicação, um nos apêndices (PDF e HTML) e um no artigo e no Apêndice G.

## Erros

### E1. Apêndice B: não recuperados por ramo com os números de antes da Emenda 8

- **Trecho:** Apêndice B, tabela `tbl-s2-consequencias`, linha A5: "Os relatos não recuperados ficam fora: 158 das bases e 184 dos outros métodos." Está em `suplemento.qmd`, L109, em `docs/apendices.html` e no PDF.
- **Fonte:** `prisma_contagens.json` dá `nao_recuperados` = 155 nas bases e 183 nos outros métodos.
- **Origem:** o texto vem do insumo `09-documento-final/insumos/garritty_2024.md` (L220), de 24/09. O `montar_suplemento.py` troca os trechos desse insumo sem editá-lo, mas não trata esse.
- **Correção:** o texto certo é "Os relatos não recuperados ficam fora: 155 das bases e 183 dos outros métodos."
- **Situação às 18h40:** já corrigido na fonte pelo outro processo. A `s2_atalhos` de `montar_suplemento.py` agora tira os dois números de `prisma_contagens.json`, e o `suplemento.qmd` remontado às 18h38 traz 155 e 183. **Falta refazer `docs/`**: `apendices.html`, `revisao.pdf` e o PDF do pacote ainda trazem 158 e 184.
- **Por que passou:** a lista de números proibidos do prompt não inclui 158 nem 184, e a trava aceita os dois porque constam dos números do v1.

### E2. Listas de conferência do pacote: deduplicação "gravada e não aplicada"

As listas vão para o pacote publicado (`docs/pacote-replicacao.zip`, em `tabelas-extras/`), e o artigo remete a elas ("listas de conferência preenchidas estão no pacote de replicação"). A correção se faz nos insumos, e o pacote precisa ser refeito.

- `09-documento-final/insumos/tabelas/checklist_prisma2020.md`, item **16a**, coluna de observação, L24.
  - **Hoje:** "O fluxo separa a remoção por *script*, a triagem por IA e os casos decididos pelo autor; as decisões sobre os pares de duplicata foram gravadas e não aplicadas, e aplicá-las não mudaria os estudos incluídos."
  - **Correção:** "O fluxo separa a remoção por *script*, a triagem por IA e os casos decididos pelo autor; as decisões sobre os pares de duplicata foram aplicadas depois da triagem (Emenda 8) e mudaram contagens do fluxo, mas não os estudos incluídos."
- `09-documento-final/insumos/tabelas/checklist_prisma_s.md`, item **16**, L18.
  - **Hoje:** "Deduplicação por *script* da ferramenta de revisão, com 145 pares incertos decididos pelo autor e gravados sem aplicação; a regra de comparação dos registros não é descrita."
  - **Correção:** "Deduplicação por *script* da ferramenta de revisão; nos 145 pares incertos, o autor concordou com as sugestões da IA, e as decisões foram aplicadas depois da triagem (Emenda 8); a regra de comparação dos registros não é descrita."

### E3. Listas de conferência do pacote: o autor teria conferido a triagem inteira, ou a busca, a seleção e a extração inteiras

As declarações cobrem só a pré-revisão PRESS, as 81 divergências, as 165 propostas e as 3 extensões, o piloto, os 560 efeitos, as 259 divergências da recodificação e o relato. A correção se faz nos insumos, e o pacote precisa ser refeito.

- `insumos/tabelas/checklist_prisma2020.md`, item **8**, L10.
  - **Hoje:** "... O autor conferiu a triagem e a elegibilidade em bloco, sem registro item a item, e a validação cega da triagem não foi feita."
  - **Correção:** "Triagem por dois agentes de IA independentes, com os modelos nomeados; no texto completo, um agente por relato, sem dupla. O autor conferiu em bloco as 81 divergências da triagem e as 165 propostas de elegibilidade, sem registro item a item, e a validação cega da triagem não foi feita."
- `insumos/tabelas/checklist_trAIce.md`, item **A1**, L4. O texto ainda descreve mal o Resumo, que diz "partes de".
  - **Hoje:** "... que o autor conferiu em bloco a busca, a seleção e a extração, ..."
  - **Correção:** "O resumo diz que agentes de IA conduziram as etapas depois do protocolo e que o autor conferiu em bloco partes da busca, da seleção e da extração, sem nomear modelos nem etapas de cada um."
- `insumos/tabelas/checklist_trAIce.md`, item **M8**, L13.
  - **Hoje:** "Um só humano, que decidiu emendas e 16 casos limítrofes e conferiu em bloco busca, triagem, elegibilidade, efeitos e relato, sem registro item a item; ..."
  - **Correção:** "Um só humano, que decidiu emendas e 16 casos limítrofes e conferiu em bloco a pré-revisão PRESS, as 81 divergências da triagem, as 165 propostas de elegibilidade, o piloto, os 560 efeitos, as divergências da recodificação e o relato, sem registro item a item; risco de viés e certeza ficaram só com a IA (Apêndice G). As divergências foram a um árbitro de IA. A formação do autor não é relatada."

### E4. "Leu e aprovou esta versão": nenhuma declaração cobre a versão posterior à Emenda 8

A aprovação registrada é a da P038, no seq 859, cujo motivo diz "o autor leu e aprovou o artigo final com apêndices (versão de entrega de 01/10/2026, commit e377c50)". Depois dela, o texto mudou: contagens do fluxo, item (xi), frase do δ, datas, declaração de IA e Apêndice G. A declaração da deduplicação registra só três decisões (aplicar, a regra e os 9 pares) e nada diz sobre ler ou aprovar o texto resultante. Três trechos afirmam a aprovação desta versão:

- `_esqueleto_revisao_final.qmd`, L222 (2.9): "... (vii) o relato da versão de 24/09/2026; e ele leu e aprovou esta versão antes da entrega."
- `_esqueleto_revisao_final.qmd`, L388 (4.4): "O autor leu a versão de 24/09/2026, da qual esta deriva sem mudar a análise, e leu e aprovou esta antes da entrega."
- `revista/tabelas/lacunas.yml`, L104 e L105 (Apêndice G, linha "Relato"): "... esta versão, que a reescreve sem mudar a análise, foi lida e aprovada por ele antes da entrega (G9), e as correções da Emenda 8 foram pedidas por ele".

**Correção**, uma de duas:

- (a) **Se o autor ler e aprovar esta versão antes de publicar:** registrar a aprovação numa linha datada da declaração (por exemplo, em `08-revisao-humana/P019_dedup/declaracao_autor_2026-09-30_dedup.md`, seção "Decisões": "4. **Relato.** O autor leu e aprovou o artigo com apêndices depois da Emenda 8, em 30/09/2026.") e manter os três trechos.
- (b) **Se não:** trocar os três trechos pelos abaixo. As duas trocas no corpo somam +2 palavras (ver O8).
  - L222: "(vii) o relato da versão de 24/09/2026; e ele leu e aprovou esta versão antes da Emenda 8."
  - L388: "O autor leu a versão de 24/09/2026, da qual esta deriva sem mudar a análise, e leu e aprovou esta antes da Emenda 8."
  - `lacunas.yml`: "Em bloco pelo autor, na versão de 24/09/2026 (declaração de 30/09/2026); esta versão, que a reescreve sem mudar a análise, foi lida e aprovada por ele antes da Emenda 8 (G9), cuja aplicação ele pediu".

### E5. Pacote de replicação com "01/10/2026"

- **Trecho:** `09-documento-final/declaracao_ia_v2.md`, L3, que o pacote leva em `09-documento-final/declaracao_ia_v2.md`: "O estado atual das etapas sem validação humana está no Apêndice G do artigo (versão de entrega de 01/10/2026, Emenda 7)."
- **Correção:** "(versão de entrega de 30/09/2026, Emendas 7 e 8)." Depois, refazer o pacote, que regrava o `MANIFESTO.csv`.

## Avisos

### A1. A tag citada como a desta versão não existe

README (L45), `CITATION.cff` (`version`), a vitrine (rodapé "tag `v3-final-2026-09-30`", via `vitrine/exportar_dados.py` L813) e `REPRODUZIR.md` (L105) citam `v3-final-2026-09-30`. Só existe `v3-final-2026-10-01`, local e no `origin`, apontando para `13b0db2`, a versão anterior à Emenda 8.

**Correção:** criar a tag `v3-final-2026-09-30` no commit final, antes de publicar o Pages e de dar *push*, como o `REPRODUZIR.md` (item 5) já prevê. Apagar a tag antiga no remoto é decisão do usuário. Se ela ficar, é histórico.

### A2. "Antes da triagem", "por script" e "sem IA" já não descrevem todos os duplicados

Dos 91 e 17 duplicados, 45 e 13 (58 registros) saíram por fusões aplicadas **depois** da triagem, e 44 deles já tinham sido triados. Essas fusões vieram de sugestões de IA aceitas pelo autor (log, seq 865 e 868). Estes trechos dizem outra coisa:

- 3.1 (`_esqueleto_revisao_final.qmd`, L230): "Antes da triagem, saíram 91 e 17 duplicados e 143 e 639 relatos pelo filtro de ano (bases e outros métodos)."
  - **Correção**, com as mesmas 21 palavras: "Na deduplicação e no filtro de ano, saíram 91 e 17 duplicados e 143 e 639 relatos (bases e outros métodos)."
- Legenda do PRISMA (`revista/figuras/legendas.yml`, L51 e L52): "A remoção antes da triagem (duplicatas e filtro de ano de publicação) foi feita por script, sem IA, com as fusões de duplicatas decididas pelo autor aplicadas depois da triagem (Emenda 8)."
  - **Correção:** "A remoção de duplicatas e o filtro de ano de publicação foram feitos por script; nos 145 pares incertos, o autor concordou com as sugestões da IA, e essas fusões (58 registros, 44 já triados) foram aplicadas depois da triagem (Emenda 8)." Os números 58 e 44 estão em `numeros_v2.json` (`dedup_absorvidos`, `dedup_absorvidos_triados`). A legenda de figura não conta no corpo.
- Caixa da figura (`revista/figuras/preparar_dados_figuras.py`, L280): "Removidos por script antes da triagem (sem IA):".
  - **Correção:** "Removidos por script:".
- Caixa do PRISMA da vitrine (`vitrine/montar_vitrine.py`, L172): "Removidos antes da triagem:".
  - **Correção:** "Removidos por script:".

### A3. Apêndice B: a linha da Emenda 8 se contradiz

A coluna "Antes ou depois de ver os dados" diz "depois de ver os dados; correção de registro ou de omissão, sem nova decisão de método". A 8b é uma regra nova, decidida depois de ver os dados, e a 8a corrigiu a ferramenta, não um registro. A introdução da tabela traz "Quatro ressalvas" e nada diz da Emenda 8.

**Correção:**

- `montar_suplemento.py`, `s3_emendas`, logo depois do ramo `if idd == "Emenda 6":` (L286):
  `if idd == "Emenda 8": quando = "8a: correção da ferramenta, sem nova decisão de método; 8b: depois de ver os dados"`
- `_esqueleto_suplemento.qmd`, L40: trocar "Quatro ressalvas" por "Cinco ressalvas" e o fim do parágrafo por "... e (iv) a Emenda 7 registra a conferência em bloco do autor e as etapas sem validação humana, sem mudar dados, decisões em vigor nem contagens; e (v) na Emenda 8, o coordenador de IA corrigiu a ferramenta (8a), e o autor decidiu, depois de ver os dados, a regra da decisão mais inclusiva (8b), que mudou contagens do fluxo, mas não os incluídos."

### A4. "Dois defeitos da ferramenta" ficou desatualizado

A 4.4 (L388) diz "Dois defeitos da ferramenta de revisão afetaram registros de triagem, mas não efeitos". Os dois são os de `spec_v2.md`, 4.4-P8: o conferidor de trechos e o classificador de "incert". A Emenda 8a registra um terceiro: a consolidação mantinha as decisões dos registros absorvidos e o `prisma` falhava. Esse também afetou registros de triagem, e a correção dele trocou 2 decisões.

**Correção**, com o mesmo número de palavras: "Três defeitos da ferramenta de revisão afetaram registros de triagem, mas não efeitos."

### A5. Alcance ambíguo de "a triagem" e de "a etapa"

- Na 2.9 (L222), "as decisões em vigor sobre: ... (ii) a triagem, com as 81 divergências mantidas no texto completo pela regra liberal" pode ser lido como aprovação de toda a triagem.
  - **Correção**, com uma palavra a menos: "(ii) as 81 divergências da triagem, mantidas no texto completo pela regra liberal;"
- Na legenda do Apêndice G (`lacunas.yml`, L14 e L15), "o autor declarou ter revisto a etapa e concordado com as decisões em vigor" vale também para a linha da triagem, onde ele reviu só as 81 divergências.
  - **Correção:** "o autor declarou ter revisto o que a coluna descreve e concordado com as decisões em vigor".

### A6. O pacote leva registros que ainda dizem "não aplicada", sem nota

- `08-revisao-humana/declaracao_autor_2026-09-30.md`, bloco "Deduplicação (P019)": "escolheu **registrar as decisões e não aplicá-las** nesta versão. A P019 fica aberta."
  - **Correção:** acrescentar ao fim do bloco "[Nota de 30/09/2026: aplicadas no mesmo dia, a pedido do autor (Emenda 8; `P019_dedup/declaracao_autor_2026-09-30_dedup.md`). A P019 fechou.]", como já foi feito em `emendas.md`.
- `08-revisao-humana/P019_dedup/dedup_revisao_v1.csv`: o `motivo` das 145 linhas diz "decisão registrada e não aplicada nesta versão (Emenda 7)". O mesmo texto está no evento de aplicação do log (seq 864). Não edite o CSV nem o log.
  - **Correção:** acrescentar em `ferramentas/pacote/LEIA.md`, depois do parágrafo da deduplicação: "O `motivo` das 145 linhas de `dedup_revisao_v1.csv` foi escrito na Emenda 7 ("decisão registrada e não aplicada nesta versão"); as decisões foram aplicadas em 30/09/2026 pela Emenda 8."

### A7. A lista PRISMA-trAIce não cita a Emenda 8

No item **M1** (`checklist_trAIce.md`, L6), os desvios com uso de IA param na Emenda 7. Na 8a, foi o coordenador de IA quem corrigiu a ferramenta.

**Correção:** "... a triagem por IA dos registros sem resumo (Emenda 6b), a Emenda 7, que registra a conferência em bloco, e a Emenda 8, em que o coordenador de IA corrigiu a ferramenta para aplicar a deduplicação."

### A8. A trava ainda aceita "01/10/2026"

`conferir_reestruturacao.py`, L89, tem `DATAS_FIXAS = ["24/09/2026", "25/09/2026", "30/09/2026", "01/10/2026"]`. A regra está repetida em `spec_final.md`, L91. Hoje nenhum texto usa a data, mas a trava não impede que ela volte.

**Correção:** tirar `"01/10/2026"` da lista e da frase da `spec_final.md`. Rode `teste_travas.sh` depois, porque o v1 não usa essa data.

### A9. O `CLAUDE.md` descreve o estado de antes da Emenda 8

O `CLAUDE.md` ainda diz:

- que a P019 está aberta ("deduplicação decidida e **não aplicada**");
- que o `etapa_atual` fica em `05_organizacao` "porque a deduplicação (P019) segue aberta";
- que não se deve aplicar a P019 com `rs dedup --revisar` "sem antes corrigir a skill";
- "Versão de entrega (30/09 e 01/10/2026)".

Isso orienta mal as próximas sessões. Pelas regras, este verificador não o altera, e cabe ao usuário decidir a atualização.

### A10. "Item a item nos 9 pares de versão" diz mais do que a declaração

A declaração registra uma decisão única: "Ligar os 9 como versões do mesmo trabalho, como a IA sugeriu (confiança alta)". O texto está no Apêndice G, linha "Deduplicação" (`lacunas.yml`, L43 e L44).

**Correção:** "...; nos 9 pares de versão, ligados por ele como a IA sugeriu (Emenda 8). Os estudos incluídos não mudaram".

## Ok com ressalva

- **O1. Frase do δ** (2.7, L206; glossário, L123). O outro processo a reescreveu às 18h38, e ela terminava assim: "...; a Emenda 5 fixou os dois primeiros em vez da mediana de cada célula que o protocolo pede". Na versão publicada e na atual, a frase é verdadeira. O protocolo pede δ por célula: mediana dos `p0` nas medidas binárias individuais e mediana dos DP na votação agregada. Os valores 0,044 e 0,046 são o "δ padrão" que o próprio protocolo reserva a células mistas ou sem `p0`. A Emenda 5, no item 8, estendeu esse δ padrão ao nulo por ±δ, depois de ver os dados, e o 0,0573 segue a regra do protocolo (item 7 e nota de 24/09). "Em vez da mediana de cada célula" deixa de fora a rota por DP. Troca sugerida, com uma palavra a menos no corpo (o glossário é tabela e não conta): "em vez do δ por célula que o protocolo pede".
- **O2. Contagens da Emenda 6b na 2.4** (L182). Os números 156, 180, 15 e 165 são de antes da deduplicação. Dos 336 registros sem resumo, 4 foram absorvidos (RS1648, RS1986, RS2740 e RS4030). O "antes da deduplicação" do texto dá conta disso.
- **O3. "A decisão mais inclusiva ... passou ao que os absorveu"** (legenda do PRISMA, L59 e L60; também a 4.4 publicada, que o outro processo reescreveu às 18h38). Em 42 dos 44 casos, ficou a decisão do registro que absorveu. Conferi que as 44 decisões finais são a mais inclusiva do par. Redação mais exata para a legenda: "Nos 44 registros já triados que as fusões absorveram, o registro que absorveu ficou com a decisão mais inclusiva do par, e os estudos incluídos não mudaram (Apêndice G)."
- **O4. Emenda 8, item 8c.** "2 foram substituídas" inclui RS1986 → RS1828, com excluir nos dois lados: a decisão da 6b, gravada por *override*, venceu a de IA. Esse caso não está entre as "4 divergências". Das quatro, só RS2740 → RS2124 foi substituída. Sugestão para `00-protocolo/emendas.md`, que não é artefato congelado: "... e 2 foram substituídas (RS2740 → RS2124, abaixo, e RS1986 → RS1828, com a mesma decisão, em que a decisão gravada por `triagem override` venceu a de IA)".
- **O5. Desvios** (L412). "Onze" são as 10 emendas mais o item (ix), "outros", que não tem linha no Apêndice B. Isso já valia para os "dez" de antes. O item (xi) não diz "depois do G9 e de ver os dados" nem cita a 8a. Sugestão, nas Informações adicionais, fora da contagem de palavras: "(xi) Emenda 8, na mesma data, decidida depois do G9 e de ver os dados, que corrigiu a ferramenta e aplicou a deduplicação decidida na Emenda 7, ...".
- **O6.** Na 2.9, "Nenhuma decisão em vigor, dado de efeito ou contagem mudou (Emenda 7)" é verdade para a Emenda 7, e a "Versão e citação" registra que a Emenda 8 mudou contagens. Não exige mudança.
- **O7. Declaração gerada do log.** As seções 6 e 7 estão corretas diante do estado e do log. Duas ressalvas de completude, que o artigo já declara:
  - as 336 decisões da Emenda 6b, gravadas como `humano` com o papel `ia_coordenador_emenda6`, entram na seção 7 só pela linha genérica "Triagem de títulos e resumos: decisões de IA sem validação calculada";
  - "560 de 560 efeitos verificados por humano" reflete marcas postas pelo coordenador a partir da declaração em bloco (motivo da P039, seq 847) e propagadas por script aos 40 CSVs por estudo (commit `09bc3d6`).

  A correção, se desejada, vai no gerador da skill (`rs declaracao-ia`), não no arquivo.
- **O8. Contagem de palavras.** O corpo tinha 8.498 palavras na primeira rodada da trava (fontes de 18h19) e 8.493 na segunda (fontes de 18h40, depois das edições do outro processo), perto do teto de 8.500. O saldo das trocas no corpo sugeridas aqui é zero: A2 (0), A4 (0), A5 (−1), E4(b) (+2) e O1 (−1). Com E4(a), fica −2. Rode a trava de novo depois de qualquer troca.
- **O9.** `08-revisao-humana/README.md`, L64: "dos 338 relatos buscados" fica mais claro como "dos 338 relatos buscados e não recuperados".
- **O10.** `08-revisao-humana/P019_dedup/LEIA.md`, as instruções de 23/09 no repositório privado, fora do pacote, ainda diz "Nenhum desses pares foi decidido". Sugestão de nota no topo: "[30/09/2026: decididos pelo autor e aplicados pela Emenda 8.]".

## O que foi conferido e está correto

- **Fluxo.** Estes trechos batem com `prisma_contagens.json`:
  - Resumo e *Abstract*: 338 de 522;
  - 3.1: 1.767 e 1.706; 91 e 17; 143 e 639; 1.533 e 1.050; 1.277 e 784; 155 de 256 e 183 de 266 (338 de 522); 101 e 83; 59 e 70; 39 e 50; 41 estudos e 55 relatos, 42 e 13;
  - 4.4: 338 de 522;
  - figura do PRISMA: os 32 valores das caixas;
  - Apêndice G: 91 e 17; 145; 44; 9;
  - linguagem simples e vitrine (texto e JSON embutido);
  - Emenda 8: 3.365 únicos (log seq 865), 58 absorvidos, 44 triados, 42 mantidas e 2 substituídas, as 4 divergências (seq 868); 521 na alternativa (declaração).

  Também conferi que nenhum absorvido tinha decisão de texto completo nem estava entre os incluídos, que `incluidos.csv` tem o mesmo SHA antes e depois (seq 856 e 870) e que buscados = incluir + incerto = 522 em `triagem_ta_final.csv`.
- **Deduplicação.** Não há "decidida e não aplicada" nem P019 aberta no artigo, nos apêndices, na linguagem simples, nas legendas, na vitrine, no README, no LEIA do pacote nem no `08-revisao-humana/README.md`. A regra aparece igual na Emenda 8, na declaração e no log: decisão mais inclusiva, 44 absorvidos já triados, 9 pares de versão ligados pelo autor (seq 862, `decidido_por = revisor_humano_1`) e incluídos inalterados.
- **Atribuição.** Batem com a declaração os trechos do Resumo, do *Abstract* e das Mensagens principais ("partes de busca, seleção e extração"), da 2.3 (PRESS), da 2.4 (81 divergências; 165 + 3 + 16), da 2.5 (piloto, 560 efeitos, 259 divergências), da 2.6 e da 2.8 (RoB e GRADE só por IA), da 3.8 (mecanismos: só as divergências da recodificação), da linguagem simples, do README, do LEIA e da vitrine. A frase "estão em revisão pelo autor" (vitrine, README e LEIA) não afirma validação concluída.
- **Datas.** Versão de 30/09/2026 e período de uso de IA de 19/09/2026 a 30/09/2026 no artigo (capa, declaração de IA, versão e citação), nos apêndices, na linguagem simples, na vitrine, no README, no LEIA e no `CITATION.cff`. Nenhum "01/10/2026" nem "2026-10-01" no PDF nem nos HTML.
- **Emendas.** A tabela Resumo de `emendas.md` está bem formada, com a linha "Tipos:" depois da tabela, e o `s3_emendas` lê o título da Emenda 8 sem o "(tipos C e E)".

## Scripts e comandos usados (todos só de leitura)

- `python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd`, rodado duas vezes: às 18h33, OK com 8.498 palavras e sem mudança no `git status` antes e depois; às 18h40, depois das edições do outro processo, OK com 8.493 palavras.
- `pdftotext -layout docs/revisao.pdf` e `pdftotext docs/revisao.pdf`, com saída no *scratchpad*, e `pdfinfo`.
- `git diff v3-final-2026-10-01 -- <arquivos do prompt>`, `git diff HEAD --stat`, `git log`, `git tag`, `git show v3-final-2026-10-01:06-analise/caixa_ferramentas.csv` e `git ls-remote --tags origin`.
- `unzip -l docs/pacote-replicacao.zip` e extração no *scratchpad*, com `cmp` dos arquivos do pacote contra as fontes: checklists, LEIA, `emendas.md` e declaração de IA são idênticos às fontes.
- Python *inline*, sem escrita no projeto, para:
  - ler `rs_log.jsonl` (seq 835 a 874; aberturas e fechamentos de pendências, portões, `rob_consolidado`, `dedup_executado` e `triagem_consolidada.absorvidos_dedup`) e `rs_estado.json` (42 pendências);
  - ler `dados/decisoes.jsonl` (6.511 decisões; 336 com revisor `ia_coordenador_emenda6`) e os `certeza*.csv` (SHA e `validado_humano`);
  - ler `caixa_ferramentas.csv`, `triagem_ta_final.csv`, `elegibilidade_tc_final.csv`, `incluidos.csv` e `sem_resumo_revisao/registros_336.csv`;
  - extrair o texto visível de `docs/index.html` e de `docs/linguagem-simples.html`.
- Um *script* próprio no *scratchpad* da sessão, fora do repositório: `conferir_fluxo_emenda8.py <raiz> <scratchpad>`. Ele lê os números esperados de `prisma_contagens.json` e `numeros_v2.json` e procura números antigos (342, 526, "46 e 4", "148 e 648", 1.573, 1.054, 1.314, 787, "158 das bases", "184 dos outros", 3.423) e frases proibidas ("não aplicad", "gravados sem aplicação", "P019 fica aberta", 01/10/2026, "conferiu a triagem", "conferiu em bloco a busca") no artigo, nos apêndices, na linguagem simples, nas legendas, na vitrine, no README, nos LEIAs, no texto do PDF, nos HTML e nos `.md` do pacote.

## Correções aplicadas pelo coordenador de IA (30/09/2026, depois desta verificação)

- **E1:** `montar_suplemento.s2_atalhos` tira os não recuperados por ramo de `prisma_contagens.json` (155 e 183); `docs/` refeito.
- **E2, E3 e A7:** `insumos/tabelas/checklist_prisma2020.md` (itens 8 e 16a), `checklist_prisma_s.md` (item 16) e `checklist_trAIce.md` (A1, M1 e M8) com o texto sugerido.
- **E4:** opção (b), porque o autor ainda não leu a versão posterior à Emenda 8: 2.9, 4.4 e a linha "Relato" do Apêndice G dizem que ele leu e aprovou esta versão "antes da Emenda 8", e a aplicação da Emenda 8 foi pedida por ele. Se o autor aprovar a versão final, a declaração é registrada e os três trechos voltam a "antes da entrega".
- **E5:** `declaracao_ia_v2.md` com "versão de entrega de 30/09/2026, Emendas 7 e 8".
- **A1:** a tag `v3-final-2026-09-30` é criada no commit final, com a autorização do autor para o *push*.
- **A2:** 3.1, legenda e caixa da figura do PRISMA e caixa do PRISMA da vitrine, com o texto sugerido.
- **A3:** linha da Emenda 8 no Apêndice B ("8a: correção da ferramenta, sem nova decisão de método; 8b: depois de ver os dados") e "Cinco ressalvas", com o item (v).
- **A4, A5, A10, O1, O3, O4, O5 e O9:** com o texto sugerido.
- **A6 e O10:** notas na declaração de 30/09/2026, no LEIA do pacote e no LEIA da P019.
- **A8:** "01/10/2026" saiu de `DATAS_FIXAS` e da `spec_final.md`; `teste_travas.sh` OK.
- **A9:** o `CLAUDE.md` já tinha sido atualizado no commit `aa31429`; a leitura foi anterior.
- **Sem mudança:** O2, O6, O7 e O8 (ressalvas sem correção pedida).

Depois das correções, a trava deu OK, com 0 falhas, 0 avisos e 8.492 palavras no corpo.
