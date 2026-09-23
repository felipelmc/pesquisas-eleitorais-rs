**RASCUNHO NÃO VALIDADO**

Pendências abertas (copiadas da seção 6 de `07-relatorio/declaracao_uso_ia.md`): P001 (revisao_press), P004 (revisao_humana_portao, G3), P006 (validacao_humana, amostra01, 141 registros), P007 (validacao_humana, elusao01, 300 registros), P008 (revisao_humana_portao, G4), P019 (dedup_candidatos, 145 pares), P020 (fila_humana_triagem, 81 divergências), P023 (revisao_humana_portao, G5), P025 (revisao_piloto, 3 fichas), P026 (revisao_humana_portao, G6), P028 (conferencia_elegibilidade_tc, 150 decisões), P032 (verificacao_humana_efeitos, 554 efeitos), P033 (revisao_humana_portao, G7), P035 (revisao_humana_portao, G8), P036 (certeza_humana, 21 linhas do GRADE), P037 (concordancia_extracao).

# Declaração de uso de inteligência artificial: efeitos da divulgação de pesquisas eleitorais sobre a intenção de voto e o comparecimento (*bandwagon* e *underdog*), revisão sistemática rápida

## Texto curto para o manuscrito

Usamos modelos da Anthropic, acessados como subagentes do Claude Code entre 19/09/2026 e 23/09/2026: `claude-sonnet-5` e `claude-opus-5` na triagem de títulos e resumos (revisores A e B), `claude-opus-5` na proposta de elegibilidade no texto completo e na extração, `claude-sonnet-5` na recodificação cega de parte da extração, `claude-opus-5-5` e `claude-sonnet-5` nos julgamentos de risco de viés (avaliadores A e B), `claude-opus-5-5` como árbitro dos desacordos de risco de viés e no rascunho do GRADE, e um coordenador de IA que executou os scripts e coordenou os subagentes. O rascunho do manuscrito também foi redigido por subagente de IA a partir dos arquivos do projeto. Nesta revisão rápida, com o atalho A2 aprovado pelo revisor humano no G1, a IA decidiu a triagem de títulos e resumos pela regra liberal e propôs, sem validação humana, a elegibilidade, a extração, o risco de viés e a certeza; o revisor humano decidiu os casos residuais de elegibilidade, assumiu as exclusões por título de registros sem resumo propostas pelos dois triadores de IA e confirmou em bloco as 88 propostas do árbitro de risco de viés. Critérios e prompts versionados com sha256, saídas, código e métricas estão na pasta do projeto (repositório privado). Não houve validação humana da triagem: o recall não foi calculado, e as amostras de validação (141 registros) e de elusão (300 registros) seguem sem codificação. A concordância entre os triadores de IA na primeira onda foi 0,97 (κ 0,90) e a da recodificação cega da extração foi 58,5% (560 comparações), medidas de consistência entre agentes e não de acurácia. Títulos, resumos e textos completos foram processados pelos modelos da Anthropic; os termos de uso quanto a treino e retenção e os interesses dos autores nas ferramentas estão a preencher pelos autores. Limitações: todos os modelos são do mesmo provedor, o árbitro do risco de viés é o mesmo modelo do avaliador A, as versões dos modelos podem mudar, e 16 pendências de validação humana estão abertas. As decisões de IA não validadas estão sinalizadas como pendências, e o manuscrito segue marcado como rascunho não validado até que os autores as confiram e assumam a responsabilidade pelo conteúdo.

## 1. Ferramentas, versões e acesso (PRISMA-trAIce M2; RAISE 1 rec. 1.9)

| Ferramenta ou modelo | Versão exata | Desenvolvedor ou provedor | Acesso | Primeiro e último uso | Parâmetros |
|---|---|---|---|---|---|
| Coordenador de IA | não registrado no log (Claude Opus 5, segundo o protocolo) | Anthropic | Claude Code, skill `revisao-sistematica` | 2026-09-19 a 2026-09-23 | não registrados |
| Triagem, revisor A | `claude-sonnet-5` | Anthropic | subagente do Claude Code | 2026-09-19 a 2026-09-20 | não registrados |
| Triagem, revisor B | `claude-opus-5` | Anthropic | subagente do Claude Code | 2026-09-19 a 2026-09-20 | não registrados |
| Elegibilidade e extração | `claude-opus-5` (segundo o protocolo e os critérios do G6) | Anthropic | subagente do Claude Code | não registrado no log | não registrados |
| Recodificação cega da extração | `claude-sonnet-5` | Anthropic | subagente do Claude Code | 2026-09-23 | não registrados |
| Risco de viés, avaliadores A e B | `claude-opus-5-5` (A) e `claude-sonnet-5` (B) | Anthropic | subagente do Claude Code | não registrado no log | não registrados |
| Risco de viés, árbitro | `claude-opus-5-5`, em contexto novo | Anthropic | subagente do Claude Code | não registrado no log | não registrados |
| Rascunho do GRADE | `claude-opus-5-5` | Anthropic | subagente do Claude Code | não registrado no log | não registrados |

