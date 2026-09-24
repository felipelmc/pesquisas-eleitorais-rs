// QA visual e de acessibilidade da vitrine (docs/index.html), com Playwright e axe.
// USO (de 09-documento-final/vitrine/qa/):  node capturar.mjs [--rapido]
//   --rapido  só 1440 e 390 px, tema claro, sem movimento reduzido
// Saídas em qa/capturas/ (fora do git): PNG por largura × tema × movimento, texto visível e relatorio.json.
// Falha (código 1) com erro de console, requisição externa, violação axe serious/critical ou percurso de teclado quebrado.
import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import { mkdirSync, writeFileSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const aqui = path.dirname(fileURLToPath(import.meta.url));
const pagina = path.resolve(aqui, '../../../docs/index.html');
const url = pathToFileURL(pagina).href;
const saida = path.join(aqui, 'capturas');
mkdirSync(saida, { recursive: true });

const rapido = process.argv.includes('--rapido');
const argL = process.argv.find((a) => a.startsWith('--larguras='));
const larguras = argL ? argL.split('=')[1].split(',').map(Number) : rapido ? [1440, 390] : [1440, 1024, 768, 390];
const temas = rapido ? ['light'] : ['light', 'dark'];
const movimentos = rapido ? ['no-preference'] : ['no-preference', 'reduce'];

const relatorio = { url, execucoes: [], falhas: [] };
const browser = await chromium.launch();

async function rolarTudo(page) {
  await page.evaluate(async () => {
    const passo = Math.max(300, Math.floor(window.innerHeight * 0.7));
    for (let y = 0; y < document.body.scrollHeight; y += passo) {
      window.scrollTo({ top: y, behavior: 'instant' });
      await new Promise((r) => setTimeout(r, 90));
    }
    window.scrollTo({ top: 0, behavior: 'instant' });
    await new Promise((r) => setTimeout(r, 400));
  });
}

for (const largura of larguras) {
  for (const tema of temas) {
    for (const mov of movimentos) {
      const ctx = await browser.newContext({
        viewport: { width: largura, height: largura < 768 ? 844 : 900 },
        colorScheme: tema, reducedMotion: mov, deviceScaleFactor: largura < 768 ? 2 : 1,
        hasTouch: largura < 768, isMobile: largura < 768,
      });
      const page = await ctx.newPage();
      const erros = [], externas = [];
      page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') erros.push(`${m.type()}: ${m.text()}`); });
      page.on('pageerror', (e) => erros.push(`pageerror: ${e.message}`));
      page.on('request', (r) => { const u = r.url(); if (!u.startsWith('file:') && !u.startsWith('data:') && !u.startsWith('about:')) externas.push(u); });
      await page.goto(url, { waitUntil: 'load' });
      await page.waitForTimeout(300);
      await rolarTudo(page);
      await page.waitForTimeout(mov === 'reduce' ? 100 : 1100);
      const nome = `vitrine-${largura}-${tema === 'light' ? 'claro' : 'escuro'}${mov === 'reduce' ? '-reduzido' : ''}`;
      await page.screenshot({ path: path.join(saida, `${nome}.png`), fullPage: true });
      // rolagem horizontal da página
      const horizontal = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      // axe (uma vez por largura e tema, sem depender do movimento)
      let axe = null;
      if (mov === 'no-preference') {
        const r = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
        axe = r.violations.map((v) => ({ id: v.id, impacto: v.impact, n: v.nodes.length, alvo: v.nodes.slice(0, 3).map((n) => n.target.join(' ')) }));
      }
      if (largura === 1440 && tema === 'light' && mov === 'no-preference') {
        writeFileSync(path.join(saida, 'texto_visivel.txt'), await page.evaluate(() => document.body.innerText), 'utf-8');
      }
      const exec = { nome, largura, tema, mov, erros, externas, horizontal, axe };
      relatorio.execucoes.push(exec);
      if (erros.length) relatorio.falhas.push(`${nome}: ${erros.length} erro(s) de console: ${erros.slice(0, 3).join(' | ')}`);
      if (externas.length) relatorio.falhas.push(`${nome}: requisições externas: ${externas.slice(0, 3).join(', ')}`);
      if (horizontal > 1) relatorio.falhas.push(`${nome}: rolagem horizontal de ${horizontal}px`);
      if (axe) {
        const graves = axe.filter((v) => v.impacto === 'serious' || v.impacto === 'critical');
        if (graves.length) relatorio.falhas.push(`${nome}: axe ${graves.map((v) => `${v.id} (${v.impacto}, ${v.n})`).join('; ')}`);
      }
      await ctx.close();
    }
  }
}

// texto de estados que não aparecem na página inicial: gavetas, análises de sensibilidade e estudos fora da síntese
{
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'load' });
  const partes = [];
  const n = await page.locator('button.celula-mapa').count();
  for (let i = 0; i < n; i++) {
    await page.locator('button.celula-mapa').nth(i).click();
    await page.waitForTimeout(120);
    partes.push(await page.evaluate(() => document.getElementById('gaveta').innerText));
    await page.keyboard.press('Escape');
    await page.waitForTimeout(80);
  }
  const segs = await page.locator('#contagem-controle .segmento').count();
  for (let i = 0; i < segs; i++) {
    await page.locator('#contagem-controle .segmento').nth(i).click();
    await page.waitForTimeout(80);
    partes.push(await page.evaluate(() => document.getElementById('contando').innerText));
  }
  await page.locator('.chave-fora').click();
  await page.waitForTimeout(80);
  partes.push(await page.evaluate(() => document.getElementById('estudo-a-estudo').innerText));
  await page.locator('#prisma-alternar').click();
  partes.push(await page.evaluate(() => document.getElementById('prisma-diagrama').innerText));
  writeFileSync(path.join(saida, 'texto_estados.txt'), partes.join('\n\n'), 'utf-8');
  relatorio.estados = { gavetas: n, analises: segs };
  await ctx.close();
}

