# Revisão humana: o que foi conferido e o que falta

Em 30/09/2026, os autores declararam ter conferido as etapas abaixo e concordar com as decisões em vigor (a conferência foi dos dois, Felipe Lamarca e Lucas Berti, sem dupla independente; `declaracao_autores_2026-09-30_coautoria.md`). A declaração está em `declaracao_autor_2026-09-30.md` e a emenda correspondente é a Emenda 7 (`00-protocolo/emendas.md`). A conferência foi **em bloco**: os autores não preencheram as planilhas item a item. O coordenador de IA preencheu os campos humanos a partir da declaração, e cada fechamento cita esse arquivo no motivo.

No mesmo dia, a deduplicação que os autores decidiram foi aplicada, com a ferramenta corrigida, e os 9 pares de versão que a aplicação reabriu foram ligados por eles (Emenda 8; `P019_dedup/declaracao_autor_2026-09-30_dedup.md`).

Ficam abertas as pendências de risco de viés, certeza (GRADE) e validação cega da triagem. Na versão de entrega, essas etapas são declaradas como feitas só por IA. Os autores estão revendo o risco de viés e o GRADE; quando concluírem, a declaração deles fecha P033, P035, P036 e P042. Os pacotes desta pasta continuam prontos para isso.

Definições de rs:

```bash
rs() { python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py "$@"; }
```

## Fechadas em 30/09/2026 (Emendas 7 e 8)

| Pendência | Etapa | O que os autores confirmaram | Registro |
|---|---|---|---|
| P001, P004 | busca (G3) | conferência da pré-revisão PRESS da S-oa-en-v5 feita por IA; decisão (a): aceitar a v5 e declarar as lacunas | `01-busca/press_revisor_humano_1.md` |
| P020 | triagem (G4) | as 81 divergências seguem ao texto completo pela regra liberal (estado atual) | `P020_triagem/fila_humana_ta_v1.csv` |
| P041, P023 | texto completo (G5) | as 165 propostas de elegibilidade e as 3 extensões de regra (RS4220, RS4487, RS4361) | `03-textos/fila_humana_tc.csv` |
| P025, P026 | piloto (G6) | os 3 estudos do piloto e a Emenda 2 | motivo no log |
| P039 | extração (G7) | os 560 efeitos, conferidos na página do PDF (`verificado_humano = sim`); os pontos de `efeitos/pontos_para_o_revisor.md` no estado atual | `05-decomposicao/efeitos_extraidos.csv` |
| P037 | extração | as 259 divergências da recodificação, com o valor original | `P037_concordancia/arbitragem_humana.csv` |
| P038 | relato (G9) | leu e aprovou o artigo final com apêndices (versão de entrega) | motivo no log |
| P019 | organização | as 145 decisões de deduplicação, aplicadas depois da triagem, com a decisão mais inclusiva nos 44 registros absorvidos já triados, e os 9 pares de versão, ligados por eles (Emenda 8) | `P019_dedup/declaracao_autor_2026-09-30_dedup.md` |


## Ordem sugerida e esforço

Pendências que continuam abertas:

| # | Pendência | Etapa | O que fazer | Pacote | Esforço |
|---|---|---|---|---|---|
| 1 | P006 | triagem T/A | amostra de validação cega: 141 registros, dois codificadores que não viram as decisões da IA | `P006_P007_validacao/` | 2 × 1,5 h |
| 2 | P007 | triagem T/A | amostra de elusão cega: 300 registros excluídos pela IA | `P006_P007_validacao/` | 2 h |
| 3 | P008 | portão G4 | confirmar o G4 depois de P006 e P007 (recall da triagem por IA) | seção abaixo | 5 min |
| 4 | P033 | extração e RoB (G7) | validar os 259 domínios de risco de viés (88 desacordos primeiro) e confirmar o G7 | `P033_rob/` | 4 a 6 h |
| 5 | P036 e P042 | síntese | validar os juízos GRADE; a P042, aberta pelo `rs caixa`, pede o mesmo | `P036_grade/` | 1 h |
| 6 | P035 | portão G8 | confirmar o G8 depois da P036 | seção abaixo | 5 min |

## Portões

Cada portão foi aprovado automaticamente pelas checagens de artefato da skill. Confirmar um portão é declarar que você leu o que ele aprovou. Feche primeiro as pendências de conteúdo daquela etapa, depois o portão:

```bash
rs --dir . pendencia fechar P008 --motivo "G4 confirmado: <resumo>" --por revisor_humano_1
```

Troque `P008` por P035, conforme o portão.

## Depois de fechar pendências

- Se RoB ou GRADE mudarem, refaça a cadeia do `REPRODUZIR.md` (seção "Refazer os produtos") e depois `bash ferramentas/refazer_produtos.sh`.
- Se a certeza mudar, a sentinela de `09-documento-final/spec_final.md` aponta quais seções do artigo reescrever.
- Com todas as pendências fechadas, o `rs status` deixa de marcar rascunho, e a linha "RASCUNHO NÃO VALIDADO" sai da declaração de uso de IA do artigo.

## Para uma próxima versão (decisões sem pendência)

As leituras críticas simuladas por IA de 24/09/2026 (`09-documento-final/resposta_pareceres.md`) deixaram decisões dos autores que não têm pendência no `rs.py`. As ligadas a pendências já fechadas pela Emenda 7 (P037, P039) ficaram no estado atual; as ligadas à P036 entram na revisão do GRADE. Sobram estas, para uma evolução do projeto:

- busca em registros de experimentos e pré-registros (AEA, OSF, EGAP);
- versão datada do ROBINS-I V2 usada, datas de acesso e parâmetros dos modelos de IA, que não foram registrados;
- tabela dos motivos de não recuperação dos 338 relatos buscados e não recuperados e tentativa por meios legítimos (acesso institucional, empréstimo, contato com autores);
- fonte primária do voto obrigatório no Brasil (Constituição, art. 14) e uma medida publicada de confiança nas pesquisas eleitorais, para o contexto brasileiro.
