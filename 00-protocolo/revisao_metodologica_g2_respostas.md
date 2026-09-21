# Respostas ao revisor metodológico (G2)

Coordenador, 19/09/2026. Relatório: `revisao_metodologica_g2.md` (0 CRITICO, 7 ALTO, 14 MEDIO, 6 BAIXO). Decisões humanas registradas em `pergunta.md`, seção 7.

| Problema | Tratamento |
|---|---|
| R01 ALTO: voto estratégico somado ao underdog | Variável `alvo_efeito` no codebook v0; célula principal só com alvos líder, azarão (disputa de dois) e opção de referendo; efeitos de viabilidade em tabela de direção e síntese narrativa próprias (protocolo, seções 2 e 8) |
| R02 ALTO: comparadores e estimandos misturados | Comparador separa sempre as células (`--grupo familia_intervencao,construto_outcome,comparador_tipo`); multibraço só com contrastes contra o controle quando houver controle; painéis de associação fora das meta-análises (seções 6 e 8) |
| R03 ALTO: δ só para p0 = 0,50 | δ de 2 pontos percentuais convertido com a mediana dos p0 da célula; rota agregada dividida pelo DP de referência; limite superior de trivial = δ (seção 8) |
| R04 ALTO: dano condicionado ao voto | Decisão humana: estudos só de comparecimento elegíveis na célula `mobilizacao`; C3 opção (b); fio de busca T3 em EN, PT e ES; âncoras de desenvolvimento e de validação de comparecimento acrescentadas |
| R05 ALTO: filtros de idioma e ano excluem sem elusão | Decisão humana: sem restrição de idioma (filtro só etiqueta). Ano: exclusão determinística com definição operacional (`publication_year` do OpenAlex; ano de defesa na BDTD); recall calculado com `filtros_v1.json` só etiquetando, antes de `filtros_v2.json` (seções 3 e 4) |
| R06 ALTO: sobreposição de âncoras e ausência de âncoras PT/ES | O subagente isolado marcou `tambem_desenvolvimento` (11 de 19); recall relatado com e sem elas; sem âncora escrita em PT ou ES achada por via independente: B02 a B04 sem validação de recall, declarado (seção 3) |
| R07 ALTO: decisão dos portões com limiares humanos | Plano fixado na seção 10: autopiloto com desvio A2 nos critérios; G4 com concordância A × B, estabilidade e contagem de âncoras excluídas pela IA feita pelo subagente isolado; âncora independente excluída obriga nova versão dos critérios |
| R08 MEDIO: recorte e cobertura de Hardmeier | Cobertura de Hardmeier marcada como não verificada; revisão descrita como "evidência publicada desde 2010"; lacuna declarada (decisão do usuário de manter 2010) |
| R09 MEDIO: grupo pequeno × laboratório | C1 reescrito no protocolo e no codebook de elegibilidade |
| R10 MEDIO: sinônimos ausentes na B01 | S-oa-en-v2: fio S e novos desfechos (+136 registros; relevantes achados) |
| R11 MEDIO: pré-registros sem busca_id | Retirada a função de "pistas"; pré-registros só na avaliação de relato seletivo |
| R12 MEDIO: checagem de revisões rasa | `EX3` e `EX4` lidas; conclusão mantida (pergunta.md, seção 4) |
| R13 MEDIO: registro no OSF | Decisão humana: não registrar; declarado no protocolo |
| R14 MEDIO: definição de estudo | Estudo = amostra independente; ids `<id_rs>_eN`; sensibilidade com o artigo como conglomerado |
| R15 MEDIO: risco crítico na análise principal | Análise principal com `--excluir-rob critico`; sensibilidade com eles |
| R16 MEDIO: moderadores e mediador sem variável | `n_competidores`, `dias_ate_eleicao`, `ajuste_mediador` no codebook v0 |
| R17 MEDIO: g próximo de zero | Regra de ±δ; anulação só com pelo menos 3 estudos com subgrupos de sinais opostos |
| R18 MEDIO: GRADE com EPOC | Corpos só com EPOC começam em baixa |
| R19 MEDIO: árbitro × regra liberal; origem dos exemplos | Sem árbitro na triagem T/A; exemplos só das âncoras de desenvolvimento e de `EX1` a `EX4` |
| R20 MEDIO: contato com autores | Declarado como atalho A5, para aprovação no G2 |
| R21 MEDIO: ROB-ME | Juízo estruturado de evidência faltante por célula, alimentando o GRADE |
| R22 BAIXO: traduções e PRESS | S-bdtd e S-oa-pt alinhados à tabela de termos v2; revisão de B02 a B04 depois do PRESS |
| R23 BAIXO: exemplos herdados | Trocados nos dois codebooks |
| R24 BAIXO: `preferencia_previa` fora do DAG | Nó e arestas acrescentados; texto do colisor alinhado |
| R25 BAIXO: retratação sem DOI | Conferência na página da editora ou do repositório pelo coordenador, registrada |
| R26 BAIXO: volume | Leitura atualizada (cerca de 1.460 antes da deduplicação; contingência de mais ondas acionada) |
| R27 BAIXO: título e produtos | Título com "revisão rápida"; policy brief opcional |
