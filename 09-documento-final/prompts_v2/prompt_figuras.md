# Figuras do artigo (etapa 2)

Você é programador (Python 3 com pandas; R 4.5 com ggplot2 4.0, patchwork, svglite, ragg, scales, jsonlite, systemfonts). Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Faça as 7 figuras do artigo final da revisão. Leia antes:
- o plano, seções "Figuras" e "Riscos": `/Users/felipelmc/.claude/plans/veja-acredito-que-na-delegated-ripple.md`;
- o contrato de rótulos: `09-documento-final/revista/rotulos.yml`;
- as células: `09-documento-final/revista/celulas.json`;
- os números derivados: `09-documento-final/revista/numeros_v2.json`;
- as funções `dir_rot`, `rebaix` e o realismo em `07-relatorio/gerar_tabelas_relatorio.py`;
- `09-documento-final/insumos/contagens_mecanismos_moderadores.py`.

Não rode `rs.py` nem `quarto`, não abra PDFs e não rode nada em segundo plano. Escreva só em `09-documento-final/revista/figuras/`.

## Regras
- **Nenhuma análise nova.** As figuras só mostram resultados que já existem nos arquivos. Nada é reestimado. O *leave-one-out* e os intervalos já estão em `meta_resumo.json`.
- **Dados em Python, desenho em R.**
  - `figuras/preparar_dados_figuras.py` (roda da raiz; importa `07-relatorio/gerar_tabelas_relatorio.py` por caminho) grava `figuras/dados/dados_<nome>.csv` com exatamente o que cada figura desenha, rótulos prontos em português (direção por `dir_rot`, sem asteriscos de Markdown).
  - `figuras/gerar_figuras.R` só lê esses CSVs (e `rotulos_autor_ano.json`, se existir; senão monta "Sobrenome (ano)" ou "Sobrenome et al. (ano)" a partir de `07-relatorio/incluidos.csv` e anota que o rótulo final virá do citeproc).
- **Tema** em `figuras/tema_revista.R`:
  - Fira Sans (a do sistema, que é a mesma família das fontes do projeto; registre as fontes de `revista/fontes/otf` só se "Fira Sans" não existir em `systemfonts::system_fonts()`), corpo 7,5 pt;
  - linhas de 0,3 pt, sem grade menor, fundo transparente, marcadores **a**/**b** em painéis;
  - vírgula decimal e sinal de menos U+2212 (`scales::label_number(decimal.mark = ",", big.mark = ".", style_negative = "minus")`).
- **Paleta:**
  - a favor/*bandwagon*/viabilidade/*momentum* a favor/mobilização `#2a78d6`;
  - contra/*underdog*/desmobilização `#eb6834`;
  - misto: losango cinza escuro `#52514e`;
  - nulo por ±δ: anel cinza `#898781`;
  - risco de viés com a paleta *colourblind* do robvis (leia no código do robvis instalado as cores exatas de baixo/algumas preocupações/alto/crítico/sem informação).
  - Nunca "benéfico", "danoso", "Neutro" ou "sem efeito".
- **Saídas** em `figuras/saida/<nome>.svg` (svglite) e `<nome>.png` (ragg, 300 dpi). Largura de 140 mm (texto) ou 170 mm (bloco largo). Corpo mínimo de 6,5 pt na largura final.
- **Legendas** em `figuras/legendas.yml`: `<nome>: {legenda: "...", alt: "...", largura: texto|larga}`. Legenda em português, na voz de artigo, com os números como marcadores `{arquivo:caminho}` que o montador vai resolver. Por exemplo, `{meta:delta}` e `{meta_resumo:grupos.0.resultado.gl}`; documente a sintaxe no topo do YAML e use só chaves que existam. O `alt` descreve a figura em 1 ou 2 frases, sem números.

