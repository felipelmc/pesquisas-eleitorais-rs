# Notas do coordenador sobre o gate de citações (elegibilidade)

- Black2012: o verify_citacoes.py marcou as 10 citações como PDF_TEXTO_NAO_EXTRAIVEL por falso positivo da heurística (fração alfabética 0,457 nas primeiras 20 mil letras, puxada pelos pontilhados do sumário; o PDF tem camada de texto). Conferência com as mesmas funções do gate, sem a heurística (03-textos/prompts_fichamento/gate_sem_heuristica.py): 10 OK, 0 problemas. As 3 evidências citadas como "(p. ii)" (folha de rosto, numeração romana, fora do regex do gate) foram conferidas pelo coordenador com pdftotext na página 2 do PDF.
- Fairstein2019a v1 (elegib-opus5-016): 1 citação NAO_ENCONTRADA (outros_relatos_mesmo_estudo, p. 5); ficha movida para _reprovadas/ e refeita por subagente novo (elegib-opus5-018).
- Fairstein2019a v2 (elegib-opus5-018): o subagente rodou o gate por conta própria e trocou 1 citação no mesmo contexto (p. 5 → p. 4); gate do coordenador: 16/16 OK. A partir daqui o prompt proíbe o fichador de rodar o verificador.
- Fairstein2018a v1 (elegib-opus5-019): 1 citação PAGINA_ERRADA (outros_relatos_mesmo_estudo, p. 14); movida para _reprovadas/ e refeita por subagente novo (elegib-opus5-020).
- Klor2017a v1 (elegib-opus5-022): 1 citação NAO_ENCONTRADA (c3_desfecho, p. 23); movida para _reprovadas/ e refeita por subagente novo (elegib-opus5-025).
- Klor2017a v2 (elegib-opus5-025): a mesma citação de c3 (p. 23) reprovou de novo. Causa: a camada de texto do PDF codifica a ligadura 'ff' como '¤' ('di¤erence'), que o gate não normaliza; o trecho confere visualmente (pdftotext p. 23). Refeita por subagente novo (elegib-opus5-027) com a dica geral, acrescentada ao prompt, de evitar palavras com ligaduras nas evidências.
- Morton2013a: ficha (elegib-opus5-024) descartada, não por reprovação de conteúdo: o PDF era o mesmo de Morton2015a (outro relato); o relato de 2013 ficou como não recuperado.
- Dahlgaard2015a v1 (elegib-opus5-029): 1 citação NAO_ENCONTRADA (c3, p. 14): o fichador corrigiu um erro de digitação do original ('hvis der valg i morgen' → 'hvis der var valg'); refeita por subagente novo (elegib-opus5-030).
- Desvio operacional: documentos com mais de 300 páginas (Posavec2015a 339, Anon2022b 356, Belo2013 677) são lidos por plano documentado (sumário, introdução, capítulos de método/resultados/conclusão inteiros, demais capítulos pelas duas primeiras páginas), não página a página, por limite de contexto do subagente; registrado no prompt (item 7) e nas notas de cada ficha.
- CarreraBarroso2022a v1 (elegib-opus5-059): 1 citação NAO_ENCONTRADA (c2, p. 164): o fichador trocou 'se realizó de una muestra' por 'con una muestra'; refeita por subagente novo (elegib-opus5-061).
- Ragozzino2014c: gate 18/18 OK; as 4 evidências com página romana (p. iv, v), fora do regex do gate, foram conferidas pelo coordenador com pdftotext nas pp. 4 e 5 do PDF.
- Witsman2016a: gate 10/10 OK; as 3 evidências com página romana (p. iii) foram conferidas pelo coordenador com pdftotext na p. 4 do PDF.
- Mavridis2016a: ficha (elegib-opus5-090) descartada porque o PDF era de outro trabalho (texto_confere = Não); o verificar_conteudo.py deu 'confere' por falso positivo com título genérico.
- Posavec2015a v1 (elegib-opus5-096): 1 citação PAGINA_ERRADA (c1, citada como p. 294; o trecho está na p. impressa 248); refeita por subagente novo (elegib-opus5-098).
- Daigle2010a: gate marcou PDF_TEXTO_NAO_EXTRAIVEL nas 18 citações por falso positivo da heurística (fração alfabética 0,484, puxada pelo sumário e pelas tabelas); conferência com as mesmas funções do gate, sem a heurística: 18 OK, 0 problemas.
- Posavec2015a v2 (elegib-opus5-098): a mesma citação de c1 (p. 294) reprovou de novo. Conferência do coordenador na página citada (PDF 295, rodapé "294"): o trecho está lá, mas o original traz "punoljetnoga stanovništva" e as duas fichas transcreveram "punoljetnog". Diferença de uma letra, numa variante morfológica do croata. Não houve terceira releitura do livro (339 páginas) porque a exclusão do texto se apoia em c4 (surveys transversais com exposição autorrelatada) e não nessa evidência. A ficha fica como está e entra no consolidar marcada pelo gate; o caso vai à fila humana com esta nota.
- Belo2013: gate marcou PDF_TEXTO_NAO_EXTRAIVEL por falso positivo da heurística; conferência sem a heurística e das 3 evidências em página romana (p. i, conferidas na p. 2 do PDF) feita pelo coordenador.

