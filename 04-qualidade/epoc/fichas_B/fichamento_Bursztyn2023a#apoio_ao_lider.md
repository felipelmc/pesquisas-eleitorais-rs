---
citekey: Bursztyn2023a
ficha_id: Bursztyn2023a#apoio_ao_lider
n_fichas_do_texto: 2
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Bursztyn2023a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Bursztyn2023a-epoc
data_fichamento: 2026-09-23
ferramenta: epoc
paginas_pdf: 66
faixas_lidas: 1-20,21-40,41-60,61-66
---

## 00_Resultado
- **desenho_epoc** — resposta: grupo_controle — evidência: "estimate the following model on a balanced panel of" (p. 22)
- **resultado_avaliado** — resposta: Tabela 6, coluna 2: efeito da interação proximidade × apoio estimado ao lado atrás sobre a parcela municipal de votos do lado atrás — evidência: "vote share for the trailing side (column 2) as dependent" (p. 42)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: "predetermined pre-disposition to vote for the side trailing" (p. 42)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: "vote share, in percent of votes cast, in the preceding" (p. 42)
- **cg_linha_base_outcome** — resposta: proposta_baixo — evidência: "municipality fixed effects are captured by" (p. 22)
- **cg_caracteristicas_base** — resposta: proposta_incerto — evidência: "distribution of Trailing Side's Estimated Support accross 2176" (p. 52)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: "balanced panel of 2176 municipalities observed in all 57" (p. 42)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "are available in disaggregate form for all levels" (p. 9)
- **cg_contaminacao** — resposta: proposta_alto — evidência: "national-level poll (and its closeness) before each vote provides" (p. 8)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: "estimate equation 4, but now examining municipality vote share" (p. 22)
- **cg_outros_riscos** — resposta: proposta_alto — evidência: "vote shares in the preceding legislative election to minimize" (p. 22)

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
Desenho: a Tabela 6 é um painel município×voto (2.176 municípios, 57 votos com pesquisa, 1998–2019) com efeitos fixos de município e de canton×voto, relacionando o apoio pré-determinado ao lado atrás (medido antes do período de estudo, na eleição legislativa anterior) à proximidade da pesquisa. Não há sorteio nem grupo de controle não exposto: todos os municípios recebem a mesma pesquisa nacional simultaneamente, variando apenas no "apoio ao lado atrás" (covariável preexistente). Por isso foi classificado como `grupo_controle` (ensaio não randomizado com unidades agregadas), seguindo a orientação do protocolo de que DiD/heterogeneidade com unidades agregadas (município) cai nesse desenho EPOC, e não em `its` (não há série de múltiplos pontos temporais antes/depois neste modelo especificamente; a série temporal do desenho está no outro resultado, `mobilizacao`).

Por domínio:
- `cg_sequencia_aleatoria` e `cg_ocultacao_alocacao`: proposta_alto porque a variável de "apoio ao lado atrás" é uma característica histórica do município, não uma alocação sorteada nem controlada/oculta pelos autores — é observacional por definição.
- `cg_linha_base_outcome`: sobrepus o algoritmo padrão (que pede outcome medido na linha de base) porque o modelo inclui efeito fixo de município, o que absorve o nível basal de turnout de cada município; por isso proposta_baixo, e não incerto.
- `cg_caracteristicas_base`: proposta_incerto porque o texto mostra a distribuição da covariável de apoio (Figura C.5) mas não testa formalmente balanceamento entre grupos, já que o desenho é de heterogeneidade contínua, não de dois grupos discretos.
- `cg_contaminacao`: proposta_alto porque a pesquisa eleitoral é um sinal nacional divulgado simultaneamente a todos os municípios — não há como proteger um "grupo controle" de receber a mesma informação; a variação estudada é de intensidade de apoio prévio, não de exposição/não exposição.
- `cg_outros_riscos`: proposta_alto — mesmo com o cuidado de usar votos da eleição legislativa anterior para reduzir simultaneidade (nota de rodapé 37), o desenho continua sujeito a confundimento residual entre o apoio histórico ao lado atrás e outros fatores locais (ex.: intensidade de campanha) correlacionados com a proximidade da pesquisa.
- Proposta geral: como quatro domínios (sequência aleatória, ocultação de alocação, contaminação, outros riscos) foram propostos como alto, a proposta geral deste resultado é `proposta_alto` (agravado por vários domínios com problema).

Resultado localizado na Tabela 6, coluna 2, linha "Ex Ante Closeness (std.) × Trailing Side's Estimated Support" = 0.0634*** (0.0213), p. 42 do PDF.
SI (sem informação): nenhuma resposta usou código de "sem informação" — EPOC `grupo_controle`/`its` não tem código dedicado para isso; o mais próximo, `incerto`, foi usado uma vez (`cg_caracteristicas_base`) e conta como incerto, não como SI.
