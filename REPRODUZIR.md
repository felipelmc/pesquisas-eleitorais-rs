# Reproduzir e manter o projeto

Guia técnico do repositório: estrutura, PDFs locais, a cadeia que refaz efeitos, síntese e produtos, e o histórico das sessões de trabalho. A porta de entrada é o `README.md`.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `00-protocolo/` | pergunta, teoria do programa e DAG, protocolo congelado no G2, codebooks, âncoras, `emendas.md` (E001, E002 e Emendas 1 a 8), `correcao_atribuicao.csv` |
| `01-busca/` | strings versionadas, `log_buscas.csv`, recall das âncoras, pré-PRESS por IA, pares de duplicata |
| `02-triagem/` | lotes e respostas dos triadores A e B, árbitro, fila humana, amostras de validação e elusão (não codificadas), `sem_resumo_revisao/` (Emenda 6b) |
| `03-textos/` | lista para baixar, relatório de PDFs, fichas de elegibilidade, `elegibilidade_tc_final.csv`, ligação de relatos, `sessao_2026-09-23/`. Os PDFs (`pdfs/`, `pdfs_descartados/`) **não são versionados** (ver abaixo) |
| `04-qualidade/` | RoB 2, ROBINS-I V2 e EPOC: fichas A e B, propostas do árbitro (`arbitragem/`), consenso, `rob_geral.csv`, `notas_rob.md` |
| `05-decomposicao/` | fichamentos (`fichamentos_master.csv`), efeitos por estudo (`efeitos/<chave>.csv`), verificação, validação da extração, `notas_extracao_completa.md`, `correcoes_revisao_g8.csv`, `correcoes_sessao_2026-09-23.csv` |
| `06-analise/` | efeitos calculados, entradas e saídas da SWiM (principal e sensibilidades, inclusive ICC 0,20), meta exploratória, `certeza.csv`, `certeza_agrupamento_amplo.csv`, `revisao_metodologica_g8.md`. `_superado_pre_revisao_g8/` guarda a síntese anterior à Emenda 5, só para histórico |
| `07-relatorio/` | relatório técnico de 24/09 (`relatorio.qmd`, superado pelo artigo e não publicado), PRISMA (contagens, SVG, PNG), checklists PRISMA e SWiM, `references.bib`, declaração de uso de IA, prompts do redator |
| `08-revisao-humana/` | declarações dos autores (30/09/2026, inclusive a de coautoria), o que foi fechado e o que falta, pacotes de cada pendência (abertas e fechadas), re-extração cega e arbitragens dos efeitos |
| `09-documento-final/` | artigo final. O texto fica em `_esqueleto_revisao_final.qmd`; `montar_revisao_final.py` insere figuras (`@@FIGURA@@`) e tabelas (`@@TABELA@@`) geradas dos arquivos e grava `revisao_final.qmd`. Os apêndices A a G saem de `_esqueleto_suplemento.qmd` por `montar_suplemento.py` (arquivo `suplemento.qmd`, publicado como `apendices.html` e juntado ao PDF do artigo), e o resumo em linguagem simples está em `linguagem_simples.qmd`. `revista/` guarda o template Typst, o filtro `inline.lua`, as fontes OFL, o CSL da APSA, `rotulos.yml` (contrato de rótulos), `celulas.json` e `numeros_v2.json` (únicas portas de número derivado), `referencias.json` e as figuras (`revista/figuras/`, dados em Python e desenho em R). As travas são `conferir_reestruturacao.py` (números, enunciados, callouts, rótulos, proibições) e `conferir_numeros.py` (passes de estilo). Também estão aqui: `spec_final.md` (especificação da versão de entrega, com a sentinela; `spec_v2.md` é a de 24/09), `insumos/` (livro, exemplares, Garritty, revisões anteriores, contexto brasileiro), `prompts_final/` e `_blocos/` (redação da versão de entrega), `verificacao_entrega.md` (verificação independente da versão de entrega), os históricos `prompts_v2/`, `verificacao_v2.md` e `verificacao_final.md`, `auditoria_final*.md`, `resposta_pareceres.md`, `_leituras/`, `_avaliacao/`, `_qa/`, `declaracao_ia_v2.md` e a vitrine (`vitrine/`: exportação, fontes do JS e CSS, QA com Playwright) |
| `docs/` | versão publicada no GitHub Pages (lista branca): `index.html` (vitrine), `revisao.pdf` (artigo e apêndices num PDF só), `revisao.html`, `apendices.html`, `linguagem-simples.html` e `pacote-replicacao.zip`. Tudo é gerado por `ferramentas/publicar.sh` |
| `dados/` | registros e decisões. Só a skill escreve aqui |
| `rs_estado.json`, `rs_log.jsonl` | estado e registro de eventos da skill (append-only). Nunca editar à mão |
| `ferramentas/` | `publicar.sh` (gera e confere `docs/`), `refazer_produtos.sh` (sentinela, tabelas, caixa e publicação), `juntar_pdf.py` (artigo + apêndices), `montar_pacote.py` (pacote de replicação sanitizado; modelo do `LEIA.md` em `pacote/`), `propagar_verificado_humano.py` (leva a marca `verificado_humano` do arquivo combinado aos CSVs por estudo; dry run por padrão, `--aplicar` grava), `barra_publicacao.py`, e conferências auxiliares: `checar_arbitros.py <raiz> [max_palavras] [subpasta]` confere vocabulário e trecho literal na página das propostas do árbitro de RoB; `achar_trecho.py <verificacao_citacoes.csv> <pasta_pdfs>` sugere o trecho literal mais próximo para citações reprovadas no gate |

