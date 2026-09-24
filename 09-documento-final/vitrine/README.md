# Vitrine

Página de entrada da revisão no GitHub Pages (`docs/index.html`): um único HTML autocontido, sem requisição externa, com
fontes, D3, dados e textos embutidos. A especificação está em `PLANO_DESIGN.md`.

## Montar

Da raiz do projeto:

```bash
python3 09-documento-final/vitrine/montar_vitrine.py          # rascunho (avisa se ainda há texto provisório)
python3 09-documento-final/vitrine/montar_vitrine.py --final  # falha se ainda houver texto provisório
```

O `montar_vitrine.py` roda `exportar_dados.py` (grava `build/vitrine.json`, com SCHEMA de campos e *asserts*), resolve os
marcadores de `conteudo/textos.yml`, gera a camada estática e grava `docs/index.html` (limite de 3 MB). Nada mais é
escrito fora de `vitrine/`.

- Números, certezas e enunciados vêm dos arquivos do projeto; `textos.yml` só usa marcadores `{{numeros.x}}`/`{{meta.x}}`.
- Mensagens principais e resumo em linguagem simples são extraídos pelo AST (`quarto pandoc -t json`) do artigo novo e de
  `09-documento-final/linguagem_simples.qmd`. Enquanto não existirem, a página usa o texto do v1 com a marca "Provisório".

## Conferir

```bash
python3 09-documento-final/vitrine/qa/testar_sanitizacao.py docs/ --so index.html
python3 09-documento-final/vitrine/qa/checar_links.py
python3 09-documento-final/vitrine/qa/verificar_licencas.py
cd 09-documento-final/vitrine/qa && npm ci && node capturar.mjs    # capturas, console, rede, axe, teclado
python3 09-documento-final/vitrine/qa/testar_textos.py           # depois do capturar.mjs (usa o texto renderizado)
```

`qa/capturas/`, `qa/node_modules/` e `build/` ficam fora do git.

## Arquivos

- `exportar_dados.py`, `montar_vitrine.py`: dados e montagem.
- `conteudo/textos.yml`: textos editoriais, na voz do autor.
- `src/index.html` (modelo com marcadores), `src/css/` (tokens dos dois temas, base, layout, gráficos), `src/js/`
  (um arquivo por componente, concatenados como IIFE no namespace `window.V`).
- `vendor/`: D3 7.9.0, topojson-client 3.1.0 e world-atlas 2.0.2, com licenças e SHA256. Só o D3 é embutido: o
  mapa-múndi ficou de fora porque a codificação de países ainda não foi conferida por humano (há, por exemplo, um
  país codificado como "União Europeia ou Reino Unido").
