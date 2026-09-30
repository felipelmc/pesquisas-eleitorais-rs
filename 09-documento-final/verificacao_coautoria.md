# Verificação independente: coautoria e repositório público (30/09/2026)

Verificador independente de IA (claude-opus-5-5), sem autoria de nenhum dos textos. Prompt: `09-documento-final/prompts_final/prompt_verificacao_coautoria.md`. Fonte do fato: `08-revisao-humana/declaracao_autores_2026-09-30_coautoria.md`.

Não rodei `rs.py`, `montar_*.py`, `publicar.sh` nem `refazer_produtos.sh`, e não fiz nenhum comando git que escreva. Não abri PDF de estudo. Li `docs/revisao.pdf` com `pdftotext` e `pdfinfo`, o texto visível e os dados embutidos dos quatro HTML de `docs/`, e o conteúdo de `docs/pacote-replicacao.zip`, extraído no *scratchpad*. Li também as fontes e usei *scripts* só de leitura.

**Resultado: 6 erros e 8 avisos.** Todos são de texto ou de empacotamento. Nenhum toca número, célula ou certeza.

## Resumo do que foi checado

| # | Conferência | Resultado |
|---|---|---|
| 1 | Autoria | O PDF está certo: na p. 1 aparece "Felipe Lamarca · MAPE/IESP-UERJ; Lucas Berti · IESP-UERJ"; nos metadados, `Author: Felipe Lamarca & Lucas Berti`; o cabeçalho "Lamarca e Berti · …" está em 49 das 50 páginas. `revisao.html` e `apendices.html` trazem o bloco "Autores / Afiliações" certo e `<meta name="author">` para os dois. Em `index.html`, a autoria visível, o "Como citar" e o BibTeX (`author = {Lamarca, Felipe and Berti, Lucas}`) estão certos. `README.md`, `CITATION.cff`, o `LEIA.md` e o "Como citar" do artigo estão certos. **`linguagem-simples.html` não tem nenhum nome** (E1). O pacote não leva a declaração de coautoria (E2). |
| 2 | Atribuição | No PDF, nos HTML, nas listas de conferência, em `lacunas.yml` e em `legendas.yml`, "autor" no singular aparece uma única vez em texto publicado, na tabela de emendas do Apêndice B (E3). Há um verbo no singular com sujeito "os autores" (A1). Nenhum texto afirma dupla conferência humana independente: toda menção diz "sem dupla independente" ou "juntos, em bloco". |
| 3 | Sem exagero | Nada atribui aos autores a validação do risco de viés, do GRADE ou da triagem cega. Nada diz que conferiram "a triagem" inteira: os textos falam em "partes da busca, da seleção e da extração" ou dão a lista. Ressalva: README, LEIA e vitrine dizem que o risco de viés e o GRADE estão "em revisão" pelos autores, o que nenhuma declaração registra (A2). |
| 4 | CRediT e declarações | Tudo certo. "Felipe Lamarca e Lucas Berti contribuíram igualmente. Os dois: …" traz os 13 papéis, e a obtenção de financiamento não se aplica. "Os autores declaram não ter conflito de interesses nem relação com a Anthropic". "Agentes de IA executaram, sob supervisão dos autores, parte dessas tarefas […] e não são autores." |
| 5 | Acesso | Informações adicionais (iv), README ("Licenças"), LEIA, Apêndice A e a nota da Emenda 7c descrevem o repositório como público. Três listas de conferência ainda chamam de privados os *prompts*, as fichas, o *log* e as sementes (E4 a E6). Há incoerências menores sobre o que fica só com os autores (A3 a A7). |
| 6 | `publico/` | Tudo certo. `decisoes_sem_trechos.csv` (6.511 linhas, 12 colunas), `dedup_revisao_v1_sem_resumos.csv` (145 linhas, 25 colunas) e `registros_unicos_sem_resumo.csv` (4.576 linhas, 20 colunas, os mesmos `id_rs` do original) não têm colunas `resumo*`, `trecho*`, `justificativa*` nem `motivo_override`, nem nenhum e-mail. `mapa_commits_reescrita.csv` também está limpo. |
| 7 | Travas | `PYTHONDONTWRITEBYTECODE=1 python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd` deu `RESULTADO: OK (0 falha(s), 0 aviso(s))`: datas, 1.471 números, 18 células, estrutura, citações, proibições e relato, em modo final. O corpo tem **8.496 palavras**, 4 abaixo do teto de 8.500. Nenhuma correção abaixo acrescenta palavras entre a Introdução e as Conclusões. |

