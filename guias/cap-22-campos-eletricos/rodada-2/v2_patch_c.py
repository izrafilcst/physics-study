"""v2, parte C: Degrau 6, visão geral, questões, síntese, Dúvidas da turma e JavaScript."""
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


def troca_trecho(ini_txt, fim_txt, novo, inclui_fim=False):
    """Troca de ini_txt (inclusive) até fim_txt (exclusive, ou inclusive)."""
    global s
    try:
        i = s.index(ini_txt)
        j = s.index(fim_txt, i)
    except ValueError:
        erros.append(f'[trecho não achado] {ini_txt[:60]!r}')
        return
    if inclui_fim:
        j += len(fim_txt)
    s = s[:i] + novo + s[j:]


# ================= Degrau 6 =================
rep('Um disco carregado é isso: uma pilha de <b>anéis</b> concêntricos, do centro até a borda.',
    'Um disco carregado é isso: um conjunto de <b>anéis</b> concêntricos, encaixados uns nos outros no mesmo plano, do centro até a borda.')
rep('e andar um passo para cima não muda nada. Perto do disco, o campo quase não muda com z.</p>',
    'e andar um passo para cima muda muito pouco. Perto do disco, o campo quase não muda com z (até z = 0,1R, cai menos de 10 %).</p>')
rep('<p>Grandeza nova: a <b>densidade superficial de carga</b>, \\(\\sigma = Q/A\\) (C/m²). Num disco, \\(A = \\pi R^2\\).</p>',
    '<p>Grandeza nova: a <b>densidade superficial de carga</b>, \\(\\sigma = Q/A\\) (C/m²). Num disco, \\(A = \\pi R^2\\). Numa folha fina, conte a carga toda (das duas faces juntas).</p>')
rep('<line class="ve" x1="160" y1="60" x2="138.7" y2="20.4"/>',
    '<line class="ve" x1="160" y1="60" x2="138.7" y2="20.4"/><line class="vr" x1="160" y1="60" x2="160" y2="12" style="stroke-width:2.4"/><text x="166" y="46" class="t-r t-s">E</text>')
rep('(A integral sai com a substituição \\(u = z^2 + r^2\\), \\(du = 2r\\,dr\\).)</p>',
    '(A integral sai com a substituição \\(u = z^2 + r^2\\): \\(du = 2r\\,dr\\), então \\(\\displaystyle\\int\\frac{r\\,dr}{(z^2+r^2)^{3/2}} = \\frac12\\int u^{-3/2}\\,du = -u^{-1/2} = -\\frac{1}{\\sqrt{z^2+r^2}}\\).)</p>')
rep('<li><b>Logo acima do centro (z → 0):</b> o parêntese vale 1 e \\(E = \\dfrac{\\sigma}{2\\varepsilon_0}\\). É o <b>maior</b> valor no eixo; chame de \\(E_m\\). Repare: não depende de R.</li>',
    '<li><b>Logo acima do centro (z → 0⁺, isto é, z positivo e cada vez menor):</b> o parêntese vale 1 e \\(E = \\dfrac{\\sigma}{2\\varepsilon_0}\\). É o <b>maior</b> valor no eixo; chame de \\(E_m\\). Repare: não depende de R. Logo abaixo do disco, o campo tem o mesmo módulo e aponta para baixo: ao atravessar o disco, ele salta de +σ/(2ε₀) para −σ/(2ε₀). Esse salto, σ/ε₀, é a ponte para a lei de Gauss (Cap. 23).</li>')
rep('quando R/z é pequeno (binômio).', 'quando R/z é pequeno (aproximação binomial: \\((1+x)^n \\approx 1 + nx\\) para x pequeno).')
rep('<p class="enun"><b>Antes de mexer:</b> bem perto do disco (z = 0,1R), o campo do disco é quase igual ao de…</p>\n    <div class="alts">\n      <button class="alt" type="button" data-fb="A carga pontual daria um campo enorme ali (ela cresce com 1/z²). O disco espalha a carga.">uma carga pontual com a mesma carga</button>\n      <button class="alt" type="button" data-ok="1" data-fb="Isso: de perto, as bordas estão “longe” e o disco parece infinito. Com z = 0,1R, o disco dá 0,90 Eₘ.">uma placa infinita com o mesmo σ</button>\n      <button class="alt" type="button" data-fb="Zero é o campo no centro de um anel. Logo acima de um disco, o campo é o máximo.">zero</button>',
    '<p class="enun"><b>Antes de mexer:</b> a uma distância igual ao raio (z = R), o campo do disco vale aproximadamente…</p>\n    <div class="alts">\n      <button class="alt" type="button" data-fb="0,9 Eₘ é o valor bem mais perto, em z = 0,1R.">0,9 Eₘ</button>\n      <button class="alt" type="button" data-fb="Metade de Eₘ acontece antes, mais perto do disco. Em z = R já caiu mais.">0,5 Eₘ</button>\n      <button class="alt" type="button" data-ok="1" data-fb="Isso: 1 − 1/√2 = 0,29. Ainda longe de ser uma carga pontual, que daria 0,5 Eₘ (71 % a mais). Confira no widget e procure onde cada aproximação passa a servir.">0,3 Eₘ</button>\n      <button class="alt" type="button" data-fb="0,1 Eₘ só bem mais longe, perto de z = 2R.">0,1 Eₘ</button>')
