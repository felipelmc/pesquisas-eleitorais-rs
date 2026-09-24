/* dados e textos embutidos pela montagem */
V.D = JSON.parse(document.getElementById('dados-vitrine').textContent);
V.T = JSON.parse(document.getElementById('textos-vitrine').textContent);
V.t = function (caminho) {
  var o = V.T;
  caminho.split('.').forEach(function (k) { o = o == null ? o : o[k]; });
  return o == null ? '' : o;
};
V.estudo = function (ch) { return V.D.estudos[ch]; };

/* fmt: formatação pt-BR, glifos de direção, selo de certeza e símbolos de risco de viés.
   Todos os números exibidos já vêm formatados de vitrine.json; aqui só há utilidades de desenho. */
var OPACIDADE = { 1: 0.35, 2: 0.55, 3: 0.8, 4: 1 };
var NIVEL_TXT = { 1: 'muito baixa', 2: 'baixa', 3: 'moderada', 4: 'alta' };
var uid = 0;

V.esc = function (s) {
  return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
  });
};
V.semTags = function (s) { return String(s || '').replace(/<[^>]+>/g, ''); };
V.num = function (x, d) {
  if (x == null || isNaN(x)) return 'NR';
  d = d == null ? 2 : d;
  var s = Math.abs(x).toFixed(d).split('.');
  s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  return (x < 0 ? '−' : '') + s.join(',');
};

/* glifo de direção em SVG: pos ▲, neg ▼, misto ◆ (metade azul, metade laranja), nulo ○, sem ─ */
V.glifo = function (tipo, opts) {
  opts = opts || {};
  var s = opts.tamanho || 16, n = opts.nivel || 4, op = opts.opacidade != null ? opts.opacidade : OPACIDADE[n];
  var r = s / 2, pad = 1.6, sw = opts.traco || 1.6;
  var a = ' class="glifo glifo-' + tipo + '" width="' + s + '" height="' + s + '" viewBox="0 0 ' + s + ' ' + s + '"';
  var rot = opts.rotulo ? ' role="img" aria-label="' + V.esc(opts.rotulo) + '"' : ' aria-hidden="true" focusable="false"';
  var corpo;
  if (tipo === 'pos') {
    corpo = '<polygon points="' + r + ',' + (pad + 0.5) + ' ' + (s - pad) + ',' + (s - pad - 1) + ' ' + pad + ',' + (s - pad - 1) +
      '" fill="var(--pos)" fill-opacity="' + op + '" stroke="var(--pos)" stroke-width="' + sw + '" stroke-linejoin="round"/>';
  } else if (tipo === 'neg') {
    corpo = '<polygon points="' + pad + ',' + (pad + 1) + ' ' + (s - pad) + ',' + (pad + 1) + ' ' + r + ',' + (s - pad - 0.5) +
      '" fill="var(--neg)" fill-opacity="' + op + '" stroke="var(--neg)" stroke-width="' + sw + '" stroke-linejoin="round"/>';
  } else if (tipo === 'misto') {
    var id = 'mc' + (++uid);
    var d = 'M' + r + ' ' + pad + ' L' + (s - pad) + ' ' + r + ' L' + r + ' ' + (s - pad) + ' L' + pad + ' ' + r + ' Z';
    corpo = '<defs><clipPath id="' + id + 'e"><rect x="0" y="0" width="' + r + '" height="' + s + '"/></clipPath>' +
      '<clipPath id="' + id + 'd"><rect x="' + r + '" y="0" width="' + r + '" height="' + s + '"/></clipPath></defs>' +
      '<path d="' + d + '" clip-path="url(#' + id + 'e)" fill="var(--pos)" fill-opacity="' + op + '" stroke="var(--pos)" stroke-width="' + (sw + 0.4) + '" stroke-linejoin="round"/>' +
      '<path d="' + d + '" clip-path="url(#' + id + 'd)" fill="var(--neg)" fill-opacity="' + op + '" stroke="var(--neg)" stroke-width="' + (sw + 0.4) + '" stroke-linejoin="round"/>';
  } else if (tipo === 'nulo') {
    corpo = '<circle cx="' + r + '" cy="' + r + '" r="' + (r - pad - 0.6) + '" fill="none" stroke="var(--nulo)" stroke-width="' + (sw + 0.6) + '"/>';
  } else {
    corpo = '<line x1="' + (pad + 2) + '" y1="' + r + '" x2="' + (s - pad - 2) + '" y2="' + r + '" stroke="var(--ink-3)" stroke-width="' + (sw + 0.4) + '" stroke-linecap="round"/>';
  }
  return '<svg' + a + rot + '>' + corpo + '</svg>';
};

