---
citekey: Magesan2024
ficha_id: Magesan2024
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Magesan2024.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_149
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: parcial — título e autores batem com o registro, mas o PDF é uma versão posterior (datada de 7 de julho de 2025) do mesmo working paper registrado com ano 2024 — evidência: "Pivotality" (p. 1); "July 7, 2025" (p. 1)
- **tipo_documento** — resposta: working_paper — evidência: "JEL Classification: D72, D78" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Não — a população são cidadãos que decidem assinar ou não petições ao governo britânico, não eleitores escolhendo entre candidatos, partidos ou opções de referendo, nem unidades eleitorais agregadas — evidência: "any citizen can sign and add her name to the petition" (p. 8)
- **c2_intervencao_estudada** — resposta: Não — a exposição analisada é a contagem corrente de assinaturas em relação ao limiar de resposta do governo, não um resultado de pesquisa eleitoral — evidência: "the current signature count is public knowledge for potential signatories" (p. 2)
- **c3_desfecho** — resposta: Não — o desfecho é a taxa de assinatura por petição ao longo do tempo, sem medida de intenção de voto, voto agregado ou comparecimento eleitoral — evidência: "where the outcome is rate of signature within petition over time" (p. 10)
- **c4_desenho_elegivel** — resposta: Sim — quase-experimento de descontinuidade de regressão com variação identificada em torno dos limiares de 10 mil e 100 mil assinaturas — evidência: "we use standard RD methodology to recover the structural model parameter" (p. 17)
- **c5_estudo_primario** — resposta: Sim — estudo primário com coleta própria de dados de alta frequência por raspagem do sistema de petições — evidência: "We used a scraper to track petitions over time" (p. 10)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento — evidência: "Pivotality" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: Menciona um Supplementary Appendix com a construção dos dados de alta frequência e com a Table A.8; não menciona versão anterior, tese, dissertação ou outro artigo com os mesmos dados — evidência: "See the Supplementary Appendix for more detail on the construction" (p. 10)
- **fonte_dados_amostra** — resposta: Dados próprios de alta frequência, raspados do sistema de petições do governo britânico entre maio de 2023 e o fim de abril de 2024, com 2.370 petições encerradas observadas (709.834 observações), somados ao cadastro público de todas as petições desde 2011 — evidência: "from May 2023 to the end of April 2024" (p. 4); "we observed 2370 petitions in total that closed" (p. 11)
- **registro_financiamento** — resposta: SSHRC, IG grant 435-2019-0437 (sem menção a pré-registro) — evidência: "Magesan gratefully acknowledges funding from SSHRC through IG grant 435-2019-0437." (p. 1)

## Notas do codificador
- Offset de página: a numeração impressa no rodapé coincide com o índice do PDF (rodapé "1" na folha 1 do PDF, rodapé "29" na folha 29, e rodapés 2, 4, 8, 10, 11 e 17 nas folhas homônimas), logo `offset_pagina: 0`. Todas as citações desta ficha foram conferidas nas folhas indicadas pela fórmula folha = página anotada + 0.
- `texto_confere` = parcial porque o título ("Pivotality") e os dois autores batem exatamente com o registro, mas a folha de rosto traz a data de 7 de julho de 2025, enquanto o registro é do working paper de 2024 (DOI SSRN): trata-se de outra versão do mesmo trabalho, não de outro trabalho.
- `tipo_documento` = working_paper: o documento não declara periódico nem nota de publicação; traz folha de rosto datada, palavras-chave, classificação JEL e agradecimentos com financiamento, e a nota 26 agradece a "an anonymous reviewer". A evidência usada é a linha de classificação JEL, o marcador literal mais próximo dessa natureza no próprio texto.
- C1, C2 e C3 falham pelo mesmo motivo de fundo: o objeto empírico são assinaturas em petições ao governo do Reino Unido, não eleições. Os autores chegam a tratar a contagem corrente de assinaturas como análoga a informação de pesquisa ("effectively receiving poll information in real time", p. 8) e a proximidade do limiar como análoga à disputa apertada, mas nenhuma pesquisa eleitoral (pré-eleitoral, agregador, projeção ou boca de urna) é manipulada ou medida, e nenhum desfecho de voto ou de comparecimento eleitoral é analisado.
- C4 = Sim avalia apenas o tipo de desenho: é um quase-experimento de descontinuidade com variação identificada, desenho listado como aceito. A ressalva de que a descontinuidade identifica exposição ao limiar de assinaturas, e não a um resultado de pesquisa eleitoral, está registrada em C2, que é onde o protocolo a trata.
- `outros_relatos_mesmo_estudo`: a única menção a outro documento do mesmo estudo é ao Supplementary Appendix (notas 14 e p. 21, "Supplementary Appendix Table A.8"), que não veio no PDF. Não é uma versão anterior nem um relato independente, mas foi registrado por ser um documento separado com os mesmos dados.
