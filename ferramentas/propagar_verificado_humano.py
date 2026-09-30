"""Leva a marca `verificado_humano` do arquivo combinado aos CSVs por estudo.

USO (da raiz do projeto):
    python3 ferramentas/propagar_verificado_humano.py            # só confere e mostra o que mudaria
    python3 ferramentas/propagar_verificado_humano.py --aplicar  # grava

Por quê: a conferência dos 560 efeitos (P039, Emenda 7) marcou `verificado_humano = sim` em
05-decomposicao/efeitos_extraidos.csv, mas os 40 arquivos 05-decomposicao/efeitos/<chave>.csv, que são a entrada do
`rs analise preparar-efeitos`, ficaram com a coluna vazia. O `preparar-efeitos` só herda a marca do arquivo combinado
anterior; se ele for apagado ou regenerado do zero, a marca se perde. Este script copia a marca para os arquivos por
estudo, linha a linha, pela chave `id_efeito`, e só onde os dados do efeito são os mesmos nos dois arquivos (a
impressão digital `_impressao` do próprio `efeitos_verificar` da skill). Não muda nenhuma outra coluna, preserva a
codificação e as quebras de linha e escreve de forma atômica. Sai com código 1 se algo não bater.

Cuidado depois de rodar: ao corrigir uma linha de efeito, apague a marca dela. O `preparar-efeitos` derruba a marca
herdada do arquivo combinado quando os dados mudam, mas não a que já vem no arquivo por estudo.
"""
import csv
import io
import os
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".claude/skills/revisao-sistematica/scripts"))
from rslib.efeitos_verificar import _impressao  # noqa: E402
from rslib.handoff import sim  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
COMBINADO = RAIZ / "05-decomposicao/efeitos_extraidos.csv"
PASTA = RAIZ / "05-decomposicao/efeitos"
COLUNA = "verificado_humano"


def ler(caminho):
    bruto = caminho.read_bytes()
    if bruto.startswith(b"\xef\xbb\xbf"):
        raise SystemExit(f"{caminho.name}: arquivo com BOM, fora do padrão esperado")
    texto = bruto.decode("utf-8")
    fim = "\r\n" if "\r\n" in texto else "\n"
    leitor = csv.DictReader(io.StringIO(texto, newline=""))
    return texto, fim, leitor.fieldnames, list(leitor)


def serializar(colunas, linhas, fim):
    saida = io.StringIO()
    escritor = csv.DictWriter(saida, fieldnames=colunas, lineterminator=fim)
    escritor.writeheader()
    escritor.writerows(linhas)
    return saida.getvalue()


def main(aplicar):
    _, _, _, combinado = ler(COMBINADO)
    por_id = {}
    for linha in combinado:
        if linha["id_efeito"] in por_id:
            raise SystemExit(f"id_efeito repetido no arquivo combinado: {linha['id_efeito']}")
        por_id[linha["id_efeito"]] = linha
    marcadas, conflitos, puladas, arquivos = 0, [], [], {}
    for caminho in sorted(PASTA.glob("*.csv")):
        texto, fim, colunas, linhas = ler(caminho)
        if serializar(colunas, linhas, fim) != texto:
            raise SystemExit(f"{caminho.name}: reler e regravar sem mudança não reproduz o arquivo; nada foi gravado")
        mudou = False
        for linha in linhas:
            antes = dict(linha)
            ref = por_id.get(linha["id_efeito"])
            if ref is None or linha["chave"] != ref["chave"] or linha["chave"] != caminho.stem:
                puladas.append(f"{caminho.name}:{linha['id_efeito']} (sem par no combinado ou chave diferente)")
                continue
            if not sim(ref.get(COLUNA)):
                puladas.append(f"{caminho.name}:{linha['id_efeito']} (sem marca no combinado)")
                continue
            if _impressao(linha) != _impressao(ref):
                puladas.append(f"{caminho.name}:{linha['id_efeito']} (dados diferentes do combinado)")
                continue
            atual = (linha.get(COLUNA) or "").strip()
            if atual and atual != ref[COLUNA]:
                conflitos.append(f"{caminho.name}:{linha['id_efeito']} ({atual!r} × {ref[COLUNA]!r})")
                continue
            if not atual:
                linha[COLUNA] = ref[COLUNA]
                marcadas += 1
                mudou = True
            diferentes = {c for c in colunas if linha[c] != antes[c]}
            assert diferentes <= {COLUNA}, (caminho.name, diferentes)
        if mudou:
            arquivos[caminho] = serializar(colunas, linhas, fim)
    print(f"{marcadas} linhas a marcar em {len(arquivos)} arquivos; {len(conflitos)} conflitos; {len(puladas)} puladas")
    for item in (conflitos + puladas)[:20]:
        print("  ", item)
    if conflitos or puladas or marcadas != len(combinado):
        print(f"esperava marcar as {len(combinado)} linhas do combinado sem conflito nem linha pulada: nada foi gravado")
        return 1
    if not aplicar:
        print("dry run: rode com --aplicar para gravar")
        return 0
    for caminho, conteudo in arquivos.items():
        fd, tmp = tempfile.mkstemp(dir=caminho.parent, prefix=f".{caminho.name}.")
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(conteudo)
        shutil.copymode(caminho, tmp)
        os.replace(tmp, caminho)
    print(f"gravado: {len(arquivos)} arquivos")
    return 0


if __name__ == "__main__":
    sys.exit(main("--aplicar" in sys.argv[1:]))
