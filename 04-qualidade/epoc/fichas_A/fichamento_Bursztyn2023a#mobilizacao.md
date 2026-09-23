---
citekey: Bursztyn2023a
ficha_id: Bursztyn2023a#mobilizacao
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
- **desenho_epoc** — resposta: its — evidência: "This is a simple event study, examining voter turnout by" (p. 13); "Using unique data from the canton of Geneva that allow us to" (p. 13)
- **resultado_avaliado** — resposta: mobilizacao: Tabela 3, coluna 1, comparecimento líquido diário (Net Turnout, %) em Genebra, coeficiente do dia +1 após a divulgação × proximidade ex ante padronizada = 0.3905** (EP 0.1737; p do wild cluster bootstrap 0.045); 52 votações, 766 observações voto×dia, efeitos fixos de votação e de dia em relação à pesquisa — evidência: "1 day after poll × Ex Ante Closeness (std.)" (p. 39); "0.3905**" (p. 39)

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
- **its_teste_t_sem_tendencia** — resposta: Não — evidência: "The table presents OLS estimates with two measures of daily turnout" (p. 39); "This is a simple event study, examining voter turnout by" (p. 13)
- **its_intervencao_independente** — resposta: proposta_baixo — evidência: "But, this response appears only three days" (p. 4); "Nor can the political supply side account for the response of voter" (p. 15); "Prior to the day when polls are released, we see no difference" (p. 14)
- **its_forma_efeito_pre_especificada** — resposta: proposta_baixo — evidência: "with the day of poll release" (p. 14); "how polls released on day t can produce an increase" (p. 14)
- **its_coleta_nao_afetada** — resposta: proposta_baixo — evidência: "of incoming ballots from early voters at a daily level." (p. 9); "Incoming postal ballots (around 90% of the" (p. 9)
- **its_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "administrative records on the timing of voter turnout" (p. 8)
- **its_dados_incompletos** — resposta: proposta_baixo — evidência: "as some votes do not have voting data for earlier days." (p. 15); "that our results are not sensitive to this choice of sample window." (p. 15)
- **its_relato_seletivo** — resposta: proposta_baixo — evidência: "We consider cumulative turnout rate as of" (p. 9); "Panel A: Cumulative Turnout" (p. 30); "Panel B: Turnout / All Voters" (p. 32)
- **its_outros_riscos** — resposta: proposta_baixo — evidência: "Day to Vote Fixed Effects" (p. 39); "from 5 voting days before to the last voting day after" (p. 39); "prior to poll release is the omitted category of reference." (p. 31)

## Notas do codificador
- Justificativa de `its_intervencao_independente` (movida do campo de resposta pelo coordenador): eventos concorrentes: resposta dos anúncios políticos nos jornais de Genebra, que só aumentam a partir do dia +3 (depois do dia +1 avaliado); cobertura da pesquisa pela mídia, que é o próprio canal da intervenção; tipo de questão, absorvido pelos efeitos fixos de votação e sem diferenças antes da divulgação
- Justificativa de `its_forma_efeito_pre_especificada` (movida do campo de resposta pelo coordenador): o ponto de análise é o dia da divulgação da pesquisa, e a defasagem de um dia é justificada pelo registro postal
- Justificativa de `its_outros_riscos` (movida do campo de resposta pelo coordenador): sazonalidade por dia da semana controlada só na coluna 2 (efeitos fixos de dia até a eleição), com resultado semelhante ao da coluna 1; antecipação testada pelos coeficientes prévios (teste conjunto p = 0.973); só 5 dias úteis de votação antes da divulgação e painel desbalanceado; inconsistência no dia de referência omitido entre o texto e a nota da Figura 3
Classificador fixado pelo coordenador: desenho_epoc = its (estudo de eventos do comparecimento diário em Genebra em torno do dia da divulgação da pesquisa, sem grupo controle separado; a "dose" é a proximidade ex ante da pesquisa, interagida com indicadores de dia em relação à divulgação, com efeitos fixos de votação e de dia). As nove variáveis de grupo controle ficaram NA_secao pelo fluxo.

