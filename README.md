# Pesquisas eleitorais publicadas mudam o voto?

Síntese sistemática de evidências, conduzida com agentes de IA, sobre os efeitos *bandwagon* e *underdog* e o comparecimento. Felipe Lamarca (MAPE/IESP-UERJ), versão de entrega de 01/10/2026.

- **Artigo com apêndices (PDF único):** [`docs/revisao.pdf`](docs/revisao.pdf), também em <https://felipelamarca.com/pesquisas-eleitorais-rs/revisao.pdf>.
- **Página do projeto:** <https://felipelamarca.com/pesquisas-eleitorais-rs/>. Traz a vitrine interativa, o artigo em HTML, os apêndices e o resumo em linguagem simples.
- **Pacote de replicação público:** <https://felipelamarca.com/pesquisas-eleitorais-rs/pacote-replicacao.zip>. Leva protocolo, dados, síntese e código, sem resumos nem e-mails de terceiros.

## Pergunta e resultado

**Pergunta.** Qual é o efeito da exposição a resultados de pesquisas eleitorais publicadas (pré-eleitorais, agregadores e projeções, boca de urna) sobre a intenção ou a escolha de voto? A direção é *bandwagon* (apoio a quem aparece à frente) ou *underdog* (apoio a quem aparece atrás)? E qual é o efeito sobre o comparecimento?

**Escopo.** Relatos publicados desde 2010, em escopo global. As buscas foram feitas no OpenAlex (em inglês, português e espanhol) e na BDTD, com bola de neve. O resultado são 41 estudos e 55 relatos, com 560 efeitos extraídos. A síntese é sem meta-análise (SWiM), e a certeza foi julgada com GRADE.

**Resultado.**
- **Apoio a quem aparece à frente, em experimentos:** a direção é *bandwagon*. Nas duas células com mais estudos, os 4 experimentos de cada uma apontam nessa direção, mas a certeza é muito baixa, e quase tudo é laboratório ou vinheta.
- **Comparecimento:** receber pesquisa de disputa apertada, em vez de folgada, provavelmente não muda o comparecimento além de ±2 pontos percentuais (um experimento de campo; certeza moderada).
- **Tamanho do efeito:** a evidência não diz de quanto é o efeito, nem permite afirmar que não há efeito.

## O que teve e o que não teve validação humana

Agentes de IA conduziram as etapas depois do protocolo. O protocolo e a pergunta foram aprovados pelo autor. Em 30/09/2026, o autor declarou ter conferido **em bloco** a busca, a triagem, a elegibilidade, os efeitos (contra a página dos PDFs) e o relato, e ter mantido as decisões em vigor. O registro está em [`08-revisao-humana/declaracao_autor_2026-09-30.md`](08-revisao-humana/declaracao_autor_2026-09-30.md) e na Emenda 7.

Ficaram **sem validação humana**:
- o risco de viés e a certeza da evidência, julgados só por IA;
- a validação cega da triagem;
- a aplicação da deduplicação dos 145 pares candidatos, que foi decidida e não aplicada.

Essas pendências estão abertas para uma próxima versão ([`08-revisao-humana/README.md`](08-revisao-humana/README.md)). Por isso o `rs status` ainda marca o projeto como rascunho, e a declaração de uso de IA do artigo abre com "RASCUNHO NÃO VALIDADO".

## O que há neste repositório

| Onde | O quê |
|---|---|
| `docs/` | **produto publicado**: `revisao.pdf` (artigo e apêndices), `revisao.html`, `apendices.html`, `linguagem-simples.html`, `pacote-replicacao.zip` e a vitrine (`index.html`) |
| `09-documento-final/` | **fonte do artigo**: `_esqueleto_revisao_final.qmd` (texto), `_esqueleto_suplemento.qmd` (apêndices), `linguagem_simples.qmd`, template e figuras em `revista/`, travas (`conferir_*.py`), especificação `spec_final.md` e vitrine |
| `00-protocolo/` a `08-revisao-humana/`, `dados/`, `rs_estado.json`, `rs_log.jsonl` | **trilha de auditoria** da skill `revisao-sistematica`: protocolo e emendas, buscas, triagem, textos completos, risco de viés, extração, análise, relato e revisão humana. A skill depende destes caminhos; não mova as pastas |
| `ferramentas/` | publicação (`publicar.sh`, `refazer_produtos.sh`), junção do PDF, pacote de replicação e conferências auxiliares |

O material superado fica onde está, porque emendas e notas o citam. Ele não é entrada de nada:
- versões anteriores do artigo: `09-documento-final/_esqueleto_v1_oqf.qmd`, `_revisao_final_v1_oqf.qmd`, `_esqueleto_v2_2409.qmd`, `_esqueleto_suplemento_v2_2409.qmd`, `spec_v2.md` e `prompts_v2/`;
- o relatório técnico de 24/09: `07-relatorio/relatorio.qmd`;
- a síntese anterior à Emenda 5: `06-analise/_superado_pre_revisao_g8/`;
- os backups de efeitos: `05-decomposicao/efeitos_backup_*`.

As versões ficam nas tags `v1-oqf-2026-09-24` (formato *O que funciona?*) e `v2-rascunho-2026-09-24` (artigo de 24/09). A estrutura detalhada, os PDFs locais, a cadeia que refaz efeitos, síntese e produtos e o histórico das sessões estão em [`REPRODUZIR.md`](REPRODUZIR.md).

## Como citar

Lamarca, Felipe. 2026. *Pesquisas eleitorais publicadas mudam o voto? Síntese sistemática de evidências, conduzida com agentes de IA, sobre os efeitos* bandwagon *e* underdog *e o comparecimento*. Documento de trabalho, versão de 01/10/2026. <https://felipelamarca.com/pesquisas-eleitorais-rs/>. Ver também [`CITATION.cff`](CITATION.cff).

## Licenças

O código é MIT ([`LICENSE`](LICENSE)). Textos, figuras e dados derivados são CC BY 4.0 ([`LICENSE-CC-BY-4.0.md`](LICENSE-CC-BY-4.0.md)); o mesmo arquivo lista o que mantém os termos de origem (metadados bibliográficos, trechos citados, estilo de citação, fontes, D3).

Este repositório é privado, e o acesso é sob pedido ao autor. Ele guarda os PDFs de terceiros só no disco local, fora do Git. Nenhum PDF foi obtido por Sci-Hub, LibGen ou outra fonte não autorizada.
