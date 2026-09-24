# Correções técnicas depois da verificação (etapa 6c)

Você é programador (Python, R). Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Corrija os itens abaixo de `09-documento-final/verificacao_v2.md`. Leia cada item lá antes de corrigir. Rode Python com `python3 -B`. Não rode `rs.py`, não abra PDFs de estudos e não mexa em `_esqueleto_revisao_final.qmd` além do que o item R1 pede.

1. **V10 (forest plots).** Ordene os efeitos de cada painel por precisão, do menor ao maior erro-padrão, em `revista/figuras/preparar_dados_figuras.py`. Acrescente à legenda de `metas` em `revista/figuras/legendas.yml` a frase da correção de V10, conferindo nos arquivos de risco de viés que ela é verdadeira. Regere as figuras com `Rscript revista/figuras/gerar_figuras.R` e rode `verificar_figuras.py`.
2. **V11 (PRISMA).** Tire as caixas zeradas que não se aplicam. Separe na figura ou na legenda os 16 casos limítrofes decididos pelo autor no texto completo (8 inclusões e 8 exclusões), conferidos no `rs_log.jsonl`, só leitura, e em `00-protocolo/correcao_atribuicao.csv`. Troque o trecho da legenda pelo da correção de V11.
3. **V12 (excluídos limítrofes sem referência).**
   - Identifique os estudos excluídos citados na §3.1 do esqueleto (procure "Scheuerman", "Yosef", "Bischoff", "Hizen", "Morton 2015b", "Reveco", "Corbetta", "Kim 2018b", "Kim 2025a", "Freden 2021", "Mavridis") nos arquivos de elegibilidade (`03-textos/fichamentos_master.csv`, só as colunas de identificação e decisão, e `dados/`, só leitura).
   - Crie `09-documento-final/referencias_excluidos.bib` com metadados conferidos pelo DOI no Crossref, só título, autores, ano, veículo e DOI, sem resumos. As chaves são as internas.
   - Inclua esse `.bib` em `revista/preparar_referencias.py`, que continua sem mexer em `07-relatorio/references.bib`.
   - Crie no suplemento uma tabela "Estudos excluídos na leitura do texto completo que poderiam parecer elegíveis (PRISMA 16b)", com a citação `@chave` e o motivo (critério C1 a C6 em português). Ela entra em S4 como segunda tabela, `tbl-s4-excluidos`, gerada em `montar_suplemento.py` a partir dos arquivos.
   - No esqueleto, troque as chamadas soltas da §3.1 por `@chave` (mesma frase; só a forma de citar muda) e acrescente "(lista com referências e motivos no [S4](suplemento.html#s4-caracteristicas))".
4. **R1 (arredondamento).** Use arredondamento decimal meio para cima (`Decimal.quantize(ROUND_HALF_UP)`) em todo formatador de proporção e IC: `revista/gerar_celulas.py`, `montar_revisao_final.py`, `montar_suplemento.py`, `revista/figuras/preparar_dados_figuras.py`, `vitrine/exportar_dados.py` e, se preciso, `07-relatorio/gerar_tabelas_relatorio.py`. Assim 0,975 vira "0,98". Acrescente essa variante à lista branca de `conferir_reestruturacao.py`. No esqueleto, troque "0,00 a 0,97" por "0,00 a 0,98" nas linhas indicadas em R1, e em nenhuma outra.
5. **R7 (Emenda 3 em S3).** No tipo da Emenda 3 em `montar_suplemento.py`, use a correção de R7.

Depois rode, na ordem:
- `python3 -B 09-documento-final/revista/gerar_celulas.py` e `revista/preparar_referencias.py`;
- `revista/figuras/preparar_dados_figuras.py`, `Rscript .../gerar_figuras.R` e `verificar_figuras.py`;
- `montar_revisao_final.py`, `montar_suplemento.py` e `conferir_reestruturacao.py` (sem FALHA);
- `revista/teste_travas.sh`;
- os renders Typst do artigo e do suplemento, sem aviso.

Responda com até 12 linhas: o que mudou em cada item e o resultado das travas.
