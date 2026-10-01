# Leitura de controle do passe de voz (30/09/2026)

Você é leitor independente e não escreveu nenhum dos textos. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Grave só `09-documento-final/_qa/controle_voz.md`. Não edite outros arquivos. Não rode `rs.py`, `montar_*.py`, `publicar.sh`, `refazer_produtos.sh`, `quarto` nem comandos git que escrevam.

## O passe

Agentes de IA reescreveram a prosa da síntese seguindo `09-documento-final/prompts_final/prompt_voz_autor.md`:
- (a) tirar a cara de IA;
- (b) escrever na voz do primeiro autor, Felipe Lamarca, a partir do guia e dos trechos de `09-documento-final/insumos/amostras_voz_v2.md`;
- (c) primeira pessoa do plural para tudo o que os autores fizeram.

Leia os dois arquivos antes de começar.

## Arquivos

Para cada par, o "antes" está em `{{VOZ}}/antes/` e o "depois" no lugar indicado:

| Antes | Depois |
|---|---|
| `antes/A.qmd` a `antes/D.qmd` | `09-documento-final/_esqueleto_revisao_final.qmd` (o artigo, já juntado) |
| `antes/_esqueleto_suplemento.qmd` | `09-documento-final/_esqueleto_suplemento.qmd` |
| `antes/lacunas.yml` | `09-documento-final/revista/tabelas/lacunas.yml` |
| `antes/linguagem_simples.qmd` | `09-documento-final/linguagem_simples.qmd` |
| `antes/legendas.yml` | `09-documento-final/revista/figuras/legendas.yml` |
| `antes/textos.yml` | `09-documento-final/vitrine/conteudo/textos.yml` |
| `antes/README.md` | `README.md` |
| `antes/LEIA.md` | `ferramentas/pacote/LEIA.md` |

Use `diff` ou um *script* seu, só de leitura. As notas de cada redator estão em `{{VOZ}}/*_notas.md`.

## O que conferir

1. **Sentido.** Nenhuma afirmação mudou de sentido. Procure em especial:
   - ressalva enfraquecida ou reforçada, inclusive palavras de certeza ("provavelmente", "pode", "a evidência é muito incerta") introduzidas em frase sobre efeito;
   - alcance trocado ("em bloco" sumido; "partes da busca" virando "a busca");
   - atribuição de estudo citado trocada;
   - comparação ou classe de desenho trocada;
   - fato a mais ou a menos.
2. **Atores.**
   - Toda ação de IA continua atribuída à IA (agentes, coordenador, árbitro, triadores) e nenhuma virou "nós".
   - Toda ação dos autores está na primeira pessoa e não sobrou "os autores" narrando os próprios autores. "Os autores" de estudo citado pode ficar.
   - Liste cada ocorrência de "os autores", "dos autores", "pelos autores" e "aos autores" nos arquivos "depois", com a classificação "ok (estudo citado)" ou "corrigir".
3. **Honestidade.** Continuam presentes, com o mesmo alcance:
   - conferências em bloco, sem dupla independente e sem registro item a item;
   - risco de viés e certeza só por IA, sem validação humana;
   - validação cega da triagem não feita;
   - PRESS por IA que não equivale a revisão independente;
   - "Concordar com a IA depois de ver as decisões não vale como codificação cega";
   - pendências abertas;
   - "RASCUNHO NÃO VALIDADO" uma vez;
   - na declaração de IA, que agentes redigiram o texto e que agentes ajustaram o estilo à voz do primeiro autor.
4. **Marcas de IA que sobraram**, pelos critérios da `tirar-cara-de-ia` (`/Users/felipelmc/.claude/skills/tirar-cara-de-ia/SKILL.md` e `references/portugues.md`):
   - telegrafia;
   - aberturas repetidas;
   - regra dos três;
   - "não X, mas Y" em série;
   - conectivos proibidos ("Contudo", "Entretanto", "Todavia", "Porém", "Ademais", "Em suma", "Dessa forma", e "Assim," ou "Logo," abrindo frase, "Além disso," abrindo parágrafo);
   - palavras proibidas do `my-voice.md`;
   - excesso de fórmula da voz dele (o mesmo conectivo muitas vezes perto, ` -- ` demais, "Trata-se de" em série).

   Cite até 15 trechos, os piores, cada um com uma reescrita sugerida que não mude palavras, números nem chaves e não aumente o número de palavras.
5. **Semelhança com o corpus.** Escolha 6 parágrafos (2 da abertura e da Introdução, 2 dos Resultados e 2 da Discussão ou da linguagem simples). Para cada um, dê uma nota de 1 a 5 para "soa como os trechos de `amostras_voz_v2.md`", justificada em uma linha com o número do trecho mais parecido.
6. **Travas.** Rode, da raiz, e registre os resultados:
   - `python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd`;
   - para cada par, `python3 09-documento-final/conferir_numeros.py <antes> <depois>`. Nos blocos A a D, compare a concatenação de `antes/cabeca.qmd`, `antes/A.qmd` … `antes/D.qmd` e `antes/cauda.qmd`, gravada num arquivo temporário seu, com o esqueleto.

## Saída

Em `09-documento-final/_qa/controle_voz.md`:
- um resumo;
- uma lista de divergências classificadas como `erro` (mudou sentido, ator ou fato), `aviso` (marca de IA, excesso de fórmula ou estilo destoante) ou `ok com ressalva`, cada uma com arquivo, trecho atual e correção em texto exato;
- as notas de semelhança;
- o resultado das travas.

Responda com UMA linha: `OK controle_voz.md: <n> erros, <n> avisos; semelhança média <x>/5`.