rep('3 % acima. Bate com a previsão: de longe o disco parece um ponto, mas não exatamente.</p>',
    '3 % acima. Bate com a previsão: de longe o disco parece um ponto, mas não exatamente. Ordem de grandeza: σ = 5,3 µC/m² é 10 % do máximo que o ar aguenta junto ao disco (σ/(2ε₀) = 3 × 10⁶ N/C dá σ ≈ 5,3 × 10⁻⁵ C/m²).</p>')
rep('<b>Na verdade</b>, para um disco ou placa isolante com carga numa face, é \\(\\sigma/(2\\varepsilon_0)\\).',
    '<b>Na verdade</b>, para um disco ou placa isolante fina (σ = carga total por área), é \\(\\sigma/(2\\varepsilon_0)\\).')

# ================= Visão geral =================
rep('<p class="pequeno">Nenhuma das suas questões usa estes tópicos. Leia para saber que existem e onde estão no livro.</p>',
    '<p class="pequeno">Nenhuma questão deste guia pede as fórmulas destes tópicos (o P9 é um dipolo, mas se resolve somando dois campos, como no Degrau 3). Leia só para saber que existem e onde estão no livro; os produtos vetorial (×) e escalar (·) são de Física 1.</p>')

# ================= Questões =================
rep('Ímpares têm gabarito do livro; pares têm "resposta calculada pelo guia, sem gabarito oficial".</p>',
    'Ímpares têm gabarito do livro; pares (o livro não dá a resposta) têm "resposta calculada pelo guia, sem gabarito oficial".</p>\n  <p class="pequeno">"nível ·, ··, ···" é a dificuldade marcada no livro (fácil, médio, difícil). A conferência aceita 2 % de diferença em relação ao valor certo (5 % no P81, cujos dados têm 2 algarismos). Ângulos valem em qualquer forma equivalente (−90° = 270°; 180° = −180°).</p>')
rep('<li>enxofre: 2,07 g/cm³ (só para o P81b)</li>', '<li>enxofre: 2,07 g/cm³ (usada na resolução do P81b)</li>')
rep('data-unid="C" data-resp="-0.02933"', 'data-unid="C" data-resp="-0.02933" data-tol="0.05"')
rep('as duas metades da esfera se repeliriam com cerca de \\(k(q/2)^2/R^2 \\approx 10^9\\) N (a conta exata para uma casca dá 7 × 10⁸ N, o peso de 70 mil toneladas)',
    'as duas metades da esfera se repeliriam com uma força da ordem de 10⁹ N (estimativa grosseira: \\(k(q/2)^2/R^2 = 1{,}4\\times10^9\\) N; a conta exata, com a carga na superfície, dá 7 × 10⁸ N, o peso de 70 mil toneladas)')
rep('<p class="usa">Usa: campo de carga pontual, sentido pelo sinal, cancelamento de campos alinhados com P.</p>',
    '<p class="usa">Usa: campo de carga pontual, sentido pelo sinal, soma de campos alinhados com P.</p>')
rep('<p class="usa">Usa: Pitágoras, componentes com o triângulo 3-4-5, simetria com sinais opostos, ângulo pelo quadrante.</p>',
    '<p class="usa">Usa: Pitágoras, componentes, simetria, ângulo pelo quadrante.</p>')
rep('<p class="usa">Usa: distância até o centro de um quadrado, cancelamento de um par, campo de carga pontual, ângulo.</p>',
    '<p class="usa">Usa: distâncias até P, campo de carga pontual, soma de campos, ângulo.</p>')
rep('<p class="usa">Usa: λ de um semicírculo, campo no centro de um arco, carga pontual, resolver em símbolos.</p>',
    '<p class="usa">Usa: λ de uma semicircunferência, campo no centro de um arco, carga pontual, resolver em símbolos.</p>')
rep('<p class="usa">Usa: λ de um quarto de círculo, simetria com sinais opostos, integral no arco, orientação.</p>',
    '<p class="usa">Usa: λ de um quarto de circunferência, simetria, integral no arco, ângulo com +x.</p>')
rep('<use href="#qp" x="105.5" y="95.5"/><text x="70" y="88" class="t-p">q₁</text>', '<use href="#qp" x="105.5" y="95.5"/><text x="30" y="86" class="t-p">q₁ = +5e</text>')
rep('<use href="#qp" x="214.5" y="204.5"/><text x="232" y="214" class="t-p">q₂</text>', '<use href="#qp" x="214.5" y="204.5"/><text x="232" y="214" class="t-p">q₂ = +5e</text>')
rep('<use href="#qp" x="214.5" y="95.5"/><text x="228" y="110" class="t-p">q₃</text>', '<use href="#qp" x="214.5" y="95.5"/><text x="230" y="112" class="t-p">q₃ = +3e</text>')
rep('<use href="#qn" x="269" y="41"/><text x="284" y="56" class="t-n">q₄</text>', '<use href="#qn" x="269" y="41"/><text x="180" y="30" class="t-n">q₄ = −12e</text>')
rep('[288,"288 N/C é o campo de q₁ (ou q₂) sozinha. E o parceiro dela do outro lado?"]',
    '[288,"288 N/C é o campo de q₁ (ou q₂) sozinha. Some com sinais, reta por reta."]')
