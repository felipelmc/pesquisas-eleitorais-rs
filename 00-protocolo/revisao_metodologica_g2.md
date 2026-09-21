# Revisão metodológica — G2

Tipo de revisão: efetividade_swim (variante rápida). Arquivos lidos: 16 de 16 (9 em `00-protocolo/`, sem `ancoras_validacao.csv`; 7 em `01-busca/`; cada um lido inteiro numa parte; `brutos/` e `bola_de_neve/` vazias; nenhum PDF ou imagem). Itens verificados: 16; não aplicáveis: 3.
Resumo: CRITICO 0 · ALTO 7 · MEDIO 14 · BAIXO 6

## Problemas

### R01 [ALTO] Convenção de sinal classifica voto estratégico em disputas multicandidato como underdog
- Item: P10
- Onde: protocolo.md → seção 2, regras de sinal (linha 76); teoria_programa.md → tabela por elo, E2 (linha 27); codebook_v0_efetividade.csv → `b2_direcao_estimativa_principal` (linha 39)
- Evidência: "Quando o estudo mede o apoio ao candidato que está atrás, a linha de efeito continua no construto `apoio_ao_lider`, com `direcao_desejada` = `reduzir`" (protocolo.md:76) × E2: "aumentar (*bandwagon*) ou migração para o segundo colocado competitivo" (teoria_programa.md:27)
- Por que importa: Em pluralidade com três ou mais candidatos, ou em sistema proporcional com cláusula de barreira (os sinais de coalizão de Meffert & Gschwend, 2011, fonte do próprio E2), a pesquisa pode aumentar o apoio a quem está atrás por cálculo de viabilidade: deserção para o segundo colocado viável ou voto de socorro a um parceiro abaixo da cláusula. Pela regra atual, esses efeitos saem com g < 0 e são somados ao underdog por simpatia (E5). Isso distorce justamente a resposta sobre a direção.
- Correção sugerida: Acrescentar à seção 2 uma regra para disputas multicandidato: o efeito é extraído para o candidato cuja posição a pesquisa manipula ou informa, com nova variável categórica `alvo_efeito` (lider | segundo_viavel | terceiro_inviavel | partido_abaixo_clausula | opcao_referendo) no codebook v0. Contrastes de viabilidade ou de cláusula vão para célula própria, ou ao menos para uma sensibilidade que os retire da célula principal. Replicar a regra no prompt de `b2_direcao_estimativa_principal` e, nos produtos, rotular a direção como bandwagon/underdog, não como "benéfica/danosa".

### R02 [ALTO] Checklist de comparabilidade junta contrastes e estimandos de magnitudes diferentes
- Item: P11
- Onde: protocolo.md → seção 8, [15a] (linhas 232 e 236); seção 6, regras de efeito (linha 198); seção 8, [15c] moderadores (linhas 249-255)
- Evidência: "sem pesquisa, ou mesmo candidato mostrado atrás (contrastes do mesmo sinal esperado)" (232); "um efeito por contraste com o controle ou entre braços, tratados com CHE" (198); "ATE e ITT juntos em experimentos | LATE, ATT e RDD local analisados em separado" (236)
- Por que importa: O contraste "à frente × atrás" soma a reação a ver o candidato na frente com a reação, de sinal oposto, a vê-lo atrás, e tende a ter magnitude diferente de "à frente × sem pesquisa". Agregá-los na mesma célula infla a heterogeneidade e deixa o g combinado sem leitura clara frente a δ. Aceitar, do mesmo estudo, contrastes com o controle e entre braços gera efeitos linearmente dependentes (a−c, b−c, a−b), que a CHE com ρ = 0,6 não representa. O estimando `associacao` (painel com exposição medida, aceito no C4 e previsto em `b2_estimando`) não tem lugar na tabela, e `comparador_tipo` não está entre os moderadores pré-especificados.
- Correção sugerida: Na [15a], separar por comparador: célula principal "à frente × sem pesquisa" e "à frente × atrás" em célula própria (no mínimo, `comparador_tipo` como moderador pré-especificado na [15c]). No multibraço, fixar "contrastes com o controle quando houver controle; contraste entre braços só sem controle". Alocar os painéis com estimando `associacao` numa célula não randomizada própria ou só na sensibilidade.

