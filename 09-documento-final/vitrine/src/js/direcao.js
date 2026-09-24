/* estudo a estudo: gráfico de direção (Boon & Thomson), uma linha por estudo em cada célula,
   com filtros e a chave que mostra, em cinza, os estudos fora da síntese principal */
var FILTROS = [
  { id: 'exposicao', rot: 'direcao.f_exposicao', ops: [['pesquisa_pre_eleitoral', 'pesquisa pré-eleitoral'], ['agregador_projecao', 'agregador ou projeção'], ['boca_de_urna', 'boca de urna'], ['apuracao_parcial', 'apuração parcial']] },
  { id: 'desfecho', rot: 'direcao.f_desfecho', ops: [['apoio_ao_lider', 'apoio'], ['mobilizacao', 'comparecimento']] },
  { id: 'desenho', rot: 'direcao.f_desenho', ops: [['randomizado', 'randomizado'], ['nao_randomizado', 'não randomizado']] },
  { id: 'contexto', rot: 'direcao.f_contexto', ops: [['real', 'real'], ['induzido', 'preferências induzidas'], ['hipotetico', 'hipotético']] },
  { id: 'regiao', rot: 'direcao.f_regiao', ops: [['brasil', 'Brasil'], ['america_latina', 'América Latina'], ['outro', 'outras']] }
];
var estado = { exposicao: null, desfecho: null, desenho: null, contexto: null, regiao: null, fora: false };
var BLOCO_ROT = {};
V.D.blocos.forEach(function (b) { BLOCO_ROT[b.id] = b.rotulo; });

function famCodCelula(c) { return c.familia === 'outro' ? 'apuracao_parcial' : c.familia; }
function passa(fam, construto, classe, s) {
  if (estado.exposicao && fam !== estado.exposicao) return false;
  if (estado.desfecho && construto !== estado.desfecho) return false;
  if (estado.desenho && classe !== estado.desenho) return false;
  if (estado.contexto && s.realismo !== estado.contexto) return false;
  if (estado.regiao && s.regioes.indexOf(estado.regiao) < 0) return false;
  return true;
}
function efeitosTxt(e) {
  var outros = e.n_efeitos - e.n_pos - e.n_neg;
  var t = '<span class="dir-tally" aria-hidden="true">' + V.glifo('pos', { tamanho: 10, traco: 1.2 }) + e.n_pos + '</span>' +
    '<span class="dir-tally" aria-hidden="true">' + V.glifo('neg', { tamanho: 10, traco: 1.2 }) + e.n_neg + '</span>' +
    (outros > 0 ? '<span class="dir-tally" aria-hidden="true">' + V.glifo('nulo', { tamanho: 10, traco: 1 }) + outros + '</span>' : '') +
    '<span class="visualmente-oculto">' + e.n_pos + ' efeitos na direção positiva, ' + e.n_neg + ' na negativa' +
    (outros > 0 ? ', ' + outros + ' sem direção ou nulos' : '') + ', </span><span class="dir-de">de ' + e.n_efeitos + '</span>';
  return t;
}
function linha(e, c, s, cinza, motivo) {
  var g = cinza ? V.glifo(e.glifo, { nivel: 4, opacidade: 0.25, tamanho: 18 }).replace(/var\(--(pos|neg)\)/g, 'var(--nulo)') :
    V.glifo(e.glifo, { nivel: c ? c.nivel : 4, tamanho: 18 });
  return '<li class="dir-linha' + (cinza ? ' dir-cinza' : '') + '">' +
    '<span class="dir-glifo">' + g + '</span>' +
    '<span class="dir-estudo"><span class="dir-nome">' + V.esc(s.rotulo) + '</span><span class="dir-rot-dir">' + e.direcao_rot + '</span></span>' +
    '<span class="dir-meta">' + V.esc(s.pais) + ' · ' + s.desenho + (motivo ? '<span class="dir-motivo">' + V.esc(motivo) + '</span>' : '') + '</span>' +
    '<span class="dir-efeitos">' + (e.n_efeitos ? efeitosTxt(e) : '') + '</span>' +
    '<span class="dir-n">' + (e.n_fmt && e.n_fmt !== 'NR' ? e.n_fmt + ' <span class="dir-unid">' + V.esc(s.unidade) + '</span>' : '<span class="dir-unid">n NR</span>') + '</span>' +
    '<span class="dir-rob">' + (e.rob ? V.rob(e.rob, { soSimbolo: true }) : (s.rob.length ? V.rob(s.rob[0], { soSimbolo: true }) : '')) + '</span>' +
    '</li>';
}

