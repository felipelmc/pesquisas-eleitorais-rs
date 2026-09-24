# Vitrine interativa (etapa 9): construção

Você é designer de visualização de dados e engenheiro de front-end, do nível de The Pudding, Our World in Data e das peças interativas da Nature. Construa a vitrine interativa da revisão sistemática "Pesquisas eleitorais publicadas mudam o voto?" (autor Felipe Lamarca, MAPE/IESP-UERJ). Ela será a página de entrada no GitHub Pages. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.

## Leia antes, inteiros
- `09-documento-final/vitrine/PLANO_DESIGN.md`: a especificação completa (arco, sistema visual, stack, arquivos, QA).
- O plano geral: `/Users/felipelmc/.claude/plans/veja-acredito-que-na-delegated-ripple.md`, etapa 9 e "Riscos".
- Os dados:
  - `09-documento-final/revista/celulas.json` e `revista/numeros_v2.json`;
  - `07-relatorio/prisma_contagens.json` e `07-relatorio/_pendencias_abertas.json`;
  - `06-analise/swim_*/swim_resumo.json`, `swim_*/tabelas/swim_direcao.csv` e `06-analise/meta_*/meta_resumo.json`;
  - `04-qualidade/rob_*_consenso.csv` e `rob_geral.csv`;
  - `07-relatorio/incluidos.csv` e `09-documento-final/insumos/tabelas/*.md`;
  - `00-protocolo/correcao_atribuicao.csv`;
  - `rs_log.jsonl`: só os eventos `portao` e `emenda_protocolo`, agregados; nunca publique o log bruto.
- As funções de formatação de `07-relatorio/gerar_tabelas_relatorio.py`.
- A voz do autor: `/Users/felipelmc/.claude/commands/my-voice.md`.

## Limites
- Escreva só em `09-documento-final/vitrine/` e gere `docs/index.html` só pelo `montar_vitrine.py`. Não edite outros arquivos.
- Não rode `rs.py` nem abra PDFs. Não use CDN na página final: as bibliotecas já estão em `vitrine/vendor/` (D3 7.9.0, topojson-client 3.1.0, world-atlas 2.0.2 110m, com licenças e SHA256), e as fontes woff2 oficiais em `09-documento-final/revista/fontes/woff2/`, com as licenças `OFL-*.txt`.
- Pode instalar `playwright` e `@axe-core/playwright` com `npm i -D` dentro de `vitrine/qa/`. O `node_modules/` fica fora do git: crie `vitrine/.gitignore` com `qa/node_modules/`, `qa/capturas/` e `build/`. Os navegadores do Playwright já estão no cache do usuário; se faltar o Chromium, rode `npx playwright install chromium`.
- Nada de dado proibido na página (lista no PLANO_DESIGN). As certezas, os enunciados e os números vêm dos arquivos, nunca digitados.

## Textos
`vitrine/conteudo/textos.yml` traz os textos editoriais na voz do autor, em português, curtos e diretos, sem jargão de IA, com números só por marcador `{{bloco.campo}}`. As mensagens principais e o resumo em linguagem simples vêm do artigo e de `09-documento-final/linguagem_simples.qmd`, quando existirem, extraídos pelo AST com `quarto pandoc -t json`. Enquanto não existirem, use o texto das mensagens do v1 (`09-documento-final/_revisao_final_v1_oqf.qmd`) com a marca "provisório", e o `montar_vitrine.py` falha na montagem final se ainda houver "provisório".

## Ordem de trabalho
1. `exportar_dados.py` → `build/vitrine.json`, com SCHEMA de campos permitidos e *asserts*.
2. `src/` (HTML, CSS de tokens nos dois temas, JS por componente) e `montar_vitrine.py` → `docs/index.html` autocontido, com no máximo 3 MB.
3. Primeira leva inteira e polida. Depois a segunda leva.
4. QA:
   - `qa/testar_sanitizacao.py docs/`, `qa/testar_textos.py` e `qa/checar_links.py`: por enquanto, só para `index.html`. Links para documentos que ainda não existem em `docs/` viram AVISO, não FALHA.
   - `qa/verificar_licencas.py`.
   - `qa/capturar.mjs`: capturas em 1440, 1024, 768 e 390 px, claro e escuro, zero erros de console, zero requisições externas, axe sem `serious`/`critical`, e o percurso de teclado.
5. Olhe você mesmo as capturas (Read nas imagens PNG) e corrija o que estiver feio, desalinhado, ilegível ou com sobreposição. A página tem de ser bonita: tipografia cuidada, respiro, hierarquia clara, animações sutis, gráficos legíveis no celular. Refaça até ficar no nível pedido.

Responda com até 25 linhas: componentes prontos (primeira e segunda leva), tamanho do `index.html`, resultado de cada QA, onde estão as capturas (liste 4 caminhos representativos) e o que ficou pendente.
