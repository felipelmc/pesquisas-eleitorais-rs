---
citekey: Anon2021
ficha_id: Anon2021
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Anon2021.pdf
paginacao: impressa
offset_pagina: -256
agente_fichador: fichador_el_143
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim; o título e a autora impressos no documento coincidem com os metadados do registro (a divergência de intervalo de páginas dentro do DOI está nas notas) — evidência: "УЯВНЕ, АРХЕТИПИ І СОЦІАЛЬНЕ ПРОГНОЗУВАННЯ: МОЖЛИВОСТІ ТА ОБМЕЖЕННЯ ЗАСТОСУВАННЯ" (p. 257)
- **tipo_documento** — resposta: artigo — evidência: "яка визначає мету пропонованої статті" (p. 262)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Não; o texto trata do suporte informacional e analítico da administração pública na parte de prognóstico social, não de eleitores, participantes que escolhem candidatos ou unidades eleitorais agregadas — evidência: "Порушено проблему інформаційно-аналітичного забезпечення державного управління" (p. 257)
- **c2_intervencao_estudada** — resposta: Não; nenhum resultado de pesquisa eleitoral é exposição manipulada, com variação natural identificada ou medida em painel, eleições aparecem apenas como exemplo da literatura sobre previsão citada pela autora — evidência: "результатів президентських виборів у США" (p. 263)
- **c3_desfecho** — resposta: Não; não há desfecho de voto nem de comparecimento, o objeto é delimitar possibilidades e limites das abordagens psicológicas no prognóstico social — evidência: "в окресленні можливостей та меж застосування психологічних підходів" (p. 258)
- **c4_desenho_elegivel** — resposta: Não; artigo teórico e conceitual, sem experimento, quase-experimento ou painel individual, a estratégia proposta é a retrodução como raciocínio interpretativo — evidência: "Сама по собі ретродукція є радше інтуїтивним та творчим процесом" (p. 266)
- **c5_estudo_primario** — resposta: Não; ensaio teórico sem análise própria de dados, construído sobre literatura e publicações anteriores da autora (revisão: usar na bola de neve) — evidência: "Результати проведеного дослідження дають підстави стверджувати" (p. 258)
- **c6_nao_retratado** — resposta: Sim; não há marca "RETRACTED", nota ou página de retratação no documento — evidência: "УЯВНЕ, АРХЕТИПИ І СОЦІАЛЬНЕ ПРОГНОЗУВАННЯ" (p. 257)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: A autora remete às suas publicações anteriores sobre arquetípica social, referências [16–18] da lista do artigo; não há menção a outro relato do mesmo estudo empírico (versão anterior, tese, working paper ou artigo com os mesmos dados) — evidência: "У своїх попередніх публікаціях" (p. 265)
- **fonte_dados_amostra** — resposta: 999 — evidência: 999
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Offset: o PDF tem 14 folhas e a numeração impressa vai de 257 (folha 1) a 270 (folha 14), conferida no rodapé das folhas 1 (257), 6 (262), 10 (266), 11 (267) e 14 (270). Logo `folha_do_PDF = pagina_anotada - 256`, isto é, `offset_pagina: -256`, e as páginas das evidências são as impressas. Todas as páginas citadas foram reabertas e as citações conferidas caractere a caractere; as citações em ucraniano foram copiadas do original, sem tradução e sem correção.
- Documento lido por inteiro (folhas 1 a 14, páginas impressas 257 a 270), em ranges de até 20 páginas, incluindo resumos em ucraniano, russo e inglês, corpo do texto, conclusões e as duas listas de referências.
- `texto_confere` = Sim: o título na página 257 é idêntico ao do registro e a autora é "Суший Олена Володимирівна" (primeira autora e única do texto), o que corresponde a "Суший, Olena" do registro. O DOI impresso na primeira página termina em "2021-1(26)-257-270", enquanto o DOI do registro termina em "2021-1(26)-248-260": conforme a nota do coordenador, trata-se de divergência de metadado da fonte no intervalo de páginas, e não de outro documento, por isso não usei "parcial" (que o codebook reserva para outra versão do mesmo trabalho).
- Critérios: o artigo é uma discussão teórico-metodológica sobre prognóstico social, arquétipos e o imaginário de G. Durand, no campo da administração pública. Pesquisas e previsões eleitorais só aparecem na revisão de literatura (Dowding sobre modelos de previsão de eleições presidenciais nos EUA, p. 263; Westwood, Messing e Leikes sobre previsões probabilísticas, p. 264; Norris, Dumville e Lacy sobre a eleição de 2008, p. 264), nunca como exposição analisada. Daí "Não" em c1 a c5. Nenhum critério ficou em 999, porque o documento descreve com clareza seu objeto e sua abordagem.
- `c5_estudo_primario` = Não com a frase exigida pela convenção do projeto: é ensaio teórico sem dados próprios, portanto entra na regra de "revisão: usar na bola de neve".
- `fonte_dados_amostra` = 999: o texto não relata fonte de dados, período nem tamanho de amostra, porque não há coleta ou análise empírica própria; não derivei nada da menção a uma avaliação de especialistas citada na página 260, que é dado de terceiros trazido como ilustração.
- `registro_financiamento` = 999: não há nota de pré-registro (OSF, AEA, RIDIE, EGAP) nem identificação de projeto financiado, edital ou número de processo em nenhuma página, inclusive na folha de rosto e ao fim do texto.
- `outros_relatos_mesmo_estudo`: registrei a menção às publicações anteriores da própria autora por ser a única remissão desse tipo no documento, mas deixei explícito na resposta que não se trata de outro relato do mesmo estudo, para não induzir ligação indevida.
