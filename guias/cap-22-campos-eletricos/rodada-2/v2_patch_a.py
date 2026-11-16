"""v2, parte A: CSS, Degraus 0 a 2. Aplica sobre guia-v2.html (cópia da v1)."""
import sys

ARQ = '/home/swampert/Documents/fisica/guias/cap-22-campos-eletricos/guia-v2.html'
s = open(ARQ, encoding='utf-8').read()
erros = []


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        erros.append(f'[{c}x, esperado {n}] {old[:90]!r}')
        return
    s = s.replace(old, new)


# ---------------- CSS ----------------
rep('<title>Campos Elétricos — Guia</title>', '<title>Campos Elétricos — Guia v2</title>')
rep('.formula .eq-n { float: right; font-family: var(--f-ui); font-size: .8rem; color: var(--tinta-2); margin-top: .6rem; }',
    '.formula .eq-n { display: block; text-align: right; font-family: var(--f-ui); font-size: .8rem; color: var(--tinta-2); margin: -.3rem 0 .2rem; }')
rep('.passo { margin: .6rem 0; }\n.passo > b:first-child { font-family: var(--f-ui); font-size: .85rem; color: var(--acao); display: inline-block; min-width: 7.2rem; }',
    '.passo { margin: .6rem 0; display: grid; grid-template-columns: 7.6rem 1fr; gap: .2rem .6rem; align-items: baseline; }\n'
    '.passo > b:first-child { font-family: var(--f-ui); font-size: .85rem; color: var(--acao); }\n'
    '.passo > b:first-child:empty { visibility: hidden; }\n'
    '@media (max-width: 640px) { .passo { grid-template-columns: 1fr; } }\n'
    '.ferramentas { border: 2px solid var(--res); border-radius: 12px; padding: .4rem 1rem .8rem; margin: 1.2rem 0; background: var(--papel-3); }\n'
    '.ferramentas h3 { margin-top: .5rem; color: var(--res); }\n'
    '.ferramentas dt { font-family: var(--f-ui); font-weight: 700; margin-top: .6rem; }\n'
    '.ferramentas dd { margin: .15rem 0 0 0; }\n'
    '.duvida { border-left: 4px solid var(--res); padding: .2rem 0 .2rem .9rem; margin: 1rem 0; }\n'
    '.duvida .q { font-family: var(--f-ui); font-weight: 600; }\n'
    '.link-dt { font-family: var(--f-ui); font-size: .9rem; }')
rep('.fig > svg, .tela > svg { display: block; width: 100%; height: auto; max-width: 30rem; margin: 0 auto; background-color: var(--papel-3); background-image: linear-gradient(var(--grade) 1px, transparent 1px), linear-gradient(90deg, var(--grade) 1px, transparent 1px);',
    '.fig > svg, .tela > svg { display: block; width: 100%; height: auto; max-width: 30rem; margin: 0 auto; background-color: var(--papel-3); background-image: linear-gradient(var(--grade-2) 1px, transparent 1px), linear-gradient(90deg, var(--grade-2) 1px, transparent 1px);')
rep('  --grade: #d6e0ea;\n', '  --grade: #d6e0ea;\n  --grade-2: #e9eff4;\n')
rep('    --grade: #2a3848;\n', '    --grade: #2a3848;\n    --grade-2: #1b2632;\n')
rep('  --grade: #2a3848;\n  --pos: #ff7a7a;', '  --grade: #2a3848;\n  --grade-2: #1b2632;\n  --pos: #ff7a7a;')
rep('.conf button { font: inherit; font-size: .82rem;', '.conf button { white-space: nowrap; font: inherit; font-size: .82rem;')
rep('  .escada { display: flex; flex-direction: column-reverse; }\n', '')
# texto maior nos SVG em telas estreitas (o SVG encolhe com a largura)
rep('svg text { font-family: var(--f-ui); font-size: 14px; fill: var(--tinta); }',
    'svg text { font-family: var(--f-ui); font-size: 14px; fill: var(--tinta); }\n'
    '@media (max-width: 640px) {\n'
    '  .fig svg text, .tela svg text { font-size: 17px; }\n'
    '  .fig svg .t-2, .fig svg .t-s, .tela svg .t-2, .tela svg .t-s { font-size: 15px; }\n'
    '  .fig.larga > svg { min-width: 0; }\n'
    '}')

