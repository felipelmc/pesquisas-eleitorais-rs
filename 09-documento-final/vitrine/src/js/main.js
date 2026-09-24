/* main: tema, movimento, desenho dos componentes e gatilhos de rolagem */
var raiz = document.documentElement;

function temaEscuroAtivo() {
  var t = raiz.getAttribute('data-theme');
  if (t) return t === 'dark';
  return !!(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
}
function guardar(chave, valor) {
  try { if (valor == null) localStorage.removeItem(chave); else localStorage.setItem(chave, valor); } catch (e) { /* sem armazenamento */ }
}
function atualizarBotaoTema() {
  var b = document.getElementById('botao-tema');
  if (!b) return;
  var escuro = temaEscuroAtivo();
  b.setAttribute('aria-pressed', String(escuro));
  b.querySelector('.botao-rotulo').textContent = V.semTags(escuro ? V.t('ferramentas.tema_claro') : V.t('ferramentas.tema_escuro'));
  b.setAttribute('aria-label', V.semTags(escuro ? V.t('ferramentas.tema_claro') : V.t('ferramentas.tema_escuro')));
}
function atualizarBotaoMovimento() {
  var b = document.getElementById('botao-movimento');
  if (b) b.setAttribute('aria-pressed', String(raiz.getAttribute('data-movimento') === 'reduzido'));
}

function redesenharTudo() {
  V._redesenhos.forEach(function (fn) { try { fn(); } catch (e) { console.error(e); } });
}

function iniciar() {
  var passos = [
    function () { V.legenda.desenhar(); },
    function () { V.heroi.pontos(); V.heroi.contar(); },
    function () { V.prisma.desenhar(); V.prisma.continuacao(); V.prisma.alternar(); },
    function () { V.mapa.desenhar(); },
    function () { V.direcao.iniciar(); },
    function () { V.contagem.iniciar(); },
    function () { V.forest.desenhar(); },
    function () { V.robGrafico.desenhar(); },
    function () { V.processo.desenhar(); }
  ];
  passos.forEach(function (p) { try { p(); } catch (e) { console.error(e); } });

  /* depois das fontes, o herói e os gráficos com rótulos medidos são refeitos uma vez, sem animação de novo */
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () {
      try { V.heroi.pontos(); V.prisma.desenhar(); } catch (e) { console.error(e); }
    });
  }

  /* tema */
  atualizarBotaoTema();
  V.ao(document.getElementById('botao-tema'), 'click', function () {
    var escuro = !temaEscuroAtivo();
    raiz.setAttribute('data-theme', escuro ? 'dark' : 'light');
    guardar('vitrine-tema', escuro ? 'escuro' : 'claro');
    atualizarBotaoTema();
  });
  /* movimento */
  atualizarBotaoMovimento();
  V.ao(document.getElementById('botao-movimento'), 'click', function () {
    var red = raiz.getAttribute('data-movimento') !== 'reduzido';
    if (red) raiz.setAttribute('data-movimento', 'reduzido'); else raiz.removeAttribute('data-movimento');
    guardar('vitrine-movimento', red ? 'reduzido' : null);
    atualizarBotaoMovimento();
  });

  /* "ver no mapa" nos cartões do que não sabemos */
  document.querySelectorAll('[data-destaque]').forEach(function (a) {
    a.addEventListener('click', function () {
      var tipo = a.getAttribute('data-destaque');
      setTimeout(function () { V.mapa.destacar(tipo); }, V.reduzido() ? 0 : 450);
    });
  });

  /* copiar BibTeX */
  var bc = document.getElementById('copiar-bibtex');
  if (bc) bc.addEventListener('click', function () {
    var pre = document.getElementById('bibtex'), txt = pre.textContent;
    function ok() { bc.querySelector('span').textContent = V.semTags(V.t('documentos.copiado')); setTimeout(function () { bc.querySelector('span').textContent = V.semTags(V.t('documentos.copiar')); }, 1800); }
    function selecionar() { var r = document.createRange(); r.selectNodeContents(pre); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); }
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(ok, selecionar);
      else selecionar();
    } catch (e) { selecionar(); }
  });

  /* aparição na rolagem */
  var alvos = document.querySelectorAll('.revelar');
  var acoes = {
    'pendencias': function () { V.pendencias.animar(); },
    'prisma': function () { V.prisma.animar(); },
    'mapa': function () { V.mapa.animar(); }
  };
  if ('IntersectionObserver' in window && !V.reduzido()) {
    var io = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('visivel');
        var a = en.target.getAttribute('data-acao');
        if (a && acoes[a]) acoes[a]();
        io.unobserve(en.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    alvos.forEach(function (el) { io.observe(el); });
  } else {
    alvos.forEach(function (el) { el.classList.add('visivel'); });
    try { V.prisma.animar(); V.mapa.animar(); V.pendencias.animar(); } catch (e) { console.error(e); }
  }

  /* redesenho quando a largura muda */
  var larguraAnt = window.innerWidth;
  window.addEventListener('resize', V.debounce(function () {
    if (window.innerWidth === larguraAnt) return;
    larguraAnt = window.innerWidth;
    redesenharTudo();
  }, 180));

  /* impressão: abre as tabelas */
  window.addEventListener('beforeprint', function () {
    document.querySelectorAll('details.tabela-dados').forEach(function (d) { d.setAttribute('open', ''); });
  });
}

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar);
else iniciar();
