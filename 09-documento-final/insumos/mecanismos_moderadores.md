# Mecanismos e moderadores: síntese descritiva

**RASCUNHO NÃO VALIDADO.** Insumo para o documento final, escrito por subagente (Claude Opus 5.5) em 24/09/2026 a partir dos arquivos do projeto, sem abrir PDFs. As descrições de mecanismo, moderador, efeito não intencional e equidade vêm do fichamento por IA (`05-decomposicao/fichamentos_master.csv`), que nenhum humano verificou. Os números de efeito vêm de `06-analise/efeitos.csv`, cujas 560 linhas ainda esperam a conferência humana (P039). Nada aqui é validação.

## Como ler este documento

- **Escopo.** Os 41 fichamentos do *master* (uma linha por estudo). Freden2016b é só o capítulo introdutório de uma tese; o artigo experimental não está no PDF e o estudo não tem nenhuma linha de efeito (`05-decomposicao/notas_extracao_completa.md`, primeira seção). Agranov2012a é relato secundário de Agranov2017a e não entra.
- **O que o protocolo pede.** A seção 8 do protocolo prevê "síntese narrativa estruturada" dos mecanismos testados, dos moderadores relatados e dos efeitos de viabilidade, sem síntese formal de moderadores (`00-protocolo/protocolo.md`, seção 8, "Síntese qualitativa e integração"). Os moderadores pré-especificados da seção 8 [15c] só teriam estimativa por subgrupo com k ≥ 3 por nível e teste com k ≥ 4, o que nenhuma célula alcança (não há meta-análise principal; Emenda 5, item 7). Por isso **tudo o que segue é descritivo**. A Emenda 5 (item 4) manda para esta síntese os efeitos principais que não estimam o contraste da exposição (dicionário `FORA` de `06-analise/montar_entradas_swim.py`).
- **Direção pelo estimador.** "Direção *bandwagon*" = estimativa positiva no apoio a quem a pesquisa mostra à frente; "direção de viabilidade" = mais apoio à opção mostrada como viável ou menos à mostrada como inviável; "direção de desmobilização" = estimativa negativa no comparecimento (protocolo, seção 2; Emenda 5, item 2). Significância não define direção. Quando o fichamento só relata o resultado de um teste, digo isso.
- **Dois tipos de comparação.** (a) **Dentro do estudo**: o próprio estudo estima o efeito por subgrupo, por condição ou por interação; marco se a heterogeneidade foi pré-especificada (`het_pre_especificada`). (b) **Entre estudos**: comparo a direção de estudos diferentes que diferem no moderador. A comparação entre estudos é mais fraca, porque o moderador vem junto com desenho, população e risco de viés.
- **Certeza.** Quando a afirmação corresponde a uma célula de `06-analise/certeza.csv`, dou a certeza da célula. Nos outros casos marco **[descritivo, sem certeza GRADE]**. Nenhum juízo GRADE foi validado por humano (`validado_humano = 0` em todas as linhas; pendência P036).
- **Citações de fonte.** [M: coluna] = `05-decomposicao/fichamentos_master.csv`, linha do estudo; [E: id] = `06-analise/efeitos.csv`, linha `id_efeito`; [S] = `06-analise/swim_principal/tabelas/swim_direcao.csv`; [C: linha *n*] = `06-analise/certeza.csv`, *n*-ésima linha de dados (sem contar o cabeçalho; a linha 1 é a do agregador × mobilização); [T*n*] = tabela *n* impressa por `09-documento-final/insumos/contagens_mecanismos_moderadores.py` (rodar da raiz do projeto). Valores de efeito são os gravados no arquivo (yi = g de Hedges alinhado; beta = coeficiente impresso; pp = pontos percentuais; p0 e p1 = proporções do comparador e do tratado).

## 1. Visão geral

| Item | Contagem | Fonte |
|---|---|---|
| Estudos com algum mecanismo marcado como testado (`mecanismo_testado` diferente de `nao_testado`) | 34 de 41 | [T1] |
| Tipo de evidência do mecanismo: teste de canal / hipótese dos autores / mediação estatística / relato de atores / não discutido | 23 / 12 / 3 / 2 / 1 | [T2] |
| Modelo principal que ajusta por um mediador (efeito direto, não total) | 2 (Gandhi2019, Meffert2011) | [T4] |
| Heterogeneidade pré-especificada / não declarada / não se aplica | 27 / 10 / 4 | [T6] |
| Linhas de efeito com subgrupo preenchido | 302 de 560, em 20 estudos | [T7] |
| Efeitos principais no dicionário `FORA` (interações, mecanismos, formatos) | 16, de 9 estudos | [T8] |
| Estudos sem nenhuma célula GRADE | 14 | [T20] |

**Mecanismos marcados por estudo [T1].** `mecanismo_testado` é multivalorado; um estudo pode aparecer em mais de uma linha.

| mecanismo_testado | n | estudos |
|---|---|---|
| viabilidade_estrategico | 25 | Agranov2017a, Alabrese2024a, Araujo2021a, Cornejo2023a, Freden2016b, Freden2024a, Gandhi2019, Gasperoni2015a, Gerber2020a, Grillo2024c, Groer2010a, Kaplan2019a, Klor2017a, Lago2015, Lammers2022a, Meffert2011, Meffert2012a, Schlegel2023, Stolwijk2019b, Tal2015a, Tyszler2013, Tyszler2015, Westwood2020a, Witsman2016a, Yang2023d |
| informacao | 17 | Agranov2017a, Alabrese2024a, Araujo2021a, Boukouras2020a, Bursztyn2023a, Cornejo2023a, Erlich2023, Feltovich2022, Lago2015, Meer2015a, Meffert2011, Meffert2012a, Schlegel2023, Stolwijk2019b, Tyszler2013, Tyszler2015, Westwood2020a |
| outro | 9 | Chatterjee2019a, Erlich2023, Fichnova2015a, Gandhi2019, Lammers2022a, Stolwijk2016a, Stolwijk2019b, Tal2015a, Urminsky2019 |
| nao_testado | 7 | Brugarolas2021, Dahlgaard2016a, Farjam2020a, Geers2018, Morton2015a, Timotei2013a, Unkelbach2022a |
| conformidade | 6 | Agranov2017a, Gasperoni2015a, Kaplan2019a, Lammers2022a, Stolwijk2019b, Yang2023d |
| consenso_heuristica | 3 | Boukouras2020a, Lammers2022a, Meer2015a |
| simpatia_equidade | 2 | Lammers2022a, Yang2023d |
| emocoes | 2 | Stolwijk2016a, Yang2023d |

**Mecanismo × tipo de evidência (n estudos) [T3].**

| mecanismo | mediação estatística | teste de canal | relato de atores | hipótese dos autores | não discutido |
|---|---|---|---|---|---|
| informacao | 1 | 14 | 0 | 2 | 0 |
| viabilidade_estrategico | 2 | 16 | 2 | 5 | 0 |
| consenso_heuristica | 0 | 3 | 0 | 0 | 0 |
| conformidade | 1 | 2 | 1 | 2 | 0 |
| simpatia_equidade | 0 | 1 | 1 | 0 | 0 |
| emocoes | 1 | 0 | 1 | 0 | 0 |
| outro | 2 | 7 | 0 | 0 | 0 |
| nao_testado | 0 | 0 | 0 | 6 | 1 |

Duas ressalvas pesam sobre essas contagens. Primeiro, `mecanismo_tipo_evidencia` teve 40% de concordância entre os dois codificadores de IA (κ = 0,016) e `mecanismo_testado`, 60% (κ = 0,52), ambos abaixo do limiar do protocolo (`05-decomposicao/validacao_extracao/concordancia/RELATORIO_CONCORDANCIA.md`, linhas 81 e 89). Segundo, "teste de canal" no codebook cobre desde um desenho que manipula o canal (Lammers2022a, Schlegel2023, Westwood2020a) até uma regressão do voto numa percepção medida (Witsman2016a, Cornejo2023a): a leitura abaixo separa esses casos.

## 2. Mecanismos

A teoria da exposição trata os mecanismos como rivais, com sinais possivelmente opostos, e prevê que um efeito médio próximo de zero pode esconder efeitos individuais opostos (`00-protocolo/teoria_programa.md`, seções 1 e 5). Os elos são: E1 percepção de viabilidade (expectativas), E2 cálculo estratégico, E3 heurística de consenso, E4 conformidade ou desejo de vencer, E5 simpatia pelo azarão, E6 emoções, E7 complacência e desmobilização, E8 divulgação estratégica de pesquisas enviesadas (tabela por elo, seção 2).

### 2.1 Sinal informacional e expectativas (E1; teoria rival "efeito só de expectativa")

