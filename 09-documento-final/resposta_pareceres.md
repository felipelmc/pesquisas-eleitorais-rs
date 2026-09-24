# Resposta às leituras críticas simuladas (etapa 6)

Redigida em 24/09/2026 por um subagente Opus (`claude-opus-5-5`), redator do artigo, seguindo `prompts_v2/prompt_revisao_pareceres.md`. As leituras L1 (editor de métodos) e L2 (cientista político) são simuladas por IA: não são revisão por pares, e nada aqui valida etapa alguma (P038). Não houve análise nova. Todo pedido que mudaria célula, efeito fora da contagem, alvo, GRADE, rótulo da caixa ou critério, ou que exigiria tabulação, busca ou fonte nova, ficou como "decisão do autor", ligado à pendência que o cobre. Fatos novos vieram só de `insumos/contexto_brasil.md` (seção 7), `insumos/revisoes_anteriores.md`, `insumos/garritty_2024.md` e dos arquivos de dados.

Arquivos editados: `_esqueleto_revisao_final.qmd` (montado em `revisao_final.qmd`), `linguagem_simples.qmd`, `revista/figuras/legendas.yml`, `revista/tabelas/hipoteses.yml`, `oqf_principal.yml`, `transferibilidade.yml` e a prosa de `_esqueleto_suplemento.qmd` (S2, S3, S8 e o subtítulo). Também rodei `revista/preparar_referencias.py`, porque o texto passou a citar três chaves de `referencias_contexto.bib` (TSE2021Res23669, TSE2022Divulgacao17h e TSE2018Totalizacao2Turno), e `montar_suplemento.py`, só para levar a prosa nova ao `suplemento.qmd` (o script não foi alterado).

Resumo das decisões:

| Leitura | Aceito | Aceito em parte | Não aceito | Decisão do autor | Total |
|---|---|---|---|---|---|
| L1 | 5 | 14 | 0 | 4 | 23 |
| L2 | 8 | 10 | 0 | 0 | 18 |
| Total | 13 | 24 | 0 | 4 | 41 |

Nos "aceito em parte", a parte não aplicada é decisão do autor ou tarefa do coordenador, e está dita em cada item.

## L1, editor de métodos

**L1-1. Título e regra R7.28.** Aceito em parte.
- Feito: o subtítulo passou a "Rascunho de revisão sistemática rápida, conduzida por agentes de IA e não validada, sobre os efeitos *bandwagon* e *underdog* e o comparecimento", mantendo a identificação do item 1 do PRISMA; o mesmo no suplemento e na citação. O aviso inicial e a 2.9 citam a R7.28 ("Nenhum produto desse tipo conta como revisão sistemática") e dizem que a interpretação entre estudos foi redigida por agentes, uso que a R7.27 não admite.
- Decisão do autor (P038): o estatuto do produto depois da validação e o título definitivo.

**L1-2. Validação da extração.** Aceito em parte.
- Feito, na 2.5: o limiar do protocolo (κ ou PABAK de pelo menos 0,7 e concordância de pelo menos 80% por variável) e a frase "Por esse limiar, a validação não aprovou a extração por IA". A passagem de 56 para 70 efeitos principais foi explicada: a arbitragem promoveu 13 efeitos a principais, rebaixou 5 e criou 6 linhas (contagem de `05-decomposicao/correcoes_sessao_2026-09-23.csv`, conferida contra os 70 principais de `05-decomposicao/efeitos/`). As 40 correções barradas foram identificadas como trocas do estimando de @Morton2015a. A 4.4 e a declaração de IA repetem a não aprovação.
- Decisão do autor (P037 e P039): a tabela estudo a estudo das direções (original, cega, arbitrada) para C01, C02, C13, C14 e C18 e a verificação de se as 240 extensões tocam efeitos principais. As duas são tabulação nova.

**L1-3. Enquadramento do achado principal.** Aceito.
- (a) Mensagens, Resumo, Resumo executivo, 1.4, 4.1, 5.2 e Conclusões dizem agora que as estimativas "apontaram a favor de quem aparece à frente" e seguem com a frase GRADE na forma neutra ("a evidência é muito incerta sobre o efeito de ver uma pesquisa no apoio ao líder"). Os spans de enunciado vêm de `certeza.csv` e não foram mudados.
- (b) "Rareia" e "depende do laboratório" saíram. A 3.8 e a 4.1 dizem que a regularidade "repousa sobretudo em laboratório e vinheta; em contexto real, os poucos estudos não a contrariam, mas não se sabe se ela se mantém", e a 4.2 diz que o padrão é compatível com a advertência de Barnfield, sem confirmá-la.
- (c) O glossário e a 2.7 definem "direção *bandwagon*" como rótulo operacional, compatível com adesão à maioria e com coordenação estratégica. A contribuição (ii), na 1.3 e na 4.1, ficou restrita ao que as células separam (*momentum* e deserção para o segundo viável).

