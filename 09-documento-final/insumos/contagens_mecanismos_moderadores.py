"""Contagens para 09-documento-final/insumos/mecanismos_moderadores.md.

USO (da raiz do projeto)
    python3 09-documento-final/insumos/contagens_mecanismos_moderadores.py

Só lê arquivos; não escreve nada. Imprime tabelas em Markdown que o documento cita.
Entradas:
    05-decomposicao/fichamentos_master.csv            (nível de estudo; fichamento por IA, não verificado)
    06-analise/efeitos.csv                            (560 linhas de efeito)
    06-analise/swim_entrada_com_excluidos.csv         (efeitos principais, com fora_contagem)
    06-analise/swim_principal/tabelas/swim_direcao.csv (direção por estudo e célula, análise principal)
    06-analise/certeza.csv                            (GRADE por célula)
Junções só por `chave` (= citekey do master) e `id_efeito`.
"""
import csv
import re
from collections import Counter, defaultdict

RAIZ = '.'


def ler(caminho):
    with open(f'{RAIZ}/{caminho}', encoding='utf-8') as f:
        return list(csv.DictReader(f))


master = ler('05-decomposicao/fichamentos_master.csv')
efeitos = ler('06-analise/efeitos.csv')
swim_exc = ler('06-analise/swim_entrada_com_excluidos.csv')
direcao = ler('06-analise/swim_principal/tabelas/swim_direcao.csv')
certeza = ler('06-analise/certeza.csv')

M = {r['citekey']: r for r in master}
ESTUDOS = sorted(M)


def tokens(valor, vocab):
    """Códigos controlados presentes num campo multivalorado ('a + b — especifique ...')."""
    v = (valor or '').lower()
    return [t for t in vocab if re.search(r'(^|[\s+(])' + re.escape(t) + r'($|[\s+),—-])', v)]


def tabela(cab, linhas):
    print('| ' + ' | '.join(cab) + ' |')
    print('|' + '---|' * len(cab))
    for l in linhas:
        print('| ' + ' | '.join(str(x) for x in l) + ' |')
    print()


# ---------------------------------------------------------------- 1. Mecanismos
print('## T1. Mecanismos testados (mecanismo_testado) por estudo\n')
MEC = ['informacao', 'viabilidade_estrategico', 'consenso_heuristica', 'conformidade',
       'simpatia_equidade', 'emocoes', 'outro', 'nao_testado']
por_mec = defaultdict(list)
for k in ESTUDOS:
    for t in tokens(M[k]['mecanismo_testado'], MEC):
        por_mec[t].append(k)
tabela(['mecanismo_testado', 'n estudos', 'estudos'],
       [(t, len(por_mec[t]), ', '.join(por_mec[t])) for t in MEC])

print('## T2. Tipo de evidência do mecanismo (mecanismo_tipo_evidencia)\n')
tipo = defaultdict(list)
for k in ESTUDOS:
    tipo[M[k]['mecanismo_tipo_evidencia'].strip()].append(k)
tabela(['mecanismo_tipo_evidencia', 'n', 'estudos'],
       [(t, len(v), ', '.join(v)) for t, v in sorted(tipo.items(), key=lambda x: -len(x[1]))])

print('## T3. Mecanismo × tipo de evidência (n estudos)\n')
tipos = ['mediacao_estatistica', 'teste_de_canal', 'relato_de_atores', 'hipotese_dos_autores', 'nao_discutido']
linhas = []
for t in MEC:
    c = Counter(M[k]['mecanismo_tipo_evidencia'].strip() for k in por_mec[t])
    linhas.append([t] + [c.get(x, 0) for x in tipos])
tabela(['mecanismo'] + tipos, linhas)

print('## T4. Modelo principal ajusta por mediador (ajuste_mediador começa com "Sim")\n')
tabela(['estudo', 'ajuste_mediador (início)'],
       [(k, M[k]["ajuste_mediador"][:120].replace(" — ", ": ")) for k in ESTUDOS if M[k]['ajuste_mediador'].startswith('Sim')])

