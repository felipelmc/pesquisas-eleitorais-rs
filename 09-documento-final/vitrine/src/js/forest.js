/* de quanto: as duas metas exploratórias como forest pequenos, com faixa ±δ e losango vazado.
   Nada é estimado aqui: os IC por efeito e a estimativa combinada vêm de vitrine.json. */
V.forest = {
  desenhar: function () {
    V.D.metas.forEach(function (m) {
      var alvo = document.getElementById('forest-' + m.id);
      if (!alvo) return;
      var W = V.largura(alvo), estreito = W < 420;
      var LR = estreito ? 0 : Math.min(215, W * 0.44), passo = estreito ? 44 : 30, topo = 12;
      var n = m.efeitos.length, yDiam = topo + n * passo + (estreito ? 40 : 22), H = yDiam + 52;
      var lo = d3.min(m.efeitos, function (e) { return e.lo; }), hi = d3.max(m.efeitos, function (e) { return e.hi; });
      lo = Math.min(lo, m.ic[0], -0.5); hi = Math.max(hi, m.ic[1], 0.5);
      var x = d3.scaleLinear().domain([lo, hi]).nice(5).range([estreito ? 10 : LR + 10, W - 14]);
      var s = '<svg width="' + W + '" height="' + H + '" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-labelledby="forest-legenda forest-titulo-' + m.id + '">';
      /* faixa ±δ e zero */
      s += '<rect x="' + x(-m.delta) + '" y="' + (topo - 6) + '" width="' + Math.max(2, x(m.delta) - x(-m.delta)) + '" height="' + (yDiam - topo + 22) +
        '" fill="var(--nulo)" fill-opacity="0.22"/>';
      x.ticks(5).forEach(function (t) {
        s += '<line x1="' + x(t) + '" x2="' + x(t) + '" y1="' + (topo - 6) + '" y2="' + (yDiam + 16) + '" stroke="' + (t === 0 ? 'var(--ink-3)' : 'var(--grid)') + '" stroke-width="1"/>' +
          '<text class="eixo" x="' + x(t) + '" y="' + (yDiam + 34) + '" text-anchor="middle">' + V.num(t, t % 1 ? 1 : 0) + '</text>';
      });
      s += '<text class="eixo eixo-titulo" x="' + (W - 14) + '" y="' + (H - 2) + '" text-anchor="end">g de Hedges</text>';
      m.efeitos.forEach(function (e, i) {
        var y = topo + i * passo + passo / 2;
        var rot = V.esc(e.rotulo) + ' · ' + e.efeito;
        if (estreito) s += '<text class="forest-rot" x="10" y="' + (y - 11) + '">' + rot + '</text>';
        else s += '<text class="forest-rot" x="' + LR + '" y="' + (y + 4) + '" text-anchor="end">' + rot + '</text>';
        var yy = estreito ? y + 4 : y;
        s += '<g class="forest-efeito" style="--i:' + i + '"><line x1="' + x(Math.max(e.lo, x.domain()[0])) + '" x2="' + x(Math.min(e.hi, x.domain()[1])) + '" y1="' + yy + '" y2="' + yy +
          '" stroke="var(--ink-2)" stroke-width="1.6" stroke-linecap="round"/>' +
          '<rect x="' + (x(e.yi) - 5) + '" y="' + (yy - 5) + '" width="10" height="10" fill="var(--' + (e.yi >= 0 ? 'pos' : 'neg') + ')" stroke="var(--card)" stroke-width="2" rx="1.5"/></g>';
      });
      /* estimativa combinada: losango vazado */
      var yd = yDiam;
      s += '<line x1="' + (estreito ? 10 : 0) + '" x2="' + W + '" y1="' + (yd - (estreito ? 30 : 16)) + '" y2="' + (yd - (estreito ? 30 : 16)) + '" stroke="var(--line)" stroke-width="1"/>';
      s += '<text class="forest-rot forte" x="' + (estreito ? 10 : LR) + '" y="' + (estreito ? yd - 12 : yd + 4) + '"' + (estreito ? '' : ' text-anchor="end"') + '>combinada</text>';
      s += '<path d="M' + x(m.ic[0]) + ',' + yd + 'L' + x(m.g) + ',' + (yd - 7) + 'L' + x(m.ic[1]) + ',' + yd + 'L' + x(m.g) + ',' + (yd + 7) +
        'Z" fill="var(--card)" stroke="var(--ink)" stroke-width="1.8" stroke-linejoin="round"/>';
      s += '</svg>';
      alvo.innerHTML = s;
    });
  }
};
V.aoRedimensionar(function () { V.forest.desenhar(); });
