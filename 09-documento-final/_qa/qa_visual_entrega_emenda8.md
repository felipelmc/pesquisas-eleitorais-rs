# Revisão visual do PDF de entrega (Emenda 8)

PDF revisado: `docs/revisao.pdf`, 51 páginas A4. As páginas 1 a 11 e 14 a 30 (artigo) estão em pé, as páginas 12 e 13 (Tabela 2) estão deitadas, e as páginas 31 a 51 (apêndices A a G) também. O arquivo foi gerado pelo Typst 0.14.2 e juntado pelo pypdf em 30/09/2026 às 21:19. As páginas foram rasterizadas a 110 dpi, e as Tabelas 2 e G1, a Figura 2 (PRISMA), a legenda da Figura 4 e o Apêndice A foram ampliados a 160–200 dpi. Os corpos e as fontes foram medidos com o PyMuPDF.

Legenda: **corrigir** é defeito que um diagramador de revista não deixaria passar; **aceitável** pode ficar, com ajuste opcional.

## O que foi conferido e está certo

- **Primeira página.** Traz o título, o subtítulo (com *bandwagon* e *underdog* em redondo dentro do itálico, o que está certo), o autor e a afiliação, as datas da busca, a nota de IA e a data 30/09/2026 no sobretítulo.
- **Paginação e cabeça.** A numeração vai de 1 a 51 sem saltos, e os apêndices começam na p. 31. A cabeça corrente "Lamarca · Pesquisas eleitorais e voto", com filete, aparece em todas as páginas a partir da 2, em pé e deitadas.
- **Rascunho.** Não há marca-d'água nem cabeçalho de rascunho. "RASCUNHO NÃO VALIDADO" aparece uma vez só, na p. 25.
- **Marcadores e metadados.** Os marcadores do PDF (sumário) batem com as seções, e os metadados (título, autor, palavras-chave) estão preenchidos.
- **Números do fluxo.** Conferem entre o Resumo, o Abstract, a seção 3.1, a Figura 2, a seção 4.4 e a Tabela G1: 1.767 − 91 − 143 = 1.533; 1.706 − 17 − 639 = 1.050; 256 − 155 = 101; 266 − 183 = 83; 42 + 13 = 55 relatos; 338 de 522. Os motivos de exclusão da Figura 2 também somam: 39 + 10 + 8 + 2 = 59 e 50 + 13 + 4 + 3 = 70.
- **Passagens alteradas nesta versão.** O δ na seção 2.7 e no Quadro 1 é coerente entre os dois lugares. A lista das Informações adicionais tem mesmo onze desvios, de (i) a (xi). A legenda da Figura 2 e a linha "Deduplicação" da Tabela G1 estão sem defeito de composição.
- **Figuras.** São todas vetoriais, com corpo mínimo de 7,0 pt e sem sobreposição de rótulos. O único texto em 6,5 pt é o código inline das tabelas B1 e G1 (ver aceitável 13).
- **Tabela 2.** As linhas de grupo ocupam a largura toda, e as notas ficam dentro da tabela, em sans.
- **Legendas e nomes.** As legendas das tabelas ficam em cima e as das figuras embaixo, sem legenda separada do seu objeto. Os sobrenomes dentro das citações do corpo não são mais hifenizados.

## A corrigir (13)

1. **p. 11: cerca de 35% da página em branco abaixo da Figura 3, antes das páginas deitadas da Tabela 2.** A página deitada força a quebra, e o texto que vem depois do marcador `@@TABELA sof@@` só aparece na p. 14: é o parágrafo "A Figura 4 mostra…" mais a seção 3.4.
   *Correção (texto):* no `_esqueleto_revisao_final.qmd`, levar `@@TABELA sof@@` (hoje na linha 252, logo depois do primeiro parágrafo da 3.3) para depois do segundo parágrafo da 3.4, ou para o fim da 3.4. O texto então preenche a p. 11, e a Tabela 2 continua a uma página da primeira chamada. Depois, confira onde a Figura 4 (flutuante) cai.

