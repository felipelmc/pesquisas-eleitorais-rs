/* gaveta: <dialog> modal; Esc fecha e o foco volta para quem abriu */
var dlg = document.getElementById('gaveta');
var dlgTitulo = document.getElementById('gaveta-titulo');
var dlgCorpo = document.getElementById('gaveta-corpo');
var dlgFechar = document.getElementById('gaveta-fechar');
var origem = null;

V.dica.ligarHover = function (el, fn) {
  el.addEventListener('pointerenter', function (e) { if (e.pointerType !== 'touch') V.dica.mostrar(el, fn()); });
  el.addEventListener('pointerleave', function () { V.dica.esconder(); });
};

V.gaveta = {
  abrir: function (tituloHtml, corpoHtml, quem) {
    origem = quem || document.activeElement;
    dlgTitulo.innerHTML = tituloHtml;
    dlgCorpo.innerHTML = corpoHtml;
    dlgCorpo.scrollTop = 0;
    V.dica.esconder();
    if (typeof dlg.showModal === 'function') dlg.showModal(); else dlg.setAttribute('open', '');
    document.body.style.overflow = 'hidden';
    dlgFechar.focus();
  },
  fechar: function () {
    if (dlg.open && typeof dlg.close === 'function') dlg.close(); else { dlg.removeAttribute('open'); aoFechar(); }
  }
};
function aoFechar() {
  document.body.style.overflow = '';
  if (origem && origem.focus) { try { origem.focus({ preventScroll: true }); } catch (e) { origem.focus(); } }
  origem = null;
}
dlg.addEventListener('close', aoFechar);
dlgFechar.addEventListener('click', V.gaveta.fechar);
dlg.addEventListener('click', function (e) {
  /* clique no véu (fora do conteúdo) fecha */
  var r = dlg.getBoundingClientRect();
  if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) V.gaveta.fechar();
});
