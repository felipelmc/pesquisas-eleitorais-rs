# Rascunho do GRADE por célula, v2 (24/09/2026): projeto "pesquisas eleitorais publicadas e voto"

Você rascunha o juízo de certeza (GRADE) de cada célula de efeito desta revisão. O revisor humano confirma depois; por isso `validado_humano` = `0` em todas as linhas (nenhuma validação humana).

## Leia antes (só estes arquivos, todos em `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs/`)

- `00-protocolo/protocolo.md`: seção 8 (comparabilidade, medida, δ) e seção 9, item [17] e "Pontos de partida".
- `00-protocolo/emendas.md`: Emendas 1, 4, 5 e 6 (a 5 descreve a síntese: células, sinal, efeitos fora da contagem, nulos por ±δ; a 6 diz que NENHUM julgamento de RoB foi validado por humano e que a triagem de registros sem resumo foi refeita por IA).
- `05-decomposicao/correcoes_sessao_2026-09-23.csv` e `08-revisao-humana/efeitos/pontos_para_o_revisor.md`: correções dos efeitos feitas por árbitros de IA em 23/09/2026 (comparador `outro` corrigido, novas linhas principais em Fichnova2015a e Lammers2022a, braços trocados em Freden2024a, alvos de momentum pela Emenda 4b) e os pontos que ficaram para decisão humana; cite-os quando afetarem uma célula.
- `06-analise/revisao_metodologica_g8.md`: problemas apontados na primeira versão (R01 a R19); não repita os erros descritos ali.
- `06-analise/swim_principal/swim_resumo.json` e `tabelas/swim_direcao.csv`: SWiM PRINCIPAL, uma célula por família × construto × comparador × célula de alvo × classe de desenho, sem RoB crítico.
- Sensibilidades (agrupamento amplo, descritivo): `06-analise/swim_sens_agrupamento_amplo/`, `swim_sens_com_critico/`, `swim_sens_com_excluidos_amplo/`, `swim_sens_so_contexto_real_amplo/`, `swim_sens_sem_pre2010_amplo/`, `swim_sens_sem_araujo_amplo/`.
- `06-analise/meta_exploratoria/meta_resumo.json` e `meta_exploratoria_icc020/`: meta exploratória (3 estudos, 4 efeitos, CHE + RVE pelo protocolo porque Tyszler2015 tem dois principais; inclui Tyszler2015 lido de figura; gl de Satterthwaite < 4, RVE não confiável); não há meta-análise principal.
- `06-analise/swim_sens_icc020/`: sensibilidade ICC 0,20 (Emenda 4c).
- `06-analise/swim_entrada_principal.csv`: efeitos principais com `yi`, `sei`, `rob_geral`, `estimando`, `desenho_fino`, `realismo_contexto`, `celula_alvo`, `nulo_por_delta`, `beta_proxy_sinal`.
- `04-qualidade/rob_geral.csv` e `05-decomposicao/notas_extracao_completa.md`.

Não abra PDFs, fichas nem outros arquivos; não use rede; não rode `rs.py`.

## Células a julgar

Uma linha para CADA grupo de `swim_principal/swim_resumo.json` que tenha ao menos um estudo (com direção, nulo ou misto). Copie `familia_intervencao`, `construto_outcome` (só `apoio_ao_lider` ou `mobilizacao`), `classe_desenho`, e acrescente `comparador_tipo` e `celula_alvo` do grupo. O agrupamento amplo (descritivo, decidido depois de ver os dados) vai em ARQUIVO SEPARADO, `06-analise/certeza_agrupamento_amplo.csv`, com o mesmo cabeçalho, uma linha por construto × célula de alvo × classe de `swim_sens_agrupamento_amplo`, `familia_intervencao = todas` e `comparador_tipo = todos`, marcada na justificativa como análise descritiva decidida depois de ver os dados. Assim `certeza.csv` só tem valores do contrato.

## Como julgar