2. **p. 15: uma linha só de texto no pé da página, abaixo da Figura 4.** A linha é "da exposição. A proporção ficou em 0,50 (IC 95% 0,01 a 0,99; p = 1). A evidência é muito incerta". Com isso, o parágrafo sobre boca de urna fica partido em três páginas (14, 15 e 16).
   *Correção:* abrir espaço para pelo menos três linhas. Na `revista/figuras/legendas.yml`, encurte a legenda de `direcao`, que tem sete linhas. Saem "O tamanho do símbolo é constante porque os estudos medem em unidades diferentes" e "O risco de viés usa os símbolos do robvis…", que já estão na legenda da Figura 3. Outra saída é baixar 8 a 10 mm da altura da figura em `figuras/gerar_figuras.R`. Confira de novo depois do item 1, porque o fluxo muda.

3. **p. 20: cerca de 40% da página em branco depois da seção 3.10.** A Figura 6 (`realismo`) está com `largura: texto`, então não flutua e desce inteira para a p. 21, levando junto o texto seguinte. É também a única figura com legenda e desenho na largura do texto: as Figuras 1 a 5 são largas.
   *Correção (legenda):* em `revista/figuras/legendas.yml`, trocar `realismo: largura: texto` por `largura: larga`. A figura vira `figura-larga` (`place(auto, float: true)`), o texto seguinte sobe para a p. 20, e a largura fica igual à das outras figuras.

4. **p. 12–13: "n = x" quebrado na linha, na coluna "Estudos" da Tabela 2.** Os casos são "Timotei (2013), n / = 80 respondentes", "Cornejo (2023), n = / 545 respondentes", "Chatterjee e Kamal (2019), n = / 1.737 distritos" e "Brugarolas e Miller (2021), n / não relatado".
   *Correção:* em `montar_revisao_final.estudos_sof`, usar espaço inseparável: `f"@{chave}, n = {pt(n)}"` e `"n não relatado"`.

5. **p. 34: número desatualizado na Tabela B2, linha A5.** A tabela diz "Os relatos não recuperados ficam fora: 158 das bases e 184 dos outros métodos", o que soma 342. A Figura 2, a seção 3.1, o Resumo, o Abstract e a seção 4.4 dizem 155 e 183 (338 de 522), depois da Emenda 8. A frase vem de `insumos/garritty_2024.md` (de 24/09) sem troca.
   *Correção:* em `montar_suplemento.s2_atalhos`, acrescentar à tupla de trocas `("158 das bases e 184 dos outros métodos", "155 das bases e 183 dos outros métodos")`. Melhor ainda é derivar os dois números de `prisma_contagens.json`, sem editar o insumo, como já se faz com a Emenda 7. Vale também uma trava que procure "158"/"184" no `suplemento.qmd`.

6. **p. 35–36: a Tabela B4 (emendas) deixa só a linha da Emenda 8 na p. 36, que fica cerca de 85% em branco.** É efeito direto da Emenda 8.
   *Correção:* em `montar_suplemento.s3_emendas`, rebalancear as larguras de `[9, 9, 20, 16, 16, 18, 12]` para cerca de `[7, 7, 19, 15, 15, 17, 20]`. A coluna "Reexecução exigida" quebra hoje em quatro a cinco linhas nas Emendas 2, 6 e 7, enquanto "Emenda" e "Data" sobram. Com isso, a tabela deve caber inteira na p. 35. Se não couber, encurte o parágrafo de abertura de "Emendas e desvios do protocolo", que repete a legenda.

7. **p. 37–38: citações truncadas na coluna "Estudo (relatos adicionais)" da Tabela C1.** Em todas as linhas com relato adicional, a citação sai deformada:
   - "(Agranov et al. 2012, 2017; Agranov et al.)";
   - "(Alabrese 2022; Alabrese e Fetzer; 2024)";
   - "(Stolwijk 2017; Stolwijk, Schuck, e de Vreese; 2016)";
   - "(Fairstein et al. 2018, 2019; Tal, Meir, e Gal; 2015)";
   - o mesmo em Bursztyn, Dahlgaard, Gerber e Morton.

   O insumo `insumos/tabelas/caracteristicas.md` escreve `@Agranov2017a [@Agranov2012a]`, e o Pandoc lê o colchete como localizador ou sufixo da citação narrativa.
   *Correção:* em `montar_suplemento.s4_caracteristicas`, reescrever o padrão `@X [@Y; @Z]` como `@X; relatos adicionais: @Y; @Z`, ou como `@X (e [-@Y]; [-@Z])`, e ajustar a legenda ("relatos adicionais depois do ponto e vírgula").

