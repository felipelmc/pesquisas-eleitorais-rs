/* quão confiáveis: barras 100% por domínio, uma por ferramenta, no estilo robvis (símbolos + − × ! ?) */
V.robGrafico = {
  desenhar: function () {
    var alvo = document.getElementById('rob-grafico');
    if (!alvo) return;
    var h = '';
    V.D.rob.forEach(function (f) {
      h += '<div class="rob-ferr"><h3 class="rob-ferr-titulo">' + V.esc(f.ferramenta) + ' <span>· ' + f.n_resultados + ' resultados</span></h3><ul class="rob-linhas">' +
        '<li class="rob-linha rob-cab" aria-hidden="true"><span class="rob-rot"></span><span class="rob-escala"><span>0%</span><span>100%</span></span><span class="rob-des">desacordos A e B</span></li>';
      var linhas = f.dominios.map(function (d) { return { rot: d.rotulo, j: d.j, des: d.desacordos }; });
      linhas.push({ rot: V.semTags(V.t('rob.geral')), j: f.geral, geral: true });
      linhas.forEach(function (l, i) {
        var tot = l.j.reduce(function (a, b) { return a + b.n; }, 0);
        var desc = l.j.map(function (j) { return j.n + ' ' + j.rot; }).join(', ');
        h += '<li class="rob-linha' + (l.geral ? ' rob-geral' : '') + '"><span class="rob-rot">' + V.esc(l.rot) + '</span>' +
          '<span class="rob-barra" role="img" aria-label="' + V.esc(l.rot + ': ' + desc) + '" style="--i:' + i + '">';
        l.j.forEach(function (j) {
          var w = 100 * j.n / tot;
          h += '<span class="rob-seg rob-n' + j.nivel + '" style="flex-grow:' + j.n + '" data-dica="' + V.esc('<strong>' + V.esc(l.rot) + '</strong><span class="dica-sub">' + j.n + ' de ' + tot + ': ' + j.rot + '</span>') + '">' +
            (w >= 9 ? '<span class="rob-seg-sim" aria-hidden="true">' + V.esc(j.simbolo) + '</span>' : '') + '</span>';
        });
        h += '</span><span class="rob-des">' + (l.geral ? '' : (l.des ? l.des : '<span class="rob-zero">0</span>')) + '</span></li>';
      });
      h += '</ul></div>';
    });
    alvo.innerHTML = h;
    alvo.querySelectorAll('.rob-seg').forEach(function (s) {
      V.dica.ligarHover(s, function () { return s.getAttribute('data-dica'); });
    });
  }
};
