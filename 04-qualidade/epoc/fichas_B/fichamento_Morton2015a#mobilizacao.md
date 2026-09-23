---
citekey: Morton2015a
ficha_id: Morton2015a#mobilizacao
n_fichas_do_texto: 2
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Morton2015a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Morton2015a-epoc
data_fichamento: 2026-09-23
ferramenta: epoc
paginas_pdf: 43
faixas_lidas: 1-20,21-40,41-43
---

## 00_Resultado
- **desenho_epoc** — resposta: grupo_controle — evidência: "allows us to use a difference-in-difference strategy" (p. 5)
- **resultado_avaliado** — resposta: Tabela 5, coluna (1): efeito do tratamento sobre o comparecimento (turnout), com tendência linear específica por departamento (105), dummies de OST e de turno, EP agrupado; coeficiente impresso 0.11 — evidência: "Separate time trends for each of the 105 departments are included" (p. 27)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: (derivado de: desenho antes-depois controlado com unidades agregadas, exposição fixada por reforma legal, sem componente de sorteio — ver Notas)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: (derivado de: antes-depois controlado, alocação por localização geográfica fixada por lei, sem ocultação — ver Notas)
- **cg_linha_base_outcome** — resposta: proposta_baixo — evidência: (derivado de: tendências de comparecimento pré-2005 relatadas como aproximadamente paralelas entre os territórios — ver Notas)
- **cg_caracteristicas_base** — resposta: proposta_alto — evidência: (derivado de: tamanhos populacionais muito heterogêneos entre os departamentos tratados e de controle, sem comparação formal de características — ver Notas)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: (derivado de: dados eleitorais oficiais completos, sem relato de perdas — ver Notas)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: (derivado de: desfecho objetivo, registro administrativo oficial de comparecimento — ver Notas)
- **cg_contaminacao** — resposta: proposta_baixo — evidência: (derivado de: separação geográfica e legal entre o grupo exposto e o grupo sem acesso à informação do mainland — ver Notas)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: (derivado de: o efeito estimado é relatado de forma consistente em várias especificações e tabelas — ver Notas)
- **cg_outros_riscos** — resposta: proposta_baixo — evidência: (derivado de: choques concorrentes testados e descartados por placebos e pela eleição parlamentar — ver Notas)

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

**Desenho.** Mesmo experimento natural da ficha apoio_ao_lider (reforma de 2005 nos territórios ultramarinos franceses), agora com o comparecimento eleitoral (turnout) por departamento/ano como desfecho: "This reform allows us to use a difference-in-difference strategy" (p. 5). Sem randomização; alocação por geografia e data da reforma.

**cg_sequencia_aleatoria / cg_ocultacao_alocacao.** Pela regra do codebook, antes-depois controlado é sempre proposta_alto nesses dois domínios: alocação por território, sem sorteio nem ocultação.

**cg_linha_base_outcome.** O artigo relata explicitamente que as tendências de turnout antes da reforma são comparáveis entre os três grupos de território: "turnout trends seem to be reasonably parallel before" (p. 21, referindo-se ao período anterior à mudança legislativa nas Figuras 2 e 3). Isso corresponde à checagem de equivalência da linha de base do próprio desfecho avaliado nesta ficha. Por isso, baixo.

**cg_caracteristicas_base.** As unidades variam enormemente em população: "population sizes still vary from around 4,000" (p. 19, contra cerca de 1,8 milhão no Nord). Não há tabela de covariáveis comparando grupo tratado e controle além da ponderação pelo eleitorado registrado. Por isso, alto.

**cg_dados_incompletos.** Dados de comparecimento vêm de registros eleitorais oficiais completos, N = 1260 (105 departamentos × eleições × turnos): "comprises French presidential election results" (p. 18). Sem relato de perdas. Por isso, baixo.

**cg_conhecimento_alocacao.** O comparecimento é medido por registro administrativo objetivo (não survey, não sujeito a mascaramento subjetivo): "collected from the French ministry of Internal Affairs" (p. 18). Por isso, baixo.

**cg_contaminacao.** A reforma de 2005 foi desenhada justamente para impedir que os territórios do oeste tivessem acesso à informação do mainland antes de votar: "do not have any knowledge of the choices on the mainland" (p. 5). Contaminação cruzada entre grupo tratado e controle é pouco provável dado o desenho legal/geográfico. Por isso, baixo.

**cg_relato_seletivo.** O efeito de tratamento sobre o turnout (por volta de 0.06 a 0.18, dependendo da especificação) é relatado de forma consistente nas Tabelas 3, 4, 5, 9, 10, 11 e 12, sempre estatisticamente significativo e na mesma direção: "In sum, in all specifications, the point estimate remains stable" (p. 26). Por isso, baixo.

**cg_outros_riscos.** Os autores testam explicitamente choques concorrentes que poderiam confundir o efeito sobre o turnout — placebo com 1994 como ano de reforma fictício e placebo usando a OST oriental como "tratamento" falso: "do not find any significant coefficient estimate in either case" (p. 28) — e também replicam a análise com eleições parlamentares (mesmo território, mas resultado nacional não determinado pelo voto local), não encontrando efeito significativo (Tabela 7, Figura 4), o que reforça que choques simultâneos não explicam o efeito de turnout estimado. Por isso, baixo.

**Resultados de {RESULTADOS} não encontrados:** nenhum; o resultado mobilizacao (Tabela 5, coluna 1) foi localizado como descrito no despacho.