**Quem testa.** 17 estudos marcam `informacao` [T1]; os que testam o canal com dados que separam crença e comportamento são Gerber2020a (mediação por variável instrumental), Bursztyn2023a, Erlich2023, Westwood2020a, Boukouras2020a, Meffert2011 e Lago2015 [M: mecanismo_tipo_evidencia].

**O que encontram.**

- **Gerber2020a** (experimento de campo, eleições para governador nos EUA, real) é o único teste formal de mediação do elo expectativa → comparecimento. A pesquisa mostrando disputa apertada move a crença sobre a proximidade (cerca de 2,42 p.p., segundo `08-revisao-humana/efeitos/pontos_para_o_revisor.md`, item Gerber2020a-E12), mas o efeito de 1 p.p. de crença sobre o comparecimento é praticamente zero: 0,08 p.p. (yi = 0,002; IC inteiro dentro de ±δ, marcado `nulo_por_delta`) [E: Gerber2020a-E12; `06-analise/swim_entrada_com_excluidos.csv`]. O efeito da própria exposição (pesquisa apertada × folgada, 2014) também é nulo por δ: +0,29 p.p. [E: Gerber2020a-E31]. O fichamento registra ainda que os autores testaram efeitos do tratamento na atenção às campanhas e na escolha de candidato e não os acharam [M: efeitos_nao_intencionais]. É o padrão previsto pela teoria rival 2: a pesquisa muda a expectativa, não o comportamento. **Certeza: moderada** para "pesquisa apertada × folgada não muda o comparecimento além de ±2 p.p." [C: linha 15, pesquisa_pre_eleitoral × mobilizacao × outro_resultado × randomizado]. A leitura mediacional (E12) é **[descritivo, sem certeza GRADE]**.
- **Bursztyn2023a** (referendos suíços, experimento natural, real) testa o canal da crença sobre a proximidade: depois da divulgação de uma pesquisa, quanto mais apertada ela é, maior o comparecimento líquido (β = 0,39 no dia seguinte) [E: Bursztyn2023a-E01], com coeficientes positivos também nos dias +2 e +3 [E: E02, E03] e nas interações com a cobertura da pesquisa nos jornais do cantão [E: E08 a E13]. O gradiente proximidade → comparecimento dos municípios não representativos converge para o dos representativos depois da introdução das pesquisas (tripla interação β = 0,62) [E: E14; M: moderador_descricao]. A E01 está no `FORA` por ser interação com moderador contínuo. **[descritivo, sem certeza GRADE]**
- **Erlich2023** (Geórgia, laboratório com candidatos reais) testa se a credibilidade do endossante da pesquisa condiciona a atualização. O fichamento diz que a crença se move em direção à pesquisa só no braço com endosso de universidade americana [M: moderador_descricao]. No comparecimento, os dois braços ficam na direção de desmobilização: β = −0,09 (endosso americano) e −0,44 (endosso georgiano), em log-odds [E: Erlich2023-E01, E02]. **Certeza: muito baixa** (célula de mobilização randomizada com pesquisa × sem pesquisa, que junta Agranov2017a, Groer2010a e Erlich2023) [C: linha 17].
- **Westwood2020a** (jogo de laboratório com preferências induzidas) testa se a previsão probabilística remove a incerteza sobre ser decisivo: afastar a probabilidade de vitória exibida 20 pontos de 50:50 reduz a decisão de votar em 3,4 p.p. (yi = −0,095) e 40 pontos, em 6,9 p.p. [E: Westwood2020a-E01, E02]. Mostrar a projeção em percentual de votos tem inclinação menor, também negativa (β = −0,13 por ponto; yi = −0,018) [E: E03]. O fichamento registra ainda leitura da probabilidade como percentual de votos [M: efeitos_nao_intencionais]. **Certeza: baixa** [C: linha 1, agregador_projecao × mobilizacao × outro_resultado × randomizado].
- **Boukouras2020a** (laboratório, preferências induzidas) separa dois canais do viés de pesquisa: distorção do conjunto de informação dos desinformados e ancoragem das expectativas. Revelar só as pesquisas mais favoráveis a K aumenta a taxa de vitória de K nos três experimentos (0,60 → 0,80; 0,62 → 0,73; 0,57 → 0,64), inclusive no E3, em que o eleitor é avisado do viés [E: Boukouras2020a-E01 a E03; M: mecanismo_descricao]. **Certeza: muito baixa** [C: linha 10].
- **Meffert2011** (Alemanha, laboratório com campanhas reais) mede se as pistas objetivas (pesquisas, sinais de coalizão) só mudam o voto quando viram percepções. O coeficiente da manipulação de pesquisa "apertada" sobre o voto insincero é −0,18 sem as percepções e −0,51 com elas [E: Meffert2011-E02, E01]. A E01 está no `FORA` (voto insincero com alvos opostos agregados), e a direção substantiva depende de qual alvo prevalece. **[descritivo, sem certeza GRADE]**
- **Lago2015** (46 países, corte transversal) trata a proibição de pesquisas como falha informacional que gera falha de coordenação. O sinal da interação dias de proibição × número efetivo de partidos, reorientado para a exposição, está na direção de viabilidade (menos votos desperdiçados com pesquisas em sistemas fragmentados; yi = 0,03) [E: Lago2015-E01, no `FORA`]. **[descritivo, sem certeza GRADE]**

**Força.** O elo exposição → expectativa aparece em vários desenhos, mas só Gerber2020a testa formalmente se a expectativa transmite o efeito ao comportamento, e ali a resposta é nula. Nenhum estudo faz teste formal de mediação da expectativa para o **apoio** ao líder.

### 2.2 Heurística de consenso (E3)

**Quem testa.** Lammers2022a, Meer2015a e Boukouras2020a marcam `consenso_heuristica` [T1]. Tal2015a (voto no líder como opção padrão de baixo esforço, "outro") e Fichnova2015a (*priming* pelo ranking e mera exposição, "outro") tratam de variantes [M: mecanismo_testado].

**O que encontram.**

- **Lammers2022a** é o único estudo que **manipula** o modo de processamento. Nos Estudos 2a e 2b (vinheta hipotética com dois candidatos, 90% × 10% dos outros eleitores), induzir processamento heurístico dá efeitos grandes na direção *bandwagon* (g = 1,25 e 1,03), enquanto induzir o motivo moral de igualdade dá g = −0,39 (direção *underdog*) no 2a e 0,06 no 2b [E: Lammers2022a-E06, E08, E07, E09]. A heterogeneidade foi pré-registrada [M: het_pre_especificada]. No Estudo 1 (painel polonês), a expertise política prevê a migração para o partido líder e o motivo de igualdade, a migração para o que está atrás [M: moderador_descricao]. As células são condicionais a uma vinheta sem condição neutra e o n por célula (50) é derivado (`pontos_para_o_revisor.md`, Lammers2022a). **Certeza: muito baixa** para a célula de que faz parte (mesmo candidato à frente × atrás, randomizado) [C: linha 6].
- **Meer2015a** (Países Baixos, *survey experiment* em painel real) conclui que não é o número da pesquisa que importa, mas a ênfase sobre quem ganha: pesquisa com ponto de referência de crescimento, contra o resultado "seco", dá g = 0,13 [E: Meer2015a-E01]; o resultado seco contra nenhuma pesquisa difere em 0,1 p.p., sem sinal impresso [E: E07; `pontos_para_o_revisor.md`, Meer2015a]. Nenhuma interação com preferência prévia, volatilidade ou escolaridade sustentou a hipótese condicional, e os autores leem isso como favorável aos mecanismos de gratificação e contágio, não ao atalho heurístico dos menos informados [M: mecanismo_descricao, moderador_descricao]. A E01 foi para a célula de *momentum* (Emenda 4b). **Certeza: muito baixa** [C: linha 7].
- **Boukouras2020a**: a ancoragem persiste mesmo com aviso do viés (acima, 2.1).
- **Tal2015a** (jogo online de pluralidade, preferências induzidas): o voto no candidato mais preferido sobe de 0,70 para 0,92 quando ele é o líder da pesquisa em vez do segundo [E: Tal2015a-E01]. Os autores leem o voto no líder como opção padrão que ignora os placares e reduz a utilidade esperada [M: mecanismo_descricao, efeitos_nao_intencionais]. **Certeza: muito baixa** [C: linha 6].
- **Fichnova2015a** (vinheta hipotética, candidatos fictícios): o candidato posto em primeiro na pesquisa forjada recebe posto médio melhor no arquivo polonês (g = 0,89); no eslovaco não há diferença (efeito teto) [E: Fichnova2015a-E10, E09; C: linha 6, justificativa]. **Certeza: muito baixa** [C: linha 6].
- Unkelbach2022a (Alemanha, corte transversal) só hipotetiza conformidade e heurística de consenso [M: mecanismo_tipo_evidencia = hipotese_dos_autores].

