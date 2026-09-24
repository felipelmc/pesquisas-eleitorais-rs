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
Protocolo congelado: v1.0 em 19/09/2026 (G2, evento seq 8) | Registro: não registrado (o usuário pode registrar no OSF; anotar DOI/URL e data aqui)

## Resumo

| id | data | versão | seção afetada | tipo | etapa no momento | reexecução exigida |
|---|---|---|---|---|---|---|

Tipos: A contingência prevista acionada · B emenda antes da triagem · C emenda depois de ver dados ·
D método planejado não executado · E correção de erro ou incoerência.

| E001 | 2026-09-19 | v1.0 (protocolo não alterado) | seção 3, estratégia B01 | A | antes da busca definitiva | nenhuma |
| E002 | 2026-09-19 | v1.0 (protocolo não alterado) | seção 3, estratégia B01 → B05 | A | após a busca, antes da triagem | re-deduplicação e recall |
| Emenda 1 | 2026-09-20 | protocolo.md v2 | critério C2 | C | elegibilidade, ciclo 2 | não (afeta só Araujo2021/2021a) |
| Emenda 2 | 2026-09-20 | codebook_v0_efetividade.csv v2 | b2_estimando, b2_modelo_principal, b2_criterio_modelo_principal | C | piloto de extração (G6) | não (piloto não repetido; recodificação nos 3 textos do piloto na rodada completa) |
| Emenda 3 | 2026-09-23 | codebook_v0_rob2/robins_i/epoc.csv (novos) | seção 7, codebooks de risco de viés | E | extração e RoB (G7), antes de qualquer avaliação | não |
| Emenda 4 | 2026-09-23 | v1.0 (protocolo não alterado) | seções 6 a 8: convenções de RoB geral EPOC, *momentum*, ICC imputado, consenso de RoB | C | depois da extração, antes de qualquer análise de efeito | não (4d substituída pela Emenda 6a) |
| Emenda 5 | 2026-09-23 | v1.0 (protocolo não alterado) | seção 8, síntese | C | depois da primeira síntese (G8) | SWiM, meta exploratória e GRADE refeitos |
| Emenda 6 | 2026-09-23 | v1.0 (protocolo não alterado) | seções 5 e 10: atribuição de decisões e registros sem resumo | E e C | depois do G9 | triagem complementar de 336 registros; texto completo dos que seguirem; síntese e relato refeitos |

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

## Emenda 3 — 23/09/2026 — codebooks de risco de viés copiados para o protocolo

**O que muda.** Entram em `00-protocolo/` os arquivos `codebook_v0_rob2.csv`, `codebook_v0_robins_i.csv` e `codebook_v0_epoc.csv`, cópias sem alteração dos codebooks da skill que a seção 7 do protocolo já nomeava como "codebook de partida". A única mudança de conteúdo é o preenchimento do placeholder de confundidores do ROBINS-I com a lista do DAG congelado no G2 (`apoio_latente`, `interesse_politico`, `preferencia_previa`/partidarismo; `00-protocolo/teoria_programa.md` e `dag_v1.mmd`).

**Por quê.** Correção de omissão (tipo E): a ferramenta e o codebook de cada desenho foram decididos no G2, mas os arquivos não foram copiados para a pasta congelada. Sem a cópia, os avaliadores de risco de viés não teriam um arquivo do projeto para ler.

**Quando.** Na etapa 9 (G7), antes de qualquer avaliação de risco de viés. Nenhum julgamento foi feito com outra versão.

**Alcance e efeito na síntese.** Nenhum: as perguntas e os algoritmos são os da versão nomeada no protocolo. O comando `rs emenda` não se aplica porque os arquivos são novos (não estavam congelados); a emenda fica registrada só aqui.

**Também registrado nesta data (desvio do plano de IA, seção 10):** o protocolo previa o árbitro dos desacordos de risco de viés em `claude-fable-5-1`. Por decisão de custo do revisor humano (19/09/2026), o árbitro será `claude-opus-5-5` em contexto novo, sem ver a própria avaliação A. Como A também é Opus, o árbitro não é um terceiro modelo independente; a limitação vai para o relato.

## Emenda 4 — 23/09/2026 — convenções de síntese decididas na etapa 9 (G7)