# ---------------- Degrau 0 ----------------
rep('<p>Seis perguntas, uma por ferramenta que o capítulo usa. Errou? Abre uma mini-revisão logo abaixo.</p>',
    '<p>Seis perguntas, uma por ferramenta que o capítulo usa. Errou? Abre uma mini-revisão logo abaixo. (Integrais e radianos voltam com calma no Degrau 4.)</p>')
rep('<div class="mini" data-oculto data-se="erro"><b>Mini-revisão.</b> A calculadora devolve atan(y/x) só entre −90° e +90°, e (−3, −4) dá a mesma razão que (3, 4). Faça assim: (1) ache o ângulo de referência, atan(|y|/|x|) = 53°; (2) desenhe o vetor para ver o quadrante; (3) ajuste: 3º quadrante → 180° + 53° = 233°.</div>',
    '<div class="mini" data-oculto data-se="erro"><b>Mini-revisão.</b> O plano tem quatro <b>quadrantes</b> (os quatro "quartos" separados pelos eixos), numerados no sentido anti-horário a partir do de x &gt; 0 e y &gt; 0. A tecla tan⁻¹ (arctan) devolve um ângulo só entre −90° e +90°, e (−3, −4) dá a mesma razão que (3, 4). Faça assim: (1) ache o <b>ângulo de referência</b>, o ângulo agudo com o eixo x: arctan(|y|/|x|) = 53°; (2) desenhe o vetor para ver o quadrante; (3) ajuste: 3º quadrante → 180° + 53° = 233°.</div>')
rep('Depois, "valor em cima menos valor embaixo": \\(-\\dfrac{1}{a+L} - \\left(-\\dfrac1a\\right) = \\dfrac1a - \\dfrac{1}{a+L}\\). E também: \\(\\int\\cos\\theta\\,d\\theta = \\sin\\theta\\).</div>',
    'Depois, "valor em cima menos valor embaixo": \\(-\\dfrac{1}{a+L} - \\left(-\\dfrac1a\\right) = \\dfrac1a - \\dfrac{1}{a+L}\\). No Degrau 4 você vai usar mais uma: \\(\\int\\cos\\theta\\,d\\theta = \\sin\\theta\\) (porque a derivada de sen θ é cos θ).</div>')

# ---------------- Degrau 1 ----------------
rep('Em engenharia, o campo decide quando o ar vira condutor e solta faísca: acima de uns 3 × 10⁶ N/C.</p>',
    'Em engenharia, o campo decide quando o ar vira condutor (passa a deixar a carga fluir) e solta faísca: acima de uns 3 × 10⁶ N/C, ou 3 kV por milímetro de ar.</p>')
rep('<div class="quebra"><strong>Onde a analogia quebra.</strong> (1) Preço é só um número; o campo é um <b>vetor</b>: diz quanto e para onde. (2) Não existe quilo negativo, mas existe carga negativa: ela sente a força no sentido <b>oposto</b> ao do campo. (3) Um comprador enorme pode mudar o preço da feira; uma carga grande empurra as cargas que criam o campo e muda o campo. Por isso a definição usa uma carga de teste pequena.</div>',
    '<div class="quebra"><strong>Onde a analogia quebra.</strong> (1) Preço é só um número; o campo é um <b>vetor</b>: diz quanto e para onde. (2) Não existe quilo negativo, mas existe carga negativa: ela sente a força no sentido <b>oposto</b> ao do campo. (3) Um comprador enorme pode mudar o preço da feira. Aqui, uma carga grande só muda o campo se as cargas que o criam puderem se mexer (num metal, por exemplo); por isso a definição usa uma carga de prova pequena. Com as fontes presas no lugar, F = qE vale para qualquer q. (4) Preços de barracas diferentes não se somam; campos de cargas diferentes, sim (é o Degrau 2).</div>')
