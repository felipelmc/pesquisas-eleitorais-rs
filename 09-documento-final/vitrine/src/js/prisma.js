/* prisma: fluxo dos registros feito à mão (dois ramos, colunas fixas, saídas laterais) e, no celular,
   funil em barras; depois, a continuação dos estudos em pontos (um ponto por estudo). */
function fmtInt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }

function etapas(r) {
  return [
    { n: r.identificados, rot: 'identificados' },
    { n: r.triados, rot: 'triados' },
    { n: r.buscados, rot: 'buscados' },
    { n: r.avaliados, rot: 'avaliados' },
    { n: r.incluidos, rot: 'incluídos' }
  ];
}
function saidas(r) {
  var mot = r.motivos.map(function (m) { return m.motivo + ' ' + fmtInt(m.n); }).join(' · ');
  return [
    { n: r.duplicatas + r.automacao, rot: 'removidos antes da triagem', det: fmtInt(r.duplicatas) + ' duplicatas · ' + fmtInt(r.automacao) + ' pelo filtro de ano (script)', semSoma: true },
    { n: r.excluidos_triagem, rot: 'excluídos na triagem de títulos e resumos', det: '' },
    { n: r.nao_recuperados, rot: 'não recuperados', det: 'texto completo não obtido em fonte legítima' },
    { n: r.excluidos_elegibilidade, rot: 'excluídos no texto completo', det: mot }
  ];
}

function faixa(x0, y0a, y0b, x1, y1a, y1b) {
  var xm = (x0 + x1) / 2;
  return 'M' + x0 + ',' + y0a + 'C' + xm + ',' + y0a + ' ' + xm + ',' + y1a + ' ' + x1 + ',' + y1a +
    'L' + x1 + ',' + y1b + 'C' + xm + ',' + y1b + ' ' + xm + ',' + y0b + ' ' + x0 + ',' + y0b + 'Z';
}

