# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é este projeto

Revisão sistemática conduzida com a skill `revisao-sistematica` (e as irmãs `baixar-pdfs-academicos`, `fichamento-sistematico`, `gerar-bibtex`). O tema é o efeito da exposição a pesquisas eleitorais publicadas no voto, com a direção *bandwagon* × *underdog*. Tipo `efetividade_swim`, variante rápida, autopiloto, triagem por subagentes. Pergunta, resultados, estrutura de pastas e pendências estão no `README.md`; leia-o antes de qualquer trabalho.

Estado em 23/09/2026: G1 a G9 aprovados (G1 e G2 pelo revisor humano, o resto pelo autopiloto). Os produtos saem como **RASCUNHO NÃO VALIDADO**, com 17 pendências humanas abertas. O que falta é trabalho humano; o papel do agente é preparar esse trabalho, registrá-lo pelos comandos da skill e refazer os produtos.

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
- O protocolo está congelado desde o G2. Qualquer mudança de método é emenda em `00-protocolo/emendas.md` registrada com `rs emenda`, declarando se foi decidida antes ou depois de ver os dados. Hoje há E001 e E002 (busca) e as Emendas 1 a 5; a 5 (pós-revisão metodológica do G8) define a síntese atual.
- `resolvido_por`, `verificado_humano`, `validado_humano` e `--por revisor_humano_1` só recebem papel humano quando o usuário declarar que fez aquela revisão. Concordância entre dois avaliadores de IA não valida nada.
- Direção pelo estimador, nunca pela significância. A certeza GRADE qualifica a direção, não a magnitude.
- Junções só por `id_rs`, `id_registro`, `chave` ou `chave + construto_outcome`, nunca por título.
- O coordenador não abre PDFs em volume: leitura de texto completo é trabalho de subagente, um PDF por subagente, até 3 em paralelo. Os prompts usados estão guardados junto das saídas (`05-decomposicao/prompt_complemento_efeitos.md`, `04-qualidade/prompt_arbitro_rob.md`, `06-analise/prompt_grade.md`, `07-relatorio/prompt_redator.md`); reuse-os.

## Convenções da síntese (Emenda 5)

- Célula = `familia_intervencao` × `construto_outcome` × `comparador_tipo` × `celula_alvo` × classe de desenho. Randomizado e não randomizado nunca se juntam. O agrupamento amplo (`construto_outcome,celula_alvo`) é só descritivo.
- `celula_alvo`: `principal` (líder, azarão, opção de referendo), `viabilidade` (segundo viável, terceiro inviável, partido perto da cláusula), `momentum` (só Dahlgaard2016a), `mobilizacao`.
- Sinal: `direcao_desejada = aumentar` para `lider`, `opcao_referendo` e `segundo_viavel`; `reduzir` para `azarao`, `terceiro_inviavel` e `partido_abaixo_clausula`. Nos desenhos de proibição, o efeito é reorientado para o da exposição (Chatterjee2019a, Morton2015a).
- δ = 2 p.p. convertido em g: 0,044 (apoio), 0,046 (mobilização) e 0,0588 na célula principal (mediana de p0 = 0,74). Efeito com IC95% inteiro dentro de ±δ vira nulo (`yi = 0`, coluna `nulo_por_delta`), porque o `swim.R` não aceita δ.
- Os efeitos principais que não estimam o contraste da exposição estão no dicionário `FORA` de `06-analise/montar_entradas_swim.py`, com o motivo. Eles entram só na narrativa e na sensibilidade `com_excluidos`.
- Estudos com RoB crítico saem da análise principal (`--excluir-rob critico`) e entram na sensibilidade `com_critico`.
- ICC imputado 0,05 em desenhos com cluster, com sensibilidade 0,20 (Emenda 4c). No EPOC, sequência e ocultação são ignoradas no geral (Emenda 4a, `--ignorar-no-geral`).
- Não há meta-análise principal. A meta exploratória (k = 3, inclui Tyszler2015 lido de figura) sai de `06-analise/montar_meta_exploratoria.py`.

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

## Onde está o raciocínio de cada decisão

- Método e emendas: `00-protocolo/protocolo.md`, `00-protocolo/emendas.md`.
- Extração, por estudo: `05-decomposicao/notas_extracao_completa.md`, `05-decomposicao/correcoes_revisao_g8.csv`, `05-decomposicao/complementos_efeitos/*.json`.
- Risco de viés: `04-qualidade/notas_rob.md`, `04-qualidade/arbitragem/`.
- Síntese: `06-analise/revisao_metodologica_g8.md` (problemas R01 a R19 e as correções), `06-analise/certeza.csv`.
- Uso de IA: `07-relatorio/declaracao_uso_ia.md` (gerada do log) e `07-relatorio/declaracao_uso_ia_texto.md`.