rep('<p>Virando a conta ao contrário: uma carga q qualquer, num ponto onde o campo é \\(\\vec E\\), sente</p>',
    '<p>Virando a conta ao contrário: uma carga q qualquer, num ponto onde o campo é \\(\\vec E\\), sente (os números das equações são os do livro, para você conseguir voltar a ele)</p>')
rep('<p><b>Linhas de campo</b> são o desenho do campo inteiro: em cada ponto, o campo é tangente à linha;',
    '<p><b>Linhas de campo</b> são o desenho do campo inteiro: em cada ponto, o campo é tangente à linha (encosta nela, na mesma direção);')
# Fig. 1-2: seta de 2r também no eixo horizontal
rep('<text x="150" y="98" class="t-2">r</text><text x="160" y="30" class="t-2">2r</text>',
    '<line class="ve" x1="189" y1="105" x2="197" y2="105" style="stroke-width:2"/><text x="150" y="98" class="t-2">r</text><text x="184" y="98" class="t-2">2r</text>')
# previsão nova do W1
rep('<p class="enun"><b>Antes de mexer:</b> se você dobrar a distância r entre a carga e o ponto P, o campo em P fica…</p>\n    <div class="alts">\n      <button class="alt" type="button" data-fb="Seria assim se E caísse com 1/r. Ele cai com 1/r².">pela metade</button>\n      <button class="alt" type="button" data-fb="O campo depende de r: mais longe, mais fraco.">igual</button>\n      <button class="alt" type="button" data-ok="1" data-fb="Isso: r² fica 4 vezes maior, E fica 4 vezes menor. Confira no widget.">um quarto</button>\n      <button class="alt" type="button" data-fb="Ao contrário: afastar enfraquece o campo.">o dobro</button>',
    '<p class="enun"><b>Antes de mexer:</b> você dobra a distância r entre a carga e o ponto P <b>e</b> dobra a carga. O campo em P fica…</p>\n    <div class="alts">\n      <button class="alt" type="button" data-fb="A carga dobrada dobra o campo, mas a distância dobrada o divide por 4 (1/r²): não se compensam.">igual</button>\n      <button class="alt" type="button" data-ok="1" data-fb="Isso: 2/2² = 1/2. A carga ganha um fator 2, a distância tira um fator 4. Confira no widget (+2,0 nC e r = 2).">pela metade</button>\n      <button class="alt" type="button" data-fb="Um quarto seria só dobrando a distância. A carga também dobrou.">um quarto</button>\n      <button class="alt" type="button" data-fb="Afastar enfraquece com o quadrado da distância; dobrar a carga não compensa isso.">o dobro</button>')
rep('<h3>Experimente: o campo cai com 1/r²</h3>', '<h3>Experimente: o campo cai com 1/r², e a força segue o sinal</h3>')
rep('        <text id="w1-rt" x="70" y="142" class="t-2">r</text>\n      </svg>',
    '        <text id="w1-rt" x="70" y="142" class="t-2">r</text>\n        <line id="w1-f" class="vk" x1="110" y1="56" x2="110" y2="56"/>\n        <text id="w1-ft" x="114" y="48" class="t-s"></text>\n        <text id="w1-et" x="114" y="74" class="t-e t-s">E</text>\n      </svg>')
rep('<div>Carga: <span class="seg" id="w1-sinal"><button type="button" aria-pressed="true" data-v="1">+1,0 nC</button><button type="button" aria-pressed="false" data-v="2">+2,0 nC</button><button type="button" aria-pressed="false" data-v="-1">−1,0 nC</button></span></div>',
    '<div>Carga que cria o campo: <span class="seg" id="w1-sinal"><button type="button" aria-pressed="true" data-v="1">+1,0 nC</button><button type="button" aria-pressed="false" data-v="2">+2,0 nC</button><button type="button" aria-pressed="false" data-v="-1">−1,0 nC</button></span></div>\n      <div>Carga colocada em P: <span class="seg" id="w1-prova"><button type="button" aria-pressed="true" data-v="0">nenhuma</button><button type="button" aria-pressed="false" data-v="1">+1 pC</button><button type="button" aria-pressed="false" data-v="-1">−1 pC</button></span></div>')
