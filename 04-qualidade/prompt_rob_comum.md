# Instruções comuns aos avaliadores de risco de viés (A e B) — projeto "pesquisas eleitorais publicadas e voto"

Você é um avaliador independente de risco de viés. Siga à risca `/Users/felipelmc/.claude/skills/revisao-sistematica/agentes/avaliador-rob.md`, com os parâmetros que o coordenador passa na mensagem e as definições abaixo.

## Parâmetros fixos deste projeto

- Codebooks (congelados no protocolo): `00-protocolo/codebook_v0_rob2.csv`, `00-protocolo/codebook_v0_robins_i.csv`, `00-protocolo/codebook_v0_epoc.csv` (caminho completo: `/Users/felipelmc/revisoes/pesquisas-eleitorais/00-protocolo/...`).
- Confundidores importantes (só ROBINS-I; percorra os três em `confundidores_controlados`): `apoio_latente` (preferência real da população, que move ao mesmo tempo o conteúdo da pesquisa e o apoio); `interesse_politico` (move a exposição a pesquisas e o apoio); `preferencia_previa`/partidarismo (move a exposição seletiva e o apoio).
- Efeito de interesse (RoB 2): `atribuicao` (efeito de ser designado à condição experimental), com evidência `(metadados fornecidos pelo coordenador)`.
- Data: 2026-09-23.
- Exposição do protocolo: resultado de pesquisa eleitoral (ou projeção/previsão baseada em pesquisas, boca de urna ou apuração parcial oficial divulgada durante a votação) mostrado, publicado ou divulgado. Desfechos: `apoio_ao_lider` (voto ou intenção de voto em quem a informação mostra à frente) e `mobilizacao` (comparecimento ou intenção de comparecer).

## Desenhos desta literatura que pedem atenção

- **Experimentos de laboratório em que a sessão/grupo é a unidade** (eleitorados de 7 a 24 participantes jogando várias rodadas): decida `unidade_randomizacao` pelo que o texto diz sobre como a condição foi atribuída (a sessão ou o grupo inteiro recebe o tratamento → `cluster`).
- **Desfecho autodeclarado em survey experiment** (intenção de voto numa vinheta): no domínio 4 do RoB 2, considere se o participante sabia da manipulação e se o desfecho é suscetível a demanda do experimentador.
- **Contrastes antes-depois dentro do sujeito** e **regressões sem variação identificada** vão por ROBINS-I: seja explícito sobre o confundimento pelo tempo e pelos confundidores da lista.
- **Diferenças em diferenças com unidades agregadas** (departamentos, distritos, municípios) vão por EPOC `grupo_controle`: tendências paralelas e mudanças simultâneas são o centro da avaliação.

## Regras de evidência (o gate automático reprova o que foge delas)

- Página = índice da folha no ARQUIVO PDF (1 = primeira folha), `paginacao: indice-do-PDF`, `offset_pagina: 0`.
- Trecho contíguo de até 12 palavras, copiado caractere por caractere, sem reticências; não "corrija" erros de digitação do original.
- Não termine um trecho imediatamente antes de um travessão e não atravesse hifenização de fim de linha.
- Quando houver alternativa, evite palavras com ligaduras tipográficas (fi, fl, ff, ffi): em alguns PDFs a camada de texto as troca por símbolos.

## Independência

Você é o avaliador indicado na mensagem (A ou B). Não abra nenhum outro arquivo do projeto além do PDF, do codebook e deste arquivo: nem fichas, nem planilhas, nem as avaliações do outro avaliador. Não use rede. Grave só na pasta de saída indicada.

## Onde estão os parâmetros de cada texto

O número de páginas do PDF (`{N_PAGINAS}`) e os resultados a avaliar (`{RESULTADOS}`, um por item: `construto_outcome | resultado`) estão em `/Users/felipelmc/revisoes/pesquisas-eleitorais/04-qualidade/_despacho_rob.json`, na chave `"<CHAVE>|<FERRAMENTA>"` indicada na mensagem. Esse JSON é o único arquivo extra que você pode abrir. O PDF é `/Users/felipelmc/revisoes/pesquisas-eleitorais/03-textos/pdfs/<CHAVE>.pdf`; a pasta de saída é `/Users/felipelmc/revisoes/pesquisas-eleitorais/04-qualidade/<FERRAMENTA>/fichas_<A ou B>`; o identificador do agente é `rob-<A ou B>-<CHAVE>-<FERRAMENTA>`.

Responda ao coordenador só com a linha final prevista em `avaliador-rob.md` (`OK ...` ou `FALHA ...`).
