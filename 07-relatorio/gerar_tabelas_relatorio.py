"""Gera as tabelas e os números do manuscrito (07-relatorio/relatorio.qmd) a partir dos arquivos do projeto.

USO (da raiz do projeto)
    python3 07-relatorio/gerar_tabelas_relatorio.py <pasta_saida>            # grava <pasta_saida>/<tabela>.md e numeros.json
    python3 07-relatorio/gerar_tabelas_relatorio.py <pasta_saida> <modelo> <saida.qmd>
        # além disso, troca cada linha "<!-- TABELA:nome -->" do modelo pela tabela gerada e grava o .qmd
        # modelo usado em 24/09/2026: 07-relatorio/relatorio_modelo.qmd (o texto do relatório, com os marcadores)

Só lê arquivos; não escreve em dados/, 05-decomposicao/ nem 06-analise/. Nenhum número é digitado à mão:
contagens, proporções, IC, p, g e certezas vêm de 05-decomposicao/, 04-qualidade/, 06-analise/, 07-relatorio/
e 08-revisao-humana/. Junções só por chave, id_rs, id_estudo ou chave + construto_outcome.
"""
import ast, csv, json, os, re, sys, collections

R = '.'
def ler(p):
    with open(os.path.join(R, p), encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))
def ljson(p):
    with open(os.path.join(R, p), encoding='utf-8') as f:
        return json.load(f)

# ---------- formatação pt-BR ----------
def num(x, d=2):
    if x is None or x == '':
        return 'NR'
    s = f'{float(x):,.{d}f}'
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')
def inteiro(x):
    if x in (None, '', 'NA'):
        return 'NR'
    s = f'{int(round(float(x))):,}'
    return s.replace(',', '.')
def sinal(s):
    return s.replace('-', '−')
def g_fmt(x, d=2):
    if x not in (None, '') and abs(float(x)) < 0.005:
        d = 3
    return sinal(num(x, d))
def p_fmt(p):
    if p is None or p == '':
        return 'NR'
    p = float(p)
    if p < 0.001:
        return '< 0,001'
    s = f'{p:.3f}'.rstrip('0').rstrip('.')
    return s.replace('.', ',')
def ic_fmt(ic):
    if not ic:
        return 'NR'
    return f'{num(ic[0])} a {num(ic[1])}'

ROTULO = {
    'pesquisa_pre_eleitoral': 'pesquisa pré-eleitoral', 'agregador_projecao': 'agregador ou projeção',
    'boca_de_urna': 'boca de urna', 'outro': 'apuração parcial oficial (família `outro`)',
    'apoio_ao_lider': 'apoio', 'mobilizacao': 'mobilização',
    'sem_pesquisa': 'sem pesquisa', 'outro_resultado': 'outro resultado', 'mesmo_candidato_atras': 'mesmo candidato atrás',
    'unidades_nao_expostas': 'unidades não expostas', 'antes_depois_proibicao': 'antes e depois da proibição',
    'randomizado': 'randomizado', 'nao_randomizado': 'não randomizado',
    'principal': 'principal', 'viabilidade': 'viabilidade', 'momentum': '*momentum*',
    'muito_baixa': 'muito baixa', 'baixa': 'baixa', 'moderada': 'moderada', 'alta': 'alta',
    'algumas_preocupacoes': 'algumas preocupações', 'alto': 'alto', 'baixo': 'baixo', 'grave': 'grave',
    'moderado': 'moderado', 'critico': 'crítico', 'incerto': 'incerto', 'nao_se_aplica': 'não se aplica',
    'lider': 'líder', 'azarao': 'azarão', 'segundo_viavel': 'segundo viável', 'terceiro_inviavel': 'terceiro inviável',
    'partido_abaixo_clausula': 'partido perto da cláusula', 'opcao_referendo': 'opção de referendo',
    'lider + segundo_viavel': 'líder e segundo viável',
}
def rot(x):
    return ROTULO.get(x, x.replace('_', ' '))
def comp_rot(c):
    return 'outro' if c == 'outro' else rot(c)
def fam_rot(f):
    return 'outro' if f == 'outro' else rot(f)
def dir_rot(d, construto, celula):
    pos = {'principal': '*bandwagon*', 'viabilidade': 'viabilidade', 'momentum': 'a favor', 'mobilizacao': 'mobilização'}
    neg = {'principal': '*underdog*', 'viabilidade': 'contra', 'momentum': 'contra', 'mobilizacao': 'desmobilização'}
    c = 'mobilizacao' if construto == 'mobilizacao' else celula
    return {'benefico': pos.get(c, 'positivo'), 'danoso': neg.get(c, 'negativo'), 'misto': 'misto',
            'nulo': 'nulo', 'sem_direcao': 'sem direção'}.get(d, d)
def contagem(g, construto, celula):
    c = 'mobilizacao' if construto == 'mobilizacao' else celula
    pos = {'principal': '*bandwagon*', 'viabilidade': 'viabilidade', 'momentum': 'a favor', 'mobilizacao': 'mobilização'}[c]
    neg = {'principal': '*underdog*', 'viabilidade': 'contra', 'momentum': 'contra', 'mobilizacao': 'desmobilização'}[c]
    s = f"{g['n_beneficos']} {pos}; {g['n_danosos']} {neg}"
    if g['n_mistos']:
        s += f"; {g['n_mistos']} misto"
    if g['n_nulos']:
        s += f"; {g['n_nulos']} nulo"
    if g.get('n_sem_direcao'):
        s += f"; {g['n_sem_direcao']} sem direção"
    return s