// capturas extras: gaveta aberta (desktop e celular) e tema escuro com gaveta
for (const [largura, tema] of [[1440, 'light'], [390, 'dark']]) {
  const ctx = await browser.newContext({ viewport: { width: largura, height: largura < 768 ? 844 : 900 }, colorScheme: tema, deviceScaleFactor: largura < 768 ? 2 : 1 });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'load' });
  await page.locator('#mapa').scrollIntoViewIfNeeded();
  await page.waitForTimeout(700);
  await page.locator('button.celula-mapa').first().click();
  await page.waitForTimeout(700);
  await page.screenshot({ path: path.join(saida, `gaveta-${largura}-${tema === 'light' ? 'claro' : 'escuro'}.png`) });
  await ctx.close();
}

// percurso de teclado: skip link -> filtros -> células do mapa -> Enter abre a gaveta -> Esc fecha e devolve o foco
{
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  const passos = [];
  await page.goto(url, { waitUntil: 'load' });
  await page.keyboard.press('Tab');
  const primeiro = await page.evaluate(() => document.activeElement && document.activeElement.className);
  passos.push(`1º Tab: ${primeiro}`);
  if (!String(primeiro).includes('pular')) relatorio.falhas.push('teclado: o primeiro Tab não chega ao skip link');
  await page.keyboard.press('Enter');
  const alvo = await page.evaluate(() => document.activeElement && document.activeElement.id);
  passos.push(`Enter no skip link: foco em #${alvo}`);
  if (alvo !== 'conteudo') relatorio.falhas.push('teclado: o skip link não leva o foco a #conteudo');
  let chegouFiltro = false, chegouMapa = false, n = 0;
  while (n < 400 && !chegouMapa) {
    await page.keyboard.press('Tab'); n++;
    const info = await page.evaluate(() => { const a = document.activeElement; return { cls: a.className || '', f: a.getAttribute && a.getAttribute('data-f') }; });
    if (String(info.cls).includes('celula-mapa')) chegouMapa = true;
  }
  passos.push(`células do mapa alcançadas com ${n} Tabs: ${chegouMapa}`);
  if (!chegouMapa) relatorio.falhas.push('teclado: não chega às células do mapa');
  await page.keyboard.press('Enter');
  await page.waitForTimeout(400);
  const aberta = await page.evaluate(() => document.getElementById('gaveta').open);
  passos.push(`Enter abre a gaveta: ${aberta}`);
  if (!aberta) relatorio.falhas.push('teclado: Enter não abre a gaveta');
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);
  const volta = await page.evaluate(() => ({ aberta: document.getElementById('gaveta').open, cls: document.activeElement.className }));
  passos.push(`Esc fecha: ${!volta.aberta}; foco volta para: ${volta.cls}`);
  if (volta.aberta) relatorio.falhas.push('teclado: Esc não fecha a gaveta');
  if (!String(volta.cls).includes('celula-mapa')) relatorio.falhas.push('teclado: o foco não volta para a célula do mapa');
  // filtros: continua a partir do mapa até os chips
  n = 0;
  while (n < 120 && !chegouFiltro) {
    await page.keyboard.press('Tab'); n++;
    const f = await page.evaluate(() => document.activeElement && document.activeElement.getAttribute('data-f'));
    if (f) chegouFiltro = true;
  }
  if (chegouFiltro) {
    await page.keyboard.press('ArrowRight');
    await page.keyboard.press('Tab');
    await page.keyboard.press('Enter');
    await page.waitForTimeout(200);
    const vivo = await page.evaluate(() => document.getElementById('vivo').textContent);
    passos.push(`filtros alcançados; região viva: "${vivo}"`);
  } else {
    relatorio.falhas.push('teclado: não chega aos filtros');
  }
  relatorio.teclado = passos;
  await ctx.close();
}

await browser.close();
writeFileSync(path.join(saida, 'relatorio.json'), JSON.stringify(relatorio, null, 1), 'utf-8');
for (const e of relatorio.execucoes) {
  const axeTxt = e.axe ? (e.axe.length ? e.axe.map((v) => `${v.id}:${v.impacto}`).join(',') : 'limpo') : '-';
  console.log(`${e.nome.padEnd(34)} erros=${e.erros.length} externas=${e.externas.length} horiz=${e.horizontal} axe=${axeTxt}`);
}
console.log('teclado:\n  ' + (relatorio.teclado || []).join('\n  '));
if (relatorio.falhas.length) {
  console.log('\nFALHAS:\n  ' + relatorio.falhas.join('\n  '));
  process.exit(1);
}
console.log('\nOK: nenhuma falha');
