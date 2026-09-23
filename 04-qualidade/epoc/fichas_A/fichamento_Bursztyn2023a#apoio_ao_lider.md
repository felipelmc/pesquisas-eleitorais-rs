---
citekey: Bursztyn2023a
ficha_id: Bursztyn2023a#apoio_ao_lider
n_fichas_do_texto: 2
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Bursztyn2023a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Bursztyn2023a-epoc
data_fichamento: 2026-09-23
ferramenta: epoc
paginas_pdf: 66
faixas_lidas: 1-20,21-40,41-60,61-66
---

## 00_Resultado
- **desenho_epoc** — resposta: grupo_controle — evidência: "estimate the following model on a balanced panel of 2,176 municipalities" (p. 22); "all of our analysis will consider estimated support for the trailing side" (p. 22)
- **resultado_avaliado** — resposta: Tabela 6, coluna 2: parcela municipal de votos do lado atrás na pesquisa, interação proximidade ex ante padronizada × apoio estimado ao lado atrás = 0.0634 (EP 0.0213); 2.176 municípios × 57 votações (124.032 observações), efeitos fixos de município e de cantão×votação — evidência: "Ex Ante Closeness (std.) × Trailing Side’s Estimated Support" (p. 42); "now examining municipality vote share for the trailing side" (p. 22)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: "we estimate support for the trailing side in the poll" (p. 21)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: "estimate the following model on a balanced panel of 2,176 municipalities" (p. 22)
- **cg_linha_base_outcome** — resposta: proposta_alto — evidência: "we do not observe municipality-level preferences regarding a referendum prior to" (p. 21)
- **cg_caracteristicas_base** — resposta: proposta_alto — evidência: "all of our analysis will consider estimated support for the trailing side" (p. 22)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: "balanced panel of 2,176 municipalities observed in all" (p. 22); "We are missing 26 out of 2,202 municipalities" (p. 12)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "These data are available in disaggregate form for all levels" (p. 9)
- **cg_contaminacao** — resposta: proposta_incerto — evidência: "naturally-occurring exposure to poll information that arrives to entire populations" (p. 6)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: "now examining municipality vote share for the trailing side" (p. 22)
- **cg_outros_riscos** — resposta: proposta_alto — evidência: "unobserved issue type may drive both closeness and turnout" (p. 12)

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
- Justificativa de `cg_outros_riscos` (movida do campo de resposta pelo coordenador): tipo de tema como confundidor: votações apertadas podem ser as mais alinhadas às linhas partidárias, o que torna o apoio partidário mais preditivo do voto sem efeito da pesquisa; sem placebo na era pré-pesquisas; apoio medido por proxy partidária da eleição legislativa anterior; inferência com dados agregados por município; 57 clusters
Adequação à ferramenta e ao construto. O resultado é uma regressão em painel município × votação (57 votações com pesquisa, 1998–2019) com efeitos fixos de município e de cantão×votação; a variação vem da interação entre a proximidade da pesquisa (nível da votação) e o apoio estimado ao lado atrás (nível do município, pela votação dos partidos na eleição legislativa anterior). Tratei como diferenças em diferenças com dose contínua em unidades agregadas (`grupo_controle`), mas o encaixe é fraco: não há período sem exposição nem medida do desfecho antes da divulgação da pesquisa, e todas as unidades recebem a mesma pesquisa. Os avaliadores humanos podem preferir levar este resultado para ROBINS-I (regressão sem variação identificada). O desfecho é a parcela de votos do lado que está atrás; o apoio ao líder é o complemento (100 menos essa parcela), então o sinal positivo da interação corresponde a menos apoio ao líder quando a pesquisa é mais apertada.

Sequência e ocultação. Alto por definição (não randomizado). Pela convenção EPOC da skill, não entram no julgamento geral.

Linha de base do desfecho. O desfecho (votos no lado atrás) não é observado antes da exposição, e não há teste de pré-tendência nem placebo na era sem pesquisas (antes de 1998) para esta especificação. O apoio estimado é predeterminado (eleição legislativa anterior), mas isso não mostra que o gradiente apoio → votos seria igual em votações mais e menos apertadas sem a pesquisa. Proposta alto; um humano pode ler como incerto.

Características de base. Municípios com mais e menos apoio ao lado atrás diferem por construção, e não há tabela de características por grupo. Os efeitos fixos de município e de cantão×votação absorvem diferenças de nível, mas não diferenças de gradiente por tipo de votação. O tamanho do município é controlado na análise da Tabela 5, não na Tabela 6. Proposta alto.

Dados incompletos. Painel balanceado de 2.176 municípios; faltam 26 de 2.202 por fusões complexas ou urna compartilhada (cerca de 1%, por motivos administrativos). A amostra aparada sem 0% e 100% de apoio (Tabela C.9, p. 66) dá 0.0631. Proposta baixo.

Conhecimento da alocação. Desfecho objetivo, resultados oficiais de votação do escritório federal de estatística. Proposta baixo.

Contaminação. Toda votação da amostra tem pesquisa nacional divulgada para toda a população; o contraste é de intensidade, e não entre expostos e não expostos. Não é possível dizer se as unidades de comparação estavam protegidas. Proposta incerto.

Relato seletivo. Os dois desfechos anunciados para esta análise (comparecimento e parcela de votos) aparecem na Tabela 6. Há uma inconsistência menor: o texto das contrafactuais (p. 23) cita "Table 6, columns 1 and 3", mas a tabela só tem duas colunas. Proposta baixo.

Outros riscos. O risco principal é o confundimento pelo tipo de tema: os próprios autores apontam que o tipo de tema move proximidade e comparecimento (p. 12). Aqui a ameaça é específica: votações em que a pesquisa é apertada podem ser justamente as que dividem o eleitorado pelas linhas partidárias, o que deixa o apoio partidário mais preditivo do voto municipal no lado atrás, sem que a pesquisa tenha efeito. Os efeitos fixos de cantão×votação não removem essa diferença de gradiente, e não há placebo com votações da era pré-pesquisa. Somam-se: medida do apoio por proxy partidária (erro de medida), inferência a partir de dados agregados por município e 57 clusters (sem wild bootstrap nesta tabela). Proposta alto.

Geral, só como insumo para os avaliadores humanos (o codebook não tem variável de julgamento geral): pela convenção EPOC da skill, linha de base alta leva a proposta_alto.

Nenhum item SI pede contato com autores. O resultado indicado pelo coordenador foi localizado (Tabela 6, coluna 2, p. 42).
