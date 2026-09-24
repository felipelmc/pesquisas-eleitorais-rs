# Triagem complementar dos registros sem resumo (Emenda 6b): instruções do triador

Você é o triador `REVISOR` (A ou B) de uma revisão sistemática sobre o efeito da exposição a pesquisas eleitorais publicadas no voto. Trabalhe de forma independente: não abra a resposta do outro triador nem qualquer decisão anterior sobre estes registros (`02-triagem/sem_resumo*/proposta_*`, `dados/`, `02-triagem/lotes/`).

Raiz do projeto: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.

1. Leia inteiro o arquivo de critérios `02-triagem/prompts/ta_v1.md`: critérios C1 a C5, na ordem de aplicação, com exemplos. Aplique-os como estão, sem acrescentar nem afrouxar nada.
2. Leia o lote `02-triagem/sem_resumo_revisao/lotes/<LOTE>.json`. Cada registro traz:
   - título, autores, ano, veículo e tipo de publicação;
   - `resumo_recuperado`: resumo obtido depois em fonte legítima, com a fonte em `fonte_resumo`.

   Se `fonte_resumo` for `semantic_scholar_tldr`, o texto é um resumo automático de uma frase e **não** serve de base para exclusão.
3. Para cada registro, decida `incluir`, `excluir` ou `incerto`:
   - `excluir` só quando o resumo recuperado (lido junto com o título) mostra que um critério falha. `criterio_falhou` recebe o primeiro critério que falha na ordem, e `trecho` recebe uma cópia **literal**, contígua, de até 25 palavras, **do resumo recuperado**, que demonstre a falha.
   - Sem resumo recuperado, ou com só um TLDR, a decisão é `incerto`, por mais claro que o título pareça.
   - Na dúvida, `incerto`. `incluir` quando o resumo indica que o estudo pode atender a todos os critérios.
4. Não use a web nem conhecimento externo sobre o estudo.
5. Grave `02-triagem/sem_resumo_revisao/respostas/<REVISOR>_<LOTE>.json` com uma lista de objetos, um por registro, na ordem de entrada:
   `{"id_rs": "...", "decisao": "incluir|excluir|incerto", "criterio_falhou": "C1".."C5" ou null, "justificativa": "até 400 caracteres", "trecho": "cópia literal ou null"}`
   Confira com python que há exatamente um objeto por `id_rs` do lote e que todo `trecho` de exclusão aparece literalmente em `resumo_recuperado`.
6. Não rode nada em segundo plano. Responda com UMA linha: `OK <REVISOR> <LOTE>: <n> incluir, <n> excluir, <n> incerto`.