## Cópia de trabalho e PDFs

- **Cópia de trabalho:** `~/Desktop/pesquisas-eleitorais-rs`, clone deste repositório. A revisão foi conduzida até 23/09/2026 em `~/revisoes/pesquisas-eleitorais`. Arquivos antigos (fichas, `pdf_path` de `05-decomposicao/fichamentos_master.csv`, prompts) guardam esse caminho como registro de proveniência. Não trabalhe em duas cópias ao mesmo tempo: `rs_estado.json` e `rs_log.jsonl` não se juntam bem.
- **PDFs:** ficam **só no disco local** da cópia de trabalho, fora do Git (`.gitignore`), porque são obras de terceiros.
  - `03-textos/pdfs/` tem 190 PDFs, os textos completos obtidos, nomeados `<chave>.pdf`, e uma página HTML.
  - `03-textos/pdfs_descartados/` tem 20: cópias de outra versão do mesmo trabalho, só folha de rosto ou documento errado. Os motivos estão em `03-textos/conferencia_pdfs.csv`.

  Sem eles não rodam `rs analise verificar-efeitos`, uma nova conferência dos efeitos na página do PDF, as arbitragens nem os scripts de conferência de `ferramentas/`.
- **Clone novo sem PDFs:** copie a pasta `03-textos/pdfs/` de uma cópia existente, ou baixe de novo com a skill `baixar-pdfs-academicos` a partir de `03-textos/para_baixar.csv`. O arquivo `03-textos/relatorio_pdfs.csv` diz de onde veio cada um. Os que só vieram de páginas de autor ou de repositórios podem não ser encontrados de novo; confira com `03-textos/verificacao_conteudo.csv`. Nunca use Sci-Hub ou fontes não autorizadas.

## Refazer os produtos depois de fechar pendências

Toda mudança em efeitos, RoB ou GRADE precisa passar pela cadeia inteira. A partir da raiz do projeto, com `rs() { python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py "$@"; }`:

```bash
# 1. efeitos (depois de corrigir 05-decomposicao/efeitos/<chave>.csv)
rs --dir . analise preparar-efeitos --master 05-decomposicao/fichamentos_master.csv --codebook 00-protocolo/codebook_v0_efetividade.csv
rs --dir . analise verificar-efeitos
python3 05-decomposicao/juntar_rob.py                      # junta rob_geral por chave + construto
rs --dir . analise efeitos --in 05-decomposicao/efeitos_para_sintese.csv

# 2. entradas da SWiM (células, efeitos fora da contagem, nulos por ±δ) e meta exploratória
python3 06-analise/montar_entradas_swim.py
python3 06-analise/montar_meta_exploratoria.py
#    sensibilidade ICC 0,20 (Emenda 4c)
python3 06-analise/montar_sens_icc020.py
rs --dir . analise efeitos --in 06-analise/sens_icc020_entrada.csv --out 06-analise/sens_icc020_efeitos.csv
python3 06-analise/montar_entradas_swim.py 06-analise/sens_icc020_efeitos.csv _icc020
python3 06-analise/montar_meta_exploratoria.py _icc020

# 3. SWiM principal e sensibilidades
G=familia_intervencao,construto_outcome,comparador_tipo,celula_alvo; A=construto_outcome,celula_alvo
rs --dir . analise swim --in 06-analise/swim_entrada_principal.csv --out-dir 06-analise/swim_principal --grupo $G --separar-desenho sim --excluir-rob critico
rs --dir . analise swim --in 06-analise/swim_entrada_principal.csv --out-dir 06-analise/swim_sens_com_critico --grupo $G --separar-desenho sim
rs --dir . analise swim --in 06-analise/swim_entrada_principal.csv --out-dir 06-analise/swim_sens_agrupamento_amplo --grupo $A --separar-desenho sim --excluir-rob critico
for s in com_excluidos so_contexto_real sem_pre2010 sem_araujo; do
  rs --dir . analise swim --in 06-analise/swim_entrada_$s.csv --out-dir 06-analise/swim_sens_${s}_amplo --grupo $A --separar-desenho sim --excluir-rob critico
done
rs --dir . analise swim --in 06-analise/swim_entrada_principal_icc020.csv --out-dir 06-analise/swim_sens_icc020 --grupo $G --separar-desenho sim --excluir-rob critico
for suf in "" _icc020; do
  rs --dir . analise meta --in 06-analise/meta_entrada_mesmo_candidato$suf.csv --out-dir 06-analise/meta_mesmo_candidato$suf \
    --grupo familia_intervencao,construto_outcome,comparador_tipo --dependencia che --delta 0.044 --separar-desenho sim --excluir-rob critico
done
for suf in "" _icc020; do
  rs --dir . analise meta --in 06-analise/meta_entrada_exploratoria$suf.csv --out-dir 06-analise/meta_exploratoria$suf \
    --grupo familia_intervencao,construto_outcome,comparador_tipo --dependencia che \
    --delta "$(cat 06-analise/_delta_celula.txt)" --separar-desenho sim --excluir-rob critico
done

# 4. GRADE (06-analise/certeza.csv e certeza_agrupamento_amplo.csv; rascunho por subagente com 06-analise/prompt_grade_v2.md) e relato
rs --dir . prisma            # regrava checklist_prisma.csv: preencha local_no_relato de novo depois
rs --dir . incluidos
rs --dir . pendencia listar > 07-relatorio/_pendencias_abertas.json
rs --dir . declaracao-ia     # sempre por último, antes do render
bash ferramentas/refazer_produtos.sh   # sentinela (spec_final.md), tabelas de insumo, caixa OQF e publicação (ferramentas/publicar.sh)
```

Cuidados:

- `rs bib` regrava `07-relatorio/references.bib` e apaga as três referências acrescentadas à mão (Hardmeier2008, MoyRinke2012, Barnfield2019). Se rodar, acrescente-as de novo.
- Os números do artigo são copiados dos arquivos por subagentes redatores. Se a síntese mudar, o texto precisa ser reescrito, não só renderizado (o relatório técnico de 24/09, `07-relatorio/relatorio.qmd`, está superado e não é mais mantido). O `refazer_produtos.sh` para quando a sentinela de `09-documento-final/spec_final.md` (seção 10) muda, e a seção diz quais partes reescrever. No artigo, isso significa editar o esqueleto com os prompts de `09-documento-final/prompts_final/`, remontar, passar `conferir_reestruturacao.py`, rodar a verificação e passar `conferir_numeros.py` em todo passe de estilo.
- `rs caixa` é opcional neste tipo de revisão. Rodá-lo abre a pendência `certeza_caixa`, que repete a validação do GRADE; rodá-lo de novo mantém o ID enquanto o número de células pendentes não muda.
- Os 40 arquivos `05-decomposicao/efeitos/<chave>.csv` trazem `verificado_humano = sim` desde 30/09/2026 (`ferramentas/propagar_verificado_humano.py`). Ao corrigir uma linha, apague a marca dela: o `preparar-efeitos` só derruba a marca que herda do arquivo combinado, e não a que já vem no arquivo por estudo.
- Dedup depois da triagem (como a da Emenda 8): rode `filtrar`, `triagem consolidar --regra liberal`, `textos elegibilidade consolidar` (só se algum absorvido tiver decisão de texto completo), `prisma` e `incluidos`, nesta ordem, e confira que `incluidos.csv` não mudou.
- Quando a última pendência fechar, o `rs status` deixa de marcar rascunho. Aí tire a linha "RASCUNHO NÃO VALIDADO" da abertura da declaração de uso de IA do artigo (Informações adicionais).

