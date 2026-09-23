# Redação do manuscrito PRISMA 2020 — projeto "pesquisas eleitorais publicadas e voto"

Você redige o manuscrito da revisão preenchendo `07-relatorio/relatorio.qmd` (cópia do template `manuscrito_prisma.qmd` da skill). Raiz do projeto: `/Users/felipelmc/revisoes/pesquisas-eleitorais/`. Público: pesquisadores de comportamento eleitoral e opinião pública. Idioma: português do Brasil.

## Regras que não se negociam

1. **Todo número vem de arquivo do projeto** (contagens, k, proporções, IC, p, g, κ, datas). Nunca digite número de memória nem arredonde de forma diferente em lugares diferentes. Se um número não existe em arquivo, escreva "NR" (não relatado) e diga por quê.
2. **Nenhum placeholder `{{...}}` pode sobrar.** Ao terminar, rode `grep -nE '\{\{[A-Z0-9_]+\}\}' 07-relatorio/relatorio.qmd` e confirme vazio.
3. **Direção pelo estimador, nunca pela significância.** Não escreva "sem efeito" por p > 0,05. Com SWiM, a certeza qualifica a DIREÇÃO, não a magnitude; diga isso.
4. **Toda afirmação de efeito traz a certeza GRADE** da célula (de `06-analise/certeza.csv`), no estilo GRADE ("pode aumentar", "é incerto").
5. **Produto em rascunho:** logo abaixo do título, uma linha em destaque: `RASCUNHO NÃO VALIDADO — <n> pendências humanas abertas (lista no apêndice)`, com n do arquivo de pendências. (Esse travessão no aviso é a única exceção; no resto do texto, não use travessão nem meia-risca como pontuação.)
6. **Referências:** cite estudos incluídos pela chave do `07-relatorio/references.bib` (`[@Chave]`). Fora deles, só cite obras que o protocolo já cita (seção de revisões existentes: Hardmeier 2008, Moy & Rinke 2012, Barnfield 2019 e as normas metodológicas); se precisar delas, acrescente entradas mínimas ao final de `references.bib` com os dados que o protocolo dá, sem inventar DOI, páginas ou volume.
7. **Não altere** nenhum arquivo fora de `07-relatorio/` e não rode `rs.py`. Não use rede.

## Fontes (leia antes de escrever)

- Protocolo e emendas: `00-protocolo/protocolo.md`, `00-protocolo/emendas.md` (Emendas 1 a 5; a 5 descreve a síntese final), `00-protocolo/pergunta.md`, `00-protocolo/teoria_programa.md`.
- Busca: `01-busca/log_buscas.csv`, `01-busca/strings/`, `01-busca/recall_ancoras.json`, `01-busca/prepress_*.md`.
- Fluxo: `07-relatorio/prisma_contagens.json` (todas as contagens do PRISMA), `07-relatorio/prisma.svg`, `07-relatorio/checklist_prisma.csv`.
- Triagem e elegibilidade: `02-triagem/` (resumos e validação), `03-textos/` (inventário, elegibilidade, relatório de PDFs; não abra PDFs).
- Extração: `05-decomposicao/fichamentos_master.csv` (características dos estudos), `05-decomposicao/notas_extracao_completa.md`, `05-decomposicao/validacao_extracao/concordancia/RELATORIO_CONCORDANCIA.md`.
- Risco de viés: `04-qualidade/rob_geral.csv`, `04-qualidade/rob_*_consenso.csv`, `04-qualidade/rob_*_concordancia.csv`, `04-qualidade/notas_rob.md`, `04-qualidade/arbitragem/propostas_para_confirmacao.csv`.
- Síntese: `06-analise/swim_principal/` (principal), `06-analise/swim_sens_*/` (sensibilidades), `06-analise/meta_exploratoria/` (meta exploratória, k = 3), `06-analise/swim_entrada_principal.csv`, `06-analise/montar_entradas_swim.py` (efeitos fora da contagem e motivos), `06-analise/certeza.csv` (GRADE), `06-analise/revisao_metodologica_g8.md` (revisão metodológica e o que foi corrigido).
- IA e pendências: `07-relatorio/declaracao_uso_ia.md` (gerada do log; não edite), `07-relatorio/_pendencias_abertas.json`, modelo narrativo em `/Users/felipelmc/.claude/skills/revisao-sistematica/assets/templates/declaracao_uso_ia.md`.
- Guia de placeholders: `/Users/felipelmc/.claude/skills/revisao-sistematica/references/08-relato.md`, seções 4 e 7.

