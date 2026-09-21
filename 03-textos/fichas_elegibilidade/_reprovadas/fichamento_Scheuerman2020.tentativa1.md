---
citekey: Scheuerman2020
ficha_id: Scheuerman2020
n_fichas_do_texto: 1
pdf_path: /Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/Scheuerman2020.pdf
paginacao: impressa
offset_pagina: 0
agente_fichador: fichador_el_102
data_fichamento: 2026-09-20
---

## Identificacao
- **texto_confere** — resposta: Sim; o título e os autores impressos no documento (Jaelle Scheuerman, Jason L. Harman, Nicholas Mattei, K. Brent Venable) batem com os metadados do registro, e a nota de publicação declara os anais do AAMAS 2020, compatível com o ano 2020; o arquivo é a cópia depositada no arXiv (arXiv:1912.00011v1) desse mesmo artigo. — evidência: "Heuristic Strategies in Uncertain Approval Voting Environments" (p. 1)
- **tipo_documento** — resposta: evento; artigo em anais de conferência, declarado na nota de publicação da primeira página (19th International Conference on Autonomous Agents and Multiagent Systems, AAMAS 2020, Auckland). — evidência: "Proc. of the 19th International Conference on Autonomous Agents and Multiagent" (p. 1)

## Criterios de elegibilidade
- **c1_populacao_contexto** — resposta: Sim; participantes recrutados no Mechanical Turk votam em eleições hipotéticas de aprovação com cinco candidatos e preferências induzidas (utilidade em centavos por candidato eleito). — evidência: "participants were asked to vote in a series of unrelated hypothetical elections" (p. 6)
- **c2_intervencao_estudada** — resposta: parcial; a exposição manipulada é a informação sobre a situação dos candidatos na eleição (votos já depositados para cada candidato e número de votos faltantes, n = 0, 1, 3), que faz o papel de informação de pesquisa no jogo eleitoral de laboratório, mas o documento nunca a descreve como resultado de pesquisa eleitoral, agregador, projeção ou boca de urna. — evidência: "the number of votes cast for each candidate so far" (p. 6); "We manipulate two environmental features, including the number of winners" (p. 4)
- **c3_desfecho** — resposta: Sim; o desfecho é a cédula de aprovação emitida pelo participante em cada cenário (quais candidatos aprova, classificada em truthful, take the X best e regret minimization), incluindo a abstenção; desfecho de voto (a abstenção é dentro do jogo, não comparecimento eleitoral real). — evidência: "we explore which strategies people use, and whether people vote truthfully" (p. 4); "The second most common strategy was to abstain" (p. 7)
- **c4_desenho_elegivel** — resposta: Sim; experimento comportamental online aleatorizado, com alocação aleatória dos participantes entre eleições de 2 e 3 vencedores e variação intraindividual do número de votos faltantes. — evidência: "Participants were then randomly assigned to be part of a 2-winner" (p. 6)
- **c5_estudo_primario** — resposta: Sim; o documento relata experimento próprio com 104 participantes e analisa os dados coletados. — evidência: "104 participants were recruited through Mechanical Turk to participate" (p. 6)
- **c6_nao_retratado** — resposta: Sim; não há marca, nota ou página de retratação em nenhuma das 9 páginas do documento. — evidência: "Heuristic Strategies in Uncertain Approval Voting Environments" (p. 1)

## Ligacao de relatos
- **outros_relatos_mesmo_estudo** — resposta: O documento declara construir sobre o trabalho anterior dos mesmos autores, referência [31] (Jaelle Scheuerman, Jason L. Harman, Nicholas Mattei, and Kristen Brent Venable. 2019. Heuristics in Multi-Winner Approval Voting. CoRR abs/1905.12104), ao qual acrescenta um novo experimento comportamental; o próprio arquivo é a versão depositada no arXiv (arXiv:1912.00011v1) do artigo dos anais do AAMAS 2020. — evidência: "We also build upon this work by introducing a new behavioral experiment" (p. 3)
- **fonte_dados_amostra** — resposta: Experimento comportamental online no Amazon Mechanical Turk com 104 participantes em eleições hipotéticas de aprovação com cinco candidatos, todos nos cenários de um vencedor (n=104) e depois alocados aleatoriamente em eleições de 2 vencedores (n=50) ou 3 vencedores (n=54); o documento não informa o período de coleta. — evidência: "All participants voted in the single winner scenarios (n=104)" (p. 6)
- **registro_financiamento** — resposta: 999 — evidência: 999

## Notas do codificador
- Paginação e offset: a numeração impressa aparece no rodapé central a partir da segunda página e coincide com o índice do PDF (PDF 3 traz 3, PDF 6 traz 6, PDF 9 traz 9); logo, paginacao impressa e offset_pagina 0, confirmado em páginas distantes (3, 6, 7 e 9).
- texto_confere: marquei Sim porque título, autores e ano batem com o registro e a nota de publicação da primeira página declara os anais do AAMAS 2020. Registro, ainda assim, que o arquivo traz o carimbo lateral arXiv:1912.00011v1 [cs.GT] 29 Nov 2019 e que o DOI impresso é um marcador de gabarito (https://doi.org/doi), diferente do DOI do registro; se o coordenador tratar depósito de arXiv como versão distinta, a resposta viraria parcial.
- c2 (decisão limítrofe): não há pesquisa eleitoral no sentido do protocolo. O que os participantes veem é o perfil parcial de votos já depositados mais o número de votos que faltam, isto é, informação sobre a situação dos candidatos gerada pela própria urna, não uma pesquisa pré-eleitoral, agregador ou projeção divulgada. Essa informação é, contudo, a exposição manipulada experimentalmente e cumpre no desenho o papel que a literatura citada no texto atribui à informação de pesquisa (Reijngoud e Endriss; Tal et al., com pesquisa pré-eleitoral; Fairstein et al.). Por isso parcial, e não Sim nem Não: a decisão depende de o protocolo aceitar o perfil parcial de votos como informação de pesquisa em jogo de laboratório.
- c3: o desfecho medido é a cédula efetivamente emitida, mas os resultados são reportados agregados por heurística (truthful, take the X best, regret minimization, abstenção) e por número de candidatos aprovados, e não como apoio ao candidato que lidera versus ao que está atrás. Mantive Sim porque escolha de voto é medida e a ausência de números diretamente utilizáveis não é motivo de Não; a comparação líder versus perseguidor exigiria os microdados.
- registro_financiamento: o documento não tem seção de agradecimentos nem nota de financiamento, e não cita pré-registro (OSF, AEA, RIDIE, EGAP); as páginas 8 e 9 passam das conclusões direto para as referências. Daí 999.
- Menciona consentimento informado e pagamento aos participantes (US$ 1,00 mais bônus de até US$ 8,00), mas nenhum número de protocolo ou processo.
