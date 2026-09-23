---
citekey: Morton2015a
ficha_id: Morton2015a#apoio_ao_lider
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
- **resultado_avaliado** — resposta: Tabela 8, coluna Full Sample: diferença δ entre as inclinações pré e pós-2005 da equação (2) (voto do candidato à frente no mainland vs. voto no território tratado; MQO, EP agrupado por departamento); valor impresso −5.22 — evidência: "Full Sample" (p. 34)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: (derivado de: desenho antes-depois controlado com unidades agregadas, exposição fixada por reforma legal, sem componente de sorteio — ver Notas)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: (derivado de: antes-depois controlado, alocação por localização geográfica fixada por lei, sem ocultação — ver Notas)
- **cg_linha_base_outcome** — resposta: proposta_incerto — evidência: (derivado de: ausência de checagem de equivalência pré-2005 específica para a correlação de voto bandwagon da equação (2) — ver Notas)
- **cg_caracteristicas_base** — resposta: proposta_alto — evidência: (derivado de: tamanhos populacionais muito heterogêneos entre os departamentos tratados e de controle, sem comparação formal de características — ver Notas)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: (derivado de: dados eleitorais oficiais completos, sem relato de perdas — ver Notas)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: (derivado de: desfecho objetivo, registro administrativo oficial de resultado eleitoral — ver Notas)
- **cg_contaminacao** — resposta: proposta_baixo — evidência: (derivado de: separação geográfica e legal entre o grupo exposto e o grupo sem acesso à informação do mainland — ver Notas)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: (derivado de: a Tabela 8 relata integralmente os coeficientes pré/pós, a diferença δ e várias estimativas de erro-padrão, com e sem outliers — ver Notas)
- **cg_outros_riscos** — resposta: proposta_incerto — evidência: (derivado de: os autores não distinguem entre dois mecanismos concorrentes de bandwagon para este resultado — ver Notas)

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

**Desenho.** O estudo explora uma reforma eleitoral francesa de 2005 (mudança do dia de votação nos territórios ultramarinos a oeste do mainland) como experimento natural, comparando departamentos "tratados" (Polinésia Francesa, Saint-Pierre-et-Miquelon, Guadalupe, Guiana Francesa, Martinica) contra um grupo de controle (mainland e/ou OST orientais), antes e depois de 2005: "This reform allows us to use a difference-in-difference strategy" (p. 5). Não há randomização; a exposição decorre da localização geográfica do departamento e da data em que a lei entrou em vigor.

**cg_sequencia_aleatoria / cg_ocultacao_alocacao.** Pela regra do codebook, desenhos antes-depois controlados são sempre proposta_alto nesses dois domínios: a alocação ao grupo tratado é dada pela geografia (território a oeste do mainland) e pela data da reforma, sem qualquer componente de sorteio ou ocultação de alocação.

**cg_linha_base_outcome.** O artigo mostra tendências de turnout pré-2005 aproximadamente paralelas entre os territórios (Figuras 2 e 3), mas essa checagem é feita para o desfecho de comparecimento (mobilizacao), não para a correlação de voto bandwagon avaliada nesta ficha (equação 2). Para este resultado específico, a "inclinação pré-2005" (1.18, IC a partir do erro-padrão 0.29) é o próprio parâmetro estimado, não uma checagem de equivalência de linha de base entre grupo tratado e controle; não há um teste de equivalência de níveis prévios da correlação de voto entre grupos. Por isso, incerto.

**cg_caracteristicas_base.** As unidades (departamentos/OST) têm tamanhos populacionais muito distintos: "population sizes still vary from around 4,000" (p. 19, referindo-se a Saint-Pierre-et-Miquelon versus cerca de 1,8 milhão no departamento do Nord). O artigo não apresenta uma tabela de características sociodemográficas comparando os grupos tratado e controle; a única resposta a essa heterogeneidade é ponderar pelo número de eleitores registrados, não demonstrar equivalência de covariáveis. Por isso, alto.

**cg_dados_incompletos.** A base é de resultados eleitorais oficiais completos: "comprises French presidential election results" (p. 18), sem relato de perdas de dados ou não resposta (dado administrativo, não survey). Por isso, baixo.

**cg_conhecimento_alocacao.** O desfecho (diferença de votos entre o candidato líder e o vice) vem de contagens oficiais de votos, fonte objetiva e não sujeita a viés de aferição subjetiva: "collected from the French ministry of Internal Affairs" (p. 18). Por isso, baixo.

**cg_contaminacao.** A alocação é por território/departamento inteiro, e a própria reforma de 2005 foi desenhada para eliminar o acesso à informação do mainland pelos territórios do oeste: "do not have any knowledge of the choices on the mainland" (p. 5, referindo-se à situação pós-reforma dos territórios do oeste). É pouco provável contaminação cruzada entre grupo tratado e grupo de controle dentro de uma mesma eleição, dado o desenho legal e geográfico. Por isso, baixo.

**cg_relato_seletivo.** A Tabela 8 relata as inclinações pré-2005 e pós-2005, a diferença δ e quatro estimativas de erro-padrão (OLS, clusterizado, bootstrap, block-bootstrap), tanto para a amostra completa quanto excluindo outliers: "Our estimates are summarized in Table 8" (p. 33). Não há indício de omissão de especificações descritas na equação (2). Por isso, baixo.

**cg_outros_riscos.** Os próprios autores reconhecem que o resultado (δ = −5.22) pode refletir troca de voto (vote-switching) OU um efeito de comparecimento diferencial por tipo de eleitor (turnout effect), sem que o desenho permita distinguir os dois mecanismos: "does not allow us to distinguish between the two possible explanations" (p. 35). Isso é um risco de interpretação causal específico deste resultado (o bandwagon medido pode ser confundido por composição de quem comparece), não coberto pelos domínios anteriores. Por isso, incerto.

**Resultados de {RESULTADOS} não encontrados:** nenhum; o resultado apoio_ao_lider (Tabela 8, coluna Full Sample) foi localizado como descrito no despacho.