def prop_fmt(g):
    if g['proporcao_benefica'] is None:
        return 'NR'
    return f"{num(g['proporcao_benefica'])} ({ic_fmt(g['ic_proporcao'])})"
def cit(chaves):
    return '; '.join(f'@{c}' for c in chaves)

def tabela(cab, linhas, legenda, ident, larguras=None):
    out = ['| ' + ' | '.join(cab) + ' |', '|' + '---|' * len(cab)]
    for l in linhas:
        out.append('| ' + ' | '.join(str(x).replace('|', '/') for x in l) + ' |')
    attr = f'#{ident}' + (f' tbl-colwidths="[{",".join(str(x) for x in larguras)}]"' if larguras else '')
    out += ['', f': {legenda} {{{attr}}}']
    return '\n'.join(out)

# ---------- dados ----------
master = ler('05-decomposicao/fichamentos_master.csv')
M = {r['citekey']: r for r in master}
incl = ler('07-relatorio/incluidos.csv')
eleg = {r['chave']: r for r in ler('03-textos/elegibilidade_tc_final.csv')}
unicos = {r['id_rs']: r for r in ler('dados/registros_unicos.csv')}
rob = ler('04-qualidade/rob_geral.csv')
ROB = collections.defaultdict(list)
for r in rob:
    ROB[r['chave']].append(r)
efe = ler('06-analise/efeitos.csv')
PRINC = [r for r in efe if r['modelo_principal'] == 'sim']
ent_exc = {r['id_efeito']: r for r in ler('06-analise/swim_entrada_com_excluidos.csv')}
ent_pri = {r['id_efeito']: r for r in ler('06-analise/swim_entrada_principal.csv')}
cert = ler('06-analise/certeza.csv')
cert_amp = ler('06-analise/certeza_agrupamento_amplo.csv')
fonte_fora = open(os.path.join(R, '06-analise/montar_entradas_swim.py'), encoding='utf-8').read()
FORA = ast.literal_eval(re.search(r'^FORA = (\{.*?^\})', fonte_fora, re.S | re.M).group(1))
ultimo = ''
FORA_RES = {}
for k, v in FORA.items():
    if v.startswith('idem'):
        v = ultimo + (v[4:] if len(v) > 4 else '')
    else:
        ultimo = v
    FORA_RES[k] = v
swim = {n: ljson(f'06-analise/{n}/swim_resumo.json') for n in [
    'swim_principal', 'swim_sens_com_critico', 'swim_sens_icc020', 'swim_sens_agrupamento_amplo',
    'swim_sens_so_contexto_real_amplo', 'swim_sens_sem_pre2010_amplo', 'swim_sens_sem_araujo_amplo',
    'swim_sens_com_excluidos_amplo']}
dirp = ler('06-analise/swim_principal/tabelas/swim_direcao.csv')
meta = ljson('06-analise/meta_exploratoria/meta_resumo.json')
meta20 = ljson('06-analise/meta_exploratoria_icc020/meta_resumo.json')
pend = ljson('07-relatorio/_pendencias_abertas.json')
prisma = ljson('07-relatorio/prisma_contagens.json')

# relatos por estudo (id_rs -> id_estudo)
def id_estudo_chave(ch):
    e = eleg.get(ch)
    return unicos[e['id_rs']]['id_estudo'] if e and e['id_rs'] in unicos else None
ANO = {r['chave']: r['ano'] for r in incl}
REL = collections.defaultdict(list)
for r in incl:
    REL[id_estudo_chave(r['chave'])].append(r['chave'])

# classe de desenho por chave + construto, lida das saídas da SWiM (classificação do _cli.R)
CLASSE = {}
for n in ('swim_sens_com_excluidos_amplo', 'swim_sens_com_critico', 'swim_principal'):
    for g in swim[n]['grupos']:
        for ch in g['estudos'] + g.get('excluidos_rob_critico', {}).get('estudos', []):
            CLASSE.setdefault((ch, g['construto_outcome']), g['classe_desenho'])

# ---------- características ----------
DESENHO = {'lab_preferencias_induzidas': 'laboratório, preferências induzidas',
           'lab_candidatos_reais': 'laboratório, candidatos reais', 'survey_experiment': 'experimento de survey',
           'experimento_natural': 'experimento natural', 'experimento_campo': 'experimento de campo',
           'painel_individual': 'painel individual'}
def pais_fmt(ch):
    raw = M[ch]['pais_estudo']
    if raw.strip() == '999':
        return 'NR'
    partes = [re.split(r' — | \(', p.strip())[0].strip() for p in raw.split(' ; ')]
    partes = ['Países Baixos' if p == 'Holanda' else p for p in partes]
    if len(partes) > 5:
        br = [p for p in partes if p in ('Brazil', 'Brasil')]
        return f'{len(partes)} países, entre eles o Brasil' if br else f'{len(partes)} países'
    return '; '.join(partes)
def desenho_fmt(ch):
    d = M[ch]['desenho_fino']
    for k, v in DESENHO.items():
        if d.startswith(k):
            return v + (' (artigo 2 da tese)' if ch == 'Freden2016b' else '')
    esp = {'Alabrese2024a': 'painel de distritos com data de entrevista quase aleatória',
           'Gasperoni2015a': 'campanha simulada online (DPTE)',
           'Lago2015': f'corte transversal agregado de {pais_fmt("Lago2015").split()[0]} países',
           'Meffert2012a': 'três desenhos (laboratório induzido, laboratório real, vinheta)',
           'Unkelbach2022a': '*rolling cross-section* com pesquisas do dia anterior'}
    return esp.get(ch, 'outro')
