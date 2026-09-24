# Amostras da voz do autor (textos públicos de Felipe Lamarca)

Fontes: github.com/felipelmc/Survey-Research (listas/lista3 e lista4) e felipelmc.github.io (resumos em src/pages/pt-br/publications.astro). Uso: só como referência de estilo para os passes de voz; não copiar conteúdo.

## Resumos do site
Resumo
Este trabalho analisa os determinantes da aprovação de pautas na Câmara dos Deputados, com foco em fatores políticos e institucionais que condicionam o sucesso das proposições. A literatura sobre estudos legislativos e presidencialismo destaca como variáveis relevantes organização interna do Legislativo, pork barrel, disciplina partidária, acesso à informação, patronagem e tamanho e coesão da coalizão. Partindo desse debate, o trabalho investiga em que medida esses elementos afetam a probabilidade de aprovação das pautas ao longo do processo decisório. Metodologicamente, o estudo combina análise quantitativa de proposições legislativas e votações nominais com indicadores de coordenação partidária e características institucionais do processo legislativo. Ao articular a literatura de estudos legislativos com a de presidencialismo, argumentamos que a atuação da Câmara Baixa não pode ser compreendida a partir de uma única teoria de organização, mas sim a partir de uma combinação destas.
Resumo
No Brasil, a modelagem estatística é usada no campo de Ciências Sociais quase exclusivamente para explicar fenômenos, raramente para prevê-los. A difusão de técnicas de machine learning, porém, vem dissolvendo a fronteira entre estudos preditivos e causais: a predição serve de benchmark para teorias, revela onde os modelos falham e disciplina o uso da informação disponível. Tendo isto em vista, este manuscrito parte de duas questões. A primeira é substantiva: é possível prever, com boa acurácia, o desempenho eleitoral dos partidos nas eleições proporcionais para vereador usando apenas informação disponível antes do pleito? A segunda é metodológica: como se conduz, na prática, um exercício preditivo rigoroso, dos dados brutos à validação dos resultados? Respondemos com um tutorial reprodutível aplicado aos 92 municípios fluminenses em três eleições (2016, 2020 e 2024), em expansão para o conjunto dos municípios brasileiros.

## Survey-Research, tarefas III e IV (trechos)

### listas/lista3/lista3.qmd

# Introdução

Em desenhos amostrais simples, como o desenho AAS, a estimação da média e da variância é _straightforward_ -- afinal, conhecemos as probabilidades de inclusão de cada indivíduo da população na amostra. Por outro lado, desenhos amostrais simples como o AAS são raros por uma série de questões, incluindo logísticas, de custo, etc. Na prática, utilizamos desenhos bem mais complexos e, frequentemente, não inteiramente probabilísticos. 

Com efeito, temos probabilidades de inclusão desiguais e a amostra coletada acaba por não espelhar perfeitamente as características da população. Para lidar com isso, utilizamos estratégias de ponderação: a partir de variáveis auxiliares, estimamos pesos que nos permitem aproximar os totais amostrais dos totais populacionais [@lumley2011complex; @wolf2016analysis]. Nesta tarefa, trabalho com a amostra do Estudo Eleitoral Brasileiro (ESEB) de 2022, realizada pelo Cesop e pela Quaest. Ela foi coletada com um desenho de _area-sampling_ com quotas em três estágios: sorteio de municípios e setores, por PPT; e seleção de pessoas entrevistadas por quotas. Dado esse desenho completo, implemento duas abordagens de pós-ajuste simples e independentes, que comparo na seção de resultados: pós-estratificação e rake. 

Esta tarefa está dividida em algumas seções, além desta introdução. A seguir, na seção de _setup_, faço uma série de manipulações nas bases utilizadas na tarefa; depois, apresento a metodologia em duas partes: na primeira, comparo as distribuições de variáveis demográficas na amostra e na população para escolher quais delas serão utilizadas no pós-ajuste; na segunda, implemento as duas abordagens de pós-ajuste. Por fim, nos resultados, comparo as estimativas obtidas a partir de cada estratégia de ponderação com o parâmetro populacional verdadeiro (quando conhecido, é claro) e com a estimativa obtida a partir do uso da amostra sem ponderação. Os resultados mostram que ambas as abordagens melhoram a qualidade das estimativas, ainda que com ganhos sutis em algumas variáveis e ganhos mais relevantes em outras.

# _Setup_ da tarefa e manipulação dos dados

No _chunk_ de código abaixo, importo todas as bibliotecas necessárias para a realização da tarefa, defino uma `seed` arbitrariamente escolhida e faço a leitura dos dados. No caso do banco de dados amostral, importamos uma base fornecida na descrição da tarefa; no caso do censo de 2022, importamos os dados por intermédio da biblioteca `sidrar`.


# pacotes utilizados
library(modelsummary)
library(tidyverse)
library(gt)
library(sidrar)
library(stringr)
library(stringi)
library(survey)
library(patchwork)

# seed
set.seed(42)

# dados do eseb (amostra)
eseb22 <- read.csv("data/eseb22.csv")

# dados do censo (via sidrar)
censo22 <- get_sidra(
  api = paste0(
    "/t/10061/n3/all/v/allxp/p/all/",
    "c1568/allxt/",
    "c58/1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,2503,100052/",
    "c2/allxt/",
    "c86/allxt"
  )
)


