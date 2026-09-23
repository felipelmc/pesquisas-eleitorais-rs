# Complementação de efeitos — projeto "pesquisas eleitorais publicadas e voto"

Você complementa o CSV de efeitos de UM estudo já extraído. Não re-extraia o estudo: mexa só nas linhas e nos campos listados no seu trabalho. O coordenador passa a `CHAVE` na mensagem.

## Arquivos

- Seu trabalho: chave `"<CHAVE>"` em `/Users/felipelmc/revisoes/pesquisas-eleitorais/05-decomposicao/_complemento_efeitos.json`, com três listas: `linhas_sem_alvo_ou_comparador`, `dados_faltantes`, `estimando_a_revisar` (alguma pode vir vazia).
- CSV a editar: `/Users/felipelmc/revisoes/pesquisas-eleitorais/05-decomposicao/efeitos/<CHAVE>.csv` (UTF-8, vírgula; preserve cabeçalho, ordem das linhas e todos os outros campos; use o módulo `csv` do Python para ler e gravar).
- PDF: `/Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/<CHAVE>.pdf` (leia pela camada de texto, com pymupdf; confira tabelas na página renderizada se a camada de texto embaralhar colunas).
- Protocolo (só consulta): `/Users/felipelmc/revisoes/pesquisas-eleitorais/00-protocolo/protocolo.md`, seções 2 e 6.
- Registro que você grava: `/Users/felipelmc/revisoes/pesquisas-eleitorais/05-decomposicao/complementos_efeitos/<CHAVE>.json`.

Não abra outros arquivos do projeto, não use rede, não rode `rs.py`.

## Tarefa 1 — `alvo_efeito` e `comparador_tipo` por linha

Para cada `id_efeito` em `linhas_sem_alvo_ou_comparador`, preencha o que estiver vazio, lendo `outcome`, `modelo`, `subgrupo` e `evidencia` da linha e, quando não bastar, o PDF.

- `alvo_efeito` (um valor por linha; de quem é o apoio medido, pela posição na informação que o participante ou eleitor recebeu):
  - `lider`: quem a pesquisa mostra à frente;
  - `azarao`: quem a pesquisa mostra atrás, numa disputa de DOIS;
  - `opcao_referendo`: opção à frente num referendo;
  - `segundo_viavel`: segundo colocado competitivo numa disputa com três ou mais;
  - `terceiro_inviavel`: candidato mostrado sem chance numa disputa com três ou mais;
  - `partido_abaixo_clausula`: partido perto ou abaixo da cláusula de barreira;
  - `nao_se_aplica`: linha de `mobilizacao`, ou desfecho que não é apoio a uma posição (ex.: voto no candidato preferido sem referência à posição na pesquisa; explique no registro).
- `comparador_tipo`: `sem_pesquisa` | `mesmo_candidato_atras` | `outro_resultado` | `antes_depois_proibicao` | `unidades_nao_expostas` | `outro`.
- Sinal: as linhas mantêm o sinal impresso. Linha com alvo `azarao` deve ter `direcao_desejada = reduzir`; com `lider` ou `opcao_referendo`, `aumentar`. Se encontrar linha de `apoio_ao_lider` com alvo `azarao` e `direcao_desejada = aumentar` (ou o inverso para `lider`), corrija `direcao_desejada` e registre. Nos alvos de viabilidade (`segundo_viavel`, `terceiro_inviavel`, `partido_abaixo_clausula`) não mexa em `direcao_desejada`.

## Tarefa 2 — dados faltantes das linhas principais

Para cada item de `dados_faltantes`, procure no PDF inteiro (texto, tabelas, notas, apêndices anexados) o que está descrito em `falta`. Definições:

- `p0`: proporção do MESMO desfecho no grupo de comparação da MESMA estimativa, entre 0 e 1 (percentual vira proporção).
- `n1`, `n2`: unidades independentes em cada braço que entram nesta estimativa (tratamento = 1, comparação = 2). Em laboratório com decisões repetidas, use o número de participantes, não de decisões, e diga no registro se o texto só dá decisões.
- `sdy`: desvio-padrão do desfecho no grupo de comparação (ou no pré-período, para séries). Se só houver o DP da amostra toda, use-o e registre.
- `se_pp`: erro-padrão do efeito em pontos percentuais; IC95 do efeito em p.p. vai em `ci_lo`/`ci_hi`.
- Rota `dif_prop` para coeficiente sobre desfecho binário (0/1): se o texto mostrar que o desfecho da linha é binário e o coeficiente está em proporção (modelo de probabilidade linear), troque `tipo_estatistica` para `dif_prop`, preencha `efeito_pp = beta × 100`, `se_pp = se × 100` e `p0`; mantenha `beta` e `se` como estão. Não use essa rota para logit ou probit.
- Valor derivado por aritmética de números impressos (ex.: `p0 = contagem / n`) é permitido: registre os dois trechos e a conta.
- Não ache o valor? Deixe o campo vazio e registre `nao_relatado` com o trecho que mostra onde procurou (ex.: a tabela que só dá o coeficiente). Nunca invente, nunca use valor de outro estudo, nunca estime de figura sem dizer que veio de figura.

## Tarefa 3 — `estimando` a revisar

Para cada `id_efeito` em `estimando_a_revisar`: se o efeito é o contraste de braços aleatorizados analisados como aleatorizados, `estimando = ATE` (ou `ITT` se o texto diz intenção de tratar ou há não adesão); se o contraste não é entre braços aleatorizados (ex.: comparação dentro do sujeito, regressão sobre variável não atribuída), `estimando = associacao`. Registre o trecho que decide.

## Registro (obrigatório)

Grave `complementos_efeitos/<CHAVE>.json`: uma lista com um objeto por campo alterado ou procurado:

```json
[{"id_efeito": "X-E01", "campo": "p0", "valor_antigo": "", "valor_novo": "0.42",
  "status": "preenchido | derivado | nao_relatado | corrigido",
  "trecho": "trecho VERBATIM da camada de texto, até 40 palavras",
  "pagina": 12,
  "justificativa": "uma ou duas frases"}]
```

- `pagina` = índice da folha no ARQUIVO PDF (1 = primeira folha).
- `trecho` contíguo, copiado caractere por caractere (confira na camada de texto; não corrija ligaduras nem erros; não termine antes de travessão nem atravesse hifenização de fim de linha). Para `alvo_efeito`/`comparador_tipo` decididos só pelos campos do CSV, use `"trecho": ""`, `"pagina": ""` e diga na justificativa quais campos decidiram.

Responda ao coordenador com UMA linha: `OK <CHAVE>: alvo=<n linhas> dados=<n preenchidos>/<n pedidos> estimando=<n> direcao_corrigida=<n>` ou `FALHA <motivo>`.
