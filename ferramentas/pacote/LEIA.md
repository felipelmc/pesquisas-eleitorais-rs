# Pacote de replicação

**Pesquisas eleitorais publicadas mudam o voto?** Síntese sistemática de evidências, conduzida com agentes de IA, sobre os efeitos *bandwagon* e *underdog* e o comparecimento. Felipe Lamarca (MAPE/IESP-UERJ), versão de 01/10/2026.

- Artigo com apêndices: `artigo/revisao.pdf`.
- Página do projeto: <https://felipelamarca.com/pesquisas-eleitorais-rs/>.

## O que foi e o que não foi validado por humano

Triagem, elegibilidade, extração, risco de viés e certeza foram feitos por agentes de IA. O autor conferiu, em bloco, as etapas abaixo e confirmou as decisões em vigor (`08-revisao-humana/declaracao_autor_2026-09-30.md`; Emenda 7 em `00-protocolo/emendas.md`):
- a busca;
- a triagem;
- a elegibilidade;
- os efeitos, contra a página dos PDFs;
- as divergências da recodificação;
- o relato.

**Não** tiveram validação humana:
- o risco de viés;
- os juízos de certeza (GRADE);
- a validação cega da triagem;
- a aplicação da deduplicação dos 145 pares candidatos (decidida, não aplicada).

A lista está em `07-relatorio/_pendencias_abertas.json`.

## Conteúdo

| Pasta | O que tem |
|---|---|
| `00-protocolo/` | protocolo congelado, emendas (E001, E002 e 1 a 7), pergunta, teoria do programa, *codebooks* |
| `01-busca/` | as quatro estratégias ativas (OpenAlex em inglês, português e espanhol; BDTD), log de buscas, conferência do PRESS |
| `dados/` | registros deduplicados, só com metadados bibliográficos (sem resumo, sem instituição, sem e-mail) |
| `02-triagem/`, `03-textos/` | decisão final de títulos e resumos e de texto completo, com o critério que falhou |
| `04-qualidade/` | risco de viés por domínio (RoB 2, ROBINS-I V2, EPOC) e geral |
| `05-decomposicao/` | fichamentos (sem o caminho local do PDF) e efeitos por estudo, com trecho e página |
| `06-analise/` | efeitos calculados, entradas e saídas da SWiM (principal e sensibilidades), metas exploratórias, certeza |
| `07-relatorio/` | incluídos, contagens e diagrama PRISMA, listas PRISMA e SWiM, declaração de uso de IA gerada do log |
| `skill-revisao-sistematica/` | cópia dos scripts da skill que rodou a revisão (`rs.py`, `rslib/`, `R/`), com a licença do autor |
| `tabelas-extras/` | estudos da região e efeitos de viabilidade, e as listas de conferência (PRISMA 2020, resumo, PRISMA-S, SWiM, PRISMA-trAIce), com o local de cada item no artigo final e nos apêndices |
| `MANIFESTO.csv` | caminho, origem, tamanho e SHA256 de cada arquivo |

## O que se reproduz com este pacote

- **Com o pacote e a skill incluída** (Python 3, R com `metafor` e `clubSandwich`, versões em `ambiente.txt`), um terceiro consegue refazer, a partir dos efeitos extraídos, a síntese inteira:
  - o cálculo dos efeitos;
  - as células;
  - a SWiM principal e as sensibilidades;
  - as metas exploratórias.

  Use os comandos de `rs.py analise …` e os scripts `06-analise/montar_*.py`, na ordem descrita no artigo (seção de métodos) e em `REPRODUZIR.md` do repositório.
- **Depende dos PDFs**, que não podem ser redistribuídos: conferir os trechos e as páginas citados nas fichas e nos efeitos. As referências completas dos estudos estão no artigo.
- **Fica fora do pacote**, por conter resumos de terceiros: a triagem registro a registro (lotes, pareceres dos triadores de IA), e também as fichas em Markdown, os *prompts* e o log bruto. Tudo isso está no repositório privado, que pode ser acessado mediante pedido ao autor.

## Licenças

- Código: MIT (`LICENSE`).
- Textos, figuras e dados derivados: CC BY 4.0 (`LICENSE-CC-BY-4.0.md`, que lista também o que mantém os termos de origem).
- A skill: a licença em `skill-revisao-sistematica/LICENSE.txt`.
