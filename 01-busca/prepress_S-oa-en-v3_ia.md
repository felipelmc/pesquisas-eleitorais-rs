# Pré-revisão PRESS 2015 por subagente de IA (atalho A4 do protocolo; não substitui revisão humana)

**Data:** 2026-09-19
**Estratégia revisada:** `S-oa-en-v3` (OpenAlex, `title_and_abstract.search`, com stemming, `publication_year:2008-2026`)
**Revisor:** subagente de IA isolado, sem acesso à redação da string original
**Fonte de contagens:** API OpenAlex, consultas ao vivo em 2026-09-19 (38 consultas usadas, dentro do limite de 40, com pausa de 1s)

Baseline confirmado ao vivo: **1.130** registros (idêntico ao valor de `desenvolvimento.csv`, linha `v3-en`).

Os itens 3.1 a 3.9 (vocabulário controlado) são marcados "não se aplica": o OpenAlex não tem tesauro/descritores.

## Checklist

| item | resposta | comentário | mudança recomendada |
|---|---|---|---|
| 1.1 | sim | A string cobre E (pesquisa/sondagem/survey/projeção/boca de urna, via "exit poll") e O (`apoio_ao_lider` nos fios T1/S/T2; `mobilizacao` no fio T3), alinhada ao PECO do protocolo (seção 2). Não busca P nem C, o que é esperado: P é universal em qualquer estudo eleitoral e C não tem vocabulário textual próprio. | nenhuma |
| 1.2 | sim | Quatro conceitos separados e nomeados (T1 poll+efeito; S survey+efeito; T2 exposição+voto; T3 exposição+comparecimento), documentados no protocolo (seção 3) e na tabela de termos v2. | nenhuma |
| 1.3 | sim | Só E e O compõem a busca; um quinto bloco de "efeito/desenho" já foi testado e rejeitado (`desenvolvimento.csv`, linha `v1-en-E`: perdeu 2 de 11 relevantes). Nenhum elemento supérfluo remanescente. | nenhuma |
| 1.4 | sim, com ressalva | Blocos de exposição bem calibrados (amostra de 25/25 do bloco T1 majoritariamente pertinente, ver abaixo). Testei o termo isolado "electoral forecast": é amplo demais sozinho (100% de ruído de metodologia de previsão, ver "Termos testados e não recomendados"); a string atual não o usa isolado, então não há problema a corrigir. | nenhuma |
| 1.5 | sim | B01 = 1.130 (confirmado ao vivo). Evolução documentada em `desenvolvimento.csv`: 464 → 734 → 870 → 1.130. Bloco T1 isolado = 134. O volume está acima da capacidade de referência de triagem dupla (~800), mas a contingência de mais ondas já está acionada no protocolo (seção 9) — risco operacional já reconhecido, não falha da estratégia. | nenhuma |
| 1.6 | sim | A estrutura em 4 fios e a rejeição do bloco extra de efeito/desenho estão documentadas no protocolo e no `desenvolvimento.csv`. | nenhuma |
| 2.1 | sim | AND/OR em maiúsculas confirmados por contagem programática (71 `OR`, 4 `AND`); a query completa executa sem erro (retornou 1.130). | nenhuma |
| 2.2 | sim | Parênteses balanceados (12 abrem, 12 fecham); a estrutura lida é `(T1) OR (S) OR (T2) OR (T3)`, cada bloco com um único `AND` interno — confere com a descrição do protocolo. | nenhuma |
| 2.3 | não se aplica | A string não usa `NOT`; não há risco de exclusão indevida por esse operador. | nenhuma |
| 2.4 | não (manter AND) | Testei substituir o `AND` do bloco T1 por proximidade: `"poll bandwagon"~15` = 50 registros vs. 134 do `AND` simples (perda de ~63%). Trocar precisão por perda de recall não se justifica numa revisão que já prioriza sensibilidade. | nenhuma (pela regra de ouro) |
| 2.5 | não se aplica | A estratégia não usa operadores de proximidade. | nenhuma |
| 3.1 | não se aplica | OpenAlex não tem descritores/tesauro. | — |
| 3.2 | não se aplica | idem | — |
| 3.3 | não se aplica | idem | — |
| 3.4 | não se aplica | idem | — |
| 3.5 | não se aplica | idem | — |
| 3.6 | não se aplica | idem | — |
| 3.7 | não se aplica | idem | — |
| 3.8 | não se aplica | idem | — |
| 3.9 | não se aplica | idem | — |
| 4.1 | sim | Boa cobertura de variantes: US/UK (`behavior`/`behaviour` em "voting"/"electoral"), hífen (`horse race`/`horse-race`, `band-wagon`, `pre-election`/`preelection` ×2). Nenhuma variante de grafia faltante encontrada nos testes. | nenhuma |
| 4.2 | sim, com uma adição pontual | `bandwagon`/`underdog` já formam o par de efeitos nomeados. Testei 8 candidatos de sinônimo/exposição adicionais (front-runner/frontrunner effect, GOTV, voter mobilization, vote switching, intention to vote, polling data, exit polling, electoral forecast): só `"poll effects"` mostrou ganho líquido defensável. Ver seção de mudanças. | ver "Mudanças recomendadas" #1 |
| 4.3 | sim | Truncamento corretamente **não** usado no campo padrão (que devolveria HTTP 400 com `*`, conforme a sintaxe informada). Confirmei que o stemming já equivale singular/plural: `"opinion poll"` e `"opinion polls"` retornam a mesma contagem (7.533), tornando truncamento desnecessário. | nenhuma |
| 4.4 | sim | Nenhuma sigla ambígua na string. Testei `GOTV`/`"get out the vote"` combinado com a lista de frases de exposição: contagem idêntica antes/depois (1.130 = 1.130) — não é uma lacuna. | nenhuma |
| 4.5 | sim, com observações | `poll`/`polls`/`polling` são genéricos, mas sempre em `AND` com termos de efeito ou desfecho, o que os protege (amostra do bloco T1: 25/25 pertinentes). `"horse race"`/`"horse-race"` isolados são extremamente genéricos (1.473 registros, dominados por finanças, medicina e esportes), mas o `AND` do bloco contém o ruído, e um dos achados isolados ("Projecting Confidence: How the Probabilistic Horse Race Confuses and Demobilizes the Public") é claramente pertinente à célula `mobilizacao` — não remover. Observei também polissemia do radical "poll" (ex.: a palavra "polled" foi capturada num artigo de meta-análise de poluição do ar), ruído estrutural de baixa magnitude e sem custo prático porque exige coocorrência com termos de efeito/voto ausentes nesses textos. | nenhuma (regra de ouro: não remover termos genéricos que sustentam recall) |
| 4.6 | sim | Campo `title_and_abstract` é adequado e documentado no protocolo (fonte B01). | nenhuma |
| 4.7 | sim, com nota operacional | A string tem 1.515 caracteres antes da codificação de URL; a chamada via `curl -G --data-urlencode` funcionou sem erro, mas a string expande consideravelmente quando percent-encoded (espaços, parênteses, aspas). Registrar que a execução deve seguir por API/script (como já é o caso, `rs.py buscar openalex`) e não por interface com limite de URL menor. | nenhuma na string; nota para o log de execução |
| 5.1 | sim | Nenhum erro de digitação encontrado. `preelection`, `horse-race`, `band-wagon` são variantes intencionais, não erros. | nenhuma |
| 5.2 | sim | Aspas retas (não curvas) em todas as 130 ocorrências; 0 vírgulas; nenhum uso de `*`. Observação: a frase entre aspas nem sempre garante adjacência estrita no motor do OpenAlex (ex.: `"poll effects"` casou com um artigo cuja palavra "polled" aparece perto de "effects" num sentido não eleitoral) — é um comportamento do mecanismo de busca, não um erro de sintaxe da string, e deve ser registrado como limitação de precisão, não corrigido na string. | nenhuma |
| 5.3 | não se aplica | É uma string booleana única (sem linhas numeradas a combinar). | — |
| 6.1 | sim | `publication_year:2008-2026` com margem de 2 anos antes do marco de 2010, aplicado depois no funil formal (`filtros_v2.json`) — coerente com a lógica declarada no protocolo (seções 3 e 4). | nenhuma |
| 6.2 | sim | O filtro de ano é nativo do OpenAlex (`publication_year`); testado e funcional. | nenhuma |
| 6.3 | sim | Não há filtro de idioma nem de tipo de documento, coerente com a decisão humana no G2 (sem restrição de idioma) e com o desenho de status de publicação irrestrito. Nenhum limite faltando ou excessivo identificado. | nenhuma |
| 6.4 | sim | O protocolo (seção 3–4) cita e justifica a origem do filtro de ano (mudança no ambiente informacional; intervalo desde Hardmeier 2008) e remete ao funil formal (`filtros_v1.json`/`filtros_v2.json`). | nenhuma |

