# Listas de conferência do suplemento, S11 (etapa 6b)

Você preenche as listas de conferência do artigo "Pesquisas eleitorais publicadas mudam o voto?", com o local de cada item **no artigo novo**. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Rode Python com `python3 -B`. Não rode `rs.py` e não abra PDFs de estudos.

## Leia
- O artigo montado, `09-documento-final/revisao_final.qmd` (antes, rode `python3 -B 09-documento-final/montar_revisao_final.py`), e o suplemento, `09-documento-final/suplemento.qmd`. Os IDs de seção estão em `09-documento-final/revista/rotulos.yml`.
- Os pontos de partida em `07-relatorio/checklist_prisma.csv` e `07-relatorio/checklist_swim.csv`. Eles apontam para o relatório técnico; você aponta para o artigo.
- As regras do livro sobre listas em `09-documento-final/insumos/livro_regras.md` (A11). O mapa PRISMA/SWiM → texto está na seção 3.15 de `09-documento-final/spec_v2.md`.
- Os textos oficiais das listas, pela web, só em fontes abertas:
  - PRISMA 2020 (27 itens com subitens, mais os 12 do resumo): Page et al. 2021, BMJ, PMC;
  - PRISMA-S (16 itens): Rethlefsen et al. 2021, Systematic Reviews;
  - SWiM (9 itens): Campbell et al. 2020, BMJ;
  - PRISMA-trAIce: procure a lista oficial. Se não achar a versão publicada, registre isso e use a lista que o livro descreve (seção 12), sempre "só como lista de conferência".

## Entregas
1. `09-documento-final/insumos/tabelas/checklist_prisma2020.md`, `checklist_prisma_resumo.md`, `checklist_prisma_s.md`, `checklist_swim.md` e `checklist_trAIce.md`. Cada um é uma tabela pipe com as colunas:
   - Item: número e tópico, em português, com resumo curto do item, sem copiar o texto oficial inteiro;
   - Onde no artigo: nome da seção com link para `revisao.html#<id>`, ou suplemento `suplemento.html#<id>`, ou tabela e figura;
   - Situação: `relatado`, `parcial`, `não se aplica` ou `não relatado`;
   - Observação: por que é parcial ou não se aplica, por exemplo "não houve registro", "sem meta-análise principal" ou "depende do autor (P0xx)".

   Nada de travessão ("—"): use "n.a.". Nada de caminho de arquivo. Seja honesto: item sem relato é `não relatado`.
2. Troque a função `s11_checklists()` de `09-documento-final/montar_suplemento.py` para montar S11 com as cinco tabelas, cada uma com legenda e rótulo `tbl-s11-...`, em `::: {.tabela-larga}`, com uma frase de introdução. Não mexa nas outras funções.
3. Rode `python3 -B 09-documento-final/montar_suplemento.py`, `python3 -B 09-documento-final/conferir_reestruturacao.py`, que tem de passar sem FALHA, e o render:

   ```
   cd 09-documento-final && TYPST_IGNORE_SYSTEM_FONTS=true TYPST_IGNORE_EMBEDDED_FONTS=true quarto render suplemento.qmd --to typst
   ```

   O render tem de sair sem aviso.

Responda com até 8 linhas: itens por lista e contagem por situação.
