---
citekey: Ergin2018
ficha_id: Ergin2018
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Ergin2018.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: fichador_el_152
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — evidência: "Strategic Voting and Social Welfare Rules" (p. 6)
- **tipo_documento** — resposta: tese — evidência: "to obtain the degree of Doctor at the Maastricht University," (p. 6)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: parcial, o documento não tem amostra empírica: é teoria da escolha social axiomática, com agentes abstratos que ordenam alternativas, parte em eleições hipotéticas (Cap. 3 e 4) e parte em delegações de comitê ou conferência de paz (Cap. 2), contexto que o protocolo exclui. — evidência: "chapters in this dissertation deal with social choice theory" (p. 21); "In many situations, individuals participate in collective decision making via" (p. 26)
- **c2_intervencao_estudada** — resposta: Não, nenhum resultado de pesquisa eleitoral é exposição; o objeto são regras de agregação de preferências (regras de bem-estar social) e seus axiomas. — evidência: "Social choice theory is interested in how to move from these individual" (p. 21)
- **c3_desfecho** — resposta: Não, não há desfecho de voto nem de comparecimento medido ou analisado; o que se analisa é a compatibilidade entre axiomas (Condorcet e participação) das regras. — evidência: "incompatibility between these two concepts when using social welfare rules" (p. 23)
- **c4_desenho_elegivel** — resposta: Não, desenho teórico e axiomático (definições, lemas, proposições e teoremas de caracterização), sem dados e sem variação identificada de exposição. — evidência: "we show that the conditions of Pareto optimality, consistency" (p. 44)
- **c5_estudo_primario** — resposta: parcial, é trabalho original do autor (teoremas e provas próprios), mas não há dados nem análise própria de dados; não é revisão de literatura, revisão sistemática, meta-análise, editorial nem comentário. — evidência: "this thesis in its total follows the discipline of social" (p. 127)
- **c6_nao_retratado** — resposta: Sim, não há marca 'RETRACTED', nota nem página de retratação em nenhuma folha do documento. — evidência: "Strategic voting and social welfare rules" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim, o Cap. 2 declara basear-se em Can, Csóka e Ergin (2017) e o Cap. 3 em Can, Ergin e Pourpouneh (2017), ambos Research Memoranda da Maastricht University (GSBE). — evidência: "Based on Can, Csóka, and Ergin (2017)." (p. 26); "Based on Can, Ergin, and Pourpouneh (2017)." (p. 52)
- **fonte_dados_amostra** — resposta: 999 — evidência: 999
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador

**Paginação.** A numeração impressa reinicia por parte: as folhas 1 a 9 do PDF (capa do repositório, capa do livro, folha de rosto, composição da banca, dedicatória) não têm número impresso; as folhas 10 a 18 trazem algarismos romanos (i a ix); e o corpo traz algarismos arábicos de 1 a 111, com `folha do PDF = página impressa + 19` (verificado em duas folhas distantes: folha 20 = página impressa 1, início do Capítulo 1; folha 40 = página impressa 21). Como as evidências de `texto_confere`, `tipo_documento` e `c6_nao_retratado` vêm obrigatoriamente das folhas de rosto (folhas 1 e 6), que não têm número impresso, não existe offset único válido para todas as minhas evidências. Por isso declarei `paginacao: indice-do-PDF` com `offset_pagina: 0`: **todas as páginas citadas nesta ficha são folhas do PDF (1-based)**, e cada citação foi reaberta e conferida na folha indicada.

**Faixas lidas (item 7 do prompt, documento longo).** Li o PDF inteiro, folhas 1 a 131, nas faixas 1-20, 21-40, 41-60, 61-80, 81-100, 101-120 e 121-131; depois reabri as folhas 21-26, 44 e 52 para conferir as citações. Ou seja, todas as partes exigidas pelo item 7 foram lidas por inteiro: sumário e listas (folhas 13-18), introdução (folhas 20-25), os três capítulos substantivos (Cap. 2, folhas 26-51; Cap. 3, folhas 52-67; Cap. 4, folhas 68-93), as conclusões de cada capítulo (folhas 49-51, 66-67, 92-93), a bibliografia (folhas 94-100), os apêndices A e B (folhas 102-125), a Valorisation (folhas 126-128) e o Curriculum Vitae (folha 130).

**Onde está a parte relevante para os critérios.** Não há capítulo de método empírico, dados ou resultados: os três capítulos são teóricos. A parte decisiva para c1 a c5 é o **Capítulo 1 (Introduction), folhas 20-25**, em especial a seção "Outline of the Chapters 2-4" (folhas 22-25), que descreve o desenho de cada capítulo; e as seções de modelo, que fazem as vezes de método — **2.2 "Basic notation and preliminary results" (folhas 31-38)**, **3.2 "Model" (folhas 54-55)** e **4.2 "Model" (folhas 72-78)** — todas puramente axiomáticas, com definições, lemas, proposições e provas. A **Valorisation (folhas 126-128)** confirma em prosa não técnica que a tese "in its total follows the discipline of social choice theory".

**c1 = parcial.** Decisão limítrofe. Contra "Sim": não existe amostra nem participante algum; os "eleitores" são agentes matemáticos num modelo axiomático, e o Capítulo 2 interpreta o problema como a escolha de delegados para um comitê ou conferência de paz, que o protocolo exclui ("votações de órgãos deliberativos"). A favor de "Sim": o protocolo aceita eleição hipotética, e os Capítulos 3 e 4 falam explicitamente de eleitores que escolhem entre alternativas e decidem votar ou se abster. Como a convenção do projeto manda usar 'parcial' para o caso ambíguo, e como a exclusão do texto se decide de forma inequívoca em c2 e c4, registrei 'parcial' em vez de forçar 'Sim' ou 'Não'.

**c3 = Não.** O Capítulo 3 trata da decisão de votar ou se abster, o que à primeira vista toca comparecimento; mas isso aparece como axioma sobre regras de agregação ("participation criterion"), não como comparecimento real, validado, agregado ou intenção de comparecer, e não há variável dependente de voto. Não é caso da ressalva sobre falta de dados numéricos: não há desfecho medido nem analisado empiricamente.

**c5 = parcial.** O prompt define 'Não' por uma lista (revisão, revisão sistemática, meta-análise, editorial, comentário) na qual o documento não se encaixa, mas a pergunta exige "análise própria de dados", que também não existe. Registrei 'parcial' e não escrevi 'revisão: usar na bola de neve', porque o documento não é revisão: é pesquisa original teórica. A bibliografia é extensa, mas não há síntese de evidência.

**999.** `fonte_dados_amostra` = 999 porque o documento não relata fonte de dados, período nem tamanho de amostra: não há dados. `registro_financiamento` = 999 porque não há identificador de pré-registro nem número de processo ou edital; os agradecimentos (folha 10) mencionam apoio da GSBE e um "International Travel Grant", sem qualquer número, e transcrever isso como identificador seria inferência.

**c6.** A checagem externa de retratação (OpenAlex, Crossref, página do repositório) não é minha; verifiquei apenas o documento, folha a folha, e não há aviso de retratação.
