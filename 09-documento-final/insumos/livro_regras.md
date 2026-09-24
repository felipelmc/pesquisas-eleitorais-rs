# Regras do livro para o relato do artigo final

Fonte: Felipe Lamarca, *Revisão sistemática de ponta a ponta*, <https://felipelamarca.com/Systematic-Review/metodo/>. Lido em 24/09/2026 (etapa 0b da reescrita). Para que as citações fossem literais, o HTML publicado de cada capítulo foi baixado inteiro e convertido em texto, sem resumo intermediário. Todas as citações entre aspas retas foram conferidas por programa contra esse texto; as aspas curvas dentro delas são do livro.

## Como ler este arquivo

- Cada regra tem um ID (`R<seção>.<n>`), a regra numa frase, a citação literal entre aspas retas e o endereço da seção, com âncora.
- **Aqui:** marca a aplicação de uma regra condicional a esta revisão (k, meta-análise, autopiloto, publicação). Não é regra nova, e o fato citado vem do `CLAUDE.md` do projeto.
- Tabelas marcadas *transcrição* reproduzem células do livro sem alteração.

Arquivos e capítulos:

| Arquivo | Capítulo |
|---|---|
| `06-qualidade-risco-vies.html` | 6 |
| `08a-sintese-quantitativa.html` | 8 |
| `09-certeza-evidencia-pratica.html` | 10 |
| `10-relato-divulgacao.html` | 11 |
| `11-ia-na-revisao.html` | 12 |
| `apendice-b-reprodutibilidade.html` | Apêndice B |

Seções pedidas que não existem com o número ou o conteúdo indicado:

- **§11.8** é "Erros comuns e como evitá-los", não licenças. O que publicar e as licenças estão na §11.5 (subseção "Pacote aberto de dados e código") e no Apêndice B (B.1, B.4 e B.5). Usei essas três fontes e as linhas da §11.8 que tratam de dados e licença.
- **§11.10** é "Como relatar". As frases-modelo estão dentro dela; não há seção separada de frases-modelo.
- **§6.6** é só "Visualização". O "Como relatar" do risco de viés é a **§6.12**. Usei as duas.
- **Apêndice B** não tem item numerado 27. O item 27 é do PRISMA 2020 e aparece em B.1 (linha "Dados e código"), em B.4 e na §11.5. Usei esses trechos.
- A **§10.1** remete a "versão para produtos de divulgação" à Seção 11.1, mas as regras do resumo em linguagem simples estão na **§11.4**, subseção "Resumo em linguagem simples e sumário executivo".
- Usei também trechos dos mesmos capítulos que tratam do relato: §11.3 (exibição de rótulos), §11.6 (itens do resumo PRISMA, PRISMA-S e SWiM), §11.7, §8.1 a §8.8, §10.4 a §10.10, §6.1, §6.4, §6.7, §6.10, §12.1, §12.11, §12.13 e §12.14.

---

## 1. Estrutura e ordem do relatório (§11.1, §11.2, §11.5)

- **R1.1** A diretriz principal é o PRISMA 2020. Numa revisão de efetividade sem meta-análise, o SWiM o complementa, e os itens 13 e 20 do PRISMA são relatados pelo SWiM. "Os itens 13 e 20 do PRISMA são relatados seguindo o SWiM" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#qual-diretriz-de-relato-usar>
- **R1.2** Uma extensão não substitui o PRISMA: o artigo relata os 27 itens. "Extensão não substitui o PRISMA 2020. Uma revisão OQF sem meta-análise relata os 27 itens e, dentro dos itens de síntese, segue o SWiM" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#qual-diretriz-de-relato-usar>
- **R1.3** A busca é relatada também pelo PRISMA-S (16 itens). Os checklists preenchidos, com a página de cada item, vão em apêndice. "Checklist preenchido, com a página de cada item, vai como apêndice" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#qual-diretriz-de-relato-usar>
- **R1.4** O checklist não é atestado de qualidade; serve para o leitor julgar a revisão. "Um checklist preenchido, portanto, não prova que a revisão é boa; prova que o leitor tem como julgá-la." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#qual-diretriz-de-relato-usar>
- **R1.5** Se houver limite de palavras, o detalhe vai para material suplementar num repositório aberto e permanente, com link no texto. "Com limite de palavras, o detalhe vai para material suplementar depositado em repositório aberto e permanente (OSF, Dryad, figshare), com link no texto" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#qual-diretriz-de-relato-usar>
- **R1.6** O artigo segue a estrutura OQF, nesta ordem. "Introdução; Metodologia (2.1 busca, 2.2 seleção, 2.3 sistematização e análise); Resultados (3.1 Efeito, 3.2 Mecanismo, 3.3 Moderadores, 3.4 Percepção, 3.5 Implementação e custo); Da evidência à prática; Conclusões e limitações" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-oqf>
- **R1.7** Cada seção OQF acrescenta ao modelo o que falta para cobrir os itens PRISMA indicados. Transcrição da coluna "O que acrescentar"; a linha da Introdução cita as revisões do exemplo dos celulares. <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-oqf>

  | Seção OQF | O que acrescentar (transcrição) | Itens PRISMA 2020 |
  |---|---|---|
  | Título | Nada; manter a identificação como RS | 1 |
  | Resumo | Fontes e data da última busca, método de risco de viés, número de estudos e participantes, IC, limitações da evidência, financiamento, registro | 2 |
  | 1 Introdução | Por que nova revisão diante das anteriores (Böttger e Zierer, 2024; Campbell et al., 2024); objetivo explícito | 3, 4 |
  | 2 Metodologia | Critérios completos e como os estudos foram agrupados em cada síntese; registro, protocolo e desvios | 5, 24a-c |
  | 2.1 Busca | Data da última busca por base, limites e filtros, busca de citações, apêndice PRISMA-S (Seção 4.8) | 6, 7 |
  | 2.2 Seleção | Quantos revisores por fase, independência, desempate, dicionários e IA com validação; fluxograma do ledger; excluídos limítrofes com motivo | 8, 16a, 16b |
  | 2.3 Sistematização e análise | Extração (quantos, independência, contato com autores); desfechos e regra de modelo principal; ferramenta de risco de viés; conversões; modelo, estimador e software; heterogeneidade; sensibilidade; viés de relato; certeza; versão da regra da caixa | 9-15 |
  | 3.1 Efeito | Características e risco de viés dos estudos da síntese; estimativa com IC, τ², I² e intervalo de predição no texto; certeza em cada enunciado | 17-22 |
  | 3.2 a 3.5 | Para cada achado qualitativo, estudos de suporte e confiança CERQual; separar moderador testado de hipótese | 20c, 22; ENTREQ |
  | 4 Da evidência à prática | Rótulos gerados pela regra, com certeza em cada linha; implicações proporcionais à certeza e transferibilidade ao Brasil (Seção 10.1) | 23d |
  | 5 Conclusões e limitações | Interpretação diante de outras revisões; limitações do processo em subseção própria | 23a-c |
  | Informações adicionais | Registro, financiamento, conflitos, dados e código, declaração de IA, checklists | 24-27 |

- **R1.8** Cinco melhorias sobre o formato OQF são obrigatórias:
  - certeza no resumo, em 3.1 a 3.5, na caixa, no painel e nas conclusões;
  - rótulo "Inconclusivo" na caixa e no painel;
  - limitações do processo na seção 5, separadas das da evidência;
  - declaração de IA nas informações adicionais e nos métodos;
  - disponibilidade de dados e código (item 27).

  "A especificação desta base torna obrigatórias cinco melhorias sobre o formato OQF" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-oqf>
- **R1.9** A seção 4 se chama "Da evidência à prática: implicações", e nenhuma implicação passa da certeza que a sustenta. "Esta base mantém a seção com o nome “Da evidência à prática: implicações”, como na Seção 10.1, e nenhuma implicação é mais forte do que a certeza que a sustenta." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-oqf>
- **R1.10** A tabela-fonte de achados é congelada depois do portão de síntese, e o artigo e os derivados leem só dela. "Artigo, caixa, painel e derivados leem só essa tabela." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-passos>
- **R1.11** A ordem de redação tem três passos:
  - primeiro Metodologia, Resultados, Da evidência à prática e Conclusões, pela tabela da §11.2;
  - depois as informações adicionais, com o resumo por último;
  - por fim os derivados, os checklists, o passe de estilo e a auditoria.

  "Escrever Metodologia, Resultados, Da evidência à prática e Conclusões pela tabela da Seção 11.2, com strings, datas e limites no apêndice PRISMA-S, certeza em cada enunciado e limitações da evidência (23b) separadas das do processo (23c)." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-passos>