# legenda do roteiro antes do primeiro exemplo + verificação nova do hidrogênio
rep('  <div class="exemplo">\n    <h3>Exemplo resolvido: o campo dentro do átomo de hidrogênio</h3>',
    '  <p class="pequeno"><b>Como os exemplos estão organizados.</b> Toda resolução deste guia segue os mesmos cinco passos: <b>Entender</b> (desenho, dados, incógnita) → <b>Modelar</b> (que lei vale e com que hipóteses) → <b>Resolver em símbolos</b> → <b>Calcular</b> (no SI) → <b>Verificar</b> (unidade, ordem de grandeza, casos-limite, sinal).</p>\n  <div class="exemplo">\n    <h3>Exemplo resolvido: o campo dentro do átomo de hidrogênio</h3>')
rep('<p class="passo"><b>Verificar</b> Unidade: C × N/C = N. A força bate com a lei de Coulomb do Cap. 21 (\\(ke^2/r^2\\), o mesmo número). Ordem de grandeza: esse campo é 170 mil vezes o que faz o ar soltar faísca; por isso é tão difícil arrancar o elétron do átomo.</p>',
    '<p class="passo"><b>Verificar</b> Unidade: C × N/C = N. Ordem de grandeza: F é 9 × 10²¹ vezes o peso do elétron (8,9 × 10⁻³⁰ N), então dentro do átomo a gravidade não conta. E o campo é 170 mil vezes o que faz o ar soltar faísca.</p>')
# Millikan: massa específica, diagrama, mensagem corrigida
rep('<p>Uma gota de óleo de raio 1,64 µm e massa específica 0,851 g/cm³ fica <b>parada</b>',
    '<p>Uma gota de óleo de raio 1,64 µm e massa específica (massa por volume, ρ = m/V) 0,851 g/cm³ fica <b>parada</b>')
rep('<p class="passo"><b>Entender</b> Parada → equilíbrio entre peso e força elétrica.</p>\n    <p class="passo"><b>Modelar</b> \\(m = \\rho\\,\\tfrac43\\pi r^3\\)',
    '<div class="lado"><p class="passo"><b>Entender</b> Parada → equilíbrio entre peso e força elétrica. Desenhe as duas forças.</p>\n    <figure class="fig"><svg viewBox="0 0 220 150" role="img" aria-label="Diagrama de forças da gota: peso mg para baixo, força elétrica para cima, campo E para baixo ao lado."><circle cx="90" cy="75" r="16" style="fill:var(--papel-2);stroke:var(--tinta)"/><line class="vk" x1="90" y1="91" x2="90" y2="140"/><text x="98" y="134">mg</text><line class="vk" x1="90" y1="59" x2="90" y2="10"/><text x="98" y="22">|q|E</text><line class="ve" x1="180" y1="30" x2="180" y2="120"/><text x="188" y="80" class="t-e">E</text></svg><figcaption>Forças na gota.</figcaption></figure></div>\n    <p class="passo"><b>Modelar</b> \\(m = \\rho\\,\\tfrac43\\pi r^3\\)')
rep('[[1.572e-11,"Você deixou a densidade em g/cm³ ou o raio em cm? Passe tudo para o SI: 851 kg/m³ e 1,64 × 10⁻⁶ m."]',
    '[[1.572e-11,"Esse número é a massa em gramas. Passe para kg: 1 g = 10⁻³ kg (e use 851 kg/m³ e 1,64 × 10⁻⁶ m)."]')
rep('no Cap. 28, o campo magnético faz força \\(q\\vec v\\times\\vec B\\).</p>', 'no Cap. 28, o campo magnético também faz força numa carga, mas só se ela estiver em movimento.</p>')

