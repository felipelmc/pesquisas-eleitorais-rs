# Revisão metodológica — G8

Tipo de revisão: efetividade_swim, variante rápida (sem caixa de ferramentas OQF, decisão do protocolo). Arquivos lidos: 32 de 32 (mais o protocolo). Itens verificados: 16; não aplicáveis: 4.
Resumo: CRITICO 2 · ALTO 6 · MEDIO 9 · BAIXO 2

## Problemas

### R01 [CRITICO] SWiM e GRADE agrupados só por construto × celula_alvo, misturando famílias e comparadores que o protocolo separa
- Item: S01 (também S15, S20)
- Onde: 06-analise/swim_principais/swim_resumo.json → parametros.grupo; grupos "apoio_ao_lider | principal | nao_randomizado", "mobilizacao | mobilizacao | randomizado" e "mobilizacao | mobilizacao | nao_randomizado" (sem chave familia_intervencao); 06-analise/certeza.csv linhas 3 a 7 (familia_intervencao = todas); protocolo.md linhas 259 e 308; emendas.md linha 76
- Evidência: swim_resumo.json: "grupo": ["construto_outcome", "celula_alvo"]. Protocolo: "Célula = família × construto × comparador × classe de desenho" e "SWiM: agrupamento como acima". Emenda 1: "entra em célula própria no SWiM"
- Por que importa: o teste de sinal do grupo não randomizado de apoio_ao_lider soma boca de urna (Chatterjee2019a, Morton2015a), apuração parcial (Araujo2021a, que a Emenda 1 manda para célula própria) e pesquisa pré-eleitoral; o randomizado soma comparadores sem_pesquisa, outro e mesmo_candidato_atras, que a tabela 15a manda "sempre" separar; os grupos de mobilização somam agregador_projecao com pesquisa e boca de urna com pesquisa. Nenhuma célula do protocolo (família × construto × comparador × classe) tem síntese por direção nem juízo GRADE próprio, e a tabela de resumo prevista na seção 9 ("apoio_ao_lider por formato de exposição, comparador e classe de desenho") não existe. A própria justificativa GRADE da linha 3 admite a mistura de três famílias.
- Correção sugerida: refazer a SWiM com o agrupamento do protocolo (`rs.py analise swim --grupo familia_intervencao,construto_outcome,comparador_tipo,celula_alvo --separar-desenho sim --excluir-rob critico`, com os parâmetros de swim_resumo.json) e o GRADE por essas células; o agrupamento amplo atual pode ficar só como análise descritiva ou de sensibilidade. Se o humano quiser manter células agregadas, registrar emenda tipo C (decidida depois de ver dados) com a justificativa, e manter Araujo2021a em célula própria com a sensibilidade exigida pela Emenda 1.