Também conferi que `docs/pacote-replicacao.zip` leva o mesmo `revisao.pdf` de `docs/` (md5 igual) e as mesmas listas de conferência de `09-documento-final/insumos/tabelas/`, e que o `LEIA.md` e o `CITATION.cff` do pacote são idênticos aos do repositório.

## Divergências

### Erros

**E1. O resumo em linguagem simples não tem autores** (conferência 1)
- Onde: `docs/linguagem-simples.html`, que vem de `09-documento-final/linguagem_simples.qmd`.
- Trecho: o bloco de título mostra só o título e "Data de Publicação 30/09/2026". Nenhum dos dois nomes aparece na página.
- Correção: acrescentar ao YAML de `09-documento-final/linguagem_simples.qmd`, logo depois de `date-format: "DD/MM/YYYY"`, o bloco abaixo e publicar de novo.
  ```yaml
  author:
    - name: Felipe Lamarca
      affiliations:
        - name: MAPE/IESP-UERJ
    - name: Lucas Berti
      affiliations:
        - name: IESP-UERJ
  ```

**E2. O pacote de replicação não leva a declaração de coautoria** (conferências 1 e 5)
- Onde: `ferramentas/montar_pacote.py`, linhas 96 e 97; `docs/pacote-replicacao.zip`.
- Trecho: o zip tem `08-revisao-humana/declaracao_autor_2026-09-30.md` e `P019_dedup/declaracao_autor_2026-09-30_dedup.md`, mas não `declaracao_autores_2026-09-30_coautoria.md` (`unzip -l … | grep -c coautoria` dá 0). Mesmo assim, quatro arquivos do pacote citam esse arquivo:
  - o `LEIA.md` ("`declaracao_autores_2026-09-30_coautoria.md`" e, na tabela, "declarações dos autores (conferência em bloco, deduplicação e coautoria)");
  - `00-protocolo/emendas.md` (notas da 7c e da Emenda 8);
  - as duas declarações do autor.

  O artigo diz, em (ii), que o pacote traz "a declaração dos autores".
- Correção: em `ferramentas/montar_pacote.py`, logo depois de `"08-revisao-humana/declaracao_autor_2026-09-30.md",`, acrescentar `"08-revisao-humana/declaracao_autores_2026-09-30_coautoria.md",` e publicar de novo.

**E3. "Conferência do autor" na tabela de emendas do Apêndice B** (conferência 2)
- Onde: PDF, Apêndice B (tabela de emendas, linha da Emenda 7), e `docs/apendices.html`. A linha é gerada por `09-documento-final/montar_suplemento.py`, `s3_emendas()`, que lê o título da Emenda 7 em `00-protocolo/emendas.md`, linha 162.
- Trecho: "Emenda 7 | 30/09/2026 | conferência do autor, etapas sem validação humana e versão de entrega".
- Correção: o título em `emendas.md` é registro datado e tem a nota de coautoria no fim, então é melhor não mexer nele. Em `montar_suplemento.py`, `s3_emendas()`, logo depois do bloco `if idd == "Emenda 3": …`, acrescentar as linhas abaixo e publicar de novo.
  ```python
          if idd == "Emenda 7":  # o título histórico diz "do autor"; as conferências foram dos dois autores (coautoria)
              objeto = "conferência dos autores, etapas sem validação humana e versão de entrega"
  ```

**E4. A lista PRISMA 2020 (item 27) diz que *prompts*, fichas e *log* são privados** (conferência 5)
- Onde: `09-documento-final/insumos/tabelas/checklist_prisma2020.md`, linha 44, e a cópia em `pacote-replicacao/tabelas-extras/`.
- Trecho: "O texto diz o que é público (pacote de replicação, com licenças MIT e CC BY 4.0) e o que é privado (*prompts*, fichas com trechos e *log* completo, sob pedido). Não há identificador persistente."
- Correção: "O texto diz o que é público (pacote de replicação, com licenças MIT e CC BY 4.0, e o repositório do projeto, com *prompts*, fichas com trechos e *log* completo) e o que fica só com os autores (textos completos, resumos de terceiros e pareceres dos triadores de IA). Não há identificador persistente."