- **R1.12** Os checklists, a revisão de estilo e a auditoria final fecham o relatório. "Preencher os checklists com a página de cada item, fazer a revisão de estilo e rodar a auditoria final (tabelas abaixo)." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-passos>

## 2. Resumo, resumo executivo e mensagens principais (§11.1, §11.4, §11.6)

- **R2.1** O resumo estruturado cobre os 12 itens do PRISMA 2020 para resumos. "título; objetivos; critérios de elegibilidade; fontes e data da última busca; método de risco de viés; métodos de síntese; número de estudos e participantes; resultados dos desfechos principais com IC e direção; limitações da evidência; interpretação; financiamento; registro" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-diretrizes>
- **R2.2** O resumo científico tem até 250 palavras (padrão Campbell). "o resumo científico tem até 250 palavras e o resumo em linguagem simples até 750" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-diretrizes>
- **R2.3** O resumo é escrito por último, conferindo os 12 itens. "Escrever o resumo por último, conferindo os 12 itens" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-passos>
- **R2.4** A certeza acompanha o achado em todo lugar em que ele aparece. "A certeza acompanha o achado em todo lugar em que ele aparece: resumo, tabelas, resultados e conclusões" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#que-produto-para-que-público>
- **R2.5** Heterogeneidade vai no texto e no resumo, não só na figura. "τ², I² e intervalo de predição no texto e no resumo" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-erros>
- **R2.6** Mensagens-chave e sumário executivo, para quem só lê a primeira página, seguem a pirâmide invertida e ocupam uma a duas páginas. "Mensagens em tópicos, depois sumário, depois relatório completo (“pirâmide invertida”)" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#que-produto-para-que-público>
- **R2.7** As mensagens-chave são de três a cinco frases, uma por dimensão relevante, e cada uma traz a certeza em frase padronizada. "Cada frase com a certeza, usando as frases padronizadas da Seção 10.1" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#síntese-de-evidências-e-policy-brief-o-modelo-clear>
- **R2.8** Os números do sumário, do resumo em linguagem simples e das mensagens são copiados da tabela-fonte. "Os números do sumário, do resumo em linguagem simples e das mensagens-chave são copiados da tabela-fonte, nunca redigidos de memória." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#resumo-em-linguagem-simples-e-sumário-executivo>
- **R2.9** O mesmo achado usa os mesmos números e as mesmas palavras em todos os produtos. "O mesmo achado usa os mesmos números e as mesmas palavras em todos os produtos" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#que-produto-para-que-público>
- **R2.10** Todo produto derivado traz todos os desfechos principais, com a certeza, o contexto dos estudos e o link. "Todo produto derivado traz todos os desfechos principais, com certeza, contexto dos estudos e link para a revisão e o pacote" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#disseminação-para-gestores>
- **R2.11** O título de um produto derivado não promete mais do que a certeza permite. "Sem prometer mais do que a certeza permite" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#síntese-de-evidências-e-policy-brief-o-modelo-clear>
- **R2.12** O produto derivado diz o que foi feito: bases, data da busca, número e desenho dos estudos, países. O leitor tende a supor que os autores fizeram os estudos. "Leitores tendem a achar que os autores fizeram os estudos" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#síntese-de-evidências-e-policy-brief-o-modelo-clear>
- **R2.13** Numa síntese derivada, o bloco "o que foi feito" e a certeza de cada conclusão são obrigatórios. "Numa síntese derivada de revisão OQF, o bloco “o que foi feito” e a certeza de cada conclusão são obrigatórios." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#síntese-clear-nº-11-bom-molde-com-erros-de-conferência>
- **R2.14** O contexto dos estudos e a comparação com o contexto de uso entram na mensagem principal. "O contexto dos estudos e a comparação com o contexto de uso vão na mensagem principal" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#para-quem-se-escrevem-as-implicações>
- **R2.15** A síntese para gestores começa pelo problema de política, não pela revisão. "Começar pela política, não pela revisão" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#síntese-de-evidências-e-policy-brief-o-modelo-clear>
- **R2.16** O produto derivado tem um bloco "Saber mais", obrigatório, com o link da revisão completa e do pacote. "Link da revisão completa e do pacote aberto" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#síntese-de-evidências-e-policy-brief-o-modelo-clear>
- **R2.17** Uma versão atualizada abre com o que mudou. "Versões atualizadas abrem com o que mudou" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#disseminação-para-gestores>

## 3. Resumo em linguagem simples (padrão Campbell, §11.4)

- **R3.1** O resumo em linguagem simples tem de 600 a 750 palavras, sem notas nem referências. É escrito no presente e enuncia o achado diretamente. "De 600 a 750 palavras, sem notas nem referências, em linguagem direta e no presente; o achado é enunciado diretamente, sem “a análise mostra” ou “os autores argumentam”" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#resumo-em-linguagem-simples-e-sumário-executivo>
- **R3.2** O título é uma manchete com o achado principal. "Título em estilo de manchete com o achado principal; pode indicar o tamanho do efeito ou a qualidade da evidência, e revisões vazias dizem que não há evidência" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#resumo-em-linguagem-simples-e-sumário-executivo>
- **R3.3** "A revisão em resumo" tem até 50 palavras e inclui todos os desfechos principais. "“A revisão em resumo” com até 50 palavras; com vários desfechos principais, todos entram, para evitar relato seletivo" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#resumo-em-linguagem-simples-e-sumário-executivo>
- **R3.4** Um quadro na primeira página diz o que a revisão estudou e quantos estudos incluiu. "Um quadro na primeira página diz o que a revisão estudou e quantos estudos incluiu" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#resumo-em-linguagem-simples-e-sumário-executivo>
- **R3.5** Os achados vêm em subtítulos formulados como perguntas, com as mesmas palavras para o mesmo nível de efeito. Um desfecho importante sem dados é mencionado. "Achados em subtítulos formulados como perguntas, com as mesmas palavras para o mesmo nível de efeito e consistentes com o resumo e os resultados; desfecho importante sem dados é mencionado assim mesmo" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#resumo-em-linguagem-simples-e-sumário-executivo>
- **R3.6** A seção final diz até quando se buscou e quando a revisão foi publicada. "A seção final diz até quando se buscou e quando a revisão foi publicada" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#resumo-em-linguagem-simples-e-sumário-executivo>
- **R3.7** Quando o intervalo inclui benefício e dano relevantes, a frase diz que se sabe muito pouco sobre o efeito. "quando o intervalo inclui benefício e dano relevantes, a largura do intervalo importa mais que a estimativa pontual, e a frase deve dizer que se sabe muito pouco sobre o efeito" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#resumo-em-linguagem-simples-e-sumário-executivo>
- **R3.8** O resumo em linguagem simples não faz recomendações de política; traz implicações para política e pesquisa. "O guia Campbell de resumos em linguagem simples afirma que revisões não fazem recomendações de política e pede implicações para política e pesquisa" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-oqf>
- **R3.9** Se um LLM gerar ou revisar o resumo em linguagem simples, uma pessoa confere o texto contra o original. "Conferir contra o original, sobretudo números e sentido" — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-regras>

## 4. Métodos: "diz o que esta revisão fez" (§11.5, §11.2, §8.8, §6.12, §10.10)

- **R4.1** Os métodos relatam o que foi feito, no passado, e reconhecem e explicam as mudanças em relação ao protocolo. "A seção de métodos relata o que foi feito, no passado, e toda mudança não trivial em relação ao protocolo é reconhecida e explicada" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#revisão-de-estilo>
- **R4.2** A Metodologia não explica o método de forma didática; diz o que esta revisão fez. "Cortar ou mover para a introdução; a Metodologia diz o que esta revisão fez" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#revisão-de-estilo>
- **R4.3** Cada etapa traz seus parâmetros. "Quem triou, quantos, com que concordância, com que ferramenta e versão" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#revisão-de-estilo>
- **R4.4** Na busca, os itens do PRISMA-S que pesam no relatório final são o 8, o 13, o 15 e o 16. "No relatório final pesam mais o item 8 (estratégias copiadas exatamente como executadas), o 13 (data da última busca de cada estratégia), o 15 (total de registros por base e por outra fonte) e o 16 (processo e software de deduplicação)." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-diretrizes>
- **R4.5** Os métodos de síntese relatam, no mínimo:
  - (i) critérios de agrupamento e checklist de comparabilidade;
  - (ii) métrica, direção desejada e conversões, com as aproximadas marcadas;
  - (iii) regra de um efeito por estudo ou modelo de dependência;
  - (iv) modelo, estimador, IC, heterogeneidade, intervalo de predição (PI) e software com versão;
  - (v) moderadores e teste;
  - (vi) sensibilidade;
  - (vii) viés por resultados faltantes e limiar de k;
  - (viii) método SWiM e gráficos;
  - (ix) benchmark e δ do protocolo.

  "(iii) regra de um efeito por estudo ou modelo de dependência com ρ e correção (PRISMA 13d); (iv) modelo, estimador de τ², método do IC, medidas de heterogeneidade, intervalo de predição e software com versão (PRISMA 13d)" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-relato>