**Força.** Um único estudo manipula o canal (Lammers2022a), com vinheta hipotética e risco de viés alto (D4, desfecho autodeclarado com resposta óbvia pela vinheta) [C: linha 6, justificativa]. Os demais inferem o canal do padrão de resultados.

### 2.3 Conformidade e desejo de estar do lado vencedor (E4)

**Quem testa.** Seis estudos marcam `conformidade` [T1]; dois testam com dados (Agranov2017a, Stolwijk2019b), um por relato (Yang2023d) e os outros por hipótese [T3]. Morton2015a, Timotei2013a, Dahlgaard2016a e Unkelbach2022a também invocam o canal só como interpretação [M: mecanismo_descricao].

**O que encontram.**

- **Agranov2017a** (laboratório, grupos de nove): o modelo do eleitor pivotal previa que a pesquisa aumentasse o comparecimento da minoria e reduzisse o da maioria. O observado vai na direção oposta: com pesquisa perfeita, a maioria vota mais (0,55 → 0,63 com custo de 25 centavos; 0,43 → 0,52 com custo de 50) e a minoria vota menos (0,55 → 0,38; 0,43 → 0,27) [E: Agranov2017a-E01, E05, E02, E06]. Os autores atribuem o padrão a um grupo que responde à pivotalidade e outro que quer votar no vencedor [M: mecanismo_descricao]. A heterogeneidade por maioria e minoria não foi declarada como pré-especificada [M: het_pre_especificada = nao_declarado].
- **Stolwijk2019b** (painel, Parlamento Europeu de 2014, eleitores jovens) compara cinco caminhos exposição → comparecimento (*bandwagon*, comparecimento estratégico, eficácia informacional, cinismo, interesse) por mediação estatística: o fichamento registra o interesse pela campanha como mediador dominante e as hipóteses H3a e H3b, de comparecimento estratégico, como rejeitadas [M: mecanismo_descricao, efeitos_nao_intencionais]. O efeito total está na direção de mobilização (comparecimento 0,365 → 0,504 no modelo CBPS) [E: Stolwijk2019b-E03]. **Certeza: baixa** para o efeito total [C: linha 18]; a decomposição por caminho é **[descritivo, sem certeza GRADE]**.
- **Morton2015a** (boca de urna francesa, territórios ultramarinos) não consegue separar abstenção racional de conformidade [M: mecanismo_tipo_evidencia = hipotese_dos_autores].

**Força.** Nenhum estudo isola a conformidade com manipulação ou mediação que a identifique. A evidência é interpretativa.

### 2.4 Simpatia pelo azarão e equidade (E5)

**Quem testa.** Lammers2022a (manipulação do motivo moral de igualdade) e Yang2023d (relatos abertos) [T1].

**O que encontram.** Em Lammers2022a, a condição moral dá g = −0,39 (direção *underdog*) no Estudo 2a e 0,06 no 2b [E: Lammers2022a-E07, E09]; no Estudo 1, a idade prevê negativamente a migração para o partido atrás [M: equidade_progress_plus]. Em Yang2023d, participantes relatam tanto supressão quanto estímulo ao voto ao ver o próprio candidato perdendo [M: mecanismo_descricao]; o estudo não tem linha principal (`notas_extracao_completa.md`, Yang2023d). Dois estudos observacionais acham direção *underdog* e a interpretam por outros canais: Chatterjee2019a (boca de urna na Índia; a exposição reduz a parcela do vencedor em 2,9 p.p. nas eleições estaduais e 3,5 p.p. nas gerais) [E: Chatterjee2019a-E02, E08], que os autores leem como voto no azarão ou de protesto [M: mecanismo_descricao]; e Bursztyn2023a, que fala em efeito *underdog* assimétrico por mobilização do lado atrás [M: efeitos_nao_intencionais], com a interação proximidade × apoio ao lado atrás na parcela de votos marcada nula por δ [E: Bursztyn2023a-E17; `swim_entrada_com_excluidos.csv`, `nulo_por_delta`]. **Certeza: muito baixa** para a célula de boca de urna × apoio [C: linha 2]; o resto é **[descritivo, sem certeza GRADE]**.

**Força.** Um único teste experimental do canal, em vinheta, com sinais diferentes entre replicações.

### 2.5 Emoções (E6)

**Quem testa.** Stolwijk2016a (mediação estatística em painel) e Yang2023d (relatos) [T1, T3].

**O que encontram.** Em Stolwijk2016a (Alemanha, 2013), os efeitos indiretos da exposição a reportagens de pesquisa sobre a escolha do partido são todos positivos: via entusiasmo (0,0033), via entusiasmo e avaliação do partido (0,0022), via avaliação do partido (0,0042) e, muito menores, via ansiedade (0,0002 e 0,0003) [E: Stolwijk2016a-E08, E09, E10, E06, E07]. A variável de exposição é contínua e observacional, e o estudo tem risco de viés grave [S]. **Certeza: muito baixa** para o efeito total (*momentum*) [C: linha 8]; a decomposição é **[descritivo, sem certeza GRADE]**.

**Força.** Um estudo observacional com mediação estatística e um com relatos.

### 2.6 Voto estratégico, coordenação e viabilidade (E2)

**Quem testa.** 25 estudos marcam `viabilidade_estrategico` [T1]: 16 por teste de canal, 2 por mediação, 2 por relato e 5 por hipótese [T3]. Os efeitos de viabilidade têm célula própria (protocolo, seção 2; Emenda 5, item 2).

**O que encontram.**

- **Laboratório com preferências induzidas.** Tyszler2015: a divulgação da distribuição de preferências aumenta a vitória do conjunto majoritário (0,88 → 0,93 com valor intermediário baixo; 0,72 → 0,96 com valor alto) [E: Tyszler2015-E01, E02]. Tyszler2013: a informação aumenta o voto estratégico em eleitorados heterogêneos (g = 1,57 e 1,08, por valor da opção intermediária) [E: Tyszler2013-E01, E02]; o fichamento registra que os eleitores cujo candidato tem o menor apoio (Rank 3rd) são os que mais desertam [M: moderador_descricao]. Tal2015a: com o candidato preferido em último, entre 65% e 70% votam no segundo preferido; o voto de compromisso sobe de 0,64 para 0,73 quando o segundo preferido lidera a pesquisa [M: efeitos_nao_intencionais; E: Tal2015a-E02]. Agranov2017a: a pesquisa perfeita eleva a vitória da alternativa majoritária de 0,74 para 0,91 [E: Agranov2017a-E13]. **Certeza: muito baixa** [C: linhas 6 e 13].
- **Survey experiments com eleição real.** Cornejo2023a (México): a pesquisa aumenta o apoio ao candidato anti-PRI mais bem colocado, na direção de viabilidade (g = 0,19) [E: Cornejo2023a-E05]; os autores testam a expectativa de vitória como canal [M: mecanismo_descricao]. **Certeza: muito baixa** [C: linha 14]. Freden2024a (Suécia): mostrar o partido pequeno abaixo da cláusula de 4% **aumenta** o voto nele para KD (8,2% com 2,5% na pesquisa, contra 4,1% com 5,5%) e L (6,8% contra 4,9%), o que os autores leem como voto de seguro, validado por respostas abertas; para MP o apoio muda pouco (11,5% contra 12,2%) [E: Freden2024a-E01, E04, E07; M: mecanismo_tipo_evidencia = relato_de_atores]. Pela convenção da célula, isso é direção contrária à deserção [S: Freden2024a "misto"]. Gandhi2019 (Malásia): a informação de que o partido ideologicamente mais distante lideraria a coalizão reduz o apoio à coalizão entre apoiadores do BERSATU (DiD simples, −32 p.p.) [E: Gandhi2019-E13]; o modelo principal ajusta pela chance percebida da coalizão [M: ajuste_mediador] e os principais (E01, E03) estão no `FORA`. **[descritivo, sem certeza GRADE]** para Gandhi2019; **certeza muito baixa** para Freden2024a e Schlegel2023 [C: linha 11].
- **Vinheta com eleição simulada.** Schlegel2023 (Reino Unido, candidatos fictícios): informação mais precisa com recursos cognitivos livres, sob incentivo alto, aumenta o voto estratégico em 11 p.p. (estudo principal) e 17 p.p. (piloto) [E: Schlegel2023-E01, E02]; sob incentivo baixo, nenhum tratamento tem efeito replicável [M: moderador_descricao]. O contraste só de informação dá cerca de 5,2 p.p. com IC que cruza zero (`pontos_para_o_revisor.md`, Schlegel2023). Witsman2016a (EUA, hipotética): o voto no candidato independente preferido é 0,86 quando ele aparece com 45% e 0,55 com 5% (g = 0,90); a autora testa a chance percebida de vitória como preditor [E: Witsman2016a-E01; M: mecanismo_descricao]. Gasperoni2015a: 10,1% trocam para o segundo preferido ao ver o preferido atrás [E: Gasperoni2015a-E01, no `FORA`; risco crítico].
- **Observacionais.** Alabrese2024a (Reino Unido, FPTP): margem nacional maior, em assentos seguros, reduz o comparecimento e redistribui votos entre os partidos locais, concentrando a disputa quando margem nacional e local se alinham e fragmentando a oposição quando se opõem [M: mecanismo_descricao; E: Alabrese2024a-E125 a E128, no `FORA`]. Araujo2021a (Brasil) testou o voto estratégico como explicação alternativa e o descarta porque o efeito aparece, maior, no segundo turno, com dois candidatos (1º turno +5,69 p.p.; 2º turno +11,76 p.p. para o líder anunciado) [E: Araujo2021a-E01, E06; M: efeitos_nao_intencionais].

