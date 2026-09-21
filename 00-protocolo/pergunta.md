# Ficha da pergunta

Versão 1, 19/09/2026. Rascunho redigido pelo coordenador (Claude Opus 5, via Claude Code, skill `revisao-sistematica`) a partir das respostas do usuário nesta data; aprovação humana no G1.

## 1. Pergunta

**Frase-modelo.** A exposição a resultados de pesquisas eleitorais publicadas altera a intenção de voto do eleitorado, em comparação com a não exposição (ou com a exposição a outro resultado), e em que direção: *bandwagon* (atração pelo candidato ou opção que lidera) ou *underdog* (atração por quem está em desvantagem)?

**Escala.** (2) X sobre Y: uma família de exposição sobre um desfecho principal, com um desfecho secundário.

| Elemento (PECO) | Definição |
|---|---|
| População (P) | Eleitores (indivíduos) ou unidades eleitorais (seções, municípios, distritos) em qualquer país; eleições de candidatos ou partidos e também referendos e plebiscitos; em experimentos, participantes que escolhem entre candidatos, partidos ou opções, reais, hipotéticos ou com preferências induzidas |
| Exposição (E) | Contato com resultado de pesquisa eleitoral: pesquisa pré-eleitoral publicada, agregador ou projeção baseada em pesquisas, pesquisa de boca de urna ou projeção divulgada antes do fechamento das urnas. Vale a exposição manipulada em experimento e a variação natural (proibição ou embargo de divulgação, fusos horários, calendário de publicação) |
| Comparador (C) | Não exposição; exposição a outro resultado (o mesmo candidato mostrado à frente × atrás); antes × depois de proibição ou embargo; unidades expostas × não expostas |
| Desfecho (O) | Principal: apoio ao candidato ou opção que lidera na pesquisa (intenção de voto ou escolha, individual; votação, agregada). Secundário e não intencional: desmobilização (comparecimento, interesse), extraída só quando o estudo a relata |

**Direção.** Construto `apoio_ao_lider`, `direcao_desejada = aumentar`: g > 0 indica *bandwagon*, g < 0 indica *underdog*. "Desejada" é só a convenção técnica de sinal da skill, sem juízo normativo. Em referendos, o líder é a opção à frente na pesquisa.

**Mecanismos candidatos (M).** Percepção de viabilidade e expectativas de resultado; heurística de consenso (a maioria deve ter razão); conformidade social e desejo de estar do lado vencedor; voto estratégico (abandonar quem não tem chance); simpatia pelo azarão e preocupação com equidade; busca de informação; emoções de campanha (ansiedade, entusiasmo).

**Moderadores candidatos (Z).** Sistema eleitoral e número de competidores; competitividade da disputa; força da identificação partidária; sofisticação e interesse político; formato da exposição (pesquisa isolada, agregador, projeção, boca de urna); momento da campanha; tipo de eleição (candidato ou partido × referendo); realismo do contexto experimental (real, hipotético, induzido); ano da eleição (antes × depois de 2010); região (Brasil, América Latina, outras); classe social.

## 2. Entrevista inicial

