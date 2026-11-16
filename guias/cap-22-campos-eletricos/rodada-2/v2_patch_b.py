"""v2, parte B: Degraus 3, 4 (método reescrito) e 5."""
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


# ================= Degrau 3 =================
rep('Então o triângulo que você desenha com as distâncias (3, 4, 5) é semelhante ao triângulo das componentes:</p>',
    'Então o triângulo que você desenha com as distâncias (3, 4, 5) é <b>semelhante</b> ao triângulo das componentes (mesmos ângulos, lados proporcionais):</p>')
rep('<p>com os sinais tirados do desenho. Nada de procurar "o ângulo certo" para o cosseno.</p>',
    '<p>em que Δx = x<sub>P</sub> − x<sub>carga</sub> e Δy = y<sub>P</sub> − y<sub>carga</sub> (posição de P menos posição da carga) e r é a distância entre elas. Para carga positiva, os sinais de Δx e Δy já dão o sentido; para carga negativa, inverta os dois. Nada de procurar "o ângulo certo" para o cosseno.</p>\n'
    '      <details><summary>Ver a mesma regra em forma vetorial</summary><p>\\(\\vec E = \\dfrac{kq}{r^2}\\,\\hat r\\), com q <b>com sinal</b> e \\(\\hat r = (\\Delta x, \\Delta y)/r\\) o vetor de comprimento 1 que vai da carga até P. Com q negativa, o vetor inverte sozinho. Os Caps. 23 e 24 usam muito esta forma.</p></details>')
rep('<li><b>mesmo sinal</b> → o campo total fica <b>sobre a reta de simetria</b> (a mediatriz);</li>',
    '<li><b>mesmo sinal</b> → o campo total fica <b>sobre a reta de simetria</b> (a <b>mediatriz</b>: a reta perpendicular ao segmento entre as cargas, passando pelo meio dele);</li>')
rep('<div class="formula">\\[E = \\sqrt{E_x^2 + E_y^2},\\qquad \\theta = \\text{ângulo com o semieixo }+x\\text{, pelo quadrante de }(E_x, E_y)\\]</div>',
    '<div class="formula">\\[E = \\sqrt{E_x^2 + E_y^2}\\]</div>\n  <p>A <b>orientação</b> é o ângulo com o semieixo +x, achado pelo quadrante de (E<sub>x</sub>, E<sub>y</sub>), como abaixo.</p>')
rep('<p><b>O ângulo pede desenho.</b> A calculadora devolve \\(\\arctan(E_y/E_x)\\) só entre −90° e +90°.',
    '<p><b>O ângulo pede desenho.</b> A tecla tan⁻¹ (arctan) da calculadora devolve \\(\\arctan(E_y/E_x)\\) só entre −90° e +90°.')
rep('<p>Faça em três passos: ângulo de referência \\(\\arctan(|E_y|/|E_x|)\\); quadrante pelo desenho; ajuste. No 2º quadrante, 180° − ref; no 3º, 180° + ref (ou −180° + ref); no 4º, −ref.</p>',
    '<p>Faça em três passos: (1) ângulo de referência, ref = \\(\\arctan(|E_y|/|E_x|)\\), sempre entre 0° e 90°; (2) quadrante pelo desenho; (3) ajuste pela tabela:</p>\n'
    '      <table class="ficha"><tr><th>2º quadrante (x &lt; 0, y &gt; 0)</th><th>1º quadrante (x &gt; 0, y &gt; 0)</th></tr><tr><td>180° − ref</td><td>ref</td></tr>'
    '<tr><th>3º quadrante (x &lt; 0, y &lt; 0)</th><th>4º quadrante (x &gt; 0, y &lt; 0)</th></tr><tr><td>180° + ref (= −180° + ref)</td><td>−ref (= 360° − ref)</td></tr></table>')