**E5. A lista PRISMA-S (item 5) põe as sementes num repositório privado** (conferência 5)
- Onde: `09-documento-final/insumos/tabelas/checklist_prisma_s.md`, linha 7, e a cópia no pacote. Contradiz o Apêndice A ("As sementes da busca por citação ficam no repositório público do projeto") e o Git, onde `01-busca/bola_de_neve/SN*_sementes.csv` está versionado.
- Trecho: "as sementes ficam no repositório privado do projeto."
- Correção: "as sementes ficam no repositório público do projeto."

**E6. A lista PRISMA-trAIce (M6) põe os *prompts* num repositório privado** (conferência 5)
- Onde: `09-documento-final/insumos/tabelas/checklist_trAIce.md`, linha 11, e a cópia no pacote.
- Trecho: "Os *prompts* ficam no repositório privado, com acesso sob pedido; estrutura, parâmetros e refinamento não são relatados, e só um erro no *prompt* do árbitro é mencionado."
- Correção: "Os *prompts* ficam no repositório público do projeto; estrutura, parâmetros e refinamento não são relatados, e só um erro no *prompt* do árbitro é mencionado."

### Avisos

**A1. Verbo no singular com sujeito "os autores"** (conferência 2)
- Onde: `09-documento-final/revista/tabelas/lacunas.yml`, linhas 43 a 45 (Tabela G1, linha "Deduplicação"), e daí o PDF e `apendices.html`.
- Trecho: "Em bloco pelos autores: concordou com as sugestões da IA nos 145 pares (fundir, rejeitar ou ligar), aplicadas depois da triagem, com a decisão mais inclusiva nos 44 registros já triados; nos 9 pares de versão, ligados por eles como a IA sugeriu (Emenda 8). Os estudos incluídos não mudaram".
- Correção: "Em bloco pelos autores: concordância com as sugestões da IA nos 145 pares (fundir, rejeitar ou ligar), aplicadas depois da triagem, com a decisão mais inclusiva nos 44 registros já triados; os 9 pares de versão foram ligados por eles, como a IA sugeriu (Emenda 8). Os estudos incluídos não mudaram".

**A2. "Em revisão pelos autores": o risco de viés e o GRADE** (conferência 3)
- Onde:
  - `README.md`, linha 25: "o risco de viés e a certeza da evidência, julgados por IA e hoje em revisão pelos autores;";
  - `ferramentas/pacote/LEIA.md`, linha 26: "Os autores estão revendo o risco de viés e o GRADE.";
  - `09-documento-final/vitrine/conteudo/textos.yml`, linhas 168 e 169 (e `docs/index.html`): "o risco de viés e a certeza, julgados por IA, estão em revisão pelos autores".
- Problema: não afirma validação, mas nenhuma declaração transcrita registra essa revisão em andamento. Em `declaracao_autor_2026-09-30.md`, o registro é outro: "para uma eventual evolução do projeto, será necessário incluir humanos". A declaração de coautoria diz só que essas etapas "seguem julgados só por IA".
- Correção: se os autores confirmarem que estão revendo, acrescentar esse fato à declaração de coautoria. Se não, usar os textos abaixo.
  - README: "- o risco de viés e a certeza da evidência, julgados só por IA;"
  - LEIA: apagar a frase "Os autores estão revendo o risco de viés e o GRADE."
  - Vitrine: "As que seguem abaixo continuam abertas: o risco de viés e a certeza foram julgados só por IA, e a triagem não teve validação cega."

**A3. Informações adicionais (iv): textos completos "com acesso sob pedido" e o *ledger* de fora** (conferência 5)
- Onde: `09-documento-final/_esqueleto_revisao_final.qmd`, linha 422, e daí o PDF e `revisao.html`.
- Problema:
  - (iv) põe os textos completos entre o que se dá "com acesso sob pedido", mas (iii), no mesmo parágrafo, diz que eles "não são redistribuídos", e o LEIA diz que os PDFs "não podem ser redistribuídos".
  - O registro de decisões (*ledger*, `dados/decisoes.jsonl`), que a declaração lista entre o que saiu do Git público, não aparece.
