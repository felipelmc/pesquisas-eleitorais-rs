# Abertura do artigo e resumo em linguagem simples (etapa 4)

Você escreve a abertura do artigo "Pesquisas eleitorais publicadas mudam o voto?" (autor Felipe Lamarca, MAPE/IESP-UERJ), em português, com *abstract* em inglês, e o resumo em linguagem simples, que é um documento separado. O corpo já está escrito. Você não o reescreve: resume o que ele diz. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Não rode `rs.py`, não abra PDFs e não rode nada em segundo plano.

## Leia antes
- O corpo: `09-documento-final/_esqueleto_revisao_final.qmd` e a versão montada (`python3 09-documento-final/montar_revisao_final.py` → `revisao_final.qmd`), com a Tabela de resumo dos achados (`@tbl-sof`).
- A especificação: `09-documento-final/spec_v2.md`, nas seções da abertura e do resumo em linguagem simples.
- `09-documento-final/insumos/livro_regras.md`, seções 2, 3 e 9, e `insumos/exemplares_movimentos.md`: resposta primeiro (Kalla & Broockman), *Key messages* e "o que a evidência não diz" (Cochrane), resumo em linguagem simples com perguntas (Fisher 2023).
- `revista/celulas.json`, com os enunciados literais.
- `/Users/felipelmc/.claude/commands/my-voice.md`.

## O que escrever (troque cada parágrafo `[Abertura: etapa 4]` do esqueleto)
1. **Mensagens principais**, dentro da Div que já existe: 4 ou 5 itens em lista, com até 200 palavras no total.
   - Cada item começa com um rótulo curto em negrito e traz a direção, o k, o selo `[⊕◯◯◯]{.grade}` com a palavra da certeza e a frase padrão.
   - Mensagem que junta duas células diz "cada uma com certeza muito baixa".
   - A ressalva sobre Witsman2016a-E01 acompanha o item do "mesmo candidato atrás", como no corpo.
   - Um item sobre o Brasil e um item sobre o que a evidência não permite dizer.
   - O agrupamento amplo *post hoc* nunca vira manchete.
2. **Resumo executivo** (de 500 a 800 palavras). Pirâmide invertida, começando pelo problema de política no Brasil. Só prosa, sem listas.
3. **Resumo** (até 250 palavras), dentro de `::: {.resumo}`, com subtítulos em negrito na mesma linha, cobrindo os 12 itens do resumo PRISMA 2020:
   - **Contexto.**
   - **Objetivos.**
   - **Métodos:** fontes e data da última busca; critérios de elegibilidade; risco de viés; síntese; certeza.
   - **Resultados:** estudos, participantes ou unidades quando houver, e os principais achados com a certeza.
   - **Limitações:** a IA sem validação humana; os 342 de 526 relatos não recuperados.
   - **Conclusões.**
   - **Registro e financiamento.**

   As metas exploratórias entram no máximo numa oração, sem g pontual. Feche com `**Palavras-chave:** ...`.
4. ***Abstract*** (até 250 palavras), em `::: {.resumo lang="en"}`. É o mesmo conteúdo em inglês acadêmico natural, não uma tradução palavra por palavra, com as frases GRADE em inglês: "very uncertain", "may", "probably". Feche com `**Keywords:** ...`.
5. **Resumo em linguagem simples**, em `09-documento-final/linguagem_simples.qmd`. Como YAML, use `title` (o título é a própria mensagem, em linguagem comum), `lang: pt-BR` e `format: html` com `embed-resources: true`. O texto, com 600 a 750 palavras, no presente, sem citações nem notas:
   - "A revisão em resumo", com até 50 palavras;
   - subtítulos em forma de pergunta: "Do que trata esta revisão?", "Que estudos entraram?", "O que encontramos?", "O que isso significa?", "Quais são os limites?" e "Até quando vai a busca?";
   - números em unidades simples, por exemplo "2 em cada 100 eleitores" para o δ de 2 pontos percentuais;
   - todos os desfechos principais;
   - no fim, uma linha com "Rascunho não validado; 18 pendências de revisão humana" e o link para `revisao.html`.

## Regras
- Todo número da abertura e do resumo em linguagem simples tem de aparecer no corpo ou nas fontes da trava. Nada de número novo.
- Proibido: "Neutro", "sem efeito", "não significativo", "benéfico", "danoso" e travessão.
- Não altere o corpo. As 11 caixas e os IDs continuam como estão.
- Depois de escrever:
  1. rode `python3 09-documento-final/montar_revisao_final.py` e `python3 09-documento-final/conferir_reestruturacao.py`, que tem de passar sem FALHA;
  2. rode um script seu que lista os números da abertura (Mensagens, Resumo executivo, Resumo, *Abstract*) e do resumo em linguagem simples ausentes do corpo, e que precisa sair vazio;
  3. conte as palavras de cada parte;
  4. renderize o `linguagem_simples.qmd` para HTML.

Responda com até 10 linhas: palavras por parte, os 12 itens do resumo cobertos (sim/não), o resultado das travas e do script de números.