rep('<text x="168" y="70" class="t-r t-s">θ = 233°</text>', '<text x="168" y="70" class="t-r t-s">233°</text>')
rep('<text x="66" y="112" class="t-s">53°</text>', '<text x="88" y="122" class="t-s">53°</text>')
# previsão nova do W3 (P desce até a origem)
rep('<p class="enun"><b>Antes de mexer:</b> duas cargas <b>positivas</b> iguais em x = −3 e x = +3, e P no eixo y, acima delas. Para onde aponta o campo total em P?</p>\n    <div class="alts">\n      <button class="alt" type="button" data-fb="Cada campo tem componente x, mas elas se cancelam (uma para a direita, outra para a esquerda).">para +x</button>\n      <button class="alt" type="button" data-fb="45° só sairia se as componentes x e y fossem iguais. Aqui as x se cancelam.">a 45°</button>\n      <button class="alt" type="button" data-ok="1" data-fb="Isso: mesmo sinal → o campo fica sobre a mediatriz, para longe das cargas (+y). Agora troque o sinal de uma delas no widget.">para +y</button>\n      <button class="alt" type="button" data-fb="Os campos não são opostos: os dois têm componente y para cima.">o campo é zero</button>',
    '<p class="enun"><b>Antes de mexer:</b> duas cargas <b>positivas</b> iguais estão em x = −3 cm e x = +3 cm, e P está no eixo y. Se P <b>descer</b> pelo eixo y até a origem, o campo total em P…</p>\n    <div class="alts">\n      <button class="alt" type="button" data-fb="P fica mais perto das cargas, sim, mas os dois campos ficam cada vez mais horizontais e opostos.">aumenta sem parar</button>\n      <button class="alt" type="button" data-ok="1" data-fb="Isso: na origem os dois campos são horizontais, iguais e opostos. A componente que sobrava (a y) some. No caminho, ele passa por um máximo (perto de y = 2 cm): procure no widget.">vai a zero</button>\n      <button class="alt" type="button" data-fb="A distância e as direções mudam; o campo também.">fica igual</button>\n      <button class="alt" type="button" data-fb="Com as duas positivas e P acima delas, as componentes y apontam para cima o caminho todo.">passa a apontar para −y</button>')
rep('<label>Altura de P (y, em cm): <input type="range" id="w3-y" min="1" max="6" step="0.5" value="4"></label>',
    '<label>Altura de P (y, em cm): <input type="range" id="w3-y" min="0" max="6" step="0.5" value="4"></label>')
rep('aria-label="Duas cargas no eixo x em −3 e +3; a da esquerda pode ser positiva ou negativa. O ponto P sobe pelo eixo y. Em P, setas dos dois campos, as componentes tracejadas e a seta roxa do campo total.">',
    'aria-label="Duas cargas no eixo x em −3 e +3 cm; a da esquerda pode ser positiva ou negativa. O ponto P sobe pelo eixo y. Em P, setas dos dois campos, a seta roxa do campo total e suas componentes tracejadas.">\n        <line id="w3-cx" class="fino" x1="180" y1="110" x2="180" y2="110" style="stroke:var(--res)"/><line id="w3-cy" class="fino" x1="180" y1="110" x2="180" y2="110" style="stroke:var(--res)"/>\n        <text id="w3-ta" x="44" y="296" class="t-s t-p">+q</text><text x="290" y="296" class="t-s t-p">+q</text><text x="56" y="262" class="t-2">−3</text><text x="292" y="262" class="t-2">+3</text>')
rep('<details class="porque-passo"><summary>Por que 4/5 e não 3/5?</summary><p>A componente y corresponde ao lado vertical do triângulo, que mede 4,0 cm, dividido pela hipotenusa (5,0 cm).',
    '<details class="porque-passo"><summary>Por que 4/5 e não 3/5?</summary><p>A componente y corresponde ao lado vertical do triângulo, que mede 4,0 cm, dividido pela hipotenusa (o lado maior, oposto ao ângulo reto: 5,0 cm).')
rep('N/C; \\(E = 2(7{,}19\\times10^3)(0{,}80) = 1{,}15\\times10^4\\) N/C, a 90° (para +y).</p>',
    'N/C; \\(E = 2(7{,}19\\times10^3)(0{,}80) = 1{,}15\\times10^4\\) N/C, a 90° do semieixo +x (para +y).</p>')
rep('Faz sentido com o resultado, que tem o fator 4/5 → 0. Unidade: N/C.</p>',
    'Faz sentido com o resultado: o fator 4/5 é y/r, e y/r → 0 quando y → 0. Unidade: N/C.</p>')
