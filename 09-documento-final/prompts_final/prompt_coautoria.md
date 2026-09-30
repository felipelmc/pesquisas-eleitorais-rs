# Coautoria: "o autor" passa a "os autores"

Você é o redator das mudanças de autoria da síntese. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. Leia antes o `CLAUDE.md` e a declaração `08-revisao-humana/declaracao_autores_2026-09-30_coautoria.md`.

## O fato

Lucas Berti (IESP-UERJ) é coautor, com contribuição igual à de Felipe Lamarca (MAPE/IESP-UERJ). As conferências humanas em bloco registradas foram dos dois autores, **sem dupla conferência independente**. As decisões tomadas em chat (emendas, regras, aprovações) também foram dos dois. Nada mais muda: o risco de viés e a certeza seguem julgados só por IA, as pendências abertas são as mesmas e nenhuma análise mudou.

## O que fazer

Nos arquivos abaixo, troque cada menção ao autor da síntese no singular ("o autor", "do autor", "pelo autor", "ao autor", "ele", "por ele", "dele", "suas") pela forma plural ("os autores", "dos autores", "pelos autores", "aos autores", "eles", "por eles", "deles"), com a concordância verbal e nominal ("o autor declarou" → "os autores declararam"; "decidido por ele" → "decidido por eles"; "16 casos limítrofes decididos pelo autor" → "16 casos limítrofes decididos pelos autores"). Casos especiais:

- **Livro de método.** "O livro do autor", "livro de método do autor" e semelhantes passam a "o livro de método", com a citação que já estiver lá (`@Lamarca2026Livro`). Não diga de quem é o livro.
- **Uso de IA.** "O uso de IA foi escolha do autor, para a variante rápida, com um só revisor humano" passa a "O uso de IA foi escolha dos autores, para a variante rápida, com a conferência humana feita pelos dois, em bloco, sem dupla independente". Onde o texto disser "um só revisor humano" ou "um revisor humano" sobre o que foi feito, diga que os dois autores conferiram juntos, sem dupla independente. Onde descrever o que o **protocolo** previa, deixe como está.
- **CRediT** (Informações adicionais, `**Contribuições (CRediT).**`): comece com "Felipe Lamarca e Lucas Berti contribuíram igualmente." e liste os mesmos papéis para os dois ("Os dois: conceituação, curadoria de dados, …"). A frase sobre os agentes de IA fora da autoria fica.
- **Declarações** (conflito de interesses e relação com a Anthropic): valem para os dois autores ("Os autores não têm conflito de interesses…").
- **Transcrições e datas.** Onde o texto diz que "em 30/09/2026, o autor declarou ao coordenador de IA…", passe a "os autores declararam". A transcrição foi feita a partir do que um deles disse em chat, mas a declaração é dos dois.
- **Primeira pessoa do plural** ("usamos", "declaramos"): já está certa e fica.
- **Não mude:** números, células, certezas, os spans `[...]{.enunciado cel="Cxx"}`, rótulos `{#...}`, marcadores `@@...@@`, chaves `@...`, a expressão "RASCUNHO NÃO VALIDADO", o marcador "[A confirmar pelo autor]" das travas e os comentários de código que não viram texto publicado.
- **Palavras:** o corpo do artigo, de Introdução a Conclusões, tem teto de 8.500 palavras e hoje está em 8.496. Não acrescente palavras no corpo; se uma troca somar palavras ali, compense na mesma frase.

## Arquivos

Texto publicado (edite só o texto que vira produto):
- `09-documento-final/_esqueleto_revisao_final.qmd` (não mexa no YAML do topo);
- `09-documento-final/_esqueleto_suplemento.qmd`;
- `09-documento-final/linguagem_simples.qmd`;
- `09-documento-final/revista/tabelas/*.yml` (`lacunas.yml` e os demais que tiverem "autor");
- `09-documento-final/revista/figuras/legendas.yml`;
- `09-documento-final/vitrine/conteudo/textos.yml` (sem travessão longo; a chave `heroi.autoria` fica para o coordenador);
- `09-documento-final/insumos/tabelas/checklist_*.md`.

Geradores, só as cadeias que viram texto publicado:
- `09-documento-final/montar_suplemento.py`;
- `09-documento-final/montar_revisao_final.py` (l. ~700);
- `09-documento-final/revista/figuras/verificar_figuras.py` (l. ~232): a frase que ele procura na legenda do PRISMA tem de acompanhar a legenda.

## Depois

1. Da raiz, antes de editar, copie o esqueleto: `cp 09-documento-final/_esqueleto_revisao_final.qmd <scratchpad>/esqueleto_antes_coautoria.qmd`.
2. Rode `python3 09-documento-final/conferir_numeros.py <scratchpad>/esqueleto_antes_coautoria.qmd 09-documento-final/_esqueleto_revisao_final.qmd`. A saída tem de ser vazia.
3. Rode `python3 09-documento-final/montar_revisao_final.py`, `python3 09-documento-final/montar_suplemento.py` e `python3 09-documento-final/conferir_reestruturacao.py --extra 09-documento-final/linguagem_simples.qmd`. O resultado tem de ser OK, sem falhas nem avisos e com o corpo em até 8.500 palavras.
4. Rode `python3 09-documento-final/revista/figuras/verificar_figuras.py`. Tem de sair OK.
5. Liste as menções que sobraram (`grep -n -i "o autor\|do autor\|pelo autor\|ao autor"` nos arquivos acima) e justifique cada uma.

Não rode `rs.py`, `publicar.sh` nem `refazer_produtos.sh`, e não faça commit. Responda com um resumo curto: arquivos mudados, número de trocas por arquivo, resultado das travas e as menções que sobraram.
