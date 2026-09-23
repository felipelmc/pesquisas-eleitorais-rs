---
citekey: Bursztyn2023a
ficha_id: Bursztyn2023a#mobilizacao
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
- **desenho_epoc** — resposta: its — evidência: "This is a simple event study, examining voter turnout" (p. 13)
- **resultado_avaliado** — resposta: Tabela 3, coluna 1: comparecimento líquido diário em Genebra, coeficiente do dia +1 após a divulgação da pesquisa (0.3905**) — evidência: "1 day after poll × Ex Ante Closeness (std.)" (p. 39)

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
- **its_teste_t_sem_tendencia** — resposta: Não — evidência: "estimated as coefficients on the interaction of poll closeness" (p. 13)
- **its_intervencao_independente** — resposta: proposta_baixo — evidência: "absence of pre-trends suggests that the supply side was" (p. 15)
- **its_forma_efeito_pre_especificada** — resposta: proposta_baixo — evidência: "with a full set of day-to-poll indicators" (p. 13)
- **its_coleta_nao_afetada** — resposta: proposta_baixo — evidência: "registered on the very same day of any" (p. 9)
- **its_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "Data on daily voter turnout in the canton of Geneva" (p. 8)
- **its_dados_incompletos** — resposta: proposta_baixo — evidência: "some votes do not have voting data for earlier" (p. 15)
- **its_relato_seletivo** — resposta: proposta_baixo — evidência: "we examine the log of the daily turnout level" (p. 15)
- **its_outros_riscos** — resposta: proposta_baixo — evidência: "Test of Joint Significance of Leads (p-value)" (p. 39)

## Notas do codificador
Desenho: o resultado avaliado vem do estudo de evento diário de Genebra (Tabela 3), que observa comparecimento em múltiplos dias antes e depois da liberação de cada pesquisa (dia -5 a dia 9+), agrupando 52 votos, sem um grupo de município "controle" separado que não receba a pesquisa — a variação é de dose (proximidade) em torno de um único ponto de intervenção repetido. Isso corresponde a `its` (série com vários pontos antes/depois, sem grupo controle separado), e não a `grupo_controle`, que ficou reservado para a heterogeneidade por município na Tabela 6 (outro resultado deste texto).

Por domínio:
- `its_teste_t_sem_tendencia`: Não — o desenho usa um modelo de regressão de evento com efeitos fixos de voto e de dia-para-pesquisa (equação 1), não um teste t simples ignorando tendência.
- `its_intervencao_independente`: proposta_baixo — os autores testam e não encontram diferença de tendência ou nível de comparecimento nos dias anteriores à liberação, e mostram que a resposta do "lado da oferta" (propaganda política) só aparece com defasagem de 3 dias, depois do efeito no comparecimento já ter ocorrido.
- `its_forma_efeito_pre_especificada`: proposta_baixo — o ponto de corte (dia de liberação da pesquisa) e a janela de indicadores dia-a-dia são definidos a priori pelo desenho do estudo de evento, não escolhidos a partir dos dados.
- `its_coleta_nao_afetada` e `its_conhecimento_alocacao`: proposta_baixo — o comparecimento é medido por registro administrativo de cédulas recebidas (voto por correspondência), com o mesmo processo de registro antes e depois da liberação da pesquisa; não há avaliação subjetiva do desfecho.
- `its_dados_incompletos`: proposta_baixo — o painel é desbalanceado (nem todo voto tem dados desde 5 dias antes), mas os autores replicam o resultado principal num painel balanceado (Figura 4, Painel C) com resultados semelhantes.
- `its_relato_seletivo`: proposta_baixo — os mesmos resultados são reportados com várias medidas de desfecho (comparecimento líquido, comparecimento sobre total de eleitores, log do comparecimento, comparecimento acumulado), todas convergentes.
- `its_outros_riscos`: proposta_baixo — sobrepus a preocupação inicial de que a janela pré-intervenção é curta (só 5 dias) porque o próprio artigo testa formalmente a significância conjunta dos coeficientes de "antes" (Test of Joint Significance of Leads, p = 0.973 na coluna do resultado avaliado), não rejeitando ausência de pré-tendência; o dia da eleição é sempre domingo, e os efeitos fixos de dia-para-pesquisa/dia-para-eleição absorvem sazonalidade semanal.
- Proposta geral: todos os domínios aplicáveis foram propostos como baixo (exceto o item de fluxo `its_teste_t_sem_tendencia` = Não, que é favorável), então a proposta geral deste resultado é `proposta_baixo`.

Resultado localizado na Tabela 3, coluna 1, linha "1 day after poll × Ex Ante Closeness (std.)" = 0.3905** (0.1737) [0.045], p. 39 do PDF.
SI (sem informação): nenhuma resposta usou código de "sem informação" — EPOC `its` não tem código dedicado para isso nesta ficha; todas as respostas aplicáveis foram baixo ou Não.
