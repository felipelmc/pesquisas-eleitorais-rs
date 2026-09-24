# Verificação independente do documento final

Você é o verificador independente de `09-documento-final/revisao_final.qmd`. Não escreveu o documento. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Não altere o documento; grave só `09-documento-final/verificacao.md`. Não abra PDFs, não use rede, não rode `rs.py` nem `quarto`, e não rode nada em segundo plano.

## O que conferir

1. **Números.** Confira cada número do texto corrido, das mensagens principais, do resumo, do *abstract* e das tabelas contra os arquivos de origem:
   - `07-relatorio/prisma_contagens.json`;
   - `07-relatorio/incluidos.csv`;
   - `06-analise/swim_*/swim_resumo.json`;
   - `06-analise/meta_exploratoria/meta_resumo.json`, `06-analise/meta_mesmo_candidato/meta_resumo.json` e as versões `_icc020`;
   - `06-analise/certeza.csv` e `certeza_agrupamento_amplo.csv`;
   - `06-analise/_delta_celula.txt`;
   - `05-decomposicao/efeitos_para_sintese.csv`;
   - `04-qualidade/rob_geral.csv`;
   - `09-documento-final/insumos/tabelas/numeros.json`;
   - `07-relatorio/_pendencias_abertas.json`;
   - `00-protocolo/emendas.md`;
   - `02-triagem/sem_resumo_revisao/`.

   Use scripts Python. Liste cada divergência: trecho, número no texto, número no arquivo e arquivo.
2. **Certeza.** Toda afirmação de efeito tem a certeza da célula certa (`certeza.csv`) e a frase padrão correspondente:
   - muito baixa: "a evidência é muito incerta";
   - baixa: "pode";
   - moderada: "provavelmente".

   Nenhuma afirmação de direção se apoia na significância, e não há "Neutro" nem "sem efeito".
3. **Coerência interna.** Os mesmos números aparecem nas mensagens, no resumo, no *abstract*, no corpo e nas tabelas. O documento não contradiz o manuscrito técnico (`07-relatorio/relatorio.qmd`).
4. **Marcações humanas.**
   - Toda seção que depende de validação humana tem o callout "Pendente de revisão humana" com as pendências certas: Efeito, Mecanismo, Moderadores, Caixa, Metodologia (busca, seleção, extração, RoB, GRADE) e o documento inteiro.
   - O apêndice lista as 18 pendências de `_pendencias_abertas.json`, com os IDs certos.
5. **Citações.**
   - Toda `@chave` existe em `07-relatorio/references.bib` ou em `09-documento-final/referencias_contexto.bib`.
   - As afirmações de contexto (lei, TSE, STF, PLs) batem com `09-documento-final/insumos/contexto_brasil.md`.
   - Nada do dossiê marcado "não confirmado" aparece no documento como fato.
6. **Recomendações.** Nada no texto recomenda proibir ou liberar a divulgação de pesquisas com força maior do que a certeza permite.

## Saída

Grave `09-documento-final/verificacao.md` com três partes:
- um resumo do que foi checado e quanto;
- a lista de divergências, cada uma classificada como `erro` (precisa corrigir), `aviso` (conferir) ou `ok com ressalva`, com a correção sugerida em texto exato;
- os scripts usados, num bloco de código.

Responda com UMA linha: `OK verificacao.md: <n> erros, <n> avisos`.
