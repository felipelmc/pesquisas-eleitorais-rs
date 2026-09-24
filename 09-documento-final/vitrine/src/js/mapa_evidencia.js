/* mapa de evidências: 4 blocos × 2 classes de desenho; um símbolo por estudo em cada célula do protocolo,
   cor pela direção, preenchimento pela certeza; clique abre a gaveta com o enunciado literal e os estudos */
var CEL = {};
V.D.celulas.forEach(function (c) { CEL[c.id] = c; });

function glifoEstudo(c, e, tam) {
  var est = V.estudo(e.chave);
  return '<span class="mapa-glifo" data-cel="' + c.id + '" data-chave="' + e.chave + '">' +
    V.glifo(e.glifo, { nivel: c.nivel, tamanho: tam || 22, traco: 1.8 }) +
    '<span class="visualmente-oculto">' + V.esc(est.rotulo) + ': ' + V.semTags(e.direcao_rot) + '</span></span>';
}
function rotuloCelula(c) {
  var fam = c.familia === 'pesquisa_pre_eleitoral' ? '' : '<span class="mapa-fam">' + V.esc(c.familia_rot) + '</span> ';
  return fam + '<span class="mapa-comp">comparador:</span> ' + V.esc(c.comparador_rot);
}
function estudosDistintos(ids) {
  var s = {};
  ids.forEach(function (id) { CEL[id].estudos.forEach(function (e) { s[e.chave] = 1; }); });
  return Object.keys(s).length;
}

/* barra pequena com a proporção e o IC, escala 0 a 1 */
function miniIC(c) {
  if (c.proporcao == null) return '';
  var w = 220, h = 34, x = function (v) { return 10 + v * (w - 20); };
  return '<svg class="mini-ic" width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '" role="img" aria-label="proporção ' +
    c.proporcao_fmt + ', IC 95% ' + c.ic_fmt + '">' +
    '<line x1="' + x(0) + '" x2="' + x(1) + '" y1="12" y2="12" stroke="var(--grid)" stroke-width="6" stroke-linecap="round"/>' +
    '<line x1="' + x(0.5) + '" x2="' + x(0.5) + '" y1="4" y2="20" stroke="var(--ink-3)" stroke-width="1"/>' +
    '<line x1="' + x(c.ic[0]) + '" x2="' + x(c.ic[1]) + '" y1="12" y2="12" stroke="var(--ink)" stroke-width="2" stroke-linecap="round"/>' +
    '<circle cx="' + x(c.proporcao) + '" cy="12" r="5" fill="var(--ink)" stroke="var(--bg)" stroke-width="2"/>' +
    '<text x="' + x(0) + '" y="32" class="mini-ic-eixo">0</text><text x="' + x(0.5) + '" y="32" text-anchor="middle" class="mini-ic-eixo">0,5</text>' +
    '<text x="' + x(1) + '" y="32" text-anchor="end" class="mini-ic-eixo">1</text></svg>';
}

