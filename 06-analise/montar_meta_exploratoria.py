"""Monta a entrada da meta-análise EXPLORATÓRIA (Emenda 5) e o δ da célula principal.

USO (depois de montar_entradas_swim.py)
    python3 06-analise/montar_meta_exploratoria.py
    rs --dir . analise meta --in 06-analise/meta_entrada_exploratoria.csv \
       --out-dir 06-analise/meta_exploratoria \
       --grupo familia_intervencao,construto_outcome,comparador_tipo \
       --dependencia um_por_estudo --delta "$(cat 06-analise/_delta_celula.txt)" \
       --separar-desenho sim --excluir-rob critico

Célula: pesquisa_pre_eleitoral × apoio_ao_lider × sem_pesquisa × principal, só efeitos com g
calculado e não nulo por ±δ. δ = 2 p.p. convertido para g pela mediana de p0 da célula
(logit × √3/π). Não há meta-análise principal: nenhuma célula tem k ≥ 3 comparáveis além desta.
"""
import csv, math, statistics

rows = [r for r in csv.DictReader(open('06-analise/swim_entrada_principal.csv', encoding='utf-8'))
        if r['yi'] and r['yi'] != '0']
cel = [r for r in rows if r['familia_intervencao'] == 'pesquisa_pre_eleitoral'
       and r['construto_outcome'] == 'apoio_ao_lider' and r['comparador_tipo'] == 'sem_pesquisa'
       and r['celula_alvo'] == 'principal']
print([(r['id_efeito'], r['yi'][:6], r['p0']) for r in cel])
p0 = statistics.median(float(r['p0']) for r in cel if r['p0'])
p1 = p0 + 0.02
d = math.log((p1 / (1 - p1)) / (p0 / (1 - p0))) * math.sqrt(3) / math.pi
print('mediana p0', p0, 'delta', round(d, 4))
w = csv.DictWriter(open('06-analise/meta_entrada_exploratoria.csv', 'w', encoding='utf-8', newline=''),
                   fieldnames=list(cel[0].keys()))
w.writeheader(); w.writerows(cel)
open('06-analise/_delta_celula.txt', 'w').write(f'{d:.4f}')
