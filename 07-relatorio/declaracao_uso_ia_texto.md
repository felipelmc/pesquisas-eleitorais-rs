**RASCUNHO NÃO VALIDADO**

Pendências abertas copiadas da seção 6 de `07-relatorio/declaracao_uso_ia.md`, gerada até o evento seq 828 do log:

- P001 (revisao_press);
- P004 (revisao_humana_portao, G3);
- P006 (validacao_humana, amostra01, 141 registros);
- P007 (validacao_humana, elusao01, 300 registros);
- P008 (revisao_humana_portao, G4);
- P019 (dedup_candidatos, 145 pares);
- P020 (fila_humana_triagem, 81 divergências);
- P023 (revisao_humana_portao, G5);
- P025 (revisao_piloto, 3 fichas);
- P026 (revisao_humana_portao, G6);
- P033 (revisao_humana_portao, G7);
- P035 (revisao_humana_portao, G8);
- P036 (certeza_humana);
- P037 (concordancia_extracao);
- P038 (revisao_humana_portao, G9);
- P039 (verificacao_humana_efeitos, 560 efeitos);
- P041 (conferencia_elegibilidade_tc, 165 decisões).

Depois da geração, o `rs caixa` abriu a P042 (certeza_caixa, 22 linhas), e o total passou a 18 pendências abertas (`07-relatorio/_pendencias_abertas.json`, igual ao `rs_estado.json`).

# Declaração de uso de inteligência artificial: efeitos da divulgação de pesquisas eleitorais sobre a intenção de voto e o comparecimento (*bandwagon* e *underdog*), revisão sistemática rápida

## Texto curto para o manuscrito

Usamos modelos da Anthropic, acessados pelo Claude Code, entre 19/09/2026 e 24/09/2026. O coordenador foi o Claude Opus 5.5 (`claude-opus-5-5`, com contexto de 1M), que executou os scripts da skill `revisao-sistematica`, distribuiu o trabalho entre subagentes e aplicou as correções propostas por eles. Os subagentes foram:

- `claude-sonnet-5` e `claude-opus-5`, triadores A e B de títulos e resumos;
- `claude-sonnet-5` e `claude-opus-5-5`, triadores A e B da triagem complementar dos 336 registros sem resumo (Emenda 6b);
- `claude-opus-5`, na proposta de elegibilidade no texto completo e na extração; `claude-opus-5-5`, nas fichas de texto completo feitas depois da Emenda 6b;
- `claude-sonnet-5`, na recodificação cega de 10 estudos da extração;
- `claude-opus-5-5` e `claude-sonnet-5`, avaliadores A e B do risco de viés, e `claude-opus-5-5` como árbitro dos desacordos;
- `claude-opus-5-5`, na reextração cega dos efeitos principais dos 40 estudos com dados, na arbitragem dos efeitos em 28 estudos, nas sugestões de terceiro leitor para as divergências da triagem e da extração, na pré-revisão PRESS da estratégia ativa, no rascunho do GRADE e na redação deste manuscrito.

A IA decidiu a triagem de títulos e resumos pela regra liberal e a triagem complementar dos registros sem resumo, e propôs, sem validação humana, a elegibilidade, a extração, as correções dos efeitos, o risco de viés e a certeza. O revisor humano aprovou a pergunta e o protocolo (G1 e G2), decidiu as Emendas 1, 4 (itens 4a a 4c) e 6b e 17 casos limítrofes de elegibilidade. Decisões que o log registrava como dele sem que as tivesse conferido foram corrigidas pela Emenda 6a: 336 exclusões por título, 88 consensos de risco de viés, 3 extensões de regra no texto completo, a Emenda 2 e o fechamento da P034. Critérios e prompts versionados com sha256, saídas, código e métricas estão no repositório GitHub privado `felipelmc/pesquisas-eleitorais-rs`.