**L1-4. Certeza baixa de C18.** Decisão do autor (P036; @Geers2018, P039).
- A certeza não mudou. No texto, C18 saiu das Mensagens principais (o item de comparecimento fala só de C13 e dos "demais contrastes", com certeza baixa ou muito baixa). Resumo e *Abstract* marcam a certeza baixa como "em revisão". A 3.7 e a 4.4 (ii) registram que a célula caiu um nível, e não dois, como C04, C06 e C11.
- @Geers2018: a 3.8 (vi) diz que, com o comparador codificado como "outro", ele formaria célula própria, e não entraria em C18, e que o motivo "conferência humana pendente" só foi aplicado a ele. Tratá-lo como os demais ou declarar critério geral é do autor.

**L1-5. C13.** Aceito em parte.
- Feito: a 3.7 reescreve a frase das "duas estimativas". O efeito da carta, de 0,29 ponto percentual, sustenta o nulo, e o de variável instrumental, de 0,08 ponto por ponto de crença, está em outra escala. O estimando aparece como efeito de receber a carta, sem saber quem a leu. "Receber, por carta" entrou nas Mensagens, no Resumo, no Resumo executivo, na 4.1, na 5.2 e nas Conclusões. "Permite descartar" saiu (erro E3). A 3.7 diz que a célula não foi rebaixada pela indireção e que cai um nível se o autor rebaixar pelo relato seletivo, e a 2.7 e o glossário dizem que a regra do nulo por ±δ veio da Emenda 5, depois dos dados.
- Decisão do autor: tirar a E12 da contagem (P039, ponto já listado em `08-revisao-humana/efeitos/pontos_para_o_revisor.md`); rebaixar por indireção (P036); sensibilidade com δ de 1 p.p. (P036).

**L1-6. Lacunas da busca.** Decisão do autor (P001 e P004).
- As três buscas suplementares (OpenAlex com proibição, embargo, apuração parcial e comparecimento; SciELO; BDTD com comparecimento) são análise nova.
- No texto: a 2.1 diz que as fontes atendem à recomendação 5 "só na forma". A 2.3 diz que as lacunas não foram corrigidas e que proibições e comparecimento são os mais expostos a perdas. A 4.3 chama a lacuna brasileira de lacuna também da busca, e a 5.3 pede a atualização com essas fontes. Uma nota em S2 explica o "no limite".

**L1-7. Relatos não recuperados e fluxo do texto completo.** Aceito em parte.
- Feito: a 3.1 e a 2.4 dizem que 165 dos 342 não recuperados vêm da triagem complementar de registros sem resumo. A 2.4 reconcilia os 184 avaliados: 165 decisões da IA (47 inclusões e 118 exclusões), 16 casos limítrofes do autor (8 e 8) e 3 exclusões em que a IA estendeu uma regra do autor. As somas fecham com os 55 incluídos e as 129 exclusões. A legenda da Fig. 2 separa o que o autor decidiu e explica que a Emenda 6b está no fluxo sem ramo próprio.
- Coordenador: o ramo da Emenda 6b e a caixa que separa autor e IA no diagrama (`preparar_dados_figuras.py`).
- Decisão do autor (sem pendência aberta): tabular os motivos de não recuperação e tentar meios legítimos (acesso institucional, empréstimo, contato com autores).

**L1-8. Protocolo, dados e código inacessíveis.** Decisão do autor (sem pendência aberta).
- Por instrução do coordenador, o repositório privado fica registrado como decisão do autor, sem mudar a política. A 2.1 e as Informações adicionais dizem que, sem depósito aberto, o leitor não pode conferir o protocolo nem o que foi decidido antes ou depois dos dados, e a disponibilidade diz, item a item, o que está fechado "por decisão do autor". Depósito com DOI, licença e código em R com versões ficam com o autor.

**L1-9. Checklists.** Aceito, a cargo do coordenador (erro E1).
- S11 está sendo preenchido por outro agente. Por instrução do coordenador, a 2.1 mantém a frase de que S11 dá o local de cada item.

**L1-10. Resumo e *Abstract*.** Aceito.
- Os dois trazem agora a faixa de n (de 12 eleitorados a 453.016 seções eleitorais; a faixa também está na 3.3), as limitações da evidência (de 1 a 4 estudos por célula, quase só laboratório e vinheta, todos os experimentos com algumas preocupações ou risco alto de viés) e a formulação única "Agentes de IA conduziram as etapas pós-protocolo, com decisões pontuais do autor". A apuração parcial aparece "por emenda", e a proporção e o IC estão nos dois.
- A decomposição dos 342 ficou na 3.1, porque o Resumo está no limite de 250 palavras (248 na medida mais severa).

