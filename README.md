# Pesquisas eleitorais publicadas e voto: revisão sistemática (bandwagon × underdog)

> **RASCUNHO NÃO VALIDADO.** Todas as etapas depois do protocolo foram feitas por subagentes de IA no modo autopiloto. Há 18 pendências humanas abertas; a lista, a ordem e os pacotes prontos estão em [`08-revisao-humana/README.md`](08-revisao-humana/README.md). Nenhum resultado deve ser citado como final antes de elas serem fechadas.

**No navegador:** <https://felipelamarca.com/pesquisas-eleitorais-rs/>. A página de entrada leva a quatro coisas:

- a **revisão final**, no formato *O que funciona?* do MAPE adaptado (`revisao.html` e `.docx`);
- o **relatório técnico** PRISMA (`relatorio-tecnico.html` e `.docx`);
- o **guia da revisão humana**;
- as mensagens principais.

O repositório é privado, mas as páginas do Pages são acessíveis a quem tiver o link.

## Pergunta

Qual é o efeito da exposição a resultados de pesquisas eleitorais publicadas (pesquisas pré-eleitorais, agregadores e projeções, boca de urna) sobre a intenção ou escolha de voto, e em que direção: *bandwagon* (apoio a quem aparece à frente) ou *underdog* (apoio a quem aparece atrás)? Desfecho secundário: mobilização (comparecimento, intenção de votar).

- **Tipo:** efetividade com SWiM (síntese sem meta-análise), variante rápida, skill `revisao-sistematica`.
- **Recorte:** relatos publicados desde 2010, escopo global, com seção própria para Brasil e América Latina.
- **Fontes:** OpenAlex (EN, PT, ES), BDTD e bola de neve (citações para frente e para trás). Não usa Web of Science, Scopus nem SciELO.
- **Portões:**
  - G1 e G2 foram aprovados pelo revisor humano em 19/09/2026.
  - G3 a G9 foram aprovados pelo autopiloto; o último, o G9, em 23/09/2026.
  - A sessão de 23 e 24/09/2026 corrigiu e refez etapas sem reaprovar portões (ver abaixo).

## Resultados em rascunho (24/09/2026)

| | |
|---|---|
| Registros | 1.767 nas bases (1.687 OpenAlex, 80 BDTD) e 1.706 por citação |
| Texto completo | 526 relatos buscados, 184 avaliados, 342 não recuperados, só por fontes legítimas |
| Incluídos | 41 estudos, 55 relatos (40 estudos com efeitos) |
| Efeitos extraídos | 560, nenhum conferido por humano; os principais foram re-extraídos às cegas e arbitrados por IA |

A certeza GRADE (`06-analise/certeza.csv`, rascunho de IA) qualifica a **direção** do efeito, não a magnitude.

- **Apoio a quem a pesquisa mostra à frente, em experimentos.** A direção é *bandwagon*.
  - Na célula principal do protocolo (pesquisa pré-eleitoral × sem pesquisa × randomizado), 4 de 4 estudos apontam nessa direção (teste de sinal p = 0,125). A certeza é muito baixa.
  - Na célula em que o mesmo candidato aparece à frente ou atrás (randomizado), também são 4 de 4 (p = 0,125), com certeza muito baixa. Três desses quatro estudos só entraram aqui depois das correções de 23/09.
  - No agrupamento amplo randomizado, que é descritivo e foi decidido depois de ver os dados, são 9 de 9 (p = 0,004). A certeza é muito baixa, por causa do rebaixamento por viés de publicação; decidir isso é um ponto para o revisor.
  - Quase tudo é laboratório ou vinheta hipotética: considerando só contexto real, sobra um experimento.
- **Estudos não randomizados:** as direções se dividem (3 de 4 no agrupamento amplo), com certeza muito baixa.
- **Mobilização:** não há direção consistente. Um experimento de campo (Gerber2020a) dá um efeito nulo ou trivial, com o IC inteiro dentro de ±2 p.p. (certeza moderada). Os estudos de boca de urna apontam desmobilização, com certeza muito baixa.
- **Tamanho do efeito:** não há meta-análise principal. As duas meta-análises exploratórias usam CHE + RVE, e as duas têm graus de liberdade de Satterthwaite abaixo de 4, o que torna o RVE não confiável:
  - célula "sem pesquisa" (3 estudos, 4 efeitos): g = 0,48, com IC95% de −1,51 a 2,47;
  - célula "mesmo candidato atrás" (3 estudos, 6 efeitos, desfechos em escalas diferentes): g = 0,62, com IC95% de −0,48 a 1,72.
- **Brasil:** o único estudo brasileiro, Araujo2021a, trata da apuração parcial oficial, não de pesquisa (Emenda 1).

Há dois documentos, e os dois estão publicados:

- **Revisão final**, fonte `09-documento-final/revisao_final.qmd`, publicada em `docs/revisao.html`. É o documento principal, no formato *O que funciona?* (OQF) do MAPE/IESP-UERJ adaptado: mensagens principais, efeito, mecanismos, moderadores, caixa de ferramentas, implicações para o debate brasileiro, metodologia e limitações, com as marcações do que ainda depende de revisão humana.
- **Relatório técnico**, fonte `07-relatorio/relatorio.qmd`, publicado em `docs/relatorio-tecnico.html`. É o manuscrito PRISMA 2020 completo, com tabelas estudo a estudo.

## Sessão de 23 e 24/09/2026: o que foi feito

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

Os commits da sessão vão de `0309f24` em diante (`git log`).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `00-protocolo/` | pergunta, teoria do programa e DAG, protocolo congelado no G2, codebooks, âncoras, `emendas.md` (E001, E002 e Emendas 1 a 6), `correcao_atribuicao.csv` |
| `01-busca/` | strings versionadas, `log_buscas.csv`, recall das âncoras, pré-PRESS por IA, pares de duplicata |
| `02-triagem/` | lotes e respostas dos triadores A e B, árbitro, fila humana, amostras de validação e elusão (não codificadas), `sem_resumo_revisao/` (Emenda 6b) |
| `03-textos/` | lista para baixar, relatório de PDFs, fichas de elegibilidade, `elegibilidade_tc_final.csv`, ligação de relatos, `sessao_2026-09-23/`. Os PDFs (`pdfs/`, `pdfs_descartados/`) **não são versionados** (ver abaixo) |
| `04-qualidade/` | RoB 2, ROBINS-I V2 e EPOC: fichas A e B, propostas do árbitro (`arbitragem/`), consenso, `rob_geral.csv`, `notas_rob.md` |
| `05-decomposicao/` | fichamentos (`fichamentos_master.csv`), efeitos por estudo (`efeitos/<chave>.csv`), verificação, validação da extração, `notas_extracao_completa.md`, `correcoes_revisao_g8.csv`, `correcoes_sessao_2026-09-23.csv` |
| `06-analise/` | efeitos calculados, entradas e saídas da SWiM (principal e sensibilidades, inclusive ICC 0,20), meta exploratória, `certeza.csv`, `certeza_agrupamento_amplo.csv`, `revisao_metodologica_g8.md`. `_superado_pre_revisao_g8/` guarda a síntese anterior à Emenda 5, só para histórico |
| `07-relatorio/` | manuscrito, PRISMA (contagens, SVG, PNG), checklists PRISMA e SWiM, `references.bib`, declaração de uso de IA, prompts do redator |
| `08-revisao-humana/` | pacotes das 18 pendências: índice, ordem, esforço, comandos, re-extração cega e arbitragens dos efeitos |
| `09-documento-final/` | revisão final no formato OQF adaptado. O texto fica em `_esqueleto_revisao_final.qmd`, e `montar_revisao_final.py` insere as tabelas geradas e grava `revisao_final.qmd`. Também estão aqui: insumos (contexto brasileiro com fontes, mecanismos e moderadores, números, caixa OQF), prompts do redator, do estilo e da verificação, `conferir_numeros.py` (trava dos passes de estilo), `verificacao.md` e a página de entrada (`index.qmd`) |
| `docs/` | versão publicada no GitHub Pages: `index.html` (entrada), `revisao.html`, `relatorio-tecnico.html`, `revisao-humana.html` e os `.docx`. Tudo é gerado por `docs/publicar.sh` |
| `dados/` | registros e decisões. Só a skill escreve aqui |
| `rs_estado.json`, `rs_log.jsonl` | estado e registro de eventos da skill (append-only). Nunca editar à mão |
| `ferramentas/` | conferências auxiliares: `checar_arbitros.py <raiz> [max_palavras] [subpasta]` confere vocabulário e trecho literal na página das propostas do árbitro de RoB; `achar_trecho.py <verificacao_citacoes.csv> <pasta_pdfs>` sugere o trecho literal mais próximo para citações reprovadas no gate |

## Cópia de trabalho e PDFs

- **Cópia de trabalho:** `~/Desktop/pesquisas-eleitorais-rs`, clone deste repositório. A revisão foi conduzida até 23/09/2026 em `~/revisoes/pesquisas-eleitorais`. Arquivos antigos (fichas, `pdf_path` de `05-decomposicao/fichamentos_master.csv`, prompts) guardam esse caminho como registro de proveniência. Não trabalhe em duas cópias ao mesmo tempo: `rs_estado.json` e `rs_log.jsonl` não se juntam bem.
- **PDFs:** ficam **só no disco local** da cópia de trabalho, fora do Git (`.gitignore`), porque são obras de terceiros.
  - `03-textos/pdfs/` tem 190 PDFs, os textos completos obtidos, nomeados `<chave>.pdf`, e uma página HTML.
  - `03-textos/pdfs_descartados/` tem 20: cópias de outra versão do mesmo trabalho, só folha de rosto ou documento errado. Os motivos estão em `03-textos/conferencia_pdfs.csv`.

  Sem eles não rodam `rs analise verificar-efeitos`, a conferência humana dos efeitos (P039), as arbitragens nem os scripts de `ferramentas/`.
