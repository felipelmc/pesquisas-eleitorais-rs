# Verificação independente de `revisao_final.qmd`

Verificador: subagente de IA (Claude Opus 5.5), 24/09/2026, a partir de `09-documento-final/prompt_verificacao.md`. Não alterei o documento. Não abri PDFs, não usei rede e não rodei `rs.py` nem `quarto`. Esta verificação é de IA e não vale como validação humana.

## 1. O que foi checado e quanto

- **Números (item 1).** O script `s4_verificar.py` fez 75 checagens programáticas, cada uma confrontando um trecho literal do documento com o valor recalculado do arquivo de origem. Delas, 73 passaram e 2 falharam (divergências 1 e 12). Os números conferidos foram:
  - as contagens gerais (41/55, 560/40, 37, 27 estudos em 18 células, realismo 25/9/7, anos de publicação de 2010 a 2024);
  - os 11 números do PRISMA, as buscas B02 a B05 e as rodadas SN1 a SN3 (no `rs_log.jsonl`);
  - a Emenda 6b (172, 156 e 180);
  - o risco de viés (43/37; 17/6, 2/8/3 e 6/1; 21/23, 11/13, 259/88/79);
  - δ = 0,0573;
  - as duas metas exploratórias (g, IC, p, gl, τ², I², *leave-one-out*, ICC 0,20 e ρ);
  - as 19 linhas da @tbl-swim contra `swim_principal/swim_resumo.json` e `certeza.csv` (estudos, direções, proporção, IC, p e certeza);
  - as contagens de certeza (15/2/1; amplo 7 muito baixa);
  - as sensibilidades (amplo 9/9 com p = 0,004; com excluídos 10/11 com p = 0,012; sem pré-2010 8/8 com p = 0,008; sem Araujo 2/3; só contexto real; ICC 0,20 idêntico à principal);
  - 12 trechos de efeitos individuais (g, EP e p.p. em `06-analise/efeitos.csv`);
  - as contagens de moderadores (13 estudos na célula principal, 8 com regra do experimento; voto obrigatório);
  - as pendências.

  À mão, conferi ainda:
  - as sensibilidades "só contexto real" e "com críticos", linha a linha (`s1_swim.py`);
  - a @tbl-caixa-celulas e a @tbl-oqf contra `caixa_ferramentas.csv` e `insumos/caixa_oqf_painel.md`;
  - a @tbl-regional contra `efeitos.csv`, `rob_geral.csv` e o *master*;
  - as contagens de mecanismos e moderadores contra `insumos/mecanismos_moderadores.md` e a saída de `contagens_mecanismos_moderadores.py` (T9, T11, T12, T14 e T16);
  - as emendas contra `00-protocolo/emendas.md`;
  - triagem, extração, reextração (15/23/12/6; 772/240/40) e elegibilidade (17, 3, 165 = 47 + 118) contra `07-relatorio/relatorio.qmd`, `correcoes_sessao_2026-09-23.csv` (772 linhas, 240 extensões) e `08-revisao-humana/README.md`.
- **Certeza (item 2).** Conferi as afirmações de efeito das mensagens principais, do resumo executivo, do resumo, do *abstract*, das seções Efeito, Mecanismo, Moderadores, Caixa e Brasil e das limitações contra a certeza da célula em `certeza.csv`:
  - todas as certezas citadas batem com a célula;
  - não há "Neutro" nem "sem efeito";
  - nenhuma direção se apoia em significância.

  Há 4 trechos com direção enunciada sem a frase padrão (divergências 2 a 5).
- **Coerência interna (item 3).** Os números batem entre as mensagens, o resumo executivo, o resumo, o *abstract*, o corpo e as tabelas. Não achei contradição com `07-relatorio/relatorio.qmd`, que traz os mesmos números de busca, triagem, extração, RoB, SWiM, metas e sensibilidades. A única diferença de ênfase é a da divergência 1: o relatório técnico não dá o número de estudos.
- **Marcações humanas (item 4).** Há o callout "Pendente de revisão humana" em:
  - Efeito;
  - Mecanismo;
  - Moderadores;
  - Caixa;
  - Brasil;
  - Metodologia, com busca (P001, P004), seleção (P019, P020, P006, P007, P041, P008, P023), extração (P039, P037, P025, P026), RoB (P033) e GRADE (P036, P042, P035);
  - o documento inteiro (P038, depois do resumo executivo, e o aviso de rascunho no topo).

  O Apêndice A tem as 18 pendências, com os IDs iguais aos de `_pendencias_abertas.json`, e as 18 aparecem também fora do apêndice. A descrição da P042 está errada (divergência 12).
- **Citações (item 5).** As 51 chaves `@` existem em `references.bib` ou em `referencias_contexto.bib`, e as referências cruzadas `@sec-`, `@tbl-` e `@fig-` têm alvo. Conferi 10 afirmações de contexto (lei, resolução do TSE, STF, PLs, CPI, ESOMAR/WAPOR, Meireles, Pereira e Nunes, Barnfield, revisões anteriores) contra `insumos/contexto_brasil.md`. Nenhum item marcado como "não confirmado" aparece como fato: a CPI não é dada como instalada, e não se cita erro médio nem conclusões de Hardmeier. Há três imprecisões menores (divergências 7 a 9).
- **Recomendações (item 6).** Nenhum trecho recomenda proibir nem liberar a divulgação. O texto repete que a evidência "não sustenta nem a restrição nem a manutenção" e separa o fundamento do STF (direito à informação) da evidência de efeito. Nada a corrigir.

**Total: 1 erro, 11 avisos, 6 ok com ressalva.**

## 2. Divergências

### Erros