**L1-11. Justificativa da abordagem rápida e S2.** Aceito em parte.
- Feito: a 2.1 diz que a variante rápida foi escolha do autor, sem outra justificativa no protocolo, que a consulta a *stakeholders* pesaria num debate com atores identificáveis, e cita o item "led only by experienced systematic reviewers". Uma nota na prosa de S2 reclassifica o prazo ("ainda não se aplica") e a recomendação 22 ("só em parte") e acrescenta o item do revisor experiente.
- Coordenador: a tabela de S2 vem de `insumos/garritty_2024.md` pelo `montar_suplemento.py` e não foi alterada.

**L1-12. Classificação das emendas.** Aceito em parte.
- Feito: a 2.1 diz que a Emenda 3 registrou uma decisão de método do autor (troca do árbitro por custo), que a Emenda 2 foi decidida pelo coordenador de IA e que as Emendas 1, 2, 4, 5 e 6b vieram depois de ver dados, a 4 depois da extração. A frase sobre o agrupamento amplo foi reescrita: ele é descritivo porque junta formatos e comparadores que o protocolo separa. A 3.6 diz que a Emenda 4b veio depois da extração. A prosa de S3 traz as três ressalvas, e a 2.7 e o glossário dizem que o alvo veio da Emenda 5.
- Coordenador: a legenda da Tab. 2 é gerada por `montar_revisao_final.py` e não foi alterada.

**L1-13. Notas de rebaixamento e imprecisão.** Aceito em parte.
- Feito: a 2.8 diz o limiar de cada juízo (zero para a direção; ±δ para a célula nula). A 3.3 declara o desvio de formato da Tab. 2 (18 comparações numa tabela, em quatro blocos). A 4.4 descreve as notas como genéricas e põe como quarta questão do autor a regra única de imprecisão nas células de 1 estudo: as sem medida de precisão desceram um nível, e as com IC que cruza zero, dois (conferido em `06-analise/certeza.csv`).
- Decisão do autor (P036): notas específicas por célula, regra única de imprecisão, divisão da Tab. 2, coluna de cenário e revisão de C02 à luz da meta.

**L1-14. C14.** Decisão do autor (P036 e P039).
- No texto, C14 saiu das Mensagens principais. A 3.7 diz que as 5.845 decisões vêm de mais de mil participantes (1.171 no fichamento, número que não está nas fontes da lista branca). Também diz que a extração não registra se o EP corrige o agrupamento, e que disso depende o rebaixamento por imprecisão. Conferir o EP e decidir a permanência da célula nas mensagens é do autor.

**L1-15. Frases de certeza.** Aceito.
- (a) "Permite descartar" saiu. (b) Nos trechos de destaque, a forma neutra "muito incerta sobre o efeito de X em Y". Os spans vêm de `certeza.csv` e não mudaram. (c) O resumo em linguagem simples abre com "as estimativas apontam a favor de quem aparece à frente, mas a evidência é muito incerta".

**L1-16. Metas exploratórias.** Aceito em parte.
- Feito: os valores de g saíram do Resumo executivo e da linha Escala da Tab. 4, que agora diz que as metas não informam o tamanho. A legenda da Fig. 6 declara a ordem alfabética e o risco de viés de cada painel. A 2.7 e a 4.4 declaram que não há IC de Wald ou de HKSJ nem IC para τ². Os g das metas voltam só na 4.1, no contraste de magnitude pedido por L2-2.
- Decisão do autor (P036): Wald e HKSJ como sensibilidade.
- Coordenador: ordenar por precisão (`preparar_dados_figuras.py`).

**L1-17. Painel da caixa.** Aceito em parte.
- Feito: o coordenador já refez o painel de S9 a partir de `celulas.json` (erro E2). No texto, a 2.8 diz que a "Força" traduz a certeza em palavras (insuficiente para muito baixa, fraca para baixa) e que o *script* leu só 8 das 18 células, sem mudar rótulos. A 5.1 explica por que o agrupamento amplo de apoio randomizado (9 de 9) não recebe rótulo direcional. A legenda da Tab. 4 diz o que é a Força.
- Coordenador (P042): o vocabulário da Força na tabela, que sai do *script*.

**L1-18. Recorte de 2010.** Aceito em parte.
- Feito: a 2.2 diz que o protocolo justificou o corte pela mudança do ambiente informacional, sem argumentá-lo, e que, aplicado ao ano de publicação, ele funciona como atualização da literatura, com estudos de dados anteriores. A 4.4 declara o intervalo de 2008 a 2009 como limitação, e a 4.2 diz que a comparação com a evidência anterior a 2010 fica fora do alcance.
- Decisão do autor (P039, onde está a regra de ano dos laboratórios): a regra única, pelo ano da coleta, da sensibilidade.