### R02 [CRITICO] Convenção de sinal incoerente: estudos com o mesmo tipo de alvo ou a mesma evidência substantiva codificados em direções opostas
- Item: S05 (também S09, S13)
- Onde: 06-analise/swim_principais.csv → colunas direcao_desejada, alvo_efeito, or_, yi das linhas Cornejo2023a-E05, Meer2015a-E01, Freden2024a-E01/E04/E07, Lago2015-E01, Bursztyn2023a-E01, Alabrese2024a-E002, Morton2015a-E41; certeza.csv linhas 4 e 6
- Evidência: Cornejo2023a-E05: segundo_viavel, reduzir, OR 1,419, yi −0,193 ("danoso"); Meer2015a-E01: segundo_viavel, aumentar, OR 1,259, yi +0,127 ("benefico"). Morton2015a-E41: evidencia "Difference δ −5.22", beta 5.22, sem aviso
- Por que importa: (a) na célula de viabilidade, a certeza.csv define positivo como "apoio à opção viável", mas Cornejo2023a (apoio ao candidato anti-PRI viável aumenta, OR > 1) entra como contrário porque herdou `reduzir` da harmonização de polaridade para azarão (notas_extracao_completa.md, "Harmonização de polaridade aplicada"), antes de o alvo virar segundo_viavel; Freden2024a (partido abaixo da cláusula perdendo apoio) está com `aumentar`, enquanto Lago2015 (terceiro inviável) usa `reduzir`. Com convenção única, a célula randomizada de viabilidade passa de "1 a favor, 1 contra, 1 misto" para 2 a favor e Freden2024a com 2 de 3 na direção de viabilidade, e o juízo de inconsistência da linha 6 da certeza.csv ("sinais que não convergem") cai. (b) Na mobilização não randomizada, Bursztyn2023a-E01 (interação dia após a pesquisa × proximidade: pesquisa de disputa apertada aumenta o comparecimento) e Alabrese2024a-E002 (interação margem nacional × segurança local: margem maior reduz o comparecimento) dizem a mesma coisa substantiva (pesquisa de disputa folgada desmobiliza), mas entram um como mobilização e outro como desmobilização, só pela escala do moderador. (c) Morton2015a-E41 tem sinal invertido em relação ao impresso sem registro do motivo (ao contrário de Chatterjee2019a, documentado nas notas), e é esse sinal que põe Morton2015a como "benefico".
- Correção sugerida: fixar e registrar uma convenção por celula_alvo (viabilidade: positivo = mais apoio à opção mostrada como viável ou menos apoio à mostrada como inviável; para exposições contínuas: sinal da exposição a pesquisa que mostra disputa folgada, ou retirar da contagem, ver R03); corrigir direcao_desejada de Cornejo2023a (E05 a E18) e Freden2024a; documentar ou reverter a inversão de Morton2015a-E41 com trecho; rodar de novo `rs.py analise verificar-efeitos`, o preparo e a SWiM, e refazer as linhas 4 e 6 da certeza.csv.

### R03 [ALTO] Efeitos que não estimam o contraste da exposição contam como voto de direção nas células principais
- Item: S01 (também S05, S13)
- Onde: 06-analise/swim_principais/tabelas/swim_direcao.csv e swim_principais.csv, linhas Lammers2022a-E01/E03, Gandhi2019-E01/E03, Fichnova2015a-E01/E05, Klor2017a-E01, Urminsky2019-E01, Bursztyn2023a-E01/E17, Alabrese2024a-E002/E129; 05-decomposicao/notas_extracao_completa.md linhas 24 a 36 e 118 a 121; certeza.csv linhas 2 e 4
- Evidência: notas: "os `d` extraídos ... medem ... o efeito do modo de raciocínio sob exposição, não o efeito da exposição em si" e "considerar excluir Lammers2022a". Gandhi2019-E01 modelo: "coeficiente da interação tripla DAP Treatment × Time × BERSATU Supporter"
- Por que importa: Lammers2022a (efeito do modo de raciocínio), Gandhi2019 (interação tripla, diferença de efeito entre apoiadores; é o único voto contrário na célula randomizada), Fichnova2015a (R de Spearman entre o ranking da pesquisa forjada e o dos respondentes, sem grupo de comparação), Klor2017a-E01 (coeficiente de pertencer ao time maior sobre a decisão de votar, isto é, comparecimento dentro da condição informada) e Urminsky2019 (formatos da mesma previsão; as notas mandam célula própria) não comparam exposição com não exposição ou com outro resultado. Bursztyn2023a e Alabrese2024a entram por termos de interação cujo sinal não é o efeito da exposição (R02). A certeza.csv reconhece Lammers2022a como indireto, mas o mantém na contagem e na lista de estudos. Sem Lammers2022a, Gandhi2019, Fichnova2015a e Klor2017a, a célula randomizada de apoio_ao_lider fica em 8 de 8 (a direção se mantém, mas a composição e a justificativa mudam); sem Urminsky2019 (e sem Klor2017a, ver R05), a mobilização randomizada fica em 3 contra 2.
- Correção sugerida: marcar esses efeitos como fora da contagem principal (ou `modelo_principal = nao` com motivo) e levá-los para a síntese narrativa de mecanismos e moderadores; rodar de novo a SWiM e reescrever as listas de estudos e as justificativas da certeza.csv. Decisão humana de exclusão (ver lista abaixo).

