"""Monta docs/index.html (a vitrine) num único arquivo autocontido.

USO (de qualquer pasta):
    python3 09-documento-final/vitrine/montar_vitrine.py            # rascunho: avisa se houver texto provisório
    python3 09-documento-final/vitrine/montar_vitrine.py --final    # montagem final: falha se houver "provisório"
    python3 09-documento-final/vitrine/montar_vitrine.py --sem-exportar   # usa o build/vitrine.json que já existe

Passos: roda exportar_dados.py (build/vitrine.json, com SCHEMA e asserts), resolve os marcadores {{bloco.campo}} de
conteudo/textos.yml, gera em Python a camada estática (mensagens, cartões, tabelas de dados, linha do tempo do Brasil,
países, pendências, documentos), concatena CSS e JS em ordem fixa (cada JS como IIFE no namespace window.V), embute
fontes woff2 em base64, D3 com a licença, os dados e os textos, e grava docs/index.html (no máximo 3 MB).
Só escreve docs/index.html.
"""
import argparse
import base64
import html
import importlib.util
import json
import re
import sys
from pathlib import Path

import yaml

VITRINE = Path(__file__).resolve().parent
RAIZ = VITRINE.parents[1]
DOCS = RAIZ / "docs"
SAIDA = DOCS / "index.html"
LIMITE = 3 * 1024 * 1024
FONTES = RAIZ / "09-documento-final/revista/fontes"
FACES = [("STIX Two Text", 400, "normal", "STIXTwoText-Regular.woff2"),
         ("STIX Two Text", 400, "italic", "STIXTwoText-Italic.woff2"),
         ("STIX Two Text", 600, "normal", "STIXTwoText-SemiBold.woff2"),
         ("Fira Sans", 400, "normal", "FiraSans-Regular.woff2"),
         ("Fira Sans", 400, "italic", "FiraSans-Italic.woff2"),
         ("Fira Sans", 500, "normal", "FiraSans-Medium.woff2"),
         ("Fira Sans", 600, "normal", "FiraSans-SemiBold.woff2")]
CSS = ["tokens", "base", "layout", "graficos"]
JS = ["fmt", "tooltip", "gaveta", "legenda", "heroi", "prisma", "mapa_evidencia", "direcao", "contagem", "forest", "rob",
      "processo", "pendencias", "main"]
VENDOR = [("d3-7.9.0.min.js", "LICENSE-d3.txt")]


def falha(msg):
    sys.exit(f"montar_vitrine.py: ERRO: {msg}")


def esc(s):
    return html.escape(str(s), quote=True)