rep('[1.841e-10,"Você ficou com as componentes y, mas são elas que se cancelam (sinais opostos). Sobram as x: o fator é 3/5."]',
    '[1.841e-10,"Você ficou com as componentes y, mas são elas que se cancelam (sinais opostos). Sobram as x: Eₓ = E·Δx/r, com Δx/r = 3/5."]')
rep('data-rot="(b) orientação θ =" data-unid="°" data-resp="180"', 'data-rot="(b) ângulo com +x =" data-unid="°" data-resp="180"')
rep('data-rot="(b) direção θ (em relação a +x) =" data-unid="°" data-resp="45"', 'data-rot="(b) ângulo com +x =" data-unid="°" data-resp="45"')
rep('data-rot="(b) orientação θ =" data-unid="°" data-resp="-90"', 'data-rot="(b) ângulo com +x =" data-unid="°" data-resp="-90"')
rep('data-rot="(c) direção θ =" data-unid="°" data-resp="180"', 'data-rot="(c) ângulo com +x =" data-unid="°" data-resp="180"')
rep('<line class="fino" x1="80" y1="50" x2="230" y2="200"/>',
    '<line class="fino" x1="80" y1="50" x2="230" y2="200"/><polyline points="80,50 230,50 230,200" class="fino" style="opacity:.5"/>')
rep('<figcaption>Figura 22-42 (reconstruída a partir do PDF do livro). P é o centro do quadrado de lado a.</figcaption>',
    '<figcaption>Figura 22-42 (reconstruída a partir do PDF do livro). P é o ponto médio de 1–2, que é também o centro do quadrado de lado a (o 4º vértice, pontilhado, não está no livro).</figcaption>')
# desafio do P15 (não conta para o placar)
i = s.index('<div class="ajuda" data-q="P15">')
s = s[:i] + '''<div class="exemplo lacunas">
        <p><b>Desafio (não é do livro, não conta no placar): e se q₁ fosse +2e?</b> Faça depois de acertar o P15. O par q₁–q₂ deixa de se cancelar e o campo sai das diagonais: bom treino de componentes e quadrante.</p>
        <div class="num" id="P15-des-a" data-lacuna="1" data-rot="|E| =" data-unid="N/C" data-resp="178.9" data-mostra="179 N/C (Eₓ = 170 N/C, E_y = 56,6 N/C)" data-erros='[[160,"Esse é o campo de q₃ sozinha. Agora q₁ (2e) e q₂ (e) não se cancelam mais: sobra o campo de uma carga e."],[400,"Você somou os módulos. Some componentes: cada campo aponta ao longo de uma diagonal."]]'></div>
        <div class="num" id="P15-des-b" data-lacuna="1" data-ang="1" data-rot="ângulo com +x =" data-unid="°" data-resp="18.43" data-mostra="18,4° (1º quadrante: arctan(56,6/170))" data-erros='[[45,"45° seria se q₁ e q₂ ainda se cancelassem."]]'></div>
      </div>

      ''' + s[i:]
rep('<li>λ do semicírculo (comprimento πR).</li>', '<li>λ da semicircunferência (comprimento πR).</li>')
rep('o campo no centro de um arco uniforme, caso semicírculo.', 'o campo no centro de um arco uniforme, caso semicircunferência.')
rep('<b>E se…</b> o semicírculo estivesse à direita de P?', '<b>E se…</b> a semicircunferência estivesse à direita de P?')
# P31: nota sobre a letra a, figura em escala com o centro, dica 2 sem a armadilha
rep('(d) pela barra e (e) por uma partícula de carga −q = −4,23 fC colocada no lugar anteriormente ocupado pelo centro da barra.</p>',
    '(d) pela barra e (e) por uma partícula de carga −q = −4,23 fC colocada no lugar anteriormente ocupado pelo centro da barra.</p>\n      <p class="pequeno">Atenção: nos itens (d) e (e) o livro reusa a letra a para outra distância (50 m, medida do <b>centro</b> da barra). Neste guia ela se chama D.</p>')
troca_trecho('<svg viewBox="0 0 360 120" role="img" aria-label="Figura 22-54 reconstruída',
             '</svg>',
             '''<svg viewBox="0 0 360 130" role="img" aria-label="Figura 22-54 reconstruída, em escala: barra com carga −q no eixo x, de comprimento L = 8,15 cm, à esquerda; o ponto P fica à direita, no eixo x, a uma distância a = 12,0 cm da ponta direita da barra. Um traço marca o centro da barra.">
          <line class="eixo-s" x1="10" y1="60" x2="350" y2="60"/><text x="338" y="80" class="t-2">x</text>
          <line x1="30" y1="60" x2="130" y2="60" class="barra-n"/>
          <line class="fino" x1="80" y1="48" x2="80" y2="72" style="stroke-dasharray:none"/><text x="62" y="40" class="t-2">centro</text>
          <text x="66" y="24" class="t-n">−q</text>
          <use href="#pt" x="277" y="60"/><text x="273" y="45">P</text>
          <line class="cota" x1="30" y1="95" x2="128" y2="95"/><text x="76" y="114" class="t-2">L</text>
          <line class="cota" x1="132" y1="95" x2="277" y2="95"/><text x="200" y="114" class="t-2">a</text>
        </svg>''', inclui_fim=True)