**1. `erro`: voto obrigatório (seção Moderadores, parágrafo "Voto obrigatório").**
- Trecho no texto: "Nenhum dos 12 estudos de comparecimento da síntese principal tem voto obrigatório codificado como sim. Desses, 2 estão codificados como não e 10 como não informado."
- No arquivo: as células de mobilização de `06-analise/swim_principal/swim_resumo.json` têm **11** estudos. Cruzados com `05-decomposicao/fichamentos_master.csv`, 2 estão como "Não" (Gerber2020a e Grillo2024c) e **9** como 999.
- Origem do erro: o 12 e o 10 vêm da tabela T16 de `contagens_mecanismos_moderadores.py`, que conta também Kaplan2019a. Esse estudo está em risco crítico e fica fora da síntese principal.
- Correção sugerida: "Nenhum dos 11 estudos de comparecimento da síntese principal tem voto obrigatório codificado como sim. Desses, 2 estão codificados como não e 9 como não informado."

### Avisos

**2. `aviso`: certeza baixa sem a frase padrão (resumo executivo, 4.º parágrafo).**
- Trecho no texto: "Estudos em eleições reais apontam para mais participação depois da divulgação de pesquisas, e um jogo *online* aponta para menos participação quando a projeção mostra a eleição decidida (certeza baixa nos dois casos)."
- Correção sugerida: "Em eleições reais, ter visto a divulgação de pesquisas pode aumentar a participação e, num jogo *online*, ver projeções que mostram a eleição decidida pode reduzi-la (certeza baixa nos dois casos)."

**3. `aviso`: direção sem a frase padrão (Mecanismo, "Pivotalidade e emoções").**
- Trecho no texto: "As exposições que fazem a eleição parecer decidida (...) aparecem na direção de desmobilização [...], com certeza baixa para as projeções e muito baixa para a boca de urna."
- Correção sugerida: "Ver projeções longe de 50:50 pode reduzir a decisão de votar (certeza baixa), e a evidência é muito incerta sobre se a boca de urna divulgada antes do fechamento reduz o comparecimento (certeza muito baixa) [@Westwood2020a; @Morton2015a; @Grillo2024c]."

  No mesmo parágrafo, o trecho "revelar a distribuição de preferências aumenta o comparecimento só em eleitorados quase divididos [@Klor2017a]" deve passar a "em @Klor2017a, revelar a distribuição de preferências aparece associado a mais comparecimento só em eleitorados quase divididos (achado dentro do estudo, descritivo; a célula tem certeza muito baixa)".

**4. `aviso`: certeza atribuída à célula errada (Mecanismo, "Voto estratégico e viabilidade").**
- Trecho no texto: "Neles, a informação sobre a distribuição de preferências aumenta a deserção para a opção viável [@Tyszler2015; @Tyszler2013; @Tal2015a]. (...) A certeza é muito baixa nas células de viabilidade."
- No arquivo: Tyszler2015 e Tal2015a estão nas células de alvo **principal** (sem pesquisa e mesmo candidato atrás; `certeza.csv`). Tyszler2013 não tem efeito principal e não entra em nenhuma célula (`numeros.json`, `sem_principal`). O fato é afirmado sem qualificação.
- Correção sugerida: "Neles, a informação sobre a distribuição de preferências aparece associada a mais deserção para a opção viável [@Tyszler2015; @Tyszler2013; @Tal2015a], um achado descritivo: os dois primeiros estão em células de apoio principal com certeza muito baixa, e @Tyszler2013 não entra em nenhuma célula."

**5. `aviso`: nulo de Gerber sem a frase padrão (Moderadores, "Proximidade da disputa").**
- Trecho no texto: "O desenho mais forte [@Gerber2020a] não acha efeito além de ±2 pontos percentuais (certeza moderada)."
- Correção sugerida: "No desenho mais forte [@Gerber2020a], receber pesquisa apertada, em vez de folgada, provavelmente não muda o comparecimento além de ±2 pontos percentuais (certeza moderada)."

**6. `aviso`: "único teste pré-especificado" (@tbl-oqf, linha Moderador).**
- Trecho no texto: "o partidarismo não atenuou o efeito no único teste pré-especificado (@Cornejo2023a)".
- No arquivo: o dossiê `insumos/mecanismos_moderadores.md` (3.6) marca como pré-especificada também a moderação por partido apoiado em Gandhi2019, cujos efeitos estão no `FORA`, e a de preferência prévia em Meer2015a.
- Correção sugerida: "o partidarismo não atenuou o efeito no único teste pré-especificado dentro da síntese principal (@Cornejo2023a)".

**7. `aviso`: quem registra a pesquisa (Contextualização, 1.º parágrafo).**
- Trecho no texto: "a Lei das Eleições obriga quem divulga pesquisa eleitoral a registrá-la na Justiça Eleitoral até cinco dias antes da divulgação".
- No dossiê: `contexto_brasil.md`, seção 1, diz que o art. 33 obriga as entidades e empresas que **realizam** pesquisas para conhecimento público.
- Correção sugerida: "a Lei das Eleições obriga as entidades e empresas que realizam pesquisas eleitorais para conhecimento público a registrá-las na Justiça Eleitoral até cinco dias antes da divulgação".

**8. `aviso`: tramitação do PL 2.567/2022 (Contextualização, 3.º parágrafo).**
- Trecho no texto: "Em 24/09/2026, o primeiro estava pronto para pauta".
- No dossiê: o PL 2.567/2022 está apensado ao PL 1.764/2022, que está apensado ao PL 96/2011. A situação "Pronta para Pauta", desde 13/03/2025, é a da proposição principal, cujo id é 491042, o link da nota.
- Correção sugerida: "Em 24/09/2026, o primeiro tramitava apensado ao PL nº 96/2011, pronto para pauta".

**9. `aviso`: embargo de pesquisas pré-eleitorais (seção "O que isso significa para o debate brasileiro", 2.º parágrafo e item "Regulação da divulgação").**
- Trechos no texto: "Nenhum estudo avalia um embargo de pesquisas pré-eleitorais como o que o STF derrubou em 2006." e "A evidência sobre proibições vem de boca de urna em outros países".
- No arquivo: @Lago2015, citado na frase anterior, é justamente um corte transversal sobre dias de proibição de pesquisas pré-eleitorais (46 países, efeito E01 no `FORA`).
- Correção sugerida: "Nenhum estudo da síntese principal avalia um embargo de pesquisas pré-eleitorais como o que o STF derrubou em 2006; o único que trata disso, @Lago2015, é um corte transversal que ficou fora da contagem." Para o outro trecho: "A evidência sobre proibições vem de boca de urna em outros países e de um corte transversal fora da contagem [@Lago2015]."