# ---------------- Degrau 2 ----------------
rep('<p>Nos outros casos, os campos apontam para o mesmo lado e se somam.</p>',
    '<p>Nos outros casos, os campos apontam para o mesmo lado e se somam.</p>\n      <p>Quem ganha não é a carga maior: é a de maior <b>|q|/r²</b>.</p>')
rep('<p>Para cancelar de verdade, falta o módulo empatar: \\(k|q_1|/r_1^2 = k|q_2|/r_2^2\\). Ou seja, <b>|q| proporcional a r²</b>: uma carga 4 vezes maior a uma distância 2 vezes maior faz o mesmo campo.</p>',
    '')
rep('<div class="quebra"><strong>Onde a analogia quebra.</strong> Ventiladores reais sopram num cone e os ventos se misturam;',
    '<div class="quebra"><strong>Onde a analogia quebra.</strong> O barquinho é a carga de prova, que é <b>positiva</b>; um elétron seria um barco que o ventilador puxa. Ventiladores reais sopram num cone e os ventos se misturam;')
# previsão nova do W2 (o mais perto ganha)
rep('<p class="enun"><b>Antes de mexer:</b> uma carga de +1 nC está 1 cm à esquerda de P, e uma de +4 nC está 2 cm à direita de P. O campo total em P…</p>\n    <div class="alts">\n      <button class="alt" type="button" data-fb="A carga +1 empurra P para a direita, mas a +4 empurra para a esquerda, e com a mesma força: 4/2² = 1/1².">aponta para a direita</button>\n      <button class="alt" type="button" data-fb="A carga maior não ganha sozinha: ela está mais longe. O que conta é |q|/r².">aponta para a esquerda (a carga maior ganha)</button>\n      <button class="alt" type="button" data-ok="1" data-fb="Isso: lados opostos e mesmo sinal → sentidos opostos; e 1/1² = 4/2² → mesmo módulo. Confira no widget.">é zero</button>\n      <button class="alt" type="button" data-fb="k multiplica os dois campos igualmente; não muda quem ganha.">depende do valor de k</button>',
    '<p class="enun"><b>Antes de mexer:</b> uma carga de +1 nC está 1 cm à esquerda de P, e uma de +4 nC está 3 cm à direita de P. O campo total em P…</p>\n    <div class="alts">\n      <button class="alt" type="button" data-fb="A +4 é maior, mas está 3 vezes mais longe: 4/3² = 0,44, contra 1/1² = 1 da outra.">aponta para a esquerda (a carga maior ganha)</button>\n      <button class="alt" type="button" data-fb="Para zerar, |q|/r² teria de empatar: 1/1² = 1 contra 4/3² = 0,44. Não empata.">é zero</button>\n      <button class="alt" type="button" data-ok="1" data-fb="Isso: 1/1² = 1 contra 4/3² = 0,44. A mais perto ganha: 8,99 × 10⁴ − 4,0 × 10⁴ = 5,0 × 10⁴ N/C para a direita. Confira no widget, e procure uma posição de B que zere o campo.">aponta para a direita</button>\n      <button class="alt" type="button" data-fb="k multiplica os dois campos igualmente; não muda quem ganha.">depende do valor de k</button>')
rep('<label>Carga B (nC): <input type="range" id="w2-qb" min="-4" max="4" step="1" value="4"></label>\n      <label>Posição de B (cm): <input type="range" id="w2-xb" min="-4" max="4" step="1" value="2"></label>',
    '<label>Carga B (nC): <input type="range" id="w2-qb" min="-4" max="4" step="1" value="4"></label>\n      <label>Posição de B (cm): <input type="range" id="w2-xb" min="-4" max="4" step="1" value="3"></label>')
rep('<p class="pequeno">Tente: mesmo lado com sinais opostos; lados opostos com sinais opostos. Quando os campos se cancelam?</p>',
    '<p class="pequeno">Tente: ache uma posição de B (com +4 nC) que zere o campo em P. Depois teste mesmo lado com sinais opostos. Quando os campos se cancelam?</p>')
