# Notas do coordenador — extração completa (G7)

## Pendências abertas para resolver depois das ondas de fichamento

- **Freden2016b**: o PDF em `03-textos/pdfs/Freden2016b.pdf` é só o "kappa" (capítulo introdutório) da tese de doutorado por compilação; os quatro artigos empíricos (incluindo o Artigo 2, o survey experiment com pesquisas manipuladas na Suécia 2013/2014, que é o desenho relevante para o protocolo) não estão no arquivo — só o sumário nas páginas impressas 47, 69, 95 e 125. A ficha ficou com quase todo o bloco 13 em 999 por essa razão, não por falha do fichador. Ação necessária: localizar e baixar o Artigo 2 (capítulo publicado em livro Springer sobre "Voting Experiments", segundo a própria tese) ou a tese completa com os quatro artigos, e refichar.

## Correções de gate feitas pelo coordenador (rodada completa, antes de refazer com subagente novo)

O gate (`verify_citacoes.py`) reprovou 11 citações em 9 fichas na primeira passada. Conferi cada uma contra a camada de texto do PDF e corrigi diretamente (sem novo subagente, por serem erros pontuais de transcrição/paginação, não de conteúdo):

- Agranov2017a (mecanismo_id): página errada (p. 2 → p. 3, mesmo offset).
- Alabrese2024a (mecanismo_tipo_evidencia): citação cortada bem na hifenização de fim de linha ("media-"); completada para "mediator".
- Chatterjee2019a (pais_estudo, regiao): a ficha "corrigiu" o erro de digitação do próprio PDF ("Arunchal" → "Arunachal"); restaurada a grafia impressa.
- Cornejo2023a (problema_pesquisa): faltava a palavra "that" presente no original.
- Farjam2020a (outcome_medida): "based on" no lugar de "by", presente no original.
- Gasperoni2015a (populacao + nota do codificador): a ficha registrou "thorough" como o erro de digitação verbatim, mas o PDF traz "thorugh" (typo diferente); corrigido e a nota do codificador também.
- Morton2015a (b2_estimando): ordem de palavras trocada ("difference-in-difference (DID) estimator" → "difference-in-difference estimator (DID)", como impresso).
- Schlegel2023 (construto_outcome, alvo_efeito): faltava "the" antes de "Candidate".

**Aceito sem correção, com justificativa (mesmo critério do piloto G6):** Araujo2021a, `b2_n_total` — o número (452.656) só existe rasterizado dentro da Figura 2, sem camada de texto; conferido visualmente pelo coordenador, é o mesmo caso documentado em `05-decomposicao/piloto/notas_gate.md`.

## Lammers2022a: os efeitos extraídos não isolam o efeito principal da exposição

Os Estudos 2a/2b cruzam dois fatores manipulados: a posição mostrada na pesquisa (90% vs. 10%
de apoio ao candidato preferido, a exposição do protocolo) e o modo de raciocínio induzido
(heurístico vs. moral-igualdade). Os autores não reportam o efeito principal nem o efeito
simples da posição isoladamente — só a interação e o efeito simples do MODO dentro de cada
posição (heurístico vs. moral-igualdade, condicionado à posição mostrada). Os dois `d` extraídos
como `modelo_principal` (E01: d=0,73; E03: d=0,58) medem, portanto, o efeito do modo de
raciocínio sob exposição, não o efeito da exposição em si.

Isso é uma limitação do que o próprio artigo reporta, não um erro de extração. Fica registrado
para a síntese (G8): considerar excluir Lammers2022a da meta-análise do efeito principal de
`apoio_ao_lider` (célula pesquisa_pre_eleitoral, survey experiment) ou tratá-lo só como
evidência de mecanismo/moderador na síntese narrativa, com a ressalva explícita de que os
tamanhos de efeito disponíveis não isolam a exposição à pesquisa.

## Correção de instrução minha: Brugarolas2021

