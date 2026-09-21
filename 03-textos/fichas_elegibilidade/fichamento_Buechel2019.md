---
citekey: Buechel2019
ficha_id: Buechel2019
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Buechel2019.pdf
paginacao: impressa
offset_pagina: -240
agente_fichador: fichador_el_165
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — evidência: "The swing voter’s curse in social networks" (p. 241)
- **tipo_documento** — resposta: artigo — evidência: "Article history:" (p. 241); "Available online 3 September 2019" (p. 241)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim, participantes de laboratório (grupos de nove: cinco "experts" e quatro "non-experts") votam por maioria entre duas políticas alternativas, com preferências induzidas por pagamento, o que corresponde a uma eleição/plebiscito de laboratório. — evidência: "Voters simultaneously vote for one of the two policies or abstain." (p. 245); "All subjects in a session played the game described above" (p. 249)
- **c2_intervencao_estudada** — resposta: Não, a exposição analisada é a recomendação de voto privada enviada por vizinhos na rede social e a estrutura da rede (rede vazia, fortemente balanceada, fracamente balanceada, estrela) como tratamento; não há resultado de pesquisa eleitoral como exposição. — evidência: "We focus our analysis on vote recommendations that are provided" (p. 242); "Each of these networks corresponds to one experimental treatment" (p. 249)
- **c3_desfecho** — resposta: Sim, o desfecho é de voto e de comparecimento: mede-se a escolha de voto de cada participante entre as duas políticas (votar conforme a mensagem, votar no oposto) e a abstenção/turnout do grupo, além do resultado agregado da votação. — evidência: "learned the chosen policy, the true state, and the voter turnout" (p. 250); "the value 1 if the voting outcome matches the majority signal" (p. 254)
- **c4_desenho_elegivel** — resposta: Sim, experimento de laboratório aleatorizado: papéis sorteados, rematching aleatório dos grupos a cada rodada e os quatro tipos de rede como tratamentos variados dentro dos sujeitos. — evidência: "subjects were randomly matched into groups of nine" (p. 250); "subjects randomly received the role of an expert" (p. 250)
- **c5_estudo_primario** — resposta: Sim, estudo primário com dados próprios do experimento de laboratório conduzido pelos autores (840 observações de grupo e 7.560 individuais), além do modelo teórico. — evidência: "we conducted a laboratory experiment to test our focality assumption" (p. 242); "On the group level we have 840 observations." (p. 250)
- **c6_nao_retratado** — resposta: Sim, não há marca "RETRACTED", nota ou página de retratação em nenhuma parte do documento. — evidência: "curse in social networks" (p. 241)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim; o documento remete a uma versão anterior de working paper permanentemente disponível online (Buechel e Mechtenberg, 2017), que contém o Estudo II e o material suplementar SOM C.3. — evidência: "in an earlier working paper version that is permanently available online" (p. 256); "Study II can be found in SOM C.3" (p. 249)
- **fonte_dados_amostra** — resposta: Experimento de laboratório no WISO-lab da Universidade de Hamburgo, com nove sessões de 27 participantes e 189 sujeitos ao todo, jogando 40 rodadas em quatro tratamentos de rede (840 observações de grupo; 7.560 individuais); o documento não informa o período/ano em que as sessões foram realizadas. — evidência: "The experiment was conducted in the WISO-lab of the University of Hamburg" (p. 249); "In total, 189 subjects participated in the experiment." (p. 250)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação: a numeração impressa é a paginação contínua do periódico (Games and Economic Behavior 118 (2019) 241–268). A folha 1 do PDF é a página impressa 241, logo `folha_do_PDF = pagina_anotada + (-240)`. Conferi o rodapé/cabeçalho de páginas distantes: impressa 242 → folha 2, impressa 249 → folha 9, impressa 250 → folha 10, impressa 254 → folha 14, impressa 256 → folha 16, impressa 268 (última) → folha 28. Todas as citações desta ficha foram reabertas nas folhas indicadas pela fórmula.
- C1: o voto é entre duas políticas alternativas (P_A e P_B) num jogo de maioria em laboratório, com preferências induzidas (5 euros por decisão coletiva correta). Não se trata de escolha de consumo/mercado nem de votação de órgão deliberativo real (júri, comitê, conselho); o próprio texto enquadra o cenário como aplicável "predominantly to large elections". Por isso respondi Sim, ainda que a decisão seja sobre políticas e não sobre candidatos: equivale a opções de referendo/plebiscito em eleição de laboratório.
- C2 é o critério que falha. O objeto empírico é a comunicação pré-voto entre eleitores na forma de recomendações de voto privadas, e a variação exógena é a estrutura da rede, não a divulgação de pesquisa eleitoral. "Straw polls" aparecem apenas na literatura relacionada (Coughlan, 2000; Guarnaschelli et al., 2000), como contexto teórico, e não como exposição analisada. Não há pesquisa pré-eleitoral, agregador, projeção ou boca de urna no desenho.
- C3: além da escolha de voto individual (votar a mensagem, votar o oposto, abster-se), o desenho mede abstenção e turnout do grupo, e o desfecho agregado do voto entra na variável de eficiência informacional. Respondi Sim para voto e comparecimento.
- C5: o artigo combina modelo teórico e experimento próprio; como há análise própria de dados originais, é estudo primário (não é revisão).
- C6: a checagem interna cobre só o documento; não há qualquer aviso de retratação nas 28 folhas. Como evidência usei um fragmento literal contíguo do título na primeira página ("curse in social networks"), para evitar depender do apóstrofo tipográfico do título completo, que já consta em `texto_confere`.
- `registro_financiamento` = 999 porque o documento não traz identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP) nem número de processo/edital. Há apenas agradecimento genérico de apoio financeiro na nota de rodapé da primeira página ("the financial support by the Fritz Thyssen Foundation", p. 241), sem número de projeto, o que não satisfaz o prompt da variável.
- Li integralmente as 28 folhas do PDF (páginas impressas 241 a 268), em duas faixas (folhas 1-14 e 15-28), e reabri as folhas 1-2, 5, 9-10 e 14 para conferir as citações.