def desenho_cod(ch):
    d = M[ch]['desenho_fino']
    for k in DESENHO:
        if d.startswith(k):
            return k
    return 'outro'
def fam_cod(ch):
    f = M[ch]['familia_intervencao']
    return 'apuracao_parcial' if f.startswith('outro') else f
FAM_TXT = {'pesquisa_pre_eleitoral': 'pesquisa pré-eleitoral', 'agregador_projecao': 'agregador ou projeção',
           'boca_de_urna': 'boca de urna', 'apuracao_parcial': 'apuração parcial oficial'}
REG_TXT = {'outro': 'outras', 'america_latina': 'América Latina', 'brasil': 'Brasil', '999': 'NR'}
def reg_fmt(ch):
    return ', '.join(REG_TXT.get(x.strip(), x.strip()) for x in M[ch]['regiao'].split('+'))
ELEI = {'candidato_partido': 'candidatos ou partidos', 'simulada_abstrata': 'simulada abstrata', 'referendo': 'referendo'}
REAL = {'real': 'real', 'induzido': 'induzido', 'hipotetico': 'hipotético'}
def constr_fmt(ch):
    c = M[ch]['construto_outcome']
    return {'apoio_ao_lider': 'apoio', 'mobilizacao': 'mobilização', 'apoio_ao_lider + mobilizacao': 'apoio e mobilização'}.get(c, c)
FERR = {'rob2': 'RoB 2', 'robins_i': 'ROBINS-I', 'epoc': 'EPOC'}
princ_por_chave = collections.defaultdict(list)
for r in PRINC:
    princ_por_chave[r['chave']].append(r)
efe_chaves = {r['chave'] for r in efe}
def rob_fmt(ch):
    rs = ROB.get(ch)
    if not rs:
        return 'não avaliado (sem efeito principal extraído)'
    if len(rs) == 1:
        r = rs[0]
        extra = f" ({rot(r['construto_outcome'])})" if '+' in M[ch]['construto_outcome'] else ''
        return f"{FERR[r['ferramenta']]}: {rot(r['rob_geral'])}{extra}"
    return '; '.join(f"{FERR[r['ferramenta']]}: {rot(r['rob_geral'])} ({rot(r['construto_outcome'])})" for r in rs)

def t_caracteristicas():
    linhas = []
    for ch in sorted(M, key=str.lower):
        ide = id_estudo_chave(ch)
        outros = sorted(c for c in REL.get(ide, []) if c != ch)
        est = f'@{ch}' + (f" ({'; '.join('@' + c for c in outros)})" if outros else '')
        fam = FAM_TXT[fam_cod(ch)]
        linhas.append([est, ANO.get(ch, 'NR'), desenho_fmt(ch), fam, f'{pais_fmt(ch)} ({reg_fmt(ch)})',
                       ELEI.get(M[ch]['tipo_eleicao'], M[ch]['tipo_eleicao']), REAL.get(M[ch]['realismo_contexto'], M[ch]['realismo_contexto']),
                       constr_fmt(ch), rob_fmt(ch)])
    return tabela(['Estudo (relatos adicionais)', 'Ano', 'Desenho', 'Exposição', 'País (região)', 'Eleição', 'Contexto', 'Construto', 'Risco de viés geral'],
                  linhas, 'Características dos estudos incluídos (`05-decomposicao/fichamentos_master.csv`; ano do relato principal em `07-relatorio/incluidos.csv`; risco de viés em `04-qualidade/rob_geral.csv`). Construto: desfechos extraídos do estudo. Risco de viés geral por resultado (ferramenta: julgamento), nenhum validado por humano.',
                  'tbl-caracteristicas', [15, 5, 15, 10, 13, 9, 7, 9, 17])

# ---------- risco de viés ----------
def cons(f):
    d = collections.defaultdict(dict)
    for r in ler(f'04-qualidade/rob_{f}_consenso.csv'):
        v = rot(r['julgamento_consenso'])
        if r['julgamento_a'] != r['julgamento_b']:
            v += '†'
        d[(r['chave'], r['construto_outcome'])][r['dominio']] = v
    return d
GERAL = {(r['chave'], r['construto_outcome'], r['ferramenta']): rot(r['rob_geral']) for r in rob}
def t_rob(f, doms, cab, legenda, ident):
    d = cons(f)
    linhas = []
    for (ch, co) in sorted(d, key=lambda x: (x[0].lower(), x[1])):
        linhas.append([f'@{ch}', rot(co)] + [d[(ch, co)].get(k, 'não se aplica') for k in doms] + [GERAL[(ch, co, f)]])
    return tabela(['Estudo', 'Construto'] + cab + ['Geral'], linhas, legenda, ident)

# ---------- estudos individuais ----------
def outra_medida(r, e):
    p = []
    if r['efeito_pp']:
        p.append(f"{sinal(num(r['efeito_pp']))} p.p.")
    if r['p0'] and r['p1']:
        p.append(f"p0 = {num(r['p0'])}; p1 = {num(r['p1'])}")
    elif r['p0']:
        p.append(f"p0 = {num(r['p0'])}")
    if r['beta'] and not r['yi'] and not r['efeito_pp']:
        p.append(f"β = {sinal(num(r['beta'], 3))}")
    if r['aproximado'] == '1':
        p.append('conversão aproximada')
    if e and e.get('beta_proxy_sinal'):
        p.append(f"sinal por {e['beta_proxy_sinal'].replace('efeito_pp', 'efeito em p.p.').replace('ln(or_)', 'ln(OR)')}")
    return '; '.join(p) if p else 'NR'
