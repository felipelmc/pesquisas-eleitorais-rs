# Verificação independente final do artigo

Feita em 24/09/2026 por um subagente Opus (`claude-opus-5-5`) que não escreveu nenhum dos textos, seguindo `prompts_v2/prompt_verificacao_final.md`. É a rodada final, depois da resposta às leituras críticas (`resposta_pareceres.md`), das correções técnicas (etapa 6c), do preenchimento de S11 e dos passes de voz e anti-IA (etapa 7). Não alterei nenhum texto do artigo, do suplemento ou do resumo em linguagem simples. Não abri PDFs de estudos nem rodei `rs.py`. Esta verificação é de IA e não valida nada: as 18 pendências humanas continuam abertas.

Objetos conferidos:

- `09-documento-final/revisao_final.qmd`, remontado do esqueleto numa pasta temporária e idêntico byte a byte ao arquivo atual, com as figuras (`revista/figuras/legendas.yml` e `revista/figuras/dados/`) e as tabelas (`revista/tabelas/*.yml`);
- `09-documento-final/suplemento.qmd`, regravado por `montar_suplemento.py` sem diferença;
- `09-documento-final/linguagem_simples.qmd`;
- as saídas publicadas em `docs/` (`revisao.html`, `.pdf` e `.docx`, `suplemento.html` e `.pdf`, `linguagem-simples.html`), renderizadas às 17:03 e 17:04, depois da última versão do `.qmd` (16:59).

## Resultado

**1 erro, 5 avisos e 13 casos ok com ressalva.** A auditoria A1 a A36 está em `auditoria_final_v2.md`: 18 cumpridos, 15 parciais e 3 não cumpridos (A21 e A36 dependem do autor).

Os 4 erros e os 17 avisos da `verificacao_v2.md` foram resolvidos, com duas exceções parciais: o fluxograma separa autor e IA só na legenda (V11), e a versão do R ficou marcada para o autor (V17). Das 14 ressalvas da v2, 13 foram resolvidas ou justificadas. A R11 ("efeito médio") voltou no §1.2 com o passe de voz.

O único erro está no resumo em linguagem simples: os projetos de lei aparecem "depois de 2022", e eles são de outubro de 2022.

Nenhum número de célula, meta-análise, risco de viés, PRISMA, sensibilidade, Tab. 1, transferibilidade ou efeito citado diverge da fonte. Os passes de estilo não mudaram número, chave, certeza nem enunciado (trava `conferir_numeros.py` vazia no esqueleto, no resumo em linguagem simples, nas legendas e nas três tabelas editáveis), não criaram verbo mais forte que a certeza e não trouxeram fato novo. As listas de S11 apontam para 185 âncoras que existem, com o número de seção, figura, tabela e quadro certo.

## O que foi checado e quanto

| Conferência | O que foi feito | Quanto | Resultado |
|---|---|---|---|
| 1. Números | Cada número do texto, das tabelas, das legendas, do resumo, do *abstract*, das mensagens e do resumo em linguagem simples, confrontado com a fonte. Fórmulas de `celulas.json` e `numeros_v2.json` refeitas: Clopper-Pearson e teste de sinal por programa, δ reconvertido de 2 p.p., as 35 porcentagens da Tab. 1, as contagens de transferibilidade a partir do *master*, o n de cada estudo da Tab. 2 | 144 verificações de programa, todas OK, mais a leitura inteira dos três textos; a trava `conferir_reestruturacao.py` passou com 0 falhas e 0 avisos | 1 erro de data (E1); ressalvas R1 a R3 |
| 2. Certeza | Todo enunciado de efeito: certeza da célula certa e frase padrão; busca de "significativ", "Neutro", "sem efeito", "não tem efeito", "permite descartar" e "é evidência de que" | 18 enunciados (iguais, caractere a caractere, aos de `certeza.csv`), cerca de 50 frases de efeito fora deles, 7 legendas e 5 tabelas | 18 de 18 enunciados certos; avisos V3 e V4; nenhum termo proibido (os 5 "não têm efeito" do artigo são negações do tipo "não permite afirmar que elas não têm efeito", e o do suplemento é "não têm efeito principal extraído") |
| 3. Leitura às cegas | Mensagens, Resumo, *Abstract*, Resumo executivo, Discussão 4.1, Conclusões e resumo em linguagem simples reescritos com a direção invertida | 18 conclusões | 1 com enquadramento otimista no escopo pedido (4.1, § 3; V2) e 1 fora dele (5.2; V3) |
| 4. Marcações humanas | Caixas comparadas com `_revisao_final_v1_oqf.qmd`; apêndice com `_pendencias_abertas.json`; marcadores e papéis humanos com `emendas.md`, `protocolo.md` e `correcao_atribuicao.csv` | 11 caixas, 18 pendências, 6 marcadores, 15 atribuições ao autor | 11 caixas nas seções correspondentes e com os mesmos conjuntos de IDs; 18 de 18 pendências; todo papel do autor tem registro; ressalva R10 sobre o marcador da versão do R |
| 5. Citações e revisões anteriores | Toda `@chave` em `revista/referencias.json`; afirmações sobre Barnfield, Moy e Rinke, Hardmeier e Coşgun em `revisoes_anteriores.md`; Brasil em `contexto_brasil.md` e, no caso de @Araujo2021a, na ficha do estudo; revisões rápidas em `garritty_2024.md` | 104 chaves no artigo e 74 no suplemento; 12 afirmações sobre revisões anteriores; 16 sobre o Brasil; 7 citações literais de Garritty | Todas as chaves existem, inclusive as 13 dos excluídos limítrofes. Duas chamadas por *link* sem referência em S11 (V5). Hardmeier sempre "não verificada". Nenhum item "não confirmado" do dossiê. Citações de Garritty literais |
| 6. Recomendações | Verbos das implicações comparados com a tabela R6.8 | 10 frases (artigo e linguagem simples) | Nenhuma recomenda proibir ou liberar a divulgação. Com certeza muito baixa, o texto usa "não cabe implicação de adoção nem de revogação" e remete a decisão a quem tem mandato |
| 7. Auditoria | Itens A1 a A36 de `insumos/livro_regras.md`, seção 8, comparados com `auditoria_final.md` | 36 itens | `auditoria_final_v2.md` |
| Rodada final | Cada erro, aviso e ressalva da `verificacao_v2.md`; *diff* palavra a palavra dos passes de estilo (commit `c1abeb1` contra `HEAD`); os 185 *links* de S11 contra o HTML publicado | 35 itens da v2; 178 linhas do esqueleto, 20 do resumo em linguagem simples, 116 das legendas e 3 tabelas | Tabela em "Situação dos itens da v2" |

## Divergências

Cada divergência traz o trecho, o que diz a fonte, a correção em texto exato e o arquivo onde se corrige. As linhas são de `revisao_final.qmd` (montado) e, entre parênteses, de `_esqueleto_revisao_final.qmd`.

### Erro

**E1. Data dos projetos de lei no resumo em linguagem simples.**

- **Trecho:** `linguagem_simples.qmd`, "Do que trata esta revisão?", linha 23: "Depois de 2022, projetos de lei propuseram punir quem divulgasse pesquisas que errassem além da margem de erro."
- **Fonte:** `insumos/contexto_brasil.md`, seção 3: o PL nº 2.558/2022 foi apresentado em 5/10/2022 e o PL nº 2.567/2022, em 6/10/2022, "após o primeiro turno das eleições de 2022". O artigo diz "Depois do primeiro turno de 2022" (§1.1, L132, e Resumo executivo, L66). "Depois de 2022" situa os projetos a partir de 2023.
- **Correção**, que deixa o texto com 749 palavras na contagem da trava (limite de 750): "Em outubro de 2022, projetos de lei propuseram punir quem divulgasse pesquisas que errassem além da margem de erro."
- **Onde:** `linguagem_simples.qmd`.

### Avisos

**V1. "Efeito médio" voltou ao §1.2.**

- **Trecho:** §1.2, L140 (L135): "Com canais de sinais opostos, um efeito médio perto de zero não significa que ninguém mude de voto."
- **Fonte:** R5.37 e A17: a adaptação brasileira do GRADE reserva "efeito médio" para o tamanho intermediário. A v2 (R11) pediu "efeito na média", e a resposta aos pareceres dá a correção como feita na 1.2. O *diff* mostra que o passe de voz da etapa 7 trocou "efeito na média" de volta por "efeito médio". A linha R1 da Tab. 3 ficou certa.
- **Correção:** "Com canais de sinais opostos, um efeito na média perto de zero não significa que ninguém mude de voto."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V2. Discussão 4.1, § 3: contraste de magnitude com as metas.**

- **Trecho:** L576 (L450): "A magnitude vai na mesma linha, também sem teste. Nos experimentos de *survey* com partidos reais das células de viabilidade e de *momentum*, os g ficaram entre 0,12 e 0,19 [@Dahlgaard2016a; @Meer2015a; @Cornejo2023a], e, nas metas de laboratório e vinheta, em 0,48 e 0,62. As medidas pouco se comparam, mas o contraste é compatível com um efeito maior em contexto hipotético e com a persistência da direção."
- **Fonte:**
  - o Resumo executivo (L72) e a linha Escala da Tab. 4 dizem que as duas metas "não informam o tamanho", e a §2.7 lê menos de 4 graus de liberdade como inferência não confiável (R2.9: as mesmas palavras em todo lugar);
  - em `06-analise/efeitos.csv`, os três g de *survey* têm IC que cruza zero (@Dahlgaard2016a, −0,04 a 0,28; @Meer2015a, −0,01 a 0,27; @Cornejo2023a, −0,01 a 0,40), e são de alvos (viabilidade e *momentum*) diferentes do das metas (alvo principal). "Persistência da direção" junta direções de alvos diferentes;
  - com a direção invertida (g maiores nos *surveys*), a frase soaria igualmente confiante, "compatível com um efeito maior em contexto real". É o enquadramento que A23 pede para detectar.
