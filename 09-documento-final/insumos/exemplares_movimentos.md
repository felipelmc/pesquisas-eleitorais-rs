# Movimentos de revisões exemplares (etapa 0b)

Insumo para a reescrita do artigo final da revisão sobre exposição a pesquisas eleitorais publicadas, voto (*bandwagon* × *underdog*) e comparecimento. Reúne sete textos exemplares, o que cada um faz na escrita e no relato, e fecha com uma rubrica de 15 movimentos (M01 a M15) para conferir o texto novo.

Gerado em 24/09/2026 por subagente (Opus), a partir de `09-documento-final/prompts_v2/prompt_exemplares.md`.

## Como os textos foram lidos

- Só fontes abertas e legítimas. Nada de Sci-Hub, LibGen, Anna's Archive, Z-Library, ResearchGate, Academia.edu ou Scribd, e nenhum *paywall* ou bloqueio foi contornado.
- E1 a E5: HTML aberto do PubMed Central, lido com WebFetch. Para conferir as citações literais, o mesmo HTML foi convertido em texto na pasta temporária da sessão.
- E6 e E7: a página da Cambridge Core respondeu HTTP 429 ao WebFetch em todas as tentativas, e isso não foi contornado. Usei as versões abertas indicadas no prompt. Para E6, a versão aceita dos autores (26/07/2017) no eScholarship, repositório institucional da Universidade da Califórnia. Para E7, a versão publicada (licença CC BY 4.0) na página de Alexander Coppock. As duas foram lidas com WebFetch. A ferramenta guardou uma cópia temporária do PDF fora do projeto, apagada ao fim do trabalho. Nenhum PDF foi salvo no projeto.
- Todas as citações abaixo são literais, em inglês, e foram conferidas contra o texto-fonte. Diferenças de hifenização e espaçamento foram ignoradas. As chamadas numéricas de referência (sobrescritos) ficaram de fora das citações. Em E6, a redação pode diferir em detalhes da versão diagramada da APSR, porque a fonte é a versão aceita.
- E1 é uma diretriz de relato, não uma revisão. Os "movimentos" dele são prescrições, e o que interessa aqui é o que ele manda fazer.

Siglas usadas na rubrica: E1 Campbell et al. 2020 (SWiM); E2 Burns et al. 2019 (Cochrane); E3 Fisher et al. 2023 (Campbell); E4 Lorenz-Spreen et al. 2023; E5 Pfänder e Altay 2025; E6 Kalla e Broockman 2018; E7 Blair, Coppock e Moor 2020.

---

## E1. Campbell et al. 2020, SWiM (BMJ)

