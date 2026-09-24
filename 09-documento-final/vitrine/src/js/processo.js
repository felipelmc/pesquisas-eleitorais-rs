/* o método em 60 segundos: eixo do tempo com as raias Humano, IA e Script, mais as emendas do protocolo.
   A raia de cada evento vem de vitrine.json (ator.id do log, corrigido por correcao_atribuicao.csv). */
var DIA = 86400;
var MESES = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'];
function diaUTC(iso) { return Date.UTC(+iso.slice(0, 4), +iso.slice(5, 7) - 1, +iso.slice(8, 10)) / 1000; }
function rotDia(t) { var d = new Date(t * 1000); return d.getUTCDate() + ' ' + MESES[d.getUTCMonth()]; }
function hora(t) { var d = new Date(t * 1000); return ('0' + d.getUTCHours()).slice(-2) + 'h' + ('0' + d.getUTCMinutes()).slice(-2); }

V.processo = {
  desenhar: function () {
    var alvo = document.getElementById('processo-grafico');
    if (!alvo) return;
    var P = V.D.processo, W = V.largura(alvo);
    var fig = alvo.closest('figure');
    if (fig) fig.classList.toggle('modo-lista', W < 700);
    if (W < 700) return V.processo.lista(alvo);
    var dias = P.dias_com_evento.map(diaUTC);
    /* segmentos: um por dia com evento; dias vazios entre eles viram um intervalo estreito */
    var LR = 92, R = W - 16, gapW = 64, nGaps = 0;
    for (var i = 1; i < dias.length; i++) if (dias[i] - dias[i - 1] > DIA) nGaps++;
    var diaW = (R - LR - nGaps * gapW) / dias.length;
    var segs = [], x = LR;
    dias.forEach(function (d, i) {
      if (i > 0 && d - dias[i - 1] > DIA) { segs.push({ gap: true, x: x, w: gapW, de: dias[i - 1] + DIA, ate: d - DIA }); x += gapW; }
      segs.push({ t0: d, x: x, w: diaW }); x += diaW;
    });
    var xt = function (t) {
      for (var j = 0; j < segs.length; j++) {
        var s = segs[j];
        if (!s.gap && t >= s.t0 && t < s.t0 + DIA) return s.x + (t - s.t0) / DIA * s.w;
      }
      return null;
    };
    var raias = [['humano', V.t('processo.raias.humano')], ['ia', V.t('processo.raias.ia')], ['script', V.t('processo.raias.script')], ['emendas', V.t('processo.raias.emendas')]];
    var topo = 56, rh = 58, H = topo + raias.length * rh + 30;
    var yR = {}; raias.forEach(function (r, k) { yR[r[0]] = topo + k * rh + rh / 2; });
    var s = '<svg width="' + W + '" height="' + H + '" viewBox="0 0 ' + W + ' ' + H + '" role="group" aria-labelledby="processo-legenda">';
    /* sessão de 23 e 24/09 */
    var ini = dias.filter(function (d) { return d >= diaUTC('2026-09-23'); })[0];
    if (ini != null) {
      var xs0 = xt(ini), xs1 = R;
      s += '<rect x="' + xs0 + '" y="' + (topo - 8) + '" width="' + (xs1 - xs0) + '" height="' + (raias.length * rh + 8) + '" fill="var(--aviso-bg)" rx="8"/>';
      s += '<foreignObject x="' + (xs0 + 8) + '" y="0" width="' + (xs1 - xs0 - 12) + '" height="' + (topo - 10) + '"><div xmlns="http://www.w3.org/1999/xhtml" class="processo-sessao">' + V.t('processo.sessao') + '</div></foreignObject>';
    }
    /* raias e eixo */
    raias.forEach(function (r) {
      var y = yR[r[0]];
      s += '<line x1="' + LR + '" x2="' + R + '" y1="' + y + '" y2="' + y + '" stroke="var(--grid)" stroke-width="1"/>';
      s += '<text class="processo-raia processo-raia-' + r[0] + '" x="' + (LR - 14) + '" y="' + (y + 4) + '" text-anchor="end">' + V.semTags(r[1]) + '</text>';
    });
    segs.forEach(function (sg) {
      if (sg.gap) {
        s += '<rect x="' + (sg.x + 6) + '" y="' + topo + '" width="' + (sg.w - 12) + '" height="' + (raias.length * rh - 8) + '" fill="url(#hachura-processo)"/>' +
          '<text class="eixo" x="' + (sg.x + sg.w / 2) + '" y="' + (H - 8) + '" text-anchor="middle">' + rotDia(sg.de).split(' ')[0] + '–' + rotDia(sg.ate) + '</text>';
        return;
      }
      s += '<line x1="' + sg.x + '" x2="' + sg.x + '" y1="' + (topo - 4) + '" y2="' + (H - 24) + '" stroke="var(--line)" stroke-width="1"/>' +
        '<text class="eixo eixo-dia" x="' + (sg.x + 6) + '" y="' + (H - 8) + '">' + rotDia(sg.t0) + '</text>';
    });
    s += '<defs><pattern id="hachura-processo" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="var(--hachura)" stroke-width="3"/></pattern></defs>';
    /* eventos do log (portões e emendas): eventos muito próximos na mesma raia viram um grupo com um só rótulo */
    var marcas = '';
    ['humano', 'ia'].forEach(function (raia) {
      var evs = P.eventos.map(function (e, k) { return { e: e, k: k, x: xt(e.t) }; })
        .filter(function (o) { return o.e.raia === raia && o.x != null; }).sort(function (a, b) { return a.x - b.x; });
      var grupos = [];
      evs.forEach(function (o) {
        var g = grupos[grupos.length - 1];
        if (g && o.x - g[g.length - 1].x < 22) g.push(o); else grupos.push([o]);
      });
      var y = yR[raia], ultimoFim = -1e9, fileira = 0;
      grupos.forEach(function (g) {
        var cx = g.reduce(function (a, o) { return a + o.x; }, 0) / g.length;
        var nomes = g.map(function (o) { return o.e.rotulo.split(':')[0]; });
        var rot = nomes.length > 1 ? nomes.slice(0, -1).join(', ') + ' e ' + nomes[nomes.length - 1] : nomes[0];
        var larg = rot.length * 6.6 + 6;
        fileira = (cx - larg / 2 < ultimoFim + 6) ? fileira + 1 : 0;
        ultimoFim = cx + larg / 2;
        var ly = y - 14 - fileira * 14;
        g.forEach(function (o, j) {
          var xx = cx + (j - (g.length - 1) / 2) * 14, e = o.e;
          var cor = e.raia === 'humano' ? 'var(--humano)' : 'var(--ia)';
          marcas += '<g class="processo-evento" tabindex="0" role="img" aria-label="' + V.esc(e.rotulo + ', ' + rotDia(e.t) + ' ' + hora(e.t) + ' UTC, ' + V.semTags(V.t('processo.raias.' + e.raia))) + '" data-k="' + o.k + '">' +
            (e.tipo === 'portao' ? '<circle cx="' + xx + '" cy="' + y + '" r="6" fill="' + cor + '" stroke="var(--card)" stroke-width="2"/>' :
              '<rect x="' + (xx - 5.5) + '" y="' + (y - 5.5) + '" width="11" height="11" transform="rotate(45 ' + xx + ' ' + y + ')" fill="' + cor + '" stroke="var(--card)" stroke-width="2"/>') +
            (e.gravado_humano && e.raia !== 'humano' ? '<circle cx="' + xx + '" cy="' + y + '" r="10" fill="none" stroke="var(--humano)" stroke-width="1.4" stroke-dasharray="2 2.4"/>' : '') +
            '</g>';
        });
        marcas += '<text class="processo-rot" x="' + cx + '" y="' + ly + '" text-anchor="middle">' + V.esc(rot) + '</text>';
      });
    });
    P.scripts.forEach(function (sc, k) {
      var xx = xt(sc.t), y = yR.script;
      if (xx == null) return;
      marcas += '<g class="processo-evento processo-script" tabindex="0" role="img" aria-label="' + V.esc(sc.rotulo + ', ' + rotDia(sc.t) + ' ' + hora(sc.t) + ' UTC, script') + '" data-script="' + k + '"><rect x="' + (xx - 5) + '" y="' + (y - 5) + '" width="10" height="10" fill="var(--card)" stroke="var(--script)" stroke-width="2"/></g>';
    });
    /* emendas registradas só no protocolo: por dia, sem hora */
    var porDia = {};
    P.emendas.forEach(function (e) { (porDia[e.data] = porDia[e.data] || []).push(e); });
    Object.keys(porDia).forEach(function (d) {
      var t0 = diaUTC(d), xx = xt(t0 + DIA / 2), y = yR.emendas, lista = porDia[d];
      if (xx == null) return;
      var ids = lista.map(function (e) { return e.id.replace('Emenda ', ''); });
      var rot = lista[0].id.indexOf('Emenda') === 0 ? (lista.length > 1 ? 'Emendas ' + ids.join(', ') : 'Emenda ' + ids[0]) : ids.join(', ');
      rot = rot.replace(/, (\S+)$/, ' e $1');
      var sg = segs.filter(function (q) { return !q.gap && q.t0 === t0; })[0];
      marcas += '<g class="processo-evento processo-emenda" tabindex="0" role="img" aria-label="' + V.esc(rot + ', ' + rotDia(t0)) + '" data-dia="' + d + '"><line x1="' + (sg.x + 6) + '" x2="' + (sg.x + sg.w - 6) + '" y1="' + y + '" y2="' + y +
        '" stroke="var(--ink-3)" stroke-width="3" stroke-linecap="round" stroke-opacity="0.45"/><text class="processo-rot" x="' + xx + '" y="' + (y - 10) + '" text-anchor="middle">' + V.esc(rot) + '</text></g>';
    });
    s += marcas + '</svg>';
    alvo.innerHTML = s;
    /* dicas */
    alvo.querySelectorAll('.processo-evento').forEach(function (g) {
      V.dica.ligar(g, function () {
        if (g.hasAttribute('data-k')) {
          var e = P.eventos[+g.getAttribute('data-k')];
          return '<strong>' + V.esc(e.rotulo) + '</strong><span class="dica-sub">' + rotDia(e.t) + ', ' + hora(e.t) + ' UTC · ' + V.semTags(V.t('processo.raias.' + e.raia)) + '</span>' +
            (e.gravado_humano && e.raia !== 'humano' ? '<span class="dica-sub">' + V.t('processo.gravado_humano') + '</span>' : '');
        }
        if (g.hasAttribute('data-script')) {
          var sc = P.scripts[+g.getAttribute('data-script')];
          return '<strong>' + V.esc(sc.rotulo) + '</strong><span class="dica-sub">' + rotDia(sc.t) + ', ' + hora(sc.t) + ' UTC</span>';
        }
        var d = g.getAttribute('data-dia');
        return porDia[d].map(function (e) { return '<strong>' + V.esc(e.id) + '</strong>: ' + V.t('processo.emendas.' + e.id); }).join('<br>') +
          '<span class="dica-sub">' + V.t('processo.emenda_sem_log') + '</span>';
      });
    });
  },
  /* celular: lista por dia */
  lista: function (alvo) {
    var P = V.D.processo, porDia = {};
    P.eventos.forEach(function (e) { var d = e.ts.slice(0, 10); (porDia[d] = porDia[d] || []).push({ t: e.t, rot: e.rotulo, raia: e.raia, gh: e.gravado_humano }); });
    P.scripts.forEach(function (s) { var d = s.ts.slice(0, 10); (porDia[d] = porDia[d] || []).push({ t: s.t, rot: s.rotulo, raia: 'script' }); });
    P.emendas.forEach(function (e) { (porDia[e.data] = porDia[e.data] || []).push({ t: diaUTC(e.data) + DIA - 1, rot: e.id + ': ' + V.semTags(V.t('processo.emendas.' + e.id)), raia: 'emendas' }); });
    var h = '<ol class="processo-lista">';
    Object.keys(porDia).sort().forEach(function (d) {
      h += '<li><p class="processo-dia">' + rotDia(diaUTC(d)) + '</p>' + (d === '2026-09-23' ? '<p class="processo-sessao-lista">' + V.t('processo.sessao') + '</p>' : '') + '<ul>';
      porDia[d].sort(function (a, b) { return a.t - b.t; }).forEach(function (e) {
        h += '<li class="processo-item processo-item-' + e.raia + '"><span class="processo-chip">' + V.semTags(V.t('processo.raias.' + e.raia)) + '</span> ' + V.esc(e.rot) +
          (e.gh && e.raia !== 'humano' ? ' <span class="processo-obs">(' + V.t('processo.gravado_humano') + ')</span>' : '') + '</li>';
      });
      h += '</ul></li>';
    });
    alvo.innerHTML = h + '</ol>';
  }
};
V.aoRedimensionar(function () { V.processo.desenhar(); });
