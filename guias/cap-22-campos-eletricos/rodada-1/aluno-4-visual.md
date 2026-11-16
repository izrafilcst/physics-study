# Aluno 4 (visual e prático): relatório da Rodada 1, Capítulo 22

Material usado: as 40 capturas (`celular-*`, `desktop-*`, `escuro-d4`, `escuro-p38`), o texto cego, e o HTML só para ver os SVG e o JavaScript dos widgets (W1 a W6) e dois trechos de CSS. Não abri `conferir/` nem `ajuda/`. As capturas mostram cada widget já destravado e no estado inicial; os outros estados (W3 com −q, W4 em "metade +, metade −", W4 a 360°) eu só avaliei lendo o código, e digo isso onde importa.

Medidas que fiz nas capturas (pixels): P38, P8, P9, P15, P26, P29, Fig. 2-2, Fig. 3-1, Fig. 4-3 e Fig. 5-1 (escalas, na seção 3).

Observação fora do papel de aluno: para o P8, olhei `plano.md` e `calculos.py` depois de calcular a figura sozinho. Os dois confirmam que "tudo se cancela" (E = 0) é intencional. Então o problema do P8 não é a figura, é o aluno não ser preparado para um zero (item V27).

---

## 1. Itens de crítica

Gravidade: **bloqueia** = não dá para continuar ou o aluno aprende errado sem saber; **atrapalha** = perde tempo ou confiança; **polimento** = incomoda mas não impede.
Nenhum item chegou a "bloqueia". Os oito mais pesados são marcados com asterisco no número (V05\*, V07\*, V08\*, V15\*, V18\*, V20\*, V23\*, V24\*).