def na_contagem(r, e):
    motivos = []
    if e and e.get('fora_contagem'):
        motivos.append('fora da contagem')
    if r['rob_geral'] == 'critico':
        motivos.append('risco crítico')
    if not motivos and e and e['celula_alvo'] == 'outro':
        motivos.append('célula outro')
    return 'sim' if not motivos else 'não (' + '; '.join(motivos) + ')'
def g_ep(r, e):
    if not r['yi']:
        return 'NR'
    s = f"{g_fmt(r['yi'])} ({num(r['sei'], 3)})"
    if e and e.get('nulo_por_delta'):
        s += '; nulo por ±δ'
    return s
def t_individuais():
    linhas = []
    for r in sorted(PRINC, key=lambda r: (r['chave'].lower(), r['id_efeito'])):
        e = ent_exc.get(r['id_efeito'])
        cel = e['celula_alvo'] if e else 'NR'
        linhas.append([f"@{r['chave']}", r['id_efeito'].split('-')[-1], rot(r['construto_outcome']), 'outro alvo' if cel == 'outro' else rot(cel),
                       comp_rot(r['comparador_tipo']), g_ep(r, e), outra_medida(r, e), na_contagem(r, e)])
    return tabela(['Estudo', 'Efeito', 'Desfecho', 'Célula de alvo', 'Comparador', 'g (EP)', 'Outra medida', 'Na contagem?'], linhas,
                  'Efeitos principais por estudo (`06-analise/efeitos.csv`, `modelo_principal = sim`; célula e situação na contagem em `06-analise/swim_entrada_com_excluidos.csv`). g de Hedges alinhado: positivo = *bandwagon*, viabilidade, *momentum* a favor ou mobilização. NR = não calculado ou não relatado; nulo por ±δ = IC 95% inteiro dentro de ±δ.',
                  'tbl-individuais', [14, 6, 9, 10, 13, 14, 24, 10])

# ---------- SWiM principal e certeza ----------
def chave_cert(r):
    return (r['familia_intervencao'], r['construto_outcome'], r['comparador_tipo'], r['celula_alvo'], r['classe_desenho'])
CERT = {chave_cert(r): r for r in cert}
def chave_g(g):
    return (g['familia_intervencao'], g['construto_outcome'], g['comparador_tipo'], g['celula_alvo'], g['classe_desenho'])
ORDEM_FAM = {'pesquisa_pre_eleitoral': 0, 'agregador_projecao': 1, 'boca_de_urna': 2, 'outro': 3}
ORDEM_CEL = {'principal': 0, 'viabilidade': 1, 'momentum': 2, 'mobilizacao': 3}
def ordem_g(g):
    return (ORDEM_FAM[g['familia_intervencao']], g['construto_outcome'], ORDEM_CEL[g['celula_alvo']], g['comparador_tipo'], g['classe_desenho'])
def t_swim():
    linhas = []
    for g in sorted(swim['swim_principal']['grupos'], key=ordem_g):
        crit = g['excluidos_rob_critico']['estudos']
        est = cit(g['estudos']) if g['estudos'] else 'nenhum'
        if crit:
            est += f' (fora, risco crítico: {cit(crit)})'
        c = CERT.get(chave_g(g))
        linhas.append([fam_rot(g['familia_intervencao']), f"{rot(g['construto_outcome'])} ({rot(g['celula_alvo'])})", comp_rot(g['comparador_tipo']),
                       rot(g['classe_desenho']), est, contagem(g, g['construto_outcome'], g['celula_alvo']) if g['k_estudos'] else 'nenhum estudo',
                       prop_fmt(g), p_fmt(g['p_sinal']), rot(c['certeza']) if c else 'não julgada (célula vazia)'])
    return tabela(['Exposição', 'Desfecho (célula de alvo)', 'Comparador', 'Classe', 'Estudos', 'Direções', 'Proporção (IC 95%)', 'p (sinal)', 'Certeza'], linhas,
                  'SWiM principal por célula do protocolo (`06-analise/swim_principal/swim_resumo.json`, sem risco crítico). Proporção = estudos na direção positiva entre os estudos com direção definida (nulos e mistos fora do denominador), com IC 95% de Clopper-Pearson; p do teste de sinal binomial exato bilateral. Certeza de `06-analise/certeza.csv`, sobre a direção, rascunho de IA não validado.',
                  'tbl-swim', [11, 12, 11, 9, 20, 14, 11, 5, 7])