**10. `aviso`: cabeçalho do fluxograma PRISMA (@fig-prisma).**
- No arquivo: `07-relatorio/prisma.png` e `prisma_contagens.json` listam 17 pendências, sem a P042. O documento diz 18.
- Correção sugerida: na legenda da figura, "Fluxograma PRISMA 2020 calculado do registro de decisões (rascunho). O cabeçalho da figura foi gerado antes da abertura da P042 e lista 17 das 18 pendências abertas." Refazer o `rs prisma` também resolveria, mas ele regrava `checklist_prisma.csv` (armadilha do CLAUDE.md).

**11. `aviso`: fonte do item (vi) no callout de Efeito.**
- Trecho no texto: "Os árbitros de IA deixaram em aberto decisões (...) (`08-revisao-humana/efeitos/pontos_para_o_revisor.md`). São elas: (...) e (vi) o rebaixamento por viés de publicação no agrupamento amplo."
- No arquivo: o item (vi) não está em `pontos_para_o_revisor.md`. Ele vem do rascunho do GRADE (`certeza_agrupamento_amplo.csv`; P036).
- Correção sugerida: "(...) e (v) a regra de ano da eleição nos experimentos de laboratório. O rascunho do GRADE deixou ainda para o autor (vi) o rebaixamento por viés de publicação no agrupamento amplo."

**12. `aviso`: descrição da P042 no Apêndice A.**
- Trecho no texto (linha da P042): "validar os juízos GRADE. A P042 foi aberta pelo `rs caixa` em 24/09 e pede o mesmo".
- No arquivo: `_pendencias_abertas.json` registra "completar certeza (GRADE/CERQual) e enunciados das células pendentes" (n = 22). A linha repete a da P036, copiada da linha combinada "P036 e P042" do README de `08-revisao-humana/`.
- Correção sugerida: "completar a certeza (GRADE/CERQual) e os enunciados das 22 células pendentes que o `rs caixa` apontou; na prática, pede a mesma validação da P036".

### Ok com ressalva

**13. `ok com ressalva`: primeira mensagem principal.** A frase "A evidência é muito incerta sobre se ver uma pesquisa aumenta o apoio a quem ela mostra à frente (8 experimentos...)" junta duas células do protocolo. As duas têm certeza muito baixa em `certeza.csv`, e por isso a frase padrão está certa, mas o "8 experimentos" não corresponde a nenhuma linha de GRADE. O agrupamento amplo tem 9 estudos. Sugestão: "(8 experimentos em duas células, cada uma com certeza muito baixa; quase todos em laboratório ou com vinheta hipotética)".

**14. `ok com ressalva`: resumo e *abstract*.** "Ter visto a divulgação de pesquisas pode aumentar o comparecimento" encurta o enunciado da célula, que diz "a intenção de votar ou o comparecimento". A mensagem principal e o corpo usam a forma completa. Sugestão: "pode aumentar a intenção de votar ou o comparecimento" / "*may increase turnout intention or turnout*".

**15. `ok com ressalva`: revisões anteriores.** "@Hardmeier2008, um capítulo com meta-análise" e "@MoyRinke2012 fizeram uma revisão narrativa, sem protocolo nem busca sistemática" vêm do protocolo (`00-protocolo/protocolo.md`, tabela de revisões) e do relatório técnico. O dossiê de contexto, porém, registra que não teve acesso ao texto dos dois capítulos. O próprio documento já ressalva Hardmeier. Sugestão: "um capítulo que a checagem do protocolo classificou como síntese com meta-análise".

**16. `ok com ressalva`: quem decidiu o árbitro.** Na Metodologia, a Emenda 3 diz que o árbitro "passou, por custo, a um modelo igual ao do avaliador A" sem dizer quem decidiu. `emendas.md` e o relatório técnico atribuem a escolha ao revisor humano, que não aparece na lista de decisões humanas da seção "Uso de inteligência artificial". Sugestão: acrescentar "e escolheu por custo o árbitro do risco de viés (Emenda 3)" à frase "O único humano, o autor, aprovou (...)".

**17. `ok com ressalva`: δ da célula principal.** O documento usa δ = 0,0573 (mediana de p0 = 0,73), como `_delta_celula.txt`, `meta_resumo.json` e a nota de 24/09 em `emendas.md`. O `CLAUDE.md` ainda cita 0,0588 e 0,74, e a Emenda 5, item 7, cita 0,059 e "REML + Hartung-Knapp". O método rodado é CHE + RVE (CR2), que o protocolo previa para dependência (relatório técnico, 13d). Nada a corrigir no documento; o descompasso está nos arquivos de apoio.

**18. `ok com ressalva`: caixa na célula de Gerber2020a.** Em `caixa_ferramentas.csv`, o rótulo de pesquisa pré-eleitoral × mobilização × randomizado usa certeza muito baixa, que vem da célula de Agranov2017a, Groer2010a e Erlich2023, e não a moderada de Gerber2020a. O documento explica isso: rótulo por família × desfecho × desenho, repetido nas células, e Nulo só com meta-análise. A certeza por célula da @tbl-caixa-celulas está certa (moderada).

## 3. Scripts usados

Todos rodam da raiz do projeto e só leem arquivos. Também usei, sem alterar, `09-documento-final/insumos/contagens_mecanismos_moderadores.py` (tabelas T9, T11, T12, T14 e T16).

### `s1_swim.py`

