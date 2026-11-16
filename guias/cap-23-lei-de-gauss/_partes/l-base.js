<script>
(function () {
  'use strict';
  var CHAVE = 'guia-cap23-v1';
  var DEGRAUS = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7'];
  var QUESTOES = ['P5', 'P24', 'P52', 'P76', 'P29', 'P39', 'P53'];
  var est = {};
  try { est = JSON.parse(localStorage.getItem(CHAVE) || '{}') || {}; } catch (e) { est = {}; }
  est.r = est.r || {};    // respostas: id -> {ok, primeira, conf, tent, v}
  est.aj = est.aj || {};  // ajuda: questão -> maior nível aberto
  est.deg = est.deg || {};
  est.ref = est.ref || {};
  function salvar() { try { localStorage.setItem(CHAVE, JSON.stringify(est)); } catch (e) {} }

  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function el(tag, attrs, txt) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    if (txt != null) n.textContent = txt;
    return n;
  }

  /* ---------- números em pt-BR ---------- */
  var SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
  function fmt(v, d) { return (Math.round(v * Math.pow(10, d)) / Math.pow(10, d)).toFixed(d).replace('.', ',').replace('-', '−'); }
  function fmtSci(v, sig) {
    sig = sig || 3;
    if (v === 0) return '0';
    var ex = Math.floor(Math.log10(Math.abs(v)));
    var m = v / Math.pow(10, ex);
    if (Math.abs(m) >= 9.995) { m /= 10; ex += 1; }
    if (ex >= -2 && ex <= 2) return fmt(v, Math.max(0, sig - 1 - ex));
    return fmt(m, sig - 1) + ' × 10' + String(ex).split('').map(function (c) { return SUP[c]; }).join('');
  }

  /* ---------- leitor de números: vírgula, ×10^, sobrescritos, π, √, frações ---------- */
  var SUPINV = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-', '⁺': '+' };
  function lerNumero(txt, unid) {
    var s = String(txt || '').trim();
    if (!s) return { erro: 'Digite um número.' };
    if (unid) {
      var u = unid.replace(/[()]/g, '').trim();
      if (u && s.toLowerCase().slice(-u.length) === u.toLowerCase()) s = s.slice(0, -u.length).trim();
    }
    s = s.replace(/°|graus?/gi, '').replace(/[−–—]/g, '-').replace(/\s+/g, '');
    s = s.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+/g, function (m) { return '^(' + m.split('').map(function (c) { return SUPINV[c]; }).join('') + ')'; });
    s = s.replace(/,/g, '.').replace(/[×·]/g, '*').replace(/(\d)[xX](?=\d)/g, '$1*').replace(/\*\*/g, '^');
    s = s.replace(/sqrt/gi, '√').replace(/pi/gi, 'π');
    var i = 0;
    function pk() { return s[i]; }
    function numero() {
      var m = /^(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?/.exec(s.slice(i));
      if (!m) throw new Error('x');
      i += m[0].length; return parseFloat(m[0]);
    }
    function primario() {
      var c = pk();
      if (c === '(') { i++; var v = expr(); if (pk() !== ')') throw new Error('x'); i++; return v; }
      if (c === 'π') { i++; return Math.PI; }
      if (c === '√') { i++; return Math.sqrt(unario()); }
      return numero();
    }
    function potencia() { var b = primario(); if (pk() === '^') { i++; return Math.pow(b, unario()); } return b; }
    function unario() { if (pk() === '-') { i++; return -unario(); } if (pk() === '+') { i++; return unario(); } return potencia(); }
    function termo() {
      var v = unario();
      for (;;) {
        var c = pk();
        if (c === '*') { i++; v *= unario(); }
        else if (c === '/') { i++; v /= unario(); }
        else if (c === 'π' || c === '√' || c === '(') { v *= unario(); }
        else return v;
      }
    }
    function expr() {
      var v = termo();
      for (;;) {
        var c = pk();
        if (c === '+') { i++; v += termo(); } else if (c === '-') { i++; v -= termo(); } else return v;
      }
    }
    try {
      var v = expr();
      if (i !== s.length || !isFinite(v)) throw new Error('x');
      return { v: v };
    } catch (e) {
      return { erro: 'Não consegui ler "' + txt + '". Digite só o número (a unidade já está indicada), como 1,38e-10 ou 1,38×10^-10.' };
    }
  }

  function bate(v, alvo, box) {
    if (box.dataset.ang) { var d = (((v - alvo) % 360) + 540) % 360 - 180; return Math.abs(d) <= 1.5; }
    if (box.dataset.abs) return Math.abs(v - alvo) <= parseFloat(box.dataset.abs);
    var tol = parseFloat(box.dataset.tol || '0.02');
    return Math.abs(v - alvo) <= tol * Math.abs(alvo);
  }

  /* ---------- confiança ---------- */
  function linhaConfianca(box) {
    var wrap = el('span', { class: 'conf', role: 'group', 'aria-label': 'Sua confiança' });
    wrap.appendChild(el('span', null, 'Confiança:'));
    [['1', 'chute'], ['2', 'acho que sim'], ['3', 'certeza']].forEach(function (p) {
      var b = el('button', { type: 'button', 'aria-pressed': 'false', 'data-c': p[0] }, p[0] + ' ' + p[1]);
      b.addEventListener('click', function () {
        $$('button', wrap).forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
        b.setAttribute('aria-pressed', 'true');
        box.dataset.confEscolhida = p[0];
      });
      wrap.appendChild(b);
    });
    return wrap;
  }

  function registrar(id, ok, box) {
    var r = est.r[id] || { tent: 0 };
    r.tent = (r.tent || 0) + 1;
    if (r.primeira == null) {
      r.primeira = ok;
      r.conf = box.dataset.confEscolhida ? parseInt(box.dataset.confEscolhida, 10) : null;
    }
    if (ok) r.ok = true;
    est.r[id] = r;
    salvar();
    atualizarTudo();
  }

  /* ---------- quizzes de alternativas ---------- */
  function montarQuiz(box) {
    var id = box.id;
    var alts = $$('.alt', box);
    var letras = 'abcdefg';
    alts.forEach(function (b, k) {
      var l = el('span', { class: 'let' }, letras[k] + ')');
      b.insertBefore(l, b.firstChild);
      b.setAttribute('role', 'radio');
      b.setAttribute('aria-checked', 'false');
    });
    var grupo = $('.alts', box);
    if (grupo) grupo.setAttribute('role', 'radiogroup');
    var fb = el('p', { class: 'fb', 'aria-live': 'polite' });

    if (box.dataset.tipo === 'palpite') {
      alts.forEach(function (b, k) {
        b.addEventListener('click', function () {
          alts.forEach(function (x) { x.setAttribute('aria-checked', 'false'); });
          b.setAttribute('aria-checked', 'true');
          est.palpite = { k: k, txt: b.textContent.replace(/^[a-g]\)/, '').trim() };
          salvar();
          fb.className = 'fb';
          fb.textContent = 'Palpite guardado. A resposta aparece no Degrau 3.';
          mostrarPalpite();
        });
      });
      box.appendChild(fb);
      if (est.palpite && alts[est.palpite.k]) { alts[est.palpite.k].setAttribute('aria-checked', 'true'); fb.textContent = 'Palpite guardado.'; }
      return;
    }

    alts.forEach(function (b) {
      b.addEventListener('click', function () {
        alts.forEach(function (x) { x.setAttribute('aria-checked', 'false'); });
        b.setAttribute('aria-checked', 'true');
      });
    });
    var linha = el('div', { class: 'linha-acao' });
    var querConf = box.dataset.conf === '1';
    if (querConf) linha.appendChild(linhaConfianca(box));
    var btn = el('button', { type: 'button', class: 'btn' }, 'Conferir');
    linha.appendChild(btn);
    box.appendChild(linha);
    box.appendChild(fb);

    btn.addEventListener('click', function () {
      var esc = alts.filter(function (b) { return b.getAttribute('aria-checked') === 'true'; })[0];
      if (!esc) { fb.className = 'fb no'; fb.textContent = 'Escolha uma alternativa.'; return; }
      if (querConf && !box.dataset.confEscolhida && !(est.r[id] && est.r[id].primeira != null)) {
        fb.className = 'fb no'; fb.textContent = 'Marque sua confiança (1 a 3) antes de conferir.'; return;
      }
      var ok = esc.dataset.ok === '1';
      alts.forEach(function (b) { b.classList.remove('certa', 'errada'); });
      esc.classList.add(ok ? 'certa' : 'errada');
      fb.className = 'fb ' + (ok ? 'ok' : 'no');
      fb.textContent = ok ? 'Certo. ' : 'Ainda não. ';
      if (esc.dataset.fb) fb.appendChild(el('span', { class: 'expl' }, esc.dataset.fb));
      if (!ok && !box.dataset.prever) fb.appendChild(el('span', { class: 'expl' }, 'Pense de novo e escolha outra.'));
      var mini = $('.mini[data-se="erro"]', box);
      if (mini && !ok) mini.classList.add('mostrar');
      $$('[data-oculto]:not(.mini)', box).forEach(function (n) { if (ok) n.classList.add('mostrar'); });
      if (box.dataset.prever) destravar(box.dataset.prever);
      registrar(id, ok, box);
      verCheckpoint(box);
    });

    var r = est.r[id];
    if (r && r.ok) {
      alts.forEach(function (b) { if (b.dataset.ok === '1') { b.classList.add('certa'); b.setAttribute('aria-checked', 'true'); } });
      fb.className = 'fb ok'; fb.textContent = 'Você já acertou esta.';
      if (box.dataset.prever) destravar(box.dataset.prever);
    } else if (r && box.dataset.prever) { destravar(box.dataset.prever); }
  }

  /* ---------- campos numéricos ---------- */
  function montarNum(box) {
    var id = box.id;
    var campo = el('div', { class: 'campo' });
    var lab = el('label', { for: 'in-' + id }, box.dataset.rot || 'Resposta:');
    var inp = el('input', { id: 'in-' + id, type: 'text', inputmode: 'decimal', autocomplete: 'off', spellcheck: 'false' });
    var un = el('span', { class: 'unid' }, box.dataset.unid || '');
    campo.appendChild(lab); campo.appendChild(inp); campo.appendChild(un);
    var depois = $$('[data-oculto]', box);
    box.insertBefore(campo, box.firstChild);
    var linha = el('div', { class: 'linha-acao' });
    var querConf = box.dataset.conf === '1';
    if (querConf) linha.appendChild(linhaConfianca(box));
    var btn = el('button', { type: 'button', class: 'btn' }, 'Conferir');
    linha.appendChild(btn);
    var btnMostrar = null;
    if (box.dataset.lacuna) {
      btnMostrar = el('button', { type: 'button', class: 'btn sec', hidden: '' }, 'Mostrar a resposta');
      linha.appendChild(btnMostrar);
    }
    box.appendChild(linha);
    var fb = el('p', { class: 'fb', 'aria-live': 'polite' });
    box.appendChild(fb);
    depois.forEach(function (n) { box.appendChild(n); });

    function conferir() {
      var lido = lerNumero(inp.value, box.dataset.unid);
      if (lido.erro) { fb.className = 'fb no'; fb.textContent = lido.erro; return; }
      if (querConf && !box.dataset.confEscolhida && !(est.r[id] && est.r[id].primeira != null)) {
        fb.className = 'fb no'; fb.textContent = 'Marque sua confiança (1 a 3) antes de conferir.'; return;
      }
      var v = lido.v, alvo = parseFloat(box.dataset.resp);
      var ok = bate(v, alvo, box);
      fb.className = 'fb ' + (ok ? 'ok' : 'no');
      if (ok) {
        fb.textContent = 'Certo.';
        if (box.dataset.mostra) fb.appendChild(el('span', { class: 'expl' }, box.dataset.mostra));
        depois.forEach(function (n) { n.classList.add('mostrar'); });
      } else {
        var msg = null;
        try {
          JSON.parse(box.dataset.erros || '[]').forEach(function (par) {
            if (!msg && bate(v, par[0], { dataset: { tol: '0.02', ang: box.dataset.ang } })) msg = par[1];
          });
        } catch (e) {}
        if (!msg && box.dataset.sinal && bate(-v, alvo, box)) msg = 'O módulo está certo. E o sinal?';
        if (!msg && !box.dataset.ang && alvo !== 0 && v / alvo > 0) {
          var l = Math.log10(v / alvo);
          if (Math.abs(l - Math.round(l)) < 0.009 && Math.round(l) !== 0) msg = 'Os algarismos batem, mas a potência de 10 não. Confira prefixos (µ, n, p, f) e a conversão de cm para m.';
        }
        if (!msg && !box.dataset.ang && alvo !== 0 && v / alvo < 0 && !box.dataset.sinal && bate(-v, alvo, box)) msg = 'Aqui a resposta é um módulo (positivo).';
        fb.textContent = 'Ainda não. ';
        fb.appendChild(el('span', { class: 'expl' }, msg || 'Refaça a conta em símbolos, confira as unidades (tudo em SI) e tente de novo.'));
        if (btnMostrar) btnMostrar.hidden = false;
      }
      var r = est.r[id] || {};
      r.v = inp.value;
      est.r[id] = r;
      registrar(id, ok, box);
      verCheckpoint(box);
    }
    btn.addEventListener('click', conferir);
    inp.addEventListener('keydown', function (ev) { if (ev.key === 'Enter') conferir(); });
    if (btnMostrar) btnMostrar.addEventListener('click', function () {
      fb.className = 'fb';
      fb.textContent = 'Resposta: ' + (box.dataset.mostra || box.dataset.resp);
      depois.forEach(function (n) { n.classList.add('mostrar'); });
    });
    var r = est.r[id];
    if (r && r.v) inp.value = r.v;
    if (r && r.ok) { fb.className = 'fb ok'; fb.textContent = 'Você já acertou esta.'; depois.forEach(function (n) { n.classList.add('mostrar'); }); }
  }

  /* ---------- checkpoint ---------- */
  function verCheckpoint(box) {
    var cp = box.closest('.checkpoint');
    if (!cp) return;
    var itens = $$('.quiz', cp);
    var resp = itens.filter(function (q) { return est.r[q.id] && est.r[q.id].primeira != null; });
    var certas = itens.filter(function (q) { return est.r[q.id] && est.r[q.id].primeira === true; }).length;
    var ver = $('.veredito', cp);
    var deg = cp.dataset.degrau;
    ver.innerHTML = '';
    if (resp.length < itens.length) { ver.textContent = 'Respondidas: ' + resp.length + ' de ' + itens.length + '.'; return; }
    if (certas >= 2) {
      ver.textContent = 'Você acertou ' + certas + ' de ' + itens.length + ' de primeira. Pode subir!';
      if (!est.deg[deg]) { est.deg[deg] = true; salvar(); atualizarTudo(); }
    } else {
      ver.textContent = 'Você acertou ' + certas + ' de ' + itens.length + ' de primeira. Releia os blocos ligados às que errou e refaça. ';
      var b = el('button', { type: 'button', class: 'btn sec' }, est.deg[deg] ? 'Degrau marcado como concluído' : 'Marcar o degrau como concluído mesmo assim');
      b.addEventListener('click', function () { est.deg[deg] = true; salvar(); atualizarTudo(); b.textContent = 'Degrau marcado como concluído'; });
      ver.appendChild(b);
    }
  }

  /* ---------- ajuda em níveis ---------- */
  function montarAjuda(aj) {
    var q = aj.dataset.q;
    var niveis = $$('.nivel', aj);
    var barra = el('div', { class: 'botoes-ajuda', role: 'group', 'aria-label': 'Ajuda, um nível por vez' });
    var roteiro = $('.roteiro', aj);
    roteiro.parentNode.insertBefore(barra, roteiro.nextSibling);
    var reflexao = $('.reflexao', aj);
    var max = est.aj[q] || 0;
    var botoes = niveis.map(function (sec, k) {
      var n = k + 1;
      sec.id = sec.id || ('aj-' + q + '-' + n);
      var b = el('button', { type: 'button', 'aria-expanded': 'false', 'aria-controls': sec.id }, sec.dataset.titulo || ('Nível ' + n));
      if (n > max + 1) b.disabled = true;
      b.addEventListener('click', function () {
        var aberto = b.getAttribute('aria-expanded') === 'true';
        b.setAttribute('aria-expanded', aberto ? 'false' : 'true');
        sec.hidden = aberto;
        if (!aberto) {
          if (n > (est.aj[q] || 0)) { est.aj[q] = n; salvar(); }
          if (botoes[k + 1]) botoes[k + 1].disabled = false;
          if (n >= 4 && reflexao) reflexao.hidden = false;
        }
      });
      barra.appendChild(b);
      return b;
    });
    if (reflexao) {
      var ta = $('textarea', reflexao);
      if (est.ref[q]) ta.value = est.ref[q];
      ta.addEventListener('input', function () { est.ref[q] = ta.value; salvar(); });
      if (max >= 4) reflexao.hidden = false;
    }
  }

  function mostrarPalpite() {
    var p = $('[data-palpite]');
    if (!p) return;
    if (est.palpite) { p.hidden = false; p.textContent = 'Seu palpite no aquecimento: "' + est.palpite.txt + '". Compare com a conta abaixo.'; }
  }

  /* ---------- progresso, mapa e calibração ---------- */
  function questaoResolvida(q) {
    var art = document.getElementById(q);
    if (!art) return false;
    var partes = $$('.num[data-q], .quiz[data-q]', art);
    return partes.length > 0 && partes.every(function (p) { return est.r[p.id] && est.r[p.id].ok; });
  }
  function atualizarTudo() {
    var nd = DEGRAUS.filter(function (d) { return est.deg[d]; }).length;
    var nq = QUESTOES.filter(questaoResolvida).length;
    var pct = Math.round(100 * (nd + nq) / (DEGRAUS.length + QUESTOES.length));
    $('#prog-txt').textContent = 'Progresso: ' + nd + ' de ' + DEGRAUS.length + ' degraus, ' + nq + ' de ' + QUESTOES.length + ' questões';
    $('#prog-barra').style.width = pct + '%';
    $('.progresso .barra').setAttribute('aria-valuenow', String(pct));
    var atualMarcado = false;
    $$('.escada li').forEach(function (li) {
      var d = li.dataset.deg;
      var feito = d === 'd0' ? Object.keys(est.r).some(function (k) { return /^pre\d/.test(k); }) : !!est.deg[d];
      li.classList.toggle('feito', feito);
      li.classList.remove('atual');
      if (!feito && !atualMarcado) { li.classList.add('atual'); atualMarcado = true; }
    });
    $$('.chip-q').forEach(function (c) { c.classList.toggle('feito', questaoResolvida(c.dataset.q)); });
    var cal = $('#calibracao');
    if (cal) {
      var ids = Object.keys(est.r).filter(function (k) { return est.r[k].conf; });
      if (ids.length) {
        var c3 = ids.filter(function (k) { return est.r[k].conf === 3; });
        var erradas = c3.filter(function (k) { return est.r[k].primeira === false; });
        cal.innerHTML = '';
        cal.appendChild(el('p', null, 'Respostas com confiança marcada: ' + ids.length + '. Com "certeza" (3): ' + c3.length + ', das quais ' + erradas.length + ' erradas de primeira.'));
        if (erradas.length) {
          var ul = el('ul');
          erradas.forEach(function (k) {
            var alvo = document.getElementById(k);
            var li = el('li');
            var a = el('a', { href: '#' + k }, (alvo && alvo.closest('section, article') ? (alvo.closest('section, article').querySelector('h2, h3') || {}).textContent || k : k) + ' (' + k + ')');
            li.appendChild(a); ul.appendChild(li);
          });
          cal.appendChild(ul);
          cal.appendChild(el('p', { class: 'pequeno' }, 'Estas são as mais valiosas para revisar: você achava que sabia.'));
        } else {
          cal.appendChild(el('p', { class: 'pequeno' }, 'Nenhum erro com confiança máxima até agora.'));
        }
      }
    }
  }

  /* ---------- tema ---------- */
  function montarTema() {
    var b = $('#btn-tema');
    var nomes = { auto: 'automático', claro: 'claro', escuro: 'escuro' };
    var atual = 'auto';
    try { atual = localStorage.getItem('guia-cap23-tema') || 'auto'; } catch (e) {}
    function aplicar() {
      var h = document.documentElement;
      if (atual === 'claro') h.setAttribute('data-theme', 'light');
      else if (atual === 'escuro') h.setAttribute('data-theme', 'dark');
      else h.removeAttribute('data-theme');
      b.textContent = 'Tema: ' + nomes[atual];
    }
    b.addEventListener('click', function () {
      atual = atual === 'auto' ? 'claro' : atual === 'claro' ? 'escuro' : 'auto';
      try { localStorage.setItem('guia-cap23-tema', atual); } catch (e) {}
      aplicar();
    });
    aplicar();
  }

  /* ---------- widgets ---------- */
  var destravados = {};
  function destravar(w) {
    var n = document.getElementById(w);
    if (n) n.classList.remove('travado');
    destravados[w] = true;
  }
  function seg(id, cb) {
    var g = document.getElementById(id);
    $$('button', g).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('button', g).forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
        b.setAttribute('aria-pressed', 'true');
        cb();
      });
    });
  }
  function segVal(id) { var b = $('#' + id + ' button[aria-pressed="true"]'); return b ? b.dataset.v : null; }
  function attr(n, o) { Object.keys(o).forEach(function (k) { n.setAttribute(k, o[k]); }); }
  var SVGNS = 'http://www.w3.org/2000/svg';
  function svgEl(tag, o) { var n = document.createElementNS(SVGNS, tag); attr(n, o || {}); return n; }
  function usoCarga(q, x, y) { return svgEl('use', { href: q > 0 ? '#qp' : '#qn', x: x, y: y }); }