## Gasperoni2015a — tentativa 1 (fichador_el_092): REPROVADA
Gate: 14 OK, 4 PAGINA_ERRADA, 1 NAO_ENCONTRADA (total 19, problemas 5).
Diagnóstico do coordenador: o deslocamento não é uniforme (p. 7 -> 8, p. 17 -> 19, p. 19 -> 20), logo não é erro de `offset_pagina`, e sim paginação anotada a olho. A citação de c5_estudo_primario ("performed thorough quota sampling") não existe no PDF em nenhuma página: o fichador relatou ter reproduzido um erro de digitação do original, mas o original não traz essa forma.
Ação: ficha movida para _reprovadas/ e reenviada a um fichador novo, em contexto limpo (fichador_el_094).
Tentativa 2 (fichador_el_094): APROVADA, 14 citações, 0 problemas. O fichador novo manteve `indice-do-PDF` com offset 0 e reabriu folha a folha as páginas citadas.

## Scheuerman2020 — tentativa 1 (fichador_el_102): REPROVADA
Gate: 11 OK, 1 NAO_ENCONTRADA (total 12, problemas 1), em c3_desfecho.
Diagnóstico do coordenador: a página estava certa (p. 4), mas a citação juntou dois pedaços separados do original, suprimindo sem reticências a oração do meio. O texto da p. 4 é "we explore which strategies people use, if they maximize expected utility, and whether people vote truthfully...". Não é erro de paginação: é citação não literal.
Ação: ficha movida para _reprovadas/ e reenviada a um fichador novo, em contexto limpo (fichador_el_105).
Tentativa 2 (fichador_el_105): APROVADA, 16 citações, 0 problemas.

## Freden2021 — tentativa 1 (fichador_el_106): REPROVADA
Gate: 10 OK, 1 NAO_ENCONTRADA (total 11, problemas 1), em c2_intervencao_estudada.
Diagnóstico do coordenador: página certa (p. 3), diferença de uma letra. O original escreve "compared with election campaign opinion polls levels in order to measure" e a ficha registrou "opinion poll levels". O fichador corrigiu silenciosamente um erro de concordância do original, o que quebra a literalidade.
Ação: documento curto (10 páginas), refeito por fichador novo em contexto limpo (fichador_el_109) em vez de aceitar a variante.
Tentativa 2 (fichador_el_109): APROVADA, 12 citações, 0 problemas.

## Houser2011 — tentativa 1 (fichador_el_121): REPROVADA
Gate: 14 OK, 5 PAGINA_ERRADA (total 19, problemas 5), todas em variáveis de identificação (texto_confere, tipo_documento, c6_nao_retratado).
Diagnóstico do coordenador: as citações são literais e estão na capa (folha 1 do PDF), conferido por mim com busca direta no texto extraído. O erro é de convenção de página: o fichador declarou `offset_pagina: 3` e anotou a capa como "(p. 1)", que sob esse offset o gate procura na folha 4. A convenção deste projeto, já usada por outros fichadores, é anotar a capa não numerada como "(p. 0)", que com offset 3 cai exatamente na folha 1.
Ação: refeito por fichador novo em contexto limpo (fichador_el_126), com a convenção explicitada no pedido.