### R03 [ALTO] δ em g só vale para p0 = 0,50 e não serve à rota agregada; faixas incoerentes com δ
- Item: P12
- Onde: protocolo.md → seção 8, tabela de δ (linhas 271-276); seção 6, regras de efeito (linha 201)
- Evidência: "2 pontos percentuais no apoio ao líder | 0,044 (proporção de referência 0,50)"; faixas "trivial:0, pequena:0.022, moderada:0.066, grande:0.111"; "Votação agregada em pontos percentuais: rota de coeficiente padronizado pelo desvio-padrão da votação (`beta_sd`)"
- Por que importa: Pela fórmula declarada (d = ln(OR)·√3/π), os mesmos 2 pontos valem g = 0,044 com p0 = 0,50, 0,052 com p0 = 0,30 e 0,067 com p0 = 0,20 (conferido pelo revisor), isto é, "moderada" pelas faixas; em disputas multicandidato o apoio ao líder raramente está perto de 0,50. Na rota agregada, 2 pontos equivalem a 2/DP da votação (0,20 se o DP for de 10 pontos), e δ = 0,044 trataria como relevantes efeitos de cerca de 0,4 ponto. A faixa trivial termina em 0,022, abaixo de δ: efeitos entre 0,022 e 0,044 seriam "pequenos" e, ao mesmo tempo, abaixo do limiar de relevância. As faixas não se ancoram no campo, embora a síntese atualizada (Hardmeier, 2008) seja uma meta-análise.
- Correção sugerida: Declarar δ por métrica e por célula. Para desfechos binários individuais, δ = 2 pontos convertido pelo p0 de referência declarado de cada célula (ex.: mediana dos p0 dos estudos). Para a rota `beta_sd`, δ_g = 2 pontos divididos pelo DP de referência da votação, declarado. Fazer o limite superior de "trivial" coincidir com δ. Conferir se Hardmeier (2008) relata magnitudes utilizáveis como referência de campo; se não, manter a declaração de convenção. Usar `analise meta --delta <δ em g da célula>`.

### R04 [ALTO] Dano (desmobilização) só entra condicionado a medir voto: a pergunta secundária não pode ser respondida
- Item: P10 (também P04 e P06)
- Onde: protocolo.md → seção 1 (linha 47), tabela de desfechos (linha 72), C3 (linha 134), seção 9 (linha 298); 01-busca/strings/S-oa-en-v1.txt (bloco de desfecho); ancoras_desenvolvimento.csv → D14
- Evidência: "A exposição reduz a mobilização (comparecimento e interesse)?" (47); "não (extraído só quando relatado num estudo elegível)" (72); C3 exclui "Só comparecimento" (134); D14: "desfecho só comparecimento: provável inelegível (C3)"
- Por que importa: Os estudos sobre pesquisas e comparecimento (D14; exploracao_EX2.csv, linhas 30 e 77) ficam fora pelo C3, e as strings não têm termos de comparecimento. O corpo sobre o dano (E7) será só o subconjunto de estudos que também mediram voto, selecionado por um critério ligado ao desfecho. A resposta à pergunta secundária e o GRADE de `mobilizacao` na tabela de resumo ficariam enviesados: é a armadilha "danos nunca buscados", embora o dano esteja no DAG.
- Correção sugerida: Decisão humana entre (a) ampliar o C3 para "voto OU comparecimento/interesse" só na célula `mobilizacao`, com termos de comparecimento (turnout, participation; comparecimento, abstenção; participación, abstención) num fio próprio testado com `rs.py buscar openalex --query '<fio>' --contar`, ou (b) retirar a pergunta secundária e o desfecho da tabela de resumo, relatando `mobilizacao` como achado incidental em estudos de voto, com indireção declarada. Registrar a opção no protocolo antes do G2.

### R05 [ALTO] Filtros de idioma e de ano excluem sem amostra de elusão
- Item: P05
- Onde: protocolo.md → seção 4, funil formal (linhas 150-154)
- Evidência: "Filtro de idioma em modo excluir (fora de pt, en, es)... Nenhuma exclusão por dicionário: não é necessária amostra de elusão de filtro."
- Por que importa: A regra da skill vale para toda exclusão do funil formal, não só para dicionários ("exclusão só se descrita aqui, com amostra de elusão", 01-pergunta-protocolo.md, seção 10). O idioma do OpenAlex é detectado automaticamente e erra; os códigos de idioma do JSON do BDTD precisam casar com pt/en/es; o ano do OpenAlex pode ser o de uma versão preliminar. Com o A2, nenhum humano veria esses erros. Além disso, o recall das âncoras deve rodar com os filtros em `etiquetar` (02-busca.md, seção 3, passo 12), e `filtrar --ancoras` sai com código 2 se uma âncora for excluída por filtro; o protocolo não concilia as duas coisas.
- Correção sugerida: Manter a exclusão, mas prever amostra de elusão (`rs.py filtrar ... --amostra-elusao`, references/03-organizacao-triagem.md, seção 4): todos os registros excluídos por idioma (volume pequeno) e os de 2008-2009 excluídos por ano, lidos ao menos por subagente com trecho e relatados. Alternativa: passar o idioma para `etiquetar` e aplicá-lo na triagem. Declarar que o recall das âncoras é calculado com os filtros em `etiquetar`, antes da versão com exclusão.