### R04 [ALTO] Análise principal inclui resultados em risco crítico, ao contrário do protocolo
- Item: S07 (também S20)
- Onde: 06-analise/swim_principais/swim_resumo.json → parametros.excluir_rob = "nenhum"; meta_principal/meta_resumo.json → parametros.excluir_rob = "nenhum"; swim_sens_sem_critico/swim_resumo.json; protocolo.md linha 268
- Evidência: protocolo: "a análise principal exclui resultados em risco crítico (`--excluir-rob critico`), que ficam na revisão e entram numa análise de sensibilidade com eles". SWiM principal com Unkelbach2022a, Gasperoni2015a e Kaplan2019a (todos `critico`)
- Por que importa: a ordem está invertida: a "principal" contém os críticos e a sensibilidade os retira. Na célula não randomizada de apoio_ao_lider, a contagem conforme ao protocolo é 4 de 7 (p = 1,00), não 5 de 8, e é a de 5 de 8 que abre a justificativa da linha 3 da certeza.csv. A meta-análise não tinha linhas críticas, mas foi rodada sem o parâmetro do protocolo.
- Correção sugerida: tratar `swim_sens_sem_critico` como principal (ou rodar de novo a SWiM e a meta com `--excluir-rob critico`) e a atual como sensibilidade "com críticos"; atualizar os números citados na certeza.csv.

### R05 [ALTO] Contrastes antes e depois dentro do sujeito, avaliados com ROBINS-I, entram na classe randomizada
- Item: S02 (também S13)
- Onde: 06-analise/efeitos.csv → desenho de Klor2017a-E06 e Kaplan2019a-E01; swim_principais/tabelas/swim_direcao.csv grupo "mobilizacao | mobilizacao | randomizado"; 04-qualidade/rob_geral.csv (Klor2017a mobilizacao = robins_i, moderado; Kaplan2019a = robins_i, critico); certeza.csv linha 4
- Evidência: Klor2017a-E06: "RCT (experimento de laboratório; comparação intraindividual antes/depois da revelação da distribuição)"; Kaplan2019a-E01: "medida antes-depois intra-sujeito, sem braço sem prognóstico"
- Por que importa: a classe foi deduzida da palavra "RCT" no campo `desenho`, mas o contraste extraído não é randomizado (por isso a ferramenta escolhida foi ROBINS-I). O protocolo proíbe juntar randomizados e não randomizados; Klor2017a conta como voto de mobilização na célula randomizada (4 contra 3; sem ele, 3 contra 3) e a GRADE lhe dá ponto de partida alto. Gasperoni2015a, com desenho análogo, foi corretamente para não randomizado.
- Correção sugerida: reescrever o `desenho` dessas linhas sem "randomizado" (como em Gasperoni2015a), rodar de novo o preparo e a SWiM, e mover os estudos para a linha não randomizada da certeza.csv.

