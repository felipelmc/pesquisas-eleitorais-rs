# Revisão visual do PDF do artigo (etapa 8)

PDF revisado: `09-documento-final/revisao_final.pdf`, 39 páginas (A4; 15 a 17 deitadas), gerado pelo Typst 0.14.2 em 24/09/2026 às 16:59. As páginas foram rasterizadas a 110 dpi, e as figuras foram ampliadas a 200 dpi. Durante a revisão, o `docs/publicar.sh` moveu o arquivo para `docs/revisao.pdf`. A medição de corpos e fontes usou uma cópia desse arquivo, com a mesma data de criação.

Legenda: **corrigir** = defeito que um diagramador de revista não deixaria passar; **aceitável** = pode ficar, com ajuste opcional.

## A corrigir (19)

1. **p. 4, 11, 18 e 20: vazios grandes no pé da página.** Sobram 36%, 55%, 31% e 26% da mancha em branco, porque as figuras largas (Figuras 1, 2, 5 e 6) não flutuam e vão inteiras para a página seguinte. O texto que vem depois delas poderia preencher o vazio.
   *Correção:* no template, separar figura larga de tabela larga. Em `inline.lua`, `.figura-larga` passa a gerar `#figura-larga[...]` e `.tabela-larga` continua `#largura-total[...]`. No `typst-template.typ`: `#let figura-larga(body) = place(auto, float: true, clearance: 1.4em, pad(x: -14mm, body))`. Tabelas largas não flutuam, porque as Tabelas 3 e 5 ocupam duas páginas. Conferir depois se a Figura 2 (PRISMA) continua perto da primeira citação.

2. **p. 5, 12, 19, 21 e 32 (abaixo) e p. 18, 25 e 31 (acima): figura ou tabela larga colada no texto.** Entre a legenda e o parágrafo seguinte, o espaço é o de um parágrafo comum (cerca de 0,6 em). O `pad` descarta o `above`/`below: 1.4em` da figura. Nas figuras de largura normal (Figura 7, p. 27), o respiro está certo.
   *Correção:* `#let largura-total(body) = block(above: 1.4em, below: 1.4em, pad(x: -14mm, body))`, e o mesmo respiro na `figura-larga` do item 1, se ela não flutuar.

3. **p. 2–3: o bloco RESUMO quebra na página.** Ficam quatro linhas na p. 2, e o corte cai no meio de "Métodos." ("…na BDTD / e por citação").
   *Correção:* `breakable: false` em `#let resumo` (Resumo e Abstract cabem cada um numa página). Outra opção é pôr Resumo e Abstract logo depois do bloco de título, como em revista (ver aceitável 10).

4. **p. 12: a Tabela 1 começa órfã no pé da página.** Ficam a legenda, o cabeçalho e só a linha de grupo "Desenho"; a tabela segue na p. 13.
   *Correção:* a Tabela 1 cabe numa página. Deixá-la inteira e flutuante, com `placement: auto` por uma classe no `inline.lua` (por exemplo `.tabela-inteira` → `#figure(placement: auto, ...)` ou `block(breakable: false)`). O texto "Dos 41 estudos, 27 entram…" sobe para a p. 12.

5. **p. 38–39: a legenda da Tabela 6 fica no pé da p. 38, e a tabela começa na p. 39.**
   *Correção:* no `show figure.caption` do template, quando a legenda vai no topo (`it.position == top`), envolvê-la em `block(sticky: true)[...]`. Assim ela acompanha o começo da tabela. Isso também reforça o item 4.

6. **p. 5–7: a legenda dos Quadros fica embaixo, e a das Tabelas em cima.** O Quadro 1 abre na p. 5 sem rótulo, e a legenda só aparece no fim, na p. 6. O Quarto grava `figure.caption(position: bottom)` explícito, que passa por cima do `set figure.caption(position: top)` do template.
   *Correção:* em `revista/_revista.yml`, acrescentar `qdr-cap-location: top`, ou `caption-location: top` na entrada `crossref.custom` de `qdr`.

7. **p. 15–16: na Tabela 2, as linhas de grupo ficam presas à primeira coluna (15%).** "Viabilidade: apoio à op-/ção mostrada como viá-/vel" e "*Momentum*: partido mos-/trado ganhando ou per-/dendo apoio" ocupam três linhas hifenizadas, com cinco células vazias ao lado.
   *Correção:* no gerador da tabela, `table.cell(colspan: 6)[#strong[…]]` nas linhas de grupo (mesma coisa na Tabela 1, p. 12–13, por consistência).