### R06 [ALTO] Validação da busca por âncoras pouco informativa: provável sobreposição com o desenvolvimento e nenhuma âncora para B02-B04
- Item: P06
- Onde: protocolo.md → seção 3, validação da busca (linha 121); 01-busca/ancoras_desenvolvimento.csv (D01-D14); 01-busca/strings/desenvolvimento.csv (linhas 8-13)
- Evidência: âncoras de validação "a partir das listas de referências de Moy & Rinke (2012) e Barnfield (2019) e das citações para frente de Hardmeier (2008) e Barnfield (2019)" (121); desenvolvimento.csv: "sem âncoras PT", "sem âncoras ES", "sem âncoras BDTD"
- Por que importa: As 14 âncoras de desenvolvimento, usadas para afinar a B01 (13 de 14 recuperadas), são estudos de 2014 a 2026 do mesmo núcleo e plausivelmente citam Hardmeier (2008) ou são citadas por Barnfield (2019). Toda âncora presente nos dois arquivos é recuperada por construção e infla o recall (validação circular, 02-busca.md, seção 14), e o protocolo não tem regra para isso. As fontes das âncoras de validação são literatura internacional em inglês, então as estratégias em português, em espanhol e do BDTD, que sustentam a seção regional, provavelmente ficam sem âncora indexada, limite que não está declarado. O arquivo congela no G2. O revisor não abriu `ancoras_validacao.csv`: as duas situações precisam ser conferidas por script ou pelo subagente isolado.
- Correção sugerida: Antes do G2, o mesmo subagente isolado (nunca o coordenador) compara DOI e título normalizado dos dois arquivos, marca na coluna `observacao` as âncoras de validação que também são de desenvolvimento, e o recall passa a ser relatado com e sem elas. O mesmo subagente acrescenta âncoras elegíveis em português ou espanhol achadas por via independente das strings, com `indexada_em` (openalex|bdtd). Se não houver, declarar na seção 3 que B02-B04 ficam sem validação de recall.

### R07 [ALTO] Protocolo não diz como serão decididos os portões com limiares de validação humana
- Item: P17
- Onde: protocolo.md → seção 10, linha da triagem T/A (linha 317); seção 5 (linha 166); cabeçalho (linha 14)
- Evidência: "Limiares da skill não verificáveis sem humanos (recall de pelo menos 0,95 com limite inferior do IC de pelo menos 0,90; elusão; estabilidade): amostras preparadas e não calculadas"
- Por que importa: Sem `atalho_rapida`, o G4 segue a regra geral (tipos-de-revisao.md, seção 6, passo 5), com limiares que a skill chama de vinculantes (01-pergunta-protocolo.md, seção 10, passo 10). O protocolo não diz se o G4 será aprovado com desvio declarado, forçado ou adiado, nem que evidência substitui o recall; decidir isso depois de ver os dados é decisão *post hoc* sobre o próprio controle de qualidade. O mesmo vale para a verificação dos números de efeito (pendência `verificacao_humana_efeitos`).
- Correção sugerida: Escrever na seção 10 o plano: o G4 será aprovado pelo `revisor_humano_1` com o desvio A2 nos critérios (ex.: `"desvio": "A2: recall não calculado"`), apoiado em medidas calculáveis sem humano: concordância A × B, estabilidade na re-triagem de 10% e número de âncoras de desenvolvimento e de validação excluídas pela triagem de IA, contado por script sem que o coordenador leia títulos. Declarar que os produtos seguem marcados "RASCUNHO NÃO VALIDADO" até fechar `validacao_humana` e `verificacao_humana_efeitos`.

### R08 [MEDIO] Recorte de 2010 não coincide com o fim da cobertura de Hardmeier e subestima a lacuna
- Item: P04
- Onde: protocolo.md → [1b] (linha 15) e seção 4, características dos relatos (linha 141); pergunta.md → seção 4 (linha 79)
- Evidência: "O marco é o fim da cobertura da última síntese formal identificada (Hardmeier, 2008)... Limitação declarada: estudos publicados em 2008 e 2009 ficam fora" (141); Hardmeier: "Síntese com meta-análise de estudos até meados dos anos 2000" (pergunta.md:79)
- Por que importa: Se a cobertura de Hardmeier termina em meados dos anos 2000, a lacuna vai de lá até 2009, não só 2008-2009, e 2010 não é o fim da cobertura. A skill trata atualização como busca com sobreposição de datas; sem ela, "atualiza" (linha 15) e a limitação declarada ficam imprecisas.
- Correção sugerida: Conferir no capítulo o último ano de busca ou de estudo incluído. Decisão humana entre (a) limite inferior nesse ano, com sobreposição (e filtro do OpenAlex ajustado), ou (b) manter 2010 justificado só pelo marco do ambiente informacional, descrever a revisão como "evidência publicada desde 2010" e declarar a lacuna real.

