/* herói: contadores que rodam uma vez e 41 pontos neutros ao fundo (um por estudo, sem cor de direção) */
function formatarInteiro(n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }

V.heroi = {
  contar: function () {
    var alvos = document.querySelectorAll('[data-contar]');
    if (V.reduzido() || typeof d3 === 'undefined') return;
    var dur = 900, t0 = null;
    var itens = Array.prototype.map.call(alvos, function (el) {
      return { el: el, fim: +el.getAttribute('data-contar'), txt: el.textContent };
    });
    itens.forEach(function (it) { it.el.textContent = '0'; });
    function passo(ts) {
      if (t0 === null) t0 = ts;
      var k = Math.min(1, (ts - t0) / dur), e = d3.easeCubicInOut(k);
      itens.forEach(function (it) { it.el.textContent = k >= 1 ? it.txt : formatarInteiro(it.fim * e); });
      if (k < 1) requestAnimationFrame(passo);
    }
    requestAnimationFrame(passo);
  },
  pontos: function () {
    if (typeof d3 === 'undefined') return;
    var svg = document.querySelector('.heroi-pontos');
    if (!svg) return;
    var sec = svg.parentNode, w = sec.clientWidth, h = sec.clientHeight;
    /* o círculo fica ao lado do parágrafo de abertura, sem tocar no título nem nos contadores;
       sem espaço para ele, os pontos vão para a faixa abaixo dos contadores */
    var rs = sec.getBoundingClientRect(), caixa = function (sel) { var r = sec.querySelector(sel).getBoundingClientRect(); return { l: r.left - rs.left, r: r.right - rs.left, t: r.top - rs.top, b: r.bottom - rs.top }; };
    var ti = caixa('h1'), le = caixa('.heroi-lede'), co = caixa('.contadores'), ct = caixa('.heroi-conteudo');
    var dir = ct.r - parseFloat(getComputedStyle(sec.querySelector('.heroi-conteudo')).paddingRight);
    var raio = Math.min(190, (dir - le.r) / 2 - 60, (co.t - ti.b) / 2 - 40);
    var n = V.D.heroi.pontos;
    if (window.innerWidth < 1024 || raio < 110) {
      svg.classList.add('oculto'); document.querySelector('.heroi-faixa').classList.add('ativa');
      return V.heroi.faixa();
    }
    svg.classList.remove('oculto'); document.querySelector('.heroi-faixa').classList.remove('ativa');
    var cx = (le.r + dir) / 2 + 12, cy = (ti.b + co.t) / 2, rp = 6.5;
    var ouro = Math.PI * (3 - Math.sqrt(5));
    var pts = d3.range(n).map(function (i) {
      var r = raio * Math.sqrt((i + 0.5) / n), a = i * ouro;
      return { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a), i: i };
    });
    var s = d3.select(svg).attr('viewBox', null);
    s.selectAll('*').remove();
    var g = s.append('g');
    g.append('circle').attr('cx', cx).attr('cy', cy).attr('r', raio + rp * 3.2)
      .attr('fill', 'none').attr('stroke', 'var(--line)').attr('stroke-width', 1);
    var c = g.selectAll('circle.p').data(pts).join('circle').attr('class', 'p')
      .attr('fill', 'var(--ink-3)').attr('fill-opacity', 0.5).attr('r', rp);
    var jaFoi = V.heroi._desenhado; V.heroi._desenhado = true;
    if (V.reduzido() || jaFoi) { c.attr('cx', function (d) { return d.x; }).attr('cy', function (d) { return d.y; }); return; }
    c.attr('cx', cx).attr('cy', cy).attr('r', 0)
      .transition().delay(function (d) { return V.atraso(d.i, 6); }).duration(600).ease(d3.easeCubicInOut)
      .attr('cx', function (d) { return d.x; }).attr('cy', function (d) { return d.y; }).attr('r', rp);
  }
};
/* celular e tablet: os mesmos pontos numa faixa abaixo dos contadores */
V.heroi.faixa = function () {
  var svg = document.querySelector('.heroi-faixa');
  if (!svg) return;
  var n = V.D.heroi.pontos, w = svg.getBoundingClientRect().width || 320;
  var porLinha = Math.min(n, Math.max(10, Math.floor((w + 3) / 11))), linhas = Math.ceil(n / porLinha);
  var passo = Math.min(16, w / porLinha), r = Math.min(5, passo * 0.36), h = linhas * passo;
  var s = d3.select(svg).attr('viewBox', '0 0 ' + w + ' ' + h).attr('height', h);
  s.selectAll('*').remove();
  var c = s.selectAll('circle').data(d3.range(n)).join('circle')
    .attr('cx', function (i) { return r + (i % porLinha) * passo; }).attr('cy', function (i) { return r + Math.floor(i / porLinha) * passo; })
    .attr('fill', 'var(--ink-3)').attr('fill-opacity', 0.55).attr('r', r);
  var jaFoi = V.heroi._faixaFeita; V.heroi._faixaFeita = true;
  if (!V.reduzido() && !jaFoi) c.attr('r', 0).transition().delay(function (i) { return V.atraso(i, 6); }).duration(500).attr('r', r);
};
V.aoRedimensionar(function () { V.heroi.pontos(); });
