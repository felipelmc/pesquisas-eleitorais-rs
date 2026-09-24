# Relatório de sessão — textos, versões e ligações de relato (2026-09-23)

Leitura prévia: `03-textos/notas_ligacao_relatos.md`, `03-textos/notas_metadados_bib.md`,
`05-decomposicao/notas_extracao_completa.md` (Freden2016b), `03-textos/ligacao_relatos.csv`,
`03-textos/relatorio_pdfs.csv`, `03-textos/inventario_textos.csv`, `05-decomposicao/fichamentos_master.csv`
e `05-decomposicao/lista_extracao_completa.csv` (esta última supriu `id_rs`/`chave` que não estão em
`fichamentos_master.csv`, que só tem `citekey`).

Nenhum arquivo existente foi alterado. PDFs obtidos ficam em `pdfs_novos/` (fora do Git).

---

## 1. Freden2016b — Artigo 2 da tese

**O Artigo 2 não é o capítulo Springer.** A nota em `05-decomposicao/notas_extracao_completa.md`
("capítulo publicado em livro Springer sobre 'Voting Experiments'") está trocada. Lendo o próprio
sumário da tese (`03-textos/pdfs/Freden2016b.pdf`, texto corrido, "Article 2: Fredén, A. 2016a.
*Coalitions, Polls and Expectations. Strategic Voting in PR Systems* (Manuscript)", p. impressa 47) —
o Springer chapter é o **Artigo 3** ("Coalitions, Coordination and Electoral Choice: A Lab
Experimental Study of Strategic Voting", p. 95). A descrição do conteúdo do Artigo 2 no próprio texto
("elaborating on the impact of pre-electoral signals and polling levels...", via Internet, survey
experiment) bate com o registro já existente no corpus: **Freden2016a** (RS1525, DOI
`10.1111/1467-9477.12087`), cujo status já é `nao_encontrado` em `relatorio_pdfs.csv`.

Confirmação bibliográfica (WebSearch + OpenAlex + Semantic Scholar): esse manuscrito foi publicado como
**Fredén, A. (2017). "Opinion Polls, Coalition Signals and Strategic Voting: Evidence from a Survey
Experiment." Scandinavian Political Studies, 40(3), 247–264.** DOI `10.1111/1467-9477.12087`.
- OpenAlex marca `publication_year: 2017` (a planilha do projeto tem 2016 — corrigir no .bib/registro).
- SSRN/IDEAS e a página do departamento (svet.lu.se) confirmam a mesma numeração de volume/fascículo.
- CEPR/RePEc não têm essa peça (é Wiley, não CEPR).

**Tentativa de recuperação legítima (repetida, todas as fontes já testadas antes voltaram a falhar hoje):**
- OpenAlex: `open_access.is_oa = false`, `any_repository_has_fulltext = false`; as duas únicas
  localizações são a própria Wiley (fechada) e o registro da Lund University Publications (metadados
  só, sem arquivo).
- Unpaywall: não consultado via API (exigiria e-mail real no parâmetro; não usei o e-mail pessoal do
  usuário para uma chamada de API de terceiros sem pedido explícito). O retrato do OpenAlex já cobre o
  mesmo dado (`is_oa=false`).
- Semantic Scholar: `openAccessPdf.status = "CLOSED"`.
- Registro LUP (`lup.lub.lu.se/search/record/72ccc6a6-...`): sem arquivo anexado, só link para a Wiley.
- DiVA Karlstad (`kau.diva-portal.org`, diva2:1263696): host ainda inacessível pela rede (mesmo bloqueio
  já documentado em `notas_metadados_bib.md`; não é paywall, é indisponibilidade técnica).
- Wiley (`onlinelibrary.wiley.com`): paywall, não contornado.
- Busca por preprint/working paper (electoraldemocracy.com, sites pessoais, SSRN, OSF): nada encontrado.

**Conclusão: Artigo 2 = Freden2016a, permanece não recuperável por fonte legítima.**
Não criei `pdfs_novos/Freden2016b_artigo2.pdf`. Recomendo: (a) corrigir o ano de Freden2016a para 2017
no `.bib`/planilha de metadados; (b) manter RS1525 como "não recuperado" (mesma categoria dos outros
casos de bloqueio técnico/paywall definitivo já listados); (c) não é necessário nenhum registro novo —
Freden2016a já é o `id_rs` correto para o Artigo 2, só precisa do PDF.

---

## 2. Klor2017a — versão de 2017 vs. manuscrito de 2006

**Metadados confirmados (OpenAlex):** Esteban F. Klor & Eyal Winter, "On public opinion polls and
voters' turnout", **Journal of Public Economic Theory** (não "Journal of Theoretical Politics" — são
periódicos diferentes; a hipótese do enunciado da tarefa estava incorreta), DOI `10.1111/jpet.12274`.
OpenAlex marca `publication_year: 2017`; a página da SSRN/CEPR indica publicação impressa em "Journal
of Public Economic Theory, vol. 20(2), pages 239–256", abril de 2018 (padrão comum da Wiley: early view
2017, fascículo impresso 2018).

