# Declaração do autor sobre a revisão humana (30/09/2026)

Este arquivo transcreve o que o autor (`revisor_humano_1`) declarou em chat ao coordenador de IA (Claude Code, `claude-opus-5-5`) em 30/09/2026, ao pedir a versão final de entrega. Os fechamentos de pendência feitos com base nessa declaração citam este arquivo no motivo. O agente transcreveu; não houve conferência item a item registrada pelo próprio autor nas planilhas.

## Declaração geral, nas palavras do autor

> De fato eu já fiz uma revisão bastante sistemática e minuciosa de todas as informações do relatório e todos os dados intermediários, e gostei bastante do resultado e concordo com todas as decisões tomadas pelos modelos.

## O que a revisão cobriu, segundo o autor

Perguntado sobre o que a revisão cobriu de fato, o autor marcou:

| Bloco | Itens | Pendências |
|---|---|---|
| Busca e triagem | pré-revisão PRESS da string ativa (S-oa-en-v5); 145 pares candidatos de duplicata; 81 divergências da triagem de títulos e resumos; 165 decisões de elegibilidade no texto completo | P001, P004, P019, P020, P041, P023 |
| Efeitos contra os PDFs | os 560 efeitos conferidos na página do PDF; as 259 divergências da recodificação da extração; o piloto de 3 estudos | P039, P037, P025, P026 |
| Artigo e relatório | leitura do artigo, do suplemento e do relatório técnico | P038 |

O autor **não** marcou o bloco "RoB e GRADE" (259 domínios de risco de viés e os juízos de certeza).

## Decisões do autor na mesma conversa

- **RoB e GRADE**, nas palavras do autor:

  > Pode declarar que essa etapa foi feita inteiramente por IA para a versão da entrega do trabalho; para uma eventual evolução do projeto, será necessário incluir humanos no processo

  Ficam abertas P033, P035, P036 e P042.

- **Validação cega da triagem (P006 e P007).** O autor escolheu declarar a validação como não feita. Concordar com a IA depois de ver as decisões não vale como codificação cega. P006, P007 e o portão G4 (P008) ficam abertos.

- **Filas de divergência.** O autor escolheu o **estado atual**:
  - P020: os 81 registros seguem ao texto completo pela regra liberal, como hoje;
  - P037: os 259 itens ficam com o valor original;
  - P039: os pontos de julgamento de `efeitos/pontos_para_o_revisor.md` ficam como estão, porque nenhum foi alterado pelo coordenador.

- **Deduplicação (P019).**
  - O autor concorda com as sugestões da IA nos 145 pares.
  - Antes, tinha escolhido aplicar essas sugestões. Informado de que aplicar quebraria o `rs prisma` e criaria 9 pares novos, que ele não viu, escolheu **registrar as decisões e não aplicá-las** nesta versão.
  - A P019 fica aberta.
  - [Nota de 30/09/2026: aplicadas no mesmo dia, a pedido do autor (Emenda 8; `P019_dedup/declaracao_autor_2026-09-30_dedup.md`). A P019 fechou.]

- **Rótulo.** O produto passa a se chamar "síntese sistemática de evidências conduzida com agentes de IA", pela regra R7.28 do livro do autor, sem o adjetivo "rápida".

- **Marca de rascunho.**
  - O PDF sai sem marca-d'água e sem os avisos de pendência.
  - A declaração de IA abre com "RASCUNHO NÃO VALIDADO" e a lista do que ficou sem validação humana (R7.23).

- **Declarações para o artigo.** Sem conflito de interesses, nem relação com a Anthropic. Todos os papéis CRediT humanos são do autor.

- **Repositório.** Segue privado. Um pacote de replicação sem resumos nem e-mails de terceiros é publicado pelo GitHub Pages, com MIT para o código e CC BY 4.0 para textos e dados.
