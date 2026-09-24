# QA visual do PDF — `09-documento-final/suplemento.pdf`

Revisão página a página (33 páginas), rasterizadas a 110 dpi. Metodologia: leitura de cada
página como imagem, contra o checklist do prompt (margens, legibilidade, viúvas/órfãs,
páginas quase vazias, hifenização, caixas de aviso, legendas, marca-d'água, tipografia,
cabeçalhos/rodapé e primeira página).

## Lista de problemas

| # | Página(s) | O que está errado | Gravidade | Correção sugerida |
|---|-----------|--------------------|-----------|--------------------|
| 1 | 5 (antes da 6) | Depois do fim da Tabela 3, a página 5 fica cerca de 80% em branco antes de "S3 Emendas e desvios do protocolo" começar do zero na página 6. Não há página deitada nem outro motivo aparente para o salto. | corrigir | No `typst-template.typ`, revisar a regra de "manter junto" (`box`/`block` com `breakable: false` ou `keep-with-next`) que parece empurrar o bloco inteiro (título + parágrafo + tabela seguinte) para a próxima página quando não cabe por completo. Permitir que ao menos o título de seção e o parágrafo introdutório fluam na página corrente, mesmo que a tabela seguinte quebre. |
| 2 | 9 (antes da 10) | Após a última linha da Tabela 5 (que termina perto do topo da página 9), o restante da página fica em branco antes da Tabela 6 começar na página 10. | corrigir | Mesma causa do item 1: revisar o agrupamento de bloco table+legenda no template para não arrastar a página inteira em branco. |
| 3 | 10 (antes da 11) | A Tabela 6 ocupa só ~1/3 da página 10; o resto fica em branco antes de "S5 Risco de viés por domínio" começar na página 11. | corrigir | Mesma causa do item 1. |
| 4 | 13 (antes da 14) | Só uma linha residual da Tabela 9 aparece no topo da página 13; o restante (~85%) fica em branco antes de "S6 Efeitos principais por estudo" começar na página 14. | corrigir | Mesma causa do item 1; caso mais extremo da série (linha solta seguida de página quase vazia). |
| 5 | 17 (antes da 18) | A Tabela 11 termina por volta de 1/3 da página 17; o restante fica em branco antes de "S8 Agrupamento amplo e análises de sensibilidade" começar na página 18. | corrigir | Mesma causa do item 1. |
| 6 | 21 (antes da 22) | A tabela de rebaixamentos GRADE (ver item 7) termina por volta de 1/3 da página 21; o restante fica em branco antes de "S9 Caixa de ferramentas célula a célula" começar na página 22. | corrigir | Mesma causa do item 1. |
| 7 | 20 → 21 | A legenda "Tabela 13. Resumo dos achados do agrupamento amplo, post hoc (GRADE...)" é impressa sozinha no rodapé da página 20, logo depois da última linha da Tabela 12 (que tem a mesma estrutura de colunas e ocupa as páginas 18–20). A tabela que essa legenda descreve (colunas "Célula", "Estudos", "Direção", "Certeza", "Rebaixamentos") só aparece no topo da página 21, sem repetir a legenda nem indicar "(cont.)". | corrigir | Agrupar legenda + cabeçalho de coluna + ao menos a primeira linha de dados da Tabela 13 num único bloco "manter junto" no template, para que a legenda não fique isolada numa página enquanto o corpo da tabela vai para a seguinte. Alternativa mais simples: mover a legenda inteira para o topo da página 21, junto da tabela. |
| 8 | 23 (antes da 24) | A Tabela 15 (painel OQF, 6 linhas) ocupa só ~1/5 da página 23; o restante fica em branco antes de "S10 Estudos da região e efeitos de viabilidade e momentum" começar na página 24. | corrigir | Mesma causa do item 1. |
| 9 | 7 e 22 | O sobrenome polonês "Wojciechowski" é hifenizado como "Wojcie-chowski" nas células estreitas da coluna "Estudo" (Tabela 5, p. 7) e da coluna "Estudos" (Tabela 14, p. 22), sempre que aparece em "Fichnová e Wojciechowski". A quebra é tecnicamente aceitável em português, mas soa estranha num sobrenome estrangeiro. | aceitável | Se o efeito incomodar visualmente, desabilitar hifenização para nomes próprios nessas colunas (`hyphenate: false` no texto da célula) ou alargar levemente a coluna. Não é urgente. |
| 10 | 22–23 | Na coluna "Intervenção" das Tabelas 14 e 15, o valor "Pesquisa pré-eleitoral" quebra quase sempre como "Pesquisa pré-eleito-ral" (linha 1: "pré-eleito-", linha 2: "ral"), repetindo-se em muitas linhas consecutivas. A hifenização é válida, mas o padrão repetitivo pesa visualmente numa tabela densa. | aceitável | Alargar a coluna "Intervenção" (ela é a mais estreita das duas tabelas) ou abreviar o rótulo (ex.: "Pesquisa pré-eleit." ou quebra manual antes de "eleitoral") para reduzir a repetição da mesma quebra em quase toda a tabela. |

## Itens do checklist sem problema encontrado

- Nenhuma tabela ou texto estourando a margem ou cortado nas 33 páginas.
- Nenhuma figura no documento (o suplemento só tem tabelas); nada ilegível por corpo pequeno demais.
- Nenhuma viúva/órfã de título de seção isolado sozinho no rodapé de uma página (os títulos de seção sempre têm ao menos o parágrafo introdutório junto, quando aparecem).
- As caixas "RASCUNHO NÃO VALIDADO" (capa) e o aviso da nota de rodapé aparecem inteiras e bem quebradas.
- Marca-d'água "RASCUNHO NÃO VALIDADO" na diagonal está presente e consistente em todas as páginas de conteúdo (2 a 33), sem sobrepor o texto a ponto de atrapalhar a leitura.
- Tipografia (fonte, tamanho, filetes de tabela, espaçamento) é consistente ao longo de todo o documento.
- Cabeçalho corrente ("Lamarca · Pesquisas eleitorais e voto" à esquerda, "RASCUNHO NÃO VALIDADO" à direita) e numeração de página ("n / 33") presentes e corretos em todas as páginas internas.
- Primeira página: título "Material suplementar", subtítulo, autoria ("Felipe Lamarca · MAPE/IESP-UERJ"), datas de busca, nota de IA ("Rascunho redigido por IA... não revisada pelo autor (P038)") e caixa de aviso de rascunho não validado, todos presentes.

## Avaliação geral

O suplemento está bem diagramado como peça de apoio técnico — tabelas densas, mas
legíveis, com tipografia e cabeçalhos consistentes do início ao fim. O problema real é
estrutural e recorrente, não estético: uma regra de quebra de página no template está
deixando pelo menos sete páginas majoritariamente em branco sempre que uma tabela longa
termina perto do topo, e no mesmo mecanismo separou de vez uma legenda (Tabela 13) do
corpo da tabela que ela descreve.
