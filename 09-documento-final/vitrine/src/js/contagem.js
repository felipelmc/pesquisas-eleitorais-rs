/* contando a direção: proporção na direção positiva com IC de Clopper-Pearson, por célula,
   com um controle segmentado entre as células do protocolo e as análises de sensibilidade */
var atual = 'protocolo';
var BLOCO_NOME = {};
V.D.blocos.forEach(function (b) { BLOCO_NOME[b.id] = b.rotulo; });
BLOCO_NOME.outro = 'Apoio, outro alvo';

V.contagem = {
  iniciar: function () {
    var ctl = document.getElementById('contagem-controle');
    if (!ctl) return;
    var h = '';
    V.D.sensibilidades.forEach(function (a, i) {
      var n = a.grupos.filter(function (g) { return g.k > 0; }).length;
      h += '<button type="button" class="segmento" role="radio" aria-checked="' + (i === 0) + '" tabindex="' + (i === 0 ? 0 : -1) +
        '" data-id="' + a.id + '">' + a.rotulo + (a.id === 'protocolo' || a.id === 'amplo' ? ' <span class="segmento-n">(' + n + ')</span>' : '') +
        (a.post_hoc ? ' <span class="segmento-tag"><i lang="en">post hoc</i></span>' : '') + '</button>';
    });
    ctl.innerHTML = h;
    var bts = ctl.querySelectorAll('.segmento');
    function escolher(b, foco) {
      bts.forEach(function (x) { x.setAttribute('aria-checked', String(x === b)); x.tabIndex = x === b ? 0 : -1; });
      if (foco) b.focus();
      atual = b.getAttribute('data-id');
      V.contagem.desenhar(true);
    }
    bts.forEach(function (b, i) {
      b.addEventListener('click', function () { escolher(b, false); });
      b.addEventListener('keydown', function (e) {
        var j = null;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') j = (i + 1) % bts.length;
        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') j = (i - 1 + bts.length) % bts.length;
        if (j !== null) { e.preventDefault(); escolher(bts[j], true); }
      });
    });
    V.contagem.desenhar(false);
  },
  desenhar: function (anunciar) {
    var alvo = document.getElementById('contagem-grafico');
    if (!alvo) return;
    var a = V.D.sensibilidades.filter(function (x) { return x.id === atual; })[0];
    var W = V.largura(alvo), estreito = W < 640;
    var nota = document.getElementById('contagem-nota');
    var notas = [];
    if (a.post_hoc) notas.push(V.t('contagem.post_hoc'));
    if (a.id === 'real') notas.push(V.t('contagem.nota_real'));
    if (!a.grade) notas.push(V.t('contagem.nota_sem_grade'));
    nota.innerHTML = notas.map(function (n) { return '<span>' + n + '</span>'; }).join(' ');
    nota.hidden = !notas.length;

    var LR = estreito ? 0 : Math.min(250, W * 0.3), LD = estreito ? 0 : (a.grade ? 235 : 120);
    var x0 = LR + 8, x1 = W - LD - 12;
    if (estreito) { x0 = 10; x1 = W - 10; }
    var x = function (v) { return x0 + v * (x1 - x0); };
    var linhaH = estreito ? 92 : 42, cabH = estreito ? 34 : 30, topo = 30;
    var blocoAnt = null, y = topo, itens = [];
    a.grupos.forEach(function (g) {
      if (g.bloco !== blocoAnt) { itens.push({ cab: true, bloco: g.bloco, y: y }); y += cabH; blocoAnt = g.bloco; }
      itens.push({ g: g, y: y }); y += linhaH;
    });
    var H = y + 34;
    var s = '<svg class="contagem-svg" width="' + W + '" height="' + H + '" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-labelledby="contagem-legenda">';
    /* grade e linha de empate (no celular, só marcas curtas em cada linha) */
    [0, 0.25, 0.5, 0.75, 1].forEach(function (v) {
      if (!estreito) s += '<line x1="' + x(v) + '" x2="' + x(v) + '" y1="' + (topo - 8) + '" y2="' + (H - 26) + '" stroke="' + (v === 0.5 ? 'var(--ink-3)' : 'var(--grid)') + '" stroke-width="1"/>';
      s += '<text class="eixo" x="' + x(v) + '" y="' + (H - 8) + '" text-anchor="' + (estreito && v === 0 ? 'start' : estreito && v === 1 ? 'end' : 'middle') + '">' + V.num(v, v === 0 || v === 1 ? 0 : 2) + '</text>';
    });
    s += '<text class="eixo eixo-titulo" x="' + x(0) + '" y="' + (topo - 14) + '">' + V.semTags(V.t('contagem.eixo')) + '</text>';
    itens.forEach(function (it, i) {
      if (it.cab) {
        s += '<text class="contagem-bloco" x="' + (estreito ? x0 : 0) + '" y="' + (it.y + 18) + '"' + (it.bloco === 'momentum' ? ' font-style="italic"' : '') + '>' + V.semTags(BLOCO_NOME[it.bloco]) + '</text>';
        return;
      }
      var g = it.g, yc = estreito ? it.y + 48 : it.y + 17;
      var prot = a.id === 'protocolo';
      var partes = V.semTags(g.rotulo).split(' · ');
      var rot = prot ? partes[partes.length - 1] : g.classe_rot;
      var fam = prot && partes.length > 1 && partes[0] !== 'Pesquisa pré-eleitoral' ? partes[0].toLowerCase() + ' · ' : '';
      var sub = prot ? fam + g.classe_rot.toLowerCase() : '';
      var ly = estreito ? it.y + 14 : yc + (sub ? -1 : 4);
      s += '<g class="contagem-linha" style="--i:' + i + '">';
      if (estreito) {
        s += '<line x1="' + x(0) + '" x2="' + x(1) + '" y1="' + yc + '" y2="' + yc + '" stroke="var(--grid)" stroke-width="1"/>';
        [0, 0.5, 1].forEach(function (v) { s += '<line x1="' + x(v) + '" x2="' + x(v) + '" y1="' + (yc - 7) + '" y2="' + (yc + 7) + '" stroke="' + (v === 0.5 ? 'var(--ink-3)' : 'var(--line-2)') + '" stroke-width="1"/>'; });
      }
      s += '<text class="contagem-rot" x="' + (estreito ? x0 : LR) + '" y="' + ly + '"' + (estreito ? '' : ' text-anchor="end"') + '>' + V.esc(rot) +
        (sub ? '<tspan class="contagem-sub" x="' + (estreito ? x0 : LR) + '" dy="14">' + V.esc(sub) + '</tspan>' : '') + '</text>';
      if (g.proporcao != null) {
        s += '<line class="ic" x1="' + x(g.ic[0]) + '" x2="' + x(g.ic[1]) + '" y1="' + yc + '" y2="' + yc + '" stroke="var(--ink-2)" stroke-width="1.6" stroke-linecap="round"/>' +
          '<circle class="ponto" cx="' + x(g.proporcao) + '" cy="' + yc + '" r="5.5" fill="var(--ink)" stroke="var(--card)" stroke-width="2"/>';
      } else if (g.k > 0) {
        s += '<circle cx="' + x(0.5) + '" cy="' + yc + '" r="5.5" fill="none" stroke="var(--nulo)" stroke-width="2"/>' +
          '<text class="contagem-vazio" x="' + (estreito ? x(0.5) + 12 : x(0.5) - 12) + '" y="' + (yc + 4) + '"' + (estreito ? '' : ' text-anchor="end"') + '>' + V.semTags(V.t('contagem.so_nulo')) + '</text>';
      } else {
        s += '<text class="contagem-vazio" x="' + x(0.5) + '" y="' + (yc + 4) + '" text-anchor="middle">' + V.semTags(V.t('contagem.sem_estudo')) + '</text>';
      }
      var info = g.k ? 'k = ' + g.k + (g.p_fmt != null ? ' · p = ' + g.p_fmt : '') : '';
      if (estreito) {
        s += '<text class="contagem-info" x="' + x0 + '" y="' + (it.y + 74) + '">' + info + '</text>';
      } else {
        s += '<text class="contagem-info" x="' + (x1 + 16) + '" y="' + (yc + 4) + '">' + info + '</text>';
      }
      s += '</g>';
    });
    s += '</svg>';
    /* selos (HTML sobreposto, porque o selo é HTML com palavra) */
    var selos = '';
    if (a.grade) {
      itens.forEach(function (it) {
        if (it.cab || !it.g.nivel) return;
        var yc = estreito ? it.y + 70 : it.y + 17;
        selos += '<span class="contagem-selo' + (estreito ? ' estreito' : '') + '" style="top:' + (yc - 9) + 'px;' + (estreito ? 'right:10px' : 'left:' + (x1 + 122) + 'px') + '">' +
          V.selo(it.g.nivel, { raio: 4 }) + '</span>';
      });
    }
    alvo.innerHTML = '<div class="contagem-camadas">' + s + selos + '</div>';
    alvo.setAttribute('data-analise', a.id);
    if (anunciar && !V.reduzido()) {
      alvo.querySelectorAll('.contagem-linha').forEach(function (l, i) { l.style.animationDelay = V.atraso(i, 14) + 'ms'; l.classList.add('entra'); });
    }
    V.contagem.tabela(a);
    if (anunciar) document.getElementById('vivo').textContent = V.semTags(a.rotulo) + ': ' + a.grupos.length + ' grupos.';
  },
  tabela: function (a) {
    var t = document.getElementById('contagem-tabela-corpo');
    if (!t) return;
    t.innerHTML = a.grupos.map(function (g) {
      return '<tr><td>' + V.esc(V.semTags(BLOCO_NOME[g.bloco])) + '</td><td>' + V.esc(V.semTags(g.rotulo)) + '</td><td>' + V.esc(g.classe_rot) + '</td>' +
        '<td class="num">' + g.k + '</td><td class="num">' + g.n_pos + '</td><td class="num">' + g.n_neg + '</td><td class="num">' + g.n_mistos + '</td><td class="num">' + g.n_nulos + '</td>' +
        '<td class="num">' + (g.ic_fmt || 'NR') + '</td><td class="num">' + (g.p_fmt || 'NR') + '</td><td>' + (g.certeza_rot || V.t('contagem.sem_grade')) + '</td></tr>';
    }).join('');
    document.getElementById('contagem-tabela-titulo').textContent = V.semTags(a.rotulo);
  }
};
V.aoRedimensionar(function () { V.contagem.desenhar(false); });
