# Revisão humana: o que foi conferido e o que falta

Em 30/09/2026, o autor declarou ter conferido as etapas abaixo e concordar com as decisões em vigor. A declaração está em `declaracao_autor_2026-09-30.md` e a emenda correspondente é a Emenda 7 (`00-protocolo/emendas.md`). A conferência foi **em bloco**: o autor não preencheu as planilhas item a item. O coordenador de IA preencheu os campos humanos a partir da declaração, e cada fechamento cita esse arquivo no motivo.

Ficam abertas as pendências de risco de viés, certeza (GRADE), validação cega da triagem e aplicação da deduplicação. Na versão de entrega, essas etapas são declaradas como feitas só por IA. Numa evolução do projeto, precisam de revisão humana: os pacotes desta pasta continuam prontos para isso.

Definições de rs:

```bash
rs() { python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py "$@"; }
```

## Fechadas em 30/09/2026 (Emenda 7)

| Pendência | Etapa | O que o autor confirmou | Registro |
|---|---|---|---|
| P001, P004 | busca (G3) | conferência da pré-revisão PRESS da S-oa-en-v5 feita por IA; decisão (a): aceitar a v5 e declarar as lacunas | `01-busca/press_revisor_humano_1.md` |
| P020 | triagem (G4) | as 81 divergências seguem ao texto completo pela regra liberal (estado atual) | `P020_triagem/fila_humana_ta_v1.csv` |
| P041, P023 | texto completo (G5) | as 165 propostas de elegibilidade e as 3 extensões de regra (RS4220, RS4487, RS4361) | `03-textos/fila_humana_tc.csv` |
| P025, P026 | piloto (G6) | os 3 estudos do piloto e a Emenda 2 | motivo no log |
| P039 | extração (G7) | os 560 efeitos, conferidos na página do PDF (`verificado_humano = sim`); os pontos de `efeitos/pontos_para_o_revisor.md` no estado atual | `05-decomposicao/efeitos_extraidos.csv` |
| P037 | extração | as 259 divergências da recodificação, com o valor original | `P037_concordancia/arbitragem_humana.csv` |

A P038 (G9, relato) fecha quando o autor aprovar o PDF final.

## Ordem sugerida e esforço

Pendências que continuam abertas, para a próxima versão:

| # | Pendência | Etapa | O que fazer | Pacote | Esforço |
|---|---|---|---|---|---|
| 1 | P019 | organização | aplicar as decisões de deduplicação já registradas nos 145 pares (66 fusões, 56 rejeições, 23 ligações). Antes, corrigir no `rs.py` a consolidação da triagem para registros absorvidos, rodar o filtro de novo e decidir os 9 pares de versão que surgirão; depois, refazer o PRISMA | `P019_dedup/` | 2 a 3 h |
| 2 | P006 | triagem T/A | amostra de validação cega: 141 registros, dois codificadores que não viram as decisões da IA | `P006_P007_validacao/` | 2 × 1,5 h |
| 3 | P007 | triagem T/A | amostra de elusão cega: 300 registros excluídos pela IA | `P006_P007_validacao/` | 2 h |
| 4 | P008 | portão G4 | confirmar o G4 depois de P006 e P007 (recall da triagem por IA) | seção abaixo | 5 min |
| 5 | P033 | extração e RoB (G7) | validar os 259 domínios de risco de viés (88 desacordos primeiro) e confirmar o G7 | `P033_rob/` | 4 a 6 h |
| 6 | P036 e P042 | síntese | validar os juízos GRADE; a P042, aberta pelo `rs caixa`, pede o mesmo | `P036_grade/` | 1 h |
| 7 | P035 | portão G8 | confirmar o G8 depois da P036 | seção abaixo | 5 min |
| 8 | P038 | portão G9 | ler o artigo final (`docs/revisao.pdf`) e confirmar o G9 | artigo em `docs/revisao.pdf` | 1 h |

## Portões

Cada portão foi aprovado automaticamente pelas checagens de artefato da skill. Confirmar um portão é declarar que você leu o que ele aprovou. Feche primeiro as pendências de conteúdo daquela etapa, depois o portão:

```bash
rs --dir . pendencia fechar P008 --motivo "G4 confirmado: <resumo>" --por revisor_humano_1
```

Troque `P008` por P035 ou P038, conforme o portão.

## Depois de fechar pendências

- Se RoB ou GRADE mudarem, refaça a cadeia do `REPRODUZIR.md` (seção "Refazer os produtos") e depois `bash ferramentas/refazer_produtos.sh`.
- Se a certeza mudar, a sentinela de `09-documento-final/spec_final.md` aponta quais seções do artigo reescrever.
- Com todas as pendências fechadas, o `rs status` deixa de marcar rascunho, e a linha "RASCUNHO NÃO VALIDADO" sai da declaração de uso de IA do artigo.