## Houser2011 — tentativa 2 (fichador_el_126): REPROVADA, e a culpa da maior parte é do coordenador
Gate: 11 OK, 3 PAGINA_ERRADA, 1 NAO_ENCONTRADA (total 15, problemas 4).
Correção de uma instrução errada minha: eu disse ao fichador que a convenção do projeto é anotar material sem numeração impressa como "(p. 0)" para cair na primeira folha do PDF. **Isso só vale quando `offset_pagina` é 1.** O gate resolve `folha_do_PDF = pagina_anotada + offset_pagina`; neste documento o offset é 3 (capa, folha de rosto e resumo antes da página impressa 1), então "(p. 0)" aponta para a folha 3, e não para a folha 1, onde as três citações de fato estão. O fichador percebeu e avisou antes de eu rodar o gate; a ficha reprovou pela minha instrução, não por erro dele.
A quarta falha é independente e é de camada de texto: a citação de c4 ("first two subjects were randomly chosen to be candidates") existe na folha 18, mas o PDF extrai a ligadura "fi" de forma corrompida ("n orst two subjects"), como já ocorrera em Klor2017a. Conferido por mim com busca direta no texto extraído.
Ação: terceira tentativa com fichador novo (fichador_el_130), agora com a regra de página enunciada corretamente e com o aviso de ligadura.

## Moreno2016 — tentativa 1 (fichador_el_128): ACEITA com incidente documentado
Gate: 14 OK, 1 NAO_ENCONTRADA (total 15, problemas 1), em `registro_financiamento`.
Diagnóstico do coordenador: a citação existe na folha 2, exatamente onde o fichador a anotou. A camada de texto deste PDF suprime a ligadura "fi": "financial support from Junta de Andalucía (SEJ-5980 and P09-SEJ-4941REC)" é extraído como "...nancial support from junta de andalucia (sej5980 and p09sej4941rec)". Conferi por busca direta no texto extraído: "Junta de Andalucía" e "SEJ-5980" aparecem na folha 2; o único trecho que não casa é a palavra com ligadura.
Decisão: aceitar, em vez de mandar reler 36 páginas por um glifo. Critérios usados, os mesmos de Posavec2015a: (a) localizei a evidência de forma independente; (b) a única divergência é um glifo que o extrator corrompe, não o conteúdo; (c) a variável afetada não é critério de elegibilidade (c1 a c6 passaram todos). Registrado aqui para o relato.
Tentativa 3 (fichador_el_130): APROVADA, 9 citações, 0 problemas. Com a regra de paginação enunciada pela fórmula, o fichador anotou a capa como (p. -2) sob offset 3, e escolheu evidências sem ligaduras. A ficha tem menos citações que as anteriores porque as evidências com "fi" foram trocadas por alternativas.

## Yosef2017 — tentativa 1 (fichador_el_134): REPROVADA
Gate: 12 OK, 2 NAO_ENCONTRADA (total 14, problemas 2), em c2_intervencao_estudada e c4_desenho_elegivel.
Diagnóstico do coordenador, por busca direta no texto extraído:
- c4: o original da folha 5 diz "note that **humans** had no idea whether they were playing against humans or against bots"; a ficha registrou "Note that the **students** had no idea whether they were". Troca de palavra, não artefato de extração — o documento usa "students" em outras frases da mesma página, o que explica a confusão, mas a citação deixa de ser literal.
- c2: "this paper is to examine how the deadline" não existe de forma contígua na folha 1; o trecho atravessa a quebra ("the focus of this" termina a folha).
Ação: refeito por fichador novo em contexto limpo (fichador_el_136), com aviso sobre trechos que atravessam quebra de página ou de coluna.