### R06 [ALTO] δ não calculado pela regra do protocolo e imprecisão da célula principal não julgada frente a δ
- Item: S13 (também S06)
- Onde: meta_principal/meta_resumo.json → parametros.delta = 0.044, delta_fonte = "argumento (confirmar no protocolo)"; certeza.csv linha 2 (coluna justificativa, domínio Imprecisão); protocolo.md linhas 297 e 323
- Evidência: protocolo: "convertidos para g com a proporção de referência de cada célula, isto é, a mediana dos `p0`" e "A imprecisão é julgada frente a δ". certeza.csv: "Imprecisão: não rebaixada para a direção"
- Por que importa: na única célula agregada (p0 = 0,74, 0,40 e 0,88; mediana 0,74), 2 p.p. correspondem a g ≈ 0,059, não 0,044; o δ de referência 0,50 só vale para células mistas ou sem p0. Na certeza, a linha 2 não rebaixa a imprecisão porque qualifica "a direção", embora o protocolo mande julgar frente a δ e a meta tenha IC de −1,72 a 2,53 (ou −0,69 a 1,49 no modelo sem RVE), que cruza ±δ com folga; com o rebaixamento previsto, a certeza cairia para muito baixa. A escolha de qualificar só a direção (Murad) é defensável para células só com SWiM, mas precisa ser declarada como desvio onde há meta-análise.
- Correção sugerida: calcular δ por célula com a mediana dos p0 e registrar antes da interpretação; rodar de novo `rs.py analise meta ... --delta <δ da célula>`; julgar a imprecisão da linha 2 frente a δ ou registrar em emenda que a certeza qualifica só a direção, e deixar a decisão ao humano.

### R07 [ALTO] Entrada da única meta-análise contraria as notas de extração e a Emenda 4c
- Item: S05 (também S04)
- Onde: 06-analise/efeitos_meta_principal.csv → linhas Tyszler2015-E01 (n1 = n2 = 6, aproximado = 0) e Timotei2013a-E01 (cluster e icc vazios); notas_extracao_completa.md linhas 104 a 109; 04-qualidade/notas_rob.md ("Timotei2013a (RoB 2) = cluster")
- Evidência: notas: "Conferência visual humana obrigatória; sem EP nem teste — entra na síntese narrativa (SWiM), não na meta-análise". notas_rob: "Timotei2013a (RoB 2) = cluster: a exposição é entregue a grupos de 20"
- Por que importa: Tyszler2015 entrou na meta de k = 3 com proporções lidas de gráfico e sem marca de aproximado (Brugarolas2021, em situação igual, foi para a sensibilidade); com ele fora, a célula não atinge k = 3 e não haveria meta-análise. Timotei2013a é experimento por conglomerado segundo a própria avaliação de risco de viés, mas a variância não recebeu o efeito de desenho da Emenda 4c (1 + 19 × 0,05 ≈ 1,95), o que lhe dá peso excessivo. Em Boukouras2020a a unidade é a rodada, mas m = 15 é o número de sujeitos por sessão; a Emenda 4c manda usar a unidade da estimativa (conferir).
- Correção sugerida: tirar Tyszler2015-E01 da meta (ou marcar `aproximado = 1` e decidir em emenda), preencher `cluster = 20` e `icc = 0.05` em Timotei2013a, conferir m de Boukouras2020a, rodar de novo efeitos, meta e sensibilidades; se k < 3, a célula passa para SWiM, como prevê a contingência do protocolo.

### R08 [ALTO] Sensibilidades obrigatórias do protocolo não executadas nem declaradas
- Item: S07
- Onde: 06-analise (não há produto); protocolo.md linhas 285 a 293; emendas.md linha 76; efeitos.csv → ano_eleicao_pre2010 de Morton2015a e Chatterjee2019a
- Evidência: ausência constatada em 06-analise de "sem contextos induzidos", "sem estudos de dados anteriores a 2010", "artigo como conglomerado no RVE" e da sensibilidade sem Araujo2021a pedida na Emenda 1 ("A sensibilidade sem ele deve ser reportada")
- Por que importa: na célula randomizada de apoio_ao_lider, só Farjam2020a (a favor) e Gandhi2019 (contra, ver R03) têm `realismo_contexto = real`; a direção *bandwagon* vem inteira de laboratório induzido e vinheta hipotética, o que a sensibilidade "sem contextos induzidos" mostraria e o GRADE rebaixa só um nível. Morton2015a (eleições desde 1981, reforma de 2005) e Chatterjee2019a (exposição anterior à proibição de 2010) têm `ano_eleicao_pre2010 = nao`, embora a exposição seja de dados anteriores a 2010, o que invalida a futura sensibilidade por ano.
- Correção sugerida: rodar a SWiM (e a meta, onde k permitir) sem `realismo_contexto` induzido e hipotético, sem dados anteriores a 2010 (depois de recodificar Morton2015a e Chatterjee2019a) e sem Araujo2021a; declarar como não executável o que não tiver k; citar os resultados na certeza.csv.