**L1-19. Resultados faltantes.** Aceito em parte.
- Feito: a 2.7 diz como o item 14 foi avaliado (domínio de viés de publicação do GRADE; sem teste de assimetria; sem busca em registros de pré-registro). A 3.8 diz que a lista de efeitos fora da contagem tirou do agrupamento o único randomizado contrário (@Gandhi2019).
- Decisão do autor (sem pendência aberta): a busca em registros (AEA, OSF, EGAP).

**L1-20. Itens de relato.** Aceito em parte.
- Feito: os excluídos limítrofes aparecem sem os sufixos de chave interna ("Kim 2018", "Kim 2025", "Mavridis 2016", "um segundo estudo de Morton e coautores, de 2015"), com a frase de que as referências completas ainda faltam. A deduplicação é atribuída à ferramenta de revisão (`rs.py`), e a 2.3 diz que as sementes estão só nos arquivos do projeto. A versão do clubSandwich foi para os métodos, e a do R ficou como **[A confirmar pelo autor]**.
- Coordenador: as referências dos excluídos (entradas `.bib` ou tabela no suplemento).
- Não feito, sem fonte registrada: data da versão do ROBINS-I V2, datas de acesso e parâmetros dos modelos. Decisão do autor, sem pendência aberta.

**L1-21. Declaração de IA.** Aceito em parte.
- Feito: (b) o termo de uso do provedor e quem pagou aparecem como "não registrados" (2.9 e declaração). (c) Justificativa: o uso de IA foi escolha do autor para uma revisão rápida. (d) Formulação única nos dois documentos: "as etapas depois do protocolo foram conduzidas por agentes de IA, com decisões pontuais do autor". (e) Datas passaram a 24/09/2026.
- Decisão do autor (P037): (a) os IC do κ e dos 58,5%, que são cálculo novo. A declaração diz "sem IC calculado".

**L1-22. "Célula principal" e soma de classes.** Aceito.
- "Alvo principal" nomeia a dimensão em todo o texto. Na 3.10, as contagens de realismo e de número de competidores vêm separadas por classe de desenho.

**L1-23. Tabela de transferibilidade.** Aceito em parte.
- Feito: a 5.2 diz que a transferibilidade "foi examinada" e que "o juízo de preocupação por fator ficou para o autor"; a legenda da Tab. 5 diz o mesmo.
- Decisão do autor (sem pendência aberta): a fonte primária do voto obrigatório (CF, art. 14), que não está em dossiê verificado e por isso não entrou, e a busca por uma medida publicada de confiança nas pesquisas.
- Decisão do autor (P036): o juízo por fator.

## L2, cientista político

**L2-1. A direção *bandwagon* mistura canais.** Aceito em parte.
- (a) Feito:
  - Mensagens, Resumo, *Abstract*, Resumo executivo e Conclusões falam em "a favor de quem aparece à frente". O glossário e a 2.7 dizem que "*bandwagon*" é rótulo operacional, compatível com E3 e E4 e com coordenação estratégica (E2), sem separação quando o estudo não tem alvo de viabilidade.
  - A 3.4 dá a leitura dos autores estudo a estudo, conferida no fichamento: @Tyszler2015, coordenação estratégica em pluralidade com três opções; @Agranov2017a, maioria que vota mais e minoria que vota menos, atribuídas à pivotalidade e ao desejo de votar no vencedor; @Tal2015a, compromisso estratégico e voto no líder como opção padrão; @Witsman2016a, voto estratégico. Diz também que o E5 quase não opera em jogos com pagamento induzido.
  - A contribuição (ii) foi corrigida, e a linha E2 da Tab. 3 diz que dois testes estão nas células de apoio principal. A 3.10 aponta os estudos com dois competidores como o teste mais limpo.
  - Os enunciados da Tab. 2 e os títulos da Fig. 4 vêm de `certeza.csv` e dos *scripts* e mantêm "*bandwagon*".
- (b) Decisão do autor (P037, alvo e comparador; P036): levar @Agranov2017a à mobilização e @Tyszler2015, @Tal2015a e @Witsman2016a a célula de coordenação ou de viabilidade. Entrou como item (ii) das decisões em aberto da 3.8.

**L2-2. Validade externa e @Farjam2020a.** Aceito em parte.
- Feito: @Farjam2020a é descrito como "votação experimental *online* sobre organizações políticas reais, com prêmio para a mais votada e sem eleição em curso", conferido no fichamento, na 3.4, 3.10 e 4.3, na Tab. 4, na legenda da Fig. 7 e na linha R3 da Tab. 3. A 3.10 diz que nenhum estudo do alvo principal mede pesquisa pré-eleitoral numa eleição real. "Rareia" e "depende" saíram (L1-3). A 4.1 traz o contraste descritivo de magnitude (g de 0,12 a 0,19 nos *surveys* com partidos reais; 0,48 e 0,62 nas metas de laboratório e vinheta), com a ressalva das medidas. A comparação com Barnfield ficou "compatível, sem confirmá-la", e a R3 registra a confusão com o formato.
- Não usei as diferenças de 15 a 30 pontos citadas por L2, porque esses números não estão nas fontes da lista branca.
- Decisão do autor (P037): reclassificar o realismo de @Farjam2020a, item (ix) da 3.8.

