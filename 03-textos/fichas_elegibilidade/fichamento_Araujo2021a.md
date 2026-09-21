---
citekey: Araujo2021a
ficha_id: Araujo2021a
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Araujo2021a.pdf
paginacao: impressa
offset_pagina: 1
agente_fichador: fichador_el_108
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim — o título e o primeiro autor do documento batem com os metadados do registro (Araújo, Víctor; Gatto, Malu A. C.; DOI 10.1017/S000712342100034X) — evidência: "Casting Ballots When Knowing Results" (p. 1)
- **tipo_documento** — resposta: artigo — artigo publicado no British Journal of Political Science (versão publicada depositada no repositório ZORA) — evidência: "British Journal of Political Science (2021), page 1 of 19" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim — eleitores brasileiros em eleição presidencial real (2018), analisados em unidades eleitorais agregadas (urnas eletrônicas por seção) — evidência: "In the 2018 Brazilian presidential elections, unpredictable technical glitches caused" (p. 1); "In each station, there is one voting machine" (p. 9)
- **c2_intervencao_estudada** — resposta: parcial — a exposição analisada é a divulgação dos resultados oficiais da apuração às 19:00 BRT enquanto urnas atrasadas ainda votavam, não o resultado de uma pesquisa eleitoral; os autores contrastam explicitamente seu caso com pesquisas pré-eleitorais — evidência: "machines that remained open after preliminary results started being announced" (p. 10); "our results emerge from a situation of exposure to vote tallies" (p. 16)
- **c3_desfecho** — resposta: Sim — desfecho de voto: participação de votos por candidato (primeiro, segundo e terceiro colocados) e votos brancos e nulos por urna; comparecimento entra apenas como controle, não como desfecho — evidência: "share of votes for Haddad (second place)" (p. 9)
- **c4_desenho_elegivel** — resposta: Sim — experimento natural com variação exógena da exposição (falhas técnicas da biometria que atrasaram o fechamento de urnas), estimado por MQO com dummy de tratamento — evidência: "strategic voting; natural experiment; Brazil" (p. 1); "Ordinary Least Squares (OLS) models for each outcome variable" (p. 10)
- **c5_estudo_primario** — resposta: Sim — estudo primário com análise própria de dados oficiais por urna nos dois turnos de 2018 — evidência: "323 voters are registered to cast ballots on each voting machine" (p. 9)
- **c6_nao_retratado** — resposta: Sim — não há marca, nota ou página de retratação no documento — evidência: "Casting Ballots When Knowing Results" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: O documento remete a apêndices online (Supplementary Material) e à base de replicação depositada no Harvard Dataverse (Araújo V and Gatto MAC 2021, Replication Data for: 'Casting ballots when knowing results'); a capa do repositório ZORA registra a versão de registro publicada no British Journal of Political Science, 52(4):1709-1727 (2022) — evidência: "Replication data for this article can be found in Harvard Dataverse" (p. 17)
- **fonte_dados_amostra** — resposta: Dados eleitorais oficiais por urna eletrônica (N = 454.490 urnas) nos dois turnos da eleição presidencial brasileira de 2018, com horário de fechamento de cada urna definindo o tratamento (8.548 urnas tratadas no 1º turno) — evidência: "Using timestamp data of the last vote cast in each voting machine" (p. 2); "8,548 (1.6 per cent) observations are in our treatment group" (p. 10)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- **Offset de página.** O PDF tem 20 páginas: a página 1 do PDF é a capa do repositório ZORA (sem numeração impressa) e a página 2 do PDF traz o cabeçalho impresso "British Journal of Political Science (2021), page 1 of 19". Confirmei o offset em duas páginas distantes: PDF 11 = impressa 10 (cabeçalho "10  Victor Araújo and Malu A.C. Gatto") e PDF 20 = impressa 19. Logo, impressa P → PDF = P + 1, `offset_pagina: 1`. Todas as evidências usam a numeração impressa.
- **texto_confere.** Marquei `Sim`, e não `parcial`: o arquivo é a versão publicada (a capa do ZORA diz "Published Version"), com o mesmo título, os mesmos autores e o mesmo DOI do registro. A única divergência é de paginação/ano de fascículo: o corpo do artigo é a versão FirstView de 2021 (páginas 1-19), enquanto a capa informa a publicação final em 2022, 52(4):1709-1727. Não é outra versão do trabalho (preprint, working paper, tese), é o mesmo artigo antes da paginação de fascículo.
- **c2 — por que `parcial`.** É o ponto limítrofe da ficha. A exposição identificada não é uma pesquisa eleitoral no sentido do protocolo: é a divulgação oficial dos resultados parciais da apuração (vote tallies), que começou às 19:00 BRT enquanto urnas atrasadas por falhas da biometria continuavam abertas. Os próprios autores marcam essa diferença em relação à literatura de pesquisas ("our results emerge from a situation of exposure to vote tallies, not pre-electoral polls", p. 16). Por outro lado, o caso é funcionalmente próximo do item "projeção divulgada antes do fechamento das urnas" do critério (informação sobre o resultado divulgada antes de os eleitores terminarem de votar, com desenho de experimento natural, na mesma literatura de voto sequencial que o protocolo cobre: Morton et al. 2015, Chatterjee e Kamal 2020 sobre boca de urna). Como não cai claramente nem na lista de exposições aceitas (a informação não vem de survey) nem nas exclusões explícitas (resultados de eleições passadas, mercados de apostas, métricas de redes sociais), deixei `parcial` para arbitragem do coordenador em vez de excluir.
- **c3.** O desfecho é de voto (share de votos por candidato e share de brancos e nulos na urna). O comparecimento não é desfecho: entra como covariável de controle ("we also control for turnout rates", p. 11), e o desenho impede efeito via comparecimento, porque quem chega depois do horário oficial de fechamento não entra na fila.
- **c4.** Além do experimento natural principal, o artigo traz testes de placebo (urnas atrasadas mas fechadas antes das 19:00) e uma checagem com a eleição de 2014, o que reforça a variação identificada da exposição.
- **registro_financiamento.** Não há número de processo, edital nem identificador de pré-registro (OSF, AEA RCT Registry, RIDIE, EGAP) no documento. Os agradecimentos (p. 17) citam apenas pessoas, revisores e seminários, e a Data Availability Statement traz um DOI de base de dados (10.7910/DVN/GD92NS), que é repositório de replicação, não registro prévio. Por isso `999`, e não a transcrição desse DOI.
- **Divergência interna do texto (não afeta os critérios).** O número de urnas tratadas no segundo turno aparece como 1,024 na introdução (p. 2) e como 1,084 na seção de dados (p. 10), ambas com "(0.24 per cent)". Registro aqui para a etapa de extração; não usei esse número em nenhuma resposta.