/* selo de certeza: ⊕ preenchidos e ◯ vazios desenhados em SVG, sempre com a palavra */
V.selo = function (nivel, opts) {
  opts = opts || {};
  if (!nivel) return '<span class="selo selo-sem">' + V.esc(opts.semTexto || 'sem GRADE próprio') + '</span>';
  var r = opts.raio || 5, gap = 2.5, w = 4 * (2 * r) + 3 * gap + 2, h = 2 * r + 2, c = '';
  for (var i = 0; i < 4; i++) {
    var cx = 1 + r + i * (2 * r + gap), cy = 1 + r;
    if (i < nivel) {
      c += '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="var(--ink)" stroke="var(--ink)" stroke-width="1"/>' +
        '<path d="M' + (cx - r * 0.55) + ' ' + cy + 'H' + (cx + r * 0.55) + 'M' + cx + ' ' + (cy - r * 0.55) + 'V' + (cy + r * 0.55) +
        '" stroke="var(--bg)" stroke-width="1.4" stroke-linecap="round"/>';
    } else {
      c += '<circle cx="' + cx + '" cy="' + cy + '" r="' + (r - 0.5) + '" fill="none" stroke="var(--ink-3)" stroke-width="1"/>';
    }
  }
  var palavra = opts.semPalavra ? '' : '<span class="selo-palavra">' + (opts.prefixo ? V.esc(opts.prefixo) : '<span class="visualmente-oculto">certeza </span>') + NIVEL_TXT[nivel] + '</span>';
  return '<span class="selo selo-n' + nivel + '"><svg width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h +
    '" aria-hidden="true" focusable="false">' + c + '</svg>' + palavra + '</span>';
};
V.nivelTxt = function (n) { return NIVEL_TXT[n]; };
V.opacidade = function (n) { return OPACIDADE[n] || 1; };

/* símbolo de risco de viés no estilo robvis: + − × ! ? */
V.rob = function (r, opts) {
  opts = opts || {};
  if (!r) return '<span class="rob-vazio">NR</span>';
  var s = '<span class="rob-simbolo rob-n' + r.nivel + '" aria-hidden="true">' + V.esc(r.simbolo) + '</span>';
  if (opts.soSimbolo) return '<span class="rob" title="' + V.esc(r.ferramenta + ': ' + r.geral_rot) + '">' + s +
    '<span class="visualmente-oculto">' + V.esc(r.ferramenta + ': ' + r.geral_rot) + '</span></span>';
  return '<span class="rob">' + s + '<span class="rob-texto">' + V.esc(r.ferramenta + ': ' + r.geral_rot) + '</span></span>';
};

/* movimento: respeita prefers-reduced-motion e o botão "Reduzir animações" */
V.reduzido = function () {
  if (document.documentElement.getAttribute('data-movimento') === 'reduzido') return true;
  return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
};
V.dur = function (ms) { return V.reduzido() ? 0 : Math.min(ms == null ? 560 : ms, 700); };
V.atraso = function (i, passo) { return V.reduzido() ? 0 : Math.min(i * (passo || 20), 280); };

V.el = function (tag, attrs, html) {
  var e = document.createElement(tag);
  if (attrs) for (var k in attrs) if (attrs[k] != null) e.setAttribute(k, attrs[k]);
  if (html != null) e.innerHTML = html;
  return e;
};
V.ao = function (el, ev, fn) { if (el) el.addEventListener(ev, fn); };
V.largura = function (el) { return Math.max(0, Math.floor(el.getBoundingClientRect().width)); };
V.celular = function () { return window.matchMedia('(max-width: 767px)').matches; };
V.debounce = function (fn, ms) { var t; return function () { clearTimeout(t); t = setTimeout(fn, ms || 150); }; };

/* registra desenhos que dependem da largura para refazer no resize */
V._redesenhos = [];
V.aoRedimensionar = function (fn) { V._redesenhos.push(fn); };
