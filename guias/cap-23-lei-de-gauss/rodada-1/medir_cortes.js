// Mede rótulos de SVG que saem da área visível (viewBox), estouro de largura a 390 px
// e fórmulas KaTeX com erro. Uso: node medir_cortes.js <arquivo.html> [porta]
const { chromium } = require('/home/swampert/.npm/_npx/9833c18b2d85bc59/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome' });
  const url = 'http://127.0.0.1:' + (process.argv[3] || '8723') + '/' + (process.argv[2] || 'guia-v2.html');
  for (const w of [1280, 390]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    await p.goto(url); await p.waitForTimeout(2500);
    await p.evaluate(() => { document.querySelectorAll('.widget').forEach(x => x.classList.remove('travado')); document.querySelectorAll('.nivel').forEach(n => n.hidden = false); document.querySelectorAll('[data-oculto]').forEach(n => n.classList.add('mostrar')); });
    const r = await p.evaluate(() => {
      const out = [];
      document.querySelectorAll('svg[viewBox]').forEach(svg => {
        const vb = svg.viewBox.baseVal; if (!vb || !vb.width) return;
        const fig = svg.closest('figure'); const cap = fig && fig.querySelector('figcaption') ? fig.querySelector('figcaption').textContent.slice(0, 40) : ((svg.closest('.widget') || svg.closest('[id]') || {}).id);
        svg.querySelectorAll('text').forEach(t => {
          let bb; try { bb = t.getBBox(); } catch (e) { return; }
          if (!bb.width) return;
          if (bb.x < vb.x - 0.5 || bb.y < vb.y - 0.5 || bb.x + bb.width > vb.x + vb.width + 0.5 || bb.y + bb.height > vb.y + vb.height + 0.5)
            out.push('  ' + cap + ' | "' + t.textContent + '" x=' + bb.x.toFixed(0) + '..' + (bb.x + bb.width).toFixed(0) + ' y=' + bb.y.toFixed(0) + '..' + (bb.y + bb.height).toFixed(0) + ' (vb ' + vb.width + 'x' + vb.height + ')');
        });
      });
      const larg = [...document.querySelectorAll('body *')].filter(el => { const rc = el.getBoundingClientRect(); if (rc.right <= innerWidth + 2 || !rc.width) return false; let a = el.parentElement; while (a) { const ox = getComputedStyle(a).overflowX; if (ox !== 'visible') return false; a = a.parentElement; } return true; }).slice(0, 8).map(el => '  ' + el.tagName + '.' + (el.className.baseVal !== undefined ? el.className.baseVal : el.className) + ' right=' + Math.round(el.getBoundingClientRect().right));
      const kerr = [...document.querySelectorAll('.katex .mord[style*="color"], .katex-error')].map(e => e.textContent).slice(0, 10);
      return { out, larg, kerr, sw: document.documentElement.scrollWidth };
    });
    console.log('== largura ' + w + ' (scrollWidth ' + r.sw + ')');
    if (w === 1280) { console.log('rótulos fora do viewBox:'); console.log(r.out.join('\n') || '  nenhum'); console.log('KaTeX com erro:', JSON.stringify(r.kerr)); }
    console.log('elementos estourando a largura:'); console.log(r.larg.join('\n') || '  nenhum');
    await p.close();
  }
  await b.close();
})();