V.prisma = {
  desenhar: function () {
    var alvo = document.getElementById('prisma-fluxo');
    if (!alvo) return;
    var W = V.largura(alvo);
    if (W < 700) return V.prisma.funil(alvo);
    alvo.innerHTML = '';
    var P = V.D.prisma, R = P.ramos;
    var ML = 150, MR = 150, nodeW = 8, gapC = 64;
    var H = Math.round(Math.max(500, Math.min(600, W * 0.5)));
    var passo = (W - ML - MR) / 5;
    var xs = [0, 1, 2, 3, 4, 5].map(function (i) { return ML + i * passo; });
    var maxN = Math.max(R[0].identificados, R[1].identificados);
    var Hb = (H - gapC) / 2 - 86;
    var k = Hb / maxN, minT = 2;
    var esp = function (n) { return Math.max(minT, n * k); };
    var yb = H / 2 - gapC / 2, yc = H / 2 + gapC / 2;

    var svg = d3.select(alvo).append('svg').attr('width', W).attr('height', H).attr('viewBox', '0 0 ' + W + ' ' + H)
      .attr('role', 'img').attr('aria-labelledby', 'prisma-legenda').attr('class', 'prisma-svg');
    var clipId = 'prisma-clip';
    var clip = svg.append('defs').append('clipPath').attr('id', clipId).append('rect').attr('x', 0).attr('y', 0).attr('height', H)
      .attr('width', V.reduzido() || V.prisma._animado ? W : 0);
    V.prisma._clip = clip; V.prisma._W = W;
    var cont = svg.append('g').attr('clip-path', 'url(#' + clipId + ')');
    var gSaidas = cont.append('g'), gFluxo = cont.append('g'), gNos = cont.append('g');
    var gRot = svg.append('g').attr('class', 'rotulo-grafico');

    R.forEach(function (r, ri) {
      var cima = ri === 0, E = etapas(r), S = saidas(r);
      var y = function (h, parte) { /* parte: 'topo' ou 'base' do nó de altura h, alinhado à linha central */
        return cima ? (parte === 'topo' ? yb - h : yb) : (parte === 'topo' ? yc : yc + h);
      };
      E.forEach(function (e, i) {
        var h = esp(e.n), x = xs[i];
        var y0 = cima ? yb - h : yc;
        var no = gNos.append('rect').attr('x', x).attr('y', y0).attr('width', nodeW).attr('height', h).attr('rx', 1.5)
          .attr('fill', 'var(--ink)').attr('class', 'prisma-no');
        /* rótulo do nó, na faixa central */
        var ty = cima ? yb + 17 : yc - 8;
        var t = gRot.append('text').attr('x', x).attr('y', ty).attr('class', 'prisma-rot-no');
        t.append('tspan').attr('class', 'forte').text(fmtInt(e.n));
        t.append('tspan').text(' ' + e.rot);
        if (i < 4) {
          var hn = esp(E[i + 1].n), s = S[i], hs = Math.max(minT, s.n * k);
          /* fluxo principal (reto, alinhado à linha central) */
          var fy0 = cima ? yb - hn : yc, fy1 = cima ? yb : yc + hn;
          gFluxo.append('rect').attr('x', x + nodeW).attr('y', fy0).attr('width', xs[i + 1] - x - nodeW).attr('height', fy1 - fy0)
            .attr('fill', 'var(--fluxo)').attr('fill-opacity', 0.42);
          /* saída lateral: a parte de fora do nó, que sobe (ramo de cima) ou desce (ramo de baixo) e termina */
          var sa = cima ? yb - h : yc + hn, sb = cima ? yb - hn : yc + h;
          if (sb - sa < minT) { if (cima) sa = sb - minT; else sb = sa + minT; }
          var lift = Math.min(22, 6 + (sb - sa) * 0.12) * (cima ? -1 : 1);
          var xe = x + nodeW + passo * 0.46;
          var p = gSaidas.append('path').attr('d', faixa(x + nodeW, sa, sb, xe, sa + lift, sb + lift))
            .attr('fill', 'var(--fluxo-saida)').attr('class', 'prisma-saida');
          gSaidas.append('rect').attr('x', xe - 1).attr('y', Math.min(sa, sb) + lift).attr('width', 3).attr('height', Math.abs(sb - sa))
            .attr('rx', 1.5).attr('fill', 'var(--fluxo)').attr('fill-opacity', 0.5);
          /* rótulo da saída: número em negrito, descrição e detalhe quebrados na largura do passo */
          var fina = (sb - sa) < 34, lx = xe + 8, larg = passo * 0.92;
          var lin = (s.semSoma ? [] : [{ t: '− ' + fmtInt(s.n), c: 'forte' }]).concat(
            V.prisma._linhas(s.rot, larg, 'prisma-rot-saida', gRot).map(function (t) { return { t: t, c: s.semSoma ? 'forte' : '' }; }),
            s.det ? V.prisma._linhas(s.det, larg, 'prisma-rot-det', gRot).map(function (t) { return { t: t, c: 'det' }; }) : []);
          var altura = lin.length * 14;
          var ly = fina ? (cima ? sa + lift - altura - 2 : sb + lift + 16) : (sa + sb) / 2 + lift - altura / 2 + 10;
          var tt = gRot.append('text').attr('x', lx).attr('y', ly).attr('class', 'prisma-rot-saida');
          lin.forEach(function (l, j) {
            tt.append('tspan').attr('x', lx).attr('dy', j ? 14 : 0).attr('class', l.c === 'forte' ? 'forte' : l.c === 'det' ? 'det' : null).text(l.t);
          });
          [p.node()].forEach(function (n) {
            n.setAttribute('tabindex', '-1');
            V.dica.ligarHover(n, function () { return '<strong>' + (s.semSoma ? '' : fmtInt(s.n) + ' ') + s.rot + '</strong>' + (s.det ? '<span class="dica-sub">' + s.det + '</span>' : '') + '<span class="dica-sub">' + r.rotulo + '</span>'; });
          });
        } else {
          /* incluídos: converge para o nó final */
          var hf = esp(P.relatos), xf = xs[5], yfa = H / 2 - hf / 2;
          var parte = cima ? [yfa, yfa + esp(r.incluidos)] : [yfa + hf - esp(r.incluidos), yfa + hf];
          gFluxo.append('path').attr('d', faixa(x + nodeW, cima ? yb - h : yc, cima ? yb : yc + h, xf, parte[0], parte[1]))
            .attr('fill', 'var(--fluxo)').attr('fill-opacity', 0.55);
        }
      });
      /* rótulo da fonte, à esquerda */
      var h0 = esp(r.identificados), cy = cima ? yb - h0 / 2 : yc + h0 / 2;
      var tf = gRot.append('text').attr('x', ML - 14).attr('y', cy - 4).attr('text-anchor', 'end').attr('class', 'prisma-rot-fonte');
      tf.append('tspan').attr('class', 'forte').text(cima ? 'Bases' : 'Busca por citações');
      var sub = r.por_fonte.length ? r.por_fonte.map(function (f) { return f.fonte + ' ' + f.n_fmt; }).join(' · ') : 'bola de neve';
      tf.append('tspan').attr('x', ML - 14).attr('dy', 16).attr('class', 'fraco').text(sub);
    });
    /* nó final: relatos e estudos */
    var hf = esp(P.relatos), xf = xs[5];
    gNos.append('rect').attr('x', xf).attr('y', H / 2 - hf / 2).attr('width', nodeW).attr('height', hf).attr('rx', 1.5).attr('fill', 'var(--ink)');
    var fim = gRot.append('text').attr('x', xf + nodeW + 12).attr('y', H / 2 - 10).attr('class', 'prisma-rot-fim');
    fim.append('tspan').attr('class', 'enorme').text(fmtInt(P.relatos));
    fim.append('tspan').text(' relatos');
    var fim2 = gRot.append('text').attr('x', xf + nodeW + 12).attr('y', H / 2 + 22).attr('class', 'prisma-rot-fim');
    fim2.append('tspan').attr('class', 'enorme').text(fmtInt(P.estudos));
    fim2.append('tspan').text(' estudos');

  },
  _animado: false,
  animar: function () {
    if (V.prisma._animado) return;
    V.prisma._animado = true;
    if (V.prisma._clip) V.prisma._clip.transition().duration(V.dur(700)).ease(d3.easeCubicInOut).attr('width', V.prisma._W);
  },

  /* divide um texto em linhas que cabem na largura, medindo num <text> temporário */
  _linhas: function (texto, larg, classe, g) {
    var t = g.append('text').attr('class', classe).attr('x', -9999).attr('y', -9999);
    var palavras = texto.split(/\s+/), linhas = [], atual = [];
    palavras.forEach(function (p) {
      atual.push(p); t.text(atual.join(' '));
      if (t.node().getComputedTextLength() > larg && atual.length > 1) { atual.pop(); linhas.push(atual.join(' ')); atual = [p]; }
    });
    if (atual.length) linhas.push(atual.join(' '));
    t.remove();
    return linhas;
  },
  /* quebra um <text> em linhas de largura máxima */
  _quebrar: function (sel, x, larg) {
    sel.each(function () {
      var t = d3.select(this), tsp = t.selectAll('tspan');
      if (tsp.size() > 1) return;
      var palavras = t.text().split(/\s+/), linha = [], dy = 0;
      t.text(null);
      var ts = t.append('tspan').attr('x', x);
      palavras.forEach(function (p) {
        linha.push(p); ts.text(linha.join(' '));
        if (ts.node().getComputedTextLength() > larg && linha.length > 1) {
          linha.pop(); ts.text(linha.join(' ')); linha = [p];
          ts = t.append('tspan').attr('x', x).attr('dy', 14).text(p);
        }
      });
    });
  },

  /* celular: funil em barras, um ramo depois do outro */
  funil: function (alvo) {
    var P = V.D.prisma, max = Math.max(P.ramos[0].identificados, P.ramos[1].identificados), h = '';
    P.ramos.forEach(function (r) {
      var E = etapas(r), S = saidas(r);
      h += '<div class="funil-ramo"><p class="funil-titulo">' + V.esc(r.rotulo) + '</p><ol class="funil-lista">';
      E.forEach(function (e, i) {
        var w = Math.max(0.6, 100 * e.n / max);
        h += '<li class="funil-etapa"><span class="funil-barra" style="--w:' + w.toFixed(2) + '%"></span>' +
          '<span class="funil-num">' + fmtInt(e.n) + '</span> <span class="funil-rot">' + e.rot + '</span></li>';
        if (i < 4) h += '<li class="funil-saida">' + (S[i].semSoma ? '' : '<span class="funil-num">− ' + fmtInt(S[i].n) + '</span> ') + S[i].rot +
          (S[i].det ? '<span class="funil-det">' + V.esc(S[i].det) + '</span>' : '') + '</li>';
      });
      h += '</ol></div>';
    });
    h += '<p class="funil-fim"><span class="funil-num">' + fmtInt(P.relatos) + '</span> relatos · <span class="funil-num">' +
      fmtInt(P.estudos) + '</span> estudos</p>';
    alvo.innerHTML = h;
  },

  /* continuação: um ponto por estudo, das inclusões à síntese principal */
  continuacao: function () {
    var alvo = document.getElementById('prisma-estudos');
    if (!alvo) return;
    var F = V.D.prisma.fluxo_estudos, E = V.D.estudos, W = V.largura(alvo);
    var nome = function (ch) { return E[ch].rotulo; };
    var passos = [
      { n: F.estudos, rot: 'estudos incluídos' },
      { n: F.com_efeitos, rot: 'com efeitos extraídos', sai: [{ ch: F.sem_efeitos, rot: 'sem nenhum efeito extraído', cls: 'sem' }] },
      { n: F.com_principal, rot: 'com efeito principal', sai: [{ ch: F.sem_principal.filter(function (c) { return F.sem_efeitos.indexOf(c) < 0; }), rot: 'nenhum efeito principal', cls: 'sem' }] },
      { n: F.sintese, rot: 'na síntese principal', sai: [{ ch: F.criticos, rot: 'risco de viés crítico', cls: 'critico' }, { ch: F.so_fora, rot: 'efeitos principais fora da contagem', cls: 'fora' }] }
    ];
    var celular = W < 640, r = celular ? 3.6 : 5.5, gap = celular ? 2.6 : 3.5, passo = 2 * r + gap;
    var larguraPontos = celular ? W : Math.min(W * 0.58, F.estudos * passo);
    var porLinha = Math.max(8, Math.min(F.estudos, Math.floor(larguraPontos / passo)));
    var h = '<ol class="continuacao">';
    passos.forEach(function (p, i) {
      var linhas = Math.ceil(p.n / porLinha), hs = linhas * passo;
      var pontos = '';
      for (var j = 0; j < p.n; j++) {
        var cx = r + (j % porLinha) * passo, cy = r + Math.floor(j / porLinha) * passo;
        pontos += '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" style="--i:' + j + '"/>';
      }
      h += '<li class="cont-passo"><div class="cont-linha"><svg class="cont-pontos" width="' + (porLinha * passo) + '" height="' + hs +
        '" aria-hidden="true" focusable="false">' + pontos + '</svg><p class="cont-rot"><span class="cont-num">' + p.n + '</span> ' + p.rot + '</p></div>';
      if (p.sai) {
        h += '<ul class="cont-saidas">';
        p.sai.forEach(function (s) {
          var pts = '';
          s.ch.forEach(function (c, j) { pts += '<circle cx="' + (r + j * passo) + '" cy="' + r + '" r="' + r + '"/>'; });
          h += '<li class="cont-saida cont-' + s.cls + '"><svg width="' + (s.ch.length * passo) + '" height="' + (2 * r) +
            '" aria-hidden="true" focusable="false">' + pts + '</svg><span><strong>' + s.ch.length + '</strong> ' + s.rot + ': ' +
            s.ch.map(function (c) { return V.esc(nome(c)); }).join('; ') + '</span></li>';
        });
        h += '</ul>';
      }
      h += '</li>';
    });
    h += '</ol>';
    alvo.innerHTML = h;
  },

  alternar: function () {
    var b = document.getElementById('prisma-alternar'), fluxo = document.getElementById('prisma-fluxo-fig'),
      diag = document.getElementById('prisma-diagrama');
    if (!b || !diag) return;
    b.addEventListener('click', function () {
      var mostrar = diag.hidden;
      diag.hidden = !mostrar; fluxo.hidden = mostrar;
      b.setAttribute('aria-expanded', String(mostrar));
      b.querySelector('span').textContent = mostrar ? V.t('prisma.alternar_voltar') : V.t('prisma.alternar');
    });
  }
};
V.aoRedimensionar(function () { V.prisma.desenhar(); V.prisma.continuacao(); });
