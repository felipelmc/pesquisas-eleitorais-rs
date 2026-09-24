# Pré-revisão PRESS 2015 da estratégia S-oa-en-v5 (por IA)

> **PRÉ-REVISÃO POR IA, NÃO É O PRESS.** Texto de um subagente de IA (`claude-opus-5-5`) que não escreveu nenhuma das strings. Ele não substitui a revisão PRESS por pessoa: a pendência **P001** (e a P004, que depende dela) continua **aberta**. Nada aqui conta como validação humana.
>
> Data: 23/09/2026. Não houve consulta à web nem à API do OpenAlex, e o `rs.py` não foi rodado. Os números "locais" abaixo saem de um casamento aproximado feito sobre os títulos e resumos que já estão em `dados/registros.csv` e `dados/registros_unicos.csv`, com o stemmer de Porter (NLTK). O analisador do OpenAlex é outro, então esses números servem de ordem de grandeza, não de contagem oficial. Esse casamento local reproduz 40 dos 42 relatos incluídos que vieram da B05; os 2 que ele não acha estão sem resumo no arquivo local. Todo termo novo sugerido aqui está **não testado**.

## 0. Qual string revisar: a v5, não a v4

A P001 (`rs_estado.json`, espelhada no `README.md` e na tabela de pendências do `relatorio.qmd`) pede o "PRESS 2015 da estratégia S-oa-en-v4" e aponta `01-busca/strings/S-oa-en-v4.txt`. Essa string não está mais em uso. Pela emenda **E002**, a busca B01 (S-oa-en-v4, 1.235 registros) foi substituída pela **B05 (S-oa-en-v5, 1.438 registros)**, e só a B05 conta entre os identificados. **O PRESS humano deve ser feito na v5** (`01-busca/strings/S-oa-en-v5.txt`). Ao fechar a P001, diga no motivo que a revisão foi feita na v5.

Nenhuma revisão PRESS, nem de IA, cobriu até hoje o que entrou na v4 e na v5. A única pré-revisão anterior (`01-busca/prepress_S-oa-en-v3_ia.md`) é da v3. Na v5, os acréscimos foram desenhados a partir das âncoras de validação perdidas (A01, A07, A08, A19). Por isso o recall de 19/19 deixou de ser um teste independente. O PRESS humano é agora a única checagem externa que resta à estratégia inglesa.

## 1. Como a v5 está montada (para ler a string)

São sete fios unidos por OR no nível superior. Parênteses 16/16, 96 OR, 5 AND, nenhum NOT, 2.033 caracteres, nenhuma vírgula (a vírgula separa filtros no `filter` do OpenAlex), nenhuma aspa curva, nenhum `*`.

| Fio | Conteúdo | Desde | Casamento local na B05 (n = 1.438): casa / só este fio / incluídos no TC que só este fio acha |
|---|---|---|---|
| T1 | `(poll OR polls OR polling OR "election forecast" OR "election forecasting") AND (bandwagon OR underdog OR "band-wagon")` | v1 | 107 / 65 / 1 |
| S | `("pre-election survey" … "opinion survey") AND (bandwagon OR underdog)` | v2 | 11 / 8 / 0 |
| T2 | 20 frases de exposição AND 25 frases de desfecho de voto | v1; exposição ampliada na v4 e na v5, desfecho ampliado na v5 | 725 / 582 / 3 |
| T3 | as mesmas 20 frases de exposição AND comparecimento | v3 | 348 / 254 / 8 |
| PE | `"poll effects"` | v4 (E001) | 19 / 6 / 0 |
| PS | `(poll OR polls OR polling) AND ("strategic voting" OR "tactical voting")` | v5 | 70 / 32 / 2 |
| ER | `("effect of polls" … "poll release" OR "poll releases" OR "release of polls" OR "release of a poll")` | v5 | 122 / 98 / 2 |

Sem casamento local: 228 registros (193 deles sem resumo no arquivo local). Dos 55 relatos incluídos no texto completo, 42 vieram da B05 e 13 só da bola de neve (SN1 = 10, SN2 = 3), ou 24%, abaixo do alerta de 30% do protocolo. B02, B03 e B04 não contribuíram com nenhum incluído.