# ---------------------------------------------------------------- 2. Moderadores relatados
print('## T5. Moderadores relatados (moderadores_relatados) por estudo\n')
MOD = ['partidarismo', 'preferencia_previa', 'sofisticacao_interesse', 'competitividade',
       'confianca_pesquisas', 'escolaridade', 'classe', 'idade', 'outro', 'nenhum']
por_mod = defaultdict(list)
for k in ESTUDOS:
    for t in tokens(M[k]['moderadores_relatados'], MOD):
        por_mod[t].append(k)
tabela(['moderador', 'n estudos', 'estudos'], [(t, len(por_mod[t]), ', '.join(por_mod[t])) for t in MOD])

print('## T6. Heterogeneidade: pré-especificação × método (n estudos)\n')
c = Counter((M[k]['het_pre_especificada'], M[k]['het_metodo']) for k in ESTUDOS)
metodos = ['termo_interacao', 'estratificacao', 'estratificacao_e_interacao', 'nenhum']
tabela(['het_pre_especificada'] + metodos,
       [[p] + [c.get((p, m), 0) for m in metodos] for p in ['sim', 'nao_declarado', 'nao_se_aplica']])

print('## T7. Linhas de efeito com subgrupo preenchido (efeitos.csv), por estudo\n')
sub = Counter(r['chave'] for r in efeitos if r['subgrupo'].strip())
tot = Counter(r['chave'] for r in efeitos)
tabela(['estudo', 'linhas com subgrupo', 'linhas no total'],
       [(k, sub[k], tot[k]) for k in sorted(sub, key=lambda x: -sub[x])])
print(f'Total: {sum(sub.values())} de {len(efeitos)} linhas, em {len(sub)} estudos.\n')

print('## T8. Efeitos principais fora da contagem (dicionário FORA), com motivo\n')
tabela(['id_efeito', 'construto', 'celula_alvo', 'motivo (fora_contagem)'],
       [(r['id_efeito'], r['construto_outcome'], r['celula_alvo'], r['fora_contagem'])
        for r in swim_exc if r['fora_contagem']])

# ---------------------------------------------------------------- 3. Moderadores de contexto × direção
# Direção por estudo e célula na SWiM principal (swim.R; benefico = bandwagon/viabilidade/mobilização
# pelo sinal alinhado; danoso = underdog/contra a viabilidade/desmobilização).
dirs = defaultdict(list)
for r in direcao:
    partes = [p.strip() for p in r['grupo'].split('|')]
    construto, cel, classe = partes[1], partes[3], partes[4]
    marca = r['direcao'] + (' [crítico, fora do teste]' if r['excluido_rob_critico'] == 'TRUE' else '')
    dirs[r['chave']].append((construto, cel, classe, marca))


def norm(v):
    v = (v or '').strip()
    if v.startswith('outro'):
        return 'outro'
    if v.startswith('survey_experiment'):
        return 'survey_experiment'
    return v


def ncomp(v):
    try:
        n = int(v)
    except ValueError:
        return '999'
    return '2' if n <= 2 else '3 ou mais'


def cruzar(campo, construto, cel=None, f=norm):
    """n estudos por nível do moderador × direção na célula (SWiM principal)."""
    cont = defaultdict(Counter)
    lista = defaultdict(list)
    for k, ds in dirs.items():
        for (c, ce, classe, d) in ds:
            if c != construto or (cel and ce not in cel):
                continue
            nivel = f(M[k][campo])
            cont[nivel][d.split(' ')[0] + ('*' if 'crítico' in d else '')] += 1
            lista[nivel].append(f'{k} ({d.split(" ")[0]}{"*" if "crítico" in d else ""}, {classe})')
    return cont, lista


