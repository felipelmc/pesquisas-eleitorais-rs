/* pendências: a lista é estática (gerada na montagem); aqui só o medidor e a entrada escalonada dos cartões */
V.pendencias = {
  animar: function () {
    var sec = document.getElementById('pendencias');
    if (!sec || V.reduzido()) return;
    sec.querySelectorAll('.pend').forEach(function (p, i) {
      p.style.animationDelay = V.atraso(i, 15) + 'ms';
      p.classList.add('entra');
    });
    sec.querySelectorAll('.medidor-caixa').forEach(function (c, i) {
      c.style.animationDelay = V.atraso(i, 15) + 'ms';
      c.classList.add('entra');
    });
  }
};
