# Verificação independente do artigo (etapa 5)

Você é o verificador independente do artigo final e dos produtos ligados a ele. Você não escreveu nenhum deles. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Não altere os textos. Grave só `09-documento-final/verificacao_v2.md` e `09-documento-final/auditoria_final.md`. Não abra PDFs de estudos. Não rode `rs.py` nem nada em segundo plano. Pode rodar `python3 09-documento-final/montar_revisao_final.py`, `montar_suplemento.py`, as travas e scripts Python seus.

## Objetos
- `09-documento-final/revisao_final.qmd`, montado a partir do esqueleto, com figuras (`revista/figuras/legendas.yml`, `revista/figuras/dados/`) e tabelas.
- `09-documento-final/suplemento.qmd`.
- `09-documento-final/linguagem_simples.qmd`.

## Conferências
1. **Números.** Confira cada número do texto, das tabelas, das legendas, do resumo, do *abstract*, das mensagens e do resumo em linguagem simples contra os arquivos de origem:
   - `07-relatorio/prisma_contagens.json`;
   - `06-analise/swim_*/swim_resumo.json` e `06-analise/meta_*/meta_resumo.json`;
   - `06-analise/certeza*.csv` e `06-analise/_delta_celula.txt`;
   - `revista/celulas.json` e `revista/numeros_v2.json` (refaça as fórmulas);
   - `insumos/tabelas/numeros.json` e `07-relatorio/_pendencias_abertas.json`;
   - `04-qualidade/rob_*`;
   - `00-protocolo/emendas.md`;
   - `07-relatorio/relatorio.qmd`.

   Use scripts e liste cada divergência (trecho, número no texto, número na fonte, arquivo). A mesma afirmação tem de trazer os mesmos números em todos os lugares (livro, A2).
2. **Certeza.** Toda afirmação de efeito traz a certeza da célula certa e a frase padrão (muito baixa: "a evidência é muito incerta"; baixa: "pode"; moderada: "provavelmente"). Nenhuma direção se apoia em significância, e não há "significativo/não significativo", "Neutro" nem "sem efeito".
3. **Leitura às cegas** (livro, A23). Para cada conclusão (Mensagens, Resumo, Discussão 4.1, Conclusões), reescreva mentalmente com a direção invertida e diga se o texto soaria igualmente confiante. Onde soaria, há enquadramento otimista: registre como `aviso`.
4. **Marcações humanas.** As 11 caixas "Pendente de revisão humana" estão nas seções certas, com os IDs certos (compare com `_revisao_final_v1_oqf.qmd`). O apêndice lista as 18 pendências. Os marcadores "[A confirmar pelo autor]" estão onde há fato que só o autor sabe: CRediT e papéis. Nenhum papel humano é atribuído sem declaração do autor.
5. **Citações e revisões anteriores.** Toda `@chave` existe em `revista/referencias.json`. Toda afirmação sobre Barnfield, Moy & Rinke, Hardmeier ou Coşgun bate com `insumos/revisoes_anteriores.md`; Hardmeier é "não verificada". As afirmações sobre o Brasil batem com `insumos/contexto_brasil.md`, sem itens "não confirmados". As afirmações sobre revisões rápidas batem com `insumos/garritty_2024.md`.
6. **Recomendações.** Nada recomenda proibir ou liberar a divulgação com força acima da certeza (tabela de verbos do livro).
7. **Auditoria final.** Percorra os itens A1 a A36 de `insumos/livro_regras.md`, seção 8, um a um. Cada item vai para `auditoria_final.md` como `cumprido`, `parcial` ou `não cumprido`, com a evidência (seção ou linha) e a correção proposta. Itens que dependem do autor ou de depósito externo (A21, A36) ficam `não cumprido (depende do autor)`.

## Saída
- `verificacao_v2.md`:
  - resumo do que foi checado e quanto;
  - divergências classificadas como `erro`, `aviso` ou `ok com ressalva`, com a correção em texto exato e o arquivo onde se corrige (esqueleto, `legendas.yml`, `revista/tabelas/*.yml`, `linguagem_simples.qmd`);
  - os scripts usados.
- `auditoria_final.md`, conforme o item 7.

Responda com UMA linha: `OK verificacao_v2.md: <n> erros, <n> avisos; auditoria: <n> cumpridos, <n> parciais, <n> não cumpridos`.