rep('<figcaption>Figura 22-54 (reconstruída a partir do PDF do livro).</figcaption>',
    '<figcaption>Figura 22-54 (reconstruída a partir do PDF do livro; aqui em escala, a/L = 1,47; o livro não está em escala).</figcaption>')
rep('<li>(d) Mesma fórmula, mas agora a distância dada é até o <b>centro</b>: a ponta perto fica a D − L/2.</li>',
    '<li>(d) Atenção: a distância dada agora é até o <b>centro</b> da barra, não até a ponta.</li>')
rep('[1.472e-3,"Você usou a distância até o centro da barra. De perto (a ~ L), isso erra uns 7 %. Use kq/(a(a+L))."]',
    '[1.472e-3,"Você usou a distância até o centro da barra. De perto (a ~ L), isso erra uns 7 %. Some os pedacinhos de a até a + L (Degrau 5)."]')
# P38: gráfico separado do disco e em largura total
troca_trecho('<svg viewBox="0 0 470 230" role="img" aria-label="Figura 22-58 reconstruída.',
             '</svg>',
             '''<svg viewBox="0 0 130 225" style="max-width:7.5rem" role="img" aria-label="Figura 22-58a reconstruída: disco com o eixo z vertical passando pelo centro.">
          <g transform="translate(0,10)">
            <ellipse cx="60" cy="110" rx="50" ry="15" class="disco"/>
            <line class="eixo" x1="60" y1="190" x2="60" y2="20"/><text x="66" y="28" class="t-2">z</text>
            <text x="50" y="210" class="t-2">(a)</text>
          </g>
        </svg>
        <svg viewBox="0 0 345 232" role="img" aria-label="Figura 22-58b reconstruída: gráfico do módulo do campo no eixo em função de z, de 0 a z s igual a 8,0 cm, com o eixo horizontal dividido em quatro partes iguais. Linhas de grade horizontais em E m e em 0,5 E m. A curva começa em E m em z igual a zero e decresce; ela cruza a linha de 0,5 E m exatamente na segunda linha vertical da grade e termina, em z s, perto de um quarto de E m.">
          <g>
            <line class="grade-g" x1="120" y1="40" x2="120" y2="190"/><line class="grade-g" x1="190" y1="40" x2="190" y2="190"/><line class="grade-g" x1="260" y1="40" x2="260" y2="190"/><line class="grade-g" x1="330" y1="40" x2="330" y2="190"/>
            <line class="grade-g" x1="50" y1="40" x2="330" y2="40"/><line class="grade-g" x1="50" y1="115" x2="330" y2="115"/>
            <line class="eixo" x1="50" y1="190" x2="330" y2="190"/><line class="eixo" x1="50" y1="190" x2="50" y2="30"/>
            <line class="eixo" x1="120" y1="190" x2="120" y2="182"/><line class="eixo" x1="190" y1="190" x2="190" y2="182"/><line class="eixo" x1="260" y1="190" x2="260" y2="182"/><line class="eixo" x1="330" y1="190" x2="330" y2="182"/>
            <path class="curva" d="M 50.0 40.0 L 53.5 42.2 L 57.0 44.3 L 60.5 46.5 L 64.0 48.6 L 67.5 50.8 L 71.0 52.9 L 74.5 55.1 L 78.0 57.2 L 81.5 59.3 L 85.0 61.4 L 88.5 63.5 L 92.0 65.6 L 95.5 67.7 L 99.0 69.7 L 102.5 71.7 L 106.0 73.8 L 109.5 75.7 L 113.0 77.7 L 116.5 79.7 L 120.0 81.6 L 123.5 83.5 L 127.0 85.4 L 130.5 87.3 L 134.0 89.1 L 137.5 90.9 L 141.0 92.7 L 144.5 94.5 L 148.0 96.2 L 151.5 97.9 L 155.0 99.6 L 158.5 101.3 L 162.0 102.9 L 165.5 104.5 L 169.0 106.1 L 172.5 107.6 L 176.0 109.2 L 179.5 110.7 L 183.0 112.1 L 186.5 113.6 L 190.0 115.0 L 193.5 116.4 L 197.0 117.8 L 200.5 119.1 L 204.0 120.4 L 207.5 121.7 L 211.0 123.0 L 214.5 124.2 L 218.0 125.4 L 221.5 126.6 L 225.0 127.8 L 228.5 128.9 L 232.0 130.0 L 235.5 131.1 L 239.0 132.2 L 242.5 133.3 L 246.0 134.3 L 249.5 135.3 L 253.0 136.3 L 256.5 137.3 L 260.0 138.2 L 263.5 139.1 L 267.0 140.0 L 270.5 140.9 L 274.0 141.8 L 277.5 142.6 L 281.0 143.5 L 284.5 144.3 L 288.0 145.1 L 291.5 145.9 L 295.0 146.6 L 298.5 147.4 L 302.0 148.1 L 305.5 148.8 L 309.0 149.5 L 312.5 150.2 L 316.0 150.9 L 319.5 151.5 L 323.0 152.1 L 326.5 152.8 L 330.0 153.4"/>
            <text x="20" y="45" class="t-s">Eₘ</text><text x="2" y="120" class="t-s">0,5Eₘ</text><text x="40" y="208" class="t-s">0</text><text x="322" y="208" class="t-s">zₛ</text>
            <text x="160" y="226" class="t-2">z (cm)</text><text x="186" y="18" class="t-2">(b)</text>
          </g>
        </svg>''', inclui_fim=True)
