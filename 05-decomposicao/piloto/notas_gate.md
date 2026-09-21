# Notas do gate de citações — piloto de extração (G6)

## Araujo2021a — b2_n_total, "NAO_ENCONTRADA" aceita com justificativa

`verify_citacoes.py` reprovou a citação `"N = 452,656" (p. 12)` da variável `b2_n_total`
(offset_pagina = 1, PDF p. 13). Conferi eu mesmo a página: o número está genuinamente
impresso na Figura 2 ("Frontrunner", primeiro painel, "N = 452,656"), mas a figura inteira é
uma imagem rasterizada sem camada de texto — não há como o verificador (que lê a camada de
texto do PDF) confirmar um número que só existe como pixel. O corpo do texto não repete esse N
com essa precisão (só o total de urnas, 454.490, e uma nota de que o N varia por modelo); as
tabelas completas estão num apêndice online que não acompanha o PDF.

Aceito com o mesmo critério já usado na fase de elegibilidade (Moreno2016, ligadura
tipográfica): falha do gate por limitação técnica do arquivo (aqui, ausência de camada de
texto numa figura, não um problema de ligadura), valor conferido de forma independente pelo
coordenador, e variável que não é critério de elegibilidade (é uma variável de extração/
decomposição). Mantida a resposta da ficha (`b2_n_total = 452656`, evidência com a citação
literal da figura); a linha correspondente em `verificacao_citacoes.csv` fica com
`status = NAO_ENCONTRADA`, documentada aqui em vez de refeita por um novo subagente (refazer
não mudaria o resultado: o número seguiria dentro da mesma imagem).

Nenhuma outra citação das 272 verificadas nas três fichas do piloto falhou (271 OK).

## Klor2017a — correção de coordenador em `modelo_principal` (efeitos)

O extrator de efeitos marcou `modelo_principal = sim` em duas linhas para o mesmo estudo × construto (`apoio_ao_lider`): E01 (experimento de laboratório, aleatorizado) e E04 (análise transversal de 143 eleições para governador dos EUA, associação sem variação identificada). Os próprios autores chamam essa segunda análise de correlacional, sem identificação causal (ficha de elegibilidade, Notas: "os autores reconhecem que a análise empírica é correlacional e não estabelece causalidade"). O protocolo deste projeto nunca agrega desenho aleatorizado e não aleatorizado na mesma célula de síntese.

Corrigido por mim (coordenador de IA, autopiloto): `Klor2017a-E04.modelo_principal` de `sim` para `nao`. E01 (RCT) permanece como o único principal deste estudo × construto — é a análise que de fato satisfaz o critério C4 de elegibilidade do protocolo (desenho que identifica o efeito). A linha E04 continua no CSV de efeitos, disponível para menção narrativa/SWiM como evidência correlacional complementar, mas não entra na meta-análise como estimativa principal do estudo.
