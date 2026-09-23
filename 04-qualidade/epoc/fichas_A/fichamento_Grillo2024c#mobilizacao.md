---
citekey: Grillo2024c
ficha_id: Grillo2024c#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Grillo2024c.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Grillo2024c-epoc
data_fichamento: 2026-09-23
ferramenta: epoc
paginas_pdf: 20
faixas_lidas: 1-20
---

## 00_Resultado
- **desenho_epoc** — resposta: grupo_controle — evidência: "turnout rates at 12:00 as the pre-period and turnout rates at" (p. 6); "17:00 and at the closing time as post-periods" (p. 6)
- **resultado_avaliado** — resposta: mobilizacao: comparecimento departamental (%) no fechamento das urnas, Tabela 1, coluna 1 (DiD base ponderado por eleitores registrados, sem controles de clima), coeficiente Closure X 2nd Round = -3.440 (p < 0,001; EP agrupado por departamento; 96 departamentos, 576 obs.) — evidência: "Closure X 2nd Round" (p. 13); "-3.440" (p. 13)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: "We compare the turnout rates in the second round to those" (p. 3)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: "turnout rates at 12:00 as the pre-period and turnout rates at" (p. 6)
- **cg_linha_base_outcome** — resposta: proposta_baixo — evidência: "Baseline is the turnout at 12:00 in the" (p. 13); "-0.316" (p. 13); "(0.360)" (p. 13)
- **cg_caracteristicas_base** — resposta: proposta_alto — evidência: "Indicator of rain in round 1" (p. 17); "Indicator of rain in round 2" (p. 17); "0.552" (p. 17); "hence all raining variation comes from" (p. 8)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: "presidential elections for all French mainland departments" (p. 13); "576" (p. 13)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "Turnout data from the French Ministry of Interior." (p. 13)
- **cg_contaminacao** — resposta: proposta_incerto — evidência: "Belgian broadcaster RTBF predicted early in the day that Macron" (p. 6)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: "Voter turnout is measured at 12:00, 17:00 and when polling stations closed." (p. 6)
- **cg_outros_riscos** — resposta: proposta_alto — evidência: "similar trends were observed in previous elections" (p. 2); "In all three elections, the increase in turnout from" (p. 7); "-3.091" (p. 14); "-0.349" (p. 14); "(0.488)" (p. 14); "As also forecasted by most opinion polls" (p. 3)

## C_ITS
- **its_teste_t_sem_tendencia** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = grupo_controle)
- **its_intervencao_independente** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = grupo_controle)
- **its_forma_efeito_pre_especificada** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = grupo_controle)
- **its_coleta_nao_afetada** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = grupo_controle)
- **its_conhecimento_alocacao** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = grupo_controle)
- **its_dados_incompletos** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = grupo_controle)
- **its_relato_seletivo** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = grupo_controle)
- **its_outros_riscos** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = grupo_controle)

## Notas do codificador
- Justificativa de `cg_outros_riscos` (movida do campo de resposta pelo coordenador): tendências paralelas provavelmente violadas (queda de comparecimento depois das 12h no 2º turno também em 2007 e 2012; no DDD contra 2007 o efeito no fechamento some) e mudanças simultâneas só no 2º turno (chuva, eleição menos competitiva já prevista pelas pesquisas, eleitorado de esquerda sem candidato)
Desenho: diferenças em diferenças com unidades agregadas (96 departamentos da França continental), em que o "tratamento" é o 2º turno de 2017 (divulgação precoce e confiante de boca de urna pela mídia belga e suíça, a partir de ~16h) e o "controle" é o 1º turno das mesmas unidades; pré = comparecimento às 12h, pós = 17h e fechamento. Classificado como `grupo_controle` (antes-depois controlado). O resultado indicado pelo coordenador foi localizado: Tabela 1, coluna 1, Closure X 2nd Round = -3.440 (p-valor 0.000).

Por domínio:
- Sequência aleatória e ocultação da alocação: antes-depois controlado, portanto proposta_alto por regra da ferramenta.
- Outcome na linha de base: o comparecimento às 12h foi medido nos dois turnos e a diferença entre turnos é pequena e não significativa (2nd Round = -0.316, p = 0.360); o DiD ajusta o nível. Proposta_baixo para o nível de base; o problema de tendências fica em "outros riscos".
- Características de base: as unidades são as mesmas, mas o contexto dos dois "grupos" difere: chuva em 55% das capitais no 2º turno contra 1% no 1º (Tabela 5), além de competitividade e conjunto de candidatos. A coluna 1 (resultado avaliado) não controla o clima; as colunas 3 e 4 (controles de clima; só departamentos sem chuva) dão estimativas parecidas (-3.618; -3.741), o que atenua a preocupação. Pela regra ("alto se diferentes") propus alto; os humanos podem rebaixar para incerto por causa da robustez.
- Dados incompletos: registros administrativos do Ministério do Interior para todos os 96 departamentos continentais (576 obs. = 96 × 3 horários × 2 turnos). Proposta_baixo. Departamentos ultramarinos ficam fora por construção.
- Conhecimento da alocação: desfecho objetivo (comparecimento oficial). Proposta_baixo.
- Contaminação: o grupo controle (1º turno) também recebeu boca de urna divulgada por mídia estrangeira durante a votação, embora mais tarde e com menos confiança (RTBF previu cedo a liderança de Macron). Exposição parcial do controle; tende a enviesar para o nulo. Propus incerto; pode ser lido como alto.
- Relato seletivo: os dois horários pós (17h e fechamento) descritos nos métodos são relatados; não há protocolo ou pré-registro (working paper), então a avaliação se limita à coerência entre métodos e resultados. Proposta_baixo.
- Outros riscos (determinante): o próprio texto mostra que o comparecimento cresce menos depois das 12h no 2º turno também em 2007 e 2012 (Figura 1; Tabela 2: Closure X 2nd Round = -1.781 em 2012 e -3.091 em 2007). No DDD contra 2007 o efeito no fechamento é -0.349 (p = 0.488), ou seja, o padrão recorrente entre turnos explica quase todo o -3.440 da coluna 1. Há também mudanças simultâneas só no 2º turno (chuva, vitória folgada já prevista pelas pesquisas pré-eleitorais, com média de 61,79% para Macron, e eleitores de esquerda sem candidato), que podem mudar a distribuição horária do voto sem relação com a boca de urna. Todos os departamentos são tratados ao mesmo tempo, sem controle espacial não exposto. Proposta_alto.

Geral: o codebook EPOC não tem variável de julgamento geral; pelo pior domínio, o resumo seria proposta_alto (sequência e ocultação são alto por construção; o risco substantivo está em tendências paralelas e mudanças simultâneas).

Nenhuma resposta SI; não há perguntas que exijam contato com os autores.
