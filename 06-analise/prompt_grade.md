# Rascunho do GRADE por célula — projeto "pesquisas eleitorais publicadas e voto"

Você rascunha o juízo de certeza (GRADE) de cada célula de efeito desta revisão. O revisor humano confirma depois; por isso `validado_humano` fica VAZIO em todas as linhas.

## Leia antes (só estes arquivos, todos em `/Users/felipelmc/revisoes/pesquisas-eleitorais/`)

- `00-protocolo/protocolo.md`: seção 8 (comparabilidade, medida, δ) e seção 9, item [17] e "Pontos de partida" (regras do GRADE deste projeto).
- `00-protocolo/emendas.md`: Emendas 1 e 4 (célula de Araujo2021a; momentum; ICC; EPOC).
- `06-analise/swim_principais/swim_resumo.json` e `06-analise/swim_principais/tabelas/swim_direcao.csv`: síntese por direção, um voto por estudo (análise principal). Sensibilidades: `06-analise/swim_todas_linhas/` (todas as linhas, regra dos 70%) e `06-analise/swim_sens_sem_critico/` (sem RoB crítico).
- `06-analise/meta_principal/meta_resumo.json` (CHE, única célula com k ≥ 3: pesquisa pré-eleitoral × apoio ao líder × comparador sem pesquisa × randomizado) e sensibilidades em `06-analise/meta_sens_um_por_estudo/`, `meta_sens_momentum/`, `meta_sens_icc020/` (arquivo `tabelas/meta_grupos.csv` de cada uma).
- `06-analise/efeitos.csv`: g por efeito (`yi`, `sei`, `formula_id`, `aproximado`, `rob_geral`, `estimando`, `desenho`, `desenho_fino`, `realismo_contexto`, `tipo_eleicao`, `alvo_efeito`, `celula_alvo` não existe aqui, use `alvo_efeito`).
- `04-qualidade/rob_geral.csv`: risco de viés por resultado (RoB 2, ROBINS-I V2, EPOC).
- `05-decomposicao/notas_extracao_completa.md`: dados derivados de figura, efeitos sem g e decisões de extração.

Não abra PDFs, fichas nem outros arquivos; não use rede; não rode `rs.py`.

## Células a julgar (uma linha por célula e classe de desenho)

`celula_alvo` = `principal` (alvo líder, azarão numa disputa de dois ou opção à frente no referendo), `viabilidade` (segundo viável, terceiro inviável, partido perto da cláusula), `momentum_outro` (ganho/perda de apoio sem posição; voto insincero), `mobilizacao`.

| # | familia_intervencao (use exatamente) | construto_outcome | classe_desenho | grupo SWiM correspondente |
|---|---|---|---|---|
| 1 | pesquisa_pre_eleitoral | apoio_ao_lider | randomizado | `apoio_ao_lider \| principal \| randomizado` (+ meta k = 3) |
| 2 | todas | apoio_ao_lider | nao_randomizado | `apoio_ao_lider \| principal \| nao_randomizado` |
| 3 | todas | mobilizacao | randomizado | `mobilizacao \| mobilizacao \| randomizado` |
| 4 | todas | mobilizacao | nao_randomizado | `mobilizacao \| mobilizacao \| nao_randomizado` |
| 5 | todas | apoio_ao_lider_viabilidade | randomizado | `apoio_ao_lider \| viabilidade \| randomizado` |
| 6 | todas | apoio_ao_lider_viabilidade | nao_randomizado | `apoio_ao_lider \| viabilidade \| nao_randomizado` |
| 7 | pesquisa_pre_eleitoral | apoio_ao_lider_momentum | randomizado | `apoio_ao_lider \| momentum_outro \| randomizado` |

Confira em `swim_direcao.csv` a lista de estudos de cada grupo e a família de cada um; se a célula 1 tiver estudo de outra família, diga na justificativa.

## Como julgar

- Ponto de partida pelo protocolo: randomizados em alta; não randomizados avaliados com ROBINS-I V2 em alta com rebaixamento por risco de viés; corpo só com EPOC em baixa; célula com ROBINS-I e EPOC juntos: ponto de partida único baixo.
- Cinco domínios de rebaixamento (risco de viés, inconsistência, indireção, imprecisão, viés de publicação) e, para não randomizados, os de elevação. Sem meta-análise, siga Murad et al. (2017): inconsistência pela coerência das direções; imprecisão pelo número de estudos e participantes e pela largura do IC da proporção de direção; se houver meta, pelo IC e pelo intervalo de predição frente a δ (0,044 em g para `apoio_ao_lider`, 0,046 para `mobilizacao`, equivalentes a 2 p.p.).
- Indireção, pelo protocolo: contexto eleitoral e institucional, realismo (eleição hipotética ou preferências induzidas em laboratório frente a eleição real) e estimando.
- Viés de publicação: sem funil (k < 10); julgue pela limitação de fontes (só OpenAlex, BDTD e bola de neve) e pela presença de estudos nulos.
- Diga o que a certeza qualifica: a DIREÇÃO do efeito (bandwagon = positivo em `apoio_ao_lider`; em `mobilizacao`, negativo = desmobilização), não a magnitude, quando só houver SWiM.

## Saída

Grave SÓ `/Users/felipelmc/revisoes/pesquisas-eleitorais/06-analise/certeza.csv` (UTF-8, vírgula; aspas onde houver vírgula no texto), com exatamente este cabeçalho:

`familia_intervencao,construto_outcome,dimensao,classe_desenho,certeza,abordagem,enunciado,estudos,justificativa,delta,moderador_explica,explica_heterogeneidade,validado_humano`

- `dimensao = efeito`; `abordagem = GRADE`; `certeza` ∈ `alta|moderada|baixa|muito_baixa`.
- `enunciado`: uma frase com a direção e a certeza, no estilo GRADE ("pode aumentar", "provavelmente aumenta", "incerto").
- `estudos`: chaves separadas por `|`.
- `justificativa`: ponto de partida e cada domínio (rebaixado ou não, e por quê), em português, sem travessões como pontuação.
- `delta`: 0.044 ou 0.046; `moderador_explica`, `explica_heterogeneidade`, `validado_humano`: vazios.

Responda com UMA linha: `OK certeza.csv: <n> linhas; certezas=<lista>` ou `FALHA <motivo>`.