def t_viab():
    linhas = []
    dir_est = {(r['chave'], r['grupo'].split(' | ')[3]): r['direcao'] for r in dirp}
    for r in sorted(PRINC, key=lambda r: (ORDEM_CEL.get(ent_exc.get(r['id_efeito'], {}).get('celula_alvo', 'x'), 9), r['chave'].lower(), r['id_efeito'])):
        e = ent_exc.get(r['id_efeito'])
        if not e or e['celula_alvo'] not in ('viabilidade', 'momentum'):
            continue
        classe = CLASSE.get((r['chave'], r['construto_outcome']), 'NR')
        k = (r['familia_intervencao'], r['construto_outcome'], r['comparador_tipo'], e['celula_alvo'], classe)
        c = CERT.get(k)
        if e.get('fora_contagem'):
            situ = 'fora da contagem principal (sem certeza)'
        elif r['rob_geral'] == 'critico':
            situ = 'fora da análise principal (risco crítico)'
        else:
            situ = rot(c['certeza']) if c else 'NR'
        d = dir_est.get((r['chave'], e['celula_alvo']))
        linhas.append([f"@{r['chave']}", r['id_efeito'].split('-')[-1], rot(e['celula_alvo']), rot(r['alvo_efeito']), comp_rot(r['comparador_tipo']),
                       rot(classe), g_ep(r, e), dir_rot(d, r['construto_outcome'], e['celula_alvo']) if d else 'NR', rot(r['rob_geral']), situ])
    return tabela(['Estudo', 'Efeito', 'Célula', 'Alvo', 'Comparador', 'Classe', 'g (EP)', 'Direção do estudo', 'Risco de viés', 'Certeza da célula'], linhas,
                  'Efeitos principais de viabilidade e de *momentum* (achados secundários). Positivo = mais apoio à opção mostrada como viável, menos à mostrada como inviável ou abaixo da cláusula, ou mais apoio ao partido mostrado ganhando apoio. Direção do estudo na SWiM principal (NR quando o estudo não entra nela).',
                  'tbl-viabilidade', [13, 5, 9, 11, 11, 9, 11, 9, 10, 12])

def t_fora():
    linhas = []
    for r in sorted(PRINC, key=lambda r: (r['chave'].lower(), r['id_efeito'])):
        e = ent_exc.get(r['id_efeito'])
        if e and e.get('fora_contagem'):
            linhas.append([f"@{r['chave']}", r['id_efeito'].split('-')[-1], rot(r['construto_outcome']), g_ep(r, e) if r['yi'] else outra_medida(r, e),
                           FORA[r['id_efeito']].replace('idem', 'idem à linha anterior', 1) if FORA[r['id_efeito']].startswith('idem') else FORA[r['id_efeito']]])
    return tabela(['Estudo', 'Efeito', 'Desfecho', 'g (EP) ou outra medida', 'Motivo registrado para ficar fora do teste de sinal'], linhas,
                  'Efeitos principais fora da contagem e motivo registrado no dicionário `FORA` de `06-analise/montar_entradas_swim.py` (versão depois das arbitragens de 23/09/2026).',
                  'tbl-fora', [14, 6, 9, 16, 55])

SENS = [('swim_sens_agrupamento_amplo', 'Agrupamento amplo (descritivo, *post hoc*)'),
        ('swim_sens_so_contexto_real_amplo', 'Só contexto real'),
        ('swim_sens_sem_pre2010_amplo', 'Sem dados anteriores a 2010'),
        ('swim_sens_sem_araujo_amplo', 'Sem @Araujo2021a'),
        ('swim_sens_com_excluidos_amplo', 'Com os efeitos fora da contagem')]
CERT_AMP = {(r['construto_outcome'], r['celula_alvo'], r['classe_desenho']): r for r in cert_amp}
def t_sens():
    linhas = []
    for n, nome in SENS:
        for g in sorted(swim[n]['grupos'], key=lambda g: (g['construto_outcome'], ORDEM_CEL.get(g['celula_alvo'], 9), g['classe_desenho'])):
            if g['celula_alvo'] == 'outro':
                cel = 'outro alvo'
            else:
                cel = rot(g['celula_alvo'])
            est = cit(g['estudos']) if g['estudos'] else 'nenhum'
            crit = g.get('excluidos_rob_critico', {}).get('estudos', [])
            if crit:
                est += f' (fora, risco crítico: {cit(crit)})'
            dirs = contagem(g, g['construto_outcome'], g['celula_alvo']) if g['celula_alvo'] != 'outro' else f"{g['n_beneficos']} positivo; {g['n_danosos']} negativo"
            if not g['k_estudos']:
                dirs = 'nenhum estudo'
            c = CERT_AMP.get((g['construto_outcome'], g['celula_alvo'], g['classe_desenho'])) if n == 'swim_sens_agrupamento_amplo' else None
            linhas.append([nome, f"{rot(g['construto_outcome'])} ({cel})", rot(g['classe_desenho']), est, dirs, prop_fmt(g), p_fmt(g['p_sinal']),
                           rot(c['certeza']) if c else 'sem GRADE próprio'])
    return tabela(['Análise', 'Desfecho (célula)', 'Classe', 'Estudos', 'Direções', 'Proporção (IC 95%)', 'p (sinal)', 'Certeza'], linhas,
                  'Análises de sensibilidade da SWiM no agrupamento amplo (construto × célula de alvo × classe; saídas em `06-analise/swim_sens_*_amplo/`). O agrupamento amplo junta famílias e comparadores que o protocolo manda separar e é descritivo, decidido depois de ver os dados (Emenda 5). Certeza só para o agrupamento amplo sem outras mudanças (`06-analise/certeza_agrupamento_amplo.csv`).',
                  'tbl-sens', [15, 13, 9, 25, 14, 11, 5, 8])

