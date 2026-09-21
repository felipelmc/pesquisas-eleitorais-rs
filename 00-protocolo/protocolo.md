# Protocolo: efeitos da divulgação de pesquisas eleitorais sobre a intenção de voto (bandwagon e underdog), evidência publicada desde 2010: revisão rápida

Revisão sistemática de efetividade sem meta-análise obrigatória, variante rápida.

<!--
Protocolo a partir do modelo da skill revisao-sistematica (PRISMA-P 2015 entre colchetes; campos do registro geral do OSF).
Rascunho do coordenador (Claude Opus 5, via Claude Code) em 19/09/2026, revisado depois do relatório do revisor metodológico
(00-protocolo/revisao_metodologica_g2.md) e das decisões humanas de 19/09/2026; aprovação humana no G2.
-->

- **[1a] Tipo:** protocolo de revisão sistemática de efetividade sem meta-análise obrigatória (`--tipo efetividade_swim`), com meta-análise nas células comparáveis.
- **Variante:** rápida. Não há prazo externo: a variante declara os atalhos escolhidos pelo usuário. A1 a A4 foram aprovados no G1 (19/09/2026); A5 é proposto neste protocolo e aprovado no G2. Cada atalho está descrito na seção de método que altera:
  - (A1) fontes restritas a OpenAlex e BDTD, mais bola de neve pelo OpenAlex (seção 3);
  - (A2) triagem, elegibilidade, extração, risco de viés e certeza feitas por subagentes de IA, sem validação humana (seções 5, 6, 7, 9 e 10);
  - (A3) âncoras de validação da busca montadas por subagente isolado (seção 3);
  - (A4) PRESS feito só por subagente (seção 3);
  - (A5) sem contato com autores para textos ou dados faltantes (seção 6).
  Todos serão relatados como limitação do processo (PRISMA 2020, item 23c). A variante não usa o atalho de triagem do G4 com dupla humana parcial.
- **[1b] Atualização de revisão anterior?** Não no sentido formal. A revisão reúne a evidência publicada desde 2010, período posterior à última síntese formal identificada: Hardmeier (2008), "The effects of published polls on citizens", SAGE Handbook of Public Opinion Research, doi:10.4135/9781848607910.n48. O último ano de busca e de estudo incluído daquela síntese não foi verificado (capítulo sem texto aberto); a lacuna entre o fim da cobertura dela e 2009 é declarada como limitação. Não reaproveita dados daquela síntese.
- **Versão:** v1.0 | **Congelado em:** data do G2, registrada no log (`rs_log.jsonl`) | **Idioma dos produtos:** pt-BR
- **[2] Registro:** não registrado (decisão do `revisor_humano_1` em 19/09/2026). A revisão será relatada como não registrada; o protocolo congelado com sha256 no log e o pacote aberto (seção 11) são a salvaguarda contra mudanças *post hoc*.
- **[3a] Equipe e papéis:**
  - `revisor_humano_1`: único humano. Concepção, decisões de escopo, aprovação de G1 e G2, decisão dos casos residuais de elegibilidade e do consenso de risco de viés que o script exige de humano.
  - Coordenador de IA (Claude Opus 5, via Claude Code, skill `revisao-sistematica`): redige artefatos, executa os scripts e coordena subagentes.
  - Subagentes de IA (modelos na seção 10): triagem, elegibilidade, extração, risco de viés e rascunho de certeza.
- **[3b] Contribuições:** `revisor_humano_1` responde pela revisão (garantidor). A IA não é autora; seu uso é declarado pela declaração de uso de IA gerada do log (`rs.py declaracao-ia`).
- **[5a-5c] Financiamento e papel do financiador:** nenhum financiamento específico. **Conflitos de interesse:** nenhum declarado pelo `revisor_humano_1`.
- **[4] Plano de emendas:** log em `00-protocolo/emendas.md`; toda mudança datada, justificada, com etapa e resultados já conhecidos.

## 1. Pergunta e justificativa

**[6] Racional.** Pesquisas eleitorais publicadas são uma das informações mais difundidas nas campanhas. Desde 2010, o ambiente informacional mudou: agregadores de pesquisas e projeções probabilísticas ganharam espaço, e os resultados circulam por redes sociais, em contraste com o modelo anterior de pesquisa telefônica e imprensa tradicional. Ao mesmo tempo, o debate público sobre restringir a divulgação de pesquisas (proibições e embargos perto da eleição) depende de saber se a exposição altera o voto e em que direção.

A revisão sintetiza a evidência causal publicada desde 2010 sobre o efeito da exposição a resultados de pesquisas na intenção e na escolha de voto. Separa o efeito *bandwagon* (a favor de quem lidera) do *underdog* (a favor de quem está atrás), descreve o efeito sobre o comparecimento e marca os estudos sobre Brasil e América Latina para uma seção regional. É uma avaliação *ex post* de um fenômeno, não de um programa. Os usuários são pesquisadores e participantes do debate público sobre divulgação de pesquisas.

**Revisões existentes e registradas** (busca feita em 2026-09-19; detalhes em `00-protocolo/pergunta.md`, seção 4):

| Fonte consultada | Data | Termos | Revisões achadas | Decisão e em que esta difere |
|---|---|---|---|---|
| OpenAlex (listas `EX1` a `EX4`, sem importar; `EX3` com filtro de tipo revisão, lida inteira) | 2026-09-19 | termos de revisão AND termos de pesquisa eleitoral, *bandwagon*, *underdog*; `EX2` e `EX4` só no título | Hardmeier (2008), síntese com meta-análise; Moy & Rinke (2012), revisão narrativa; Barnfield (2019), revisão conceitual; revisões de *bandwagon* em marketing (2022) e credibilidade online (2023) e de precisão de pesquisas, fora do tema; revisão ampla de campanhas e comportamento eleitoral (2026) | Revisão nova da evidência publicada desde 2010, com protocolo, busca documentada, risco de viés por desenho e certeza por célula, ausentes das revisões posteriores a 2008. As revisões achadas são sementes da bola de neve e fonte das âncoras |
| OSF Registries (API, título) | 2026-09-19 | bandwagon; underdog; opinion polls; election polls; poll effects; pre-election polls | Nenhuma revisão registrada; só pré-registros de estudos primários | Seguir; os pré-registros de estudos incluídos servem só à avaliação de relato seletivo |
| BDTD (API VuFind) | 2026-09-19 | "pesquisas eleitorais"; "pesquisa eleitoral"; "pesquisas de intenção de voto"; bandwagon | Nenhuma revisão; teses sobre pesquisas eleitorais | Seguir |