- Trecho: "Ficam só com os autores, com acesso sob pedido, os textos completos, os resumos de terceiros (exportações das buscas, registros e lotes de triagem) e os pareceres dos triadores de IA, que citam trechos dos resumos."
- Correção: "Ficam só com os autores os textos completos, que não são redistribuídos, e, com acesso sob pedido, os resumos de terceiros (exportações das buscas, registros e lotes de triagem), os pareceres dos triadores de IA e o registro de decisões da triagem, que citam trechos dos resumos; a pasta publico/ do repositório traz versões deles sem resumos e sem trechos."
  - A frase fica nas Informações adicionais, fora da contagem de palavras do corpo.

**A4. README ("Licenças"): os PDFs aparecem como se estivessem no repositório privado** (conferência 5)
- Onde: `README.md`, seção "Licenças".
- Problema: os PDFs nunca entram no Git. `ferramentas/arquivar_privado.sh` diz "Os PDFs não vão".
- Trecho: "Os PDFs de terceiros, os resumos de terceiros (exportações das buscas, registros com resumo, lotes, filas e amostras de triagem) e os pareceres dos triadores de IA, que citam trechos dos resumos, ficam só no disco local dos autores, fora do Git, e num repositório privado com o histórico completo, com acesso sob pedido aos autores."
- Correção: "Os PDFs de terceiros ficam só no disco local dos autores, fora do Git, e não são redistribuídos. Os resumos de terceiros (exportações das buscas, registros com resumo, lotes, filas e amostras de triagem), os pareceres dos triadores de IA e o registro de decisões, que citam trechos dos resumos, ficam no disco local dos autores e num repositório privado com o histórico completo, com acesso sob pedido aos autores."

**A5. LEIA: "a triagem registro a registro" fica só com os autores** (conferência 5)
- Onde: `ferramentas/pacote/LEIA.md`, item "**Fica fora do pacote**".
- Problema: o próprio pacote traz a decisão final de cada registro (`02-triagem/`). O repositório público traz cada decisão de triagem sem os trechos (`publico/decisoes_sem_trechos.csv`). A frase também dá a entender que fichas, *prompts* e *log* ficam fora "por conter resumos de terceiros".
- Trecho: "**Fica fora do pacote**, por conter resumos de terceiros: a triagem registro a registro (lotes, pareceres dos triadores de IA), e também as fichas em Markdown, os *prompts* e o *log* bruto. As fichas, os *prompts* e o *log* estão no repositório público do projeto (<https://github.com/felipelmc/pesquisas-eleitorais-rs>); a triagem registro a registro e os resumos de terceiros ficam só com os autores, com acesso sob pedido."
- Correção: "**Fica fora do pacote**: os lotes de triagem e os pareceres dos triadores de IA, que citam trechos dos resumos de terceiros, e também as fichas em Markdown, os *prompts* e o *log* bruto. As fichas, os *prompts*, o *log* e as decisões de triagem registro a registro sem os trechos (`publico/decisoes_sem_trechos.csv`) estão no repositório público do projeto (<https://github.com/felipelmc/pesquisas-eleitorais-rs>). Os resumos de terceiros, os lotes, os pareceres e o registro de decisões com trechos ficam só com os autores, com acesso sob pedido."

**A6. O Apêndice A não diz o que fica só com os autores** (conferência 5)
- Onde: `09-documento-final/_esqueleto_suplemento.qmd`, linha 24, e daí o PDF e `apendices.html`.
- Problema: o prompt pede que o Apêndice A diga o que fica só com os autores, e ele cita só as sementes (públicas). As exportações brutas das buscas (`01-busca/brutos/`) saíram do Git.
- Trecho: "As sementes da busca por citação ficam no repositório público do projeto, e o pacote de replicação leva só as estratégias ativas, o registro das buscas e os *codebooks*."
- Correção: "As sementes da busca por citação ficam no repositório público do projeto; as exportações brutas das buscas, que trazem resumos de terceiros, ficam só com os autores. O pacote de replicação leva só as estratégias ativas, o registro das buscas e os *codebooks*."

