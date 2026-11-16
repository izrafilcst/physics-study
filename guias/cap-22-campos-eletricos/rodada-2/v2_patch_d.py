"""v2, parte D: correções achadas na verificação da v2 no navegador."""
import sys
ARQ = '/home/swampert/Documents/fisica/guias/cap-22-campos-eletricos/guia-v2.html'
s = open(ARQ, encoding='utf-8').read()
old = '.conf { display: inline-flex; gap: .25rem; align-items: center; }'
assert s.count(old) == 1, 'conf'
s = s.replace(old, '.conf { display: inline-flex; flex-wrap: wrap; gap: .25rem; align-items: center; }')
open(ARQ, 'w', encoding='utf-8').write(s)
print('ok')

# W5: rótulo "10" cortado na borda direita; "D/L" afastado dos números
s = open(ARQ, encoding='utf-8').read()
old = "      [0, 2, 4, 6, 8, 10].forEach(function (v) { var t = svgEl('text', { x: X(v) - 4, y: 216, class: 't-2' }); t.textContent = String(v); g.appendChild(t); });\n    }\n    attr($('#w5-m')"
assert s.count(old) == 1, 'w5 rotulos'
s = s.replace(old, "      [0, 2, 4, 6, 8].forEach(function (v) { var t = svgEl('text', { x: X(v) - 4, y: 216, class: 't-2' }); t.textContent = String(v); g.appendChild(t); });\n    }\n    attr($('#w5-m')")
old2 = '<text x="300" y="222" class="t-2">D/L</text><text x="46" y="20" class="t-2">erro (%), escala log</text>'
assert s.count(old2) == 1, 'w5 D/L'
s = s.replace(old2, '<text x="318" y="216" class="t-2">D/L</text><text x="46" y="20" class="t-2">erro (%), escala log</text>')
open(ARQ, 'w', encoding='utf-8').write(s)
print('ok W5')
