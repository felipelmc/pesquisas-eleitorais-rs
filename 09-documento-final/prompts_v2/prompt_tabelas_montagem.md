# Referências, tabelas e montagem do artigo e do suplemento (etapa 2)

Você é programador (Python 3). Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Leia antes:
- o plano: `/Users/felipelmc/.claude/plans/veja-acredito-que-na-delegated-ripple.md` (seções "Estrutura do artigo", "Figuras e tabelas" e "Etapas" 0, 2 e 8);
- `09-documento-final/revista/rotulos.yml`, `revista/_revista.yml`, `revista/celulas.json`, `revista/numeros_v2.json` e `revista/gerar_numeros_v2.py`;
- `09-documento-final/montar_revisao_final.py`, `09-documento-final/conferir_reestruturacao.py`;
- `07-relatorio/gerar_tabelas_relatorio.py` e as tabelas de `09-documento-final/insumos/tabelas/`.

Não rode `rs.py`, não abra PDFs, não rode nada em segundo plano. Não edite `_esqueleto_revisao_final.qmd` (é do redator) nem `revista/figuras/` (é de outro programador) nem `07-relatorio/references.bib`.

## Entregas

1. **`revista/preparar_referencias.py`** → `revista/referencias.json` (CSL JSON).
   - Junta `07-relatorio/references.bib`, `09-documento-final/referencias_contexto.bib` e `09-documento-final/referencias_metodo.bib` (se existir; senão, avise) com `quarto pandoc -f bibtex -t csljson`.
   - Aplica as correções:
     - `language: en` nos itens em inglês;
     - títulos em CAIXA ALTA passam a caixa de título;
     - a Lei 9.504 e a Res. TSE 23.600 viram `legislation` (autor institucional "Brasil"/"Tribunal Superior Eleitoral");
     - os PLs viram `bill`;
     - a notícia do STF segue como `webpage`.
   - Para itens com DOI sem `container-title`, `volume`, `issue` ou `page`, completa pela API do Crossref (`https://api.crossref.org/works/<doi>`), com cache em `revista/crossref_cache.json`. Só completa campos ausentes e nunca troca o que já existe.
   - Registra cada mudança em `revista/referencias_log.md`.
   - Prefixa a chave antiga com nada: as chaves continuam iguais.
2. **`revista/rotulos_autor_ano.json`:** para cada chave dos incluídos (`07-relatorio/incluidos.csv`), o rótulo de citação no texto, como o CSL `revista/american-political-science-association.csl` renderiza em pt-BR. Por exemplo, "Agranov et al. 2017" ou "Freden et al. 2024a". Para gerar, rode `quarto pandoc --citeproc --csl ... --bibliography revista/referencias.json -t plain` sobre um documento com `[@chave]` para cada chave e leia o resultado.
3. **`montar_revisao_final.py`**, estendido sem quebrar o que existe. Continua trocando linhas `@@TABELA nome@@` e passa a trocar `@@FIGURA nome@@`:
   - **FIGURA:** `![legenda](revista/figuras/saida/<nome>){#fig-... fig-alt="..."}`, a partir de `revista/figuras/legendas.yml` (pode não existir ainda; o script falha com mensagem clara). Resolve os marcadores `{arquivo:caminho}` da legenda lendo os JSON e CSV. Se `largura: larga`, envolve em `::: {.figura-larga}`. Nunca `../` no caminho.
   - **TABELA `caracteristicas` (Tab. 1):** características agregadas dos 41 estudos, a partir de `insumos/tabelas/numeros.json`: desenho, formato da exposição, realismo, região, tipo de eleição, desfechos, período e risco de viés geral por ferramenta. Duas colunas: característica e n (%).
   - **TABELA `sof` (Tab. 2):** a SoF narrativa, a partir de `celulas.json`, `06-analise/certeza.csv` e `swim_resumo.json`, com as linhas nos 4 blocos (apoio principal, viabilidade, *momentum*, comparecimento) como linhas-cabeçalho em negrito. Colunas:
     - Comparação e desenho: rótulos em português, sem códigos.
     - Estudos: citação `@chave` com o n do efeito principal e a unidade.
     - Direção: x a favor de y com direção definida, rótulo por `dir_rot`, proporção e IC de Clopper-Pearson.
     - Certeza: `[⊕◯◯◯]{.grade} muito baixa`, e assim por diante.
     - O que a evidência diz: `[<enunciado literal>]{.enunciado cel="Cxx"}`.
     - Notas: letras (a, b, c...) que remetem a uma nota de rodapé da tabela explicando cada rebaixamento, pela `rebaix()`.

     A legenda explica ⊕, a regra do x de y, que a certeza qualifica a direção e que o agrupamento amplo *post hoc* ficou fora (suplemento S8). A tabela vai envolvida em `::: {.landscape}` no nível de cima.
   - **TABELA `hipoteses` (Tab. 3):** hipóteses e elos do protocolo (`00-protocolo/teoria_programa.md`: tabela por elo E1–E8 e teorias rivais) × o que a evidência diz (quadro 2.10 de `insumos/mecanismos_moderadores.md`, sem as marcas `[C: n]`) × certeza. A certeza só aparece quando a hipótese coincide com uma célula de `celulas.json`; nas outras linhas, "sem GRADE (descritivo)", e com menos de 4 estudos por nível, "sem teste formal". O texto das células fica em `revista/tabelas/hipoteses.yml`, com a fonte de cada linha, para que o passe de estilo possa editá-lo. Dentro de `::: {.tabela-larga}`.
   - **TABELA `oqf_principal` (Tab. 4):** refatore `t_oqf_principal`. A prosa vai para `revista/tabelas/oqf_principal.yml`, sem caminhos de arquivo: a coluna "Evidência" aponta para seções (`@sec-...`) e para o suplemento em texto. Os números continuam lidos dos arquivos.
   - **TABELA `transferibilidade` (Tab. 5):** os 4 fatores de transferibilidade do protocolo (`00-protocolo/protocolo.md`, procure "transferibilidade": voto obrigatório, dois turnos, regulação da divulgação, confiança nas pesquisas) × como o Brasil é (de `insumos/contexto_brasil.md`, só itens confirmados) × quantos estudos incluídos têm a condição (calcule em `gerar_numeros_v2.py`, a partir de `insumos/tabelas/caracteristicas.md` ou dos arquivos de extração permitidos; documente a fórmula) × o que se pode dizer. Sem juízo de preocupação. Texto em `revista/tabelas/transferibilidade.yml`.
   - **TABELA `pendencias`:** a atual, com a legenda sem caminhos de arquivo.
   - **Metadados:** o script escreve no YAML do `revisao_final.qmd` montado as chaves `pendencias-abertas: <n>` (de `_pendencias_abertas.json`) e `rascunho: true` se n > 0. Não mexa no YAML do esqueleto.
   - **Checagem:** sai com erro se sobrar `@@`, se uma figura não existir em `revista/figuras/saida/` ou se um rótulo não estiver em `rotulos.yml`.