# ------------------------------------------------------------------ textos
def md_inline(s):
    """Escapa e aplica o Markdown mínimo dos textos: **x**, *x* (termo inglês) e [t](url)."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r'<i lang="en">\1</i>', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def resolver(obj, D, caminho=""):
    if isinstance(obj, dict):
        return {k: resolver(v, D, f"{caminho}.{k}") for k, v in obj.items()}
    if isinstance(obj, list):
        return [resolver(v, D, f"{caminho}[{i}]") for i, v in enumerate(obj)]
    if isinstance(obj, (int, float)) and not isinstance(obj, bool):
        return obj
    if not isinstance(obj, str):
        return obj

    def troca(m):
        bloco, campo = m.group(1), m.group(2)
        if bloco not in ("numeros", "meta") or campo not in D[bloco]:
            falha(f"marcador sem valor em textos.yml{caminho}: {{{{{bloco}.{campo}}}}}")
        return str(D[bloco][campo])
    s = re.sub(r"\{\{\s*(\w+)\.(\w+)\s*\}\}", troca, obj)
    if "{{" in s:
        falha(f"marcador malformado em textos.yml{caminho}: {obj}")
    return md_inline(s)


def conferir_brasil(itens):
    for it in itens:
        fonte = RAIZ / it.get("fonte_confirmar", "09-documento-final/insumos/contexto_brasil.md")
        txt = fonte.read_text(encoding="utf-8")
        if it["confirmar"] not in txt:
            falha(f"linha do tempo do Brasil: trecho não confirmado em {fonte.name}: {it['confirmar']!r}")
        if str(it["ano"]) not in txt:
            falha(f"linha do tempo do Brasil: ano {it['ano']} não aparece em {fonte.name}")


# ------------------------------------------------------------------ peças estáticas
def cab(T, chave, ident):
    return (f'<header class="secao-cabeca revelar"><p class="kicker">{T[chave]["kicker"]}</p>'
            f'<h2 id="{ident}">{T[chave]["titulo"]}</h2></header>')


def detalhes(titulo, cabecalho, linhas, classe_num=(), extra_id=None, caption=None):
    th = "".join(f'<th scope="col"{" class=\"num\"" if i in classe_num else ""}>{c}</th>' for i, c in enumerate(cabecalho))
    corpo = "".join("<tr>" + "".join(f'<td{" class=\"num\"" if i in classe_num else ""}>{c}</td>' for i, c in enumerate(l)) + "</tr>"
                    for l in linhas)
    tid = f' id="{extra_id}"' if extra_id else ""
    cap = f"<caption>{caption}</caption>" if caption else ""
    return (f'<details class="tabela-dados"><summary><span>{titulo}</span></summary><div class="tabela-rolagem"><table>{cap}<thead><tr>{th}</tr></thead>'
            f'<tbody{tid}>{corpo}</tbody></table></div></details>')


def contadores(D, T):
    n, ct = D["numeros"], T["heroi"]["contadores"]
    r0, r1 = D["prisma"]["ramos"][0]["identificados"], D["prisma"]["ramos"][1]["identificados"]
    itens = [
        (f'<span data-contar="{r0}">{n["registros_bases"]}</span><span class="mais">+</span><span data-contar="{r1}">{n["registros_citacoes"]}</span>',
         ct["registros"], ""),
        (f'<span data-contar="{n["estudos"]}">{n["estudos"]}</span>', f'{ct["estudos"]} <span class="fraco">({n["relatos"]} {ct["relatos"]})</span>', ""),
        (f'<span data-contar="{n["efeitos"].replace(".", "")}">{n["efeitos"]}</span>', ct["efeitos"], ""),
        (f'<span data-contar="{n["celulas"]}">{n["celulas"]}</span>', ct["celulas"], ""),
        (f'<span data-contar="{n["celulas_muito_baixa"]}">{n["celulas_muito_baixa"]}</span> <span class="mais">de</span> {n["celulas"]}',
         ct["certeza"], " contador-final"),
    ]
    return '<ul class="contadores">' + "".join(
        f'<li class="contador{c}"><span class="contador-valor">{v}</span><span class="contador-rotulo">{r}</span></li>'
        for v, r, c in itens) + "</ul>"


def bloco_mensagens(D, T):
    M = D["mensagens"]
    h = cab(T, "mensagens", "titulo-mensagens")
    if M["provisorio"]:
        h += f'<p class="provisorio revelar">{T["mensagens"]["provisorio"]}</p>'
    secoes = {"Apoio a quem aparece à frente": "sec-apoio", "Comparecimento": "sec-comparecimento",
              "Boca de urna": "sec-efeito", "Brasil": "sec-brasil", "O que a evidência não permite dizer": "sec-limitacoes-evidencia"}
    h += '<div class="cartoes cartoes-mensagens">'
    for i, m in enumerate(M["itens"], 1):
        sec = secoes.get(m["titulo"], "sec-achados")
        h += (f'<article class="cartao cartao-mensagem revelar"><p class="cartao-num">{i:02d}</p><h3>{esc(m["titulo"])}</h3>'
              f'<p>{m["html"]}</p><a class="cartao-link" href="revisao.html#{sec}">{T["mensagens"]["ler"]}</a></article>')
    return h + "</div>"


def bloco_linguagem(D, T):
    L = D["linguagem_simples"]
    h = '<div class="linguagem-grade"><div>' + cab(T, "linguagem", "titulo-linguagem")
    if L["provisorio"]:
        h += f'<p class="provisorio revelar">{T["linguagem"]["provisorio"]}</p>'
    h += f'</div><div class="linguagem-texto prosa revelar">{L["html"]}</div></div>'
    return h


def diagrama_prisma(D):
    P = D["prisma"]
    h = '<div class="pd-grade">'
    for r in P["ramos"]:
        fontes = "; ".join(f'{f["fonte"]} (n = {f["n_fmt"]})' for f in r["por_fonte"]) or "citações dos estudos incluídos"
        mot = "<br>".join(f'{esc(m["motivo"])} (n = {m["n"]})' for m in r["motivos"])
        titulo = "Via bases de dados" if r["id"] == "bases" else "Via outros métodos"
        h += _diag_ramo(r, titulo, fontes, mot)
    h += '</div>'
    h += (f'<p class="pd-final"><span class="pd-etapa">Incluídos na revisão</span>Estudos: <strong>n = {P["estudos"]}</strong> · '
          f'relatos: <strong>n = {P["relatos"]}</strong></p>')
    return h


def _fmt(n):
    return f"{n:,}".replace(",", ".")


def _diag_ramo(r, titulo, fontes, mot):
    linhas = [
        ("Identificação", f'Registros identificados: <strong>n = {r["identificados_fmt"]}</strong><br>{fontes}',
         f'Removidos antes da triagem:<br>duplicatas (n = {_fmt(r["duplicatas"])})<br>por automação, filtro de ano (n = {_fmt(r["automacao"])})'),
        ("Triagem", f'Registros triados: <strong>n = {_fmt(r["triados"])}</strong>', f'Registros excluídos: n = {_fmt(r["excluidos_triagem"])}'),
        ("", f'Relatos buscados para recuperação: <strong>n = {_fmt(r["buscados"])}</strong>', f'Relatos não recuperados: n = {_fmt(r["nao_recuperados"])}'),
        ("", f'Relatos avaliados para elegibilidade: <strong>n = {_fmt(r["avaliados"])}</strong>',
         f'Relatos excluídos (n = {_fmt(r["excluidos_elegibilidade"])}):<br>{mot}'),
        ("Incluídos", f'Relatos incluídos: <strong>n = {_fmt(r["incluidos"])}</strong>', None),
    ]
    h = f'<div class="pd-ramo"><h4>{titulo}</h4>'
    for et, principal, saida in linhas:
        etq = f'<span class="pd-etapa">{et}</span>' if et else ""
        h += f'<div class="pd-linha"><div class="pd-caixa pd-principal">{etq}{principal}</div>'
        h += f'<div class="pd-caixa pd-saida">{saida}</div></div>' if saida else "<div></div></div>"
    return h + "</div>"


def bloco_prisma(D, T):
    P, TP = D["prisma"], T["prisma"]
    h = cab(T, "prisma", "titulo-prisma") + f'<p class="secao-intro revelar">{TP["intro"]}</p>'
    h += ('<div class="prisma-topo so-js"><span></span><button type="button" class="botao botao-alternar" id="prisma-alternar" '
          f'aria-expanded="false" aria-controls="prisma-diagrama"><span>{TP["alternar"]}</span></button></div>')
    h += (f'<figure class="grafico revelar" id="prisma-fluxo-fig" data-acao="prisma"><div class="grafico-caixa"><div id="prisma-fluxo" class="so-js"></div>'
          f'<p class="nota prisma-nota">{TP["nota_automacao"]}</p></div>'
          f'<figcaption class="legenda-fig" id="prisma-legenda">{TP["legenda"]}</figcaption></figure>')
    h += (f'<figure class="grafico prisma-diagrama" id="prisma-diagrama" hidden><div class="grafico-caixa">{diagrama_prisma(D)}</div>'
          f'<figcaption class="legenda-fig">{TP["legenda_diagrama"]}</figcaption></figure>')
    linhas = []
    for r in P["ramos"]:
        linhas += [[esc(r["rotulo"]), "identificados", _fmt(r["identificados"])],
                   [esc(r["rotulo"]), "duplicatas removidas", _fmt(r["duplicatas"])],
                   [esc(r["rotulo"]), "removidos pelo filtro de ano (script)", _fmt(r["automacao"])],
                   [esc(r["rotulo"]), "triados", _fmt(r["triados"])],
                   [esc(r["rotulo"]), "excluídos na triagem", _fmt(r["excluidos_triagem"])],
                   [esc(r["rotulo"]), "buscados no texto completo", _fmt(r["buscados"])],
                   [esc(r["rotulo"]), "não recuperados", _fmt(r["nao_recuperados"])],
                   [esc(r["rotulo"]), "avaliados", _fmt(r["avaliados"])]]
        linhas += [[esc(r["rotulo"]), f'excluídos no texto completo: {esc(m["motivo"])}', _fmt(m["n"])] for m in r["motivos"]]
        linhas += [[esc(r["rotulo"]), "relatos incluídos", _fmt(r["incluidos"])]]
    linhas += [["total", "relatos incluídos", _fmt(P["relatos"])], ["total", "estudos incluídos", _fmt(P["estudos"])]]
    h += detalhes("Ver tabela", ["Ramo", "Etapa", "n"], linhas, classe_num=(2,))
    # continuação
    F, E = P["fluxo_estudos"], D["estudos"]
    h += f'<h3 class="revelar">{TP["continuacao_titulo"]}</h3><p class="secao-intro revelar">{TP["continuacao_intro"]}</p>'
    h += (f'<figure class="grafico revelar"><div class="grafico-caixa"><div id="prisma-estudos" class="so-js"></div></div>'
          f'<figcaption class="legenda-fig">{TP["legenda_continuacao"]}</figcaption></figure>')
    nomes = lambda ks: "; ".join(esc(E[k]["rotulo"]) for k in ks)
    sem_princ_com_ef = [k for k in F["sem_principal"] if k not in F["sem_efeitos"]]
    lin = [[str(F["estudos"]), "estudos incluídos", ""],
           [str(len(F["sem_efeitos"])), "saem: sem nenhum efeito extraído", nomes(F["sem_efeitos"])],
           [str(F["com_efeitos"]), "com efeitos extraídos", ""],
           [str(len(sem_princ_com_ef)), "saem: nenhum efeito principal", nomes(sem_princ_com_ef)],
           [str(F["com_principal"]), "com efeito principal", ""],
           [str(len(F["criticos"])), "saem: risco de viés crítico", nomes(F["criticos"])],
           [str(len(F["so_fora"])), "saem: efeitos principais fora da contagem", nomes(F["so_fora"])],
           [str(F["sintese"]), "na síntese principal", ""]]
    h += detalhes("Ver tabela", ["n", "Etapa", "Estudos"], lin, classe_num=(0,))
    return h


def bloco_mapa(D, T):
    TM = T["mapa"]
    h = cab(T, "mapa", "titulo-mapa") + f'<p class="secao-intro revelar">{TM["intro"]}</p>'
    h += (f'<figure class="grafico revelar" data-acao="mapa"><div id="mapa-grade" class="mapa so-js" role="group" aria-labelledby="mapa-legenda"></div>'
          f'<figcaption class="legenda-fig" id="mapa-legenda">{TM["legenda"]}</figcaption>'
          f'<div class="mapa-notas"><p class="nota">{TM["caixa_nota"]}</p><p class="nota">{TM["nota_momentum"]}</p></div></figure>')
    blocos = {b["id"]: re.sub(r"<[^>]+>", "", b["rotulo"]) for b in D["blocos"]}
    linhas = []
    for c in D["celulas"]:
        linhas.append([esc(blocos[c["bloco"]]), esc(c["familia_rot"]), esc(c["comparador_rot"]), esc(c["classe_rot"]),
                       "; ".join(esc(D["estudos"][e["chave"]]["rotulo"]) for e in c["estudos"]), c["contagem"],
                       (f'{c["proporcao_fmt"]} ({c["ic_fmt"]})' if c["proporcao_fmt"] else "NR"), c["p_fmt"] or "NR",
                       esc(c["certeza_rot"]), esc(c["enunciado"])])
    for v in D["vazias"]:
        linhas.append([esc(blocos[v["bloco"]]), esc(v["familia_rot"]), esc(v["comparador_rot"]),
                       "Não randomizado" if v["classe"] == "nao_randomizado" else "Randomizado", "nenhum", "nenhum estudo", "NR",
                       "NR", "não julgada (célula vazia)", ""])
    h += detalhes("Ver tabela", ["Bloco", "Exposição", "Comparador", "Classe", "Estudos", "Direções", "Proporção (IC 95%)", "p (sinal)",
                                 "Certeza", "Enunciado"], linhas, classe_num=(6, 7))
    return h


def bloco_direcao(D, T):
    TD = T["direcao"]
    h = cab(T, "direcao", "titulo-direcao") + f'<p class="secao-intro revelar">{TD["intro"]}</p>'
    h += f'<div class="filtros so-js" id="direcao-filtros" role="region" aria-label="{esc(re.sub("<[^>]+>", "", TD["filtros"]))}"></div>'
    h += (f'<figure class="grafico"><div id="direcao-grafico" class="so-js" role="group" aria-labelledby="direcao-legenda"></div>'
          f'<figcaption class="legenda-fig" id="direcao-legenda">{TD["legenda"]}</figcaption></figure>')
    E = D["estudos"]
    linhas = []
    for c in D["celulas"]:
        for e in c["estudos"]:
            s = E[e["chave"]]
            linhas.append([esc(f'{c["familia_rot"]} · {c["comparador_rot"]} · {c["classe_rot"].lower()}'), esc(s["rotulo"]), e["direcao_rot"],
                           f'{e["n_pos"]} / {e["n_neg"]} / {e["n_efeitos"]}', e["n_fmt"] + (f' {esc(s["unidade"])}' if e["n_amostra"] is not None else ""),
                           esc(f'{e["rob"]["ferramenta"]}: {e["rob"]["geral_rot"]}'), "síntese principal"])
    for e in D["fora"]:
        s = E[e["chave"]]
        linhas.append([esc(e["grupo_rot"] or "nenhum efeito principal"), esc(s["rotulo"]), e["direcao_rot"],
                       f'{e["n_pos"]} / {e["n_neg"]} / {e["n_efeitos"]}' if e["n_efeitos"] else "NR", e["n_fmt"],
                       esc("; ".join(f'{r["ferramenta"]}: {r["geral_rot"]}' for r in s["rob"]) or "não avaliado"), esc(s["motivo"])])
    h += detalhes("Ver tabela", ["Célula", "Estudo", "Direção", "Efeitos (positivos / negativos / total)", "n", "Risco de viés", "Situação"],
                  linhas, classe_num=(3,))
    return h


def bloco_contagem(D, T):
    TC = T["contagem"]
    h = cab(T, "contagem", "titulo-contagem") + f'<p class="secao-intro revelar">{TC["intro"]}</p>'
    h += '<div class="segmentos so-js" id="contagem-controle" role="radiogroup" aria-label="Análise"></div>'
    h += '<p class="contagem-nota" id="contagem-nota" hidden></p>'
    h += (f'<figure class="grafico revelar"><div class="grafico-caixa"><div id="contagem-grafico" class="so-js"></div></div>'
          f'<figcaption class="legenda-fig" id="contagem-legenda">{TC["legenda"]}</figcaption></figure>')
    a = D["sensibilidades"][0]
    blocos = {b["id"]: re.sub(r"<[^>]+>", "", b["rotulo"]) for b in D["blocos"]}
    linhas = [[esc(blocos.get(g["bloco"], g["bloco"])), esc(re.sub(r"<[^>]+>", "", g["rotulo"])), esc(g["classe_rot"]), g["k"], g["n_pos"], g["n_neg"],
               g["n_mistos"], g["n_nulos"], g["ic_fmt"] or "NR", g["p_fmt"] or "NR", esc(g["certeza_rot"] or "sem GRADE próprio")] for g in a["grupos"]]
    h += detalhes(f'Ver tabela: <span id="contagem-tabela-titulo">{esc(a["rotulo"])}</span>',
                  ["Bloco", "Grupo", "Classe", "k", "Positivos", "Negativos", "Mistos", "Nulos", "IC 95%", "p (sinal)", "Certeza"],
                  linhas, classe_num=(3, 4, 5, 6, 7, 8, 9), extra_id="contagem-tabela-corpo")
    return h


def bloco_forest(D, T):
    TF = T["forest"]
    h = cab(T, "forest", "titulo-forest") + f'<p class="secao-intro revelar">{TF["intro"]}</p><div class="metas">'
    for m in D["metas"]:
        h += (f'<figure class="grafico meta-caixa revelar"><div class="grafico-caixa"><h3 id="forest-titulo-{m["id"]}">{esc(m["titulo"])}</h3>'
              f'<p class="meta-sub">{m["k_estudos"]} estudos, {m["k_efeitos"]} efeitos</p><p class="carimbo">{TF["carimbo"]}</p>'
              f'<div id="forest-{m["id"]}" class="so-js"></div>'
              f'<p class="meta-numeros"><span>g = <b>{m["g_fmt"]}</b></span><span>IC 95% {m["ic_fmt"]}</span><span>p = {m["p_fmt"]}</span>'
              f'<span>gl = {m["gl_fmt"]}</span><span>τ² = {m["tau2_fmt"]}</span><span>I² = {m["i2_fmt"]}%</span>'
              f'<span>intervalo de predição {m["pi_fmt"]}</span><span>δ = {m["delta_fmt"]}</span></p>'
              '<div class="tabela-rolagem loo"><table><caption>' + TF["loo"] + '</caption><thead><tr><th scope="col">Sem</th>'
              '<th scope="col" class="num">g</th><th scope="col" class="num">IC 95%</th></tr></thead><tbody>' +
              "".join(f'<tr class="{"muda" if l["muda"] else ""}"><td>{esc(l["sem"])}{(" <span class=\"g-fraco\">(" + TF["loo_muda"] + ")</span>") if l["muda"] else ""}</td>'
                      f'<td class="num">{l["g_fmt"]}</td><td class="num">{l["ic_fmt"]}</td></tr>' for l in m["loo"]) +
              '</tbody></table></div>' +
              detalhes("Ver tabela", ["Estudo", "Efeito", "g", "EP"],
                       [[esc(e["rotulo"]), e["efeito"], e["g_fmt"], e["ep_fmt"]] for e in m["efeitos"]], classe_num=(2, 3)) +
              '</div></figure>')
    h += f'</div><p class="legenda-fig" id="forest-legenda">{TF["legenda"]} {TF["tyszler"]}</p>'
    return h


def bloco_rob(D, T):
    TR = T["rob"]
    h = cab(T, "rob", "titulo-rob") + f'<p class="secao-intro revelar">{TR["intro"]}</p>'
    h += (f'<figure class="grafico revelar"><div class="grafico-caixa"><div id="rob-grafico" class="rob-grade so-js" role="group" aria-labelledby="rob-legenda"></div></div>'
          f'<figcaption class="legenda-fig" id="rob-legenda">{TR["legenda"]} <strong>{TR["nota"]}</strong> {TR["nota_epoc"]}</figcaption></figure>')
    linhas = []
    for f in D["rob"]:
        for d in f["dominios"]:
            linhas.append([esc(f["ferramenta"]), esc(d["rotulo"]), "; ".join(f'{j["n"]} {esc(j["rot"])}' for j in d["j"]), d["desacordos"]])
        linhas.append([esc(f["ferramenta"]), "geral", "; ".join(f'{j["n"]} {esc(j["rot"])}' for j in f["geral"]), ""])
    h += detalhes("Ver tabela", ["Ferramenta", "Domínio", "Julgamentos (resultados)", "Desacordos entre avaliadores de IA"], linhas, classe_num=(3,))
    return h


def bloco_nao_sabemos(D, T):
    TN = T["nao_sabemos"]
    h = cab(T, "nao_sabemos", "titulo-nao-sabemos") + '<div class="cartoes cartoes-nao">'
    for c in TN["cartoes"]:
        dest = f' data-destaque="{esc(re.sub("<[^>]+>", "", c["destaque"]))}"' if c.get("destaque") else ""
        alvo = re.sub(r"<[^>]+>", "", c["alvo"])
        h += (f'<article class="cartao cartao-nao revelar"><p class="nao-rotulo">não sabemos</p><h3>{c["titulo"]}</h3><p>{c["texto"]}</p>'
              f'<a class="cartao-link" href="{esc(alvo)}"{dest}>{c["rotulo_alvo"]}</a></article>')
    return h + "</div>"


def bloco_onde(D, T):
    TO, P = T["onde"], D["paises"]
    h = cab(T, "onde", "titulo-onde") + f'<p class="secao-intro revelar">{TO["intro"]}</p>'
    varios = [p for p in P["lista"] if p["n"] > 1]
    um = [p for p in P["lista"] if p["n"] == 1]
    mx = max(p["n"] for p in P["lista"])
    h += f'<figure class="grafico revelar"><div class="paises"><div><ul class="paises-barras" aria-labelledby="onde-legenda">'
    for p in varios:
        br = " pais-brasil" if p["pais"] == "Brasil" else ""
        h += (f'<li class="pais{br}"><span class="pais-nome">{esc(p["pais"])}</span><span class="pais-barra" style="--w:{100 * p["n"] / mx:.1f}%"></span>'
              f'<span class="pais-n">{p["n"]}</span></li>')
    h += f'</ul></div><div class="paises-um"><h3>{TO["um_estudo"]}</h3><ul class="paises-chips">'
    for p in um:
        br = ' class="pais-brasil"' if p["pais"] == "Brasil" else ""
        h += f'<li{br}>{esc(p["pais"])}</li>'
    h += '</ul><div class="paises-extra">'
    h += f'<p><strong>Brasil</strong>: {TO["brasil_nota"]}</p>'
    for m in P["multinacional"]:
        h += (f'<p><strong>{TO["multinacional"]} ({m["n_paises"]})</strong>: {esc(m["rotulo"])}'
              f'{", " + TO["multinacional_nota"] if m["inclui_brasil"] else ""}.</p>')
    if P["nao_relatado"]:
        h += f'<p><strong>{TO["nao_relatado"]}</strong>: {"; ".join(esc(x) for x in P["nao_relatado"])}.</p>'
    h += f'</div></div></div><figcaption class="legenda-fig" id="onde-legenda">{TO["legenda"]}</figcaption></figure>'
    return h


def bloco_brasil(D, T):
    TB = T["brasil"]
    h = cab(T, "brasil", "titulo-brasil") + f'<p class="secao-intro revelar">{TB["intro"]}</p><ol class="linha-tempo">'
    for it in TB["itens"]:
        estudo = " lt-estudo" if "estudo" in it["texto"] else ""
        h += (f'<li class="lt-item revelar{estudo}"><span class="lt-ano">{it["ano"]}</span><p class="lt-texto">{it["texto"]}</p></li>')
    return h + "</ol>"


def bloco_processo(D, T):
    TP = T["processo"]
    h = cab(T, "processo", "titulo-processo") + f'<p class="secao-intro revelar">{TP["intro"]}</p>'
    h += (f'<figure class="grafico revelar"><div class="grafico-caixa"><div id="processo-grafico" class="so-js"></div>'
          '<ul class="processo-legenda-raias so-js">'
          '<li><svg width="12" height="12" aria-hidden="true"><circle cx="6" cy="6" r="5" fill="var(--ia)"/></svg>portão</li>'
          '<li><svg width="12" height="12" aria-hidden="true"><rect x="2" y="2" width="8" height="8" transform="rotate(45 6 6)" fill="var(--ia)"/></svg>emenda com evento no log</li>'
          '<li><svg width="12" height="12" aria-hidden="true"><rect x="1.5" y="1.5" width="9" height="9" fill="none" stroke="var(--script)" stroke-width="2"/></svg>saída final de script</li>'
          '<li><svg width="22" height="22" aria-hidden="true"><circle cx="11" cy="11" r="9" fill="none" stroke="var(--humano)" stroke-width="1.4" stroke-dasharray="2 2.4"/></svg>'
          f'{TP["gravado_humano"]}</li></ul>'
          f'<p class="nota">{TP["nota"]}</p></div>'
          f'<figcaption class="legenda-fig" id="processo-legenda">{TP["legenda"]}</figcaption></figure>')
    P = D["processo"]
    raia = {"humano": TP["raias"]["humano"], "ia": TP["raias"]["ia"], "script": TP["raias"]["script"]}
    linhas = [[e["ts"][:10], e["ts"][11:16] + " UTC", esc(e["rotulo"]), raia[e["raia"]],
               ("sim" if e["gravado_humano"] and e["raia"] != "humano" else "")] for e in P["eventos"]]
    linhas += [[s["ts"][:10], s["ts"][11:16] + " UTC", esc(s["rotulo"]), raia["script"], ""] for s in P["scripts"]]
    linhas += [[e["data"], "", f'{esc(e["id"])}: {TP["emendas"][e["id"]]}', TP["raias"]["emendas"], ""] for e in P["emendas"]]
    linhas.sort(key=lambda l: (l[0], l[1]))
    h += detalhes("Ver tabela", ["Data", "Hora", "Evento", "Raia", "Gravado como humano no log"], linhas)
    return h


ANCORA_LACUNAS = "ap-g-ia"  # seção do Apêndice G em apendices.html (_esqueleto_suplemento.qmd)


def bloco_pendencias(D, T):
    TP, P = T["pendencias"], D["pendencias"]
    h = ('<div class="pend-topo"><div>' + cab(T, "pendencias", "titulo-pendencias") + f'<p class="secao-intro revelar">{TP["intro"]}</p></div>'
         f'<div class="medidor revelar" data-acao="pendencias"><p class="medidor-valor">{P["fechadas"]} <small>de {P["total"]} fechadas</small></p>'
         '<div class="medidor-caixas" aria-hidden="true">'
         + "".join(f'<span class="medidor-caixa{" fechada" if i < P["fechadas"] else ""}"></span>' for i in range(P["total"])) +
         f'</div><p class="nota"><a href="apendices.html#{ANCORA_LACUNAS}">{TP["guia"]}</a></p></div></div>')
    h += '<ol class="pipeline">'
    for i, e in enumerate(P["etapas"], 1):
        port = f'<span class="etapa-portao">portão {", ".join(e["portoes"])}</span>' if e["portoes"] else ""
        h += (f'<li class="etapa revelar"><span class="etapa-ponto" aria-hidden="true">{i}</span><div><div class="etapa-cabeca"><h3>{esc(e["rotulo"])}</h3>{port}</div>'
              '<ul class="pend-lista">')
        for it in e["itens"]:
            h += (f'<li class="pend"><span class="pend-id">{it["id"]}</span><span class="pend-estado">aberta</span>'
                  f'<p class="pend-fazer">{esc(it["fazer"])}</p><span class="pend-esforco">{TP["esforco"]}: {esc(it["esforco"])}</span></li>')
        h += '</ul></div></li>'
    return h + '</ol>'


def bloco_documentos(D, T):
    TD, M = T["documentos"], D["meta"]
    h = cab(T, "documentos", "titulo-documentos")
    for g in ("artigo", "apendices", "apoio"):
        h += f'<div class="docs-grupo"><h3>{TD["grupos"][g]}</h3><div class="docs-grade">'
        for d in [x for x in D["documentos"] if x["grupo"] == g]:
            inner = (f'<span class="doc-formato">{d["formato"]}</span><span class="doc-titulo">{esc(d["rotulo"])}</span>'
                     f'<span class="doc-desc">{esc(d["desc"])}</span>')
            if d["existe"]:
                h += f'<a class="doc revelar" href="{d["arquivo"]}">{inner}<span class="doc-tam tamanho-arquivo">{d["tamanho"]}</span></a>'
            else:
                h += f'<div class="doc doc-indisponivel revelar">{inner}<span class="doc-tam">{TD["em_preparacao"]}</span></div>'
        h += '</div></div>'
    titulo_art = ("Pesquisas eleitorais publicadas mudam o voto? Síntese sistemática de evidências, conduzida com agentes "
                  "de IA, sobre os efeitos bandwagon e underdog e o comparecimento")
    cit = (f'{esc(M["autor"].split()[-1])}, {esc(M["autor"].rsplit(" ", 1)[0])}. 2026. “Pesquisas eleitorais publicadas mudam o voto? '
           'Síntese sistemática de evidências, conduzida com agentes de IA, sobre os efeitos <i lang="en">bandwagon</i> e '
           '<i lang="en">underdog</i> e o comparecimento.” '
           f'{TD["citar_nota"]} {esc(M["afiliacao"])}. <span class="url">{esc(M["url"])}</span>')
    bib = ("@unpublished{Lamarca2026pesquisas,\n"
           f"  author = {{{M['autor'].split()[-1]}, {M['autor'].rsplit(' ', 1)[0]}}},\n"
           f"  title  = {{{titulo_art}}},\n"
           "  year   = {2026},\n"
           f"  note   = {{{re.sub('<[^>]+>', '', TD['citar_nota'])} {M['afiliacao']}}},\n"
           f"  url    = {{{M['url']}}}\n}}")
    h += (f'<div class="citacao"><div><h3 class="docs-grupo-titulo">{TD["citar_titulo"]}</h3><p class="citacao-texto">{cit}</p></div>'
          f'<div><pre id="bibtex"><code>{esc(bib)}</code></pre><button type="button" class="botao so-js" id="copiar-bibtex"><span>{TD["copiar"]}</span></button></div></div>')
    return h


def bloco_rodape(D, T):
    TR = T["rodape"]
    return ('<div class="rodape-grade">'
            f'<div><h2>{TR["creditos_titulo"]}</h2><p>{TR["creditos"]}</p></div>'
            f'<div><p class="rodape-ia">{TR["ia"]}</p><p>{TR["versao"]}</p></div>'
            f'<div><h2>{TR["mudou_titulo"]}</h2><p>{TR["mudou"]}</p></div></div>')


# ------------------------------------------------------------------ montagem
def fontes_css():
    out = ["/* Fontes: STIX Two Text (OFL 1.1) e Fira Sans (OFL 1.1), woff2 oficiais sem modificação. */"]
    for nome in ("OFL-STIX.txt", "OFL-Fira.txt"):
        out.append("/*\n" + (FONTES / nome).read_text(encoding="utf-8").replace("*/", "* /") + "\n*/")
    for fam, peso, estilo, arq in FACES:
        b64 = base64.b64encode((FONTES / "woff2" / arq).read_bytes()).decode()
        out.append(f'@font-face {{ font-family: "{fam}"; font-style: {estilo}; font-weight: {peso}; font-display: swap; '
                   f'src: url(data:font/woff2;base64,{b64}) format("woff2"); }}')
    return "\n".join(out)


def js_montado():
    partes = []
    for lib, lic in VENDOR:
        licenca = (VITRINE / "vendor" / lic).read_text(encoding="utf-8").replace("*/", "* /")
        partes.append(f"/*! {lib}\n{licenca}\n*/\n" + (VITRINE / "vendor" / lib).read_text(encoding="utf-8"))
    partes.append("window.V = window.V || {};")
    for nome in JS:
        src = (VITRINE / "src/js" / f"{nome}.js").read_text(encoding="utf-8")
        partes.append(f"/* ---- {nome}.js ---- */\n;(function (V) {{\n'use strict';\n{src}\n}})(window.V);")
    js = "\n".join(partes)
    return js.replace("</script", "<\\/script")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", action="store_true", help="falha se houver texto provisório")
    ap.add_argument("--sem-exportar", action="store_true")
    args = ap.parse_args()

    spec = importlib.util.spec_from_file_location("exportar_dados", VITRINE / "exportar_dados.py")
    exp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(exp)
    if not args.sem_exportar:
        exp.main()
    D = json.loads((VITRINE / "build/vitrine.json").read_text(encoding="utf-8"))
    exp.validar(D)

    textos = yaml.safe_load((VITRINE / "conteudo/textos.yml").read_text(encoding="utf-8"))
    conferir_brasil(textos["brasil"]["itens"])
    T = resolver(textos, D)

    tpl = (VITRINE / "src/index.html").read_text(encoding="utf-8")
    est = {
        "titulo_pagina": "Pesquisas eleitorais e voto",
        "descricao": esc("Síntese sistemática de evidências, conduzida com agentes de IA, sobre o efeito de pesquisas eleitorais "
                         "publicadas no voto e no comparecimento (Felipe Lamarca, MAPE/IESP-UERJ)."),
        "og_titulo": "Pesquisas eleitorais publicadas mudam o voto?",
        "pular": T["ferramentas"]["pular"], "movimento": T["ferramentas"]["movimento"], "fechar": T["gaveta"]["fechar"],
        "heroi_kicker": T["heroi"]["kicker"], "titulo": esc(D["meta"]["titulo"]), "heroi_autoria": T["heroi"]["autoria"],
        "heroi_lede": T["heroi"]["lede"], "heroi_contadores": contadores(D, T), "heroi_pontos": T["heroi"]["pontos"],
        "mensagens": bloco_mensagens(D, T), "linguagem": bloco_linguagem(D, T), "prisma": bloco_prisma(D, T),
        "mapa": bloco_mapa(D, T), "direcao": bloco_direcao(D, T), "contagem": bloco_contagem(D, T),
        "forest": bloco_forest(D, T), "rob": bloco_rob(D, T), "nao_sabemos": bloco_nao_sabemos(D, T),
        "onde": bloco_onde(D, T), "brasil": bloco_brasil(D, T), "processo": bloco_processo(D, T),
        "pendencias": bloco_pendencias(D, T), "documentos": bloco_documentos(D, T), "rodape": bloco_rodape(D, T),
    }
    for k, v in est.items():
        marca = f"<!--ESTATICO:{k}-->"
        if marca not in tpl:
            falha(f"marcador ausente no modelo: {marca}")
        tpl = tpl.replace(marca, v)
    sobra = re.findall(r"<!--ESTATICO:(\w+)-->", tpl)
    if sobra:
        falha(f"marcadores sem conteúdo: {sobra}")

    css = fontes_css() + "\n" + "\n".join((VITRINE / "src/css" / f"{n}.css").read_text(encoding="utf-8") for n in CSS)
    dados = json.dumps(D, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    txts = json.dumps(T, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out = (tpl.replace("<!--FONTES-->\n<!--CSS-->", css).replace("<!--DADOS-->", dados).replace("<!--TEXTOS-->", txts)
           .replace("<!--JS-->", js_montado()))
    for m in ("<!--FONTES-->", "<!--CSS-->", "<!--DADOS-->", "<!--TEXTOS-->", "<!--JS-->"):
        if m in out:
            falha(f"marcador não substituído: {m}")

    visivel = re.sub(r"<script.*?</script>|<style.*?</style>", " ", out, flags=re.S)
    provisorio = "provisório" in visivel.lower() or D["mensagens"]["provisorio"] or D["linguagem_simples"]["provisorio"]
    if provisorio and args.final:
        falha("montagem final com texto provisório (mensagens ou linguagem simples ainda do v1)")

    tam = len(out.encode("utf-8"))
    if tam > LIMITE:
        falha(f"docs/index.html com {tam / 1048576:.2f} MB (limite 3 MB)")
    DOCS.mkdir(exist_ok=True)
    SAIDA.write_text(out, encoding="utf-8")
    print(f"docs/index.html: {tam / 1048576:.2f} MB" + ("  (AVISO: há texto provisório; a montagem final falharia)" if provisorio else ""))


if __name__ == "__main__":
    main()