| # | Local | Tipo | Gravidade | Evidência (captura) | Sugestão |
|---|---|---|---|---|---|
| V01 | Topo, mapa da subida | outro | polimento | `celular-topo`: no celular a escada vira uma lista alinhada à direita com o degrau 6 no alto e o 0 embaixo, ao contrário da ordem da página. `desktop-topo`: o degrau 0 tem uma faixa âmbar no topo que nenhuma legenda explica. A legenda de cores não tem "força (preto)", cor usada nas Figs. 0-1 e 1-1. | Listar 0 a 6 de cima para baixo no celular; legendar ou tirar a faixa; acrescentar "força: preto" à legenda. |
| V02 | Fig. 0-1 (gancho) | figura confusa | polimento | `desktop-d0`: esfera de enxofre amarela e setas de campo âmbar quase do mesmo tom, mas "âmbar = campo". As setas de E ficam soltas ao lado da esfera. `celular-d0`: "E ≈ 150 N/C" e "W = 4,4 N" ficam com ~9 px. | Esfera em cinza-amarelado com contorno; setas E sobre a esfera. |
| V03 | Fig. 1-2 (1/r²) | figura confusa | polimento | `desktop-d1_01`: as setas de r ficam nos eixos e as de 2r nas diagonais, então a comparação "4 vezes menor" é entre direções diferentes. As setas de ¼ do tamanho têm ~12 px e parecem só pontas. Não há ponto P onde a seta nasce, contra a regra do próprio texto ("nasce em P"). Rótulos "r" e "2r" ~8 px no celular. | Pôr as setas de r e 2r na mesma semirreta, marcar P com ponto e fazer a seta de 2r com pelo menos 25 px. |
| V04 | Rótulos "Eq. 22-1, 22-28, 22-3, 22-16, 22-26" e as etiquetas "centro de um arco uniforme" e "P no prolongamento da barra" | outro | atrapalha | `desktop-d6_00`: "Eq. 22-16" aparece ao lado de "O disco de densidade σ e raio R…", mas é a equação do anel. `desktop-d4_01`: "centro de um arco uniforme" flutua ao lado de "Dois casos que você vai usar". `desktop-d1_01`: "Eq. 22-3" fica na linha do "Sentido:". No HTML, `.formula .eq-n {float:right}` vem depois da fórmula em bloco, então cai na linha do parágrafo seguinte. O guia cita equações pelo número ("Eq. 22-3", "Eq. 22-26"), então errar qual é qual custa caro. | Pôr o número dentro do bloco da fórmula, na mesma linha, à direita. |
| V05\* | Fórmulas-chave no celular | figura confusa (corte) | atrapalha | `celular-d5` ("A conta"): `= kλ(1/a − 1/(a+L)) = kλL/(a…` é cortado; o resultado usado no P31, kλL/(a(a+L)), some. "De longe": o limite `→ kq/D²` é cortado. `celular-d4`: "num arco: L = rφ (φ em radianos)" é cortado em "(φ". `celular-d3`: "θ = ângulo com o semieixo +x, pelo quadrante de (Ex, Ey)" é cortado em "sem". O CSS usa `.katex-display{overflow-x:auto}` sem sombra nem seta de rolagem. | Quebrar em linhas (`aligned`), pôr o resultado final sozinho numa linha, e/ou sombra de rolagem. |
| V06 | Rótulos de passo (Entender, Modelar, Resolver, Calcular, Verificar) | outro | polimento | `desktop-d1_03`, `desktop-d4_04`, `celular-d1`: o rótulo é `inline-block` de 7,2 rem e a 2ª linha do texto volta para baixo do rótulo, sem recuo; com frações grandes em linha as linhas se atropelam (`desktop-d4_04`, "Calcular": o "kQ" encosta no "2π" da linha de cima). | Grade de duas colunas (rótulo, texto) com recuo; no celular, rótulo acima do texto. |
| V07\* | Texto dentro dos SVG no celular | figura confusa | atrapalha | O SVG diminui junto com a largura, e o texto de 12 px vira ~7 px: W2 (marcas −4 a 4, E_A, E_B: `sheet-d2`), Fig. 2-1, Fig. 5-1 ("L", "a", "x"), Teste 2 e Pergunta 11 (`celular-d4`: arcos de ~35 px, "(a)" a "(e)" ~6 px), P29/P31 ("R", "a"), e **P38** (`celular-p38`: "Eₘ", "0,5Eₘ", "zₛ", "z (cm)" ~6 a 7 px, a figura em que o aluno precisa ler a grade). | Texto mínimo efetivo de 11 px (CSS por largura), figuras largas com rolagem horizontal ou toque para ampliar; P38 em largura total. |
| V08\* | Fig. 2-2 (exemplo resolvido) | erro físico (figura contra texto) | atrapalha | `desktop-d2_02`: só aparecem E_A e E_B. Não há seta roxa do total (7,5 × 10⁴ N/C), embora o `aria-label` do SVG diga que existe e a legenda do topo reserve roxo para o total. Conferi no HTML: só duas linhas `ve`. | Desenhar a seta roxa do total (comprimento = soma) abaixo das duas, rotulada E. |
| V09 | W2 (controles e estado inicial) | dica fraca | polimento | `desktop-d2_01/02`: os quatro sliders não mostram o valor (só "Carga A (nC):"); o aluno lê o número no desenho ("A: +1"). Quando o total é zero, a palavra "total" fica sem seta e parece bug (a seta é ocultada com `visibility:hidden` se |L| < 1). O estado inicial (A = +1 em −1 cm, B = +4 em +2 cm) é exatamente o da previsão: ao abrir, o widget já mostra a resposta. | Valor numérico ao lado de cada slider; escrever "total = 0" no lugar da seta; abrir em outro estado e pedir "ache outro arranjo em que dê zero". |
| V10 | Pergunta 4 (Degrau 2) | figura confusa | polimento | `desktop-d2_05`: a linha de cota embaixo tem pontas de seta que se sobrepõem em "⤫" entre cada par de cargas e **não tem o rótulo d**, que a legenda cita. | Rotular "d" em cada vão; uma seta por vão, sem sobrepor. |
| V11 | Regra dos quadrantes (Degrau 3) | denso demais | atrapalha | `desktop-d3_01`: "No 2º quadrante, 180° − ref; no 3º, 180° + ref (ou −180° + ref); no 4º, −ref" é um parágrafo. A Fig. 3-2 só mostra o 3º quadrante. É o erro que o guia mais avisa (atan da calculadora). | Figura de 4 quadrantes com o ângulo de referência e a fórmula escritos em cada um. |
| V12 | Fig. 3-2 | figura confusa | polimento | `fig32` (ampliada): o "53°" está ~150 px longe do arcozinho que rotula e é cortado pela tracejada de x = −3; os dois arcos (233° e 53°) com seta terminam quase no mesmo ponto. A grade de fundo não bate com os valores −3 e −4. | Pôr "53°" encostado no arco pequeno, sem tracejada por cima; alinhar a grade às unidades ou remover. |
| V13 | W3 | falta prática (figura) | atrapalha | `desktop-d3_02`: o SVG só tem E₁, E₂ e total; **não há componentes tracejadas** (o `aria-label` e o bloco de texto dizem que há), nem rótulos +q/−q nas cargas, nem números nos eixos. A leitura sai em "unidades de kq/cm²" (unidade que ninguém usa), e o ângulo aparece só em número. O estado inicial (y = 4, +q, +q) é a Fig. 3-1: já mostra a previsão. | Desenhar Ex e Ey tracejadas; marcar −3, +3 e y; leitura com q = 2 nC em N/C; arco de θ. |
| V14 | Fig. 3-3 (triângulo) | figura confusa | polimento | `desktop-d3_03`: os lados do triângulo atravessam "\|q\| = 12 nC" nos dois vértices e "2,0 m". A lacuna pede "ângulo entre cada campo e o eixo de simetria" e a figura não desenha o campo nem o 30°. | Rótulos afastados dos lados; mostrar o ângulo de 30° do vértice (ou pedir ao aluno que o desenhe). |
| V15\* | Fig. 4-3 (arco de 120°) | figura confusa | atrapalha | `fig43` (ampliada): o texto "120°" está entre o tracejado de cima e o eixo, **sem arco**, e lê-se como ~60°. O ângulo total (de um tracejado ao outro, ±60° de cada lado) nunca é marcado, e a integral usa exatamente ±60°. (A geometria está certa: medi extremos a 59,7°; o erro é só de rótulo.) | Arco de 120° cruzando o eixo, com "φ = 120°"; marcar também "60°" de cada lado. |
| V16 | Fig. 4-1 (par simétrico) | figura confusa | atrapalha | `desktop-d4_01`: (i) φ e os limites ±φ/2 não aparecem; só θ do elemento. (ii) dE′ (seta de cima) é do pedaço de baixo, dq′, e dE (seta de baixo) é do de cima: as setas estão cruzadas e só têm rótulo na ponta, então eu li ao contrário na primeira vez. (iii) "verticais: se cancelam" está solto no canto, longe do tracejado âmbar que une as pontas das setas. (iv) A componente que sobra (dE cos θ) não é desenhada. (v) `escuro-d4_01`: o arco fica fosco, bem menos contrastante que os pontos. | Prolongar cada dE em tracejado até o pedaço que o gera; rótulo "se cancelam" ao lado do tracejado vertical; desenhar dE cos θ; marcar φ. |
| V17 | Fig. 4-2 | dica entrega demais | polimento | `desktop-d4_02`: a figura e o parágrafo ao lado resolvem a direção do P26 (verticais somam para baixo, −90°) antes de o aluno tentar o P26, que tem o mesmo desenho. Rótulos "+", "−", "horizontais: se cancelam" ~9 px. | Manter o conceito, mas esconder a seta roxa até o aluno prever o sentido. |
| V18\* | W5 (barra × ponto) | figura confusa | atrapalha | `desktop-d5_02`: a curva começa em D/L = 0,6 (razão 3,3) e a partir de D/L ≈ 3 fica colada na linha tracejada de 1. A pergunta é onde o erro chega a 1 %, e a diferença nesse ponto é 0,0101 × 70 = 0,7 px no SVG: **a resposta, D = 5L, não se enxerga no gráfico**, só na frase de baixo. Sem marca em D/L = 0,5 (abaixo disso P estaria dentro da barra). | Plotar o erro em % com eixo vertical logarítmico (ou dois painéis: 0,5 a 3 e 3 a 10), com uma faixa de ±1 % sombreada; traço vertical em D/L = 0,5 ("P na ponta: E → ∞"). |
| V19 | Fig. 5-1 e Fig. 5-2 | figura confusa | polimento | `fig5`: a cota L e a cota a terminam numa mesma ponta de seta sobreposta ("✕"); "dq = λ dx", "L", "a", "x" com ~8 px e cinza claro. Na Fig. 5-1 o ponto P e a ponta "perto" estão à direita; na 5-2 "perto" está à esquerda (a legenda avisa, mas o aluno tem de espelhar na cabeça). | Desenhar P à esquerda na 5-1 (ou o eixo da 5-2 invertido); aumentar rótulos. |
| V20\* | Fig. 5-1 e P31 (D e o centro da barra) | falta prática (figura) | atrapalha | D (distância de P ao centro) é central em "De longe, a barra vira um ponto", no W5, no Erro comum 1 e no P31 (d) e (e), mas **nenhuma figura marca o centro nem o D**. O enunciado do P31 usa "a" para duas coisas (12,0 cm da extremidade em (b), (c); 50 m do centro em (d), (e)) e `desktop-p31` só mostra a primeira. A Fig. 22-54 também não está em escala: a (12,0 cm) aparece com 0,6 L (134 px contra 220 px de L) quando vale 1,47 L. | Marcar o centro e D em tracejado na Fig. 5-1 e na Fig. 22-54, com a nota "(d), (e): a é medido do centro"; avisar "fora de escala" ou desenhar em escala. |
| V21 | Fig. 6-1 (anel e disco) | figura confusa | polimento | `fig61`: duas setas âmbar inclinadas em P e nenhuma seta roxa para a componente que sobra (a legenda diz "sobra só a componente ao longo de z"). Dois "z" (rótulo do eixo e distância). "r" e "R" ~8 px. Os tracejados vão do anel ao P e as setas continuam do lado oposto (cruzadas, como na Fig. 4-1). | Seta roxa vertical; cota de z com setas; "z" do eixo diferente da cota. |
| V22 | W6 (disco) | falta prática | atrapalha | `desktop-d6_02`: o gráfico é E/Eₘ contra z/R, mas o P38 e o Erro comum 3 do degrau tratam da leitura de **z em cm com R escondido**. O widget não treina isso. Roxo (cor de "campo total") é usado para "placa infinita" e para o marcador. O rótulo "disco" é cruzado pela curva pontilhada. | Botão "eixo em cm, R oculto" (o aluno acha a escala e depois R); trocar roxo por cinza/verde no que não é campo total. |
| V23\* | Previsões de W1, W2, W3 e W6 | salto lógico (pedagógico) | atrapalha | A resposta está escrita logo acima da pergunta. W1: Ficha "r dobra → E cai para ¼" e Fig. 1-2 ("4 vezes menor"). W2: o parágrafo "|q| ∝ r²: uma carga 4 vezes maior a uma distância 2 vezes maior faz o mesmo campo" tem os mesmos números (1 nC a 1 cm; 4 nC a 2 cm). W3: a Fig. 3-1 imediatamente acima mostra E total para +y. W6: "Logo acima do centro… placa infinita" é um dos três limites do bullet. Prever o que acabou de ser dito vira releitura, e `desktop-d2_01` mostra a alternativa b com "(a carga maior ganha)" como isca que o texto já desmontou. | Mover a previsão para antes do texto que a responde, ou mudar o caso: W1 "dobro da distância e metade da carga?", W2 "A = +2 nC a 1 cm e B = +8 nC a 3 cm", W3 "agora a da esquerda é negativa: para onde aponta?". |
| V24\* | Falta um widget de F = qE | falta prática | atrapalha | O Degrau 1 é "campo = força por coulomb", mas W1 só mexe em r e no sinal da carga **fonte**. Nada mostra a força numa carga de prova de sinal e valor escolhidos. O P81 e o checkpoint do elétron dependem desse sinal ("força oposta ao campo"), e a pergunta mais pedida pelo guia, "o sentido muda com o sinal?", só existe em texto. | W1b: ponto P, carga de prova ±q₀ ajustável, seta amarela de E e seta preta de F = qE; leitura "F = q E, para onde". |
| V25 | W4 | dica fraca | polimento | `desktop-d4_03`: até φ ≈ 90° a seta roxa e a tracejada diferem menos de 10 % (a leitura diz 5 % em 60°), invisível a olho. No modo "metade +, metade −" a tracejada de referência some e só sobra a seta para baixo. | Barra horizontal (comprimento da seta × kQ/r²) abaixo da figura; manter uma referência no modo misto (por exemplo, a mesma carga toda de um lado). |
| V26 | W1 | dica fraca | polimento | `celular-d1`: em r = 2r₀ a seta fica com ~10 px (parece só ponta). O código usa `L = max(6, 60|q|/r²)`: em r = 4r₀ o valor real seria 3,75 e aparecem 6, então o "1/16" aparece como "1/10". O valor de r em unidades de r₀ não aparece ao lado do slider (só em cm na leitura). | Remover o piso ou mostrar uma "fantasma" tracejada de r₀ para comparação; mostrar r/r₀ no rótulo. |
| V27 | P8 | salto lógico | atrapalha | `desktop-p8`: pela figura, q₁ e q₂ (5e, a d, lados opostos) se cancelam e q₃ e q₄ (3e a d; 12e a 2d, **mesmo lado**) também: 3 − 12/4 = 0. O campo é zero e o enunciado pergunta "qual é o módulo". Nada na figura (sem as cargas rotuladas com valores) nem na dica "calcule |q|/r² em e/d²" avisa que zero é uma resposta possível. O Degrau 2 ensina o cancelamento, mas o "Agora você completa" dele também dá zero (1 nC a 1 cm contra 4 nC a 2 cm, outra vez), então o aluno vê o 4:1 em quatro lugares. | Escrever "+5e", "+5e", "+3e", "−12e" na figura; frase na dica 1: "o resultado pode ser zero, confira por pares". |
| V28 | P81 e a gota de Millikan | falta prática | atrapalha | `desktop-p81` não tem figura; só o texto e as alternativas, e a dica lembra "já desenhou a esfera com as forças?" sem mostrar o que desenhar. Em `desktop-d1_04`, as quatro lacunas da gota de Millikan (massa, peso, q, q/e) são cálculo puro, sem desenho da gota entre placas com mg e qE. | Para o P81, mostrar a Fig. 0-1 como molde após a primeira tentativa. Para Millikan, uma figura de diagrama de forças com as setas rotuladas (pedir ao aluno que acerte o sentido de qE). |
| V29 | "Usa: …" de cada questão e chips P81…P38 no mapa | dica entrega demais | polimento | `desktop-p9`: "Usa: Pitágoras, componentes com o triângulo 3-4-5, simetria com sinais opostos, ângulo pelo quadrante" é o plano de ataque inteiro, antes do aluno tentar. A Síntese ensina a escolher a ferramenta, mas cada problema já a entrega. | Esconder o "Usa:" atrás de um botão ou só na Dica 1; na revisão intercalada, problemas sem "Usa:". |
| V30 | Figuras de checkpoint sem eixos | figura confusa | polimento | `desktop-d3_04` (Pergunta 3): a pergunta fala em "componentes x, +y, −x" e a figura não tem "x" nem "y". `desktop-d4_06` (Pergunta 11): a legenda diz "4º quadrante" e a figura não tem eixos nem rótulo de quadrante. O Teste 3 (Degrau 1) tem os dois. | Eixos finos com "x", "y" em todas. |
| V31 | Fundo quadriculado das figuras | outro | polimento | Todas as figuras (exceto P38, W5 e W6) têm papel milimetrado de fundo sem relação com as unidades; na Fig. 3-2, −3 e −4 não caem em linhas da grade. Em P38 e W5/W6 a grade tem significado. O aluno pode contar quadradinhos como escala. | Grade bem mais fraca, ou remover onde não significa nada. |
| V32 | Fig. 0-1, pré-teste e ficha (ordens de grandeza) | falta prática | polimento | Ver seção 5: faltam referências de mundo real e uma régua de ordens de grandeza do campo. | Seção 5. |