- **R4.6** Se houve síntese sem meta-análise, os métodos dizem o método, a pergunta que ele responde e os gráficos, além do benchmark e de δ. "(viii) se houve síntese sem meta-análise, método, pergunta respondida e gráficos (SWiM 3, 7); (ix) benchmark de magnitude e δ fixados no protocolo." — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-relato>
- **R4.7** O método de síntese é nomeado; "síntese narrativa" sozinha não basta. "O Handbook pede ainda que a revisão nomeie o método em vez de escrever só “síntese narrativa”" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-diretrizes>
- **R4.8** *A maioria dos estudos* é contagem implícita e precisa ser declarada como método. "Frases como “a maioria dos estudos encontrou” são contagem implícita e precisam ser declaradas como método" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#síntese-sem-meta-análise>
- **R4.9** A direção vem da estimativa pontual, relativa à direção desejada. A significância fica em variável separada. "com a direção sempre pela estimativa pontual relativa à direcao_desejada e a significância em variável separada" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#síntese-sem-meta-análise>
- **R4.10** Contagem de votos por significância não é método de síntese. "Contagem de votos por significância estatística não é método de síntese" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#checklist-de-comparabilidade-conceitual>
- **R4.11** Randomizados e não randomizados são apresentados e analisados em separado. "Estudos randomizados e não randomizados são apresentados e analisados separadamente e não entram na mesma meta-análise" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#checklist-de-comparabilidade-conceitual>
- **R4.12** Resultados de não randomizados em risco crítico ficam fora das análises, e a análise completa vai para a sensibilidade. "Resultados de estudos não randomizados em risco crítico de viés ficam fora das análises" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#checklist-de-comparabilidade-conceitual>
- **R4.13** Revisões e meta-análises não se somam aos estudos primários. Numa revisão rápida, entram só no nível de revisão, com controle de sobreposição. "em revisões rápidas e em overviews, podem ser usadas como fonte de evidência no nível de revisão, com controle explícito de sobreposição (CCA) e sem somar seus estudos aos primários" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#checklist-de-comparabilidade-conceitual>
- **R4.14** Rótulos de magnitude vêm do benchmark do campo fixado no protocolo. "Rótulos como “pequeno” e “grande” dependem do campo e são fixados no protocolo, não escolhidos depois" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#benchmarks-de-interpretação-da-magnitude>
- **R4.15** O relato do risco de viés tem um mínimo:
  - ferramenta e versão por desenho, e a regra de fronteira;
  - resultados avaliados;
  - avaliadores e resolução de desacordos;
  - uso de IA;
  - critérios de exclusão;
  - como o julgamento entrou nas análises;
  - risco por estudo e por síntese;
  - limitação resultante.

  "O relato mínimo informa ferramenta e versão por desenho e a regra de fronteira; resultados avaliados; avaliadores, independência e resolução de desacordos; uso de IA; critérios de desenho e de exclusão previstos; como o julgamento entrou nas análises; risco de viés de cada estudo e de cada síntese; limitação resultante" — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#sec-06-relato>
- **R4.16** Cada ferramenta é citada com nome, versão e data. A ROBINS-I V2 é um rascunho. "Nome, versão e data; a ROBINS-I V2 de 20/11/2025 ainda é rascunho sujeito a mudança" — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#parâmetros-que-o-protocolo-fixa>
- **R4.17** No risco de viés, a IA só rascunha, com trecho e página; os julgamentos são humanos. "A especificação desta base permite que um modelo de linguagem rascunhe respostas às perguntas-sinalizadoras com trecho literal e página; os julgamentos são humanos" — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#sec-06-quem>
- **R4.18** Kappa não é critério de aceitação do risco de viés. Registram-se os julgamentos originais, os desacordos e o modo de resolução. "sem limiar de kappa como critério de aceitação para risco de viés" — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#sec-06-quem>
- **R4.19** Os métodos de certeza informam:
  - a abordagem por tipo de achado;
  - quem julgou e como as divergências foram resolvidas;
  - os limiares e sua origem no protocolo;
  - o ponto de partida de cada corpo.

  "Abordagem de certeza por tipo de achado (GRADE, ICEMAN, GRADE-CERQual, enunciado narrativo), quem julgou e como divergências foram resolvidas" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-relato>
- **R4.20** O ponto de partida de cada corpo depende da ferramenta. Com ROBINS-I, o corpo não randomizado pode começar em alta, mas em geral cai dois níveis. Sem ROBINS-I, começa em baixa. "Podem começar em alta, mas em geral são rebaixados dois níveis por confundimento e seleção" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#ponto-de-partida-e-quanto-rebaixar>
- **R4.21** Sem meta-análise, a certeza continua obrigatória, com os domínios adaptados (Murad et al.). "Quando os estudos medem o desfecho de modos que não permitem agregação, a certeza continua obrigatória" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#grade-sem-meta-análise>
- **R4.22** Cada rebaixamento e cada elevação são justificados por escrito. "Idealmente duas pessoas independentes, com consenso; cada rebaixamento e elevação justificado por escrito (MECIR C74 e C75, obrigatórios)" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#ponto-de-partida-e-quanto-rebaixar>

## 5. Resultados

### 5.1 Fluxograma (item 16a)

- **R5.1** Nenhuma contagem do fluxograma é digitada: todas saem do ledger, com as somas conferidas. "Todo número do fluxograma sai do ledger de decisões e passa pelas somas de conferência (Seção 5.1); nenhuma contagem é digitada." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#que-produto-para-que-público>
- **R5.2** Com automação, o fluxograma separa as exclusões por humanos das exclusões por ferramentas. "quando houver automação, quantos foram excluídos por humanos e quantos por ferramentas" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-diretrizes>
- **R5.3** O fluxograma informa o número por base, não só o total. "O modelo sugere informar, quando possível, o número por base ou registro, e não só o total" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-diretrizes>
- **R5.4** O modelo do fluxograma segue as fontes consultadas; bola de neve exige o ramo de outras fontes. "Bola de neve, repositório do IPEA, sites de órgãos e contato com autores exigem o modelo com o ramo de outras fontes." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#qual-diretriz-de-relato-usar>
- **R5.5** Caixas que não se aplicam saem do diagrama. "As caixas cinzas do modelo só são preenchidas quando se aplicam; do contrário, saem do diagrama." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#qual-diretriz-de-relato-usar>
- **R5.6** Texto não localizado conta como relato não recuperado, não como exclusão. "tratar “não localizado” como relato não recuperado" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-passos>
- **R5.7** Revisões entram como fonte de citações, não como estudos incluídos. "Revisões vão ao ramo de outras fontes como fonte de citações" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-erros>

### 5.2 Estudos, resultados individuais e risco de viés (itens 18, 19, 20a)

- **R5.8** O risco de viés aparece para cada estudo e para os estudos de cada síntese. "O PRISMA 2020 pede o risco de viés de cada estudo e dos estudos de cada síntese" — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#sec-06-visualizacao>
- **R5.9** Os julgamentos ficam ao lado de cada estudo no *forest plot*. Nos gráficos de barras, as regiões são proporcionais ao peso. "O Handbook recomenda forest plots com os julgamentos ao lado de cada estudo, tabelas completas disponíveis e, em gráficos de barras, regiões proporcionais ao peso na meta-análise, não ao número de estudos" — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#sec-06-visualizacao>
- **R5.10** Dados da ROBINS-I V2 não vão para o modelo ROBINS-I do robvis, que usa a ordem de domínios da V1. Use tabela própria ou legenda conferida. "o modelo ROBINS-I rotula os domínios na ordem da versão 1 (D2 seleção, D3 classificação), enquanto a V2 inverte a ordem e tem seis domínios" — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#sec-06-visualizacao>
- **R5.11** Tabelas e gráficos de risco de viés vêm com a conferência de que as contagens somam o total avaliado. "Tabelas e gráficos, com asserção de que as contagens somam o número de resultados avaliados." — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#sec-06-passos>
- **R5.12** O risco de viés não pode sumir do resumo nem das conclusões quando varia entre estudos. "Só se todos têm o mesmo risco; nos demais casos o risco some do resumo e das conclusões" — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#como-o-julgamento-entra-na-síntese>
- **R5.13** Cada estudo aparece com suas estatísticas e sua estimativa com precisão, de preferência em tabela ou gráfico. "Para cada estudo, estatísticas por grupo e estimativa com precisão, de preferência em tabelas ou gráficos" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-diretrizes>