rep('<text x="40" y="180" class="t-s">|q| = 12 nC</text><text x="250" y="180" class="t-s">|q| = 12 nC</text>',
    '<text x="10" y="210" class="t-s">|q| = 12 nC</text><text x="262" y="210" class="t-s">|q| = 12 nC</text>')
rep('<text x="100" y="105" class="t-2">2,0 m</text><text x="240" y="105" class="t-2">2,0 m</text><text x="160" y="212" class="t-2">2,0 m</text>',
    '<text x="86" y="105" class="t-2">2,0 m</text><text x="236" y="105" class="t-2">2,0 m</text><text x="160" y="190" class="t-2">2,0 m</text>')
rep('data-mostra="27 N/C (gabarito do livro: 27 N/C) — agora sobram as componentes paralelas à base: 2E sen 30°" data-erros=\'[[46.71,',
    'data-mostra="27 N/C (gabarito do livro: 27 N/C) — agora sobram as componentes paralelas à base: 2E sen 30°" data-erros=\'[[0,"Sinais opostos não cancelam tudo: cancelam a componente ao longo do eixo de simetria e somam a paralela à base."],[46.71,')
rep('<b>Na verdade</b> r é a distância em linha reta da carga até P: Pitágoras. No centro de um quadrado de lado a, r = a/√2.</li>',
    '<b>Na verdade</b> r é a distância em linha reta da carga até P: use Pitágoras.</li>')
rep('<svg viewBox="0 0 300 130" role="img" aria-label="Pergunta 3 do livro: duas cargas −q no eixo x, à mesma distância d da origem, uma de cada lado. O ponto P está no eixo y, acima da origem.">',
    '<svg viewBox="0 0 300 130" role="img" aria-label="Pergunta 3 do livro: duas cargas −q no eixo x, à mesma distância d da origem, uma de cada lado. O ponto P está no eixo y, acima da origem.">\n        <text x="282" y="94" class="t-2">x</text><text x="156" y="16" class="t-2">y</text>')

# ================= Degrau 4: método reescrito =================
rep('Se só <b>metade</b> da mesa tem gente, os empurrões "de lado" se anulam aos pares e sobra um empurrão para o lado vazio.</p>',
    'Se só <b>metade</b> da mesa tem gente, os empurrões "de lado" se anulam aos pares e sobra um empurrão para o lado vazio.</p>')
rep('E cargas negativas <b>puxam</b> em vez de empurrar.</div>',
    'E cargas negativas <b>puxam</b> em vez de empurrar: se metade da mesa empurra e a outra metade puxa, os efeitos podem se <b>somar</b> em vez de se cancelar (veja "sinais opostos", abaixo). E "mesa cheia dá zero" vale só no centro exato; fora dele, não.</div>')