Decisões do `revisor_humano_1` por questionário, em 23/09/2026, depois da extração e antes de qualquer análise de efeito (nenhuma meta-análise ou SWiM tinha sido rodada).

**4a. `rob_geral` do EPOC.** Os critérios `cg_sequencia_aleatoria` e `cg_ocultacao_alocacao` ficam fora do algoritmo do geral (`--ignorar-no-geral`), porque são `alto` por definição em todo quase-experimento com grupo controle (os 5 resultados desse tipo tinham `alto` nos dois critérios, por concordância de A e B). O geral é o pior dos demais critérios, com `incerto` = moderado. *Por quê:* sem isso, o geral de todo estudo EPOC seria `alto` só pelo desenho, e o risco de viés não discriminaria entre os estudos (references/05-qualidade.md da skill, seção 4: convenção a declarar). *Efeito:* 6 dos 7 resultados EPOC continuam `alto` pelos demais critérios.

**4b. Efeitos de *momentum*.** Efeitos em que a pesquisa mostra o partido ganhando ou perdendo apoio, sem mostrar sua posição (ex.: Dahlgaard2016a, Social-Democratas), têm `alvo_efeito = nao_se_aplica` pela definição congelada e ficam fora da célula principal de `apoio_ao_lider`. Entram numa tabela de direção própria, ao lado dos efeitos de viabilidade, e numa análise de sensibilidade que os soma à célula principal (ganho = mostrado à frente). *Por quê:* o protocolo define o alvo pela posição mostrada, e ganho ou perda de apoio é outra informação (tendência); somá-la sem aviso mudaria a pergunta. *Alcance:* só a síntese; nenhuma extração muda.

**4c. Ajuste de conglomerado sem ICC relatado.** Nos efeitos de desenhos em conglomerado (sessão ou grupo de laboratório atribuído à condição; rodadas repetidas do mesmo grupo) sem EP já ajustado, a variância é multiplicada pelo efeito de desenho 1 + (m − 1)·ICC, com m = tamanho médio do conglomerado (participantes por grupo ou rodadas por grupo, o que for a unidade da estimativa) e ICC imputado = 0,05 na análise principal e 0,20 na sensibilidade. *Por quê:* nenhum estudo relata ICC, e sem ajuste a variância sai subestimada (Cochrane Handbook, cap. 23, ICC emprestado com análise de sensibilidade). A seção 6 do protocolo já pedia o ajuste com tamanho médio e ICC; a emenda só fixa o valor imputado. *Tipo:* desvio declarado.

**4d. Consenso de risco de viés.** *(Substituída pela Emenda 6a: a confirmação em bloco não aconteceu.)* As 88 propostas do árbitro (45 RoB 2, 34 ROBINS-I, 9 EPOC) foram confirmadas em bloco pelo `revisor_humano_1`, com trecho literal conferido por script. O árbitro seguiu o avaliador A em 79 domínios (90%), B em 7 e propôs terceiro valor em 2; como A e árbitro são o mesmo modelo, a proporção é declarada como possível viés de afinidade. Os 171 domínios concordantes entre A e B continuam sem validação humana (`validado_humano = 0`).

## Emenda 5 — 23/09/2026 — correções da síntese após o revisor metodológico do G8 (tipo C, decididas depois de ver os dados)

Motivo: o revisor metodológico (subagente, `06-analise/revisao_metodologica_g8.md`) apontou 2 problemas CRÍTICOS e 6 ALTOS na primeira síntese. As correções abaixo foram aplicadas pelo coordenador de IA em autopiloto, depois de ver resultados; por isso são declaradas como tipo C. As saídas anteriores estão em `06-analise/_superado_pre_revisao_g8/`, e as alterações nos CSVs de efeitos, linha a linha, em `05-decomposicao/correcoes_revisao_g8.csv` (cópia anterior em `05-decomposicao/efeitos_backup_pre_revisao_g8/`).