| Tema | Resposta (19/09/2026) |
|---|---|
| Decisão e uso | Atualizar a síntese da evidência sobre efeitos de pesquisas publicadas desde a última síntese formal (Hardmeier, 2008), com seção de aprofundamento sobre Brasil e América Latina. Uso acadêmico e subsídio ao debate público sobre divulgação de pesquisas. Avaliação *ex post* de um fenômeno, não de um programa [a confirmar no G1] |
| Exposição (X) | Resultados de pesquisas eleitorais publicadas, inclusive boca de urna divulgada no dia da eleição (decisão do usuário) |
| Resultados (Y) | Só intenção ou escolha de voto como critério de elegibilidade (decisão do usuário); comparecimento e interesse como desfecho secundário quando relatados |
| Mecanismos (M) | Hipóteses da seção 1, a detalhar na teoria (etapa 2) |
| Moderadores (Z) | Seção 1; Brasil e América Latina marcados para análise regional |
| População e contexto | Global, sem restrição de país |
| Recorte | Publicação a partir de 2010 (decisão do usuário). Justificativa: (a) a última síntese formal identificada é Hardmeier (2008); (b) desde então o ambiente informacional mudou (agregadores de pesquisas, difusão por redes sociais, em contraste com o modelo de pesquisa telefônica e imprensa tradicional). O ano da eleição estudada entra como moderador, com análise de sensibilidade sem os estudos de dados anteriores a 2010. Limitação declarada: estudos publicados em 2008 e 2009 ficam fora da síntese anterior e desta |
| Idiomas | Inglês, português e espanhol |
| RS conhecidas | Hardmeier (2008); ver seção 4 |
| Recursos | Um revisor humano (o usuário); todas as etapas executadas por subagentes de IA, sem validação humana, com as limitações declaradas no fim (decisão do usuário). Sem prazo externo. Fontes: OpenAlex e BDTD (decisão do usuário, sem exportações de WoS, Scopus ou SciELO). R e Quarto instalados |
| Stakeholders | Nenhum consultado; declarado como limitação |
| IA | Modo API não usado. Triagem, elegibilidade, extração, risco de viés e certeza por subagentes do Claude Code (modelos Anthropic); títulos, resumos e textos completos são processados por esses modelos. E-mail de contato do usuário autorizado para o *polite pool* do OpenAlex e do Unpaywall (só variável de ambiente, nunca gravado no projeto) |

Casos-limite decididos pelo usuário: elegíveis experimentos de laboratório com preferências induzidas, referendos e plebiscitos, e boca de urna no dia da eleição. Fora: estudos observacionais agregados sem variação identificada de exposição (tendência de pesquisas comparada ao resultado, "momentum"). Experimentos naturais e quase-experimentos com unidades agregadas (proibições, fusos horários) continuam elegíveis.

PDFs: cascata completa de fontes legítimas da `baixar-pdfs-academicos`. O usuário autorizou o Sci-Hub, mas ele não é usado: a skill de revisão proíbe esse passo (`--scihub-dois`), e o coordenador não usa fontes não autorizadas. O que não for obtido vira "não recuperado" no PRISMA.

## 3. Tipo de revisão

**`efetividade_swim`, variante rápida.**

| Alternativa | Por que não |
|---|---|
| `efetividade_meta` | A comparabilidade entre desenhos (survey experiments, laboratório, experimentos naturais, painéis) é incerta. O protocolo prevê meta-análise só nas células com k ≥ 3 comparáveis, e o SWiM corre sempre em paralelo (tipos-de-revisao.md, seção 1) |
| `oqf_mista_sequencial` | Formato de avaliação de política pública. A exposição a pesquisas não é um programa, e as linhas de implementação, percepção e custo da caixa de ferramentas não se aplicam |
| `escopo` | Não responde "afeta e em que direção" (tipos-de-revisao.md, seção 9) |

Variante rápida (árvore, passo 10): há um revisor humano e o usuário escolheu cortar etapas. Os atalhos vão declarados no G1, escritos no protocolo antes do G2 e relatados como limitação (PRISMA 2020, item 23c):

1. Fontes restritas a OpenAlex e BDTD, mais bola de neve pelo OpenAlex, sem WoS, Scopus nem SciELO. A regra padrão é ≥ 2 bases, base regional, teses, cinzenta e citações.
2. Triagem, elegibilidade, extração, risco de viés e certeza feitas por subagentes de IA, sem validação humana. Não há calibração, amostra de validação codificada, elusão lida por humano, nem verificação humana dos números.
3. Âncoras de validação da busca montadas por um subagente isolado, não por uma pessoa.
4. PRESS feito só por subagente.

A variante não usa o atalho de triagem do G4 (`atalho_rapida`), porque ele exige dupla humana em ≥ 20% dos registros.

**Título provisório.** Efeitos da divulgação de pesquisas eleitorais sobre a intenção de voto (*bandwagon* e *underdog*): revisão rápida. Subtítulo: revisão sistemática de efetividade sem meta-análise, variante rápida.

## 4. Revisões existentes e registradas (checagem de 19/09/2026)

