# Verificação independente: coautoria e repositório público

Você é verificador independente e não escreveu nenhum dos textos. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Grave só `09-documento-final/verificacao_coautoria.md`. Não rode `rs.py`, `montar_*.py`, `publicar.sh`, `refazer_produtos.sh` nem comandos git que escrevam. Não abra PDF de estudo. Pode ler tudo, rodar `pdftotext`/`pdfinfo` em `docs/revisao.pdf` e rodar scripts seus que só leiam.

## O fato (fonte: `08-revisao-humana/declaracao_autores_2026-09-30_coautoria.md`)

- Lucas Berti (IESP-UERJ) é coautor, com contribuição igual à de Felipe Lamarca (MAPE/IESP-UERJ), e os papéis CRediT são os mesmos.
- As conferências humanas em bloco e as decisões registradas foram dos dois, **sem dupla conferência independente**.
- O risco de viés e a certeza seguem só de IA; P006, P007, P008, P033, P035, P036 e P042 seguem abertas.
- O repositório `felipelmc/pesquisas-eleitorais-rs` passa a ser público, sem os resumos de terceiros, os lotes e pareceres de triagem e o ledger de decisões, que ficam só com os autores (disco local e repositório privado `-completo`). A pasta `publico/` traz versões sem resumos.

## Conferências

1. **Autoria.** Os dois nomes e as afiliações certas aparecem em:
   - PDF: primeira página e metadados;
   - `docs/revisao.html`, `docs/apendices.html`, `docs/linguagem-simples.html` e `docs/index.html` (texto visível e BibTeX);
   - `README.md`, `CITATION.cff` e `ferramentas/pacote/LEIA.md`;
   - as citações sugeridas.
2. **Atribuição.** Nenhum texto publicado diz "o autor" (singular) sobre conferência, decisão ou aprovação humana, nem afirma dupla conferência humana independente. Liste cada ocorrência. Os textos publicados são o artigo, os apêndices, a linguagem simples, a vitrine, o README, o LEIA do pacote, as listas de conferência em `09-documento-final/insumos/tabelas/checklist_*.md`, `lacunas.yml` e `legendas.yml`.
3. **Sem exagero.** Nada atribui aos autores a validação do risco de viés, do GRADE ou da triagem cega, nem diz que eles conferiram "a triagem" inteira.
4. **CRediT e declarações.** Informações adicionais: contribuição igual, papéis para os dois, conflito de interesses dos dois, agentes de IA fora da autoria.
5. **Acesso.**
   - Informações adicionais (iv), o README ("Licenças"), o LEIA do pacote, o Apêndice A e a Emenda 7c (nota) descrevem o repositório como público e dizem o que fica só com os autores, de modo coerente entre si e com a declaração.
   - Nenhum texto publicado diz que o repositório é privado, a não ser como histórico datado.
6. **`publico/`.** Os três CSV não têm colunas `resumo`, `trecho`, `justificativa` nem `motivo_override`, nem e-mails.
7. **Travas.** Rode `python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd` e registre o resultado.

## Saída

Em `verificacao_coautoria.md`:
- um resumo do que foi checado;
- as divergências, classificadas como `erro`, `aviso` ou `ok com ressalva`, cada uma com o trecho, a correção em texto exato e o arquivo.

Responda com UMA linha: `OK verificacao_coautoria.md: <n> erros, <n> avisos`.
