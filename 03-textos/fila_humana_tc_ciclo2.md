# Fila humana de elegibilidade no texto completo — ciclo 2 (bola de neve SN1)

A consolidação fechou em **46 incluir, 86 excluir, 9 incerto** sobre 141 textos fichados. Os nove incertos estão abaixo, agrupados por natureza do problema. Todos têm ficha aprovada no gate de citações.

---

## Grupo A — artefato do classificador da skill (2 textos)

**Yang2023d** e **Schlegel2023**: os seis critérios estão respondidos "Sim", com evidência verbatim conferida, e o gate passou sem nenhum problema. Caíram em `incerto` porque o classificador de respostas da skill (`rslib/textos.py`, função `classificar_resposta`) marca como inconclusiva qualquer resposta que contenha a sequência "incert" — e os dois estudos são sobre **visualização de incerteza**, de modo que a palavra "incerteza" aparece na justificativa substantiva.

- Yang2023d: experimento aleatorizado com quatro visualizações de previsão eleitoral construída sobre as pesquisas do FiveThirtyEight; desfecho de comparecimento. Painel de três ondas nas midterms de 2022.
- Schlegel2023: experimento pré-registrado de eleição simulada que varia a incerteza **entre** pesquisas de três institutos; desfecho de escolha de voto.

Não é caso de julgamento: é falso positivo de um `in` de substring. Recomendação: **incluir os dois**.

---

## Grupo B — placar parcial em jogo eleitoral de laboratório (4 textos)

**Scheuerman2019, Scheuerman2020, Scheuerman2021, Yosef2017.** Nestes experimentos o participante vê a contagem corrente de votos (ou o perfil de cédulas já depositadas) antes de votar. A literatura de voto iterativo chama isso de *poll information*, e o protocolo aceita jogos de laboratório com preferências induzidas (C1). Mas nenhum dos textos descreve a exposição como pesquisa eleitoral, agregador, projeção ou boca de urna: o que o participante vê é a apuração parcial do próprio jogo. Em Yosef2017 o placar é ainda constante entre condições — o que varia é o prazo e a composição humanos/bots.

Recomendação: **excluir por C2**. O protocolo define a exposição como resultado de pesquisa (estimativa baseada em levantamento, agregador, projeção ou boca de urna); contagem de votos efetivos não é pesquisa.

---

## Grupo C — apuração oficial parcial divulgada durante a votação (2 relatos, 1 estudo)

**Araujo2021** (preprint) e **Araujo2021a** (British Journal of Political Science) — mesmo estudo. A exposição é a divulgação oficial dos resultados parciais a partir das 19:00, enquanto urnas atrasadas por falha da biometria ainda votavam, nas eleições brasileiras. Variação natural e identificada, desfecho de voto agregado por urna.

É o caso mais difícil da fila, e o mais custoso de excluir: seria um dos poucos estudos latino-americanos do corpus. Ainda assim, os próprios autores marcam a diferença — "our results emerge from a situation of exposure to vote tallies, not pre-electoral polls" — e apuração não é pesquisa.

Recomendação: **excluir por C2**, registrando no relatório que existe uma literatura vizinha sobre divulgação de apuração em tempo real, deixada fora pela definição de exposição do protocolo.

---

## Grupo D — pesquisa como medida agregada, sem identificação (1 texto)

**Mavridis2016a**, capítulo 1 da tese ("Polling in a Proportional Representation System"): o número de pesquisas entra como exposição, mas só em evidência descritiva e em regressão transversal, sem manipulação, variação natural identificada ou painel individual.

Recomendação: **excluir por C4** (desenho), que é onde a falha é inequívoca.

---

## Efeito de cada decisão

Se as quatro recomendações forem aceitas: **48 incluir, 93 excluir, 0 incerto**, e o G5 deixa de estar bloqueado.
