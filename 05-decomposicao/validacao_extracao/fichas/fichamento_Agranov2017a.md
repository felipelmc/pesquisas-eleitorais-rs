---
citekey: Agranov2017a
ficha_id: Agranov2017a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Agranov2017a.pdf
paginacao: impressa
offset_pagina: 3
agente_fichador: rec-B-Agranov2017a (claude-sonnet-5)
data_fichamento: 2026-09-23
---

## 01_Formal
- **titulo** — resposta: What makes voters turn out: The effects of polls and beliefs — evidência: "What makes voters turn out: The effects of polls and beliefs" (p. 1)
- **ano** — resposta: 2016 — evidência: "September 2016" (p. -1)
- **tipo_publicacao** — resposta: preprint (working paper/discussion paper da série WZB, sem revisão por pares até esta versão) — evidência: "Discussion Paper" (p. -1)
- **idioma** — resposta: en — evidência: "Keywords: Collective Choice, Polls, Strategic Voting." (p. 1)
- **pais_estudo** — resposta: Estados Unidos — Califórnia, Los Angeles (local do experimento; não a afiliação institucional dos autores) — evidência: "California Social Sciences Experimental Laboratory (CASSEL) at UCLA" (p. 10)

## 02_Metodologica
- **tipo_estudo** — resposta: b2 — evidência: "the experiments employ a 3 × 2 design based on" (p. 10)
- **problema_pesquisa** — resposta: Testar se eleitores respondem a probabilidades de serem decisivos (pivotal) e como crenças eliciadas sobre o resultado, formadas via pesquisas de intenção de voto, afetam a decisão de participar. — evidência: "We use laboratory experiments to test for one of" (p. 1)
- **unidade_analise** — resposta: individuo — evidência: "each decides whether to abstain, vote red, or vote blue" (p. 10)
- **populacao** — resposta: Sujeitos de laboratório (pool de participantes do CASSEL/UCLA), organizados em grupos de 9 por sessão. — evidência: "Overall, 198 subjects participated." (p. 10)
- **periodo_dados** — resposta: 999 — evidência: 999
- **fonte_dados** — resposta: primarios — evidência: "We use laboratory experiments to test for one of" (p. 1)

## 03_Intervencao_outcome
- **intervencao_descricao** — resposta: Informação sobre a distribuição de preferências do grupo (o "jarro"/estado) fornecida antes da decisão de votar em cada período: no tratamento No Polls, nenhuma informação além do próprio sorteio; no Perfect Polls, revelação do jarro realizado (informação perfeita); no Lab Polls, pesquisa de intenção de voto entre os 9 sujeitos do grupo, com o resultado agregado (nº de abstenções, votos red, votos blue) divulgado antes do voto real. Meio: tela do experimento; momento: imediatamente antes de cada decisão de voto. — evidência: "subjects participated in a poll reporting their voting intentions" (p. 3)
- **familia_intervencao** — resposta: pesquisa_pre_eleitoral — evidência: "subjects are asked to declare their intended actions" (p. 9)
- **comparador** — resposta: Tratamento No Polls (sem qualquer informação sobre a distribuição de preferências) como linha de base; Perfect Polls (informação perfeita) como comparador do extremo oposto ao Lab Polls (pesquisa ruidosa e não vinculante). — evidência: "subjects were provided with no further information" (p. 3)
- **construto_outcome** — resposta: mobilizacao — evidência: "voting propensity increases systematically with subjects' predictions of their" (p. 1)
- **outcome_medida** — resposta: Decisão binária de votar (red ou blue, sempre pela alternativa preferida do próprio sujeito) versus abster-se em cada período (comparecimento individual), com recompensa de $2 condicionada à vitória da alternativa preferida e custo de participação de 25 ou 50 centavos. — evidência: "each decides whether to abstain, vote red, or vote blue" (p. 10)

