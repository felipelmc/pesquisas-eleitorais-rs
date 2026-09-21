# Log de emendas ao protocolo

<!--
Como usar este arquivo
- Copie para 00-protocolo/emendas.md ANTES do G2. Arquivos de 00-protocolo/ cujo nome começa
  com "emenda" não são congelados no G2: este log continua editável depois do congelamento.
- Uma entrada por decisão, na ordem em que foram tomadas. Nunca apague entradas antigas.
- Escreva a entrada ANTES de alterar o artefato congelado. Depois de alterar, rode
  `$RS emenda --arquivo <arquivo alterado> --motivo "E00N: <resumo>" --por <papel>`
  e copie para a entrada o campo `versao` devolvido pelo comando.
- Contingência já prevista no protocolo não é emenda: registre só que foi acionada (tipo A).
- Esta é a fonte da seção "Diferenças entre protocolo e revisão" (PRISMA 2020 item 24c).
- Placeholders entre <>. Nada de nomes de pessoas: use papéis (revisor_humano_1...).
-->

Projeto: Exposição a pesquisas eleitorais publicadas → intenção de voto (bandwagon/underdog)
Protocolo congelado: v1.0 em (preencher no G2) | Registro: não registrado (o usuário pode registrar no OSF; anotar DOI/URL e data aqui)

## Resumo

| id | data | versão | seção afetada | tipo | etapa no momento | reexecução exigida |
|---|---|---|---|---|---|---|

Tipos: A contingência prevista acionada · B emenda antes da triagem · C emenda depois de ver dados ·
D método planejado não executado · E correção de erro ou incoerência.

| E001 | 2026-09-19 | v1.0 (protocolo não alterado) | seção 3, estratégia B01 | A | antes da busca definitiva | nenhuma |
| E002 | 2026-09-19 | v1.0 (protocolo não alterado) | seção 3, estratégia B01 → B05 | A | após a busca, antes da triagem | re-deduplicação e recall |
| Emenda 1 | 2026-09-20 | protocolo.md v2 | critério C2 | C | elegibilidade, ciclo 2 | não (afeta só Araujo2021/2021a) |
| Emenda 2 | 2026-09-20 | codebook_v0_efetividade.csv v2 | b2_estimando, b2_modelo_principal, b2_criterio_modelo_principal | C | piloto de extração (G6) | não (piloto não repetido; recodificação nos 3 textos do piloto na rodada completa) |

## E001

- **Data da decisão:** 2026-09-19
- **Versão:** protocolo v1.0 inalterado; string executada S-oa-en-v4 (o protocolo traz o rascunho S-oa-en-v3)
- **Arquivo(s) alterado(s):** `01-busca/strings/S-oa-en-v4.txt` (novo); nenhum arquivo congelado alterado
- **Seção / item:** protocolo, seção 3, validação da busca ("Se o PRESS mudar a B01, B02 a B04 são revistas...")
- **Texto anterior:** S-oa-en-v3 (1.130 registros, 2008+)
- **Texto novo:** S-oa-en-v3 + `OR "poll effects"` no nível superior + `"polling data"` nas frases de exposição dos fios T2 e T3 (1.235 registros; 19 de 19 âncoras de desenvolvimento)
- **Tipo e motivo:** A (contingência prevista acionada): a pré-revisão PRESS por subagente (`01-busca/prepress_S-oa-en-v3_ia.md`) achou estudos relevantes não recuperados. B02 a B04 revistas contra a mesma tabela de termos: sem mudança necessária (inconsistência menor apontada em PT, "voto estratégico" ausente do fio T1, sem efeito prático porque "voto útil" já está lá)
- **Etapa da revisão no momento:** antes da busca definitiva
- **Resultados já conhecidos quando se decidiu:** só contagens exploratórias
- **Impacto:** +105 registros a triar na B01
- **Ação:** B01 executada com S-oa-en-v4
- **Aprovado por:** autopiloto (contingência prevista no protocolo aprovado no G2)
- **Registro atualizado:** não se aplica (não registrado)
- **Evento no log:** não se aplica (nenhum arquivo congelado alterado)

## E002

- **Data da decisão:** 2026-09-19
- **Versão:** protocolo v1.0 inalterado; busca B01 (S-oa-en-v4) substituída pela B05 (S-oa-en-v5)
- **Arquivo(s) alterado(s):** `01-busca/strings/S-oa-en-v5.txt` (novo); nenhum arquivo congelado alterado
- **Seção / item:** protocolo, seção 3 ("âncora perdida leva a nova versão da string, com substituição da busca")
- **Texto anterior:** S-oa-en-v4 (1.235 registros); recall das âncoras de validação 15/19 (0,79; IC95% 0,54 a 0,94), perdidas A01, A07, A08, A19
- **Texto novo:** S-oa-en-v5 (1.438 registros): vocabulário de cobertura de pesquisas, volatilidade de voto, "polls" sem qualificador com voto estratégico, "efeitos das pesquisas" e divulgação de pesquisa. Recall 19/19 (1,00; IC95% 0,82 a 1,00)
- **Tipo e motivo:** A (contingência prevista acionada). Diagnóstico feito pelo subagente isolado, sem que o coordenador visse títulos. As 4 perdidas não estavam entre as marcadas `tambem_desenvolvimento`, logo o recall da v4 nas 8 âncoras independentes foi 4/8. Depois da correção, essas 4 deixam de ser teste independente: o recall final não é evidência independente de sensibilidade (relatado como limitação)
- **Etapa da revisão no momento:** após a busca definitiva, antes da triagem
- **Resultados já conhecidos quando se decidiu:** contagens da busca e recall das âncoras; nenhuma decisão de triagem
- **Impacto:** +203 registros na estratégia em inglês; 1.721 registros únicos ativos depois da re-deduplicação
- **Ação:** `rs.py buscar openalex --busca-id B05 ... --substituir B01`; `dedup`; `filtrar --ancoras`
- **Aprovado por:** autopiloto (contingência prevista no protocolo aprovado no G2)
- **Registro atualizado:** não se aplica (não registrado)
- **Evento no log:** `busca_substituida`

