# Pesquisas eleitorais publicadas e voto: revisão sistemática (bandwagon × underdog)

> **RASCUNHO NÃO VALIDADO.** Todas as etapas depois do protocolo foram feitas por subagentes de IA no modo autopiloto. Há 17 pendências humanas abertas (lista abaixo). Nenhum resultado deve ser citado ou divulgado antes de elas serem fechadas.

## Pergunta

Qual é o efeito da exposição a resultados de pesquisas eleitorais publicadas (pesquisas pré-eleitorais, agregadores e projeções, boca de urna) sobre a intenção ou escolha de voto, e em que direção: *bandwagon* (apoio a quem aparece à frente) ou *underdog* (apoio a quem aparece atrás)? Desfecho secundário: mobilização (comparecimento, intenção de votar).

- Tipo: efetividade com SWiM (síntese sem meta-análise), variante rápida, skill `revisao-sistematica`.
- Recorte: relatos publicados desde 2010, escopo global, com seção própria para Brasil e América Latina.
- Fontes: OpenAlex (EN, PT, ES), BDTD e bola de neve (citações para frente e para trás). Sem Web of Science, Scopus ou SciELO.
- Portões: G1 e G2 aprovados pelo revisor humano em 19/09/2026; G3 a G9 aprovados pelo autopiloto, com a última aprovação (G9) em 23/09/2026.

## Resultados em rascunho

| | |
|---|---|
| Registros | 1.767 nas bases (1.687 OpenAlex, 80 BDTD) e 1.706 por citação |
| Incluídos | 41 estudos, 55 relatos |
| Não recuperados | 95 relatos das bases e 82 dos outros métodos, só por fontes legítimas |
| Efeitos extraídos | 554, nenhum conferido por humano |

A certeza GRADE (em `06-analise/certeza.csv`) qualifica a **direção** do efeito, não a magnitude:

- **Apoio a quem a pesquisa mostra à frente, em experimentos.** A direção é *bandwagon*.
  - Na célula principal do protocolo (pesquisa pré-eleitoral × sem pesquisa × randomizado), 4 de 4 estudos apontam nessa direção (teste de sinal p = 0,125). A certeza é muito baixa.
  - No agrupamento amplo randomizado, que é descritivo e foi decidido depois de ver os dados, são 8 de 8 (p = 0,008). A certeza é baixa.
  - Quase tudo é laboratório ou vinheta hipotética: com só contexto real, sobra um experimento.
- **Estudos não randomizados:** as direções se dividem, com certeza muito baixa.
- **Mobilização:** sem direção consistente. Os três estudos de boca de urna apontam desmobilização, mas esse padrão foi notado depois de ver os dados.
- **Tamanho do efeito:** não há meta-análise principal. A exploratória (k = 3) dá g = 0,46, com IC95% de −0,62 a 1,53.
- **Brasil:** o único estudo brasileiro, Araujo2021a, trata da apuração parcial oficial, não de pesquisa (Emenda 1).

O manuscrito completo está em `07-relatorio/relatorio.html` e `07-relatorio/relatorio.docx` (fonte: `relatorio.qmd`).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `00-protocolo/` | pergunta, teoria do programa e DAG, protocolo congelado no G2, codebooks, âncoras, `emendas.md` (Emendas 1 a 5) |
| `01-busca/` | strings versionadas, `log_buscas.csv`, recall das âncoras, pré-PRESS por IA, pares de duplicata |
| `02-triagem/` | lotes e respostas dos triadores A e B, árbitro, fila humana, amostras de validação e elusão (não codificadas) |
| `03-textos/` | lista para baixar, relatório de PDFs, fichas de elegibilidade, `elegibilidade_tc_final.csv`, ligação de relatos. Os PDFs (`pdfs/`) **não são versionados** |
| `04-qualidade/` | RoB 2, ROBINS-I V2 e EPOC: fichas A e B, propostas do árbitro (`arbitragem/`), consenso, `rob_geral.csv`, `notas_rob.md` |
| `05-decomposicao/` | fichamentos (`fichamentos_master.csv`), efeitos por estudo (`efeitos/<chave>.csv`), verificação, validação da extração, `notas_extracao_completa.md` |
| `06-analise/` | efeitos calculados, entradas e saídas da SWiM (principal e sensibilidades), meta exploratória, `certeza.csv`, `revisao_metodologica_g8.md`. `_superado_pre_revisao_g8/` guarda a síntese anterior à Emenda 5, só para histórico |
| `07-relatorio/` | manuscrito, PRISMA (contagens, SVG, PNG), checklists PRISMA e SWiM, `references.bib`, declaração de uso de IA |
| `dados/` | registros e decisões. Só a skill escreve aqui |
| `rs_estado.json`, `rs_log.jsonl` | estado e registro de eventos da skill (append-only). Nunca editar à mão |

