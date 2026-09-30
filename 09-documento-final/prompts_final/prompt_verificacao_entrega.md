# Verificação independente da versão de entrega (Emenda 7)

Você é o verificador independente do artigo final, dos apêndices e do resumo em linguagem simples. Você não escreveu nenhum deles.

- **Raiz:** `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.
- **Não altere os textos.** Grave só `09-documento-final/verificacao_entrega.md`.
- **Não faça:** abrir PDFs de estudos; rodar `rs.py`; rodar nada em segundo plano.
- **Pode rodar:**
  - `python3 09-documento-final/montar_revisao_final.py` e `montar_suplemento.py`;
  - `python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd`;
  - scripts Python seus, que só leiam.

## Objetos

- `09-documento-final/revisao_final.qmd`: o artigo, montado do esqueleto, com as figuras (`revista/figuras/legendas.yml`) e as tabelas.
- `09-documento-final/suplemento.qmd`: os apêndices A a G, com a tabela `revista/tabelas/lacunas.yml`.
- `09-documento-final/linguagem_simples.qmd`.

O contrato é `09-documento-final/spec_final.md`. A análise não mudou desde 24/09/2026: o texto não pode trazer número, célula, certeza ou meta diferentes das fontes.

## Conferências

1. **Números.** Confira cada número do texto, das tabelas, das legendas, das mensagens, do resumo, do *abstract* e do resumo em linguagem simples contra os arquivos de origem. Use scripts e liste cada divergência: trecho, número no texto, número na fonte e arquivo. A mesma afirmação tem de trazer os mesmos números em todos os lugares. As fontes são:
   - `07-relatorio/prisma_contagens.json`;
   - `06-analise/swim_*/swim_resumo.json`, `06-analise/meta_*/meta_resumo.json`, `06-analise/certeza*.csv` e `06-analise/_delta_celula.txt`;
   - `revista/celulas.json` e `revista/numeros_v2.json`;
   - `insumos/tabelas/numeros.json`;
   - `07-relatorio/_pendencias_abertas.json` e `07-relatorio/declaracao_uso_ia.md`;
   - `04-qualidade/rob_*`;
   - `00-protocolo/emendas.md`, inclusive a Emenda 7.
2. **Certeza e direção.**
   - Cada afirmação de efeito traz a certeza da célula certa e a frase padrão: "a evidência é muito incerta" (muito baixa), "pode" (baixa) e "provavelmente" (moderada).
   - Nenhuma direção se apoia em significância.
   - Nenhuma recomendação vem com força acima da certeza.
   - O g das metas não aparece nas Mensagens, no Resumo, no *Abstract* nem nas Conclusões.
3. **Leitura às cegas.** Para cada conclusão (Mensagens, Resumo, Discussão 4.1 e Conclusões), inverta mentalmente a direção. Se o texto soasse igualmente confiante, registre `aviso` por enquadramento otimista.
4. **Atribuição humana. É o ponto mais importante desta versão.** O texto só pode dizer que o autor conferiu o que a declaração dele cobre (`08-revisao-humana/declaracao_autor_2026-09-30.md`):
   - busca: conferência da pré-revisão PRESS por IA, e não PRESS independente;
   - triagem: 81 divergências mantidas pela regra liberal;
   - elegibilidade: 165 propostas e 3 extensões de regra;
   - piloto;
   - os 560 efeitos, contra a página do PDF;
   - as 259 divergências da recodificação, com o valor original;
   - o relato.

   Conferências **em bloco**, e não item a item. Reprove como `erro` qualquer frase que:
   - atribua ao autor a validação do risco de viés, do GRADE ou da triagem cega;
   - chame o produto de "revisão sistemática" (o nome é "síntese sistemática de evidências conduzida com agentes de IA");
   - omita que o risco de viés e a certeza foram julgados só por IA.

   "RASCUNHO NÃO VALIDADO" aparece uma só vez, na abertura da declaração de IA, com as pendências abertas (P006, P007, P008, P019, P033, P035, P036 e P042). A tabela do Apêndice G tem de bater com a Emenda 7 e com `_pendencias_abertas.json`, menos a P038.
5. **Autocontido.** Um leitor sem acesso ao repositório entende a pergunta, os critérios, a busca, a seleção, a extração, o risco de viés, a síntese, a certeza, os resultados por célula e as limitações, só com o PDF (artigo e apêndices)? Liste o que faltar. O artigo remete aos apêndices por letra: confira se cada remissão aponta para o apêndice certo.
6. **Citações e revisões anteriores.**
   - Toda `@chave` existe em `revista/referencias.json`.
   - As afirmações sobre revisões anteriores batem com `insumos/revisoes_anteriores.md`, com Hardmeier como "não verificada".
   - As afirmações sobre o Brasil batem com `insumos/contexto_brasil.md`.
   - As afirmações sobre revisões rápidas batem com `insumos/garritty_2024.md`.
7. **Declarações do autor.** Informações adicionais trazem:
   - nenhum conflito de interesses, nem relação com a Anthropic;
   - CRediT todo do autor, com os agentes de IA fora da autoria;
   - R 4.5.2;
   - repositório privado com acesso sob pedido, e pacote público em `pacote-replicacao.zip`, com MIT e CC BY 4.0;
   - nenhum marcador "[A confirmar pelo autor]".
8. **Travas.** Rode `conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd` e registre o resultado.

## Saída

Grave `verificacao_entrega.md` com:
- um resumo do que foi checado e quanto;
- as divergências classificadas como `erro`, `aviso` ou `ok com ressalva`, cada uma com a correção em texto exato e o arquivo onde se corrige (`_esqueleto_revisao_final.qmd`, `_esqueleto_suplemento.qmd`, `revista/tabelas/lacunas.yml`, `revista/figuras/legendas.yml` ou `linguagem_simples.qmd`);
- os scripts usados.

Responda com UMA linha: `OK verificacao_entrega.md: <n> erros, <n> avisos`.
