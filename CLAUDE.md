# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é este projeto

Revisão sistemática conduzida com a skill `revisao-sistematica` (e as irmãs `baixar-pdfs-academicos`, `fichamento-sistematico`, `gerar-bibtex`). O tema é o efeito da exposição a pesquisas eleitorais publicadas no voto, com a direção *bandwagon* × *underdog*. Tipo `efetividade_swim`, variante rápida, autopiloto, triagem por subagentes. Pergunta, resultados, estrutura de pastas e pendências estão no `README.md`; leia-o antes de qualquer trabalho.

Estado em 24/09/2026: G1 e G2 aprovados pelo revisor humano, G3 a G9 pelo autopiloto. A sessão de 23 e 24/09 fez tudo o que não depende de humano:
- Emenda 6: correção de atribuição e triagem complementar dos registros sem resumo;
- re-extração cega e arbitragem dos efeitos, com 771 correções;
- síntese e GRADE refeitos;
- pacotes de revisão humana;
- publicação no GitHub Pages.

Os produtos saem como **RASCUNHO NÃO VALIDADO**, com **18 pendências humanas abertas**. A ordem e os pacotes estão em `08-revisao-humana/README.md`. O que falta é trabalho humano; o papel do agente é preparar esse trabalho, registrá-lo pelos comandos da skill e refazer os produtos.

## Como começar uma sessão

```bash
rs() { python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py "$@"; }; rs --dir ~/Desktop/pesquisas-eleitorais-rs status
rs --dir ~/Desktop/pesquisas-eleitorais-rs pendencia listar
```

Defina a função `rs` em cada chamada de Bash (cada chamada abre um shell novo). Não deduza o estado da conversa: o `status` e o `rs_log.jsonl` são a fonte. A cadeia completa para refazer efeitos, síntese e relato está no `README.md`, seção "Refazer os produtos depois de fechar pendências".

Como ler o `status` (sai em JSON):
- `etapa_atual` aparece como `05_organizacao` mesmo com G9 aprovado, porque a deduplicação (P019) segue aberta. Isso é esperado; o campo `proxima_acao` diz o que vem a seguir.
- Algumas descrições de pendência citam IDs já substituídos (P005, P022, P034). Vale a lista de `pendencia listar`, não os IDs citados dentro do texto.
- `buscas_inativas: B01` é a busca em inglês substituída pela B05 (emenda E002). Não é um erro.

Ferramentas: `python3`, `Rscript` e `quarto`. Os scripts R que o `rs` chama (`efeitos.R`, `swim.R`, `_cli.R`) ficam em `~/.claude/skills/revisao-sistematica/scripts/R/`, não no repositório. No repositório, os únicos scripts são os de junção e montagem da síntese (`05-decomposicao/juntar_rob.py`, `06-analise/montar_*.py`), os de conferência em `ferramentas/` (uso no README) e o `03-textos/prompts_fichamento/gate_sem_heuristica.py` (`<ficha.md> <pdf>`). Este último roda o gate de citação do `fichamento-sistematico` sem a heurística de "PDF sem texto", que reprova teses por engano.

## Regras do usuário (valem em toda sessão)