## Mudanças recomendadas

**1. Acrescentar `"poll effects"` como alternativa autônoma (top-level `OR`), sem exigir `AND` com termo de desfecho.**

- String testada (acréscimo): `(S-oa-en-v3 atual) OR "poll effects"`
- Contagem antes: **1.130**. Contagem depois: **1.142** (+12).
- Justificativa: entre os 12 registros novos, ao menos um é claramente pertinente e não é recuperado por nenhum bloco atual — *"Experiments on the Effects of Opinion Polls and Implications for Laws Banning Pre-election Polling"* (2016). É um registro sem resumo indexado no OpenAlex (só título), cujo título por si atende E ("Opinion Polls") e é diretamente relevante ao debate sobre proibição de pesquisas citado no racional do protocolo (seção 1); não é recuperado pelos blocos T2/T3 porque o título não contém nenhuma das frases de desfecho (vote choice, turnout etc.) e não há resumo para supri-las. Outros 2 registros são ambíguos na triagem ("13 Cognitive Preconditions for Direct Poll Effects on Voters..."; "Impact of Poll Results on Personal Opinions and Perceptions of Collective Opinion"); os ~9 restantes são ruído claro de outras áreas (poluição do ar, prótese dentária, estresse equino, parafuso ortopédico "Poller"), explicado por polissemia do radical "poll" combinado com a palavra comum "effects" — custo baixo (12 registros) mesmo sob restrição de capacidade de triagem.
- Como inserir: acrescentar ` OR "poll effects"` ao final da string atual (fora dos parênteses dos 4 blocos existentes).

