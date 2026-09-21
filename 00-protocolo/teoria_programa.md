# Teoria da exposição: pesquisas eleitorais publicadas e intenção de voto

Versão 1, 19/09/2026. Diagrama: `00-protocolo/dag_v1.mmd`.

**Registro de uso de IA.** Rascunho do coordenador (Claude Opus 5, via Claude Code, skill `revisao-sistematica`) em 19/09/2026. O prompt pedia: modelo da exposição a pesquisas publicadas → intenção de voto, com mecanismos de *bandwagon* e *underdog*, teorias rivais, efeitos não intencionais por elo, confundidores, colisores e moderadores. Nenhuma seta foi conferida em texto completo nesta versão. A coluna "Origem" diz de onde vem cada elo:

- "literatura (título/resumo)": estudo visto só por título ou resumo na busca exploratória de 19/09/2026;
- "hipótese gerada por IA, não verificada": sem fonte conferida.

Não houve consulta a stakeholders. A versão congelada no G2 é decisão humana.

## 1. Narrativa

A revisão trata uma **exposição**, não um programa: o eleitor vê o resultado de uma pesquisa (pré-eleitoral, agregador ou projeção, boca de urna), por escolha própria, por acaso ou por manipulação experimental. A teoria descreve como essa informação pode mudar a intenção de voto e em que direção.

- **Nível 1 (exposição → resultado).** Se o eleitor vê que o candidato L lidera, então passa a saber quem está à frente, e isso pode aumentar o apoio a L (*bandwagon*) ou ao candidato que está atrás (*underdog*), desde que a informação seja percebida como crível e a preferência prévia não seja firme.
- **Nível 2 (exposição → mecanismo → resultado).** Os mecanismos candidatos são rivais, não complementares por definição. Os de *bandwagon*: viabilidade/estratégico, consenso, conformidade. O de *underdog*: simpatia e equidade. O efeito líquido observado é a soma de canais com sinais opostos: um g próximo de zero não significa ausência de efeito individual.
- **Nível 3 (completo).** Nos desenhos observacionais, o conteúdo da pesquisa reflete o apoio latente na população (causa comum da pesquisa e do voto), e a exposição depende do interesse político (causa comum da exposição e do voto). Nos experimentos, esses caminhos são cortados pela aleatorização, mas o desfecho é autodeclarado e hipotético.

**Classificação.** Aspecto simples: o efeito individual de uma informação num experimento. Aspecto complicado: canais simultâneos de sinais opostos; efeitos distintos por sistema eleitoral. Aspecto complexo: retroalimentação entre pesquisas, cobertura e voto ao longo da campanha. A recorrência é desdobrada no tempo: `pesquisa_t1 → apoio_t2 → pesquisa_t2`.

## 2. Tabela por elo

| Elo | Efeito pretendido (descrição do canal) | Efeito não intencional possível | Direção esperada sobre `apoio_ao_lider` | Onde seria medido | Origem |
|---|---|---|---|---|---|
| E1 exposição → percepção de viabilidade | Eleitor atualiza a expectativa de quem vence | Superestimar a certeza de vitória, sobretudo com projeções probabilísticas | intermediário | Expectativa de vitória, probabilidade percebida | hipótese gerada por IA, não verificada |
| E2 viabilidade → cálculo estratégico → apoio | Abandonar candidato inviável e migrar para um viável | Deserção de terceiros candidatos; concentração do voto | aumentar (*bandwagon*) ou migração para o segundo colocado competitivo | Escolha em experimentos multicandidato; voto estratégico | literatura (título/resumo): Meffert & Gschwend (2011), sinais de coalizão e voto estratégico |
| E3 exposição → heurística de consenso → apoio | "Se muitos apoiam, deve ser bom" | Voto menos informado | aumentar (*bandwagon*) | Intenção de voto; medidas de processamento heurístico | literatura (título/resumo): estudo de 2022 que associa *bandwagon* a processamento heurístico |
| E4 exposição → conformidade/desejo de vencer → apoio | Aderir ao lado vencedor | Pressão social, espiral do silêncio | aumentar (*bandwagon*) | Intenção de voto | hipótese gerada por IA, não verificada |
| E5 exposição → simpatia/equidade → apoio ao azarão | Apoiar quem está em desvantagem | — | reduzir (*underdog*) | Intenção de voto | literatura (título/resumo): estudo de 2022 que associa *underdog* a preocupação com equidade |
| E6 exposição → emoções (ansiedade, entusiasmo) → apoio | Entusiasmo pelo líder, ansiedade de apoiadores do azarão | Mobilização reativa do lado perdedor | ambígua | Medidas de emoção; intenção de voto | literatura (título/resumo): estudo sobre ansiedade e entusiasmo no efeito *bandwagon* (IJPOR) |
| E7 (incentivo perverso) exposição → complacência → desmobilização | — | Apoiadores do líder (ou do azarão desanimado) deixam de votar ou de se informar | dano: queda no desfecho `mobilizacao` (comparecimento e interesse), direção desejada `aumentar` | Comparecimento, interesse, busca de informação | literatura (título/resumo): estudo sobre exposição a pesquisas e menor interesse no resultado; hipótese de complacência gerada por IA |
| E8 (incentivo perverso) divulgação estratégica de pesquisas enviesadas → exposição | — | Atores com interesse publicam números favoráveis para induzir *bandwagon* | afeta o conteúdo da exposição, não o sinal do efeito | Estudos de proibição e regulação; qualidade das pesquisas | hipótese gerada por IA, não verificada (contexto do debate regulatório) |