def imprimir_cruzamento(titulo, campo, construto, cel=None, f=norm):
    print(f'## {titulo}\n')
    cont, lista = cruzar(campo, construto, cel, f)
    cats = ['benefico', 'danoso', 'misto', 'nulo', 'benefico*', 'danoso*']
    tabela([campo] + cats + ['estudos (direção, classe)'],
           [[n] + [cont[n].get(x, 0) for x in cats] + ['; '.join(lista[n])] for n in sorted(cont)])


print('Legenda: direção por estudo na SWiM principal (06-analise/swim_principal/tabelas/swim_direcao.csv). '
      '"*" = estudo em risco crítico, fora do teste de sinal principal. Um estudo pode aparecer em mais de uma '
      'célula. Comparação entre estudos, descritiva.\n')
AP_PRINC = {'principal'}
imprimir_cruzamento('T9. Apoio ao líder, célula principal: realismo do contexto', 'realismo_contexto',
                    'apoio_ao_lider', AP_PRINC)
imprimir_cruzamento('T10. Apoio ao líder, célula principal: desenho fino', 'desenho_fino',
                    'apoio_ao_lider', AP_PRINC)
imprimir_cruzamento('T11. Apoio ao líder, célula principal: sistema eleitoral', 'sistema_eleitoral',
                    'apoio_ao_lider', AP_PRINC)
imprimir_cruzamento('T12. Apoio ao líder, célula principal: número de competidores', 'n_competidores',
                    'apoio_ao_lider', AP_PRINC, ncomp)
imprimir_cruzamento('T13. Apoio ao líder, células principal, momentum e viabilidade: família da exposição',
                    'familia_intervencao', 'apoio_ao_lider')
imprimir_cruzamento('T14. Mobilização: realismo do contexto', 'realismo_contexto', 'mobilizacao')
imprimir_cruzamento('T15. Mobilização: família da exposição', 'familia_intervencao', 'mobilizacao')
imprimir_cruzamento('T16. Mobilização: voto obrigatório', 'voto_obrigatorio', 'mobilizacao')
imprimir_cruzamento('T17. Mobilização: número de competidores', 'n_competidores', 'mobilizacao', None, ncomp)

# ---------------------------------------------------------------- 4. Contexto (todos os 41)
print('## T18. Distribuição dos moderadores de contexto nos 41 fichamentos\n')
for campo, f in [('sistema_eleitoral', norm), ('n_competidores', ncomp), ('realismo_contexto', norm),
                 ('tipo_eleicao', norm), ('familia_intervencao', norm), ('regiao', norm),
                 ('voto_obrigatorio', norm), ('desenho_fino', norm)]:
    c = Counter(f(M[k][campo]) for k in ESTUDOS)
    print(f'- {campo}: ' + '; '.join(f'{a} = {b}' for a, b in c.most_common()))
print()
d_inf = [(k, M[k]['dias_ate_eleicao']) for k in ESTUDOS if M[k]['dias_ate_eleicao'].strip() != '999']
print(f'- dias_ate_eleicao informado em {len(d_inf)} de {len(ESTUDOS)}: ' + '; '.join(f'{k} = {v}' for k, v in d_inf))
m_inf = [k for k in ESTUDOS if M[k]['margem_mostrada'].strip() != '999']
print(f'- margem_mostrada informada em {len(m_inf)} de {len(ESTUDOS)}: ' + ', '.join(m_inf))
reg = [(k, M[k]['regiao'], M[k]['pais_estudo'][:60]) for k in ESTUDOS if M[k]['regiao'].strip() not in ('outro',)]
print('- regiao diferente de "outro": ' + '; '.join(f'{k} = {r} ({p})' for k, r, p in reg))
vo = [(k, M[k]['voto_obrigatorio']) for k in ESTUDOS if M[k]['voto_obrigatorio'].strip() != '999']
print('- voto_obrigatorio informado: ' + '; '.join(f'{k} = {v}' for k, v in vo))
print()

