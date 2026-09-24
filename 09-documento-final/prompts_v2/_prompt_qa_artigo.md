# Revisão visual do PDF (etapa 8)

Você é diagramador de revista acadêmica. Revise o PDF `09-documento-final/revisao_final.pdf` página por página. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Rasterize as páginas com `python3 -B -c "import pymupdf; ..."` a 110 dpi, numa pasta do scratchpad `/private/tmp/claude-501/-Users-felipelmc-Desktop-pesquisas-eleitorais-rs/fa308fbd-5109-4741-84b2-ffc424ac6966/scratchpad/qa_pdf/`, e leia cada imagem com a ferramenta Read. Não edite nenhum arquivo do projeto.

## Checklist por página
- tabela ou figura estourando a margem ou cortada;
- figura ilegível (corpo menor que cerca de 6,5 pt, sobreposição de rótulos);
- viúva ou órfã, título de seção isolado no pé da página;
- página quase vazia sem motivo, por exemplo antes de uma página deitada;
- hifenização estranha ou palavra estrangeira mal hifenizada;
- caixas "Pendente de revisão humana" quebradas de forma ruim;
- legenda separada da figura ou da tabela;
- marca-d'água ou cabeçalho sobre o texto de modo que atrapalhe a leitura;
- inconsistência tipográfica: fonte, tamanho, espaçamento, filetes;
- números de página, cabeça corrente e primeira página: título, subtítulo, autor, aviso de rascunho e nota de IA.

## Saída
Grave `09-documento-final/_qa/qa_visual_artigo.md` com uma lista de problemas: página, o que está errado, gravidade (`corrigir` ou `aceitável`) e a correção sugerida, no template Typst (`09-documento-final/revista/typst-template.typ`), no filtro, na legenda ou no texto. Termine com uma avaliação geral de duas frases: o PDF parece um artigo de revista acadêmica bem diagramado?

Responda com UMA linha: `OK qa_visual_artigo.md: <n> a corrigir, <n> aceitáveis`.