ini = s.index('  <p>Antes, uma grandeza nova.')
fim = s.index('  <h3>Ficha das grandezas novas</h3>', ini)
NOVO_D4 = r'''  <div class="ferramentas">
    <h3>Ferramentas de Cálculo deste degrau</h3>
    <p class="pequeno">Leia uma vez antes de seguir: o resto do degrau usa as quatro.</p>
    <dl>
      <dt>Radiano</dt>
      <dd>É o ângulo em que o arco tem o mesmo comprimento do raio. Uma volta (360°) mede 2π rad, então 180° = π rad, 90° = π/2 rad e 120° = 2π/3 rad. Por isso o comprimento de um arco é \(s = r\varphi\) com φ <b>em radianos</b> (com graus, a fórmula dá errado).</dd>
      <dt>O "d" na frente de uma letra</dt>
      <dd>Quer dizer "um pedacinho muito pequeno de". ds é um pedacinho de comprimento do arco, dq é a carga desse pedacinho, dθ é o ângulo que ele ocupa visto do centro. A regra \(s = r\varphi\) vale para um pedaço: \(ds = r\,d\theta\).</dd>
      <dt>Integral</dt>
      <dd>É a soma de infinitos pedacinhos. \(\int_a^b f(\theta)\,d\theta\) soma f(θ)·dθ de θ = a até θ = b. Para calcular: ache uma função cuja derivada é f (a <b>primitiva</b>) e faça "valor em b menos valor em a".</dd>
      <dt>A integral deste degrau</dt>
      <dd>A derivada de sen θ é cos θ, então a primitiva de cos θ é sen θ: \(\int_{-\alpha}^{\alpha}\cos\theta\,d\theta = \sin\alpha - \sin(-\alpha) = 2\sin\alpha\). Na calculadora, use o modo da unidade que você digitou: sen 60° = sen(π/3 rad) = 0,866, mas sen(60 rad) é outro número.</dd>
    </dl>
  </div>

  <p>Grandeza nova: num objeto fino, a carga vem por unidade de comprimento. É a <b>densidade linear de carga</b>:</p>
  <div class="formula">\[\lambda = \frac{Q}{L}\quad(\text{C/m})\]
  \[\text{num arco: } L = r\,\varphi\quad(\varphi\text{ em rad})\]</div>
  <p>Um pedacinho de comprimento ds tem carga \(dq = \lambda\,ds = \lambda\,r\,d\theta\).</p>

  <figure class="fig larga">
    <svg viewBox="0 0 380 290" role="img" aria-label="Arco carregado positivamente à esquerda do ponto P, simétrico em relação ao eixo horizontal, com abertura phi (metade para cada lado). Um pedacinho dq acima do eixo, a um ângulo theta, e o pedacinho simétrico dq linha abaixo. Em P, cada pedacinho cria um campo ao longo da reta que o liga a P, apontando para longe dele: o de dq aponta para baixo e para a direita, o de dq linha para cima e para a direita. As componentes verticais se cancelam; as horizontais, dE cos theta cada, se somam.">
      <line class="fino" x1="20" y1="140" x2="370" y2="140"/>
      <path d="M 209.3 31.2 A 120 120 0 0 0 209.3 248.8" class="barra-p" style="stroke-width:5;opacity:.55"/>
      <line class="fino" x1="260" y1="140" x2="209.3" y2="31.2" style="opacity:.6"/><line class="fino" x1="260" y1="140" x2="209.3" y2="248.8" style="opacity:.6"/>
      <text x="236" y="40" class="t-2">φ/2</text><text x="236" y="250" class="t-2">φ/2</text>
      <line class="fino" x1="168.1" y1="62.9" x2="313.6" y2="185"/><line class="fino" x1="168.1" y1="217.1" x2="313.6" y2="95"/>
      <circle cx="168.1" cy="62.9" r="6" class="qp"/><circle cx="168.1" cy="217.1" r="6" class="qp"/>
      <text x="120" y="58" class="t-p t-s">dq</text><text x="120" y="232" class="t-p t-s">dq′</text>
      <text x="200" y="90" class="t-2">r</text>
      <path d="M 235 140 A 25 25 0 0 1 240.85 123.9" class="fino" style="stroke-dasharray:none"/><text x="220" y="133" class="t-s">θ</text>
      <use href="#pt" x="260" y="140"/><text x="252" y="164">P</text>
      <line class="ve" x1="260" y1="140" x2="313.6" y2="185"/><text x="262" y="205" class="t-e t-s">dE (de dq)</text>
      <line class="ve" x1="260" y1="140" x2="313.6" y2="95"/><text x="262" y="84" class="t-e t-s">dE′ (de dq′)</text>
      <line class="fino" x1="313.6" y1="140" x2="313.6" y2="185" style="stroke:var(--campo)"/><line class="fino" x1="313.6" y1="140" x2="313.6" y2="95" style="stroke:var(--campo)"/>
      <text x="322" y="120" class="t-2">se</text><text x="322" y="134" class="t-2">cancelam</text>
      <line class="vr" x1="260" y1="140" x2="365" y2="140" style="stroke-width:2.2"/>
      <text x="300" y="276" class="t-r t-s">somam: dE cos θ</text><text x="300" y="262" class="t-2">horizontais</text>
    </svg>
    <figcaption>Figura 4-1. Cada pedacinho cria em P um campo ao longo da reta pedacinho–P (tracejada), para longe dele: por isso a seta de baixo vem de dq, o de cima. As componentes verticais se cancelam aos pares; as horizontais, dE cos θ cada, se somam.</figcaption>
  </figure>

  <h3>O método do elemento, em seis passos</h3>
  <p>Acompanhe na Figura 4-1.</p>
  <ol>
    <li><b>Desenhe um pedacinho</b> ds no ângulo θ, medido a partir do eixo de simetria (a reta que passa por P e pelo meio do arco), e o pedacinho simétrico, no ângulo −θ.</li>
    <li><b>Carga do pedacinho:</b> \(dq = \lambda\,ds = \lambda\,r\,d\theta\). Use |λ|; o sinal entra no desenho (passo 6).</li>
    <li><b>Campo do pedacinho:</b> ele é tão pequeno que vale a Eq. 22-3: \(dE = k\dfrac{dq}{r^2} = \dfrac{k\lambda}{r}\,d\theta\). É igual para todos os pedacinhos, porque todos estão a uma distância r de P.</li>
    <li><b>Separe cada dE em duas partes.</b> Ao longo do eixo: \(dE\cos\theta\) (pela trigonometria do triângulo da figura, cos θ é a fração de dE que aponta ao longo do eixo). Perpendicular ao eixo: \(dE\sin\theta\). O pedacinho simétrico tem a mesma parte ao longo do eixo e a parte perpendicular oposta, que se cancela. Sobra somar \(dE\cos\theta\).</li>
    <li><b>Some todos os pedacinhos</b> com uma integral, de uma ponta à outra: θ de −φ/2 a +φ/2.</li>
    <li><b>Sentido pelo desenho:</b> para longe do arco se a carga é positiva, para o arco se é negativa. Se pedirem em termos de Q, troque \(\lambda = Q/(r\varphi)\).</li>
  </ol>
  <div class="formula">\[\begin{aligned}E &= \frac{k\lambda}{r}\int_{-\varphi/2}^{\varphi/2}\cos\theta\,d\theta\\ &= \frac{2k\lambda}{r}\,\sin\frac{\varphi}{2}\\ &= \frac{kQ}{r^2}\cdot\frac{\sin(\varphi/2)}{\varphi/2}\end{aligned}\]<span class="eq-n">centro de um arco uniforme</span></div>
  <p>O caso do P29: <b>semicircunferência</b> (φ = π rad): sen(π/2) = 1, então \(E = \dfrac{2k\lambda}{r} = \dfrac{2kQ}{\pi r^2}\). E um anel completo? Descubra no widget, mais abaixo.</p>
  <details>
    <summary>Ver de onde vem a última forma</summary>
    <p>Com \(\lambda = Q/(r\varphi)\): \(\dfrac{2k\lambda}{r}\sin\dfrac{\varphi}{2} = \dfrac{2kQ}{r^2\varphi}\sin\dfrac{\varphi}{2} = \dfrac{kQ}{r^2}\cdot\dfrac{\sin(\varphi/2)}{\varphi/2}\). O primeiro fator é o campo da carga toda num ponto a uma distância r; o segundo é sempre menor que 1. Esse "desconto" é o quanto os empurrões laterais se desperdiçam.</p>
  </details>

  <h3>E se as metades tiverem sinais opostos?</h3>
  <div class="lado">
    <figure class="fig">
      <svg viewBox="0 0 400 240" role="img" aria-label="Semicircunferência à esquerda de P: o quarto de cima positivo, o quarto de baixo negativo. Um pedacinho positivo em cima empurra P para baixo e para a direita; o pedacinho negativo simétrico puxa P para baixo e para a esquerda. As componentes horizontais se cancelam; as verticais se somam para baixo.">
        <line class="fino" x1="20" y1="120" x2="310" y2="120"/>
        <path d="M 220 20 A 100 100 0 0 0 120 120" class="barra-p" style="stroke-width:5;opacity:.6"/>
        <path d="M 120 120 A 100 100 0 0 0 220 220" class="barra-n" style="stroke-width:5;opacity:.6"/>
        <circle cx="143.4" cy="55.7" r="6" class="qp"/><circle cx="143.4" cy="184.3" r="6" class="qn"/>
        <text x="130" y="30" class="t-p">+</text><text x="130" y="218" class="t-n">−</text>
        <use href="#pt" x="220" y="120"/><text x="226" y="112">P</text>
        <line class="ve" x1="220" y1="120" x2="266" y2="158.6"/><line class="ve" x1="220" y1="120" x2="174" y2="158.6"/>
        <line class="fino" x1="174" y1="158.6" x2="266" y2="158.6" style="stroke:var(--campo)"/>
        <line class="vr" x1="220" y1="120" x2="220" y2="196" style="stroke-width:2.4"/>
        <text x="270" y="176" class="t-2">horizontais:</text><text x="270" y="190" class="t-2">se cancelam</text>
        <text x="226" y="214" class="t-r t-s">verticais somam</text>
      </svg>
      <figcaption>Figura 4-2. Cada metade é um quarto de circunferência: + em cima, − embaixo. Agora quem se cancela é a componente horizontal.</figcaption>
    </figure>
    <div>
      <p>O pedaço + de cima <b>empurra</b> P para baixo e para a direita. O pedaço − simétrico <b>puxa</b> P para baixo e para a esquerda. Agora são as componentes <b>horizontais</b> que se cancelam, e as verticais se somam.</p>
      <p>A conta muda em dois pontos. (1) A parte que sobra é a perpendicular ao eixo, \(dE\sin\theta\). (2) As duas metades empurram para o <b>mesmo</b> lado, então <b>integre só a metade de cima, de 0 a φ/2, e dobre</b>:</p>
    </div>
  </div>
  <div class="formula">\[E = 2\cdot\frac{k\lambda}{r}\int_0^{\varphi/2}\sin\theta\,d\theta = \frac{2k\lambda}{r}\left(1 - \cos\frac{\varphi}{2}\right)\]</div>
  <p class="pequeno">Cuidado: de −φ/2 a +φ/2, ∫sen θ dθ dá zero (o seno é ímpar). Isso valeria para duas metades de <b>mesmo</b> sinal, em que essa parte de fato se cancela. Regra geral: antes de integrar, desenhe o par simétrico com os sinais certos e veja o que some.</p>

'''
s = s[:ini] + NOVO_D4 + s[fim:]
rep('<text x="104" y="76" class="t-2">r</text><text x="110" y="104" class="t-2">120°</text>',
    '<text x="104" y="76" class="t-2">r</text><path d="M 115 146 A 30 30 0 0 0 115 94" class="fino" style="stroke-dasharray:none;stroke:var(--res)"/><text x="122" y="100" class="t-2">60°</text><text x="122" y="152" class="t-2">60°</text><text x="12" y="226" class="t-r t-s">φ = 120° (60° para cada lado)</text>')
