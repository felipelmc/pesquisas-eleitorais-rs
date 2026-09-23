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
- **desenho_epoc** — resposta: its — evidência: "We use only the vote difference in the western OST" (p. 33); "test for a bandwagon effect using simple t-tests on" (p. 33)
- **resultado_avaliado** — resposta: Tabela 8, coluna "Full Sample" (diferença δ entre as inclinações pré e pós-2005 da equação (2), MQO, dependente Δtreated,st, EP agrupado por departamento); δ impresso -5.22 — evidência: "Estimating equation (2) with ∆treated,st as the dependent variable" (p. 34)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=its)
- **cg_ocultacao_alocacao** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=its)
- **cg_linha_base_outcome** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=its)
- **cg_caracteristicas_base** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=its)
- **cg_dados_incompletos** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=its)
- **cg_conhecimento_alocacao** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=its)
- **cg_contaminacao** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=its)
- **cg_relato_seletivo** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=its)
- **cg_outros_riscos** — resposta: NA_secao — evidência: (fluxo: desenho_epoc=its)

## C_ITS
- **its_teste_t_sem_tendencia** — resposta: Não — evidência: (derivado de: o modelo estima coeficientes de inclinação separados pré e pós-2005, não apenas médias comparadas por teste t — ver Notas)
- **its_intervencao_independente** — resposta: proposta_alto — evidência: (derivado de: "the growth of the Internet, making access to information easier" (p. 18); "the spread of online election result information after 5:00PM had grown" (p. 18) — ver Notas)
- **its_forma_efeito_pre_especificada** — resposta: proposta_baixo — evidência: (derivado de: "This reform became effective in 2005" (p. 17) — ver Notas)
- **its_coleta_nao_afetada** — resposta: proposta_baixo — evidência: (derivado de: "The data were collected from the French ministry of Internal Affairs" (p. 18) — ver Notas)
- **its_conhecimento_alocacao** — resposta: proposta_baixo — evidência: (derivado de: "The data were collected from the French ministry of Internal Affairs" (p. 18) — ver Notas)
- **its_dados_incompletos** — resposta: proposta_baixo — evidência: (derivado de: "comprises French presidential election results" (p. 18) — ver Notas)
- **its_relato_seletivo** — resposta: proposta_baixo — evidência: (derivado de: "such outlier observations are not a problem" (p. 34) — ver Notas)
- **its_outros_riscos** — resposta: proposta_alto — evidência: (derivado de: "−4.04∗" (p. 34); "(2.89)" (p. 34) — ver Notas)

## Notas do codificador

**Desenho (fixado pelo coordenador).** Para este resultado (apoio_ao_lider), o classificador `desenho_epoc` foi fixado como `its` pelo coordenador, e não decidido por mim: o resultado avaliado é a Tabela 8, coluna "Full Sample", a diferença δ entre as inclinações (pré e pós-2005) da equação (2), que regride a diferença de votos no OST tratado (Δs,t) sobre a diferença de votos no continente (Δmainland,t), separadamente antes e depois da reforma de 2005, usando as seis eleições presidenciais de 1981 a 2012, sem uma série de grupo controle separada como variável dependente: "We use only the vote difference in the western OST" (p. 33). Isso contrasta com a ficha `mobilizacao` do mesmo texto (mesmo experimento natural, equação (1)), em que o desenho foi classificado como `grupo_controle` (DiD com o OST oriental e/ou o continente como comparador), porque naquele caso a variável dependente é o comparecimento nos próprios departamentos de controle. Por isso, os dois resultados do mesmo artigo recebem classificadores diferentes dentro da ferramenta EPOC.

**C_Grupo_controle.** Todas as nove variáveis desta seção são `NA_secao` por fluxo, já que `desenho_epoc=its` fixado pelo coordenador.

**its_teste_t_sem_tendencia.** A equação (2) não é uma simples comparação de médias pré/pós por teste t ignorando a tendência: ela estima coeficientes de inclinação (slope) distintos para o período pré-2005 e pós-2005 (Tabela 8: "Pre-2005 slope estimate" 1.18***, "Post-2005 slope estimate" -4.04*) e testa a diferença δ entre essas inclinações. O texto usa a expressão "simple t-tests" para descrever o teste de significância sobre δ, mas esse teste é sobre a diferença entre parâmetros de um modelo de regressão que já incorpora a inclinação (trend) em cada período, não uma comparação bruta de níveis pré/pós sem modelar tendência. Por isso, resposta Não.