## Velden2017a — tentativa 1 (fichador_el_135): REPROVADA
Gate: 0 OK, 8 PAGINA_ERRADA (total 8, problemas 8). Todas as citações falharam, inclusive as dos seis critérios.
Diagnóstico do coordenador: erro uniforme de uma unidade. Localizei cinco das oito citações por busca direta no texto extraído e todas estão exatamente uma folha adiante do que a ficha prevê (delta 17, não 16). O conteúdo das citações existe e é literal; o que está errado é o ancoramento de página, de ponta a ponta. O fichador declarou `offset_pagina: 16` e disse tê-lo conferido em p. 23 = folha 39 e p. 103 = folha 119, mas as páginas anotadas nas evidências saíram uma unidade abaixo da página impressa real.
Decisão: reprovar, e não aceitar com documentação. O critério que usei em Moreno2016 (aceitar) exigia que a falha fosse artefato de extração e não atingisse critério de elegibilidade; aqui nenhuma citação está verificada pelo gate, inclusive as de c1 a c6. Refeito por fichador novo em contexto limpo (fichador_el_137), com instrução de validar o offset contra as próprias citações antes de fechar.
Yosef2017, tentativa 2 (fichador_el_136): APROVADA, 13 citações, 0 problemas.
Velden2017a, tentativa 2 (fichador_el_137): APROVADA, 8 citações, 0 problemas. O offset correto é 17, confirmado em cinco pontos distantes e validado contra cada citação antes de fechar, como pedido.

## Anon2021 — tentativa 1 (fichador_el_143): REPROVADA
Gate: 8 OK, 1 NAO_ENCONTRADA (total 9, problemas 1), em c4_desenho_elegivel.
Diagnóstico do coordenador: a frase está na folha 10 (p. impressa 266), exatamente onde o fichador a anotou, mas a camada de texto corrompe parte dos caracteres cirílicos num trecho específico: o PDF extrai "інтуітивним та творчім" onde o texto visível traz "інтуїтивним та творчим" (perde o trema de "ї" e troca "и" por "і"). As outras oito citações, em trechos de corpo normal, passaram sem problema, o que indica corrupção restrita a um run de fonte (provavelmente itálico), não ao documento inteiro.
Decisão: reprovar e refazer, e não aceitar com documentação, porque desta vez a falha atinge um critério de elegibilidade (c4) — a exceção que abri em Moreno2016 estava limitada a variável que não é critério. Documento curto (14 páginas), refeito por fichador novo (fichador_el_144) com aviso para evitar trechos em itálico.
Anon2021, tentativa 2 (fichador_el_144): APROVADA, 9 citações, 0 problemas. Bastou evitar trechos em itálico, onde a extração corrompe ї e и.

## Brownback2024 — tentativa 1 (fichador_el_147): REPROVADA
Gate: 13 OK, 1 NAO_ENCONTRADA (total 14, problemas 1), em c2_intervencao_estudada.
Diagnóstico do coordenador: a folha 2 (p. impressa 450) diz "we reveal random subsamples from an **assigned** information source (poll data or actual choice behaviors)"; a ficha registrou "random subsamples from an **actual** information source". A palavra "actual" aparece logo adiante na mesma frase, o que explica a troca. É erro de literalidade, não artefato de extração, e atinge critério de elegibilidade.
Ação: refeito por fichador novo em contexto limpo (fichador_el_150), com aviso sobre trocar palavra por outra da vizinhança.
Brownback2024, tentativa 2 (fichador_el_150): APROVADA, 16 citações, 0 problemas.

## Corbetta2013 — PDF digitalizado, sem camada de texto
O arquivo recuperado tem 26 páginas e nenhuma camada de texto (`pdftotext` devolve vazio). O fichador precisa lê-lo pela ferramenta Read, que enxerga a imagem da página; o gate de citações vai marcar todas as evidências como PDF_TEXTO_NAO_EXTRAIVEL, que a consolidação não trata como reprovação. Registrado aqui para que o relato não confunda esse caso com citação não verificada por erro do fichador.
Resultado do gate em Corbetta2013: 15 NAO_ENCONTRADA, 0 OK. A heurística PDF_TEXTO_NAO_EXTRAIVEL não disparou porque a extração devolve string vazia, e não texto com baixa fração alfabética; o efeito prático é que as citações de um PDF digitalizado são indistinguíveis, para o verificador, de citações inventadas. A consolidação vai marcar o texto como `incerto`. Não é possível, com este arquivo, separar as duas hipóteses por meios automáticos: a decisão vai à fila humana.
