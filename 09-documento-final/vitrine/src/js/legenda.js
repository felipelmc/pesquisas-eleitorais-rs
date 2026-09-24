/* legenda de leitura: glifos de direção, selo de certeza e símbolos de risco de viés (fixa ao lado no desktop) */
V.legenda = {
  desenhar: function () {
    var el = document.getElementById('legenda-leitura');
    if (!el) return;
    var dir = [
      ['pos', '<i lang="en">bandwagon</i>, viabilidade, a favor, mobilização'],
      ['neg', '<i lang="en">underdog</i>, contra, desmobilização'],
      ['misto', 'misto'],
      ['nulo', 'nulo ou trivial (IC dentro de ±δ)']
    ];
    var h = '<h2 id="titulo-legenda">' + V.t('legenda_leitura.titulo') + '</h2><div class="legenda-grupos">';
    h += '<div><h3>' + V.t('legenda_leitura.direcao') + '</h3><ul>';
    dir.forEach(function (d) { h += '<li>' + V.glifo(d[0], { nivel: 4 }) + '<span>' + d[1] + '</span></li>'; });
    h += '</ul></div>';
    h += '<div><h3>' + V.t('legenda_leitura.certeza') + '</h3><ul>';
    [4, 3, 2, 1].forEach(function (n) {
      h += '<li>' + V.selo(n, { prefixo: ' ' }) + '<span class="legenda-amostra">' + V.glifo('pos', { nivel: n, tamanho: 14 }) + '</span></li>';
    });
    h += '</ul><p class="nota">' + V.t('legenda_leitura.certeza_nota') + '</p></div>';
    h += '<div><h3>' + V.t('legenda_leitura.rob') + '</h3><ul>';
    [[1, '+', 'baixo'], [2, '−', 'algumas preocupações ou moderado'], [2, '?', 'incerto (EPOC)'], [3, '×', 'alto ou grave'], [4, '!', 'crítico']].forEach(function (r) {
      h += '<li><span class="rob-simbolo rob-n' + r[0] + '" aria-hidden="true">' + r[1] + '</span><span>' + r[2] + '</span></li>';
    });
    h += '</ul></div></div>';
    el.innerHTML = h;
  }
};