### R09 [MEDIO] Efeitos com IC inteiro dentro de ±δ contados como direção
- Item: S09
- Onde: efeitos_meta_principal.csv → Gerber2020a-E31 (yi 0,0078; vi 3,1e-05) e Bursztyn2023a-E17 (yi −0,0035; vi 1,4e-06); swim_direcao.csv; protocolo.md linha 309
- Evidência: protocolo: "Um g próximo de zero é classificado pelo IC frente a ±δ". swim_resumo.json: n_nulos = 0 em todos os grupos
- Por que importa: Gerber2020a (IC ≈ −0,003 a 0,019) e Bursztyn2023a-E17 (IC ≈ −0,006 a −0,001) ficam dentro de ±δ e deveriam ser classificados como trivial ou nulo, mas entram como mobilização e como *underdog*. O maior estudo da mobilização randomizada (cerca de 126 mil pessoas) passa a ser um voto a favor.
- Correção sugerida: aplicar a classificação por ±δ antes do teste de sinal (ou relatá-la ao lado) e ajustar as contagens da certeza.csv.

### R10 [MEDIO] g acima de 2 não conferidos e usados como argumento na certeza
- Item: S05
- Onde: efeitos.csv → Fichnova2015a-E01/E05 (yi 3,67 e 7,10, formula r_d_n_total, n_total = 7), Alabrese2024a-E002 (yi −2,14), Geers2018-E01 (beta −30,835); certeza.csv linha 2
- Evidência: aviso: "|g| > 2: conferir extração"; certeza.csv: "Fichnova2015a n = 7" e "efeitos positivos e grandes (Fichnova2015a, g de 3,7 e 7,1)"
- Por que importa: em Fichnova2015a, R de Spearman entre dois rankings de 7 candidatos foi convertido como correlação ponto-bisserial com n = 7 (os respondentes são 37 e 42): o g não tem sentido, e a certeza o cita como indício de viés de publicação e como tamanho de amostra. Geers2018, que as notas mandam conferir por humano, dá a direção de desmobilização por um β implausível. `verificado_humano` está vazio nas 554 linhas.
- Correção sugerida: anular o g de Fichnova2015a (só direção, ou fora; ver R03), corrigir n_amostra, conferir Alabrese2024a e Geers2018 na página e tirar esses números da justificativa GRADE.

### R11 [MEDIO] Modelo e estatísticas da meta-análise mal lidos para k = 3
- Item: S04 (também S06, S08)
- Onde: meta_principal/meta_resumo.json → grupos[8].resultado (gl 1,23; rve_confiavel false; tau2_dentro_estudos; pi); meta_sens_icc020 e meta_sens_momentum → parametros.dependencia = "um_por_estudo"; certeza.csv linhas 2 e 8
- Evidência: "aviso_rve": "gl de Satterthwaite = 1.23 < 4: inferência robusta não confiável"; certeza.csv: "intervalo de predição de -4,33 a 5,14, cruzando zero e ±δ"
- Por que importa: com um efeito por estudo, o CHE não identifica τ² dentro de estudos (a divisão 50/50 é artefato) e o RVE com 3 conglomerados não é confiável; o modelo do protocolo nesse caso é REML + HK (o `um_por_estudo`). As sensibilidades de ICC e de *momentum* foram rodadas com outro modelo de dependência e comparadas com o CHE, mudando duas coisas ao mesmo tempo. A certeza cita IP com k = 3 e k = 4, que o protocolo só interpreta com k ≥ 5.
- Correção sugerida: declarar REML + HK como principal quando todo estudo tem um efeito (ou registrar a escolha), comparar sensibilidades com o mesmo modelo e tirar o IP do juízo de imprecisão.