rep('[[4,"4,0 cm é o z em que o campo cai à metade, não o raio. Use a fórmula do disco para achar R."]',
    '[[4,"Você leu um z no gráfico e parou aí. O raio sai da fórmula do disco usando esse ponto (Degrau 6)."]')
# figuras das questões sem grade de fundo
qi = s.index('id="questoes"')
qf = s.index('id="sintese"')
s = s[:qi] + s[qi:qf].replace('<figure class="fig">', '<figure class="fig sem-grade">') + s[qf:]

# ================= Síntese e revisão =================
rep('procure pares que se cancelam (lado + sinal, e |q| ∝ r²).', 'procure pares que se cancelam (regra de bolso do Degrau 2: lado e sinal, e |q|/r² igual).')
rep('<p class="sim"><b>Sim:</b> trate o objeto como carga pontual com a carga total. Erro ≈ (tamanho/2D)². (Degraus 5 e 6; P31 d–e.)</p>',
    '<p class="sim"><b>Sim:</b> se a carga total não for zero, trate o objeto como carga pontual com a carga total, com D medido do centro. O erro cai com (tamanho/D)²; o fator depende da forma (barra: (L/2D)²). (Degraus 5 e 6; P31 d–e.)</p>')
rep('(aí a componente que sobra muda: integre com seno)', '(aí sobra a outra componente: integre só a metade de cima, com seno, de 0 a φ/2, e dobre)')
rep('P fora da reta da barra (aí há componentes; Fig. 22-14 do livro)', 'P fora da reta da barra (aí há componentes; Fig. 22-14b e c do livro)')
rep('<td data-r="Use quando">eixo de um disco isolante uniforme</td>', '<td data-r="Use quando">eixo de um disco isolante uniforme (σ = carga total por área)</td>')
rep('data-fb="Esse é o semicírculo.">2kQ/(πR²)</button>', 'data-fb="Esse é o da semicircunferência.">2kQ/(πR²)</button>')
rep('<td data-r="Valores reais">semicírculo: π rad; quarto: π/2; 120°: 2π/3</td>', '<td data-r="Valores reais">semicircunferência: π rad; quarto: π/2; 120°: 2π/3</td>')
rep('data-fb="No semicírculo ele cai para 64 % (2/π); depois continua caindo.">diminui até a metade</button>',
    'data-fb="Na semicircunferência ele cai para 64 % (2/π); depois continua caindo.">diminui até a metade</button>')