```python
import json,glob
for f in sorted(glob.glob('06-analise/swim_*/swim_resumo.json')):
    d=json.load(open(f))
    print('=====',f, d['parametros'].get('grupo'), 'excl', d['parametros'].get('excluir_rob'))
    for g in d['grupos']:
        ic=g['ic_proporcao']; 
        ics = f"{ic[0]:.2f}-{ic[1]:.2f}" if ic else 'NA'
        pb=g['proporcao_benefica']
        sens=g.get('sensibilidade',{}).get('com_rob_critico',{})
        s = f" |CRIT: exec={sens.get('executado')} b={sens.get('n_beneficos')} d={sens.get('n_danosos')} ic={sens.get('ic_proporcao')} p={sens.get('p_sinal')}" if sens.get('executado') else ''
        print(g['grupo'],'| k',g['k_estudos'],'n',g['n_estudos'],'b',g['n_beneficos'],'d',g['n_danosos'],'m',g['n_mistos'],'nul',g['n_nulos'],'sd',g['n_sem_direcao'],'prop',pb,ics,'p',g['p_sinal'],'altos',g['so_risco_alto'],g['estudos'],'crit',g.get('excluidos_rob_critico',{}).get('estudos'),s)
```

### `s2_contagens.py`

```python
import csv, json
from collections import Counter
ef=list(csv.DictReader(open('05-decomposicao/efeitos_para_sintese.csv')))
print('efeitos',len(ef),'estudos com efeitos',len({e['chave'] for e in ef}))
princ=[e for e in ef if e['modelo_principal'] in ('1','sim','True','true')]
print('modelo_principal valores',Counter(e['modelo_principal'] for e in ef))
print('principais',len(princ),'estudos com principal',len({e['chave'] for e in princ}))
m=list(csv.DictReader(open('05-decomposicao/fichamentos_master.csv')))
print('master',len(m))
for col in ['realismo_contexto','regiao','pais_estudo','ano','voto_obrigatorio','sistema_eleitoral','n_competidores','dias_ate_eleicao']:
    if col in m[0]: print(col,Counter(x[col] for x in m).most_common(40))
rob=list(csv.DictReader(open('04-qualidade/rob_geral.csv')))
print('rob resultados',len(rob),'estudos',len({r['chave'] for r in rob}))
print(Counter((r['ferramenta'],r['rob_geral']) for r in rob))
print('criticos',sorted({r['chave'] for r in rob if r['rob_geral']=='critico'}))
```

### `s3_citacoes.py`

```python
import re
doc=open('09-documento-final/revisao_final.qmd').read()
keys=set(re.findall(r'(?<![\w.])@([A-Za-z][\w:-]*)',doc))
xref={k for k in keys if k.startswith(('sec-','tbl-','fig-'))}
cites=keys-xref
bib=set()
for f in ['07-relatorio/references.bib','09-documento-final/referencias_contexto.bib']:
    bib|=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,',open(f).read()))
print('citações',len(cites),'faltando no bib:',sorted(cites-bib))
# xrefs
ids=set(re.findall(r'#((?:sec|tbl|fig)-[\w-]+)',doc))
print('xrefs sem alvo:',sorted(xref-ids))
# chaves sem @ (tipo Gerber2020a-E12) que não existem no bib
bare=set(re.findall(r'\b([A-Z][a-z]+\d{4}[a-z]?)(?:-E\d+)?\b',doc))
print('chaves nuas não no bib:',sorted(b for b in bare if b not in bib))
```

### `s4_verificar.py`