### R12 [MEDIO] Avisos de comparabilidade sem resposta e desfechos de nível diferente na célula agregada
- Item: S01
- Onde: meta_principal/meta_resumo.json → grupos[8].comparabilidade.avisos; efeitos_meta_principal.csv → outcome de Agranov2017a-E13, Tyszler2015-E01, Timotei2013a-E01
- Evidência: "vários outcomes no mesmo construto: conferir se medem o mesmo conceito"; outcomes: "alternativa preferida pela maioria ex ante ... eleita", "Fração de eleições cujo vencedor está no Majoritarian Set", "% de respondentes em favor do candidato A"
- Por que importa: dois dos três efeitos medem o resultado da eleição de grupo (quem venceu), não o apoio individual ao líder mostrado, e em Agranov2017a o subagente registrou que a alternativa vencedora "nem sempre" coincide com a mostrada; δ em pontos de apoio não se traduz para fração de eleições. Nenhum arquivo responde os avisos.
- Correção sugerida: responder os avisos por escrito (manter, separar ou só SWiM) e levar a decisão à indireção do GRADE.

### R13 [MEDIO] Célula momentum_outro junta Meffert2011 (voto insincero) com o momentum da Emenda 4b
- Item: S01 (também S13)
- Onde: swim_principais.csv → Meffert2011-E01 (alvo nao_se_aplica, reduzir, celula_alvo momentum_outro); certeza.csv linha 8; emendas.md, Emenda 4b
- Evidência: Meffert2011-E01 outcome "Insincere vote (voto em partido diferente do mais preferido)"; enunciado: "pesquisas que mostram um partido ganhando apoio, sem mostrar sua posição"
- Por que importa: a Emenda 4b cria a tabela só para ganho ou perda de apoio; Meffert2011 testa pesquisa apertada perto da cláusula e voto insincero, sem relação com ganho de apoio, e "benefico" aí significa menos voto insincero. O enunciado da certeza descreve um estímulo que Meffert2011 não testa.
- Correção sugerida: mover Meffert2011 para a tabela de viabilidade (com a convenção de R02) ou para síntese narrativa, e refazer a linha 8 da certeza.csv só com Dahlgaard2016a (ou declarar k = 1).

### R14 [MEDIO] certeza.csv fora do contrato de campos
- Item: S15
- Onde: 06-analise/certeza.csv → familia_intervencao (linhas 3 a 7), construto_outcome (linhas 6 a 8), validado_humano (todas)
- Evidência: "todas,apoio_ao_lider_viabilidade,efeito,randomizado,muito_baixa"; validado_humano vazio
- Por que importa: "todas" não é família dos JSON nem do master, e apoio_ao_lider_viabilidade e apoio_ao_lider_momentum não são construtos do protocolo (a separação é por alvo), o que impede junção automática com a síntese; o protocolo pede `validado_humano = 0` e pendência `certeza_humana`, e o arquivo não traz a marca "RASCUNHO NÃO VALIDADO".
- Correção sugerida: uma linha por célula do protocolo (R01), com a família e o construto grafados como nos JSON e uma coluna para o alvo; `validado_humano = 0`; abrir ou conferir a pendência `certeza_humana`.

### R15 [MEDIO] Decisões da síntese que desviam do protocolo sem emenda registrada
- Item: S20
- Onde: 00-protocolo/emendas.md (última entrada: Emenda 4, 23/09/2026; tabela-resumo sem a linha da Emenda 4 e "Protocolo congelado: v1.0 em (preencher no G2)")
- Evidência: ausência constatada em emendas.md de registro para o agrupamento da SWiM (R01), `--excluir-rob nenhum` (R04), δ fixo (R06), a coluna celula_alvo com momentum_outro (R13), o sinal por proxy `beta_proxy_sinal` e as células GRADE de viabilidade e momentum
- Por que importa: são decisões tomadas depois de ver os dados, que o PRISMA 2020 (item 24c) pede relatar como diferenças entre protocolo e revisão.
- Correção sugerida: registrar uma emenda tipo C (ou E, para correções) por decisão, com data, motivo e resultados já conhecidos; completar a tabela-resumo e a data de congelamento.

