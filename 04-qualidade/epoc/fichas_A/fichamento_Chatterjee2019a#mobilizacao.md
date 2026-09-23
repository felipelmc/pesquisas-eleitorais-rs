---
citekey: Chatterjee2019a
ficha_id: Chatterjee2019a#mobilizacao
n_fichas_do_texto: 2
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Chatterjee2019a.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-A-Chatterjee2019a-epoc
data_fichamento: 2026-09-23
ferramenta: epoc
paginas_pdf: 33
faixas_lidas: 1-20,21-33
---

## 00_Resultado
- **desenho_epoc** — resposta: grupo_controle — evidência: "compare states having single and multi phase elections before and after" (p. 4); "comparing the same states from an earlier round of elections" (p. 18)
- **resultado_avaliado** — resposta: Tabela 7 (eleições estaduais para assembleias legislativas), bloco Voter Turnout, coluna 2 com controles (população, razão de sexo, alfabetização, total de eleitores, emprego urbano): DiD δ = 4.706*** (1.290), N = 1355; efeito da proibição de boca de urna sobre o comparecimento — evidência: "Impact of Exit Poll Bans on Voter Turnout and Winning Margins" (p. 28); "4.706***" (p. 28)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: "As conducting such experiment is infeasible and impractical" (p. 18); "we have to compare states that had elections just before" (p. 18)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: "the ban given predetermined electoral calendar in India" (p. 3); "Luckily, the states that went to elections just before and just" (p. 18)
- **cg_linha_base_outcome** — resposta: proposta_incerto — evidência: "comparing the same states from an earlier round of elections" (p. 18); "9.492***" (p. 28)
- **cg_caracteristicas_base** — resposta: proposta_alto — evidência: "these groups of states may have intrinsically" (p. 18); "Table 2: Summary Statistics" (p. 17)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: "the dataset consists of 681 constituencies of four" (p. 14); "1355" (p. 28)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: "We use administrative data from the statistical reports published" (p. 14)
- **cg_contaminacao** — resposta: proposta_baixo — evidência: "results of exit polls are reported at the end of the day" (p. 18); "Interestingly, all these states had single phase elections and therefore" (p. 11)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: "include voter turnout and winning margin" (p. 19)
- **cg_outros_riscos** — resposta: proposta_alto — evidência: "Bihar was the only state which had multi-phase election" (p. 14); "Due to this delimitation exercise, we are unable to" (p. 16); "any clear evidence of an impact on voter turnout" (p. 30)

## Notas do codificador
- Justificativa de `cg_outros_riscos` (movida do campo de resposta pelo coordenador): um único estado tratado (Bihar) contra três controles, com um só período pré e nenhum teste de tendências prévias para o comparecimento; choques específicos de Bihar entre as duas eleições ficam confundidos com a proibição; estimativa cai de 9,5 para 4,7 pontos com controles, sinal de desequilíbrio; redistritamento entre os períodos; erros-padrão robustos não agrupados; conclusão do texto contradiz a tabela
Classificador: diferenças em diferenças com unidades agregadas (circunscrições em estados), estados de eleição multifásica (tratados) contra estados de fase única (controles), antes e depois da proibição. EPOC grupo_controle, como manda o protocolo.

Sequência aleatória e ocultação: antes-depois controlado, SEMPRE proposta_alto.

Linha de base do outcome: o comparecimento foi medido na eleição anterior nos mesmos estados, mas o texto não relata o comparecimento pré por grupo; a figura de tendências paralelas (p. 24) mostra só participação de votos nas eleições nacionais, sem comparecimento. A queda do coeficiente de 9.492 (sem controles) para 4.706 (com controles) sugere diferenças importantes entre grupos, ajustadas só por covariáveis estaduais. Sem dados de linha de base, proposta_incerto; um humano pode ir para alto.

Características de base: Tabela 2 agregada, sem separar grupos; autores admitem possíveis diferenças intrínsecas. Proposta_alto.

Dados incompletos: 681 circunscrições em duas eleições dariam 1362 observações; a Tabela 7 usa 1355 (7 faltando, cerca de 0,5%), sem explicação. Perda pequena perto do efeito, proposta_baixo; incerto é defensável porque a perda não é explicada.

Conhecimento da alocação: comparecimento de registros administrativos da Comissão Eleitoral, objetivo.

Contaminação: alocação por estado; nos estados de fase única a boca de urna só sai após o fim da votação, então a proibição não afeta o controle (pressuposto dos autores).

Relato seletivo: o comparecimento consta dos outcomes da p. 19 e aparece nas Tabelas 7 e 8. Não há omissão, mas há relato inconsistente: a conclusão (p. 30) diz não haver evidência clara de impacto sobre o comparecimento, enquanto a Tabela 7 mostra efeito de 4.706*** nas eleições estaduais; a conclusão parece se apoiar só na Tabela 8 (nacionais). Registrado em outros riscos.

Outros riscos (domínio decisivo): um só estado tratado (Bihar) com uma eleição antes e uma depois; qualquer mudança específica de Bihar no comparecimento entre as eleições é confundida com a proibição; nenhum teste de tendências prévias para o comparecimento; efeito bruto de 9,5 pontos é grande e sensível aos controles; erros-padrão robustos por observação, não agrupados por estado; delimitação de 2008 entre os períodos; nas eleições nacionais o sinal se inverte (Tabela 8, -0.897 com controles). Não está documentado se houve boca de urna divulgada entre fases na eleição pré-proibição de Bihar. Proposta_alto.

Geral (não há variável no codebook): pelo pior domínio, alto.

Sem perguntas com SI. Resultado localizado conforme indicado pelo coordenador.