Como checamos:
- **OpenAlex, sem importar nada:**
  - `EX1`: termos de revisão AND termos de pesquisa eleitoral ou *bandwagon*/*underdog*; `n_api` = 427; muito ruidoso;
  - `EX2`: só no título; `n_api` = 787; listas em `exploracao_EX1.csv` e `exploracao_EX2.csv`.
- **OSF Registries**, pela API, no título: *bandwagon* (13 registros), *underdog* (7), *opinion polls* (2), *election polls* (4), *poll effects* (3), *pre-election polls* (2).
- **BDTD**, pela API VuFind.

Não foram consultados Campbell, 3ie, PROSPERO nem Cochrane: o tema não é de política de desenvolvimento nem de saúde.

Checagem complementar (19/09/2026), pedida pelo revisor metodológico (R12), com leitura de todos os resultados listados:

- `EX3`: termos de pesquisa eleitoral ou *bandwagon*/*underdog* AND voto, com `--filtro type:review`; `n_api` = 9, lidos todos.
- `EX4`: termos de revisão AND (*bandwagon*, *underdog*, *poll*, *sondeos*, *encuestas*, "pesquisas eleitorais"), só no título; `n_api` = 400, lidos os 200 primeiros.

Nenhuma síntese sobre efeitos de pesquisas publicadas no voto posterior a 2008. Achados periféricos, usados só como sementes da bola de neve: "Election polls: a survey, a critique, and proposals" (2017) e uma revisão sistemática ampla sobre campanhas eleitorais e comportamento do eleitor (2026).

| Referência | Pergunta | Tipo | Sobreposição com esta revisão |
|---|---|---|---|
| Hardmeier (2008), "The effects of published polls on citizens", SAGE Handbook of Public Opinion Research, doi:10.4135/9781848607910.n48 | Efeitos de pesquisas publicadas sobre cidadãos | Síntese com meta-análise; último ano de busca e de estudo incluído não verificado (capítulo sem texto aberto) | Mesma pergunta; é a síntese que esta revisão atualiza |
| Moy & Rinke (2012), "Attitudinal and behavioral consequences of published opinion polls", in Holtz-Bacha & Strömbäck (orgs.), doi:10.1057/9780230374959_11 (preprint SocArXiv 10.31235/osf.io/32z5j) | Consequências atitudinais e comportamentais de pesquisas publicadas | Revisão narrativa | Parcial; sem protocolo nem busca sistemática; fonte de âncoras e sementes |
| Barnfield (2019), "Think twice before jumping on the bandwagon", Political Studies Review, doi:10.1177/1478929919870691 | Conceitos na pesquisa sobre efeito *bandwagon* | Revisão conceitual | Parcial; fonte de âncoras e sementes |
| "Bandwagon effect revisited: a systematic review…" (2022), J. Business Research, doi:10.1016/j.jbusres.2022.01.085 | *Bandwagon* no consumo | RS | Nenhuma (marketing) |
| "Do bandwagon cues affect credibility perceptions?" (2023), doi:10.1177/00936502221124395 | Pistas de popularidade e credibilidade de conteúdo online | Meta-análise | Nenhuma (não é voto) |
| "The twilight of the polls?" (2018), Government and Opposition, doi:10.1017/gov.2018.7 | Precisão das pesquisas | Revisão | Nenhuma (precisão, não efeito) |
| OSF Registries | — | — | Nenhuma RS registrada sobre o tema. Só pré-registros de estudos primários: "Poll Wars: the effects of pre-election polls on voting behaviour" (2020); "Margins of error in public opinion polls and citizens' vote intentions" (2021); a série "Bandwagoning in direct democratic decisions" (2024–2025); "Jumping on the bandwagon… 2021 German federal election" (2021). Pistas para a busca, nunca estudos por si |

**Decisão.** A última síntese formal (Hardmeier, 2008) está desatualizada, e não há RS registrada em andamento. Pela tabela da seção 4 da referência, o caminho é **atualizar**, com RS de estudos primários publicados a partir de 2010. As revisões achadas servem ao racional, às âncoras de validação e às sementes da bola de neve; nunca entram como estudos.