## 05_Mecanismo_moderador_percepcao_custo
- **mecanismo_id** — resposta: Sim — justificativa: os autores propõem e estimam formalmente um mecanismo de "desejo de votar com o vencedor" que explicaria a maior propensão a votar quando a vantagem esperada é grande. — evidência: "voters receive a benefit from voting for the winner" (p. 3)
- **mecanismo_tipo_evidencia** — resposta: teste_de_canal — evidência: "we estimate the parameter a that maximizes the likelihood" (p. 28)
- **mecanismo_descricao** — resposta: Recurso: benefício adicional 'a' por votar com o vencedor da eleição (além do benefício V/2 de ser decisivo); Raciocínio: sujeitos com utilidade u_i = V/2·Prob[alternativa preferida vence] + a·Prob[votar com o vencedor] − c votam mais quando esperam grande vantagem, pois o segundo termo cresce com a probabilidade de estar do lado vencedor; Contexto: estimado por sujeito, ajustando 'a' às 20 decisões de cada um, comparado entre os três tratamentos informacionais. — evidência: "voters receive a benefit from voting for the winner" (p. 3)
- **moderador_id** — resposta: Sim — justificativa: o efeito da informação (polls) sobre a propensão a votar difere conforme o sujeito pertence à maioria ou à minoria esperada do grupo. — evidência: "the availability of information reduces the probability of minority participation" (p. 18)
- **moderador_descricao** — resposta: Pertencimento a maioria/minoria (conforme a distribuição de preferências revelada ou percebida) modera o efeito da informação: com Perfect Polls e Lab Polls, a probabilidade de participação da maioria aumenta e a da minoria diminui, em comparação com o tratamento No Polls. — evidência: "the availability of information reduces the probability of minority participation" (p. 18)
- **het_metodo** — resposta: estratificacao_e_interacao — evidência: "Lead of the majority if in majority (belief)" (p. 24)
- **het_pre_especificada** — resposta: nao_declarado — evidência: 999
- **equidade_progress_plus** — resposta: 999 — evidência: 999
- **efeitos_nao_intencionais** — resposta: Desmobilização do grupo minoritário associada à disponibilidade de informação sobre a distribuição de preferências (redução da participação da minoria quando há Perfect Polls ou Lab Polls, em contraste com a previsão teórica de maior participação da minoria informada). — evidência: "the availability of information reduces the probability of minority participation" (p. 18)
- **limitacoes_autores** — resposta: Os próprios autores reconhecem que o desenho não permite separar o desejo de votar com o vencedor do desejo de votar com a maioria. — evidência: "the current design is not tailored for" (p. 36)

## 13_Bloco_b2_quantitativo_explicativo
- **b2_estrategia_identificacao** — resposta: experimento_aleatorizado_cluster (unidade de atribuição = sessão/grupo de 9 sujeitos, cada sessão implementando um único tratamento informacional) — evidência: "Each experimental session implemented one of the information treatments" (p. 10)
- **b2_hipoteses_testes** — resposta: 999 — evidência: 999
- **b2_estimador** — resposta: logit_probit — evidência: "we run a Probit regression predicting the dependence of participation" (p. 23)
- **b2_estimando** — resposta: ATE — evidência: "Each experimental session implemented one of the information treatments" (p. 10)
- **b2_nivel_atribuicao_cluster** — resposta: Atribuição do tratamento informacional ao nível da sessão/grupo (9 sujeitos por grupo); os erros-padrão da regressão Probit (Tabela 4) foram agrupados por indivíduo (não por grupo/sessão); tamanho médio do cluster de tratamento = 9; ICC não reportado. — evidência: "clustering standard errors by individuals" (p. 23)
- **b2_n_total** — resposta: No Polls: 879 observações; Perfect Polls: 1174 observações; Lab Polls: 1024 observações (198 sujeitos no total do experimento). — evidência: "# of obs. 879 1174 1024" (p. 24)
- **b2_controles** — resposta: Dummies de grupo (Group 2 a Group 8) ; Period ; High Cost of Voting ; Cumulative profit at t-1 ; Profit at t-1 ; Voted at t-1 ; Voted and won at t-1 ; Abstained and won at t-1 ; Composition lead of the preferred alternative (belief) ; Lead of the majority if in majority (belief) ; Lead of the majority if in minority (belief) ; Lead of the preferred candidate (poll, apenas Lab Polls) — evidência: "High Cost of Voting" (p. 24)
- **b2_dp_y_tipo** — resposta: nao_reportado — evidência: 999
- **b2_teste_falsificacao** — resposta: Não — justificativa: não há menção a placebo, pré-tendência, outcome falso ou corte falso no texto lido; há apenas testes de ausência de efeitos de grupo/tempo na regressão (não configuram teste de falsificação no sentido do codebook). — evidência: 999
- **b2_modelo_principal** — resposta: mobilizacao: Tabela 4, regressões Probit por tratamento (colunas No Polls, Perfect Polls, Lab Polls) — evidência: "we run a Probit regression predicting the dependence of participation" (p. 23)
- **b2_criterio_modelo_principal** — resposta: regra_do_protocolo — evidência: "we run a Probit regression predicting the dependence of participation" (p. 23)
- **b2_direcao_estimativa_principal** — resposta: mobilizacao: zero — evidência: "Participation costs are not significantly different across treatments" (p. 31)
- **b2_significancia_05** — resposta: mobilizacao: nao — evidência: "Participation costs are not significantly different across treatments" (p. 31)
- **b2_interpretacao_autores** — resposta: As pesquisas pré-eleitorais não geram os efeitos negativos de bem-estar previstos pela teoria; ao contrário, aumentam a participação da maioria esperada e geram mais eleições com grande margem. — evidência: "pre-election polls do not exhibit the detrimental effects on welfare" (p. 35)

