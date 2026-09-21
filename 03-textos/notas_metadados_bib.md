# Notas do coordenador: erros de metadados a corrigir no .bib

- Rodriguez2020: autor impresso é 'José M. Ramírez' (UCM), não 'Rodríguez, José María' (metadados OpenAlex); corrigir no .bib (ficha de elegibilidade, notas do codificador)
- ManuelReynoso2022: autor é 'Víctor Manuel Reynoso' (sobrenome Reynoso), não 'Manuel-Reynoso, Víctor'

## Candidatos a duplicata detectados na fase 5 (bola de neve SN1)
Identificados por md5 identico entre PDFs de chaves diferentes e por titulo/autores identicos. Entram na pendencia de dedup_candidatos, nao foram fundidos por mim:
- Granzier2019 (NBER WP 26599) e Granziersd (mesmo titulo e autores, sem ano e sem DOI).
- Grillo2024c, Grillo2024d e Grillo2024e: tres variantes de DOI do mesmo artigo na Revue economique (10.3917/reco.pr2.0188, 10.3917/reco.752.0353, 10.3917/e.reco.752.0353).
- Chernov2025b (SSRN/NBER WP 33339) e Chernov2026a (Journal of Econometrics): preprint e publicado do mesmo estudo, a ligar como relatos.
- Yang2023d (preprint OSF) e Yang2023e (IEEE TVCG): preprint e publicado do mesmo estudo, a ligar como relatos.
- Araujo2021 (preprint APSA) e Araujo2021a (British Journal of Political Science): preprint e publicado do mesmo estudo, a ligar como relatos.
- Halbach2019 e Halbach2019a: mesmo capitulo (Springer, 10.1007/978-3-030-22219-2_36), o segundo registro com o titulo truncado em "Follow Me:".
- Moy2012, Moy2014 e Moy2018: tres registros do mesmo capitulo de Moy e Rinke, com DOI do capitulo (10.1057/9780230374959_11), DOI alternativo da Palgrave (10.1057/9780230374959.0018) e DOI do deposito no SocArXiv (10.31235/osf.io/32z5j).

## Textos de acesso aberto que a rede bloqueou (declarar como limitacao)
Itens comprovadamente OA, mas cujos servidores respondem a clientes automatizados com desafio anti-bot (Cloudflare/Anubis), tanto para os agentes quanto para o coordenador: Aldrich2018 (livro OA no OAPEN/Fulcrum/JSTOR), Overbeck2024 (IJPOR, CC BY-NC-ND), TenenboimWeinblatt2022a (capitulo OA no OAPEN/T&F), Blais2017 (Erudit), Kuru2018 (tese no Deep Blue/UMich), Kselman2020 (UNLV OASIS e DukeSpace), Bytzek2011 e Schliebs2017 (SSOAR/MADOC), Freden2014 e Freden2020 (DiVA fora do ar), Torres2022 e Anon2022f (socialsciencereproduction.org sem resolucao de DNS). Nao e paywall: e indisponibilidade tecnica para download automatizado. Entram no PRISMA como nao recuperados.
- Dassonneville2014a: a planilha traz a segunda autora como "Katherine Grieb, A."; o documento assina "Annika Grieb". Corrigir no .bib.
- Stoetzer2024: a planilha traz o segundo autor como "Kayser, Mark Andreas Lindst Auml Dt", corrupção de codificação na fonte; o documento assina "Mark A. Kayser". Corrigir no .bib.
- Granziersd: a cascata voltou a baixar o NBER WP 26599 para esta chave numa terceira rodada, porque o registro segue como `nao_encontrado` no relatorio e `--apenas-pendentes` o repesca. O arquivo e byte a byte igual ao de Granzier2019, ja fichado e excluido por C2. Removido de novo da pasta de PDFs; a copia de referencia esta em pdfs_descartados/. Precisa de decisao: ou o par entra como duplicata na conferencia de dedup, ou Granziersd recebe a mesma decisao de texto completo de Granzier2019 por override humano.

## Segundo defeito encontrado na skill (declarar como limitação)
`rslib/triagem_lotes.trecho_confere` valida a citação do triador contra título e resumo normalizados, exigindo fronteira de palavra (`f" {alvo} "`). A normalização remove o travessão sem inserir separador: no resumo de RS4613, "accountability—some incumbents" vira "accountabilitysome incumbents". Uma citação literal que termine imediatamente antes de um travessão passa a não ter fronteira à direita e é recusada como inexistente.
Efeito observado: os dois revisores, de forma independente, citaram o mesmo trecho correto e tiveram o lote rejeitado (A/lote_106 e B/lote_107 da SN3). A correção seria trocar a remoção de pontuação por substituição por espaço, na mesma função usada para normalizar título e resumo.
Isto se soma ao defeito já registrado em `rslib/textos.classificar_resposta`, que trata qualquer resposta contendo a substring "incert" como inconclusiva.

## Meffert2012a: inclusão tardia que não é fruto da SN3

Meffert2012a entrou como estudo incluído somente na consolidação final de elegibilidade, depois de SN3 já ter fechado com zero inclusões novas. A causa não foi a bola de neve: o registro já estava no corpus desde uma busca anterior, pendente de recuperação de PDF, e a cascata de download (`--apenas-pendentes`) finalmente o recuperou numa rodada de reexecução tardia. Por isso esta inclusão **não reabre o critério de parada da bola de neve** (SN1 +7, SN2 +3, SN3 +0): a saturação foi avaliada e atingida sobre o conjunto de citantes/citados, e este caso é externo a esse fluxo. Registrar esta distinção explicitamente no relato, para que a leitura da saturação não seja confundida com uma quarta rodada de bola de neve.