### 5.3 SWiM, contagem por direção e figuras

- **R5.14** O artigo relata os 9 itens do SWiM:
  - 1a/1b: grupos da síntese e mudanças;
  - 2: métrica;
  - 3: métodos;
  - 4: priorização;
  - 5: heterogeneidade;
  - 6: certeza;
  - 7: métodos gráficos e ordem;
  - 8: resultados;
  - 9: limitações.

  "Métodos gráficos e tabulares; características usadas para ordenar os estudos" (item 7) — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-diretrizes>
- **R5.15** Cada comparação e desfecho vem com o achado, a certeza e os estudos que contribuem, em linguagem coerente com a pergunta (SWiM 8). "Resultado de cada comparação e desfecho, com certeza, em linguagem coerente com a pergunta, indicando os estudos que contribuem" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-diretrizes>
- **R5.16** A contagem por direção usa teste de sinal binomial exato bilateral, com proporção e IC de Clopper-Pearson. "Teste de sinal binomial exato bilateral sobre a direção da estimativa pontual, com proporção e IC exato de Clopper-Pearson (Wilson como alternativa)" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#testes-combinados-da-proposta-oqf-estatuto-e-uso>
- **R5.17** Padrões da contagem por direção não são chamados de estatisticamente significativos. "padrões não devem ser descritos como “estatisticamente significativos”" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#síntese-sem-meta-análise>
- **R5.18** Todo resultado de teste combinado vem com a ressalva literal abaixo. Isso inclui o Cooper, que é o teste de sinal. "O teste combina valores-p (ou direções) e não informa a magnitude do efeito; não distingue estudos grandes com efeitos pequenos de estudos pequenos com efeitos grandes; quando significativo, indica apenas que há efeito em pelo menos um estudo (ou que a proporção de efeitos benéficos difere de metade); quando não significativo, com poucos estudos pequenos, não indica ausência de efeito. É análise secundária e não define o rótulo de efeito." — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#testes-combinados-da-proposta-oqf-estatuto-e-uso>
  - Aqui: vale para o teste de sinal por célula do `swim.R`. O livro trata o Cooper como "a contagem de votos por direção".
- **R5.19** Teste combinado nunca define o rótulo de efeito. "Testes combinados de valores-p nunca definem, sozinhos, o rótulo de efeito da caixa de ferramentas" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#checklist-de-comparabilidade-conceitual>
- **R5.20** Sem combinação, o *forest plot* não tem diamante e é ordenado ou dividido por uma característica relevante. "Forest plot sem diamante, ordenado ou dividido por uma característica relevante (desenho, risco de viés, tamanho)" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#síntese-sem-meta-análise>
- **R5.21** No *effect direction plot*, cada linha é um estudo e cada coluna um domínio de desfecho. O tamanho da seta indica o n, e a cor da linha indica o risco de viés. "O tamanho da seta indica o n do grupo de intervenção (> 300; 50 a 300; < 50) e a cor da linha, o risco de viés" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#síntese-sem-meta-análise>
- **R5.22** O *harvest plot* classifica os estudos pela direção, nunca pela significância. "Os artigos originais classificavam por significância; a versão aceitável classifica por direção" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#síntese-sem-meta-análise>
- **R5.23** O *albatross plot* só é usado quando se tem p e n. "exige só p unilateral e n total (ou p bilateral, direção e n)" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#síntese-sem-meta-análise>
- **R5.24** Todo gráfico de síntese sem meta-análise declara o método e a característica usada para ordenar os estudos. "Declarar o método e as características usadas para ordenar os estudos" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#visualização-dos-resultados>
- **R5.25** No *forest plot*, os estudos são identificados por autor e ano e ordenados por uma característica, não em ordem alfabética. τ², I² e PI também vão no texto. "Estudos identificados por autor e ano; ordem por característica (tamanho do efeito, peso, ano, risco de viés), não alfabética; estimativa combinada com IC; τ², I² e intervalo de predição também no texto" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#visualização-dos-resultados>

### 5.4 Meta-análises com poucos estudos

- **R5.26** A agregação exige k ≥ 3. Com dois ou três estudos, os intervalos HKSJ e Wald aparecem lado a lado. "Com dois ou três estudos o HKSJ tende a dar intervalos largos demais e o Wald, estreitos demais; comparar os dois em sensibilidade" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#número-mínimo-de-estudos>
- **R5.27** O IC de τ² e o PI só são interpretados com cerca de cinco estudos ou mais. "O IC de τ² (Q-profile) e o intervalo de predição só são informativos com cerca de cinco estudos ou mais" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#número-mínimo-de-estudos>
  - Aqui: as duas metas exploratórias têm 3 estudos cada, abaixo desse limiar.
- **R5.28** No modelo CHE + RVE, resultado com menos de 4 graus de liberdade de Satterthwaite não é confiável. "A skill trata gl < 4 como resultado não confiável" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#dependência-de-efeitos>
  - Aqui: a meta da célula principal “sem pesquisa” usa `--dependencia che`.
- **R5.29** Resultados por célula, no mínimo: "por célula, k, número de participantes, estimativa com IC, τ² com IC, τ, I², intervalo de predição, estudos que contribuem e seu risco de viés" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-relato>
- **R5.30** Com menos de dez estudos, o texto diz que não houve teste de assimetria. "com menos de dez estudos, não testamos assimetria" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-relato>
- **R5.31** A heterogeneidade é interpretada por τ e pelo PI, na escala do efeito, e não só pelo I². "O que orienta decisão substantiva é τ, na escala do efeito, e o intervalo de predição." — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#heterogeneidade-q-τ²-i²-e-intervalo-de-predição>
- **R5.32** Resultado com I² alto ou PI que cruza zero não é chamado de "consistente". "Linguagem guiada pelo PI e pela sensibilidade" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-erros>
- **R5.33** As análises de sensibilidade vão numa tabela, não em vários *forest plots*. "Resumir numa tabela, não em vários forest plots" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-passos>
- **R5.34** Com menos de quatro estudos por nível, as estimativas por nível vêm lado a lado, e o texto declara que a diferença não foi testada. "Abaixo disso, a revisão apresenta as estimativas por nível lado a lado e declara que não testou a diferença." — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#número-mínimo-de-estudos>

### 5.5 Certeza, frases padronizadas e tabela SoF (§10.1)

- **R5.35** A certeza é julgada em relação a um limiar ou a uma faixa declarados. "Certeza é sempre relativa a um limiar ou a uma faixa" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#níveis-e-limiares>
- **R5.36** Cada conclusão de efeito usa a frase que combina certeza e tamanho do efeito (Santesso et al. 2020; Cochrane Handbook, Tabela 15.6.b). Transcrição da tabela; <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#linguagem-padronizada-das-conclusões>

  | Certeza | Efeito grande | Efeito médio | Efeito pequeno e relevante | Trivial ou nenhum |
  |---|---|---|---|---|
  | Alta | X resulta em grande aumento/redução de Y | X aumenta/reduz Y | X aumenta/reduz Y ligeiramente | X resulta em pouca ou nenhuma diferença em Y |
  | Moderada | X provavelmente resulta em grande aumento/redução de Y | X provavelmente aumenta/reduz Y | X provavelmente aumenta/reduz Y ligeiramente | X provavelmente resulta em pouca ou nenhuma diferença em Y |
  | Baixa | X pode resultar em grande aumento/redução de Y | X pode aumentar/reduzir Y | X pode aumentar/reduzir Y ligeiramente | X pode resultar em pouca ou nenhuma diferença em Y |
  | Muito baixa | A evidência é muito incerta sobre o efeito de X em Y | Idem | Idem | Idem |