# ---------- Brasil e América Latina ----------
def t_regional():
    regs = [ch for ch in sorted(M) if any(x.strip() in ('brasil', 'america_latina') for x in M[ch]['regiao'].split('+'))]
    linhas = []
    for ch in regs:
        pr = princ_por_chave.get(ch, [])
        efs = '; '.join(f"{r['id_efeito'].split('-')[-1]}: {g_ep(r, ent_exc.get(r['id_efeito']))}" + (f" ({sinal(num(r['efeito_pp']))} p.p.)" if r['efeito_pp'] else '') for r in pr)
        situ = []
        for r in pr:
            e = ent_exc.get(r['id_efeito'])
            if e and e.get('fora_contagem'):
                situ.append('fora da contagem principal: ' + FORA_RES[r['id_efeito']])
        classe = CLASSE.get((ch, pr[0]['construto_outcome'])) if pr else None
        k = (pr[0]['familia_intervencao'], pr[0]['construto_outcome'], pr[0]['comparador_tipo'], ent_exc[pr[0]['id_efeito']]['celula_alvo'], classe) if pr else None
        c = CERT.get(k) if k else None
        cert_txt = rot(c['certeza']) if c and not situ else 'sem certeza atribuída'
        linhas.append([f'@{ch}', f"{pais_fmt(ch)}; ano da eleição codificado: {M[ch]['ano_eleicao'] if M[ch]['ano_eleicao'] != '999' else 'NR'}",
                       FAM_TXT[fam_cod(ch)], efs or 'NR', f"{rob_fmt(ch)}; certeza: {cert_txt}" + (f"; {situ[0]}" if situ else '')])
    return tabela(['Estudo', 'País e eleição', 'Exposição', 'Efeito principal, g (EP)', 'Risco de viés; certeza da célula'], linhas,
                  'Estudos com `regiao` igual a Brasil ou América Latina no *master* de extração.', 'tbl-regional', [13, 20, 14, 23, 30])

# ---------- resumo dos achados (GRADE) ----------
DOMS = ['Risco de viés', 'Inconsistência', 'Indireção', 'Imprecisão', 'Viés de publicação']
def rebaix(j):
    partida = re.search(r'Ponto de partida: (alta|baixa)', j)
    out = []
    for d in DOMS:
        m = re.search(re.escape(d) + r': (rebaixad[oa]) (\d) níve', j)
        if m:
            out.append(f'{d.lower() if d != "Risco de viés" else "risco de viés"} −{m.group(2)}')
    return ('; '.join(out) if out else 'nenhum') + f" (partida {partida.group(1) if partida else 'NR'})"
NAM = {}
for r in dirp:
    NAM[r['chave'], r['grupo']] = r['n_amostra']
def t_sof():
    linhas = []
    gm = {chave_g(g): g for g in swim['swim_principal']['grupos']}
    for k in sorted(CERT, key=lambda k: (ORDEM_FAM[k[0]], k[1], ORDEM_CEL[k[3]], k[2], k[4])):
        c = CERT[k]; g = gm[k]
        grupo = g['grupo']
        ests = '; '.join(f"@{ch} ({inteiro(NAM.get((ch, grupo)))})" for ch in g['estudos'])
        d = contagem(g, k[1], k[3]) + (f" ({prop_fmt(g).replace(' (', '; ').rstrip(')')})" if g['proporcao_benefica'] is not None else '')
        linhas.append([f"{fam_rot(k[0])}; {rot(k[1])} ({rot(k[3])}); {comp_rot(k[2])}; {rot(k[4])}", ests, d, rot(c['certeza']), rebaix(c['justificativa'])])
    ga = {(g['construto_outcome'], g['celula_alvo'], g['classe_desenho']): g for g in swim['swim_sens_agrupamento_amplo']['grupos']}
    for k in sorted(CERT_AMP, key=lambda k: (k[0], ORDEM_CEL[k[1]], k[2])):
        c = CERT_AMP[k]; g = ga[k]
        ests = '; '.join(f'@{ch}' for ch in g['estudos'])
        d = contagem(g, k[0], k[1]) + (f" ({prop_fmt(g).replace(' (', '; ').rstrip(')')})" if g['proporcao_benefica'] is not None else '')
        linhas.append([f"agrupamento amplo, *post hoc*; {rot(k[0])} ({rot(k[1])}); vários; {rot(k[2])}", ests, d, rot(c['certeza']), rebaix(c['justificativa'])])
    return tabela(['Célula (exposição; desfecho; comparador; classe)', 'Estudos (n de cada estudo, unidade própria)', 'Direção (proporção; IC 95%)', 'Certeza', 'Rebaixamentos (ponto de partida)'], linhas,
                  'Resumo dos achados (GRADE, rascunho de IA não validado; `06-analise/certeza.csv` e `06-analise/certeza_agrupamento_amplo.csv`). n do efeito principal na unidade própria de cada estudo (`06-analise/swim_principal/tabelas/swim_direcao.csv`); no agrupamento amplo, os n são os mesmos das células do protocolo. Com SWiM, a certeza qualifica a direção, não a magnitude.',
                  'tbl-sof', [24, 26, 20, 8, 22])

# ---------- pendências ----------
def t_pend():
    readme = open(os.path.join(R, '08-revisao-humana/README.md'), encoding='utf-8').read()
    pac = {}
    for l in readme.splitlines():
        m = re.match(r'\| \d+ \| (P\d+)(?: e (P\d+))? \| [^|]+ \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', l)
        if m:
            for p in (m.group(1), m.group(2)):
                if p:
                    pac[p] = (m.group(3).strip(), m.group(4).strip(), m.group(5).strip())
    linhas = []
    for p in pend['pendencias']:
        a = pac.get(p['id'], ('NR', 'NR', 'NR'))
        a = tuple('seção de portões do README da pasta' if x == 'seção abaixo' else x for x in a)
        linhas.append([p['id'], p['tipo'], p['etapa'], p['portao'] or 'nenhum', p['n'] if p['n'] is not None else 'não se aplica', p['descricao'], a[1], a[2]])
    return tabela(['Id', 'Tipo', 'Etapa', 'Portão', 'N', 'Descrição (registrada no estado)', 'Pacote em `08-revisao-humana/`', 'Esforço estimado'], linhas,
                  f"Pendências humanas abertas ({pend['abertas']}), copiadas de `07-relatorio/_pendencias_abertas.json`; pacote e esforço de `08-revisao-humana/README.md`. As descrições são as registradas quando cada pendência foi aberta e podem citar contagens anteriores (por exemplo, P001 cita a string v4, substituída pela v5).",
                  'tbl-pendencias', [5, 10, 10, 6, 5, 40, 14, 10])