### R09 [MEDIO] Fronteira ambígua entre "laboratório com preferências induzidas" e "grupo pequeno" no C1
- Item: P04
- Onde: protocolo.md → C1 (linha 132); codebook_elegibilidade.csv → `c1_populacao_contexto` (linha 4)
- Evidência: inclui "eleição real, hipotética ou de laboratório (inclusive com preferências induzidas)"; exclui "votações de júri, comitê, grupo pequeno ou legislativo"
- Por que importa: Experimentos eleitorais de laboratório com preferências induzidas costumam ser feitos em sessões de 10 a 20 participantes. Sem calibração humana (A2), triadores de IA podem aplicar "grupo pequeno" e excluí-los de forma inconsistente.
- Correção sugerida: Reescrever: "grupo pequeno" exclui só órgãos deliberativos reais (júri, comitê, conselho, legislativo); jogos eleitorais de laboratório com informação de pesquisa entram qualquer que seja o tamanho do grupo. Pôr um exemplo VÁLIDO e um INVÁLIDO no `ta_v1.md` e no prompt de `c1_populacao_contexto`.

### R10 [MEDIO] B01 sem sinônimos frequentes de desfecho e de "pesquisa"
- Item: P06
- Onde: 01-busca/strings/S-oa-en-v1.txt (bloco de desfecho do T2; bloco de pesquisa do T1); termos_v1.md (linhas 7 e 10)
- Evidência: ausência constatada de "party choice", "electoral choice", "voter preference(s)", "electoral support" e "party support" no T2, e de "survey" no T1
- Por que importa: Com o atalho A1, a sensibilidade da B01 sustenta a revisão. Teste do revisor na API do OpenAlex (19/09/2026, 2008+, `title_and_abstract`, sem importar): exposição do T2 AND esses desfechos, sem os desfechos atuais e sem bandwagon/underdog, dá 127 registros; ("pre-election survey" OR "preelection survey" OR "electoral survey" OR "opinion survey" OR "survey results") AND (bandwagon OR underdog), sem poll/polls/polling, dá 9. Nas duas amostras há ao menos um candidato plausível à triagem (títulos omitidos para preservar a independência das âncoras). Termos de proibição e projeção (poll ban, early call, network projection) acrescentaram 16 registros, nenhum pertinente, e não precisam entrar.
- Correção sugerida: Testar uma v2 com esses termos (`rs.py buscar openalex --query '<v2>' --contar` e `--busca-id EXn --listar 50`), registrar em `desenvolvimento.csv` e levar ao subagente do PRESS; se adotada, `S-oa-en-v2` no protocolo antes do G2.

### R11 [MEDIO] Pré-registros do OSF previstos como "pistas" sem método nem busca_id
- Item: P06
- Onde: protocolo.md → seção 1, tabela de revisões (linha 37) e tabela de fontes (linhas 87-93); pergunta.md → seção 4 (linha 85)
- Evidência: "Seguir; pré-registros são pistas para a busca, não revisões" (37)
- Por que importa: Estudo achado por essas pistas entraria fora do ledger (PRISMA sem lastro, 02-busca.md, seção 14) ou não entraria; a fonte está prevista no texto, mas sem `busca_id`, data e forma de execução.
- Correção sugerida: Criar `MN1` (lista manual dos relatos resultantes dos pré-registros achados, com data, importada por `rs.py importar --arquivo <lista> --fonte generico --busca-id MN1 --executada-em AAAA-MM-DD`), o que amplia o A1 e exige decisão humana; ou retirar a frase e usar os pré-registros só na avaliação de relato seletivo.

### R12 [MEDIO] Checagem de revisões existentes leu cerca de 10% dos registros recuperados
- Item: P03
- Onde: pergunta.md → seção 4 (linhas 69-72); exploracao_EX1.csv (50 registros); exploracao_EX2.csv (80 registros)
- Evidência: "`EX1`... `n_api` = 427; muito ruidoso; `EX2`: só no título; `n_api` = 787"
- Por que importa: A conclusão "não há RS recente" apoia-se nos 50 e 80 primeiros por relevância, e a lista EX1 é quase toda de revisões de saúde, sem utilidade. Uma meta-análise recente mais abaixo nas listas mudaria a decisão de atualizar.
- Correção sugerida: Rodar consultas específicas e ler todos os resultados, por exemplo `rs.py buscar openalex --busca-id EX3 --query '(bandwagon OR underdog OR "poll effects" OR "published polls") AND (poll OR polls OR polling OR election)' --filtro 'type:review' --contar` e depois `--listar`, e outra com ("meta-analysis" OR "systematic review" OR "literature review") AND (bandwagon OR underdog OR poll OR polls) com `--campo title`; registrar data e resultado em pergunta.md.