**L2-3. Comparecimento sem teoria do sinal.** Aceito em parte.
- Feito: a 1.2 descreve pivotalidade, efeito "Titanic" e mobilização de quem está atrás e declara que o modelo do protocolo não os tem; a legenda da Fig. 1 diz o mesmo. O glossário usa definição neutra ("a teoria prevê os dois sinais"). A 3.7 diz que ver × não ver não tem sinal previsto. C18 aparece como associação observacional em dois contextos europeus (3.7, Resumo executivo, Conclusões e linguagem simples). A 4.1 lê C13 e C14 juntas pela teoria rival do artefato. A linha E7 da Tab. 3 começa pelo desenho mais forte. C14 e C18 saíram das Mensagens (decisão editorial).
- Decisão do autor: dizer o que as pesquisas mostravam e para quem, nas células ver × não ver, que o fichamento não registra de modo uniforme (P039); separar células pelo conteúdo ou pelo lado do eleitor, e o GRADE de C18 (P036).

**L2-4. δ de 2 p.p. e "trivial".** Aceito em parte.
- Feito: "trivial" saiu de todo o texto fora do span de C13, que vem de `certeza.csv` e não pode mudar. O glossário, o Resumo executivo, a 4.3 e a linguagem simples dizem que efeitos menores que δ podem decidir eleições apertadas e que a classificação nada diz sobre eles. @Gerber2020a vem em pontos percentuais (0,29 p.p.).
- Não entrou a margem do segundo turno de 2022, que não está em dossiê verificado.
- Decisão do autor: o IC de @Gerber2020a em p.p., que é conversão nova (P039); o valor de δ e a palavra "trivial" no enunciado (P036).

**L2-5. Lacuna brasileira como lacuna da busca.** Aceito.
- O texto diz "nesta busca" nas Mensagens, no Resumo executivo, na 1.4, na 4.3 ("A lacuna é também da busca, que não incluiu a SciELO, âncoras em português ou espanhol, a leitura de periódicos e anais brasileiros nem consulta a especialistas"), na 5.2, nas Conclusões e na linguagem simples.
- Decisão do autor (P001 e P004): a busca suplementar.

**L2-6. Regras do dia da eleição.** Aceito, com a seção 7 de `contexto_brasil.md`.
- A 1.1 traz a Res.-TSE nº 23.600/2019, art. 12, na redação de 2024 (divulgação de levantamento do dia só a partir das 17h de Brasília), o crime de "boca de urna" (Lei nº 9.504/1997, art. 39, § 5º, II), a unificação do horário em 2022 (votação e divulgação a partir das 17h de Brasília) e o início da divulgação às 19h de Brasília em 2018.
- A 5.2 e a linha de regulação da Tab. 5 dizem que as proibições estudadas na França e na Índia correspondem a uma regra que o Brasil já aplica, e que @Araujo2021a informa sobre a brecha do voto na fila. O glossário e a 1.1 fixam "pesquisa de boca de urna".
- Três chaves novas de `referencias_contexto.bib`; `preparar_referencias.py` rodado.

**L2-7. Frase-síntese sobre regulação.** Aceito.
- Nas Mensagens, no Resumo executivo, na 5.2, nas Conclusões e na linguagem simples: "Sozinha, a evidência não demonstra que a divulgação de pesquisas muda votos, nem que é inócua". A 5.2 e o Resumo executivo acrescentam que a consequência depende de quem carrega o ônus da prova, escolha jurídica e normativa, e que o STF decidiu em 2006 sem depender de prova sobre o efeito.

**L2-8. Base teórica.** Aceito em parte.
- Feito: o glossário ganhou a linha "Alvo do efeito", que liga cada alvo à tipologia de Barnfield. A 1.2 e a legenda da Fig. 1 separam percepção de popularidade (E3 e E4) e de viabilidade (E2).
- Decisão do autor (sem pendência aberta): as referências clássicas (Simon; Downs; Riker e Ordeshook; Cox; Forsythe, Myerson, Rietz e Weber; Mutz; Bartels; Noelle-Neumann). L2 as cita de memória, elas não estão em dossiê verificado nem nos `.bib` e dependem de conferência. Mudar o modelo lógico do protocolo também é do autor.