A seção 1 do arquivo gerado registra só `claude-opus-5` e `claude-sonnet-5` (triagem, 117 eventos e 2785 decisões cada) e o coordenador sem modelo registrado; os demais modelos vêm do protocolo, de `04-qualidade/notas_rob.md`, de `00-protocolo/emendas.md` (Emenda 3) e das descrições das pendências.

## 2. Finalidade e papel por etapa (M3; RAISE 1 rec. 1.8; I1)

| Etapa | Tarefa exata | Papel da IA | Quem decide | Por que usar IA nesta tarefa |
|---|---|---|---|---|
| Busca | sugestão de termos; pré-revisão PRESS; montagem das âncoras de validação | propõe | coordenador em autopiloto (atalhos A3 e A4) | um só revisor humano; atalhos aprovados no G1 |
| Triagem de títulos e resumos | decisão incluir, excluir ou incerto por registro, com critério e justificativa | decide (regra liberal) | IA; registros sem resumo excluídos por título só com decisão do revisor humano | volume de registros acima da capacidade de um revisor |
| Texto completo | proposta de elegibilidade com trecho literal e página | propõe | IA nos casos fechados; revisor humano nos incertos e limítrofes | idem |
| Extração | fichas e dados de efeito com trecho e página | propõe | IA, sem verificação humana (decisão humana no G2) | idem |
| Risco de viés | respostas às perguntas-sinalizadoras e julgamento por domínio | rascunha | consenso automático onde A e B concordam; árbitro de IA nos desacordos, confirmado em bloco pelo revisor humano | idem |
| Certeza (GRADE) | juízo por domínio e enunciado por célula | rascunha | ninguém ainda (pendência P036) | idem |
| Relato | rascunho do manuscrito a partir dos arquivos | redige | autores (a conferir) | idem |

## 3. Protocolo e desvios (M1)

- Plano de IA registrado em: `00-protocolo/protocolo.md`, seção 10, aprovado no G2 em 19/09/2026; revisão não registrada no OSF.
- Desvios e emendas: E001 e E002 (contingências da busca); Emendas 1 a 5 em `00-protocolo/emendas.md`. Desvios do plano de IA: árbitro do risco de viés trocado de `claude-fable-5-1` para `claude-opus-5-5` por decisão de custo do revisor humano (Emenda 3); classificadores de desenho em desacordo no risco de viés fixados pelo coordenador, e não pelo árbitro (`04-qualidade/notas_rob.md`).

## 4. Entradas, saídas e prompts (M4, M5, M6)

- Dados enviados por registro: título, resumo, autores, ano, veículo e tipo de publicação na triagem; PDFs completos na elegibilidade, na extração e no risco de viés. Nenhum treino ou ajuste fino.
- Formato da saída: JSON por registro na triagem; fichas com trecho literal e página na elegibilidade, na extração e no risco de viés, conferidas pelo verificador de citações da skill `fichamento-sistematico`; citações reprovadas corrigidas pelo coordenador contra a camada de texto do PDF, sem mudar a resposta.
- Pós-processamento: consolidação pela regra liberal (sem árbitro); registro sem resumo nunca excluído pela IA.
- Prompts e critérios: `02-triagem/prompts/ta_v1.md` (sha256 `cd9cbfe00d4e4e45`); codebooks `00-protocolo/codebook_elegibilidade.csv` (`65dddc46db76bb2c`) e `00-protocolo/codebook_v0_efetividade.csv` (`47a0cc5ad53896ed`); protocolo (`88530b9042361ced`); prompts de risco de viés em `04-qualidade/prompt_rob_comum.md` e `04-qualidade/prompt_arbitro_rob.md`; prompt do GRADE em `06-analise/prompt_grade.md`.

## 5. Interação humano-IA (M8; PRISMA 2020 item 8)

- Revisores humanos: um (`revisor_humano_1`), sem dupla humana em nenhuma etapa.
- Verificação: aprovação de G1 e G2; decisão das emendas de escopo; decisão dos casos incertos e limítrofes de elegibilidade; conferência e adoção das propostas de exclusão por título de registros sem resumo (336 decisões registradas como humanas na consolidação final da triagem); confirmação em bloco das 88 propostas do árbitro de risco de viés. Não houve leitura humana das divergências da triagem (81), das decisões de elegibilidade propostas (150), dos 554 efeitos nem do GRADE.
- Resolução de discrepâncias: regra liberal na triagem; árbitro de IA com confirmação humana no risco de viés.
- Treinamento e calibração: não se aplica (sem dupla humana; atalho A2).

## 6. Avaliação de desempenho (M9, R2; PRISMA 2020 item 8)