- **Correção:** "Os tamanhos não permitem ir além disso. Nos experimentos de *survey* com partidos reais das células de viabilidade e de *momentum*, os g ficaram entre 0,12 e 0,19 [@Dahlgaard2016a; @Meer2015a; @Cornejo2023a], todos com IC que cruza zero, e as metas de laboratório e vinheta deram 0,48 e 0,62, com IC que cruza zero e menos de 4 graus de liberdade. Os alvos e as medidas diferem, e as metas não informam o tamanho. O contraste é compatível com a teoria rival do artefato, sem testá-la."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V3. Divulgação seletiva (5.2) sem a frase padrão.**

- **Trecho:** §5.2, L657 (L510): "A divulgação seletiva de pesquisas favoráveis, canal a que se dirigem o registro prévio e o crime de pesquisa fraudulenta, tem um só teste, em laboratório, em que revelar só as pesquisas favoráveis a um candidato aumentou a vitória desse candidato, mesmo com aviso ao eleitor, com certeza muito baixa [@Boukouras2020a]."
- **Fonte:** C03 tem certeza muito baixa (`certeza.csv`), e a frase padrão é "a evidência é muito incerta" (R5.36). Na forma atual, "aumentou [...] com certeza muito baixa" apresenta o resultado do estudo como achado da revisão, num parágrafo dirigido ao Congresso e à Justiça Eleitoral. Invertida ("não mudou a vitória, com certeza muito baixa"), soaria igual.
- **Correção:** "A divulgação seletiva de pesquisas favoráveis, canal a que se dirigem o registro prévio e o crime de pesquisa fraudulenta, tem um só teste, em laboratório. Nele, revelar só as pesquisas favoráveis a um candidato aumentou a vitória desse candidato, mesmo com aviso ao eleitor, mas a evidência é muito incerta sobre esse efeito (certeza muito baixa) [@Boukouras2020a]."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V4. Proximidade e comparecimento (3.10) sem certeza.**

- **Trecho:** §3.10, L554 (L428): "Nos estudos que variam a proximidade, a disputa apertada aparece com mais comparecimento, e a decidida, com menos [@Bursztyn2023a; @Klor2017a; @Alabrese2024a], mas não no desenho mais forte, @Gerber2020a."
- **Fonte:** @Bursztyn2023a (E01) e @Alabrese2024a (E002) só têm efeitos fora da contagem (S7, interação com moderador contínuo), sem GRADE. @Klor2017a está na C15, com certeza muito baixa. A3 pede a certeza em todo enunciado de efeito. Invertida, a frase soaria igual.
- **Correção:** "Nos estudos que variam a proximidade, a disputa apertada aparece com mais comparecimento, e a decidida, com menos [@Bursztyn2023a; @Klor2017a; @Alabrese2024a], mas dois deles só têm efeitos fora da contagem, sem GRADE, e o terceiro está numa célula de certeza muito baixa. No desenho mais forte, @Gerber2020a, o padrão não aparece (certeza moderada)."
- **Onde:** `_esqueleto_revisao_final.qmd`.

**V5. Duas chamadas sem referência em S11.**

- **Trecho:** S11, legenda de `tbl-s11-traice`: "na versão publicada por [Holst et al. (2025)](https://doi.org/10.2196/80247) [...] ([Moher et al. 2026](https://doi.org/10.2196/104210))".
- **Fonte:** nenhuma das duas obras está em `revista/referencias.json` (107 entradas). A8 pede que toda chamada corresponda a uma referência com o mesmo ano. O artigo também nomeia o PRISMA-trAIce no §2.1 (L191) sem citá-lo.
- **Correção:** criar as duas entradas em `referencias_metodo.bib`, com os metadados conferidos no Crossref pelos DOIs 10.2196/80247 e 10.2196/104210 (chaves sugeridas: `Holst2025PRISMAtrAIce` e `Moher2026PRISMAtrAIce`), rodar `revista/preparar_referencias.py` e trocar:
  - na legenda: "na versão publicada por @Holst2025PRISMAtrAIce, usado só como lista de conferência, sem declaração de conformidade: é uma proposta que o PRISMA Executive não endossa [@Moher2026PRISMAtrAIce], e o livro que orienta esta revisão manda usá-la ao lado dos itens 8, 9 e 11 do PRISMA 2020 [@Lamarca2026Livro]";
  - no §2.1: "com o PRISMA-trAIce [@Holst2025PRISMAtrAIce] só como lista de conferência".
- **Onde:** `montar_suplemento.py` (linha 464), `referencias_metodo.bib` e `_esqueleto_revisao_final.qmd`.

### Ok com ressalva

**R1. Data da busca no *Abstract*.** O Resumo diz "(19 e 20/09/2026)", e o *Abstract* (L108; L103), "searched in September 2026". O item 4 do PRISMA para resumos pede a data da última busca, e S11 diz que o *Abstract* tem o mesmo conteúdo. Correção: "OpenAlex, BDTD and citations were searched on 19 and 20 September 2026." Onde: esqueleto.

**R2. "Todos os experimentos" no Resumo e no *Abstract*.** Resumo (L91; L86): "todos os experimentos com algumas preocupações ou risco alto de viés"; *Abstract* (L112; L107): "every experiment at some concerns or high risk of bias". Vale para os 23 resultados randomizados (RoB 2). Entre os experimentos naturais, @Brugarolas2021 (C18) está em risco moderado e @Bursztyn2023a, em risco baixo no comparecimento (EPOC). Correção: "todos os experimentos randomizados com algumas preocupações ou risco alto de viés" e "every randomised experiment at some concerns or high risk of bias" (Resumo com 249 palavras na contagem da trava). Onde: esqueleto.

**R3. Correções barradas.** §2.5 (L247; L238): "e barrou 40. Estas eram trocas do estimando de @Morton2015a". `08-revisao-humana/efeitos/aplicacao_arbitragem.csv` tem 41 sugestões não aplicadas: as 40 de @Morton2015a e 1 de sistema eleitoral para @Brugarolas2021, baseada em conhecimento externo, que o `relatorio.qmd` (linha 128) registra. Correção: "e deixou de aplicar 41. Quarenta eram trocas do estimando de @Morton2015a que vinham de um erro do próprio coordenador no *prompt* do árbitro, e uma era uma sugestão de sistema eleitoral para @Brugarolas2021 baseada em conhecimento externo." Onde: esqueleto.

**R4. Fluxograma: autor e IA só na legenda.** As caixas zeradas saíram e a legenda separa os 16 casos do autor (8 inclusões e 8 exclusões), mas as caixas do texto completo (`dados_prisma.csv`) não trazem, por ramo, quantos foram decididos pelo autor, e a Emenda 6b não tem ramo próprio (a legenda declara as duas coisas). S11 diz mais que isso: "O fluxo separa [...] os casos decididos pelo autor" (item 16a) e "O fluxograma e o texto separam [...]" (PRISMA-trAIce, R1). Correção preferida: em cada caixa "Relatos excluídos" e na de incluídos, uma linha "decididos pelo autor (n = x)", gerada do *ledger* em `revista/figuras/preparar_dados_figuras.py`. Se o diagrama não mudar, trocar em S11 por "A legenda do fluxograma separa a remoção por *script*, a triagem por IA e os casos decididos pelo autor; o diagrama não separa por ramo". Onde: `preparar_dados_figuras.py`, ou `insumos/tabelas/checklist_prisma2020.md` (16a) e `checklist_trAIce.md` (R1).

**R5. "Força" do painel de S9.** A linha "Pesquisa pré-eleitoral × Comparecimento" tem força "fraca" e certeza "moderada", e a §2.8 define a força como tradução da certeza ("fraca, para baixa"). A legenda de S9 explica que a força saiu da ferramenta, calculada com a certeza baixa de uma só célula, e que depende da P042. A contradição está declarada, mas só no suplemento. Correção, no fim do parágrafo da §2.8: "No painel de S9, a força de pesquisa pré-eleitoral × comparecimento continua a da ferramenta (fraca), calculada com uma célula de certeza baixa; com todas as células, a maior certeza é moderada." Onde: esqueleto (ou refazer a caixa por célula na P042).

**R6. Tabelas de S2 contra a prosa de S2 e o artigo.** A prosa de S2 reclassifica três leituras, e as tabelas, que vêm de `insumos/garritty_2024.md`, não mudaram:
- "Prazo [...] | Dentro: a revisão rodou de 19/09 a 24/09/2026", quando a prosa diz que o prazo "ainda não se aplica";
- "Certeza: 22 [...] | Dentro", quando a prosa diz "só em parte";
- "3.3 [...] | Dentro: publicação desde 2010, com justificativa substantiva", quando o artigo (§2.2) diz que o protocolo justificou o corte "sem argumentá-lo".

Correções, em `insumos/garritty_2024.md` (linhas 228 e 233 e a linha da recomendação 22): "Ainda não se aplica: a revisão não terminou"; "Em parte: a certeza foi julgada em 18 células e no agrupamento amplo, com o alvo fixado depois de ver os dados"; "Dentro na forma: o protocolo cita a mudança do ambiente informacional, sem argumentá-la".

**R7. Alcance de "nenhum de pesquisa pré-eleitoral numa eleição".** O Resumo executivo (L72; L67) diz "Em contexto real, há poucos estudos (nenhum de pesquisa pré-eleitoral numa eleição)", e a linha R3 da Tab. 3, "Nenhum estudo, porém, mede pesquisa pré-eleitoral numa eleição real". Os dois valem para o alvo principal (§3.10 diz isso), mas, soltos, contradizem @Cornejo2023a, @Freden2024a, @Dahlgaard2016a, @Meer2015a, @Gerber2020a, @Stolwijk2016a e @Stolwijk2019b, que medem pesquisa pré-eleitoral em eleição real noutras células. Correções: "(nenhum, no alvo principal, de pesquisa pré-eleitoral numa eleição)"; na Tab. 3, "Nenhum estudo desse alvo, porém, mede pesquisa pré-eleitoral numa eleição real." Onde: esqueleto e `revista/tabelas/hipoteses.yml` (linha 220).

