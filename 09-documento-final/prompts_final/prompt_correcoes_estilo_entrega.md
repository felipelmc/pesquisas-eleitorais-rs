# Correções da verificação e passe de estilo: versão de entrega (Emenda 7)

Você corrige o artigo final a partir da verificação independente e depois faz um passe de estilo.

- **Raiz:** `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.
- **Arquivos que você edita:** `09-documento-final/_esqueleto_revisao_final.qmd` (o artigo), `09-documento-final/_esqueleto_suplemento.qmd` (os apêndices), `09-documento-final/linguagem_simples.qmd` e a seção 1.10 de `09-documento-final/spec_final.md` (só a FC-IA).
- **Não faça:**
  - editar código, `revista/tabelas/lacunas.yml`, `revista/figuras/legendas.yml`, `rotulos.yml` e `numeros_v2.json`;
  - rodar `rs.py`;
  - abrir PDFs;
  - rodar nada em segundo plano.

Rode Python com `python3 -B`.

## Fase 1: correções

Leia `09-documento-final/verificacao_entrega.md` inteiro e aplique, no texto, estas correções:

- **E2**, só na seção 3.9. A legenda da Tab. 3 já foi corrigida pelo coordenador.
- **A1**, os seis cortes. O corpo, de Introdução a Conclusões, tem de ficar em até 8.500 palavras pela trava.
- **A2**, com esta redação: "(vii) o relato da versão de 24/09/2026; e ele leu e aprovou esta versão antes da entrega." Ajuste a pontuação da lista. A publicação só sai depois dessa aprovação.
- **A3** (Mensagens, declaração de IA, Resumo, *Abstract*, linguagem simples e FC-IA da `spec_final.md`), com as compensações de palavras indicadas.
- **A4**, **A5** (2.7 e Q1), **A6** e **A7**.
- **A8**, com o parágrafo "Agentes desta versão" do Apêndice G. A lista de agentes desta versão é:
  - um arquiteto (`spec_final.md`);
  - três redatores;
  - um agente das listas de conferência (`claude-sonnet-5`);
  - uma verificação independente;
  - um agente de correções e estilo (você).

  Todos são `claude-opus-5-5`, exceto o das listas. Os *prompts* ficam no repositório do projeto, e a tabela desta versão, com modelo e *hash*, vai no pacote de replicação (o coordenador a acrescenta).
- **R1**: respeite os limites (Mensagens até 170 palavras; Resumo e *Abstract* até 250 pelo comando da seção 1.9 da `spec_final.md`).
- **R2 a R6** e **R9 a R12**. No R12, só o texto do Apêndice A e o desdobramento de PRESS na primeira ocorrência do artigo: "PRESS (*Peer Review of Electronic Search Strategies*)". A trava proíbe o termo em português para revisão por pares.
- **R4**, só se couber no limite das Mensagens.

Depois:

```
python3 -B 09-documento-final/montar_revisao_final.py
python3 -B 09-documento-final/montar_suplemento.py
python3 -B 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd
```

Corrija até a trava sair sem FALHA e sem AVISO. Então salve cópias:

- `09-documento-final/_blocos/pos_correcoes_artigo.qmd`, do esqueleto do artigo;
- `09-documento-final/_blocos/pos_correcoes_apendices.qmd`, do esqueleto dos apêndices;
- `09-documento-final/_blocos/pos_correcoes_ls.qmd`, da linguagem simples.

## Fase 2: passe de estilo (um só, combinado)

Leia `/Users/felipelmc/.claude/commands/my-voice.md` (voz do autor) e `~/.claude/skills/tirar-cara-de-ia/SKILL.md`, com as referências que ele indicar (vícios de IA em português acadêmico). Aplique os dois no artigo inteiro, na introdução de cada apêndice e na linguagem simples:

- frases mais diretas;
- sem as construções e o vocabulário típicos de IA;
- a voz do autor (primeira pessoa do plural nos Métodos; nenhuma abertura "Além disso", "Portanto", "Assim" ou "Consequentemente").

Você **não** pode mudar números, chaves de citação, rótulos, marcadores, IDs, títulos com ID, enunciados `.enunciado`, "certeza <nível>", frases de certeza ("a evidência é muito incerta", "pode", "provavelmente"), as frases canônicas da seção 1.10 da `spec_final.md` nem o sentido de qualquer afirmação. Não crie afirmação nova.

Depois de cada arquivo, rode a trava do passe de estilo. A saída tem de ser vazia (código 0). Se não for, desfaça o que mudou número, chave, rótulo, enunciado ou certeza.

```
python3 -B 09-documento-final/conferir_numeros.py 09-documento-final/_blocos/pos_correcoes_artigo.qmd 09-documento-final/_esqueleto_revisao_final.qmd
python3 -B 09-documento-final/conferir_numeros.py 09-documento-final/_blocos/pos_correcoes_apendices.qmd 09-documento-final/_esqueleto_suplemento.qmd
python3 -B 09-documento-final/conferir_numeros.py 09-documento-final/_blocos/pos_correcoes_ls.qmd 09-documento-final/linguagem_simples.qmd
```

No fim, rode de novo a montagem e a trava de reestruturação, que tem de sair sem FALHA e sem AVISO.

Responda em até 12 linhas:

- correções aplicadas e as não aplicadas, com o motivo;
- palavras do corpo e dos blocos limitados;
- resultado das travas;
- o que o passe de estilo mudou, em linhas gerais.