## Histórico das sessões

A versão de entrega de 30/09/2026 (tag `v3-final-2026-09-30`) registrou a conferência do autor (Emenda 7), reescreveu o artigo como PDF único com apêndices e aplicou a deduplicação decidida por ele (Emenda 8), sem mudar a análise; só as contagens do fluxo mudaram. A versão de 24/09/2026 está na tag `v2-rascunho-2026-09-24`; a anterior, no formato *O que funciona?*, na tag `v1-oqf-2026-09-24`. As seções abaixo descrevem o que foi feito até 24/09/2026, com os números daquela data.

### Revisão geral de 30/09/2026, noite (Emenda 8)

Uma revisão geral do projeto, por três auditorias de IA só de leitura (documentação, artigo e produtos, dados), achou os dados consistentes e os problemas em textos, datas e numa ferramenta. O que o autor decidiu e o que foi feito:

1. **Skill `revisao-sistematica` v1.4** (repositório espelho `~/Desktop/Systematic-Review`, branch `fix/dedup-ids-absorvidos`, com testes de regressão):
   - a consolidação da triagem e da elegibilidade leva a decisão de um registro absorvido pelo dedup ao que o absorveu, e o `prisma` acusa ids absorvidos com invariantes que dizem o que rodar;
   - a caixa de ferramentas agrega as linhas de certeza mais finas que a célula dela (`subcelulas-1`), sem esconder a de maior certeza, e a P042 manteve o ID;
   - a declaração de uso de IA anota, na seção 6, o fechamento das pendências citadas nas descrições e lista, na seção 7, os juízos de IA sem validação humana, em vez de um texto fixo.
2. **P019 aplicada (Emenda 8):** as 145 decisões do autor e os 9 pares de versão que ele ligou; a regra "a decisão mais inclusiva vence" nos 44 registros absorvidos já triados. Mudaram só contagens do fluxo (522 buscados, 338 não recuperados); incluídos, efeitos e síntese ficaram iguais.
3. **Marca `verificado_humano`** propagada aos 40 CSVs por estudo (`ferramentas/propagar_verificado_humano.py`); os arquivos combinados ficaram idênticos.
4. **Textos:** versão e período de uso de IA em 30/09/2026; o δ de 0,044 e 0,046 descrito como desvio da Emenda 5; o que o autor conferiu descrito como no artigo (partes da busca, da seleção e da extração) na vitrine, no README e no pacote; faixa de topo da vitrine retirada a pedido do autor; README, REPRODUZIR, LEIAs, `CITATION.cff` (licenças CC BY 4.0 e MIT) e tabela de emendas corrigidos.
5. **Tag** `v3-final-2026-09-30`, no lugar da `v3-final-2026-10-01`.

Os autores estão revendo o risco de viés e o GRADE (P033, P035, P036 e P042).

Na mesma noite, Lucas Berti (IESP-UERJ) passou a coautor, com contribuição igual à de Felipe Lamarca, e as conferências e decisões registradas foram declaradas dos dois (`08-revisao-humana/declaracao_autores_2026-09-30_coautoria.md`). Os produtos passaram de "o autor" a "os autores".