- **R5.37** Em português, o tamanho usa "efeito médio" no lugar de "efeito moderado", para não se confundir com certeza moderada. "A adaptação transcultural para o português brasileiro recomenda “efeito médio” no lugar de “efeito moderado”, para não confundir tamanho com certeza moderada" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#linguagem-padronizada-das-conclusões>
- **R5.38** Ausência de evidência não é evidência de ausência. Com IC que inclui zero, não se escreve "não tem efeito". "se o IC inclui zero, não se escreve “não tem efeito”, e se ele é compatível com benefício e dano, as duas possibilidades são mencionadas" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#linguagem-padronizada-das-conclusões>
- **R5.39** Cada conclusão é lida às cegas, invertendo a direção, para detectar enquadramento otimista. "A conclusão é lida “às cegas”, invertendo a direção do resultado, para detectar enquadramento otimista." — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#linguagem-padronizada-das-conclusões>
- **R5.40** A interpretação usa estimativas e ICs, sem a dicotomia significativo/não significativo (MECIR C72). "a interpretação usa estimativas e ICs, sem a dicotomia “significativo / não significativo”" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#linguagem-padronizada-das-conclusões>
- **R5.41** "Nulo" ou "sem efeito" só com IC inteiro dentro de ±δ e certeza ao menos moderada. "“Nulo” só com IC dentro de ±δ e certeza ≥ moderada" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-erros>
- **R5.42** A tabela de risco de viés é separada do perfil GRADE e não o substitui. "Tabela de risco de viés (Seção 6.1) separada do perfil GRADE" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-erros>
- **R5.43** A tabela SoF tem colunas fixas, e desfecho sem meta-análise entra com resumo narrativo. "Montar a tabela SoF: população e cenário, comparação, desfechos, magnitude, participantes e estudos, certeza, comentários e explicações; desfechos sem meta-análise entram com resumo narrativo" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-passos>
- **R5.44** Cada tabela SoF tem no máximo sete desfechos, número fixado no protocolo. "até sete desfechos por tabela SoF" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-passos>
- **R5.45** Há uma tabela SoF por comparação, com a certeza e a explicação de cada rebaixamento ou elevação. "Tabela SoF por comparação, com certeza e explicação de cada rebaixamento ou elevação" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-relato>
- **R5.46** Na tabela de resumo dos achados, os motivos de rebaixamento vão em notas. "Nível de certeza e motivos de rebaixamento em notas" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#visualização-dos-resultados>
- **R5.47** Moderador de credibilidade baixa ou muito baixa aparece como hipótese, e o moderador testado fica separado da hipótese. "na caixa, moderador com credibilidade baixa ou muito baixa aparece como hipótese" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#credibilidade-de-moderadores>
- **R5.48** Na caixa, "Escala" é magnitude e "Força" é a certeza GRADE; nunca é magnitude ou significância. "“Força” na caixa é força da evidência." — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#da-certeza-à-caixa-de-ferramentas>
- **R5.49** Os rótulos seguem uma ordem fixa (regra caixa-3). "sem juízo de certeza, “Pendente”; certeza muito baixa, “Inconclusivo”; “Misto” (só com k ≥ 5, δ e achado explicativo com confiança própria; senão, “Inconclusivo”); “Positivo” ou “Negativo”; “Nulo”; “Inconclusivo” nos demais casos" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#regras-para-gerar-o-painel>
- **R5.50** Sem meta-análise, o rótulo "Positivo" tem condições próprias:
  - teste de sinal com p < 0,05;
  - pelo menos 5 estudos, com 70% ou mais benéficos;
  - não só estudos de alto risco;
  - certeza mínima baixa.

  "Estimativa benéfica com IC que exclui zero; sem meta-análise, teste de sinal p < 0,05, ≥ 5 estudos, ≥ 70% benéficos, não só estudos de alto risco" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#da-certeza-à-caixa-de-ferramentas>
- **R5.51** Nenhum rótulo é publicado sem regra escrita e versionada, aplicada à tabela-fonte do artigo. "Nenhum rótulo (Positivo, Moderada, Baixo) é publicado sem regra escrita, versionada e aplicada à mesma tabela-fonte que alimenta o artigo." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#que-produto-para-que-público>
- **R5.52** "Neutro" não é usado, e a magnitude não aparece se não houver faixa declarada. "Sem faixa declarada, a magnitude não aparece." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#regras-para-gerar-o-painel>
- **R5.53** O texto de cada linha é gerado da mesma tabela que gera o rótulo, com as frases padronizadas. "O texto da linha é gerado da mesma tabela que gera o rótulo, com as frases padronizadas por certeza da Seção 10.1." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#regras-para-gerar-o-painel>

## 6. Discussão, limitações e implicações

- **R6.1** A discussão cobre os itens 23a a 23d. "Interpretação à luz de outras evidências; limitações da evidência; limitações do processo da revisão; implicações para prática, política e pesquisa" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-diretrizes>
- **R6.2** As conclusões interpretam os achados diante de outras revisões, e as limitações do processo ficam em subseção própria. "Interpretação diante de outras revisões; limitações do processo em subseção própria" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-oqf>
- **R6.3** As limitações do processo (23c) têm conteúdo mínimo. "Item 23c: idiomas, bases, número de revisores, filtros automáticos, triagem por IA, relatos não recuperados, análises planejadas e não feitas" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-oqf>
- **R6.4** As limitações não são transferidas para a literatura: a revisão diz o que fez e o que deixou de fazer. "Dizer o que a revisão fez com a heterogeneidade e o que deixou de fazer" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#revisão-de-estilo>
- **R6.5** O artigo tem as seções Campbell sobre vieses do processo e diferenças em relação ao protocolo. "“vieses potenciais no processo da revisão” e “diferenças entre protocolo e revisão”" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-diretrizes>
- **R6.6** As limitações da síntese e dos agrupamentos são relatadas (SWiM 9). "Limitações dos métodos de síntese e dos agrupamentos" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-diretrizes>
- **R6.7** A interpretação segue os Campbell Standards 7a a 7d. "Interpretar magnitude à luz da credibilidade; discutir a incerteza (heterogeneidade); interpretar à luz da diretividade (generalização, validade externa e de construto); implicações na medida justificada por 7a-7c" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-diretrizes>
- **R6.8** Os verbos das implicações são proporcionais à certeza. Transcrição da tabela; <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#implicações-proporcionais-à-certeza>

  | Certeza do efeito principal | Transferibilidade ao contexto de uso | Implicação admissível | Verbo típico |
  |---|---|---|---|
  | Alta ou moderada | Sem preocupações sérias | Opção favorecida, com condições de implementação e monitoramento | “adotar”, “priorizar” |
  | Alta ou moderada | Preocupações moderadas ou sérias | Condicional aos fatores de transferibilidade; piloto ou implementação restrita | “considerar, desde que” |
  | Baixa | Qualquer | Condicional; só com avaliação de impacto ou piloto; dizer o que mudaria a conclusão | “pode ser considerada, com avaliação” |
  | Muito baixa | Qualquer | Nenhuma implicação de adoção baseada em efetividade; implicações de pesquisa e de desenho de avaliação | “a evidência não permite concluir” |

- **R6.9** Nenhuma implicação é mais forte que a certeza. "a exigência da especificação (Seção D.4) de que nenhuma implicação seja mais forte que a certeza" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#implicações-proporcionais-à-certeza>
- **R6.10** O texto deixa explícito que a decisão cabe a quem tem mandato. "deixar explícito que a decisão cabe a quem tem mandato para tomá-la" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#implicações-proporcionais-à-certeza>
- **R6.11** As implicações para pesquisa saem dos domínios que rebaixaram a certeza. "implicações para pesquisa saem dos domínios que rebaixaram a certeza (risco de viés pede estudos melhores; indireção, estudos no contexto de uso; imprecisão, mais participantes)" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-passos>
- **R6.12** Implicação condicional diz as condições; com incerteza importante, as conclusões incluem monitoramento e avaliação. "recomendações condicionais precisam dizer quais condições favorecem ou desfavorecem a opção, e monitoramento e avaliação fazem parte das conclusões quando há incerteza importante" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#critérios-etd-para-decisões-de-política-pública>
- **R6.13** O EtD-lite liga cada critério ao que a revisão fornece. Transcrição resumida (critério → o que a revisão fornece); <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#critérios-etd-para-decisões-de-política-pública>
  - Prioridade do problema → Introdução e contexto da política.
  - Efeitos desejáveis e indesejáveis → Células de efeito com magnitude e GRADE, incluindo efeitos perversos do DAG (Seção 2.1).
  - Certeza → Tabela SoF.
  - Valores → Achados de percepção com CERQual.
  - Balanço → Julgamento explícito com as linhas anteriores.
  - Recursos e custo-efetividade → Linha “custo” da caixa; “não reportado” quando não houver.
  - Equidade → Moderadores (vulnerabilidade, renda, região) com ICEMAN ou CERQual.
  - Aceitabilidade → Achados de percepção com CERQual.
  - Viabilidade → Linha “implementação” da caixa.
  - Transferibilidade ao Brasil → Avaliação TRANSFER.
