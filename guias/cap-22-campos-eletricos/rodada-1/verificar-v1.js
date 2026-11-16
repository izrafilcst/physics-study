async (page) => {
  // Verificação automática do guia (Etapa 4): console, ajuda fechada e em ordem,
  // widgets, largura a 390 e 1280 px, e capturas de tela de cada seção.
  const VERSAO = 'guia-v1.html';
  const TELAS = '/home/swampert/Documents/fisica/guias/cap-22-campos-eletricos/rodada-1/telas/';
  const r = { erros: [] };
  page.on('console', m => { if (m.type() === 'error') r.erros.push(m.text()); });
  page.on('pageerror', e => r.erros.push('pageerror: ' + e.message));
  for (const [nome, w] of [['celular', 390], ['desktop', 1280]]) {
    await page.setViewportSize({ width: w, height: 900 });
    await page.goto('http://127.0.0.1:8722/' + VERSAO);
    await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
    await page.reload();
    await page.waitForTimeout(2000);
    if (nome === 'celular') {
      r.katex = await page.evaluate(() => document.documentElement.classList.contains('katex-ok'));
      r.katexErros = await page.evaluate(() => document.querySelectorAll('.katex-error').length);
      r.niveisAbertosNoInicio = await page.evaluate(() => [...document.querySelectorAll('.nivel')].filter(n => !n.hidden).length);
      r.botoesAjudaNoInicio = await page.evaluate(() => [...document.querySelectorAll('.botoes-ajuda')].map(b => [...b.querySelectorAll('button')].map(x => x.disabled ? 0 : 1).join('')).join(' '));
      const b = page.locator('#P38 .botoes-ajuda button');
      await b.nth(0).click();
      r.depoisDoNivel1 = await page.evaluate(() => [...document.querySelectorAll('#P38 .botoes-ajuda button')].map(x => (x.disabled ? 'D' : 'E')).join(''));
      await b.nth(0).click();
      r.widgetsTravados = await page.evaluate(() => [...document.querySelectorAll('.widget')].filter(x => x.classList.contains('travado')).length);
    }
    for (const wd of ['w1', 'w2', 'w3', 'w4', 'w5', 'w6']) {
      const q = page.locator('#prev-' + wd);
      await q.locator('.alt[data-ok="1"]').click();
      await q.locator('.btn').click();
    }
    if (nome === 'celular') {
      r.widgetsTravadosDepois = await page.evaluate(() => [...document.querySelectorAll('.widget')].filter(x => x.classList.contains('travado')).length);
      const leituras = {};
      await page.locator('#w1-r').fill('2'); leituras.w1 = await page.locator('#w1-leitura').innerText();
      await page.locator('#w2-qb').fill('-4'); leituras.w2 = await page.locator('#w2-leitura').innerText();
      await page.locator('#w2-qb').fill('4');
      await page.locator('#w4-phi').fill('180'); leituras.w4 = await page.locator('#w4-leitura').innerText();
      await page.locator('#w4-phi').fill('60');
      await page.locator('#w6-z').fill('0.6'); leituras.w6 = await page.locator('#w6-leitura').innerText();
      await page.locator('#w6-z').fill('1');
      r.leituras = leituras;
    }
    r['largura_' + w] = await page.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth].join('/'));
    const secs = [['topo', 'header.topo'], ['d0', '#d0'], ['d1', '#d1'], ['d2', '#d2'], ['d3', '#d3'], ['d4', '#d4'], ['d5', '#d5'], ['d6', '#d6'], ['visao', '#visao'], ['p81', '#P81'], ['p8', '#P8'], ['p9', '#P9'], ['p15', '#P15'], ['p29', '#P29'], ['p26', '#P26'], ['p31', '#P31'], ['p38', '#P38'], ['sintese', '#sintese'], ['revisao', '#revisao']];
    for (const [n, sel] of secs) {
      if (await page.locator(sel).count()) await page.locator(sel).screenshot({ path: TELAS + nome + '-' + n + '.png', timeout: 15000 });
    }
  }
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.locator('#d4').screenshot({ path: TELAS + 'escuro-d4.png' });
  await page.locator('#P38').screenshot({ path: TELAS + 'escuro-p38.png' });
  await page.emulateMedia({ colorScheme: 'light' });
  return JSON.stringify(r, null, 1);
}