**Referência.** Campbell M, McKenzie JE, Sowden A, Katikireddi SV, Brennan SE, Ellis S, Hartmann-Boyce J, Ryan R, Shepperd S, Thomas J, Welch V, Thomson H. Synthesis without meta-analysis (SWiM) in systematic reviews: reporting guideline. *BMJ*. 2020;368:l6890. doi:[10.1136/bmj.l6890](https://doi.org/10.1136/bmj.l6890). PMCID PMC7190266; PMID 31948937.

**Como foi lido.** WebFetch em <https://pmc.ncbi.nlm.nih.gov/articles/PMC7190266/> (HTML aberto, CC BY 4.0).

**Estrutura de seções.** Abstract; Summary points; Scope of SWiM reporting guideline; Development of SWiM reporting guideline; Synthesis without meta-analysis reporting items (Item 1: grouping studies for synthesis; Item 2: describe the standardised metric and transformation method used; Item 3: describe the synthesis methods; Item 4: criteria used to prioritise results for summary and synthesis; Item 5: investigation of heterogeneity in reported effects; Item 6: certainty of evidence; Item 7: data presentation methods; Item 8: reporting results; Item 9: limitations of the synthesis, cada um com "Description" e "Explanation"); Discussion; Acknowledgments.

**Resumo.** Um parágrafo sem subtítulos, com 97 palavras, seguido de uma caixa "Summary points" com cinco itens.

**Como apresenta resultados.** A Tabela 1 é o *checklist* dos 9 itens, com colunas para número, item, descrição e página onde o item foi relatado. A Tabela 2 cruza a pergunta respondida com o método de síntese e o dado mínimo exigido (estimativa, variância, direção, valor-p). Os exemplos de cada item estão no material suplementar 2.

**Movimentos (prescritos).**

- **Agrupamento justificado pela teoria da mudança** (Item 1a). Diz como os estudos foram agrupados e por quê, com base no modelo lógico da intervenção.
  > "Providing the rationale, or theory of change, for how the intervention is expected to work and affect the outcome(s) will inform authors’ and review users’ decisions about the appropriateness and usefulness of the groupings."
- **Mudança de agrupamento pós-protocolo declarada** (Item 1b). Relata o que mudou em relação ao protocolo e o motivo, para o leitor julgar se os dados influenciaram a mudança.
  > "Reporting changes to the planned groups, and the reason(s) for these, is important for transparency, as this allows readers to assess whether the changes may have been influenced by study findings."
- **Métrica padronizada e conversões explicadas** (Item 2). Diz qual métrica comum foi usada, por que, e como cada efeito foi convertido.
  > "Explain why the metric(s) was chosen, and describe any methods used to transform the intervention effects, as reported in the study, to the standardised metric, citing any methodological guidance used."
- **Critérios de prioridade definidos antes** (Item 4). Diz quais estudos entram na síntese principal (desenho, risco de viés, relevância) e que o critério foi fixado de antemão.
  > "Pre-specification of these criteria provides transparency as to why certain studies are prioritised and limits the risk of selective reporting of study findings."
- **Heterogeneidade com modéstia** (Item 5). Investigação informal limitada, marcada quando não foi pré-especificada.
  > "Investigations of heterogeneity should be limited, as they are rarely definitive; this is more likely to be the case when informal methods are used."
  > "It should also be noted if the investigation of heterogeneity was not pre-specified."
- **Tabelas e figuras na ordem do texto** (Item 7). Ordena estudos por características-chave (desenho, risco de viés) e na mesma sequência da narrativa.
  > "Study findings presented in tables or graphs should be ordered in the same way as the syntheses are reported in the narrative text to facilitate the comparison of findings from each included study."
- **Achado, certeza e estudos que contribuem** (Item 8). Cada comparação e desfecho tem frase-síntese, certeza e a lista dos estudos que a sustentam.
  > "Describe the result in language that is consistent with the question the synthesis addresses and indicate which studies contribute to the synthesis."
  > "For each comparison and outcome, a description of the synthesis findings should be provided, making clear which studies contribute to each synthesis (for example, listing in the text or tabulated)."
- **A pergunta muda com o método** (Item 9). A contagem por direção responde se há evidência de efeito, não qual é o efeito médio. O texto precisa dizer isso ao tirar conclusões.
  > "the question will ask “is there any evidence of an effect?” rather than “what is the average intervention effect?”"
  > "Limitations of the synthesis might arise from post-protocol changes in how the synthesis was structured and the synthesis method selected."
- **Nome preciso do método** (Discussion). Evita "síntese narrativa" e nomeia o método efetivamente usado.
  > "Avoidance of the term “narrative synthesis” in SWiM is a deliberate move to promote clarity in the methods used in reviews in which the synthesis does not rely on meta-analysis."
- **Modelo lógico revisto à luz dos achados** (Item 8). Relata se o modelo lógico mudou durante a revisão.
  > "If a pre-specified logic model was used, authors may report any changes made to the logic model during the review or as a result of the review findings."

---

## E2. Burns et al. 2019, Cochrane CD010919.pub2

**Referência.** Burns J, Boogaard H, Polus S, Pfadenhauer LM, Rohwer AC, van Erp AM, Turley R, Rehfuess E. Interventions to reduce ambient particulate matter air pollution and their effect on health. *Cochrane Database of Systematic Reviews*. 2019;(5):CD010919. doi:[10.1002/14651858.CD010919.pub2](https://doi.org/10.1002/14651858.CD010919.pub2). PMCID PMC6526394.

**Como foi lido.** WebFetch em <https://pmc.ncbi.nlm.nih.gov/articles/PMC6526394/> (HTML aberto).

**Estrutura de seções.** Abstract (Background; Objectives; Search methods; Selection criteria; Data collection and analysis; Main results; Authors' conclusions); Plain language summary; Summary of findings (4 tabelas); Background (Description of the condition; Description of the intervention; How the intervention might work; Why it is important to do this review); Objectives; Methods (Criteria for considering studies for this review; Search methods for identification of studies; Data collection and analysis, com Data synthesis, Subgroup analysis and investigation of heterogeneity, Sensitivity analysis, Certainty of evidence, Review Advisory Group); Results (Description of studies; Risk of bias in included studies; Effects of interventions, por categoria de intervenção e depois por desfechos de saúde e de qualidade do ar; Subgroup analysis of temporary interventions; Supporting studies); Discussion (Summary of main results; Overall completeness and applicability of evidence; Quality of the evidence; Potential biases in the review process; Agreements and disagreements with other studies or reviews); Authors' conclusions (Implications for practice; Implications for research); Appendices 1 a 9; Characteristics of studies; Differences between protocol and review; Contributions of authors; Declarations of interest.

**Resumo.** Estruturado no padrão Cochrane, com cerca de 700 palavras. O resumo em linguagem simples (cerca de 690 palavras) tem título-pergunta ("Ambient air quality – what works to reduce pollution and improve health?") e subtítulos em forma de pergunta: Why did we conduct this review?; What is the aim of this review?; What were the main results of this review?; How do we interpret these results?; How up to date is this review?

**Como apresenta resultados.** Quatro tabelas *Summary of findings*, uma por categoria de intervenção, com as colunas Outcomes, № of studies (discriminado por desenho), Certainty of the evidence (GRADE, com símbolos ⊕) e Impact. A coluna Impact é uma frase que nomeia os estudos e dá o tamanho do efeito. As notas de rodapé justificam cada rebaixamento. Há oito *harvest plots* (saúde e qualidade do ar em cada categoria): colunas pela direção do efeito, altura da barra pelo risco de viés, cor pelo tipo de comparação. Completam o quadro o modelo lógico (Figura 2), o fluxograma, mapas e um apêndice com os dados de cada estudo. Os resultados são narrados estudo a estudo, com desenho e risco de viés.

**Movimentos.**

- **Lacuna na primeira linha do resumo** (Abstract, Background). Diz que ninguém tinha feito aquilo antes.
  > "To date, no systematic review has assessed the effectiveness of interventions aiming to reduce ambient air pollution."
- **Resposta com certeza no resumo** (Abstract, Main results). Dá a certeza antes do padrão de achados e fecha com uma frase-resposta.
  > "The evidence base, comprising non‐randomized studies only, was of low or very low certainty for all intervention categories and primary outcomes."
  > "Overall, however, the evidence suggests that the assessed interventions do not worsen air quality or health."
- **Certeza traduzida para o leigo** (Plain language summary). Explica o que "baixa certeza" quer dizer para quem lê.
  > "The evidence we identified was of low and very low certainty, which means we cannot be very confident in the overall findings."
- **Modelo lógico feito no protocolo** (Background, How the intervention might work). A teoria vem antes dos dados e organiza a revisão.
  > "At the protocol stage we developed a system‐based logic model to visualize and communicate the relationship between various ambient pollutants and interventions in their broader societal and environmental context, as well as to structure and guide the review process"
- **SoF com estudos nomeados e rebaixamento explicado** (Summary of findings). Cada célula diz quantos estudos, de que desenho, quais são e por que a certeza caiu.
  > "1 cITS‐EPOC study showed a significant 5.9% decrease in cardiovascular mortality associated with the intervention (Yorifuji 2016)."
  > "Rated −1 for inconsistency, as effects from the studies range from positive to negative effects."
- **Narrativa estudo a estudo com desenho e risco de viés** (Results, Effects of interventions). Cada frase de resultado apresenta o estudo pelo desenho e pelo risco de viés antes do efeito.
  > "Deschênes 2012, a cITS‐EPOC study with no substantial risk of bias concerns, observed no clear change in either all‐cause mortality (1.57 fewer deaths per 100,000 population)"
- **Gráfico por direção com ressalva contra contagem de votos** (Methods, Data synthesis; Discussion). Explica o que a coluna "sem efeito claro" mistura e desencoraja a contagem simples.
  > "Please note that this distinction relies on statistical significance but acknowledges that 'unclear effects' may include effects favouring the intervention or favouring the control, as well as true null effects."
  > "This practice is explicitly discouraged in association with harvest plots, and readers are encouraged to carefully read the detailed narrative summary."
- **Ausência de evidência não é evidência de ausência** (Abstract; Discussion).
  > "it is important to emphasize that lack of evidence of an association is not equivalent to evidence of no association."
  > "It should be emphasized that no evidence of an effect is not equivalent to evidence of no effect"
- **Crítica ao próprio instrumento de certeza** (Quality of the evidence). Mostra o limite do GRADE para estudos não randomizados.
  > "which suggests that GRADE does not appropriately differentiate between NRS designs with moderate and low internal validity"
- **Viés do processo com contrafactual e declaração de cegueira aos resultados** (Potential biases in the review process). Diz que outra decisão teria dado outra base de evidência e que as mudanças não foram guiadas pelos resultados.
  > "Had we included cohort studies, this would have yielded a different evidence base, which may have influenced the results and interpretations of the review."
  > "These decisions, however, were based solely on methodological considerations and problems, and were made without consideration of study results."
- **Desvios do protocolo em seção própria** (Differences between protocol and review). Lista cada mudança, a razão e se foi post hoc.
  > "we made the post hoc decision to further classify included studies into main studies"
  > "In the protocol, we planned a single‐reviewer title and abstract screening to remove any clearly irrelevant evidence."
- **Estudos publicados depois da busca** (Overall completeness). Diz se a evidência nova mudaria a conclusão.
  > "based on an informal survey of these studies, it does not appear that the conclusions of this review would be altered based on this recent evidence."
- **Comparação com revisões anteriores** (Agreements and disagreements). Diz em que a revisão difere das anteriores no método e onde discorda delas.
  > "None of these reviews, however, applied systematic and transparent methods"
  > "The heterogeneous evidence base we identified did not entirely support this overall conclusion with respect to effectiveness."
- **Implicações separadas e honestas** (Implications for practice; Implications for research). Na prática, admite que não há resposta simples. Na pesquisa, diz o que outros revisores deveriam fazer.
  > "With the identified evidence base, we were not able to provide a simple answer regarding 'what works'."
  > "Future systematic reviews of interventions aiming to reduce ambient air pollution could consider a more granular categorization of interventions"

---

## E3. Fisher et al. 2023, Campbell Systematic Reviews

**Referência.** Fisher BW, Petrosino A, Persson H, Guckenburg S, Fronius T, Benitez I, Earl K. School-based law enforcement strategies to reduce crime, increase perceptions of safety, and improve learning outcomes in primary and secondary schools: a systematic review. *Campbell Systematic Reviews*. 2023;19(4):e1360. doi:[10.1002/cl2.1360](https://doi.org/10.1002/cl2.1360). PMCID PMC10630714.

**Como foi lido.** WebFetch em <https://pmc.ncbi.nlm.nih.gov/articles/PMC10630714/> (HTML aberto).

**Estrutura de seções.** Abstract (Background; Objectives; Methods; Results; Authors' Conclusions); 1. Plain language summary (1.1 Systematic review evidence supports the criticism that school‐based law enforcement criminalizes students and schools; 1.2 What is this review about?; 1.3 What studies are included?; 1.4 What are the main findings of this review?; 1.5 What do the findings of the review mean?; 1.6 How up‐to‐date is this review?); 2. Background; 3. The intervention (3.1 How the intervention might work; 3.2 Why it is important to do this review); 4. Objectives (4.1 Potential positive effects; 4.2 Potential negative consequences); 5. Methods (5.1 a 5.3, com 5.3.5 Assessment of risk of bias, 5.3.7 Unit of analysis issues, 5.3.12 Data synthesis, 5.3.13 Subgroup analysis, 5.3.14 Sensitivity analysis); 6. Results (6.1 Description of studies; 6.2 Risk of bias in included studies; 6.3 Synthesis of results: 6.3.1 Crime and behavior; 6.3.2 Perceptions of school; 6.3.3 Learning outcomes; 6.3.4 Moderator analyses; 6.3.5 Publication bias; 6.3.6 Sensitivity analyses); 7. Discussion (7.1 Summary of main results; 7.2 Overall completeness and applicability of evidence; 7.3 Quality of the evidence; 7.4 Potential biases in the review process; 7.5 Agreements and disagreements with other studies or reviews); 8. Authors' conclusions (8.1 Implications for practice; 8.2 Implications for research); Contributions of authors; Declarations of interest; Plans for updating the review; Differences between protocol and review; Sources of support.

**Resumo.** Estruturado no padrão Campbell, com cerca de 490 palavras. Os resultados vêm com g e IC 95%. O resumo em linguagem simples usa como primeiro subtítulo o próprio achado e depois perguntas.

**Como apresenta resultados.** A Figura 1 é a teoria da mudança; a Figura 2, o fluxograma PRISMA. A Tabela 1 traz as características dos estudos. A Tabela 2 dá os efeitos médios ponderados (g, EP, p, IC, τ², I², número de relatos e de efeitos), separados por unidade de análise (escola × aluno). A Tabela 3 traz os moderadores. Não há SoF nem GRADE: a qualidade entra como moderador (transversal × longitudinal, controle do desfecho anterior, número de covariáveis).

**Movimentos.**

- **Título que já é o achado** (Plain language summary, 1.1). O primeiro subtítulo do resumo simples é a resposta.
  > "Systematic review evidence supports the criticism that school‐based law enforcement criminalizes students and schools"
- **Resposta direta no resumo** (Abstract, Authors' Conclusions).
  > "This study's findings provide no evidence that there is a safety‐promoting component of SBLE, and support the criticism that SBLE criminalizes students and schools."
- **Teoria com previsões rivais** (3.1 How the intervention might work; 4. Objectives). Apresenta a lógica da dissuasão e a das consequências não intencionais, e divide os objetivos entre efeitos positivos e negativos.
  > "One expectation for how SBLE might work is grounded in the logic of crime deterrence"
  > "However, there is possibility of unintended negative consequences that police presence leads to overuse of legal responses to behavior normally resolved by school administration"
- **Resultado lido contra a previsão** (6.3.1). Cada efeito é comparado com o que cada teoria esperava.
  > "This effect is in the opposite direction of what would be expected if SBLE had a crime deterrent effect."
  > "This effect is consistent with what would be expected by the school criminalization perspective, with more punishment occurring in schools with SBLE."
- **Correlacional por padrão, causal só condicional** (7.3; Abstract). Diz com todas as letras como ler os achados e condiciona a recomendação.
  > "As such, the findings presented here should be interpreted as correlational rather than causal."
  > "To the extent that the findings are causal, schools that invest in strategies to improve safety will likely benefit from divesting from SBLE"
- **Estudos nomeados pelo desenho** (6.2 Risk of bias). Identifica quais estudos têm desenho que sustenta inferência causal.
  > "For example, two studies (Owens, 2017; Weisburst, 2019) used instrumental variable approaches with credibly exogenous variation in the implementation of SBLE."
- **Achado frágil rebaixado no próprio texto** (1.4; 7.3). O único achado favorável é qualificado pela pouca evidência e pelos estudos que o sustentam.
  > "We also found that students in schools with SBLE tended to feel safer at school, although this finding is less trustworthy because it is based on very little data."
  > "Moreover, these two studies (McKay et al., 2006; Stokes et al., 1996) used fairly weak study designs that do not permit strong causal inferences."
- **O que a evidência não permite responder** (7.2). Redefine o que a meta-análise mede diante do que os estudos relatam.
  > "Although we intended to examine differences across SBLE programs of different types, not enough data about the programming was present in the literature to permit such analyses."
  > "Given this limitation in the primary studies, this meta‐analysis can be understood as an analysis of the impacts of the mere presence of SBLE."
- **Vieses do processo em seção própria** (7.4, separada de 7.3 Quality of the evidence). Nomeia decisões dos autores e falhas de procedimento.
  > "Other researchers may have made different decisions about what effect sizes should and should not be grouped together, and this may shape the findings and conclusions of the study."
  > "This could have introduced bias through human error that might have been detected if another coder was available."
- **Desvios do protocolo com motivo e checagem do impacto** (Differences between protocol and review).
  > "This change was made to avoid losing data or making arbitrary choices about which effect sizes to include and exclude."
  > "Nevertheless, we did not find that the weighted mean effect sizes of studies using the SSOCS data were significantly different from those using other data."
- **Comparação com meta-análises anteriores** (7.5). Diz onde concorda e explica a diferença pelo desfecho que a outra não incluiu.
  > "This aligns closely with the current study's finding that associates SBLE with increased exclusionary discipline."
  > "It is notable that the current study's finding linking SBLE to greater crime and behavior problems was driven largely by the increase in school discipline, a measure that was not included in the Turanovic et al. (2019) study."
- **Implicações para prática e pesquisa separadas e numeradas** (8.1; 8.2).
  > "Given these findings, practitioners are likely to benefit from reconsidering their use of SBLE."
  > "First, as noted, methodologically rigorous studies are needed to address the issue of selection bias that is common in this literature."

---

## E4. Lorenz-Spreen et al. 2023, Nature Human Behaviour

**Referência.** Lorenz-Spreen P, Oswald L, Lewandowsky S, Hertwig R. A systematic review of worldwide causal and correlational evidence on digital media and democracy. *Nature Human Behaviour*. 2023;7(1):74-101 (publicado on-line em 7 nov. 2022). doi:[10.1038/s41562-022-01460-1](https://doi.org/10.1038/s41562-022-01460-1). PMCID PMC9883171.

**Como foi lido.** WebFetch em <https://pmc.ncbi.nlm.nih.gov/articles/PMC9883171/> (HTML aberto).

**Estrutura de seções.** Abstract; Main; Results (Direction of associations; Causal inference; Effects on key political variables: Participation, Trust, Political knowledge, Polarization, Populism, Echo chambers and news exposure; Heterogeneity; Sampling methods and risk of bias); Discussion (com a subseção Limitations); Conclusion; Methods (Study selection criteria; Search strategy, study selection, coding and data extraction; Data synthesis and analysis; Deviations from the protocol; Reporting summary).

**Resumo.** Um parágrafo sem subtítulos, com 150 palavras, mais uma frase-síntese editorial. A primeira frase é a pergunta; a última, a implicação.

**Como apresenta resultados.** Não há tabela no corpo do texto; a tabela codificada completa está no OSF. O resultado principal vem em figuras:
- Figura 2: distribuição das direções por variável política, colorida por "benéfico" ou "prejudicial à democracia" independentemente do sinal estatístico. Funciona como um gráfico de direção do efeito.
- Figura 3: um diagrama de caminhos por artigo causal, com a estratégia de identificação em cada caixa.
- Figura 4: mapas ordenados pelo Liberal Democracy Index.
- Figura 5: tamanho de amostra × tipo de amostragem, usado como indicador de risco de viés.
- Figuras 6 e 7: busca e técnicas causais.

**Movimentos.**

- **Pergunta controversa na primeira frase** (Abstract).
  > "One of today’s most controversial and consequential issues is whether the global uptake of digital media is causally related to a decline in democracy."
- **Pergunta pré-registrada citada literalmente** (Main). Mostra a pergunta tal como foi registrada, com link para o protocolo.
  > "We aimed to answer the pre-registered question “If, to what degree and in which contexts, do digital media have detrimental effects on democracy?”"
- **Duas camadas de evidência: correlacional ampla e causal em profundidade** (Main; Methods).
  > "We then conducted an in-depth analysis of the small subset of articles reporting causal evidence."
  > "This two-step approach permitted us to focus on causal effects while still taking the full spectrum of correlational evidence into account."
- **Direção conceitual, não estatística** (Results, Direction of associations). Recodifica cada associação pelo sentido substantivo e explica a regra.
  > "We decided to present relationships not at a statistical level but at a conceptual level."
  > "Throughout, we represent beneficial associations in turquoise and detrimental associations in orange, irrespective of the underlying statistical polarity."
- **Convergência entre causal e correlacional** (Results, Causal inference; Polarization). Diz se as duas camadas apontam na mesma direção.
  > "The overall picture converges closely with the one drawn in Fig. 2."
  > "The body of causal articles largely supported the detrimental associations of digital media that emerged, by and large, in the correlational articles."
- **Estudos que contrariam o padrão descritos pelo desenho** (Effects on key political variables). Traz exemplos com o desenho. Não lista todos os estudos de cada achado, e diz isso.
  > "in a 2 month field experiment, exposure to counter-attitudinal news on Facebook reduced affective polarization"
  > "The chosen examples are stand-ins and illustrations of the general trends."
- **Lacuna explícita e limite de generalização** (Participation; Heterogeneity).
  > "Our search did not identify any studies that examined causal effects of digital media on political participation in authoritarian regimes in Africa or the Middle East."
  > "We strongly caution against a generalization of findings that are necessarily bound to a specific political setting (for example, the United States) to other contexts."
- **Interpretação ambígua devolvida ao leitor** (Causal inference). Marca à parte, em outra cor, o que não dá para classificar.
  > "Instead of simply adopting the authors’ interpretation of the effects or imposing our own interpretation of effects in authoritarian contexts, we leave this interpretation to the reader (denoted in purple in the figure)."
- **Poucos nulos lidos como possível viés de publicação** (Sampling methods and risk of bias).
  > "We found relatively few null effects for some variables. This could be accurate, but it could also be driven by the file-drawer problem—the failure to publish null results."
- **Verbos graduados pela força da evidência** (Discussion).
  > "For democratic countries, evidence clearly indicates that digital media increase political participation."
  > "Less clear but still suggestive are the findings that digital media have positive effects on political knowledge and exposure to diverse viewpoints in news."
- **Limitações como troca declarada** (Limitations). A amplitude custou a comparação quantitativa, e a estratégia pré-registrada gerou desequilíbrio entre desfechos.
  > "This is a trade-off we had to make in exchange for the breadth of our overview of the landscape of evidence across disciplines."
  > "However, following this pre-registered search strategy led to the selection of unequal numbers of studies for different outcome variables."
- **Desvios do protocolo em subseção própria** (Methods, Deviations from the protocol).
  > "The volume of papers our query returned prevented an in-depth analysis of confounding variables."
- **Revisões anteriores e o que esta acrescenta** (Main).
  > "These extant reviews, however, did not contrast and integrate the wide range of politically relevant variables into one comprehensive analysis—an objective that we pursue here."
- **Lacunas de pesquisa nomeadas** (Discussion; Conclusion).
  > "Alongside the need for more causal evidence, we found several research gaps, including the relationship between trust and digital media and the seeming contradiction between network homophily and diverse news exposure."

---

## E5. Pfänder e Altay 2025, Nature Human Behaviour

**Referência.** Pfänder J, Altay S. Spotting false news and doubting true news: a systematic review and meta-analysis of news judgements. *Nature Human Behaviour*. 2025;9(4):688-699. doi:[10.1038/s41562-024-02086-1](https://doi.org/10.1038/s41562-024-02086-1). PMCID PMC12018262.

**Como foi lido.** WebFetch em <https://pmc.ncbi.nlm.nih.gov/articles/PMC12018262/> (HTML aberto).

**Estrutura de seções.** Abstract; Main; People rate true news as more accurate than false news; People are better at rating false news as false than true news as true; Results (Descriptives; Analytic procedures; Main results: Discernment, Skepticism bias; Moderators: Cross-cultural variability, Scales, Format, Topic, Sources, Political concordance; Individual-level data); Discussion; Methods (Data: Eligibility criteria, Deviations from eligibility criteria, Literature search; Statistical methods: Deviations from pre-registration, Outcomes, Effect sizes, Models, Publication bias; Reporting summary).

**Resumo.** Um parágrafo sem subtítulos, com 165 palavras, mais uma frase-síntese editorial. Abre com uma pergunta, dá os efeitos com IC, traduz em uma frase ("In other words...") e fecha com a implicação.

**Como apresenta resultados.** A Figura 2 é conceitual: mostra como as duas medidas são calculadas antes de qualquer resultado. Seguem *forest plots* dos 303 efeitos (Figura 3), um gráfico do moderador causal (Figura 4) e a distribuição por participante (Figura 5). Em Extended Data ficam o PRISMA, o funil e a curva-p. As tabelas de regressão dos moderadores estão no suplemento, e no texto os coeficientes aparecem como "Deltas" com a aritmética explicada.

**Movimentos.**

- **Resumo que abre com a pergunta e traduz o resultado** (Abstract).
  > "How good are people at judging the veracity of news?"
  > "In other words, participants were able to discern true from false news and erred on the side of skepticism rather than credulity."
- **Por que a resposta importa, em forma condicional** (Main). Liga cada resposta possível a uma política diferente.
  > "If people lack the skills to detect false news, interventions should focus on improving these skills."
- **Hipóteses pré-registradas derivadas da literatura, perguntas quando falta teoria** (Main; subtítulos da introdução). Os subtítulos da introdução são as próprias hipóteses.
  > "This led us to pre-register the hypothesis that people would rate true news as more accurate than false news."
  > "We formulated research questions instead of hypotheses for our moderator analyses because of a lack of strong theoretical expectations."
- **Métrica explicada com números concretos** (Methods, Outcomes; Results, Moderators).
  > "In both cases, the discernment is the same: participants rated true news as more accurate by 30 percentage points than false news."
  > "To obtain the predicted value for discordant news, one needs to add the ‘Delta’ to the intercept (−0.2 + 0.78 = 0.58)."
- **Efeito traduzido em proporção de pessoas** (Individual-level data).
  > "As shown in Fig. 5, 79.92% of individual participants had a positive discernment score, and 59.06% of participants had a positive skepticism bias score."
- **Moderador manipulado separado de moderador entre estudos** (Political concordance). Diz quais comparações permitem inferência causal.
  > "The moderators investigated above were (mostly) not experimentally manipulated within studies, but instead varied between studies, which impedes causal inference."
  > "Political concordance is an exception in this regard."
- **Desvio da pré-registração com motivo e teste** (Analytic procedures; Deviations from pre-registration).
  > "We chose to deviate from the pre-registration and use Cohen’s d instead, because it is easier to interpret and corresponds to the standards recommended by the Cochrane manual"
  > "All estimators yielded similar results."
- **Desvio de elegibilidade com direção do viés** (Deviations from eligibility criteria). O estudo excluído favorecia a hipótese dos autores, então a exclusão joga contra eles.
  > "The paper provides 6 effect sizes, all of which strongly favour our second hypothesis (one effect being as large as d = 2.54)."
- **Limitações conceituais (da evidência) separadas das metodológicas (do processo)** (Discussion).
  > "Our meta-analysis has two main conceptual limitations."
  > "Furthermore, our meta-analysis has methodological limitations, which we address in a series of robustness checks in the Supplementary Sections."
- **Estudos que destoam nomeados e dimensionados** (Discussion).
  > "The three studies (53 effect sizes; 10,170 participants; all in the United States) find (1) lower discernment than our meta-analytic average and (2) a negative skepticism (that is, a credulity) bias"
- **O que não se pode descartar** (Discussion).
  > "However, we cannot rule out that people’s current discernment skills stem in part from the current and past work of fact-checking organizations."
- **Conclusão com a ressalva embutida** (Discussion, parágrafo final).
  > "(although the effect is small and probably contingent on false news selection)"
  > "there may be more room to increase the acceptance of true news than to reduce the acceptance of false news."
- **Implicações para prática e para pesquisa em frases distintas** (Discussion).
  > "Second, the fact that people can, on average, discern true from false news lends support to crowdsourced fact-checking initiatives."
  > "At the very least, when testing interventions, researchers should evaluate their effect on both true and false news, not just false news."
- **Posição diante da revisão anterior e de achados prévios** (Main; Sources).
  > "Yet, a scoping review of the literature on belief in false news (including a total of 26 articles) has shown that, in experiments, participants ‘can detect deceitful messages reasonably well’."
  > "In line with past findings, we did not observe a statistically significant difference in discernment between studies that displayed the source of the news items"

---

## E6. Kalla e Broockman 2018, APSR

**Referência.** Kalla JL, Broockman DE. The minimal persuasive effects of campaign contact in general elections: evidence from 49 field experiments. *American Political Science Review*. 2018;112(1):148-166. doi:[10.1017/S0003055417000363](https://doi.org/10.1017/S0003055417000363).

**Como foi lido.** Versão aceita dos autores (26/07/2017), no repositório institucional eScholarship (Universidade da Califórnia), lida com WebFetch em <https://escholarship.org/content/qt103775sx/qt103775sx.pdf>. A página da editora (Cambridge Core) respondeu HTTP 429 e não foi contornada.

**Estrutura de seções.** A introdução não tem título. Seguem: Theoretical Perspectives; Meta-Analysis of Field Experiments and Quasi-Experiments (Data; Results); Original Field Studies in 2015 and 2016 (Design: Persuasive Interventions, Field Experiment and Survey Designs; Results); When Persuasion in General Elections Appears Possible (In General Elections, Early Persuasion Rapidly Decays and Late Persuasion Rarely Appears; Potential Exceptions Close to Election Day: Identifying Rare Cross-pressure and Exploiting Unusual Candidates); Discussion; References; Online Appendix.

**Resumo.** Um parágrafo sem subtítulos, com 147 palavras na versão aceita. Tem tese, duas evidências numeradas ("First... Second..."), duas exceções numeradas e uma frase de contribuição.

**Como apresenta resultados.** A Tabela 1 traz as previsões teóricas por contexto (partido presente? perto da eleição? previsão), com uma linha "Outside of paper's scope". A Figura 1 são *forest plots* em pontos percentuais, com subconjuntos definidos pela teoria (tratamento a menos de dois meses da eleição; mais cedo com medida imediata; mais cedo com medida tardia). A Figura 2 mostra a distribuição das estatísticas t (viés de publicação); a Figura 3, primárias e plebiscitos. A Tabela 2 dá os experimentos originais em DP; a Figura 4, os efeitos por tipo de contato; a Tabela 3, o decaimento. A introdução traz os achados em lista de tópicos ("We find:").

**Movimentos.**

- **Tese no resumo, com número** (Abstract).
  > "We argue that the best estimate of the effects of campaign contact and advertising on Americans’ candidates choices in general elections is zero."
- **Debate dividido como motivação** (Introdução). Mostra que as revisões discordam e que falta identificação causal.
  > "It is surprisingly unclear on the basis of existing evidence."
  > "Reviews reach opposite conclusions"
- **Achados em lista logo na introdução** (Introdução).
  > "The best estimate for the persuasive effects of campaign contact and advertising—such as mail, phone calls, and canvassing—on Americans’ candidate choices in general elections is zero."
- **O que a evidência não diz** (Introdução). Em item próprio da lista de achados, diz sobre o que a evidência se cala.
  > "Our evidence is silent on several questions."
  > "It does not speak to the effects of candidates’ qualities, positions, or overall campaign “message.”"
- **Delimitação do argumento** (Introdução; Discussion).
  > "To be clear, our argument is not that campaigns, broadly speaking, do not matter."
- **Teoria transformada em tabela de previsões** (Theoretical Perspectives). As previsões vêm antes dos dados, com contextos em que o efeito é e não é esperado.
  > "These arguments yield the theoretical predictions shown in Table 1."
  > "Existing work does not clearly test these predictions."
- **Métrica comum e estimando declarados** (Meta-Analysis, Data). Recodifica tudo para pontos percentuais do voto e prefere o efeito entre os que cumpriram o tratamento.
  > "so that the estimates always have the interpretation of “percentage point effect on vote share.”"
  > "Where possible, we used complier average causal effect (treatment-on-treated) estimates."
- **Unidade simples: "1 em N eleitores"** (Meta-Analysis, Results).
  > "our best guess is that it persuades about 1 in 800 voters, substantively zero."
- **Viés de publicação argumentado com números e com estudos não publicados** (Meta-Analysis, Results).
  > "only two studies have statistically significant point estimates, about what would be expected given mild publication bias and this number of public studies."
  > "yielded at least five additional experiments with null effects that have not been written up"
- **Exceções tratadas como tentativas, com os estudos nomeados** (Potential Exceptions).
  > "It is quite possible given the general pattern of null effects that the studies we discuss here are statistical flukes."
  > "First, Rogers and Nickerson (2013) worked with a pro-choice organization ahead of the 2008 US Senate election in Oregon"
- **Hierarquia de desenho explícita** (Original Field Studies, Results). O quase-experimento vale menos que o experimento, e o texto diz isso.
  > "However, an important caveat to these conclusions is that the difference-in-differences designs entail stronger assumptions than the field experiments from Subtable (c) does."
- **Divergência com revisões anteriores explicada pela evidência que elas usaram** (Theoretical Perspectives; Discussion).
  > "However, the vast majority of the evidence that has been marshaled in favor of this claim comes from observational studies, studies of primary elections, and studies of campaign interventions that collect outcomes far before election day."
  > "This pattern of findings is surprising in light of recent reviews of the literature on campaign effects that posit that the classic “minimal effects” view of campaign contact and advertising can be decidedly rejected."
- **Limitações da evidência anunciadas como tal** (Discussion).
  > "We also hasten to note several limitations to our evidence."
  > "First, the existing literature (and, by extension, our meta-analysis) provides only scarce evidence on the effects of television and digital advertising"
- **Implicação para a prática e desenho para a pesquisa** (Discussion).
  > "Indeed, another implication of our results is that campaigns may underinvest in voter turnout efforts relative to persuasive communication."
  > "This is a proposition that future research could test by randomly assigning entire campaign strategies"
- **Ceticismo em relação a desenhos não experimentais** (Discussion, frase final).
  > "studies conducted outside of active campaign contexts that claim to find large campaign effects in general elections should be viewed with healthy skepticism."

---

## E7. Blair, Coppock e Moor 2020, APSR

**Referência.** Blair G, Coppock A, Moor M. When to worry about sensitivity bias: a social reference theory and evidence from 30 years of list experiments. *American Political Science Review*. 2020;114(4):1297-1315. doi:[10.1017/S0003055420000374](https://doi.org/10.1017/S0003055420000374). Acesso aberto, CC BY 4.0.

**Como foi lido.** Versão publicada (acesso aberto, CC BY 4.0) na página do autor, lida com WebFetch em <https://alexandercoppock.com/blair_coppock_moor_2020.pdf> (link na página <https://alexandercoppock.com/blair_coppock_moor_2020.html>). A página da editora respondeu HTTP 429 e não foi contornada.

**Estrutura de seções.** A introdução não tem título. Seguem: A Social Reference Theory of Sensitivity Bias; Sources of Sensitivity Bias in Four Political Science Literatures (Clientelism in Developing Countries; Prejudice; Voter Turnout; Support for Authoritarian Regimes); List Experiments to Reduce Sensitivity Bias; Trade-offs in the Choice of Measurement Design (com a subseção Improving the Power of the List Experiment Design); Meta-analysis Research Design; Meta-analysis Results; Sensitivity Bias in Four Political Science Literatures (Clientelism in Developing Countries; Voter Turnout; Prejudice; Support for Authoritarian Regimes); Empirical Distribution of Sensitivity Bias and Sample Size; Summary of Empirical Results; Discussion; Supplementary Materials; References.

**Resumo.** Um parágrafo sem subtítulos, com 132 palavras. Tem três contribuições numeradas ("We make three contributions. First... Second... Third...") e fecha com a resposta em pontos percentuais.

**Como apresenta resultados.** A Tabela 1 traz as fontes previstas de viés em cada literatura (referente social, se ele pode saber a resposta, custo, direção prevista), montada antes dos dados. A Tabela 2 e a Figura 1 dão um exemplo trabalhado. As Figuras 2 e 3 e a Tabela 3 tratam do *trade-off* de desenho e do poder. A Figura 4 mostra, por literatura, as estimativas de cada estudo, a média com intervalo de credibilidade de 95% e os intervalos de predição de 50% e 95%. A Tabela 4 dá as estimativas meta-analíticas por direção prevista, com N de estudos. A Figura 5 compara o tamanho de cada estudo com o recomendado.

**Movimentos.**

- **Contribuições numeradas no resumo** (Abstract).
  > "We make three contributions."
- **Resposta em pontos percentuais no resumo** (Abstract).
  > "We find that sensitivity biases are typically smaller than 10 percentage points and in some domains are approximately zero."
- **Teoria com condições explícitas** (A Social Reference Theory). A teoria diz quando esperar o viés e em que direção.
  > "Sensitivity bias occurs for a given respondent if and only if all four of the following elements are present:"
  > "When all four elements are present, articulating how they play out in a specific context can generate educated guesses about the plausible direction and magnitude of bias."
- **Direção prevista codificada antes do resultado** (Meta-analysis Research Design).
  > "We first categorized studies by substantive domain, then by the expected direction of sensitivity bias: overreporting or underreporting."
  > "Wherever possible, we relied on the logics of misreporting forwarded by the original authors and in rare cases had to substitute our own best judgment."
- **Sinal e figura explicados ao leitor** (Sensitivity Bias in Four Literatures). Percorre a primeira figura em detalhe e explica o que o intervalo de predição mostra.
  > "Under the assumptions laid out above, negative values indicate that the list experiment recovered a higher prevalence rate than the direct question, revealing underreporting due to sensitivity bias."
  > "These intervals are different from confidence intervals in that they describe our best guess about the distribution of sensitivity biases in vote-buying questions and not our uncertainty about the average level of bias."
- **Veredito para cada previsão** (Sensitivity Bias in Four Literatures).
  > "In summary, the theoretical prediction of underreporting bias in direct questions about vote buying is supported on average, but there is also a considerable range of bias from very large to none at all."
  > "Contrary to expectations, we find relatively little evidence of bias, at least for the specific set of direct questions that have been tested."
- **Nulo lido com cautela** (Summary of Empirical Results). Troca "não há viés" por "dá para descartar vieses maiores que X".
  > "The power of the list experiment to detect moderate sensitivity bias is low, so our conclusion of limited bias in most direct measures may be an instance of “accepting the null” of no bias."
  > "The more cautious interpretation is that we can rule out average biases as large as 10 or 15 percentage points in most cases."
- **O que a meta-análise responde e o que não responde** (Summary of Empirical Results; Meta-analysis Research Design).
  > "First and foremost, this is not a validation study since for most topics, we do not have access to the true prevalence rate."
  > "If readers are unwilling to make these auxiliary assumptions, then our meta-analysis is still of use as a summary of how much the two measurement technologies differ."
- **Limites da busca e do diagnóstico de publicação admitidos** (Meta-analysis Research Design).
  > "We certainly failed in this task."
  > "For this reason, we do not present diagnostics such as funnel plots or p-curves."
- **Decisão de processo justificada pela neutralidade, com o custo declarado** (Meta-analysis Research Design).
  > "We elected not to independently obtain direct question prevalence estimates (e.g., from publicly available surveys), as such discretion could lead to the perception that we were seeking to obtain a pattern either favorable or unfavorable to list experiments."
  > "We acknowledge that relying on original authors for direct question estimates introduces a second source of selection in addition to publication bias."
- **Resposta curta a uma pergunta direta** (Summary of Empirical Results).
  > "Is sensitivity bias likely to be a problem?"
  > "Surprisingly to us, subjects appear to honestly report their prejudices based on race, religion, and sexual orientation."
- **Custo em unidade intuitiva e recomendação prática** (Discussion).
  > "Under typical conditions, list experiments are approximately 14 times noisier than direct questions"
  > "When list experiments or similar methods are selected, they should be conducted only with large samples or when biases are expected to be substantial."
- **Comparação com estudos de validação e com a expectativa da área** (Introdução; Voter Turnout).
  > "Our results indicate that sensitivity bias is typically small to moderate, contra the evident expectation on either the authors’ or their real or imagined reviewers’ parts that misreporting was a large concern."
  > "We interpret this evidence to indicate that at most a small proportion of the measurement error that others have documented by comparing survey responses to validated turnout records from the voter file is due to sensitivity bias, as opposed to memory or recall failures."

---

## Rubrica de movimentos (M01 a M15)

Cada movimento é julgado em três níveis: **sim**, **parcial** ou **não**. O critério foi escrito para ser conferido no texto sem interpretação: procurar a frase, a seção ou o elemento indicado. Onde há leitura própria desta revisão, ela vem em "Aqui". Os valores de certeza e as listas de estudos devem sair dos arquivos da síntese, nunca desta rubrica.

**M01. Resposta primeiro, no resumo e na introdução.**
Descrição: a resposta à pergunta, com direção e certeza, aparece no resumo e se repete no fim da introdução, antes dos métodos.
Exemplares: E2, E3, E4, E5, E6, E7 (E1 exige no item 8 que a linguagem responda à pergunta da síntese).
Critério: **sim** se (a) o resumo tem uma frase que responde à pergunta com direção e nível de certeza e (b) a introdução termina com a mesma resposta, antes de Métodos; **parcial** se só um dos dois ocorre, ou se a resposta vem sem certeza; **não** se o leitor só encontra a resposta em Resultados ou na Discussão.
Aqui: a resposta cobre voto (apoio a quem aparece à frente) e comparecimento, nos termos dos enunciados das células.

**M02. Contribuições explícitas.**
Descrição: o texto diz, em frase própria e de preferência numerada, o que a revisão acrescenta ao que já se sabia.
Exemplares: E7 ("We make three contributions"), E6 ("our second empirical contribution"), E4 ("an objective that we pursue here"), E2 ("no systematic review has assessed"), E5.
Critério: **sim** se há uma frase ou lista que enumera as contribuições (duas ou mais) na introdução e elas voltam na Discussão; **parcial** se a contribuição fica implícita ("preenche uma lacuna") ou aparece só uma vez; **não** se ausente.

**M03. Teoria antes da evidência (modelo lógico e previsões).**
Descrição: antes dos resultados, o texto apresenta o modelo lógico e as previsões concorrentes (em que direção e em que contexto se espera cada efeito) e, nos resultados, dá o veredito sobre cada previsão.
Exemplares: E6 (Tabela 1 de previsões), E7 (quatro condições e direção prevista por literatura), E3 (dissuasão × criminalização), E5 (hipóteses pré-registradas), E2 (modelo lógico no protocolo), E1 (item 1a).
Critério: **sim** se existe figura ou tabela de previsões ou do modelo lógico antes dos resultados e cada achado principal é lido contra uma previsão nomeada ("contrário ao que previa X", "compatível com Y"); **parcial** se a teoria aparece mas os resultados não voltam a ela; **não** se a teoria só surge na Discussão ou está ausente.
Aqui: *bandwagon*, *underdog*, voto estratégico e mobilização como previsões rivais, cada uma com a célula-alvo em que se manifestaria.

**M04. Métrica e direção explicadas antes dos resultados.**
Descrição: o texto diz qual é a métrica comum, como os efeitos foram convertidos e como o sinal foi orientado (o que conta como efeito na direção da previsão), com a pergunta que o método responde.
Exemplares: E1 (itens 2, 3 e 9), E4 ("not at a statistical level but at a conceptual level"), E6 (tudo em pontos percentuais do voto), E7 (o que um valor negativo significa), E5 (Figura 2 conceitual).
Critério: **sim** se Métodos (ou um quadro) explica a métrica, a conversão, a regra de orientação do sinal e o que a contagem por direção responde ("há evidência de efeito?", não "qual é o efeito médio?"); **parcial** se falta um desses quatro elementos; **não** se o leitor precisa adivinhar o sinal.
Aqui: a regra de `direcao_desejada` por célula-alvo, a reorientação nos desenhos de proibição, a conversão para g e o δ de 2 p.p.

**M05. Unidades simples.**
Descrição: os efeitos principais aparecem também numa unidade que o leitor entende sem estatística (pontos percentuais, "1 em N", proporção de estudos, "X vezes"), com uma frase de tradução.
Exemplares: E6 ("1 in 800 voters"), E7 ("smaller than 10 percentage points"; "14 times noisier"), E5 ("30 percentage points"; "79.92% of individual participants"; "In other words..."), E2 (percentuais e mortes por 100 mil no SoF).
Critério: **sim** se todo efeito citado no resumo e nas mensagens principais tem uma versão em unidade simples ao lado da estatística (g, IC, p); **parcial** se só alguns têm; **não** se o texto fica só em g, d ou p.
Aqui: g convertido para pontos percentuais com o p0 da célula, e contagens por direção ditas como "x de y estudos".

**M06. Estudos nomeados em cada achado (SWiM item 8).**
Descrição: cada frase-síntese de célula diz quantos estudos a sustentam e quais são, com desenho e risco de viés quando for o caso.
Exemplares: E1 (item 8), E2 (SoF e narrativa com estudo, desenho e risco de viés), E3 (estudos nomeados por desenho e no achado frágil), E6 (exceções com os estudos citados), E5 (os três estudos que destoam). E4 cumpre em parte e avisa que usa exemplos.
Critério: **sim** se cada enunciado de célula traz k e as citações dos estudos (no texto ou na linha correspondente de uma tabela SoF chamada no mesmo parágrafo); **parcial** se traz k sem nomes, ou nomes só em apêndice; **não** se o achado é dito sem estudos.

**M07. Certeza ligada ao verbo.**
Descrição: a força do verbo acompanha o nível de certeza, e achados frágeis ou exceções são marcados como tentativos no próprio texto.
Exemplares: E2 (resumo em linguagem simples e SoF), E3 ("less trustworthy because it is based on very little data"), E4 ("clearly indicates" × "less clear but still suggestive"), E6 ("statistical flukes"), E5 ("probably contingent").
Critério: **sim** se cada enunciado de achado traz o nível GRADE e um verbo compatível com ele (convenção de linguagem do GRADE, Santesso et al. 2020: alta = afirmação direta; moderada = "provavelmente"; baixa = "pode"; muito baixa = "é incerto se"; a conferir em `livro_regras.md`) e não há verbo mais forte que a certeza em nenhum lugar, inclusive no resumo e nas mensagens principais; **parcial** se a certeza é dada mas o verbo destoa em algum trecho; **não** se a certeza não aparece junto do achado.

**M08. Causal separado de correlacional.**
Descrição: o texto separa o que vem de desenho com sorteio do que vem de desenho observacional, não os junta e diz como ler cada classe.
Exemplares: E4 (duas camadas e convergência), E3 ("interpreted as correlational rather than causal"; "To the extent that the findings are causal"), E5 (moderador manipulado × entre estudos), E6 (hierarquia experimento × diferença-em-diferenças; ceticismo com estudos não experimentais), E2 (só não randomizados, certeza de partida baixa).
Critério: **sim** se resultados e enunciados vêm separados por classe de desenho, com a regra dita em Métodos e o estimando (efeito causal, ATT, associação) declarado para cada classe, e o texto diz se as classes convergem; **parcial** se a separação existe na análise mas a prosa as mistura; **não** se efeitos de desenhos diferentes são somados ou narrados juntos sem distinção.

**M09. Ausência de evidência não é evidência de ausência.**
Descrição: nulos e intervalos largos são lidos pelo que podem descartar, e não como prova de efeito zero.
Exemplares: E2 ("no evidence of an effect is not equivalent to evidence of no effect"), E7 ("accepting the null"; "we can rule out average biases as large as 10 or 15 percentage points"), E6 ("substantively zero", com o limite otimista "1 in 175").
Critério: **sim** se todo "nulo" é qualificado por uma margem (equivalência, δ ou "descarta efeitos maiores que X") ou por poder, e o texto separa "sem evidência" de "evidência de nulo"; **parcial** se a distinção aparece uma vez, em Métodos, e não volta aos resultados; **não** se "não houve efeito" aparece sem qualificação.
Aqui: o critério de nulo por δ (IC 95% dentro de ±δ) e a diferença entre célula nula e célula sem evidência.

**M10. O que a evidência não permite responder.**
Descrição: o texto diz quais perguntas a evidência não alcança (contextos, populações, desfechos, mecanismos) e por quê.
Exemplares: E6 ("Our evidence is silent on several questions"), E4 (nenhum estudo em regimes autoritários na África ou no Oriente Médio; cautela na generalização), E3 ("the mere presence of SBLE"), E7 ("this is not a validation study"), E2 (não há resposta simples sobre "o que funciona").
Critério: **sim** se há um parágrafo ou item próprio, no resumo ou na introdução e de novo na Discussão, que lista as perguntas sem resposta e o motivo (sem estudos, desenho fraco, desfecho não medido); **parcial** se isso só aparece espalhado nas limitações; **não** se ausente.
Aqui: células vazias, falta de estudos no Brasil, mecanismos não testados.

**M11. Tabela e figura que carregam o resultado, na ordem do texto.**
Descrição: o resultado principal está numa tabela-resumo (SoF ou equivalente) e numa figura por direção ou por efeito, ordenadas como a narrativa e com desenho e risco de viés visíveis.
Exemplares: E2 (SoF e *harvest plots* com risco de viés na altura da barra), E1 (item 7), E4 (Figura 2 por direção), E6 (*forest plots* por subconjunto teórico), E7 (Figura 4 com intervalos de predição), E3 (Tabela 2 por unidade de análise).
Critério: **sim** se há uma tabela-resumo com uma linha por célula (k, direção, certeza, estudos) e uma figura por direção do efeito, e as duas seguem a ordem das seções de resultados; **parcial** se falta uma delas ou a ordem difere do texto; **não** se os resultados estão só na prosa.

**M12. Desvios do protocolo com motivo, momento e direção provável do viés.**
Descrição: cada desvio é listado com o motivo, se foi decidido antes ou depois de ver os dados e para que lado ele pode empurrar o resultado, com teste de sensibilidade quando houver.
Exemplares: E5 (exclusão de estudo que favorecia a hipótese dos autores; "All estimators yielded similar results"), E3 (mudança com motivo e checagem do efeito), E2 (seção própria e "without consideration of study results"), E4 (subseção própria), E1 (item 1b).
Critério: **sim** se há seção ou tabela de desvios e, para cada um, o motivo, o momento (antes ou depois dos dados) e a direção provável do viés ou o resultado da sensibilidade; **parcial** se os desvios são listados sem momento ou sem direção do viés; **não** se os desvios não aparecem ou ficam só no protocolo.
Aqui: E001, E002 e as Emendas 1 a 6, com o momento registrado em `00-protocolo/emendas.md`.

**M13. Limitações do processo separadas das limitações da evidência.**
Descrição: as limitações da evidência (desenho, risco de viés, imprecisão, contexto dos estudos) ficam em bloco separado das do processo de revisão (busca, triagem, extração, decisões dos autores, uso de IA).
Exemplares: E3 (7.3 Quality of the evidence × 7.4 Potential biases in the review process), E2 (Quality of the evidence × Potential biases in the review process), E5 ("conceptual limitations" × "methodological limitations"), E6 ("limitations to our evidence"), E7 (busca incompleta e seleção pelo que os autores relataram).
Critério: **sim** se há dois blocos com título próprio (PRISMA 2020, itens 23b e 23c) e cada limitação do processo diz o efeito provável na conclusão; **parcial** se os blocos existem mas misturam os dois tipos, ou se o efeito na conclusão não é dito; **não** se há um só bloco genérico.
Aqui: variante rápida, triagem e extração por IA, conferência humana pendente.

**M14. Comparação com revisões anteriores.**
Descrição: o texto diz o que revisões anteriores concluíram, onde esta concorda ou discorda e por que (evidência diferente, método diferente, desfecho diferente).
Exemplares: E2 (métodos das anteriores e discordância), E3 (duas meta-análises, e a diferença explicada por um desfecho), E4 (o que as anteriores não integram), E6 (as revisões anteriores se apoiam em evidência observacional e medida longe da eleição), E5 (revisão de escopo anterior).
Critério: **sim** se cada revisão anterior relevante é nomeada com o que concluiu e a relação com esta revisão é dita com o motivo da diferença, no início e na Discussão; **parcial** se as anteriores são citadas sem comparação de conclusões, ou só num dos dois lugares; **não** se ausentes.
Aqui: Hardmeier 2008, Moy e Rinke 2012 e Barnfield 2019, com verbo de conclusão só se a obra estiver marcada como verificada em `revisoes_anteriores.md`.

**M15. Implicações separadas para prática e para pesquisa.**
Descrição: as implicações para quem decide (imprensa, institutos, legislador, tribunal eleitoral) ficam separadas das implicações para pesquisa, e nenhuma é mais forte que a certeza.
Exemplares: E2 e E3 (subseções próprias), E5 (frases distintas para checadores e para pesquisadores), E6 (campanhas × desenho de pesquisa futura), E7 (recomendação a pesquisadores de survey).
Critério: **sim** se há dois blocos rotulados, cada implicação remete a um achado com sua certeza e o verbo é proporcional; **parcial** se estão no mesmo bloco ou se alguma implicação vai além do que a certeza permite; **não** se ausentes.

### Quadro-resumo: movimento × exemplar

| Movimento | E1 | E2 | E3 | E4 | E5 | E6 | E7 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| M01 Resposta primeiro | prescreve | sim | sim | sim | sim | sim | sim |
| M02 Contribuições explícitas | | parcial | parcial | sim | parcial | sim | sim |
| M03 Teoria antes da evidência | prescreve | sim | sim | parcial | sim | sim | sim |
| M04 Métrica e direção explicadas | prescreve | sim | parcial | sim | sim | sim | sim |
| M05 Unidades simples | | sim | | parcial | sim | sim | sim |
| M06 Estudos nomeados por achado | prescreve | sim | sim | parcial | parcial | sim | parcial |
| M07 Certeza ligada ao verbo | prescreve | sim | parcial | parcial | parcial | parcial | parcial |
| M08 Causal × correlacional | | sim | sim | sim | sim | sim | |
| M09 Ausência ≠ evidência de ausência | | sim | | | | sim | sim |
| M10 O que não se responde | prescreve | sim | sim | sim | sim | sim | sim |
| M11 Tabela e figura na ordem do texto | prescreve | sim | parcial | sim | sim | sim | sim |
| M12 Desvios com direção do viés | prescreve | parcial | sim | parcial | sim | | |
| M13 Processo × evidência | prescreve | sim | sim | parcial | sim | parcial | parcial |
| M14 Revisões anteriores | | sim | sim | sim | parcial | sim | parcial |
| M15 Prática × pesquisa | | sim | sim | parcial | sim | sim | sim |

Célula vazia: o exemplar não faz o movimento, ou ele não se aplica (E1 é diretriz; E6 e E7 não têm protocolo registrado). Em M07, só E2 usa GRADE; os demais graduam o verbo sem nível formal de certeza e, pelo critério, ficam em parcial. O julgamento de cada célula é do leitor desta etapa, feito com o critério acima, e serve para escolher de qual exemplar copiar cada movimento.