Instruí o extrator de efeitos com `outcomes: apoio_ao_lider`, mas este texto mede só
`mobilizacao` (intenção de comparecer) — erro meu, não conferi a ficha antes de montar o
prompt. O subagente corrigiu sozinho, com base na própria ficha e no protocolo, e registrou
`construto_outcome = mobilizacao` corretamente. Também ajustei `estimando` de `RDD_local` para
`ITT` no CSV de efeitos, para ficar consistente com a ficha (o texto discute explicitamente
"could be treated as an intention to treat (ITT) effect", que tem prioridade sobre RDD_local na
ordem da Emenda 2).

## Convenção or_=exp(beta) para coeficiente logit sem OR impresso — não uniformizada

Cornejo2023a apontou uma inconsistência real: Meer2015a e Cornejo2023a calcularam
`or_ = exp(beta)` quando o texto só imprime o coeficiente logit (log-odds) e o EP, sem razão de
chances; Geers2018 deixou `or_` vazio no mesmo tipo de situação. Verifiquei os valores: em
Meer2015a e Cornejo2023a os coeficientes são de magnitude plausível para log-odds (ordem de
0,1 a 2,4), e `exp(beta)` é uma transformação exata, não uma invenção — mantive a convenção.
Em Geers2018 os coeficientes são -30,8 e -5,7, associados a um preditor contínuo de escala
estreita (DP ≈ 0,21): `exp(-30,8)` daria uma razão de chances implausível. Não uniformizei às
cegas. Decisão: deixar como está e deixar o alerta de plausibilidade de `analise
verificar-efeitos` (|g| > 2) sinalizar Geers2018 quando a etapa rodar, para conferência humana
específica desse caso (conferir se o EP foi lido como DP, a unidade do preditor, ou se o
coeficiente reportado é de fato log-odds por unidade cheia do índice 0-1).

## Retomada em 23/09/2026: sobreposição de dados entre estudos incluídos

- **Agranov2012a ↔ Agranov2017a: mesmo estudo, não estavam ligados.** Mesmo título, mesmos
  quatro autores, mesmo experimento (198 sujeitos, 440 eleições); 2012a é o manuscrito de
  dez/2014 (registro SSRN) e 2017a o WZB DP de set/2016 (registro do artigo JEEA). Ligados
  com `textos ligar-relatos` (03-textos/pares_relatos_g7.csv), relato principal Agranov2017a.
  Os estudos incluídos passam de 41 para 40. Os efeitos já extraídos de Agranov2012a saem de
  `05-decomposicao/efeitos/` (vão para `efeitos_descartados/`) quando os de Agranov2017a
  estiverem prontos, para não contar o mesmo experimento duas vezes.
- **Meffert2012a contém os dados de Meffert2011.** O capítulo reúne três experimentos; o
  "psicológico" (laboratório em Mannheim, janeiro de 2006, duas campanhas estaduais alemãs,
  voto insincero) é o experimento publicado em Meffert2011. Na extração de efeitos de
  Meffert2012a entram só o experimento econômico e o survey experiment austríaco; o psicológico
  fica com Meffert2011.
- **Tyszler2013 reusa dados de Tyszler2015.** As comparações com eleitorados homogêneos em
  Tyszler2013 usam dados do artigo-companheiro (TS11 = Tyszler2015). Na extração de efeitos de
  Tyszler2013 entram só os dados heterogêneos próprios.
- Correção do meu commit anterior: a lista de "17 estudos sem efeitos" incluía Westwood2020a
  por engano (já tinha efeitos); eram 16 mais Freden2016b.

## Polaridade de desfechos de apoio a quem está atrás: harmonizar antes do G7

O codebook manda: desfecho que mede apoio a quem a pesquisa mostra atrás continua
`apoio_ao_lider`, com `direcao_desejada = reduzir` e sinal como impresso. Alguns extratores
inverteram o sinal em vez disso (Araujo2021a E02-E09, Lammers2022a E02/E04) — matematicamente
equivalente se `direcao_desejada = aumentar`. Outros deixaram o sinal como impresso e só
avisaram (Bursztyn2023a E17/E18). Antes de `preparar-efeitos` final, conferir linha a linha que
toda linha de apoio a quem está atrás tem OU sinal invertido com `aumentar` OU sinal impresso
com `reduzir` — nunca sinal impresso com `aumentar`. A partir desta retomada os prompts dos
extratores fixam a segunda forma.