# ---------- números para o texto ----------
def numeros():
    n = {}
    n['estudos'] = len(M); n['relatos'] = len(incl)
    n['estudos_com_efeitos'] = len(efe_chaves); n['efeitos'] = len(efe)
    n['efeitos_principais'] = len(PRINC); n['estudos_com_principal'] = len(princ_por_chave)
    n['sem_principal'] = sorted(set(M) - set(princ_por_chave))
    n['desenho'] = collections.Counter(desenho_cod(ch) for ch in M)
    n['familia'] = collections.Counter(fam_cod(ch) for ch in M)
    n['realismo'] = collections.Counter(M[ch]['realismo_contexto'] for ch in M)
    n['eleicao'] = collections.Counter(M[ch]['tipo_eleicao'] for ch in M)
    n['construto'] = collections.Counter(M[ch]['construto_outcome'] for ch in M)
    n['regiao'] = collections.Counter(M[ch]['regiao'] for ch in M)
    anos = [int(ANO[ch]) for ch in M if ANO.get(ch, '').isdigit()]
    n['ano_min'], n['ano_max'] = min(anos), max(anos)
    n['rob_resultados'] = len(rob); n['rob_estudos'] = len({r['chave'] for r in rob})
    n['rob_por_ferr'] = {f: dict(collections.Counter(r['rob_geral'] for r in rob if r['ferramenta'] == f)) for f in FERR}
    c2 = ler('04-qualidade/rob_rob2_consenso.csv')
    n['rob2_D5_algumas'] = sum(1 for r in c2 if r['dominio'] == 'D5' and r['julgamento_consenso'] == 'algumas_preocupacoes')
    ci = ler('04-qualidade/rob_robins_i_consenso.csv')
    n['robins_D1_grave_critico'] = sum(1 for r in ci if r['dominio'] == 'D1' and r['julgamento_consenso'] in ('grave', 'critico'))
    tot = seg = collections.Counter()
    tot = collections.Counter(); seg = collections.Counter()
    for f in FERR:
        for r in ler(f'04-qualidade/rob_{f}_consenso.csv'):
            tot[r['resolvido_por'].split(':')[0]] += 1
            if r['julgamento_a'] != r['julgamento_b']:
                cc = r['julgamento_consenso']
                seg['A' if cc == r['julgamento_a'] else 'B' if cc == r['julgamento_b'] else 'outro'] += 1
    n['rob_dominios'] = dict(tot); n['arbitro_segue'] = dict(seg)
    n['swim_principal_grupos'] = len(swim['swim_principal']['grupos'])
    n['swim_principal_celulas_com_estudo'] = sum(1 for g in swim['swim_principal']['grupos'] if g['k_estudos'])
    n['swim_principal_estudos'] = sorted({ch for g in swim['swim_principal']['grupos'] for ch in g['estudos']})
    n['n_swim_principal_estudos'] = len(n['swim_principal_estudos'])
    n['criticos'] = sorted({r['chave'] for r in rob if r['rob_geral'] == 'critico'})
    n['fora_estudos_so_fora'] = sorted({r['chave'] for r in PRINC if ent_exc.get(r['id_efeito'], {}).get('fora_contagem')} - set(n['swim_principal_estudos']) - set(n['criticos']))
    n['certeza_contagem'] = dict(collections.Counter(r['certeza'] for r in cert))
    n['certeza_amplo_contagem'] = dict(collections.Counter(r['certeza'] for r in cert_amp))
    # ICC 0,20 igual à principal?
    def assin(nm):
        return sorted((g['grupo'], g['n_beneficos'], g['n_danosos'], g['n_mistos'], g['n_nulos']) for g in swim[nm]['grupos'])
    n['icc020_igual_principal'] = assin('swim_principal') == assin('swim_sens_icc020')
    gm = meta['grupos'][0]; r = gm['resultado']
    n['meta'] = {'k_estudos': gm['k_estudos'], 'k_efeitos': gm['k_efeitos'], 'estudos': gm['estudos'], 'modelo': r['modelo'],
                 'g': g_fmt(r['estimativa']), 'ic': [g_fmt(x) for x in r['ic']], 'p': p_fmt(r['p']), 'gl': num(r['gl']),
                 'tau2': num(r['tau2']), 'I2': num(r['I2'], 0), 'pi': [g_fmt(x) for x in r['pi']], 'delta': num(meta['parametros']['delta'], 4),
                 'loo': [g_fmt(gm['sensibilidade']['leave_one_out']['estimativa_min']), g_fmt(gm['sensibilidade']['leave_one_out']['estimativa_max'])],
                 'loo_muda': gm['sensibilidade']['leave_one_out']['estudos_que_mudam_conclusao'],
                 'rho': [(x['rho'], g_fmt(x['estimativa']), [g_fmt(y) for y in x['ic']]) for x in gm['sensibilidade']['rho']]}
    r2 = meta20['grupos'][0]['resultado']
    n['meta_icc020'] = {'g': g_fmt(r2['estimativa']), 'ic': [g_fmt(x) for x in r2['ic']], 'gl': num(r2['gl'])}
    loo = ler('06-analise/meta_exploratoria/tabelas/loo_01_pesquisa_pre_eleitoral_apoio_ao_lider_sem_pesquisa_randomiza.csv')
    n['meta_loo'] = [(x['estudo_removido'], g_fmt(x['estimativa']), g_fmt(x['ic_inf']), g_fmt(x['ic_sup'])) for x in loo]
    for nome in ('meta_mesmo_candidato', 'meta_mesmo_candidato_icc020'):
        mm = ljson(f'06-analise/{nome}/meta_resumo.json'); gm2 = mm['grupos'][0]; r3 = gm2['resultado']
        n[nome] = {'k_estudos': gm2['k_estudos'], 'k_efeitos': gm2['k_efeitos'], 'estudos': gm2['estudos'], 'delta': num(mm['parametros']['delta'], 3),
                   'g': g_fmt(r3['estimativa']), 'ic': [g_fmt(x) for x in r3['ic']], 'p': p_fmt(r3['p']), 'gl': num(r3['gl']),
                   'rve_confiavel': r3['rve_confiavel'], 'tau2': num(r3['tau2']), 'I2': num(r3['I2'], 0), 'pi': [g_fmt(x) for x in r3['pi']],
                   'avisos': gm2['comparabilidade']['avisos'],
                   'loo': [(x['estudo_removido'], g_fmt(x['estimativa']), g_fmt(x['ic_inf']), g_fmt(x['ic_sup'])) for x in ler(gm2['sensibilidade']['leave_one_out']['tabela'])],
                   'rho': [(x['rho'], g_fmt(x['estimativa']), [g_fmt(y) for y in x['ic']]) for x in gm2['sensibilidade']['rho']]}
    n['voto_obrig_mob_sim'] = [ch for ch in M if 'mobilizacao' in M[ch]['construto_outcome'] and M[ch]['voto_obrigatorio'].lower().startswith('sim')]
    n['pendencias'] = pend['abertas']
    return n