Não houve validação humana: o recall da triagem não foi calculado, e as amostras de validação (141 registros) e de elusão (300 registros) seguem sem codificação. Nenhum dos 560 efeitos foi conferido por humano na página do texto completo, e nenhum julgamento de risco de viés ou de certeza foi validado. A concordância entre os triadores de IA na primeira onda foi 0,97 (κ 0,90) e a da recodificação cega da extração foi 58,5% (560 comparações), medidas de consistência entre agentes e não de acurácia. Títulos, resumos e textos completos obtidos por fontes legítimas foram processados pelos modelos da Anthropic; os termos de treino e retenção do acesso não estão registrados no projeto. O autor não declara conflito de interesse, inclusive com o provedor das ferramentas. Limitações: todos os modelos são do mesmo provedor, o árbitro do risco de viés e o dos efeitos são do mesmo modelo de outros agentes que eles julgam, as versões dos modelos podem mudar, e 18 pendências de validação humana estão abertas. As decisões de IA não validadas estão sinalizadas como pendências, e o manuscrito segue marcado como rascunho não validado até que o autor as confira e assuma a responsabilidade pelo conteúdo.

## 1. Ferramentas, versões e acesso (PRISMA-trAIce M2; RAISE 1 rec. 1.9)

| Ferramenta ou modelo | Versão exata | Desenvolvedor ou provedor | Acesso | Primeiro e último uso | Parâmetros |
|---|---|---|---|---|---|
| Coordenador de IA | `claude-opus-5-5` (Claude Opus 5.5, contexto de 1M), segundo o coordenador; o log não registra o modelo, e o protocolo previa `claude-opus-5` | Anthropic | Claude Code, skill `revisao-sistematica` | 19/09/2026 a 24/09/2026 (primeiro e último evento de `rs_log.jsonl`) | não registrados |
| Triagem, revisor A | `claude-sonnet-5` | Anthropic | subagente do Claude Code | 19/09/2026 a 20/09/2026 (log) | não registrados |
| Triagem, revisor B | `claude-opus-5` | Anthropic | subagente do Claude Code | 19/09/2026 a 20/09/2026 (log) | não registrados |
| Triagem complementar (Emenda 6b), A e B | `claude-sonnet-5` (A) e `claude-opus-5-5` (B) | Anthropic | subagente do Claude Code | 23/09/2026 (Emenda 6) | não registrados |
| Elegibilidade e extração | `claude-opus-5` (protocolo e critérios do G6); fichas de texto completo depois da Emenda 6b, `claude-opus-5-5` | Anthropic | subagente do Claude Code | não registrado no log | não registrados |
| Recodificação cega da extração | `claude-sonnet-5` | Anthropic | subagente do Claude Code | não registrado no log | não registrados |
| Risco de viés, avaliadores A e B | `claude-opus-5-5` (A) e `claude-sonnet-5` (B) | Anthropic | subagente do Claude Code | não registrado no log | não registrados |
| Risco de viés, árbitro | `claude-opus-5-5`, em contexto novo | Anthropic | subagente do Claude Code | não registrado no log | não registrados |
| Reextração cega e arbitragem dos efeitos | `claude-opus-5-5` (campo `modelo_extrator` das 40 reextrações; origem das correções em `05-decomposicao/correcoes_sessao_2026-09-23.csv`) | Anthropic | subagente do Claude Code, um PDF por agente | 23/09/2026 a 24/09/2026 | não registrados |
| Terceiros leitores (P020 e P037) e pré-revisão PRESS da v5 | `claude-opus-5-5` | Anthropic | subagente do Claude Code | 23/09/2026 a 24/09/2026 | não registrados |
| Rascunho do GRADE | `claude-opus-5-5`, com `06-analise/prompt_grade_v2.md` | Anthropic | subagente do Claude Code | 24/09/2026 (`08-revisao-humana/P036_grade/LEIA.md`) | não registrados |
| Redação do manuscrito | `claude-opus-5-5`, com `07-relatorio/prompt_redator_v2.md` | Anthropic | subagente do Claude Code | 24/09/2026 | não registrados |

A seção 1 do arquivo gerado registra só `claude-opus-5` e `claude-sonnet-5` (triagem, 117 eventos e 2785 decisões cada) e o coordenador sem modelo registrado. Os demais modelos vêm do protocolo, de `04-qualidade/notas_rob.md`, de `00-protocolo/emendas.md` (Emendas 3 e 6), dos arquivos de `08-revisao-humana/` e das descrições das pendências.

## 2. Finalidade e papel por etapa (M3; RAISE 1 rec. 1.8; I1)