```python
"""Verificação programática de revisao_final.qmd contra os arquivos de origem. Só lê arquivos."""
import csv, json, re
from collections import Counter
D = open('09-documento-final/revisao_final.qmd').read()
TXT = re.sub(r'\s+', ' ', D)
res = []
def ok(nome, cond, det=''):
    res.append(('OK' if cond else 'FALHA', nome, det))
def has(s): return s in TXT
def br(x, d=2): return f'{x:.{d}f}'.replace('.', ',')

# ---------- fontes
pr = json.load(open('07-relatorio/prisma_contagens.json'))
nj = json.load(open('09-documento-final/insumos/tabelas/numeros.json'))
pend = json.load(open('07-relatorio/_pendencias_abertas.json'))
sw = json.load(open('06-analise/swim_principal/swim_resumo.json'))
amplo = {g['grupo']: g for g in json.load(open('06-analise/swim_sens_agrupamento_amplo/swim_resumo.json'))['grupos']}
cert = list(csv.DictReader(open('06-analise/certeza.csv')))
certA = list(csv.DictReader(open('06-analise/certeza_agrupamento_amplo.csv')))
ef = list(csv.DictReader(open('05-decomposicao/efeitos_para_sintese.csv')))
rob = list(csv.DictReader(open('04-qualidade/rob_geral.csv')))
master = {r['citekey']: r for r in csv.DictReader(open('05-decomposicao/fichamentos_master.csv'))}
inc = {r['chave']: r for r in csv.DictReader(open('07-relatorio/incluidos.csv'))}
delta = open('06-analise/_delta_celula.txt').read().strip()
meta = json.load(open('06-analise/meta_exploratoria/meta_resumo.json'))['grupos'][0]['resultado']
metaM = json.load(open('06-analise/meta_mesmo_candidato/meta_resumo.json'))['grupos'][0]['resultado']
metaI = json.load(open('06-analise/meta_exploratoria_icc020/meta_resumo.json'))['grupos'][0]['resultado']
sr = list(csv.DictReader(open('02-triagem/sem_resumo_revisao/resumos_recuperados.csv')))
fila = list(csv.DictReader(open('02-triagem/sem_resumo_revisao/fila_humana_ta_v1.csv')))

# ---------- contagens gerais
ok('41 estudos / 55 relatos', pr['incluidos'] == {'estudos': 41, 'relatos': 55} and has('41 estudos (55 relatos)'))
ok('560 efeitos de 40 estudos', len(ef) == 560 and len({e['chave'] for e in ef}) == 40 and has('40 têm efeitos extraídos (560 no total)'))
ok('37 estudos com principal', len({e['chave'] for e in ef if e['modelo_principal'] == 'sim'}) == 37 and has('37 têm ao menos um efeito principal'))
ok('27 estudos em 18 células', nj['n_swim_principal_estudos'] == 27 and nj['swim_principal_celulas_com_estudo'] == 18 and has('27 estudos em 18 células'))
ok('realismo 25/9/7', Counter(m['realismo_contexto'] for m in master.values()) == Counter(real=25, induzido=9, hipotetico=7) and has('real em 25 dos 41 estudos, com preferências induzidas em 9 e hipotético em 7'))
anos = [int(inc[k]['ano']) for k in master]
ok('publicados 2010 a 2024', (min(anos), max(anos)) == (2010, 2024) and has('publicados de 2010 a 2024'))
# ---------- PRISMA
b, o = pr['bases'], pr['outros_metodos']
for frag, val in [('1.767 registros nas bases', b['identificados']['bases'] == 1767),
                  ('1.687 no OpenAlex e 80 na BDTD', b['identificados']['por_fonte'] == {'openalex': 1687, 'bdtd': 80}),
                  ('1.706 por busca de citação', o['identificados']['busca_citacoes'] == 1706),
                  ('triamos 1.573 registros das bases e 1.054', (b['triados'], o['triados']) == (1573, 1054)),
                  ('texto completo de 259 e 267', (b['buscados'], o['buscados']) == (259, 267)),
                  ('158 e 184 não foram recuperados', (b['nao_recuperados'], o['nao_recuperados']) == (158, 184)),
                  ('101 e 83 foram avaliados', (b['avaliados'], o['avaliados']) == (101, 83)),
                  ('59 e 70 exclusões', (b['excluidos_elegibilidade']['total'], o['excluidos_elegibilidade']['total']) == (59, 70)),
                  ('(39 e 50)', (b['excluidos_elegibilidade']['motivos']['c2_intervencao_estudada'], o['excluidos_elegibilidade']['motivos']['c2_intervencao_estudada']) == (39, 50)),
                  ('(42 das bases e 13 dos outros métodos)', (b['incluidos_relatos'], o['incluidos_relatos']) == (42, 13)),
                  ('Os 1.235 registros da busca substituída B01', pr['buscas_inativas']['n_registros'] == 1235)]:
    ok('PRISMA: ' + frag, val and has(frag))
log = {r['busca_id']: int(r['n_resultados_base']) for r in csv.DictReader(open('01-busca/log_buscas.csv'))}
ok('buscas B05/B02/B03/B04', (log['B05'], log['B02'], log['B03'], log['B04']) == (1438, 118, 131, 80) and has('(B05, 1.438 registros), português (B02, 118) e espanhol (B03, 131)') and has('(B04, 80 registros)'))
sn = {}
for l in open('rs_log.jsonl'):
    e = json.loads(l)
    if e.get('evento') == 'busca_registrada' and e['dados'].get('rodada', '').startswith('SN'):
        sn[e['dados']['rodada']] = (e['dados']['n_sementes'], e['dados']['n_gravados'], e['ts'][:10])
ok('SN1-SN3', sn == {'SN1': (38, 1189, '2026-09-19'), 'SN2': (12, 411, '2026-09-20'), 'SN3': (3, 106, '2026-09-20')} and has('SN1 (38 sementes, 1.189 registros, 19/09/2026), SN2 (12 sementes, 411 registros, 20/09/2026) e SN3 (3 sementes, 106 registros, 20/09/2026)'), str(sn))
# ---------- Emenda 6b
nrec = sum(1 for x in sr if x['resumo'].strip())
dec = Counter(x['decisao_humana'] for x in fila)
ok('6b: 172 resumos, 156 exclusões, 180 seguiram', (len(sr), nrec, dec['excluir'], dec['incerto']) == (336, 172, 156, 180) and has('172 deles') and has('Houve 156 exclusões, e 180 registros'))
# ---------- RoB
c = Counter((r['ferramenta'], r['rob_geral']) for r in rob)
ok('RoB 43 resultados de 37 estudos', len(rob) == 43 and len({r['chave'] for r in rob}) == 37 and has('43 resultados de 37 estudos'))
ok('RoB 2 17/6, ROBINS 2/8/3, EPOC 6/1', (c[('rob2','algumas_preocupacoes')], c[('rob2','alto')], c[('robins_i','moderado')], c[('robins_i','grave')], c[('robins_i','critico')], c[('epoc','alto')], c[('epoc','baixo')]) == (17,6,2,8,3,6,1)
   and has('23 com RoB 2 (17 com algumas preocupações e 6 em risco alto), 13 com ROBINS-I V2 (2 moderado, 8 grave e 3 crítico) e 7 com EPOC (6 alto e 1 baixo)'))
ok('críticos', sorted(r['chave'] for r in rob if r['rob_geral'] == 'critico') == ['Gasperoni2015a', 'Kaplan2019a', 'Unkelbach2022a'])
ok('D5 21/23, D1 11/13, 259/88/79', (nj['rob2_D5_algumas'], nj['robins_D1_grave_critico'], sum(nj['rob_dominios'].values()), nj['rob_dominios']['arbitro_ia'], nj['arbitro_segue']['A']) == (21, 11, 259, 88, 79))
# ---------- δ e metas
ok('δ célula = 0,0573', delta == '0.0573' and has('0,0573'))
ok('meta sem pesquisa', (br(meta['estimativa']), br(meta['ic'][0]), br(meta['ic'][1]), br(meta['p'],3), br(meta['gl']), br(meta['tau2']), str(round(meta['I2']))) == ('0,48','-1,51','2,47','0,263','1,25','0,04','15')
   and has('g = 0,48 (IC 95% −1,51 a 2,47; p = 0,263), com 1,25 grau') and has('τ² = 0,04 e I² = 15%'))
ok('meta sem pesquisa, LOO 0,19 a 0,69; sem Timotei 0,40 a 0,98', nj['meta']['loo'] == ['0,19', '0,69'] and ['ES1876', '0,69', '0,40', '0,98'] in nj['meta_loo'] and has('variou de 0,19 a 0,69') and has('sem @Timotei2013a (0,40 a 0,98)'))
ok('meta ICC 0,20 (0,51; −0,97 a 1,98) não muda leitura', not metaI['ic_exclui_zero'])
ok('meta mesmo candidato', (br(metaM['estimativa']), br(metaM['ic'][0]), br(metaM['ic'][1]), br(metaM['p'],3), br(metaM['gl']), str(round(metaM['I2']))) == ('0,62','-0,48','1,72','0,111','1,46','94')
   and has('g = 0,62 (IC 95% −0,48 a 1,72; p = 0,111), com 1,46 grau') and has('I² = 94%') and has('variou de 0,55 a 0,90') and has('sem @Lammers2022a (0,85 a 0,94)'))
# ---------- tabela SWiM principal x swim_resumo e certeza
lab = {'pesquisa pré-eleitoral': 'pesquisa_pre_eleitoral', 'agregador ou projeção': 'agregador_projecao', 'boca de urna': 'boca_de_urna', 'outro': 'outro',
       'mesmo candidato atrás': 'mesmo_candidato_atras', 'outro resultado': 'outro_resultado', 'sem pesquisa': 'sem_pesquisa', 'unidades não expostas': 'unidades_nao_expostas',
       'antes e depois da proibição': 'antes_depois_proibicao', 'randomizado': 'randomizado', 'não randomizado': 'nao_randomizado'}
grupos = {(g['familia_intervencao'], g['construto_outcome'], g['comparador_tipo'], g['celula_alvo'], g['classe_desenho']): g for g in sw['grupos']}
cmap = {(r['familia_intervencao'], r['construto_outcome'], r['comparador_tipo'], r['celula_alvo'], r['classe_desenho']): r['certeza'].replace('_', ' ') for r in cert}
tab = D.split('| Exposição | Desfecho')[1].split(': SWiM principal')[0]
linhas = [l for l in tab.strip().split('\n')[2:] if l.startswith('|')]
ok('tbl-swim tem 19 linhas', len(linhas) == len(sw['grupos']) == 19)
for l in linhas:
    c = [x.strip() for x in l.strip('|').split('|')]
    fam = lab[c[0]]; cons, alvo = re.match(r'(\w+) \(\*?([^)*]+)\*?\)', c[1]).groups()
    cons = {'apoio': 'apoio_ao_lider', 'mobilização': 'mobilizacao'}[cons]; alvo = {'mobilização': 'mobilizacao'}.get(alvo, alvo)
    k = (fam, cons, lab.get(c[2], c[2]), alvo, lab[c[3]]); g = grupos.get(k)
    if not g: ok('tbl-swim linha sem grupo', False, l[:80]); continue
    est = re.findall(r'@(\w+)', c[4].split('(fora')[0])
    nums = [int(x) for x in re.findall(r'(\d+) ', c[5] + ' ')]
    esp = [g['n_beneficos'], g['n_danosos']] + ([g['n_mistos']] if g['n_mistos'] else []) + ([g['n_nulos']] if g['n_nulos'] else [])
    if g['n_nulos'] and not g['n_beneficos']: esp = [0, 0, g['n_nulos']]
    ic = g['ic_proporcao']; prop = 'NR' if ic is None else f"{br(g['proporcao_benefica'])} ({br(ic[0])} a {br(ic[1])})"
    pv = 'NR' if g['p_sinal'] is None else ('1' if g['p_sinal'] == 1 else br(g['p_sinal'], 3).rstrip('0'))
    certz = cmap.get(k, 'não julgada (célula vazia)')
    if not g['estudos']: esp, nums = [], []
    okl = est == g['estudos'] and nums[:len(esp)] == esp and c[6] == prop and c[7] == pv and c[8] == certz
    ok('tbl-swim ' + ' | '.join(k), okl, f'doc: {c[4:]} | arq: {g["estudos"]} {esp} {prop} p={pv} {certz}')
# ---------- certeza: contagem
cc = Counter(r['certeza'] for r in cert)
ok('certeza 15/2/1 e amplo 7 muito baixa', cc == Counter(muito_baixa=15, baixa=2, moderada=1) and Counter(r['certeza'] for r in certA) == Counter(muito_baixa=7)
   and has('15 ficaram com certeza muito baixa, 2 com baixa e 1 com moderada') and has('As 7 linhas do agrupamento amplo ficaram todas com muito baixa'))
# ---------- sensibilidades (agrupamento amplo)
def s(path, grupo):
    return {g['grupo']: g for g in json.load(open(path))['grupos']}[grupo]
g9 = amplo['apoio_ao_lider | principal | randomizado']
ok('amplo 9 de 9, IC 0,66-1,00, p 0,004', (g9['n_beneficos'], g9['n_estudos'], br(g9['ic_proporcao'][0]), round(g9['p_sinal'], 3)) == (9, 9, '0,66', 0.004) and has('9 de 9 experimentos foram na direção *bandwagon* (proporção 1,00; IC 95% 0,66 a 1,00; p = 0,004)'))
gx = s('06-analise/swim_sens_com_excluidos_amplo/swim_resumo.json', 'apoio_ao_lider | principal | randomizado')
ok('com excluídos 10 de 11, p 0,012', (gx['n_beneficos'], gx['n_estudos'], round(gx['p_sinal'], 3)) == (10, 11, 0.012) and has('10 de 11 na direção *bandwagon* (p = 0,012)'))
gp = s('06-analise/swim_sens_sem_pre2010_amplo/swim_resumo.json', 'apoio_ao_lider | principal | randomizado')
ok('sem pré-2010 8 de 8, p 0,008', (gp['n_beneficos'], gp['n_estudos'], round(gp['p_sinal'], 3)) == (8, 8, 0.008) and has('8 de 8 (p = 0,008)'))
ga = s('06-analise/swim_sens_sem_araujo_amplo/swim_resumo.json', 'apoio_ao_lider | principal | nao_randomizado')
ok('sem Araujo 2 de 3', (ga['n_beneficos'], ga['n_estudos']) == (2, 3) and has('ficam com 2 de 3'))
gr = s('06-analise/swim_sens_so_contexto_real_amplo/swim_resumo.json', 'mobilizacao | mobilizacao | nao_randomizado')
ok('só real: mobilização não rand. 2/2/1 misto', (gr['n_beneficos'], gr['n_danosos'], gr['n_mistos']) == (2, 2, 1))
ok('ICC 0,20 igual à principal', [ (g['grupo'], g['n_beneficos'], g['n_danosos'], g['n_mistos'], g['n_nulos']) for g in json.load(open('06-analise/swim_sens_icc020/swim_resumo.json'))['grupos']]
   == [(g['grupo'], g['n_beneficos'], g['n_danosos'], g['n_mistos'], g['n_nulos']) for g in sw['grupos']])
# ---------- efeitos individuais (06-analise/efeitos.csv)
E = {r['id_efeito']: r for r in csv.DictReader(open('06-analise/efeitos.csv'))}
def g_(i): return float(E[i]['yi'])
def se_(i): return float(E[i]['sei'])
for frag, cond in [('E01: 0,13 (0,003) (5,69 p.p.); E06: 0,26 (0,003) (11,76 p.p.)', (br(g_('Araujo2021a-E01')), br(se_('Araujo2021a-E01'),3), E['Araujo2021a-E01']['efeito_pp'], br(g_('Araujo2021a-E06'))) == ('0,13','0,003','5.69','0,26')),
                   ('E05: 0,19 (0,105)', (br(g_('Cornejo2023a-E05')), br(se_('Cornejo2023a-E05'),3)) == ('0,19','0,105')),
                   ('E01: 0,03 (0,016)', (br(g_('Lago2015-E01')), br(se_('Lago2015-E01'),3)) == ('0,03','0,016')),
                   ('+3,40 pontos percentuais; g = 0,12, EP 0,080', (br(g_('Dahlgaard2016a-E01')), br(se_('Dahlgaard2016a-E01'),3)) == ('0,12','0,080')),
                   ('@Meer2015a (g = 0,13, EP 0,072)', (br(g_('Meer2015a-E01')), br(se_('Meer2015a-E01'),3)) == ('0,13','0,072')),
                   ('g = −0,10, EP 0,023', (br(g_('Westwood2020a-E01')), br(se_('Westwood2020a-E01'),3), E['Westwood2020a-E01']['n_total']) == ('-0,10','0,023','5845') and g_('Westwood2020a-E01') + 1.96*se_('Westwood2020a-E01') < -0.046),
                   ('g = 1,25 e 1,03 no modo heurístico e −0,39 e 0,06', [br(g_(f'Lammers2022a-E0{i}')) for i in (6,8,7,9)] == ['1,25','1,03','-0,39','0,06']),
                   ('(g = −0,41 na convenção da célula)', br(g_('Freden2024a-E01')) == '-0,41'),
                   ('(g = 0,33) do que entre independentes (0,09)', [br(g_(f'Cornejo2023a-E{i}')) for i in ('06','08','10')] == ['0,33','0,09','-0,05']),
                   ('(−11 pontos percentuais)', float(E['Morton2015a-E12']['efeito_pp']) == -11),
                   ('(+11 e +17 pontos percentuais)', (E['Schlegel2023-E01']['efeito_pp'], E['Schlegel2023-E02']['efeito_pp']) == ('11','17')),
                   ('comparecimento em 0,08 ponto', E['Gerber2020a-E12']['efeito_pp'] == '0.08')]:
    ok('efeito: ' + frag, cond and has(frag.replace('−','−')), frag)
# ---------- moderadores: voto obrigatório nas células de mobilização da SWiM principal
mob = sorted({e for g in sw['grupos'] if g['construto_outcome'] == 'mobilizacao' for e in g['estudos']})
vo = Counter(master[k]['voto_obrigatorio'] for k in mob)
ok('voto obrigatório: "12 estudos ... 2 não e 10 não informado"', (len(mob), vo.get('Não', 0), vo.get('999', 0)) == (12, 2, 10), f'arquivo: {len(mob)} estudos de comparecimento na SWiM principal, Não = {vo.get("Não",0)}, 999 = {vo.get("999",0)}, Sim = {vo.get("Sim",0)} ({mob})')
ap = sorted({e for g in amplo.values() if g['grupo'].startswith('apoio_ao_lider | principal') for e in g['estudos']})
ok('13 estudos da célula principal; 8 com regra do experimento', len(ap) == 13 and sum(master[k]['sistema_eleitoral'] == 'regra_do_experimento' for k in ap) == 8)
# ---------- pendências
ids_doc = re.findall(r'^\| (P\d{3}) \|', D, re.M)
ids_arq = [p['id'] for p in pend['pendencias']]
ok('apêndice: 18 pendências, IDs iguais', len(ids_doc) == 18 and sorted(ids_doc) == sorted(ids_arq) and pend['abertas'] == 18, f'doc {sorted(ids_doc)}')
ok('todas as pendências citadas em algum callout/trecho fora do apêndice', all(i in D.split('# Apêndice A')[0] for i in ids_arq), str([i for i in ids_arq if i not in D.split('# Apêndice A')[0]]))
P = {p['id']: p for p in pend['pendencias']}
ok('P042 descrita como no arquivo', 'completar certeza' in D.split('| P042 |')[1].split('\n')[0], 'arquivo: ' + P['P042']['descricao'])
ok('P041 n=165, P039 n=560, P019 145, P020 81, P006 141, P007 300', (P['P041']['n'], P['P039']['n'], P['P019']['n'], P['P020']['n'], P['P006']['n'], P['P007']['n']) == (165, 560, 145, 81, 141, 300))
# ---------- termos proibidos
ok('sem "Neutro" / "sem efeito"', not re.search(r'\bNeutro\b|sem efeito', D))

for r in res:
    if r[0] != 'OK' or True: print(r[0], '|', r[1], '|', r[2][:300] if r[0] != 'OK' else '')
print(Counter(r[0] for r in res))
```