- **R6.14** A transferibilidade é julgada, nunca presumida. "Regra do projeto: transferibilidade é julgada (indireção no GRADE, relevância no CERQual, TRANSFER), nunca presumida." — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#indireção-em-avaliação-de-políticas>
- **R6.15** A revisão examina a validade externa, mas não a concede. "A revisão ajuda a examinar a validade externa (heterogeneidade, moderadores, contextos cobertos), mas não a concede." — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#indireção-em-avaliação-de-políticas>
- **R6.16** A transferibilidade não gera um segundo rebaixamento, e o texto registra em que domínio cada fator foi contado. "Se a indireção já foi rebaixada por diferença de contexto, a mesma diferença não rebaixa de novo no EtD nem na relevância CERQual." — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#fatores-candidatos-para-o-brasil>
- **R6.17** O artigo relata os fatores de transferibilidade, como foram escolhidos e o julgamento de cada um. "Fatores de transferibilidade, como foram escolhidos e o julgamento por fator" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-relato>
- **R6.18** Um fator candidato para o Brasil é a escassez de estudos de países de renda média e baixa. "Escassez de estudos de países de renda média e baixa, que pode exigir pesquisa primária local em vez de transposição" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#fatores-candidatos-para-o-brasil>
- **R6.19** As opções aparecem lado a lado, com a mesma métrica e a mesma escala de certeza. "Apresentar opções lado a lado, com a mesma métrica de magnitude e a mesma escala de certeza" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#para-quem-se-escrevem-as-implicações>
- **R6.20** Cada implicação se liga ao marco normativo. Com certeza baixa, a revisão pode reenquadrar o problema sem virar recomendação. "Ligar cada implicação ao marco normativo e às exigências de controle; com certeza baixa, a revisão ainda pode reenquadrar o problema, sem virar recomendação" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#para-quem-se-escrevem-as-implicações>
- **R6.21** As implicações são opções condicionadas, não receitas universais. "Opções condicionadas, com os valores em jogo explícitos, entregues no tempo da decisão, e não receitas universais" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#para-quem-se-escrevem-as-implicações>

## 7. Informações adicionais: registro, financiamento, conflitos, dados e código, IA

- **R7.1** Registro, financiamento, conflitos, dados e código e uso de IA aparecem sempre, mesmo que a resposta seja "não houve". "Registro, financiamento, conflitos de interesse, disponibilidade de dados e código e uso de IA aparecem sempre, mesmo quando a resposta é “não houve”" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#que-produto-para-que-público>
- **R7.2** O registro e as emendas vêm com a mudança, o motivo e a etapa; seguem-se financiamento, conflitos, disponibilidade e declaração de IA. "registro e emendas com a mudança, o motivo e a etapa (24a-c)" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-passos>
- **R7.3** Toda emenda é datada e rastreada. "Toda emenda é datada e rastreada, e o relato informa a mudança, o motivo e a etapa em que ocorreu" — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-regras>
- **R7.4** O relato responde o que foi decidido depois de ver os dados. "O log de desvios responde a uma pergunta que o leitor sempre faz: o que foi decidido depois de ver os dados?" — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-log>
- **R7.5** A ausência se declara no item correspondente. "Revisão sem registro, sem protocolo ou sem dados públicos diz isso nos itens correspondentes" — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-regras>
- **R7.6** Financiamento (item 25) e conflitos (item 26) têm itens próprios. "financiamento (25); conflitos (26); disponibilidade (27); declaração de IA (Seção 12.15)" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-passos>
- **R7.7** O item 27 diz quais materiais estão públicos e onde. "O item 27 do PRISMA 2020 pede que se diga quais materiais estão públicos e onde: formulários de coleta, dados extraídos, dados usados nas análises, código e outros materiais" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#pacote-aberto-de-dados-e-código>
- **R7.8** Cada material tem o endereço exato; o link não pode levar a outro documento. "Declaração do item 27 com cada material e endereço exato" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-erros>
- **R7.9** O pacote aberto tem arquivos definidos. Transcrição (arquivo → item); <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#pacote-aberto-de-dados-e-código>
  - README → 27;
  - Protocolo e log de emendas → 24;
  - Log de buscas e strings → 6, 7; PRISMA-S;
  - Registros e decisões → 8, 16;
  - Contagens do fluxograma → 16a;
  - Codebook e formulário → 9, 10;
  - Dados extraídos → 10, 19;
  - Risco de viés → 11, 18;
  - Tabela de conversões → 13b;
  - Código e ambiente → 13d, 27;
  - Tabela-fonte e regra de rótulos → 22;
  - Prompts, modelos e validação de IA → 8, 9; Seção 12.15.
- **R7.10** O identificador persistente do depósito aparece no artigo e em cada produto derivado. "Identificador persistente do depósito aparece no artigo, na síntese de evidências e em cada produto derivado" — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-pacote>
  - Aqui: o repositório GitHub é privado, e o GitHub Pages só publica os documentos. O item 27 precisa dizer o que é público e onde; o que não estiver depositado entra como ausência (R7.5).
- **R7.11** Exportações de bases licenciadas ficam de fora: o pacote leva identificadores e decisões. "IDs e decisões no pacote; resumos só se a licença permitir" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-erros>
- **R7.12** Os PDFs dos estudos não entram no pacote. "PDFs dos estudos não entram no pacote." — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-pacote>
- **R7.13** Cada componente do material próprio declara uma licença explícita. "declare uma licença explícita no README de cada componente. A skill revisao-sistematica adota MIT para o código e CC BY 4.0 para textos, modelos e codebooks" — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-licencas>
- **R7.14** O código roda do zero, com as versões dos pacotes registradas. "Código roda do zero num ambiente limpo, com as versões dos pacotes usados na análise registradas junto dos scripts" — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-pacote>
- **R7.15** Os termos de envio de textos a provedores de IA são conferidos e relatados. "os acordos de processamento e de confidencialidade são conferidos antes do uso e relatados" — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-licencas>
- **R7.16** Dados pessoais são removidos ou tratados conforme a LGPD. "Dados pessoais (de autores contatados, de participantes de validação) são removidos ou tratados conforme a LGPD" — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-pacote>
- **R7.17** O relato de IA tem quatro partes, e a decisão de usar IA é relatada desde o protocolo. "O relato mínimo tem quatro partes: o plano de IA no protocolo, um parágrafo de métodos por etapa com IA, os resultados da validação e a declaração de uso de IA." — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-relato>
- **R7.18** Declara-se todo uso de IA que faz ou sugere julgamento. Isso inclui textos que resumem a força da evidência e as implicações, e o resumo em linguagem simples. "Declarar o uso de IA sempre que ela fizer ou sugerir julgamentos sobre elegibilidade, avaliação crítica (inclusive risco de viés), extração de dados bibliográficos, numéricos ou qualitativos, síntese de dois ou mais estudos, certeza da evidência, textos que resumem a força da evidência e suas implicações, ou resumos em linguagem simples" — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-diretrizes>
  - Aqui: subagentes escreveram os números do manuscrito a partir dos arquivos (`CLAUDE.md`, seção “Armadilhas”), e isso entra na declaração.
- **R7.19** A declaração de IA tem conteúdo mínimo (RAISE 1.9):
  - nome, versão e datas de uso;
  - finalidade e partes afetadas;
  - justificativa e validação;
  - interesses e financiamento da ferramenta;
  - limitações.

  "Relatar: nome, versão e datas de uso; finalidade e partes da revisão afetadas" — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-diretrizes>