function detalheCelula(c) {
  var h = '<article class="g-celula">';
  h += '<header class="g-celula-cab"><h3>' + V.esc(c.familia_rot.charAt(0).toUpperCase() + c.familia_rot.slice(1)) +
    ' <span class="g-sep">·</span> ' + V.esc(c.comparador_rot) + '</h3>' + V.selo(c.nivel, { prefixo: 'certeza ' }) + '</header>';
  h += '<p class="g-rotulo">' + (V.t('gaveta.enunciado')) + '</p><blockquote class="g-enunciado">' + V.esc(c.enunciado) + '</blockquote>';
  h += '<dl class="g-numeros">';
  h += '<div><dt>' + (V.t('gaveta.contagem')) + '</dt><dd>' + c.contagem +
    (c.x_de_y ? ' <span class="g-fraco">(' + c.x_de_y + ' com direção definida)</span>' : '') + '</dd></div>';
  if (c.proporcao != null) {
    h += '<div><dt>' + (V.t('gaveta.ic')) + '</dt><dd>' + c.proporcao_fmt + ' <span class="g-fraco">(IC 95% ' + c.ic_fmt + ')</span>' + miniIC(c) + '</dd></div>';
  }
  h += '<div><dt>' + (V.t('gaveta.p')) + '</dt><dd>' + (c.p_fmt != null ? 'p = ' + c.p_fmt : (V.t('gaveta.sem_p'))) + '</dd></div>';
  h += '<div><dt>' + (V.t('gaveta.rebaixamentos')) + '</dt><dd class="g-chips">' +
    (c.rebaixamentos.length ? c.rebaixamentos.map(function (r) { return '<span class="g-chip">' + V.esc(r) + '</span>'; }).join('') : '<span class="g-chip">nenhum</span>') +
    '<span class="g-chip g-chip-fraco">' + (V.t('gaveta.partida')) + ': ' + V.esc(c.partida) + '</span></dd></div>';
  h += '<div><dt>' + (V.t('gaveta.caixa')) + '</dt><dd>' + V.esc(c.caixa) + '</dd></div>';
  h += '</dl>';
  h += '<p class="g-rotulo">' + V.t('gaveta.estudos') + ' (k = ' + c.k + ')</p><ul class="g-lista">';
  c.estudos.forEach(function (e) {
    var s = V.estudo(e.chave);
    h += '<li class="g-estudo"><span class="g-estudo-glifo">' + V.glifo(e.glifo, { nivel: c.nivel, tamanho: 18 }) + '</span>' +
      '<span class="g-estudo-corpo"><span class="g-estudo-nome">' + V.esc(s.rotulo) + '</span> <span class="g-estudo-dir">' + e.direcao_rot + '</span>' +
      '<span class="g-estudo-meta">' + V.esc(s.pais) + ' · ' + s.desenho + '</span>' +
      '<span class="g-estudo-meta">n = ' + e.n_fmt + (e.n_amostra != null ? ' ' + V.esc(s.unidade) : '') + ' · ' + V.rob(e.rob) + '</span></span></li>';
  });
  h += '</ul>';
  if (c.excluidos_critico.length) {
    h += '<p class="nota g-critico">' + (V.t('gaveta.critico')) + ' ' + c.excluidos_critico.map(function (ch) { return V.esc(V.estudo(ch).rotulo); }).join('; ') + '.</p>';
  }
  h += '</article>';
  return h;
}

