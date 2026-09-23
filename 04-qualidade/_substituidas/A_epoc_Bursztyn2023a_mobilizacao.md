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
- **desenho_epoc** — resposta: grupo_controle — evidência: "This is a simple event study, examining voter turnout by" (p. 13); "eventually have closer or less close polls" (p. 14)
- **resultado_avaliado** — resposta: Tabela 3, coluna 1: comparecimento líquido diário em Genebra (net turnout, %), coeficiente do dia +1 após a divulgação × proximidade ex ante padronizada = 0.3905 (EP 0.1737; p do wild cluster bootstrap 0.045); 52 votações, 766 observações votação×dia, efeitos fixos de votação e de dia relativo à pesquisa — evidência: "1 day after poll × Ex Ante Closeness (std.)" (p. 39); "0.3905**" (p. 39)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: "we rely on naturally-occurring exposure to poll information" (p. 6)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: "we exploit the precise day-level timing of the release" (p. 3)
- **cg_linha_base_outcome** — resposta: proposta_baixo — evidência: "Prior to the day when polls are released, we see no difference" (p. 14); "0.973" (p. 39)
- **cg_caracteristicas_base** — resposta: proposta_incerto — evidência: "the importance of an issue and political advertising are strongly" (p. 13); "time-invariant issue type that might" (p. 15)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: "as some votes do not have voting data for earlier days" (p. 15); "our results are not sensitive to this choice of sample window" (p. 15)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "administrative records on the timing of voter turnout" (p. 8)
- **cg_contaminacao** — resposta: proposta_incerto — evidência: "Two rounds of polls are typically conducted" (p. 8); "naturally-occurring exposure to poll information that arrives to entire populations" (p. 6)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: "We consider cumulative turnout rate as of" (p. 9); "the log of the daily turnout level as the outcome" (p. 15)
- **cg_outros_riscos** — resposta: proposta_baixo — poucos clusters (52 votações), tratados com wild cluster bootstrap; resposta dos anúncios políticos só a partir do dia +3, depois do efeito no dia +1; inconsistência sobre o dia de referência omitido (dia da divulgação no texto e na Tabela 3, dia anterior na nota da Figura 3) — evidência: "we present p-values from the wild cluster" (p. 14); "until three days after the poll" (p. 15)

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
Classificador. O resultado vem de um estudo de eventos com exposição contínua: 52 votações em Genebra, cada uma observada de 5 dias úteis de votação antes até o último dia depois da divulgação da pesquisa final; o coeficiente de interesse é a interação entre a proximidade da pesquisa (padronizada) e o indicador de dia, com efeitos fixos de votação e de dia relativo à pesquisa. O contrafactual vem das votações com pesquisas menos apertadas (comparação de intensidade), o que é um antes-depois controlado / diferenças em diferenças com dose contínua, e não uma série interrompida sem grupo de comparação. Por isso `grupo_controle`; as variáveis de ITS ficam `NA_secao`.

Sequência e ocultação. Alto por definição (desenho não randomizado, antes-depois controlado). Pela convenção EPOC da skill, esses dois itens não entram no julgamento geral.

Linha de base do desfecho. O desfecho é medido nos 5 dias anteriores à divulgação; nenhum coeficiente de antecipação é significativo e o teste conjunto das antecipações dá p = 0.973 (0.986 no wild bootstrap). Proposta baixo.

Características de base. Não há tabela de equilíbrio entre votações com pesquisas mais e menos apertadas. A Figura 1 (p. 13 e 29) mostra que, no nível federal, proximidade, importância do tema e anúncios estão correlacionados entre si, ou seja, as votações diferem em características ligadas à proximidade. Diferenças fixas no tempo são absorvidas pelos efeitos fixos de votação, e os anúncios não diferem antes da divulgação (Figura 5), mas a importância do tema pode interagir com o calendário de votação. Proposta incerto; um humano pode ler como baixo, dado o ajuste por efeitos fixos e a ausência de pré-tendências.

Dados incompletos. Painel desbalanceado porque algumas votações não têm dados nos dias mais antigos; a versão balanceada (−2 a +8, Figura 4, Painel C) dá o mesmo resultado. O desfecho vem de registros administrativos completos. Proposta baixo.

Conhecimento da alocação. Desfecho objetivo (cédulas registradas diariamente pelo serviço cantonal). Proposta baixo.

Contaminação. Toda votação recebe pesquisa; o grupo de comparação são votações com pesquisas menos apertadas, e não votações sem pesquisa. Os eleitores também têm acesso à primeira rodada de pesquisa (cerca de 5 semanas antes) e a informação sobre proximidade em outros meios, o que se sobrepõe ao período pré. Isso tende a puxar a estimativa para zero, mas o item fica incerto porque a comparação envolve contato com a mesma intervenção em outra dose.

Relato seletivo. Os quatro desfechos anunciados (acumulado, log do número diário, taxa diária sobre todos os eleitores, taxa líquida) aparecem nos resultados (Figura 2, Tabela 3, Figura 4). Não há menção a plano de análise pré-registrado. Proposta baixo.

Outros riscos. Poucos clusters (52), tratados com wild cluster bootstrap (o p do dia +1 fica em 0.045). A resposta dos anúncios começa no dia +3, então não explica o dia +1. Há uma inconsistência de relato sobre o dia omitido (texto na p. 14 e nota da Tabela 3: dia da divulgação; nota da Figura 3, p. 31: dia anterior à divulgação). O efeito é imediato (limitação reconhecida pelos autores, nota 25). Proposta baixo.

Geral, só como insumo para os avaliadores humanos (o codebook não tem variável de julgamento geral): pela convenção EPOC da skill (ignorar sequência e ocultação no CBA; moderado se algum item-chave for incerto), a contaminação incerta leva a uma proposta_moderado.

Nenhum item SI pede contato com autores. O resultado indicado pelo coordenador foi localizado (Tabela 3, coluna 1, p. 39).