**Força.** É o canal com mais estudos e com os testes mais diretos (laboratório com incentivos). A direção de viabilidade aparece em laboratório e em Cornejo2023a; a exceção notável é o voto de seguro em Freden2024a, que é estratégico mas vai contra a deserção do partido pequeno. **Certeza: muito baixa** na análise descritiva do agrupamento amplo de viabilidade (2 a favor, 1 misto) [`06-analise/certeza_agrupamento_amplo.csv`, linha 5 de dados].

### 2.7 Pivotalidade, proximidade e (des)mobilização (E7)

**Quem testa.** Os estudos de comparecimento: Gerber2020a, Westwood2020a, Klor2017a, Agranov2017a, Groer2010a, Bursztyn2023a, Alabrese2024a, Kaplan2019a, Grillo2024c, Morton2015a, Brugarolas2021, Stolwijk2019b, Erlich2023 [M: mecanismo_descricao].

**O que encontram.**

- **Teste formal:** Gerber2020a, crença na proximidade sem efeito no comparecimento (2.1). **Certeza: moderada** [C: linha 15].
- **Previsões conclusivas desmobilizam:** Westwood2020a (probabilidade longe de 50:50) [C: linha 1, baixa]; Kaplan2019a (prognóstico no dia da votação; intenção de votar no preferido cai de 0,876 para 0,796, −8,06 p.p., valor derivado) [E: Kaplan2019a-E01], mas o estudo está em risco crítico e fora do teste principal [S]; boca de urna antes do fechamento: Morton2015a (−11 p.p.) [E: Morton2015a-E12] e Grillo2024c (−3,44 p.p.) [E: Grillo2024c-E02], cujos autores explicam a queda pela incerteza que desaparece [M: mecanismo_descricao]. **Certeza: muito baixa** [C: linhas 3 e 4].
- **Crenças de pivotalidade infladas:** Klor2017a mostra que revelar a distribuição de preferências aumenta o comparecimento só em eleitorados quase divididos (3 × 4; t = 3,13) [E: Klor2017a-E06], e o fichamento atribui isso a crenças superestimadas de ser pivotal [M: mecanismo_descricao]. **Certeza: muito baixa** [C: linha 16].
- **Carona intragrupo:** Groer2010a atribui o aumento do comparecimento aos eleitores flutuantes (0,30 → 0,40), com os aliados inalterados (0,40 → 0,40) [E: Groer2010a-E03, E04].
- **Mobilização por ativação ou interesse:** Brugarolas2021 (Espanha, 2019: +5,1 p.p. na intenção de votar logo após a divulgação da pesquisa do CIS) [E: Brugarolas2021-E01], com canal só hipotetizado [M: mecanismo_tipo_evidencia]; Stolwijk2019b (interesse, 2.3). **Certeza: baixa** [C: linha 18].

**Força.** O canal de pivotalidade tem o único teste formal de mediação da revisão, e ele é nulo. A direção de desmobilização aparece nas exposições que fazem a eleição parecer decidida (boca de urna, previsão probabilística), mas em estudos isolados por célula.

### 2.8 *Momentum* (tendência sem posição; Emenda 4b)

Dahlgaard2016a, Meer2015a, Stolwijk2016a e Unkelbach2022a estão na célula de *momentum* (`montar_entradas_swim.py`, conjunto `MOMENTUM`). Os quatro ficam na direção *bandwagon* [S], com Unkelbach2022a em risco crítico e fora do teste. Em Dahlgaard2016a, o artigo de ganho contra o controle dá +3,4 p.p. para os Social-Democratas e o de perda, −2,4 p.p.; ganho contra perda dá +5,7 p.p. (Social-Democratas) e +2,7 p.p. (Conservadores) [E: Dahlgaard2016a-E01, E02, E03, E06]. Os autores só hipotetizam o mecanismo e escrevem que ele "é um pouco obscuro" [M: mecanismo_testado, evidência p. 286]. **Certeza: muito baixa** em todas as células de *momentum* [C: linhas 7, 8 e 12].

### 2.9 Outros canais testados

- **Participação × conversão.** Chatterjee2019a testa se a mudança nas parcelas de voto vem de quem passa a comparecer ou de troca de voto [M: mecanismo_testado]; Araujo2021a testa desmobilização, troca e voto estratégico e conclui por conversão direta ao líder (brancos +0,31 e nulos −0,73 p.p. no 1º turno; +0,62 e −0,44 no 2º) [E: Araujo2021a-E04, E05, E08, E09; M: efeitos_nao_intencionais]. Morton2015a não separa os dois canais [M: mecanismo_testado].
- **Formato da previsão.** Urminsky2019 atribui ao formato (chance × margem) um viés de compreensão; a intenção de votar é menor com chance no Estudo 1 (yi = −0,195) [E: Urminsky2019-E01, no `FORA`].
- **Distância política dentro da coalizão.** Gandhi2019 (2.6).
- **Reputação do endossante.** Erlich2023 (2.1).

### 2.10 Quadro-resumo dos mecanismos

| Mecanismo (elo) | Estudos que testam com dados (mediação, contraste de canal ou relato) | Só interpretação dos autores | Direção observada | Força | Certeza |
|---|---|---|---|---|---|
| Expectativa / sinal informacional (E1) | Gerber2020a (mediação), Bursztyn2023a, Erlich2023, Westwood2020a, Boukouras2020a, Meffert2011, Lago2015 | Feltovich2022, Meffert2012a | A pesquisa move expectativas; o único teste formal (Gerber2020a) não acha efeito da expectativa no comparecimento | 1 mediação formal; demais por contraste | moderada só para o nulo de Gerber2020a [C: 15]; resto descritivo |
| Heurística de consenso (E3) | Lammers2022a (manipulação), Meer2015a, Boukouras2020a, Tal2015a, Fichnova2015a | Unkelbach2022a | *Bandwagon* sob processamento heurístico; a ênfase em quem ganha importa mais que o número | 1 manipulação, em vinheta | muito baixa [C: 6, 7] |
| Conformidade / desejo de vencer (E4) | Agranov2017a, Stolwijk2019b (mediação), Yang2023d (relato) | Morton2015a, Timotei2013a, Dahlgaard2016a, Unkelbach2022a, Gasperoni2015a, Kaplan2019a | Padrão compatível em Agranov2017a (maioria vota mais); Stolwijk2019b aponta o interesse, não a conformidade | nenhum teste que isole o canal | descritivo, sem certeza GRADE |
| Simpatia / equidade (E5) | Lammers2022a (manipulação), Yang2023d (relato) | Dahlgaard2016a | *Underdog* ou nulo sob o motivo de igualdade | 1 manipulação, em vinheta | descritivo, sem certeza GRADE |
| Emoções (E6) | Stolwijk2016a (mediação), Yang2023d (relato) | Nenhum | Efeitos indiretos positivos, maiores via entusiasmo que via ansiedade | 1 mediação observacional | descritivo, sem certeza GRADE |
| Estratégico / coordenação / viabilidade (E2) | Tyszler2013, Tyszler2015, Tal2015a, Agranov2017a, Cornejo2023a, Freden2024a (relato), Schlegel2023, Witsman2016a, Gandhi2019, Alabrese2024a, Lago2015 | Grillo2024c, Groer2010a, Kaplan2019a, Gasperoni2015a, Meffert2012a | Direção de viabilidade no laboratório e no México; voto de seguro contra a deserção na Suécia | o canal com mais estudos | muito baixa [C: 11, 14] |
| Pivotalidade / proximidade (E7) | Gerber2020a, Westwood2020a, Klor2017a, Agranov2017a, Bursztyn2023a, Alabrese2024a | Morton2015a, Grillo2024c, Groer2010a, Kaplan2019a, Brugarolas2021 | Previsões conclusivas na direção de desmobilização; disputa apertada na de mobilização; crença isolada sem efeito | estudos isolados por célula | moderada (nulo, Gerber2020a) a muito baixa [C: 1, 3, 4, 15 a 18] |

