---
citekey: Gee2024
ficha_id: Gee2024
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Gee2024.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_146
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o documento é o NBER Working Paper No. 31042 (março de 2023), versão de working paper do mesmo trabalho registrado como artigo de 2024 no JEBO; título "Pivotal or Popular: The Effects of Social Information and Feeling Pivotal on Civic Actions" e autores Laura K. Gee, Anoushka Kiyawat, Jonathan Meer e Michael J. Schreck batem com os metadados — evidência: "Pivotal or Popular" (p. 1); "of Social Information and Feeling Pivotal on Civic Actions" (p. 1)
- **tipo_documento** — resposta: working_paper — evidência: "NBER Working Paper No. 31042" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Não — os participantes são estudantes da Tufts num jogo de doação em laboratório e ex-alunos ou pais de alunos de organizações educacionais sem fins lucrativos no campo, que decidem doar a uma instituição, não eleitores escolhendo entre candidatos, partidos ou opções de referendo — evidência: "Students at Tufts University participated in a game" (p. 4); "Subjects were alumni or parents of current students of education non-profits" (p. 8)
- **c2_intervencao_estudada** — resposta: Não — a exposição manipulada é a informação social sobre quantas outras pessoas do grupo já doaram (popularidade) e a pivotalidade do próprio doador para atingir o limiar da doação-contrapartida, e não resultado de pesquisa eleitoral — evidência: "We vary the popularity of the action and whether the person is pivotal" (p. 5)
- **c3_desfecho** — resposta: Não — o desfecho é doação (fazer qualquer doação, doação qualificada de US$ 8 ou mais e valor doado); não há medida de intenção de voto, de voto nem de comparecimento — evidência: "predicting if a subject made a qualifying donation" (p. 7); "increased the likelihood of donating by an order of magnitude" (p. 15)
- **c4_desenho_elegivel** — resposta: Sim — o desenho é experimental aleatorizado: um experimento de laboratório intrassujeito com ordem de tratamentos randomizada e dois experimentos de campo com atribuição aleatória dos sujeitos aos grupos e tratamentos — evidência: "Subjects were assigned treatments in a randomized order" (p. 5); "a subject is randomly assigned to a group of 10 donors" (p. 38)
- **c5_estudo_primario** — resposta: Sim — relata estudo primário com dados próprios de um experimento de laboratório e de dois experimentos de campo conduzidos pelos autores — evidência: "We conduct a laboratory experiment" (p. 1); "We turn to a set of field experiments to test these" (p. 3)
- **c6_nao_retratado** — resposta: Sim — não há marca "RETRACTED", nota ou página de retratação no documento; a primeira página traz apenas a folha de rosto da série de working papers do NBER com o título — evidência: "AND FEELING PIVOTAL ON CIVIC ACTIONS" (p. 0)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: O documento não menciona outra versão deste mesmo trabalho, mas cita estudos anteriores realizados com o mesmo parceiro do Experimento de Campo 1, reportados em Gee, Schreck, and Singh (2020) — evidência: "We ran some previous studies with the partner" (p. 8)
- **fonte_dados_amostra** — resposta: Experimento de laboratório com 118 estudantes da Tufts University em sessões de março e abril de 2018 (subamostra de 41 em oito tratamentos) e dois experimentos de campo de doação por carta/e-mail em 2019, com 26.358 sujeitos (Campo 1) e 1.867 sujeitos (Campo 2), ex-alunos ou pais de alunos de instituições educacionais sem fins lucrativos — evidência: "All 118 subjects make donation choices for at least six treatments" (p. 5); "Field Experiment 1 included 26,358 subjects" (p. 10)
- **registro_financiamento** — resposta: Pré-registro AEARCTR-0008768 (AEA RCT Registry); aprovações de IRB da Tufts 1807022 e 1602011; apoio financeiro agradecido a Sheryl e Warren Rosenfeld, sem número de processo ou edital — evidência: "The experiments are registered under AEARCTR-0008768" (p. 0)

## Notas do codificador
- Offset de página: a numeração impressa começa no corpo do texto. A folha 3 do PDF traz o número impresso "2", a folha 21 traz "20" e a folha 41 traz "40", ou seja, folha do PDF = página impressa + 1 em todo o documento, inclusive nos apêndices (que continuam a numeração corrida, sem reinício). Logo `offset_pagina: 1`. As duas primeiras folhas do PDF (folha de rosto do NBER e página de resumo) não têm número impresso: pela fórmula elas correspondem às páginas 0 e 1, e foi assim que as anotei nas evidências que vêm delas (agradecimentos/registro e título/abstract).
- `texto_confere` = parcial e não Sim porque o PDF é a versão NBER Working Paper No. 31042 (março de 2023) do trabalho, enquanto o registro traz o artigo de 2024 com DOI de periódico; título e autores são os mesmos, então trata-se de outra versão do mesmo trabalho.
- Nas evidências do título evitei o trecho "The Effects", porque "ff" é ligadura tipográfica e pode falhar na verificação automática; o título completo está na resposta de `texto_confere`.
- c4 e c5 foram respondidos pelo critério do próprio prompt de cada variável (tipo de desenho e estudo primário), independentemente de a exposição não ser pesquisa eleitoral: o desenho é experimental aleatorizado (laboratório e campo) e os dados são próprios. A não elegibilidade do texto vem de c1, c2 e c3 (população não eleitoral, exposição de informação social sobre doadores e desfecho de doação, sem voto nem comparecimento).
- Nenhuma variável ficou com 999: todas as informações estavam no documento.
- c6 foi respondido apenas pela inspeção do próprio documento (sem aviso de retratação em nenhuma das 41 folhas); a checagem externa em OpenAlex/Crossref cabe ao coordenador.