## 06_Especificas_pesquisas
- **regiao** — resposta: outro — evidência: "California Social Sciences Experimental Laboratory (CASSEL) at UCLA" (p. 10)
- **tipo_eleicao** — resposta: simulada_abstrata — evidência: "Subjects had to choose one of two colors: Red or" (p. 3)
- **sistema_eleitoral** — resposta: regra_do_experimento — evidência: "using majority rule" (p. 3)
- **voto_obrigatorio** — resposta: 999 — evidência: 999
- **desenho_fino** — resposta: lab_preferencias_induzidas — evidência: "receives $2 for that period" (p. 10)
- **realismo_contexto** — resposta: induzido — evidência: "represented the subject's preferred alternative" (p. 3)
- **ano_eleicao** — resposta: 999 — evidência: 999
- **comparador_tipo** — resposta: sem_pesquisa — evidência: "subjects were provided with no further information" (p. 3)
- **nivel_desfecho** — resposta: escolha_incentivada_experimento — evidência: "receives $2 for that period" (p. 10)
- **margem_mostrada** — resposta: 999 — evidência: 999
- **mecanismo_testado** — resposta: conformidade — evidência: "voters receive a benefit from voting for the winner" (p. 3)
- **moderadores_relatados** — resposta: competitividade + preferencia_previa — evidência: "the availability of information reduces the probability of minority participation" (p. 18); "voting propensities are significantly lower when the preferred candidate" (p. 20)
- **alvo_efeito** — resposta: azarao + lider — evidência: "the availability of information reduces the probability of minority participation" (p. 18)
- **n_competidores** — resposta: 2 — evidência: "one of two colors: Red or Blue" (p. 3)
- **dias_ate_eleicao** — resposta: 999 — evidência: 999
- **ajuste_mediador** — resposta: Sim — evidência: "Lead of the majority if in majority (belief)" (p. 24)

## Notas do codificador

1. **Offset de página.** Confirmado abrindo páginas distantes: PDF 5 → impresso "2" (offset 3); PDF 13 → impresso "10" (offset 3); PDF 21 → impresso "18" (offset 3); PDF 34 → impresso "31" (offset 3); PDF 39 → impresso "36" (offset 3). Offset estável = 3 em todo o documento. As quatro primeiras folhas (capa EconStor, capa WZB, ficha de crédito, resumo) não têm número impresso; usei a fórmula (página impressa = índice do PDF − 3), o que dá páginas -2, -1, 0 e 1 respectivamente — a página do Abstract corresponde a "1", consistente com a Introdução começar em "2".

