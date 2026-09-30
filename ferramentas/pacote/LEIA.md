# Pacote de replicação

**Pesquisas eleitorais publicadas mudam o voto?** Síntese sistemática de evidências, conduzida com agentes de IA, sobre os efeitos *bandwagon* e *underdog* e o comparecimento. Felipe Lamarca (MAPE/IESP-UERJ) e Lucas Berti (IESP-UERJ), com contribuição igual; versão de 30/09/2026.

- Artigo com apêndices: `artigo/revisao.pdf`.
- Página do projeto: <https://felipelamarca.com/pesquisas-eleitorais-rs/>.

## O que foi e o que não foi validado por humano

Triagem, elegibilidade, extração, risco de viés e certeza foram feitos por agentes de IA. Os autores conferiram, em bloco e sem dupla conferência independente, as partes abaixo e confirmaram as decisões em vigor (`08-revisao-humana/declaracao_autor_2026-09-30.md` e `declaracao_autores_2026-09-30_coautoria.md`; Emenda 7 em `00-protocolo/emendas.md`):
- na busca, a pré-revisão PRESS feita por IA;
- na triagem, as 81 divergências entre os triadores de IA;
- na elegibilidade, as 165 propostas da IA e as 3 extensões de regra;
- o piloto de extração;
- os 560 efeitos, contra a página dos PDFs;
- as divergências da recodificação;
- o relato.

A deduplicação dos 145 pares candidatos, decidida pelos autores, foi aplicada depois da triagem, com os 9 pares de versão ligados por eles (Emenda 8; `08-revisao-humana/P019_dedup/`). O `motivo` das 145 linhas de `dedup_revisao_v1.csv` foi escrito na Emenda 7 ("decisão registrada e não aplicada nesta versão"); as decisões foram aplicadas em 30/09/2026 pela Emenda 8.

**Não** tiveram validação humana:
- o risco de viés;
- os juízos de certeza (GRADE);
- a validação cega da triagem.

Os autores estão revendo o risco de viés e o GRADE. A lista das pendências abertas está em `07-relatorio/_pendencias_abertas.json`. As descrições dessa lista são as registradas na abertura de cada pendência; a declaração de uso de IA (`07-relatorio/declaracao_uso_ia.md`, seções 6 e 7) anota o que mudou desde então, como a conferência dos 560 efeitos, citada ainda como pendente na descrição da P033.

## Conteúdo

| Pasta | O que tem |
|---|---|
| `00-protocolo/` | protocolo congelado, emendas (E001, E002 e 1 a 8), pergunta, teoria do programa, *codebooks* |
| `01-busca/` | as quatro estratégias ativas (OpenAlex em inglês, português e espanhol; BDTD), log de buscas, conferência do PRESS |
| `dados/` | registros deduplicados, só com metadados bibliográficos (sem resumo, sem instituição, sem e-mail) |
| `02-triagem/`, `03-textos/` | decisão final de títulos e resumos e de texto completo, com o critério que falhou |
| `04-qualidade/` | risco de viés por domínio (RoB 2, ROBINS-I V2, EPOC) e geral |
| `05-decomposicao/` | fichamentos (sem o caminho local do PDF) e efeitos por estudo, com trecho e página |
| `06-analise/` | efeitos calculados, entradas e saídas da SWiM (principal e sensibilidades), metas exploratórias, certeza |
| `07-relatorio/` | incluídos, contagens e diagrama PRISMA, listas PRISMA e SWiM, declaração de uso de IA gerada do log |
| `08-revisao-humana/` | declarações dos autores (conferência em bloco, deduplicação e coautoria) e as decisões de deduplicação dos pares (sem resumos) |
| `09-documento-final/` | `declaracao_ia_v2.md`: os agentes de IA que prepararam o texto, com modelo e *hash* dos *prompts* |
| `skill-revisao-sistematica/` | cópia dos scripts da skill que rodou a revisão (`rs.py`, `rslib/`, `R/`), com a licença do autor da skill |
| `tabelas-extras/` | estudos da região e efeitos de viabilidade, e as listas de conferência (PRISMA 2020, resumo, PRISMA-S, SWiM, PRISMA-trAIce), com o local de cada item no artigo final e nos apêndices |
| `MANIFESTO.csv` | caminho, origem, tamanho e SHA256 de cada arquivo |
| `CITATION.cff`, `LICENSE`, `LICENSE-CC-BY-4.0.md`, `ambiente.txt` | como citar, licenças e versões do ambiente |

## O que se reproduz com este pacote

- **Com o pacote e a skill incluída** (Python 3, R com `metafor` e `clubSandwich`, versões em `ambiente.txt`), um terceiro consegue refazer, a partir dos efeitos extraídos, a síntese inteira:
  - o cálculo dos efeitos;
  - as células;
  - a SWiM principal e as sensibilidades;
  - as metas exploratórias.

  Use os comandos de `rs.py analise …` e os scripts `06-analise/montar_*.py`, na ordem descrita no artigo (seção de métodos): preparar os efeitos, calculá-los, montar as entradas da SWiM e as metas exploratórias e rodar a SWiM principal e as sensibilidades.
- **Depende dos PDFs**, que não podem ser redistribuídos: conferir os trechos e as páginas citados nas fichas e nos efeitos. As referências completas dos estudos estão no artigo.
- **Fica fora do pacote**: os lotes de triagem e os pareceres dos triadores de IA, que citam trechos dos resumos de terceiros, e também as fichas em Markdown, os *prompts* e o log bruto. As fichas, os *prompts*, o log e as decisões de triagem registro a registro sem os trechos (`publico/decisoes_sem_trechos.csv`) estão no repositório público do projeto (<https://github.com/felipelmc/pesquisas-eleitorais-rs>). Os resumos de terceiros, os lotes, os pareceres e o registro de decisões com trechos ficam só com os autores, com acesso sob pedido.

## Licenças

- Código: MIT (`LICENSE`).
- Textos, figuras e dados derivados: CC BY 4.0 (`LICENSE-CC-BY-4.0.md`, que lista também o que mantém os termos de origem).
- A skill: a licença em `skill-revisao-sistematica/LICENSE.txt`.