rep('O arco tem 120° no total, metade para cada lado: de −60° a +60°. Para avaliar o seno, tanto faz graus ou radianos; o que exige radianos é o comprimento do arco, \\(s = r\\varphi\\).</p>',
    'O arco tem 120° no total, metade para cada lado: de −60° a +60°. Para o seno, 60° e π/3 rad são o mesmo ângulo (sen = 0,866), desde que a calculadora esteja no modo certo; o que exige radianos é o comprimento do arco, \\(s = r\\varphi\\).</p>')
rep('data-erros=\'[[0.66,"Calculadora em graus? sen(1) aqui é sen(1 rad) = 0,841."],',
    'data-erros=\'[[0.7845,"Calculadora em graus? Aqui o ângulo é 1 rad: sen(1 rad) = 0,841, não sen(1°)."],')
rep('<b>Na verdade</b> o arco dá menos, pelo fator \\(\\sin(\\varphi/2)/(\\varphi/2)\\), <b>porque</b> parte de cada empurrão é lateral e se cancela.</li>',
    '<b>Na verdade</b> o arco dá menos, pelo fator \\(\\sin(\\varphi/2)/(\\varphi/2)\\), <b>porque</b> parte de cada empurrão é lateral e se cancela.</li>')

# ================= Degrau 5 =================
rep('Campos elétricos não se bloqueiam: cada pedaço contribui como se estivesse sozinho (superposição).</div>',
    'Campos elétricos não se bloqueiam: cada pedaço contribui como se estivesse sozinho (superposição). No Cap. 23 você vai ver uma chapa de metal "bloquear" um campo; não é exceção: as cargas livres do metal se movem e criam um campo contrário, que se soma.</div>')