8. **p. 50–51: a p. 51 existe só para as cinco linhas de "Agentes desta versão"; cerca de 80% dela fica em branco.** É daí que vem a passagem de 50 para 51 páginas: a linha "Deduplicação" da Tabela G1 cresceu e empurrou a subseção. A Tabela G1 também é uma das poucas tabelas grandes dos apêndices que ficam na largura do texto.
   *Correção:* em `montar_suplemento.lacunas()`, envolver a tabela em `envolver("tabela-larga", …)` e, em `revista/tabelas/lacunas.yml`, trocar `larguras: [13, 23, 23, 29, 12]` por cerca de `[11, 23, 21, 36, 9]`, porque a coluna "Pendência aberta" só tem textos curtos. Tire da legenda a frase que repete o parágrafo de abertura do Apêndice G ("a declaração foi transcrita pelo coordenador de IA…"). Assim, "Agentes desta versão" volta para a p. 50, e o PDF volta a ter 50 páginas.

9. **p. 50, e também p. 6: nomes de modelo em fonte mono quebrados no hífen.** Na linha "Busca" da Tabela G1, o texto termina em "claude-opus-5-" e o "5" fica sozinho na linha seguinte. Há ainda "claude-/opus-5-5" e "claude-/sonnet-5" na mesma tabela, e "claude-sonnet-/5" e "claude-opus-/5" na seção 2.4.
   *Correção (template):* no `typst-template.typ`, `show raw.where(block: false): it => box(it)`. Os identificadores têm 13 a 15 caracteres e cabem em qualquer coluna.

10. **p. 25: título corrido fora do padrão.** "Declaração de uso de inteligência artificial." fica sozinho numa linha, e "RASCUNHO NÃO VALIDADO." abre um parágrafo recuado. Os outros títulos corridos das Informações adicionais ("Diferenças entre protocolo e síntese.", "Registro e protocolo.", "Versão e citação." etc.) abrem o próprio parágrafo.
    *Correção (texto):* no `_esqueleto_revisao_final.qmd`, linhas 424 e 426, juntar tudo num parágrafo só: `**Declaração de uso de inteligência artificial.** **RASCUNHO NÃO VALIDADO.** Ficaram sem validação…`. A expressão continua uma vez só e na abertura da declaração. Rode `conferir_reestruturacao.py` para confirmar a trava.

11. **Artigo, figuras e apêndices: vírgula antes do "e" final nos nomes.** Aparece em citações e referências: "Tal, Meir, e Gal 2015", "Lago, Guinjoan, e Bermúdez", "van der Meer, Hakhverdian, e Aaldering", "Agranov, Marina, …, e Leeat Yariv". Em português não se usa vírgula antes do "e" final de uma enumeração. Isso aparece dezenas de vezes, inclusive nos rótulos das Figuras 4 e 5.
    *Correção (CSL):* em `revista/american-political-science-association.csl`, `delimiter-precedes-last="never"` nas macros `author` (hoje `always`), `author-short` e `editor`. Depois, rode `gerar_rotulos_autor_ano.py` e `figuras/gerar_figuras.R`, porque os rótulos das figuras vêm das mesmas citações.

12. **p. 31–32 (Apêndice A): strings de busca justificadas e recuo irregular.**
    - Os blocos de código (Skylighting) herdam `justify: true`. Na última linha da p. 31, antes da quebra, os espaços entre `OR "encuestas electorales" OR …` ficam visivelmente esticados.
    - As entradas paralelas têm recuo diferente: B01, SN2 e SN3 têm recuo de primeira linha; B02 a B05 e SN1, que vêm depois de um bloco de código, não têm.

    *Correção (template):* `show block.where(fill: rgb("#f1f3f5")): set par(justify: false)`, que é o fundo do bloco de código do Quarto. Outra opção é emitir as strings numa div `.estrategia`, que o `inline.lua` transforma em bloco com `par(justify: false)`. Para o recuo, `montar_suplemento.s1_busca` pode envolver as entradas numa div que zere `first-line-indent`, ou separá-las com espaço vertical.

