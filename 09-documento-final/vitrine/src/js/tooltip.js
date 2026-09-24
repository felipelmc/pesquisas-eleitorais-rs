/* dica: abre por hover e por foco; no toque, vira painel inferior */
var dica = document.getElementById('dica');
var painel = document.getElementById('painel-toque');
var painelCorpo = document.getElementById('painel-toque-corpo');
var painelFechar = document.getElementById('painel-toque-fechar');
var origemPainel = null;

function posicionar(alvo) {
  var r = alvo.getBoundingClientRect();
  dica.style.left = '0px'; dica.style.top = '0px';
  var d = dica.getBoundingClientRect();
  var x = r.left + r.width / 2 - d.width / 2;
  var y = r.top - d.height - 10;
  if (y < 48) y = r.bottom + 10;
  x = Math.max(8, Math.min(x, window.innerWidth - d.width - 8));
  dica.style.left = Math.round(x) + 'px';
  dica.style.top = Math.round(y) + 'px';
}

V.dica = {
  mostrar: function (alvo, html) {
    dica.innerHTML = html;
    dica.hidden = false;
    posicionar(alvo);
  },
  esconder: function () { dica.hidden = true; },
  painel: function (html, origem) {
    painelCorpo.innerHTML = html;
    painel.hidden = false;
    origemPainel = origem || null;
    painelFechar.focus();
  },
  fecharPainel: function () {
    painel.hidden = true;
    if (origemPainel && origemPainel.focus) origemPainel.focus();
    origemPainel = null;
  },
  /* liga a dica a um elemento; fn devolve o HTML */
  ligar: function (el, fn) {
    var toque = false;
    el.addEventListener('pointerdown', function (e) { toque = e.pointerType === 'touch'; });
    el.addEventListener('pointerenter', function (e) { if (e.pointerType !== 'touch') V.dica.mostrar(el, fn()); });
    el.addEventListener('pointerleave', function () { V.dica.esconder(); });
    el.addEventListener('focus', function () { if (!toque) V.dica.mostrar(el, fn()); });
    el.addEventListener('blur', function () { V.dica.esconder(); });
    el.addEventListener('click', function (e) {
      if (toque) { e.preventDefault(); V.dica.esconder(); V.dica.painel(fn(), el); }
      toque = false;
    });
  }
};
painelFechar.addEventListener('click', V.dica.fecharPainel);
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') { V.dica.esconder(); if (!painel.hidden) V.dica.fecharPainel(); }
});
window.addEventListener('scroll', function () { if (!dica.hidden) V.dica.esconder(); }, { passive: true });