## Emenda 1 — 20/09/2026 — ampliação do critério C2
**O que muda.** A exposição elegível passa a incluir, além de resultado de pesquisa eleitoral (pesquisa isolada, média, agregador, projeção e boca de urna divulgada antes do fechamento das urnas), a **divulgação oficial de apuração parcial enquanto a votação ainda ocorre**.

**Por quê.** A bola de neve SN1 trouxe o estudo de Araújo e Gatto sobre as eleições brasileiras, em que urnas atrasadas por falha da biometria continuaram votando depois das 19:00, quando os resultados parciais já eram divulgados. É variação natural identificada, com desfecho de voto agregado por urna, e funcionalmente da mesma família que a boca de urna divulgada antes do fechamento — mas os próprios autores registram que não é pesquisa pré-eleitoral, e o C2 congelado no G2 não cobria o caso.

**Quando foi decidido.** Depois da consolidação da elegibilidade do ciclo 2, com o caso apresentado ao revisor humano junto de duas alternativas (excluir por C2, mantendo o critério congelado, ou incluir por emenda). O revisor humano escolheu incluir.

**Alcance.** Afeta os relatos Araujo2021 (preprint) e Araujo2021a (British Journal of Political Science), que são o mesmo estudo. Não reabre a triagem de títulos e resumos: nenhum registro foi excluído na ta_v1 por este ponto — os casos análogos que apareceram no texto completo (placar corrente em jogo de laboratório, Grupo B da fila humana) seguem excluídos por C2, porque contagem de votos do próprio jogo não é nem pesquisa nem apuração oficial de eleição real.

**Efeito na síntese.** Estudo com exposição de natureza distinta das demais: entra em célula própria no SWiM e não é agregado com os experimentos de pesquisa na meta-análise. A sensibilidade sem ele deve ser reportada.

## Emenda 2 — 20/09/2026 — redefinição de três variáveis do codebook de extração (b2)

**O que muda.** As redações de `b2_estimando`, `b2_modelo_principal` e `b2_criterio_modelo_principal` em `00-protocolo/codebook_v0_efetividade.csv` (bloco `13_Bloco_b2_quantitativo_explicativo`) passam de uma descrição geral para uma **ordem de decisão operacional**: `b2_estimando` passa a exigir discussão explícita de adesão/exposição no texto para classificar como ITT ou LATE, com ATE como padrão na ausência dessa discussão; `b2_modelo_principal`/`b2_criterio_modelo_principal` passam a seguir a ordem fixa declarado_pelos_autores → usado_na_interpretação (número repetido no resumo/conclusão) → regra_do_protocolo, com instrução explícita para listar mais de uma especificação quando o estudo trata amostras ou rodadas como igualmente centrais (ex.: primeiro e segundo turno).

**Por quê.** A recodificação cega do piloto de extração (G6), sobre 3 textos (Meer2015a, Klor2017a, Araujo2021a; `05-decomposicao/piloto/concordancia/RELATORIO_CONCORDANCIA.md`), encontrou concordância abaixo do limiar do protocolo (κ ou PABAK ≥ 0,7) nessas duas variáveis categóricas: `b2_estimando` (κ = 0,40) e `b2_criterio_modelo_principal` (κ = -0,50, pior que o esperado ao acaso). A leitura das divergências mostrou que os dois codificadores aplicavam critérios genuinamente diferentes (um usava a especificação declarada no corpo do texto, o outro a robustez ou a extensão citada na conclusão), não apenas palavreado distinto — o tipo de achado que a referência da skill (06-decomposicao.md, seção 5) trata como pedindo redefinição do codebook, não só arbitragem caso a caso.

**Quando foi decidido.** Na revisão humana das fichas do piloto (G6), pelo coordenador de IA em autopiloto (sem validação humana desta etapa, atalho do projeto), imediatamente após o relatório de concordância.

**Alcance.** Vale a partir de já para a rodada completa de extração. As três fichas do piloto (`05-decomposicao/piloto/fichas/`) não foram refeitas com a redação nova — repetir o piloto seria exigido só para uma mudança grande de desenho do codebook, e esta é uma clarificação pontual de três variáveis. Quando esses três textos entrarem na rodada completa de extração, serão fichados de novo (não reaproveitados do piloto), já com a redação desta emenda.

**Efeito na síntese.** Nenhum efeito direto nas células de síntese; efeito indireto esperado de melhorar a consistência de `b2_estimando` (usado para registrar o estimando do efeito, não a direção) e da localização do modelo principal (usada para saber qual estimativa de cada estudo entra na meta-análise/SWiM).