rep('<line class="cota" x1="40" y1="95" x2="240" y2="95"/><text x="136" y="112" class="t-2">L</text>\n        <line class="cota" x1="240" y1="95" x2="340" y2="95"/><text x="286" y="112" class="t-2">a</text>\n        <line class="cota" x1="126" y1="128" x2="340" y2="128"/><text x="226" y="124" class="t-2">x</text>',
    '<line class="cota" x1="40" y1="95" x2="237" y2="95"/><text x="136" y="112" class="t-2">L</text>\n        <line class="cota" x1="243" y1="95" x2="340" y2="95"/><text x="286" y="112" class="t-2">a</text>\n        <line class="cota" x1="126" y1="132" x2="340" y2="132"/><text x="226" y="128" class="t-2">x</text>\n        <line class="fino" x1="140" y1="52" x2="140" y2="68" style="stroke-dasharray:none"/><line class="fino" x1="140" y1="20" x2="340" y2="20"/><text x="200" y="15" class="t-2">D (até o centro)</text>')
rep('<svg viewBox="0 0 400 140" role="img" aria-label="Barra horizontal carregada, de comprimento L, à esquerda do ponto P, no mesmo eixo. Um pedacinho dx está a uma distância x de P. A ponta mais próxima da barra está a uma distância a de P.">',
    '<svg viewBox="0 0 400 145" role="img" aria-label="Barra horizontal carregada, de comprimento L, à esquerda do ponto P, no mesmo eixo. Um pedacinho dx está a uma distância x de P. A ponta mais próxima da barra está a uma distância a de P. Um tracejado acima marca D, a distância de P até o centro da barra.">')