**L2-9. Revisões anteriores.** Aceito.
- A 1.3 cita a meta-análise de Hardmeier e Roth pela menção de @MoyRinke2012, dizendo que não foi lida, com a ressalva de amostra concentrada nos Estados Unidos. A 4.2 discute os achados antigos de *underdog* e a possível razão de desenho. "Nenhuma revisão sistemática ou meta-análise dedicada" substituiu "síntese", e "sem outro do mesmo tipo na busca descrita" substituiu "a primeira". A contribuição sobre o comparecimento entrou na 4.2 (na amostra de Barnfield, só 10 artigos discutem mobilização; aqui, 17 estudos medem o comparecimento).
- O total de 65 artigos não entrou, porque não está nas fontes da lista branca.

**L2-10. Recorte de 2010.** Aceito em parte.
- Como em L1-18. Mudar o critério é decisão do autor (sem pendência aberta).

**L2-11. "Num país de voto facultativo".** Aceito. A 5.2 diz "num experimento de campo nos Estados Unidos, onde o voto é facultativo".

**L2-12. Dados brasileiros de transferibilidade.** Aceito em parte.
- Feito: a 5.2 e a Tab. 5 ligam os dois turnos ao voto útil a que @PereiraNunes2024 atribuem parte da distância de 2022.
- Decisão do autor (sem pendência aberta): a Constituição e a abstenção do TSE para o voto obrigatório, que não estão em dossiê verificado; Cox (M+1), Kiss e Simonovits, e a literatura de credibilidade das pesquisas (Kuru, Pasek e Traugott; Madson e Hillygus), que L2 cita de memória.

**L2-13. @Araujo2021a.** Aceito em parte.
- Feito, conferido no fichamento: a 3.4 diz que o desfecho é a parcela do candidato em toda a urna, e não só nos votos dados depois da divulgação. A 5.2 troca "falhas" por "atrasos da identificação biométrica", que deixaram eleitores na fila. A 3.9 acrescenta a ressalva de composição de quem vota tarde.
- Decisão do autor (P039): a fração de eleitores expostos, que exige ler o estudo.

**L2-14. Ligação com o debate brasileiro.** Aceito em parte.
- Feito: (a) a 5.2 diz que as justificativas dos PLs não foram examinadas. (b) O E8 e @Boukouras2020a entraram na 5.2, com certeza muito baixa, ligados ao registro prévio e ao crime de pesquisa fraudulenta. (c) A implicação para a imprensa menciona o enquadramento (@Meer2015a; @Stolwijk2016a).
- Decisão do autor (sem pendência aberta): examinar as justificativas dos PLs.

**L2-15. Contrafactual regulatório e canal das elites.** Aceito.
- A 5.3 (ii) pede comparadores com pesquisa antiga e outras pistas, para embargos, e com outro resultado, para as propostas sobre precisão. A 4.3 declara o canal das elites (doadores, imprensa, alianças, desistências) como limite de aplicabilidade.

**L2-16. @Gerber2020a mede proximidade.** Aceito. A 3.9 e as linhas E1 e R2 da Tab. 3 falam em crença sobre a proximidade da disputa, com a compatibilidade com a R2 restrita ao comparecimento.

**L2-17. Clareza.** Aceito em parte.
- Feito: a frase sobre @Witsman2016a saiu das Mensagens, e o parêntese opaco saiu do Resumo. A 3.11 foi reduzida a duas frases. Os pontos percentuais aparecem onde as fontes os trazem (@Gerber2020a, @Dahlgaard2016a, @Schlegel2023, @Araujo2021a, @Morton2015a).
- Não feito: um parágrafo novo de tradução de termos no início dos Resultados, porque o @qdr-glossario já faz esse papel e o corpo tinha de encolher; e p.p. ao lado de todo g, porque a maioria dos valores não está nas fontes da lista branca.

**L2-18. Resumo em linguagem simples.** Aceito.
- "A revisão em resumo" usa "as estimativas apontam a favor de quem aparece à frente" e o comparador "e não folgada". O texto diz que parte do padrão pode vir do voto estratégico, qualifica o estudo de comparecimento como "em dois estudos na Europa, sem sorteio", diz que efeitos menores que 2 em 100 podem decidir eleições apertadas e fala da lacuna da busca. O título já tinha a forma certa (L1-15) e foi mantido.

## Verificação independente (`verificacao_v2.md`)

**Erros**

- **E1** (S11 anunciado e vazio): a cargo do coordenador e do agente que preenche S11. Por instrução do coordenador, a 2.1 manteve a promessa de que S11 dá o local de cada item.
- **E2** (painel da caixa em S9): corrigido pelo coordenador em `montar_suplemento.py`. O texto da 2.8 e da 5.1 foi alinhado (V1).
- **E3** ("o maior experimento de campo"): corrigido. A 4.1 diz "O único experimento de campo indica que [...] provavelmente não muda [...] (certeza moderada)".
- **E4** (17 × 16 casos limítrofes): corrigido na 2.4 e na 2.9 ("16 casos limítrofes [...]; 17 registros no *log*, um deles de teste"), com nota na prosa de S2. A tabela de S2 (fonte `insumos/garritty_2024.md`), a Emenda 6a e `relatorio.qmd` ficam com o coordenador.