## Notas da retomada, por estudo (para a verificação e a síntese)

- **Witsman2016a**: p1/p0 calculados pelo extrator das contagens Yes/Total impressas nas
  Tabelas 6 e 8 (divisão exata, mas não é número impresso) — conferir na verificação humana.
  E05 é um phi omnibus 5x2, não direcional: não usar na agregação.
- **Alabrese2024a**: 132 linhas. As linhas do survey com desfecho "não apoia nenhum partido"
  (Tab. 4, A.8-A.10) foram classificadas pelo extrator como `mobilizacao`/`reduzir`, mas o
  protocolo define mobilização como comparecimento ou intenção de comparecer (interesse só como
  complemento). Não entram na agregação de mobilização; o principal de mobilização é E002
  (Tabela 2, col. 2, comparecimento). Exposição contínua (margem nacional 0-1), sem tratamento
  binário: a conversão para d não é comparável com os experimentos.
- **Tyszler2015**: a Figura 4 não imprime valores; os números vêm das faixas da conclusão
  (72-88% sem informação, 93-96% com informação), que se referem às barras "Majoritarian Set"
  e não "Majoritarian Candidate". A ligação de cada ponta da faixa a uma condição (u=3, u=8) foi
  feita pelo extrator lendo o gráfico, e no braço informado a ordem 93/96 vem só do gráfico.
  Conferência visual humana obrigatória; sem EP nem teste — entra na síntese narrativa (SWiM),
  não na meta-análise.
- **Boukouras2020a**: E04-E06 ("vote share" 20/11,7/7,3 p.p.) são numericamente idênticos às
  diferenças de taxa de vitória de E01-E03 — possível erro de rótulo dos próprios autores;
  marcados nao, não agregar junto com E01-E03.
- **Meffert2012a**: sem o experimento psicológico (que é o de Meffert2011), sobram 4 linhas do
  experimento econômico cujo desfecho é "decisão ótima" (maximiza o pagamento), sem relação
  definida com apoio ao líder; o survey austríaco só varia o sinal de coalizão, sem pesquisa.
  Nenhuma linha principal: o estudo entra só na síntese narrativa.
- **Yang2023d** e **Urminsky2019**: os contrastes disponíveis são entre FORMATOS de apresentação
  da mesma previsão (intervalo vs. dotplot; chance vs. margem), não exposição vs. não exposição
  nem resultados diferentes. Yang2023d ficou sem linha principal (7 linhas nao); Urminsky2019
  tem 1 principal (Estudo 1, chance vs. margem). Célula própria na síntese (formato da previsão),
  não agregar com os experimentos de exposição.
- **Gandhi2019**: dois principais (um por braço, interações triplas DAP e BERSATU); o p impresso
  é maior que o calculado por z=beta/EP (t com poucos gl por cluster no estado) — o verificador
  pode acusar incoerência de p, que é esperada aqui.

## Harmonização de polaridade aplicada (23/09/2026)

Conferi todas as linhas `apoio_ao_lider` cujo desfecho sugere apoio a quem está atrás.
Corrigido para `direcao_desejada = reduzir` (sinal como impresso):
- Bursztyn2023a E17, E18 (parcela de votos do lado atrás; E17 é o principal) — estavam `aumentar`.
- Chatterjee2019a E03-E06, E09-E12 (segundo colocado e demais candidatos) — estavam `aumentar`.
  O sinal destas linhas continua trocado em relação ao impresso por outro motivo, legítimo: o
  artigo estima o efeito da PROIBIÇÃO da boca de urna, e a linha registra o da exposição.
- Cornejo2023a E05-E18 (survey experiment: apoio ao candidato anti-PRI mostrado atrás do PRI na
  vinheta; E05 é o principal do experimento) — estavam `aumentar`.
