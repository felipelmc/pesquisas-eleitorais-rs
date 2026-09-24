"""Sensibilidade ICC 0,20 (Emenda 4c): troca o ICC imputado de 0,05 por 0,20 nas linhas com conglomerado.
Só as linhas com icc = 0,05 (valor imputado pela convenção) mudam; ICC relatado pelo estudo fica.

USO
    python3 06-analise/montar_sens_icc020.py
    rs --dir . analise efeitos --in 06-analise/sens_icc020_entrada.csv --out 06-analise/sens_icc020_efeitos.csv
    python3 06-analise/montar_entradas_swim.py 06-analise/sens_icc020_efeitos.csv _icc020
    python3 06-analise/montar_meta_exploratoria.py _icc020
"""
import csv
linhas = list(csv.DictReader(open('05-decomposicao/efeitos_para_sintese.csv', encoding='utf-8')))
n = 0
for l in linhas:
    try:
        if abs(float(l['icc']) - 0.05) < 1e-9:
            l['icc'] = '0.2'; n += 1
    except (ValueError, TypeError):
        pass
w = csv.DictWriter(open('06-analise/sens_icc020_entrada.csv', 'w', encoding='utf-8', newline=''), fieldnames=list(linhas[0]))
w.writeheader(); w.writerows(linhas)
print(f'{n} linhas com ICC 0,05 -> 0,20')
