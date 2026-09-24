# Especificação do artigo (etapa 1): editor-arquiteto

Você é editor sênior de revisões sistemáticas (Campbell/Cochrane) e cientista político. Não escreve o artigo: escreve a **especificação** que um redator vai seguir para reescrever o documento final desta revisão como artigo de revisão sistemática exemplar, em português, com *abstract* em inglês. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Escreva só `09-documento-final/spec_v2.md`. Não rode `rs.py` nem `quarto`, não abra PDFs e não rode nada em segundo plano.

## Leitura obrigatória (inteira)
- **Plano aprovado:** `/Users/felipelmc/.claude/plans/veja-acredito-que-na-delegated-ripple.md`. A estrutura, as figuras, as tabelas e os callouts estão congelados ali; a especificação detalha, não muda.
- **Regras do livro:** `09-documento-final/insumos/livro_regras.md`.
- **Movimentos e rubrica dos exemplares:** `09-documento-final/insumos/exemplares_movimentos.md`.
- **Revisões rápidas:** `09-documento-final/insumos/garritty_2024.md`.
- **Revisões anteriores:** `09-documento-final/insumos/revisoes_anteriores.md`. Só o que está marcado como verificado pode ser usado como conteúdo.
- **Texto atual (v1):** `09-documento-final/_esqueleto_v1_oqf.qmd`, com a versão montada em `_revisao_final_v1_oqf.qmd`, e a verificação dele em `09-documento-final/verificacao.md`.
- **Contrato de rótulos:** `09-documento-final/revista/rotulos.yml`.
- **Números prontos:** `revista/celulas.json` (enunciados e contagens das 18 células), `revista/numeros_v2.json` e `insumos/tabelas/numeros.json`.
- **Dossiês:** `insumos/contexto_brasil.md` e `insumos/mecanismos_moderadores.md`.
- **Manuscrito técnico:** `07-relatorio/relatorio.qmd`, com os métodos e resultados completos.
- **Protocolo:** `00-protocolo/protocolo.md`, `pergunta.md`, `teoria_programa.md` e `emendas.md`.
- **Pendências:** `07-relatorio/_pendencias_abertas.json` e `08-revisao-humana/README.md`.
- **Pontos de julgamento do revisor:** `08-revisao-humana/efeitos/pontos_para_o_revisor.md`.
- **Voz do autor:** `/Users/felipelmc/.claude/commands/my-voice.md`.

## O que a `spec_v2.md` deve conter
1. **Público e tom.** Uma página: quem lê, o que precisa sair sabendo, o registro (artigo de revisão em revista de ciência política) e os movimentos da rubrica que o texto tem de cumprir (códigos M01...).
2. **YAML exato do esqueleto:**
   - `title`, `subtitle` e `date` ISO;
   - `keywords`;
   - `metadata-files: [revista/_revista.yml]`;
   - `bibliography: revista/referencias.json`;
   - formatos `html` (toc à esquerda, `number-sections`), `typst` (herdado) e `docx`.
3. **Seção a seção**, na ordem do plano (Mensagens principais, Resumo executivo, Resumo, *Abstract*, 1 a 6, Informações adicionais, Referências, Apêndice A). Para cada seção:
   - o ID, pelo `rotulos.yml`;
   - o orçamento de palavras;
   - a lista **ordenada** dos parágrafos, cada um com: a função retórica, o conteúdo (afirmações com a fonte, dada como arquivo e campo ou `@chave`), os números que ele usa (só por referência ao campo de origem: `celulas.json:C03.k`, `numeros_v2.json:nao_recuperados`), o movimento (M-código ou § do livro) e os marcadores `@@FIGURA@@`/`@@TABELA@@`/quadros que entram ali;
   - os callouts "Pendente de revisão humana", com o texto de 1 ou 2 frases e os IDs exatos. São 11, com os mesmos conjuntos de IDs do v1; confira no v1.
4. **Enunciados.** Para cada célula C01...C18, em que parágrafo o enunciado literal aparece no formato `[...]{.enunciado cel="Cxx"}`, com o k e a frase de certeza no mesmo parágrafo. As mensagens principais que juntam duas células dizem "cada uma com certeza muito baixa".
5. **Mapa do v1.** Uma tabela com cada parágrafo do v1 (use o número da linha do `_esqueleto_v1_oqf.qmd`) → a seção nova ou "descartado: motivo". Nada do v1 com conteúdo verificado se perde sem motivo.
6. **O que o redator NÃO faz:**
   - análise nova;
   - número fora das fontes;
   - conclusão atribuída a revisão não verificada;
   - recomendação acima da certeza;
   - caminhos de arquivo no texto;
   - `@sec` para seção sem número;
   - `column-*`;
   - `../`;
   - "Neutro", "sem efeito", "não significativo", "benéfico" ou "danoso";
   - travessão.
7. **Decisões do autor.** A lista de pontos que o texto deve apresentar como abertos, sem resolver, cada um ligado à sua pendência.
8. **Informações adicionais.**
   - CRediT: o autor recebe só o que o log mostra (conceituação e protocolo, portões G1 e G2); a redação é de IA; os demais papéis ficam como **[A confirmar pelo autor]**.
   - Financiamento e conflitos: nenhum, por declaração do autor.
   - Registro: não registrado; protocolo congelado com sha256.
   - Dados e código, material por material, com o que é aberto e o que é fechado: o repositório é privado e a página pública traz só os produtos.
   - Declaração de IA com os agentes desta versão.
   - "Versão de trabalho de 25/09/2026; não citar como final".
   - "O que mudou desde 24/09".
9. **Resumo em linguagem simples.** A especificação do documento separado `09-documento-final/linguagem_simples.qmd`: título que é a própria mensagem, "a revisão em resumo" em até 50 palavras, perguntas como subtítulos, 600 a 750 palavras, sem citações, no presente, com a data da busca.
10. **Sentinela.** O SHA256 de `06-analise/certeza.csv`, `06-analise/swim_principal/swim_resumo.json`, `06-analise/meta_exploratoria/meta_resumo.json`, `06-analise/meta_mesmo_candidato/meta_resumo.json` e `07-relatorio/_pendencias_abertas.json`, calculado com `shasum -a 256`.

Responda com UMA linha: `OK spec_v2.md: <n> seções, <n> parágrafos especificados, <n> parágrafos do v1 mapeados (<n> descartados)`.