- **R7.20** Os itens 8, 9 e 11 do PRISMA dizem como a automação entrou em cada etapa. "no item 8, como a automação se integrou à seleção (por exemplo, se registros foram excluídos só por avaliação de máquina ou se a máquina conferiu decisões humanas)" — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-diretrizes>
- **R7.21** O PRISMA-trAIce serve só como lista de conferência; o artigo não declara conformidade com ele. "usando o PRISMA-trAIce como lista de conferência, sem declarar conformidade com ele" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-diretrizes>
- **R7.22** A declaração de IA é gerada do log, com métricas e IC; não se reduz a uma frase. "Declaração gerada do log, com métricas e IC" — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-erros>
- **R7.23** Em produto do autopiloto, a primeira linha da declaração é "RASCUNHO NÃO VALIDADO", seguida das pendências. "Em produtos do autopiloto, a primeira linha da declaração é “RASCUNHO NÃO VALIDADO”, seguida da lista de pendências." — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-relato>
- **R7.24** Nenhum produto do autopiloto é apresentado como revisão concluída. "Nenhum produto do autopiloto pode ser apresentado como revisão sistemática concluída." — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-skill>
- **R7.25** Quando a validação não aprova o uso de IA, o texto diz isso com os números. "Relato honesto de não aprovação é resultado metodológico." — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-relato>
- **R7.26** A responsabilidade é humana, inclusive pela decisão de usar IA. "A equipe responde pelo conteúdo, pelos métodos e pelos achados, incluindo a decisão de usar IA, o modo de uso e o impacto dela na síntese" — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-regras>
- **R7.27** O LLM que rascunha texto se limita à estrutura e a seções descritivas; não resume nem interpreta resultados entre estudos. "Exploratório; não resumir nem interpretar resultados entre estudos" — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-regras>
- **R7.28** Agentes que executam a revisão de ponta a ponta não são uso aceitável, e o produto deles não conta como revisão sistemática. "Nenhum produto desse tipo conta como revisão sistemática" — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-regras>
- **R7.29** Uso de IA só para ortografia, gramática ou estrutura em geral não precisa ser listado, salvo política do periódico. "o uso apenas para ortografia, gramática ou estrutura do manuscrito em geral não precisa ser listado, ressalvada a política de cada periódico" — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-diretrizes>
- **R7.30** A divulgação é registrada: onde e quando cada produto circulou. "Executar o plano de disseminação e registrar onde e quando cada produto circulou." — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-passos>

## 8. Auditoria final (checklist de aceite)

Os itens A1 a A12 são a tabela "Auditoria final" da §11.5. Os itens A13 a A20 são a tabela "Revisão de estilo" da mesma seção; o passo a passo manda "fazer a revisão de estilo e rodar a auditoria final (tabelas abaixo)". Os itens A21 a A36 vêm de outras seções, indicadas em cada um. Em cada item, o critério de aprovação é transcrito do livro.

### 8.1 Tabela "Auditoria final" (§11.5) — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#auditoria-final>

- [ ] **A1 Fluxograma.** "Somas fecham; template com ramo de outras fontes quando houve; humano e automação separados; número por base" (Page, Moher, et al. 2021, 16a)
- [ ] **A2 Consistência numérica.** "Mesmos números no resumo, texto, tabelas, figuras, caixa, painel e derivados" (The Campbell Collaboration 2016, 8)
- [ ] **A3 Certeza.** "Em todo enunciado de efeito e em toda linha da caixa e do painel" (Page, Moher, et al. 2021, 22)
- [ ] **A4 Rótulos.** "Cada rótulo reproduzível pela regra versionada a partir da tabela-fonte" (Seção 11.3)
- [ ] **A5 Figuras.** "Estudos por autor e ano, ordem explicada, rótulos conferidos contra o texto" (Page, Moher, et al. 2021, 13c)
- [ ] **A6 Heterogeneidade.** "τ², I² e intervalo de predição no texto" (Page, Moher, et al. 2021, 20b)
- [ ] **A7 Testes combinados.** "Interpretação coerente com a pergunta que o teste responde" (Page, Moher, et al. 2021, 20b)
- [ ] **A8 Citações.** "Toda chamada corresponde a uma referência com o mesmo ano" (Costa 2021, 4, 8)
- [ ] **A9 Limitações.** "Evidência e processo em subseções distintas" (Page, McKenzie, et al. 2021, 23b, 23c)
- [ ] **A10 Informações adicionais.** "Registro, emendas, financiamento, conflitos, dados e código, IA; DOI e links abrem o material indicado" (Page, McKenzie, et al. 2021, 24–27)
- [ ] **A11 Checklists e resumo.** "PRISMA 2020 e extensões com página de cada item; 12 itens do resumo" (Page, McKenzie, et al. 2021)
- [ ] **A12 Resumo em linguagem simples.** "600 a 750 palavras, todos os desfechos principais, data da busca" (The Campbell Collaboration 2016, 5–9)

### 8.2 Tabela "Revisão de estilo" (§11.5) — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#revisão-de-estilo>

Cada item: o problema que não pode aparecer, seguido de *como reescrever*.

- [ ] **A13** Sem "Explicação didática do método dentro da Metodologia". Como reescrever: "Cortar ou mover para a introdução; a Metodologia diz o que esta revisão fez".
- [ ] **A14** Sem "Narrar o percurso em vez do método". Como reescrever: "“Dois revisores extraíram, de forma independente, …”".
- [ ] **A15** Sem "Parâmetro ausente". Como reescrever: "Quem triou, quantos, com que concordância, com que ferramenta e versão".
- [ ] **A16** Sem "Adjetivo no lugar de número". Como reescrever: "“g = 0,22 (IC 95% 0,02 a 0,42; I² = 76,5%)”".
- [ ] **A17** Sem "Termo com vários sentidos". Como reescrever: "“Magnitude” para o tamanho, “certeza” para a confiança e significância só como estatística relatada".
- [ ] **A18** Sem "Ícones no lugar de números". Como reescrever: "“7 de 8 estimativas na direção benéfica”".
- [ ] **A19** Sem "Limitação transferida para a literatura". Como reescrever: "Dizer o que a revisão fez com a heterogeneidade e o que deixou de fazer".
- [ ] **A20** Sem "Numeração de figuras fora de ordem". Como reescrever: "Numerar na ordem de aparição e conferir cada chamada".

### 8.3 Conferências de outras seções do livro

- [ ] **A21** O relatório foi revisto pela equipe inteira antes de circular. "O relatório deve ser revisto pela equipe inteira antes de circular" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#revisão-de-estilo>
- [ ] **A22** O passe final de linguagem usou a skill tirar-cara-de-ia. "O passe final de linguagem usa a skill tirar-cara-de-ia" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#revisão-de-estilo>
- [ ] **A23** Cada conclusão foi lida às cegas, com a direção invertida. "A conclusão é lida “às cegas”, invertendo a direção do resultado, para detectar enquadramento otimista." — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#linguagem-padronizada-das-conclusões>
- [ ] **A24** Nenhum enunciado usa a dicotomia significativo/não significativo. "a interpretação usa estimativas e ICs, sem a dicotomia “significativo / não significativo”" — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#linguagem-padronizada-das-conclusões>
- [ ] **A25** Todo teste combinado, incluindo o teste de sinal, vem com a ressalva de R5.18. "ressalva obrigatória para qualquer teste combinado" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-relato>
- [ ] **A26** As metas com menos de dez estudos trazem a frase sobre assimetria. "com menos de dez estudos, não testamos assimetria" — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-relato>
- [ ] **A27** A declaração de IA abre com "RASCUNHO NÃO VALIDADO" e a lista de pendências, enquanto houver pendência. "Em produtos do autopiloto, a primeira linha da declaração é “RASCUNHO NÃO VALIDADO”, seguida da lista de pendências." — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-relato>

Lista "Antes de depositar, confira" (Apêndice B.4) — <https://felipelamarca.com/Systematic-Review/metodo/apendice-b-reprodutibilidade.html#sec-apb-pacote>

- [ ] **A28** "README descreve cada arquivo, a versão da revisão e a ordem para reproduzir, do arquivo de registros ao relatório."
- [ ] **A29** "Fluxograma reproduzível: as contagens publicadas saem das tabelas de registros e decisões incluídas no pacote."
- [ ] **A30** "Código roda do zero num ambiente limpo, com as versões dos pacotes usados na análise registradas junto dos scripts"
- [ ] **A31** "Tabela de conversões acompanha os dados extraídos, com fórmula e pressupostos de cada efeito convertido"
- [ ] **A32** "Tabela-fonte da caixa de ferramentas e a versão da regra de rótulos permitem refazer cada rótulo"
- [ ] **A33** "Prompts, saídas brutas e métricas de validação estão presentes quando houve uso de IA"
- [ ] **A34** "Material protegido fica de fora" (exportações licenciadas e PDFs; no lugar dos resumos, identificadores e decisões).
- [ ] **A35** "Dados pessoais (de autores contatados, de participantes de validação) são removidos ou tratados conforme a LGPD"
- [ ] **A36** "Identificador persistente do depósito aparece no artigo, na síntese de evidências e em cada produto derivado"

## 9. Frases-modelo

### 9.1 §11.10 "Como relatar" — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#sec-10-relato>

