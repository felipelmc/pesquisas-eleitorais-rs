# Passe de estilo do documento final

Você revisa o ESTILO do documento final. O texto fica em `09-documento-final/_esqueleto_revisao_final.qmd` (o `revisao_final.qmd` é montado a partir dele por `09-documento-final/montar_revisao_final.py`, que insere as tabelas geradas; EDITE SÓ O ESQUELETO) para que soe escrito pelo autor, Felipe Lamarca, cientista político do IESP-UERJ, e não por IA. O conteúdo não muda. Raiz: `/Users/felipelmc/Desktop/pesquisas-eleitorais-rs`. O coordenador diz qual PASSE você faz.

## PASSE = voz

1. Leia, inteiras, as regras de voz do autor em `/Users/felipelmc/.claude/commands/my-voice.md`: conectivos próprios, vocabulário, pontuação, padrões de seção, palavras e construções proibidas e o teste final de autenticidade.
2. Leia `09-documento-final/insumos/amostras_voz.md`. São textos públicos do autor, para ouvir o ritmo, não para copiar conteúdo. Onde as amostras usam palavras que o `my-voice.md` proíbe (por exemplo "robusta", "significativa", "além disso"), vale o `my-voice.md`.
3. Reescreva a prosa do documento na voz do autor.

## PASSE = ia

1. Leia, inteiros, `/Users/felipelmc/.claude/skills/tirar-cara-de-ia/SKILL.md` e `references/portugues.md` (se existir, também `references/estrutura-retorica-e-deteccao.md`).
2. Aplique o procedimento da skill no modo leve: diagnóstico estrutural e lexical, cortar antes de trocar, devolver ritmo e posição, sem inventar.

## Em qualquer passe, é PROIBIDO mexer em

- números, intervalos, p, g, contagens, datas e porcentagens;
- chaves de citação `[@...]` e `@...`;
- rótulos da caixa (Positivo, Negativo, Misto, Nulo, Inconclusivo, Pendente);
- frases padrão de certeza ("a evidência é muito incerta", "pode aumentar", "provavelmente", "certeza muito baixa/baixa/moderada/alta");
- IDs de pendência (P0xx) e os títulos "Pendente de revisão humana";
- o YAML, as tabelas (linhas que começam com `|`), os blocos de código e as referências a figuras e tabelas (`@fig-`, `@tbl-`);
- o sentido de qualquer afirmação, inclusive as ressalvas (não as enfraqueça nem as reforce).

Não acrescente fatos. Se achar lacuna de conteúdo, anote-a em `09-documento-final/lacunas_estilo.md` em vez de preencher.

## Como trabalhar

1. Copie o esqueleto para `09-documento-final/_esqueleto.antes_<PASSE>.qmd`.
2. Edite `_esqueleto_revisao_final.qmd`.
3. Rode `python3 09-documento-final/conferir_numeros.py 09-documento-final/_esqueleto.antes_<PASSE>.qmd 09-documento-final/_esqueleto_revisao_final.qmd`. A saída tem de ser vazia (código 0). Se não for, desfaça as mudanças que alteraram números, chaves, pendências ou certezas e rode de novo, até dar vazio.
4. Rode `grep -n "—" 09-documento-final/_esqueleto_revisao_final.qmd`: não pode haver travessão.
5. Rode, da raiz, `python3 09-documento-final/montar_revisao_final.py` para remontar o `revisao_final.qmd`.
6. Apague a cópia `_esqueleto.antes_<PASSE>.qmd` só depois que a trava der vazio.

Não rode `quarto`, `rs.py`, rede nem nada em segundo plano. Responda com UMA linha: `OK passe=<PASSE>: trava vazia; <resumo das mudanças por categoria em até 30 palavras>`.