## Pendências humanas abertas

Para listar: `rs --dir . pendencia listar`. Para fechar uma pendência só documental: `rs --dir . pendencia fechar <ID> --motivo "..." --por revisor_humano_1`. Pendência de dados fecha sozinha quando o comando correspondente é rodado de novo com a decisão humana registrada.

Ordem sugerida: a das etapas, porque decisões de busca e triagem podem mudar o conjunto de incluídos, e isso muda tudo o que vem depois.

| ID | Etapa | O que fazer | Arquivo | Como registrar |
|---|---|---|---|---|
| P001 | busca (G3) | PRESS 2015 humano da estratégia `S-oa-en-v4`. Só houve pré-revisão por IA | `01-busca/strings/S-oa-en-v4.txt`, `01-busca/prepress_*_ia.md` | gravar `01-busca/press_<revisor>.md`; se pedir nova string, nova versão com `buscar openalex --substituir` |
| P004 | busca (G3) | confirmar a aprovação automática do G3 | — | `pendencia fechar` depois de P001 |
| P019 | organização | revisar 145 pares candidatos de duplicata | `01-busca/dedup_pares.csv` | preencher `decisao` e rodar `rs dedup --revisar 01-busca/dedup_pares.csv --por revisor_humano_1` |
| P020 | triagem T/A (G4) | resolver 81 divergências entre os triadores A e B (o árbitro de IA já opinou) | `02-triagem/fila_humana_ta_v1.csv` | preencher `decisao_humana`, `criterio_humano` e `motivo_humano`; `rs triagem override --fila 02-triagem/fila_humana_ta_v1.csv --etapa ta --por revisor_humano_1` |
| P006 | triagem T/A (G4) | codificar em dupla, às cegas, a amostra de validação (141 registros) | `02-triagem/validacao/ta_v1/amostra01_cega.xlsx` | `rs validar calcular --planilha <xlsx> --finalidade validacao` |
| P007 | triagem T/A (G4) | codificar em dupla, às cegas, a amostra de elusão (300 excluídos) | `02-triagem/validacao/ta_v1/elusao01_cega.xlsx` | `rs validar calcular --planilha <xlsx> --finalidade elusao` |
| P008 | triagem T/A (G4) | confirmar a aprovação automática do G4 | — | `pendencia fechar` depois de P006, P007 e P020 |
| P028 | textos (G5) | conferir 150 decisões de elegibilidade propostas a partir das fichas (incertos primeiro) | `03-textos/elegibilidade_tc_final.csv`, `03-textos/fichas_elegibilidade/` | `rs triagem override --etapa tc --id <id_rs> --decisao ... --criterio ... --motivo ... --por revisor_humano_1` (ou `--fila`) |
| P023 | textos (G5) | confirmar a aprovação automática do G5 | — | `pendencia fechar` depois de P028 |
| P025 | piloto (G6) | conferir fichas e efeitos dos 3 estudos do piloto contra os PDFs | `05-decomposicao/piloto_fichamentos_master.csv`, `05-decomposicao/piloto/revisao_coordenador.md` | `pendencia fechar` com o resultado da conferência |
| P026 | piloto (G6) | confirmar a aprovação automática do G6 | — | `pendencia fechar` depois de P025 |
| P032 | extração (G7) | conferir 100% dos 554 efeitos na página do PDF (números, sinal, DP × EP, n, estimando, modelo principal) | `05-decomposicao/efeitos_extraidos.csv`, `verificacao_efeitos.csv` | marcar `verificado_humano = sim` em `efeitos_extraidos.csv`; `rs analise verificar-efeitos` (fecha quando todas as linhas ficam aptas) |
| P037 | extração | arbitrar a concordância da recodificação cega (58,5%; `alvo_efeito` e `comparador_tipo` em 50%) ou redefinir as variáveis e recodificar | `05-decomposicao/validacao_extracao/concordancia/` | corrigir `efeitos/<chave>.csv` ou `fichamentos_master.csv` e fechar com motivo |
| P033 | RoB (G7) | validar o RoB: 23 resultados RoB 2, 13 ROBINS-I e 7 EPOC. Os 88 desacordos foram confirmados em bloco; as 171 concordâncias entre dois avaliadores de IA **não** contam como validação | `04-qualidade/rob_*_consenso.csv` | revisar as linhas, pôr `resolvido_por = revisor_humano_1` e rodar `rs qualidade consolidar --ferramenta <f> --consenso <csv> --por revisor_humano_1` (EPOC com `--ignorar-no-geral`, Emenda 4a) |
| P036 | síntese | validar os 21 juízos GRADE. Decisão em aberto: rebaixar ou não por viés de publicação o agrupamento amplo randomizado de apoio, o que o levaria de baixa para muito baixa | `06-analise/certeza.csv` | preencher `validado_humano` e alterar o que discordar |
| P035 | síntese (G8) | confirmar a aprovação automática do G8 | — | `pendencia fechar` depois de P036 |
| P038 | relato (G9) | confirmar a aprovação automática do G9 (leitura do manuscrito) | `07-relatorio/relatorio.qmd` | `pendencia fechar` depois de todas as outras |

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