O livro avisa: "O relatório precisa conter, no mínimo, os blocos abaixo. Os exemplos usam a revisão dos celulares; colchetes marcam o que depende do projeto." Os números abaixo são do exemplo dos celulares, não desta revisão.

**M1. Conformidade com diretrizes (Metodologia).**

> Esta revisão segue o PRISMA 2020, com as extensões PRISMA-S para a busca e SWiM para as sínteses sem meta-análise, e o ENTREQ para a síntese qualitativa. Os checklists preenchidos, com a página de cada item, estão no Apêndice [A].

**M2. Fluxograma (Resultados).**

> A busca em quatro bases, em [data], identificou 1.740 registros (Google Scholar 400, SciELO 87, Scopus 798, Web of Science 455). Antes da triagem, foram removidos 223 duplicados, 135 registros por filtros de metadado [previstos no protocolo] (ano, 87; tipo de documento, 48) e 641 por dicionários aplicados ao resumo (metodologia, 592; tema, 49). [Duas revisoras] triaram 741 títulos e resumos, [de forma independente], e excluíram [n]. Dos [n] relatos buscados, [n] não foram recuperados; dos [n] avaliados em texto completo, [n] foram excluídos (motivos na Figura [x]). [n] estudos vieram das bases e [n] da busca de citações em duas revisões anteriores, que não entram como estudos incluídos.

**M3. Limitações do processo (Conclusões e limitações).**

> A exclusão por dicionários aplicados ao resumo pode ter eliminado estudos relevantes sem termos metodológicos no resumo; não medimos a sensibilidade desses filtros. A busca ficou restrita a português e inglês e a estudos revisados por pares, sem notas técnicas. [A triagem foi feita por uma revisora, com verificação de [n]% dos registros por outra.] [Não contatamos autores para dados faltantes.]

**M4. Da evidência à prática: implicações.**

> Os rótulos da caixa de ferramentas seguem a regra v[1.0] (Apêndice [B]), aplicada à tabela de achados disponível no pacote aberto. Cada linha informa a certeza da evidência, e nenhuma implicação é mais forte do que essa certeza.

**M5. Registro e protocolo.**

> Registro e protocolo. O protocolo foi registrado no OSF em [data] ([DOI]); as [n] emendas estão no log, com a mudança, o motivo e a etapa em que ocorreram. [Ou: A revisão não foi registrada e não houve protocolo prévio.]

**M6. Financiamento.**

> Financiamento. [Fonte]; o financiador não teve papel no desenho, na análise nem na redação. [Ou: A revisão não recebeu financiamento específico.]

**M7. Conflitos de interesse.**

> Conflitos de interesse. [Declaração.]

**M8. Disponibilidade de dados, código e materiais.**

> Disponibilidade de dados, código e materiais. Estão em [DOI do OSF]: o formulário de extração, os dados extraídos de cada estudo, os dados usados nas análises, o código em R, a tabela de achados com a regra de rótulos e a lista de registros triados com as decisões. Os resumos exportados das bases não foram incluídos por restrição de licença.

**M9. Uso de inteligência artificial.**

> Uso de inteligência artificial. [Declaração gerada conforme a Seção 12.15.]

**M10. Divulgação.**

> Além deste artigo, os achados foram publicados como síntese de evidências, resumo em linguagem simples e linha no painel O Que Funciona ([endereço]), gerados da mesma tabela de achados e da regra de rótulos v[1.0], e apresentados a [públicos] em [datas].

### 9.2 Frases-modelo de outros capítulos

Estas frases usam o exemplo dos celulares. Os colchetes e os valores ilustrativos dependem do projeto.

**M11. Certeza (métodos e resultados)** — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#sec-09-relato>. O livro avisa que o limiar, as avaliadoras e os gestores do exemplo são hipotéticos.

> A certeza da evidência foi avaliada com GRADE para cada combinação de intervenção e desfecho, por duas pesquisadoras de forma independente, com consenso. Ensaios randomizados partiram de certeza alta; estudos não randomizados avaliados com ROBINS-I partiram de alta e foram rebaixados conforme o julgamento de risco de viés. A imprecisão foi julgada em relação ao limiar de 0,10 desvio-padrão fixado no protocolo, e a inconsistência pela dispersão das estimativas, pelo I² e pelo intervalo de predição.

> Para o desempenho acadêmico, a certeza foi muito baixa (rebaixada por risco de viés, inconsistência, indireção e imprecisão; tabela 4): a evidência é muito incerta sobre o efeito da proibição. Há confiança baixa de que atribuir a fiscalização apenas aos professores gera tensões em sala. Não recomendamos justificar a política por ganhos de aprendizagem; redes que a implementarem podem acompanhar cumprimento, conflitos e desempenho com desenho que permita avaliação de impacto.

**M12. Linha de tabela SoF (ilustrativa)** — <https://felipelamarca.com/Systematic-Review/metodo/09-certeza-evidencia-pratica.html#o-que-deveria-ser-feito-grade-reconstruído>

> Estudantes da educação básica e superior de 12 países; proibição ou restrição × ausência de restrição; desempenho acadêmico (medidas diversas); g = 0,22 (0,02 a 0,42), intervalo de predição de −0,28 a 0,71; 8 estimativas; ⊕◯◯◯ muito baixa (risco de viés, inconsistência, indireção, imprecisão).

**M13. Métodos de síntese** — <https://felipelamarca.com/Systematic-Review/metodo/08a-sintese-quantitativa.html#sec-08a-relato>

> Só combinamos estudos da mesma família de intervenção e construto de desfecho, com comparador, janela, população e estimando equivalentes; randomizados e não randomizados foram analisados em separado.

> Sem meta-análise, usamos contagem pela direção da estimativa pontual com teste de sinal exato bilateral, proporção com IC de Clopper-Pearson e effect direction plot, seguindo o SWiM.

**M14. Redação que atende aos itens 13c, 20a, 20b e 22** — <https://felipelamarca.com/Systematic-Review/metodo/10-relato-divulgacao.html#celulares-a-seção-3.1-e-o-forest-plot>

> Oito estimativas de desempenho foram combinadas em modelo de efeitos aleatórios (REML, IC de Hartung-Knapp; Figura [x], estudos ordenados por precisão e identificados por autor e ano): g = 0,22 (IC 95% 0,02 a 0,42; τ² = 0,037; I² = 76,5%; intervalo de predição de −0,28 a 0,71).

> A evidência é muito incerta sobre o efeito da proibição no desempenho (certeza muito baixa, rebaixada por risco de viés, inconsistência, indireção e imprecisão; Tabela [y]).

**M15. Risco de viés, resultados** — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#sec-06-relato>

> Resultados. Dos [n] resultados de ensaios, [n] tiveram risco baixo, [n] algumas preocupações e [n] alto; dos [n] não randomizados, [n] moderado, [n] grave e [n] crítico (Figura X). O domínio mais vezes grave foi o confundimento. Sem os resultados de risco alto ou grave, a estimativa passou de [valor] para [valor]. Houve [n] desacordos antes do consenso, concentrados em [domínio].

**M16. Risco de viés, métodos (trecho sobre a IA)** — <https://felipelamarca.com/Systematic-Review/metodo/06-qualidade-risco-vies.html#sec-06-relato>

> Um modelo de linguagem [modelo, versão] rascunhou respostas às perguntas-sinalizadoras com trecho e página; todos os julgamentos foram humanos.

Aqui: use só se for verdade no log. Enquanto as pendências humanas estiverem abertas, a frase não se aplica como está.

**M17. Declaração de uso de IA** — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-relato>

> Declaração de uso de inteligência artificial. Usamos [modelo A, versão] e [modelo B, versão], acessados por API entre [datas], para triagem de títulos e resumos, e [modelo C, versão] para propor elegibilidade em texto completo e rascunhar a extração de dados, sempre com trecho literal e página verificados por programa e conferidos por pessoas.

> Todas as decisões finais de inclusão, os juízos de risco de viés e a síntese foram feitos por pessoas, que assumem integral responsabilidade pelo conteúdo desta revisão.

Aqui: o modelo supõe portões humanos fechados. Neste autopiloto, a declaração abre com "RASCUNHO NÃO VALIDADO" e as pendências (R7.23), e só atribui a pessoas o que o log registra como humano.

**M18. Validação que não aprovou o LLM** — <https://felipelamarca.com/Systematic-Review/metodo/11-ia-na-revisao.html#sec-11-relato>

> “o limiar pré-especificado era inalcançável com [21] incluídos (limite inferior máximo possível de [0,839]); os modelos foram usados apenas como terceira leitura, e toda exclusão foi decidida por duas revisoras”