**R8. Partidarismo na Tab. 4.** A linha Moderador diz "O partidarismo não atenuou o efeito no único teste pré-especificado dentro da síntese principal (@Cornejo2023a)". Em @Cornejo2023a, o efeito foi maior entre partidários (g 0,33) que entre independentes (0,09) e perto de zero entre quem prefere o PRI (−0,05), como diz a §3.10. A frase escolhe um dos contrastes. Correção: "No único teste pré-especificado dentro da síntese principal (@Cornejo2023a), o efeito foi maior entre partidários que entre independentes e perto de zero entre quem prefere o PRI." Onde: `revista/tabelas/oqf_principal.yml` (linha 42).

**R9. "Brecha dessa regra" (5.2).** L640 (L504): "Essas proibições correspondem a uma regra que o Brasil já aplica, a de só divulgar levantamentos do dia a partir das 17h de Brasília [...]. @Araujo2021a informa sobre uma brecha dessa regra, o voto de quem ainda está na fila quando a apuração começa a ser divulgada." A regra dos levantamentos do dia (Res.-TSE nº 23.600/2019, art. 12) e a do início da divulgação da apuração (Res.-TSE nº 23.669/2021; 19h de Brasília em 2018) são regras diferentes (`contexto_brasil.md`, 7.1 e 7.3); a Tab. 5 descreve o caso certo. Correção: "@Araujo2021a informa sobre uma brecha de outra regra do dia da eleição, a do início da divulgação da apuração: o voto de quem ainda está na fila quando a apuração começa a ser divulgada." Onde: esqueleto.

**R10. Parâmetros ausentes (A15).**
- A §2.4 (L233; L224) não nomeia o modelo do subagente de elegibilidade, e o `relatorio.qmd` (linha 72) nomeia. Correção: "No texto completo, um subagente de IA por PDF (`claude-opus-5`; `claude-opus-5-5` nas fichas feitas depois da Emenda 6b) propôs a elegibilidade [...]".
- A versão do R está marcada "[A confirmar pelo autor]" (§2.7, L269). Não é fato que só o autor sabe: a máquina de análise tem hoje o R 4.5.2, o metafor 5.0.1 e o clubSandwich 0.7.0, mas a versão de cada rodada não ficou no *log*. Correção: "no R 4.5.2 (versão instalada na máquina de análise em 24/09/2026; a versão de cada rodada não ficou registrada)". Os outros cinco marcadores estão onde devem (CRediT, relação com o provedor, condições de acesso e licença).
- Onde: esqueleto.

**R11. Comentários do coordenador desatualizados.** O comentário do esqueleto na linha 35 diz que "ajustado ao estilo do autor" saiu "porque o passe de estilo (etapa 7) ainda não rodou; recoloque depois dele". Os passes de voz e anti-IA rodaram (commits `fe1721b` e `7f450c5`, travas vazias), e a expressão não voltou. O comentário da linha 282 ("conferir ao fim da etapa 7 os agentes e as etapas efetivamente rodados") também segue lá, e a §2.9 está certa quanto às etapas que cita. Os comentários não aparecem para o leitor. Correção: decidir se "ajustado ao estilo do autor" volta ao aviso inicial e à §4.4 e apagar os dois comentários. A prosa do suplemento (S2, S3, S8 e as listas de S11) não passou pelos passes de estilo. Onde: esqueleto.

**R12. O Resumo não traz implicações.** S11 marca o item 10 do PRISMA para resumos como parcial: as Conclusões do Resumo interpretam, mas não trazem implicação. Correção, sem passar das 250 palavras: tirar "**Contexto.** Regular pesquisas exige saber se mudam o voto." (não é item do PRISMA para resumos) e acrescentar ao fim das Conclusões "A evidência não permite concluir sobre regular a divulgação." No *Abstract*, tirar "**Background.** [...]" e acrescentar "The evidence does not support conclusions about regulating poll publication." Onde: esqueleto.

**R13. Saídas locais antigas.** `09-documento-final/revisao_final.html` e `.docx` são das 14:37, e `suplemento.html`, das 14:03, anteriores ao `.qmd` (16:59). As saídas publicadas em `docs/` são das 17:03 e 17:04, trazem o texto atual e passam em `verificar_pdf.py` (artigo com 39 páginas; suplemento com 33). O `revisao_final.pdf` local não existe mais. Correção: apagar ou refazer as cópias locais, para que ninguém confira a versão errada. Não é mudança de texto.

## Situação dos itens da `verificacao_v2.md`

| Item | Situação | Evidência |
|---|---|---|
| E1 S11 vazio | resolvido | S11 tem as cinco listas (PRISMA 2020, resumo, PRISMA-S, SWiM e PRISMA-trAIce), com 185 *links* para âncoras que existem no HTML publicado e números de seção, figura, tabela e quadro certos; as contagens de situação das legendas batem com as linhas |
| E2 painel de S9 | resolvido | estudos (1, 2, 3, 1, 16 e 7) e maior certeza refeitos das 18 células; a força ficou a da ferramenta (R5) |
| E3 "maior experimento de campo" | resolvido | §4.1: "O único experimento de campo indica [...] provavelmente não muda" |
| E4 17 × 16 casos | resolvido | artigo (§2.4, §2.9), S2 (tabela e prosa), `garritty_2024.md` e `relatorio.qmd`; a Emenda 6a explica a linha de teste |
| V1 caixa leu 8 de 18 | resolvido | §2.8 e §5.1 |
| V2 Emenda 4 | resolvido | §2.1 |
| V3 células não randomizadas | resolvido | §4.1, § 1 |
| V4 "se confirmam" | resolvido | §4.1, § 4 |
| V5 nulo sem "provavelmente" | resolvido | Resumo executivo e §3.7 |
| V6 "A revisão em resumo" | resolvido | 49 palavras, com "e não folgada" |
| V7 "efeitos grandes" | resolvido | §3.10, com +11,76 e −11 pontos |
| V8 ressalva dos p < 0,05 | resolvido | §3.8, prosa de S8 e §5.1 ("teste de sinal *post hoc*", "não recebe rótulo direcional") |
| V9 numeração | resolvido | figuras, tabelas e quadros numerados na ordem da primeira chamada |
| V10 *forest plots* | resolvido | `dados_metas.csv` ordenado pelo erro-padrão (0,26; 0,35; 1,04; 1,16 e 0,20 a 0,45), com ordem e risco de viés na legenda |
| V11 fluxograma | em parte | caixas zeradas fora; autor × IA e Emenda 6b só na legenda (R4) |
| V12 excluídos sem referência | resolvido | 13 chaves citadas e presentes em `referencias.json`; S4 lista critério e quem decidiu, e as três extensões da IA batem com as seq 669 a 671 de `correcao_atribuicao.csv` |
| V13 limitações da evidência no Resumo | resolvido | Resumo e *Abstract* |
| V14 Hardmeier no relatório técnico | resolvido | `relatorio.qmd`, linhas 51 e 649 |
| V15 saídas desatualizadas e mancha | resolvido | `docs/` renderizado depois do `.qmd`; `verificar_pdf.py` OK nos dois PDFs (R13 para as cópias locais) |
| V16 conflito com o provedor | resolvido | "[A confirmar pelo autor]" |
| V17 versões | em parte | clubSandwich 0.7.0 na §2.7; versão do R marcada para o autor (R10) |
| R1 0,97 | resolvido | "0,00 a 0,98" e "0,03 a 1,00" em todos os lugares |
| R2 datas | resolvido | 24/09/2026 nos três documentos e na declaração |
| R3 voto obrigatório | resolvido | "tem voto obrigatório codificado (2 [...] e 9 [...])" |
| R4 PL 2.567 | resolvido | "nenhum dos dois tinha sido votado em plenário" |
| R5 Emenda 4 e árbitro | resolvido | CRediT, "[A confirmar pelo autor]" |
| R6 etapas descritas | resolvido | rubrica e leituras L1 e L2 existem (`_avaliacao/`, `_leituras/`) |
| R7 Emenda 3 em S3 | resolvido | linha da Emenda 3 com a troca do árbitro |
| R8 Tab. 3 E7 e R2 | resolvido | "provavelmente não o comparecimento além de ±2 p.p." |
| R9 competidores | resolvido | §3.10 |
| R10 nível de moderador | resolvido | §2.7 |
| R11 "efeito médio" | resolvido e desfeito | Tab. 3 certa; §1.2 voltou a "efeito médio" no passe de voz (V1) |
| R12 "O que mudou" | resolvido | aviso inicial |
| R13 declaração de IA | resolvido | §2.9 e declaração |
| R14 Tab. 2 | justificado | desvio de formato declarado na §3.3 |

## Leitura às cegas

"Sim" quer dizer que o texto com a direção invertida soaria igualmente confiante sem que a certeza o sustentasse.

