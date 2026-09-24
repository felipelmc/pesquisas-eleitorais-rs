# Passe de estilo do artigo e dos produtos (etapa 7)

Você revisa o ESTILO, não o conteúdo. O objetivo é que os textos soem escritos pelo autor, Felipe Lamarca (cientista político, MAPE/IESP-UERJ), e não por IA. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. O coordenador diz qual PASSE e qual ARQUIVO você revisa.

PASSE = voz; ARQUIVO = 09-documento-final/linguagem_simples.qmd

## PASSE = voz
1. Leia, inteiras, as regras de voz de `/Users/felipelmc/.claude/commands/my-voice.md`.
2. Leia `09-documento-final/insumos/amostras_voz.md`. São textos públicos do autor, para ouvir o ritmo; não copie conteúdo. Quando as amostras usarem palavra proibida pelo `my-voice.md`, vale o `my-voice.md`.
3. Leia a rubrica de movimentos (fim de `09-documento-final/insumos/exemplares_movimentos.md`). A voz do autor não pode desfazer os movimentos: resposta primeiro, contribuições explícitas, "o que a evidência não permite dizer", estudos nomeados.
4. Reescreva a prosa na voz do autor.

## PASSE = ia
1. Leia, inteiros, `/Users/felipelmc/.claude/skills/tirar-cara-de-ia/SKILL.md`, `references/portugues.md` e, se existir, `references/estrutura-retorica-e-deteccao.md`. No *abstract* e em textos em inglês, leia também `references/ingles.md`.
2. Aplique o procedimento no modo leve: diagnóstico estrutural e lexical, cortar antes de trocar, devolver ritmo e posição, sem inventar.

## Em qualquer passe, é PROIBIDO mexer em
- números, intervalos, p, g, contagens, datas e porcentagens; marcadores `{...}` e `{{...}}` em arquivos YAML;
- chaves de citação `[@...]` e `@...`, e referências a figuras, tabelas, quadros e seções (`@fig-`, `@tbl-`, `@qdr-`, `@sec-`, `](#...)`);
- spans `[...]{.enunciado cel="..."}`, inclusive o texto de dentro, e selos `[...]{.grade}`;
- frases padrão de certeza ("a evidência é muito incerta", "pode aumentar", "provavelmente", "certeza muito baixa/baixa/moderada/alta");
- IDs de pendência (P0xx), títulos "Pendente de revisão humana" e "RASCUNHO NÃO VALIDADO", e marcadores **[A confirmar pelo autor]**;
- rótulos da caixa (Positivo, Negativo, Misto, Nulo, Inconclusivo, Pendente);
- YAML do `.qmd`, Divs `:::` e atributos `{#...}`/`{.…}`, marcadores `@@...@@`, tabelas (linhas que começam com `|`) e blocos de código;
- a lista das Mensagens principais (a forma de lista fica; o texto dos itens pode ser ajustado);
- o sentido de qualquer afirmação, inclusive as ressalvas: não enfraqueça nem reforce.

Não acrescente fatos. Se achar lacuna de conteúdo, anote-a em `09-documento-final/lacunas_estilo.md` em vez de preencher.

## Como trabalhar
1. Copie o arquivo para `09-documento-final/_antes_<PASSE>_<nome>`, com o mesmo nome e extensão.
2. Edite o ARQUIVO.
3. Rode `python3 09-documento-final/conferir_numeros.py <cópia> <ARQUIVO>`. A saída tem de ser vazia (código 0). Se não for, desfaça as mudanças que alteraram números, chaves, pendências, certezas, estrutura ou enunciados e rode de novo, até dar vazio.
4. Rode `grep -n "—" <ARQUIVO>`: não pode haver travessão.
5. Se o ARQUIVO for o esqueleto, rode, da raiz, `python3 09-documento-final/montar_revisao_final.py` e `python3 09-documento-final/conferir_reestruturacao.py`, que têm de passar sem FALHA.
6. Apague a cópia só depois que a trava der vazio.

Não rode `rs.py`, `quarto` nem nada em segundo plano. Responda com UMA linha: `OK passe=<PASSE> arquivo=<nome>: trava vazia; <resumo das mudanças por categoria em até 30 palavras>`.
