"""Monta as entradas da SWiM a partir de 06-analise/efeitos.csv (saída de efeitos.R).

USO
    python3 06-analise/montar_entradas_swim.py

Decisões (Emenda 5, 00-protocolo/emendas.md):
- celula_alvo: principal (líder, azarão, opção de referendo), viabilidade (segundo viável, terceiro
  inviável, partido perto da cláusula), momentum (ganho ou perda sem posição), mobilizacao.
- FORA: efeitos principais que não estimam o contraste da exposição (motivo por linha); vão para a
  síntese narrativa e para a sensibilidade `com_excluidos`.
- Nulo por ±δ: efeito principal com IC95 inteiro dentro de ±δ recebe yi = 0 (o swim.R lê como nulo).
- Sinal sem t/β/r: β recebe efeito_pp, p1 − p0 ou ln(OR), só para o sinal (coluna beta_proxy_sinal).
"""
import csv, math, json
DELTA = {'apoio_ao_lider': 0.044, 'mobilizacao': 0.046}
FORA = {
 'Lammers2022a-E01': 'd do modo de raciocínio sob exposição, não da exposição (notas de extração)',
 'Lammers2022a-E03': 'idem',
 'Gandhi2019-E01': 'interação tripla: diferença de efeito entre apoiadores (moderador não atribuído)',
 'Gandhi2019-E03': 'idem',
 'Fichnova2015a-E01': 'R de Spearman entre rankings (7 candidatos), sem grupo de comparação',
 'Fichnova2015a-E05': 'idem',
 'Klor2017a-E01': 'coeficiente de pertencer ao time maior sobre a decisão de votar (não é apoio ao líder nem contraste de exposição)',
 'Urminsky2019-E01': 'contraste de formato da mesma previsão (chance × margem), não exposição × não exposição',
 'Bursztyn2023a-E01': 'interação dia após a pesquisa × proximidade ex ante (moderador contínuo)',
 'Bursztyn2023a-E17': 'interação proximidade × apoio estimado ao lado atrás (moderador contínuo)',
 'Alabrese2024a-E002': 'interação margem nacional × segurança local (exposição contínua, estimando outro)',
 'Alabrese2024a-E129': 'interação da posição nacional com a posição local (moderador contínuo)',
 'Meffert2011-E01': 'voto insincero com alvos opostos agregados (sem posição única do alvo)',
 'Geers2018-E01': 'β = −30,8 implausível para exposição contínua; conferência humana pendente',
}
def cel(r):
    if r['construto_outcome'] == 'mobilizacao': return 'mobilizacao'
    a = r['alvo_efeito']
    if a in ('lider', 'azarao', 'opcao_referendo'): return 'principal'
    if a in ('segundo_viavel', 'terceiro_inviavel', 'partido_abaixo_clausula'): return 'viabilidade'
    return 'momentum' if r['chave'] == 'Dahlgaard2016a' else 'outro'
rows = list(csv.DictReader(open('06-analise/efeitos.csv', encoding='utf-8')))
campos = list(rows[0].keys()) + ['celula_alvo', 'beta_proxy_sinal', 'nulo_por_delta', 'fora_contagem']
for r in rows:
    r['celula_alvo'] = cel(r); r['beta_proxy_sinal'] = ''; r['nulo_por_delta'] = ''; r['fora_contagem'] = FORA.get(r['id_efeito'], '')
    if not (r['yi'] or r['beta'] or r['t'] or r['r'] or (r['m1'] and r['m2'])):
        v = None
        try:
            if r['efeito_pp']: v, s = float(r['efeito_pp']), 'efeito_pp'
            elif r['p1'] and r['p0']: v, s = float(r['p1']) - float(r['p0']), 'p1-p0'
            elif r['or_']: v, s = math.log(float(r['or_'])), 'ln(or_)'
        except ValueError: v = None
        if v: r['beta'] = repr(round(v, 6)); r['beta_proxy_sinal'] = s
    if r['yi'] and r['sei'] and r['modelo_principal'] == 'sim':
        y, se, d = float(r['yi']), float(r['sei']), DELTA[r['construto_outcome']]
        if -d <= y - 1.96 * se and y + 1.96 * se <= d:
            r['nulo_por_delta'] = f'IC [{y-1.96*se:.4f}; {y+1.96*se:.4f}] dentro de ±{d}'; r['yi'] = '0'
def gravar(nome, dados):
    w = csv.DictWriter(open(f'06-analise/{nome}.csv', 'w', encoding='utf-8', newline=''), fieldnames=campos); w.writeheader(); w.writerows(dados)
    return len(dados)
P = [r for r in rows if r['modelo_principal'] == 'sim']
ok = [r for r in P if not r['fora_contagem'] and r['celula_alvo'] != 'outro']
print('principal', gravar('swim_entrada_principal', ok))
print('com_excluidos', gravar('swim_entrada_com_excluidos', [r for r in P if r['celula_alvo'] != 'outro' or r['fora_contagem']]))
print('so_real', gravar('swim_entrada_so_contexto_real', [r for r in ok if r['realismo_contexto'] == 'real']))
print('sem_pre2010', gravar('swim_entrada_sem_pre2010', [r for r in ok if r['ano_eleicao_pre2010'] != 'sim']))
print('sem_araujo', gravar('swim_entrada_sem_araujo', [r for r in ok if r['chave'] != 'Araujo2021a']))
print('nulos por delta:', [(r['id_efeito'], r['nulo_por_delta']) for r in P if r['nulo_por_delta']])
print('proxies:', [(r['id_efeito'], r['beta_proxy_sinal']) for r in P if r['beta_proxy_sinal']])
