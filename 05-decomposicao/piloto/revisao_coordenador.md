# Revisão do piloto de extração (G6) — feita pelo coordenador de IA, autopiloto

Sem validação humana desta etapa (atalho do projeto). Esta é a revisão de coordenador prevista
na seção 5.6 da referência de decomposição, registrada aqui em vez de feita por um humano; a
pendência formal `revisao_piloto` fica aberta para quem quiser conferir depois.

## Textos do piloto

Meer2015a (survey experiment online, RCT individual), Klor2017a (experimento de laboratório +
análise correlacional de eleições reais), Araujo2021a (experimento natural, apuração parcial
oficial no Brasil — caso da Emenda 1). Todos classificados `tipo_estudo = b2`, sem fronteira
a1/a2 ambígua (não havia blocos a1/b1 no codebook desta revisão).

## O que a recodificação cega revelou

Concordância geral 81% (3 textos, `05-decomposicao/piloto/concordancia/RELATORIO_CONCORDANCIA.md`).
Duas variáveis categóricas ficaram abaixo do limiar do protocolo (κ ou PABAK ≥ 0,7):
`b2_estimando` (κ = 0,40) e `b2_criterio_modelo_principal` (κ = -0,50). Ação: Emenda 2 ao
codebook (`00-protocolo/emendas.md`), com regra de decisão operacional para as duas variáveis
e para `b2_modelo_principal`. As demais variáveis sinalizadas eram campos textuais livres, com
concordância naturalmente baixa por parafraseio (documentado no próprio relatório de
concordância) — não pedem mudança.

## Problemas de gate encontrados e tratados

1. **Araujo2021a, `b2_n_total`**: número só existe rasterizado dentro de uma figura (sem camada
   de texto). Conferido visualmente pelo coordenador, aceito com justificativa
   (`05-decomposicao/piloto/notas_gate.md`), mesmo critério já usado na fase de elegibilidade
   para falhas de gate por limitação técnica do arquivo.
2. **Klor2017a, dois `modelo_principal = sim`** no CSV de efeitos para o mesmo estudo ×
   construto: o experimento de laboratório (aleatorizado) e a análise transversal de eleições
   reais (que os próprios autores chamam de correlacional). Corrigido pelo coordenador: só o
   experimento de laboratório fica principal, porque é o que satisfaz o critério C4 de
   elegibilidade do protocolo e porque desenho aleatorizado e não aleatorizado nunca se agregam
   na síntese deste projeto. Documentado em `05-decomposicao/piloto/notas_gate.md`.
3. **Araujo2021a, ausência de `p0`** em 8 das 9 linhas de efeito (só a primeira tem o
   percentual de base, de uma nota de rodapé): sem ele, `efeitos.R` não converte
   `efeito_pp` em tamanho de efeito padronizado para essas linhas, inclusive a principal do
   segundo turno (E06). Não investigado mais a fundo neste piloto porque Araujo2021a será
   refichado e reextraído na rodada completa (Emenda 2, não repetição do piloto); fica
   registrado para a extração completa procurar essa informação com mais cuidado (nota de
   rodapé equivalente para o segundo turno, ou apêndice online, se disponível).
4. **Klor2017a, `sdy` ausente** nos três coeficientes de probit de efeitos aleatórios (escala
   latente, sem desvio-padrão do desfecho em escala observável relatado no texto): mesmo
   tratamento, fica para a extração completa decidir se algum outro trecho do artigo (por
   exemplo, a taxa de comparecimento agregada) permite aproximar `sdy`, ou se a linha entra só
   na síntese narrativa (SWiM) sem entrar na meta-análise.

## Coerências verificadas no master consolidado

`mecanismo_id` = Não ⇔ `mecanismo_tipo_evidencia` = `nao_discutido`: ok nos três textos.
`het_metodo` = `nenhum` ⇔ `het_pre_especificada` = `nao_se_aplica`: não se aplicou (os três
textos relataram heterogeneidade). Nenhum `tipo_estudo = 999`.

## Decisão sobre repetir o piloto

Não repetido. As mudanças no codebook (Emenda 2) são redações mais operacionais das mesmas três
variáveis, não uma mudança de estrutura ou de blocos do codebook — não é o caso de "mudança
grande" que a referência da skill (06-decomposicao.md, seção 5, passo 7) reserva para repetir o
piloto com textos novos. Os três textos do piloto serão refichados (não reaproveitados) quando
entrarem na rodada completa de extração, já com a redação emendada.