Por fim, os autores abriram o repositório. O histórico completo foi copiado para o privado `felipelmc/pesquisas-eleitorais-rs-completo`. Depois, os arquivos com resumos de terceiros e os pareceres de triagem saíram de todos os commits (`git filter-repo`; lista no bloco "resumos de terceiros" do `.gitignore`), dois e-mails de terceiros viraram "[e-mail removido]", e o autor dos commits passou ao endereço noreply do GitHub. Os hashes mudaram; o mapa antigo → novo está em `publico/mapa_commits_reescrita.csv`. Os arquivos retirados seguem no disco local, e `ferramentas/arquivar_privado.sh` leva as mudanças deles ao privado.

Por último, a pedido dos autores, o artigo e a vitrine ganharam a seção "Como esta síntese foi feita", antes da Introdução, que explica a *skill*, o livro de método (<https://felipelamarca.com/Systematic-Review/>) e os portões G1 a G9. No repositório de skills, a `tirar-cara-de-ia` saiu, e a `revisao-sistematica` deixou de mandar rodar um passe de estilo.

### Sessão de 23 e 24/09/2026: o que foi feito

A sessão fez tudo o que não depende de decisão humana e preparou o que depende. Em ordem:

1. **Correção de atribuição (Emenda 6a).**
   - O revisor declarou que não conferiu decisões que estavam registradas como suas:
     - 336 exclusões por título de registros sem resumo;
     - 88 consensos de RoB "confirmados em bloco";
     - 3 decisões de texto completo em que a IA estendeu uma regra dele;
     - a Emenda 2;
     - o fechamento da P034.
   - A tabela está em `00-protocolo/correcao_atribuicao.csv`.
   - Nos consensos de RoB, `resolvido_por` voltou a indicar a IA.
   - O log e o ledger só aceitam acréscimo; a correção fica registrada na emenda.
2. **Triagem complementar dos registros sem resumo (Emenda 6b).** Por decisão do revisor, nenhum registro é excluído só pelo título.
   - Os resumos foram recuperados de fontes legítimas para 169 dos 336 registros.
   - Dois triadores de IA independentes decidiram (concordância de 160 em 169): 156 exclusões e 180 registros seguindo ao texto completo.
   - Dos 181 textos buscados, 10 foram obtidos agora e 5 já estavam em disco. Os 15 foram fichados, e nenhum é elegível.
   - O conjunto de incluídos não mudou. Os arquivos estão em `02-triagem/sem_resumo_revisao/`.
3. **Relatos e versões.**
   - Cinco relatos foram ligados ao estudo de origem: Grillo2024d e Grillo2024e, John2021a (pré-registro de Unkelbach2022a), Hodgson2025a e Granziersd.
   - O Artigo 2 de Freden2016b é Freden2016a, para o qual não há cópia legítima.
   - Para Klor2017a só existem manuscritos (2006 e 2014); os números são os mesmos nos dois.
   - O relatório das buscas está em `03-textos/sessao_2026-09-23/`.
4. **Conferência dos efeitos por IA** (preparação da P039, antes P032).
   - **Re-extração cega** dos efeitos principais dos 40 estudos, por subagentes Opus, um PDF por agente.
   - **Comparação** da re-extração com a original.
   - **Arbitragem** de 28 estudos, com 771 correções aplicadas, mais uma por erro de plausibilidade, registradas uma a uma em `05-decomposicao/correcoes_sessao_2026-09-23.csv`.
   - **Erros reais encontrados:**
     - em Freden2024a, os braços estavam trocados, o que invertia a direção;
     - em Fichnova2015a e Lammers2022a, o contraste da exposição não tinha sido extraído (os g de 3,7 e 7,1 vinham de uma correlação entre rankings);
     - Kaplan2019a tinha um efeito sem direção;
     - o comparador `outro` foi usado em excesso e passou a `outro_resultado` ou `sem_pesquisa`;
     - quatro estudos têm alvo de *momentum* pela Emenda 4b.
   - **Pontos de julgamento para o revisor:** `08-revisao-humana/efeitos/pontos_para_o_revisor.md`.
5. **Síntese refeita.**
   - O dicionário `FORA` foi atualizado e a célula de *momentum* segue a Emenda 4b.
   - A sensibilidade ICC 0,20 (Emenda 4c) voltou.
   - A meta exploratória passou a usar CHE, como o protocolo manda quando um estudo tem mais de um efeito principal.
   - A nova célula "mesmo candidato atrás" chegou a k = 3 com g, e rodou a meta-análise que o protocolo prevê (exploratória).
   - As 58 mudanças de `ano_eleicao_pre2010` que faltavam foram registradas.
6. **GRADE refeito por IA** (`06-analise/prompt_grade_v2.md`):
   - a conta de rebaixamentos ficou coerente;
   - os domínios de RoB estão nomeados;
   - `validado_humano = 0`;
   - o agrupamento amplo foi para `certeza_agrupamento_amplo.csv`.
7. **Pacotes de revisão humana** para todas as 18 pendências, em `08-revisao-humana/`:
   - sugestões de IA em colunas separadas e campos humanos vazios;
   - terceiros leitores nas filas de triagem e de extração;
   - pré-PRESS da string ativa;
   - planilhas de RoB e de GRADE;
   - resumo dos portões.
8. **Relato:** PRISMA, lista de incluídos, manuscrito reescrito (`07-relatorio/prompt_redator_v2.md`), declaração de IA, render e publicação no GitHub Pages (`docs/`).

Os commits da sessão vão de `5aeceef` em diante (`git log`).

### Artigo final, PDF de *journal* e vitrine (24/09/2026, tarde)

O documento final foi reescrito como artigo de revisão sistemática. O ponto de partida foi o livro do autor (*Revisão sistemática de ponta a ponta*), sete revisões exemplares (SWiM, Cochrane, Campbell, APSR, *Nature Human Behaviour*) e três pareceres de especialistas simulados por IA sobre o plano. **Nenhuma análise mudou**: as células, as contagens, as certezas, as metas e as 18 pendências são as de 24/09.

- **Estrutura:** mensagens principais, resumo executivo, resumo e *abstract* no padrão PRISMA; depois Introdução, Métodos, Resultados (com mecanismo, moderadores e "não se aplica" do OQF), Discussão, Da evidência à prática e Conclusões. O texto tem cerca de 10.400 palavras, 7 figuras novas, 5 tabelas e 2 quadros, com a SoF narrativa em página deitada. O suplemento traz S1 a S11, com as listas PRISMA 2020, PRISMA-S, SWiM e PRISMA-trAIce e os agentes de IA desta versão. O resumo em linguagem simples é um documento à parte.
- **PDF:** A4 em uma coluna, compilado em Typst (Quarto 1.9.35), com STIX Two e Fira (OFL), citações APSA, cabeçalho neutro, marca-d'água de rascunho e nenhum elemento de revista real. `revista/verificar_pdf.py` confere fontes, caixas, IDs, mancha e reprodutibilidade.
- **Controle de qualidade (tudo por IA):**
  - travas de números e de enunciados em todas as versões;
  - verificação independente em duas rodadas: 4 erros e 17 avisos na primeira, 1 erro e 5 avisos na final, todos corrigidos;
  - auditoria A1 a A36 do livro: 18 cumpridos, 15 parciais, 3 não cumpridos, dois deles do autor;
  - rubrica cega v1 × v2: 2 contra 13 movimentos cumpridos;
  - leituras críticas simuladas de métodos e de ciência política, respondidas em `09-documento-final/resposta_pareceres.md`, com as decisões do autor ligadas às pendências;
  - passes de voz (`my-voice`) e anti-IA (`tirar-cara-de-ia`);
  - revisão visual dos PDFs.
- **Vitrine:** `docs/index.html` autocontido, em D3, com dados de uma lista de campos permitidos, tema claro e escuro, versão para celular e QA com Playwright e axe.
- **Decisões que ficam com o autor**, além das 18 pendências:
  - o estatuto do título (regra R7.28 do livro: produto executado por agentes não conta como revisão sistemática);
  - os marcadores **[A confirmar pelo autor]** (CRediT, acesso ao repositório, licença);
  - as reclassificações pedidas nas leituras críticas (`resposta_pareceres.md`).
