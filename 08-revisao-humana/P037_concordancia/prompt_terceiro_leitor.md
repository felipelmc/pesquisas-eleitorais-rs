# Terceiro leitor das divergências de extração (P037)

Duas extrações de IA do mesmo estudo discordaram em algumas variáveis do codebook. A primeira é a `original`; a segunda, uma recodificação cega, é a `revalidacao`. Você é o terceiro leitor: para cada item, diz qual valor o texto sustenta. Sua resposta é **sugestão** para o revisor humano, que decide. O coordenador passa a `CHAVE`.

Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.

## Arquivos (só estes)

- Itens: `08-revisao-humana/P037_concordancia/terceiro_leitor/itens_<CHAVE>.json`, com `id_item`, `variavel`, `tipo`, `valor_original` e `valor_revalidacao`.
- Codebook: `00-protocolo/codebook_v0_efetividade.csv`. Leia a definição e o prompt de cada variável citada.
- PDF: `03-textos/pdfs/<CHAVE>.pdf`. Leia pela camada de texto com pymupdf; renderize a página quando uma tabela embaralhar.

Não abra outras fichas nem extrações, não use a rede e não rode `rs.py`.

## Para cada item

- `sugestao`:
  - `original` ou `revalidacao`: esse valor é o correto;
  - `equivalentes`: os dois dizem a mesma coisa com palavras diferentes, e a divergência é só de forma;
  - `nenhum`: os dois estão errados; dê o valor certo;
  - `indecidivel`: o texto não resolve; explique.
- `valor_sugerido`: o valor, no vocabulário do codebook.
- `trecho`: cópia literal, contígua, de até 40 palavras, da camada de texto. Pode ser vazio quando a variável é derivada de outras.
- `pagina`: índice da folha no PDF, com 1 para a primeira folha.
- `justificativa`: uma ou duas frases que apliquem a regra do codebook.

## Saída

Grave `08-revisao-humana/P037_concordancia/terceiro_leitor/resposta_<CHAVE>.json` com uma lista, um objeto por `id_item` e na mesma ordem dos itens:

`{"id_item": "...", "sugestao": "...", "valor_sugerido": "...", "trecho": "...", "pagina": 0, "justificativa": "..."}`

Confira com python se estão todos os `id_item`. Responda com UMA linha: `OK <CHAVE>: <n> itens (original=<n>, revalidacao=<n>, equivalentes=<n>, nenhum=<n>, indecidivel=<n>)`.
