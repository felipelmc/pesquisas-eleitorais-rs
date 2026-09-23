---
citekey: Grillo2024c
ficha_id: Grillo2024c#mobilizacao
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Grillo2024c.pdf
paginacao: indice-do-PDF
offset_pagina: 0
agente_fichador: rob-B-Grillo2024c-epoc
data_fichamento: 2026-09-23
ferramenta: epoc
paginas_pdf: 20
faixas_lidas: 1-20
---

## 00_Resultado
- **desenho_epoc** — resposta: grupo_controle — evidência: "We compare the turnout rates in the second round to those" (p. 3)
- **resultado_avaliado** — resposta: mobilizacao, Tabela 1 coluna 1 (baseline DiD ponderado por eleitores registrados, sem controles de clima), coeficiente Closure X 2nd Round — evidência: "Closure X 2nd Round" (p. 13)

## C_Grupo_controle
- **cg_sequencia_aleatoria** — resposta: proposta_alto — evidência: (derivado de: desenho_epoc=grupo_controle; a regra do EPOC define antes-depois controlado como sempre proposta_alto, não há sequência aleatória de alocação)
- **cg_ocultacao_alocacao** — resposta: proposta_alto — evidência: (derivado de: desenho_epoc=grupo_controle; a regra do EPOC define antes-depois controlado como sempre proposta_alto)
- **cg_linha_base_outcome** — resposta: proposta_baixo — evidência: (derivado de: Tabela 1, coeficiente da linha "2nd Round" = -0.316, p-valor 0.360, isto é, o comparecimento às 12h (linha de base pré-choque informacional) não difere significativamente entre o 1º e o 2º turno)
- **cg_caracteristicas_base** — resposta: proposta_baixo — evidência: (derivado de: os "grupos" comparados são os mesmos 96 departamentos nos dois turnos, Tabela 1 "Departments 96"; características fixas do departamento são idênticas por construção, não havendo dois conjuntos distintos de unidades)
- **cg_dados_incompletos** — resposta: proposta_baixo — evidência: (derivado de: Tabela 1, "Observations 576" = 96 departamentos x 2 turnos x 3 horários (12h, 17h, fechamento), painel completo e balanceado, sem indício de perdas)
- **cg_conhecimento_alocacao** — resposta: proposta_baixo — evidência: (derivado de: o desfecho é o comparecimento eleitoral registrado oficialmente; nota da Tabela 1 "Turnout data from the French Ministry of Interior", medida objetiva e não sujeita a mascaramento)
- **cg_contaminacao** — resposta: proposta_incerto — evidência: (derivado de: pesquisas de boca de urna também circularam no 1º turno por mídias belgas/suíças, porém divulgadas com mais cautela e mais tarde do que no 2º turno, conforme descrito na Seção 2 sobre o comportamento da RTBF no 1º turno; não é possível excluir contato do "grupo controle" com informação semelhante)
- **cg_relato_seletivo** — resposta: proposta_baixo — evidência: (derivado de: os desfechos às 17h e no fechamento, descritos na Equação 1 da Seção 3, aparecem integralmente na Tabela 1 nas quatro especificações discutidas no texto, sem omissão aparente)
- **cg_outros_riscos** — resposta: proposta_alto — evidência: (derivado de: resultado avaliado = Tabela 1 col. 1; o próprio resumo do artigo reconhece "similar trends were observed in previous elections", risco que a especificação da coluna 1 não corrige)

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
- Justificativa de `cg_outros_riscos` (movida do campo de resposta pelo coordenador): risco de tendências diferentes entre os turnos não corrigidas na especificação avaliada (Tabela 1, coluna 1, é uma DiD simples de dois turnos, sem o ajuste por tendências prévias que os autores só aplicam na comparação triplo-diferenças da Tabela 2)
Desenho: o artigo usa uma DiD comparando comparecimento no 2º turno (informado pelo choque de pesquisas de boca de urna divulgadas por mídia belga/suíça) contra o 1º turno (mesmos 96 departamentos, sem o choque, ou com choque mais tardio e cauteloso), a três horários (12h, 17h, fechamento); Seção 3, Eq. 1. Por isso desenho_epoc=grupo_controle (antes-depois controlado com unidades agregadas), conforme a orientação do coordenador para DiD com departamentos.

Por domínio: cg_sequencia_aleatoria e cg_ocultacao_alocacao são sempre proposta_alto em antes-depois controlado, pela regra do próprio codebook, independente do texto. cg_linha_base_outcome e cg_caracteristicas_base ficaram proposta_baixo porque o desenho compara os mesmos departamentos nos dois turnos (painel), e o coeficiente "2nd Round" (linha de base às 12h) não é significativo (p=0.360). cg_dados_incompletos ficou proposta_baixo pelo painel balanceado (576 = 96x2x3, sem células faltantes aparentes). cg_conhecimento_alocacao ficou proposta_baixo por ser registro administrativo objetivo (Ministério do Interior). cg_contaminacao ficou proposta_incerto porque pesquisas de boca de urna também existiram no 1º turno (mais cautelosas, mais tardias), o que é uma contaminação parcial do "grupo controle" e não permite proposta_baixo com confiança. cg_relato_seletivo ficou proposta_baixo pois os dois horários pós-tratamento anunciados na metodologia aparecem nos resultados. cg_outros_riscos ficou proposta_alto porque a especificação avaliada (Tabela 1, col. 1) é a DiD simples sem o controle de tendências prévias que os próprios autores implementam só na Tabela 2 (triplo-diferenças com 2012 e 2007); o resumo do artigo reconhece explicitamente tendências semelhantes em eleições anteriores como uma ressalva a essa coluna.

Proposta geral (pior domínio): proposta_alto (arrastado por cg_sequencia_aleatoria, cg_ocultacao_alocacao e cg_outros_riscos; note-se que não há variável "geral" no codebook_v0_epoc.csv fornecido, então este valor é só um resumo para a linha final, não uma ficha).

C_ITS inteiro é NA_secao pelo fluxo (desenho_epoc=grupo_controle), como no codebook.

Resultado de {RESULTADOS}: encontrado sem ambiguidade na Tabela 1, coluna (1) (p. 13 do PDF), coeficiente "Closure X 2nd Round" = -3.440*** (p=0.000), especificação ponderada por eleitores registrados e sem tendências de clima, exatamente como descrito no despacho.

Nenhum SI/NI/NPD/I aplicável nesta ficha (EPOC não usa esse código na seção grupo_controle; a incerteza é expressa por "incerto" em cg_contaminacao). Nenhuma sobreposição de algoritmo além da regra fixa de cg_sequencia_aleatoria/cg_ocultacao_alocacao descrita no próprio codebook.
