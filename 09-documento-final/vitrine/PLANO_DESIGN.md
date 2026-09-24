# Vitrine: especificação de design e implementação

Especificação consolidada do parecer do designer de visualização (24/09/2026), com as correções dos revisores do plano. O plano geral está em `/Users/felipelmc/.claude/plans/veja-acredito-que-na-delegated-ripple.md`, etapa 9.

## Regra de ouro

Um achado nunca aparece sem o selo de certeza (⊕ desenhado em SVG mais a palavra) e sem o `enunciado` literal da célula (`09-documento-final/revista/celulas.json`). A direção é sempre traduzida por `dir_rot()` de `07-relatorio/gerar_tabelas_relatorio.py`: *bandwagon*/*underdog* na célula principal, viabilidade/contra, *momentum* a favor/contra, mobilização/desmobilização. Nunca "benéfico", "danoso", "sem efeito", "Neutro" ou "não significativo".

## Achados dos dados que moldam o desenho

- 19 das 54 linhas de `swim_entrada_principal.csv` não têm `yi`. Por isso o gráfico por estudo mostra a direção sem o g. A magnitude só aparece nas duas metas exploratórias.
- `swim_sens_so_contexto_real_amplo` reduz o grupo randomizado "apoio, principal" de 9 de 9 *bandwagon* a um estudo. É a ressalva mais importante da página; entra como alternância, com o rótulo *post hoc*.
- A raia de cada evento da linha do tempo sai do `ator.id` (`ia_*` e `autopiloto` são IA). Humano só se o evento constar como `mantida/humano` em `00-protocolo/correcao_atribuicao.csv`. A seq 793 (Emenda 6b) está gravada como humana no log e é IA.
- Textos literais que **nunca** podem ir para a página:
  - `efeitos.csv:evidencia`;
  - `trecho` nos três `rob_*_consenso.csv`;
  - `outcome`, `modelo` e `subgrupo` nos arquivos de efeitos;
  - a `justificativa` do GRADE (vão só os selos de rebaixamento, pela `rebaix()`);
  - `descricao` e `arquivo` das pendências (usar rótulos públicos).
- A contagem de pendências vem só de `07-relatorio/_pendencias_abertas.json` (18). O `prisma_contagens.json` ainda diz 17.
- Há um grupo SWiM com k = 0 (agregador × mobilização × não randomizado; só Kaplan2019a, crítico) e uma célula com `p_sinal = None` (Gerber). As duas pedem estado vazio explícito.
- As 18 células estão como "Inconclusivo" em `caixa_oqf.json`, e a página diz isso.

## Arco da página (três atos)

Barra fixa no topo, com fundo de aviso e `role="note"`: "Rascunho não validado · 18 pendências humanas abertas", com link para o rastreador. No desktop, uma legenda de leitura (glifos de direção e de certeza) fica fixa ao lado das seções de evidência.

### Primeira leva (essencial)

1. **Herói.** A pergunta em serifa grande e a autoria (Felipe Lamarca, MAPE/IESP-UERJ). Contadores com animação: registros (bases + citações) → 41 estudos (55 relatos) → 560 efeitos → 18 células → **15 de 18 com certeza muito baixa**. Ao fundo, 41 pontos neutros, um por estudo, sem cor de direção.
2. **Mensagens principais.** Extraídas do artigo pelo AST (`quarto pandoc -t json`), em cartões com link para a seção.
3. **Em linguagem simples.** O resumo em linguagem simples, extraído do documento próprio (`09-documento-final/linguagem_simples.qmd`, quando existir).
4. **Dos registros aos estudos.**
   - Um Sankey PRISMA feito à mão, com colunas fixas, dois ramos (bases e citações) e saídas laterais com os motivos de exclusão em português.
   - Continuação do fluxo: 41 estudos → 40 com efeitos → 37 com efeito principal → 27 na síntese principal, com saídas laterais para os 3 críticos, os 7 fora da contagem e os 4 sem efeito principal (confira em `revista/numeros_v2.json`).
   - Alternância "ver diagrama PRISMA 2020", que mostra a Figura 2 do artigo.
5. **Mapa de evidências** (peça central).
   - Linhas: os 4 blocos (apoio principal, viabilidade, *momentum*, comparecimento). Colunas: randomizado e não randomizado.
   - Em cada célula do mapa, um ponto por estudo, colorido pela direção, com a opacidade do preenchimento caindo com a certeza e o contorno sempre forte. A contagem vem separada da posição, e cada célula leva o selo ⊕.
   - Célula vazia vem hachurada como "lacuna".
   - O clique abre uma gaveta com:
     - as células do protocolo daquele bloco;
     - o enunciado literal, x de y, o IC de Clopper-Pearson, o p do teste de sinal e os selos de rebaixamento;
     - os estudos (ano, país, desenho, n com a unidade, risco de viés);
     - o link para a seção do artigo (`revisao.html#sec-...`).
6. **Estudo a estudo.** Gráfico de direção no estilo Boon & Thomson.
   - Linhas: estudos, agrupados sob o cabeçalho da célula.
   - Glifos por efeito principal: ▲, ▼, ○ quando o IC fica dentro de ±δ, e ◆ para misto.
   - Coluna com o símbolo de risco de viés no estilo robvis.
   - Filtros: exposição, desfecho, classe de desenho, contexto, região, e uma chave para mostrar em cinza os estudos críticos e os fora da contagem, cada um com o motivo.
7. **O que a evidência não permite dizer.** Cinco cartões "não sabemos": o tamanho do efeito; se ele aparece fora do laboratório; o Brasil (nenhum estudo sobre pesquisas no país); "sem efeito" (ausência de evidência não é evidência de ausência); se a evidência apoia restringir ou manter as regras. Cada cartão aponta para as lacunas do mapa.
8. **Pendências.** Um *pipeline* das etapas, com os 18 chips pendurados na sua etapa (ID, o que fazer e esforço, tirados de `08-revisao-humana/README.md`) e o medidor "0 de 18 fechadas".
9. **Documentos e citação.** Cartões para:
   - PDF (`revisao.pdf`), artigo HTML, .docx e suplemento;
   - linguagem simples, relatório técnico e guia da revisão humana.

   Os tamanhos dos arquivos são calculados na montagem. A citação traz o texto "Versão de trabalho de <data>; não citar como final" e usa `@unpublished` no BibTeX.

### Segunda leva

10. **Contando a direção.** Ponto com IC por célula, numa escala de 0 a 1, com a linha em 0,5 e "k = 4, p = 0,125". Um controle segmentado alterna entre as células do protocolo (18), o agrupamento amplo *post hoc* (7), só contexto real, sem pré-2010, sem Araújo e com excluídos. O selo ⊕ só aparece onde há GRADE próprio. Em "só contexto real", uma nota diz o que sobra.
11. **De quanto?** As duas metas exploratórias como *forest* pequenos, com faixa ±δ e diamante vazado. Carimbo: "Exploratória: menos de 4 gl, RVE não confiável". O *leave-one-out* sai em tabela, e nada é estimado no navegador.
12. **Quão confiáveis são os estudos?** Barras no estilo robvis por ferramenta e domínio, com a nota "nenhum julgamento validado por humano".
13. **O método em 60 segundos.** Eixo do tempo de 19/09 a 24/09 com as raias Humano, IA e Script: portões G1 a G9 (G1 e G2 humanos), as Emendas e a sessão de 23/09. Nota: "O log registrava decisões de triagem como humanas; a Emenda 6a corrigiu".
14. **A controvérsia no Brasil.** Linha do tempo só com os itens confirmados em `insumos/contexto_brasil.md`, em tom neutro.
15. **Onde.** Faixa de países (mapa-múndi só se os países estiverem codificados com confiança). @Lago2015 aparece como "multinacional (46)". O Brasil fica destacado: "1 estudo, sobre apuração parcial oficial, não sobre pesquisa".

### Rodapé

- "Créditos e licenças" (fontes OFL; D3 e topojson ISC).
- A nota "Rascunho redigido por IA a partir dos arquivos do projeto e ajustado ao estilo do autor; não revisado pelo autor (P038)".
- "Versão de trabalho de <data> (commit <hash>); não citar como final".
- "O que mudou desde 24/09" (a versão anterior tem a tag `v1-oqf-2026-09-24`).

## Sistema visual

- **Tipografia:** STIX Two Text nos títulos e na prosa; Fira Sans na interface, nos rótulos de gráfico, nas tabelas e em todos os números grandes. As fontes são woff2 oficiais sem modificação, em `09-documento-final/revista/fontes/woff2/`, com as licenças `OFL-*.txt`. Termos em inglês vão em `<i lang="en">`. `tabular-nums` só em tabelas e eixos.
- **Paleta:** validada nos dois temas, todos os pares.

  | Papel | Claro (fundo `#fbfaf7`) | Escuro (fundo `#121417`) | Codificação secundária |
  |---|---|---|---|
  | Direção positiva (*bandwagon* / viabilidade / *momentum* a favor / mobilização) | `#2a78d6` | `#3987e5` | ▲ + rótulo |
  | Direção negativa (*underdog* / contra / desmobilização) | `#eb6834` | `#d95926` | ▼ + rótulo |
  | Misto | glifo metade azul, metade laranja | idem | ◆ + "misto" |
  | Nulo ou trivial (IC dentro de ±δ) | anel cinza `#898781` | idem | ○ + "nulo ou trivial" |
  | Humano (raia do processo) | `#1baf7a`, sempre com rótulo | `#199e70` | ● + "humano" |
  | Texto principal / secundário / apagado | `#16181d` / `#52514e` / `#6b6a66` | `#f2f1ec` / `#c3c2b7` / `#9a9890` | |

  Não use violeta para "misto": em modo escuro, ele falha contra o azul. A certeza vai com ⊕◯◯◯ a ⊕⊕⊕⊕ mais a palavra, sempre. A opacidade do preenchimento cai com a certeza: muito baixa 35%, baixa 55%, moderada 80%, alta 100%. O risco de viés fica numa coluna própria, com os símbolos robvis (+ − × !).
- **Tema:** segue `prefers-color-scheme`, com um botão que grava em `localStorage` (leitura e escrita dentro de try/catch) e usa `[data-theme]`.
- **Movimento:**
  - animação só na primeira aparição ou quando os dados mudam de estado: 400 a 700 ms, *cubic in-out*, escalonamento de no máximo 20 ms, total de no máximo 900 ms;
  - contadores rodam uma vez;
  - com `prefers-reduced-motion` ou o botão "Reduzir animações", valores finais direto e transição de 0 ms.
- **Celular (< 768 px):**
  - uma coluna;
  - mapa de evidências em cartões por bloco;
  - filtros como fileira de *chips* com rolagem horizontal;
  - *tooltips* viram painéis inferiores abertos por toque;
  - alvos de toque de pelo menos 44 px;
  - sem rolagem horizontal da página.
- **Acessibilidade:**
  - *landmarks* e *skip link*;
  - cada gráfico é um `<figure>` com legenda de uma frase, SVG com `role="img"` e `aria-labelledby`, e um `<details>` "Ver tabela" com os dados;
  - *tooltips* abrem por foco e por hover;
  - região `aria-live="polite"` para filtros;
  - estilos para `forced-colors` e folha de impressão.

## Stack e arquivos

- JavaScript puro (ES2020), D3 7.9 e topojson-client 3.1, guardados em `vendor/` com as licenças. Sem framework e sem npm na publicação. Gatilhos de rolagem com `IntersectionObserver`.
- Um único `docs/index.html` autocontido: CSS, JS, dados, fontes em base64 e mapa. No máximo 3 MB. Meta CSP `default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; font-src data:; img-src data:`. `<meta name="robots" content="noindex">`. Open Graph com "Rascunho".
- Arquivos:

```
09-documento-final/vitrine/
  README.md  PLANO_DESIGN.md  exportar_dados.py  montar_vitrine.py
  conteudo/textos.yml          # textos editoriais na voz do autor; números só por marcador {{...}}
  src/index.html               # marcadores <!--ESTATICO:x-->, <!--DADOS-->
  src/css/{tokens,base,layout,graficos}.css
  src/js/{fmt,tooltip,gaveta,legenda,heroi,prisma,mapa_evidencia,direcao,contagem,forest,rob,processo,pendencias,main}.js
  vendor/{d3-7.9.0.min.js, topojson-client-3.1.0.min.js, LICENCAS.md}
  qa/{testar_sanitizacao.py, testar_textos.py, checar_links.py, verificar_licencas.py, package.json, capturar.mjs}
  build/                       # fora do git: vitrine.json
```

- **`exportar_dados.py`:**
  - roda da raiz, importa `07-relatorio/gerar_tabelas_relatorio.py` por caminho (o módulo lê `dados/` e o master na importação: tudo bem, mas nada disso sai no JSON) e reusa `num`, `g_fmt`, `p_fmt`, `ic_fmt`, `rot`, `dir_rot`, `contagem`, `pais_fmt`, `desenho_cod`, `fam_cod` e `rebaix`;
  - converte Markdown em HTML com `quarto pandoc`;
  - exporta cada valor cru (para posicionar) e formatado (vírgula decimal, U+2212);
  - grava `build/vitrine.json` com lista de campos permitidos por bloco (`SCHEMA`), e a montagem falha com chave extra;
  - *asserts*: os enunciados são iguais em `certeza.csv`, `celulas.json` e `caixa_oqf.json`; as contagens batem com `swim_resumo.json`; as mensagens são iguais às do artigo; as pendências vêm só de `_pendencias_abertas.json`.
- **`montar_vitrine.py`:**
  - gera em Python a camada estática: mensagens, cartões, tabelas de dados e um `<noscript>` completo;
  - resolve os marcadores de `textos.yml`;
  - concatena os JS em ordem fixa, cada um como IIFE num namespace `window.V`;
  - embute tudo em `docs/index.html`.
- **QA:**
  - `testar_sanitizacao.py` roda sobre **todo o `docs/`**: HTML, `pdftotext` dos PDFs e XML dos .docx. Checa:
    - e-mail e caminhos (`/Users/`, `~/`, `revisoes/pesquisas-eleitorais`);
    - os campos proibidos acima e `ator_registrado`, `observacao`, `aviso`, `pdf_path`;
    - vazamento de `evidencia`/`trecho` (nenhuma substring de 25 caracteres ou mais);
    - títulos e resumos de registros não incluídos;
    - prompts;
    - `pontos_para_o_revisor`.
  - `testar_textos.py`: termos proibidos; os 18 enunciados literais; todo número do texto visível dentro da lista branca (reusar `09-documento-final/conferir_reestruturacao.py`).
  - `checar_links.py`: todo `href` existe em `docs/` e toda âncora `#sec-*` existe na página de destino.
  - `verificar_licencas.py`: avisos das fontes e das bibliotecas presentes.
  - `qa/capturar.mjs` (Playwright e @axe-core/playwright via `npm i -D` em `qa/`, com `node_modules` fora do git):
    - capturas em 1440, 1024, 768 e 390 px, claro e escuro, com e sem movimento reduzido, salvas em `qa/capturas/` (fora do git);
    - falha com erro de console, com requisição externa, ou se o axe apontar violação `serious` ou `critical`;
    - percurso de teclado: *skip link* → filtros → células do mapa → Enter abre a gaveta → Esc fecha e devolve o foco.