# ---------------------------------------------------------------- 5. Não intencionais e equidade
print('## T19. Efeitos não intencionais e equidade (campos diferentes de 999)\n')
ni = [k for k in ESTUDOS if M[k]['efeitos_nao_intencionais'].strip() not in ('', '999')]
print(f'- efeitos_nao_intencionais preenchido: {len(ni)} de {len(ESTUDOS)}; 999 em: '
      + ', '.join(k for k in ESTUDOS if k not in ni))
# Classificação do coordenador, lida no texto de efeitos_nao_intencionais do master (fichamento por IA,
# não verificado). 'dado' = o estudo mede ou estima o efeito com dados (qualquer direção);
# 'nao_achado' = testado e não encontrado na direção indesejada; 'discutido' = só discussão ou hipótese.
NAO_INT = {
    'Agranov2017a': {'desmobilizacao': 'dado'},            # minoria vota menos com informação
    'Alabrese2024a': {'desmobilizacao': 'dado', 'desercao': 'dado', 'pesquisa_enviesada': 'discutido'},
    'Araujo2021a': {'desmobilizacao': 'nao_achado', 'desercao': 'nao_achado'},
    'Boukouras2020a': {'bem_estar_decisao': 'dado', 'pesquisa_enviesada': 'dado'},
    'Bursztyn2023a': {'outro': 'dado'},                    # composição do eleitorado; inversão simulada
    'Chatterjee2019a': {'desmobilizacao': 'dado', 'outro': 'dado'},  # candidaturas, margem
    'Cornejo2023a': {'desercao': 'dado'},
    'Erlich2023': {'desmobilizacao': 'dado', 'outro': 'dado'},        # legitimidade
    'Farjam2020a': {'desercao': 'dado', 'pesquisa_enviesada': 'discutido'},
    'Freden2016b': {'desercao': 'dado', 'bem_estar_decisao': 'discutido'},
    'Freden2024a': {'desercao': 'nao_achado'},
    'Gasperoni2015a': {'desercao': 'dado'},
    'Geers2018': {'desmobilizacao': 'dado'},
    'Gerber2020a': {'outro': 'nao_achado'},                # busca de informação
    'Grillo2024c': {'desmobilizacao': 'dado'},
    'Groer2010a': {'bem_estar_decisao': 'dado'},           # comparecimento acima do ótimo
    'Kaplan2019a': {'desmobilizacao': 'dado'},
    'Klor2017a': {'desmobilizacao': 'dado'},               # time grande em eleitorado desequilibrado
    'Lago2015': {'bem_estar_decisao': 'dado'},             # atribuído à proibição (ausência de pesquisa)
    'Lammers2022a': {'pesquisa_enviesada': 'discutido'},
    'Meer2015a': {'outro': 'nao_achado'},                  # efeito Titanic
    'Meffert2011': {'bem_estar_decisao': 'dado'},
    'Meffert2012a': {'bem_estar_decisao': 'dado', 'desercao': 'dado'},
    'Morton2015a': {'desmobilizacao': 'dado', 'pesquisa_enviesada': 'discutido'},
    'Schlegel2023': {'outro': 'discutido'},                # desigualdade de recursos cognitivos
    'Stolwijk2019b': {'desmobilizacao': 'nao_achado'},
    'Tal2015a': {'desercao': 'dado', 'bem_estar_decisao': 'dado'},
    'Timotei2013a': {'pesquisa_enviesada': 'discutido'},
    'Tyszler2013': {'desercao': 'dado'},
    'Tyszler2015': {'desercao': 'dado', 'pesquisa_enviesada': 'discutido'},
    'Urminsky2019': {'desmobilizacao': 'dado', 'outro': 'dado'},     # apostas
    'Westwood2020a': {'desmobilizacao': 'dado', 'outro': 'dado'},    # confusão probabilidade × votos
    'Witsman2016a': {'desercao': 'dado'},
    'Yang2023d': {'desmobilizacao': 'discutido', 'outro': 'discutido'},  # relatos abertos
}
assert set(NAO_INT) == set(ni), set(NAO_INT) ^ set(ni)
cats = ['desmobilizacao', 'desercao', 'bem_estar_decisao', 'pesquisa_enviesada', 'outro']
linhas = []
for cat in cats:
    por = defaultdict(list)
    for k, d in NAO_INT.items():
        if cat in d:
            por[d[cat]].append(k)
    linhas.append([cat] + [f"{len(por[s])}: {', '.join(sorted(por[s]))}" if por[s] else '0'
                           for s in ['dado', 'nao_achado', 'discutido']])
