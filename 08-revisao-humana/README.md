# Revisão humana: o que falta e como fazer

A revisão tem **17 pendências abertas** (`rs --dir . pendencia listar`). Todas exigem decisão humana. A IA não fecha nenhuma: o skill registra fechamento só com ator humano, e as regras do projeto não permitem atribuir papel humano a decisões de IA.

Esta pasta prepara cada uma para decisão rápida. As sugestões de IA ficam sempre em colunas ou arquivos separados, e as colunas humanas vêm vazias. **Nenhuma sugestão de IA conta como validação.**

Definições de rs:

```bash
rs() { python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py "$@"; }
```

## Ordem sugerida e esforço

A ordem segue as etapas, porque decisões de busca e de triagem podem mudar o conjunto de incluídos, e isso muda tudo o que vem depois.

| # | Pendência | Etapa | O que fazer | Pacote | Esforço |
|---|---|---|---|---|---|
| 1 | P001 | busca (G3) | PRESS humano da string **ativa**, S-oa-en-v5. A pendência cita a v4, que foi substituída | `P001_press/` | 2,5 a 3,5 h |
| 2 | P004 | portão G3 | confirmar o G3 | seção abaixo | 5 min |
| 3 | P019 | organização | 145 pares candidatos de duplicata, com sugestão da IA por par | `P019_dedup/` | 1 a 1,5 h |
| 4 | P020 | triagem T/A | 81 divergências entre os triadores A e B, com sugestão de um terceiro leitor cego | `P020_triagem/` | 1 h |
| 5 | P006 | triagem T/A | amostra de validação cega: 141 registros, dois codificadores | `P006_P007_validacao/` | 2 × 1,5 h |
| 6 | P007 | triagem T/A | amostra de elusão cega: 300 registros excluídos pela IA | `P006_P007_validacao/` | 2 h |
| 7 | P008 | portão G4 | confirmar o G4 | seção abaixo | 5 min |
| 8 | P040 | texto completo | 160 decisões de elegibilidade propostas pela IA (antes P028) | `P040_elegibilidade/` | 3 a 4 h |
| 9 | P023 | portão G5 | confirmar o G5 | seção abaixo | 5 min |
| 10 | P025 | piloto | conferir os 3 estudos do piloto | `P025_piloto/` | 1 h |
| 11 | P026 | portão G6 | confirmar o G6 | seção abaixo | 5 min |
| 12 | P039 | extração | conferir os 560 efeitos na página do PDF (antes P032). Comece pelos principais e pelos pontos que os árbitros levantaram | `efeitos/` | 6 a 10 h |
| 13 | P037 | extração | 259 divergências da recodificação cega, com sugestão de um terceiro leitor | `P037_concordancia/` | 2 a 3 h |
| 14 | P033 | portão G7 e RoB | validar os 259 domínios de RoB (88 desacordos primeiro) | `P033_rob/` | 4 a 6 h |
| 15 | P036 | síntese | validar os juízos GRADE | `P036_grade/` | 1 h |
| 16 | P035 | portão G8 | confirmar o G8 | seção abaixo | 5 min |
| 17 | P038 | portão G9 | ler o manuscrito e confirmar o G9 | `07-relatorio/relatorio.html` | 2 h |

## P039: conferência dos efeitos (pasta `efeitos/`)

- `efeitos/cega/<chave>.json`: re-extração **cega** dos efeitos principais dos 40 estudos, feita por outro agente sem ver a original.
- `efeitos/comparacao_cega.csv`: original × cega, por efeito principal.
- `efeitos/arbitragem/<chave>.json`: decisão de um árbitro de IA em 28 estudos com divergência, com trecho e página.
- `05-decomposicao/correcoes_sessao_2026-09-23.csv`: as 771 correções aplicadas.
- `efeitos/aplicacao_arbitragem.csv`: o que não foi aplicado, e por quê.
- **`efeitos/pontos_para_o_revisor.md`**: decisões de julgamento que os árbitros deixaram para você. Entre elas: se Gerber2020a-E12, Feltovich2022-E01/E02 e Schlegel2023 entram no dicionário `FORA`; se Geers2018 volta à contagem; e o alvo de Witsman2016a-E01.

Como registrar: marque `verificado_humano = sim` em `05-decomposicao/efeitos_extraidos.csv` nas linhas que você conferir. Depois rode `rs --dir . analise verificar-efeitos`. A pendência fecha quando todas as linhas estiverem aptas. Qualquer correção de valor se faz em `05-decomposicao/efeitos/<chave>.csv`, e depois a cadeia do README roda de novo desde `preparar-efeitos`.

## Portões aprovados pelo autopiloto (P004, P008, P023, P026, P035 e P038)

Cada portão foi aprovado automaticamente com as checagens de artefato do skill. Confirmar um portão é declarar que você leu o que ele aprovou. Ordem de fechamento: **primeiro as pendências de conteúdo daquela etapa, depois o portão.**

| Portão | Aprovou | Depende de | Riscos principais |
|---|---|---|---|
| G3 (P004) | a busca: B05 no OpenAlex em inglês (substituiu a B01), B02, B03 e B04 em PT e ES, BDTD, e a bola de neve SN1 a SN3 | P001 | o PRESS só foi feito por IA. Lacunas: termos de proibição e de apuração parcial, e comparecimento na BDTD (`P001_press/`) |
| G4 (P008) | a triagem de títulos e resumos, com a rodada ta_v1 e dois triadores de IA | P006, P007, P020 | não há validação humana nem recall calculado. A Emenda 6b refez por IA os 336 registros sem resumo |
| G5 (P023) | a elegibilidade no texto completo: 55 relatos incluídos, 41 estudos (40 com efeitos) | P040 | propostas de IA; 17 decisões limítrofes suas; 3 extensões de regra feitas pela IA |
| G6 (P026) | o piloto de extração (3 estudos) e a Emenda 2 | P025 | a Emenda 2 foi decidida pela IA |
| G8 (P035) | a síntese (SWiM) e o GRADE | P036 | decisões da Emenda 5 tomadas depois de ver os dados; GRADE rascunhado por IA |
| G9 (P038) | o relato | todas as outras | o manuscrito foi redigido por IA a partir dos arquivos |

Comando para fechar cada portão, **só depois** de fechar as pendências de que ele depende:

```bash
rs --dir . pendencia fechar P004 --motivo "G3 conferido: <resumo>" --por revisor_humano_1
```

Troque `P004` por P008, P023, P026, P035 ou P038 conforme o portão.

## Depois de fechar pendências

Refaça os produtos pela cadeia do `README.md` da raiz, seção "Refazer os produtos depois de fechar pendências". Quando a última pendência fechar, o `rs status` deixa de marcar rascunho. Aí tire a faixa "RASCUNHO NÃO VALIDADO" do `07-relatorio/relatorio.qmd`.