**Avisos**

- **V1**: corrigido (2.8 e 5.1).
- **V2**: corrigido (2.1).
- **V3**: corrigido (4.1). As células não randomizadas vêm com 1 ou 2 estudos e certeza muito baixa, e a comparação entre classes é declarada sem teste.
- **V4**: corrigido (4.1, "ficam de pé em termos modestos, e todas dependem da validação humana"; "sugere, numa comparação descritiva e *post hoc*").
- **V5**: corrigido (Resumo executivo e 3.7, com "provavelmente" e o contexto das eleições para governador).
- **V6**: corrigido (linguagem simples).
- **V7**: corrigido. "Efeitos grandes" virou "+11,76 pontos percentuais no apoio" e "−11 pontos no comparecimento" (3.10).
- **V8**: corrigido. A ressalva está junto dos p < 0,05 na 3.8 ("Esse p, como os demais desta seção [...]"), na 5.1 ("no teste de sinal *post hoc*") e na prosa de S8.
- **V9**: corrigido. A 2.7 e a 2.8 não chamam mais figuras e tabelas antes da ordem.
- **V10**: em parte. A legenda da Fig. 6 declara a ordem (alfabética) e o risco de viés de cada painel; ordenar por precisão fica com o coordenador (`preparar_dados_figuras.py`).
- **V11**: em parte. A legenda da Fig. 2 separa autor e IA, explica a Emenda 6b e diz que as caixas com n = 0 não se aplicam; tirar as caixas fica com o coordenador.
- **V12**: em parte. Os sufixos saíram e a falta das referências está dita; as referências ficam com o coordenador.
- **V13**: corrigido (Resumo e *Abstract*).
- **V14**: fora dos arquivos editáveis (`07-relatorio/relatorio.qmd`); coordenador.
- **V15**: HTML e .docx desatualizados e mancha do PDF são do coordenador (render e `typst-template.typ`). O render Typst desta revisão saiu sem aviso, mas `verificar_pdf.py --artigo` ainda reprova 5 páginas, nos mesmos blocos largos de antes (pp. 5, 11, 14, 19 e 25).
- **V16**: corrigido ("Nenhum, por declaração do autor no protocolo. Relação com o provedor das ferramentas de IA: **[A confirmar pelo autor]**").
- **V17**: em parte. clubSandwich 0.7.0 foi para a 2.7, e a versão do R ficou **[A confirmar pelo autor]**; a da ferramenta de revisão não está registrada.

**Ok com ressalva**

- **R1**: justificado, sem mudança. "0,97" ficou para bater com a Tab. 2 e S8, que saem do formatador; a troca por "0,98" em todos os lugares depende de corrigir `gerar_celulas.py` e os montadores (coordenador).
- **R2**: corrigido. Artigo, linguagem simples e declaração de IA passam a 24/09/2026. S2 vem da fonte do coordenador, que deve confirmar a data no dia da publicação (há um comentário no esqueleto).
- **R3**: corrigido (Resumo executivo, 3.10 e Tab. 5: "tem voto obrigatório codificado", com 2 sem e 9 sem a informação).
- **R4**: corrigido por simplificação: "em 24/09/2026, nenhum dos dois tinha sido votado em plenário".
- **R5**: corrigido (CRediT: "entre elas a Emenda 4 e a troca do árbitro, **[A confirmar pelo autor]**").
- **R6**: justificado. As três leituras e a rubrica existem agora; o comentário para conferir na etapa 7 ficou.
- **R7**: em parte. Nota na prosa de S3; a tabela vem de `montar_suplemento.py` (coordenador).
- **R8**: corrigido (Tab. 3, linhas E7 e R2).
- **R9**: corrigido (3.10, agora por classe de desenho).
- **R10**: corrigido (2.7, "3 estudos em cada nível de um moderador").
- **R11**: corrigido ("efeito na média" na 1.2 e na linha R1 da Tab. 3; a 2.7 diz "tamanho do efeito").
- **R12**: corrigido. O aviso inicial diz que esta versão responde às leituras sem mudar a análise e remete ao "O que mudou".
- **R13**: corrigido (2.9 e declaração: justificativa, quem pagou e termos "não registrados").
- **R14**: declarado na 3.3 como desvio de formato.

## Auditoria (`auditoria_final.md`), itens parciais e não cumpridos que dependem do texto