1. **Agrupamento (R01).** A SWiM principal volta à célula do protocolo: família × construto × comparador × célula de alvo × classe de desenho (`--grupo familia_intervencao,construto_outcome,comparador_tipo,celula_alvo --separar-desenho sim`). O agrupamento amplo (construto × célula de alvo × classe) fica como análise descritiva de sensibilidade, identificada como decidida depois de ver os dados.
2. **Convenção de sinal por alvo (R02).** `direcao_desejada` passa a seguir o alvo em todas as linhas de `apoio_ao_lider`: `aumentar` para líder, opção à frente no referendo e segundo viável; `reduzir` para azarão, terceiro inviável e partido perto da cláusula. Na célula de viabilidade, positivo = mais apoio à opção mostrada como viável ou menos apoio à mostrada como inviável (deserção estratégica). 49 linhas mudaram (Cornejo2023a, Freden2024a, Chatterjee2019a, Araujo2021a E02, Dahlgaard2016a Conservadores, Alabrese2024a, Gasperoni2015a E03, Meffert2012a, Witsman2016a E05). Linhas de `mobilizacao` passam a ter `alvo_efeito = nao_se_aplica` (95 linhas).
3. **Morton2015a E41.** O artigo imprime δ = −5,22 como mudança da inclinação depois da reforma de 2005, que retirou a exposição dos territórios ocidentais à boca de urna metropolitana. A linha registra +5,22, efeito da exposição, pela mesma regra já aplicada a Chatterjee2019a (efeito da proibição invertido para efeito da exposição).
4. **Efeitos fora da contagem principal (R03, R10, R13).** Efeitos principais que não estimam o contraste da exposição saem do teste de sinal e vão para a síntese narrativa de mecanismos e moderadores e para a sensibilidade `com_excluidos`: Lammers2022a E01/E03, Gandhi2019 E01/E03, Fichnova2015a E01/E05, Klor2017a E01, Urminsky2019 E01, Bursztyn2023a E01/E17, Alabrese2024a E002/E129, Meffert2011 E01 e Geers2018 E01 (motivos em `06-analise/montar_entradas_swim.py`).
5. **Risco crítico (R04).** A análise principal usa `--excluir-rob critico`, como o protocolo já previa; a versão com críticos é sensibilidade.
6. **Classe de desenho (R05).** Klor2017a E06 e Kaplan2019a E01 são contrastes antes e depois dentro do sujeito (avaliados com ROBINS-I): o `desenho` foi reescrito sem "RCT" e os dois passam à classe não randomizada.
7. **Meta-análise (R06, R07, R11).** Tyszler2015 E01 (proporções lidas de figura, sem EP) sai da meta-análise, como as notas de extração já pediam; sem ele nenhuma célula tem k ≥ 3 com g, e a síntese principal é só SWiM (contingência do protocolo). A meta de k = 3 com Tyszler2015 é relatada como exploratória, com REML + Hartung-Knapp (um efeito por estudo) e δ = 0,059 (2 p.p. convertidos com a mediana dos p0 da célula, 0,74). Timotei2013a recebe `cluster = 20` e `icc = 0,05` (Emenda 4c).
8. **Nulo por ±δ (R09).** Efeito principal com IC95 inteiro dentro de ±δ (0,044 para apoio, 0,046 para mobilização) entra na SWiM como nulo: Gerber2020a E12 e E31, Bursztyn2023a E17.
9. **Sinal sem t, β ou r.** Na entrada da SWiM, β recebe efeito_pp, p1 − p0 ou ln(OR) só para dar o sinal (coluna `beta_proxy_sinal`): Schlegel2023, Stolwijk2016a, Stolwijk2019b, Tal2015a.
10. **Sensibilidades (R08).** Rodadas no agrupamento amplo: sem contextos induzidos ou hipotéticos (`realismo_contexto = real`), sem dados anteriores a 2010 (Morton2015a e Chatterjee2019a recodificados para `ano_eleicao_pre2010 = sim`, pois a exposição é anterior às reformas de 2005 e 2010), sem Araujo2021a (Emenda 1), com os efeitos fora da contagem e com os críticos. O artigo como conglomerado no RVE não se aplica (não há meta principal).

## Emenda 6 — 23/09/2026 — correção de atribuição humana e triagem complementar dos registros sem resumo (tipos E e C)

**6a. Correção de atribuição (tipo E).** Na retomada de 23/09/2026, o revisor humano declarou que **não conferiu** decisões que o log e os arquivos registravam como suas. A tabela completa, evento a evento, está em `00-protocolo/correcao_atribuicao.csv` (449 linhas). Em resumo:

- **Não foram conferidas por humano:**
  - 336 exclusões na T/A de registros **sem resumo**, propostas pelos triadores de IA a partir do título (eventos `decisao_override` de 19 e 20/09, motivo "conferida e assumida pelo revisor humano");
  - as 88 propostas do árbitro de risco de viés que a Emenda 4d dava como "confirmadas em bloco";
  - 3 decisões de texto completo (seq 669 a 671) em que a IA estendeu a caso novo uma regra que o revisor tinha decidido para o Grupo B do ciclo 2;
  - a Emenda 2 (seq 718), decidida pelo coordenador de IA;
  - o fechamento do P034 (seq 782).
- **Confirmadas pelo revisor como decisões dele, tomadas na conversa:**
  - a aprovação do G1 e do G2;
  - a Emenda 1;
  - as 17 decisões de casos limítrofes de texto completo (seq 321 a 327 e 553 a 562; a seq 557 é uma linha de teste, substituída pela 558).

O `rs_log.jsonl` e o `dados/decisoes.jsonl` só aceitam acréscimo. Por isso as linhas antigas continuam lá, e esta emenda, junto com a tabela, é o registro da correção. Nos arquivos `04-qualidade/rob_*_consenso.csv`, `resolvido_por` passou de `revisor_humano_1` para `arbitro_ia:claude-opus-5-5`. Isso não muda nenhum julgamento e mantém `validado_humano = 0` em todo o RoB. A Emenda 4d fica substituída.

**6b. Registros sem resumo (tipo C, decidida pelo revisor humano em 23/09/2026, depois de ver os dados).** O revisor decidiu que **nenhum registro é excluído só pelo título**. Os 336 registros de 6a passam por uma etapa complementar feita só por IA, e o revisor dispensou a conferência dela:

1. O resumo é recuperado em fontes legítimas, nesta ordem: OpenAlex, Crossref, Semantic Scholar, Europe PMC e metadados da página do DOI. O que já tinha vindo em 19 e 20/09 é reaproveitado. Os arquivos ficam em `02-triagem/sem_resumo_revisao/`.
2. Dois triadores de IA independentes, A (`claude-sonnet-5`) e B (`claude-opus-5-5`), aplicam os critérios congelados de `02-triagem/prompts/ta_v1.md`, sem mudança, ao título e ao resumo recuperado. Vale a mesma regra liberal da ta_v1: o registro só é excluído se **os dois** excluírem, cada um com critério e trecho literal do resumo recuperado. Em qualquer outro caso ele segue ao texto completo. O TLDR automático do Semantic Scholar não serve de base para exclusão.
3. Registro sem resumo recuperado segue ao texto completo.
4. No texto completo, os registros que seguiram passam pelo fluxo usual: busca do PDF só em fontes legítimas, ficha de elegibilidade por subagente e `textos elegibilidade consolidar`. Os que não forem obtidos ficam como "não recuperados", nunca como excluídos.
5. As decisões entram no ledger por `triagem override --por ia_coordenador_emenda6`, porque é o único caminho do `rs.py` para substituir as linhas antigas. O comando grava `tipo_ator = humano` fixo. Por isso o papel (`ia_coordenador_emenda6`) e o motivo de cada linha dizem que a decisão é da IA, e esta emenda documenta a limitação. Nenhuma dessas linhas conta como validação humana no relato.

**Efeito.** Pode mudar o conjunto de incluídos. Se mudar, extração, RoB, síntese, GRADE e relato são refeitos pela cadeia do README. As contagens do PRISMA passam a mostrar as exclusões da etapa 6b à parte.

**Nota de 24/09/2026 (efeito da Emenda 6 e das correções de efeitos de 23/09).** O δ da célula pesquisa_pre_eleitoral × apoio_ao_lider × sem_pesquisa × principal × randomizado, definido pela Emenda 5 (item 7) como 2 p.p. convertidos pela mediana dos p0 da célula, foi recalculado com os efeitos corrigidos: mediana de p0 = 0,73, δ = 0,0573 (antes 0,74 e 0,059). A regra não mudou; mudaram os dados de entrada (`06-analise/_delta_celula.txt`).