**[7] Pergunta principal.** A exposição a resultados de pesquisas eleitorais publicadas altera a intenção ou a escolha de voto do eleitorado, em comparação com a não exposição ou com a exposição a outro resultado, e em que direção (*bandwagon* ou *underdog*)?

- **Escala:** (3) X sobre dois Y: uma família de exposição, com três formatos, sobre um desfecho principal (apoio ao líder) e um desfecho de dano (mobilização).
- **Perguntas secundárias:**
  - A exposição reduz o comparecimento (desmobilização)? Célula própria; decisão humana no G2 de admitir estudos só de comparecimento nessa célula.
  - Mecanismos (M): por quais canais (viabilidade e cálculo estratégico, heurística de consenso, conformidade, simpatia e equidade, emoções)?
  - Moderadores (Z): para quem, onde e quando o efeito é maior ou muda de sinal (tabela Z em `00-protocolo/teoria_programa.md`)?
  - Os achados diferem entre Brasil e América Latina e as demais regiões?
- **Stakeholders consultados:** não houve envolvimento; declarado como limitação.
- **Equidade (PROGRESS-Plus):** escolaridade, posição socioeconômica ou classe social e idade. Hipótese: *bandwagon* maior entre os de menor escolaridade e menor posição socioeconômica, pela heurística de consenso. Para idade não há hipótese de sinal. Os resultados por subgrupo serão extraídos quando relatados (variável `equidade_progress_plus`).

## 2. Framework e teoria do programa

**Framework** (PECO, exposição não atribuída por gestor): PECO define elegibilidade, blocos de busca e células de efeito. Mecanismos e moderadores orientam a extração e a síntese e **não** filtram estudos.

| Elemento | Definição operacional | Inclui | Não inclui | Nó do DAG |
|---|---|---|---|---|
| P (população/unidade) | Eleitores ou participantes que escolhem entre candidatos, partidos ou opções; unidades eleitorais agregadas | Eleições reais de qualquer nível e país; referendos e plebiscitos; eleições hipotéticas; jogos eleitorais de laboratório, inclusive com preferências induzidas, qualquer que seja o tamanho do grupo | Escolhas de consumo, mercado, finanças; votações de órgãos deliberativos reais (júri, comitê, conselho, legislativo) | população em que `apoio_ao_lider` e `desmobilizacao` são medidos |
| E (exposição; formatos = família) | Contato com resultado de pesquisa eleitoral | `pesquisa_pre_eleitoral`; `agregador_projecao`; `boca_de_urna` divulgada antes do fechamento das urnas. Manipulada em experimento, com variação natural identificada ou medida no indivíduo | Pesquisa usada só como fonte de dados; precisão e metodologia de pesquisas; cobertura de mídia sem desfecho de voto ou comparecimento; resultados de eleições passadas; mercados de apostas; métricas de redes sociais | `exposicao` |
| C (comparação) | Contraste que identifica o efeito da exposição | Sem pesquisa; o mesmo candidato mostrado atrás; outro resultado; antes e depois de proibição; unidades não expostas | Nenhum contraste | `exposicao` (níveis) |
| O (desfechos) | Tabela abaixo | Intenção de voto, escolha de voto, votação agregada; comparecimento (real, validado, agregado ou intenção de comparecer) | Só expectativa de vitória; só avaliação de candidato | `apoio_ao_lider`; `desmobilizacao` (medida pelo construto `mobilizacao`) |
| Contexto | Qualquer país; publicação desde 2010 | Brasil e América Latina marcados (`regiao`) | — | fora do grafo (tabela Z) |
| M (mecanismos) | Canais da teoria | viabilidade/estratégico, consenso, conformidade, simpatia/equidade, emoções | — | `percepcao_viabilidade`, `calculo_estrategico`, `heuristica_consenso`, `conformidade`, `simpatia_azarao`, `emocoes` |
| Z (moderadores; hipótese e direção) | Tabela Z da teoria | partidarismo (menor efeito se forte); sofisticação (teorias rivais); sistema eleitoral e número de competidores (maior com pluralidade e três ou mais); competitividade (mais *underdog* se apertada); formato (projeções: mais efeito em expectativas e desmobilização); momento (maior perto da eleição); tipo de eleição (maior em referendos); realismo (maior em hipotético e induzido); ano da eleição (sem hipótese de sinal); região (voto obrigatório elimina o canal da desmobilização); confiança nas pesquisas (menor efeito se baixa) | — | fora do grafo |

**Teoria da exposição:** `00-protocolo/teoria_programa.md` (níveis 1 a 3, tabela por elo com efeitos não intencionais, papéis das variáveis, tabela Z, teorias rivais) e diagrama `00-protocolo/dag_v1.mmd`, que inclui os confundidores `apoio_latente`, `interesse_politico` e `preferencia_previa` e o colisor `resposta_ao_survey`. A origem de cada seta está registrada; nenhuma foi conferida em texto completo nesta versão.

**[13] Desfechos** (`construto_outcome` e `direcao_desejada` serão copiados para a extração de efeitos):

| construto_outcome | Medidas aceitáveis | Janela | direcao_desejada | Benefício ou dano | Crítico ou importante | Critério de elegibilidade? | Elo da teoria |
|---|---|---|---|---|---|---|---|
| `apoio_ao_lider` | Intenção de voto declarada; escolha de voto declarada depois da eleição; escolha incentivada em experimento; votação agregada do candidato, partido ou opção que a pesquisa mostra à frente | Da exposição até o voto (imediata em experimentos; até o dia da eleição em estudos observacionais) | `aumentar` (convenção técnica de sinal, sem juízo normativo: g positivo = *bandwagon*, g negativo = *underdog*) | Nem benefício nem dano: desfecho descritivo com direção convencionada | crítico | sim (C3, opção a) | E2 a E6 |
| `mobilizacao` | Comparecimento declarado, validado ou agregado; intenção de comparecer; interesse ou busca de informação só como medida complementar | Até o dia da eleição | `aumentar` (queda = desmobilização) | Dano quando cai (incentivo perverso E7: complacência) | crítico | sim (C3, opção b; decisão humana no G2) | E7 |

Regras de sinal e de alvo para a extração:

- **Alvo do efeito** (`alvo_efeito`). A célula principal de `apoio_ao_lider` recebe só efeitos sobre o apoio a quem a pesquisa mostra à frente (`lider`, `opcao_referendo`) ou a quem ela mostra atrás numa disputa de dois (`azarao`). O efeito sobre o azarão entra com `direcao_desejada` = `reduzir`, e o sinal é invertido pelo script.
- **Efeitos de viabilidade em disputas com três ou mais competidores** (`segundo_viavel`, `terceiro_inviavel`, `partido_abaixo_clausula`) não entram na célula principal: somar deserção estratégica para o segundo colocado ao *underdog* por simpatia distorceria a resposta sobre a direção. Esses efeitos são extraídos e relatados numa tabela de direção própria, com síntese narrativa. Voto estratégico não é um construto separado (decisão humana no G1).
- **Randomização de quem aparece à frente:** o contraste é o apoio a um mesmo candidato mostrado à frente em comparação com mostrado atrás, analisado na célula do seu comparador (seção 8).

## 3. Fontes e busca

**[9] Fontes.** Atalho A1: só OpenAlex e BDTD, mais bola de neve.

- **Sem limite de idioma, tipo ou área na fonte.** O OpenAlex recebe um limite de data com margem (publicação desde 2008) para reduzir o volume anterior ao marco; a exclusão efetiva pelo ano de 2010 é feita pelo funil formal (seção 4).
- **Cobertura.** O OpenAlex agrega Crossref, repositórios e boa parte do conteúdo indexado em WoS, Scopus e SciELO.
- **Limitação declarada.** Não houve busca em WoS, Scopus e SciELO, nem em literatura cinzenta por sites. Não haverá contato com autores (A5).

| busca_id | Fonte | Plataforma / acesso | Tipo | Cobertura | Formato de exportação | Justificativa |
|---|---|---|---|---|---|---|
| B01 | OpenAlex, estratégia em inglês | API, `rs.py buscar openalex` (campo `title_and_abstract`), com chave de API do usuário (variável de ambiente, nunca gravada) | base | publicação 2008 até a data da busca | JSONL | Base multidisciplinar aberta com API; atalho A1 |
| B02 | OpenAlex, estratégia em português | idem | base | idem | JSONL | Literatura lusófona |
| B03 | OpenAlex, estratégia em espanhol | idem | base | idem | JSONL | Literatura latino-americana e espanhola |
| B04 | BDTD (IBICT) | API VuFind, campo `AllFields`, JSON baixado pelo coordenador e importado com `rs.py importar` | teses | todos os anos (volume pequeno); ano filtrado no funil | JSON (`bdtd_json`) | Teses e dissertações brasileiras, para a seção regional |
| SN1... | Busca por citação (para trás e para frente) | OpenAlex (`rs.py bola-de-neve`) | citação | — | JSONL | Sementes: todos os incluídos no texto completo e as revisões achadas (Hardmeier 2008; Moy & Rinke 2012; Barnfield 2019; a revisão de 2017 sobre pesquisas eleitorais e a de 2026 sobre campanhas, listadas em `pergunta.md`) |

**[10] Estratégia completa** (rascunho testado em 2026-09-19; as versões executadas ficam em `01-busca/strings/`; histórico de testes em `01-busca/strings/desenvolvimento.csv`; termos em `01-busca/strings/termos_v2.md`). Estrutura em quatro fios unidos por OR:

- **T1:** pesquisa ou projeção AND efeito nomeado (*bandwagon*/*underdog*);
- **S:** survey eleitoral AND efeito nomeado;
- **T2:** frases de exposição a resultado de pesquisa eleitoral AND frases de desfecho de voto;
- **T3:** frases de exposição AND comparecimento (célula `mobilizacao`).

Um bloco adicional de efeito ou desenho foi testado e rejeitado, porque perdeu estudos relevantes.

```text
B01 (S-oa-en-v3), OpenAlex, title_and_abstract, filtro publication_year:2008-2026:
((poll OR polls OR polling OR "election forecast" OR "election forecasting") AND (bandwagon OR underdog OR "band-wagon")) OR (("pre-election survey" OR "preelection survey" OR "electoral survey" OR "survey results" OR "opinion survey") AND (bandwagon OR underdog)) OR (("opinion poll" OR "election poll" OR "pre-election poll" OR "preelection poll" OR "poll result" OR "published poll" OR "exit poll" OR "polling information" OR "poll information" OR "poll numbers" OR "poll outcome" OR "horse race" OR "horse-race" OR "election forecast" OR "poll aggregator" OR "exposure to polls") AND ("vote choice" OR "vote intention" OR "voting intention" OR "voting behavior" OR "voting behaviour" OR "vote preference" OR "electoral behavior" OR "electoral behaviour" OR "electoral preference" OR "voting decision" OR "party preference" OR "candidate preference" OR "vote share" OR "strategic voting" OR "tactical voting" OR "party choice" OR "electoral choice" OR "voter preference" OR "electoral support" OR "party support" OR "candidate support")) OR (("opinion poll" OR "election poll" OR "pre-election poll" OR "preelection poll" OR "poll result" OR "published poll" OR "exit poll" OR "polling information" OR "poll information" OR "poll numbers" OR "poll outcome" OR "horse race" OR "horse-race" OR "election forecast" OR "poll aggregator" OR "exposure to polls") AND (turnout OR "turn out" OR abstention OR "electoral participation" OR "voter participation" OR "voting participation" OR demobilization OR demobilizes))

B02 (S-oa-pt-v3), idem:
((pesquisa OR pesquisas OR sondagem OR sondagens OR "boca de urna") AND (bandwagon OR underdog OR "efeito manada" OR "efeito de manada" OR "efeito vagão" OR "efeito de arrasto" OR "efeito carona" OR "voto útil")) OR (("pesquisa eleitoral" OR "pesquisas eleitorais" OR "pesquisa pré-eleitoral" OR "pesquisas pré-eleitorais" OR "pesquisa de intenção de voto" OR "pesquisas de intenção de voto" OR "sondagem eleitoral" OR "sondagens eleitorais" OR "boca de urna" OR "divulgação de pesquisas eleitorais" OR "divulgação das pesquisas eleitorais") AND ("intenção de voto" OR "intenções de voto" OR "decisão de voto" OR "decisão do voto" OR "escolha eleitoral" OR "comportamento eleitoral" OR "comportamento do eleitor" OR "preferência eleitoral" OR "voto útil" OR "voto estratégico" OR efeito OR efeitos OR influência OR impacto)) OR (("pesquisa eleitoral" OR "pesquisas eleitorais" OR "pesquisa pré-eleitoral" OR "pesquisas pré-eleitorais" OR "pesquisa de intenção de voto" OR "pesquisas de intenção de voto" OR "sondagem eleitoral" OR "sondagens eleitorais" OR "boca de urna") AND (comparecimento OR abstenção OR "participação eleitoral" OR "abstenção eleitoral" OR "comparecimento eleitoral"))

B03 (S-oa-es-v3), idem:
((encuesta OR encuestas OR sondeo OR sondeos OR "boca de urna") AND (bandwagon OR underdog OR "efecto arrastre" OR "efecto de arrastre" OR "carro ganador" OR "carro del ganador" OR "voto útil" OR "voto estratégico")) OR (("encuesta electoral" OR "encuestas electorales" OR "encuesta preelectoral" OR "encuestas preelectorales" OR "sondeo electoral" OR "sondeos electorales" OR "sondeos preelectorales" OR "encuestas de intención de voto" OR "boca de urna" OR "publicación de encuestas electorales" OR "difusión de encuestas electorales" OR "publicación de sondeos") AND ("intención de voto" OR "intenciones de voto" OR "decisión de voto" OR "comportamiento electoral" OR "preferencia electoral" OR "preferencias electorales" OR "voto útil" OR "voto estratégico" OR efecto OR efectos OR influencia OR impacto)) OR (("encuesta electoral" OR "encuestas electorales" OR "encuesta preelectoral" OR "encuestas preelectorales" OR "sondeo electoral" OR "sondeos electorales" OR "sondeos preelectorales" OR "encuestas de intención de voto" OR "boca de urna") AND ("participación electoral" OR "abstención electoral" OR abstención OR "concurrencia a las urnas" OR "participación en las elecciones"))

B04 (S-bdtd-v3), BDTD, AllFields, sem limite:
"pesquisa eleitoral" OR "pesquisas eleitorais" OR "pesquisa pré-eleitoral" OR "pesquisas pré-eleitorais" OR "pesquisa de intenção de voto" OR "pesquisas de intenção de voto" OR "sondagem eleitoral" OR "sondagens eleitorais" OR "boca de urna" OR "divulgação de pesquisas eleitorais" OR "divulgação das pesquisas eleitorais" OR "voto útil" OR "efeito bandwagon" OR "efeito underdog"
```

**Contagens do teste** (2026-09-19, publicação desde 2008):

- B01 = 1.130;
- B02 = 118 e B03 = 131 (contagens com a chave de API do OpenAlex, 2026-09-19);
- B04 = 80 (todos os anos).

A B01 recupera 14 das 14 âncoras de desenvolvimento de voto e as 8 de comparecimento. São cerca de 1.460 registros antes da deduplicação, acima da capacidade de referência da triagem dupla por subagentes (cerca de 800); a contingência da seção 9 (mais ondas) já está acionada.

**Validação da busca:**

- **PRESS 2015** (checklist `assets/checklists/press.csv`) da estratégia B01. Atalho A4: a revisão é feita por um subagente que não escreveu a string, e a pendência `revisao_press` fica aberta. Se o PRESS mudar a B01, B02 a B04 são revistas a partir da mesma tabela de termos antes da execução, com nova versão registrada.
- **Âncoras de validação** em `00-protocolo/ancoras_validacao.csv` (19 âncoras). Atalho A3: montadas por subagente isolado, a partir das listas de referências de Moy & Rinke (2012) e Barnfield (2019) e das citações para frente de Hardmeier (2008), Barnfield (2019) e das próprias âncoras; o arquivo é lido só pelos scripts.
  - As âncoras que também são de desenvolvimento estão marcadas `tambem_desenvolvimento` (11 de 19). O recall será relatado com e sem elas; o recall informativo é o das 8 independentes.
  - Não houve âncora escrita em português ou espanhol: as buscas B02 a B04 ficam sem validação de recall, o que é declarado como limitação.
- **Cálculo do recall.** O recall é calculado com todos os filtros em modo etiquetar (`01-busca/filtros_v1.json`), antes da versão com exclusão por ano (`filtros_v2.json`). A meta é recuperar todas as âncoras indexadas; âncora perdida leva a nova versão da string, com substituição da busca (`--substituir`). O recall relativo é relatado por fonte. Há alerta se mais de 30% dos incluídos vierem só da bola de neve.

**Atualização:** rodar de novo todas as fontes se a última busca tiver mais de 12 meses na data prevista de divulgação. **Log:** PRISMA-S em `01-busca/log_buscas.csv`.

## 4. Elegibilidade

**[8] Características dos estudos:**

| Critério (mesmo id em `02-triagem/prompts/ta_vN.md` e em `00-protocolo/codebook_elegibilidade.csv`) | Inclui | Exclui | Justificativa |
|---|---|---|---|
| C1 População e contexto | Eleitores ou participantes que escolhem entre candidatos, partidos ou opções de referendo ou plebiscito, em eleição real, hipotética ou de laboratório (inclusive com preferências induzidas, qualquer que seja o tamanho do grupo ou da sessão), em qualquer país; unidades eleitorais agregadas | Escolhas de consumo, mercado, tecnologia, finanças; votações de órgãos deliberativos reais (júri, comitê, conselho, legislativo) | Pergunta sobre comportamento eleitoral; casos-limite decididos pelo usuário no G1 |
| C2 Exposição estudada como objeto empírico (não só mencionada) | Resultado de pesquisa eleitoral (pré-eleitoral, agregador ou projeção, boca de urna antes do fechamento das urnas; e, por emenda de 20/09/2026, divulgação oficial de apuração parcial enquanto a votação ainda ocorre) como exposição manipulada, com variação natural identificada ou medida no indivíduo | Pesquisa só como contexto, motivação ou fonte de dados; precisão e metodologia de pesquisas; cobertura de mídia sem desfecho de voto ou comparecimento; eleições passadas, mercados de apostas, métricas de redes sociais como exposição | Define a exposição da pergunta |
| C3 Desfecho do protocolo medido ou analisado (falta de dado numérico não exclui) | (a) Intenção de voto, escolha de voto ou votação agregada que permita comparar o apoio ao que a pesquisa mostra à frente com o apoio ao que mostra atrás; ou (b) comparecimento real, validado, agregado ou intenção de comparecer (célula `mobilizacao`) | Só avaliação ou simpatia sem medida de voto nem de comparecimento; só expectativa de vitória; só busca de informação; financiamento de campanha | Decisões do usuário: voto como desfecho principal (G1) e comparecimento admitido na célula de dano (G2) |
| C4 Desenho elegível, com o comparador exigido (pelas características, não pelo rótulo) | Experimento aleatorizado (survey, laboratório, campo, online); experimento natural ou quase-experimento com variação identificada (proibição, embargo, fuso horário, calendário de divulgação, diferenças em diferenças, descontinuidade, série interrompida); painel individual com exposição medida antes do desfecho e comparação entre níveis de exposição | Observacional agregado sem variação identificada (tendências de pesquisa comparadas ao resultado, "momentum"); percepção autodeclarada de influência sem comparação; simulação ou modelo teórico sem dados; estudo qualitativo, normativo ou teórico | Pergunta de efeito; decisão do usuário sobre estudos agregados |
| C5 Estudo primário (revisões e meta-análises NÃO são estudos: vão para bola de neve e validação da busca) | Estudo com análise própria de dados | Revisão de literatura, revisão sistemática, meta-análise, editorial, ensaio sem dados | Evita dupla contagem |
| C6 Sem retratação | Sem aviso de retratação | Retratado | Integridade. Checado no texto completo, no OpenAlex e na Crossref (`rs.py textos retratacoes`); para textos sem DOI, o coordenador confere a página da editora ou do repositório e registra a conferência |

**[8] Características dos relatos:**

- **Anos de publicação.** De 2010-01-01 até a data da última busca. O marco é a mudança no ambiente informacional (agregadores e redes sociais) e o intervalo desde a última síntese formal (Hardmeier, 2008). O recorte vale para a data de publicação, não para os dados; o ano da eleição estudada é moderador, com análise de sensibilidade sem os estudos de dados anteriores a 2010.
  - **Definição operacional do ano:** `publication_year` do OpenAlex (primeira publicação, inclusive *online first*) e o ano de defesa na BDTD.
  - **Limitação declarada:** estudos publicados entre o fim da cobertura de Hardmeier (2008), não verificado, e 2009 ficam fora desta revisão.
- **Idiomas:** sem restrição (decisão humana no G2): todo documento achado é lido pelos subagentes, em qualquer idioma. As estratégias de busca são em inglês, português e espanhol, e documentos em outros idiomas entram quando indexados com título ou resumo que as estratégias alcançam; declarado como limitação da busca.
- **Status de publicação:** qualquer (artigos, teses, dissertações, capítulos, relatórios, textos para discussão, *working papers*, *preprints*).

Regras:

- Estudos que cobrem só parte da população elegível: entram, e a análise usa a parte elegível quando o estudo a relata separadamente.
- Estudos que não relatam o desfecho de forma utilizável: não são excluídos por isso; entram na síntese pela direção, se houver, ou são listados.
- Texto não obtido: "não recuperado" no PRISMA, nunca excluído por critério.
- **Funil formal (filtros):**
  - `01-busca/filtros_v1.json`: todos os filtros em modo etiquetar (ano, tipo, idioma, dicionário de método), usado para o recall das âncoras.
  - `01-busca/filtros_v2.json`: igual, exceto o filtro de ano em modo excluir (publicação anterior a 2010; registro sem ano segue para a triagem), previsto aqui como exclusão determinística por metadado com a definição operacional acima. Não há exclusão por dicionário nem por idioma, portanto não há amostra de elusão de filtro. Se o filtro excluir alguma âncora, o script sai com código 2 e o filtro é revisto.

## 5. Seleção

- **[11a] Gestão dos registros:** `dados/registros.csv` (importação), `dados/registros_unicos.csv` (dedup auditável; os pares candidatos ficam como pendência `dedup_candidatos`, sem decisão da IA), `dados/decisoes.jsonl` (ledger), sempre via `rs.py`.
- **[11b] Triagem de títulos e resumos** (atalho A2):
  - dois revisores de IA independentes, A e B, em modelos distintos, com lotes de 25 registros e ondas de até 4 subagentes;
  - consolidação pela regra liberal: basta um revisor incluir ou marcar incerto para o registro seguir ao texto completo. Não há árbitro, porque na regra liberal ele não pode excluir; as divergências ficam na fila humana (pendência `fila_humana_triagem`) só para relato;
  - registro sem resumo nunca é excluído (vira incerto); incerto segue ao texto completo;
  - critérios versionados em `02-triagem/prompts/ta_vN.md`. Os exemplos VÁLIDO e INVÁLIDO do prompt saem das âncoras de desenvolvimento (`01-busca/ancoras_desenvolvimento.csv`) e das listas exploratórias `EX1` a `EX4`, nunca de registros sorteados para as amostras de validação, elusão ou estabilidade.
- **Calibração humana:** não se aplica (atalho A2: não há dupla humana). A concordância entre A e B é relatada como consistência entre agentes, não como acurácia. As amostras de validação e de elusão serão preparadas pelo script e deixadas como pendência `validacao_humana` para eventual codificação humana posterior.
- **Texto completo:**
  - um subagente por PDF propõe a elegibilidade com trecho verbatim e página, conferidos pelo gate de citações da skill `fichamento-sistematico`;
  - proposta com citação reprovada é refeita por outro subagente;
  - o que continuar incerto vai ao `revisor_humano_1`, que decide incluir, excluir ou aguardando classificação (exigência do PRISMA, que não fecha com incerto);
  - motivos de exclusão pelo primeiro critério que falha;
  - PDF conferido contra a referência (PDF de outro trabalho = não recuperado);
  - relatos do mesmo estudo ligados antes da extração (preprint e versão publicada nunca fundidos);
  - retratações checadas (C6).
- **Bola de neve:** rodadas SN1, SN2... sobre os incluídos, re-triadas com a mesma versão dos critérios, até uma rodada sem novas inclusões.

## 6. Extração (sistematização)

- **[11c] Piloto:** 2 a 3 estudos de desenhos diferentes (um *survey experiment*, um de laboratório, um experimento natural, conforme disponíveis) antes da extração completa (portão G6); fichas conferidas por um segundo subagente.
- **[12] Codebook v0:** `00-protocolo/codebook_v0_efetividade.csv`, com o bloco comum e o bloco b2 de `oqf_decomposicao.csv` adaptados à exposição.
  - Retirados: implementação, custo, percepção e vínculo com gestor (não se aplicam a exposição).
  - Acrescentados: `regiao`, `tipo_eleicao`, `sistema_eleitoral`, `voto_obrigatorio`, `desenho_fino`, `realismo_contexto`, `ano_eleicao`, `comparador_tipo`, `nivel_desfecho`, `margem_mostrada`, `mecanismo_testado`, `moderadores_relatados`, `alvo_efeito`, `n_competidores`, `dias_ate_eleicao`, `ajuste_mediador`.
  - O codebook de elegibilidade é `00-protocolo/codebook_elegibilidade.csv`.
- **Dupla extração** (atalho A2):
  - números de efeito extraídos por subagente com trecho e página e conferidos pelo `rs.py analise verificar-efeitos` (trecho na página, plausibilidade), sem verificação humana (decisão humana no G2): a pendência `verificacao_humana_efeitos` fica aberta;
  - variáveis categóricas recodificadas às cegas por outro subagente em max(20%, 10) estudos, exigindo κ ou PABAK de pelo menos 0,7 e concordância de pelo menos 80% por variável (senão redefinir e recodificar);
  - a concordância entre agentes mede consistência, não acurácia.
- **Contato com autores:** não haverá (atalho A5). Dados faltantes são relatados e tratados na sensibilidade e na síntese por direção.
- **Regra de modelo principal** (escrita antes da extração), na ordem:
  1. o modelo que os autores declaram principal;
  2. na falta, o de especificação completa pré-especificada;
  3. o mais próximo do dia da eleição, na janela do desfecho;
  4. empate: o primeiro da tabela principal.
  Nunca o mais significativo.
- **Unidade de análise:**
  - Estudo = amostra independente: experimento com participantes próprios, ou eleição ou país distinto. Um artigo com vários experimentos independentes tem um `id_estudo` por experimento (`<id_rs>_e1`, `<id_rs>_e2`). A sensibilidade trata o artigo como conglomerado no RVE.
  - Relato (`id_rs`) e efeito (`id_efeito`) seguem a hierarquia estudo, relato, efeito.
  - O estimando é registrado (ATE, ITT, LATE, ATT, RDD local, associação), com ajuste para conglomerados quando a sessão ou a unidade agregada é atribuída (tamanho médio e ICC).
- **Regras de efeito específicas desta literatura:**
  - Experimentos: o campo `desenho` sempre descreve a atribuição com a palavra "randomizado" (ex.: "survey experiment randomizado"), para a separação automática entre randomizados e não randomizados.
  - Colunas acrescentadas ao CSV de efeitos, depois de `se_pp`: `comparador_tipo`, `alvo_efeito`, `desenho_fino`, `regiao`, `tipo_eleicao`, `realismo_contexto`, `ano_eleicao_pre2010` (sim ou não), `sistema_eleitoral`.
  - Multibraço (líder à frente, líder atrás, controle): quando há braço de controle, extraem-se só os contrastes de cada braço com o controle; o contraste entre braços só é extraído quando não há controle. Os efeitos do mesmo estudo são tratados com CHE.
  - Subgrupos (apoiadores do líder, do azarão, indecisos) na coluna `subgrupo`.
  - Logit e probit: preferir o efeito marginal em pontos percentuais com a proporção do grupo de comparação (`efeito_pp`, `p0`). Na falta dele, logit com OR = exp(β) e IC exponenciado é uma transformação pré-especificada, marcada como aproximada; probit sem efeito marginal fica só na síntese por direção.
  - Votação agregada em pontos percentuais: rota de coeficiente padronizado pelo desvio-padrão da votação (`beta_sd`).
  - Efeito direto (modelo com `ajuste_mediador` = Sim, isto é, ajustado pela expectativa de vitória) nunca é agregado com efeito total; entra só na síntese narrativa de mecanismos.

## 7. Risco de viés

**[14] Ferramenta por desenho** (julgamento por domínio, com trecho). Atalho A2:

- O subagente A e o subagente B avaliam de forma independente.
- Onde A e B concordam, o consenso é automático.
- Nos desacordos, um árbitro-subagente propõe o consenso, e o `revisor_humano_1` o confirma, porque o script só aceita consenso humano.
- `rob_geral` sai do algoritmo de cada ferramenta.

| Desenho | Ferramenta | Codebook de partida (`assets/codebooks/`) | Nível | Uso na síntese |
|---|---|---|---|---|
| Experimento aleatorizado individual (survey, online, laboratório por indivíduo) | RoB 2 | `rob2.csv` | desfecho | Estratificação por risco e GRADE. O domínio 4 considera o desfecho autodeclarado e a demanda do experimentador |
| Experimento aleatorizado por sessão ou grupo | RoB 2, variante por conglomerado (D1b) | `rob2.csv` | desfecho | idem |
| Experimento natural ou quase-experimento com dados individuais; painel individual | ROBINS-I V2 (+ Waddington 2017) | `robins_i.csv` | desfecho | idem |
| Proibição, embargo ou calendário com unidades agregadas (diferenças em diferenças, controle sintético, série interrompida) | EPOC | `epoc.csv` | desfecho | idem; ponto de partida do GRADE na seção 9 |
| Exposição não atribuída (painel com exposição medida) | ROBINS-E seria o canônico; sem codebook na skill, usa-se ROBINS-I V2 com a limitação declarada | `robins_i.csv` | desfecho | idem |
| Qualitativo, transversal descritivo, métodos mistos | Não se aplica: fora do critério C4 | — | — | — |
| Elegibilidade de desenho (não é RoB) | Maryland SMS | não usado | — | Não se aplica: o desenho entra pelo C4, descrito por características |

**[16] Metavieses:**

- **Viés de publicação:** funil, Egger e PET-PEESE com erro-padrão modificado, e seleção 3PSM, só em células com k igual ou maior que 10.
- **Evidência faltante por célula:** juízo estruturado inspirado no ROB-ME, sem codebook na skill, rascunhado por subagente. Usa os pré-registros citados nos estudos (variável `registro_financiamento` do codebook de elegibilidade), desfechos medidos mas não relatados e a limitação de fontes (A1). Alimenta o domínio de viés de publicação do GRADE.

## 8. Síntese

**[15a] Critérios de comparabilidade** (checklist antes de agregar; o que não se encaixa vai para a síntese sem meta-análise pelo SWiM):

| Dimensão | Agrupa junto quando | Separa quando |
|---|---|---|
| Família de exposição (`familia_intervencao`) | mesmo formato: `pesquisa_pre_eleitoral`, `agregador_projecao` ou `boca_de_urna` | formatos diferentes |
| Comparador (`comparador_tipo`) | mesmo tipo de contraste | sempre separa: exposto × sem pesquisa; à frente × atrás ou outro resultado; antes × depois de proibição ou unidades não expostas |
| Construto do desfecho (`construto_outcome`) | `apoio_ao_lider` com medidas individuais ou agregadas alinhadas por direção, alvo `lider`, `opcao_referendo` ou `azarao` | `mobilizacao` sempre separado; alvos de viabilidade fora da célula (seção 2) |
| Janela de medida | imediata (experimentos) ou até o dia da eleição | não separa; entra como descritor |
| População / unidade | indivíduos; unidades agregadas analisadas à parte na classe não randomizada | — |
| Estimando | ATE e ITT juntos em experimentos | LATE, ATT e RDD local analisados em separado; painéis com estimando de associação ficam fora das meta-análises e entram só no SWiM e na síntese por direção |
| Desenho | randomizados e não randomizados nunca agregados juntos | sempre |

Célula = família × construto × comparador × classe de desenho (`rs.py analise meta --grupo familia_intervencao,construto_outcome,comparador_tipo --separar-desenho sim`).

**[15b] Medida e modelo:**

- **Medida.** g de Hedges alinhado por `direcao_desejada`: para `apoio_ao_lider`, g positivo = *bandwagon*; para `mobilizacao`, g negativo = desmobilização.
- **Conversões** com `formula_id` e `aproximado`. Desfechos binários (proporções, efeitos em pontos percentuais de LPM, DiD ou RDD, e razão de riscos) são aceitos e convertidos a d pelo log OR com a proporção do grupo de comparação; os aproximados vão para a sensibilidade.
- **Modelo.** Efeitos aleatórios REML com Hartung-Knapp; τ² com IC (interpretado só com k de pelo menos 5), I², Q e intervalo de predição.
- **Agregação** só com k de pelo menos 3 estudos (`--k-min 3`).
- **Dependência:** CHE + RVE (CR2), ρ = 0,6, com sensibilidade em 0,2, 0,5 e 0,8; graus de liberdade de Satterthwaite abaixo de 4 = não confiável. Estudos com um só efeito entram com esse efeito; com vários, pela estrutura CHE, com a regra de modelo principal definindo o modelo de cada contraste.
- **Risco crítico:** a análise principal exclui resultados em risco crítico (`--excluir-rob critico`), que ficam na revisão e entram numa análise de sensibilidade com eles.

**[15c] Heterogeneidade, subgrupos e sensibilidade:**

- **Moderadores pré-especificados,** com a direção da tabela Z:
  - `desenho_fino`;
  - `realismo_contexto` (maior em hipotético e induzido);
  - `tipo_eleicao` (maior em referendos);
  - `regiao` (Brasil, América Latina, outro; sem hipótese de sinal para `apoio_ao_lider`; menor desmobilização sob voto obrigatório);
  - ano da eleição antes e depois de 2010 (`ano_eleicao_pre2010`; sem hipótese);
  - `sistema_eleitoral` e `n_competidores` (maior com pluralidade e três ou mais competidores).
- **Limites de k:**
  - estimativa por subgrupo só com k de pelo menos 3 por nível;
  - teste de diferença entre subgrupos só com pelo menos 4 estudos por nível;
  - abaixo disso, estimativas lado a lado sem teste;
  - meta-regressão com cerca de 10 estudos por covariável;
  - intervalo de predição interpretado só com k de pelo menos 5.
- **Sensibilidade:**
  - leave-one-out;
  - sem risco alto;
  - com os resultados em risco crítico;
  - sem conversões aproximadas;
  - sem estudos de dados anteriores a 2010;
  - sem contextos induzidos;
  - artigo como conglomerado no RVE;
  - seleção 3PSM (k de pelo menos 10).

**Limiar de relevância e magnitude.** Convenção deste protocolo, sem benchmark de campo verificado. Conversão de pontos percentuais para g pelo log OR (d = ln(OR) · √3/π).

- **δ para medidas binárias individuais:** 2 pontos percentuais, convertidos para g com a proporção de referência de cada célula, isto é, a mediana dos `p0` (proporção do grupo de comparação) dos efeitos da célula. A proporção de referência é uma característica do grupo de comparação, não do efeito, e fica registrada antes da interpretação.
- **δ para votação agregada (rota `beta_sd`):** 2 pontos percentuais divididos pelo desvio-padrão de referência da votação na célula (mediana dos DP reportados).
- **Células mistas ou sem `p0`:** δ padrão calculado com referência 0,50 (`apoio_ao_lider`) ou 0,60 (`mobilizacao`).

| construto_outcome | δ / SESOI (unidade natural) | δ em g com a referência padrão | Fonte do δ | Faixas de magnitude (g, referência padrão; o limite superior de trivial é o próprio δ) | Fonte das faixas |
|---|---|---|---|---|---|
| `apoio_ao_lider` | 2 pontos percentuais no apoio ao líder | 0,044 (referência 0,50) | Convenção: magnitude capaz de mudar o vencedor em disputas apertadas | trivial:0, pequena:0.044, moderada:0.088, grande:0.133 (2, 4 e 6 pontos percentuais) | Convenção deste protocolo |
| `mobilizacao` | 2 pontos percentuais no comparecimento | 0,046 (referência 0,60) | Convenção | trivial:0, pequena:0.046, moderada:0.094, grande:0.142 (2, 4 e 6 pontos percentuais) | Convenção deste protocolo |

**[15d] Sem meta-análise:**

- SWiM: agrupamento como acima, métrica padronizada, direção pelo estimador, teste de sinal binomial exato bilateral, *effect direction plot*, *albatross plot* quando só há p e n.
- Nunca "sem efeito" por p acima de 0,05. Um g próximo de zero é classificado pelo IC frente a ±δ.
- A hipótese de efeitos opostos que se anulam (*bandwagon* num grupo, *underdog* em outro) só é afirmada quando pelo menos 3 estudos relatarem estimativas por subgrupo com sinais opostos; sem isso, é relatada como hipótese não testada.
- Testes combinados (Stouffer, Winer, Cooper, Fisher): não se aplica. O Stouffer da skill é unilateral e a pergunta é bilateral; não serão rodados.

**Síntese qualitativa e integração:** não se aplica como síntese qualitativa formal (revisão só de efeito). Os mecanismos testados (`mecanismo_testado`), os moderadores relatados e os efeitos de viabilidade em disputas com três ou mais competidores terão síntese narrativa estruturada, com os estudos de suporte.

**Seção regional (Brasil e América Latina):** tabela dos estudos com `regiao` igual a `brasil` ou `america_latina`. Terá estimativa por subgrupo se k for de pelo menos 3 por nível; se não, estimativas lado a lado e síntese por direção, com discussão do voto obrigatório e do contexto regulatório. Se não houver estudo da região, a seção relata a ausência de evidência.

**Regras da caixa de ferramentas:** não se aplica. A caixa OQF é opcional em `efetividade_swim`, e suas linhas de implementação, percepção e custo não se aplicam a uma exposição.

## 9. Certeza e da evidência à prática

- **[17] GRADE por célula de efeito:**
  - A indireção inclui o contexto eleitoral e institucional, o realismo do experimento (hipotético ou induzido frente a eleição real) e o estimando.
  - A imprecisão é julgada frente a δ.
  - Sem meta-análise, segue Murad 2017.
  - Atalho A2: o juízo é rascunhado por subagente com `validado_humano` = 0 e fica como pendência `certeza_humana`.
  - GRADE-CERQual: não se aplica (sem achados qualitativos).
  - Desfechos da tabela de resumo, escolhidos antes de ver resultados: `apoio_ao_lider` por formato de exposição, comparador e classe de desenho; `mobilizacao`.
- **Pontos de partida:**
  - randomizados começam em alta;
  - não randomizados avaliados com ROBINS-I V2 começam em alta, com rebaixamento por risco de viés;
  - corpos avaliados só com EPOC começam em baixa, porque o EPOC não examina confundimento e seleção contra um ensaio-alvo com a profundidade do ROBINS-I;
  - célula com as duas ferramentas: ponto de partida único baixo, justificado por célula.
- **Da evidência à prática:** EtD simplificado não se aplica como recomendação (é uma exposição, não uma intervenção). As implicações para o debate sobre divulgação de pesquisas serão discutidas narrativamente, sem recomendação mais forte que a certeza.
- **Fatores de transferibilidade para o Brasil:** voto obrigatório; sistema majoritário de dois turnos para cargos executivos; regulação da divulgação de pesquisas; confiança nas pesquisas.
- **Contingências:**
  - menos estudos que o k mínimo numa célula: SWiM e síntese por direção;
  - dados faltantes: sensibilidade e síntese por direção;
  - BDTD ou OpenAlex indisponível ou sem orçamento de API: nova tentativa em outro dia e registro da falha no log, sem truncar busca;
  - volume de registros maior que a capacidade da triagem por subagentes (cerca de 800 com dupla triagem, já acionada): mais ondas, com a concordância A × B e a estabilidade relatadas por onda;
  - nenhum estudo sobre Brasil ou América Latina: seção regional como ausência de evidência.

## 10. Plano de uso de IA

Execução em Claude Code, com subagentes dos modelos Anthropic; o identificador exato de cada modelo é registrado no log por rodada. Não há modo API nem envio a outros provedores. Títulos, resumos e textos completos são processados por esses modelos.

| Etapa | Ferramenta / modelo (versão) | Papel | Supervisão humana | Validação e limiar | Se falhar |
|---|---|---|---|---|---|
| Sugestão de termos da busca | coordenador (claude-opus-5) | propõe | nenhuma (atalho A4) | contagem, âncoras de desenvolvimento e amostras; PRESS por subagente | descartar termo |
| Âncoras de validação | subagente isolado (claude-opus-5) | monta; calcula, sem mostrar títulos ao coordenador, quantas âncoras a triagem por IA excluiu | nenhuma (atalho A3) | fontes independentes da string | registrar como limitação |
| Triagem T/A | subagentes: A = claude-sonnet-5, B = claude-opus-5; regra liberal, sem árbitro | decide, sem validação humana (atalho A2) | nenhuma; pendências `validacao_humana` e `fila_humana_triagem` abertas | Limiares da skill (recall de pelo menos 0,95 com limite inferior do IC de pelo menos 0,90; elusão) não verificáveis sem humanos. Medidas calculáveis sem humano: concordância A × B por onda; estabilidade (`validar estabilidade --amostra 0.1`, re-triagem de 10% por subagentes); número de âncoras de desenvolvimento e de validação excluídas pela triagem de IA | regra liberal; relato da limitação |
| Elegibilidade no texto completo | subagentes (claude-opus-5) via `fichamento-sistematico` | propõe com trecho e página | residual incerto decidido pelo `revisor_humano_1`; restante como pendência `conferencia_elegibilidade_tc` | gate de citações | refazer com subagente novo |
| Extração e efeitos | subagentes (claude-opus-5), recodificação cega (claude-sonnet-5) | propõe com trecho e página | nenhuma (decisão humana no G2); pendência `verificacao_humana_efeitos` | gate de citações; `verificar-efeitos`; κ ou PABAK de pelo menos 0,7 e pelo menos 80% nas categóricas | nova extração |
| Risco de viés | subagentes A (claude-opus-5) e B (claude-sonnet-5), árbitro (claude-fable-5-1) | rascunham julgamentos | `revisor_humano_1` confirma o consenso dos desacordos (exigência do script) | concordância por domínio (κ, PABAK) | — |
| GRADE e evidência faltante | subagente (claude-opus-5) | rascunha | nenhuma; pendência `certeza_humana` | — | — |
| Relatório | coordenador (claude-opus-5) | redige | leitura do `revisor_humano_1` quando quiser | produtos marcados "RASCUNHO NÃO VALIDADO" enquanto houver pendência | — |

**Decisão dos portões G3 a G9, fixada agora e não depois de ver os dados:**

- Os portões serão aprovados no modo autopiloto (`--por autopiloto`) quando as checagens de artefato e de limiar do script passarem.
- Cada aprovação abre a pendência `revisao_humana_portao`, e os critérios registram o desvio A2.
- O G4 é aprovado com a amostra de validação preparada e não calculada. Os critérios trazem `"desvio": "A2: recall não calculado sem humanos"`, a concordância A × B, a estabilidade e o número de âncoras excluídas pela IA. Se alguma âncora independente tiver sido excluída pela triagem de IA, a rodada é refeita com critérios vN+1 antes do G4, com o motivo registrado.
- Relatório, PRISMA e declaração de IA seguem marcados "RASCUNHO NÃO VALIDADO" enquanto houver pendência aberta, em especial `validacao_humana`, `verificacao_humana_efeitos` e `certeza_humana`.

Prompts e critérios versionados com sha256 (`02-triagem/prompts/`), com parâmetros congelados por rodada. A declaração de uso de IA é gerada do log (`rs.py declaracao-ia`) e acompanha o checklist PRISMA-trAIce, sem declarar conformidade.

## 11. Divulgação, dados e código

- **Produtos:**
  - manuscrito PRISMA 2020 (`assets/templates/manuscrito_prisma.qmd`), com diretrizes de relato PRISMA 2020, PRISMA-S e SWiM e checklist PRISMA-trAIce para o uso de IA; público: pesquisadores de comportamento eleitoral e opinião pública;
  - resumo para o debate público sobre divulgação de pesquisas (`assets/templates/policy_brief.qmd`), opcional, a pedido do `revisor_humano_1`, marcado "RASCUNHO NÃO VALIDADO" enquanto houver pendência.
- **[PRISMA 2020 item 27] Pacote aberto:** protocolo congelado, emendas, strings e log de buscas, codebooks, decisões, dados extraídos e código, todos na pasta do projeto. A publicação em repositório aberto fica a critério do `revisor_humano_1`.
- **Log de desvios:** `00-protocolo/emendas.md`.