| Item | Situação depois desta revisão |
|---|---|
| A1 | Legenda corrigida (V11); caixas zeradas e ramo da 6b ficam com o coordenador |
| A2 | E3, E4, V6 e datas corrigidos; E2 feito pelo coordenador; V14 e V15 com o coordenador |
| A3 | Resolvido (V3, V5, E3) |
| A4 | Texto alinhado (V1); o *script* da caixa célula a célula fica na P042 |
| A5 | Ordem e risco de viés declarados na legenda (V10); reordenar é do coordenador |
| A8 | Parcial (V12); referências dos excluídos com o coordenador |
| A10 | V16 e R13 resolvidos; acesso, licença e *links* publicados ficam com o autor e o coordenador |
| A11 | Resumo resolvido (V13); S11 com o coordenador |
| A15 | Parcial (V17): versão do R marcada para o autor |
| A16 | Resolvido: "efeitos grandes" (V7) e "estudos pequenos", agora "de n entre 12 e 1.113 em unidades diferentes" (3.8) |
| A17 | Resolvido (R11) |
| A20 | Resolvido (V9) |
| A21 | Depende do autor (P038) |
| A22 | O passe de estilo é a etapa 7; "ajustado ao estilo do autor" saiu do aviso e da 4.4 até lá, com comentário para o coordenador recolocar |
| A23 | Resolvido (V3 a V6, E3) |
| A25 | Resolvido (V8) |
| A28 a A31, A33, A36 | Dependem de depósito, licença e código; decisão do autor, registrada nas Informações adicionais |
| A32 | Texto alinhado; *script* na P042 |

## Rubrica cega e metatexto

- **M07**: nos trechos de destaque (Mensagens, Resumo executivo, Resumo, 4.1 e Conclusões) não restam "permite descartar", "é evidência de que", "a direção dominante é" nem "domina". A 3.10 também perdeu o "domina". As conclusões de efeito usam a contagem seguida da frase GRADE.
- **M08**: a 2.7 declara o estimando por classe pela regra congelada do *codebook*: efeito causal da designação nos randomizados (ATE ou ITT); ATT na diferença-em-diferenças sem sorteio; associação no antes e depois só nos tratados, na interação com moderador não sorteado e na regressão com controles. A 4.1 diz que as classes estimam coisas diferentes e apontam para o mesmo lado na maior parte das células, sem teste. A 3.10 não soma classes.
- **Metatexto**: saíram os "Resolvem P0xx" da 4.4 e a narração da reescrita. As 11 caixas de pendência e os marcadores [A confirmar pelo autor] ficaram: eram 4 e agora são 6, com a versão do R e a relação com o provedor.

## Enxugamento e travas

- Palavras de prosa do corpo (seções 1 a 6), sem spans, caixas, quadros, legendas e tabelas: 11.365 antes e 10.367 depois (11.478 e 10.480 contando os títulos de nível 2). Informações adicionais: 1.201 antes e 885 depois.
- Os cortes foram, em ordem: redundância entre seções (Resultados × Discussão × Conclusões), detalhe de procedimento que já está no suplemento (cruzamento com a diretriz → S2; conversões → S6; regra da caixa → S9) e explicações.
- Pela trava, as Mensagens têm 196 palavras, o Resumo 248 e o *Abstract* 246, sem as palavras-chave, na medida mais severa. O resumo em linguagem simples tem 741 e a "A revisão em resumo", 50.
- `montar_revisao_final.py`: OK.
- `conferir_reestruturacao.py`: 0 falhas e 0 avisos.
- Render Typst: sem aviso.
- `verificar_figuras.py`: OK.

## Verificação final (`verificacao_final.md`)

Etapa 8b, 24/09/2026. O erro e os cinco avisos foram corrigidos com o texto exato que a verificação propõe, e nenhum ficou sem aplicar.

- **E1**: no resumo em linguagem simples, "Depois de 2022" passou a "Em outubro de 2022".
- **V1**, que é também a ressalva R11 da `verificacao_v2.md`: na 1.2, "efeito médio" voltou a "efeito na média".
- **V2**: o § 3 da 4.1 traz a frase proposta. Ela diz que os g dos *surveys* e das metas têm IC que cruza zero, que as metas não informam o tamanho e que o contraste só é compatível com a teoria rival do artefato, sem testá-la.
- **V3**: na 5.2, a divulgação seletiva leva a frase padrão ("a evidência é muito incerta sobre esse efeito (certeza muito baixa)").
- **V4**: na 3.10, a frase sobre proximidade e comparecimento diz que dois dos três estudos só têm efeitos fora da contagem, sem GRADE, que o terceiro está numa célula de certeza muito baixa e que o padrão não aparece no experimento de campo de Gerber et al. (2020) (certeza moderada).
- **V5**: `Holst2025PRISMAtrAIce` e `Moher2026PRISMAtrAIce` entraram em `referencias_metodo.bib`, com os metadados conferidos no Crossref e registrados em `prompts_v2/log_referencias_metodo.md`. Elas são citadas na legenda de S11 (`montar_suplemento.py`) e no PRISMA-trAIce da 2.1.