tabela(['categoria', 'dado', 'nao_achado', 'discutido'], linhas)

eq = [k for k in ESTUDOS if M[k]['equidade_progress_plus'].strip() not in ('', '999')]
print(f'- equidade_progress_plus preenchido: {len(eq)} de {len(ESTUDOS)}: {", ".join(eq)}')
fat = defaultdict(list)
for k in eq:
    for seg in M[k]['equidade_progress_plus'].split(';'):
        if ':' not in seg:
            continue
        rot, cont = seg.split(':', 1)
        rot = rot.strip().lower()
        f = ('escolaridade' if rot.startswith('escolaridade') else
             'classe' if ('socioecon' in rot or 'classe' in rot) else
             'idade' if rot.startswith('idade') else None)
        if f and not cont.strip().startswith('999'):
            fat[f].append(k)
for f in ['escolaridade', 'classe', 'idade']:
    print(f'  - {f} com conteúdo diferente de 999: {len(fat[f])}: {", ".join(fat[f])}')
print()

# ---------------------------------------------------------------- 6. Certeza por estudo
print('## T20. Células GRADE (certeza.csv) em que cada estudo entra\n')
cel_est = defaultdict(list)
for r in certeza:
    rot = f"{r['familia_intervencao']}|{r['construto_outcome']}|{r['comparador_tipo']}|{r['celula_alvo']}|{r['classe_desenho']}: {r['certeza']}"
    for k in r['estudos'].split('|'):
        cel_est[k.strip()].append(rot)
tabela(['estudo', 'células (certeza)'], [(k, '<br>'.join(v)) for k, v in sorted(cel_est.items())])
sem = [k for k in ESTUDOS if k not in cel_est]
print(f'Estudos sem célula GRADE: {len(sem)}: {", ".join(sem)}\n')

# ---------------------------------------------------------------- 7. Sinais opostos entre subgrupos
print('## T21. Estudos com estimativas por subgrupo de sinais opostos (efeitos.csv; yi alinhado)\n')
print('Linhas com `subgrupo` preenchido, `yi` numérico e `sinal_alinhado` em mantido/invertido; '
      'conta linhas com yi > 0 e yi < 0 por estudo e construto. Protocolo, seção 8 [15d]: a hipótese de '
      'efeitos que se anulam só é afirmada com pelo menos 3 estudos com sinais opostos entre subgrupos.\n')
sinais = defaultdict(lambda: [0, 0, []])
for r in efeitos:
    if not r['subgrupo'].strip() or r['sinal_alinhado'] not in ('mantido', 'invertido'):
        continue
    try:
        y = float(r['yi'])
    except ValueError:
        continue
    s = sinais[(r['chave'], r['construto_outcome'])]
    if y > 0:
        s[0] += 1
    elif y < 0:
        s[1] += 1
        s[2].append(r['id_efeito'])
linhas = [(k, c, a, b, ', '.join(ids)) for (k, c), (a, b, ids) in sorted(sinais.items())]
tabela(['estudo', 'construto', 'subgrupos yi > 0', 'subgrupos yi < 0', 'ids com yi < 0'], linhas)
for c in ['apoio_ao_lider', 'mobilizacao']:
    opostos = [k for (k, cc), (a, b, _) in sinais.items() if cc == c and a and b]
    print(f'- {c}: estudos com sinais opostos entre subgrupos = {len(opostos)}: {", ".join(opostos)}')
print()