- Decisões e aprovações vão ao usuário pelo AskUserQuestion, com a opção recomendada em primeiro lugar e marcada "(Recomendado)".
- **Sci-Hub não é usado.** Nenhum agente usa Sci-Hub, LibGen, Anna's Archive, Z-Library ou espelhos, contorna paywall, login ou desafio antirrobô, nem baixa de sites de upload de terceiros (ResearchGate, Academia.edu, Scribd). PDF que não vier de fonte legítima fica como não recuperado.
- Credenciais (`OPENALEX_API_KEY`, `RS_EMAIL`) só como prefixo de variável de ambiente no comando; nunca gravadas em arquivo do projeto, script ou commit.
- Subagentes só em Sonnet (volume) e Opus (texto completo, julgamentos difíceis). Nunca Fable.
- Registro sem resumo nunca é excluído por filtro ou por LLM.
- PDFs de terceiros nunca vão para o GitHub (`03-textos/pdfs/` e `03-textos/pdfs_descartados/` estão no `.gitignore`). Repositório remoto: `felipelmc/pesquisas-eleitorais-rs`, privado.
- Cópia de trabalho: `~/Desktop/pesquisas-eleitorais-rs`, com os PDFs só no disco local (README, seção "Cópia de trabalho e PDFs"). O caminho antigo `~/revisoes/pesquisas-eleitorais` que aparece em fichas, prompts e no `pdf_path` do master é proveniência: não reescreva esses registros. Em prompts reaproveitados, troque a raiz pela da cópia de trabalho.
- Commits terminam com `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Commit e push só quando o usuário pedir.

## Regras da skill que mais pesam aqui

- Nunca edite à mão `rs_estado.json`, `rs_log.jsonl`, `dados/`. Só `rs.py` escreve neles.
- O protocolo está congelado desde o G2. Qualquer mudança de método é emenda em `00-protocolo/emendas.md` registrada com `rs emenda`, declarando se foi decidida antes ou depois de ver os dados. Hoje há E001 e E002 (busca) e as Emendas 1 a 6. A 5 (pós-revisão metodológica do G8) define a síntese. A 6 corrige atribuições humanas indevidas (`00-protocolo/correcao_atribuicao.csv`) e define a triagem complementar por IA dos registros sem resumo (6b, dispensada de conferência pelo revisor).
- `resolvido_por`, `verificado_humano`, `validado_humano` e `--por revisor_humano_1` só recebem papel humano quando o usuário declarar que fez aquela revisão. Concordância entre dois avaliadores de IA não valida nada.
- Direção pelo estimador, nunca pela significância. A certeza GRADE qualifica a direção, não a magnitude.
- Junções só por `id_rs`, `id_registro`, `chave` ou `chave + construto_outcome`, nunca por título.
- O coordenador não abre PDFs em volume: leitura de texto completo é trabalho de subagente, um PDF por subagente, até 3 em paralelo. Os prompts usados estão guardados junto das saídas; reuse-os. São eles:
  - `05-decomposicao/prompt_complemento_efeitos.md`;
  - `04-qualidade/prompt_arbitro_rob.md`;
  - `06-analise/prompt_grade_v2.md`;
  - `07-relatorio/prompt_redator_v2.md`;
  - `03-textos/prompts_fichamento/fichador_elegibilidade.md`, com a raiz trocada;
  - `08-revisao-humana/efeitos/prompt_reextracao_cega.md` e `prompt_arbitro_efeitos.md`;
  - `08-revisao-humana/P037_concordancia/prompt_terceiro_leitor.md`;
  - `02-triagem/sem_resumo_revisao/INSTRUCOES_triagem.md`;
  - `09-documento-final/prompt_redator_final.md`, `prompt_estilo.md` e `prompt_verificacao.md`.

## Convenções da síntese (Emenda 5)

- Célula = `familia_intervencao` × `construto_outcome` × `comparador_tipo` × `celula_alvo` × classe de desenho. Randomizado e não randomizado nunca se juntam. O agrupamento amplo (`construto_outcome,celula_alvo`) é só descritivo.
- `celula_alvo`: `principal` (líder, azarão, opção de referendo), `viabilidade` (segundo viável, terceiro inviável, partido perto da cláusula), `momentum` (ganho, perda ou tom sem posição; ver conjunto `MOMENTUM`), `mobilizacao`.
- Sinal: `direcao_desejada = aumentar` para `lider`, `opcao_referendo` e `segundo_viavel`; `reduzir` para `azarao`, `terceiro_inviavel` e `partido_abaixo_clausula`. Nos desenhos de proibição, o efeito é reorientado para o da exposição (Chatterjee2019a, Morton2015a).
- δ = 2 p.p. convertido em g: 0,044 (apoio), 0,046 (mobilização) e 0,0573 na célula principal (mediana de p0 = 0,73, em `06-analise/_delta_celula.txt`). Efeito com IC95% inteiro dentro de ±δ vira nulo (`yi = 0`, coluna `nulo_por_delta`), porque o `swim.R` não aceita δ.
- Os efeitos principais que não estimam o contraste da exposição estão no dicionário `FORA` de `06-analise/montar_entradas_swim.py`, com o motivo. Eles entram só na narrativa e na sensibilidade `com_excluidos`.
- *Momentum* (Emenda 4b): o conjunto `MOMENTUM` de `montar_entradas_swim.py` (Dahlgaard2016a, Meer2015a, Stolwijk2016a, Unkelbach2022a e Witsman2016a) manda à célula `momentum` as linhas de apoio com alvo `nao_se_aplica`.
- Comparador: `outro_resultado` quando o grupo de comparação viu outra pesquisa; `outro` só quando nenhum outro valor serve.
- Estimando pela regra congelada de `b2_estimando`: diferença-em-diferenças sem sorteio é ATT; antes e depois só nos tratados, ou interação com moderador não sorteado, é `associacao`.
- Estudos com RoB crítico saem da análise principal (`--excluir-rob critico`) e entram na sensibilidade `com_critico`.
- ICC imputado 0,05 em desenhos com cluster, com sensibilidade 0,20 (Emenda 4c). No EPOC, sequência e ocultação são ignoradas no geral (Emenda 4a, `--ignorar-no-geral`).
- Não há meta-análise principal. Há duas metas exploratórias: a da célula "mesmo candidato atrás" (`meta_mesmo_candidato/`, 3 estudos) e a da célula principal "sem pesquisa" (3 estudos, 4 efeitos, inclui Tyszler2015 lido de figura). Esta última sai de `06-analise/montar_meta_exploratoria.py`, com `--dependencia che` (protocolo, seção 8), porque Tyszler2015 tem dois efeitos principais.
- Sensibilidade ICC 0,20: `06-analise/montar_sens_icc020.py` e os argumentos opcionais dos dois scripts `montar_*` (cadeia no README).

## Armadilhas já encontradas

- `rs prisma` regrava `07-relatorio/checklist_prisma.csv` e apaga a coluna `local_no_relato`. Preencha-a de novo depois de cada `rs prisma`.
- `rs bib` regrava `07-relatorio/references.bib` e apaga Hardmeier2008, MoyRinke2012 e Barnfield2019, acrescentadas à mão. Se rodar, acrescente-as de novo.
- `rs declaracao-ia` vai sempre por último, depois de qualquer comando que escreva no log; depois dele, só o `quarto render`.
- `ano_eleicao = 999` significa eleição hipotética ou induzida em laboratório, não eleição antiga. `ano_eleicao_pre2010` deve ficar `nao` nesses casos.
- `desenho` precisa conter "randomizado" para o `_cli.R` classificar como randomizado. Ele já trata "não randomizado" como negação; não reclassifique por regex própria.
- Conversões do `efeitos.R`: `dif_prop` precisa de `p0` e de `se_pp`, IC ou `n1 + n2`; `beta_sd` precisa de `sdy`; o ajuste de cluster precisa de `cluster` e `icc`.
- Qualquer mudança num efeito derruba o `verificado_humano` da linha. Depois de corrigir `05-decomposicao/efeitos/<chave>.csv`, rode a cadeia inteira de novo, a partir de `preparar-efeitos`.
- Os números do manuscrito foram escritos por subagente a partir dos arquivos. Se a síntese mudar, reescreva as seções afetadas do `relatorio.qmd` (use `07-relatorio/prompt_redator.md`); não basta renderizar.
- Backups e versões superadas (`05-decomposicao/efeitos_backup_*`, `06-analise/_superado_pre_revisao_g8/`) são histórico. Não os use como entrada.
- `rs triagem consolidar` usa a regra `consenso` por padrão. A rodada ta_v1 é **liberal**: passe sempre `--regra liberal`.
- `rs triagem override` grava `tipo_ator = humano` fixo. Para registrar decisão de IA por ele (caso da Emenda 6b), use um `--por` que diga IA (`ia_coordenador_emenda6`) e um motivo explícito, e documente na emenda.
- `rs textos elegibilidade consolidar` exige `--master 03-textos/fichamentos_master.csv --codebook 00-protocolo/codebook_elegibilidade.csv`. Para fichas novas, gere as linhas com `consolida.py` do fichamento-sistematico numa pasta temporária e acrescente ao master; não refaça o master inteiro.
- `rs prisma` quebra a invariante `recuperacao_fecha` quando há PDF recuperado sem decisão de texto completo. Isso acontece, por exemplo, com PDFs que já estavam em disco quando o registro voltou ao texto completo. Fiche esses textos.
- `07-relatorio/_pendencias_abertas.json` não é gerado por comando da skill. Refaça-o com `rs --dir . pendencia listar > 07-relatorio/_pendencias_abertas.json`.
- `rs caixa` é opcional neste tipo de revisão, e rodá-lo abre uma pendência `certeza_caixa` (foi o que criou a P042, que repete a P036).
- Pendências mudam de ID quando o comando as reabre: P032 virou P039, e P028 virou P040 e depois P041. Confira no `rs pendencia listar`.
- O gate de citações das fichas de elegibilidade é `03-textos/prompts_fichamento/gate_sem_heuristica.py <ficha> <pdf>`. Ficha reprovada vai para `_reprovadas/` como `<nome>.tentativaN.md` e é refeita por um fichador novo, nunca corrigida à mão.
- Na publicação, `bash docs/publicar.sh` gera `docs/`: a entrada (`09-documento-final/index.qmd`, com as mensagens principais extraídas da revisão final), `revisao.html`, `relatorio-tecnico.html` e `revisao-humana.html`. Nada de dados brutos, fichas ou PDFs entra em `docs/`. O endereço é <https://felipelamarca.com/pesquisas-eleitorais-rs/>, o domínio próprio do Pages do usuário.
- Revisão final (`09-documento-final/`):
  - Edite só `_esqueleto_revisao_final.qmd` e depois rode `montar_revisao_final.py`. Rodar o script sobrescreve `revisao_final.qmd`.
  - Passes de estilo seguem `prompt_estilo.md`, com as regras de `~/.claude/commands/my-voice.md` e a skill `tirar-cara-de-ia`. Cada passe exige a trava `conferir_numeros.py` vazia.
  - Os callouts "Pendente de revisão humana" e o apêndice de pendências ficam até o usuário fechar as pendências.

## Onde está o raciocínio de cada decisão

- Método e emendas: `00-protocolo/protocolo.md`, `00-protocolo/emendas.md`.
- Extração, por estudo: `05-decomposicao/notas_extracao_completa.md`, `05-decomposicao/correcoes_revisao_g8.csv`, `05-decomposicao/complementos_efeitos/*.json`.
- Risco de viés: `04-qualidade/notas_rob.md`, `04-qualidade/arbitragem/`.
- Síntese: `06-analise/revisao_metodologica_g8.md` (problemas R01 a R19 e as correções), `06-analise/certeza.csv` e `certeza_agrupamento_amplo.csv`.
- Conferência dos efeitos por IA em 23/09: `08-revisao-humana/efeitos/` (re-extração cega, comparação, arbitragens, `pontos_para_o_revisor.md`), `05-decomposicao/correcoes_sessao_2026-09-23.csv`.
- Revisão humana: `08-revisao-humana/README.md` (ordem, esforço, pacote e comando de cada pendência).
- Uso de IA: `07-relatorio/declaracao_uso_ia.md` (gerada do log) e `07-relatorio/declaracao_uso_ia_texto.md`.