8. **p. 17: página deitada quase vazia (cerca de 75% em branco), só com as *Notas* da Tabela 2.** As notas também saem em serifa de 10 pt, o corpo do texto, e não no corpo da tabela (sans 7,6 pt).
   *Correção:* pôr as notas dentro do `figure` da tabela, em sans 7,6 pt, com uma classe `.nota-tabela` ou como última linha `table.cell(colspan: 6)`. Para caberem na p. 16, compactar a Tabela 2: `inset: (x: 3.5pt, y: 2.2pt)` e `leading: 0.4em` só nela. Outra saída é encurtar a legenda da p. 15, que tem quatro linhas, e levar a explicação dos símbolos GRADE para as notas.

9. **p. 15, 16 e 20–22: itálico inconsistente em *bandwagon* e *momentum*.** Na Tabela 2, a coluna "Direção" usa itálico, e a coluna "O que a evidência diz" usa redondo: "na direção bandwagon", "(momentum; 1 estudo…)". No corpo do texto, os enunciados padronizados também saem em redondo ("4 de 4 estudos na direção bandwagon", p. 20; "3 de 3 efeitos na direção bandwagon", p. 21; "(momentum; 1 estudo…)", p. 22), ao lado de *bandwagon* em itálico na mesma frase.
   *Correção (texto):* italicizar os termos dentro dos spans `.enunciado` do `_esqueleto_revisao_final.qmd` e no gerador da Tabela 2. Antes, confirmar que `conferir_numeros.py` compara o texto com `stringify`, que ignora a ênfase.

10. **p. 15–16: na coluna "Estudos" da Tabela 2, o n entra no link da citação.** "Agranov et al. 2017, 300 eleições de grupo", "Farjam 2020, 1.113 participantes", "Dahlgaard et al. 2016, 1.700": o número sai azul e parece localizador de página. Em outras linhas, o n fica fora ("Witsman 2016, n = 142").
    *Correção (texto/gerador):* escrever o n fora do colchete da citação e sempre no mesmo formato, por exemplo `[@Agranov2017a]: n = 300 eleições de grupo`.

11. **p. 10, 14–16, 24–27 e 31–32: nomes próprios hifenizados nas citações.** Entre eles, "Sch-ram" (p. 16 e 31), "Gs-chwend" (p. 25), "Vre-ese" (p. 26), "Sto-etzer" (p. 25), "Puste-jovsky" (p. 10), "Un-kelbach" (p. 24), "Unkel-bach" (p. 26), "Ti-motei" e "Fre-dén" (p. 15), "Hakh-verdian" e "Bru-garolas" (p. 16), "Ber-múdez", "Ka-plan", "Gas-peroni" (p. 25), "Wits-man" (p. 27), "Wojcie-chowski" (p. 14 e 25) e "Gio-vannoni" (p. 31). Os padrões do português cortam sobrenomes alemães, holandeses e poloneses em sílabas erradas.
    *Correção:* no `inline.lua`, uma função `Cite(el)` que devolve `{RawInline("typst", "#text(hyphenate: false)["), el, RawInline("typst", "]")}`. Nas citações entre parênteses, `show link: set text(hyphenate: false)` já basta.

12. **p. 8, 9, 33, 34 e 39: código, nomes de modelo e caminhos hifenizados.** "claude-/-opus-5-5" (p. 8 e 9) e "claude-/-sonnet-5" (p. 9) repetem o hífen, à portuguesa, dentro de um identificador. "claude-son-/net-5" (p. 34) e "feli-/pelmc/…" (p. 33) recebem hífen que não existe. Na Tabela 6 (p. 39), "08-re-/visao-humana/", "P006_P007_vali-/dacao/", "P041_elegibili-/dade/", "P037_concordan-/cia/" e "07-relatorio/re-/latorio.html" alteram o caminho que o revisor vai digitar.
    *Correção:* no `inline.lua`, função `Code`, gerar `#text(font: ..., size: 0.86em, lang: "en", hyphenate: false, "...")`. Os pontos de quebra (U+200B) depois de `/ _ .` continuam. Se precisar, acrescentar U+200B depois de `-`, sem repetir o hífen.