2. **tipo_estudo = b2.** Desenho experimental de laboratório com três tratamentos informacionais (No Polls / Perfect Polls / Lab Polls) manipulados entre sessões, análise por comparação de propensões de voto entre tratamentos e por regressão Probit individual (Tabela 4, Seção 4.3). Não é revisão, meta-análise ou ensaio sem dados próprios.

3. **pais_estudo** inferido do local de realização do experimento (CASSEL/UCLA, Califórnia, EUA) — não é a afiliação institucional dos autores (Caltech, Purdue, Sydney/Cologne), que o codebook pede para não usar. Não há eleição real nem afirmação explícita da nacionalidade dos sujeitos, apenas o local do laboratório.

4. **999 por ausência de eleição real.** periodo_dados, voto_obrigatorio, ano_eleicao, dias_ate_eleicao e margem_mostrada foram marcados 999 porque o desenho é um jogo de laboratório com jarros vermelho/azul, sem eleição real associada e sem data de coleta declarada no texto lido.

5. **b2_estrategia_identificacao.** Classifiquei como experimento_aleatorizado_cluster (unidade = sessão/grupo de 9 sujeitos), mas registro a ressalva: o texto usa "randomizados" apenas para a formação dos grupos dentro da sessão e para o sorteio do jarro/estado a cada período; não encontrei uma frase explícita afirmando que a alocação de cada sessão a um tratamento informacional foi sorteada. Fica sinalizado para eventual arbitragem, caso o primeiro codificador tenha preferido "outro — especifique" por falta dessa afirmação literal.

6. **construto_outcome = mobilizacao apenas.** A cor preferida de cada sujeito é fixada pelo próprio sorteio (badge) no início do período e não é alterada pela informação recebida; a informação afeta apenas a decisão de votar/abster-se, não qual alternativa apoiar. Por isso não registrei apoio_ao_lider como outcome analisado nesta ficha (não há troca de escolha entre alternativas).

7. **b2_direcao_estimativa_principal / b2_significancia_05 = zero / não, para mobilizacao.** Baseei-me na comparação agregada de custos de participação e bem-estar entre tratamentos (p. 31: "Participation costs are not significantly different across treatments"). Há, porém, forte heterogeneidade em sentidos opostos entre maioria (a informação aumenta a participação) e minoria (a informação reduz a participação) — Tabela 3, p. 18. Sinalizo para arbitragem: um segundo julgamento pode preferir registrar a direção por subgrupo (maioria: benéfica; minoria: danosa) em vez do efeito líquido agregado que usei aqui.

8. **mecanismo_tipo_evidencia = teste_de_canal**, não hipotese_dos_autores, porque os autores não apenas propõem o mecanismo (desejo de votar com o vencedor) mas estimam formalmente um parâmetro estrutural por sujeito e comparam sua distribuição entre tratamentos (Figura 3, Seção 4.4), o que caracteriza um teste quantitativo do canal.

9. **moderadores_relatados** mapeado para "competitividade + preferencia_previa": a lista fixa do codebook não tem categoria literal para "pertencimento a grupo majoritário/minoritário", que é o moderador central do artigo; usei preferencia_previa como aproximação, e competitividade para a resposta à proximidade/landslide da eleição (Figura 1, Seção 4.2).

10. **alvo_efeito = azarao + lider**, pois o artigo mede separadamente o comparecimento de apoiadores da alternativa majoritária (líder) e da minoritária (azarão) — Tabela 3.

11. **ajuste_mediador = Sim**: o modelo principal (Tabela 4) inclui como regressores as crenças sobre a distância/vitória esperada ("Composition lead...", "Lead of the majority if in majority/minority (belief)"), que funcionam como controle da expectativa de vitória/viabilidade percebida, tal como descrito na definição do codebook.

12. Nenhuma outra ficha/planilha/CSV/nota do projeto foi aberta durante esta codificação, apenas o PDF e este arquivo de instruções.