## 2. Avaliação por elemento PRESS

Escala: **sem problemas** · **revisão sugerida** · **revisão necessária**. Os itens seguem `~/.claude/skills/revisao-sistematica/assets/checklists/press.csv`.

### 2.1 Tradução da pergunta (itens 1.1 a 1.6): **revisão sugerida**

- **1.1 Correspondência com o PECO.** E e O estão cobertos, e não buscar P nem C é o esperado. Há duas lacunas diante da definição de E no protocolo (seção 2) e na Emenda 1:
  - **Proibição ou embargo de divulgação.** O protocolo põe essa variação natural dentro de E, mas a v5 não tem vocabulário para ela: não há "ban", "embargo", "blackout" nem "restriction". Chatterjee2019a entrou por `"exit poll"`. Lago2015 ("pre–Election Day poll restrictions", "laws forbidding the publication of polling results", "wasted votes", "electoral coordination") só veio pela SN2. Localmente ele casa com `"poll result"` pelo stemming de "polling results", mas nenhuma das frases de desfecho aparece no texto.
  - **Apuração parcial oficial (Emenda 1).** C2 foi ampliado em 20/09, e a string não acompanhou. Araujo2021/2021a ("official tallies started being announced", "information exposure", "bandwagon effect") só veio pela SN1. T1 exige `poll`, e o resumo não tem essa palavra.
- **1.2 Conceitos claros.** Os fios estão separados, mas a documentação ficou para trás: o protocolo (seção 3), a `termos_v2.md` e o `relatorio.qmd` (linha 103: "A estratégia tem quatro fios") descrevem a v3, com quatro fios. A v5 tem sete, e PE, PS e ER não aparecem na tabela de termos. Não é um defeito da busca, mas o relato (PRISMA-S) precisa descrever a string que de fato rodou.
- **1.3 Número de elementos.** Sem problema. Não há bloco de desenho, que foi testado e rejeitado (`desenvolvimento.csv`, v1-en-E).
- **1.4 Amplitude.**
  - `"poll release"`/`"poll releases"` (fio ER) é amplo demais. Localmente, casa com 66 dos 98 registros que só o ER acha. Na amostra aparecem comunicados de pesquisas de opinião sobre saúde e consumo ("APA poll: Social media has negative impact…", "Poll Release #2020-09…") e até "Crossbred Effect of Poll Dorset with Mongolian Sheep". Os 2 incluídos que, no casamento local, só o ER acha (Brugarolas2021 e Agranov2012a) casam com `"effect(s) of polls"`, e não com `"poll release"`. Agranov2012a já vinha na v4, provavelmente por outro fio no resumo que o OpenAlex tem.
  - Em T3, o comparecimento está estreito para desfechos formulados como intenção: Yang2023d ("election forecasts", "political participation intention") só veio pela SN1.
- **1.5 Volume.** 1.438 registros, com a contribuição de cada fio na tabela da seção 1. O volume é compatível com a contingência de ondas já acionada.
- **1.6 Estratégias incomuns.** A v5 foi ajustada ao conjunto de validação. A E002 e o relatório (linhas 103 e 520) já declaram que o recall final não é independente. Sem outra mudança.

### 2.2 Operadores booleanos e de proximidade (2.1 a 2.5): **sem problemas** (uma sugestão menor)

- 2.1: AND e OR em maiúsculas, nenhum operador em minúscula fora de aspas, execução sem erro (`B05_openalex.consulta.json`: `n_api = 1438`, `truncada = false`).
- 2.2: a precedência está correta. Sugestão menor: **envolver a string inteira num par de parênteses externo** no arquivo documentado. Na execução isso não muda nada, porque o `,publication_year:2008-2026` entra como outro filtro. Mas quem reproduzir a busca numa interface que acrescente `AND` terá outra precedência, porque os sete fios e o `"poll effects"` solto estão no nível superior sem parênteses.
- 2.3: não há NOT. 2.5: não se aplica.
- 2.4: a pré-revisão da v3 testou proximidade em T1 e perdeu 63%. Manter o AND. Se o revisor quiser conter o ruído de `"poll release"`, a opção é AND com termos eleitorais (seção 3, R6), não proximidade.

