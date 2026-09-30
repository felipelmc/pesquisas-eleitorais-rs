# Listas de conferência da versão de entrega (Emenda 7)

Você atualiza as listas de conferência para o artigo final, "Pesquisas eleitorais publicadas mudam o voto?". O produto passou a se chamar "síntese sistemática de evidências conduzida com agentes de IA". O PDF entregue tem o artigo e, logo depois, os apêndices A a G.

- **Raiz:** `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.
- **Python:** rode com `python3 -B`.
- **Não faça:** rodar `rs.py`; abrir PDFs de estudos; mexer em código; mexer no artigo.

## Leia

- O artigo montado, `09-documento-final/revisao_final.qmd`. Os IDs das seções estão em `revista/rotulos.yml`.
- Os apêndices montados, `09-documento-final/suplemento.qmd`. Os IDs são `ap-a-busca`, `ap-b-emendas`, `ap-c-estudos`, `ap-d-rob`, `ap-e-efeitos`, `ap-f-sensibilidades` e `ap-g-ia`, publicados em `apendices.html`.
- As listas da versão de 24/09/2026, que são o seu ponto de partida: `09-documento-final/insumos/tabelas/checklist_{prisma2020,prisma_resumo,prisma_s,swim,trAIce}.md`. Elas apontam para `revisao.html#...` e `suplemento.html#...`, da versão anterior.
- `07-relatorio/checklist_prisma.csv` (a coluna `local_no_relato` foi apagada por um `rs prisma`) e `07-relatorio/checklist_swim.csv` (que ainda aponta para o relatório técnico).
- A Emenda 7 em `00-protocolo/emendas.md` e `08-revisao-humana/declaracao_autor_2026-09-30.md`. Elas dizem o que teve e o que não teve validação humana:
  - **não teve:** o risco de viés, o GRADE, a validação cega da triagem e a aplicação da deduplicação;
  - **teve, em bloco pelo autor:** busca, triagem, elegibilidade, efeitos e relato.

## Entregas

1. **As cinco listas** em `09-documento-final/insumos/tabelas/checklist_*.md`, reescritas para o artigo final. Mantenha o formato: tabela pipe com as colunas Item, Onde no artigo, Situação e Observação.
   - "Onde no artigo" aponta para `revisao.html#<id>` ou para `apendices.html#ap-...`, com o nome da seção ou do apêndice. Nada de `suplemento.html`, "S1" a "S11" ou "relatório técnico".
   - Seções que saíram: resumo executivo, 3.11 (percepção, implementação e custo), caixa OQF e Apêndice A de pendências. Os itens que apontavam para elas passam ao novo local ou a `não relatado`/`parcial`, com observação honesta.
   - O item 1 do PRISMA (título) fica `parcial`. A observação diz que o trabalho se identifica como síntese sistemática de evidências conduzida com agentes de IA, e não como revisão sistemática, pela regra do livro do autor sobre produtos de agentes.
   - Onde a observação citava pendências, ela passa a dizer o estado final. Por exemplo: "risco de viés julgado só por IA, sem validação humana (Apêndice G)". Nada de "depende do autor (P0xx)" para o que foi fechado.
   - Sem travessão (use "n.a."), sem caminho de arquivo, sem "rascunho" e sem "[A confirmar pelo autor]". Números só os que já estão nas listas de 24/09 ou no artigo.
2. **A coluna `local_no_relato`** de `07-relatorio/checklist_prisma.csv`, preenchida de novo, e a de `07-relatorio/checklist_swim.csv`, atualizada. Ambas apontam para o artigo final, em texto curto, por exemplo "Métodos > Fontes e busca (2.3); Apêndice A".
   - Não mude as outras colunas nem a ordem.
   - Mantenha a codificação (UTF-8 com BOM no `checklist_prisma.csv`, se ele tiver) e o fim de linha de cada arquivo.

Responda em até 8 linhas: itens por lista, contagem por situação e o que ficou `não relatado`.