rep('<div class="formula">\\[E = k\\lambda\\int_a^{a+L}\\frac{dx}{x^2} = k\\lambda\\left(\\frac1a - \\frac1{a+L}\\right) = \\frac{k\\lambda L}{a(a+L)} = \\frac{k\\,|q|}{a\\,(a+L)}\\]<span class="eq-n">P no prolongamento da barra</span></div>',
    '<div class="formula">\\[\\begin{aligned}E &= k\\lambda\\int_a^{a+L}\\frac{dx}{x^2} = k\\lambda\\left[-\\frac1x\\right]_a^{a+L}\\\\ &= k\\lambda\\left(\\frac1a - \\frac1{a+L}\\right)\\\\ &= \\frac{k\\lambda L}{a(a+L)} = \\frac{k\\,|q|}{a\\,(a+L)}\\end{aligned}\\]<span class="eq-n">P no prolongamento da barra</span></div>\n  <p class="pequeno">A primitiva de 1/x² = x⁻² é −1/x (Degrau 0, item 5). "Valor em cima menos valor embaixo": \\(-\\tfrac{1}{a+L} + \\tfrac1a\\). E λL é a carga da barra.</p>')
rep('A "distância equivalente" \\(\\sqrt{a(a+L)}\\) fica entre a ponta perto e a ponta longe (é a média geométrica das duas).</p>',
    'A "distância equivalente" \\(\\sqrt{a(a+L)}\\) fica entre a ponta perto e a ponta longe (é a <b>média geométrica</b> das duas: a raiz do produto).</p>')
rep('<div class="formula">\\[E = \\frac{kq}{(D - L/2)(D + L/2)} = \\frac{kq}{D^2 - L^2/4}\\ \\xrightarrow{\\ D\\,\\gg\\,L\\ }\\ \\frac{kq}{D^2}\\]</div>\n  <p>Quando D é muito maior que L, o termo L²/4 fica desprezível e sobra a carga pontual. Isso vale para qualquer objeto carregado: visto de longe, ele parece um ponto.</p>',
    '<div class="formula">\\[\\begin{aligned}E &= \\frac{kq}{(D - L/2)(D + L/2)}\\\\ &= \\frac{kq}{D^2 - L^2/4}\\end{aligned}\\]</div>\n'
    '  <p>Quando D ≫ L (lê-se "D muito maior que L"), o termo L²/4 fica desprezível e sobra \\(kq/D^2\\): a carga pontual. O <b>erro</b> de trocar a barra por um ponto, isto é, a diferença dividida pelo valor certo, é exatamente \\((L/2D)^2\\).</p>\n'
    '  <p>Isso vale para qualquer objeto com carga total diferente de zero, se D for medido a partir do centro: visto de longe, ele parece um ponto. O tamanho do erro depende da forma (para o disco do Degrau 6 é 0,75(R/z)²). Com carga total zero, como num dipolo, o campo de longe cai mais depressa que 1/D².</p>')