# ================= Dúvidas da turma =================
DT = '''<!-- ======================= DÚVIDAS DA TURMA ======================= -->
<section class="wrap" id="duvidas" aria-labelledby="duvidas-tit" style="margin-top:3rem">
  <h2 id="duvidas-tit">Dúvidas da turma</h2>
  <p class="pequeno">Perguntas que os alunos fizeram na primeira versão deste guia, com a resposta do Professor. Cada uma está ligada ao degrau de onde veio.</p>

  <h3 id="dt-d2">Degrau 2 — Na mesma reta</h3>
  <div class="duvida"><p class="q">No P8 deu zero. É para dar zero mesmo? E se q₄ estivesse do outro lado?</p>
    <p>Dá zero: os dois pares se cancelam (|q|/r² igual, sentidos opostos). Com q₄ na outra diagonal, q₃ e q₄ ficariam em lados opostos com sinais opostos, e os campos se somariam: 346 N/C. Na prova, o sinal é: compare |q|/r² antes de calcular. <a href="#d2">Voltar ao Degrau 2</a></p></div>
  <div class="duvida"><p class="q">Se eu largar uma carga de prova positiva no P do P8, onde o campo é zero, ela fica parada para sempre?</p>
    <p>Só se ninguém a empurrar. Desloque-a um pouco ao longo da reta q₁–q₂ e o campo a empurra de volta; desloque-a ao longo da reta q₃–q₄, ou para fora do plano, e o campo a empurra para longe. É um ponto de sela. Nenhum arranjo de cargas paradas tem um ponto onde uma carga fique presa em todas as direções (teorema de Earnshaw); a razão é a lei de Gauss do Cap. 23. <a href="#d2">Voltar ao Degrau 2</a></p></div>

  <h3 id="dt-d3">Degrau 3 — No plano</h3>
  <div class="duvida"><p class="q">E se, no P9, P estivesse na origem? Ou no eixo x, fora das cargas?</p>
    <p>Na origem, os dois campos apontam para −x e se somam: 2kq/9 = 6,39 × 10⁻¹⁰ N/C, 4,6 vezes o de y = 4 m. A regra "sinais opostos → campo paralelo à reta das cargas" vale em toda a mediatriz. No eixo x, em x = +6 m, o +q (a 3 m) empurra para +x e o −q (a 9 m) puxa para −x; ganha o mais perto, e o campo aponta para +x. A regra não fala desse caso: ela é para pontos da mediatriz. <a href="#d3">Voltar ao Degrau 3</a></p></div>

  <h3 id="dt-d4">Degrau 4 — Arcos</h3>
  <div class="duvida"><p class="q">Com metades de sinais opostos, a integral é "a mesma, com seno"?</p>
    <p>Não com os mesmos limites. De −φ/2 a +φ/2, ∫sen θ dθ = 0. Com sinais opostos, a metade de baixo empurra para o mesmo lado que a de cima: integre de 0 a φ/2 e dobre. Na semicircunferência, 2∫₀^{π/2} sen θ dθ = 2. <a href="#d4">Voltar ao Degrau 4</a></p></div>
  <div class="duvida"><p class="q">O que é radiano, e por que s = rφ só vale com ele?</p>
    <p>Um radiano é o ângulo em que o arco tem o comprimento do raio. Uma volta tem 2π rad, então 180° = π rad e 120° = 2π/3 rad. A fórmula s = rφ é a própria definição do radiano; com graus ela precisaria de um fator π/180. <a href="#d4">Voltar ao Degrau 4</a></p></div>
  <div class="duvida"><p class="q">Na Figura 4-1 as setas parecem trocadas. Posso desenhar cada dE ao longo da reta pedacinho–P?</p>
    <p>Pode e deve: o dE de um pedaço positivo fica na reta que liga o pedaço a P, apontando para longe do pedaço. Por isso a seta de baixo vem do pedaço de cima. <a href="#d4">Voltar ao Degrau 4</a></p></div>

  <h3 id="dt-d5">Degrau 5 — Barra reta</h3>
  <div class="duvida"><p class="q">"Erra 1 %": 1 % de quê? E por que (L/2D)² não serve para o disco?</p>
    <p>Erro é a diferença entre o valor aproximado e o certo, dividida pelo certo. Para a barra no eixo, é exatamente (L/2D)²: 25 % em D = L, 1 % em D = 5L. Para o disco no eixo, de longe, o erro é 0,75(R/z)². O que vale sempre (com carga total diferente de zero) é: o erro cai com o quadrado de tamanho/distância. <a href="#d5">Voltar ao Degrau 5</a></p></div>
  <div class="duvida"><p class="q">Se eu puser uma chapa de cobre entre a barra e P, o campo em P muda? A superposição falha?</p>
    <p>Muda, e a superposição não falha. O cobre tem elétrons livres que se movem e criam um campo contrário; o campo em P é a soma do campo da barra com o das cargas que apareceram no cobre. É a blindagem do Cap. 23. <a href="#d5">Voltar ao Degrau 5</a></p></div>

  <h3 id="dt-d6">Degrau 6 — Disco</h3>
  <div class="duvida"><p class="q">E se o disco tiver σ em cada face? E se for de metal?</p>
    <p>Numa folha fina, o que conta é a carga total por área: com 5,3 µC/m² em cada face, σ = 10,6 µC/m² e Eₘ = 6,0 × 10⁵ N/C. Num disco de metal, a carga não fica uniforme (se concentra na borda) e o campo junto à superfície é σ_face/ε₀; isso é o Cap. 23. O guia trata o disco isolante uniforme do livro. <a href="#d6">Voltar ao Degrau 6</a></p></div>
  <div class="duvida"><p class="q">No P38, de onde sai "cada divisão vale 2 cm"? E como uso z/R = 1/√3 se R é a incógnita?</p>
    <p>Do próprio gráfico: o eixo vai de 0 a zₛ = 8,0 cm em 4 divisões iguais, então cada uma vale 2,0 cm. Ler a escala assim faz parte do problema (o livro também só numera 0 e zₛ). E use a relação ao contrário: você lê o z da metade e sabe que, em qualquer disco, esse z vale R/√3. Então R = √3 vezes esse z. <a href="#P38">Voltar ao P38</a></p></div>

  <h3 id="dt-visao">O resto do capítulo</h3>
  <div class="duvida"><p class="q">O P9 é um dipolo?</p>
    <p>É: duas cargas iguais e opostas. Mas o problema se resolve somando dois campos (Degrau 3), sem as fórmulas de dipolo, que valem para pontos distantes. O P9 até confere uma previsão da teoria: na mediatriz, o campo tem o sentido oposto ao do momento dipolar. <a href="#visao">Voltar à visão geral</a></p></div>
</section>

'''
rep('<!-- ======================= SÍNTESE ======================= -->', DT + '<!-- ======================= SÍNTESE ======================= -->')
for d in ['d2', 'd3', 'd4', 'd5', 'd6']:
    i = s.index(f'id="{d}"')
    j = s.index('</section>', i)
    s = s[:j] + f'  <p class="link-dt"><a href="#dt-{d}">Dúvidas da turma sobre este degrau</a></p>\n' + s[j:]