4. **`montar_suplemento.py` e `_esqueleto_suplemento.qmd`:**
   - `_esqueleto_suplemento.qmd`: YAML com `title: "Material suplementar"`, o mesmo `metadata-files: [revista/_revista.yml]` e `bibliography: revista/referencias.json`. Seções S1 a S11, com os IDs de `rotulos.yml`, cada uma com 1 ou 2 frases de introdução e um marcador `@@TABELA ...@@`.
   - `montar_suplemento.py` → `suplemento.qmd`, com estas fontes:
     - S1: strings de busca de `07-relatorio/relatorio.qmd` ou `01-busca/`;
     - S2: marcador que usa `insumos/garritty_2024.md` se existir; senão, "em preparação";
     - S3: emendas de `00-protocolo/emendas.md`, uma linha por emenda, com a data e se foi decidida antes ou depois de ver os dados;
     - S4: `insumos/tabelas/caracteristicas.md`;
     - S5: `insumos/tabelas/rob2.md`, `robins.md` e `epoc.md`, com o EPOC recodificado em B/A/I/n.a. e legenda;
     - S6: `individuais.md`;
     - S7: `fora.md`;
     - S8: `sens.md` mais o SoF do agrupamento amplo;
     - S9: `insumos/caixa_oqf_celulas.md` e `caixa_oqf_painel.md`;
     - S10: `regional.md` e `viabilidade.md`;
     - S11: "em preparação" (os checklists serão feitos depois do texto).
   - Tabelas largas em `::: {.tabela-larga}` ou `::: {.landscape}` no nível de cima.
   - Nada de "—" (troque por "n.a."). Nada de `../`.
5. **Teste:** rode `preparar_referencias.py`, gere `rotulos_autor_ano.json`, rode `montar_suplemento.py` e renderize o suplemento em Typst:

   ```
   cd 09-documento-final && TYPST_IGNORE_SYSTEM_FONTS=true TYPST_IGNORE_EMBEDDED_FONTS=true quarto render suplemento.qmd --to typst
   ```

   Esse render é permitido, só nesse arquivo. Corrija até compilar sem erro. O artigo em si ainda não tem texto novo: teste as funções de tabela chamando-as isoladamente e gravando cada saída em `revista/tabelas/previa_<nome>.md`.

Responda com até 25 linhas: entregas, contagem de entradas completadas pelo Crossref, rótulos gerados, páginas do `suplemento.pdf` e problemas encontrados.
