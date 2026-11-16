
  function pathDe(pts) { return pts.map(function (p, i) { return (i ? 'L ' : 'M ') + p[0].toFixed(1) + ' ' + p[1].toFixed(1); }).join(' '); }
  function zeroSeMinusculo(v) { return Math.abs(v) < 1e-9 ? 0 : v; }

  /* W1: quadrado girando num campo uniforme */
  function w1() {
    var th = parseFloat($('#w1-ang').value), t = th * Math.PI / 180;
    var cx = 180, cy = 120, L = 80;
    var nx = Math.cos(t), ny = -Math.sin(t);
    var dx = Math.sin(t), dy = Math.cos(t);
    attr($('#w1-placa'), { x1: cx - L * dx, y1: cy - L * dy, x2: cx + L * dx, y2: cy + L * dy });
    attr($('#w1-normal'), { x1: cx, y1: cy, x2: cx + 55 * nx, y2: cy + 55 * ny });
    var r = 30;
    $('#w1-arco').setAttribute('d', th < 3 ? '' : 'M ' + (cx + r) + ' ' + cy + ' A ' + r + ' ' + r + ' 0 0 0 ' + (cx + r * Math.cos(t)).toFixed(1) + ' ' + (cy - r * Math.sin(t)).toFixed(1));
    attr($('#w1-th'), { x: (cx + 42 * Math.cos(t / 2) - 4).toFixed(1), y: (cy - 42 * Math.sin(t / 2) + 4).toFixed(1) });
    var g = $('#w1-linhas'); g.innerHTML = '';
    var meia = L * Math.abs(Math.cos(t)), n = 0, tot = 0;
    for (var y = 30; y <= 210; y += 20) {
      var cruza = Math.abs(y - cy) < meia - 0.5;
      tot++; if (cruza) n++;
      var ln = svgEl('line', { x1: 15, x2: 345, y1: y, y2: y, class: cruza ? 've' : 'linha-campo' });
      if (!cruza) ln.setAttribute('style', 'marker-end:url(#m-k)');
      g.appendChild(ln);
    }
    var c = zeroSeMinusculo(Math.cos(t));
    var phi = zeroSeMinusculo(1000 * 0.01 * Math.cos(t));
    var sentido = c > 1e-6 ? 'o campo atravessa no sentido da normal: fluxo positivo.' : (c < -1e-6 ? 'o campo atravessa contra a normal: fluxo negativo.' : 'o campo passa rente ao quadrado: fluxo zero.');
    $('#w1-leitura').textContent = 'θ = ' + th + '°: cos θ = ' + fmt(c, 2) + '; Φ = E·A·cos θ = 1 000 × 0,0100 × ' + fmt(c, 2) + ' = ' + fmt(phi, 1) + ' N·m²/C. Linhas que atravessam o quadrado: ' + n + ' de ' + tot + '. Aqui ' + sentido;
  }

  /* W2: saldo de linhas numa superfície fechada */
  function formaW2(tipo) {
    var cx = 175, cy = 130, p = [], i;
    if (tipo === 'q') return [[cx - 80, cy - 80], [cx + 80, cy - 80], [cx + 80, cy + 80], [cx - 80, cy + 80]];
    if (tipo === 'c') { for (i = 0; i < 96; i++) { var a = 2 * Math.PI * i / 96; p.push([cx + 85 * Math.cos(a), cy + 85 * Math.sin(a)]); } return p; }
    for (i = 0; i < 120; i++) { var b = 2 * Math.PI * i / 120; var rr = 82 * (1 + 0.3 * Math.sin(3 * b) + 0.12 * Math.cos(2 * b)); p.push([cx + rr * Math.cos(b), cy + rr * Math.sin(b)]); }
    return p;
  }
  function dentroPoligono(pt, poly) {
    var x = pt[0], y = pt[1], dentro = false;
    for (var i = 0, j = poly.length - 1; i < poly.length; j = i++) {
      var xi = poly[i][0], yi = poly[i][1], xj = poly[j][0], yj = poly[j][1];
      if (((yi > y) !== (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi) + xi)) dentro = !dentro;
    }
    return dentro;
  }
  function cruzamentos(o, d, poly) {
    var ts = [];
    for (var i = 0; i < poly.length; i++) {
      var a = poly[i], b = poly[(i + 1) % poly.length];
      var ex = b[0] - a[0], ey = b[1] - a[1];
      var den = d[0] * ey - d[1] * ex;
      if (Math.abs(den) < 1e-12) continue;
      var t = ((a[0] - o[0]) * ey - (a[1] - o[1]) * ex) / den;
      var s = ((a[0] - o[0]) * d[1] - (a[1] - o[1]) * d[0]) / den;
      if (t > 1e-6 && s >= 0 && s < 1) ts.push(t);
    }
    return ts.sort(function (u, v) { return u - v; });
  }
  function w2() {
    var tipo = segVal('w2-tipo'), sB = parseFloat(segVal('w2-sinal')), xB = parseFloat($('#w2-x').value);
    var poly = formaW2(tipo);
    $('#w2-forma').setAttribute('d', pathDe(poly) + ' Z');
    var cargas = [{ nome: 'A', s: 1, p: [150, 125] }, { nome: 'B', s: sB, p: [xB, 150] }];
    var gR = $('#w2-raios'), gM = $('#w2-marcas'), gC = $('#w2-cargas');
    gR.innerHTML = ''; gM.innerHTML = ''; gC.innerHTML = '';
    var res = [];
    cargas.forEach(function (c) {
      var dentro = dentroPoligono(c.p, poly), sai = 0, entra = 0;
      for (var k = 0; k < 12; k++) {
        var ang = (k * 30 + 7) * Math.PI / 180, d = [Math.cos(ang), Math.sin(ang)];
        gR.appendChild(svgEl('line', { x1: c.p[0], y1: c.p[1], x2: c.p[0] + 500 * d[0], y2: c.p[1] + 500 * d[1], style: 'stroke:var(' + (c.s > 0 ? '--pos' : '--neg') + ');stroke-width:1;opacity:.45' }));
        cruzamentos(c.p, d, poly).forEach(function (t, idx) {
          var paraFora = dentro ? (idx % 2 === 0) : (idx % 2 === 1);
          var saiCampo = c.s > 0 ? paraFora : !paraFora;
          if (saiCampo) sai++; else entra++;
          gM.appendChild(svgEl('circle', { cx: (c.p[0] + t * d[0]).toFixed(1), cy: (c.p[1] + t * d[1]).toFixed(1), r: 3.6, class: saiCampo ? 'cruz-out' : 'cruz-in' }));
        });
      }
      gC.appendChild(usoCarga(c.s, c.p[0], c.p[1]));
      var tx = svgEl('text', { x: c.p[0] + 13, y: c.p[1] - 10, class: 't-s', style: 'font-weight:700' }); tx.textContent = c.nome; gC.appendChild(tx);
      res.push({ nome: c.nome, s: c.s, dentro: dentro, sai: sai, entra: entra });
    });
    var total = 0;
    var partes = res.map(function (r) {
      total += r.sai - r.entra;
      return r.nome + ' (' + (r.s > 0 ? '+' : '−') + ', ' + (r.dentro ? 'dentro' : 'fora') + '): ' + r.sai + ' saídas, ' + r.entra + ' entradas, saldo ' + (r.sai - r.entra > 0 ? '+' : '') + (r.sai - r.entra);
    });
    var qenv = res.filter(function (r) { return r.dentro; }).map(function (r) { return (r.s > 0 ? '+' : '−') + 'q'; });
    $('#w2-leitura').textContent = partes.join('. ') + '. Saldo total: ' + (total > 0 ? '+' : '') + total + ' linhas, proporcional à carga de dentro (' + (qenv.length ? qenv.join(' ') : 'nenhuma') + ').';
  }

  /* W3: esfera com cavidade */
  var W3G = false;
  function w3() {
    var a = parseFloat($('#w3-a').value), r = parseFloat($('#w3-r').value), S = 35;
    attr($('#w3-cav'), { r: a * S });
    attr($('#w3-gauss'), { r: Math.max(0.6, r * S) });
    function E(x) { if (x <= a) return 0; if (x <= 1) return (x * x * x - a * a * a) / (x * x); return (1 - a * a * a) / (x * x); }
    function X(x) { return 250 + 70 * x; }
    function Y(v) { return 200 - 150 * v; }
    if (!W3G) {
      var g = $('#w3-grade');
      [1, 2, 3].forEach(function (v) { var t = svgEl('text', { x: X(v) - 4, y: 216, class: 't-2' }); t.textContent = String(v); g.appendChild(t); });
      [[0.5, '0,5'], [1, '1']].forEach(function (p) { g.appendChild(svgEl('line', { x1: 250, x2: 470, y1: Y(p[0]), y2: Y(p[0]), class: 'grade-g' })); var t = svgEl('text', { x: 230, y: Y(p[0]) + 4, class: 't-2' }); t.textContent = p[1]; g.appendChild(t); });
      g.appendChild(svgEl('line', { x1: X(1), x2: X(1), y1: 20, y2: 200, class: 'fino' }));
      var tR = svgEl('text', { x: X(1) + 4, y: 36, class: 't-2' }); tR.textContent = 'R'; g.appendChild(tR);
      W3G = true;
    }
    var pts = [];
    for (var x = 0; x <= 3.0001; x += 0.01) pts.push([X(x), Y(E(x))]);
    $('#w3-curva').setAttribute('d', pathDe(pts));
    attr($('#w3-m'), { cx: X(r), cy: Y(E(r)) });
    var frac = r <= a ? 0 : (r >= 1 ? 1 : (r * r * r - a * a * a) / (1 - a * a * a));
    var regiao = r <= a ? (a > 0 ? 'Na cavidade: a gaussiana não envolve carga, E = 0.' : 'No centro: nada dentro, E = 0.')
      : (r <= 1 ? (a > 0 ? 'No material: quanto maior r, mais carga dentro.' : 'Dentro da esfera maciça: E cresce em linha reta com r.')
        : 'Fora: toda a carga já está dentro; E cai com 1/r², como uma carga pontual.');
    $('#w3-leitura').textContent = 'Cavidade a = ' + fmt(a, 1) + 'R; gaussiana r = ' + fmt(r, 2) + 'R: envolve ' + fmt(100 * frac, 1) + ' % da carga; E = ' + fmt(E(r), 3) + ' × ρR/(3ε₀). ' + regiao;
  }

  /* W4: cascas de cebola */
  var W4G = false;
  function w4() {
    var n = parseInt(segVal('w4-modo'), 10), r = parseFloat($('#w4-r').value);
    var g = $('#w4-aneis'); g.innerHTML = '';
    for (var i = 0; i < 10; i++) {
      var m = (i + 0.5) / 10;
      var dens = n === 0 ? 0.45 : 0.9 * m * m;
      g.appendChild(svgEl('circle', { cx: 115, cy: 115, r: (m * 70).toFixed(1), style: 'fill:none;stroke:var(--pos);stroke-width:7;stroke-opacity:' + (0.06 + dens).toFixed(2) }));
    }
    attr($('#w4-gauss'), { r: Math.max(0.6, r * 70) });
    function E(x, k) { return x <= 1 ? Math.pow(x, 1 + k) : 1 / (x * x); }
    function X(x) { return 250 + 140 * x; }
    function Y(v) { return 200 - 160 * v; }
    if (!W4G) {
      var gg = $('#w4-grade');
      [0.5, 1, 1.5].forEach(function (v) { var t = svgEl('text', { x: X(v) - 8, y: 216, class: 't-2' }); t.textContent = fmt(v, 1); gg.appendChild(t); });
      [[0.5, '0,5'], [1, '1']].forEach(function (p) { gg.appendChild(svgEl('line', { x1: 250, x2: 470, y1: Y(p[0]), y2: Y(p[0]), class: 'grade-g' })); var t = svgEl('text', { x: 230, y: Y(p[0]) + 4, class: 't-2' }); t.textContent = p[1]; gg.appendChild(t); });
      W4G = true;
    }
    function curva(k) { var p = []; for (var x = 0; x <= 1.5001; x += 0.01) p.push([X(x), Y(E(x, k))]); return pathDe(p); }
    $('#w4-curva').setAttribute('d', curva(n));
    $('#w4-outra').setAttribute('d', curva(n === 0 ? 2 : 0));
    attr($('#w4-m'), { cx: X(r), cy: Y(E(r, n)) });
    var frac = r >= 1 ? 1 : Math.pow(r, 3 + n);
    $('#w4-leitura').textContent = (n === 0 ? 'ρ uniforme' : 'ρ ∝ r²') + '; gaussiana r = ' + fmt(r, 2) + 'R: envolve ' + fmt(100 * frac, 1) + ' % da carga total; E = ' + fmt(E(r, n), 3) + ' × E(R). Tracejado: o outro modelo. ' + (r > 1 ? 'Fora, os dois coincidem: só a carga total importa.' : '');
  }

  /* W5: ponto, fio e placa */
  var W5G = false;
  function w5() {
    var geo = parseInt(segVal('w5-geo'), 10), r = parseFloat($('#w5-r').value);
    function X(x) { return 250 + 70 * (x - 1); }
    function Y(v) { return 200 - 160 * v; }
    function f(x, k) { return k === 0 ? 1 / (x * x) : (k === 1 ? 1 / x : 1); }
    if (!W5G) {
      [0, 1, 2].forEach(function (k) { var p = []; for (var x = 1; x <= 4.0001; x += 0.02) p.push([X(x), Y(f(x, k))]); $('#w5-c' + k).setAttribute('d', pathDe(p)); });
      var g = $('#w5-grade');
      [1, 2, 3, 4].forEach(function (v) { var t = svgEl('text', { x: X(v) - 4, y: 216, class: 't-2' }); t.textContent = String(v); g.appendChild(t); });
      [[0.5, '0,5'], [1, '1']].forEach(function (p) { g.appendChild(svgEl('line', { x1: 250, x2: 470, y1: Y(p[0]), y2: Y(p[0]), class: 'grade-g' })); var t = svgEl('text', { x: 230, y: Y(p[0]) + 4, class: 't-2' }); t.textContent = p[1]; g.appendChild(t); });
      W5G = true;
    }
    [0, 1, 2].forEach(function (k) { $('#w5-c' + k).style.strokeWidth = k === geo ? '3.6' : '1.6'; });
    attr($('#w5-m'), { cx: X(r), cy: Y(f(r, geo)) });
    var d = $('#w5-desenho'); d.innerHTML = '';
    var s = 22 * r;
    if (geo === 0) {
      d.appendChild(svgEl('circle', { cx: 115, cy: 115, r: s, class: 'gauss' }));
      d.appendChild(usoCarga(1, 115, 115));
    } else if (geo === 1) {
      d.appendChild(svgEl('rect', { x: 115 - s, y: 65, width: 2 * s, height: 100, class: 'gauss' }));
      d.appendChild(svgEl('line', { x1: 115, y1: 12, x2: 115, y2: 218, class: 'barra-p', style: 'stroke-width:5' }));
    } else {
      d.appendChild(svgEl('rect', { x: 115 - s, y: 95, width: 2 * s, height: 40, class: 'gauss' }));
      d.appendChild(svgEl('rect', { x: 109, y: 12, width: 12, height: 206, class: 'placa-p' }));
    }
    var t = svgEl('text', { x: 115, y: 228, class: 't-2', style: 'text-anchor:middle' });
    t.textContent = ['esfera gaussiana', 'lata gaussiana (de lado)', 'latinha (de lado)'][geo];
    d.appendChild(t);
    var area = geo === 0 ? 'a área da esfera gaussiana cresce com r² (×' + fmt(r * r, 2) + ')' : (geo === 1 ? 'a parede da lata cresce com r (×' + fmt(r, 2) + ')' : 'as tampas da latinha não crescem (×1)');
    $('#w5-leitura').textContent = ['Carga pontual', 'Fio longo', 'Placa grande'][geo] + ', r = ' + fmt(r, 2) + ' m: ' + area + ', e o mesmo fluxo se espalha por ela. E(r)/E(1 m) = ' + fmt(f(r, geo), 3) + '.';
  }

  /* W6: casca metálica com partícula dentro */
  function w6() {
    var q = parseInt($('#w6-q').value, 10), Q = parseInt($('#w6-Q').value, 10), fora = segVal('w6-pos') === 'f';
    var cx = 150, cy = 130, px = fora ? cx + 35 : cx, py = cy;
    var gp = $('#w6-part'), gs = $('#w6-sinais'), gc = $('#w6-campo');
    gp.innerHTML = ''; gs.innerHTML = ''; gc.innerHTML = '';
    if (q !== 0) gp.appendChild(usoCarga(q, px, py));
    else gp.appendChild(svgEl('circle', { cx: px, cy: py, r: 4, class: 'ponto' }));
    function sinal(s, x, y) { var t = svgEl('text', { x: x.toFixed(1), y: (y + 4).toFixed(1), class: s > 0 ? 'sinal-p' : 'sinal-n' }); t.textContent = s > 0 ? '+' : '−'; gs.appendChild(t); }
    var ni = Math.min(12, 2 * Math.abs(q));
    for (var i = 0; i < ni; i++) {
      var a = fora ? (ni === 1 ? 0 : (i / (ni - 1) - 0.5) * 2.4) : 2 * Math.PI * i / ni + 0.3;
      sinal(-q, cx + 76 * Math.cos(a), cy + 76 * Math.sin(a));
    }
    var qe = Q + q, ne = Math.min(16, 2 * Math.abs(qe));
    for (var j = 0; j < ne; j++) { var b = 2 * Math.PI * j / ne + 0.2; sinal(qe, cx + 89 * Math.cos(b), cy + 89 * Math.sin(b)); }
    if (q !== 0) {
      for (var k = 0; k < 6; k++) {
        var c = 2 * Math.PI * k / 6 + 0.5, r1 = 14, r2 = fora ? 28 : 40;
        var x1 = px + r1 * Math.cos(c), y1 = py + r1 * Math.sin(c), x2 = px + r2 * Math.cos(c), y2 = py + r2 * Math.sin(c);
        gc.appendChild(svgEl('line', q > 0 ? { x1: x1, y1: y1, x2: x2, y2: y2, class: 've' } : { x1: x2, y1: y2, x2: x1, y2: y1, class: 've' }));
      }
    }
    if (qe !== 0) {
      for (var m = 0; m < 8; m++) {
        var e = 2 * Math.PI * m / 8 + 0.39, a1 = 101, a2 = 122;
        var u1 = cx + a1 * Math.cos(e), v1 = cy + a1 * Math.sin(e), u2 = cx + a2 * Math.cos(e), v2 = cy + a2 * Math.sin(e);
        gc.appendChild(svgEl('line', qe > 0 ? { x1: u1, y1: v1, x2: u2, y2: v2, class: 've' } : { x1: u2, y1: v2, x2: u1, y2: v1, class: 've' }));
      }
    }
    function uc(v) { return (v > 0 ? '+' : (v < 0 ? '−' : '')) + Math.abs(v) + ' µC'; }
    var dist = q === 0 ? '' : (fora ? ', concentrada do lado da partícula' : ', uniforme');
    $('#w6-leitura').textContent = 'Partícula: ' + uc(q) + '. Casca: ' + uc(Q) + '. Superfície interna: −q = ' + uc(-q) + dist + '. Superfície externa: Q + q = ' + uc(qe) + (qe ? ', uniforme' : '') + '. Fora: ' + (qe ? 'campo de uma carga de ' + uc(qe) + ' no centro, ' + (qe > 0 ? 'para fora' : 'para dentro') : 'campo zero') + '. No metal: E = 0.';
  }

  function montarWidgets() {
    if ($('#w1')) { $('#w1-ang').addEventListener('input', w1); w1(); }
    if ($('#w2')) { $('#w2-x').addEventListener('input', w2); seg('w2-sinal', w2); seg('w2-tipo', w2); w2(); }
    if ($('#w3')) { $('#w3-a').addEventListener('input', w3); $('#w3-r').addEventListener('input', w3); w3(); }
    if ($('#w4')) { $('#w4-r').addEventListener('input', w4); seg('w4-modo', w4); w4(); }
    if ($('#w5')) { $('#w5-r').addEventListener('input', w5); seg('w5-geo', w5); w5(); }
    if ($('#w6')) { $('#w6-q').addEventListener('input', w6); $('#w6-Q').addEventListener('input', w6); seg('w6-pos', w6); w6(); }
  }

  function montarZerar() {
    var b = $('#btn-zerar');
    if (!b) return;
    b.addEventListener('click', function () {
      if (window.confirm('Apagar todo o seu progresso neste guia (respostas, checkpoints, anotações)?')) {
        try { localStorage.removeItem(CHAVE); } catch (e) {}
        location.reload();
      }
    });
  }

  /* ---------- início ---------- */
  function iniciar() {
    $$('.quiz').forEach(montarQuiz);
    $$('div.num').forEach(montarNum);
    $$('.ajuda').forEach(montarAjuda);
    montarTema();
    montarWidgets();
    montarZerar();
    mostrarPalpite();
    $$('.checkpoint').forEach(function (cp) { var q = $('.quiz', cp); if (q) verCheckpoint(q); });
    atualizarTudo();
    setTimeout(function () {
      if (!document.documentElement.classList.contains('katex-ok')) document.documentElement.classList.add('katex-falhou');
    }, 6000);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
</script>
</body>
</html>