| Local | Conclusão | Invertida soaria igual? | Registro |
|---|---|---|---|
| Mensagens, 1 | 4 de 4 nas duas células, "Quase todos foram de laboratório ou vinheta", "a evidência é muito incerta" | Não | ok |
| Mensagens, 2 | apertada × folgada "provavelmente não muda", em eleições para governador; demais contrastes divididos | Não | ok |
| Mensagens, 3 | Brasil: "a evidência é muito incerta" | Não | ok |
| Mensagens, 4 | "não demonstra que a divulgação muda votos, nem que é inócua" | Não: simétrica | ok |
| Resumo, Resultados | proporção 1,00 (0,40 a 1,00), "a evidência é muito incerta"; "provavelmente"; "pode" | Não | ok |
| Resumo, Conclusões | "não se sabe se há efeito, nem de que tamanho" | Não | ok |
| *Abstract* | mesmas frases, em inglês | Não | ok |
| Resumo executivo, §§ 2 e 4 | "provavelmente não muda [...] (certeza moderada, que pode cair um nível)"; "isso é diferente de ausência de evidência" | Não | ok |
| Resumo executivo, § 5 | ônus da prova; STF | Não: simétrica | ok |
| Discussão 4.1, § 1 | 9 experimentos *bandwagon* com "a evidência é muito incerta"; não randomizadas com certeza muito baixa; "sem teste" | Não | ok |
| Discussão 4.1, § 2 | campo × jogo "é o padrão que a teoria rival do artefato prevê, ainda que isso não a teste" | Não: a ressalva vem junto | ok |
| Discussão 4.1, § 3 | "o contraste é compatível com um efeito maior em contexto hipotético e com a persistência da direção" | Sim | aviso V2 |
| Discussão 4.1, § 4 | contribuições "ficam de pé em termos modestos", "sugere, numa comparação descritiva e *post hoc*" | Não | ok |
| Conclusões, § 1 | frases padrão por certeza; boca de urna muito incerta | Não | ok |
| Conclusões, § 2 | "não diz de quanto é o efeito [...] nem permite afirmar que elas não têm efeito" | Não: simétrica | ok |
| Linguagem simples, "A revisão em resumo" | "apontam a favor [...] mas a evidência é muito incerta"; "e não folgada" | Não | ok |
| Linguagem simples, "O que isso significa?" | "não permite dizer que as pesquisas mudam o resultado das eleições, nem que não mudam" | Não | ok |
| §5.2, divulgação seletiva (fora do escopo pedido) | "aumentou a vitória desse candidato, [...] com certeza muito baixa" | Sim | aviso V3 |

## Conferências que passaram sem divergência

- **Remontagem e travas:**
  - `montar_revisao_final.py` gerou um `.qmd` idêntico ao atual, e `montar_suplemento.py` regravou o suplemento sem diferença;
  - `conferir_reestruturacao.py`: 0 falhas e 0 avisos;
  - `conferir_numeros.py` entre o commit `c1abeb1` (etapa 6c) e o atual: vazia no esqueleto, no resumo em linguagem simples, em `legendas.yml`, `hipoteses.yml`, `oqf_principal.yml` e `transferibilidade.yml`. No `.qmd` montado, as únicas diferenças são parágrafos inteiros dentro de blocos `:::`, que a trava lê como atributo de *div*;
  - `verificar_figuras.py`: OK nas 7 figuras;
  - `verificar_pdf.py`: OK em `docs/revisao.pdf` (39 páginas) e `docs/suplemento.pdf` (33 páginas).
- **PRISMA** (`prisma_contagens.json`): 1.767 (1.687 + 80); 1.706 = 1.189 + 411 + 106; 1.687 = 1.438 + 118 + 131; 46 e 4 duplicados; 148 e 648 pelo filtro de ano (796); 1.573 e 1.054 triados; 1.314 e 787 excluídos; 259 e 267 buscados (526); 158 e 184 não recuperados (342); 101 e 83 avaliados; 59 e 70 excluídos, com os motivos 39/50, 8/13, 10/4 e 2/3; 41 estudos e 55 relatos (42 + 13); invariantes fechadas. O fluxograma (`dados_prisma.csv`) traz os mesmos números, sem caixas zeradas.
- **Seleção:** 184 avaliados = 165 propostas da IA (47 inclusões e 118 exclusões) + 16 casos do autor (8 e 8) + 3 extensões da IA; 55 incluídos e 129 excluídos.
- **Células:** as 18 células de `celulas.json` batem com `swim_resumo.json` e `certeza.csv` em k, x de y, mistos, nulos, IC de Clopper-Pearson (recalculado por bisseção), p do teste de sinal e certeza (15 muito baixa, 2 baixa, 1 moderada). Os 18 spans `.enunciado` são iguais ao `enunciado` de `certeza.csv`. Os IC da Tab. 2 estão arredondados meio para cima (0,03 a 1,00; 0,00 a 0,98). O n de cada estudo da Tab. 2 bate com `numeros_v2.json`; faixa de 12 a 453.016, e de 12 a 1.113 nos randomizados de apoio.
- **Painel de S9:** 1, 2, 3, 1, 16 e 7 estudos, com a maior certeza de cada grupo de células.
- **Metas:**
  - sem pesquisa: g 0,48 (−1,51 a 2,47; p 0,263; gl 1,25; τ² 0,04; τ 0,20; I² 15%; PI −3,55 a 4,51); com ICC 0,20, 0,51 (−0,97 a 1,98);
  - mesmo candidato: g 0,62 (−0,48 a 1,72; p 0,111; gl 1,46; τ² 0,41; τ 0,64; I² 94%; PI −7,82 a 9,05).
- **Sensibilidades:** 9 de 9 (p 0,004); com os efeitos fora da contagem, 10 de 11 (p 0,012); sem dados anteriores a 2010, 8 de 8 (p 0,008); sem @Araujo2021a, 2 de 3; com os críticos, @Kaplan2019a na direção de desmobilização e *momentum* não randomizado com 2 de 2 (0,16 a 1,00; p 0,5); com ICC 0,20, nenhuma contagem muda.
- **δ:** 0,0441, 0,0464 e 0,0573 (p0 de 0,50, 0,60 e 0,73; `_delta_celula.txt`).
- **Risco de viés:** 43 resultados de 37 estudos; RoB 2 17/6, ROBINS-I 2/8/3, EPOC 6/1; 259 domínios, 171 de consenso e 88 arbitrados (A 79, B 7, outro 2); C01 inteira em algumas preocupações e C02 em risco alto. As afirmações da §4.4 sobre D5 (@Westwood2020a, @Meer2015a, @Boukouras2020a, @Gerber2020a) e sobre a imprecisão das células de 1 estudo batem com S5 e com as notas da Tab. 2.
- **Extração e arbitragem:** 560 efeitos de 40 estudos, 70 principais; 772 correções, 240 extensões; 13 efeitos promovidos, 5 rebaixados e 6 linhas novas; reextração de 40 estudos e 56 efeitos (15, 23, 12 e 6) e 28 estudos arbitrados.
- **Efeitos citados** (`efeitos.csv`): @Dahlgaard2016a 0,12 (0,080; +3,40 p.p.); @Meer2015a 0,13 (0,072); @Cornejo2023a 0,19 (0,105), com subgrupos 0,33, 0,09 e −0,05; @Westwood2020a −0,10 (0,023), IC superior −0,051; @Freden2024a −0,41; @Chatterjee2019a −0,29 e −0,42; @Lammers2022a 1,25, 1,03, −0,39 e 0,06; @Araujo2021a +5,69 e +11,76 p.p.; @Morton2015a −11 p.p.; @Gerber2020a 0,29 p.p. (carta, E31) e 0,08 p.p. (variável instrumental, E12), os dois IC dentro de ±0,046; @Schlegel2023 +11 e +17 p.p.; @Feltovich2022 0,25 e 0,44.
- **Tab. 1 e transferibilidade:** as 35 porcentagens refeitas com denominador 41 e presentes no artigo; 3 estudos com voto obrigatório e 10 com o dado; 11 estudos de comparecimento na síntese (2 "não" e 9 sem a informação); 17 estudos medem comparecimento; 4 em dois turnos; 3 com regra de divulgação, 2 deles na síntese.
- **Revisões anteriores:** @Barnfield2019 (conceitual, "only ten discuss mobilisation", advertência sobre o estímulo único e a identificação partidária); @MoyRinke2012 (narrativa, sem conclusão sobre qual efeito predomina, achados antigos de *underdog*, Hardmeier e Roth como menção sem leitura); @Cosgun2026 (uma base, só inglês, alegações causais mais fortes em laboratório e *survey*); @Hardmeier2008 sempre como não verificada.
- **Brasil:** Lei 9.504/1997 (registro com cinco dias, multa, crime de pesquisa fraudulenta, crime de boca de urna), Res.-TSE 23.600/2019 (art. 11 e art. 12, 17h de Brasília), Res.-TSE 23.669/2021 e unificação de 2022, 19h de Brasília em 2018, ADIs 3.741, 3.742 e 3.743, PLs 2.567 e 2.558/2022 (sem votação em plenário em 24/09/2026), pedido de CPI sem afirmar instalação, ESOMAR/WAPOR (América Latina, sete dias na mediana), @Meireles2022 e @PereiraNunes2024. A biometria, as 19h e Bolsonaro à frente em 2018 e o voto obrigatório "com multa pequena" vêm da ficha de @Araujo2021a (`05-decomposicao/fichas/fichamento_Araujo2021a.md`, linhas 28, 37 e 66).
- **Revisões rápidas:** as citações literais de Garritty ("led only by experienced systematic reviewers", "carefully considered", "at a minimum search strategies should be double checked [...]", "the same approach for full text screening", "the absence of peer review [...]", "Register the protocol [...]", "no longer than six months") estão em `garritty_2024.md`, e as recomendações 9, 12, 16 e 23 pedem uma segunda pessoa.
- **Marcações humanas:** 11 caixas, nas seções correspondentes às do v1 e com os mesmos IDs; o apêndice lista as 18 pendências abertas (a P042 com as 22 células do campo `n` do JSON); 6 marcadores "[A confirmar pelo autor]"; declaração de IA aberta por "RASCUNHO NÃO VALIDADO". Todo papel atribuído ao autor tem registro: G1 e G2, Emenda 1 e os 16 casos na Emenda 6a; registro, financiamento e conflitos no protocolo (linhas 21 e 27); Emendas 4 e 6b e a troca do árbitro em `emendas.md`, com a Emenda 4 e o árbitro marcados na CRediT.
- **Palavras** (espaços | contagem da trava): Resumo 241 | 248 (até 250); *Abstract* 241 | 246; Mensagens 197; resumo em linguagem simples 739 | 748 (de 600 a 750); "A revisão em resumo" 49 (até 50).
- **Saídas publicadas:** `docs/revisao.html` e `.docx` trazem as frases do texto atual, conferidas por amostra; nenhuma referência ou chamada cruzada ficou sem resolver.