### 2.3 Vocabulário controlado (3.1 a 3.9): **não se aplica**

O OpenAlex não tem tesauro. Os `topics` e `keywords` que ele atribui por máquina não são descritores e não devem virar limite. No máximo, servem de checagem exploratória de sensibilidade.

### 2.4 Texto livre (4.1 a 4.7): **revisão sugerida**

- **4.1 Variantes de grafia.** O stemming não une grafias diferentes. Faltam:
  - `demobilisation`/`demobilises`/`demobilising`: a string tem só `demobilization` e `demobilizes`, e o radical de Porter de uma é "demobilis", da outra "demobil";
  - `horserace`, em uma palavra, grafia comum em ciência política ("horserace coverage");
  - as demais variantes (US/UK em behavior/behaviour, com e sem hífen em pre-election e horse-race, band-wagon) estão lá.
- **4.2 Sinônimos.** Nada disso foi testado. Na seção 3 os termos estão em ordem de prioridade, com o incluído que teria sido achado:
  - proibição ou embargo: `ban`, `banning`, `embargo`, `blackout`, `restriction(s)`, `prohibition` junto de poll (Lago2015);
  - apuração parcial e projeções no dia da eleição: `"early returns"`, `"partial results"`, `"official tallies"`, `"election night"`, `"early projections"`, `"election projections"` (Araujo2021a);
  - efeito nomeado sem `poll`: `(bandwagon OR underdog) AND (voter OR voters OR voting OR election OR electoral)` (Araujo2021a);
  - participação como intenção: `"political participation"`, `"intention to vote"`, `"likelihood of voting"`, `"turnout intention"` (este último já coberto por `turnout`) (Yang2023d);
  - agregadores: `"poll average"`, `"polling average"`, `"poll aggregation"`, `"poll prediction"` (Erlich2023 usa "poll predictions");
  - desfechos de coordenação: `"wasted vote"`, `"electoral coordination"` (Lago2015).
- **4.3 Truncamento.** Não há `*`, e está certo: a pré-revisão da v3 registrou HTTP 400 com `*` nesse campo. O stemming cobre singular e plural. A polissemia de "poll" (poll = cabeça, "polled" = gado mocho, raça Poll Dorset) gera ruído nos fios em que "poll" aparece solto (PE, ER).
- **4.4 Siglas.** Não há.
- **4.5 Especificidade.** Ver 1.4 sobre `"poll release"`. `"release of a poll"` tem uma palavra vazia ("a") dentro da frase. Vale conferir como o OpenAlex trata palavra vazia dentro de aspas; é de baixa importância, porque casou 2 registros localmente.
- **4.6 Campos.** `title_and_abstract` é adequado. Limitação: 193 dos 1.438 registros não têm resumo no arquivo local e só podem ser achados pelo título. Urminsky2019 (sem resumo) e Meffert2012a (capítulo com resumo genérico) só vieram pela bola de neve. É limite de campo, não de termos.
- **4.7 String longa.** São 2.033 caracteres, executados pela API com `rs.py`. Sem problema, desde que a execução continue por script.

### 2.5 Ortografia, sintaxe e linhas (5.1 a 5.3): **sem problemas**

- 5.1: nenhum erro de digitação; `preelection`, `horse-race` e `band-wagon` são variantes de propósito.
- 5.2: aspas retas, nenhuma vírgula, nenhum `*`. Segue valendo a observação da v3: a frase entre aspas não garante adjacência estrita no OpenAlex (exemplo: `"poll effects"` achou "polled"). É limite de precisão, não erro.
- 5.3: é uma string só, sem linhas numeradas. A lista de 20 frases de exposição se repete em T2 e T3, e conferi que as duas cópias são idênticas. Qualquer mudança futura precisa ir para as duas.

### 2.6 Limites e filtros (6.1 a 6.4): **sem problemas**

