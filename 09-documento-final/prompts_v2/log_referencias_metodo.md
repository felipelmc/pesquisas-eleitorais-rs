# Log de conferência — referências_metodo.bib

Todas as 23 entradas conferidas nesta sessão (24/09/2026). Fonte primária: API do Crossref
(`https://api.crossref.org/works/<DOI>`) para tudo que tem DOI de artigo/registro; para o resto,
página oficial, PDF oficial ou CRAN, como indicado. Nenhuma chave colide com `07-relatorio/references.bib`
nem com `09-documento-final/referencias_contexto.bib` (conferido por script).

| Chave | DOI/URL | Fonte da conferência | Campos não confirmados |
|---|---|---|---|
| Page2021PRISMA | 10.1136/bmj.n71 | Crossref | — |
| Page2021PRISMAEE | 10.1136/bmj.n160 | Crossref | — |
| Rethlefsen2021PRISMAS | 10.1186/s13643-020-01542-z | Crossref | — |
| Campbell2020SWiM | 10.1136/bmj.l6890 | Crossref | — |
| Garritty2024Rapid | 10.1136/bmj-2023-076335 | Crossref (9 autores, lista completa) | — |
| Santesso2020GRADE | 10.1016/j.jclinepi.2019.10.014 | Crossref | — |
| Murad2017GRADE | 10.1136/ebmed-2017-110668 | Crossref | Nome do periódico no Crossref é "Evidence Based Medicine" (sem hífen), não "BMJ Evidence-Based Medicine" — usei o nome do Crossref; a revista foi renomeada depois de 2017. |
| Guyatt2008GRADE | 10.1136/bmj.39489.470347.AD | Crossref | Página completa é 924–926 (o prompt citava só "924", o início) |
| Sterne2019RoB2 | 10.1136/bmj.l4898 | Crossref | — |
| Sterne2016ROBINSI | 10.1136/bmj.i4919 | Crossref | — |
| Sterne2025ROBINSIV2 | https://www.riskofbias.info/welcome/robins-i-v2 | Página oficial (via leitor de texto r.jina.ai, pois a página é renderizada em JS) | Sem publicação revisada por pares até a data de acesso — confirmado que só há documento em rascunho (PDF/editável no Google Drive), versão de 20/11/2025. Autoria "Sterne, Higgins e ROBINS-I V2 development group" seguindo a própria página ("development group... led by Jonathan Sterne and Julian Higgins") e conferida contra a citação que o livro do usuário (`felipelamarca.com/Systematic-Review`) já usa para a mesma ferramenta. Sem DOI. |
| EPOC2017RoB | https://epoc.cochrane.org/sites/epoc.cochrane.org/files/uploads/Resources-for-authors2017/suggested_risk_of_bias_criteria_for_epoc_reviews.pdf | PDF oficial da EPOC (metadados + "Suggested citation" impressa no rodapé do próprio PDF) | O metadado interno do PDF lista `/Author: Andy Oxman` (autor do arquivo Word), mas a citação sugerida oficial, impressa no documento, atribui a autoria à organização ("Cochrane Effective Practice and Organisation of Care (EPOC)"); usei a autoria institucional, que é a que consta como "Suggested citation". |
| Clopper1934IC | 10.1093/biomet/26.4.404 | Crossref | — |
| Pustejovsky2022CHE | 10.1007/s11121-021-01246-3 | Crossref (published-print 2022-04; published-online 2021-05-07) | Usei o ano de publicação impressa (2022), que bate com volume/fascículo 23(3) citados no prompt. |
| Viechtbauer2010Metafor | 10.18637/jss.v036.i03 | Crossref | Journal of Statistical Software não pagina artigos (publicação eletrônica contínua); deixei o campo `pages` de fora. |
| Pustejovsky2026ClubSandwich | https://cran.r-project.org/package=clubSandwich | Página do CRAN + `Rscript -e 'packageVersion("clubSandwich")'` no ambiente do projeto | Versão instalada confirmada: 0.7.0 (também a versão publicada no CRAN em 2026-05-04 no momento da conferência). O DOI 10.32614/CRAN.package.clubSandwich é o DOI "de conceito" do pacote no CRAN (aponta para a página geral/versão corrente, não uma versão específica). |
| Boon2021EffectDirection | 10.1002/jrsm.1458 | Crossref (published-print 2021-01, matching volume 12(1)) | — |
| Higgins2024Handbook | https://training.cochrane.org/handbook | Página oficial (via r.jina.ai) | Página lista "Senior Editors" (Higgins, Thomas) e "Associate Editors" (Chandler, Cumpston, Li, Page, Welch) sem distinguir os dois grupos no campo BibTeX `editor` (BibTeX simples não tem campo separado para editor sênior/associado); todos os 7 nomes entraram como editores. |
| CampbellCollaboration2016PLS | 10.4073/cpg.2016.2 | Crossref (sem autor pessoa física) + página arquivada via Wayback Machine (a URL atual do Crossref para o DOI devolve 404; a versão de 2019-08-02 no archive.org confirma título, autoria institucional "The Steering Group of The Campbell Collaboration" e data de publicação 2016-11-29) | Não incluí `url` no registro porque a URL atual (`campbellcollaboration.org/library/how-to-write-a-campbell-pls.html`) está fora do ar; o DOI resolve para essa mesma URL quebrada. |
| Aloe2024MECCIR | 10.1002/cl2.1445 | Crossref | Lista de autores do Crossref inclui um autor coletivo adicional, "Campbell MECCIR Working Group", incluído como último autor. Sem número de página tradicional (artigo eletrônico, `article-number` cl2.1445 usado no campo `pages`, seguindo a mesma convenção já usada nas entradas de BMJ com `elocation-id`). |
| Schaefer2025OQF | 10.31219/osf.io/aht4j_v1 | Crossref | Nome completo do terceiro autor confirmado no Crossref: "Carlos Barros Barreto Martins De Freitas" (o prompt abrevia como "Freitas"). |
| Lamarca2026Livro | https://felipelamarca.com/Systematic-Review/ | Página oficial (HTML da própria página, gerada por Quarto) | Título "Revisão sistemática de ponta a ponta" e autor "Felipe Lamarca" confirmados no `<title>` e `<meta name="author">` da página. A página não exibe ano de publicação nem aviso de direitos autorais; usei o ano do cabeçalho HTTP `Last-Modified` (2026) e documentei isso na entrada (campo `note`) por não ser uma confirmação direta no corpo da página, só no metadado de servidor. |
| Nikolakopoulos2020SignTest | 10.1002/jrsm.1427 | Crossref (published-print 2020-09, matching volume 11(5)) | Autor único (Stavros Nikolakopoulos); o prompt não citava autor, só o DOI — confirmado que o DOI resolve e traz metadados completos. |