## 5. Mapeamento preliminar (contagens no OpenAlex, 19/09/2026, campo título e resumo com *stemming*)

| Bloco | Anos | n |
|---|---|---|
| Exposição (EN) AND desfecho de voto (EN) | todos | 615 |
| Exposição (EN) AND (*bandwagon* OR *underdog*) | todos | 94 |
| Exposição (EN) AND (desfecho OR *bandwagon*/*underdog*) | todos | 688 |
| Idem | 2008+ | 464 |
| Exposição (EN) AND (*bandwagon* OR *underdog*) | 2008+ | 67 |
| (poll OR polls OR polling) AND (*bandwagon* OR *underdog*) AND (vote OR voting OR voters OR election) | todos | 139 |
| Exposição (EN) AND desenho (experimento, natural, randomizado, DiD, RDD, quase-experimental) | todos | 1.301 |
| Exposição (EN) AND desfecho (EN) AND desenho | todos | 97 |
| Exposição (PT) AND efeito/desfecho (PT) | 2008+ | 193 |
| Exposição (ES) AND efeito/desfecho (ES) | 2008+ | 129 |
| BDTD: "pesquisas eleitorais" / "pesquisa eleitoral" / "pesquisas de intenção de voto" | todos | 36 / 30 / 22 |

Leitura: somados os três idiomas, são algumas centenas de registros a partir de 2008, antes da deduplicação; os blocos em PT e ES ainda eram largos nesta exploração. As estratégias testadas depois (`01-busca/strings/desenvolvimento.csv`) somam cerca de 870 (EN) + 117 (PT) + 129 (ES) + 80 (BDTD) registros antes da deduplicação, acima da capacidade de referência da triagem dupla por subagentes (~800). A contingência prevista no protocolo (mais ondas, com concordância e estabilidade relatadas por onda) já está acionada. O núcleo mais específico (*bandwagon*/*underdog*) tem dezenas de registros. Não há meta de número de estudos: se o volume vier grande demais, o escopo é reavaliado antes do G2 ou por emenda.

## 6. Critérios propostos para o G1

```json
{"pergunta": "A exposição a resultados de pesquisas eleitorais publicadas altera a intenção de voto do eleitorado, em comparação com a não exposição ou com a exposição a outro resultado, e em que direção (bandwagon ou underdog)?", "tipo_revisao": "efetividade_swim", "variante": "rapida", "atalhos": ["fontes restritas a OpenAlex e BDTD, mais bola de neve pelo OpenAlex, sem WoS, Scopus e SciELO", "triagem, elegibilidade, extração, risco de viés e certeza feitas por subagentes de IA, sem validação humana", "âncoras de validação montadas por subagente isolado", "PRESS feito só por subagente"], "escala": 2, "rs_existentes": "Hardmeier (2008) é a última síntese formal; Moy e Rinke (2012) narrativa; Barnfield (2019) conceitual; nenhuma RS registrada no OSF; decisão: atualizar com estudos publicados desde 2010", "comparabilidade": "incerta: meta-análise nas células com k >= 3 comparáveis e SWiM em paralelo", "equipe": 1, "prazo": "sem prazo externo"}
```

## 7. Decisões tomadas entre o G1 e o G2 (19/09/2026)

Depois do relatório do revisor metodológico (`revisao_metodologica_g2.md`), o usuário decidiu:

1. **Idiomas:** sem restrição de idioma do documento (buscas seguem em EN, PT e ES); todo texto é lido pelos subagentes.
2. **Efeitos:** números e sinais extraídos só por IA, sem verificação humana; a pendência fica aberta e a síntese sai como rascunho.
3. **Mobilização:** estudos só de comparecimento passam a ser elegíveis numa célula própria (`mobilizacao`), com fio de busca próprio.
4. **Registro:** a revisão não será registrada no OSF.

Pelo padrão metodológico, adotado pelo coordenador e levado ao G2:

- sem contato com autores (atalho A5);
- corte de 2010 mantido, descrito como "evidência publicada desde 2010";
- resultados em risco crítico fora da análise principal;
- pré-registros do OSF usados só para avaliar relato seletivo.