# Fig. 2-2 com a seta do total
rep('<line class="ve" x1="200" y1="60" x2="240" y2="60"/><text x="245" y="64" class="t-e t-s">E<tspan dy="4" style="font-size:10px">B</tspan></text>',
    '<line class="ve" x1="200" y1="60" x2="240" y2="60"/><text x="245" y="64" class="t-e t-s">E<tspan dy="4" style="font-size:10px">B</tspan></text>\n        <line class="vr" x1="200" y1="100" x2="300" y2="100"/><text x="304" y="104" class="t-r t-s">E total</text>')
rep('<figcaption>Figura 2-2. A empurra P para longe (para +x); B puxa P para si (também para +x).</figcaption>',
    '<figcaption>Figura 2-2. A empurra P para longe (para +x); B puxa P para si (também para +x). O total (roxo) é a soma dos dois.</figcaption>')
rep('<p class="passo"><b>Calcular</b> \\(E_A = \\dfrac{(8{,}99\\times10^9)(2{,}0\\times10^{-9})}{(0{,}020)^2}',
    '<p class="passo"><b>Calcular</b> Em metros: 2,0 cm = 0,020 m e 3,0 cm = 0,030 m. \\(E_A = \\dfrac{(8{,}99\\times10^9)(2{,}0\\times10^{-9})}{(0{,}020)^2}')
# lacuna nova: mesmo lado, sinais opostos, sem cancelar
rep('<p>\\(q_C = +1{,}0\\) nC está em x = +1,0 cm e \\(q_D = -4{,}0\\) nC em x = +2,0 cm. Qual é o campo na origem?</p>',
    '<p>\\(q_C = +1{,}0\\) nC está em x = +1,0 cm e \\(q_D = -3{,}0\\) nC em x = +2,0 cm. Qual é o campo na origem?</p>')
rep('aria-label="Eixo x. Ponto P na origem. Carga C positiva, +1,0 nC, em x = 1,0 cm. Carga D negativa, −4,0 nC, em x = 2,0 cm. Sem setas: desenhe você."',
    'aria-label="Eixo x. Ponto P na origem. Carga C positiva, +1,0 nC, em x = 1,0 cm. Carga D negativa, −3,0 nC, em x = 2,0 cm. Sem setas: desenhe você."')
rep('<text x="300" y="38" class="t-n">D: −4,0 nC</text>', '<text x="300" y="38" class="t-n">D: −3,0 nC</text>')
rep('data-erros=\'[[8.99e8,"Você usou r = 1 em vez de 0,010 m? Passe cm para m antes de elevar ao quadrado."]]\'',
    'data-erros=\'[[8.99,"Você usou r = 1 m? Passe 1,0 cm para 0,010 m antes de elevar ao quadrado."],[8.99e8,"Você converteu duas vezes? 1,0 cm = 0,010 m, e r² = 1,0 × 10⁻⁴ m²."]]\'')
rep('<div class="num" id="lac-r-3" data-lacuna="1" data-rot="E_D (módulo) =" data-unid="N/C" data-resp="8.99e4" data-mostra="8,99 × 10⁴ N/C (4 vezes a carga, 2 vezes a distância)" data-erros=\'[[3.596e5,"Você usou r = 1 cm para D? D está a 2,0 cm de P."],[1.798e5,"Você elevou r ao quadrado? 2² = 4, não 2."]]\'></div>',
    '<div class="num" id="lac-r-3" data-lacuna="1" data-rot="E_D (módulo) =" data-unid="N/C" data-resp="6.742e4" data-mostra="6,74 × 10⁴ N/C (3 vezes a carga, 2 vezes a distância: 3/4 do de C)" data-erros=\'[[2.697e5,"Você usou r = 1 cm para D? D está a 2,0 cm de P."],[1.349e5,"Você elevou r ao quadrado? (0,020)² = 4,0 × 10⁻⁴ m²."]]\'></div>')