rep('Depois dos degraus: <a href="#visao">o resto do capítulo em 2 minutos</a>, <a href="#questoes">as questões</a>, <a href="#sintese">síntese</a> e <a href="#revisao">revisão intercalada</a>.',
    'Depois dos degraus: <a href="#visao">o resto do capítulo em 2 minutos</a>, <a href="#questoes">as questões</a>, <a href="#duvidas">dúvidas da turma</a>, <a href="#sintese">síntese</a> e <a href="#revisao">revisão intercalada</a>.')

# ================= JavaScript =================
rep("""    if (!s) return { erro: 'Digite um número.' };
    if (unid) {
      var u = unid.replace(/[()]/g, '').trim();
      if (u && s.toLowerCase().slice(-u.length) === u.toLowerCase()) s = s.slice(0, -u.length).trim();
    }""", """    if (!s) return { erro: 'Digite um número.' };
    if (/^(zero|nulo|nula)$/i.test(s)) return { v: 0 };
    var fator = 1;
    if (unid) {
      var u = unid.replace(/[()]/g, '').trim();
      var conv = { m: { m: 1, cm: 0.01, mm: 0.001 }, cm: { cm: 1, m: 100, mm: 0.1 } }[u];
      var suf = /\\s*(cm|mm|m)\\s*$/i.exec(s);
      if (conv && suf && conv[suf[1].toLowerCase()] != null) { fator = conv[suf[1].toLowerCase()]; s = s.slice(0, suf.index).trim(); }
      else if (u && s.toLowerCase().slice(-u.length) === u.toLowerCase()) s = s.slice(0, -u.length).trim();
    }""")
rep("      return { v: v };", "      return { v: v * fator };")
# W1: força numa carga colocada em P
i = s.index("    var E = 9989 * Math.abs(q) / (r * r);")
j = s.index('\n', s.index("$('#w1-leitura').textContent", i))
s = s[:i] + """    attr($('#w1-et'), { x: x + dir * L / 2 - 4 });
    var pq = parseFloat(segVal('w1-prova'));
    var E = 9989 * Math.abs(q) / (r * r);
    var txt = 'r = ' + fmt(3 * r, 1) + ' cm, carga ' + (q > 0 ? '+' : '−') + fmt(Math.abs(q), 1) + ' nC: E = ' + fmtSci(E) + ' N/C, ' + (dir > 0 ? 'para longe da carga' : 'para a carga') + ' (' + fmt(Math.abs(q) / (r * r), 3).replace(/,?0+$/, '') + ' × o campo de 1,0 nC a 3,0 cm).';
    var f = $('#w1-f'), ft = $('#w1-ft');
    if (pq) {
      var fdir = dir * pq, LF = Math.max(10, L);
      attr(f, { x1: x, x2: x + fdir * LF, y1: 56, y2: 56 });
      f.style.visibility = 'visible';
      ft.textContent = 'F = qE';
      attr(ft, { x: x + (fdir > 0 ? 4 : -60) });
      txt += ' Carga de ' + (pq > 0 ? '+' : '−') + '1 pC em P: F = |q|E = ' + fmtSci(1e-12 * E) + ' N, ' + (fdir === dir ? 'no mesmo sentido de E' : 'no sentido oposto ao de E') + '.';
    } else { f.style.visibility = 'hidden'; ft.textContent = ''; }
    $('#w1-leitura').textContent = txt;""" + s[j:]
rep("if ($('#w1')) { $('#w1-r').addEventListener('input', w1); seg('w1-sinal', w1); w1(); }",
    "if ($('#w1')) { $('#w1-r').addEventListener('input', w1); seg('w1-sinal', w1); seg('w1-prova', w1); w1(); }")
# W2: valores ao lado dos sliders e "total = 0"
rep('<label>Carga A (nC): <input type="range" id="w2-qa"', '<label>Carga A: <b id="w2-qa-v"></b> nC <input type="range" id="w2-qa"')
rep('<label>Posição de A (cm): <input type="range" id="w2-xa"', '<label>Posição de A: <b id="w2-xa-v"></b> cm <input type="range" id="w2-xa"')
rep('<label>Carga B (nC): <input type="range" id="w2-qb"', '<label>Carga B: <b id="w2-qb-v"></b> nC <input type="range" id="w2-qb"')
rep('<label>Posição de B (cm): <input type="range" id="w2-xb"', '<label>Posição de B: <b id="w2-xb-v"></b> cm <input type="range" id="w2-xb"')
rep("seta('w2-va', 'w2-ta', ea, 45); seta('w2-vb', 'w2-tb', eb, 25); seta('w2-vt', 'w2-tt', et, 140);",
    "seta('w2-va', 'w2-ta', ea, 45); seta('w2-vb', 'w2-tb', eb, 25); seta('w2-vt', 'w2-tt', et, 140);\n"
    "    $('#w2-tt').textContent = Math.abs(et) < 1e-9 ? 'total = 0' : 'total';\n"
    "    function sn(v) { return (v > 0 ? '+' : v < 0 ? '−' : '') + Math.abs(v); }\n"
    "    $('#w2-qa-v').textContent = sn(qa); $('#w2-xa-v').textContent = sn(xa); $('#w2-qb-v').textContent = sn(qb); $('#w2-xb-v').textContent = sn(xb);")