## 3. Moderadores: para quem, onde, quando

**Relatados pelos estudos [T5].** preferência prévia 12, sofisticação ou interesse 10, competitividade 9, partidarismo 8, escolaridade 4, idade 4, classe 1, confiança nas pesquisas 1, "outro" 32, nenhum 4. `moderadores_relatados` teve 60% de concordância entre os codificadores (κ = 0,57), abaixo do limiar (`RELATORIO_CONCORDANCIA.md`, linha 90).

**Contexto dos 41 estudos [T18].** Sistema eleitoral: regra do experimento 14, proporcional 8, pluralidade 6, não informado (999) 5, maioria em dois turnos 4, outro 2, referendo 1, misto 1. Competidores: 3 ou mais 24, dois 17. Realismo: real 25, induzido 9, hipotético 7. Tipo de eleição: candidato ou partido 32, simulada abstrata 8, referendo 1. Família: pesquisa pré-eleitoral 33, agregador ou projeção 4, boca de urna 3, outro 1. Dias até a eleição informados em 11 de 41; margem mostrada informada em 16 de 41; voto obrigatório informado em 10 de 41.

**Direção por moderador, entre estudos.** As tabelas abaixo cruzam o moderador de nível de estudo [M] com a direção do estudo na SWiM principal [S]. "benefico" = direção *bandwagon*, de viabilidade ou de mobilização; "danoso" = *underdog*, contra a viabilidade ou desmobilização; "*" = risco crítico, fora do teste principal. Um estudo pode aparecer em mais de uma célula. É comparação entre estudos e é **[descritivo, sem certeza GRADE]**.

### 3.1 Sistema eleitoral e número de competidores

Hipótese da tabela Z: efeito maior com pluralidade e três ou mais competidores (`teoria_programa.md`, seção 4).

**Dentro do estudo.**

- Farjam2020a (laboratório com temas reais) interage a exposição com três regras (maioria, representação plena, limiar de 13%) e relata nenhuma interação notável [M: moderador_descricao]; heterogeneidade pré-especificada.
- Lago2015: a interação proibição × número efetivo de partidos está na direção de viabilidade (mais votos desperdiçados sem pesquisas quando o sistema é fragmentado) [E: Lago2015-E01, no `FORA`]; o efeito condicional com ENEP = 0 tem sinal oposto (yi = −0,13) [E: E02]; pré-especificada.
- Araujo2021a: primeiro turno com vários candidatos, +5,69 p.p.; segundo turno com dois, +11,76 p.p. [E: E01, E06]. Contraste entre turnos, não declarado como heterogeneidade.
- Tal2015a: o número de eleitores da pesquisa (103, 1.009, 10.007) não muda o padrão qualitativo [M: moderador_descricao].
- Freden2016b: suecos e canadenses se comportam de modo parecido sob regras iguais [M: moderador_descricao]. Esse registro vem de um artigo da tese que não está no PDF.

**Entre estudos, apoio ao líder na célula principal [T11, T12].**

| n_competidores | na direção *bandwagon* | *underdog* | estudos |
|---|---|---|---|
| 2 | 5 | 0 | Lammers2022a, Feltovich2022, Boukouras2020a, Agranov2017a, Timotei2013a |
| 3 ou mais | 7 | 1 | Morton2015a, Araujo2021a, Tal2015a, Fichnova2015a, Witsman2016a, Farjam2020a, Tyszler2015; *underdog*: Chatterjee2019a |

Oito dos 13 estudos da célula principal usam "regra do experimento" como sistema eleitoral [T11]. A direção não muda com o número de competidores, e a SWiM não mede magnitude, então a hipótese Z não pode ser avaliada.

### 3.2 Proximidade da disputa e margem mostrada

Hipótese Z: mais *underdog* (mobilização do lado atrás) em disputa apertada e mais *bandwagon* ou desmobilização em disputa decidida. A margem mostrada só está informada em 16 estudos [T18], e `margem_mostrada` teve 35% de concordância entre os codificadores (`RELATORIO_CONCORDANCIA.md`, linha 79).

**Dentro do estudo.**

- **Comparecimento.** Gerber2020a, apertada × folgada: nulo por δ; **certeza moderada** [C: 15]. Bursztyn2023a: quanto mais apertada a pesquisa, maior o comparecimento e, onde o lado atrás tem mais apoio prévio, maior o comparecimento (β = 0,0125) [E: E15]; na parcela do lado atrás, o efeito é nulo por δ [E: E17]; pré-especificada. Alabrese2024a: margem nacional maior × assento seguro reduz o comparecimento (β = −0,18) [E: E002], mais quando o partido do incumbente local lidera nacionalmente (β = −0,24 e −0,29) do que quando não lidera (β = −0,05 e −0,07) [E: E025 a E028]; pré-especificada. Klor2017a: a informação aumenta o comparecimento só em eleitorados quase divididos [E: E06; M: moderador_descricao]; pré-especificada. Groer2010a: nos eleitorados informados o comparecimento cresce com o nível de discordância [M: moderador_descricao]. Kaplan2019a e Urminsky2019: sem relação entre o tipo de disputa e a decisão de votar [M: moderador_descricao].
- **Apoio ao líder.** Agranov2017a: a pesquisa aumenta mais a vitória da maioria quando a diferença de composição é pequena (0,70 → 0,85 e 0,69 → 0,76) do que quando é grande (0,96 → 0,97; 0,96 → 0,90) [E: E15, E16, E17, E24]; não declarada como pré-especificada. Tal2015a: as correlações de gap-leader e gap-last com a taxa de compromisso vão na direção oposta à prevista [M: moderador_descricao]. Klor2017a, eleições para governador nos EUA: g = 0,29 nas eleições esperadas como apertadas e −0,06 nas outras [E: E04, E05]; a análise não tem contraste de exposição e o árbitro sugere tratá-la como estudo à parte (`pontos_para_o_revisor.md`, Klor2017a).

**Leitura.** Nos estudos que variam a proximidade, a disputa apertada vai na direção de mais comparecimento e a decidida, na de menos; o experimento de campo (Gerber2020a), que é o desenho mais forte, não acha efeito além de ±2 p.p. A mobilização do lado atrás, prevista pela hipótese Z, aparece como padrão de comparecimento em Bursztyn2023a, mas o efeito na parcela de votos é nulo por δ. **[descritivo, sem certeza GRADE]**, exceto o nulo de Gerber2020a (moderada).

### 3.3 Realismo do contexto (laboratório e vinheta × eleição real)

Hipótese Z: efeito maior em contextos hipotéticos e induzidos.

**Apoio ao líder, célula principal [T9].**

| realismo | *bandwagon* | *underdog* | estudos |
|---|---|---|---|
| hipotético | 4 | 0 | Lammers2022a, Fichnova2015a, Witsman2016a, Timotei2013a |
| induzido | 5 | 0 | Tal2015a, Feltovich2022, Boukouras2020a, Agranov2017a, Tyszler2015 |
| real | 3 | 1 | Morton2015a, Araujo2021a, Farjam2020a; *underdog*: Chatterjee2019a |

**Mobilização [T14].**

| realismo | mobilização | desmobilização | misto | nulo | estudos |
|---|---|---|---|---|---|
| hipotético | 0 | 1* | 0 | 0 | Kaplan2019a (crítico) |
| induzido | 3 | 1 | 0 | 0 | Agranov2017a, Klor2017a, Groer2010a; desmobilização: Westwood2020a |
| real | 2 | 3 | 1 | 1 | Stolwijk2019b, Brugarolas2021; desmobilização: Morton2015a, Grillo2024c, Erlich2023; misto: Chatterjee2019a; nulo: Gerber2020a |

**Leitura.** No apoio ao líder, os 9 estudos hipotéticos ou induzidos estão todos na direção *bandwagon*; entre os 4 reais, um vai na direção oposta. No comparecimento, a direção majoritária muda com o realismo: mobilização em 3 de 4 estudos induzidos, desmobilização ou nulo em 4 de 7 reais. A justificativa GRADE registra o mesmo na sensibilidade só com contexto real: no apoio randomizado sobra só Farjam2020a, e na mobilização randomizada a direção majoritária se inverte [C: linhas 6, 13 e 17, justificativas]. A magnitude não é comparável (SWiM por direção). O realismo é o principal motivo de rebaixamento por indireção nas células de apoio [C: linhas 6 e 13]. **[descritivo, sem certeza GRADE]**

