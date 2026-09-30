# Caixa de ferramentas

**RASCUNHO NÃO VALIDADO**: há rótulos pendentes ou pendências abertas no projeto.

Regras: `caixa-3` (references/07b-sintese-qualitativa-integracao.md; Apêndice D da base de conhecimento). Entradas: 06-analise/certeza.csv.
Testes combinados não definem rótulos. Linhas `efeito_painel` resumem os corpos por desenho de cada família × outcome.
Agregação `subcelulas-1`: 5 células de efeito reúnem mais de uma linha de certeza (subcélulas); o rótulo vem da regra de subcélulas e a justificativa descreve cada uma.

| Família × outcome | Dimensão | Rótulo | Status | Força/certeza | Escala | Estudos | Fontes |
|---|---|---|---|---|---|---|---|
| agregador_projecao × mobilizacao [randomizado] | efeito | Inconclusivo | rascunho | fraca / baixa | não estimada | Westwood2020a | certeza.csv:linha 2 |
| boca_de_urna × apoio_ao_lider [nao_randomizado] | efeito | Inconclusivo | rascunho | insuficiente / muito_baixa | não estimada | Chatterjee2019a, Morton2015a | certeza.csv:linha 3 |
| boca_de_urna × mobilizacao [nao_randomizado] | efeito | Inconclusivo | rascunho | insuficiente / muito_baixa | não estimada | Chatterjee2019a, Grillo2024c, Morton2015a | certeza.csv:linha 4 ; certeza.csv:linha 5 |
| outro × apoio_ao_lider [nao_randomizado] | efeito | Inconclusivo | rascunho | insuficiente / muito_baixa | não estimada | Araujo2021a | certeza.csv:linha 6 |
| pesquisa_pre_eleitoral × apoio_ao_lider [nao_randomizado] | efeito | Inconclusivo | rascunho | insuficiente / muito_baixa | não estimada | Feltovich2022, Stolwijk2016a | certeza.csv:linha 9 ; certeza.csv:linha 10 |
| pesquisa_pre_eleitoral × apoio_ao_lider [randomizado] | efeito | Inconclusivo | rascunho | insuficiente / muito_baixa | não estimada | Agranov2017a, Boukouras2020a, Cornejo2023a, Dahlgaard2016a, Farjam2020a, Fichnova2015a, Freden2024a, Lammers2022a, Meer2015a, Schlegel2023, Tal2015a, Timotei2013a, Tyszler2015, Witsman2016a | certeza.csv:linha 7 ; certeza.csv:linha 8 ; certeza.csv:linha 11 ; certeza.csv:linha 12 ; certeza.csv:linha 13 ; certeza.csv:linha 14 ; certeza.csv:linha 15 |
| pesquisa_pre_eleitoral × mobilizacao [nao_randomizado] | efeito | Inconclusivo | rascunho | fraca / baixa | não estimada | Brugarolas2021, Klor2017a, Stolwijk2019b | certeza.csv:linha 17 ; certeza.csv:linha 19 |
| pesquisa_pre_eleitoral × mobilizacao [randomizado] | efeito | Inconclusivo | rascunho | moderada / moderada | não estimada | Agranov2017a, Erlich2023, Gerber2020a, Groer2010a | certeza.csv:linha 16 ; certeza.csv:linha 18 |
| agregador_projecao × mobilizacao [painel] | efeito_painel | Inconclusivo | rascunho | fraca / baixa | não estimada | Westwood2020a | caixa: agregador_projecao × mobilizacao [randomizado] |
| boca_de_urna × apoio_ao_lider [painel] | efeito_painel | Inconclusivo | rascunho | insuficiente / muito_baixa | não estimada | Chatterjee2019a, Morton2015a | caixa: boca_de_urna × apoio_ao_lider [nao_randomizado] |
| boca_de_urna × mobilizacao [painel] | efeito_painel | Inconclusivo | rascunho | insuficiente / muito_baixa | não estimada | Chatterjee2019a, Grillo2024c, Morton2015a | caixa: boca_de_urna × mobilizacao [nao_randomizado] |
| outro × apoio_ao_lider [painel] | efeito_painel | Inconclusivo | rascunho | insuficiente / muito_baixa | não estimada | Araujo2021a | caixa: outro × apoio_ao_lider [nao_randomizado] |
| pesquisa_pre_eleitoral × apoio_ao_lider [painel] | efeito_painel | Inconclusivo | rascunho | insuficiente / muito_baixa | não estimada | Agranov2017a, Boukouras2020a, Cornejo2023a, Dahlgaard2016a, Farjam2020a, Feltovich2022, Fichnova2015a, Freden2024a, Lammers2022a, Meer2015a, Schlegel2023, Stolwijk2016a, Tal2015a, Timotei2013a, Tyszler2015, Witsman2016a | caixa: pesquisa_pre_eleitoral × apoio_ao_lider [nao_randomizado] ; caixa: pesquisa_pre_eleitoral × apoio_ao_lider [randomizado] |
| pesquisa_pre_eleitoral × mobilizacao [painel] | efeito_painel | Inconclusivo | rascunho | moderada / moderada | não estimada | Agranov2017a, Brugarolas2021, Erlich2023, Gerber2020a, Groer2010a, Klor2017a, Stolwijk2019b | caixa: pesquisa_pre_eleitoral × mobilizacao [nao_randomizado] ; caixa: pesquisa_pre_eleitoral × mobilizacao [randomizado] |
| agregador_projecao × * | implementacao | Não avaliada | pendente |  |  |  | caixa_ferramentas_mapa.csv (critérios de implementação) |
| agregador_projecao × * | custo | Pendente | pendente |  |  |  | sem fichamentos_master.csv |
| boca_de_urna × * | implementacao | Não avaliada | pendente |  |  |  | caixa_ferramentas_mapa.csv (critérios de implementação) |
| boca_de_urna × * | custo | Pendente | pendente |  |  |  | sem fichamentos_master.csv |
| outro × * | implementacao | Não avaliada | pendente |  |  |  | caixa_ferramentas_mapa.csv (critérios de implementação) |
| outro × * | custo | Pendente | pendente |  |  |  | sem fichamentos_master.csv |
| pesquisa_pre_eleitoral × * | implementacao | Não avaliada | pendente |  |  |  | caixa_ferramentas_mapa.csv (critérios de implementação) |
| pesquisa_pre_eleitoral × * | custo | Pendente | pendente |  |  |  | sem fichamentos_master.csv |
