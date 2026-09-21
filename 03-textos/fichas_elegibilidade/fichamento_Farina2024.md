---
citekey: Farina2024
ficha_id: Farina2024
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Farina2024.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_167
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — o título e os dois autores batem com os metadados do registro, mas o documento em mãos é uma versão posterior (datada de 14 de setembro de 2025) do mesmo working paper registrado como 2024, e o próprio texto informa que circulou antes com outro título — evidência: "Hiding a Flaw? Experimental Evidence on Multi-Dimensional Information" (p. 1)
- **tipo_documento** — resposta: working_paper — manuscrito datado, não publicado em periódico, com apêndice marcado "For Online Publication Only" e menção a versão anterior circulada — evidência: "earlier circulated version was entitled" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Não — a amostra é de estudantes de graduação recrutados para um experimento de laboratório de divulgação de informação (jogo emissor-receptor sobre "secret numbers"), sem eleitores, candidatos, partidos, referendo ou unidades eleitorais — evidência: "We recruited 120 subjects from the University" (p. 10)
- **c2_intervencao_estudada** — resposta: Não — a exposição manipulada é a dimensionalidade do espaço de informação (um versus dois atributos verificáveis do emissor), não resultado de pesquisa eleitoral, agregador, projeção ou boca de urna — evidência: "modifies the control game by adding an attribute" (p. 4)
- **c3_desfecho** — resposta: Não — os desfechos são a decisão de divulgar cada número secreto e o palpite do receptor sobre esse número, além das crenças elicitadas; não há intenção de voto, voto, votação agregada nem comparecimento (nem desfecho de voto, nem de comparecimento) — evidência: "receiver guesses the number. Payoffs are designed" (p. 3); "Table 1 summarizes disclosure rates across treatments" (p. 16)
- **c4_desenho_elegivel** — resposta: Sim — é experimento aleatorizado de laboratório, com desenho entre sujeitos, papéis fixos e pareamento aleatório, em sessões de controle e de tratamento (a inelegibilidade deste texto vem da exposição e do desfecho, não do desenho) — evidência: "We use a between-subjects design with fixed roles and random matching." (p. 10)
- **c5_estudo_primario** — resposta: Sim — relata experimento próprio conduzido pelos autores, com dados coletados em laboratório e análise estatística própria — evidência: "In this paper, we use a lab experiment to study" (p. 3)
- **c6_nao_retratado** — resposta: Sim — não há marca "RETRACTED", nota ou página de retratação em nenhuma das 70 folhas do PDF — evidência: "Hiding a Flaw? Experimental Evidence on Multi-Dimensional Information" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Sim, o documento menciona uma versão anterior do mesmo trabalho, intitulada "Hiding a Flaw: An Experimental Analysis on Multi-Dimensional Information Disclosure" — evidência: "earlier circulated version was entitled" (p. 1)
- **fonte_dados_amostra** — resposta: Experimento de laboratório no Experimental Economics Laboratory da University of Maryland (EEL-UMD), nos semestres de primavera e outono de 2022, com 120 estudantes de graduação em 10 sessões (4 de controle e 6 de tratamento, 60 sujeitos por condição), 50 rodadas por sujeito — evidência: "We recruited 120 subjects from the University" (p. 10); "during the Spring and Fall semesters of 2022" (p. 10)
- **registro_financiamento** — resposta: Não há identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP) nem número de processo ou edital no documento; o único financiamento citado é o "Behavioral and Social Sciences Dean's Research Initiative Award, University of Maryland, College Park", nomeado sem número — evidência: "Research Initiative Award, University of Maryland, College Park" (p. 1)

## Notas do codificador
- Paginação: a numeração impressa do corpo do texto coincide com o índice do PDF (folha 1 imprime "1", folha 10 imprime "10", folha 16 imprime "16", folha 20 imprime "20", folha 33 imprime "33"), logo `offset_pagina: 0`. Atenção para o coordenador: o "Online Appendix (For Online Publication Only)" reinicia a numeração impressa em 1 a partir da folha 48 do PDF (e as folhas de instruções lidas aos participantes não têm número impresso). Nenhuma evidência desta ficha vem do apêndice online: todas as citações estão entre as páginas impressas 1 e 16, faixa em que a fórmula folha_do_PDF = pagina_anotada + 0 foi conferida citação por citação.
- `texto_confere` = parcial (e não Sim) porque o título ("Hiding a Flaw? Experimental Evidence on Multi-Dimensional Information Disclosure") e os autores (Agata Farina; Mario Leccese) batem exatamente com os metadados, mas a folha de rosto traz a data de 14 de setembro de 2025, enquanto o registro é de 2024 — ou seja, é uma versão revista do mesmo working paper. A nota de rodapé de agradecimentos registra ainda um título anterior diferente.
- `tipo_documento` = working_paper: o documento não declara em lugar nenhum "working paper", "preprint" ou veículo de publicação; a classificação apoia-se na menção explícita a uma "earlier circulated version" e na existência de um apêndice "For Online Publication Only", marcas de manuscrito ainda não publicado. Se o coordenador preferir tratar depósitos do SSRN como preprint, a alternativa seria "preprint"; não há no texto nada que decida entre os dois rótulos.
- O texto é elegível quanto ao desenho (c4 = Sim, experimento aleatorizado de laboratório) e quanto a ser estudo primário (c5 = Sim), mas falha em população/contexto, intervenção e desfecho: trata-se de um jogo de divulgação verificável de informação entre "Player S" e "Player R" sobre números secretos, com aplicações discutidas em mercados (contratação, investidores, bens de consumo, relatórios financeiros), sem qualquer eleição, candidato, partido ou pesquisa eleitoral como objeto empírico. A única menção próxima ao tema da revisão está na lista de referências (um artigo de 2018 sobre efeitos de pesquisas no comparecimento), que é citação bibliográfica, não objeto do estudo — não serve para atender c1, c2 ou c3.
- `c4` foi respondido pelo tipo de desenho, como pede o prompt da variável, mesmo o estudo não sendo elegível no conjunto: o protocolo aceita experimento aleatorizado de laboratório, e é exatamente isso que o documento descreve.
- Nenhuma variável recebeu 999 e nenhuma recebeu NA_secao (o codebook deste projeto não tem seções condicionais).
- Documento com 70 folhas, abaixo do limite de 300: foi lido por inteiro (folhas 1 a 70 do PDF), incluindo apêndices A a D e as instruções do experimento.