---

## 2. Figura por figura e widget por widget (resumo do veredito)

Legenda: ensina = o desenho mostra a ideia do bloco ao lado; parcial = mostra, mas com ruído ou lacuna; enfeite = não acrescenta ao texto.

| Elemento | Veredito | Motivo curto |
|---|---|---|
| Fig. 0-1 | ensina (como gancho) | Força elétrica tracejada e peso rotulados; cor do enxofre atrapalha (V02). |
| Fig. 1-1 | ensina | (a) com carga de prova e (b) sem ela, mesma seta; boa. |
| Fig. 1-2 | parcial | 1/r² visível, mas em direções diferentes e sem P (V03). |
| Fig. 2-1 | ensina | Quatro casos, uma linha cada, rótulo à esquerda, seta nasce em P, cores certas. |
| Fig. 2-2 | parcial | Falta o total roxo (V08). |
| Fig. 2-3 | ensina | Figura em branco para o aluno desenhar. É o único lugar em que o guia manda desenhar. |
| Teste 1 e Pergunta 4 | parcial | Teste 1 bom; Pergunta 4 com cota sem "d" (V10). |
| Fig. 3-1 | ensina | Triângulo 3-4-5 com 3,0, 4,0, 5,0 cm; E₁, E₂, E; componentes x tracejadas. Só faltam as y. |
| Fig. 3-2 | parcial | Só 3º quadrante; rótulo 53° deslocado (V11, V12). |
| Fig. 3-3 | parcial | Cargas cinza (sinais abertos), bom; rótulos cruzados pelos lados (V14). |
| Fig. 4-1 | parcial | Falta φ, setas cruzadas, rótulo solto (V16). |
| Fig. 4-2 | ensina (demais) | Resolve o P26 por antecipação (V17). |
| Fig. 4-3 | parcial | 120° mal rotulado (V15). |
| Teste 2 e Pergunta 11 | ensina | Desenhos limpos; só pequenos no celular (V07, V30). |
| Fig. 5-1 | parcial | Sem D/centro; cotas sobrepostas; tiny (V19, V20). |
| Fig. 5-2 | ensina | Área sob 1/x² entre a e a + L, com seta "área sombreada = integral". Espelhada em relação à 5-1. |
| Fig. 6-1 | parcial | Sem componente que sobra (V21). |
| Pergunta 9 (disco, 2R, anel) | ensina | Proporções certas (92, 182, 182 px; anel de 92 a 182). |
| W1 | parcial | Só ensina 1/r² (V23, V24, V26). |
| W2 | ensina | Leitura em palavras e setas empilhadas; ver V09. |
| W3 | parcial | Sem componentes (V13). |
| W4 | ensina | Seta tracejada (carga toda) contra seta roxa (arco) mais leitura com "desconto %". |
| W5 | parcial | O 1 % não se vê (V18). |
| W6 | ensina | Três curvas num gráfico normalizado; leitura com erro de cada aproximação. Falta o modo "cm" (V22). |
| Figuras das questões | ensina | P8, P9, P15, P26, P29 e P38 reproduzem o enunciado; P31 fora de escala (V20). |