| Etapa | Tarefa exata | Papel da IA | Quem decide | Por que usar IA nesta tarefa |
|---|---|---|---|---|
| Busca | sugestão de termos; pré-revisão PRESS da v3 e, em 23/09/2026, da v5; montagem das âncoras de validação | propõe | coordenador em autopiloto (atalhos A3 e A4); o PRESS humano está pendente (P001) | um só revisor humano; atalhos aprovados no G1 |
| Triagem de títulos e resumos | decisão incluir, excluir ou incerto por registro, com critério e justificativa | decide (regra liberal) | IA; as 81 divergências aguardam o revisor (P020), com sugestão de um terceiro leitor de IA | volume de registros acima da capacidade de um revisor |
| Registros sem resumo (Emenda 6b) | recuperação do resumo em fontes legítimas e nova triagem com os critérios da `ta_v1` | decide (exclusão só se os dois triadores excluírem, com trecho do resumo recuperado) | IA; o revisor dispensou a conferência | decisão do revisor de não excluir nenhum registro só pelo título |
| Texto completo | proposta de elegibilidade com trecho literal e página | propõe | IA nos casos fechados (165 decisões aguardam conferência humana, P041); revisor humano em 17 casos limítrofes | idem |
| Extração | fichas e dados de efeito com trecho e página; reextração cega e arbitragem dos efeitos principais | propõe e corrige | IA, sem verificação humana (P039 e P037) | idem |
| Risco de viés | respostas às perguntas-sinalizadoras e julgamento por domínio | rascunha | consenso automático onde A e B concordam; árbitro de IA nos desacordos; ninguém validou (P033) | idem |
| Certeza (GRADE) | juízo por domínio e enunciado por célula | rascunha | ninguém ainda (P036 e P042) | idem |
| Relato | rascunho do manuscrito a partir dos arquivos | redige | o autor, na leitura do G9 (P038) | idem |

## 3. Protocolo e desvios (M1)

- Plano de IA registrado em: `00-protocolo/protocolo.md`, seção 10, aprovado no G2 em 19/09/2026; revisão não registrada no OSF.
- Desvios e emendas: E001 e E002 (contingências da busca) e Emendas 1 a 6 em `00-protocolo/emendas.md`. Desvios do plano de IA:
  - o árbitro do risco de viés passou de `claude-fable-5-1` para `claude-opus-5-5`, por decisão de custo do revisor humano (Emenda 3);
  - os classificadores de desenho em desacordo no risco de viés foram fixados pelo coordenador, e não pelo árbitro (`04-qualidade/notas_rob.md`);
  - a confirmação humana em bloco dos 88 consensos de risco de viés, prevista pelo plano e registrada na Emenda 4d, não aconteceu (Emenda 6a);
  - a triagem complementar dos registros sem resumo foi feita só por IA (Emenda 6b);
  - a reextração cega e a arbitragem dos efeitos não estavam no plano; foram feitas para preparar a conferência humana (P039).

## 4. Entradas, saídas e prompts (M4, M5, M6)

- Dados enviados por registro: título, resumo, autores, ano, veículo e tipo de publicação na triagem; resumo recuperado em fontes legítimas na triagem complementar; PDFs completos na elegibilidade, na extração, na reextração cega, na arbitragem e no risco de viés. Nenhum treino ou ajuste fino.
- Formato da saída: JSON por registro na triagem, com critério e trecho literal nas exclusões; fichas com trecho literal e página na elegibilidade, na extração e no risco de viés, conferidas pelo verificador de citações da skill `fichamento-sistematico`; JSON por estudo na reextração cega e na arbitragem, com trecho e página. Citações reprovadas foram corrigidas pelo coordenador contra a camada de texto do PDF, sem mudar a resposta.
- Pós-processamento: consolidação pela regra liberal (sem árbitro); registro sem resumo nunca excluído sem resumo recuperado; correções dos árbitros aplicadas pelo coordenador, com 240 extensões a linhas análogas e 41 propostas não aplicadas, entre elas 40 que dependiam de um erro do prompt do árbitro sobre o estimando em diferença em diferenças (`08-revisao-humana/efeitos/aplicacao_arbitragem.csv`).
- Prompts e critérios:
  - `02-triagem/prompts/ta_v1.md` (sha256 `cd9cbfe00d4e4e45`);
  - `02-triagem/sem_resumo_revisao/INSTRUCOES_triagem.md`;
  - codebooks `00-protocolo/codebook_elegibilidade.csv` (`65dddc46db76bb2c`) e `00-protocolo/codebook_v0_efetividade.csv` (`47a0cc5ad53896ed`);
  - protocolo (`88530b9042361ced`);
  - prompts de risco de viés em `04-qualidade/prompt_rob_comum.md` e `04-qualidade/prompt_arbitro_rob.md`;
  - prompts de efeitos em `08-revisao-humana/efeitos/prompt_reextracao_cega.md` e `prompt_arbitro_efeitos.md`;
  - prompt do GRADE em `06-analise/prompt_grade_v2.md`;
  - prompt do redator em `07-relatorio/prompt_redator_v2.md`.

