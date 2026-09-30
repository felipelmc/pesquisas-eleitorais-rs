# Redação da versão de entrega: um bloco do artigo (Emenda 7)

Você é um dos três redatores da versão de entrega do artigo "Pesquisas eleitorais publicadas mudam o voto?", de Felipe Lamarca (MAPE/IESP-UERJ). O produto passa a se chamar "síntese sistemática de evidências conduzida com agentes de IA". O texto é em português do Brasil, com o *abstract* em inglês.

- Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. O caminho antigo `~/revisoes/pesquisas-eleitorais`, que aparece em arquivos, é só proveniência.
- A análise não muda: células, contagens, certezas e metas são as de 24/09/2026.
- O contrato é `09-documento-final/spec_final.md`. Siga-o à risca, e onde ele não disser nada vale a `spec_v2.md` (seções 0, 4 e 6).

## Seu bloco

O coordenador diz qual é o seu bloco (1, 2 ou 3) na mensagem que abre esta tarefa. Fronteiras, orçamento e leituras estão na seção 4 da especificação. Você escreve só os arquivos do seu bloco:

- Bloco 1: `09-documento-final/_blocos/bloco1.qmd`, do YAML até o fim de `## Uso de IA e conferência humana {#sec-ia}`.
- Bloco 2: `09-documento-final/_blocos/bloco2.qmd`, de `# Resultados {#sec-resultados}` até o fim de `## Moderadores {#sec-moderadores}`, e `09-documento-final/linguagem_simples.qmd` (seção 5 da especificação).
- Bloco 3:
  - `09-documento-final/_blocos/bloco3.qmd`, de `# Discussão {#sec-discussao}` até `# Referências`, com o Div `::: {#refs}`;
  - `09-documento-final/_esqueleto_suplemento.qmd`, os apêndices A a G (seção 3 da especificação);
  - `09-documento-final/revista/tabelas/lacunas.yml`, com as chaves `legenda`, `larguras`, `colunas` e `linhas` (seção 3.3).

  O coordenador junta os três blocos em `_esqueleto_revisao_final.qmd`. Não edite esse arquivo.

## Antes de escrever, leia

1. A `spec_final.md` inteira, com atenção às seções 1 (regras), 2 (estrutura) e 4 (a sua linha da tabela).
2. As linhas do esqueleto congelado `09-documento-final/_esqueleto_v2_2409.qmd` indicadas para o seu bloco. As referências `esq:Lnnn` da especificação apontam para esse arquivo, que é o texto de partida.
3. `/Users/felipelmc/.claude/commands/my-voice.md`, com a voz do autor.
4. As fontes listadas para o seu bloco na seção 4 da especificação.

## Regras que as travas conferem (resumo da seção 1 da especificação)

- **Números.**
  - Só entram números das fontes permitidas (seção 1.1) ou que já estejam no esqueleto congelado com o mesmo sentido.
  - Nenhuma conta nova, porcentagem nova ou contagem nova.
  - Nenhum dos números da lista "não entram".
- **Enunciados** (só no Bloco 2): `[<enunciado literal de revista/celulas.json>]{.enunciado cel="Cxx"}`, sem mudar uma vírgula. No mesmo parágrafo vão "certeza <nível>" e o k (seção 1.2).
- **Figuras e tabelas.**
  - Figuras e tabelas geradas entram só por marcador em linha própria (`@@FIGURA nome@@`, `@@TABELA nome@@`), com os nomes da seção 1.3, e são citadas por `@fig-`/`@tbl-`.
  - Quadros como no esqueleto congelado.
  - `@sec-` só para seção numerada.
  - Os apêndices, só por texto ("Apêndice C").
- **Proibições** (seção 1.4):
  - os termos "Neutro", "sem efeito", "benéfic", "danos", "significativ" e "revisão por pares";
  - travessão;
  - caminhos de arquivo em prosa;
  - nomes internos;
  - "suplemento";
  - "[A confirmar pelo autor]";
  - "Pendente de revisão humana";
  - a palavra "rascunho". A exceção é a abertura literal da declaração de IA (IA-7, Bloco 3), a única ocorrência de "RASCUNHO NÃO VALIDADO".
- **Datas:** só as da seção 1.5.
- **Direção e certeza** (seção 1.6): a direção vem do estimador, nunca da significância. A certeza qualifica a direção, e não a magnitude. Nenhuma recomendação acima da certeza.
- **Marcas da versão de entrega** (seção 1.7):
  - "esta síntese", nunca "esta revisão";
  - IDs P0xx só em IA-7 e na tabela do Apêndice G;
  - os pontos de julgamento aparecem como leituras alternativas não adotadas;
  - o GRADE e o risco de viés aparecem como julgados só por IA, sem validação humana.
- **Frases canônicas** da seção 1.10 onde a especificação mandar.
- **Voz** (seção 1.8).

## Como trabalhar

1. Escreva o(s) seu(s) arquivo(s), seção por seção, na ordem da especificação.
2. Confira o orçamento com o comando da seção 1.9, trocando o arquivo pelo seu. Cada subseção fica dentro de ±10%, e os limites duros não podem ser passados.
3. Faça uma autoconferência:
   - grep por "rascunho", "suplemento", "Pendente", "[A confirmar", "—" (travessão), "revisão sistemática" (referindo-se a este trabalho) e "esta revisão";
   - confira cada número contra a fonte;
   - no Bloco 2, confira cada span contra `revista/celulas.json`.
4. Só no Bloco 3: rode `python3 09-documento-final/montar_suplemento.py` para ver se os apêndices montam. Se o erro vier do código (legendas antigas, função), anote no relatório e não mexa no código: essa parte é do coordenador.
5. Não rode `rs.py`, não abra PDFs, não mexa em código Python, R ou Typst, nem em `rotulos.yml`, `numeros_v2.json`, `celulas.json` e figuras. Não rode nada em segundo plano.

Responda em até 15 linhas:

- palavras por subseção e total;
- desvios da especificação, com o motivo;
- números que você usou e que não estavam no esqueleto congelado, com a fonte de cada um;
- dúvidas para o coordenador.
