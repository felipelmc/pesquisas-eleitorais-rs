# Triagem por título dos registros sem resumo (proposta de IA; decisão final humana)

Contexto: estes 166 registros foram para o texto completo só porque não tinham resumo na base (a IA não exclui registro sem resumo). O revisor pediu uma triagem por IA, pelo título, para separar os que parecem relevantes. Sua proposta NÃO é a decisão final: um humano confere a lista antes de qualquer exclusão.

1. Leia, inteiro, o arquivo de critérios CRITERIOS (critérios C1 a C5 da triagem, na ordem de aplicação, com exemplos). Aplique-os como estão.
2. Leia o arquivo REGISTROS (lista JSON). Cada registro tem título, autores, ano, veículo, tipo de publicação e, às vezes, `resumo_externo` (resumo obtido do Semantic Scholar ou da Crossref; `[TLDR]` é um resumo automático de uma frase).
3. Para cada registro, proponha:
   - `excluir` só quando o título (com veículo, tipo e resumo externo, se houver) mostra SEM MARGEM que um critério falha. Exemplos: tema não eleitoral (C1); previsão eleitoral, precisão ou metodologia de pesquisas, modelos de previsão, mercados de apostas, ou pesquisas só como fonte de dados (C2); desfecho claramente não é voto nem comparecimento (C3); estudo claramente descritivo, de tendência agregada ou de percepção autodeclarada (C4); revisão, editorial, nota do editor, livro-texto, dataset ou codebook de survey, modelo teórico sem dados (C5).
   - `seguir` em qualquer outro caso, inclusive quando o título é ambíguo ou curto demais para decidir. Na dúvida, `seguir`.
4. Não use conhecimento externo sobre autores ou o estudo, nem a web. Não abra nenhum outro arquivo além dos dois indicados.
5. Grave em SAIDA uma lista JSON com um objeto por registro, na ordem de entrada, todos os 166:
   `{"id_rs": "...", "proposta": "seguir"|"excluir", "criterio": "C1".."C5" ou "", "justificativa": "<uma frase curta>"}`
   Em `seguir`, `criterio` = "". Confira com `python3 -c "import json; d=json.load(open('<SAIDA>')); print(len(d))"` que são 166 objetos com id_rs únicos.
6. Não rode nada em segundo plano. Resposta final: uma linha, "OK: N seguir, M excluir".
