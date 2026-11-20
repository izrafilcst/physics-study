// Verificação automática do preparatório (Etapa 4): console, KaTeX, ajuda fechada e em ordem,
// widgets travados/destravados e leituras, conferência numérica, palpite, relógio,
// largura a 390 e 1280 px, tema escuro, impressão e capturas de cada seção.
// Uso (servidor em guias/): node verificar.js <caminho-relativo-do-html> <pasta-das-telas> [porta]
const path = require('path');
const { chromium } = require('/home/swampert/.npm/_npx/9833c18b2d85bc59/node_modules/playwright');
const ARQ = process.argv[2] || 'preparatorio-av2/guia-v1.html';
const TELAS = process.argv[3] || path.join(__dirname, 'telas');
const PORTA = process.argv[4] || '8724';
const URL = 'http://127.0.0.1:' + PORTA + '/' + ARQ;

async function setRange(page, sel, v) {
  await page.evaluate(([s, val]) => { const el = document.querySelector(s); el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); }, [sel, String(v)]);
}
async function responderNum(page, id, valor, conf) {
  await page.fill('#in-' + id, valor);
  if (conf) await page.locator('#' + id + ' .conf button[data-c="' + conf + '"]').click();
  await page.locator('#' + id + ' .linha-acao .btn').first().click();
  return (await page.locator('#' + id + ' .fb').innerText()).replace(/\s+/g, ' ');
}
async function responderQuiz(page, id, certo, conf) {
  const q = page.locator('#' + id);
  if (certo) await q.locator('.alt[data-ok="1"]').click(); else await q.locator('.alt:not([data-ok])').first().click();
  if (conf && await q.locator('.conf button').count()) await q.locator('.conf button[data-c="' + conf + '"]').click();
  await q.locator('.linha-acao .btn').first().click();
}

