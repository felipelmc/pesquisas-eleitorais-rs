# Notas do coordenador — extração completa (G7)

## Pendências abertas para resolver depois das ondas de fichamento

- **Freden2016b**: o PDF em `03-textos/pdfs/Freden2016b.pdf` é só o "kappa" (capítulo introdutório) da tese de doutorado por compilação; os quatro artigos empíricos (incluindo o Artigo 2, o survey experiment com pesquisas manipuladas na Suécia 2013/2014, que é o desenho relevante para o protocolo) não estão no arquivo — só o sumário nas páginas impressas 47, 69, 95 e 125. A ficha ficou com quase todo o bloco 13 em 999 por essa razão, não por falha do fichador. Ação necessária: localizar e baixar o Artigo 2 (capítulo publicado em livro Springer sobre "Voting Experiments", segundo a própria tese) ou a tese completa com os quatro artigos, e refichar.

## Correções de gate feitas pelo coordenador (rodada completa, antes de refazer com subagente novo)

O gate (`verify_citacoes.py`) reprovou 11 citações em 9 fichas na primeira passada. Conferi cada uma contra a camada de texto do PDF e corrigi diretamente (sem novo subagente, por serem erros pontuais de transcrição/paginação, não de conteúdo):

- Agranov2017a (mecanismo_id): página errada (p. 2 → p. 3, mesmo offset).
- Alabrese2024a (mecanismo_tipo_evidencia): citação cortada bem na hifenização de fim de linha ("media-"); completada para "mediator".
- Chatterjee2019a (pais_estudo, regiao): a ficha "corrigiu" o erro de digitação do próprio PDF ("Arunchal" → "Arunachal"); restaurada a grafia impressa.
- Cornejo2023a (problema_pesquisa): faltava a palavra "that" presente no original.
- Farjam2020a (outcome_medida): "based on" no lugar de "by", presente no original.
- Gasperoni2015a (populacao + nota do codificador): a ficha registrou "thorough" como o erro de digitação verbatim, mas o PDF traz "thorugh" (typo diferente); corrigido e a nota do codificador também.
- Morton2015a (b2_estimando): ordem de palavras trocada ("difference-in-difference (DID) estimator" → "difference-in-difference estimator (DID)", como impresso).
- Schlegel2023 (construto_outcome, alvo_efeito): faltava "the" antes de "Candidate".

**Aceito sem correção, com justificativa (mesmo critério do piloto G6):** Araujo2021a, `b2_n_total` — o número (452.656) só existe rasterizado dentro da Figura 2, sem camada de texto; conferido visualmente pelo coordenador, é o mesmo caso documentado em `05-decomposicao/piloto/notas_gate.md`.

## Lammers2022a: os efeitos extraídos não isolam o efeito principal da exposição

Os Estudos 2a/2b cruzam dois fatores manipulados: a posição mostrada na pesquisa (90% vs. 10%
de apoio ao candidato preferido, a exposição do protocolo) e o modo de raciocínio induzido
(heurístico vs. moral-igualdade). Os autores não reportam o efeito principal nem o efeito
simples da posição isoladamente — só a interação e o efeito simples do MODO dentro de cada
posição (heurístico vs. moral-igualdade, condicionado à posição mostrada). Os dois `d` extraídos
como `modelo_principal` (E01: d=0,73; E03: d=0,58) medem, portanto, o efeito do modo de
raciocínio sob exposição, não o efeito da exposição em si.

Isso é uma limitação do que o próprio artigo reporta, não um erro de extração. Fica registrado
para a síntese (G8): considerar excluir Lammers2022a da meta-análise do efeito principal de
`apoio_ao_lider` (célula pesquisa_pre_eleitoral, survey experiment) ou tratá-lo só como
evidência de mecanismo/moderador na síntese narrativa, com a ressalva explícita de que os
tamanhos de efeito disponíveis não isolam a exposição à pesquisa.

## Correção de instrução minha: Brugarolas2021

Instruí o extrator de efeitos com `outcomes: apoio_ao_lider`, mas este texto mede só
`mobilizacao` (intenção de comparecer) — erro meu, não conferi a ficha antes de montar o
prompt. O subagente corrigiu sozinho, com base na própria ficha e no protocolo, e registrou
`construto_outcome = mobilizacao` corretamente. Também ajustei `estimando` de `RDD_local` para
`ITT` no CSV de efeitos, para ficar consistente com a ficha (o texto discute explicitamente
"could be treated as an intention to treat (ITT) effect", que tem prioridade sobre RDD_local na
ordem da Emenda 2).

## Convenção or_=exp(beta) para coeficiente logit sem OR impresso — não uniformizada

Cornejo2023a apontou uma inconsistência real: Meer2015a e Cornejo2023a calcularam
`or_ = exp(beta)` quando o texto só imprime o coeficiente logit (log-odds) e o EP, sem razão de
chances; Geers2018 deixou `or_` vazio no mesmo tipo de situação. Verifiquei os valores: em
Meer2015a e Cornejo2023a os coeficientes são de magnitude plausível para log-odds (ordem de
0,1 a 2,4), e `exp(beta)` é uma transformação exata, não uma invenção — mantive a convenção.
Em Geers2018 os coeficientes são -30,8 e -5,7, associados a um preditor contínuo de escala
estreita (DP ≈ 0,21): `exp(-30,8)` daria uma razão de chances implausível. Não uniformizei às
cegas. Decisão: deixar como está e deixar o alerta de plausibilidade de `analise
verificar-efeitos` (|g| > 2) sinalizar Geers2018 quando a etapa rodar, para conferência humana
específica desse caso (conferir se o EP foi lido como DP, a unidade do preditor, ou se o
coeficiente reportado é de fato log-odds por unidade cheia do índice 0-1).