## 4. Correções aplicadas (24/09/2026)

Aplicadas por subagente de IA (Claude Opus 5.5) no esqueleto `09-documento-final/_esqueleto_revisao_final.qmd` e, para as divergências 6 e 12, no `09-documento-final/montar_revisao_final.py`. O `revisao_final.qmd` foi refeito com `python3 09-documento-final/montar_revisao_final.py`. O `08-revisao-humana/README.md` não foi alterado. As divergências 17 e 18 não pediam correção no documento.

| # | Onde | O que foi feito |
|---|---|---|
| 1 | Moderadores, "Voto obrigatório" | "12 estudos ... 2 ... 10" passou a "11 estudos ... 2 ... 9", como sugerido. |
| 2 | Resumo executivo, 4.º parágrafo | Trecho trocado pelo texto sugerido ("Em eleições reais, ter visto a divulgação de pesquisas pode aumentar a participação e, num jogo *online*, ver projeções que mostram a eleição decidida pode reduzi-la (certeza baixa nos dois casos)"). |
| 3 | Mecanismo, "Pivotalidade e emoções" | Primeira frase trocada pela sugerida (projeções: "pode reduzir", certeza baixa; boca de urna: "a evidência é muito incerta", certeza muito baixa). A frase de @Klor2017a passou a "em @Klor2017a, revelar a distribuição de preferências aparece associado a mais comparecimento só em eleitorados quase divididos (achado dentro do estudo, descritivo; a célula tem certeza muito baixa)". |
| 4 | Mecanismo, "Voto estratégico e viabilidade" | "aumenta a deserção" passou a "aparece associada a mais deserção", com o acréscimo de que os dois primeiros estudos estão em células de apoio principal com certeza muito baixa e @Tyszler2013 não entra em nenhuma célula. |
| 5 | Moderadores, "Proximidade da disputa" | Frase de @Gerber2020a reescrita com a frase padrão ("provavelmente não muda o comparecimento além de ±2 pontos percentuais (certeza moderada)"). |
| 6 | @tbl-oqf, linha Moderador | No `montar_revisao_final.py`: "único teste pré-especificado dentro da síntese principal (@Cornejo2023a)". |
| 7 | Contextualização, 1.º parágrafo | "quem divulga pesquisa eleitoral a registrá-la" passou a "as entidades e empresas que realizam pesquisas eleitorais para conhecimento público a registrá-las". |
| 8 | Contextualização, 3.º parágrafo | "o primeiro estava pronto para pauta" passou a "o primeiro tramitava apensado ao PL nº 96/2011, pronto para pauta". |
| 9 | "O que isso significa para o debate brasileiro" e item "Regulação da divulgação" | As duas frases trocadas pelas sugeridas, citando @Lago2015 como corte transversal fora da contagem. |
| 10 | Legenda da @fig-prisma | Acrescentado: "O cabeçalho da figura foi gerado antes da abertura da P042 e lista 17 das 18 pendências abertas." O `rs prisma` não foi rodado. |
| 11 | Callout de Efeito | A lista de `pontos_para_o_revisor.md` termina em (v); o item (vi) passou a vir do rascunho do GRADE, como sugerido. |
| 12 | Apêndice A, linha da P042 | No `montar_revisao_final.py`, a tarefa da P042 deixou de vir da linha combinada "P036 e P042" do README e passou a ser montada do registro da pendência em `07-relatorio/_pendencias_abertas.json` (n = 22): "completar a certeza (GRADE/CERQual) e os enunciados das 22 células pendentes que o `rs caixa` apontou; na prática, pede a mesma validação da P036". A legenda da @tbl-pendencias registra essa exceção. Etapa, pacote e esforço continuam do README. |
| 13 | Primeira mensagem principal | "(8 experimentos, quase todos ...; certeza muito baixa)" passou a "(8 experimentos em duas células, cada uma com certeza muito baixa; quase todos em laboratório ou com vinheta hipotética)". |
| 14 | Resumo e *abstract* | "pode aumentar o comparecimento" passou a "pode aumentar a intenção de votar ou o comparecimento"; "*may increase turnout*" passou a "*may increase turnout intention or turnout*". |
| 15 | Revisões anteriores | "@Hardmeier2008, um capítulo com meta-análise" passou a "um capítulo que a checagem do protocolo classificou como síntese com meta-análise". |
| 16 | Uso de inteligência artificial | Acrescentado à lista de decisões do autor: "e escolheu por custo o árbitro do risco de viés (Emenda 3)". |

