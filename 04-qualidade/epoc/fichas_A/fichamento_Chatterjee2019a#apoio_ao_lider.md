---
citekey: Chatterjee2019a
ficha_id: Chatterjee2019a#apoio_ao_lider
n_fichas_do_texto: 2
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Chatterjee2019a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Chatterjee2019a-epoc
data_fichamento: 2026-09-23
ferramenta: epoc
paginas_pdf: 33
faixas_lidas: 1-20,21-33
---

## 00_Resultado
- **desenho_epoc** — resposta: grupo_controle — evidência: "compare states having single and multi phase elections before and after" (p. 4); "comparing the same states from an earlier round of elections" (p. 18)
- **resultado_avaliado** — resposta: Tabela 3 (eleições estaduais para assembleias legislativas), bloco Winner, coluna 2 com controles (população, razão de sexo, alfabetização, total de eleitores, emprego urbano): DiD δ = 2.921* (1.196), N = 1352; efeito da proibição de boca de urna sobre a votação do vencedor — evidência: "Impact of Exit Poll Bans on Vote Shares of Candidates" (p. 21); "2.921*" (p. 21)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: "As conducting such experiment is infeasible and impractical" (p. 18); "we have to compare states that had elections just before" (p. 18)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: "the ban given predetermined electoral calendar in India" (p. 3); "Luckily, the states that went to elections just before and just" (p. 18)
- **cg_linha_base_outcome** — resposta: proposta_incerto — evidência: "comparing the same states from an earlier round of elections" (p. 18); "the national election data provides relatively high frequency pre-ban data" (p. 23)
- **cg_caracteristicas_base** — resposta: proposta_alto — evidência: "these groups of states may have intrinsically" (p. 18); "Table 2: Summary Statistics" (p. 17)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: "the dataset consists of 681 constituencies of four" (p. 14); "1352" (p. 21)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "We use administrative data from the statistical reports published" (p. 14)
- **cg_contaminacao** — resposta: proposta_baixo — evidência: "results of exit polls are reported at the end of the day" (p. 18); "Interestingly, all these states had single phase elections and therefore" (p. 11)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: "outcomes such as vote share of winner, vote share of runner up" (p. 19)
- **cg_outros_riscos** — resposta: proposta_alto — evidência: "Bihar was the only state which had multi-phase election" (p. 14); "Due to this delimitation exercise, we are unable to" (p. 16); "Robust Standard Errors in parentheses" (p. 21)

## Notas do codificador
- Justificativa de `cg_outros_riscos` (movida do campo de resposta pelo coordenador): um único estado tratado (Bihar) contra três controles, com um só período pré e sem teste de tendências prévias para as eleições estaduais; choques específicos de Bihar entre as duas eleições ficam confundidos com a proibição; redistritamento (delimitação de 2008) entre os períodos; erros-padrão robustos não agrupados com um só cluster tratado; exposição a boca de urna entre fases no período pré não documentada
Classificador: diferenças em diferenças com unidades agregadas (circunscrições em estados), comparando estados de eleição sempre multifásica (tratados) e de fase única (controles), antes e depois da proibição de 2009/2010. Pelo protocolo do projeto vai por EPOC grupo_controle.

Sequência aleatória e ocultação: antes-depois controlado, SEMPRE proposta_alto pelo EPOC; a atribuição decorre do calendário eleitoral e do número de fases.

Linha de base do outcome: o outcome foi medido na rodada eleitoral anterior nos mesmos estados e o DiD remove diferenças de nível, mas o texto não relata a votação do vencedor por grupo antes da proibição na amostra estadual (a Tabela 2 é agregada) e a figura de tendências paralelas (p. 24) cobre só as eleições nacionais. Sem dado para julgar se havia diferença importante, proposta_incerto.

Características de base: a Tabela 2 não separa tratados e controles; os autores admitem que os grupos podem diferir intrinsecamente. Não relatadas por grupo, proposta_alto.

Dados incompletos: dados administrativos; 681 circunscrições em duas eleições dariam 1362 observações (N = 1362 na Tabela 5), mas a Tabela 3 tem 1352, cerca de 0,7% faltando, sem explicação nem distribuição por grupo. Como a perda é pequena perto do efeito, proposta_baixo; um humano pode preferir incerto porque a perda não é explicada.

Conhecimento da alocação: votação vem de registros administrativos da Comissão Eleitoral, outcome objetivo.

Contaminação: alocação por estado; nos estados de fase única a boca de urna só sai após o fim da votação, então a proibição não tem efeito sobre o controle. É um pressuposto dos autores, não verificado.

Relato seletivo: todos os outcomes listados na p. 19 aparecem nas Tabelas 3 a 8. Há, porém, inconsistências de texto: a p. 12 diz que os eleitores mostram efeito bandwagon, o contrário do achado principal (underdog).

Outros riscos (domínio decisivo): na análise estadual o grupo tratado é um único estado, Bihar, com uma eleição antes e uma depois; qualquer mudança específica de Bihar entre as eleições é indistinguível do efeito da proibição, e não há teste de tendências prévias para essa amostra. O controle para demografia estadual usa na prática oito observações estado-período. Os erros-padrão são robustos por observação, não agrupados por estado, o que superestima a precisão com um só estado tratado. A delimitação de 2008 mudou as fronteiras das circunscrições entre os períodos, impedindo painel. O texto não documenta se houve boca de urna divulgada entre fases na eleição pré-proibição de Bihar (a p. 10 relata restrições anteriores da Comissão Eleitoral, em 1998). Proposta_alto.

Geral (não há variável no codebook): pelo pior domínio, alto.

Sem perguntas com SI. Resultado localizado conforme indicado pelo coordenador.