## Scripts usados

Rodados da raiz do projeto, com `python3 -B`:

1. `python3 -B 09-documento-final/montar_revisao_final.py --saida <scratchpad>/rf_montado.qmd`, seguido de `diff` com `revisao_final.qmd`: idênticos.
2. `python3 -B 09-documento-final/montar_suplemento.py`: regravou `suplemento.qmd`, idêntico à cópia anterior.
3. `python3 -B 09-documento-final/conferir_reestruturacao.py` (também com `--suplemento`): 0 falhas e 0 avisos.
4. `python3 -B 09-documento-final/conferir_numeros.py <versão de c1abeb1> <versão atual>`, no esqueleto, no resumo em linguagem simples, em `legendas.yml` e nas três tabelas editáveis: saída vazia.
5. `python3 -B 09-documento-final/revista/figuras/verificar_figuras.py`: OK.
6. `python3 -B 09-documento-final/revista/verificar_pdf.py docs/revisao.pdf --artigo` e `docs/suplemento.pdf --suplemento`: OK.
7. `git diff --word-diff=plain c1abeb1 HEAD`, no esqueleto, no resumo em linguagem simples, nas legendas, nas tabelas editáveis e nos textos da vitrine, lido palavra a palavra para achar verbos mais fortes e fatos novos.
8. `verif_final.py`, escrito para esta verificação e transcrito abaixo. Resultado em 24/09/2026: 144 verificações OK, 0 divergências e 69 linhas INFO, que registram, entre outras coisas, os trechos das divergências acima (todos presentes no texto atual).
9. Consultas avulsas: `08-revisao-humana/efeitos/aplicacao_arbitragem.csv` (41 não aplicadas), `comparacao_cega*.csv`, `03-textos/elegibilidade_tc_final.csv` (seq 669 a 671), a ficha de @Araujo2021a, `docs/revisao.html` (âncoras, números de seção e legendas), `Rscript --version`, `quarto --version` e `quarto typst --version`.

### Transcrição de `verif_final.py`

O *script* foi rodado de uma pasta temporária e não fica no projeto. Para refazer a verificação, basta copiar o bloco abaixo e rodá-lo com `python3 -B`.