13. **p. 34–38: URLs e DOIs das Referências quebram com hífen repetido.** Exemplos: "pedido-de-/-criacao-de-cpi" (p. 34), "freedom-to-conduct-and-publish-opinion-polls-july-/-2023.pdf" (p. 35), "Systematic-/-Review/" (p. 36), "s13643-020-01542-/-z" (p. 37), "direto-do-/-plenario", "tse-explica-a-/-partidos", "republicacao-resolucao-no-23-600-de-12-de-dezembro-de-2019-dispoe-sobre-/-pesquisas-eleitorais" (p. 38). Quem copia o endereço lê "--".
    *Correção:* `show link: set text(lang: "en", hyphenate: false)` no template. Com `lang: "en"`, o Typst não repete o hífen.

14. **p. 1: título com viúva.** "Pesquisas eleitorais publicadas mudam o / voto?" deixa uma palavra só na segunda linha do título de 19 pt.
    *Correção:* no bloco de título do template, `block(width: 80%)[#text(... 19pt ...)[#title]]`, que quebra em "Pesquisas eleitorais publicadas / mudam o voto?".

15. **p. 18: a Figura 4 usa cor sem explicar.** Os pontos e ICs são azuis (maioria a favor), laranja (maioria contra) ou cinza (empate, boca de urna 1 de 2). A legenda do gráfico só explica a forma (classe de desenho), e a legenda escrita não fala da cor.
    *Correção:* acrescentar a chave de cor ao gráfico (`gerar_figuras.R`) ou uma frase na legenda (`figuras/legendas.yml`): "Azul: maioria dos estudos a favor; laranja: maioria contra; cinza: empate."

16. **p. 19: a Figura 5 rotula o estudo brasileiro como "Araujo e Gatto (2021b)".** No texto, nas Tabelas 2 e 5 e na Figura 4 (via texto), o mesmo estudo é "2021a". O `rotulos_autor_ano.json` mapeia `Araujo2021a` → "Araujo e Gatto 2021b", fora de sincronia com as letras que o citeproc atribui.
    *Correção:* refazer `gerar_rotulos_autor_ano.py` para seguir o sufixo do citeproc (`Araujo2021a` → 2021a) e regenerar as figuras.

17. **p. 17, 23, 25–27, 29 e 30: citações entre parênteses aninhados (24 ocorrências).** Exemplos: "(Kaplan (2019))", "(Gandhi e Ong (2019))", "(Gerber et al. (2020))", "(Tyszler e Schram (2015); Tal, Meir, e Gal (2015))", "(Farjam (2020))", "(Araujo e Gatto (2021a))", "(Cor-nejo (2023))". São 5 na Tabela 3 (p. 25) e 7 na p. 26.
    *Correção (texto):* dentro de parênteses, trocar `@chave` por `[@chave]` (ou juntar a citação ao parêntese: "(Kaplan 2019)"), no esqueleto e nos geradores das Tabelas 2, 3 e 4.

18. **p. 36–37: data de acesso posterior à data do documento.** "Lamarca, Felipe. 2026. Revisão sistemática de ponta a ponta … (25 de setembro de 2026)" e "Sterne, Higgins, e ROBINS-I V2 development group. 2025 … (25 de setembro de 2026)". O documento é de 24/09/2026, e as demais referências têm acesso em 24 de setembro.
    *Correção:* em `revista/referencias.json`, `accessed` = 2026-09-24 nas duas entradas.

19. **p. 25–26: a linha E4 da Tabela 3 se parte entre as páginas.** A cauda da célula "Estudos que testam com dados" ("2015; Timotei 2013; Unkel-/bach, John, e Vogel 2022)") fica sozinha no topo da p. 26, sob o cabeçalho repetido.
    *Correção:* no template, `set table.cell(breakable: false)` (Typst ≥ 0.12). A linha inteira passa para a p. 26.

## Aceitáveis (12)