## 3. Papéis das variáveis

| Variável | Papel | No DAG | Na extração | Na síntese |
|---|---|---|---|---|
| `apoio_latente` (preferência real da população) | Confundidor em desenhos observacionais | → conteúdo da pesquisa; → apoio | Como o estudo separa o efeito da pesquisa da mudança real de opinião (desenho, controles, variação exógena) | Domínio de confundimento no ROBINS-I; motivo da exclusão de estudos agregados sem variação identificada |
| `interesse_politico` | Confundidor da exposição medida em painéis | → exposição; → apoio | Ajuste por interesse e consumo de mídia | Domínio de confundimento |
| `preferencia_previa` / partidarismo | Confundidor em painéis; moderador em experimentos | → exposição seletiva; → apoio | Ajuste pela intenção anterior (linha de base) | Confundimento e moderação |
| `resposta_ao_survey` (permanecer no painel, completar o experimento) | Colisor | ← exposição; ← intenção de voto (setas diretas no DAG) | Perda de seguimento e seleção da amostra | Alerta de viés de seleção; nunca "controlar" |
| `percepcao_viabilidade` | Mediador | X → M → Y | O modelo ajusta pela expectativa? (efeito direto × total) | Não agregar efeito direto com total |
| Heurística, conformidade, simpatia, emoções | Mecanismos latentes | Nós raramente medidos | Trecho verbatim quando testados | Síntese narrativa dos mecanismos |
| Complacência → desmobilização | Incentivo perverso | Aresta tracejada | Desfecho adverso com direção própria | Desfecho secundário `mobilizacao` (célula própria; queda = desmobilização) |

## 4. Tabela Z (moderadores: fora do grafo)

| Moderador | Hipótese | Direção esperada | Origem |
|---|---|---|---|
| Força da identificação partidária | Partidários fortes mudam menos | Menor magnitude com partidarismo forte | hipótese gerada por IA, não verificada |
| Sofisticação e interesse político | Teorias rivais: (a) menos sofisticados usam a heurística de consenso; (b) mais sofisticados fazem cálculo estratégico | (a) *bandwagon* maior com baixa sofisticação; (b) maior com alta; registrar as duas | hipótese gerada por IA, não verificada |
| Sistema eleitoral e número de competidores | Pluralidade com três ou mais candidatos favorece a deserção estratégica; na representação proporcional valem os sinais de coalizão | Maior com pluralidade e três ou mais competidores | literatura (título/resumo): Meffert & Gschwend (2011) |
| Competitividade da disputa | Disputa apertada favorece a mobilização do azarão; disputa decidida favorece *bandwagon* ou desmobilização | Mais *underdog* quando apertada | hipótese gerada por IA, não verificada |
| Formato da exposição (pesquisa isolada, agregador/projeção probabilística, boca de urna) | Projeções probabilísticas aumentam a certeza percebida | Maior efeito sobre expectativas e desmobilização com projeções | hipótese gerada por IA, não verificada |
| Momento da campanha | Mais efeito perto da eleição, com menos tempo para outra informação | Maior perto do dia da eleição | hipótese gerada por IA, não verificada |
| Tipo de eleição (candidato ou partido × referendo) | Referendos de baixa informação são mais sensíveis a pistas de consenso | Maior em referendos | literatura (título/resumo): pré-registros e estudos suíços sobre *bandwagoning* em democracia direta |
| Realismo do contexto (real, hipotético, preferências induzidas) | Sem preferência prévia, a informação pesa mais | Maior em contextos hipotéticos e induzidos | hipótese gerada por IA, não verificada |
| Ano da eleição (antes × depois de 2010) | Novo ambiente informacional (agregadores, redes sociais) | Desconhecida (sem hipótese de sinal) | justificativa do recorte (usuário) |
| Região (Brasil, América Latina, outras) | Voto obrigatório (Brasil e parte da América Latina) elimina o canal da desmobilização; multipartidarismo; desconfiança nas pesquisas | Desconhecida para `apoio_ao_lider`; menor desmobilização sob voto obrigatório | hipótese gerada por IA, não verificada |
| Confiança nas pesquisas | Quem desconfia descarta a informação | Menor magnitude com baixa confiança | hipótese gerada por IA, não verificada |

**Equidade (PROGRESS-Plus).** Os fatores escolhidos são escolaridade, posição socioeconômica ou classe e idade.

- **Escolaridade e classe:** *bandwagon* maior entre os de menor escolaridade ou classe, pela heurística de consenso. Origem: literatura (título/resumo), estudo de 2022 sobre classe social e efeitos de pesquisas na eleição alemã de 2021; hipótese de direção gerada por IA.
- **Idade:** sem hipótese de sinal.

Esses fatores entram como moderadores pré-especificados, com extração do resultado por subgrupo quando o estudo o relata.

## 5. Teorias rivais registradas

1. **Efeitos que se anulam.** *Bandwagon* e *underdog* coexistem na mesma população, e o efeito médio próximo de zero esconde efeitos individuais opostos. Consequência: extrair subgrupos (apoiadores do líder × do azarão × indecisos) quando relatados.
2. **Efeito só de expectativa.** A pesquisa muda expectativas, mas não o voto. Consequência: o desfecho elegível é o voto; a expectativa entra só como mediador.
3. **Efeito artefatual do experimento.** Em *survey experiments* com candidatos hipotéticos, o efeito reflete a demanda do experimentador. Consequência: moderador de realismo; domínio de medida do RoB 2 (desfecho autodeclarado).
