# Árbitro de efeitos: extração original × re-extração cega (P032, preparação)

Duas extrações de IA dos efeitos principais do mesmo estudo divergem. A primeira é a **original**, já usada na síntese; a segunda é a **cega**, feita sem ver a original. Você decide, pelo texto e pelas convenções do projeto, o que está certo e propõe as correções. Suas propostas são aplicadas pelo coordenador. `verificado_humano` continua vazio: a conferência humana vem depois. O coordenador passa a `CHAVE`.

Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`.

## Leia

1. A extração original: `05-decomposicao/efeitos/<CHAVE>.csv`, com todas as linhas. As principais têm `modelo_principal = sim`.
2. A cega: `08-revisao-humana/efeitos/cega/<CHAVE>.json`.
3. As divergências já detectadas: as linhas de `<CHAVE>` em `08-revisao-humana/efeitos/comparacao_cega.csv`. O script só compara números e rótulos; confira também o que ele não pega.
4. O PDF: `03-textos/pdfs/<CHAVE>.pdf`. Leia com pymupdf e renderize a página quando uma tabela embaralhar.
5. As convenções do projeto:
   - `00-protocolo/protocolo.md`, seções 2, 6 e 8;
   - `00-protocolo/codebook_v0_efetividade.csv`, linhas `b2_modelo_principal`, `b2_criterio_modelo_principal` e `b2_estimando`;
   - `00-protocolo/emendas.md`, Emendas 2, 4 e 5;
   - o dicionário `FORA` no topo de `06-analise/montar_entradas_swim.py`, que lista efeitos principais que não estimam o contraste da exposição;
   - as notas deste estudo em `05-decomposicao/notas_extracao_completa.md` (busque por `<CHAVE>`);
   - as definições de campo em `05-decomposicao/prompt_complemento_efeitos.md`, tarefas 1 e 2. Os caminhos citados nesse prompt usam uma raiz antiga; troque-a pela raiz acima.

## Convenções que decidem os casos comuns

- **Sinal e direção.** O sinal fica como impresso. `direcao_desejada` é `aumentar` para os alvos `lider`, `opcao_referendo` e `segundo_viavel`, e `reduzir` para `azarao`, `terceiro_inviavel` e `partido_abaixo_clausula`. Nos desenhos de proibição (Chatterjee2019a, Morton2015a), a linha registra o efeito **da exposição**, isto é, o efeito da proibição com o sinal invertido (Emenda 5, item 3). Uma "diferença de sinal" que se explique por essas regras não é erro.
- **Comparador:**
  - `outro_resultado`: o grupo de comparação viu **outra pesquisa ou outro resultado**;
  - `sem_pesquisa`: o grupo de comparação não viu pesquisa;
  - `mesmo_candidato_atras`: o mesmo candidato é mostrado em outra posição;
  - `unidades_nao_expostas`: unidades observacionais sem exposição;
  - `antes_depois_proibicao`;
  - `outro`: só quando nenhum dos anteriores serve.
- **Alvo:** é a posição da opção cujo apoio é medido **na informação recebida**. Manipulação de tendência sem posição (*momentum*) recebe `nao_se_aplica` (Emenda 4b).
- **Modelo principal:** segue a ordem da Emenda 2. Não troque o modelo principal só porque a cega escolheu outro. Troque quando o texto mostrar que a regra leva a outro modelo, e cite o trecho.
- **Classe de desenho:** o campo `desenho` precisa conter "randomizado", "RCT" ou "aleatori" só quando o contraste é entre braços atribuídos por sorteio.

## Para cada divergência (e para qualquer erro que você encontrar)

Decida entre `manter`, quando a original está certa, e `corrigir`, quando está errada. Em `corrigir`, dê o valor novo de cada campo. Não mexa em `verificado_humano`, `ficha_id`, `chave` nem `id_estudo`. Não crie linhas novas, a menos que o efeito principal esteja ausente na original. Nesse caso, proponha uma linha completa com `id_efeito` no formato `<CHAVE>-Enn`, com o próximo número livre.

## Saída

Grave `08-revisao-humana/efeitos/arbitragem/<CHAVE>.json`:

```json
{"chave": "<CHAVE>", "resumo": "duas ou três frases",
 "decisoes": [
  {"id_efeito": "<CHAVE>-E01", "divergencia": "o que divergia", "veredito": "manter|corrigir",
   "alteracoes": [{"campo": "comparador_tipo", "de": "outro", "para": "outro_resultado"}],
   "trecho": "verbatim, até 40 palavras", "pagina": 12, "justificativa": "uma ou duas frases"}
 ],
 "linhas_novas": []}
```

`pagina` é o índice da folha no PDF. Os nomes de `campo` são os do cabeçalho do CSV original. Confira que o JSON carrega. Responda com UMA linha: `OK <CHAVE>: <n> decisões (<n> corrigir, <n> manter)`.