### Termos testados e não recomendados (documentados para transparência)

| termo testado | estrutura da consulta | antes → depois (ou contagem isolada) | decisão |
|---|---|---|---|
| `"front-runner effect"` / `"frontrunner effect"` (frase exata) | frase isolada | 1 registro total, e é sobre economia do trabalho ("Career Concerns and Belief Precision about Talent") | rejeitado — sem uso na literatura eleitoral |
| `front-runner`/`frontrunner` (palavra solta) AND (bandwagon/underdog/vote choice/vote intention/voting behavior) | 1.130 → 1.164 (+34) | dos 34 novos, só 1 plausivelmente pertinente ("Being an Underdog Or a Frontrunner: the Effects of Candidate Labels on Voters' Responses"); os demais são ruído de outras áreas (transição energética, vacinas, arte, geopolítica) | rejeitado — custo/ganho desfavorável (1 em 34) |
| `"electoral forecast"` (frase isolada, sem exigir efeito/voto) | 1.130 → 1.235 (+105) | amostra de 25/25 novos é sobre metodologia/acurácia de previsão eleitoral, exatamente o que o critério C2 do protocolo exclui | rejeitado — nenhum plausivelmente pertinente |
| `"polling data"` AND (vote choice/vote intention/voting behavior/turnout/abstention) | 1.130 → 1.181 (+51) | 1 registro claramente pertinente ("The effect of polling data on independent voting behavior"), mas os demais 50 são majoritariamente ruído coincidente (uso de "polling data" como fonte de dados, não como objeto de exposição, o que o critério C2 já exclui) | não recomendado — custo alto (51) para 1 ganho claro; mencionar como candidato de baixa prioridade para o revisor humano decidir |
| `"exit polling"` AND (bandwagon/underdog/vote choice/vote intention/turnout/abstention) | 1.130 → 1.140 (+10) | nenhum dos 10 novos parece estudar exposição a *exit polls*; a maioria usa "exit polling" como método de mensuração do próprio desfecho | rejeitado |
| `"intention to vote"` (frase, ordem invertida de "vote intention") AND lista de frases de exposição | 1.130 → 1.134 (+4) | os 4 novos são sobre acurácia de pesquisas, pesquisa e retorno de ações, e análise de discurso midiático — nenhum claramente pertinente | rejeitado |
| `"vote switching"` AND lista de frases de exposição | 1.130 → 1.132 (+2) | os 2 novos (volatilidade eleitoral na Eslováquia; dados de replicação sobre migração de voto na Alemanha) não mencionam exposição a pesquisas | rejeitado |
| `"voter mobilization"`/`"voter mobilisation"` AND lista de frases de exposição | 1.130 → 1.130 (0) | nenhum registro novo | rejeitado |
| `GOTV`/`"get out the vote"` AND lista de frases de exposição | 1.130 → 1.130 (0) | nenhum registro novo | rejeitado |