**A7. PRISMA-trAIce (M2): a ferramenta de revisão aparece como "não pública"** (conferência 5)
- Onde: `09-documento-final/insumos/tabelas/checklist_trAIce.md`, linha 7, e a cópia no pacote.
- Problema: o artigo, em (ii), diz que o pacote traz "uma cópia da ferramenta de revisão", e o pacote tem `skill-revisao-sistematica/`.
- Trecho: "a ferramenta de revisão que coordena os agentes não é pública nem descrita em detalhe."
- Correção: "os *scripts* da ferramenta de revisão que coordena os agentes estão no pacote de replicação, mas a ferramenta não é descrita em detalhe."

**A8. As licenças dão o *copyright* só a Felipe Lamarca** (autoria)
- Onde:
  - `LICENSE`, linha 3: "Copyright (c) 2026 Felipe Lamarca";
  - `LICENSE-CC-BY-4.0.md`, linha 3: "Copyright (c) 2026 Felipe Lamarca.", e o título "## O que não é do autor e mantém os termos de origem".
  - As cópias no pacote têm o mesmo texto.
- Problema: não está na lista do prompt, mas contradiz a coautoria com contribuição igual. Os titulares são decisão dos autores.
- Correção, se os dois forem titulares:
  - `LICENSE`: "Copyright (c) 2026 Felipe Lamarca and Lucas Berti";
  - `LICENSE-CC-BY-4.0.md`: "Copyright (c) 2026 Felipe Lamarca e Lucas Berti." e "## O que não é dos autores e mantém os termos de origem".
  - A licença da cópia da *skill* ("licença do autor da skill") fica como está.

### Ok com ressalva

- **Comentários de `lacunas.yml`** (linhas 6, 11 e 12). Dizem "declaração do autor", "o autor aprovou" e "Se o autor não aprovar". São comentários YAML e não aparecem nos produtos. Se quiser trocar, use "os autores aprovaram" e "Se os autores não aprovarem".
- **Emenda 7 (7a, 7b e 7c) e declarações transcritas.** Mantêm "o autor" e "O repositório continua privado" como registro datado, com notas de 30/09/2026 (coautoria e abertura), como pede a declaração. A nota da 7c lista "os resumos de terceiros, os lotes e os pareceres de triagem" e não cita o registro de decisões. Para alinhar com A3 e A4, basta acrescentar ", e o registro de decisões". A declaração do autor diz "Todos os papéis CRediT humanos são do autor". Isso é transcrição datada, com a nota de coautoria no topo.
- **Seção 2.9.** A lista (i) a (vii) do que os autores reviram não inclui as decisões de deduplicação, que a declaração de coautoria cita. Elas estão na seção 2.4, na legenda da Figura 2 e no Apêndice G. Não acrescente nada ali: o corpo está em 8.496 palavras.
- **Citações sugeridas.** A da vitrine termina com "IESP-UERJ." (texto e BibTeX `note`); a do artigo e a do README, não. Os dois nomes estão certos em todas.
- **Vitrine, dado embutido.** `docs/index.html` traz `"commit":"5716d07"`, *hash* anterior à reescrita do histórico (hoje `881437c`, pelo `publico/mapa_commits_reescrita.csv`). O campo não aparece na página, porque o rodapé cita a tag, e se corrige na próxima montagem.
- **Arquivos de trabalho versionados no repositório público** (fora da lista do prompt). A linha 9 de `CLAUDE.md` diz "O repositório segue privado", o que contradiz a linha 47 ("**público** desde 30/09/2026"), e fala de "O autor". A linha 17 de `REPRODUZIR.md` diz "declaração do autor (30/09/2026)". Convém atualizar.
- **`publico/`.** `motivo_ia` em `dedup_revisao_v1_sem_resumos.csv` fala de resumos ("resumo idêntico", "resumo quase idêntico") sem transcrevê-los. Em `decisoes_sem_trechos.csv`, 336 linhas de `ia_coordenador_emenda6` têm `tipo_ator = humano`: é a armadilha conhecida do `triagem override`, declarada na Emenda 6b e nas limitações do artigo.
- **Página de entrada (`index.html`).** Não tem `<meta name="author">`. A autoria visível e o BibTeX estão certos, como pede o prompt.