- Araujo2021a E02-E05, E07-E09: tinham o sinal invertido por polaridade com `aumentar`;
  restaurado o sinal impresso e posto `reduzir` (mesmo resultado, mas agora o número bate com a
  página para a conferência humana).
Mantidos como estão, com ressalva: Lammers2022a E02/E04 (reorientados pelo extrator; o estudo
já está marcado para não entrar na agregação do efeito principal); Gasperoni2015a E01 e
estratos (misturam os dois alvos de troca, líder e segundo colocado); Tyszler2013 E01/E02
(fração de voto estratégico mistura deserções para o líder e para outro candidato).

## Agranov2012a fora da rodada completa

Ficha movida para `05-decomposicao/fichas_relatos_secundarios/` e efeitos para
`efeitos_descartados/`: é relato secundário do estudo ES1529 (principal Agranov2017a).

## Moderadores por efeito e complementação (23/09/2026)

- O protocolo (seção 6) pede, depois de `se_pp`, as colunas `comparador_tipo`, `alvo_efeito`, `desenho_fino`, `regiao`, `tipo_eleicao`, `realismo_contexto`, `ano_eleicao_pre2010` e `sistema_eleitoral`; a célula de meta-análise usa também `familia_intervencao`. Os extratores não as gravaram. O coordenador as acrescentou por script (cópia dos CSVs anteriores em `efeitos_backup_pre_moderadores/`):
  - as de nível de estudo vêm do `fichamentos_master.csv`, com "outro — especifique" normalizado para `outro`; `ano_eleicao_pre2010` = `sim` só quando `ano_eleicao` < 2010 (999, eleição abstrata, vira `nao`);
  - `alvo_efeito` e `comparador_tipo` vêm do master quando ele tem um só valor; linhas de `mobilizacao` recebem `alvo_efeito = nao_se_aplica`; `comparador_tipo = outro` quando o master diz "outro".
