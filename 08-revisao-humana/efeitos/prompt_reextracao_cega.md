# Re-extração cega dos efeitos principais: projeto "pesquisas eleitorais publicadas e voto"

Você é um segundo extrator, independente. A partir de UM texto completo, extrai o(s) efeito(s) do **modelo principal** de cada construto do protocolo. Esse estudo já foi extraído por outro agente, mas você **não vê** essa extração. A comparação entre as duas mostra ao revisor humano onde conferir primeiro (pendência P032). O coordenador passa a `CHAVE` na mensagem.

Raiz do projeto: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.

## Arquivos que você pode abrir (e só estes)

- PDF: `03-textos/pdfs/<CHAVE>.pdf`. Leia pela camada de texto com pymupdf. Quando a camada de texto embaralhar as colunas de uma tabela, renderize a página e confira.
- Protocolo: `00-protocolo/protocolo.md`, seções 2 (construtos, exposição, comparadores) e 6 (extração), só para consulta.
- Codebook: `00-protocolo/codebook_v0_efetividade.csv`, linhas `b2_modelo_principal`, `b2_criterio_modelo_principal` e `b2_estimando` (regra da Emenda 2).

**Proibido:** abrir `05-decomposicao/`, `06-analise/`, `08-revisao-humana/` (exceto o seu arquivo de saída) ou qualquer outra extração; usar a rede; rodar `rs.py`.

## O que extrair

1. **Construtos.** Identifique quais construtos do protocolo o estudo analisa:
   - `apoio_ao_lider`: apoio ou intenção de voto numa opção, conforme a posição em que a pesquisa a mostra;
   - `mobilizacao`: comparecimento ou intenção de votar.
2. **Modelo principal.** Para cada construto, localize o modelo principal pela ordem do codebook e use a primeira que der resultado:
   1. `declarado_pelos_autores`;
   2. `usado_na_interpretacao` (o número repetido no resumo ou na conclusão);
   3. `regra_do_protocolo`.

   Se o estudo trata amostras ou rodadas como igualmente centrais, liste cada uma.
3. **Uma linha por estimativa** do modelo principal, com o contraste da exposição à pesquisa. Os campos seguem os nomes do CSV de efeitos da revisão:
   - `outcome` (como o texto nomeia) e `construto_outcome`;
   - `modelo`: tabela, coluna, especificação e controles, com a página impressa e a folha do PDF;
   - `subgrupo`, com vazio quando não houver;
   - `alvo_efeito`: `lider` | `azarao` | `opcao_referendo` | `segundo_viavel` | `terceiro_inviavel` | `partido_abaixo_clausula` | `nao_se_aplica`;
   - `comparador_tipo`: `sem_pesquisa` | `mesmo_candidato_atras` | `outro_resultado` | `antes_depois_proibicao` | `unidades_nao_expostas` | `outro`;
   - `desenho` (escreva "randomizado" só se o contraste for entre braços aleatorizados) e `estimando`: `ATE` | `ITT` | `LATE` | `associacao`;
   - `tipo_estatistica`: `md` | `dif_prop` | `or` | `beta` | `t` | `f` | `r` | `outro`;
   - os números **como impressos**, nos campos que existirem: `m1`, `sd1`, `n1`, `m2`, `sd2`, `n2`, `t`, `df`, `f`, `beta`, `se`, `sdy`, `or_`, `ci_lo`, `ci_hi`, `r`, `p`, `n_total`, `p0`, `p1`, `efeito_pp`, `se_pp`. O sinal fica como impresso. Distinga desvio-padrão de erro-padrão pelo que o texto diz.
   - `cluster`: tamanho médio do conglomerado, quando a unidade atribuída for sessão ou grupo; senão, vazio;
   - `evidencia`: trecho **verbatim** da camada de texto, com até 40 palavras, contíguo, copiado caractere por caractere;
   - `pagina`: índice da folha no arquivo PDF (1 = primeira folha);
   - `origem_valor`: `impresso` | `derivado` (conta sobre números impressos; mostre a conta em `nota`) | `lido_de_figura` | `nao_relatado`;
   - `nota`: uma ou duas frases, com qualquer dúvida (rótulo ambíguo, EP ou DP, unidade do preditor, controle compartilhado entre contrastes, conglomerado).
4. **Números.** Nunca invente um número nem estime de figura sem marcar `lido_de_figura`. Se o estudo não tiver o contraste da exposição (por exemplo, o principal é um modelo teórico ou outra manipulação), diga isso em `nota` e registre o que existe.

## Saída

Grave `08-revisao-humana/efeitos/cega/<CHAVE>.json`:

```json
{"chave": "<CHAVE>", "modelo_extrator": "claude-opus-5-5",
 "construtos": ["apoio_ao_lider"],
 "criterio_modelo_principal": {"apoio_ao_lider": "declarado_pelos_autores"},
 "localizacao_modelo_principal": {"apoio_ao_lider": "Tabela 2, col. 3 (p. 14; folha 15)"},
 "efeitos": [ { "...campos acima..." } ]}
```

Confira o JSON com `python3 -c "import json; json.load(open('<arquivo>'))"`. Responda ao coordenador com UMA linha: `OK <CHAVE>: <n> efeitos, construtos=<lista>` ou `FALHA <motivo>`.