### R13 [MEDIO] Registro no OSF opcional e sem prazo antes da busca definitiva
- Item: P03
- Onde: protocolo.md → [2] (linha 17)
- Evidência: "sem registro prévio no momento do G2... a submissão é opcional e cabe ao usuário"
- Por que importa: Numa revisão em que triagem, extração, risco de viés e certeza ficam com IA sem validação, o protocolo público e datado é a principal salvaguarda contra mudanças *post hoc*; registro feito depois da busca não é pré-registro (01-pergunta-protocolo.md, seção 12).
- Correção sugerida: Decidir no G2 registrar no OSF (Generalized Systematic Review Registration) antes de executar B01-B04, isto é, antes do G3, e anotar DOI e data em `emendas.md`; se não registrar, dizer no protocolo que a revisão não será registrada.

### R14 [MEDIO] "Estudo" não definido para artigos com vários experimentos independentes
- Item: P07
- Onde: protocolo.md → seção 6, unidade de análise (linha 195); seção 8, agregação (linha 244); ancoras_desenvolvimento.csv → D07
- Evidência: "Unidade de análise: estudo (`id_estudo`), relato (`id_rs`), efeito (`id_efeito`)"; D07: "painel e experimentos; Polônia"
- Por que importa: Nesta literatura, um artigo relata com frequência vários experimentos com amostras, países ou eleições distintas. Contar o artigo ou cada experimento como estudo muda k, os limiares (k ≥ 3, ≥ 4 por nível, ≥ 10) e a estrutura de dependência.
- Correção sugerida: Definir estudo como amostra independente (experimento com participantes próprios ou eleição distinta), com regra de identificador (ex.: `<id_rs>_e1`, `<id_rs>_e2`) e sensibilidade com o artigo como conglomerado no RVE.

### R15 [MEDIO] Resultados em risco crítico na análise principal
- Item: P08
- Onde: protocolo.md → seção 8, [15c] (linha 269)
- Evidência: "Risco crítico: resultados em risco crítico ficam na análise principal, com sensibilidade sem eles."
- Por que importa: O ROBINS-I define risco crítico como estudo problemático demais para dar evidência útil sobre o efeito; mantê-lo na estimativa principal deixa esses resultados moverem o número central. A regra da skill de não excluir automaticamente se cumpre mantendo-os na revisão e na sensibilidade, sem pô-los na análise principal.
- Correção sugerida: Inverter: análise principal sem resultados em risco crítico e sensibilidade com eles; ou justificar no protocolo a escolha atual.

### R16 [MEDIO] Moderadores e mediador da teoria sem variável no codebook
- Item: P09
- Onde: teoria_programa.md → tabela Z (linhas 53 e 56) e papéis das variáveis (linha 43); protocolo.md → seção 6 (linha 202); codebook_v0_efetividade.csv
- Evidência: "Maior com pluralidade e três ou mais competidores" (53); "Maior perto do dia da eleição" (56); "O modelo ajusta pela expectativa? (efeito direto × total)" (43)
- Por que importa: A skill exige variável para cada moderador, mecanismo e dano da teoria. Não há variável para número de competidores (`sistema_eleitoral` não basta), para o momento da exposição (só texto livre em `intervencao_descricao`) nem para o ajuste pelo mediador; a regra "efeito direto nunca é agregado com efeito total" (linha 202) fica sem campo que a aplique.
- Correção sugerida: Acrescentar ao codebook v0, antes do G2, `n_competidores` (numerica_int), `dias_ate_eleicao` (numerica_int, 999 se ausente) e `ajuste_mediador` (categorica: sim | nao | 999; sim quando o modelo principal condiciona na expectativa de vitória).

### R17 [MEDIO] Leitura de g próximo de zero pré-autoriza a hipótese de efeitos que se anulam
- Item: P11
- Onde: protocolo.md → seção 8, [15d] (linha 282)
- Evidência: "Um g próximo de zero é lido à luz da teoria rival de efeitos opostos que se anulam."
- Por que importa: Sem condição de evidência, qualquer média nula vira "efeitos ocultos", conclusão impossível de refutar. A teoria rival só é testável com estimativas por subgrupo (apoiadores do líder, do azarão, indecisos), que o protocolo já manda extrair.
- Correção sugerida: Reescrever: g próximo de zero é classificado pelo IC frente a ±δ; a anulação só é afirmada quando houver estimativas por subgrupo com sinais opostos num número mínimo de estudos fixado no protocolo; sem isso, é relatada como hipótese não testada.

