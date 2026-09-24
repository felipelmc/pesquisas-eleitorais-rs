# Referências metodológicas verificadas (etapa 0)

Você cria `09-documento-final/referencias_metodo.bib`, com as referências metodológicas que o artigo final vai citar. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Escreva só esse arquivo e `09-documento-final/prompts_v2/log_referencias_metodo.md`.

## Regras
- Cada entrada precisa de metadados conferidos na fonte: API do Crossref (`https://api.crossref.org/works/<DOI>`), página da editora ou PubMed. Não invente DOI, volume ou página. Se não confirmar um campo, deixe-o de fora e anote no log.
- Nada de Sci-Hub, LibGen, Anna's Archive, Z-Library, ResearchGate, Academia.edu ou Scribd.
- As chaves seguem o padrão `SobrenomeAnoMetodo` (ex.: `Page2021PRISMA`). Confira que nenhuma chave colide com `07-relatorio/references.bib` nem com `09-documento-final/referencias_contexto.bib`.
- Títulos com as maiúsculas protegidas por chaves (`{PRISMA}`, `{GRADE}`) e `language = {english}` nas obras em inglês.

## Obras (com a razão de cada uma)
1. PRISMA 2020 (Page et al. 2021, BMJ 372:n71) e a explicação e elaboração (Page et al. 2021, BMJ 372:n160).
2. PRISMA-S (Rethlefsen et al. 2021, Systematic Reviews 10:39).
3. SWiM (Campbell M et al. 2020, BMJ 368:l6890).
4. Garritty C et al. 2024, BMJ 384:e076335 (recomendações atualizadas para revisões rápidas da Cochrane).
5. GRADE: Santesso N et al. 2020, J Clin Epidemiol 119:126-135 (GRADE guidelines 26, frases informativas); Murad MH et al. 2017, BMJ Evidence-Based Medicine 22(3):85-87 (certeza sem estimativa única); Guyatt GH et al. 2008 BMJ 336:924 (GRADE: an emerging consensus).
6. RoB 2 (Sterne JAC et al. 2019, BMJ 366:l4898). ROBINS-I (Sterne JAC et al. 2016, BMJ 355:i4919). ROBINS-I V2: confira se há publicação citável (Sterne et al. 2024/2025, site riskofbias.info); se só houver o site, crie `@misc` com URL e data de acesso 25/09/2026.
7. EPOC: critérios de risco de viés do Cochrane EPOC (Suggested risk of bias criteria for EPOC reviews, 2017), como `@misc` com URL oficial.
8. Clopper CJ, Pearson ES 1934, Biometrika 26(4):404-413.
9. Dependência entre efeitos: Pustejovsky JE, Tipton E 2022, Prevention Science 23:425-438 (CHE); Viechtbauer W 2010, J Stat Softw 36(3) (metafor); Pustejovsky JE, clubSandwich (pacote R, CRAN, versão instalada: rode `Rscript -e 'cat(as.character(packageVersion("clubSandwich")))'`).
10. Boon MH, Thomson H 2021, Research Synthesis Methods 12(1):29-33 (effect direction plot).
11. Cochrane Handbook for Systematic Reviews of Interventions, versão 6.5 (2024) ou a atual, como `@book` com editores e URL.
12. Campbell: orientação de resumos em linguagem simples (Campbell Collaboration 2016, Campbell Policies and Guidelines Series n. 2, DOI 10.4073/cpg.2016.2); Campbell Standards (MECCIR/Campbell standards 2024) se houver DOI.
13. OQF: Schaefer, Borges & Freitas 2025, preprint OSF, DOI 10.31219/osf.io/aht4j_v1 (confira título e autores completos).
14. O livro: Lamarca, Felipe. *Revisão sistemática de ponta a ponta*. <https://felipelamarca.com/Systematic-Review/>, como `@book` ou `@online` com ano e data de acesso 25/09/2026 (confira título e ano na própria página).
15. A crítica ao uso do teste de sinal em revisões (Research Synthesis Methods, DOI 10.1002/jrsm.1427): confira autores, título e ano no Crossref e inclua só se o DOI resolver.

## Saída
- `09-documento-final/referencias_metodo.bib`.
- `09-documento-final/prompts_v2/log_referencias_metodo.md`: tabela chave | DOI/URL | fonte da conferência | campos não confirmados.
Responda com UMA linha: `OK referencias_metodo.bib: <n> entradas, <n> com campo não confirmado`.