if __name__ == '__main__':
    saida = sys.argv[1]
    os.makedirs(saida, exist_ok=True)
    T = {'caracteristicas': t_caracteristicas(),
         'rob2': t_rob('rob2', ['D1', 'D1b', 'D2', 'D3', 'D4', 'D5'],
                       ['D1 randomização', 'D1b recrutamento (conglomerado)', 'D2 desvios', 'D3 dados faltantes', 'D4 mensuração', 'D5 relato seletivo'],
                       'RoB 2 por domínio (consenso). † = domínio em desacordo entre os avaliadores de IA A e B, com consenso proposto pelo árbitro de IA (`claude-opus-5-5`); nenhum julgamento validado por humano (Emenda 6a).', 'tbl-rob2'),
         'robins': t_rob('robins_i', ['D1', 'D2', 'D3', 'D4', 'D5', 'D6'],
                         ['D1 confundimento', 'D2 classificação da exposição', 'D3 seleção', 'D4 dados faltantes', 'D5 mensuração', 'D6 relato seletivo'],
                         'ROBINS-I V2 por domínio (consenso). † como na tabela anterior.', 'tbl-robins'),
         'epoc': t_rob('epoc', ['cg_sequencia_aleatoria', 'cg_ocultacao_alocacao', 'cg_caracteristicas_base', 'cg_linha_base_outcome', 'cg_dados_incompletos',
                                'cg_conhecimento_alocacao', 'cg_contaminacao', 'cg_relato_seletivo', 'cg_outros_riscos', 'its_intervencao_independente',
                                'its_forma_efeito_pre_especificada', 'its_coleta_nao_afetada', 'its_conhecimento_alocacao', 'its_dados_incompletos',
                                'its_relato_seletivo', 'its_outros_riscos'],
                       ['GC seq.', 'GC ocult.', 'GC caract. base', 'GC desfecho base', 'GC dados incompl.', 'GC conhec.', 'GC contam.', 'GC relato sel.', 'GC outros',
                        'ITS indep.', 'ITS forma pré-esp.', 'ITS coleta', 'ITS conhec.', 'ITS dados incompl.', 'ITS relato sel.', 'ITS outros'],
                       'EPOC por critério (consenso). GC = critérios para desenho com grupo controle; ITS = série temporal interrompida. Sequência aleatória e ocultação da alocação ficam fora do geral (Emenda 4a). † como nas tabelas anteriores.', 'tbl-epoc'),
         'individuais': t_individuais(), 'swim': t_swim(), 'viabilidade': t_viab(), 'fora': t_fora(), 'sens': t_sens(),
         'regional': t_regional(), 'sof': t_sof(), 'pendencias': t_pend()}
    for k, v in T.items():
        open(os.path.join(saida, f'{k}.md'), 'w', encoding='utf-8').write(v + '\n')
    json.dump(numeros(), open(os.path.join(saida, 'numeros.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
    if len(sys.argv) == 4:
        modelo = open(sys.argv[2], encoding='utf-8').read()
        def troca(m):
            return T[m.group(1)]
        final = re.sub(r'^<!-- TABELA:(\w+) -->$', troca, modelo, flags=re.M)
        faltam = re.findall(r'<!-- TABELA:(\w+) -->', final)
        if faltam:
            sys.exit(f'marcadores sem tabela: {faltam}')
        open(sys.argv[3], 'w', encoding='utf-8').write(final)
        print('gravado', sys.argv[3])