### R18 [MEDIO] GRADE com ponto de partida alto para corpo avaliado por EPOC
- Item: P15
- Onde: protocolo.md → seção 9 (linha 299); seção 7, tabela de ferramentas (linha 218)
- Evidência: "Corpo não randomizado avaliado com ferramentas diferentes (ROBINS-I V2 e EPOC na mesma célula): ponto de partida único alto, com rebaixamento por risco de viés"
- Por que importa: O GRADE admite ponto de partida alto para estudos não randomizados quando o risco de viés é avaliado com ROBINS-I, que examina confundimento e seleção contra um ensaio-alvo. Os critérios EPOC para série interrompida e antes e depois controlado não fazem isso com a mesma profundidade, e começar alto pode superestimar a certeza das células agregadas (proibições, embargos).
- Correção sugerida: Avaliar também com ROBINS-I V2 os estudos agregados de diferenças em diferenças, controle sintético e série interrompida (EPOC como complemento), ou começar em baixa os corpos avaliados só por EPOC, com justificativa por célula.

### R19 [MEDIO] Papel do árbitro contradiz a regra liberal; origem dos exemplos do prompt não definida
- Item: P17
- Onde: protocolo.md → seção 5, [11b] e calibração (linhas 160-166)
- Evidência: "árbitro cego num terceiro modelo nas divergências; regra de consolidação liberal (qualquer inclusão ou incerto segue ao texto completo)"
- Por que importa: Se o árbitro pode derrubar o "incluir" de A ou de B, a regra liberal, única salvaguarda de uma triagem sem validação, deixa de valer e a IA exclui sozinha registros que um modelo incluiu; se não pode, o árbitro não tem função. Sem calibração humana, o protocolo não diz de onde saem os exemplos VÁLIDO/INVÁLIDO do `ta_v1.md`; se vierem de registros que depois caírem na amostra de validação, ela fica contaminada.
- Correção sugerida: Escrever que toda divergência com um "incluir" ou "incerto" segue ao texto completo e em que casos o árbitro decide (ou se só é registrado para relato). Fixar que os exemplos saem de D01-D14 e das listas EX1/EX2, nunca de registros da amostra de validação ou de elusão.

### R20 [MEDIO] Dispensa de contato com autores atribuída ao A2, que não a inclui
- Item: P18
- Onde: protocolo.md → seção 6 (linha 188); pergunta.md → seção 6, atalhos aprovados no G1 (linha 110)
- Evidência: "Contato com autores: não haverá (atalho A2; revisor humano único)"
- Por que importa: O A2 aprovado no G1 trata de triagem, elegibilidade, extração, risco de viés e certeza por IA. Dispensar o contato com autores para dados faltantes é outro atalho, não aprovado no G1, e aumenta a perda de efeitos (estudos só na síntese por direção).
- Correção sugerida: Declarar como atalho A5 na lista do cabeçalho, com a consequência, e pedir aprovação explícita no G2; ou prever contato mínimo (e-mail redigido pela IA e enviado pelo humano, 2 tentativas, prazo de 14 dias, registro em planilha).

### R21 [MEDIO] Sem avaliação de viés por evidência faltante (ROB-ME)
- Item: P18
- Onde: protocolo.md → seção 7, [16] (linha 223)
- Evidência: "viés de publicação (funil, Egger e PET-PEESE com erro-padrão modificado, e seleção 3PSM) só em células com k igual ou maior que 10"
- Por que importa: Com k provavelmente abaixo de 10 na maioria das células, os testes de funil não rodam; uma base bibliográfica só, sem cinzenta nem contato com autores, aumenta o risco de resultados faltantes. Sem ROB-ME, o domínio de viés de publicação do GRADE fica sem juízo estruturado.
- Correção sugerida: Acrescentar ROB-ME por síntese (célula), usando os pré-registros (`registro_financiamento`) e os desfechos medidos mas não relatados, para alimentar o GRADE.