13. **p. 42: o cabeçalho "Geral" da Tabela D3 hifenizado ("Ge-/ral").** A última coluna tem 3% da largura.
    *Correção:* em `montar_suplemento.py` (tabela `tbl-s5-epoc`), trocar as larguras de `[10, 7] + [5] * 16 + [3]` para `[9, 7] + [5] * 16 + [4]`.

## Aceitáveis (15)

1. **p. 1: "IA." sozinho na última linha da nota de IA** ("…Ver a declaração de uso de / IA.").
   *Sugestão:* em `revista/_revista.yml`, `nota-ia`, pôr espaço inseparável em "uso de IA" ou encurtar para "Ver a declaração de IA".

2. **p. 2: pontos a confirmar.**
   - "Em 24/09/2026, nenhum dos dois tinha sido votado em plenário." A data não acompanha a versão de 30/09. Se a tramitação dos PLs foi conferida de novo, atualize a data; se não, está certa como data de verificação.
   - Na mesma página, "Lei nº / 11.300/2006" quebra entre "nº" e o número.

   *Sugestão:* espaço inseparável em "nº 11.300/2006" no esqueleto.

3. **p. 3–4: o Quadro 1 começa no pé da p. 3 com uma linha só ("Como ler").** O cabeçalho se repete na p. 4, então a leitura não se perde.
   *Sugestão:* subir o marcador do Quadro 1 um parágrafo, ou deixar pelo menos duas linhas juntas com o cabeçalho.

4. **p. 4 (Quadro 1, linha do δ) e p. 7 (seção 2.7): frase do δ longa e ambígua.** A oração "fixados pela Emenda 5 […] em vez da mediana de cada célula que o protocolo pede, e 0,0573 na célula principal…" dá a entender que 0,0573 faz parte do "em vez de". A composição está certa; o problema é de leitura.
   *Sugestão (texto):* "…: 0,044 no apoio e 0,046 no comparecimento, com a proporção de referência padrão, e 0,0573 na célula principal (…), com a mediana do grupo de comparação; a Emenda 5 fixou esses valores em vez da mediana de cada célula que o protocolo pede." Rode `conferir_numeros.py` depois.

5. **p. 9 (Figura 2): a caixa final diz "Estudos incluídos na revisão (n = 41)", mas o produto se chama "síntese" (R7.28).** O PRISMA admite adaptar o rótulo.
   *Sugestão:* "Estudos incluídos na síntese" no gerador da figura. A legenda tem dez linhas e repete parte dos Métodos; pode ser cortada, se quiser.

6. **p. 10 (Tabela 1): categorias de risco de viés em ordem de frequência, não de gravidade.** No ROBINS-I, a ordem sai "grave, crítico, moderado".
   *Sugestão:* ordenar moderado, grave e crítico (e baixo, algumas preocupações e alto) no gerador da tabela `caracteristicas`.

7. **p. 17: parágrafo que começa com minúscula ("van der Meer, Hakhverdian, e Aaldering (2015) (survey…").**
   *Sugestão (texto):* reescrever para não abrir a frase com a partícula (por exemplo, "No *survey* holandês de van der Meer…").

8. **p. 24: na lista dos onze desvios, o item (ix), "outros", fica entre a Emenda 6 e a Emenda 7 e quebra a ordem cronológica.**
   *Sugestão (texto):* passar "outros" para o fim, como item (xi). A contagem de onze continua a mesma.

9. **p. 29: dois problemas de quebra nas referências.** O DOI de Rethlefsen quebra deixando "z." sozinho na linha, e "Multi-/-Winner" repete o hífen (regra do português aplicada a um título em inglês).
   *Sugestão:* nenhuma obrigatória. Se incomodar, use `lang: "en"` nos títulos em inglês da bibliografia.

10. **p. 33–39 e 50: a largura das tabelas dos apêndices varia.**
    - B1, B2, B4, C1, D1 a D3, E1, E2, F1 e F2 vão até cerca de 1 cm da borda do papel;
    - B3, C2 e G1 ficam na largura do texto (na p. 34, B2 e B3 estão lado a lado com larguras diferentes).

    *Sugestão:* `envolver("tabela-larga", …)` também em B3 (`tbl-s2-outras`) e C2 (`s4_excluidos`). A G1 já está no item 8 da lista a corrigir.