| Medida | Valor (IC 95%) | Fonte no projeto |
|---|---|---|
| Padrão de referência | não construído (sem dupla humana) | `02-triagem/validacao/ta_v1/amostra01_cega.xlsx` |
| Amostra de validação | 141 registros preparados (100 aleatórios e 41 de enriquecimento), não codificados | `amostra01_desenho.json` |
| Sensibilidade (recall) | não calculada | seção 4 de `declaracao_uso_ia.md`: nenhuma validação com finalidade validação da rodada ativa |
| Especificidade, precisão, VPN | não calculadas | idem |
| κ e PABAK (IA × humanos) | não calculados | idem |
| WSS | não calculado | idem |
| Limiar pré-especificado e resultado | recall ≥ 0,95 com limite inferior ≥ 0,90: não verificável | idem |
| Elusão | amostra de 300 registros preparada, não lida | `elusao01_desenho.json` |
| Estabilidade | re-triagem de 158 registros: A com concordância binária 0,98 (κ 0,93; PABAK 0,96) e 3 mudanças de seguimento; B com concordância 1,00 (κ 1,00) | `02-triagem/validacao/ta_v1/estabilidade.json` |
| Concordância A × B (consistência) | binária 0,97; κ 0,90; PABAK 0,94 (primeira onda, 1573 registros) | critérios do G4 no log |
| Extração categórica | recodificação cega de 10 estudos: 58,5% (560 comparações); 37 variáveis abaixo do limiar | `05-decomposicao/validacao_extracao/concordancia/RELATORIO_CONCORDANCIA.md` |
| Risco de viés (consistência A × B) | concordância por domínio de 0,43 a 1,00 no RoB 2, de 0,38 a 0,77 no ROBINS-I e de 0,60 a 1,00 no EPOC | `04-qualidade/rob_*_concordancia.csv` |
| Números de efeito verificados | 0 de 554 verificados por humano | `05-decomposicao/verificacao_efeitos.csv` |

Análise de erros: não se aplica sem padrão humano. Nenhuma âncora de validação foi excluída pela triagem de IA. O limiar de recall não foi atingido nem testado; o remédio previsto é a codificação humana das amostras (P006 e P007).

## 7. Seleção: decisões de IA e de humanos (R1; PRISMA 2020 item 16a)

Nas bases, 148 registros foram removidos pelo filtro automático de ano previsto no protocolo, e 1383 foram excluídos na triagem; nos outros métodos, 648 pelo filtro de ano e 898 na triagem (`07-relatorio/prisma_contagens.json`). Na triagem, a consolidação final registra 2210 decisões por consenso dos dois triadores de IA, 81 pela regra liberal e 336 humanas (exclusões por título de registros sem resumo, propostas pela IA e assumidas pelo revisor humano).

## 8. Governança de dados, direitos e ética (M10; RAISE 1 rec. 1.10)

- Provedores e termos: Anthropic, via Claude Code; uso para treino, retenção e localização dos dados a preencher pelos autores.
- Consentimento para o modo API: não se aplica (modo API não usado).
- Direitos autorais dos textos enviados: PDFs obtidos por fontes legítimas; Sci-Hub não foi usado; licença de cada texto a preencher pelos autores.
- Dados pessoais e LGPD: não houve processamento de dados pessoais além de metadados bibliográficos; e-mail de contato usado só como variável de ambiente para o *polite pool* do OpenAlex.

## 9. Interesses e financiamento (RAISE 1 rec. 1.9)

Custo de API registrado: não registrado (a triagem por subagentes do Claude Code não registra custo por chamada). Relação dos autores com a Anthropic e quem pagou o uso: a preencher pelos autores.

## 10. Limitações e impacto (D1)

Sem validação humana, não se sabe quantos estudos elegíveis a triagem de IA perdeu nem quantos erros há nos efeitos extraídos e nos julgamentos. Todos os modelos são do mesmo provedor, o que pode correlacionar erros entre avaliadores. O árbitro do risco de viés é o mesmo modelo do avaliador A e seguiu A em 79 de 88 domínios. O avaliador B errou mais a transcrição literal das citações, corrigida pelo coordenador. Modelos comerciais podem mudar sem aviso. A concordância entre agentes mede consistência, não acurácia.

## 11. Responsabilidade humana (RAISE 1 rec. 1.1)

As ferramentas de IA foram usadas nos papéis descritos acima, com supervisão humana limitada aos portões G1 e G2, às emendas, aos casos residuais de elegibilidade, às exclusões por título e à confirmação em bloco do consenso de risco de viés. As demais decisões de IA não foram validadas e estão listadas como pendências. Critérios, protocolo, decisões finais de elegibilidade, juízos de risco de viés e de certeza, síntese e conclusões serão de responsabilidade dos autores depois que eles conferirem as saídas; até lá, o manuscrito é rascunho não validado.