---

## 3. Eixos, unidades e escalas contra o enunciado

Medi nas capturas desktop (pixels) e comparei com o enunciado.

| Figura | O que conferi | Resultado |
|---|---|---|
| **P38** (Fig. 22-58b) | Linhas verticais de grade em x = 262, 356, 450, 545, 639 (4 divisões iguais de 94 px). Horizontais em 300 (Eₘ), 402 (0,5Eₘ), 502 (zero). Curva: 1,00 em z = 0; 0,718 em z = 2 cm; **0,500 em z = 4 cm (cruza exatamente a 2ª vertical sobre a linha de 0,5Eₘ)**; 0,342 em z = 6 cm; 0,243 em z = 8 cm. | Bate com R = 4,0·√3 ≈ 6,93 cm: a fórmula dá 0,723, 0,345 e 0,244 nos três outros pontos (erro < 1 %). zₛ = 8,0 cm está só em letra no eixo, como no livro. Em `escuro-p38` a grade e a curva ficam visíveis. |
| P8 (Fig. 22-36) | q₁ e q₂ a 114 px de P em lados opostos; q₃ a 114 px; q₄ a 230 px (= 2d); ângulo reto marcado em P. | Bate com o enunciado. O resultado é E = 0 (V27). |
| P9 (Fig. 22-37) | ±3,00 m = 126 px (42,2 px/m); P a 169 px = 4,00 m. | Em escala (triângulo 3-4-5 correto). |
| P15 (Fig. 22-42) | q₃ (0,0), q₁ a 238 px acima, q₂ a 239 px à direita; P no centro do quadrado. | Em escala. |
| P26 (Fig. 22-50) | Semicírculo à esquerda de P; +q no quadrante de cima, −q no de baixo; raio de 155 px. | Bate com o enunciado. |
| P29 (Fig. 22-52) | R do arco = 97 px; R da carga pontual = 102 px; mesma escala nas duas partes. | Bate. |
| P31 (Fig. 22-54) | L = 220 px; a = 134 px. | **Fora de escala**: a/L = 0,6 contra 1,47 do enunciado (V20). Falta o D para (d), (e). |
| Fig. 2-2 | 47,5 px/cm nos dois lados de P; setas E_A = 74 px e E_B = 52 px para 4,5 e 3,0 × 10⁴ N/C. | Escala boa (1,42 contra 1,5); falta o total. |
| Fig. 3-1 | 36 px/cm em x e y; E₁ ≈ 51 px, E ≈ 74 px. | Boa; o total fica ~10 % curto (74 contra 82). |
| Fig. 4-3 | Extremos do arco a 59,7° do eixo, raio de 307 a 315 px. | Geometria certa (120°); rótulo errado (V15). |
| Fig. 5-1 | a/L = 162/328 = 0,49. | Bate com o exemplo (a = 5 cm, L = 10 cm). |
| W5 (código) | f(x) = 1/(1 − 1/(4x²)); mínimo 0,6 e 1,0101 em x = 5. | Certo; a escala do eixo esconde o 1 % (V18). |
| W6 (código) | E/Eₘ = 1 − u/√(u²+1); carga pontual = 1/(2u²). Em z = R: 0,293 e 0,500. | Certo; bate com a leitura "erra 241 %" e "erra 71 %". |
| Unidades dos widgets | W2, W3, W4 expressam o campo em "N/C × 8,99×10⁴", "kq/cm²" e "× kQ/r²". | Corretas, mas só W1 dá N/C (V13). |