## As figuras (nomes = chaves de `rotulos.yml`)
1. **`modelo_logico`.** Reproduz os nós e as arestas de `00-protocolo/dag_v1.mmd`: só o E2 passa pela percepção de viabilidade; E3 a E6 saem direto da exposição; a complacência e a desmobilização são tracejadas; os confundidores ficam em cinza; a resposta ao *survey* é o colisor. Rótulos em português legível (ex.: "exposição à pesquisa", "percepção de viabilidade", "cálculo estratégico", "heurística de consenso", "conformidade", "simpatia pelo azarão", "emoções", "apoio a quem aparece à frente", "complacência", "desmobilização", "apoio latente", "interesse político", "preferência prévia", "pesquisa anterior", "pesquisa seguinte", "divulgação enviesada", "resposta ao survey"). Os moderadores (Tabela Z de `00-protocolo/teoria_programa.md`) vão num quadro à direita. Layout manual em ggplot (geom_label/geom_curve/geom_segment com setas). Grave também `dados/dag_arestas.csv` com as arestas desenhadas.
2. **`prisma`.** PRISMA 2020 com dois ramos (bases; busca por citação), redesenhado a partir de `07-relatorio/prisma_contagens.json`. Motivos de exclusão em português, a partir de `00-protocolo/codebook_elegibilidade.csv` ou do protocolo. A remoção automática (duplicatas, filtro de ano) fica separada da triagem por IA. Sem cabeçalho de pendências (a legenda diz que o fluxo é rascunho; as 18 pendências vêm de `07-relatorio/_pendencias_abertas.json`). Sem travessão.
3. **`rob`.** Barras empilhadas horizontais por ferramenta e domínio: RoB 2 (D1, D1b, D2 a D5, geral), ROBINS-I V2 (D1 a D6, geral) e EPOC. Proporção de estudos por julgamento, a partir de `04-qualidade/rob_rob2_consenso.csv`, `rob_robins_i_consenso.csv`, `rob_epoc_consenso.csv` e `rob_geral.csv`. Nomes dos domínios em português, dos codebooks `00-protocolo/codebook_v0_*.csv`. Painéis com patchwork. Nota: "julgamentos de IA não validados".
4. **`celulas`.** Para as células de `celulas.json`: ponto na proporção a favor com IC de Clopper-Pearson, em painéis pelos 4 blocos. Forma por classe de desenho, linha em 0,5, rótulo "x de y" e, à direita, a certeza com ⊕◯ (desenhe círculos, não dependa de glifo) mais a palavra. Célula só com nulos ou com proporção nula ganha marca própria ("nulo por ±δ"), e a célula vazia (k = 0) aparece como "sem estudo".
5. **`direcao`.** Gráfico de direção do efeito por estudo, lido de `06-analise/swim_principal/tabelas/swim_direcao.csv`.
   - Linhas: estudos agrupados por célula e ordenados por desenho → risco de viés.
   - Glifos: ▲ a favor, ▼ contra, ◆ misto, ○ nulo por ±δ, com cor pela direção.
   - Coluna de risco de viés em símbolos robvis, e tamanho constante.
   - Painel à parte "fora da contagem (agrupamento amplo, *post hoc*)", lido de `06-analise/swim_sens_com_excluidos_amplo/tabelas/swim_direcao.csv`, só com os estudos que não estão na principal.
6. **`metas`.** Dois *forest plots*:
   - **a:** meta exploratória "sem pesquisa", de `06-analise/meta_exploratoria/` (`meta_entrada*.csv`, `meta_resumo.json`, tabelas);
   - **b:** "mesmo candidato atrás", de `06-analise/meta_mesmo_candidato/`.

   Em cada painel:
   - rótulos autor-ano, com os dois efeitos de Tyszler2015 distinguidos;
   - faixa ±δ sombreada, com o δ do `parametros.delta` de cada meta;
   - diamante vazado para a estimativa combinada;
   - **sem** a barra do intervalo de predição, que vai para a legenda;
   - eixo em g com vírgula.
7. **`realismo`.** Moderador realismo do contexto (hipotético, induzido, real) × direção, em painéis separados por classe de desenho. Uma barra por estudo × célula, com contagens iguais às das tabelas T9 e T14 de `insumos/contagens_mecanismos_moderadores.py` (rode o script para conferir). Legenda: "comparação descritiva, sem teste".

## Conferência
`figuras/verificar_figuras.py` falha se:
- (i) as contagens dos `dados_*.csv` não baterem com a origem (células com `celulas.json`/`swim_resumo.json`; PRISMA com o JSON; RoB com os CSVs; realismo com T9/T14);
- (ii) o texto dos SVG tiver termo proibido (benéfic, danos, Neutro, "sem efeito", "significativ") ou número com ponto decimal;
- (iii) as arestas de `dag_arestas.csv` diferirem das de `dag_v1.mmd`;
- (iv) faltar `alt` em `legendas.yml`.

Rode tudo e deixe as 7 figuras prontas. Responda com até 20 linhas: arquivos gerados, dimensões, o resultado de `verificar_figuras.py` e qualquer decisão de desenho que o revisor deva olhar.
