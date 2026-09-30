# Declaração dos autores sobre a coautoria (30/09/2026)

Este arquivo transcreve o que Felipe Lamarca declarou em chat ao coordenador de IA (Claude Code, `claude-opus-5-5`) em 30/09/2026, depois da versão de entrega. O agente transcreveu; os fechamentos de pendência e as declarações anteriores não foram reescritos.

## O que foi declarado

1. **Coautoria.** O trabalho foi desenvolvido com Lucas Berti, do IESP-UERJ, que é coautor, com contribuição igual à de Felipe Lamarca. Os papéis CRediT são os mesmos para os dois.
2. **Conferências humanas.** As conferências em bloco registradas em `declaracao_autor_2026-09-30.md` e em `P019_dedup/declaracao_autor_2026-09-30_dedup.md` foram feitas pelos dois autores, com contribuição igual:
   - a pré-revisão PRESS;
   - as 81 divergências da triagem;
   - as 165 propostas de elegibilidade e as 3 extensões de regra;
   - o piloto;
   - os 560 efeitos;
   - as divergências da recodificação;
   - o relato;
   - as decisões de deduplicação.

   Não houve dupla conferência humana independente: nenhuma dessas conferências foi feita em separado, às cegas, por cada autor.
3. **Decisões.** As decisões que Felipe Lamarca transmitiu em chat ao coordenador de IA foram dos dois autores. Isso inclui:
   - as emendas;
   - a regra das decisões divergentes na deduplicação e os 9 pares de versão;
   - as datas;
   - a aprovação da versão final;
   - a saída da faixa de topo da vitrine;
   - a abertura do repositório.

## Abertura do repositório

Na mesma data, os autores decidiram abrir o repositório `felipelmc/pesquisas-eleitorais-rs`. Antes, o histórico completo foi copiado para um repositório privado (`felipelmc/pesquisas-eleitorais-rs-completo`). Depois, foram tirados de todos os commits públicos, e passaram a ficar só no disco local e no repositório privado, estes arquivos:
- os resumos de terceiros em volume: exportações brutas das buscas, registros com resumo, lotes, filas e amostras de triagem, triagem dos registros sem resumo e pacotes de revisão humana com resumo;
- os pareceres dos triadores de IA e o ledger de decisões, que citam trechos dos resumos.

Os e-mails de terceiros que sobravam em arquivos públicos foram trocados por "[e-mail removido]" em todo o histórico.

## Como isso aparece nos registros

- No `rs_log.jsonl` e no `rs_estado.json`, `revisor_humano_1` é um papel, e não uma pessoa. As conferências e os fechamentos registrados com esse papel valem para os dois autores. O log só aceita acréscimo e não foi reescrito.
- Os produtos (artigo, apêndices, resumo em linguagem simples, vitrine, README e pacote de replicação) passam a dizer "os autores" onde antes diziam "o autor", sem afirmar dupla conferência independente.
- O risco de viés e a certeza da evidência seguem julgados só por IA, e P006, P007, P008, P033, P035, P036 e P042 continuam abertas.
