---
citekey: Morton2015a
ficha_id: Morton2015a#mobilizacao
n_fichas_do_texto: 2
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Morton2015a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Morton2015a-epoc
data_fichamento: 2026-09-23
ferramenta: epoc
paginas_pdf: 43
faixas_lidas: 1-20,21-40,41-43
---

## 00_Resultado
- **desenho_epoc** — resposta: grupo_controle — evidência: "only the eastern OST as a control group" (p. 20); "departments from the mainland as an additional control group" (p. 20)
- **resultado_avaliado** — resposta: Tabela 5, coluna (1): efeito do tratamento 0.11 (EP agrupado 0.02) sobre o comparecimento nas presidenciais, com tendência linear por departamento (105), dummies de OST e de turno, N = 1260; o sinal indica que votar sem conhecer a boca de urna aumenta o comparecimento em cerca de 11 pontos (conhecê-la reduz em cerca de 11 pontos) — evidência: "Separate time trends for each of the 105 departments are included." (p. 27)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: "we exploit a 2005 voting reform in France" (p. 5)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: "it was decided to change the voting day to Saturday" (p. 17)
- **cg_linha_base_outcome** — resposta: proposta_incerto — evidência: "turnout trends seem to be reasonably parallel before the legislative change" (p. 21); "46% in 2002 and 65% in 2007 for the western OSTs." (p. 23)
- **cg_caracteristicas_base** — resposta: proposta_alto — evidência: "it is not immediately clear what observable characteristics could" (p. 21); "majority of the population in the overseas territories" (p. 18)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: "all six elections and all 105 departments, which makes a total" (p. 23)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "data were collected from the French ministry of Internal" (p. 18)
- **cg_contaminacao** — resposta: proposta_incerto — evidência: "the spread of online election result information after 5:00PM had grown substantially" (p. 18)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: "knowing the outcome of early voting decreases turnout by about 12" (p. 36); "the results are not reported here" (p. 28)
- **cg_outros_riscos** — resposta: proposta_incerto — evidência: "allowed the western territories to switch their election day to Saturday" (p. 17); "nine clusters which is not enough to estimate clustered standard errors" (p. 23)

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
Desenho: diferenças em diferenças com unidades agregadas (105 departamentos, 6 eleições presidenciais 1981-2012, 2 turnos). Tratados: os 5 OST a oeste da França continental (Polinésia Francesa, Saint-Pierre-et-Miquelon, Guadalupe, Guiana, Martinica), que desde a reforma de 2005 votam no sábado, antes da divulgação da boca de urna continental; controles: OST do leste e departamentos continentais. Classificado como grupo_controle (antes-depois controlado), por isso a seção ITS recebe NA_secao.

Resultado: Tabela 5, coluna (1), p. 27 (0.11, EP 0.02, EP agrupados por departamento). O texto oscila entre 11 pontos (p. 26) e 12 pontos na especificação que chamam de preferida (p. 36) sem dizer qual coluna é a preferida.

Por critério:
- Sequência aleatória e ocultação da alocação: proposta_alto por regra do codebook (não randomizado / antes-depois controlado). A alocação vem de uma reforma legal que moveu a eleição dos OST do oeste para o sábado.
- Outcome na linha de base: o comparecimento foi medido em 4 eleições antes da reforma, mas os níveis diferem (em 2002, 46% nos OST do oeste contra 55% nos do leste, p. 23). O DiD remove a diferença de nível e o modelo da Tabela 5 inclui tendências por departamento; as tendências pré parecem paralelas só por inspeção visual (Figuras 2 e 3, p. 21-22), e o placebo com 1994 como ano falso não é mostrado (p. 28). A estimativa muda com a especificação de tendência (0.06 com tendência comum, Tabela 4, colunas 1-5, contra 0.11 a 0.18 com tendências específicas, Tabelas 4 e 5), o que sugere que as trajetórias pré não são idênticas. O codebook só admite baixo com diferença ajustada em ensaio randomizado; por isso proposta_incerto em vez de baixo.
- Características de base: nenhuma tabela de características dos grupos; os autores só argumentam que não é claro quais observáveis afetariam o comparecimento de forma diferente (nota 27, p. 20-21) e mencionam que a população dos OST é majoritariamente não branca (p. 18) e que os tamanhos variam muito (p. 19). Pelo codebook, não relatadas => proposta_alto.
- Dados incompletos: resultados eleitorais administrativos de todos os 105 departamentos em todas as 12 votações (N = 1260 = 105 x 12); Saint-Martin e Saint-Barthélemy foram somados a Guadalupe em 2012 para manter a série (p. 19). proposta_baixo.
- Conhecimento da alocação: desfecho objetivo (comparecimento oficial, Ministério do Interior e politiquemania.com, conferido por amostras com os números oficiais, p. 18-19). proposta_baixo.
- Contaminação: os OST do leste votam antes do continente e não recebem a boca de urna, mas os eleitores continentais (parte do grupo controle no modelo da Tabela 5) passaram a ter acesso a estimativas antecipadas via sites belgas e suíços a partir das 17h em 2007 e 2012 (p. 18), justamente no período pós-reforma. Isso pode reduzir o comparecimento do controle continental e inflar o DiD. A estimativa só com os OST do leste como controle (Tabela 3, 0.11) é parecida, o que atenua. proposta_incerto.
- Relato seletivo: os dois desfechos anunciados (comparecimento e voto no favorito) são relatados; várias checagens de robustez não são mostradas (placebo 1994, leste como falso tratado, dummy da Guiana 2002, QMLE fracionário; ver p. 28 e nota 32, p. 26). Não é omissão de desfecho, por isso proposta_baixo, mas os avaliadores humanos podem preferir incerto.
- Outros riscos (descrição do risco, que o codebook pede após travessão; mantida aqui para não quebrar a leitura do valor): (1) intervenção composta: a reforma mudou o dia da votação de domingo para sábado só no grupo tratado (p. 17), e o efeito do dia da semana não é separado do efeito da informação; o placebo com eleições legislativas (Tabela 7, p. 31; Tabela 13, p. 40) só ajuda se as legislativas dos OST também passaram ao sábado, o que o texto não diz; (2) apenas 5 unidades tratadas, com EP agrupados por departamento (105 clusters, poucos tratados); os próprios autores dizem que 9 clusters não bastam para EP agrupados (p. 23); (3) eventos simultâneos de 2002 (mandato de 5 anos, candidatura da Guiana, Le Pen no 2º turno) discutidos e testados (p. 17-18, 28-29, Tabelas 6 e 12); (4) nota 22 com a marca FIXME (p. 17), sinal de manuscrito aceito não revisado, sem efeito sobre a estimativa. proposta_incerto.

Sem variável geral no codebook EPOC; pior critério proposto: alto (sequência e ocultação por regra; características de base). Nenhuma pergunta com SI.