- **Clone novo sem PDFs:** copie a pasta `03-textos/pdfs/` de uma cópia existente, ou baixe de novo com a skill `baixar-pdfs-academicos` a partir de `03-textos/para_baixar.csv`. O arquivo `03-textos/relatorio_pdfs.csv` diz de onde veio cada um. Os que só vieram de páginas de autor ou de repositórios podem não ser encontrados de novo; confira com `03-textos/verificacao_conteudo.csv`. Nunca use Sci-Hub ou fontes não autorizadas.

## Pendências humanas abertas (18)

A lista completa, a ordem sugerida, o esforço estimado, o pacote de cada uma e os comandos para registrar estão em **[`08-revisao-humana/README.md`](08-revisao-humana/README.md)**. Para listar: `rs --dir . pendencia listar`.

| ID | Etapa | Em uma linha |
|---|---|---|
| P001, P004 | busca (G3) | PRESS humano da string ativa (v5) e confirmação do G3 |
| P019 | organização | 145 pares candidatos de duplicata |
| P020, P006, P007, P008 | triagem (G4) | 81 divergências; validação cega (141) e elusão (300); confirmação do G4 |
| P041, P023 | texto completo (G5) | 165 decisões de elegibilidade propostas pela IA (antes P028 e P040); confirmação do G5 |
| P025, P026 | piloto (G6) | conferir os 3 estudos do piloto; confirmação do G6 |
| P039, P037, P033 | extração e RoB (G7) | conferir os 560 efeitos (antes P032); arbitrar 259 divergências da extração; validar 259 domínios de RoB |
| P036, P042, P035 | síntese (G8) | validar o GRADE (a P042, aberta pelo `rs caixa`, pede o mesmo); confirmação do G8 |
| P038 | relato (G9) | ler o manuscrito e confirmar o G9 |

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
# manuscrito: subagente com 07-relatorio/prompt_redator_v2.md
rs --dir . declaracao-ia     # sempre por último, antes do render
cd 07-relatorio && quarto render relatorio.qmd --to html && quarto render relatorio.qmd --to docx && cd ..
python3 09-documento-final/gerar_caixa_oqf.py && python3 09-documento-final/montar_revisao_final.py   # documento final
bash docs/publicar.sh        # entrada, revisão final, relatório técnico e guia em docs/ (GitHub Pages)
```

Cuidados:

- `rs bib` regrava `07-relatorio/references.bib` e apaga as três referências acrescentadas à mão (Hardmeier2008, MoyRinke2012, Barnfield2019). Se rodar, acrescente-as de novo.
- Os números do manuscrito e da revisão final são copiados dos arquivos por subagentes redatores. Se a síntese mudar, os dois textos precisam ser reescritos, não só renderizados. Na revisão final, isso significa editar o esqueleto, remontar, conferir com `09-documento-final/prompt_verificacao.md` e passar a trava de números em todo passe de estilo.
- `rs caixa` é opcional neste tipo de revisão. Rodá-lo abre a pendência `certeza_caixa`, que repete a validação do GRADE.
- Quando a última pendência fechar, o `rs status` deixa de marcar rascunho. Aí tire a faixa "RASCUNHO NÃO VALIDADO" do topo do `relatorio.qmd`.

## Limitações declaradas

- Triagem, elegibilidade, extração, RoB e GRADE foram feitos por subagentes de IA (Claude Sonnet e Opus, mesmo provedor), sem validação humana.
- Decisões registradas como humanas sem conferência humana foram corrigidas na Emenda 6a. Como o log só aceita acréscimo, as linhas antigas continuam lá.
- A triagem dos registros sem resumo foi refeita só por IA (Emenda 6b), com a conferência dispensada pelo revisor. O comando do skill grava `tipo_ator = humano` fixo nessas linhas; o papel `ia_coordenador_emenda6` e o motivo de cada uma dizem que a decisão é da IA.
- O árbitro do RoB foi do mesmo modelo do avaliador A e seguiu A em 79 de 88 domínios. Nenhum julgamento de RoB foi validado por humano.
- A concordância da extração ficou abaixo do limiar (58,5%). Os efeitos principais foram re-extraídos às cegas e arbitrados por IA, mas nenhum número foi conferido por humano.
- As âncoras e o PRESS foram feitos só por IA. O pré-PRESS da string ativa aponta lacunas de termos.
- Foi usado ROBINS-I V2 no lugar do ROBINS-E, que é o canônico para exposição.
- As decisões das Emendas 5 e 6b foram tomadas depois de ver os dados.
- Nenhum PDF foi obtido por Sci-Hub, LibGen ou outra fonte não autorizada.

Detalhes na seção de limitações do manuscrito e em `07-relatorio/declaracao_uso_ia_texto.md`.