### 3.4 Tipo de eleição

Hipótese Z: efeito maior em referendos. Só um estudo é de referendo (Bursztyn2023a) [T18], de modo que a hipótese não pode ser examinada entre estudos.

**Dentro do estudo.** Chatterjee2019a estratifica eleições estaduais e gerais (não declarada como pré-especificada): na parcela do vencedor, as duas vão na direção *underdog* (−2,92 e −3,50 p.p.) [E: E02, E08]; no comparecimento, as estaduais vão na de desmobilização (−4,71 p.p.) e as gerais, na de mobilização (+0,90 p.p.) [E: E14, E16]. Westwood2020a não acha diferença por cargo (Câmara, Senado, Presidência) [M: moderador_descricao]. **[descritivo, sem certeza GRADE]**

### 3.5 Momento: dias até a eleição

Hipótese Z: efeito maior perto do dia da eleição. `dias_ate_eleicao` está informado em 11 de 41 estudos, com 60% de concordância (`RELATORIO_CONCORDANCIA.md`, linha 88): 0 dias em Araujo2021a, Grillo2024c e Morton2015a; de 2 a 13 nos outros oito [T18].

**Dentro do estudo.** Bursztyn2023a: coeficientes positivos nos dias +1, +2 e +3 após a divulgação (0,39; 0,35; 0,42) [E: E01 a E03]. Urminsky2019: a diferença de intenção de votar entre chance e margem é −0,21 em setembro e −0,03 no fim de outubro de 2016 [E: E02, E03]. Alabrese2024a: na amostra individual, a interação só aparece entre os entrevistados antes da eleição; os entrevistados depois servem de placebo [M: moderador_descricao]. Unkelbach2022a: a associação com a intenção de voto no SPD é maior entre quem relatou ter visto pesquisas na semana anterior [M: moderador_descricao]; risco crítico.

**Entre estudos.** As três exposições no próprio dia da votação (boca de urna e apuração parcial) dão efeitos grandes no apoio (Araujo2021a, Morton2015a) e desmobilização (Morton2015a, Grillo2024c), mas também são as únicas de variação natural com eleição real, e o momento se confunde com o desenho. **[descritivo, sem certeza GRADE]**

### 3.6 Partidarismo, preferência prévia, sofisticação e interesse

Hipóteses Z: partidários fortes mudam menos; teorias rivais para a sofisticação, com (a) mais *bandwagon* entre os pouco sofisticados, pela heurística, e (b) mais entre os sofisticados, pelo cálculo estratégico.

**Dentro do estudo, apoio.**

- **Cornejo2023a** (pré-especificada): o efeito na direção de viabilidade é maior entre partidários (g = 0,33), partidários de terceiros partidos (0,36) e eleitores anti-PRI (0,36) do que entre independentes (0,09), e fica perto de zero, com sinal oposto, entre quem prefere o PRI (−0,05) [E: Cornejo2023a-E06 a E10]. Os autores esperavam voto estratégico atenuado entre partidários [M: het_pre_especificada, evidência p. 80]; a direção observada é a contrária.
- **Gandhi2019** (pré-especificada): o efeito depende de qual partido o respondente apoia. Contra os demais apoiadores da coalizão: BERSATU −30,3 p.p., DAP −7,8, PAS −14,1, AMANAH +13,7 [E: E01, E03, E09, E11].
- **Freden2024a**: simpatizantes dos Moderados votam mais em KD quando ele está abaixo da cláusula; os dos Democratas Suecos, sobretudo no próprio partido [M: moderador_descricao].
- **Lammers2022a**: a expertise política prevê a migração para o líder, e o motivo de igualdade, para o que está atrás (Estudo 1); a heurística induzida dá *bandwagon* (Estudos 2a e 2b) [M: moderador_descricao; E: E06 a E09].
- **Meer2015a** (pré-especificada): nenhuma interação com preferência prévia pelo PvdA, volatilidade ou escolaridade [M: moderador_descricao].
- **Gasperoni2015a** (não declarada; risco crítico): proporções de quem trocou de voto entre os expostos, sem comparador: conhecimento baixo 0,12, médio-baixo 0,14, médio-alto 0,08, alto 0,05; interesse baixo 0,06, intermediário 0,12, alto 0,16; identificação com coalizão nenhuma 0,06 e forte 0,13 [E: Gasperoni2015a-E18 a E28]. Os autores dizem que nenhuma diferença é significativa [M: moderador_descricao].
- **Witsman2016a** e **Kaplan2019a**: partidarismo e filiação sem relação com o voto ou a troca [M: moderador_descricao].
- **Boukouras2020a**: os eleitores desinformados votam mais em K [M: moderador_descricao].

**Dentro do estudo, crenças e comparecimento.**

- **Gerber2020a**: os menos informados atualizam mais a crença; no comparecimento, o nulo se mantém em todas as subamostras [M: moderador_descricao].
- **Meffert2011**: ler mais artigos de pesquisa reduz o erro de previsão sobretudo entre os pouco sofisticados; o efeito não é sobre o voto [M: moderador_descricao].
- **Erlich2023**: a atualização cresce com o conhecimento só no braço americano, e pró-GDC atualizam mais [M: moderador_descricao].
- **Stolwijk2019b** (pré-especificada): o efeito indireto via interesse aparece entre os de eficácia informacional alta, não entre os de baixa [M: moderador_descricao].
- **Westwood2020a**: sem efeito da numeracia; o raciocínio motivado se atenua com o formato probabilístico [M: moderador_descricao].
- **Geers2018**: entre os moderadamente interessados, a exposição a notícias de pesquisa se associa à conversão para outro partido [M: moderador_descricao].
- **Lago2015**: sem pesquisas, só os menos informados perdem acurácia [M: equidade_progress_plus].
- **Agranov2017a**: maioria vota mais e minoria vota menos com pesquisa [E: E01 a E08] (2.3).
- **Groer2010a**: o aumento do comparecimento vem só dos flutuantes [E: E03, E04].

**Leitura.** O partidarismo não atenua o efeito em Cornejo2023a e o redireciona em Gandhi2019; nos demais estudos em que foi examinado, não o modera. Sobre a sofisticação, as duas teorias rivais têm algum apoio: os menos informados atualizam mais as crenças e respondem mais à heurística induzida (Gerber2020a, Meffert2011, Lago2015, Lammers2022a), enquanto quem trocou de voto em Gasperoni2015a é mais interessado. Nenhum estudo testa as duas no mesmo desenho. **[descritivo, sem certeza GRADE]**

**Efeitos que se anulam (teoria rival 1).** O protocolo só permite afirmar essa hipótese com pelo menos 3 estudos que relatem subgrupos com sinais opostos (seção 8 [15d]). A varredura mecânica acha 6 estudos com linhas de subgrupo de sinais opostos no apoio (Agranov2017a, Alabrese2024a, Cornejo2023a, Freden2024a, Klor2017a, Lammers2022a) [T21]. Na maioria, porém, os "subgrupos" são composições do eleitorado (Agranov2017a-E24), partidos-alvo (Freden2024a), especificações de interação (Alabrese2024a) ou outra análise (Klor2017a-E05). Só dois estudos têm sinais opostos entre grupos de eleitores ou de processamento: Cornejo2023a (preferem o PRI, E10) e Lammers2022a (motivo moral, E07). Como são menos de 3, a hipótese fica **não testada**, como manda o protocolo. **[descritivo, sem certeza GRADE]**

### 3.7 Tipo de pesquisa: pré-eleitoral, agregador ou projeção, boca de urna

Hipótese Z: projeções probabilísticas têm mais efeito sobre expectativas e desmobilização.

**Entre estudos [T13, T15].**

| família | Apoio: *bandwagon* ou viabilidade | Apoio: contrário | Apoio: misto | Mobilização | Desmobilização | Mobilização: misto ou nulo |
|---|---|---|---|---|---|---|
| pesquisa pré-eleitoral | 15 (+1 crítico) | 0 | 1 (Freden2024a) | 5 | 1 (Erlich2023) | 1 nulo (Gerber2020a) |
| agregador ou projeção | sem estudo | sem estudo | sem estudo | 0 | 1 (Westwood2020a) + 1 crítico (Kaplan2019a) | 0 |
| boca de urna | 1 (Morton2015a) | 1 (Chatterjee2019a) | 0 | 0 | 2 (Morton2015a, Grillo2024c) | 1 misto (Chatterjee2019a) |
| apuração parcial (outro) | 1 (Araujo2021a) | 0 | 0 | sem estudo | sem estudo | sem estudo |