Conferências depois das correções: nenhum travessão no esqueleto, no `revisao_final.qmd` nem no script; as 51 chaves `@` do `revisao_final.qmd` existem em `07-relatorio/references.bib` ou `09-documento-final/referencias_contexto.bib`; todas as referências cruzadas têm alvo.

### Saída da trava

`python3 09-documento-final/conferir_numeros.py _esqueleto.antes_correcoes.qmd _esqueleto_revisao_final.qmd` (a cópia de antes foi apagada depois):

```
[numeros] sumiram: {'10': 1, '12': 1}
[numeros] apareceram: {'3': 1, '18': 1, '9': 1, '96': 1, '2011': 1, '2015': 2, '2013': 1, '11': 1, '17': 1, '042': 1}
[chaves] sumiram: {}
[chaves] apareceram: {'Lago2015': 2, 'Tyszler2013': 1}
[pendencias] sumiram: {}
[pendencias] apareceram: {'P042': 1}
[certezas] sumiram: {}
[certezas] apareceram: {'muito baixa': 3}
```

Explicação de cada diferença (todas intencionais):

- **Números que sumiram, 12 e 10; números que apareceram, 11 e 9:** divergência 1 (voto obrigatório).
- **3:** divergência 16 ("Emenda 3").
- **96 e 2011:** divergência 8 ("PL nº 96/2011").
- **17, 18 e 042:** divergência 10 (legenda da figura: "P042", "17 das 18"); a expressão da trava lê o "042" de "P042" como número.
- **2015 (2) e 2013 (1):** os anos dentro das chaves novas @Lago2015 (divergência 9, duas vezes) e @Tyszler2013 (divergência 4, a segunda menção); a trava lê os dígitos das chaves como números.
- **Chaves Lago2015 (2) e Tyszler2013 (1):** divergências 9 e 4.
- **Pendência P042 (1):** divergência 10.
- **"certeza muito baixa" (3):** duas da divergência 3 (boca de urna e célula de @Klor2017a) e uma da divergência 4 (células de apoio principal). Na divergência 13, "certeza muito baixa" só mudou de lugar na frase, e nas divergências 3 e 5 "certeza baixa" e "certeza moderada" foram mantidas, por isso não aparecem.

As divergências 6 e 12 foram feitas no script e não passam pela trava do esqueleto: acrescentam só texto sem número à @tbl-oqf e, na @tbl-pendencias, o n = 22 lido do arquivo de pendências.