**Não há versão publicada de acesso aberto.** OpenAlex: `is_oa=false`, `any_repository_has_fulltext=false`.
A página do próprio autor (scholars.huji.ac.il/eklor) tentou ser acessada diretamente
(`.../files/eklor/files/cepr-dp5669.pdf`) mas devolveu erro do servidor (bloqueio, mesmo padrão já visto
em outros repositórios institucionais desta revisão — não é paywall).

**Encontrei uma revisão do manuscrito bem mais próxima da versão final, via Wayback Machine** (fonte
legítima da cascata): `http://web.archive.org/web/20220217161220/https://scholars.huji.ac.il/sites/default/files/eklor/files/cepr-dp5669.pdf`
— um snapshot de 2022 do mesmo PDF hospedado na própria página institucional do autor (Esteban Klor,
HUJI). Esse arquivo está datado de **março de 2014** (42 páginas), não é o artigo publicado (2017/2018)
mas é uma revisão substancialmente posterior ao manuscrito CEPR DP5669 de **setembro de 2006** que já
está em `03-textos/pdfs/Klor2017a.pdf` (47 páginas).

**Comparação (mesmo experimento e dados, manuscrito revisado):**
- Mesmo título, mesmos autores, mesmo experimento (informação sobre divisão do eleitorado e efeito no
  comparecimento) e mesma evidência empírica ("Empirical evidence on gubernatorial elections in the
  U.S. between 1990 and 2005", idêntico nas duas versões).
- Estrutura de seções quase idêntica: "3. Experimental Design", "4. Experimental Results", "5. Evidence
  from Gubernatorial Elections in the US", mesmas Figuras 1, 3 e 4 com a mesma legenda, nas duas versões.
- Diferenças: a versão 2014 remove a seção 2 "Theoretical Framework" como capítulo numerado separado,
  reorganiza a seção 6 ("A Behavioral Model") e muda ligeiramente a classificação JEL (2006: C72, C92,
  D72, H41 → 2014: C92, D72) e a redação do resumo — sinal de revisão editorial, não de outro estudo.
- Confirma-se: **mesmo estudo, mesmos dados/experimento**, mas o PDF de 2014 é uma revisão mais próxima
  da versão publicada do que o manuscrito de 2006 já presente no corpus.

**Ação:** salvei o PDF de 2014 (recuperado via Wayback Machine) em
`pdfs_novos/Klor2017a_2017.pdf` — atenção: **não é literalmente a versão publicada de 2017/2018** (essa
continua paywalled na Wiley, sem repositório), é a melhor revisão de acesso aberto disponível
legitimamente. Recomendo ao coordenador decidir se vale re-fichar a partir desta versão (o conteúdo
substantivo do experimento parece inalterado, mas não conferi célula a célula os números/tabelas).

---

## 3. PDFs recuperados mas não ligados — classificação

Todos os oito estão em `03-textos/pdfs_descartados/` (não em `03-textos/pdfs/`, apesar do `status=ok`
em `relatorio_pdfs.csv`). Abri as duas primeiras páginas de cada um (pdftotext) e comparei por md5 com
os PDFs já usados na extração.

| chave | id_rs | Classificação | Evidência |
|---|---|---|---|
| **Boukouras2023a** | RS2149 | **(a)** mesmo arquivo do estudo incluído **Boukouras2020a** (RS2247) | md5 idêntico (`8a636c68f1f2b5a265d6b1b7470602ed`) — é literalmente o mesmo PDF do WP nº 1902 da U. Southampton, "Can Biased Polls Distort Electoral Results? Evidence from the Lab and the Field", já usado para RS2247. **Já ligado** em `ligacao_relatos.csv` (grupo `RS2149\|RS2247`) — nenhuma ação necessária. |
| **Grillo2024d** | RS1805 | **(a)** mesmo arquivo do estudo incluído **Grillo2024c** (RS1596) | md5 idêntico (`774abaf7...`) ao WP AMSE 2022-Nr07 já usado para RS1596. DOI `10.3917/reco.752.0353` é apenas outra numeração DOI do mesmo artigo na Revue économique (já documentado em `notas_metadados_bib.md`). **Não ligado** — proposto em `pares_relatos_propostos.csv`. |
| **Grillo2024e** | RS1914 | **(a)** idem, mesmo arquivo de **Grillo2024c** (RS1596) | md5 idêntico; terceira numeração DOI (`10.3917/e.reco.752.0353`) do mesmo artigo. **Não ligado** — proposto. |
| **Chernov2026a** | RS1782 | Nem (a) nem (b): é a mesma publicação de **Chernov2025b** (RS1780), mas esse estudo **já foi avaliado e excluído** em texto completo (critério C2 — "a key data input into these models are polls", isto é, o artigo usa pesquisas como insumo para prever *prediction markets*, não estuda o efeito da exposição a pesquisas publicadas sobre o voto). md5 idêntico (`af35f7d8...`). **Já ligado** em `ligacao_relatos.csv` (grupo `RS1780\|RS1782`) — nenhuma ação necessária; não é candidato à inclusão. |
| **Yang2023e** | RS4000 | **(a)** mesmo arquivo do estudo incluído **Yang2023d** (RS3978) | md5 idêntico (`728ed329...`). **Já ligado** em `ligacao_relatos.csv` (grupo `RS3978\|RS4000`) — nenhuma ação necessária. |
| **Hodgson2025a** | RS2126 | Nem (a) nem (b): mesmo artigo de **Hodgson2012a** (RS1610), que **já foi excluído** em texto completo (C2 — "the effect of actual votes rather than polls or projections"; o desenho usa resultados eleitorais reais em eleições britânicas escalonadas 1885–1910, não pesquisas de opinião). md5 idêntico (`41511b24...`) ao post-print já em `03-textos/pdfs/Hodgson2012a.pdf`. **Não ligado** — proposto (mesma lógica do caso Granziersd, tarefa 5). |
| **Granziersd** | RS3831 | Ver tarefa 5 abaixo | — |
| **Herrmann2024a** | RS4032 | **(b)** possivelmente relevante, mas retrievido incompleto | Ver detalhe abaixo. |

### Herrmann2024a — detalhe

O PDF em `pdfs_descartados/Herrmann2024a_apenas_folha_de_rosto.pdf` é só a folha de rosto + as
"Propositions" da tese de doutorado **Oliver Herrmann, "Is your vote vital? Five essays on voter
behavior"** (U. Groningen, 2024, DOI `10.33612/diss.1049901276`). A proposição 3 diz textualmente:
"**Bandwagon effects**, where individuals are more likely to vote if they perceive their group as the
likely winner, **are prominent in election experiments** (Chapter 3)." — isso é diretamente relevante
ao protocolo (expectativa de vitória → voto/comparecimento).

- Tentei baixar a tese completa em `research.rug.nl/files/1049901278/Complete_thesis.pdf` (link legítimo,
  encontrado no próprio registro RUG Pure) — **bloqueada por desafio anti-robô Cloudflare** ("Just a
  moment..."), sem snapshot no Wayback Machine. Não tentei contornar (regra do projeto). Mesma categoria
  já documentada em `notas_metadados_bib.md` ("Textos de acesso aberto que a rede bloqueou").
- **Achado adicional (fora do escopo literal da tarefa, mas relevante):** existe um registro **separado**
  no corpus, `dados/registros_unicos.csv`, **RS4020, chave `Herrmann2024`** (sem "a"), DOI
  `10.2139/ssrn.4834498`, "**Reference Dependence in Voting Behavior: Experimental Evidence**" (Herrmann,
  Jong-A-Pin & Schoonbeek, SSRN 2024) — quase certamente o Capítulo 3 da mesma tese, publicado como
  preprint autônomo. RS4020 está com flag `sem_resumo` e parado em **TA "incerto"**
  (`02-triagem/triagem_ta_final.csv`, linha 2208), nunca avaliado em texto completo.
  Recuperei o resumo (SSRN bloqueia scraping direto por Cloudflare; usei o snapshot do Wayback Machine de
  2025-04-29, fonte legítima): *"...we show that there are large and persistent bandwagon effects in our
  model elections, a finding that is difficult to reconcile with standard models of voter turnout."* —
  é um jogo eleitoral experimental de laboratório com rodadas repetidas, testando efeito bandwagon sobre
  o comparecimento. **Isto parece um candidato de alta relevância, hoje parado sem motivo aparente
  (falta só o resumo, que agora está recuperado).**
  - Não tentei o download do PDF da SSRN (mesmo bloqueio Cloudflare que a página RUG; a página está
    marcada `is_oa=true / oa_status=green` no OpenAlex, ou seja, é gratuita para humanos, só bloqueada
    para automação).
  - Recomendo ao coordenador: (1) resolver a triagem TA de RS4020 com o resumo recuperado acima; (2) se
    incluído, buscar o PDF via download manual (navegador) já que a rede automatizada está bloqueada;
    (3) esclarecer a relação RS4020×RS4032 antes de fichar (a tese tem 5 ensaios distintos — não devem
    ser tratados como "o mesmo estudo" só por virem do mesmo documento; ver caso Stolwijk abaixo para o
    critério usado).
  - **Nota de processo:** percebi que há um processo concorrente rodando nesta mesma sessão de trabalho
    (`02-triagem/sem_resumo_revisao/`, arquivos com timestamp de poucos minutos atrás, script
    `recuperar_resumos.py` ainda em execução no momento em que este relatório foi escrito) tentando
    recuperar resumos para 336 registros com flag `sem_resumo`, entre eles possivelmente RS4020. Não
    mexi nessa pasta (fora do escopo desta sessão) — só registro para o coordenador não duplicar o
    trabalho e conferir se esse processo já resolveu RS4020 de forma equivalente.
- Não criei entrada em `pares_relatos_propostos.csv` para RS4020×RS4032: a evidência aponta fortemente
  para "capítulo da mesma tese", mas não tenho leitura completa dos dois textos para confirmar se são
  extraíveis como o mesmo efeito/dado (a tese cobre 5 ensaios diferentes). Fica como recomendação, não
  como par fechado.

---

## 4. Pares duvidosos — mesmo estudo ou estudos distintos?

### Cornejo2023a vs. Castro Cornejo 2019 (POQ) / 2019a (RLOP) / 2020~2021 (IJPOR) / 2021 (LARR)

**Estudos distintos.** Busquei os quatro textos (via WebSearch + página pessoal do autor,
rodrigocastrocornejo.com/research.html) e confirmei que **já estão no corpus**, cada um com seu próprio
`id_rs`, e **já foram excluídos em título/resumo** por critério C2 (não estudam exposição a pesquisas
eleitorais sobre o voto):

| chave | id_rs | Tema | Status TA |
|---|---|---|---|
| Cornejo2019 | RS3654 | Public Opinion Quarterly — efeito da redação de pergunta na medição de partidarismo | excluído (C2) |
| Cornejo2019a | RS3698 | RLOP (espanhol) — interesse na campanha e consistência da intenção de voto | excluído (C2) |
| Cornejo2020 | RS3790 | IJPOR (2021, v.33 n.4) — como campanhas "esclarecem" independentes | excluído (C2) |
| Cornejo2021 | RS3805 | LARR — estabilidade de curto/longo prazo do partidarismo | excluído (C2) |

Nenhum desses tem como variável de tratamento a exposição a pesquisas eleitorais publicadas — são sobre
metodologia de mensuração de partidarismo e efeitos gerais de campanha. **Cornejo2023a (RS1625, incluído)
é o único desse conjunto de autor que isola o efeito de "saber o resultado de uma pesquisa" no
experimento de survey de 2015 (painel Michoacán/Nuevo León).** Não há relato a ligar.

**Achado incidental (não é um par a propor, é tranquilizador):** encontrei que `dados/registros_unicos.csv`
tem pares de `id_rs` com o mesmíssimo DOI/ID OpenAlex para Cornejo2023≡Cornejo2023a (RS0219≡RS1625) e
Cornejo2024≡Cornejo2024a (RS0498≡RS2068). Investiguei se isso é um problema de deduplicação ativo: **não
é.** Todos os registros com `flags=busca_inativa` (955 no total, incluindo esses dois) foram
**uniformemente excluídos da triagem TA** — nenhum dos 955 aparece em `02-triagem/triagem_ta_final.csv`.
É um lote de busca substituída/inativa, mantido só para proveniência, e nunca entrou no funil ativo.
Não há risco de dupla contagem; não propus pares para esse lote (seriam ~950 linhas irrelevantes).

### Timotei2013a vs. Vieraşu & Brătucu (2011) / Vierasu (2012)

**O autor é "Vieraşu Timotei"** (nome próprio Timotei, sobrenome Vieraşu — a chave do projeto inverteu a
ordem, o que é comum em nomes romenos citados por sistemas anglófonos).

- **2011: encontrado e lido.** "How to Manipulate Polls" (T. Vieraşu, A. Talpău, A. Herţanu, M.
  Bălăşescu), *Bulletin of the Transilvania University of Braşov*, Series V, Vol. 4(53) No. 2, 2011,
  pp. 79–86 (acesso aberto, `webbut.unitbv.ro`). Título diferente do citado na nota do fichador
  ("Polls and manipulation", ICBE) — pode ser um terceiro texto do mesmo autor, ou uma referência
  imprecisa; o que encontrei e li é seguramente do mesmo grupo de pesquisa. **Contém só o experimento
  "Yes Sir"** (manipulação de redação/ordem de perguntas, 3 formulários A/B/C) — **não tem o experimento
  "Fake Poll"** (candidato A/B, exposição a pesquisa fictícia) que é a única parte de Timotei2013a
  relevante para este protocolo. **Não é o mesmo estudo/dado do efeito extraído.**
- **2012 ("Influencing public opinion using polls", MMK 2012, vol. III, pp. 643-652):** não localizado
  por nenhuma fonte de busca legítima (não indexado em bases abertas que consultei; "MMK" é
  provavelmente uma conferência de baixa indexação). **Não verificável.** Como Timotei2013a declara que
  os dados do "Fake Poll" foram coletados em fevereiro de 2013 (posterior à conferência MMK 2012), *se*
  o texto de 2012 já contiver um experimento de exposição a pesquisa, seria necessariamente uma coleta
  de dados anterior/diferente — mas não posso confirmar isso sem acesso ao texto.
- Nenhum dos dois (2011, 2012) está no corpus da revisão (`dados/registros_unicos.csv` não tem
  "Vierasu"/"Bratucu" além de Timotei2013a) — **não há par a ligar em `ligacao_relatos.csv`** de qualquer
  forma, independente da conclusão acima.

### Unkelbach2022a vs. John2021a

**Confirmado: mesmo estudo** (pré-registro → artigo). Verifiquei via API pública do OSF:
- `osf.io/ms3ek` (o DOI de John2021a) é o registro de pré-registro, título idêntico a John2021a:
  "Jumping on the Bandwagon: Investigation of the role of voters' social class for poll effects in the
  context of the 2021 German federal election", criado em 2021-11-14, descrição: combina dados do
  "2021 GLES RCS (ZA7703)" com resultados de pesquisas publicadas seguindo o procedimento de Faas et al.
  (2008) — bate exatamente com o desenho de Unkelbach2022a.
- `osf.io/g6r7v` (citado no texto de Unkelbach2022a, pp. 9 e 17, como "the preregistration... available
  at osf.io/g6r7v") é um nó de **projeto** OSF (não um registro), mesmo título exato, criado logo depois
  (2021-12-01) — é o componente de materiais/suplemento do mesmo pré-registro.
- John2021a (RS1887) está parado em **TA "incerto"** desde sempre (`triagem_ta_final.csv`, linha 624) e,
  por ser só um pré-registro sem resultados, não é um manuscrito extraível — já apontado assim em
  `relatorio_pdfs.csv` (`status=nao_e_manuscrito`).
- **Não ligado em `ligacao_relatos.csv`** — proposto em `pares_relatos_propostos.csv`.

### Reveco2026 vs. Dann et al. (2026), "Missing Voters?"

**Estudos distintos**, apesar de tratarem do mesmo evento (as eleições peruanas de 2026 com atraso na
instalação de mesas eleitorais). Verifiquei diretamente as duas publicações:
- **Dann, Díaz-Cayeros, Magaloni & Peña (Stanford Democracy Action Lab), "Missing Voters? An Analysis of
  the Effects on Turnout of the Election Administration Delays in the 2026 Peru First Round Presidential
  Elections"** (18/05/2026) — estuda o efeito do **atraso administrativo** (mesas abrindo horas depois do
  previsto) sobre o **comparecimento**. Não estuda exposição a pesquisas/estimativas — não atenderia
  C2/C3 do protocolo (a intervenção não é uma pesquisa publicada, é a demora logística em si).
- **Reveco2026 (RS2747, incluído)** — Alejandro Plaza Reveco, estuda a exposição de eleitores que
  votaram depois de já saberem estimativas (Ipsos/Datum) publicadas por causa do mesmo atraso — isso sim
  é a intervenção do protocolo.
- Não há sobreposição de autoria nem de desenho — **não é um par de relatos, é só o mesmo evento
  estudado por ângulos diferentes.** Não propus ligação.
- **Achado incidental relevante:** localizei uma **terceira equipe, totalmente independente**, estudando
  exatamente o mesmo desenho de Reveco2026 (o mesmo "quase-experimento" dos ~55.000 eleitores que votaram
  no dia seguinte após verem as estimativas Ipsos/Datum): **Gallardo, Velarde & Gutarra, "Information and
  voting: Evidence from Peru's 2026 presidential election"** (arXiv:2606.01687). Autoria diferente de
  Reveco2026, sem citação cruzada entre os dois — parece ser uma "descoberta paralela" de dois grupos
  sobre o mesmo evento, não um relato do mesmo estudo. **Não está no corpus.** Sinalizo como candidato
  a busca atualizada/snowball (mesmo desenho, motivador de posição de quantitativo de teste
  robusto/sensibilidade), mas não é tarefa desta sessão decidir inclusão.

### Stolwijk2017a (tese) vs. Stolwijk2016a vs. Stolwijk2019b (terceiro relato)

**Confirmei que a ligação atual está correta e completa — não acrescentar Stolwijk2019b ao grupo.**
Já existe o grupo `RS1548|RS1637` em `ligacao_relatos.csv` (Stolwijk2016a = Capítulo 3 da tese
Stolwijk2017a, painel Bundestag 2013). Li o corpo da tese (`03-textos/pdfs/Stolwijk2017a.pdf`) para
verificar a hipótese de que faltaria ligar um terceiro relato:
- A própria introdução da tese diz: **"study 1 investigate[s] the German 2013 Federal election campaign
  to the Bundestag, and study 2 examines the Dutch 2014 elections to the European Parliament (EP)"**
  (p. impressa, linha 1117-1118) — são **dois estudos empíricos diferentes**, com amostras, países e
  eleições distintos, não o mesmo dado contado duas vezes.
- O Capítulo 2 (linhas ~2695-3660) é explicitamente sobre "**a representative four wave panel survey
  among Dutch voters** in the 2014 European Parliament (EP) elections" — isso é o mesmo desenho/dado de
  **Stolwijk2019b** (RS1611, já incluído e extraído de forma independente, com seu próprio `id_estudo`
  ES1611 em `lista_extracao_completa.csv`, extraído do artigo publicado, não da tese).
- Como Stolwijk2019b já é extraído a partir do artigo autônomo (não da tese) e representa uma amostra/
  desenho **diferente** do de Stolwijk2016a (Bundestag 2013), **fundir os três relatos num só grupo seria
  um erro de método** — descartaria uma estimativa de efeito independente da síntese (reduziria k
  indevidamente). A leitura de "ligar os três relatos por estudo" na nota original provavelmente queria
  dizer "documentar a proveniência comum" (mesma tese), não "tratar como o mesmo id_estudo". **Nenhuma
  ação de ligação necessária; manter RS1611 independente.**

---

## 5. Granziersd — o que é e o que fazer

**Granziersd é um download duplicado, byte a byte idêntico, do mesmo NBER Working Paper 26599**
("Coordination and Bandwagon Effects: How Past Rankings Shape the Behavior of Voters and Candidates",
Granzier, Pons & Tricaud) já baixado para a chave **Granzier2019 (RS3728)**.

- md5 de `pdfs_descartados/Granziersd_igual_a_Granzier2019.pdf` = `ae9872ec8c661ab96cd276b5b5c46abd`,
  idêntico ao de `03-textos/pdfs/Granzier2019.pdf`.
- O registro `Granziersd` no `relatorio_pdfs.csv` não tem ano nem DOI (metadado incompleto vindo de uma
  rodada de busca por título) — é o mesmo motivo já registrado em `notas_metadados_bib.md`: a cascata
  redescobriu o mesmo PDF numa terceira rodada porque o registro seguia `nao_encontrado`.
- **Granzier2019/RS3728 já foi avaliado e excluído em texto completo** por `c2_intervencao_estudada`
  ("a dummy equal to 1 if the candidate had a higher rank"; "this paper shows that candidate rankings in
  past contests..." — o desenho usa **posições em disputas passadas** para prever comportamento
  estratégico, não pesquisas de opinião publicadas).
- **Recomendação (o que a própria nota do coordenador já cogitava):** dar a Granziersd/RS3831 a **mesma
  decisão de texto completo de Granzier2019 por override humano** (excluir, `c2_intervencao_estudada`),
  em vez de triá-lo de novo como candidato novo — é o mesmo documento. Proposto em
  `pares_relatos_propostos.csv` com `relato_primario=RS3728`.
- Caso irmão com a mesma lógica: **Hodgson2025a/RS2126** (ver tarefa 3) — mesmo padrão, também proposto.

---

## Resumo dos arquivos desta sessão

- `pdfs_novos/Klor2017a_2017.pdf` — revisão de março/2014 do manuscrito Klor & Winter (não é o artigo
  publicado; é a melhor cópia de acesso aberto legítima encontrada, via Wayback Machine).
- `pares_relatos_propostos.csv` — 5 pares "mesmo estudo, ainda não ligados": Grillo2024d→Grillo2024c,
  Grillo2024e→Grillo2024c, Granziersd→Granzier2019, Hodgson2025a→Hodgson2012a, John2021a→Unkelbach2022a.
- Não criado: `pdfs_novos/Freden2016b_artigo2.pdf` (Artigo 2 = Freden2016a, DOI `10.1111/1467-9477.12087`,
  permanece sem cópia de acesso aberto legítima).

## Pendências para o coordenador (além dos itens já cobertos)

1. Corrigir o ano de Freden2016a para 2017 (2016→2017) na próxima passada de metadados/.bib.
2. Resolver a triagem TA de **RS4020 (Herrmann2024, SSRN)** com o resumo recuperado nesta sessão
   (bandwagon effect sobre comparecimento em jogo eleitoral experimental) — candidato provavelmente
   elegível, hoje parado só por falta de resumo.
3. Conferir se o processo concorrente em `02-triagem/sem_resumo_revisao/` já cobre RS4020 antes de
   duplicar trabalho.
4. Avaliar manualmente (fora de rede automatizada) o PDF completo de Herrmann2024a
   (`research.rug.nl/files/1049901278/Complete_thesis.pdf`, bloqueado por Cloudflare para automação, mas
   provavelmente acessível por navegador humano) e do SSRN 4834498, se RS4020 for incluído.
5. Aplicar `pares_relatos_propostos.csv` em `ligacao_relatos.csv` pelos comandos da skill (não editei
   esse arquivo à mão).
