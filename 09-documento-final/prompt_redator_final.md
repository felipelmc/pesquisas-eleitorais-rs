# Redação do documento final: revisão no formato *O que funciona?* (OQF) adaptado

Você escreve o documento final desta revisão sistemática em `09-documento-final/revisao_final.qmd`. O formato combina duas referências: as revisões OQF do MAPE (Laboratório de Monitoramento e Avaliação de Políticas e Eleições, IESP-UERJ; <https://mape.org.br/oqf/>; proposta metodológica de Schaefer, Borges e Freitas 2025) e a estrutura de revisões sistemáticas de revistas de referência (Campbell Systematic Reviews, PRISMA 2020). O público são pesquisadores de comportamento eleitoral, pessoas que acompanham o debate público sobre a divulgação de pesquisas e gestores de órgãos eleitorais. Idioma: português do Brasil.

Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Escreva só dentro de `09-documento-final/`. Não rode `rs.py`, não abra PDFs, não use a rede e não rode nada em segundo plano.

## Fontes, que você deve ler antes de escrever

- **O manuscrito técnico:** `07-relatorio/relatorio.qmd`. É a fonte principal de conteúdo e números: métodos, resultados, sensibilidades, GRADE, limitações, Emendas e declaração de IA. O documento final **não pode divergir dele em nenhum número**.
- **Números e tabelas prontos:**
  - `09-documento-final/insumos/tabelas/numeros.json` e as tabelas `*.md` dessa pasta, geradas por `07-relatorio/gerar_tabelas_relatorio.py`;
  - `09-documento-final/insumos/caixa_oqf_celulas.md`, `caixa_oqf_painel.md` e `caixa_oqf.json`, geradas por `09-documento-final/gerar_caixa_oqf.py`.

  Inclua as tabelas copiando o conteúdo; não digite números à mão.
- **Dossiês:**
  - `09-documento-final/insumos/contexto_brasil.md`, com o contexto legal e o debate brasileiro, as revisões anteriores e as chaves de `09-documento-final/referencias_contexto.bib`;
  - `09-documento-final/insumos/mecanismos_moderadores.md`, com a síntese descritiva de mecanismos e moderadores.
- **Arquivos de origem, para conferir:**
  - protocolo: `00-protocolo/protocolo.md`, `pergunta.md`, `teoria_programa.md`, `emendas.md`;
  - fluxo: `07-relatorio/prisma_contagens.json`;
  - síntese: `06-analise/certeza.csv`, `06-analise/certeza_agrupamento_amplo.csv`, `06-analise/swim_*/swim_resumo.json`, `06-analise/meta_exploratoria/meta_resumo.json`, `06-analise/meta_mesmo_candidato/meta_resumo.json`;
  - pendências: `07-relatorio/_pendencias_abertas.json` e `08-revisao-humana/README.md`.
- **Modelos de formato:**
  - `~/.claude/skills/revisao-sistematica/assets/templates/relatorio_oqf.qmd` e `policy_brief.qmd`;
  - `~/.claude/skills/revisao-sistematica/references/08-relato.md`, seções 5, 6 e 11: melhorias obrigatórias sobre o OQF e frases padrão de certeza.

## Estrutura do documento

**Cabeçalho (YAML):**
- `title: "Pesquisas eleitorais publicadas mudam o voto?"`;
- `subtitle: "Revisão sistemática rápida no formato *O que funciona?*"`;
- `author: "Felipe Lamarca (MAPE/IESP-UERJ)"`;
- `date: "24/09/2026 (rascunho)"`;
- `lang: pt-BR`;
- `bibliography: [../07-relatorio/references.bib, referencias_contexto.bib]`;
- formatos html (`toc: true`, `toc-depth: 2`, `number-sections: true`) e docx.

**Logo abaixo do título:**
- Um callout de aviso com "RASCUNHO NÃO VALIDADO". Ele diz que há `n` pendências humanas abertas (`n` de `_pendencias_abertas.json`), que toda etapa depois do protocolo foi feita por IA e que os resultados não devem ser citados como finais. Aponte para o apêndice de pendências.
- Um callout "Como ler este documento", em duas ou três frases: a certeza qualifica a direção, não o tamanho, e os rótulos seguem as regras da caixa de ferramentas.

**Seções (sem numeração nas duas primeiras):**

1. **Mensagens principais** (sem número). De 3 a 5 mensagens curtas. Cada uma tem a direção, o número de estudos e a certeza GRADE, com a frase padrão:
   - alta: "aumenta";
   - moderada: "provavelmente aumenta";
   - baixa: "pode aumentar";
   - muito baixa: "a evidência é muito incerta sobre…".

   Inclua uma mensagem sobre o Brasil (o único estudo brasileiro trata de apuração parcial oficial) e uma sobre o que a evidência não permite dizer.
2. **Resumo executivo** (sem número). Uma página em prosa, sem listas.
3. **Resumo estruturado e Abstract.** Resumo em português e *abstract* em inglês, estruturados em Objetivos, Métodos, Resultados, Conclusões e Registro/Financiamento, cada um com até 350 palavras.
4. **Contextualização:**
   - o problema no Brasil, a partir do dossiê: regras de divulgação e registro, a decisão do STF, as propostas de restrição, o debate sobre os "erros das pesquisas";
   - conceitos (*bandwagon*, *underdog*, voto estratégico, mobilização e desmobilização, *momentum*), a partir de Barnfield e do protocolo;
   - a pergunta X → Y e o PICOC em tabela;
   - revisões anteriores e o que esta revisão acrescenta;
   - a teoria de mudança em um parágrafo (DAG do protocolo).
5. **Efeito: a exposição a pesquisas muda o voto e o comparecimento?**
   - 5.1 Apoio a quem aparece à frente. Células separadas por desenho e comparador. Traga a tabela das células e as duas metas exploratórias, sempre como exploratórias, com gl < 4 e RVE não confiável.
   - 5.2 Viabilidade e voto estratégico.
   - 5.3 *Momentum*.
   - 5.4 Comparecimento.
   - 5.5 O que as sensibilidades mudam: só contexto real, com críticos, ICC 0,20, com excluídos.

   Em cada parágrafo de efeito: direção, quantos estudos, desenho, certeza e a frase padrão.
6. **Mecanismo: como funciona?** Síntese descritiva do dossiê, marcada como descritiva quando não houver certeza GRADE.
7. **Moderadores: para quem, onde e quando?** Mesma regra da seção 6.
8. **Percepção, implementação e custo.** Uma seção curta dizendo por que essas dimensões do OQF não se aplicam: a exposição a pesquisas não é um programa implementado por um gestor (`00-protocolo/pergunta.md`, protocolo §8). Diga o que faria sentido avaliar num estudo futuro, por exemplo, a percepção de eleitores sobre pesquisas e o custo regulatório de restrições.
9. **Caixa de ferramentas.**
   - Tabela no formato OQF, com linhas Escala, Força, Mecanismo, Moderador, Implementação, Percepção e Custo, para a pergunta principal (pesquisa pré-eleitoral × apoio). Uma coluna "Evidência" diz de onde vem cada linha, e uma coluna "Certeza" traz a certeza.
   - Em seguida, a tabela `caixa_oqf_celulas.md`, célula a célula.
   - Legenda dos rótulos: Positivo, Negativo, Misto, Nulo, Inconclusivo e Pendente, seguindo a regra caixa-3. Explique por que todas as células são "Inconclusivo".
   - "Neutro" é proibido.
10. **O que isso significa para o debate brasileiro.** Implicações sem recomendação mais forte que a certeza: não há "deve proibir" nem "deve liberar". Diga o que a evidência permite e o que não permite afirmar sobre restringir a divulgação, e liste os fatores de transferibilidade do protocolo: voto obrigatório, dois turnos, regulação da divulgação, confiança nas pesquisas. Feche com "Implicações para a pesquisa": estudos com eleição real no Brasil, desenhos com comparador sem pesquisa, pré-registro.
11. **Metodologia.**
    - Protocolo e emendas (E001, E002 e Emendas 1 a 6, em uma frase cada).
    - PICOC e critérios.
    - Fontes, strings e datas.
    - Seleção: triagem por IA, Emenda 6b e texto completo.
    - Fluxo PRISMA, com a figura `../07-relatorio/prisma.png` e as contagens.
    - Extração, com re-extração cega e arbitragem.
    - Risco de viés (RoB 2, ROBINS-I V2, EPOC).
    - Síntese: SWiM, δ, FORA, sensibilidades, metas exploratórias.
    - GRADE.
    - Uso de IA: que modelo fez o quê.
12. **Limitações.** 12.1 Da evidência. 12.2 Do processo, completo, como no manuscrito técnico, incluindo a Emenda 6 e a validação humana que falta.
13. **Informações adicionais:**
    - dados e código: o repositório privado felipelmc/pesquisas-eleitorais-rs e a página <https://felipelamarca.com/pesquisas-eleitorais-rs/>;
    - relatório técnico completo: `relatorio-tecnico.html` na mesma página;
    - financiamento: nenhum;
    - conflitos: nenhum;
    - declaração de uso de IA resumida, com link para a completa no relatório técnico;
    - como citar.
14. **Referências.**
15. **Apêndice A, "Pendências humanas abertas".** Uma tabela com as 18, com a tabela de `08-revisao-humana/README.md` como fonte, e o link `revisao-humana.html`.

## Marcações de revisão humana (obrigatórias; o autor pediu para mantê-las)

- **Onde vão:** no fim de cada seção que depende de validação humana, um callout `::: {.callout-important}` com o título "Pendente de revisão humana". Ele diz, em uma ou duas frases, qual pendência afeta aquela seção e o que falta.
- **Correspondência mínima entre seção e pendências:**
  - Efeito: P039, P037, P033 e P036/P042;
  - Mecanismo e Moderadores: P039 e P037;
  - Caixa: P036/P042 e P035;
  - Metodologia, busca: P001 e P004;
  - Metodologia, seleção: P019, P020, P006, P007, P008, P041 e P023;
  - Metodologia, extração: P025, P026, P039 e P037;
  - Metodologia, RoB: P033;
  - Documento inteiro: P038.
- **Pontos de julgamento:** onde couberem, cite os pontos de `08-revisao-humana/efeitos/pontos_para_o_revisor.md` que o autor precisa decidir, por exemplo o dicionário `FORA`, o rebaixamento por viés de publicação e o comparador de Grillo2024c.

## Regras

1. **Números.** Todo número vem de arquivo, nunca de memória. Use os números de `numeros.json` e das tabelas e confira com o manuscrito técnico. Se não achar um número, escreva que não foi relatado.
2. **Direção pelo estimador,** nunca pela significância. Nunca escreva "sem efeito" porque p > 0,05, e nunca use "Neutro".
3. **Certeza em toda afirmação de efeito.** Com SWiM, a certeza qualifica a direção, não a magnitude.
4. **Citações.** Estudos incluídos, com as chaves de `../07-relatorio/references.bib`; contexto, com as chaves de `referencias_contexto.bib`. Não invente chaves. Obras citadas em `contexto_brasil.md` sem chave vão com o link em nota.
5. **Estilo, já no primeiro rascunho** (depois haverá passes de voz):
   - Prosa corrida, com listas só onde o conteúdo for de fato uma lista.
   - Sem travessão (—) como pontuação; "--" é aceito.
   - Termos em inglês em itálico.
   - Frases de tamanho variado.
   - Sem "além disso" em série, sem "é importante ressaltar", sem tríades mecânicas, sem "não apenas X, mas também Y".
   - Primeira pessoa do plural quando o autor fala da revisão ("buscamos", "incluímos").
6. **Tamanho:** entre 20 e 25 páginas em A4, sem contar apêndices e referências.
7. **Ao terminar:**
   - rode `grep -nE '\{\{|a preencher|a conferir|—'` (a única ocorrência de travessão permitida é nenhuma, porque o aviso usa dois-pontos);
   - confira se toda `@chave` existe num dos dois `.bib`;
   - confira se os números do resumo, das mensagens e das tabelas são os mesmos.

Responda em UMA linha: `OK revisao_final.qmd: <n> palavras; chaves ok; callouts=<n>` ou `FALHA <motivo>`. Na linha seguinte, liste as dúvidas que o autor precisa decidir.
