---
citekey: Morton2015a
ficha_id: Morton2015a#apoio_ao_lider
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
- **desenho_epoc** — resposta: its — evidência: "equation (2) estimates a pre- and post-2005 slope" (p. 33)
- **resultado_avaliado** — resposta: Tabela 8, coluna Full Sample: diferença delta entre as inclinações pós e pré-2005 da equação (2), estimada por MQO só com os OST do oeste, delta = -5.22 (EP agrupado por departamento 2.04; OLS 2.91; bootstrap 1.23; block bootstrap 1.73), N = 60; delta negativo indica efeito de adesão ao favorito (bandwagon) antes da reforma — evidência: "is therefore negative (−5.22) and statistically" (p. 33); "Clustered by department" (p. 34)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = its)
- **cg_ocultacao_alocacao** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = its)
- **cg_linha_base_outcome** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = its)
- **cg_caracteristicas_base** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = its)
- **cg_dados_incompletos** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = its)
- **cg_conhecimento_alocacao** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = its)
- **cg_contaminacao** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = its)
- **cg_relato_seletivo** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = its)
- **cg_outros_riscos** — resposta: NA_secao — evidência: (fluxo: desenho_epoc = its)

## C_ITS
- **its_teste_t_sem_tendencia** — resposta: Sim — evidência: "This approach allows us to test for a bandwagon" (p. 33); "simple t-tests on δ" (p. 33)
- **its_intervencao_independente** — resposta: proposta_alto — evidência: "four potentially relevant events happened over the period studied" (p. 17)
- **its_forma_efeito_pre_especificada** — resposta: proposta_baixo — evidência: "equation (2) estimates a pre- and post-2005 slope" (p. 33)
- **its_coleta_nao_afetada** — resposta: proposta_baixo — evidência: "data were collected from the French ministry of Internal" (p. 18); "count their results and population in the 2012 elections jointly" (p. 19)
- **its_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "data were collected from the French ministry of Internal" (p. 18)
- **its_dados_incompletos** — resposta: proposta_baixo — evidência: "Pierre and Miquelon, Guadeloupe, French Guiana, and Martinique." (p. 19); "second election rounds from 1981 onwards" (p. 18)
- **its_relato_seletivo** — resposta: proposta_baixo — evidência: "Several standard error estimates are given for the t-test" (p. 34)
- **its_outros_riscos** — resposta: proposta_alto — evidência: "observe four elections at two time points after the law changed" (p. 28); "Visual inspection of the raw data suggests" (p. 33)

## Notas do codificador
Desenho: a análise de bandwagon (seção 6, equação 2, p. 32-33) regride a diferença de votos entre o primeiro e o segundo colocados nos 5 OST do oeste sobre a mesma diferença no continente (e OST do leste), com dummy pós-2005 e interação; os departamentos não tratados entram só no regressor, não como grupo controle. São 8 votações antes (1981-2002, 2 turnos) e 4 depois (2007 e 2012) nas mesmas unidades, sem grupo controle separado: classifiquei como its pelo critério do codebook (vários pontos antes e depois, sem grupo controle separado). Não é uma ITS clássica (o desfecho não é modelado como série no tempo; o que muda na reforma é a inclinação da relação com a margem continental). Se os avaliadores humanos preferirem grupo_controle, a seção C_Grupo_controle precisa ser preenchida. Por isso a seção de grupo controle recebe NA_secao.

Resultado: Tabela 8, coluna Full Sample (p. 34): pré-2005 1.18 (0.29), pós-2005 -4.04 (2.89), delta -5.22. O texto (p. 33) traz 1.17 e -4.05, discrepância pequena com a tabela. Excluindo as votações com margem continental acima de 20 pontos (N = 50), delta = -11.49 e a inclinação pré perde significância (7.45, EP 4.71).

Por critério:
- Teste t sem tendência: Sim. A equação (2) não tem termo de tempo; compara inclinações pré e pós com teste t sobre delta, sem justificativa sobre tendência secular (a única justificativa é que os regressores são predeterminados, p. 33). Ressalva: a comparação é de inclinações em relação à margem continental, não de níveis de uma série, o que reduz mas não elimina a preocupação com tendência (ex.: afastamento político gradual dos OST em relação ao continente). Pelo EPOC, Sim implica que o estudo não entra salvo reanálise; ponto para decisão humana.
- Intervenção independente: o texto lista quatro eventos concorrentes (p. 17-18), mas a análise de bandwagon não controla nenhum deles. Eventos concorrentes (descrição que o codebook pede após travessão; mantida aqui para não quebrar a leitura do valor): redução do mandato presidencial de 7 para 5 anos (2002); primeira candidatura de um OST, a Guiana (1º turno de 2002); Le Pen no 2º turno de 2002 (votação com margem de 64 pontos, que pesa na inclinação pré); crescimento da internet e das estimativas antecipadas após as 17h em 2007 e 2012; mudança do dia da votação para sábado, parte da própria reforma. Com só duas eleições pós-reforma, qualquer peculiaridade dos candidatos de 2007 e 2012 no oeste se confunde com a reforma. proposta_alto.
- Forma do efeito: o ponto de corte é a própria reforma (vigente a partir de 2005; primeira eleição sob a regra em 2007), com mudança de inclinação especificada a priori na equação (2). A exclusão de outliers veio da inspeção visual, mas afeta só a coluna de robustez, não a Full Sample. proposta_baixo.
- Coleta não afetada: mesma fonte de resultados oficiais em todo o período (p. 18-19); Saint-Martin e Saint-Barthélemy somados a Guadalupe em 2012 para manter a série. proposta_baixo.
- Conhecimento da intervenção: desfecho objetivo (contagem oficial de votos). proposta_baixo.
- Dados incompletos: 5 OST x 12 votações = 60 observações, o N da Tabela 8 (p. 34); série completa. proposta_baixo.
- Relato seletivo: inclinações pré e pós, delta, quatro tipos de EP e a versão sem outliers são relatados; os autores reconhecem que não conseguem separar troca de voto de efeito sobre comparecimento (p. 34-35). proposta_baixo.
- Outros riscos: (1) poucos pontos pós-intervenção (duas eleições, 4 votações), abaixo do mínimo usual de 3 pontos por período no EPOC para ITS; (2) inclinação pré dominada por votações de margem grande (a inclinação pré passa de 1.18 para 7.45 não significativa ao excluir 2 votações), e a definição de outliers veio da inspeção visual dos dados; (3) inferência com apenas 5 clusters, embora os autores digam (p. 23) que 9 clusters não bastam para EP agrupados; (4) dados agregados não permitem separar mecanismo (troca de voto ou comparecimento seletivo). proposta_alto.

Sem variável geral no codebook EPOC; pior critério proposto: alto (intervenção independente; outros riscos). Nenhuma pergunta com SI.
