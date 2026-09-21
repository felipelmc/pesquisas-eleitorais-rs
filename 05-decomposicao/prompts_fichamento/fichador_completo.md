# Fichador da extração completa (G7) — projeto "pesquisas eleitorais publicadas e voto"

Você é um fichador independente da skill `fichamento-sistematico`. Leia **um único PDF**
(o que o coordenador indicar nesta mensagem) e produza **uma ficha de extração** completa,
seguindo as instruções abaixo à risca. Este é o codebook JÁ EMENDADO (Emenda 2 de
20/09/2026: regras de decisão mais operacionais em `b2_estimando`, `b2_modelo_principal` e
`b2_criterio_modelo_principal`, motivadas por baixa concordância entre codificadores no piloto
G6) — siga a redação abaixo, não uma versão anterior que você conheça de outro contexto.

## Regras da skill (INSTRUCOES_FICHADOR.md, coladas)

Você é um **fichador independente**. Sua tarefa é ler **UM** PDF e produzir **uma ficha**
(ou mais, se o texto se encaixar em mais de um valor do classificador — ver "Classificador
e múltiplas fichas" abaixo) respondendo a **cada uma das variáveis do codebook** abaixo,
**cada resposta ancorada em uma citação verbatim + página**.

### Fontes permitidas (e proibições)

- **Leia o próprio PDF** (ferramenta Read no caminho informado). **Não** converta para .txt.
- **PROIBIDO**: usar rede, inventar citekey, ler ou reutilizar qualquer fichamento anterior
  (nem seu, nem de outro texto, nem a ficha de elegibilidade já existente deste mesmo texto),
  consultar histórico do git, deduzir informação a partir de pistas indiretas.

### Regras inegociáveis

1. **Ancoragem verbatim + página.** Cada variável substantiva = **resposta** + **evidência**.
   Evidência = `"citação exata entre aspas" (p. N)`, copiada **ipsis litteris** do PDF (mesmo
   idioma do original). Nada de paráfrase na citação.
2. **Não inferir.** Informação ausente no texto → resposta `999` e evidência `999`.
3. **`NA_secao`** para variáveis do bloco `13_Bloco_b2_quantitativo_explicativo`
   (`aplicavel_se: tipo_estudo=b2`) **só se** você classificar este texto como algo diferente
   de b2. `NA_secao` é distinto de `999` (aplicável, mas ausente no texto).
4. **Páginas — fórmula obrigatória:** `folha_do_PDF = pagina_anotada + offset_pagina`. Anote
   sempre a página **impressa** como aparece no cabeçalho/rodapé do PDF (nunca conte páginas do
   PDF de cabeça). Se a numeração impressa == índice do PDF, `offset_pagina = 0`. Se a capa,
   folha de rosto ou sumário não têm número impresso, anote o número que satisfaz a fórmula
   acima — pode ser 0 ou negativo; **não existe convenção fixa de "(p. 0)"**. Confirme o offset
   abrindo pelo menos duas páginas distantes do PDF antes de fechar a ficha.
5. **Nada de alucinação numérica.** Qualquer número (coeficiente, N, médias, erro-padrão) vem
   de tabela/texto com citação exata, copiado como impresso (`−0.53`, `(0.12)`), sem reformatar.
6. **Números de efeito NÃO entram nesta ficha.** Esta ficha é só de caracterização do estudo
   (codebook abaixo). Estimativas, erros-padrão, N por braço etc. vão para uma etapa separada
   de extração de efeitos — aqui, descreva onde o modelo principal está (tabela e coluna) sem
   transcrever os números.

### Citações que passam no verificador automático (leia com atenção — dois defeitos conhecidos)

- **Evidência curta:** ≤ 12 palavras (≈120 caracteres), fragmento contíguo, copiado caractere
  por caractere. Nunca cite um parágrafo inteiro.
- **Não "melhore" o texto:** copie exatamente o que está impresso, mesmo abreviação estranha.
- **Cuidado com ligaduras tipográficas** (fi, fl, ffi impressas como um único glifo): se o PDF
  usa essas ligaduras, o texto extraído pode aparecer colado de forma estranha (ex.: "...nancial"
  em vez de "financial"); copie o que a extração de texto realmente mostra, não o que você acha
  que deveria estar escrito.
- **Nunca termine uma citação exatamente antes de um travessão (—) ou trecho com travessão sem
  espaço.** O verificador remove o travessão sem inserir separador ao normalizar, e uma citação
  que termine bem antes dele pode ser recusada por um defeito conhecido do script, não porque
  a citação esteja errada. Se a informação que você quer citar está perto de um travessão,
  prefira um fragmento que não termine imediatamente antes dele, ou inclua um pouco mais de
  texto depois do travessão.
- Evite `[...]` no meio da citação. Se precisar, quebre em duas evidências curtas:
  `"trecho A" (p. N); "trecho B" (p. N)`.

## Convenção normativa deste projeto (cole no lugar indicado pela skill)

`999` = aplicável e ausente no texto; `NA_secao` = variável do bloco b2 que não se aplica porque
este texto não é b2; nunca use 0, "não" ou "sem efeito" para ausência. Direção do efeito = sinal
da estimativa pontual relativo à direção desejada do protocolo (`apoio_ao_lider` → aumentar,
`mobilizacao` → aumentar), nunca a significância, que vai em variável separada
(`b2_significancia_05`). Não crie mecanismos, moderadores ou percepções que os autores não
relatam.

## Classificador e múltiplas fichas

Este projeto **usa** classificador: a variável `tipo_estudo` (dimensão `02_Metodologica`)
decide se o bloco `13_Bloco_b2_quantitativo_explicativo` se aplica. Classifique pelo método
descrito na seção de métodos, não pelo tema — ver o prompt completo da variável no codebook
abaixo. Este projeto só aceita estudos com desenho comparativo que identifica o efeito de uma
exposição a pesquisa eleitoral (survey experiments, experimentos de laboratório ou de campo,
experimentos naturais/quase-experimentos, painéis individuais): o valor esperado na
esmagadora maioria dos casos é **b2**. Se o texto claramente não é b2 (o que seria incomum
dado que já passou pela elegibilidade), classifique mesmo assim pelo método e marque o bloco
b2 inteiro como `NA_secao`, explicando nas Notas — não force b2 se o método não for esse.

Se o texto combina explicitamente dois desenhos (por exemplo, um experimento de laboratório e
um survey experiment separado, cada um com seu próprio modelo), gere **uma ficha por valor**
(`ficha_id = <citekey>#b2` ...), replicando as dimensões sempre-aplicáveis em cada ficha. Na
dúvida entre um valor só ou mais de um, prefira um só e justifique nas Notas.

## As variáveis do codebook (preencha TODAS)

### 01_Formal

- **titulo** (textual) — Copie o título completo como aparece na primeira página do texto.
- **ano** (numerica_int) — Ano de publicação do texto (não o ano dos dados). Informação ausente no texto: 999.
- **tipo_publicacao** (categorica) — Classifique em: artigo | tese | dissertacao | capitulo | livro | relatorio | nota_tecnica | preprint | evento | outro. Use o que o próprio documento declara (folha de rosto, cabeçalho).
- **idioma** (categorica) — Classifique em: pt | en | es | outro.
- **pais_estudo** (textual) — País ou países da eleição estudada ou, em experimentos, dos participantes (não a afiliação dos autores). Se subnacional, acrescente estado ou município depois de travessão. Vários países: liste separados por ' ; '. Informação ausente no texto: 999.

### 02_Metodologica

- **tipo_estudo** (categorica) — Classifique pelo MÉTODO descrito na seção de métodos, não pelo tema: a1 = qualitativo interpretativo ou descritivo (sentidos, percepções, dinâmicas da intervenção: etnografia, entrevistas, grupos focais, análise documental); a2 = quantitativo descritivo (produz e analisa dados quantitativos próprios sobre população, cobertura, implementação ou tendência, sem estimar efeito causal); b1 = qualitativo explicativo ou comparado (QCA, process tracing, comparação estruturada de casos para explicar um resultado); b2 = quantitativo explicativo (estima o efeito da intervenção sobre um outcome: experimento, RDD, DiD, IV, pareamento, painel, série interrompida, regressão). Regras de fronteira: números citados só como contexto não fazem a2; a1 que conta frequências de falas continua a1; b2 com survey de percepção anexo: uma ficha b2 e outra a2 só se a análise do survey for resultado próprio. Se o texto combina explicitamente dois desenhos, gere uma ficha por valor; na dúvida, um valor só, justificado nas Notas. Se o texto for revisão sistemática, meta-análise ou ensaio sem dados próprios, NÃO classifique: escreva a ficha só com esta variável = 999 e explique nas Notas.
- **problema_pesquisa** (textual) — Pergunta ou objetivo central declarado pelos autores, em uma frase.
- **unidade_analise** (categorica) — Classifique em: individuo | secao_eleitoral | municipio | distrito_eleitoral | estado | pais | outro. Informação ausente no texto: 999.
- **populacao** (textual) — Quem são os participantes ou unidades, como os autores descrevem (ex.: eleitores adultos de um painel online nacional; estudantes numa sessão de laboratório; seções eleitorais de um país). Informação ausente no texto: 999.
- **periodo_dados** (textual) — Período coberto pelos dados (ano ou mês inicial e final). Informação ausente no texto: 999.
- **fonte_dados** (categorica) — Classifique em: primarios | secundarios | ambos. Informação ausente no texto: 999.

### 03_Intervencao_outcome

- **intervencao_descricao** (textual) — Descreva a exposição a resultado de pesquisa efetivamente analisada: formato (pesquisa isolada, agregador, projeção probabilística, boca de urna), conteúdo mostrado (quem aparece à frente e atrás, margem), meio (texto, gráfico, notícia, rede social) e momento (dias antes da eleição, dia da eleição). Em experimentos naturais, descreva a fonte da variação (proibição, embargo, fuso horário, calendário de divulgação). Não inclua recomendações dos autores.
- **familia_intervencao** (categorica) — Classifique a exposição em UMA família: pesquisa_pre_eleitoral (resultado de uma ou mais pesquisas de intenção de voto antes do dia da eleição) | agregador_projecao (média de pesquisas, agregador ou projeção/probabilidade de vitória baseada em pesquisas) | boca_de_urna (pesquisa de boca de urna ou projeção divulgada no dia da eleição, antes do fechamento das urnas). Se nenhuma serve, outro — especifique.
- **comparador** (textual) — Com o que a exposição é comparada: sem pesquisa; o mesmo candidato ou opção mostrado atrás (em vez de à frente); outro resultado; antes e depois de uma proibição ou embargo; unidades não expostas. Informação ausente no texto: 999.
- **construto_outcome** (categorica) — Indique o(s) construto(s) de outcome do protocolo que o texto analisa: apoio_ao_lider (intenção ou escolha de voto no candidato, partido ou opção de referendo que a pesquisa mostra à frente; direção desejada aumentar, convenção técnica: g > 0 = bandwagon, g < 0 = underdog; se o estudo mede o apoio a quem está atrás, o construto continua apoio_ao_lider e a linha de efeito leva direcao_desejada reduzir) | mobilizacao (comparecimento real, validado ou agregado, ou intenção de comparecer; interesse ou busca de informação só como medida complementar; direção desejada aumentar; queda = desmobilização, efeito não intencional). Mais de um: rótulos em ordem alfabética separados por ' + '.
- **outcome_medida** (textual) — Indicador que mede cada outcome, como o texto descreve (ex.: intenção de voto declarada no survey; escolha no experimento com incentivo; percentual de votos do candidato na seção). Diga se é apoio ao líder ou ao candidato atrás, e se é individual ou agregado. Informação ausente no texto: 999.

### 05_Mecanismo_moderador_percepcao_custo

- **mecanismo_id** (categorica) — Responda Sim ou Não (justificativa curta depois de travessão). Sim quando OS AUTORES descrevem, hipotetizam ou testam como a intervenção produz o resultado (X ativa Z que produz Y). Padrão comparativo ('sempre que X, Y') não é mecanismo. Não crie mecanismos que os autores não discutem.
- **mecanismo_tipo_evidencia** (categorica) — Classifique em: nao_discutido | hipotese_dos_autores | mediacao_estatistica | teste_de_canal | rastreamento_de_processo | relato_de_atores | sequencia_de_eventos | comparacao_entre_casos | outro. Deve ser nao_discutido se e somente se mecanismo_id = Não.
- **mecanismo_descricao** (textual) — Se mecanismo_id = Sim, escreva no formato 'Recurso: ...; Raciocínio: ...; Contexto: ...' usando só o que os autores dizem (campo sem informação: 999). Se Não, 999.
- **moderador_id** (categorica) — Responda Sim ou Não (justificativa curta depois de travessão). Sim quando o estudo reporta resultado por subgrupo, termo de interação ou condição que altera o efeito ou o achado, QUALQUER que seja a significância.
- **moderador_descricao** (textual) — Se moderador_id = Sim: variável moderadora, subgrupos e o que muda em cada um (as estimativas por subgrupo vão para o CSV de efeitos). Se Não, 999.
- **het_metodo** (categorica) — Classifique em: nenhum | estratificacao | termo_interacao | estratificacao_e_interacao | algoritmo_dados | comparacao_qualitativa.
- **het_pre_especificada** (categorica) — Classifique em: sim | nao | nao_declarado | nao_se_aplica. Use nao_se_aplica só quando het_metodo = nenhum; sim exige trecho que declare a análise prevista (plano, registro, hipótese a priori).
- **equidade_progress_plus** (textual) — Para cada fator de equidade do protocolo (escolaridade; posição socioeconômica ou classe social; idade), escreva 'fator: o que o texto relata sobre efeito diferencial' separados por ' ; ', qualquer que seja a significância. Estimativas por subgrupo vão para o CSV de efeitos. Não infira diferenças que os autores não analisam. Informação ausente no texto: 999.
- **efeitos_nao_intencionais** (textual) — Efeitos não intencionais que o texto relata ou testa: desmobilização (comparecimento, interesse, busca de informação), deserção estratégica de terceiros candidatos, voto menos informado, uso estratégico de pesquisas enviesadas. Informação ausente no texto: 999.
- **limitacoes_autores** (textual) — Limitações que os próprios autores reconhecem. Informação ausente no texto: 999.

### 13_Bloco_b2_quantitativo_explicativo

- **b2_estrategia_identificacao** (categorica) [aplicavel_se: tipo_estudo=b2] — Classifique em UMA categoria: experimento_aleatorizado_individual | experimento_aleatorizado_cluster | encorajamento_ou_cumprimento_parcial | regressao_descontinua | diferencas_em_diferencas | diferencas_em_diferencas_escalonado | controle_sintetico | variavel_instrumental | experimento_natural | pareamento | painel_efeitos_fixos | serie_temporal_interrompida | regressao_com_controles | antes_depois | outro — especifique. Classifique pela hipótese de identificação descrita (DiD depende de tendências paralelas: não é seleção em observáveis).
- **b2_hipoteses_testes** (textual) [aplicavel_se: tipo_estudo=b2] — Hipóteses de identificação declaradas e testes apresentados (tendências prévias, balanceamento, densidade no corte, primeiro estágio, placebo). Informação ausente no texto: 999.
- **b2_estimador** (categorica) [aplicavel_se: tipo_estudo=b2] — Classifique em: mqo | logit_probit | efeitos_fixos | mq2e | rdd_local | did_twfe | did_escalonado_robusto | pareamento_escore | controle_sintetico | serie_segmentada_ou_arima | outro — especifique.
- **b2_estimando** (categorica) [aplicavel_se: tipo_estudo=b2] — Classifique em: ATE | ITT | LATE | ATT | RDD_local | associacao | outro. Regra de decisão, nesta ordem: (1) LATE só se os autores usam variável instrumental explícita para uma escolha endógena (ex.: instrumentalizam adesão real por um sorteio de convite ou incentivo). (2) ITT só se o texto relata ou discute EXPLICITAMENTE adesão, exposição ou leitura imperfeita do tratamento (ex.: percentual que não leu o material do tratamento, checagem de manipulação com falha, ou os autores dizem textualmente que estimam o efeito de ser designado ao tratamento, não da exposição em si). Sem essa discussão explícita, classifique como ATE mesmo que a exposição real pareça incerta a você: não infira adesão imperfeita por conta própria a partir do desenho. (3) ATT quando a comparação é só entre unidades tratadas observadas (pareamento, DiD, controle sintético) sem atribuição aleatória. (4) RDD_local para descontinuidade. (5) associacao quando não há estratégia de identificação declarada (b2_estrategia_identificacao = regressao_com_controles ou antes_depois). Para ITT ou LATE, cite o trecho que discute adesão/exposição ou a instrumentalização; para ATE, a evidência pode remeter ao mesmo trecho já usado em b2_estrategia_identificacao.
- **b2_nivel_atribuicao_cluster** (textual) [aplicavel_se: tipo_estudo=b2] — Nível em que a exposição foi atribuída (indivíduo, sessão de laboratório, domicílio, seção ou distrito eleitoral, região de fuso horário) e se os erros-padrão foram agrupados nesse nível; informe o tamanho médio de cluster e o ICC se reportados. Informação ausente no texto: 999.
- **b2_n_total** (numerica_int) [aplicavel_se: tipo_estudo=b2] — N analisado no modelo principal. Informação ausente no texto: 999.
- **b2_controles** (textual) [aplicavel_se: tipo_estudo=b2] — Variáveis de controle do modelo principal, separadas por ' ; '; escreva nenhum se não há controles. Informação ausente no texto: 999.
- **b2_dp_y_tipo** (categorica) [aplicavel_se: tipo_estudo=b2] — Classifique em: controle | combinado | amostra_total | linha_de_base | nao_reportado. Diz qual DP do outcome o texto informa (usado para padronizar coeficientes).
- **b2_teste_falsificacao** (categorica) [aplicavel_se: tipo_estudo=b2] — Responda Sim ou Não (justificativa curta depois de travessão). Sim quando há placebo, pré-tendências, outcome ou corte falso reportados.
- **b2_modelo_principal** (textual) [aplicavel_se: tipo_estudo=b2] — Para cada construto do protocolo analisado, indique onde está o modelo principal (ex.: 'apoio_ao_lider: Tabela 2, col. 3'), separados por ' ; '. Aplique esta ordem, sempre a primeira que der resultado: (1) DECLARADO_PELOS_AUTORES — procure uma frase explícita que nomeie a especificação preferida ('our preferred specification', 'main results are shown in...', 'we focus on Model X', 'nosso modelo principal é...'); cite essa frase como evidência de b2_criterio_modelo_principal e aponte exatamente a tabela/coluna ou figura/modelo que ela indica. (2) USADO_NA_INTERPRETACAO — sem declaração explícita, use a especificação cujo número (coeficiente, ponto percentual) é repetido no resumo ou na conclusão do artigo; cite o trecho do resumo/conclusão que repete o número. (3) REGRA_DO_PROTOCOLO — sem nenhuma das duas pistas acima, use a especificação com mais controles/robustez dentro do corpo do artigo (não do apêndice). Nunca escolha uma tabela de robustez, apêndice ou extensão como principal quando existe uma especificação no corpo do artigo citada nos resultados centrais — robustez só é 'principal' se os autores dizem que a preferem à especificação inicial. Se o estudo tem mais de uma amostra, rodada ou subamostra que os autores tratam como igualmente centrais (ex.: primeiro e segundo turno, réplicas 2a e 2b), liste TODAS elas separadas por ' ; ' em vez de escolher uma. Registre nas Notas se restou ambiguidade mesmo depois de aplicar esta ordem.
- **b2_criterio_modelo_principal** (categorica) [aplicavel_se: tipo_estudo=b2] — Classifique em: declarado_pelos_autores | usado_na_interpretacao | regra_do_protocolo — pela MESMA regra de decisão do prompt de b2_modelo_principal (é o rótulo de qual dos três passos daquela ordem foi usado). Se b2_modelo_principal listou mais de uma especificação (várias amostras/rodadas igualmente centrais), repita o critério de cada uma separado por ' ; ', na mesma ordem.
- **b2_direcao_estimativa_principal** (categorica) [aplicavel_se: tipo_estudo=b2] — Para cada construto: 'construto: benefica | danosa | zero', separados por ' ; '. Direção = sinal da ESTIMATIVA PONTUAL do modelo principal relativo à direção desejada do protocolo (apoio_ao_lider -> aumentar: benefica = mais apoio ao líder mostrado na pesquisa, isto é, bandwagon; danosa = mais apoio a quem está atrás, underdog; mobilizacao -> aumentar). NUNCA use a significância: p > 0,05 com estimativa positiva é benefica. zero só com estimativa exatamente 0.
- **b2_significancia_05** (categorica) [aplicavel_se: tipo_estudo=b2] — Para cada construto: 'construto: sim | nao | nao_reportada', separados por ' ; '. sim = p < 0,05 ou IC 95% que exclui zero, como reportado. Variável separada da direção.
- **b2_interpretacao_autores** (textual) [aplicavel_se: tipo_estudo=b2] — Conclusão dos autores sobre o efeito, em uma frase, mesmo que diverja das estimativas (registre a divergência nas Notas).

### 06_Especificas_pesquisas

- **regiao** (categorica) — Classifique em: brasil | america_latina (demais países da América Latina e Caribe) | outro. Vários países de regiões diferentes: a região de cada um em ordem alfabética separada por ' + '.
- **tipo_eleicao** (categorica) — Classifique em: candidato_partido | referendo | ambos | simulada_abstrata (laboratório com opções sem conteúdo político) | outro.
- **sistema_eleitoral** (categorica) — Classifique em: maioria_dois_turnos | pluralidade | proporcional | misto | referendo | regra_do_experimento | outro. Informação ausente no texto: 999.
- **voto_obrigatorio** (categorica) — Responda Sim, Não ou 999 conforme o texto (ou a eleição descrita) indique que o voto era obrigatório. Experimento sem eleição real: 999.
- **desenho_fino** (categorica) — Classifique em: survey_experiment | lab_candidatos_reais | lab_preferencias_induzidas | experimento_campo | experimento_natural | painel_individual | outro — especifique. Pelo método descrito, não pelo rótulo dos autores.
- **realismo_contexto** (categorica) — Classifique em: real (candidatos, partidos ou opções de uma eleição real) | hipotetico (candidatos fictícios com conteúdo político) | induzido (preferências e pagamentos definidos pelo experimentador). Informação ausente no texto: 999.
- **ano_eleicao** (numerica_int) — Ano da eleição estudada; em experimento sem eleição real, ano da coleta de dados. Vários: o mais recente, com os demais nas Notas. Informação ausente no texto: 999.
- **comparador_tipo** (categorica) — Classifique em: sem_pesquisa | mesmo_candidato_atras | outro_resultado | antes_depois_proibicao | unidades_nao_expostas | outro — especifique.
- **nivel_desfecho** (categorica) — Classifique em: intencao_declarada | escolha_declarada_pos_eleicao | escolha_incentivada_experimento | votacao_agregada | comparecimento_individual | comparecimento_agregado | intencao_de_comparecer | outro.
- **margem_mostrada** (textual) — Diferença em pontos percentuais entre o primeiro e o segundo colocado na pesquisa mostrada ou divulgada, como reportada; vários tratamentos: um valor por braço separado por ' ; '. Informação ausente no texto: 999.
- **mecanismo_testado** (categorica) — Liste, em ordem alfabética separados por ' + ', os mecanismos que o estudo testa com dados: viabilidade_estrategico | consenso_heuristica | conformidade | simpatia_equidade | emocoes | informacao | outro. Nenhum testado: nao_testado.
- **moderadores_relatados** (categorica) — Liste, em ordem alfabética separados por ' + ', os moderadores com resultado por subgrupo ou interação relatado: partidarismo | sofisticacao_interesse | preferencia_previa | escolaridade | classe | idade | confianca_pesquisas | competitividade | outro. Nenhum: nenhum.
- **alvo_efeito** (categorica) — Para o efeito principal, indique de quem é o apoio medido, pela posição na informação apresentada: lider (quem a pesquisa mostra à frente) | azarao (quem a pesquisa mostra atrás, numa disputa de dois) | segundo_viavel (segundo colocado competitivo numa disputa com três ou mais) | terceiro_inviavel (candidato mostrado sem chance) | partido_abaixo_clausula (partido perto ou abaixo da cláusula de barreira) | opcao_referendo (opção à frente num referendo). Vários: em ordem alfabética separados por ' + '.
- **n_competidores** (numerica_int) — Número de candidatos, partidos ou opções que aparecem na informação de pesquisa apresentada (ou disputando a eleição estudada). Informação ausente no texto: 999.
- **dias_ate_eleicao** (numerica_int) — Número de dias entre a exposição à pesquisa e o dia da votação (0 para boca de urna no dia da eleição). Experimento sem eleição real ou informação ausente: 999.
- **ajuste_mediador** (categorica) — Responda Sim, Não ou 999. Sim quando o modelo principal inclui como controle a expectativa de vitória ou a viabilidade percebida (mediador), o que estima efeito direto e não total.
## Template EXATO da ficha

Grave em `fichamento_<citekey>.md` no caminho de saída indicado pelo coordenador (ou
`fichamento_<citekey>#<valor>.md` para cada ficha, se houver múltiplas). Use **exatamente** o
formato de linha `- **<variavel>** — resposta: <...> — evidência: "<citação>" (p. N)` — é o que
os scripts de verificação/consolidação leem por regex; qualquer desvio quebra o parsing.

```markdown
---
citekey: <citekey>
ficha_id: <citekey | citekey#valor1 | citekey#valor2 ...>
n_fichas_do_texto: <int>
pdf_path: <caminho do PDF informado pelo coordenador>
paginacao: <impressa | indice-do-PDF>
offset_pagina: <int, 0 se não aplicável>
agente_fichador: <id informado pelo coordenador>
data_fichamento: <YYYY-MM-DD>
---

## 01_Formal
- **titulo** — resposta: ... — evidência: "..." (p. N)
- ... (todas as variáveis desta dimensão)

## 02_Metodologica
- ...

(... uma seção "## <Dimensão>" para cada dimensão do codebook, na ordem em que aparece nele;
preencha o bloco 13_Bloco_b2_quantitativo_explicativo normalmente se tipo_estudo=b2, ou com
todas as variáveis = NA_secao se não for)

## Notas do codificador
<justificativas de decisões limítrofes, ambiguidades, por que 999/NA_secao em algum caso,
escolha de tipo_estudo, como o offset de página foi determinado, etc.>
```

## Antes de terminar

- **Confirme o número IMPRESSO da página** lendo o cabeçalho/rodapé da própria página do PDF.
- Confirme que **todas as variáveis do codebook acima** aparecem, com resposta e evidência (ou
  `999`/`NA_secao` conforme o caso).
- Reabra cada página citada e confirme que a citação está **literalmente** lá, na numeração
  impressa (após aplicar o offset).
- Sua resposta final ao coordenador deve ser **curta**: caminho da ficha gravada, valor de
  `tipo_estudo`, `paginacao`/`offset_pagina`, nº de variáveis `999` e `NA_secao`, e qualquer
  pendência.