`publication_year:2008-2026`, com dois anos de margem antes do marco de 2010, que é aplicado pelo funil (`filtros_v2.json`). Não há filtro de idioma nem de tipo, o que bate com o G2. O filtro não vem de estratégia publicada, e a justificativa está no protocolo (seções 3 e 4).

## 3. Mudanças sugeridas para o revisor testar (nenhuma testada)

Para cada linha: contar `S-oa-en-v5 OR <acréscimo>` no OpenAlex com o mesmo filtro de ano, subtrair 1.438, olhar os registros novos e conferir se já estão na base por DOI ou `id_fonte` em `dados/registros_unicos.csv`.

| # | Acréscimo (OR no nível superior, salvo indicação) | Motivo | Prioridade |
|---|---|---|---|
| R1 | `((poll OR polls OR polling) AND (ban OR bans OR banning OR embargo OR blackout OR restriction OR restrictions OR prohibition) AND (voter OR voters OR voting OR election OR elections OR electoral OR turnout))` | E do protocolo inclui proibição e embargo; Lago2015 só veio pela SN2 | alta |
| R2 | `((bandwagon OR underdog) AND (voter OR voters OR voting OR election OR elections OR electoral))` | efeito nomeado sem a palavra poll; Araujo2021a | alta (checar o volume: *bandwagon* em marketing fica contido pelos termos eleitorais) |
| R3 | `(("early returns" OR "partial results" OR "official tallies" OR "election night" OR "early projections" OR "election projections") AND (turnout OR bandwagon OR "vote choice" OR "vote switching" OR "voting behavior" OR "voting behaviour"))` | Emenda 1 | média |
| R4 | em T3: `OR "political participation" OR "intention to vote" OR "likelihood of voting" OR demobilisation OR demobilises` | Yang2023d; grafia britânica | média |
| R5 | nas duas listas de exposição (T2 e T3): `OR horserace OR "poll average" OR "polling average" OR "poll aggregation" OR "poll prediction"` | variante de grafia; agregadores | média |
| R6 | trocar `"poll release" OR "poll releases" OR "release of polls" OR "release of a poll"` por essa lista `AND (voter OR voters OR voting OR election OR elections OR electoral OR turnout)` | ruído do ER (cerca de 66 registros locais), sem incluído perdido localmente | baixa (só precisão; a triagem já foi feita) |
| R7 | parênteses externos na string documentada | reprodutibilidade | baixa |

**O que nenhuma string conserta** (limites que vão para o relato, e a bola de neve compensa): experimentos de laboratório em que a exposição é "information about the preference distribution", sem a palavra poll (Tyszler2013, Tyszler2015, Schlegel2023); capítulo com resumo genérico (Meffert2012a); registro sem resumo (Urminsky2019); vinheta que não fala em pesquisa (Gandhi2019); resumo sobre outra coisa (Feltovich2022); documento em dinamarquês (Dahlgaard2015b, cuja versão em inglês, Dahlgaard2015a, foi achada).

**Consequência de mudar agora.** A revisão já passou do G9. Trocar a B05 (`--substituir`) reabriria deduplicação, triagem e tudo o que vem depois. A alternativa proporcional é uma **busca suplementar só com o delta** (um novo `busca_id`, os registros novos triados com a mesma `ta_v1`). Ela exige emenda de **tipo C** (decidida depois de ver os dados). A outra saída é aceitar a v5 e declarar as lacunas como limitação. A decisão é do revisor humano.

## 4. O que mudou de v3/v4 para v5, e o que foi feito das recomendações da pré-revisão da v3

| De → para | Mudança (`desenvolvimento.csv`) | Registros |
|---|---|---|
| v3 → v4 (E001) | `OR "poll effects"` no nível superior; `"polling data"` na exposição de T2 e T3 | 1.130 → 1.235 |
| v4 → v5 (E002) | exposição: `"poll news"`, `"poll coverage"`, `"coverage of polls"`; desfecho em T2: `"electoral volatility"`, `"vote switching"`, `"vote change"`, `"party switching"`; fio PS; fio ER | 1.235 → 1.438 |