- 136 linhas de 12 estudos com vários alvos ou comparadores no master, e 19 efeitos principais sem os dados que a conversão exige (p0, n por braço, sdy, EP), foram despachados a subagentes Opus com `prompt_complemento_efeitos.md` (lista em `_complemento_efeitos.json`). Cada alteração fica registrada com trecho e página em `complementos_efeitos/<chave>.json`.
- Efeitos principais com estimando de associação (Feltovich2022 E01–E02, Fichnova2015a E01 e E05, Gasperoni2015a E01, Geers2018 E01, Lago2015 E01, Stolwijk2016a E01, Unkelbach2022a E02) ficam fora das meta-análises e entram só na SWiM e na síntese por direção (protocolo, seção 8, 15a). Por isso não foram complementados.
- **Decisão pendente para a síntese (conglomerados sem ICC).** `efeitos.R` só aplica o efeito de desenho 1 + (m − 1)·ICC com `cluster` e `icc` preenchidos; sem eles, avisa que a variância está subestimada. Os experimentos de laboratório por sessão ou grupo não relatam ICC. Exemplo: Agranov2017a E13 usa n1 = 160 e n2 = 140 eleições (8 e 7 grupos × 20 períodos, derivado pelo subagente e conferido na Tabela 5). Proposta, a declarar como desvio do protocolo: `cluster` = tamanho médio do grupo ou número de rodadas por grupo, ICC imputado 0,05 na análise principal e 0,20 na sensibilidade (Cochrane Handbook, cap. 23, ICC emprestado com sensibilidade).
- Agranov2017a E13–E26: `alvo_efeito = lider`, com a ressalva do subagente de que o desfecho é a vitória da alternativa favorecida pela maioria realizada, que em geral, mas nem sempre, coincide com a mostrada na pesquisa.
- Brugarolas2021 E01: `p0 = 0,849` lido nas coordenadas vetoriais da Figura 2 (o apêndice com as tabelas não está no PDF); a mesma leitura reproduz o efeito impresso (5,0 frente a 5,1 p.p.). Valor de figura: vai para a sensibilidade.
- Araujo2021a E06: `p0 = 0,49` derivado do ganho relativo impresso (11,76 p.p. / 24%).
- Dahlgaard2016a: E03 e E06 (artigo de ganho × artigo de perda) passaram de `sem_pesquisa` para `outro_resultado` (coordenador, apontado pelo subagente: o estudo tem grupo de controle, e esses dois são contrastes entre resultados). As linhas dos Social-Democratas (inclusive o principal E01) ficaram com `alvo_efeito = nao_se_aplica`: o tratamento mostra ganho ou perda do partido, não sua posição. **Decisão pendente:** efeitos de *momentum* (ganho × perda) entram ou não na célula principal.
- Farjam2020a E02: `sdy` não relatado (Tabela 2 só dá estimativas, IC95 e fatores de Bayes); desfecho ordinal 0/1/2 em regressão ordinal mista bayesiana cuja função de ligação o texto não informa. Como a rota OR = exp(β) só vale para logit, o coordenador não a aplicou: o efeito fica sem g e entra só na síntese por direção (IC95 0,07 a 0,58, positivo = *bandwagon*).
- **Erro do coordenador corrigido:** no script de junção, `ano_eleicao = 999` passou no teste numérico e virou `ano_eleicao_pre2010 = sim`. Apontado pelo subagente de Lammers2022a; corrigido em todos os CSVs (999 → `nao`). Lammers2022a E05 (painel da eleição polonesa real de 2019, Estudo 1) tinha herdado os campos do experimento; corrigidos para `comparador_tipo = outro`, `desenho_fino = painel_individual`, `tipo_eleicao = candidato_partido`, `realismo_contexto = real`, `sistema_eleitoral = proporcional`.
- **Emenda 4c aplicada:** `icc = 0.05` nas linhas com `cluster` > 1 e `icc` vazio (tamanho médio do conglomerado já preenchido pelos extratores; Agranov2017a E13 com m = 20 rodadas por grupo). `efeitos.R` só aplica o efeito de desenho quando a variância vem dos tamanhos de amostra; linhas com EP ou IC informados ficam intactas. Tyszler2015 E01 não recebe ajuste porque n1 = n2 = 6 já são eleitorados (a unidade de conglomerado). Unkelbach2022a traz ICC estimado pelo próprio modelo multinível. A sensibilidade com ICC = 0,20 é rodada sobre uma cópia de `06-analise/efeitos.csv`.

## Concordância da extração (recodificação cega, 23/09/2026)

- Amostra: 10 estudos sorteados (semente 20260923) entre os 38 fora do piloto (max(20%, 10)); segundo codificador `claude-sonnet-5`, cego, com o mesmo prompt da extração completa (`prompts_fichamento/fichador_completo.md`). Fichas em `validacao_extracao/fichas/`; relatório em `validacao_extracao/concordancia/RELATORIO_CONCORDANCIA.md`.
- Resultado: concordância de valores 58,5% (560 comparações), desenho (tipo_estudo) 10/10; 37 variáveis abaixo do limiar do protocolo (κ ou PABAK ≥ 0,7 e concordância ≥ 80%). Entre as que alimentam a síntese: `alvo_efeito` 50% (κ 0,38), `comparador_tipo` 50% (κ 0,38), `b2_estimando` 60% (κ 0,15), `b2_direcao_estimativa_principal` 50% (κ 0,28); `familia_intervencao`, `regiao` (100%), `realismo_contexto` (90%), `desenho_fino` e `construto_outcome` (80%) passam.
- Parte das divergências é artefato: o segundo codificador abriu duas fichas em Cornejo2023a e Lammers2022a (uma por desenho), que o script funde por texto; e 999 contra valor conta como divergência. Gate de citações das fichas de validação: 457/507 OK (34 página errada, 16 não encontradas), não corrigido porque essas fichas só servem à concordância.
- Consequência para a síntese: alvo e comparador usados nas células vêm da codificação por efeito (complementação com trecho e página, `complementos_efeitos/`), não do master; mesmo assim, a baixa concordância indica ambiguidade real na definição desses códigos e entra nas limitações e na indireção do GRADE. Pendência `concordancia_extracao` aberta para arbitragem humana.
