---
citekey: Chatterjee2019a
ficha_id: Chatterjee2019a#apoio_ao_lider
n_fichas_do_texto: 2
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Chatterjee2019a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Chatterjee2019a-epoc
data_fichamento: 2026-09-23
ferramenta: epoc
paginas_pdf: 33
faixas_lidas: 1-20,21-33
---

## 00_Resultado
- **desenho_epoc** — resposta: grupo_controle — evidência: "We have used difference-in-difference setup" (p. 18)
- **resultado_avaliado** — resposta: Tabela 3, bloco Winner, coluna 2 (com controles: population, sex ratio, literacy, total electors, urban employment), DiD — evidência: "2.921*" (p. 21)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: (derivado de: comparação não randomizada entre estados definidos pelo calendário eleitoral pré-existente, não por sorteio; "conducting such experiment is infeasible and impractical" (p. 18))
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: (derivado de: desenho antes-depois controlado por DiD, sem alocação central nem por unidade; "comparing the same states from an earlier round" (p. 18))
- **cg_linha_base_outcome** — resposta: proposta_incerto — evidência: (derivado de: o teste de tendências paralelas (Figura 2) foi feito só com a amostra de eleições nacionais, não com a amostra de eleições estaduais (Tabela 3) usada neste resultado; os próprios autores dizem que a suposição contrafactual não é testável diretamente; "it is statistically not possible to accurately test this" (p. 23))
- **cg_caracteristicas_base** — resposta: proposta_alto — evidência: (derivado de: população, razão de sexo, alfabetização, eleitores e emprego urbano só entram como controles de regressão, sem tabela comparando esses valores entre os grupos tratado e controle; "These variables include population, sex ratio, literacy , total electors and urban employment" (p. 15))
- **cg_dados_incompletos** — resposta: proposta_incerto — evidência: (derivado de: na Tabela 3 (bloco Winner), o N é 1352 nas colunas sem e com controles, sem discussão textual da diferença entre esse N e o universo de 681 constituências x 2 eleições)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: (derivado de: desfecho é dado administrativo objetivo dos relatórios da comissão eleitoral, não sujeito a mascaramento; "We use administrative data from the statistical reports" (p. 14))
- **cg_contaminacao** — resposta: proposta_baixo — evidência: (derivado de: o próprio mecanismo do desenho impede contaminação, já que o resultado só é divulgado ao final do dia de votação; "cannot affect the behavior of voters of single-phase election" (p. 18))
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: (derivado de: todos os desfechos anunciados na seção empírica (vote share, comportamento de candidatos, turnout, margem) aparecem nos resultados; "Our final set of outcomes include voter turnout and winning margin" (p. 19))
- **cg_outros_riscos** — resposta: proposta_alto — evidência: (derivado de: os próprios autores reconhecem risco de resposta sistematicamente diferente ao banimento entre os estados comparados, ligado a pautas eleitorais distintas; "electorate in the states chosen for the analysis systematically differ" (p. 22))

## C_ITS
- **its_teste_t_sem_tendencia** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=grupo_controle)
- **its_intervencao_independente** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=grupo_controle)
- **its_forma_efeito_pre_especificada** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=grupo_controle)
- **its_coleta_nao_afetada** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=grupo_controle)
- **its_conhecimento_alocacao** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=grupo_controle)
- **its_dados_incompletos** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=grupo_controle)
- **its_relato_seletivo** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=grupo_controle)
- **its_outros_riscos** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=grupo_controle)

## Notas do codificador
Desenho: DiD com unidades agregadas (estados/constituências), comparando estados que tiveram eleições pouco antes e pouco depois do banimento de exit polls (Lei de 2009), e cruzando essa variação temporal com a divisão estrutural entre estados "sempre multifásicos" e "sempre monofásicos" (equação 1, p. 18). Não há randomização em nenhum nível; por isso `cg_sequencia_aleatoria` e `cg_ocultacao_alocacao` são obrigatoriamente `proposta_alto` pela regra da ferramenta para desenhos não randomizados/antes-depois controlados.

`cg_linha_base_outcome`: o único teste de pré-tendências do artigo (seção 4.3, Figura 2, p. 22-23) foi feito com a amostra de eleições gerais/nacionais, não com a amostra de eleições estaduais que gera a Tabela 3 usada neste resultado (`apoio_ao_lider`). Não há checagem de linha de base equivalente relatada para a amostra estadual, e os autores afirmam explicitamente que a suposição contrafactual "is statistically not possible to accurately test" — por isso optei por `incerto` em vez de aproveitar o resultado favorável da Figura 2, que se refere a outra subamostra.

`cg_caracteristicas_base`: população, razão de sexo, alfabetização, eleitores totais e emprego urbano (p. 15) entram só como covariáveis de controle nas regressões; não encontrei nenhuma tabela de balanceamento comparando essas características entre os grupos "always multi" e "always single" (a Tabela 2, p. 16, é estatística descritiva geral da amostra, não dividida por grupo). Por isso `alto`.

`cg_dados_incompletos`: na Tabela 3 (bloco Winner, ambas as colunas) N=1352; não há qualquer nota do texto explicando por que esse N é menor que o universo teórico de 681 constituências x 2 eleições = 1362 (número que aparece nas regressões de comportamento de candidatos, Tabela 5). Como o texto não discute a causa dessa diferença, mantive `incerto` em vez de presumir que a perda é inócua.

`cg_outros_riscos`: na seção 4.2 (p. 21) os próprios autores levantam a possibilidade de que "the electorate in the states chosen for the analysis systematically differ in their response to the exit poll ban" por causa de pautas eleitorais diferentes entre eleições estaduais e nacionais e de voto cruzado (split-ticket voting); tratei isso como risco adicional reconhecido pelos autores, e não como uma limitação genérica de generalização.

Resumo do algoritmo: pelo pior domínio entre os nove itens de C_Grupo_controle (quatro em `alto`: sequência aleatória, ocultação, características de base, outros riscos), a proposta geral informal seria `alto`. Este campo não existe no codebook v0 (`codebook_v0_epoc.csv` não tem variável de julgamento geral), por isso não foi escrito como linha de ficha — fica só registrado aqui para o humano que for consolidar.

Resultado de `{RESULTADOS}` localizado sem problemas: Tabela 3, bloco Winner, coluna 2 (com controles), p. 21 (impressa 20).