## Contagem de campos não confirmados

A coluna "Campos não confirmados" acima registra tanto lacunas reais quanto notas de conferência (nome de periódico renomeado, ano de impressão vs. online, autor coletivo adicional etc.), para rastreabilidade completa. Das 23 entradas, só duas têm um campo que devia existir e que não pôde ser confirmado e por isso ficou de fora ou só parcialmente sustentado:

- **CampbellCollaboration2016PLS**: sem campo `url` — a URL do DOI (e a do Crossref) devolve 404; usei só o DOI, que resolve para essa mesma página quebrada.
- **Lamarca2026Livro**: o campo `year` está presente, mas não confirmado no corpo da página (que não traz data de publicação nem aviso de direitos autorais) — foi inferido do cabeçalho HTTP `Last-Modified`, e isso está anotado no campo `note` da entrada.

As demais 21 entradas têm todos os campos incluídos conferidos diretamente na fonte (Crossref, PDF oficial ou página oficial).

## Notas gerais

- Todas as maiúsculas de siglas nos títulos (PRISMA, PRISMA-S, SWiM, GRADE, RoB, ROBINS-I, MECCIR, R, metafor) foram protegidas com chaves.
- `language = {english}` foi adicionado a todas as obras em inglês; as duas obras em português (Schaefer2025OQF, Lamarca2026Livro) ficaram sem esse campo.
- Nenhum DOI, volume ou página foi inventado: onde a fonte não trazia o dado (ex.: paginação do JSS, URL utilizável da página do Campbell PLS), o campo ficou de fora, com a lacuna anotada acima.
- Nenhuma fonte proibida (Sci-Hub, LibGen, Anna's Archive, Z-Library, ResearchGate, Academia.edu, Scribd) foi usada. Duas páginas em JavaScript pesado (riskofbias.info e o Google Sites por trás dele) foram lidas via `r.jina.ai`, um leitor público de texto, não um espelho de paywall; uma página fora do ar (Campbell PLS) foi conferida via Wayback Machine, arquivo público.
