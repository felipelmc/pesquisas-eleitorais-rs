# P037: arbitragem da concordância da extração

> **Fechada em 30/09/2026 (Emenda 7).** O autor declarou ter conferido esta etapa em bloco e manteve o estado atual (`08-revisao-humana/declaracao_autor_2026-09-30.md`). O texto abaixo descreve o pacote como foi preparado em 23/09/2026.


A recodificação cega de 10 estudos (Sonnet) concordou com a extração original em só 58,5% dos valores. As 259 divergências (`discorda` e `discorda_parcial` em `05-decomposicao/validacao_extracao/concordancia/concordancia.csv`) estão em `arbitragem_humana.csv`.

Para cada divergência, um **terceiro leitor de IA** (`claude-opus-5-5`, um PDF por agente) leu o texto e sugeriu qual valor o texto sustenta. As respostas brutas estão em `terceiro_leitor/resposta_<chave>.json`. Os valores possíveis da sugestão são:

- `original`;
- `revalidacao`;
- `equivalentes`: a mesma coisa dita com outras palavras;
- `nenhum`: os dois valores estão errados, e o terceiro leitor dá outro;
- `indecidivel`.

A planilha vem ordenada com `nenhum` e `indecidivel` primeiro.

**A sugestão não decide nada.** Preencha `decisao_humana` (`original`, `revalidacao` ou `outro`), `valor_final` e `motivo_humano`.

Depois:

1. Corrija os valores em `05-decomposicao/fichamentos_master.csv` ou em `05-decomposicao/efeitos/<chave>.csv`. Mudar um efeito derruba o `verificado_humano` daquela linha.
2. Refaça a cadeia do `REPRODUZIR.md` a partir de `preparar-efeitos`.
3. Feche a pendência:
   ```bash
   rs --dir . pendencia fechar P037 --motivo "arbitragem humana de N divergências" --por revisor_humano_1
   ```

Nos estudos que foram arbitrados na conferência dos efeitos (P032/P039), as variáveis de efeito já foram corrigidas por IA (`05-decomposicao/correcoes_sessao_2026-09-23.csv`). Confira ali antes de mudar.