# W3: componentes tracejadas, rótulo da carga, leitura em N/C, campo nulo
rep("    var ex = e1[0] + e2[0], ey = e1[1] + e2[1];",
    "    var ex = e1[0] + e2[0], ey = e1[1] + e2[1];\n    if (Math.abs(ex) < 1e-12) ex = 0;\n    if (Math.abs(ey) < 1e-12) ey = 0;")
rep("    seta('w3-v1', e1); seta('w3-v2', e2); seta('w3-vt', [ex, ey]);",
    "    seta('w3-v1', e1); seta('w3-v2', e2); seta('w3-vt', [ex, ey]);\n"
    "    var Lt = Math.sqrt(ex * ex + ey * ey) * F, esct = Lt > 200 ? 200 / Lt : 1;\n"
    "    var tx = 180 + ex * F * esct, ty = py - ey * F * esct;\n"
    "    attr($('#w3-cx'), { x1: 180, y1: py, x2: tx, y2: py }); attr($('#w3-cy'), { x1: tx, y1: py, x2: tx, y2: ty });\n"
    "    var ta = $('#w3-ta'); ta.textContent = sa > 0 ? '+q' : '−q'; ta.setAttribute('class', sa > 0 ? 't-s t-p' : 't-s t-n');")
i = s.index("    $('#w3-leitura').textContent")
j = s.index('\n', i)
s = s[:i] + """    var K = 8.99e9 * 2e-9 / 1e-4;
    $('#w3-leitura').textContent = mod < 1e-12 ? 'Com P em y = ' + fmt(y, 1) + ' cm o campo total é zero: os dois campos são horizontais, iguais e opostos.' :
      'Com q = 2,0 nC e distâncias em cm: Ex = ' + fmtSci(ex * K) + ' N/C, Ey = ' + fmtSci(ey * K) + ' N/C, |E| = ' + fmtSci(mod * K) + ' N/C, ângulo com +x = ' + fmt(th, 0) + '°. ' + (sa > 0 ? 'Mesmo sinal: o total fica sobre o eixo y.' : 'Sinais opostos: o total fica paralelo ao eixo x.');""" + s[j:]
# W5: erro em % em escala log, com a faixa de 1 %
i = s.index('  function w5() {')
j = s.index('  function w6() {')
s = s[:i] + """  function w5() {
    var u = parseFloat($('#w5-d').value);
    function erro(x) { return 100 / (4 * x * x); }
    function X(x) { return 40 + 31 * x; }
    function Y(v) { return 200 - (Math.log10(v) + 1) * 60; }
    if (!$('#w5-curva').getAttribute('d')) {
      var p = [];
      for (var x = 0.6; x <= 10.0001; x += 0.05) p.push((p.length ? 'L ' : 'M ') + X(x).toFixed(1) + ' ' + Y(erro(x)).toFixed(1));
      $('#w5-curva').setAttribute('d', p.join(' '));
      attr($('#w5-um'), { y1: Y(1), y2: Y(1) });
      attr($('#w5-faixa'), { y: Y(1), height: 200 - Y(1) });
      attr($('#w5-tf'), { y: Y(1) + 16 });
      var g = $('#w5-grade');
      [[0.1, '0,1'], [1, '1'], [10, '10'], [100, '100']].forEach(function (p2) {
        var t = svgEl('text', { x: 4, y: Y(p2[0]) + 4, class: 't-2' }); t.textContent = p2[1]; g.appendChild(t);
        g.appendChild(svgEl('line', { x1: 40, x2: 350, y1: Y(p2[0]), y2: Y(p2[0]), class: 'grade-g' }));
      });
      [0, 2, 4, 6, 8, 10].forEach(function (v) { var t = svgEl('text', { x: X(v) - 4, y: 216, class: 't-2' }); t.textContent = String(v); g.appendChild(t); });
    }
    attr($('#w5-m'), { cx: X(u), cy: Y(erro(u)) });
    var e = erro(u);
    $('#w5-leitura').textContent = 'D = ' + fmt(u, 1) + ' L: trocar a barra por uma carga pontual no centro erra ' + fmt(e, e < 1 ? 2 : 1) + ' % (o ponto dá um pouco menos que a barra). ' + (e <= 1.0001 ? 'Dentro da faixa de 1 %.' : 'Ainda fora da faixa de 1 %.');
  }

""" + s[j:]

open(ARQ, 'w', encoding='utf-8').write(s)
print('erros:' if erros else 'ok, sem erros')
for e in erros:
    print(' ', e)
sys.exit(1 if erros else 0)