V.direcao = {
  iniciar: function () {
    var f = document.getElementById('direcao-filtros');
    if (!f) return;
    var h = '';
    FILTROS.forEach(function (fl) {
      h += '<div class="filtro-grupo" role="group" aria-label="' + V.semTags(V.t(fl.rot)) + '"><span class="filtro-rot">' + V.t(fl.rot) + '</span><div class="filtro-chips">';
      h += '<button type="button" class="chip" data-f="' + fl.id + '" data-v="" aria-pressed="true">' + V.t('direcao.todos') + '</button>';
      fl.ops.forEach(function (o) { h += '<button type="button" class="chip" data-f="' + fl.id + '" data-v="' + o[0] + '" aria-pressed="false">' + V.esc(o[1]) + '</button>'; });
      h += '</div></div>';
    });
    h += '<label class="chave-fora"><input type="checkbox" id="direcao-fora"><span class="chave-trilho" aria-hidden="true"></span><span>' + V.t('direcao.mostrar_fora') + '</span></label>';
    f.innerHTML = h;
    f.querySelectorAll('button.chip').forEach(function (b) {
      b.addEventListener('click', function () {
        var id = b.getAttribute('data-f'), v = b.getAttribute('data-v') || null;
        estado[id] = v;
        f.querySelectorAll('button.chip[data-f="' + id + '"]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        V.direcao.desenhar(true);
      });
    });
    document.getElementById('direcao-fora').addEventListener('change', function (e) { estado.fora = e.target.checked; V.direcao.desenhar(true); });
    V.direcao.desenhar(false);
  },
  desenhar: function (anunciar) {
    var alvo = document.getElementById('direcao-grafico');
    if (!alvo) return;
    var h = '', nLinhas = 0, est = {};
    V.D.celulas.forEach(function (c) {
      var ls = c.estudos.filter(function (e) { return passa(famCodCelula(c), c.construto, c.classe, V.estudo(e.chave)); });
      if (!ls.length) return;
      h += '<div class="dir-grupo"><div class="dir-grupo-cab"><span class="dir-grupo-titulo"><span class="dir-grupo-bloco">' + BLOCO_ROT[c.bloco] + '</span> ' +
        V.esc((c.familia === 'pesquisa_pre_eleitoral' ? '' : c.familia_rot + ' · ') + 'comparador: ' + c.comparador_rot + ' · ' + c.classe_rot.toLowerCase()) +
        '</span><span class="dir-grupo-info">' + V.selo(c.nivel, { raio: 4.5 }) + '<span class="dir-grupo-cont">' + c.contagem + '</span></span></div><ul class="dir-linhas">';
      ls.forEach(function (e) { h += linha(e, c, V.estudo(e.chave), false); nLinhas++; est[e.chave] = 1; });
      h += '</ul></div>';
    });
    if (estado.fora) {
      var fl = V.D.fora.filter(function (e) {
        var s = V.estudo(e.chave);
        if (!e.construto) return !estado.desfecho && !estado.desenho && passa(s.familia, null, null, s);
        return passa(s.familia, e.construto, e.classe, s);
      });
      if (fl.length) {
        h += '<div class="dir-grupo dir-grupo-fora"><div class="dir-grupo-cab"><span class="dir-grupo-titulo"><span class="dir-grupo-bloco">' + V.t('direcao.fora_titulo') +
          '</span> ' + V.t('direcao.fora_intro') + '</span></div><ul class="dir-linhas">';
        fl.forEach(function (e) {
          var s = V.estudo(e.chave);
          h += linha(e, null, s, true, (e.grupo_rot ? e.grupo_rot + '. ' : '') + s.motivo);
          nLinhas++; est[e.chave] = 1;
        });
        h += '</ul></div>';
      }
    }
    if (!nLinhas) h = '<p class="dir-vazio">' + V.t('direcao.vazio') + '</p>';
    alvo.innerHTML = h;
    if (anunciar) {
      document.getElementById('vivo').textContent = V.semTags(V.t('direcao.vivo')).replace('{n}', nLinhas).replace('{e}', Object.keys(est).length);
    }
    if (anunciar && !V.reduzido()) {
      alvo.querySelectorAll('.dir-linha').forEach(function (li, i) {
        li.style.animationDelay = V.atraso(i, 12) + 'ms';
        li.classList.add('entra');
      });
    }
  }
};