**its_intervencao_independente.** A Seção 3.3 do artigo lista explicitamente eventos concorrentes no período estudado (redução do mandato presidencial em 2002, primeiro candidato do OST na primeira volta de 2002, avanço de Le Pen ao segundo turno em 2002) e reconhece um quarto fator, mais relevante para este resultado específico (a correlação do voto do OST com o continente): o crescimento do acesso à internet ao longo da década, que permitiu o acesso informal a resultados vazados mesmo após a reforma de 2005, de forma crescente entre as eleições de 2007 e 2012: "the growth of the Internet, making access to information easier" (p. 18); "the spread of online election result information after 5:00PM had grown" (p. 18). Isso é uma ameaça de confundimento temporal específica ao resultado de bandwagon (equação 2), pois pode atenuar ou alterar de forma não uniforme a inclinação "pós-2005" entre as duas eleições pós-reforma (2007 e 2012). Os autores mencionam apenas que "allow for different time trends" nas estimações de turnout (equação 1); não há um teste de robustez equivalente reportado especificamente para a equação (2) que isole esse fator. Por isso, proposta_alto.

**its_forma_efeito_pre_especificada.** O ponto de quebra (2005) corresponde à data real da mudança legal, não a um ponto escolhido a partir dos dados: "This reform became effective in 2005" (p. 17). A Tabela 8 rotula diretamente "Pre-2005 slope estimate" e "Post-2005 slope estimate" usando essa mesma data. Por isso, proposta_baixo.

**its_coleta_nao_afetada / its_conhecimento_alocacao.** Os dados de resultado eleitoral (usados para construir Δmainland,t e Δs,t) vêm de registro administrativo oficial, coletado da mesma fonte antes e depois da reforma, sem mudança de método de registro nem de mensuração ligada à intervenção, e sem possibilidade de mascaramento subjetivo (é resultado eleitoral oficial, não uma medida subjetiva sujeita a viés do avaliador): "The data were collected from the French ministry of Internal Affairs" (p. 18). Por isso, proposta_baixo nas duas variáveis.

**its_dados_incompletos.** A base usada nesta estimação (Tabela 8, N = 60 na amostra completa) é construída a partir do conjunto completo de resultados eleitorais presidenciais oficiais desde 1981: "comprises French presidential election results" (p. 18). Não há relato de perdas ou de dados faltantes para os OSTs tratados nesse período. Por isso, proposta_baixo.

**its_relato_seletivo.** Os autores reportam tanto a especificação com amostra completa quanto a excluindo outliers na mesma Tabela 8, e discutem explicitamente que o resultado se mantém significativo na segunda especificação: "such outlier observations are not a problem" (p. 34). Não há indício de omissão seletiva de especificações ou de resultados discordantes para este desfecho. Por isso, proposta_baixo.

**its_outros_riscos.** O período pós-reforma cobre apenas duas eleições presidenciais (2007 e 2012, quatro observações de turno por OST tratado), contra quatro eleições pré-reforma (1981, 1988, 1995, 2002); a inclinação pós-2005 é estimada com erro-padrão relativamente grande em relação ao coeficiente ("−4.04∗" (p. 34); "(2.89)" (p. 34)), refletindo poucos pontos temporais pós-intervenção para ancorar essa inclinação. Combinado com a preocupação de tendência concorrente (acesso à internet crescendo desigualmente entre 2007 e 2012), isso é um risco adicional de instabilidade da estimativa pós-período. Por isso, proposta_alto.

**Sobre a frase da p. 33 ("Essentially, equation (2) estimates...").** Essa frase do manuscrito (rotulado "Author's Accepted Manuscript", ainda sem revisão editorial final) tem construção sintática confusa na leitura direta do PDF; por isso não a usei como evidência de nenhuma resposta, preferindo trechos vizinhos inequívocos ("We use only the vote difference in the western OST"; "test for a bandwagon effect using simple t-tests on").

**Resultados de {RESULTADOS} não encontrados:** nenhum; o resultado apoio_ao_lider (Tabela 8, coluna Full Sample) foi localizado como descrito no despacho. O resultado mobilizacao deste texto já foi fichado anteriormente (ficha separada, não tocada nesta rodada).
