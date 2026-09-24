# P019 — Revisão humana dos candidatos a duplicata

## O que é esta planilha

`dedup_revisao_v1.csv` contém os **145 pares** que `01-busca/dedup_pares.csv` marcou como
`decisao=candidato` (excluídos os que já ficaram no mesmo cluster por transitividade, ou seja,
`resolvido_transitivamente` no `motivo`). Nenhum desses pares foi decidido — são os que a regra
`R3_titulo_exato` (com conflito de DOI no cluster), `R5_candidato` ou `versao` não conseguiu
resolver sozinha (ver `references/03-organizacao-triagem.md`, seção 3).

Todas as colunas originais de `dedup_pares.csv` (`id_a`, `id_b`, `regra`, `score`, ..., `decisao`,
`decidido_por`, `motivo`) estão intactas, na mesma ordem, com os mesmos valores (`decisao=candidato`,
`decidido_por=script`). Depois vêm colunas de metadado só para leitura (`titulo_a/b`, `autores_a/b`,
`veiculo_a/b`, `tipo_a/b`, `resumo_a/b` truncado em 300 caracteres) e por último as colunas de
**sugestão de IA**:

- `sugestao_ia`: `confirmado` (fundir os dois registros), `rejeitado` (são registros diferentes,
  não fundir) ou `ligado` (só aparece quando `regra=versao`: manter os dois registros separados,
  cada um com seu `id_rs`, mas ligados ao mesmo `id_estudo` — nunca funde um par de versão).
- `confianca_ia`: `alta`, `media` ou `baixa`.
- `motivo_ia`: uma frase citando o metadado concreto que embasou a sugestão (mesmo DOI, título e
  autor idênticos, preprint x versão publicada, capítulos diferentes de um mesmo livro etc.).
- `ordem_revisao`: ordem sugerida de revisão, com os casos de `confianca_ia=baixa` primeiro (são 4),
  depois `media` (29) e por último `alta` (112). A planilha já está gravada nessa ordem.

**`sugestao_ia` é só uma sugestão de IA, revisada uma frase por vez lendo os metadados — nunca uma
decisão.** Ela não decide nada sozinha e concordância entre avaliadores de IA não valida nada (regra
do projeto). Quem decide é o revisor humano, preenchendo as colunas originais.

## Como preencher

Nas colunas **originais** (não crie colunas novas, as extras são ignoradas pelo `rs.py`):

- `decisao`: `confirmado`, `rejeitado` ou (só em par com `regra=versao`) `ligado`. Deixar
  `candidato` mantém o par pendente (não conta como decidido).
- `decidido_por`: seu papel, nunca seu nome — ex. `revisor_humano_1`. Pode ficar em branco linha a
  linha se você rodar o comando com `--por revisor_humano_1` (aplica a todas as linhas decididas
  sem `decidido_por` próprio).
- `motivo`: sua justificativa (pode concordar ou discordar de `motivo_ia`; escreva a sua, não copie
  a da IA sem checar).

Não mexa nas colunas de metadado nem nas de sugestão de IA — elas não são lidas pelo `rs.py`.

Contagem por `sugestao_ia`: 66 `confirmado`, 56 `rejeitado`, 23 `ligado`.
Contagem por `confianca_ia`: 112 `alta`, 29 `media`, 4 `baixa`.

## Comando para gravar a revisão

Rode a partir da raiz do projeto (`~/Desktop/pesquisas-eleitorais-rs`):

```bash
rs() { python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py "$@"; }; cd ~/Desktop/pesquisas-eleitorais-rs
rs --dir . dedup --revisar 08-revisao-humana/P019_dedup/dedup_revisao_v1.csv --por revisor_humano_1
```

Conferido no código (`rslib/dedup.py`, função `_resolver`): o `--revisar` aceita esse caminho fora
de `01-busca/` sem problema — ele resolve o caminho relativo à raiz do projeto quando o arquivo não
existe relativo ao diretório de onde o comando foi chamado, e aceita caminho absoluto também. **Não
é preciso copiar o arquivo para `01-busca/`.**

Repita `rs --dir . dedup --revisar ...` até `candidatos_pendentes = 0` no resumo (linhas deixadas
como `candidato` continuam pendentes). Depois disso, a pendência P019 fecha sozinha (no autopiloto,
`dedup` abre `dedup_candidatos`; ela fecha quando os candidatos zeram).

## Observações para quem revisar

- Vários pares repetem o mesmo padrão (mesmo estudo com DOI trocado por editora, dataset ICPSR
  versionado, preprint em múltiplas plataformas, coluna de jornal recorrente, resenha de livro x o
  livro, capítulo "Introduction" de livros diferentes) — o `motivo_ia` aponta o padrão em cada caso,
  mas confira antes de aceitar em lote.
- Vários pares com `regra` diferente de `versao` envolvem um NBER working paper (`tipo_publicacao
  =relatorio`) publicado depois em periódico — a regra `versao` do script só pega quando o tipo é
  `preprint`, então esses casos não puderam receber `ligado` aqui; a sugestão é `rejeitado` (não
  fundir), com a nota de considerar `textos ligar-relatos` na etapa 7 se os dois ficarem no corpus.
- Os pares de baixíssima confiança (`confianca_ia=baixa`) pedem atenção extra: possível duplicação
  em periódico predatório (índice de metadado com nome de autor variante), rascunho x versão final
  com conteúdo que pode ter mudado, e um par retratação (`WITHDRAWN`) x reimpressão (`Reprint of`).
