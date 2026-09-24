# Redação do corpo do artigo (etapa 3)

Você é o redator do artigo final desta revisão sistemática rápida: "Pesquisas eleitorais publicadas mudam o voto?". O autor é Felipe Lamarca (MAPE/IESP-UERJ). O texto é em português do Brasil, com *abstract* em inglês. Siga a especificação `09-documento-final/spec_v2.md` parágrafo a parágrafo. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Escreva só `09-documento-final/_esqueleto_revisao_final.qmd`; a versão v1 está guardada em `_esqueleto_v1_oqf.qmd`. Não rode `rs.py`, não abra PDFs e não rode nada em segundo plano.

## Leitura obrigatória antes de escrever
- `09-documento-final/spec_v2.md`, inteira. É o contrato.
- `09-documento-final/insumos/livro_regras.md` e `insumos/exemplares_movimentos.md`, sobretudo a rubrica e as frases-modelo.
- `09-documento-final/revista/rotulos.yml`, `revista/celulas.json` e `revista/numeros_v2.json`.
- `09-documento-final/revista/tabelas/previa_*.md` e `revista/figuras/legendas.yml`, para saber o que as tabelas e figuras mostram.
- Todas as fontes que a especificação cita para cada parágrafo.
- `/Users/felipelmc/.claude/commands/my-voice.md`, com as regras de voz do autor. Os passes de estilo vêm depois, mas escreva já perto dessa voz.

## Convenções da fonte (as travas verificam)
- **YAML:** o da especificação.
- **Mensagens principais:** `::: {.mensagens-principais}` com `## Mensagens principais {#mensagens-principais .unnumbered}`. Resumo e *Abstract* como `::: {.resumo}` e `::: {.resumo lang="en"}`, com títulos `.unnumbered` e IDs `resumo`/`abstract`. Resumo executivo como `# Resumo executivo {#resumo-executivo .unnumbered}`.
- **Seções numeradas** com os IDs de `rotulos.yml`. `@sec-` só para seções numeradas; para as outras, use `[texto](#id)`.
- **Figuras e tabelas geradas:** entram só por marcador em linha própria, `@@FIGURA nome@@` ou `@@TABELA nome@@`, e são citadas no texto por `@fig-...`/`@tbl-...`. Quadros (`qdr-glossario`, `qdr-picoc`) são escritos por você como Div `::: {#qdr-...}` com a tabela e a legenda como último parágrafo, com `tbl-colwidths` quando útil.
- **Enunciados:** cada célula C01...C18 aparece ao menos uma vez em prosa como `[<enunciado literal de celulas.json>]{.enunciado cel="Cxx"}`, com o k e a frase de certeza da célula no mesmo parágrafo. Não altere uma vírgula do enunciado.
- **Certeza:** frases padrão ("a evidência é muito incerta sobre...", "pode...", "provavelmente..."). O selo vai como `[⊕◯◯◯]{.grade} muito baixa` onde fizer sentido (Mensagens, Resumo). Direção pelo estimador, nunca pela significância; com 4 de 4, p = 0,125, e isso não é "não significativo".
- **Callouts:** os 11 "Pendente de revisão humana" (`::: {.callout-important}` com `## Pendente de revisão humana`), com os IDs exatos da especificação, e o aviso de rascunho (`::: {.callout-warning}` com `## RASCUNHO NÃO VALIDADO: 18 pendências humanas abertas`).
- **Citações** `[@chave]` só de chaves existentes em `revista/referencias.json`. Estudos que contribuem são nomeados em cada achado (SWiM, item 8).
- **Proibido:**
  - número digitado que não esteja nas fontes;
  - caminhos de arquivo;
  - `../`;
  - `column-`;
  - "Neutro", "sem efeito", "benéfico/danoso" e "significativo";
  - travessão;
  - conclusão atribuída a revisão marcada "não verificada";
  - "revisão por pares".
- **Autor:** marque **[A confirmar pelo autor]** onde a especificação mandar.

## Como trabalhar
1. Escreva o YAML, o aviso de rascunho, o corpo (seções 1 a 6), Informações adicionais, Referências, Apêndice A e os 11 callouts, incluindo o da P038, logo depois das Mensagens principais. A abertura (Mensagens principais, Resumo executivo, Resumo e *Abstract*) é escrita na etapa 4 por outro redator. Deixe as Divs e os títulos dessas seções no lugar, cada uma com um único parágrafo `[Abertura: etapa 4]`.
2. Monte com `python3 09-documento-final/montar_revisao_final.py`.
3. Rode `python3 09-documento-final/conferir_reestruturacao.py`. Corrija até passar, sem FALHA. Justifique no relatório final cada AVISO que ficar.
4. Renderize, de dentro de `09-documento-final/`:

   ```
   TYPST_IGNORE_SYSTEM_FONTS=true TYPST_IGNORE_EMBEDDED_FONTS=true quarto render revisao_final.qmd --to typst
   quarto render revisao_final.qmd --to html
   quarto render revisao_final.qmd --to docx
   ```

   Corrija até os três compilarem sem aviso de citação ou referência cruzada sem resolver.
5. Confira o orçamento: `wc -w` por seção, dentro de ±10% da especificação.

Responda com até 15 linhas: palavras por seção, resultado das travas (FALHAS e AVISOS), resultado dos três renders e os desvios da especificação com o motivo.
