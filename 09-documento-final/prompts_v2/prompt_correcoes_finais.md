# Correções finais: verificação final e revisão visual (etapa 8b)

Você é programador e redator. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Rode Python com `python3 -B`. Não rode `rs.py`, não abra PDFs de estudos e não mexa no template Typst (`revista/typst-template.typ`) nem em `revista/inline.lua`, que o coordenador já corrigiu.

## O que corrigir
1. **`09-documento-final/verificacao_final.md`:** o erro E1, os avisos V1 a V5 e a ressalva sobre "efeito médio" (R11) que voltou no §1.2. Use as correções em texto exato que o arquivo propõe, ou justifique em `09-documento-final/resposta_pareceres.md`, numa seção nova "Verificação final", quando não aplicar.
2. **`09-documento-final/_qa/qa_visual_artigo.md`**, itens "a corrigir":
   - **7:** linhas de grupo das Tabelas 1 e 2 com `colspan`. No Markdown pipe não dá; use o recurso que funcionar no Typst e no HTML, por exemplo uma linha com o texto só na primeira célula e as demais vazias, com a primeira célula larga, ou uma tabela Typst crua só no formato Typst. Documente a escolha.
   - **8:** notas da Tabela 2 dentro da tabela, em sans, e mais compactas, para não sobrar uma página deitada quase vazia.
   - **9:** *bandwagon* e *momentum* em itálico dentro dos enunciados. O texto dos spans `.enunciado` tem de continuar idêntico ao de `celulas.json` depois do `stringify`. Confira que `conferir_reestruturacao.py` compara pelo `stringify`; se não comparar, ajuste a trava para ignorar a ênfase, sem afrouxar a comparação de palavras.
   - **10:** o n fora do colchete da citação na coluna Estudos da Tabela 2, sempre no mesmo formato.
   - **15:** chave de cor da Figura 4.
   - **16:** Araujo2021a com o sufixo certo nas figuras. Refaça `revista/gerar_rotulos_autor_ano.py` para seguir o sufixo do citeproc e regere as figuras.
   - **17:** citações entre parênteses aninhados; troque por `[@chave]` ou por "(Autor ano)" no esqueleto e nos geradores das Tabelas 2, 3 e 4.
   - **18:** datas de acesso 2026-09-24. Corrija na fonte (`.bib` de método) e depois rode `revista/preparar_referencias.py`.
3. **Aceitáveis que valem o esforço:**
   - 4: corpo mínimo de 7 pt nas figuras (`tema_revista.R`);
   - 5: letras de painel alinhadas;
   - 6: quebra fixa entre os símbolos ⊕ e a palavra da certeza nas células;
   - 7: espaço não separável em "p = …";
   - 8: ordem de Araujo 2021a/b na bibliografia, dando o mês de publicação às duas entradas;
   - 11: "*survey*" em itálico no nó da Figura 1, se o ggplot permitir.

## Travas
Depois de tudo, rode:
- `revista/figuras/preparar_dados_figuras.py`, `Rscript revista/figuras/gerar_figuras.R` e `verificar_figuras.py`;
- `montar_revisao_final.py` e `montar_suplemento.py`;
- `conferir_reestruturacao.py` (0 FALHA);
- `revista/teste_travas.sh`;
- os renders Typst do artigo e do suplemento, com `TYPST_IGNORE_SYSTEM_FONTS=true TYPST_IGNORE_EMBEDDED_FONTS=true`, sem aviso;
- `revista/verificar_pdf.py` nos dois PDFs (OK).

Nos arquivos de texto que já passaram pelos passes de estilo, as mudanças se limitam ao que os itens pedem.

Responda com até 12 linhas: item por item, feito ou justificado, e o resultado das travas.