### R22 [BAIXO] Traduções não equivalentes, PRESS depois da tradução e ruído previsível
- Item: P06
- Onde: 01-busca/strings/S-bdtd-v1.txt; S-oa-pt-v1.txt; S-oa-en-v1.txt; protocolo.md → seção 3, validação (linha 120)
- Evidência: S-bdtd-v1 não tem "pesquisa(s) pré-eleitoral(is)" nem "divulgação de pesquisas", presentes em S-oa-pt-v1; PRESS "da estratégia B01 antes da execução definitiva"
- Por que importa: A skill pede o PRESS da base principal antes de traduzir; se o PRESS mudar a B01, B02-B04 ficam desalinhadas. "election forecast" AND "vote share" traz a literatura de modelos de previsão e de precisão, excluída pelo C2.
- Correção sugerida: Depois do PRESS, revisar B02-B04 a partir da mesma tabela de termos, completar a S-bdtd e registrar o ruído esperado em `desenvolvimento.csv`.

### R23 [BAIXO] Exemplos herdados do modelo nos prompts dos codebooks
- Item: P09
- Onde: codebook_v0_efetividade.csv → `populacao` (linha 10), `b2_nivel_atribuicao_cluster` (linha 32), `b2_modelo_principal` (linha 37); codebook_elegibilidade.csv → `fonte_dados_amostra` (linha 11)
- Evidência: "(indivíduo, turma, escola, município)"; "(ex.: 'desempenho: Tabela 3, col. 4')"; "(ex.: registros administrativos de 2010 a 2018, 5.570 municípios)"
- Por que importa: Exemplos de outra área confundem subagentes extratores que trabalham sem supervisão humana.
- Correção sugerida: Trocar por exemplos desta literatura (sessão de laboratório, painel, seção eleitoral; "apoio_ao_lider: Tabela 2, col. 3").

### R24 [BAIXO] DAG sem o confundidor `preferencia_previa` descrito na teoria
- Item: P02
- Onde: teoria_programa.md → papéis das variáveis (linhas 41-42); dag_v1.mmd
- Evidência: "`preferencia_previa` / partidarismo | Confundidor em painéis; moderador em experimentos | → exposição seletiva; → apoio" (41); nó ausente em dag_v1.mmd
- Por que importa: Os domínios de confundimento do ROBINS-I nos painéis saem do DAG, e figura e teoria precisam coincidir. A teoria também diz "← exposição (via interesse)" para `resposta_ao_survey`, e o DAG desenha seta direta.
- Correção sugerida: Acrescentar `PP[preferencia_previa] --> X` e `PP --> Y1` ao diagrama e à lista de arestas declaradas; alinhar o texto sobre `resposta_ao_survey`.

### R25 [BAIXO] Checagem de retratação sem conferência dos textos sem DOI
- Item: P18
- Onde: protocolo.md → C6 (linha 137); codebook_elegibilidade.csv → `c6_nao_retratado` (linha 9)
- Evidência: "checado no texto completo, no OpenAlex e na Crossref"; prompt: "aplicada na conferência humana"
- Por que importa: Teses do BDTD e trabalhos sem DOI (ex.: D13) escapam às consultas por DOI; e, com o A2, não há conferência humana para a maioria dos registros.
- Correção sugerida: Dizer que os registros sem DOI são conferidos na página da editora ou do repositório pelo coordenador, com registro, e quem aplica a checagem externa sob o A2.

### R26 [BAIXO] Volume esperado já passa da capacidade declarada
- Item: P17
- Onde: pergunta.md → seção 5 (linha 105); protocolo.md → seção 3 (linha 116) e seção 9, contingências (linha 306)
- Evidência: "volume compatível com triagem dupla por subagentes (abaixo de ~800 registros)"; contagens "B01 = 734, B02 = 286, B03 = 131; B04 = 80"
- Por que importa: São cerca de 1.231 registros antes da deduplicação: a contingência de mais ondas já está acionada, e a ficha da pergunta diz o contrário.
- Correção sugerida: Atualizar a leitura das contagens na seção 3 e prever as ondas, com concordância e estabilidade relatadas por onda.

### R27 [BAIXO] Título sem "revisão rápida" e público do debate sem produto
- Item: P19 (também P01)
- Onde: protocolo.md → título (linha 1); seção 1 (linha 30); seção 11 (linha 328)
- Evidência: "# Protocolo de revisão sistemática: exposição a pesquisas eleitorais..."; "Os usuários são pesquisadores e participantes do debate público"
- Por que importa: O formato da skill para a variante é "[Tema]: revisão rápida (tipo de origem no subtítulo)"; o único produto é o manuscrito, embora o público do debate regulatório seja usuário declarado.
- Correção sugerida: Ajustar o título ao da ficha da pergunta; declarar o público do manuscrito e se haverá produto para o debate público (marcado "RASCUNHO NÃO VALIDADO" enquanto houver pendência).

