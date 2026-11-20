// Verificação automática do guia (Etapa 4): console, KaTeX, ajuda fechada e em ordem,
// widgets travados e destravados, leituras dos widgets, conferência numérica,
// largura a 390 e 1280 px e capturas de cada seção.
// Uso: node verificar.js <arquivo.html> <pasta-das-telas> [porta]
const path = require('path');
const { chromium } = require('/home/swampert/.npm/_npx/9833c18b2d85bc59/node_modules/playwright');
const ARQ = process.argv[2] || 'guia-v1.html';
const TELAS = process.argv[3] || path.join(__dirname, 'telas');
const PORTA = process.argv[4] || '8723';
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
      r.katexErros = await page.evaluate(() => document.querySelectorAll('.katex-error').length);
      r.formulasRenderizadas = await page.evaluate(() => document.querySelectorAll('.katex').length);
      r.niveisAbertosNoInicio = await page.evaluate(() => [...document.querySelectorAll('.nivel')].filter(n => !n.hidden).length);
      r.botoesAjudaNoInicio = await page.evaluate(() => [...document.querySelectorAll('.botoes-ajuda')].map(b => [...b.querySelectorAll('button')].map(x => x.disabled ? 0 : 1).join('')).join(' '));
      const b = page.locator('#P5 .botoes-ajuda button');
      await b.nth(0).click();
      r.depoisDoNivel1 = await page.evaluate(() => [...document.querySelectorAll('#P5 .botoes-ajuda button')].map(x => (x.disabled ? 'D' : 'E')).join(''));
      r.nivel1Visivel = await page.evaluate(() => !document.querySelector('#P5 .nivel[data-nivel="1"]').hidden);
      r.nivel2Visivel = await page.evaluate(() => !document.querySelector('#P5 .nivel[data-nivel="2"]').hidden);
      await b.nth(0).click();
      r.widgetsTravados = await page.evaluate(() => [...document.querySelectorAll('.widget')].filter(x => x.classList.contains('travado')).length);
    }
    for (const wd of ['w1', 'w2', 'w3', 'w4', 'w5', 'w6']) {
      const q = page.locator('#prev-' + wd);
      await q.locator('.alt[data-ok="1"]').click();
      await q.locator('.linha-acao .btn').click();
    }
    if (nome === 'celular') {
      r.widgetsTravadosDepois = await page.evaluate(() => [...document.querySelectorAll('.widget')].filter(x => x.classList.contains('travado')).length);
      const L = {};
      await setRange(page, '#w1-ang', 60); L.w1_60 = await page.locator('#w1-leitura').innerText();
      await setRange(page, '#w1-ang', 120); L.w1_120 = await page.locator('#w1-leitura').innerText();
      await setRange(page, '#w1-ang', 90); L.w1_90 = await page.locator('#w1-leitura').innerText();
      await setRange(page, '#w1-ang', 0);
      L.w2_fora = await page.locator('#w2-leitura').innerText();
      await setRange(page, '#w2-x', 200); L.w2_dentro = await page.locator('#w2-leitura').innerText();
      await page.locator('#w2-sinal button[data-v="-1"]').click(); L.w2_dentro_neg = await page.locator('#w2-leitura').innerText();
      await page.locator('#w2-tipo button[data-v="b"]').click(); await setRange(page, '#w2-x', 320); await page.locator('#w2-sinal button[data-v="1"]').click();
      L.w2_batata_fora = await page.locator('#w2-leitura').innerText();
      await setRange(page, '#w3-a', 0.4); await setRange(page, '#w3-r', 0.8); L.w3 = await page.locator('#w3-leitura').innerText();
      await setRange(page, '#w3-a', 0); await setRange(page, '#w3-r', 0.8);
      await page.locator('#w4-modo button[data-v="2"]').click(); await setRange(page, '#w4-r', 0.5); L.w4 = await page.locator('#w4-leitura').innerText();
      await page.locator('#w4-modo button[data-v="0"]').click();
      await setRange(page, '#w5-r', 2); L.w5_fio = await page.locator('#w5-leitura').innerText();
      await page.locator('#w5-geo button[data-v="0"]').click(); L.w5_ponto = await page.locator('#w5-leitura').innerText();
      await page.locator('#w5-geo button[data-v="1"]').click(); await setRange(page, '#w5-r', 1);
      await setRange(page, '#w6-q', 3); await setRange(page, '#w6-Q', -1); L.w6 = await page.locator('#w6-leitura').innerText();
      await setRange(page, '#w6-Q', 0);
      r.leituras = L;
      const N = {};
      N.p5_ok = await responderNum(page, 'P5-a', '3,01e-9', '2');
      N.p5_sobrescrito = await responderNum(page, 'P5-a', '3,02×10⁻⁹');
      N.p5_errado_cubo = await responderNum(page, 'P5-a', '1,81e-8');
      N.p5_potencia = await responderNum(page, 'P5-a', '3,02e-6');
      N.p24b = await responderNum(page, 'P24-b', '5,99×10^3', '3');
      N.p29e_sinal = await responderNum(page, 'P29-e', '3,40e-12', '2');
      N.p29e_ok = await responderNum(page, 'P29-e', '-3,40e-12');
      N.p39 = await responderNum(page, 'P39-a', '5,0e-9', '2');
      N.p53c_unidade = await responderNum(page, 'P53-c', '0,00558', '2');
      N.p53c = await responderNum(page, 'P53-c', '5,58');
      N.lac5_gabarito = await responderNum(page, 'lac5-1', '2,3e6');
      r.conferencia = N;
      // gráficos escondidos até acertar
      r.graficoP24Escondido = await page.evaluate(() => getComputedStyle(document.querySelector('#P24-c figure')).display === 'none');
      await page.locator('#P24-c .alt[data-ok="1"]').click(); await page.locator('#P24-c .conf button[data-c="2"]').click(); await page.locator('#P24-c .linha-acao .btn').click();
      r.graficoP24DepoisDeAcertar = await page.evaluate(() => getComputedStyle(document.querySelector('#P24-c figure')).display !== 'none');
      // checkpoint do degrau 1
      for (const id of ['ck1-1', 'ck1-2', 'ck1-3']) { await page.locator('#' + id + ' .alt[data-ok="1"]').click(); await page.locator('#' + id + ' .conf button[data-c="3"]').click(); await page.locator('#' + id + ' .linha-acao .btn').click(); }
      r.vereditoD1 = await page.locator('#d1 .veredito').innerText();
      r.progresso = await page.locator('#prog-txt').innerText();
      // palpite
      await page.locator('#gancho .alt').nth(2).click();
      r.palpiteNoD3 = await page.evaluate(() => { const p = document.querySelector('[data-palpite]'); return p.hidden ? '(escondido)' : p.textContent; });
    }
    r['largura_' + w] = await page.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth].join('/'));
    const secs = [['topo', 'header.topo'], ['d0', '#d0'], ['d1', '#d1'], ['d2', '#d2'], ['d3', '#d3'], ['d4', '#d4'], ['d5', '#d5'], ['d6', '#d6'], ['d7', '#d7'], ['visao', '#visao'], ['p5', '#P5'], ['p24', '#P24'], ['p52', '#P52'], ['p76', '#P76'], ['p29', '#P29'], ['p39', '#P39'], ['p53', '#P53'], ['duvidas', '#duvidas'], ['sintese', '#sintese'], ['revisao', '#revisao']];
    for (const [n, sel] of secs) {
      if (await page.locator(sel).count()) await page.locator(sel).screenshot({ path: path.join(TELAS, nome + '-' + n + '.png'), timeout: 20000 });
    }
    if (nome === 'desktop') {
      for (const id of ['w1', 'w2', 'w3', 'w4', 'w5', 'w6']) await page.locator('#' + id).screenshot({ path: path.join(TELAS, 'widget-' + id + '.png') });
      await setRange(page, '#w1-ang', 135); await page.locator('#w1').screenshot({ path: path.join(TELAS, 'widget-w1-135graus.png') });
      await page.locator('#w2-tipo button[data-v="b"]').click(); await setRange(page, '#w2-x', 200); await page.locator('#w2-sinal button[data-v="-1"]').click(); await page.locator('#w2').screenshot({ path: path.join(TELAS, 'widget-w2-batata.png') });
      await setRange(page, '#w3-a', 0.4); await setRange(page, '#w3-r', 0.8); await page.locator('#w3').screenshot({ path: path.join(TELAS, 'widget-w3-cavidade.png') });
      await page.locator('#w4-modo button[data-v="2"]').click(); await page.locator('#w4').screenshot({ path: path.join(TELAS, 'widget-w4-r2.png') });
      await page.locator('#w5-geo button[data-v="2"]').click(); await setRange(page, '#w5-r', 3); await page.locator('#w5').screenshot({ path: path.join(TELAS, 'widget-w5-placa.png') });
      await setRange(page, '#w6-q', 3); await setRange(page, '#w6-Q', -1); await page.locator('#w6-pos button[data-v="f"]').click(); await page.locator('#w6').screenshot({ path: path.join(TELAS, 'widget-w6-fora.png') });
      await page.emulateMedia({ colorScheme: 'dark' });
      await page.locator('#d3').screenshot({ path: path.join(TELAS, 'escuro-d3.png') });
      await page.locator('#P29').screenshot({ path: path.join(TELAS, 'escuro-p29.png') });
      await page.emulateMedia({ colorScheme: 'light', media: 'print' });
      await page.locator('header.topo').screenshot({ path: path.join(TELAS, 'impressao-topo.png') });
    }
    await ctx.close();
  }
  await browser.close();
  console.log(JSON.stringify(r, null, 1));
})().catch(e => { console.error('ERRO', e); process.exit(1); });
