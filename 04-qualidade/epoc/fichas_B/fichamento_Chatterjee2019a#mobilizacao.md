---
citekey: Chatterjee2019a
ficha_id: Chatterjee2019a#mobilizacao
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
- **resultado_avaliado** — resposta: Tabela 7, bloco Voter Turnout, coluna 2 (com controles: population, sex ratio, literacy, total electors, urban employment), DiD — evidência: "4.706***" (p. 28)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: (derivado de: comparação não randomizada entre estados definidos pelo calendário eleitoral pré-existente, não por sorteio; "conducting such experiment is infeasible and impractical" (p. 18))
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: (derivado de: desenho antes-depois controlado por DiD, sem alocação central nem por unidade; "comparing the same states from an earlier round" (p. 18))
- **cg_linha_base_outcome** — resposta: proposta_incerto — evidência: (derivado de: o teste de tendências paralelas (Figura 2) foi feito só com a amostra de eleições nacionais, não com a amostra de eleições estaduais (Tabela 7) usada neste resultado; os próprios autores dizem que a suposição contrafactual não é testável diretamente; "it is statistically not possible to accurately test this" (p. 23))
- **cg_caracteristicas_base** — resposta: proposta_alto — evidência: (derivado de: população, razão de sexo, alfabetização, eleitores e emprego urbano só entram como controles de regressão, sem tabela comparando esses valores entre os grupos tratado e controle; "These variables include population, sex ratio, literacy , total electors and urban employment" (p. 15))
- **cg_dados_incompletos** — resposta: proposta_incerto — evidência: (derivado de: na Tabela 7 (bloco Voter Turnout), o N é 1355 nas colunas sem e com controles, sem discussão textual da diferença entre esse N e o universo de 681 constituências x 2 eleições)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: (derivado de: desfecho é dado administrativo objetivo dos relatórios da comissão eleitoral (turnout/poll percentage), não sujeito a mascaramento; "We use administrative data from the statistical reports" (p. 14))
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
Mesmo desenho da ficha `#apoio_ao_lider` (DiD com unidades agregadas, comparando estados por calendário eleitoral antes/depois do banimento de 2009 e por tipo sempre-multifásico/sempre-monofásico, equação 1, p. 18); os julgamentos de C_Grupo_controle são os mesmos porque dependem do desenho do estudo como um todo, não do desfecho específico. Repito aqui as justificativas centrais:

`cg_sequencia_aleatoria` e `cg_ocultacao_alocacao`: `alto` obrigatório porque não há randomização e o desenho é antes-depois controlado (DiD).

`cg_linha_base_outcome`: o teste de tendências paralelas (Figura 2, p. 22-23) inclui uma série de "Vote Share Winner/Runner Up/Others", mas não uma série equivalente de turnout, e mesmo essa figura usa a amostra de eleições nacionais, não a de eleições estaduais que gera a Tabela 7 (usada neste resultado, `mobilizacao`). Sem checagem direta de linha de base para o turnout estadual, mantive `incerto`.

`cg_caracteristicas_base`: mesma ausência de tabela de balanceamento por grupo já descrita na outra ficha (p. 15-16) — `alto`.

`cg_dados_incompletos`: na Tabela 7 (bloco Voter Turnout) N=1355 em ambas as colunas (sem e com controles); não há explicação textual da diferença frente ao universo teórico de 1362 observações. Mantive `incerto`.

`cg_conhecimento_alocacao`: turnout (voter turnout / poll percentage) é dado administrativo objetivo dos relatórios da comissão eleitoral (p. 14) — `baixo`.

`cg_contaminacao` e `cg_relato_seletivo`: mesmas justificativas da outra ficha (mecanismo do desenho evita contaminação; todos os desfechos anunciados nos métodos aparecem nos resultados, incluindo turnout, citado explicitamente em "Our final set of outcomes include voter turnout and winning margin", p. 19) — `baixo`.

`cg_outros_riscos`: mesmo risco reconhecido pelos próprios autores de resposta sistematicamente diferente entre os estados comparados (p. 21-22) — `alto`.

Resumo do algoritmo: pelo pior domínio entre os nove itens de C_Grupo_controle (quatro em `alto`), a proposta geral informal seria `alto`, igual à outra ficha. O codebook v0 (`codebook_v0_epoc.csv`) não tem variável de julgamento geral, por isso não escrevi essa linha na ficha; registro aqui só para quem for consolidar.

Resultado de `{RESULTADOS}` localizado sem problemas: Tabela 7, bloco Voter Turnout, coluna 2 (com controles), p. 28 (impressa 27).