Resultado localizado: Tabela 3, coluna 1 (p. 39 do PDF), linha "1 day after poll × Ex Ante Closeness (std.)", coeficiente 0.3905**, EP 0.1737, p bootstrap [0.045]. Nesta ficha só se avalia o resultado mobilizacao; a ficha de apoio_ao_lider do mesmo texto não foi tocada.

its_teste_t_sem_tendencia: Não. A análise é uma regressão de estudo de eventos com efeitos fixos de votação e de dia em relação à pesquisa, 14 coeficientes pós e 5 prévios, erros agrupados por votação e wild cluster bootstrap (p. 13-14, 39); não é uma comparação pré-pós por teste t.

its_intervencao_independente (proposta_baixo): a ameaça principal seria o "lado da oferta" (campanhas) reagir à pesquisa ou antecipá-la. Os autores testam isso com anúncios diários nos dois jornais de Genebra (Figura 5, p. 33): nenhuma diferença antes da divulgação e aumento só no dia +3, depois do dia +1 avaliado aqui (p. 4, 15). Os coeficientes prévios de comparecimento são pequenos e não significativos (teste conjunto p = 0.973, p. 39). Resta a possibilidade de outros choques do mesmo dia correlacionados com a proximidade (cobertura de mídia além dos anúncios), mas a cobertura é o próprio canal da exposição do protocolo.

its_forma_efeito_pre_especificada (proposta_baixo): o ponto de análise é o dia da divulgação, fixado pelo calendário da SRG (p. 8, 10), não escolhido pelos dados. A previsão dos autores é de efeito positivo "for some d > 0" (p. 13), sem especificar o dia; o dia +1 é justificado pela nota 26 (p. 14), que explica como uma pesquisa divulgada no dia t chega às cédulas registradas em t + 1. Não há pré-registro. Um humano pode querer rebaixar para incerto pela forma pouco especificada (vários dias pós testados).

its_coleta_nao_afetada e its_conhecimento_alocacao (proposta_baixo): o desfecho é o registro administrativo diário de cédulas recebidas pelo serviço cantonal de votações de Genebra (Service of Popular Votes and Elections), com o mesmo procedimento antes e depois da divulgação (p. 8-9, 46); desfecho objetivo.

its_dados_incompletos (proposta_baixo): o painel é desbalanceado porque algumas votações não têm dados dos dias mais antigos; o painel balanceado de -2 a +8 dá resultados semelhantes (Figura 4, painel C; p. 15, 32). O dado faltante de anúncios (domingo de eleição, p. 11) não afeta o desfecho de comparecimento.

its_relato_seletivo (proposta_baixo): os quatro desfechos descritos nos métodos (comparecimento acumulado, log do número diário, taxa diária sobre todos os eleitores, taxa líquida; p. 9) aparecem nos resultados (Figura 2, Figura 4, Tabela 3, Tabela C.3). O acumulado só aparece como gráfico bruto (Figura 2), sem estimativa de estudo de eventos. Não há protocolo ou pré-registro para comparar.

its_outros_riscos (proposta_baixo): (a) sazonalidade por dia da semana: a coluna 1 não inclui efeitos fixos de dia até a eleição, que capturam o dia da semana (nota 27, p. 14); a coluna 2 os inclui e o coeficiente do dia +1 fica em 0.3709** (p. 39). (b) Antecipação: coeficientes prévios nulos. (c) Poucos pontos pré-intervenção: 5 dias úteis antes da divulgação, com painel desbalanceado. (d) Multiplicidade: o dia +1 é um de 14 coeficientes pós; o teste do efeito acumulado dá p = 0.092 (p. 39). (e) Inconsistência de relato: o texto (p. 14) e a nota da Tabela 3 (p. 39) dizem que o dia de referência omitido é o dia da divulgação, mas a nota da Figura 3 (p. 31) diz que é o dia anterior à divulgação; isso muda a interpretação do dia +1 e vale conferir com os autores. Com (c)-(e), um humano pode preferir proposta_incerto neste item.

Não há julgamento geral no codebook EPOC deste projeto; nenhuma variável SI. O resultado despachado para esta ficha foi localizado.
