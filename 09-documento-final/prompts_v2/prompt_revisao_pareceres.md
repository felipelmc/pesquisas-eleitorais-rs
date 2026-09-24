# Revisão depois das leituras críticas (etapa 6)

Você é o redator do artigo "Pesquisas eleitorais publicadas mudam o voto?" e responde a duas leituras críticas simuladas por IA: `09-documento-final/_leituras/L1_metodos.md` e `09-documento-final/_leituras/L2_ciencia_politica.md`. Leve em conta também a verificação independente, `09-documento-final/verificacao_v2.md` e `09-documento-final/auditoria_final.md`, e a rubrica cega, `09-documento-final/_avaliacao/rubrica.md`. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Rode scripts Python com `python3 -B`. Não rode `rs.py`, não abra PDFs e não rode nada em segundo plano.

## Onde você pode editar
- `09-documento-final/_esqueleto_revisao_final.qmd`;
- `09-documento-final/linguagem_simples.qmd`;
- `09-documento-final/revista/figuras/legendas.yml`: só o texto; os marcadores ficam;
- `09-documento-final/revista/tabelas/*.yml`: só o texto;
- `09-documento-final/_esqueleto_suplemento.qmd`: só a prosa.

Não mexa em arquivos de dados, figuras, scripts nem em `spec_v2.md`.

## Regras
0. **Fatos novos** só de dossiês verificados: `insumos/contexto_brasil.md` (inclusive a seção 7, "Regras do dia da eleição", recém-acrescentada), `insumos/revisoes_anteriores.md`, `insumos/garritty_2024.md`, `insumos/mecanismos_moderadores.md` e os arquivos de dados. Item "não confirmado" não entra como fato. Se citar uma chave nova de `referencias_contexto.bib`, rode `python3 -B 09-documento-final/revista/preparar_referencias.py` (usa o cache) antes de montar.
1. **Só redação, ordem e cortes.**
   - Um pedido que exija análise nova, ou que mude célula, efeito fora da contagem, alvo, GRADE, rótulo da caixa ou critério, NÃO é aplicado. Ele vai para `09-documento-final/resposta_pareceres.md` como "decisão do autor", ligado à pendência correspondente (P0xx). Se nenhuma pendência cobrir o pedido, marque "decisão do autor (sem pendência aberta)".
   - O texto do artigo pode apresentar esses pontos como abertos, sem resolvê-los.
2. **Todos os erros de `verificacao_v2.md` são corrigidos.** Cada aviso é corrigido ou justificado. Cada item "parcial" ou "não cumprido" da auditoria que dependa do texto é resolvido.
3. **Enxugamento.**
   - O corpo (seções 1 a 6) tem hoje cerca de 12 mil palavras, contra cerca de 9.430 na especificação. Leve-o a **no máximo 10.500 palavras de prosa** (sem os spans `.enunciado`, as caixas, os quadros, as legendas e as tabelas), e as Informações adicionais a no máximo 900.
   - Corte primeiro a redundância, depois o detalhe de procedimento que já está no suplemento (troque por "detalhes no [S2](suplemento.html#s2-atalhos)"), e só então explicações.
   - Nunca corte conteúdo exigido pelo PRISMA, pelo SWiM ou pelo livro. Nunca corte os estudos nomeados em cada achado, as ressalvas de certeza, as caixas de pendência nem os marcadores [A confirmar pelo autor].
4. **Travas.** Todo número continua saindo das fontes. Depois de cada rodada:
   - `python3 -B 09-documento-final/montar_revisao_final.py`;
   - `python3 -B 09-documento-final/conferir_reestruturacao.py`, que tem de passar sem FALHA;
   - o render Typst: `cd 09-documento-final && TYPST_IGNORE_SYSTEM_FONTS=true TYPST_IGNORE_EMBEDDED_FONTS=true quarto render revisao_final.qmd --to typst`, sem aviso.
5. **Rubrica.** Resolva os dois movimentos parciais da rubrica cega:
   - M07: nenhum verbo mais forte que a certeza em trecho de destaque (Mensagens, Resumo executivo, Resumo, Discussão 4.1, Conclusões). Troque "permite descartar", "é evidência de que", "a direção dominante é" e "domina" pelas frases padrão da certeza da célula.
   - M08: declare na Síntese (2.7) o estimando de cada classe de desenho, pela regra congelada do protocolo: efeito causal nos randomizados; ATT na diferença-em-diferenças sem sorteio; associação no antes e depois só nos tratados e na interação com moderador não sorteado. Diga na Discussão se as classes convergem, e na contagem de realismo (3.10) não some as classes.

   Corte também o metatexto repetido de processo dentro dos parágrafos, como "Resolvem P0xx" em cada parágrafo: as caixas de pendência e o Apêndice A já fazem esse papel. Os marcadores [A confirmar pelo autor] e as 11 caixas ficam.
6. **Resposta ponto a ponto.** Em `resposta_pareceres.md`, cada comentário de L1 e L2 recebe:
   - uma decisão: `aceito`, `aceito em parte`, `não aceito` ou `decisão do autor`;
   - o que foi feito e onde;
   - para `não aceito`, o motivo.

   Depois, uma seção para os erros e avisos da verificação e para os itens da auditoria.

Responda com até 12 linhas:
- quantos comentários em cada categoria;
- palavras do corpo antes e depois;
- o resultado das travas e do render;
- a lista das "decisões do autor" novas.