---

## 4. Widgets W1 a W6: previsão, resposta e leitura

| W | A previsão faz sentido antes de mexer? | O widget responde? | A leitura numérica ajuda? | O que eu mudaria |
|---|---|---|---|---|
| W1 | Sim, mas é redundante: a resposta está na Ficha e na legenda da Fig. 1-2 (V23). | Sim: seta cai com 1/r², mas fica minúscula a partir de 2r₀ (V26). | Sim: "E = 2,50 × 10³ N/C… 0,25 × o valor a 3,0 cm". | Pôr carga de prova (V24); remover o piso de 6 px (V26). |
| W2 | Boa pergunta, redundante com o parágrafo de cima e igual ao estado inicial (V09, V23). | Sim: seta em E_A e E_B, e o total some. | Sim: dá módulo e sentido em palavras ("para a direita"). | Mostrar o valor nos sliders; novo estado inicial; "total = 0". |
| W3 | A previsão (+, + → +y) é a própria Fig. 3-1 (V23). | Parcialmente: sem componentes, o aluno não vê "Ex cancela". | Em "kq/cm²", pouco útil. | Componentes tracejadas, eixos numerados, q real, arco de θ (V13). |
| W4 | Boa: mesa cheia contra metade; a resposta não é óbvia ("até a metade" é isca). | Sim: o arco abre e a seta roxa encolhe. | Sim: "0,955 × kQ/r² … desconto 5 %". | Barra de comprimento; referência no modo misto (V25). Não vi a captura do modo misto nem de 360°. |
| W5 | Ótima: pergunta quantitativa (1 %). | **Não** no gráfico (V18); só na frase. | Sim: "1,3333 … erra 25,0 % (para menos)". | Erro em % em escala log com faixa de 1 %. |
| W6 | Redundante com o bullet "Logo acima do centro" (V23). | Sim: marcador sobre a curva e três referências. | Sim: "erra 241 %", "erra 71 %". | Modo "z em cm, R oculto" para treinar o P38 (V22). |