Os 4 relatos incluídos que a v5 achou e a v4 não (comparação por `id_fonte` entre B01 e B05) são Meffert2011 e Freden2016b (fio PS), Geers2018 ("poll news" com "electoral volatility", em T2) e Brugarolas2021 (fio ER).

| Recomendação da pré-revisão da v3 | Situação |
|---|---|
| Nº 1: `OR "poll effects"` | **Atendida** (v4). Localmente, nenhum incluído depende só dela |
| `"polling data"` (a pré-revisão achou que não compensava e deixou para o revisor humano) | **Adotada** na v4 pela regra de parada da skill. Pagou: Witsman2016a ("The effect of polling data on independent voting behavior") está entre os incluídos |
| Nota 4.7: executar por API ou script | **Atendida** |
| Nota 5.2: adjacência imperfeita das frases como limitação de precisão | Continua valendo. Não achei essa limitação no relatório |
| PT: `"voto estratégico"` fora do fio T1 | **Não atendida** (E001: "sem efeito prático") |
| BDTD: sem termos de comparecimento | **Não atendida** (S-bdtd-v3 = v2) |
| BDTD: sem `bandwagon`/`underdog` soltos | **Não atendida** |

Além disso, o protocolo manda rever B02 a B04 contra a mesma tabela de termos quando a B01 mudar. A E001 registra essa revisão para a v4. A E002 não diz nada sobre B02 a B04, e os conceitos que entraram na v5 (cobertura de pesquisas, volatilidade e troca de voto, divulgação e efeitos das pesquisas, pesquisa com voto estratégico) não foram traduzidos. A `termos_v2.md` também não foi atualizada.

## 5. Lacunas das strings PT, ES e BDTD

Contexto: nenhuma âncora em PT ou ES, recall de B02 e B03 igual a 0/19, esperado porque as âncoras são em inglês, e B04 sem âncoras. Nenhum incluído veio dessas buscas. Chegaram ao texto completo 5 registros da B02, 22 da B03 e 8 da B04, todos como "incerto". A seção regional (Brasil e América Latina) depende hoje da busca inglesa e da bola de neve. Araujo2021a, o estudo brasileiro, veio pela SN1.

**S-oa-pt-v3**
- Efeito nomeado: falta `azarão`/`"efeito azarão"`, o termo corrente para *underdog* no Brasil. `"voto estratégico"` continua fora do fio T1.
- Exposição: faltam o português europeu `"boca das urnas"` e `"sondagem à boca das urnas"` (a frase `"boca de urna"` não casa com "das urnas"), `"sondagem pré-eleitoral"`/`"sondagens pré-eleitorais"`, a grafia `preeleitoral` sem hífen, agregadores (`"agregador de pesquisas"`, `"média das pesquisas"`), proibição (`"proibição de divulgação"`, `"proibição de pesquisas"`) e apuração parcial (`"apuração parcial"`, `"resultados parciais"`), que é a Emenda 1 no contexto brasileiro.
- Desfecho: a lista de voto tem o escape genérico (`efeito OR influência OR impacto`), e isso compensa. Em comparecimento, falta `"participação política"`.

**S-oa-es-v3**
- Exposição: falta `"pie de urna"` (`"sondeos a pie de urna"`, `"encuesta a pie de urna"`), o termo da Espanha para boca de urna. Faltam também `"encuesta de salida"`, os singulares `"encuesta de intención de voto"` e `"sondeo preelectoral"`, as grafias com hífen `pre-electoral`/`pre-electorales`, a proibição (`"veda electoral"`, `"veda de encuestas"`, `"prohibición de publicar encuestas"`) e agregadores (`"promedio de encuestas"`, `"agregador de encuestas"`).
- Efeito nomeado: faltam `desvalido`/`"efecto del desvalido"` e `"subirse al carro"`.
- Comparecimento: falta `abstencionismo`, que dificilmente casa com `abstención` por stemming. Faltam também `"participación política"`, `desmovilización` e `"movilización electoral"`.