rep('<div class="num" id="lac-r-5" data-lacuna="1" data-rot="Campo total em P, E_x =" data-unid="N/C" data-resp="0" data-abs="900" data-mostra="0: os dois campos têm o mesmo módulo e sentidos opostos" data-erros=\'[[1.798e5,"Você somou os módulos. Os sentidos são opostos: um é −x, o outro +x."],[-1.798e5,"Os sentidos são opostos: some com sinais, −8,99 × 10⁴ + 8,99 × 10⁴."]]\'></div>',
    '<div class="num" id="lac-r-5" data-lacuna="1" data-sinal="1" data-rot="Campo total em P, E_x (com sinal; + é para a direita) =" data-unid="N/C" data-resp="-2.248e4" data-mostra="−2,25 × 10⁴ N/C: sentidos opostos, mas os módulos não empatam (1/1² contra 3/2²), e C, mais perto, ganha" data-erros=\'[[1.573e5,"Você somou os módulos. Os sentidos são opostos: um é −x, o outro +x."],[-1.573e5,"Os sentidos são opostos: some com sinais, −8,99 × 10⁴ + 6,74 × 10⁴."],[0,"Zero só se |q|/r² empatasse: 1/1² = 1 contra 3/2² = 0,75."]]\'></div>')
rep('<li><b>Muita gente pensa</b> que campo zero num ponto quer dizer "não há cargas por perto". <b>Na verdade</b> pode haver cargas enormes cujos campos se cancelam exatamente ali.</li>',
    '<li><b>Muita gente pensa</b> que campo zero num ponto quer dizer "não há cargas por perto" (ou que errou a conta). <b>Na verdade</b> pode haver cargas enormes cujos campos se cancelam exatamente ali. Zero é uma resposta possível: confira por pares, comparando |q|/r² e os sentidos.</li>')
rep('<line class="cota" x1="75" y1="214" x2="135" y2="214"/><line class="cota" x1="135" y1="214" x2="195" y2="214"/><line class="cota" x1="195" y1="214" x2="255" y2="214"/><line class="cota" x1="255" y1="214" x2="315" y2="214"/>',
    '<line class="cota" x1="77" y1="214" x2="133" y2="214"/><line class="cota" x1="137" y1="214" x2="193" y2="214"/><line class="cota" x1="197" y1="214" x2="253" y2="214"/><line class="cota" x1="257" y1="214" x2="313" y2="214"/>')
rep('<svg viewBox="0 0 360 220" role="img" aria-label="Pergunta 4 do livro:', '<svg viewBox="0 0 360 236" role="img" aria-label="Pergunta 4 do livro:')
rep('<line class="cota" x1="257" y1="214" x2="313" y2="214"/>',
    '<line class="cota" x1="257" y1="214" x2="313" y2="214"/>\n        <text x="101" y="231" class="t-2">d</text><text x="161" y="231" class="t-2">d</text><text x="221" y="231" class="t-2">d</text><text x="281" y="231" class="t-2">d</text>')
rep('(Pergunta par: resposta calculada pelo guia.)', '(Pergunta de número par: o livro não traz gabarito; resposta calculada pelo guia.)')

# checkpoints: regra completa de avanço
rep('    <h3>Checkpoint do Degrau 1</h3>\n    <p class="pequeno">Marque a confiança antes de conferir. Suba quando acertar 2 de 3 de primeira.</p>',
    '    <h3>Checkpoint do Degrau 1</h3>')
REGRA = '<p class="pequeno">Marque a confiança antes de conferir. Acertou 2 ou 3 de primeira: suba. Acertou 0 ou 1: releia os blocos que o feedback indicar, refaça as que errou e então siga (a página deixa marcar o degrau como concluído).</p>'
for n in range(1, 7):
    rep(f'<h3>Checkpoint do Degrau {n}</h3>', f'<h3>Checkpoint do Degrau {n}</h3>\n    {REGRA}')

open(ARQ, 'w', encoding='utf-8').write(s)
print('erros:' if erros else 'ok, sem erros')
for e in erros:
    print(' ', e)
sys.exit(1 if erros else 0)