(async () => {
  const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome' });
  const r = { erros: [] };
  for (const [nome, w] of [['celular', 390], ['desktop', 1280]]) {
    const ctx = await browser.newContext({ viewport: { width: w, height: 900 } });
    const page = await ctx.newPage();
    page.on('console', m => { if (m.type() === 'error') r.erros.push(nome + ': ' + m.text()); });
    page.on('pageerror', e => r.erros.push(nome + ' pageerror: ' + e.message));
    page.on('dialog', d => d.accept());
    await page.goto(URL);
    await page.waitForTimeout(2500);
    if (nome === 'celular') {
      r.katex = await page.evaluate(() => document.documentElement.classList.contains('katex-ok'));
      r.katexErros = await page.evaluate(() => [...document.querySelectorAll('.katex-error')].map(e => e.textContent.slice(0, 60)));
      r.formulasRenderizadas = await page.evaluate(() => document.querySelectorAll('.katex').length);
      r.niveisAbertosNoInicio = await page.evaluate(() => [...document.querySelectorAll('.nivel')].filter(n => !n.hidden).length);
      r.totalNiveis = await page.evaluate(() => document.querySelectorAll('.nivel').length);
      r.botoesLiberadosNoInicio = await page.evaluate(() => [...document.querySelectorAll('.botoes-ajuda')].every(b => { const bs = [...b.querySelectorAll('button')]; return !bs[0].disabled && bs.slice(1).every(x => x.disabled); }));
      const b = page.locator('#PA5 .botoes-ajuda button');
      await b.nth(0).click();
      r.depoisDoNivel1 = await page.evaluate(() => [...document.querySelectorAll('#PA5 .botoes-ajuda button')].map(x => (x.disabled ? 'D' : 'E')).join(''));
      r.nivel1Visivel = await page.evaluate(() => !document.querySelector('#PA5 .nivel[data-nivel="1"]').hidden);
      r.nivel2Visivel = await page.evaluate(() => !document.querySelector('#PA5 .nivel[data-nivel="2"]').hidden);
      await b.nth(0).click();
      r.cartaoBotoes = await page.locator('#C23-53 .botoes-ajuda button').count();
      r.widgetsTravados = await page.evaluate(() => [...document.querySelectorAll('.widget')].filter(x => x.classList.contains('travado')).length);
    }
    for (const wd of ['w4', 'w5', 'w7']) await responderQuiz(page, 'prev-' + wd, true);
    if (nome === 'celular') {
      r.widgetsTravadosDepois = await page.evaluate(() => [...document.querySelectorAll('.widget')].filter(x => x.classList.contains('travado')).length);
      const L = {};
      L.w4_inicial = await page.locator('#w4-leitura').innerText();
      await setRange(page, '#w4-r', 1.25); L.w4_fora = await page.locator('#w4-leitura').innerText();
      await page.locator('#w4-n button[data-v="0"]').click(); await setRange(page, '#w4-r', 0.5); L.w4_uniforme = await page.locator('#w4-leitura').innerText();
      L.w5_PA6 = await page.locator('#w5-leitura').innerText();
      await page.locator('#w5-p button[data-v="p"]').click(); L.w5_proton = await page.locator('#w5-leitura').innerText();
      await page.locator('#w5-p button[data-v="e"]').click(); await setRange(page, '#w5-v', 4.58); L.w5_V_dobrada = await page.locator('#w5-leitura').innerText();
      L.w7_P30_27 = await page.locator('#w7-leitura').innerText();
      await setRange(page, '#w7-a', 3); await setRange(page, '#w7-t', 10); L.w7_PA10 = await page.locator('#w7-leitura').innerText();
      r.leituras = L;
      const N = {};
      N.pa1_ok = await responderNum(page, 'PA1-a', '1,28e7', '2');
      N.pa5_dentro = await responderNum(page, 'PA5-a', '1,9', '3');
      N.pa5_ok = await responderNum(page, 'PA5-a', '3,6');
      N.pa6_semMeio = await responderNum(page, 'PA6-a', '8,34e-4', '2');
      N.p28_5_sinal = await responderNum(page, 'P28-5-a', '2,0', '2');
      N.p28_5_ok = await responderNum(page, 'P28-5-a', '-2,0');
      N.pa10_livro = await responderNum(page, 'PA10-a', '80e-6', '2');
      N.pa10_ok = await responderNum(page, 'PA10-a', '1,08 × 10⁻³');
      N.pa9_ok = await responderNum(page, 'PA9-a', '0,54', '2');
      N.pa4_extra_zero = await responderNum(page, 'PA4-b', '0', '2');
      N.lac2_2 = await responderNum(page, 'lac2-2', '9,42e-10');
      N.s4 = await responderNum(page, 'S4-b', '8,2e-5');
      r.conferencia = N;
      for (const id of ['ck1-1', 'ck1-2', 'ck1-3']) await responderQuiz(page, id, true, '3');
      r.vereditoD1 = await page.locator('#d1 .veredito').innerText();
      await responderQuiz(page, 'rev1', false, '3');
      r.calibracao = (await page.locator('#calibracao').innerText()).replace(/\s+/g, ' ');
      r.progresso = await page.locator('#prog-txt').innerText();
      await page.locator('#gancho .alt').nth(1).click();
      r.palpiteNaPA9 = await page.evaluate(() => { const p = document.querySelector('[data-palpite]'); return p.hidden ? '(escondido)' : p.textContent; });
      await page.locator('#btn-relogio').click(); await page.waitForTimeout(1500);
      r.relogio = await page.locator('#relogio').innerText();
      await page.locator('#btn-relogio-zerar').click();
      r.relogioZerado = await page.locator('#relogio').innerText();
      await page.reload(); await page.waitForTimeout(2000);
      r.persistiuAposReload = await page.locator('#prog-txt').innerText();
    }
    r['largura_' + w] = await page.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth].join('/'));
    r['largos_' + w] = await page.evaluate(() => [...document.querySelectorAll('main *')].filter(e => e.getBoundingClientRect().right > document.documentElement.clientWidth + 1 && !e.closest('.tabela-rola') && !e.closest('.katex-display')).slice(0, 5).map(e => e.tagName + '.' + e.className + '#' + e.id));
    const secs = [['topo', 'header.topo'], ['raiox', '#raiox-sec'], ['d0', '#d0'], ['d1', '#d1'], ['d2', '#d2'], ['d3', '#d3'], ['d4', '#d4'], ['d5', '#d5'], ['d6', '#d6'], ['d7', '#d7'],
      ['PA1', '#PA1'], ['PA2', '#PA2'], ['PA3', '#PA3'], ['PA4', '#PA4'], ['PA5', '#PA5'], ['P28-5', '#P28-5'], ['PA6', '#PA6'], ['P28-48', '#P28-48'], ['PA7', '#PA7'],
      ['P29-11', '#P29-11'], ['PA8', '#PA8'], ['P29-87', '#P29-87'], ['PA9', '#PA9'], ['P30-19', '#P30-19'], ['P30-27', '#P30-27'], ['PA10', '#PA10'], ['P30-33', '#P30-33'],
      ['cartoes', '#cartoes'], ['simulado', '#simulado'], ['sintese', '#sintese'], ['revisao', '#revisao']];
    for (const [n, sel] of secs) {
      if (await page.locator(sel).count()) await page.locator(sel).screenshot({ path: path.join(TELAS, nome + '-' + n + '.png'), timeout: 30000 });
    }
    if (nome === 'desktop') {
      for (const id of ['w4', 'w5', 'w7']) await page.locator('#' + id).screenshot({ path: path.join(TELAS, 'widget-' + id + '.png') });
      for (const q of ['P29-87', 'PA8']) {
        const bs = page.locator('#' + q + ' .botoes-ajuda button');
        for (let k = 0; k < 4; k++) await bs.nth(k).click();
        await page.locator('#' + q).screenshot({ path: path.join(TELAS, 'resolucao-' + q + '.png'), timeout: 30000 });
      }
      await page.emulateMedia({ colorScheme: 'dark' });
      await page.locator('#d5').screenshot({ path: path.join(TELAS, 'escuro-d5.png') });
      await page.locator('#raiox-sec').screenshot({ path: path.join(TELAS, 'escuro-raiox.png') });
      await page.emulateMedia({ colorScheme: 'light', media: 'print' });
      await page.locator('header.topo').screenshot({ path: path.join(TELAS, 'impressao-topo.png') });
    }
    await ctx.close();
  }
  await browser.close();
  console.log(JSON.stringify(r, null, 2));
})();