1. **p. 1: subtítulo hifenizado ("não vali-/dada").** *Sugestão:* `hyphenate: false` no `text(...)` do subtítulo.
2. **Marca-d'água "RASCUNHO NÃO VALIDADO", em todas as páginas.** É clara (vermelho a 94% de transparência) e não atrapalha a leitura, nem nas tabelas deitadas. Some sob os fundos das caixas de Mensagens, Resumo e Abstract (p. 1–3), porque vai no `background`. É inconsistente, mas inofensivo.
3. **Figuras 1, 2, 3, 5 e 6 e Tabelas 3 e 5 avançam 14 mm nas margens (p. 5, 12, 14, 19, 21, 25 e 31).** O avanço é simétrico e intencional (`largura-total`); a legenda acompanha a largura. A Figura 7 fica na largura da mancha, o que é coerente com o conteúdo dela.
4. **Corpo mínimo das figuras, no limite de 6,5 pt:** rótulos E1–E8 da Figura 1 (6,4 pt), "n = 23" da Figura 3 (6,4 pt), sinais de menos e "×" da Figura 5 (6,4 pt), "42 relatos"/"13 relatos" da Figura 2 (6,45 pt) e caminhos em mono da Tabela 6 (6,5 pt). Tudo é legível a 100%, sem sobreposição de rótulos. *Sugestão:* subir para 7 pt em `tema_revista.R`.
5. **Letras de painel (a, b, c) desalinhadas do título do painel nas Figuras 3, 5 e 6 (p. 14, 19 e 21).** A letra fica meia linha acima ou numa linha própria. *Sugestão:* `plot.tag.position`/`plot.tag` com `vjust` igual ao título, em `gerar_figuras.R`.
6. **p. 16: na célula de certeza da linha de Gerber, "⊕⊕⊕◯ mo-/derada" quebra dentro da palavra.** Nas outras linhas, os símbolos e o rótulo ficam em linhas separadas. *Sugestão:* quebra de linha fixa entre símbolos e rótulo em todas as células de certeza.
7. **p. 24: quebra dentro de expressão ("(p / = 0,008)").** *Sugestão:* espaço não separável em "p = …" no texto (`p~=~0,008`).
8. **p. 34: na bibliografia, "Araujo e Gatto 2021b" (preprint) vem antes de "2021a" (BJPolS).** *Sugestão:* dar mês de publicação às duas entradas em `referencias.json` para que ordem e sufixo coincidam.
9. **p. 38: o Apêndice A começa na mesma página do fim das Referências.** É aceitável num documento de trabalho; em revista, abriria página nova (`pagebreak(weak: true)` antes do apêndice).
10. **p. 1–3: Resumo e Abstract só aparecem depois das Mensagens principais e do Resumo executivo.** Isso serve a um documento de trabalho. Em revista, viriam logo abaixo do bloco de título.
11. **p. 5: na Figura 1, o nó "resposta ao survey" sai em redondo, e a legenda escreve *survey* em itálico.**
12. **p. 15, 16 e 25–26: "band-/wagon" e "momen-/tum" hifenizados em colunas estreitas.** Os cortes são corretos em inglês. *Sugestão:* `hyphenate: false` na regra `show regex(...bandwagon|underdog|momentum...)` do template.

## Conferido sem problema

As caixas "Pendente de revisão humana" (p. 1, 8, 9, 10, 14, 24, 25, 27, 31 e 32) e a caixa de rascunho da p. 1 não quebram entre páginas. Não há título de seção isolado no pé da página, nem viúva ou órfã de uma linha. Nenhuma tabela ou figura sai da página nem aparece cortada. A cabeça corrente ("Lamarca · Pesquisas eleitorais e voto" / "RASCUNHO NÃO VALIDADO") e a numeração "n / 39" estão presentes em todas as páginas, inclusive nas deitadas, e faltam só na p. 1, como deve ser. A p. 1 traz a faixa com a data, o título, o subtítulo, o autor e a filiação, a última busca, a nota de IA e o aviso de rascunho. Os corpos são coerentes: texto em serifa de 10 pt, tabelas em sans de 7,6 pt, legendas em sans de 7,9 pt, caixas entre 8,4 e 8,8 pt e referências em 8,8 pt. As tabelas longas repetem o cabeçalho.

## Avaliação geral

O PDF já parece um artigo acadêmico bem diagramado. A tipografia é coerente, as páginas deitadas e as tabelas longas estão bem resolvidas, as figuras são vetoriais e legíveis, e a primeira página tem tudo o que precisa. Ainda falta o acabamento de revista: as figuras largas não flutuam e deixam quatro vazios grandes, os blocos largos ficam colados ao texto, algumas legendas e cabeçalhos ficam órfãos, e há hifenização em nomes, códigos e URLs. Quase tudo se resolve no template e no `inline.lua`.