---

## 5. Aplicações reais e ordens de grandeza que faltam

Onde o guia dá um número sem referência ou onde uma aplicação de engenharia caberia. As contas são minhas, com as constantes do próprio guia.

1. **Aquecimento / P81: a carga que a esfera exigiria.** O guia nunca diz o tamanho. q = W/E = 4,4/150 ≈ 0,029 C. Referência: um balão esfregado tem alguns nC, ou seja, 7 ordens de grandeza menos. Para a esfera de enxofre (2,07 g/cm³, 450 g, raio ≈ 3,7 cm), o campo na superfície seria kq/R² ≈ 2 × 10¹¹ N/C, uns 60 mil vezes a ruptura do ar. Essa conta é a resposta do P81(b) e valia como "punchline" na Dica 4.
2. **Régua de ordens de grandeza do campo (Degrau 1).** A ficha tem 150, 10⁴, 3 × 10⁶ e 5 × 10¹¹ N/C enterrados numa célula. Uma régua logarítmica horizontal (tempo bom, 1 nC a 3 cm, ruptura do ar, átomo de H) ensinaria isso em um olhar. Junto: 3 × 10⁶ N/C = 3 kV por mm de ar.
3. **Escala da carga.** Só aparecem "alguns nC" (balão) e 4,23 fC (P31). Faltam µC (placa ou fita carregada) e ~15 C (um relâmpago). No pré-teste 1, 4,23 fC = ~26 mil elétrons (já está na ficha do λ) poderia vir junto.
4. **Degrau 2 (molécula, capacitor, cabo)** e **Degrau 3 (placa de circuito):** são citados sem número. Exemplo para o Degrau 3: 5 V entre duas trilhas a 0,2 mm dá ~2,5 × 10⁴ N/C, 100 vezes abaixo da ruptura; é a ordem de grandeza com que um projetista de placa convive. (Atenção: E = V/d é do Cap. 24; usar só como pergunta de curiosidade.)
5. **P15:** a resposta é de uns 160 N/C com três partículas elementares a 6 µm. É da mesma ordem dos 150 N/C do ar em tempo bom (do Aquecimento). Vale um comentário depois da resposta.
6. **Degrau 5 (fio ou trilha):** linha de transmissão de alta tensão dá campo no solo de uns 10⁴ N/C, 300 vezes abaixo da ruptura. Dá sentido a "de longe, a barra vira um ponto" (o fio visto da rua) e ao "D ≳ 5L".
7. **Degrau 6 (σ):** σ = 5,3 µC/m² do Problema 34 e da revisão rev-3 dá Eₘ = 3 × 10⁵ N/C, **exatamente 10 % da ruptura do ar**: σ máximo no ar ≈ 2ε₀ × 3 × 10⁶ ≈ 5,3 × 10⁻⁵ C/m². É um número bonito que o guia deixa passar, e ancora "placa de capacitor" e "tambor de copiadora" (ambos citados no "Por que isso existe").
8. **Degrau 4:** só tem a referência de λ (10⁻⁸ C/m para a barra de plástico). Não vi aplicação natural de arco; é melhor não forçar uma.
9. **Os widgets** dão resultado em unidades normalizadas (kq/cm², kQ/r², Eₘ). Só o W1 dá N/C. Um rótulo "com q = 2 nC, isso é ___ N/C" no W3 e no W4 faria a ponte.

