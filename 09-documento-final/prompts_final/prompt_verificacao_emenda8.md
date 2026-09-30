# Verificação independente das mudanças de 30/09/2026, noite (Emenda 8)

Você é o verificador independente do artigo final, dos apêndices, do resumo em linguagem simples e da vitrine. Você não escreveu nenhum deles. Esta rodada confere só o que mudou depois da verificação de `09-documento-final/verificacao_entrega.md`.

- **Raiz:** `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.
- **Não altere os textos.** Grave só `09-documento-final/verificacao_emenda8.md`.
- **Não faça:** abrir PDFs de estudos; rodar `rs.py`; rodar `montar_*.py`, `publicar.sh` ou qualquer script que escreva; rodar nada em segundo plano.
- **Pode rodar:** `python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd` e scripts Python seus, que só leiam; `git diff`, `git log`, `pdftotext`.

## O que mudou

Veja `git diff v3-final-2026-10-01 -- 09-documento-final/_esqueleto_revisao_final.qmd 09-documento-final/_esqueleto_suplemento.qmd 09-documento-final/linguagem_simples.qmd 09-documento-final/revista/tabelas/lacunas.yml 09-documento-final/revista/figuras/legendas.yml 09-documento-final/vitrine/conteudo/textos.yml 00-protocolo/emendas.md README.md ferramentas/pacote/LEIA.md`:

- a deduplicação decidida pelo autor foi aplicada depois da triagem (Emenda 8, em `00-protocolo/emendas.md`; declaração em `08-revisao-humana/P019_dedup/declaracao_autor_2026-09-30_dedup.md`), e o fluxo PRISMA mudou;
- a P019 fechou; ficam abertas P006, P007, P008, P033, P035, P036 e P042;
- a frase do δ (Métodos 2.7 e quadro Q1) passou a atribuir 0,044 e 0,046 à Emenda 5;
- versão e período de uso de IA passaram a 30/09/2026;
- a lista de desvios ganhou o item (xi);
- a vitrine perdeu a faixa de topo e teve textos reescritos; o README e o LEIA do pacote reescreveram o que o autor conferiu.

## Conferências

1. **Números do fluxo.** Todo número de fluxo no artigo (Resumo, *Abstract*, 2.4, 3.1, 4.4), na legenda do PRISMA, no Apêndice G, no resumo em linguagem simples, na Emenda 8, no README e na vitrine (`09-documento-final/vitrine/conteudo/textos.yml` e `docs/index.html`) bate com `07-relatorio/prisma_contagens.json` e `09-documento-final/revista/numeros_v2.json` (entradas `dedup_*`). Liste cada divergência: trecho, número no texto, número na fonte, arquivo. Confira também `docs/revisao.pdf` com `pdftotext`: nenhum "342", "526", "46 e 4", "148 e 648", "1.573", "1.054", "1.314", "787" de fluxo pode sobrar.
2. **Deduplicação.** Nenhum texto ativo (artigo, apêndices, linguagem simples, legendas, vitrine, README, LEIA do pacote, `08-revisao-humana/README.md`) pode dizer que a deduplicação foi "decidida e não aplicada" nem citar a P019 como aberta. O que se diz da regra (decisão mais inclusiva; 44 absorvidos já triados; 9 pares de versão ligados pelo autor; incluídos inalterados) bate com a Emenda 8 e com a declaração.
3. **Atribuição humana. É o ponto mais importante.** O texto só pode dizer que o autor conferiu o que as declarações dele cobrem (`08-revisao-humana/declaracao_autor_2026-09-30.md` e `P019_dedup/declaracao_autor_2026-09-30_dedup.md`). Reprove como `erro` qualquer frase, em qualquer produto, que atribua ao autor a validação do risco de viés, do GRADE ou da triagem cega, ou que diga que ele conferiu "a triagem" inteira (ele conferiu as 81 divergências). A frase da vitrine de que o risco de viés e a certeza "estão em revisão pelo autor" reflete o que ele disse nesta sessão; confira só que ela não afirma validação concluída. "RASCUNHO NÃO VALIDADO" aparece uma só vez no artigo, na declaração de IA, com as 7 pendências abertas.
4. **δ.** A frase nova é verdadeira diante de `00-protocolo/protocolo.md` (seção 8, "Limiar de relevância e magnitude") e da Emenda 5 (itens 7 e 8)? Os números 0,044, 0,046 e 0,0573 continuam iguais a `06-analise/certeza.csv` e `06-analise/_delta_celula.txt`?
5. **Datas.** Nenhum "01/10/2026" nem "2026-10-01" em texto ativo ou em `docs/` (exceto histórico: tags antigas citadas como tais). Versão e período de IA em 30/09/2026.
6. **Desvios.** A lista "onze desvios" de Informações adicionais bate com a tabela Resumo de `00-protocolo/emendas.md` e com o Apêndice B.
7. **Declaração de IA gerada do log** (`07-relatorio/declaracao_uso_ia.md`, seções 6 e 7): as anotações de pendências fechadas e a lista de juízos só de IA estão corretas diante de `rs_estado.json` e `rs_log.jsonl` (leia; não rode `rs.py`)?
8. **Travas.** Rode `conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd` e registre o resultado e a contagem de palavras do corpo (alvo 7.500 a 8.500).

## Saída

Grave `09-documento-final/verificacao_emenda8.md` com:
- um resumo do que foi checado e quanto;
- as divergências classificadas como `erro`, `aviso` ou `ok com ressalva`, cada uma com a correção em texto exato e o arquivo onde se corrige;
- os scripts usados.

Responda com UMA linha: `OK verificacao_emenda8.md: <n> erros, <n> avisos`.
