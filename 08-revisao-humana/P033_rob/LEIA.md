# P033: validação humana do risco de viés

Nenhum julgamento de risco de viés foi validado por humano. Os 88 consensos que a Emenda 4d dava como "confirmados em bloco" são, na verdade, propostas do árbitro de IA (`claude-opus-5-5`). Os outros 171 são concordâncias entre dois avaliadores de IA (A e B). Nenhum desses casos conta como validação (Emenda 6a).

## A planilha

O arquivo é `rob_revisao_humana.csv`, com uma linha por domínio × estudo × construto, 259 no total:

| ferramenta | desacordo A × B (revisar primeiro) | concordância A × B |
|---|---|---|
| RoB 2 | 45 | 77 |
| ROBINS-I V2 | 34 | 44 |
| EPOC | 9 | 50 |

Colunas:

- `julgamento_a`, `julgamento_b` e `proposta_consenso_ia`: os julgamentos dos avaliadores de IA e a proposta de consenso;
- `origem_proposta`: `arbitro_ia:...` quando houve desacordo, e `concordancia:ia_proposta_A+ia_proposta_B` quando houve acordo;
- `justificativa_ia`, `trecho` e `pagina`: a evidência citada pela IA. Confira o trecho na página do PDF.
- `julgamento_humano` e `justificativa_humana`: para você preencher.

Ponto já levantado pelos árbitros de efeitos: em **Fichnova2015a**, 17 dos 37 respondentes eslovacos não aparecem nas tabelas. É perda não relatada, e o domínio 3 do RoB 2 está como baixo.

## Como registrar

1. Para cada linha, copie o julgamento validado ou alterado para `julgamento_consenso` e a sua justificativa para `justificativa`, nos arquivos `04-qualidade/rob_<ferramenta>_consenso.csv`, na linha com a mesma `chave`, o mesmo `construto_outcome` e o mesmo `dominio`. Em `resolvido_por`, escreva `revisor_humano_1` **só nas linhas que você mesmo conferiu**.
2. Consolide cada ferramenta:
   ```bash
   rs() { python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py "$@"; }
   rs --dir . qualidade consolidar --ferramenta rob2 --consenso 04-qualidade/rob_rob2_consenso.csv --por revisor_humano_1
   rs --dir . qualidade consolidar --ferramenta robins_i --consenso 04-qualidade/rob_robins_i_consenso.csv --por revisor_humano_1
   rs --dir . qualidade consolidar --ferramenta epoc --consenso 04-qualidade/rob_epoc_consenso.csv --por revisor_humano_1 --ignorar-no-geral cg_sequencia_aleatoria,cg_ocultacao_alocacao
   ```
   Antes de rodar, confira na ajuda do comando o formato de `--ignorar-no-geral` (Emenda 4a).
3. `rob_geral.csv` só recebe `validado_humano = 1` quando **todas** as linhas usadas no julgamento geral tiverem `resolvido_por` humano.
4. Depois, refaça a cadeia do README a partir de `juntar_rob.py`.