## 5. Interação humano-IA (M8; PRISMA 2020 item 8)

- Revisores humanos: um (`revisor_humano_1`), sem dupla humana em nenhuma etapa.
- Verificação feita pelo revisor: aprovação de G1 e G2; decisão das Emendas 1, 4 (4a a 4c) e 6b; decisão de 17 casos limítrofes de elegibilidade; escolha por custo do árbitro do risco de viés. Não houve leitura humana das divergências da triagem (81), das decisões de elegibilidade propostas (165), dos 560 efeitos, dos 259 domínios de risco de viés nem do GRADE.
- Registro de papéis: o comando `triagem override` grava `tipo_ator = humano` fixo. Por isso as 336 decisões da Emenda 6b aparecem como humanas no ledger, com o papel `ia_coordenador_emenda6`, e em `02-triagem/triagem_ta_final.csv` (`decidido_por = humano`); são decisões de IA.
- Resolução de discrepâncias: regra liberal na triagem; árbitro de IA no risco de viés e nos efeitos, sem confirmação humana.
- Treinamento e calibração: não se aplica (sem dupla humana; atalho A2).

## 6. Avaliação de desempenho (M9, R2; PRISMA 2020 item 8)

| Medida | Valor (IC 95%) | Fonte no projeto |
|---|---|---|
| Padrão de referência | não construído (sem dupla humana) | `02-triagem/validacao/ta_v1/amostra01_cega.xlsx` |
| Amostra de validação | 141 registros preparados, não codificados | `amostra01_desenho.json` |
| Sensibilidade (recall) | não calculada | seção 4 de `declaracao_uso_ia.md`: nenhuma validação com finalidade validação da rodada ativa |
| Especificidade, precisão, VPN | não calculadas | idem |
| κ e PABAK (IA × humanos) | não calculados | idem |
| WSS | não calculado | idem |
| Limiar pré-especificado e resultado | recall ≥ 0,95 com limite inferior ≥ 0,90: não verificável | idem |
| Elusão | amostra de 300 registros preparada, não lida | `elusao01_desenho.json` |
| Estabilidade | re-triagem de 158 registros: A com concordância binária 0,98 (κ 0,93; PABAK 0,96) e 3 mudanças de seguimento; B com concordância 1,00 (κ 1,00) | `02-triagem/validacao/ta_v1/estabilidade.json` |
| Concordância A × B (consistência) | binária 0,97; κ 0,90; PABAK 0,94 (primeira onda, 1573 registros) | critérios do G4 no log |
| Triagem complementar (Emenda 6b) | 336 registros; resumo recuperado para 172; 156 excluídos pelos dois triadores; 180 ao texto completo, dos quais 15 avaliados e excluídos e 165 não recuperados | `02-triagem/sem_resumo_revisao/`, `03-textos/elegibilidade_tc_final.csv` |
| Extração categórica | recodificação cega de 10 estudos: 58,5% (560 comparações); 37 variáveis abaixo do limiar | `05-decomposicao/validacao_extracao/concordancia/RELATORIO_CONCORDANCIA.md` |
| Efeitos principais, original × reextração cega (consistência) | 56 efeitos: 15 concordam, 23 com o mesmo valor e outra classificação, 12 com outro valor principal, 6 com sinal diferente; 26 de 40 estudos com ao menos uma divergência | `08-revisao-humana/efeitos/comparacao_cega.csv` e `comparacao_cega_estudos.csv` |
| Risco de viés (consistência A × B) | concordância por domínio de 0,43 a 1,00 no RoB 2, de 0,38 a 0,77 no ROBINS-I e de 0,60 a 1,00 no EPOC; árbitro seguiu A em 79 de 88 domínios | `04-qualidade/rob_*_concordancia.csv`, `rob_*_consenso.csv` |
| Números de efeito verificados | 0 de 560 verificados por humano | `05-decomposicao/verificacao_efeitos.csv` |

