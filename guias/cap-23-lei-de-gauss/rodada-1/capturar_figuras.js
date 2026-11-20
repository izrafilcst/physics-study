// Captura figuras específicas pelo início da legenda. Uso: node capturar_figuras.js <html> <pasta> "Figura 2-2" "Figura 7-3" ...
const path = require('path');
const { chromium } = require('/home/swampert/.npm/_npx/9833c18b2d85bc59/node_modules/playwright');
(async () => {
  const [arq, pasta, ...legs] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome' });
  const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
  await p.goto('http://127.0.0.1:8723/' + arq); await p.waitForTimeout(2500);
  await p.evaluate(() => document.querySelectorAll('.nivel').forEach(n => n.hidden = false));
  for (const l of legs) {
    const f = p.locator('figure', { has: p.locator('figcaption', { hasText: l }) }).first();
    if (await f.count()) await f.screenshot({ path: path.join(pasta, 'fig-' + l.replace(/[^\w-]+/g, '_') + '.png') });
    else console.log('não achei', l);
  }
  await b.close();
})();