**S-bdtd-v3** (lista OR simples, porque parênteses aninhados dão HTTP 403 na API VuFind)
- Não há nenhum termo de comparecimento (fio T3). A v3 é idêntica à v2, sob a hipótese de que as frases eleitorais bastam porque o AllFields inclui o resumo. Ninguém testou essa hipótese.
- Não há `bandwagon` nem `underdog` soltos (só `"efeito bandwagon"` e `"efeito underdog"`). Também faltam `azarão`, `"voto estratégico"` e `"boca das urnas"`.
- Para contornar a falta de aninhamento: rodar **várias consultas simples e unir os resultados** (por exemplo, `"pesquisas eleitorais" AND comparecimento`; `bandwagon AND eleitoral`; `underdog AND eleitoral`), cada uma registrada no log. Um AND sem parênteses provavelmente passa, mas é preciso testar. Outra saída é a busca avançada do VuFind com grupos. O volume é pequeno (80), então o custo de triagem é baixo.

## 6. Pacote para o revisor humano

**Tempo estimado:** de 2,5 a 3,5 horas; cerca de 1,5 hora sem os testes de contagem.

1. **(5 min)** Ler o aviso e a seção 0. O PRESS é da **v5**.
2. **(15 min)** Ler `01-busca/strings/S-oa-en-v5.txt` com a tabela da seção 1 ao lado. Conferir se os sete fios traduzem o PECO do `protocolo.md`, seção 2, e o C2 ampliado pela Emenda 1.
3. **(45 a 60 min)** Percorrer os 34 itens de `~/.claude/skills/revisao-sistematica/assets/checklists/press.csv`, marcando para cada um se concorda com a seção 2 deste arquivo. Os pontos em que o julgamento humano mais pesa são 1.1 (proibição e apuração parcial), 1.4 (`"poll release"`), 4.1 e 4.2.
4. **(30 a 60 min, opcional mas recomendado)** Testar R1 a R5 no OpenAlex com a chave do usuário como prefixo de variável de ambiente, nunca gravada em arquivo. Anotar a contagem antes e depois e quantos registros novos são pertinentes e ainda não estão em `dados/registros_unicos.csv`.
5. **(20 a 30 min)** Ler a seção 5 e decidir se PT, ES e BDTD pedem nova versão ou só entram como limitação.
6. **(10 min)** Decidir a consequência, com três caminhos:
   - (a) aceitar a v5 e declarar as lacunas;
   - (b) busca suplementar só com o delta, por emenda tipo C;
   - (c) substituir a B05, o que não é recomendado a esta altura.
7. **(20 min)** Gravar o resultado em **`01-busca/press_<revisor>.md`** (por exemplo, `01-busca/press_revisor_humano_1.md`): data; string revisada (S-oa-en-v5); uma linha por item com resposta, comentário e mudança pedida; decisão final. Este arquivo de IA pode ser citado, mas o PRESS é o documento humano.
8. **Fechar as pendências**, a partir da raiz do projeto e só depois de a revisão ter sido feita de fato por pessoa:

   ```bash
   cd ~/Desktop/pesquisas-eleitorais-rs
   python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py --dir . pendencia fechar P001 --motivo "PRESS 2015 humano feito na S-oa-en-v5 (string ativa da B05; a P001 citava a v4, substituída pela E002); resultado em 01-busca/press_<revisor>.md; decisão: <a/b/c>" --por revisor_humano_1
   python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py --dir . pendencia fechar P004 --motivo "G3 confirmado depois do PRESS humano (P001)" --por revisor_humano_1
   ```

9. **Depois de fechar:**
   - se a decisão for (b), escrever a emenda em `00-protocolo/emendas.md` antes de rodar a busca;
   - em qualquer caso, corrigir no `relatorio.qmd` a descrição da estratégia ("quatro fios", linha 103) e a frase sobre o PRESS (linhas 65 e 520);
   - conferir se o campo `press_revisor` da B05 em `01-busca/log_buscas.csv` ("pré-revisão da v3") deve mudar;
   - rodar `rs declaracao-ia` por último e então `quarto render`, como diz o `CLAUDE.md`.