11. **p. 40 e 43–49: quebras repetidas em colunas estreitas.**
    - "algumas preocupa-/ções†" (D1);
    - "não (fora da conta-/gem)" (E1, coluna de 10% ao lado de "Outra medida", que tem 24% e sobra);
    - "sem GRADE pró-/prio" (F1);
    - sobrenomes nas colunas de estudo ("Wojcie-/chowski", "Hakhver-/dian", "Ber-/múdez"), porque ali o nome é texto, não citação, e o `hyphenate: false` não se aplica.

    *Sugestão:* passar a E1 para `[14, 6, 9, 10, 13, 14, 20, 14]`, alargar "Certeza" na F1 e usar `hyphenate: false` na primeira coluna das tabelas dos apêndices.

12. **p. 46: "idem à linha anterior" na primeira linha da página, remetendo à linha no pé da p. 45 (Tabela E2).**
    *Sugestão:* escrever o motivo por extenso em vez de "idem" no gerador da Tabela E2.

13. **p. 33 e 50: código inline em 6,5 pt nas tabelas** (`claude-sonnet-5`, `verificar-efeitos`, `apoio_ao_lider`). Está no limite da legibilidade, mas é legível.
    *Sugestão:* `show raw` com `size: 0.92em` dentro de tabelas, se quiser.

14. **p. 2: "en bloc" em redondo no Abstract** ("selection and extraction en bloc"). No resto do texto, os termos estrangeiros vão em itálico.
    *Sugestão (texto):* `*en bloc*` no Abstract.

15. **Páginas com vazio natural.** Estes vazios são esperados e não pedem ação:
    - p. 13 (fim da Tabela 2);
    - p. 30 (fim das referências, antes dos apêndices deitados);
    - p. 32, 39, 42 e 46 (fim de apêndice, porque cada apêndice abre página nova);
    - p. 36 e 51, que ficam normais depois dos itens 6 e 8 da lista a corrigir.

## Avaliação geral

Sim, o PDF parece um artigo de revista acadêmica bem diagramado: a primeira página é completa, a tipografia é consistente, as figuras vetoriais e as tabelas são legíveis, e os números do fluxo PRISMA conferem em todos os lugares. Para chegar à versão de gráfica faltam três vazios de página no artigo (p. 11, 15 e 20), as duas páginas quase vazias criadas pela Emenda 8 (p. 36 e 51), a citação deformada na Tabela C1 e o número defasado (158/184) na Tabela B2, e tudo isso se corrige nos geradores e no template, sem mexer na análise.

## Correções aplicadas pelo coordenador de IA (30/09/2026)

- **A corrigir, feitos:** 1 (marcador da Tabela 2 depois do segundo parágrafo da 3.4), 2 (legenda da Figura 4 encurtada), 3 (Figura 6 larga, desenhada a 168 mm), 4 (espaço inseparável em "n = x" e "n não relatado"), 5 (não recuperados da Tabela B2 lidos de `prisma_contagens.json`), 6 (larguras da Tabela B4), 7 (relatos adicionais da Tabela C1 depois de "também"), 8 (Tabela G1 larga, larguras e legenda mais curta), 9 (código inline de até 30 caracteres numa caixa, sem quebra no hífen), 11 (CSL sem vírgula antes do "e" final; rótulos e figuras refeitos), 12 (blocos de código sem justificar; parágrafos dos apêndices sem recuo de primeira linha) e 13 (larguras da Tabela D3).
- **A corrigir, não feito:** 10. A `spec_final.md` (IA-7) pede o rótulo da declaração de IA numa linha e o parágrafo seguinte aberto por "RASCUNHO NÃO VALIDADO".
- **Aceitáveis, feitos:** 1 (espaço inseparável em "uso de IA"), 2 (espaço inseparável em "nº 11.300/2006"; a data de 24/09 é a da verificação dos projetos de lei e fica), 4 (frase do δ reescrita), 5 ("Estudos incluídos na síntese" na figura e na vitrine), 7 (parágrafo de van der Meer sem abrir com minúscula) e 14 (*en bloc* em itálico).
- **Aceitáveis, deixados como estão:** 3, 6, 8, 9, 10, 11, 12, 13 e 15.