**Dentro do estudo.** Westwood2020a: a probabilidade de vitória tem inclinação sobre a decisão de votar mais negativa (yi = −0,095 para +20 pontos) que a projeção em percentual de votos (yi = −0,018) [E: E01, E03]. Urminsky2019: chance × margem, −0,195 na intenção de votar [E: E01, no `FORA`]. Meer2015a: o enquadramento importa mais que o número [E: E01, E07]. Yang2023d: o tipo de visualização muda emoções e confiança, com 2-Interval mais forte e 1-Dotplot com maior distância entre partidários [M: moderador_descricao]; nenhuma linha principal.

**Leitura.** As exposições que fazem o resultado parecer decidido (boca de urna antes do fechamento, previsão probabilística) estão na direção de desmobilização; a pesquisa pré-eleitoral está sobretudo na de mobilização. Isso está de acordo com a hipótese Z, mas a família se confunde com o desenho: toda boca de urna é experimento natural em eleição real. **Certeza: baixa** para Westwood2020a [C: 1] e **muito baixa** para boca de urna [C: 2 a 4]; o contraste entre famílias é **[descritivo, sem certeza GRADE]**.

### 3.8 Região: Brasil e América Latina, voto obrigatório

**Estudos da região [T18].** Araujo2021a (Brasil, apuração parcial oficial, voto obrigatório), Cornejo2023a (México, *survey experiment* em eleição real) e Lago2015 (46 países, entre eles o Brasil). A tabela regional com g, risco de viés e certeza está em `09-documento-final/insumos/tabelas/regional.md`.

- **Araujo2021a:** direção *bandwagon* nos dois turnos (+5,69 e +11,76 p.p.) [E: E01, E06]; os autores testam e descartam desmobilização (brancos e nulos com variações de menos de 1 p.p.) e voto estratégico [M: efeitos_nao_intencionais]. **Certeza: muito baixa** [C: linha 5]. Único estudo com eleição real sob voto obrigatório e sistema de dois turnos, os dois fatores de transferibilidade para o Brasil da seção 9 do protocolo.
- **Cornejo2023a:** direção de viabilidade, maior entre partidários (3.6). **Certeza: muito baixa** [C: linha 14].
- **Lago2015:** interação no `FORA`, sem certeza.

**Voto obrigatório.** Codificado "Sim" em Araujo2021a e em dois laboratórios (Feltovich2022, Tyszler2015), onde o voto é obrigatório pelo desenho [T18]. Nenhum dos 12 estudos de mobilização da SWiM principal tem `voto_obrigatorio` = "Sim": dois estão como "Não" (Gerber2020a, Grillo2024c) e dez como 999, não informado [T16]. A hipótese Z de que o voto obrigatório elimina o canal da desmobilização não pode ser examinada; o indício mais próximo é a variação pequena de brancos e nulos em Araujo2021a. **[descritivo, sem certeza GRADE]**

## 4. Efeitos não intencionais e equidade

### 4.1 Efeitos não intencionais

`efeitos_nao_intencionais` está preenchido em 34 dos 41 fichamentos [T19]. A classificação abaixo é do coordenador, lida no texto do fichamento, e está codificada no dicionário `NAO_INT` do script: "dado" = medido com dados, em qualquer direção; "não achado" = testado e não encontrado; "discutido" = só discussão ou hipótese.

| Categoria | Com dados | Testado e não achado | Só discutido |
|---|---|---|---|
| Desmobilização (E7) | 11: Agranov2017a, Alabrese2024a, Chatterjee2019a, Erlich2023, Geers2018, Grillo2024c, Kaplan2019a, Klor2017a, Morton2015a, Urminsky2019, Westwood2020a | 2: Araujo2021a, Stolwijk2019b | 1: Yang2023d |
| Deserção do preferido ou de terceiros (E2) | 10: Alabrese2024a, Cornejo2023a, Farjam2020a, Freden2016b, Gasperoni2015a, Meffert2012a, Tal2015a, Tyszler2013, Tyszler2015, Witsman2016a | 2: Araujo2021a, Freden2024a | 0 |
| Perda de bem-estar ou decisões piores | 6: Boukouras2020a, Groer2010a, Lago2015, Meffert2011, Meffert2012a, Tal2015a | 0 | 1: Freden2016b |
| Pesquisas enviesadas ou manipulação (E8) | 1: Boukouras2020a | 0 | 6: Alabrese2024a, Farjam2020a, Lammers2022a, Morton2015a, Timotei2013a, Tyszler2015 |
| Outros | 5: Bursztyn2023a, Chatterjee2019a, Erlich2023, Urminsky2019, Westwood2020a | 2: Gerber2020a, Meer2015a | 2: Schlegel2023, Yang2023d |

O que o fichamento registra, em síntese [M: efeitos_nao_intencionais]:

- **Desmobilização.** Nas exposições que mostram a eleição decidida: Morton2015a (cerca de 11 p.p.), Grillo2024c (com abstenção relativamente maior à esquerda, que os autores dizem ter reduzido a margem em cerca de 1 p.p.), Westwood2020a, Kaplan2019a; da minoria em Agranov2017a; do time grande em eleitorados desequilibrados em Klor2017a; nos assentos seguros em Alabrese2024a. Araujo2021a acha só apoio fraco para desmobilização, e Stolwijk2019b rejeita o comparecimento estratégico.
- **Deserção.** É o próprio desfecho dos estudos de viabilidade. Freden2024a não acha a deserção para "não desperdiçar o voto".
- **Bem-estar.** Boukouras2020a: pagamentos menores e o candidato de maior valência perde mais com pesquisas enviesadas. Groer2010a: comparecimento acima do socialmente ótimo. Tal2015a: o voto no líder reduz a utilidade esperada. Meffert2011 e Meffert2012a: sinais de coalizão levam a decisões erradas.
- **Pesquisas enviesadas (E8).** Só Boukouras2020a testa a divulgação seletiva; nos demais é discussão. Timotei2013a usa uma pesquisa fabricada como tratamento.
- **Outros.** Erlich2023: queda na percepção de legitimidade do resultado no braço americano. Westwood2020a: probabilidade lida como percentual de votos. Urminsky2019: mais disposição a apostar. Bursztyn2023a: mudança na composição do eleitorado, grande o bastante, em simulação dos autores, para inverter referendos. Chatterjee2019a: efeitos na entrada e retirada de candidaturas. Gerber2020a: nenhum efeito na busca de informação. Meer2015a: nenhum "efeito Titanic".
- **Sem registro (999):** Brugarolas2021, Dahlgaard2016a, Feltovich2022, Fichnova2015a, Gandhi2019, Stolwijk2016a, Unkelbach2022a [T19].

Só a desmobilização tem célula GRADE (construto `mobilizacao`, desfecho crítico do protocolo), com a certeza de cada célula dada na seção 2.7. As demais categorias são **[descritivo, sem certeza GRADE]**. `efeitos_nao_intencionais` teve 0% de concordância textual entre os codificadores, porque o campo é texto livre (`RELATORIO_CONCORDANCIA.md`, linha 63).

### 4.2 Equidade (PROGRESS-Plus: escolaridade, classe, idade)

`equidade_progress_plus` está preenchido em 12 fichamentos, dois deles (Stolwijk2019b, Yang2023d) com 999 em todos os fatores [T19]. Hipótese do protocolo: *bandwagon* maior entre os de menor escolaridade ou classe; nenhuma hipótese para a idade (`teoria_programa.md`, seção 4).

| Fator | Estudos com conteúdo | O que relatam [M: equidade_progress_plus] |
|---|---|---|
| Escolaridade | 6: Dahlgaard2016a, Gasperoni2015a, Gerber2020a, Lago2015, Meer2015a, Unkelbach2022a | Com efeito diferencial testado: Dahlgaard2016a (nenhuma diferença), Meer2015a (nenhuma interação), Unkelbach2022a (moderação só para os Verdes, com associação mais forte entre os menos escolarizados; risco crítico). Descritivo: Gasperoni2015a (quem trocou é mais escolarizado, sem significância). Sem efeito diferencial: Gerber2020a (só crença prévia), Lago2015 (só controle). |
| Classe | 2: Lago2015, Unkelbach2022a | Unkelbach2022a: hipótese central, sem moderação para nenhum dos seis partidos. Lago2015: interpretação de desigualdade informacional, sem medir classe. |
| Idade | 6: Farjam2020a, Gasperoni2015a, Kaplan2019a, Lago2015, Lammers2022a, Witsman2016a | Lammers2022a: a idade prevê negativamente o efeito *underdog*. Gasperoni2015a: os mais jovens trocam mais, sem significância. Kaplan2019a e Witsman2016a: sem relação. Farjam2020a e Lago2015: só controle. |