---

## 6. Onde o texto está denso e uma figura resolveria; onde falta "desenhe você"

**Denso, precisa de figura**
- Regra dos quatro quadrantes (V11).
- Método do elemento em seis passos (Degrau 4): é uma lista. Uma figura com os seis passos numerados sobre o arco (1 dq e θ; 2 ds = r dθ; 3 dE de cada um; 4 par simétrico; 5 limites ±φ/2; 6 sentido) substituiria a lista. A Fig. 4-1 faz 1, 3 e 4, mas não 5 (V16).
- "A ficha das grandezas novas" (Degraus 1 e 4): tabela com 5 colunas e texto corrido; no celular vira cartões de 5 linhas por grandeza (`celular-d1`, `celular-d4`). Um ícone pequeno por grandeza e a régua de V32/seção 5 ajudariam.
- "Para cancelar de verdade, falta o módulo empatar" (Degrau 2): sem figura. Um "balança" desenhado (1 nC a 1 cm contra 4 nC a 2 cm, mesmas setas) tornaria o 4:1 óbvio.
- A tabela "Equações do capítulo" na Síntese (`desktop-sintese`): oito linhas de fórmulas sem o desenho da geometria de cada uma (arco, barra, anel, disco, placa).
- "De longe, a barra vira um ponto" (D = a + L/2): sem figura do D (V20).

**Onde faltam "desenhe você" e faltam moldes**
- Só a Fig. 2-3 vem em branco para o aluno desenhar. Faltaria o mesmo nos degraus 3 e 4 (um par de cargas, P, "desenhe E₁ e E₂ e o total" com o gabarito sob botão) e nos problemas (as dicas dizem "já desenhou as setas?", mas nenhuma figura oferece o molde).
- P81 e Millikan sem diagrama de forças (V28).
- A regra "a seta nasce em P" é desenhada com o ponto P nas Figs. 1-1(b), 2-1 e 3-1, mas não na Fig. 1-2, justamente a que o Erro comum do Degrau 1 cita (V03).