rep('<button class="alt" type="button" data-fb="Com D = L, o erro ainda é de 33 %: o ponto P fica a só meio comprimento da ponta.">D = L</button>',
    '<button class="alt" type="button" data-fb="Com D = L, o erro ainda é de 25 %: o ponto P fica a só meio comprimento da ponta.">D = L</button>')
rep('<button class="alt" type="button" data-fb="Com D = 2L, o erro é de uns 7 %.">D = 2L</button>',
    '<button class="alt" type="button" data-fb="Com D = 2L, o erro é de uns 6 %: (1/4)².">D = 2L</button>')
rep('data-fb="Isso: a razão é 1/(1 − (L/2D)²); com D = 5L, (1/10)² = 0,01 → erro de 1 %. Confira no widget.">D = 5L</button>',
    'data-fb="Isso: o erro é (L/2D)²; com D = 5L, (1/10)² = 0,01, ou 1 %. Confira no widget.">D = 5L</button>')
rep('<h4>W5 — Barra × carga pontual</h4>', '<h4>W5 — Erro de trocar a barra por um ponto</h4>')
rep('<svg viewBox="0 0 360 230" role="img" aria-label="Gráfico da razão entre o campo da barra e o campo de uma carga pontual no centro dela, em função de D sobre L, de 0,6 a 10. A curva começa alta e cai até quase 1. Um marcador móvel mostra o valor escolhido.">\n        <line class="eixo-s" x1="40" y1="200" x2="350" y2="200"/><line class="eixo-s" x1="40" y1="200" x2="40" y2="10"/>\n        <g id="w5-grade"></g>\n        <path id="w5-curva" class="curva" d=""/>\n        <line id="w5-um" class="curva-2" x1="40" y1="0" x2="350" y2="0"/>\n        <circle id="w5-m" r="6" cx="0" cy="0" style="fill:var(--res)"/>\n        <text x="300" y="222" class="t-2">D/L</text><text x="46" y="20" class="t-2">E(barra) / E(ponto)</text>',
    '<svg viewBox="0 0 360 230" role="img" aria-label="Gráfico do erro, em porcentagem e em escala logarítmica, de trocar a barra por uma carga pontual no centro, em função de D sobre L, de 0,6 a 10. A faixa de erro menor que 1 % está sombreada. A curva começa perto de 70 % e entra na faixa de 1 % em D igual a 5L. Um marcador móvel mostra o valor escolhido.">\n        <rect id="w5-faixa" x="40" y="0" width="310" height="0" class="area"/>\n        <line class="eixo-s" x1="40" y1="200" x2="350" y2="200"/><line class="eixo-s" x1="40" y1="200" x2="40" y2="10"/>\n        <g id="w5-grade"></g>\n        <path id="w5-curva" class="curva" d=""/>\n        <line id="w5-um" class="curva-2" x1="40" y1="0" x2="350" y2="0"/>\n        <circle id="w5-m" r="6" cx="0" cy="0" style="fill:var(--res)"/>\n        <text x="300" y="222" class="t-2">D/L</text><text x="46" y="20" class="t-2">erro (%), escala log</text><text id="w5-tf" x="250" y="0" class="t-2">erro &lt; 1 %</text>')
rep('data-erros=\'[[20.23,"Faltou o L no numerador? Com λ (e não q) a fórmula é kλL/(a(a+L))."],[15.17,"Você usou 4,0 m como a. A ponta perto está a 1,0 m de P."]]\'',
    'data-erros=\'[[20.23,"Faltou o L no numerador? Com λ (e não q) a fórmula é kλL/(a(a+L))."],[8.669,"Você usou 4,0 m como a. A ponta perto está a 1,0 m de P."],[15.17,"Você pôs a carga toda na ponta longe (x = 0). Os pedaços de perto pesam mais: use a fórmula da barra."]]\'')

open(ARQ, 'w', encoding='utf-8').write(s)
print('erros:' if erros else 'ok, sem erros')
for e in erros:
    print(' ', e)
sys.exit(1 if erros else 0)