## O que o texto precisa conter (além dos placeholders do template)

- **Métodos:** o tipo (efetividade com SWiM, variante rápida) e os atalhos declarados no G1; autopiloto com subagentes e o papel de cada modelo; RoB 2, ROBINS-I V2 (declarando ROBINS-E como canônico para exposição) e EPOC; convenção de sinal por alvo (Emenda 5); células do protocolo; nulos por ±δ; δ = 2 p.p. convertido.
- **Resultados:** tabela de características dos 41 estudos (desenho fino, família, país/região, tipo de eleição, realismo, construto, RoB), tabela da SWiM principal por célula (estudos, direções, proporção, IC, p do teste de sinal, certeza), tabela das sensibilidades, a meta exploratória como exploratória, a lista dos efeitos fora da contagem com motivo, e a tabela de viabilidade e de *momentum* como achados secundários.
- **Seção Brasil e América Latina** (subseção própria dos resultados): estudos com `regiao` brasil ou america_latina (master), o que cada um estuda e mostra, com a ressalva de que o único estudo brasileiro (Araujo2021a) trata de apuração parcial oficial, não de pesquisa (Emenda 1); fatores de transferibilidade do protocolo (voto obrigatório, dois turnos, regulação da divulgação de pesquisas, confiança nas pesquisas), sem generalizar além da evidência.
- **Discussão, limitações da evidência** (subseção própria): dependência de laboratório e vinheta hipotética (sensibilidade só com contexto real), poucos estudos por célula, imprecisão, estudos com dados lidos de figura, ausência de meta-análise principal.
- **Discussão, limitações do processo** (subseção própria, completa): fontes restritas (OpenAlex, BDTD, bola de neve; sem WoS/Scopus/SciELO); triagem, elegibilidade, extração, RoB e certeza feitas por subagentes de IA sem validação humana (lista de pendências abertas); âncoras e PRESS só por IA; todos os modelos do mesmo provedor; árbitro do RoB do mesmo modelo do avaliador A (seguiu A em 79 de 88 domínios); consenso de RoB confirmado em bloco; concordância da extração abaixo do limiar (58,5%, variáveis sinalizadas); PDFs não recuperados; ROBINS-I no lugar de ROBINS-E; decisões da Emenda 5 tomadas depois de ver os dados; Sci-Hub e fontes não autorizadas não foram usados.
- **Outras informações:** registro (o protocolo não foi registrado no OSF, salvo se o protocolo disser outra coisa), emendas, financiamento e conflitos (escreva "a preencher pelos autores" onde o projeto não informa), disponibilidade de dados e código (pasta do projeto; repositório privado), declaração de IA (inclua `declaracao_uso_ia.md` por include, como o template já faz, e escreva o texto narrativo em `07-relatorio/declaracao_uso_ia_texto.md` a partir do modelo da skill).
- **Autoria:** `{{TEXTO_AUTORES}}` = "a preencher pelos autores" (não invente nomes).

## Checklists

- Preencha a coluna `local_no_relato` de `07-relatorio/checklist_prisma.csv` (seção e subseção do relatório onde cada item está; "não se aplica" com motivo).
- Crie `07-relatorio/checklist_swim.csv` a partir de `/Users/felipelmc/.claude/skills/revisao-sistematica/assets/checklists/` (arquivo do SWiM, se existir; se não existir, liste os 9 itens do SWiM de Campbell et al. 2020 com o local no relato).

## Ao terminar

Confira: placeholders vazios; números batendo entre resumo, texto e tabelas; nenhuma afirmação de efeito sem certeza. Responda com UMA linha: `OK relatorio.qmd: <n> palavras; placeholders=0; checklists=<arquivos>` ou `FALHA <motivo>`.