# 3. SWiM principal e sensibilidades
G=familia_intervencao,construto_outcome,comparador_tipo,celula_alvo; A=construto_outcome,celula_alvo
rs --dir . analise swim --in 06-analise/swim_entrada_principal.csv --out-dir 06-analise/swim_principal --grupo $G --separar-desenho sim --excluir-rob critico
rs --dir . analise swim --in 06-analise/swim_entrada_principal.csv --out-dir 06-analise/swim_sens_com_critico --grupo $G --separar-desenho sim
rs --dir . analise swim --in 06-analise/swim_entrada_principal.csv --out-dir 06-analise/swim_sens_agrupamento_amplo --grupo $A --separar-desenho sim --excluir-rob critico
for s in com_excluidos so_contexto_real sem_pre2010 sem_araujo; do
  rs --dir . analise swim --in 06-analise/swim_entrada_$s.csv --out-dir 06-analise/swim_sens_${s}_amplo --grupo $A --separar-desenho sim --excluir-rob critico
done
rs --dir . analise meta --in 06-analise/meta_entrada_exploratoria.csv --out-dir 06-analise/meta_exploratoria \
  --grupo familia_intervencao,construto_outcome,comparador_tipo --dependencia um_por_estudo \
  --delta "$(cat 06-analise/_delta_celula.txt)" --separar-desenho sim --excluir-rob critico

# 4. GRADE (06-analise/certeza.csv; rascunho por subagente com 06-analise/prompt_grade.md) e relato
rs --dir . prisma            # regrava checklist_prisma.csv: preencha local_no_relato de novo depois
rs --dir . incluidos
rs --dir . declaracao-ia     # sempre por último, antes do render
cd 07-relatorio && quarto render relatorio.qmd --to html && quarto render relatorio.qmd --to docx
```

Cuidados:

- `rs bib` regrava `07-relatorio/references.bib` e apaga as três referências acrescentadas à mão (Hardmeier2008, MoyRinke2012, Barnfield2019). Se rodar, acrescente-as de novo.
- Os números do manuscrito foram copiados dos arquivos por um subagente redator (`07-relatorio/prompt_redator.md`). Se a síntese mudar, o texto precisa ser reescrito, não só renderizado.
- Quando a última pendência fechar, o `rs status` deixa de marcar rascunho. Aí tire a faixa "RASCUNHO NÃO VALIDADO" do topo do `relatorio.qmd`.

## Limitações declaradas

- Triagem, elegibilidade, extração, RoB e GRADE foram feitos por subagentes de IA (Claude Sonnet e Opus, mesmo provedor), sem validação humana.
- O árbitro do RoB foi do mesmo modelo do avaliador A e seguiu A em 79 de 88 domínios. Os 88 consensos foram confirmados em bloco.
- A concordância da extração ficou abaixo do limiar (58,5%).
- As âncoras e o PRESS foram feitos só por IA.
- Foi usado ROBINS-I V2 no lugar de ROBINS-E (canônico para exposição).
- As decisões da Emenda 5 foram tomadas depois de ver os dados.
- Nenhum PDF foi obtido por Sci-Hub, LibGen ou outra fonte não autorizada.

Detalhes na seção de limitações do manuscrito e em `07-relatorio/declaracao_uso_ia_texto.md`.
