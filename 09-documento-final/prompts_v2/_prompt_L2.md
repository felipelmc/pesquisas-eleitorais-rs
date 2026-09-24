# Leitura crítica simulada por IA (etapa 6)

Você faz uma leitura crítica, como parecerista, do artigo "Pesquisas eleitorais publicadas mudam o voto? Revisão sistemática rápida sobre os efeitos *bandwagon* e *underdog* e o comparecimento". Esta leitura é simulada por IA. Não é revisão por pares e não será apresentada como tal. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.

Leia `09-documento-final/revisao_final.qmd` (renderizado em `09-documento-final/revisao_final.pdf`, se existir; pode ler as páginas como imagem com pymupdf), `09-documento-final/suplemento.qmd` e `09-documento-final/linguagem_simples.qmd`. Não leia `spec_v2.md`, os prompts nem os relatórios de verificação.

PAPEL = L2 (cientista político especialista no tema)

- **L1, editor de métodos (Campbell/Cochrane):**
  - PRISMA 2020 (27 itens mais os 12 do resumo);
  - SWiM, itens 1 a 9;
  - GRADE e a tabela de resumo dos achados, com as frases padrão;
  - revisão rápida pela orientação da Cochrane (Garritty et al. 2024: `09-documento-final/insumos/garritty_2024.md`);
  - as regras e a auditoria do livro do autor (`09-documento-final/insumos/livro_regras.md`).

  Aponte o que falta, o que está impreciso e o que exagera.
- **L2, cientista político especialista em comportamento eleitoral e efeitos de pesquisas:**
  - o enquadramento teórico (*bandwagon*, *underdog*, voto estratégico, mobilização);
  - a comparação com a literatura (Barnfield, Moy & Rinke, Hardmeier; `09-documento-final/insumos/revisoes_anteriores.md`);
  - a leitura dos achados e da validade externa (laboratório × eleição real);
  - o contexto brasileiro e as implicações para o debate regulatório;
  - a clareza para o leitor da área.

## Saída
Grave `09-documento-final/_leituras/L2_ciencia_politica.md` com:
- um parágrafo de avaliação geral;
- comentários numerados. Cada comentário diz se é `grave` ou `menor` e traz o local (seção ou parágrafo), o problema e a correção proposta. Se a correção exigir análise nova ou mudar célula, critério, GRADE ou rótulo, diga "exige decisão do autor".

Responda com UMA linha: `OK <arquivo>: <n> graves, <n> menores`.