### R16 [MEDIO] Sensibilidade "todas as linhas" inclui linhas que as notas mandam não agregar, e a certeza usa suas contagens como prova de estabilidade
- Item: S07
- Onde: 06-analise/swim_todas_linhas.csv (Alabrese2024a, 96 linhas de mobilização com outcome "nao apoia nenhum partido"; Yang2023d em mobilização); notas_extracao_completa.md, Alabrese2024a e Yang2023d; certeza.csv linhas 2, 4 e 5
- Evidência: notas: "Não entram na agregação de mobilização"; certeza.csv linha 5: "com todas as linhas, 5 de 9 em desmobilização"
- Por que importa: a sensibilidade mistura desfechos fora do construto e contrastes de formato, então não mede a estabilidade da principal.
- Correção sugerida: filtrar essas linhas (e as de Witsman2016a-E05, phi omnibus) antes da sensibilidade e rodar de novo.

### R17 [MEDIO] Transferibilidade ao Brasil e seção regional não produzidas
- Item: S18
- Onde: 06-analise (não há produto); protocolo.md seção 8, "Seção regional", e seção 9, "Fatores de transferibilidade"
- Evidência: ausência constatada de avaliação de voto obrigatório, dois turnos, regulação da divulgação e confiança nas pesquisas, e da tabela de estudos com `regiao` brasil ou america_latina
- Por que importa: o protocolo prevê as duas coisas; o único estudo brasileiro (Araujo2021a) é de apuração parcial, não de pesquisa, e isso precisa ser dito explicitamente.
- Correção sugerida: produzir a tabela regional e o quadro dos quatro fatores antes do relatório, ou declarar que ficam para o G9.

### R18 [BAIXO] Confundimento possivelmente contado duas vezes nas células mistas ROBINS-I e EPOC
- Item: S13
- Onde: certeza.csv linhas 3 e 5 (justificativa)
- Evidência: "Ponto de partida: baixa, único para a célula ... Risco de viés: rebaixado; todos os resultados em risco alto (EPOC), grave ou crítico (ROBINS-I)"
- Por que importa: o ponto de partida baixo já reflete a falta de exame do confundimento; rebaixar de novo por ROBINS-I grave, cujo motivo costuma ser o confundimento, conta a mesma limitação duas vezes. Não muda o resultado (já no piso).
- Correção sugerida: dizer na justificativa quais domínios do ROBINS-I motivam o rebaixamento além do confundimento.

### R19 [BAIXO] Codificações inconsistentes de moderadores e de modelo principal
- Item: S05
- Onde: efeitos.csv → alvo_efeito de Morton2015a-E12, Erlich2023-E01, Gerber2020a-E31, Bursztyn2023a-E01 (mobilização com lider ou azarao); regiao ("999", "america_latina + brasil + outro"); modelo_principal = sim em vários efeitos de Araujo2021a, Lammers2022a e Boukouras2020a
- Evidência: notas: "linhas de `mobilizacao` recebem `alvo_efeito = nao_se_aplica`"; meta_sens_um_por_estudo: "dependencia_nao_resolvida"
- Por que importa: atrapalha subgrupos por região e a sensibilidade de um efeito por estudo; em Boukouras2020a, E01 e E03 dividem o mesmo controle.
- Correção sugerida: normalizar os valores e marcar um modelo principal por contraste (ou registrar que os vários "sim" são contrastes distintos tratados por CHE).