**Leitura.** Dos três estudos que testam a escolaridade como moderadora, um acha a direção prevista para um partido (Unkelbach2022a, em risco crítico) e dois não acham diferença; o único teste de classe não acha moderação. A hipótese de equidade não encontra apoio consistente. **[descritivo, sem certeza GRADE]**

## 5. Certeza: o que tem célula GRADE e o que não tem

| Afirmação desta síntese | Célula de `certeza.csv` | Certeza |
|---|---|---|
| Pesquisa apertada × folgada não muda o comparecimento além de ±2 p.p. (Gerber2020a) | pesquisa_pre_eleitoral × mobilizacao × outro_resultado × randomizado (linha 15) | moderada |
| Projeção probabilística longe de 50:50, direção de desmobilização (Westwood2020a) | agregador_projecao × mobilizacao × outro_resultado × randomizado (linha 1) | baixa |
| Ter visto a divulgação de pesquisas, direção de mobilização (Stolwijk2019b, Brugarolas2021) | pesquisa_pre_eleitoral × mobilizacao × unidades_nao_expostas × não randomizado (linha 18) | baixa |
| Boca de urna, apoio e comparecimento (Morton2015a, Chatterjee2019a, Grillo2024c) | linhas 2 a 4 | muito baixa |
| Apuração parcial no Brasil (Araujo2021a) | linha 5 | muito baixa |
| Mesmo candidato à frente × atrás, inclusive os resultados de Lammers2022a e Tal2015a | linha 6 | muito baixa |
| *Momentum* (Dahlgaard2016a, Meer2015a, Stolwijk2016a) | linhas 7, 8 e 12 | muito baixa |
| Pesquisa × sem pesquisa no apoio (Agranov2017a, Farjam2020a, Timotei2013a, Tyszler2015) | linha 13 | muito baixa |
| Viabilidade (Schlegel2023, Freden2024a, Cornejo2023a) | linhas 11 e 14 | muito baixa |
| Comparecimento em laboratório e Erlich2023; Klor2017a | linhas 16 e 17 | muito baixa |
| Mediação (Gerber2020a-E12, Stolwijk2016a, Stolwijk2019b), mecanismos por interpretação, todos os contrastes de moderador dentro e entre estudos, efeitos não intencionais além da desmobilização, equidade, efeitos do `FORA` | nenhuma | **descritivo, sem certeza GRADE** |

A certeza GRADE qualifica a direção, não a magnitude, e em nenhuma célula foi validada por humano [C: coluna validado_humano]. 14 estudos não entram em nenhuma célula: Alabrese2024a, Bursztyn2023a, Freden2016b, Gandhi2019, Gasperoni2015a, Geers2018, Kaplan2019a, Lago2015, Meffert2011, Meffert2012a, Tyszler2013, Unkelbach2022a, Urminsky2019 e Yang2023d [T20]. Muito do que esta síntese diz sobre mecanismos e moderadores vem deles.

## 6. Pontos para o revisor humano

**P039: conferência dos 560 efeitos.** Todo número desta síntese vem de `efeitos.csv` e muda se a conferência mudar a linha. Os que mais pesam aqui:

- Lammers2022a-E06 a E09: n por célula (50) derivado; células condicionais a uma vinheta sem condição neutra. São a base das seções 2.2 e 2.4.
- Gerber2020a-E12: estimativa por IV de 1 p.p. de crença, não da exposição. É a base da seção 2.1.
- Tyszler2015-E01 e E02: valores lidos de figura.
- Kaplan2019a-E01: valor derivado; a folha 26 conta 21 trocas, não as 27 impressas.
- Freden2024a-E01, E04, E07: estatística impressa como t(1,744) e similares.
- Cornejo2023a-E06 a E10 e Gandhi2019-E01 a E13: base do moderador partidarismo.
- Chatterjee2019a e Morton2015a-E41: sinais invertidos da proibição para a exposição (Emenda 5, item 3).
- Bursztyn2023a-E17: nulo por δ.
- Alabrese2024a-E002 e E125 a E128: |g| > 2, alerta do `efeitos.R`.
- Gasperoni2015a-E18 a E28: proporções sem comparador.
- Westwood2020a-E01 a E03.

**P037: concordância da extração.** Abaixo do limiar entre os campos usados aqui (`RELATORIO_CONCORDANCIA.md`): `mecanismo_tipo_evidencia` (40%, κ = 0,016), `mecanismo_testado` (60%), `moderadores_relatados` (60%), `sistema_eleitoral` (60%), `dias_ate_eleicao` (60%), `margem_mostrada` (35%), `ajuste_mediador` (70%), `voto_obrigatorio` (70%) e os textos livres `mecanismo_descricao`, `moderador_descricao` e `efeitos_nao_intencionais`. Acima do limiar: `realismo_contexto`, `tipo_eleicao`, `n_competidores`, `regiao`, `het_metodo`, `het_pre_especificada` e `desenho_fino`. As tabelas por mecanismo e por moderador (seções 1 e 3) dependem sobretudo dos campos abaixo do limiar; as de realismo e de competidores, dos que passam.

**P033: risco de viés.** A leitura de força depende de RoB não validado:

- Unkelbach2022a, Kaplan2019a e Gasperoni2015a em risco crítico, fora do teste principal [S; `swim_entrada_com_excluidos.csv`];
- Lammers2022a, Tal2015a, Fichnova2015a e Witsman2016a em risco alto;
- Fichnova2015a: 17 de 37 respondentes eslovacos fora das tabelas, com D3 baixo (`pontos_para_o_revisor.md`).

**Decisões pendentes em `pontos_para_o_revisor.md` que mudam esta síntese.**

- **Gerber2020a-E12 para o `FORA`:** não muda a direção, mas muda o papel do estudo (efeito de exposição × mecanismo).
- **Klor2017a-E01:** o motivo do `FORA` conflita com o comparador `mesmo_candidato_atras`. Se voltar, entra na célula da linha 6. A análise de governadores dos EUA (E04 e E05), usada aqui como moderador de proximidade, seria estudo à parte.
- **Geers2018-E01 e E02:** o árbitro sugere pô-los de volta na contagem, só pela direção (desmobilização).
- **Feltovich2022-E01 e E02:** a prévia pode ser mecanismo de coordenação, não exposição. Se entrarem no `FORA`, saem da célula da linha 9 e da contagem por realismo e competidores (seções 3.1 e 3.3).
- **Witsman2016a-E01:** se o alvo passar a viabilidade, o estudo sai da célula principal e muda as tabelas 3.1 e 3.3 e a seção 2.6.
- **Schlegel2023:** entrar no `FORA` ou só receber ressalva, porque o contraste mistura precisão da pesquisa com carga cognitiva. Afeta a seção 2.6.
- **Alabrese2024a:** participação nos votos × probabilidade de vitória como desfecho de apoio.
- **Grillo2024c:** comparador `outro_resultado` × `unidades_nao_expostas`.
- **Brugarolas2021:** `sistema_eleitoral` = 999 por regra do codebook; o árbitro sugere proporcional, o que mudaria a tabela 3.1.
- **Codificação do ano da eleição em laboratório:** inconsistente entre 999 e o ano da coleta; afeta a sensibilidade sem pré-2010.
- **Meer2015a:** a E01 está na célula de *momentum*; a E07 não tem sinal impresso.
- **Unkelbach2022a:** alvo `nao_se_aplica`; EPs possivelmente copiados errados no artigo.

**Específicos desta síntese.**

- A classificação dos efeitos não intencionais (dicionário `NAO_INT` do script) é leitura do coordenador de IA sobre o texto do fichamento e precisa de conferência.
- A leitura da varredura de sinais opostos [T21], isto é, quais "subgrupos" são grupos de eleitores, é julgamento e decide se a teoria rival 1 fica como hipótese não testada.
- Freden2016b tem mecanismo e moderadores fichados a partir do capítulo introdutório da tese (`notas_extracao_completa.md`): os registros não têm efeito correspondente e devem ser lidos como relato dos autores sobre artigos que o projeto não tem.
- A Emenda 6b pode mudar o conjunto de incluídos. Se mudar, as contagens deste documento precisam ser refeitas com o script.

## Apêndice: reprodução

Todas as contagens das seções 1, 3 e 4 e as listas de estudos por célula saem de:

```bash
cd ~/Desktop/pesquisas-eleitorais-rs
python3 09-documento-final/insumos/contagens_mecanismos_moderadores.py
```

O script só lê arquivos (`fichamentos_master.csv`, `efeitos.csv`, `swim_entrada_com_excluidos.csv`, `swim_principal/tabelas/swim_direcao.csv`, `certeza.csv`), junta tudo por `chave` e `id_efeito` e imprime as tabelas T1 a T21 citadas no texto. Os valores de efeito citados por `id_efeito` podem ser conferidos direto em `06-analise/efeitos.csv`.