```python
"""Verificação final independente: refaz, a partir dos arquivos primários, os números e as conferências de texto
do artigo, do suplemento e do resumo em linguagem simples. Só lê arquivos. Uso: python3 -B verif_final.py
"""
import csv
import html as H
import json
import math
import re
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP
from math import comb
from pathlib import Path

R = Path("/Users/felipelmc/Desktop/pesquisas-eleitorais-rs")
D = R / "09-documento-final"
out = []


def ok(cond, msg):
    out.append(("OK  " if cond else "DIV ") + msg)


def info(msg):
    out.append("INFO " + msg)


def lcsv(p):
    return list(csv.DictReader(open(p, encoding="utf-8-sig")))


def cp(x, n, a=0.05):
    def cdf(k, n, p):
        return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))

    def bis(f, lo=0.0, hi=1.0):
        for _ in range(200):
            m = (lo + hi) / 2
            if f(m):
                lo = m
            else:
                hi = m
        return (lo + hi) / 2
    lo = 0.0 if x == 0 else bis(lambda p: 1 - cdf(x - 1, n, p) < a / 2)
    hi = 1.0 if x == n else bis(lambda p: cdf(x, n, p) > a / 2)
    return lo, hi


def psinal(x, n):
    if n == 0:
        return None
    k = min(x, n - x)
    return min(1.0, 2 * sum(comb(n, i) for i in range(0, k + 1)) / 2 ** n)


def br(v, casas=2):
    # arredonda a 9 casas antes (tira o ruído da bisseção: 0,0249999999 -> 0,025) e depois meio para cima
    q = Decimal(str(round(v, 9))).quantize(Decimal(1).scaleb(-casas), ROUND_HALF_UP)
    return f"{q}".replace(".", ",")


A = (D / "revisao_final.qmd").read_text(encoding="utf-8")
ESQ = (D / "_esqueleto_revisao_final.qmd").read_text(encoding="utf-8")
SUP = (D / "suplemento.qmd").read_text(encoding="utf-8")
LS = (D / "linguagem_simples.qmd").read_text(encoding="utf-8")
V1 = (D / "_revisao_final_v1_oqf.qmd").read_text(encoding="utf-8")
LEG = (D / "revista/figuras/legendas.yml").read_text(encoding="utf-8")
TODOS = {"artigo": A, "suplemento": SUP, "linguagem simples": LS}

# ------------------------------------------------------------------ 1. PRISMA
P = json.load(open(R / "07-relatorio/prisma_contagens.json"))
b, o = P["bases"], P["outros_metodos"]
ok(b["identificados"]["bases"] == 1767 and b["identificados"]["por_fonte"] == {"openalex": 1687, "bdtd": 80}, "PRISMA identificados 1.767 (1.687 + 80)")
ok(o["identificados"]["busca_citacoes"] == 1706, f"citação 1.706 ({o['identificados']['busca_citacoes']})")
ok(1189 + 411 + 106 == 1706 and 1438 + 118 + 131 == 1687, "SN1+SN2+SN3 = 1.706; B05+B02+B03 = 1.687")
ok((b["buscados"], o["buscados"], b["nao_recuperados"], o["nao_recuperados"]) == (259, 267, 158, 184), "buscados 259/267, não recuperados 158/184")
ok((b["avaliados"], o["avaliados"]) == (101, 83), f"avaliados 101/83 ({b['avaliados']}/{o['avaliados']})")
ok(b["removidos_antes_triagem"]["automacao"] + o["removidos_antes_triagem"]["automacao"] == 796, "796 pelo filtro de ano")
ok(all(i["ok"] for i in P["invariantes"]), "invariantes do PRISMA fecham")
info("PRISMA chaves bases: " + json.dumps({k: v for k, v in b.items() if k not in ('identificados',)}, ensure_ascii=False)[:900])
info("PRISMA chaves outros: " + json.dumps({k: v for k, v in o.items() if k not in ('identificados',)}, ensure_ascii=False)[:900])
info("PRISMA incluídos: " + json.dumps(P.get("incluidos", P.get("inclusao", {})), ensure_ascii=False)[:400])

# ------------------------------------------------------------------ 2. células
S = json.load(open(R / "06-analise/swim_principal/swim_resumo.json"))
C = json.load(open(D / "revista/celulas.json"))
cert = lcsv(R / "06-analise/certeza.csv")
K5 = ("familia_intervencao", "construto_outcome", "comparador_tipo", "celula_alvo", "classe_desenho")
chave_cert = {tuple(r[k] for k in K5): r for r in cert}
grupos = {tuple(g[k] for k in K5): g for g in S["grupos"]}
cel_por_id = {}
for c in C["celulas"]:
    k = tuple(c[x] for x in K5)
    g = grupos[k]
    x, n = g["n_beneficos"], g["n_estudos"]
    lo, hi = cp(x, n) if n else (None, None)
    p = psinal(x, n)
    iguais = (c["k"] == g["k_estudos"] and c["n_beneficos"] == x and c["n_estudos_com_direcao"] == n
              and c["n_mistos"] == g["n_mistos"] and c["n_nulos"] == g["n_nulos"]
              and (n == 0 or (abs(lo - c["ic_proporcao"][0]) < 1e-6 and abs(hi - c["ic_proporcao"][1]) < 1e-6))
              and (p is None or abs(p - c["p_sinal"]) < 1e-9)
              and chave_cert[k]["certeza"] == c["certeza"] and set(c["estudos"]) == set(g["estudos"])
              and chave_cert[k]["enunciado"].strip() == c["enunciado"].strip())
    ok(iguais, f"{c['id']} k={c['k']} {x}/{n} IC=({None if lo is None else round(lo, 4)}, {None if hi is None else round(hi, 4)}) p={p} certeza={c['certeza']}")
    cel_por_id[c["id"]] = c
    # enunciado no artigo igual ao de certeza.csv
    span = re.search(r"\[([^\[\]]+)\]\{\.enunciado cel=\"" + c["id"] + r"\"\}", A)
    ok(span is not None and span.group(1).strip() == c["enunciado"].strip(), f"{c['id']}: span do artigo = enunciado de certeza.csv")
    # linha da Tab. 2: direção e IC formatados
    if n:
        ic_txt = f"IC 95% {br(lo)} a {br(hi)}"
        linha = [l for l in A.split("\n") if f'cel="{c["id"]}"' in l and l.startswith("|")]
        ok(bool(linha) and ic_txt in linha[0], f"{c['id']}: Tab. 2 traz '{ic_txt}'")
ok(Counter(r["certeza"] for r in cert) == Counter({"muito_baixa": 15, "baixa": 2, "moderada": 1}), "certeza: 15 muito baixa, 2 baixa, 1 moderada")
est_sint = sorted({e for g in S["grupos"] for e in g["estudos"]})
ok(len(est_sint) == 27, f"27 estudos na síntese principal ({len(est_sint)})")
ok(sum(1 for g in S["grupos"] if g["k_estudos"] > 0) == 18 and len(S["grupos"]) == 19, "18 células com estudo, 19 grupos")
# 0,97 (arredondamento) não pode sobrar
for nome, t in TODOS.items():
    ok("0,97)" not in t and "0,00 a 0,97" not in t, f"{nome}: sem o '0,97' do arredondamento assimétrico (R1 da v2)")

# painel da caixa (S9) contra as células
linhas_painel = re.findall(r"^\| (Agregador ou projeção|Boca de urna|Apuração parcial oficial|Pesquisa pré-eleitoral) \| (Apoio|Comparecimento) \| (\w+) \| (\w+) \| ([\w ]+) \| (\d+) \|$", SUP, re.M)
fam = {"Agregador ou projeção": "agregador_projecao", "Boca de urna": "boca_de_urna", "Apuração parcial oficial": "outro", "Pesquisa pré-eleitoral": "pesquisa_pre_eleitoral"}
con = {"Apoio": "apoio_ao_lider", "Comparecimento": "mobilizacao"}
ordem = ["muito_baixa", "baixa", "moderada", "alta"]
for f_, c_, rot, forca, certz, nest in linhas_painel:
    cs = [c for c in C["celulas"] if c["familia_intervencao"] == fam[f_] and c["construto_outcome"] == con[c_]]
    est = {e for c in cs for e in c["estudos"]}
    maior = max((c["certeza"] for c in cs), key=ordem.index).replace("_", " ")
    ok(int(nest) == len(est) and certz.strip() == maior, f"S9 painel {f_} × {c_}: {nest} estudos, certeza {certz}; células: {len(est)}, {maior}; força '{forca}'")

# ------------------------------------------------------------------ 3. metas
for nome, pasta, esperado in [("sem pesquisa", "meta_exploratoria", (0.48, -1.51, 2.47, 0.263, 1.25, 0.04, 0.20, 15, -3.55, 4.51)),
                              ("mesmo candidato", "meta_mesmo_candidato", (0.62, -0.48, 1.72, 0.111, 1.46, 0.41, 0.64, 94, -7.82, 9.05))]:
    m = json.load(open(R / f"06-analise/{pasta}/meta_resumo.json"))["grupos"][0]["resultado"]
    obt = (round(m["estimativa"], 2), round(m["ic"][0], 2), round(m["ic"][1], 2), round(m["p"], 3), round(m["gl"], 2),
           round(m["tau2"], 2), round(m["tau"], 2), round(m["I2"]), round(m["pi"][0], 2), round(m["pi"][1], 2))
    ok(obt == esperado, f"meta {nome}: {obt}")
mi = json.load(open(R / "06-analise/meta_exploratoria_icc020/meta_resumo.json"))["grupos"][0]["resultado"]
ok((round(mi["estimativa"], 2), round(mi["ic"][0], 2), round(mi["ic"][1], 2)) == (0.51, -0.97, 1.98), f"meta ICC 0,20: {round(mi['estimativa'],2)} ({round(mi['ic'][0],2)} a {round(mi['ic'][1],2)})")

# ------------------------------------------------------------------ 4. RoB
rg = lcsv(R / "04-qualidade/rob_geral.csv")
ok(len(rg) == 43 and len({r['chave'] for r in rg}) == 37, "RoB: 43 resultados de 37 estudos")
cont = Counter((r["ferramenta"], r["rob_geral"]) for r in rg)
ok(cont == Counter({("rob2", "algumas_preocupacoes"): 17, ("rob2", "alto"): 6, ("robins_i", "grave"): 8, ("robins_i", "critico"): 3,
                    ("robins_i", "moderado"): 2, ("epoc", "alto"): 6, ("epoc", "baixo"): 1}), f"RoB geral por ferramenta: {dict(cont)}")
info("EPOC baixo: " + str([(r["chave"], r.get("construto_outcome", r.get("construto", ""))) for r in rg if r["ferramenta"] == "epoc" and r["rob_geral"] == "baixo"]))
info("ROBINS-I moderado: " + str([(r["chave"], r.get("construto_outcome", r.get("construto", ""))) for r in rg if r["rob_geral"] == "moderado"]))
tot = auto = 0
seg = Counter()
for f in ["rob_rob2_consenso.csv", "rob_robins_i_consenso.csv", "rob_epoc_consenso.csv"]:
    for r in lcsv(R / "04-qualidade" / f):
        tot += 1
        if r["julgamento_a"] == r["julgamento_b"]:
            auto += 1
        else:
            seg["A" if r["julgamento_consenso"] == r["julgamento_a"] else "B" if r["julgamento_consenso"] == r["julgamento_b"] else "outro"] += 1
ok((tot, auto, seg["A"], seg["B"], seg["outro"]) == (259, 171, 79, 7, 2), f"domínios {tot}, consenso {auto}, árbitro A/B/outro {seg['A']}/{seg['B']}/{seg['outro']}")
# C01 algumas preocupações, C02 alto
geral = {}
for r in rg:
    geral.setdefault(r["chave"], set()).add(r["rob_geral"])
ok(all(geral[e] == {"algumas_preocupacoes"} for e in cel_por_id["C01"]["estudos"]), "C01: todos em algumas preocupações")
ok(all(geral[e] == {"alto"} for e in cel_por_id["C02"]["estudos"]), "C02: todos em risco alto")
# 'todos os experimentos com algumas preocupações ou risco alto' (Resumo)
nr = [(r["chave"], r["ferramenta"], r["rob_geral"]) for r in rg if r["ferramenta"] != "rob2" and r["rob_geral"] in ("baixo", "moderado")]
info(f"resultados não RoB 2 em risco baixo ou moderado (contraexemplos a 'todos os experimentos'): {nr}")

# ------------------------------------------------------------------ 5. decisões do autor, correções, arbitragem
ca = lcsv(R / "00-protocolo/correcao_atribuicao.csv")
lim = [r for r in ca if r["classificacao"] == "mantida" and r["etapa"] == "07_textos_elegibilidade"]
reais = {r["objeto"].split()[0] for r in lim if "teste" not in r["observacao"]}
ok(len(lim) == 17 and len(reais) == 16, f"casos limítrofes do autor: {len(lim)} linhas no log, {len(reais)} registros distintos")
corr = lcsv(R / "05-decomposicao/correcoes_sessao_2026-09-23.csv")
ext = sum(1 for r in corr if r["origem"].startswith("coordenador de IA, extens"))
mp = Counter((r["de"], r["para"]) for r in corr if r["campo"] == "modelo_principal")
novas = sum(1 for r in corr if r["campo"] == "*linha_nova*")
ok(len(corr) == 772 and ext == 240 and mp[("nao", "sim")] == 13 and mp[("sim", "nao")] == 5 and novas == 6,
   f"correções {len(corr)}, extensões {ext}, promovidos {mp[('nao','sim')]}, rebaixados {mp[('sim','nao')]}, linhas novas {novas}")
na = list(csv.reader(open(R / "08-revisao-humana/efeitos/aplicacao_arbitragem.csv", encoding="utf-8-sig")))[1:]
na_c = Counter((x[1], x[3]) for x in na if x[0] == "nao_aplicado")
info(f"não aplicadas: {sum(na_c.values())} ({dict(na_c)}); o artigo diz 'barrou 40', todas de Morton2015a")
ef = lcsv(R / "06-analise/efeitos.csv")
ok(len(ef) == 560 and len({r['chave'] for r in ef}) == 40 and sum(1 for r in ef if r["modelo_principal"] == "sim") == 70, "560 efeitos de 40 estudos, 70 principais")

# ------------------------------------------------------------------ 6. efeitos citados no texto
E = {(r["chave"], r["id_efeito"].split("-")[-1]): r for r in ef}


def g(ch, e):
    r = E[(ch, e)]
    return float(r["yi"]) if r["yi"] not in ("", "NA") else None, float(r["sei"]) if r["sei"] not in ("", "NA") else None, r


for (ch, e, esp_g, esp_ep, pp) in [("Dahlgaard2016a", "E01", 0.12, 0.080, 3.4), ("Meer2015a", "E01", 0.13, 0.072, None),
                                  ("Cornejo2023a", "E05", 0.19, 0.105, None), ("Westwood2020a", "E01", -0.10, 0.023, -3.4),
                                  ("Freden2024a", "E01", -0.41, None, None), ("Chatterjee2019a", "E02", -0.29, None, None),
                                  ("Chatterjee2019a", "E08", -0.42, None, None), ("Lammers2022a", "E06", 1.25, None, None),
                                  ("Lammers2022a", "E08", 1.03, None, None), ("Lammers2022a", "E07", -0.39, None, None),
                                  ("Lammers2022a", "E09", 0.06, None, None), ("Araujo2021a", "E01", None, None, 5.69),
                                  ("Araujo2021a", "E06", None, None, 11.76), ("Morton2015a", "E12", None, None, -11.0),
                                  ("Gerber2020a", "E31", None, None, 0.29), ("Gerber2020a", "E12", None, None, 0.08)]:
    yi, sei, r = g(ch, e)
    c1 = esp_g is None or (yi is not None and round(yi, 2) == esp_g)
    c2 = esp_ep is None or (sei is not None and round(sei, 3) == esp_ep)
    c3 = pp is None or (r["efeito_pp"] not in ("", "NA") and abs(float(r["efeito_pp"]) - pp) < 0.006)
    ok(c1 and c2 and c3, f"{ch} {e}: g={yi if yi is None else round(yi, 3)} EP={sei if sei is None else round(sei, 3)} pp={r['efeito_pp']} (texto g={esp_g}, EP={esp_ep}, pp={pp})")
for ch, e in [("Gerber2020a", "E12"), ("Gerber2020a", "E31")]:
    yi, sei, r = g(ch, e)
    lo, hi = yi - 1.96 * sei, yi + 1.96 * sei
    ok(-0.046 <= lo and hi <= 0.046, f"{ch} {e}: IC ({lo:.4f}; {hi:.4f}) dentro de ±0,046; modelo='{r['modelo'][:80]}'")
yi, sei, r = g("Westwood2020a", "E01")
ok(yi + 1.96 * sei < -0.046, f"Westwood2020a: IC superior {yi + 1.96 * sei:.4f} abaixo de −δ")
for ch, e in [("Dahlgaard2016a", "E01"), ("Meer2015a", "E01"), ("Cornejo2023a", "E05")]:
    yi, sei, r = g(ch, e)
    info(f"{ch} {e}: IC 95% ({yi - 1.96 * sei:.3f}; {yi + 1.96 * sei:.3f})")
info("Schlegel2023: " + str([(r["id_efeito"], r["efeito_pp"]) for r in ef if r["chave"] == "Schlegel2023" and r["modelo_principal"] == "sim"]))
info("Feltovich2022: " + str([(r["id_efeito"], r["beta"]) for r in ef if r["chave"] == "Feltovich2022" and r["modelo_principal"] == "sim"]))
info("Cornejo2023a subgrupos: " + str([(r["id_efeito"], r["subgrupo"][:40], round(float(r["yi"]), 2)) for r in ef if r["chave"] == "Cornejo2023a" and r["yi"] not in ("", "NA") and r["subgrupo"] not in ("", "NA")]))
# faixa de n (12 a 453.016) e (12 a 1.113) nos randomizados de apoio
nv2 = json.load(open(D / "revista/numeros_v2.json"))
ns = [x["n"] for cc in nv2["sof_n_por_estudo"]["por_celula"].values() for x in cc if x["n"]]
ok(min(ns) == 12 and max(ns) == 453016, f"faixa de n nas células: {min(ns)} a {max(ns)}")
nrand = [x["n"] for cid in ("C01", "C02", "C03") for x in nv2["sof_n_por_estudo"]["por_celula"][cid] if x["n"]]
ok(min(nrand) == 12 and max(nrand) == 1113, f"n nos randomizados de apoio: {min(nrand)} a {max(nrand)}")
# g entre 0,12 e 0,19 (4.1)
info("g de 0,12 a 0,19 em 4.1: Dahlgaard 0,12, Meer 0,13, Cornejo 0,19 (conferidos acima)")

# ------------------------------------------------------------------ 7. sensibilidades
def swim(pasta):
    return json.load(open(R / f"06-analise/{pasta}/swim_resumo.json"))["grupos"]


for pasta, alvo, esp in [("swim_sens_agrupamento_amplo", ("apoio_ao_lider", "principal", "randomizado"), (9, 9, 0.004)),
                         ("swim_sens_com_excluidos_amplo", ("apoio_ao_lider", "principal", "randomizado"), (10, 11, 0.012)),
                         ("swim_sens_sem_pre2010_amplo", ("apoio_ao_lider", "principal", "randomizado"), (8, 8, 0.008)),
                         ("swim_sens_sem_araujo_amplo", ("apoio_ao_lider", "principal", "nao_randomizado"), (2, 3, 1.0))]:
    gg = [g_ for g_ in swim(pasta) if (g_["construto_outcome"], g_["celula_alvo"], g_["classe_desenho"]) == alvo]
    g_ = gg[0]
    ok((g_["n_beneficos"], g_["n_estudos"], round(g_["p_sinal"], 3)) == esp, f"{pasta} {alvo}: {g_['n_beneficos']} de {g_['n_estudos']}, p={round(g_['p_sinal'], 3)}")
cc = [g_ for g_ in swim("swim_sens_com_critico") if "Unkelbach2022a" in g_["estudos"]][0]
ok((cc["n_beneficos"], cc["n_estudos"], round(cc["ic_proporcao"][0], 2), cc["p_sinal"]) == (2, 2, 0.16, 0.5), f"com críticos, momentum não randomizado: {cc['n_beneficos']} de {cc['n_estudos']}, IC {cc['ic_proporcao']}, p {cc['p_sinal']}")
kk = [g_ for g_ in swim("swim_sens_com_critico") if "Kaplan2019a" in g_["estudos"]][0]
ok(kk["n_danosos"] == 1, "com críticos: Kaplan2019a na direção de desmobilização")
# ICC 0,20 não muda contagem
g0 = {tuple(x[k] for k in K5): (x["n_beneficos"], x["n_danosos"], x["n_mistos"], x["n_nulos"]) for x in S["grupos"]}
g2 = {tuple(x[k] for k in K5): (x["n_beneficos"], x["n_danosos"], x["n_mistos"], x["n_nulos"]) for x in swim("swim_sens_icc020")}
ok(g0 == g2, "ICC 0,20 não muda nenhuma contagem por célula")

# ------------------------------------------------------------------ 8. δ
for p0, esp in [(0.50, 0.044), (0.60, 0.046), (0.73, 0.0573)]:
    p1 = p0 + 0.02
    d = math.log((p1 / (1 - p1)) / (p0 / (1 - p0))) * math.sqrt(3) / math.pi
    ok(abs(d - esp) < 0.0006, f"δ com p0 = {p0}: g = {d:.4f} (texto {esp})")
ok((R / "06-analise/_delta_celula.txt").read_text().strip() == "0.0573", "_delta_celula.txt = 0.0573")

# ------------------------------------------------------------------ 9. numeros_v2: refazer fórmulas
N = json.load(open(D / "insumos/tabelas/numeros.json"))
for l in nv2["tab1_caracteristicas"]["linhas"]:
    esperado = float(Decimal(str(100 * l["n"] / l["denominador"])).quantize(Decimal("0.1"), ROUND_HALF_UP))
    ok(abs(esperado - l["pct"]) < 1e-9 and l["denominador"] == 41, f"Tab. 1 {l['grupo']}/{l['codigo']}: {l['n']}/{l['denominador']} = {esperado}% (json {l['pct']})") if abs(esperado - l["pct"]) >= 1e-9 else None
ok(all(abs(float(Decimal(str(100 * l["n"] / l["denominador"])).quantize(Decimal("0.1"), ROUND_HALF_UP)) - l["pct"]) < 1e-9 for l in nv2["tab1_caracteristicas"]["linhas"]), f"Tab. 1: {len(nv2['tab1_caracteristicas']['linhas'])} porcentagens refeitas")
for l in nv2["tab1_caracteristicas"]["linhas"]:
    pct = br(l["pct"], 1)
    if f"| {l['n']} ({pct}) |" not in A:
        out.append(f"DIV Tab. 1: '{l['n']} ({pct})' não aparece no artigo ({l['grupo']}/{l['codigo']})")
M = lcsv(R / "05-decomposicao/fichamentos_master.csv")
vo_sim = sorted(r["citekey"] for r in M if r.get("voto_obrigatorio", "").strip().lower().startswith("sim"))
vo_inf = sorted(r["citekey"] for r in M if r.get("voto_obrigatorio", "").strip().lower().startswith(("sim", "não", "nao")))
ok(vo_sim == sorted(nv2["transf_voto_obrigatorio_sim"]["chaves"]) and len(vo_inf) == 10, f"voto obrigatório: sim {vo_sim}; informado {len(vo_inf)}")
comp_sint = sorted({e for c in C["celulas"] if c["construto_outcome"] == "mobilizacao" for e in c["estudos"]})
vo = {r["citekey"]: r.get("voto_obrigatorio", "") for r in M}
ok(len(comp_sint) == 11, f"11 estudos de comparecimento na síntese: {len(comp_sint)}; voto_obrig: {Counter(vo.get(e, '?')[:3] for e in comp_sint)}")
dt = sorted(r["citekey"] for r in M if r.get("sistema_eleitoral", "") == "maioria_dois_turnos")
ok(len(dt) == 4, f"dois turnos: {dt}")
comp17 = sorted(r["citekey"] for r in M if "mobilizacao" in r.get("construto_outcome", ""))
ok(len(comp17) == 17, f"17 estudos medem comparecimento ({len(comp17)})")
ok(N["pendencias"] == 18 and nv2["pendencias_abertas"]["valor"] == 18, "18 pendências nos dois JSON")

# ------------------------------------------------------------------ 10. pendências e apêndice
pend = json.load(open(R / "07-relatorio/_pendencias_abertas.json"))
ids = [p["id"] for p in pend["pendencias"] if p["status"] == "aberta"]
tab = re.findall(r"^\| (P0\d\d) \|", A, re.M)
ok(sorted(ids) == sorted(tab) and len(ids) == 18, f"apêndice: {len(tab)} pendências; abertas no JSON: {len(ids)}")
p42 = [p for p in pend["pendencias"] if p["id"] == "P042"][0]
info("P042 no JSON: " + json.dumps(p42, ensure_ascii=False)[:600])

# ------------------------------------------------------------------ 11. texto: palavras


def palavras_ws(t):
    t = re.sub(r"\[([^\]]*)\]\{[^}]*\}", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return len([w for w in t.replace("*", "").split() if re.search(r"\w", w)])


def palavras_rx(t):
    t = re.sub(r"\{(?=[#.]|[\w-]+=)[^{}\n]*\}", " ", t)
    t = re.sub(r"\]\([^)\n]*\)", "]", t)
    return len(re.findall(r"[0-9A-Za-zÀ-ÿ]+(?:[-'’][0-9A-Za-zÀ-ÿ]+)*", t))


res = re.search(r"# Resumo \{#resumo.*?\n(.*?)\*\*Palavras-chave", A, re.S).group(1)
abs_ = re.search(r"# Abstract \{#abstract.*?\n(.*?)\*\*Keywords", A, re.S).group(1)
msg = re.search(r"# Mensagens principais.*?\n(.*?)\n:::", A, re.S).group(1)
ls_corpo = re.sub(r"^#+ .*$|^:::.*$", "", LS.split("---", 2)[2], flags=re.M)
ls_res = re.search(r"## A revisão em resumo\n\n(.*?)\n\n:::", LS, re.S).group(1)
info(f"palavras (espaços | regex da trava): resumo {palavras_ws(res)} | {palavras_rx(res)} (até 250); abstract {palavras_ws(abs_)} | {palavras_rx(abs_)}; "
     f"mensagens {palavras_ws(msg)} | {palavras_rx(msg)}; linguagem simples {palavras_ws(ls_corpo)} | {palavras_rx(ls_corpo)} (600 a 750); "
     f"'A revisão em resumo' {palavras_ws(ls_res)} | {palavras_rx(ls_res)} (até 50)")

# ------------------------------------------------------------------ 12. numeração de figuras, tabelas e quadros
linhas = A.split("\n")
defs, prim = {}, {}
for i, l in enumerate(linhas, 1):
    for m in re.finditer(r"\{#((?:fig|tbl|qdr)-[\w-]+)", l):
        defs.setdefault(m.group(1), i)
    for m in re.finditer(r"@((?:fig|tbl|qdr)-[\w-]+)", l):
        prim.setdefault(m.group(1), i)
for tipo in ("fig", "tbl", "qdr"):
    ks = sorted([k for k in defs if k.startswith(tipo)], key=defs.get)
    chamadas = sorted([k for k in ks if k in prim], key=prim.get)
    ok([k for k in ks if k in prim] == chamadas and all(prim[k] <= defs[k] + 1 for k in chamadas),
       f"{tipo}: numeração {ks} x ordem da 1ª chamada {chamadas}")

# ------------------------------------------------------------------ 13. chaves de citação
refs = {r["id"]: r for r in json.load(open(D / "revista/referencias.json"))}
for nome, t in (("artigo", A), ("suplemento", SUP), ("linguagem simples", LS)):
    ks = {k for k in re.findall(r"(?<![\w.])@([A-Za-z][\w:-]*\w)", re.sub(r"https?://\S+", "", t))
          if not k.startswith(("fig-", "tbl-", "sec-", "qdr-"))}
    falt = sorted(k for k in ks if k not in refs)
    ok(not falt, f"{nome}: {len(ks)} chaves, ausentes em referencias.json: {falt}")
for k in ["Bischoff2012", "Hizen2025", "Morton2015b", "Scheuerman2019", "Scheuerman2020", "Scheuerman2021", "Yosef2017", "Reveco2026",
          "Corbetta2013", "Kim2018b", "Kim2025a", "Freden2021", "Mavridis2016a"]:
    r = refs.get(k)
    ano = (r or {}).get("issued", {}).get("date-parts", [[None]])[0][0] if r else None
    info(f"excluído citado {k}: {'presente' if r else 'AUSENTE'}; ano {ano}; título {(r or {}).get('title', '')[:70]}")

# ------------------------------------------------------------------ 14. caixas, marcadores e termos


def callouts(t):
    blocos = re.findall(r"## Pendente de revisão humana\n\n(.*?)\n:::", t, re.S)
    return Counter(tuple(sorted(set(re.findall(r"P0\d\d", bl)))) for bl in blocos)


ok(callouts(A) == callouts(V1) and sum(callouts(A).values()) == 11, f"11 caixas com os mesmos conjuntos de IDs do v1: {sum(callouts(A).values())}; {dict(callouts(A))}")
info(f"marcadores [A confirmar pelo autor]: artigo {A.count('[A confirmar pelo autor]')}, suplemento {SUP.count('[A confirmar pelo autor]')}, LS {LS.count('[A confirmar pelo autor]')}")
for nome, t in TODOS.items():
    achados = re.findall(r"(?i)significativ\w*|\bneutro\b|sem efeito|não tem efeito|não têm efeito|permite descartar|é evidência de que", t)
    info(f"{nome}: termos a conferir {Counter(achados)}")
    em = [m.start() for m in re.finditer(r"efeito médio", t)]
    info(f"{nome}: 'efeito médio' em {len(em)} lugar(es): " + " | ".join(t[max(0, i - 60):i + 40].replace("\n", " ") for i in em))

# ------------------------------------------------------------------ 15. S11 e links entre documentos
h = (R / "docs/revisao.html").read_text(encoding="utf-8")
hs = (R / "docs/suplemento.html").read_text(encoding="utf-8")
ids_a = set(re.findall(r'id="([^"]+)"', h))
ids_s = set(re.findall(r'id="([^"]+)"', hs))
secnum = dict((a, n) for a, _, n in re.findall(r'<section id="([^"]+)" class="level(\d)[^"]*"[^>]*>\s*<h\d[^>]*data-number="([^"]*)"', h))
capnum = {m.group(1): H.unescape(re.sub("<[^>]+>", "", m.group(2))).replace("\xa0", " ").strip().split(":")[0]
          for m in re.finditer(r'id="((?:fig|tbl|qdr)-[a-z-]+)-caption-[^"]*"[^>]*>(.{0,80})', h, re.S)}
s11 = SUP.split("# S11 ", 1)[1]
links = re.findall(r"\[([^\]]+)\]\((revisao|suplemento)\.html(?:#([\w-]+))?\)", s11)
bad = []
for rot, doc, anc in links:
    if anc and anc not in (ids_a if doc == "revisao" else ids_s):
        bad.append(f"{doc}#{anc} inexistente")
    m = re.search(r"\(seção ([\d.]+)\)", rot)
    if m and anc and secnum.get(anc) != m.group(1):
        bad.append(f"'{rot}' aponta {anc}, que é a seção {secnum.get(anc)}")
    m = re.match(r"(Figura|Tabela|Quadro) (\d+)$", rot)
    if m and anc and capnum.get(anc) != rot:
        bad.append(f"'{rot}' aponta {anc}, que é '{capnum.get(anc)}'")
    m = re.match(r"S(\d+) ", rot)
    if m and doc == "suplemento" and not anc.startswith(f"s{m.group(1)}-"):
        bad.append(f"'{rot}' aponta {anc}")
# "seções 2.3 a 2.9, de [Fontes e busca]" e "seções 3.4 a 3.7"
for faixa, a1, a2 in re.findall(r"seções ([\d.]+ a [\d.]+), de \[[^\]]+\]\(revisao\.html#([\w-]+)\) a \[[^\]]+\]\(revisao\.html#([\w-]+)\)", s11):
    x, y = faixa.split(" a ")
    if (secnum.get(a1), secnum.get(a2)) != (x, y):
        bad.append(f"faixa 'seções {faixa}' aponta {a1}={secnum.get(a1)} e {a2}={secnum.get(a2)}")
ok(not bad, f"S11: {len(links)} links, todos para âncoras existentes e com número de seção, figura e tabela certo; problemas: {bad}")
# contagens de situação em S11
for tb in re.findall(r"(\| Item \| Onde no artigo.*?)\n\n: (.*?)\{#(tbl-s11-[\w-]+)", s11, re.S):
    corpo, leg, rid = tb
    sit = Counter(re.findall(r"^\| \*\*[^|]+\| [^|]+\| (relatado|parcial|não se aplica|não relatado) \|", corpo, re.M))
    info(f"S11 {rid}: {dict(sit)}; legenda: {re.search(r'Situação: ([^.{]+)', leg).group(1) if 'Situação' in leg else '?'}")
# links do artigo ao suplemento
for anc in set(re.findall(r"suplemento\.html#([\w-]+)", A)):
    ok(anc in ids_s, f"artigo → suplemento#{anc} existe")
for anc in set(re.findall(r"\]\(#([\w-]+)\)", A)):
    ok(anc in ids_a, f"artigo → #{anc} existe")
ok("revisao.html" in LS and (R / "docs/revisao.html").exists(), "linguagem simples → revisao.html existe em docs/")

# ------------------------------------------------------------------ 16. frases que precisam dos mesmos números em todo lugar
for rot, rx in [("126.126", r"126\.126"), ("453.016", r"453\.016"), ("342 de 526", r"342 de 526|342 dos 526"), ("41 estudos", r"41 estudos"),
                ("0,40 a 1,00", r"0,40 a 1,00"), ("18 pendências", r"18 pendências")]:
    info(f"'{rot}': artigo {len(re.findall(rx, A))}, suplemento {len(re.findall(rx, SUP))}, LS {len(re.findall(rx, LS))}")

# ------------------------------------------------------------------ 17. trechos apontados nesta verificação (presença no texto atual)
achar = [
    ("artigo", A, "um efeito médio perto de zero"),
    ("linguagem simples", LS, "Depois de 2022, projetos de lei"),
    ("artigo", A, "as metas de laboratório e vinheta, em 0,48 e 0,62"),
    ("artigo", A, "não informam o tamanho"),
    ("artigo", A, "aumentou a vitória desse candidato, mesmo com aviso ao eleitor, com certeza muito baixa"),
    ("artigo", A, "a disputa apertada aparece com mais comparecimento, e a decidida, com menos"),
    ("suplemento", SUP, "Holst et al. (2025)"),
    ("suplemento", SUP, "Moher et al. 2026"),
    ("artigo", A, "citations were searched in September 2026"),
    ("artigo", A, "todos os experimentos com algumas preocupações ou risco alto de viés"),
    ("artigo", A, "every experiment at some concerns or high risk of bias"),
    ("artigo", A, "nenhum de pesquisa pré-eleitoral numa eleição"),
    ("artigo", A, "e barrou 40"),
    ("artigo", A, "O partidarismo não atenuou o efeito"),
    ("artigo", A, "informa sobre uma brecha dessa regra"),
    ("artigo", A, "no R (versão **[A confirmar pelo autor]**)"),
    ("artigo", A, "um subagente de IA por PDF propôs a elegibilidade"),
    ("esqueleto", ESQ, "o passe de estilo (etapa 7) ainda não rodou"),
    ("esqueleto", ESQ, "conferir ao fim da etapa 7"),
    ("suplemento", SUP, "| Pesquisa pré-eleitoral | Comparecimento | Inconclusivo | fraca | moderada | 7 |"),
    ("suplemento", SUP, "| Prazo (\"no longer than six months\") | Dentro"),
    ("suplemento", SUP, "com justificativa substantiva"),
]
for nome, t, trecho in achar:
    info(f"trecho em {nome}: {'presente' if trecho in t else 'AUSENTE'} «{trecho}»")

print("\n".join(out))
print(f"\n{sum(1 for l in out if l.startswith('DIV'))} divergências, {sum(1 for l in out if l.startswith('OK'))} OK, {sum(1 for l in out if l.startswith('INFO'))} INFO")
```