## Cobertura
| Item | Situação | Observação |
|---|---|---|
| S01 | problema R01, R03, R12, R13 | agrupamento fora do protocolo; efeitos que não medem a exposição; avisos sem resposta |
| S02 | problema R05 | classe deduzida da palavra "RCT"; sem desenho_nao_informado |
| S03 | ok | rejeitado_revisao = 0; nenhum estudo é revisão; Agranov2012a ligado como relato secundário |
| S04 | problema R11 | CHE + RVE com gl 1,23 como principal; modelo pré-especificado, não escolhido pelo resultado |
| S05 | problema R02, R07, R10, R19 | sinais, entrada da meta, g > 2, ICC de Timotei2013a |
| S06 | problema R11 | k ≥ 3 respeitado; viés de publicação não rodado (k < 10), correto; IP citado com k = 3 e 4 |
| S07 | problema R04, R08, R16 | leave-one-out feito; críticos invertidos; induzidos, pré-2010, sem Araujo2021a e conglomerado ausentes |
| S08 | ok (ver R11) | "consistente" não usado com IP cruzando zero; I² não lido como absoluto |
| S09 | problema R09 | direção pelo estimador e teste de sinal corretos; sem contagem por significância; ±δ ignorado |
| S10 | ok | testes combinados não rodados, como decidido no protocolo |
| S11 | não se aplica | protocolo: sem síntese qualitativa formal |
| S12 | ok | padrão boca de urna × pesquisa na mobilização marcado como "observado a posteriori e não testado" |
| S13 | problema R06, R18 | pontos de partida conforme o protocolo; justificativa por domínio escrita; duas pessoas dispensadas pelo atalho A2 |
| S14 | não se aplica | protocolo: GRADE-CERQual não se aplica |
| S15 | problema R14 | estudos de suporte existem e batem com swim_direcao.csv |
| S16 | não se aplica | protocolo: caixa de ferramentas não se aplica; nenhum produto de caixa gerado |
| S17 | não se aplica | sem linhas de implementação ou custo (exposição, não programa) |
| S18 | problema R17 | fatores de transferibilidade e seção regional ausentes |
| S19 | ok | enunciados no estilo GRADE ("pode aumentar", "é incerto"); nenhuma recomendação |
| S20 | problema R15 | desvios sem emenda; certeza.csv sem marca de rascunho (R14) |

Cobertura de leitura: 06-analise inteira (28 arquivos de texto, CSV e JSON; PNG e PDF de figuras ignorados); os CSV grandes (efeitos.csv, sens_icc020_efeitos.csv, sens_icc020_entrada.csv e swim_todas_linhas.csv, 554 linhas cada) foram lidos por script em todas as linhas e colunas, com leitura detalhada das 56 linhas de modelo principal e conferência de que as cópias de sensibilidade só diferem nas colunas esperadas; mais emendas.md, notas_extracao_completa.md, rob_geral.csv e notas_rob.md, e o protocolo inteiro.

## Pontos que exigem decisão humana
- Excluir da contagem principal Lammers2022a, Gandhi2019, Fichnova2015a, Klor2017a-E01, Urminsky2019 e os termos de interação de Bursztyn2023a e Alabrese2024a (R03), e Tyszler2015 da meta (R07), sabendo que a célula agregada pode cair abaixo de k = 3.
- Manter o agrupamento por célula do protocolo ou aceitar, por emenda tipo C depois de ver dados, células SWiM mais amplas (R01).
- Convenção de sinal da tabela de viabilidade e das exposições contínuas (R02).
- Certeza da célula randomizada de apoio_ao_lider: julgar a imprecisão frente a δ (provável muito baixa) ou aceitar, com registro, que a certeza qualifica só a direção (R06); e se a suspeita de viés de publicação (estudos pequenos de laboratório, fontes limitadas) vira rebaixamento.
- Se Timotei2013a é experimento por conglomerado para fins de variância, como decidido no risco de viés (R07).
- Todos os juízos da certeza.csv seguem sem validação humana (pendência `certeza_humana`), assim como os números de efeito (`verificacao_humana_efeitos`).
