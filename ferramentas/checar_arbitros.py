"""Confere os JSONs do árbitro: vocabulário, trecho ≤ N palavras e literal na página (índice do PDF).
Uso: python3 checar_arbitros.py <raiz_projeto> [max_palavras=12] [subpasta=04-qualidade/arbitragem]"""
import sys, json, glob, os, re, pymupdf
raiz=sys.argv[1]; maxp=int(sys.argv[2]) if len(sys.argv)>2 else 12
sub=sys.argv[3] if len(sys.argv)>3 else '04-qualidade/arbitragem'
VOC={'rob2':{'baixo','algumas_preocupacoes','alto'},'robins_i':{'baixo_exceto_confundimento','moderado','grave','critico','baixo'},'epoc':{'baixo','incerto','alto'}}
ws=lambda s: re.sub(r'\s+',' ',s).strip()
cache={}
def pag(ch,p):
    if ch not in cache: cache[ch]=[ws(x.get_text()) for x in pymupdf.open(f'{raiz}/03-textos/pdfs/{ch}.pdf')]
    return cache[ch][p-1] if 1<=p<=len(cache[ch]) else ''
prob=0; n=0
for f in sorted(glob.glob(f'{raiz}/{sub}/*/*.json')):
    ferr=os.path.basename(os.path.dirname(f)); ch=os.path.basename(f).split('#')[0]
    for d in json.load(open(f,encoding='utf-8')):
        n+=1; erros=[]
        if d.get('julgamento_consenso') not in VOC[ferr]: erros.append('vocab '+str(d.get('julgamento_consenso')))
        if ferr=='robins_i' and d['dominio']!='D1' and d['julgamento_consenso']=='baixo_exceto_confundimento': erros.append('vocab D1 fora de D1')
        t=ws(d.get('trecho','')); 
        if len(t.split())>maxp: erros.append(f'trecho {len(t.split())} palavras')
        if t and t not in pag(ch,int(d['pagina'])):
            onde=[i+1 for i,x in enumerate(cache[ch]) if t in x]
            erros.append(f'trecho fora da p.{d["pagina"]} (achado em {onde})')
        if not t: erros.append('trecho vazio')
        if erros: prob+=1; print(os.path.basename(f), d['dominio'], '|', '; '.join(erros), '|', t)
print(f'{n} domínios, {prob} com problema')