Note que os formatos das tabelas são distintos. Na base do ESEB, cada linha representa um respondente; na base do censo, por outro lado, as informações são agregadas, o que significa que cada linha representa uma combinação de uma série de variáveis sociodemográficas, e a coluna `Valor` indica o número de indivíduos da população brasileira que se enquadram naquela particular combinação.

Uma etapa importante e que deve ser realizada antes da etapa de ponderação é o tratamento das bases de dados. Em particular, para realizar os pós-ajustes de maneira adequada, é importante que as categorias das variáveis auxiliares sejam compatíveis entre as duas bases. Por conta disso, empreendemos uma série de tratamentos, incluindo desde a filtragem de colunas até a recodificação de variáveis sociodemográficas. No caso do censo de 2022 foi necessário, por exemplo, recodificar as categorias das variáveis de idade, cor/raça e sexo. Já no caso do ESEB, recodificamos algumas variáveis para facilitar a interpretação dos resultados. Removemos também a parte da amostra composta por menores de 18 anos, já que a base do censo extraída do censo não dispõe dessa informação

### listas/lista4/lista4.qmd

# Introdução

A técnica de _Multilevel Regression with Poststratification (MRP)_ combina dois passos complementares. No primeiro, ajusta-se um modelo de regressão multinível que estima, para cada estrato sociodemográfico relevante (UF, sexo, idade, cor/raça, escolaridade etc.), a probabilidade de o respondente exibir o comportamento ou atitude de interesse. No segundo passo, essas probabilidades são pós-estratificadas: multiplicamos cada predição pelo tamanho real de seu estrato na população (aqui, a PNAD Contínua), gerando uma estimativa ponderada que corrige as distorções da amostra original.

A regressão multinível é uma técnica estatística que permite modelar dados com estrutura hierárquica ou agrupada -- como indivíduos dentro de estados, partidos, ou outras unidades geográficas ou sociais @gelman2007data. Esse modelo incorpora variações em diferentes níveis ao permitir que interceptos (e, se necessário, coeficientes) variem entre grupos, ao invés de assumir que todos os grupos compartilham os mesmos parâmetros. Essa abordagem é especialmente poderosa porque melhora a precisão das estimativas em subgrupos com poucos dados, utilizando o conceito de "shrinkage", que suaviza estimativas extremas com base na média geral, equilibrando variabilidade e robustez.

Aplicamos esse procedimento a um survey _online_ com 2.015 adultos brasileiros recrutados via Facebook @smith2024religion. Primeiro, diagnosticamos os vieses da amostra comparando-a à estrutura populacional. Em seguida, faço uma análise exploratória -- conforme sugerido por @ghitza2013deep -- não-exaustiva para, finalmente, testar duas especificações de MrP para estimar a proporção de voto em Jair Bolsonaro no 1º turno de 2018 -- cujo valor, conhecido, é de 46.03%, útil como _ground truth_. O modelo mais simples, apenas com interceptos variáveis, subestimou o apoio. O segundo, incluindo _slopes_ variáveis para idade e escolaridade por estado, convergiu para a proporção verdadeira.

Com essa especificação mais robusta projetamos, então, a proporção da população contrária à legalização do aborto. O MrP indica que cerca de 67% dos brasileiros se declaram contra, resultado alinhado às pesquisas publicadas pela Datafolha (2024) e Quaest (2023) há não muito tempo atrás. Regionalmente, a oposição é maior no Sul e Centro-Oeste e menor no Norte. Em geral, o exercício mostra como, mesmo partindo de um survey não-probabilístico e enviesado, o MrP permite recuperar estimativas nacionais próximas da realidade demográfica.

# _Setup_ da tarefa e manipulação dos dados

Aqui, simplesmente faço a importação das bibliotecas necessárias à análise, defino uma seed e faço a leitura dos dados. Note que extraio também dados do pacote `geobr` para possibilitar a apresentação de algumas análises exploratórias na forma de mapas. No mais, crio uma coluna nos dois bancos de dados principais derivando a região à qual cada estado pertence.


# bibliotecas necessarias
library(tidyverse)
library(geobr)
library(sf)
library(scales)
library(rlang)
library(lme4)
library(gt)

# seed (modelos multinivel sao ajustados por algoritmos de otimizacao)
set.seed(42)

# leitura dos bancos -- estratos e o survey
load("data/estratos.Rda")
df <- read.csv("data/smith_boas_2019.csv")

# Baixa os dados geográficos das UFs
ufs_sf <- geobr::read_state(code_state = "all", year = 2019)

# Mapeamento de UF para Região
uf_para_regiao <- c(
  # Norte
  "AC" = "Norte", "AP" = "Norte", "AM" = "Norte", "PA" = "Norte",
  "RO" = "Norte", "RR" = "Norte", "TO" = "Norte",

  # Nordeste
  "MA" = "Nordeste", "PI" = "Nordeste", "CE" = "Nordeste", "RN" = "Nordeste",
  "PB" = "Nordeste", "PE" = "Nordeste", "AL" = "Nordeste", "SE" = "Nordeste",
  "BA" = "Nordeste",