Análise de erros: não se aplica sem padrão humano. Nenhuma âncora de validação foi excluída pela triagem de IA. O limiar de recall não foi atingido nem testado; o remédio previsto é a codificação humana das amostras (P006 e P007).

## 7. Seleção: decisões de IA e de humanos (R1; PRISMA 2020 item 16a)

Nas bases, 148 registros foram removidos pelo filtro automático de ano previsto no protocolo, e 1314 foram excluídos na triagem; nos outros métodos, 648 pelo filtro de ano e 787 na triagem (`07-relatorio/prisma_contagens.json`). Em `02-triagem/triagem_ta_final.csv`, a consolidação registra 2210 decisões por consenso dos dois triadores de IA, 81 pela regra liberal e 336 com `decidido_por = humano`. Estas últimas são as decisões da triagem complementar da Emenda 6b, feitas por IA (156 exclusões e 180 registros enviados ao texto completo), gravadas como humanas pelo comando `triagem override`. No texto completo, 184 relatos foram avaliados (55 incluídos e 129 excluídos), com decisões propostas por IA e 17 casos limítrofes decididos pelo revisor humano.

## 8. Governança de dados, direitos e ética (M10; RAISE 1 rec. 1.10)

- Provedores e termos: Anthropic, via Claude Code; os termos de uso para treino, retenção e localização dos dados não estão registrados no projeto.
- Consentimento para o modo API: não se aplica (modo API não usado).
- Direitos autorais dos textos enviados: PDFs obtidos só por fontes legítimas (acesso aberto, repositórios, páginas de autor e editoras sem contorno de paywall), guardados só no disco local e não redistribuídos; Sci-Hub, LibGen, Anna's Archive, Z-Library e sites de upload de terceiros não foram usados; a licença de cada texto não está registrada no projeto.
- Dados pessoais e LGPD: não houve processamento de dados pessoais além de metadados bibliográficos; o e-mail de contato foi usado só como variável de ambiente para o *polite pool* do OpenAlex, sem gravação em arquivo.

## 9. Interesses e financiamento (RAISE 1 rec. 1.9)

Custo de API registrado: não registrado (a triagem por subagentes do Claude Code não registra custo por chamada). Financiamento: nenhum financiamento específico. Conflitos de interesse: nenhum conflito de interesse declarado, inclusive com o provedor das ferramentas. Quem pagou o acesso às ferramentas: não registrado no projeto.

## 10. Limitações e impacto (D1)

Sem validação humana, não se sabe quantos estudos elegíveis a triagem de IA perdeu, inclusive entre as 156 exclusões da triagem complementar, nem quantos erros há nos efeitos extraídos e nos julgamentos. Todos os modelos são do mesmo provedor, o que pode correlacionar erros entre avaliadores. O árbitro do risco de viés é o mesmo modelo do avaliador A e seguiu A em 79 de 88 domínios. A reextração cega e a arbitragem dos efeitos usaram o mesmo modelo. O avaliador B do risco de viés errou mais a transcrição literal das citações, corrigida pelo coordenador. O prompt do árbitro dos efeitos tinha um erro do coordenador sobre o estimando em diferença em diferenças, corrigido antes da aplicação. Dois defeitos da skill afetaram a conferência de trechos na triagem e a classificação de respostas inconclusivas no texto completo (`03-textos/notas_metadados_bib.md`). Modelos comerciais podem mudar sem aviso. A concordância entre agentes mede consistência, não acurácia.

## 11. Responsabilidade humana (RAISE 1 rec. 1.1)

As ferramentas de IA foram usadas nos papéis descritos acima. A supervisão humana se limitou aos portões G1 e G2, às Emendas 1, 4 (4a a 4c) e 6b, a 17 casos limítrofes de elegibilidade e à escolha do árbitro do risco de viés. As demais decisões de IA não foram validadas e estão listadas como pendências; decisões antes atribuídas ao revisor sem que ele as tivesse conferido foram corrigidas pela Emenda 6a. Critérios, protocolo, decisões finais de elegibilidade, juízos de risco de viés e de certeza, síntese e conclusões serão de responsabilidade do autor depois que ele conferir as saídas; até lá, o manuscrito é rascunho não validado.