## Cobertura
| Item | Situação | Observação |
|---|---|---|
| P01 | ok | `efetividade_swim` está na matriz e responde a pergunta de efeito com comparabilidade incerta; atalhos A1-A4 declarados na seção que alteram; título em R27 |
| P02 | problema R24 | X, Y, M, Z e PECO completos; tabela por elo com efeitos não intencionais e incentivos perversos (E7, E8); arestas do DAG conferidas contra a lista declarada (coincidem) |
| P03 | problema R12, R13 | OpenAlex, OSF Registries e BDTD checados com data; decisão de atualizar justificada |
| P04 | problema R08, R09 (R04 afeta o C3) | IDs C1-C6 iguais no protocolo e no codebook de elegibilidade; `02-triagem/prompts/ta_vN.md` ainda não existe (conferir no G4); nenhum critério depende de resultado ou de dado numérico |
| P05 | problema R05 | Registro sem resumo nunca excluído; tipo de documento e dicionário de método só etiquetam |
| P06 | problema R06, R10, R11, R22 | Blocos PT/EN/ES, sintaxe por base, BDTD, bola de neve com a mesma versão dos critérios, PRESS por subagente (A4), regra de substituição e log PRISMA-S previstos; `ancoras_validacao.csv` existe (ls), conteúdo e `indexada_em` não conferidos por regra |
| P07 | problema R14 | Hierarquia estudo > relato > efeito e ligação de relatos previstas; revisões só como sementes e âncoras (C5) |
| P08 | problema R15 | Ferramenta por desenho (RoB 2, variante por conglomerado, ROBINS-I V2, EPOC); Maryland fora da qualidade; uso em sensibilidade e GRADE, sem exclusão automática |
| P09 | problema R16, R23 | Bloco comum + b2; piloto de 2 a 3 estudos; recodificação cega em max(20%, 10) com κ/PABAK ≥ 0,7 e ≥ 80%; verificação humana dos números cortada por A2 (declarado, pendência) |
| P10 | problema R01, R04 | Direção pelo estimador, significância em variável separada e regra de modelo principal fixadas |
| P11 | problema R02, R17 | REML + Hartung-Knapp, τ² com IC, I², PI, CHE + RVE com gl ≥ 4, limiares de k, leave-one-out, sensibilidades e contingência previstos |
| P12 | problema R03 | δ e faixas fixados a priori, declarados como convenção, com conversão escrita |
| P13 | não se aplica | Testes combinados não previstos, com motivo registrado na [15d] |
| P14 | não se aplica | Revisão só de efeito; mecanismos em síntese narrativa estruturada |
| P15 | problema R18 | GRADE por célula com indireção por contexto, realismo e estimando; Murad 2017; CERQual não se aplica; sem segunda pessoa (A2 declarado, pendência `certeza_humana`) |
| P16 | não se aplica | Caixa de ferramentas opcional em `efetividade_swim`, dispensa declarada na seção 8 |
| P17 | problema R07, R19, R26 | Prompts com sha256, árbitro de terceiro modelo do mesmo provedor (declarado), estabilidade em 10%, "aguardando classificação" previsto; calibração, validação e elusão humanas cortadas por A2 (declarado) |
| P18 | problema R20, R21, R25 | Conglomerados (ICC), PROGRESS-Plus, 4 fatores de transferibilidade, log de emendas e pacote aberto (item 27) previstos |
| P19 | problema R27 | PRISMA 2020, PRISMA-S, SWiM e PRISMA-trAIce previstos |

## Pontos que exigem decisão humana
- Desmobilização (R04): ampliar o C3 só para a célula `mobilizacao`, com fio de busca próprio, ou retirar a pergunta secundária e o desfecho da tabela de resumo.
- Recorte (R08): manter 2010 com a lacuna real declarada, ou fixar o limite no fim da cobertura de Hardmeier (2008), com sobreposição.
- Mitigação do A2 onde é barata: verificação humana de 100% dos números de efeito e do alinhamento de sinal dos estudos incluídos (provavelmente algumas dezenas), já que a pergunta principal é a direção; ou o caminho `atalho_rapida` no G4 (dupla humana em ≥ 20% e segunda leitura dos excluídos). Mudar atalho exige novo G1.
- Idiomas: a justificativa "capacidade de leitura do revisor humano" pesa pouco quando a IA lê os textos (A2); decidir se admite alemão e francês (parte desta literatura vem de eleições alemãs) ou mantém pt/en/es como limitação.
- Contato com autores (R20): aprovar como atalho A5 ou adotar plano mínimo.
- Registro no OSF antes do G3 (R13).
- Fonte `MN1` para os relatos dos pré-registros do OSF (R11), que amplia o A1.
- Resultados em risco crítico dentro ou fora da análise principal (R15).