---

## 7. Perguntas ao Professor

1. **Professor, no P8 eu desenhei as quatro setas e q₁ cancela q₂ (5e a d, lados opostos), e q₃ cancela q₄ (3e a d contra 12e a 2d, do mesmo lado). Deu zero. É para dar zero mesmo? Por que o enunciado pergunta o módulo, e o que eu faria se a q₄ estivesse do outro lado da figura?**
2. **Professor, na Fig. 4-3 o "120°" está entre o tracejado de cima e o eixo. Esse ângulo é o arco inteiro ou só a metade de cima? Por que o limite da integral é ±60° se o desenho parece mostrar 120° naquele canto?**
3. **Professor, na Fig. 4-1 a seta de cima é dE′, que pertence ao pedaço de baixo (dq′), e a de baixo é dE, do pedaço de cima. Por que não rotular cada seta junto do pedaço que a cria? Posso desenhar cada dE ao longo da reta do pedaço até P, apontando para longe do pedaço, e ficar com isso?**
4. **Professor, no P31 a letra "a" aparece duas vezes: 12,0 cm da extremidade em (b) e 50 m do centro em (d) e (e). Em (d) eu uso kq/(a(a+L)) com a = 50 m, ou a = 50 − L/2? Quanto isso muda o número, e o que a figura quer que eu entenda?**
5. **Professor, no W5 a curva fica colada na linha de 1 já em D = 3L. Como eu enxergo o "1 %" no gráfico? O gráfico serve para quê além de me dar o ponto D = 1L, onde o erro é grande?**
6. **Professor, o P38 mostra E/Eₘ contra z em cm, e o W6 mostra contra z/R. Eu só descubro R no fim. Por que posso usar o ponto "0,5Eₘ em z/R = 1/√3" se R é justamente a incógnita?**
7. **Professor, "1 nC a 1 cm e 4 nC a 2 cm" aparece na previsão do W2, na regra de cancelamento, no "Agora você completa" do Degrau 2 e (3e contra 12e a 2d) no P8. É coincidência ou é a ideia? Se for a ideia, como eu reconheço isso numa prova em que ninguém avisa?**

---

## 8. O que funcionou (não remover na versão 2)

- **Fig. 2-1 (quatro casos numa reta):** rótulo em cada linha, seta nascendo em P, vermelho/azul/âmbar corretos, uma imagem substitui a regra de sinais.
- **Fig. 2-3 e Fig. 3-3 (sem setas e sem sinais):** o aluno completa. Cargas em cinza quando o sinal é uma decisão do aluno.
- **Fig. 3-1 (3-4-5 desenhado com 3,0, 4,0, 5,0 cm):** a figura é o exemplo resolvido; componentes x tracejadas e E em roxo.
- **Fig. 5-2 (área sob 1/x²):** liga a integral ao desenho e à ideia de "perto pesa mais".
- **Pergunta 9 e Pergunta 11 (checkpoints):** objetos nas proporções certas (R, 2R, anel de R a 2R) e seis arranjos de arco bem distinguíveis no desktop.
- **Figuras das questões reconstruídas:** P8, P9, P15, P26, P29 e P38 batem com os enunciados e estão em escala; o P38 foi conferido em quatro pontos da curva com erro < 1 %, e os cruzamentos de grade são nítidos também no tema escuro (`escuro-p38`).
- **W4:** seta tracejada (carga toda num ponto) contra seta roxa (arco real), mais a frase "desconto dos empurrões laterais: 5 %". É a melhor ligação figura-fórmula do guia.
- **W5 e W6, leituras numéricas:** "erra 25,0 % (para menos)", "erra 241 %", "erra 71 %" respondem a "quão ruim é aproximar?" com um número.
- **W6, normalização z/R:** uma só curva para todos os discos; é a ideia de que o P38 depende.
- **Fluxo previsão → widget → confirmação** (opção em verde, "Certo.", explicação curta) e o aviso de que o widget fica borrado até responder.
- **Tema escuro:** vermelho vira salmão, azul vira azul-claro, âmbar e roxo clareiam; os símbolos "+" e "−" dentro das cargas dão codificação redundante, que ajuda quem confunde vermelho e azul.
- **Aquecimento (Fig. 0-1 e a pergunta-gancho):** 150 N/C "tempo bom", 4,4 N = ~450 g. Dá corpo ao número.
- **Ficha "Valores reais":** átomo de H a 5 × 10¹¹ N/C e "170 mil vezes a ruptura do ar", barra do P31 com "uns 26 mil elétrons em 8 cm".
- **"Onde a analogia quebra":** caixa tracejada curta, honesta, depois de cada analogia.
- **Síntese em cartões com "não":** ao ver o desenho em fila, o aluno percebe a escolha da ferramenta.
