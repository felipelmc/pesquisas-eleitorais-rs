# Notas do coordenador — risco de viés (G7)

- A = claude-opus-5-5, B = claude-sonnet-5, avaliações independentes; mesmo prompt comum
  (`04-qualidade/prompt_rob_comum.md`) e mesmos parâmetros por texto (`_despacho_rob.json`).
- Correções de âncora feitas pelo coordenador (a resposta não muda; só o trecho que a sustenta):
  - B, Agranov2017a#mobilizacao, `resultado_avaliado`: a linha da Tabela 3 citada não existe na
    camada de texto (o PDF troca os espaços da tabela por "%"); âncora trocada pela legenda
    "Table 3: Observed Participation Propensities" (p. 21).
- Erro meu no despacho: a descrição de cada resultado em `_despacho_rob.json` foi cortada em 120
  caracteres nas primeiras 13 avaliações (até Cornejo2023a A). Os avaliadores localizaram o
  resultado pela tabela/coluna citada no início do texto e relataram OK; a partir de Cornejo2023a B
  o despacho leva o texto completo do modelo principal.
- Divergência de classificador: Bursztyn2023a#mobilizacao — A usou `desenho_epoc=grupo_controle`,
  B usou `its` (estudo de eventos do comparecimento diário em torno da divulgação). Com
  classificadores diferentes os critérios não coincidem e `qualidade consolidar` recusa o par.
  Resolver antes da fase 1: o árbitro decide o classificador (com trecho), e o avaliador que
  divergiu é refeito por subagente novo com o classificador fixado.
- Checagem intermediária (34 de 76 avaliações): A (Opus) com 0 problemas de citação em 22 fichas;
  B (Sonnet) com 13 em 21 fichas — 7 páginas trocadas por uma (Boukouras2020a D4 ×3, Erlich2023
  D3, Feltovich2022 ×2) e 6 trechos parafraseados ou lidos de tabela pulando coluna (Erlich2023
  ×2, Fichnova2015a, Gandhi2019, Feltovich2022, Geers2018 ×2). Corrigidos pelo coordenador contra a
  camada de texto; nenhuma resposta mudou. O padrão entra nas limitações (o modelo B erra mais a
  transcrição literal).
- Divergências de classificador até aqui: Boukouras2020a#apoio_ao_lider (A individual × B
  cluster) e Bursztyn2023a#mobilizacao (A grupo_controle × B its). Vão ao árbitro antes da fase 1.
- Segunda checagem (74 de 76): mais 25 citações do B corrigidas pelo coordenador — 8 páginas
  trocadas; 12 trechos em que o B "limpou" ligaduras ou trocou palavras (Klor2017a, cuja camada
  de texto troca fi/ff/fl por "…", "¤", "‡"; Stolwijk2016a "as used" × "as was used";
  Unkelbach2022a "that" × "this"; Stolwijk2019b "=" que o PDF extrai como "¼"); 5 âncoras
  trocadas por um trecho equivalente que existe na página (Schlegel2023 d4_q3, cuja frase citada
  é da vinheta do material suplementar e não está no PDF; Stolwijk2019b ×2, célula de tabela).
  Nenhuma resposta mudou. A (Opus) seguiu com 0 problemas em todas as fichas.
- Divergências de classificador (4): Boukouras2020a e Timotei2013a (RoB 2, individual ×
  cluster); Bursztyn2023a#mobilizacao e Morton2015a#apoio_ao_lider (EPOC, grupo controle × ITS).
- Classificadores fixados pelo coordenador pelas regras já escritas (prompt comum e seção 7 do
  protocolo), antes da consolidação; o avaliador que divergiu é refeito por subagente novo com o
  classificador dado, e a ficha antiga vai para `04-qualidade/_substituidas/`:
  - Boukouras2020a (RoB 2) = cluster: a condição vale para a sessão inteira ("a sessão ou o grupo
    inteiro recebe o tratamento → cluster"). Refeito o A.
  - Timotei2013a (RoB 2) = cluster: a exposição é entregue a grupos de 20. Refeito o B.
  - Bursztyn2023a#mobilizacao (EPOC) = its: estudo de eventos do comparecimento diário em Genebra em
    torno da divulgação, sem grupo controle separado nesse modelo. Refeito o A.
  - Morton2015a#apoio_ao_lider (EPOC) = its: a equação (2) compara inclinações antes e depois de
    2005 em série longa (eleições desde 1981), sem grupo controle separado. Refeito o B.
  Desvio declarado: no plano, o árbitro decidiria também o classificador.
- Morton2015a#apoio_ao_lider (B refeito): o avaliador relatou que um grep por fichas EPOC com its listou nomes de arquivo das duas pastas, inclusive o do A para o mesmo item, sem abrir conteúdo. Ressalva de independência registrada.

## EPOC fase 1 (23/09/2026, retomada)

- A primeira execução da fase 1 do EPOC falhou com "8 valores inválidos em A/B": 7 respostas das fichas A e 1 da ficha B (Grillo2024c `cg_outros_riscos`) traziam a justificativa depois de " — " dentro do campo de resposta (`proposta_alto — ...`). O coordenador moveu cada justificativa, sem alterar a resposta, para as Notas do codificador da própria ficha ("movida do campo de resposta pelo coordenador").
- Duas citações da ficha B de Morton2015a#apoio_ao_lider reprovadas no gate foram trocadas pelo texto literal da camada de texto, sem mudar a resposta: "electoral result" → "election result" (p. 18) e "-4.04*" → "−4.04∗" (p. 34, sinal de menos e asterisco tipográficos).
- Gate depois das correções: A 133/133 OK; B 57/57 OK. Fase 1: 7 resultados, 59 linhas, 9 desacordos (pendência P031). Domínios sinalizados por concordância baixa: `cg_caracteristicas_base`, `cg_contaminacao`, `cg_dados_incompletos`, `cg_linha_base_outcome` (n = 5 resultados, κ pouco informativo).
- O aviso de 16 pares ausentes em Chatterjee2019a (variáveis `its_*`) é esperado: o classificador `desenho_epoc = grupo_controle` dispensa o bloco de série interrompida.