V.mapa = {
  desenhar: function () {
    var alvo = document.getElementById('mapa-grade');
    if (!alvo) return;
    var h = '<div class="mapa-cabecalho" aria-hidden="true"><span></span>';
    V.D.blocos[0].classes.forEach(function (cl) { h += '<span>' + V.esc(cl.rotulo) + '</span>'; });
    h += '</div>';
    V.D.blocos.forEach(function (b) {
      var todos = [];
      b.classes.forEach(function (cl) { todos = todos.concat(cl.celulas); });
      h += '<div class="mapa-linha" data-bloco="' + b.id + '">';
      h += '<div class="mapa-bloco"><h3>' + b.rotulo + '</h3><p class="nota">' + estudosDistintos(todos) + ' estudos · ' + todos.length +
        (todos.length === 1 ? ' célula' : ' células') + '</p></div>';
      b.classes.forEach(function (cl) {
        var vaz = cl.vazias.map(function (i) { return V.D.vazias[i]; });
        if (!cl.celulas.length && !vaz.length) {
          h += '<div class="celula-mapa lacuna" data-bloco="' + b.id + '" data-classe="' + cl.classe + '"><span class="mapa-classe-rot">' + V.esc(cl.rotulo) +
            '</span><span class="lacuna-texto">' + (V.t('mapa.lacuna')) + '</span></div>';
          return;
        }
        var n = estudosDistintos(cl.celulas);
        var aria = V.semTags(b.rotulo) + ', ' + cl.rotulo.toLowerCase() + ': ' + n + ' estudos em ' + cl.celulas.length +
          (cl.celulas.length === 1 ? ' célula' : ' células') + '. ' + V.t('mapa.abrir') + '.';
        h += '<button type="button" class="celula-mapa" data-bloco="' + b.id + '" data-classe="' + cl.classe + '" aria-label="' + V.esc(aria) + '">';
        h += '<span class="mapa-classe-rot">' + V.esc(cl.rotulo) + '</span>';
        h += '<span class="mapa-subs">';
        cl.celulas.forEach(function (id, j) {
          var c = CEL[id];
          h += '<span class="mapa-sub" style="--j:' + j + '"><span class="mapa-sub-rot">' + rotuloCelula(c) + '</span>' +
            '<span class="mapa-glifos">' + c.estudos.map(function (e) { return glifoEstudo(c, e); }).join('') + '</span>' +
            '<span class="mapa-sub-selo">' + V.selo(c.nivel, { raio: 4.5 }) + '</span></span>';
        });
        vaz.forEach(function (v) {
          h += '<span class="mapa-sub mapa-sub-vazia"><span class="mapa-sub-rot"><span class="mapa-fam">' + V.esc(v.familia_rot) + '</span> <span class="mapa-comp">comparador:</span> ' + V.esc(v.comparador_rot) + '</span>' +
            '<span class="mapa-vazia-texto">' + (V.t('mapa.vazia')) + (v.excluidos_critico.length ? ' (' + v.excluidos_critico.length + ' com risco crítico, fora)' : '') + '</span></span>';
        });
        h += '</span><span class="mapa-abrir" aria-hidden="true">' + (V.t('mapa.abrir')) + '</span></button>';
      });
      h += '</div>';
    });
    alvo.innerHTML = h;
    alvo.querySelectorAll('button.celula-mapa').forEach(function (bt) {
      bt.addEventListener('click', function () { V.mapa.abrir(bt.getAttribute('data-bloco'), bt.getAttribute('data-classe'), bt); });
    });
    alvo.querySelectorAll('.mapa-glifo').forEach(function (g) {
      V.dica.ligarHover(g, function () {
        var c = CEL[g.getAttribute('data-cel')], ch = g.getAttribute('data-chave'), s = V.estudo(ch);
        var e = c.estudos.filter(function (x) { return x.chave === ch; })[0];
        return '<strong>' + V.esc(s.rotulo) + '</strong><span class="dica-sub">' + e.direcao_rot + ' · ' + V.esc(s.pais) + '</span>';
      });
    });
    if (!V.reduzido() && !V.mapa._animado) alvo.classList.add('mapa-animar');
  },
  _animado: false,
  animar: function () {
    V.mapa._animado = true;
    var alvo = document.getElementById('mapa-grade');
    if (alvo) alvo.classList.add('mapa-entrou');
  },
  abrir: function (bloco, classe, quem) {
    var b = V.D.blocos.filter(function (x) { return x.id === bloco; })[0];
    var cl = b.classes.filter(function (x) { return x.classe === classe; })[0];
    var titulo = '<small>' + V.esc(cl.rotulo) + '</small>' + b.rotulo;
    var corpo = cl.celulas.map(function (id) { return detalheCelula(CEL[id]); }).join('');
    cl.vazias.forEach(function (i) {
      var v = V.D.vazias[i];
      corpo += '<article class="g-celula g-vazia"><header class="g-celula-cab"><h3>' + V.esc(v.familia_rot.charAt(0).toUpperCase() + v.familia_rot.slice(1)) +
        ' <span class="g-sep">·</span> ' + V.esc(v.comparador_rot) + '</h3></header><p>' + (V.t('mapa.vazia')) + '. ' +
        (v.excluidos_critico.length ? (V.t('gaveta.critico')) + ' ' + v.excluidos_critico.map(function (ch) { return V.esc(V.estudo(ch).rotulo); }).join('; ') + '.' : '') + '</p></article>';
    });
    corpo += '<p class="g-rodape"><a class="botao" href="revisao.html#' + b.secao + '">' + (V.t('gaveta.artigo')) + ' →</a></p>' +
      '<p class="nota">' + (V.t('gaveta.validacao')) + ' ' + V.t('mapa.caixa_nota') + '</p>';
    V.gaveta.abrir(titulo, corpo, quem);
  },
  destacar: function (tipo) {
    var sel = tipo === 'lacuna' ? '.celula-mapa.lacuna' : '.celula-mapa[data-bloco="' + tipo + '"]';
    document.querySelectorAll(sel).forEach(function (el) {
      el.classList.remove('destaque'); void el.offsetWidth; el.classList.add('destaque');
    });
  }
};