- Ponto de partida pelo protocolo: randomizados em alta; não randomizados avaliados com ROBINS-I V2 em alta com rebaixamento por risco de viés; corpo só com EPOC em baixa; célula com ROBINS-I e EPOC juntos: ponto de partida único baixo.
- Cinco domínios de rebaixamento (risco de viés, inconsistência, indireção, imprecisão, viés de publicação) e, para não randomizados, os de elevação. Sem meta-análise, siga Murad et al. (2017): inconsistência pela coerência das direções; imprecisão pelo número de estudos e participantes e pela largura do IC da proporção de direção; se houver meta, pelo IC e pelo intervalo de predição frente a δ (0,044 em g para `apoio_ao_lider`, 0,046 para `mobilizacao`, equivalentes a 2 p.p.).
- Indireção, pelo protocolo: contexto eleitoral e institucional, realismo (eleição hipotética ou preferências induzidas em laboratório frente a eleição real) e estimando.
- Imprecisão: com 1 a 4 estudos por célula, o teste de sinal não tem poder; julgue pelo número de estudos e de participantes e diga isso. Não use intervalo de predição com k < 5.
- Indireção: diga quantos estudos da célula são laboratório com preferências induzidas ou vinheta hipotética (coluna `realismo_contexto`) e cite a sensibilidade só com contexto real.
- Viés de publicação: sem funil (k < 10); julgue pela limitação de fontes (só OpenAlex, BDTD e bola de neve) e pela presença de estudos nulos.
- Aritmética coerente: parta do nível inicial, desça um nível por domínio rebaixado (dois quando grave) e escreva o resultado que a conta dá; a `certeza` tem de ser exatamente o fim da conta descrita na justificativa. Não escreva "a conferir" nem deixe decisões em aberto: se um rebaixamento é discutível, decida e diga que é ponto para o revisor humano.
- Risco de viés com ROBINS-I: nomeie os domínios que levaram ao julgamento (confundimento, seleção, classificação da exposição, desvios, dados faltantes, mensuração do desfecho, seleção do resultado relatado), a partir de `04-qualidade/rob_geral.csv` e das notas de RoB; lembre que nenhum julgamento de RoB foi validado por humano (Emenda 6a).
- Diga o que a certeza qualifica: a DIREÇÃO do efeito (bandwagon = positivo em `apoio_ao_lider`; em `mobilizacao`, negativo = desmobilização), não a magnitude, quando só houver SWiM.

## Saída

Grave SÓ `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs/06-analise/certeza.csv` e `06-analise/certeza_agrupamento_amplo.csv` (UTF-8, vírgula; aspas onde houver vírgula no texto), com exatamente este cabeçalho:

`familia_intervencao,construto_outcome,dimensao,classe_desenho,certeza,abordagem,enunciado,estudos,justificativa,delta,moderador_explica,explica_heterogeneidade,validado_humano,comparador_tipo,celula_alvo`

- `dimensao = efeito`; `abordagem = GRADE`; `certeza` ∈ `alta|moderada|baixa|muito_baixa`.
- `enunciado`: uma frase com a direção e a certeza, no estilo GRADE ("pode aumentar", "provavelmente aumenta", "incerto").
- `estudos`: chaves separadas por `|`.
- `justificativa`: ponto de partida e cada domínio (rebaixado ou não, e por quê), em português, sem travessões como pontuação.
- `delta`: 0.044 (apoio), 0.046 (mobilização), 0.0573 na célula pesquisa_pre_eleitoral × apoio_ao_lider × sem_pesquisa × principal × randomizado (valor de `06-analise/_delta_celula.txt`); `moderador_explica` e `explica_heterogeneidade` vazios; `validado_humano` = 0.

Responda com UMA linha: `OK certeza.csv: <n> linhas; amplo: <n> linhas; certezas=<lista>` ou `FALHA <motivo>`, e depois um parágrafo curto com os pontos que o revisor humano deve decidir.