Nenhuma remoção de termo foi recomendada (regra de ouro do protocolo): os termos genéricos (`poll`, `horse race`) só aparecem em `AND` com termos de efeito ou desfecho, e ao menos um achado de amostra confirma que "horse race" recupera um registro pertinente à célula `mobilizacao`.

## Coerência das traduções

- **S-oa-pt-v3 e S-oa-es-v3 têm 3 blocos, não 4.** Isso é coerente e não é uma lacuna: em português e espanhol, `pesquisa`/`sondagem` e `encuesta`/`sondeo` já cobrem tanto o sentido de "poll" quanto o de "survey" do inglês, dispensando o fio `S` (survey) separado que existe só na versão EN.
- **Assimetria real entre EN e PT/ES:** o bloco de desfecho de voto (T2) em PT e ES inclui um "escape" genérico — `efeito OR efeitos OR influência OR impacto` (PT) e `efecto OR efectos OR influencia OR impacto` (ES) — que a versão EN **não tem**. Esse escape é exatamente o tipo de termo que teria recuperado o achado "Experiments on the Effects of Opinion Polls..." se ele estivesse em português. Isso não invalida PT/ES (que são só comentados, não testados aqui), mas explica de forma direta por que a mudança recomendada nº 1 (`"poll effects"`) é necessária para alinhar EN ao mesmo nível de cobertura que PT/ES já têm. Não testei se esse termo genérico introduz ruído excessivo em PT/ES (fora do escopo desta revisão, que só comenta coerência com a principal).
- **Pequena inconsistência interna PT vs. ES:** o bloco 1 do ES inclui `voto estratégico` como sinônimo de efeito nomeado (junto com bandwagon/underdog), enquanto o bloco 1 do PT não inclui `voto útil`/`voto estratégico` nesse mesmo papel (só no bloco de desfecho). Não é uma incoerência com a EN (que também não tem "strategic voting" no bloco de efeito nomeado, só no de desfecho), mas é uma assimetria entre as duas traduções que vale registrar.
- **S-bdtd-v3 não tem estrutura AND/OR aninhada** (limitação da API VuFind: parênteses aninhados geram HTTP 403, conforme `desenvolvimento.csv`, linha `v1-bdtd`), por isso é uma lista `OR` plana. Duas consequências relevantes para a coerência com a EN:
  1. **Falta o equivalente ao fio T3** (comparecimento): EN, PT e ES v3 acrescentaram explicitamente termos de comparecimento/abstenção combinados com a exposição; a BDTD v3 é idêntica à v2 e não tem nenhum termo de comparecimento na lista, apoiada só na suposição de que teses sobre comparecimento também mencionam uma das frases eleitorais gerais já listadas. Como é uma lista plana (`OR`), adicionar termos como `"comparecimento eleitoral"` ou `"abstenção eleitoral"` seria tecnicamente simples (não exige parênteses aninhados) e alinharia a BDTD ao mesmo raciocínio do T3 nas outras três strings — mas não testei isso (a BDTD não é uma base do OpenAlex e o teste desta revisão está restrito à API do OpenAlex).
  2. **Falta o par nu `bandwagon`/`underdog`**: a BDTD só tem as frases compostas `"efeito bandwagon"` e `"efeito underdog"`, enquanto EN/PT/ES também aceitam as palavras soltas. Teses brasileiras que usem o termo em inglês sem a palavra "efeito" (ex.: "o bandwagon nas eleições municipais") ficariam de fora. Baixo risco dado o volume pequeno da BDTD (80 registros), mas vale registrar como limitação declarável.

---
*Gerado por subagente de IA (atalho A4 do protocolo de `pesquisas-eleitorais`). A pendência `revisao_press` permanece aberta até leitura humana desta pré-revisão, conforme o protocolo (seção 3).*
