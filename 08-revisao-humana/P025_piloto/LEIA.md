# P025: conferência humana do piloto de extração (G6)

> **Fechada em 30/09/2026 (Emenda 7).** O autor declarou ter conferido esta etapa em bloco e manteve o estado atual (`08-revisao-humana/declaracao_autor_2026-09-30.md`). O texto abaixo descreve o pacote como foi preparado em 23/09/2026.


O piloto teve 3 textos: Meer2015a (survey experiment), Klor2017a (laboratório e eleições reais) e Araujo2021a (experimento natural, Emenda 1). Até 30/09/2026, só o coordenador de IA tinha revisado o piloto (`05-decomposicao/piloto/revisao_coordenador.md`). A Emenda 2 saiu dessa revisão e foi decidida pela IA (Emenda 6a).

## O que já foi feito por IA depois do piloto (não substitui a conferência)

- Os três textos foram fichados de novo na rodada completa, com a redação da Emenda 2.
- Em 23/09/2026, os três passaram pela **re-extração cega** dos efeitos principais (`08-revisao-humana/efeitos/cega/`).
- Meer2015a e Klor2017a divergiram da extração original e foram **arbitrados** (`08-revisao-humana/efeitos/arbitragem/`). As correções estão em `05-decomposicao/correcoes_sessao_2026-09-23.csv`.
- Araujo2021a concordou com a original nos números.

## Checklist para o revisor humano (cerca de 1 hora)

Para cada texto, com o PDF aberto (`03-textos/pdfs/<chave>.pdf`):

- [ ] **Ficha** (`05-decomposicao/fichas/` ou `05-decomposicao/piloto/fichas/`): as variáveis de desenho, população, exposição, comparador e desfecho batem com o texto.
- [ ] **Estimando e modelo principal:** batem com a regra da Emenda 2. Conferir `b2_estimando` e `b2_modelo_principal`.
- [ ] **Efeitos principais** (`05-decomposicao/efeitos/<chave>.csv`, `modelo_principal = sim`): número, sinal, EP ou DP, n e página.
- [ ] **Decisões dos árbitros de IA**, no caso de Meer2015a e Klor2017a:
  - Meer2015a: alvo `momentum`, estimando ITT e o n2 lido da Figura 1;
  - Klor2017a: comparador `mesmo_candidato_atras` e estimando `associacao` nos contrastes antes e depois.
- [ ] **Emenda 2:** você concorda com a redefinição das três variáveis do codebook? Ela foi decidida pela IA.

## Como registrar

Se estiver tudo certo, ou depois de corrigir o que for preciso:

```bash
rs() { python3 ~/.claude/skills/revisao-sistematica/scripts/rs.py "$@"; }
rs --dir . pendencia fechar P025 --motivo "piloto conferido contra os PDFs: <resumo>" --por revisor_humano_1
rs --dir . pendencia fechar P026 --motivo "G6 confirmado após P025" --por revisor_humano_1
```

Se corrigir algum efeito, refaça a cadeia do `REPRODUZIR.md` a partir de `preparar-efeitos`.
