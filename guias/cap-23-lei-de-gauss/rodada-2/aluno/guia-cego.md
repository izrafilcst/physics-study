# Guia (cópia cega para alunos-agente)

Este arquivo é o texto que a página mostra, na mesma ordem. As figuras aparecem como [FIGURA: descrição]; as capturas de tela estão em `rodada-1/telas/`. Perguntas e campos de resposta estão marcados; a conferência de cada um está em `conferir/<id>.md`, e a ajuda das questões em `ajuda/<Q>-<n>.md`.

Halliday, Fundamentos de Física, vol. 3 — Capítulo 23

# Lei de Gauss

Uma subida em sete degraus, do "o que é fluxo?" até resolver sozinho os Problemas 5, 24, 29, 39, 52, 53 e 76.

Tempo: cerca de 2 h nos degraus e 1 h 30 min nas questões. Faça em duas ou três sessões.

## Como usar este guia
- Suba na ordem: cada degrau só usa o que veio antes. Responda às perguntas antes de ver a resposta.
- Nas questões, tente sozinho primeiro; se travar, abra a ajuda um nível por vez.
- Seu progresso fica salvo neste navegador. Passe para o degrau seguinte quando acertar 2 de 3 no checkpoint.

## Mapa da subida

Cada degrau destrava as questões marcadas em cima dele. Toque num degrau para ir até ele.
- Degrau 0: Aquecimento
- Degrau 1: Fluxo
- Degrau 2: Lei de Gauss (destrava P5)
- Degrau 3: Esferas (destrava P52)
- Degrau 4: Cascas de cebola (destrava P53)
- Degrau 5: Cilindros (destrava P24, P76)
- Degrau 6: Condutores (destrava P29)
- Degrau 7: Placas (destrava P39)

Depois dos degraus: o resto do capítulo em 2 minutos, as questões, dúvidas da turma, síntese e revisão intercalada.

## Aquecimento
10 min · uma pergunta para guardar e seis para checar a base

### Pesar a carga de um planeta com um número só

No chão, em dia de tempo bom, o ar tem um campo elétrico de uns 150 N/C apontando para baixo, para o chão (você viu isso no Problema 81 do Cap. 22). Em quase todo o planeta ele tem esse mesmo valor.

A Terra tem raio de 6 370 km. Só com esses dois números, sem medir mais nada, dá para descobrir a carga total da Terra?

[FIGURA: A Terra como um círculo azul-esverdeado. Setas âmbar curtas, em toda a volta, apontam para dentro, para a superfície: o campo de 150 N/C para baixo. Um círculo tracejado verde, um pouco maior que a Terra, é uma superfície imaginária em volta do planeta.]

Figura 0-1. O campo de "tempo bom" aponta para o chão em toda a volta da Terra.

**[PERGUNTA gancho]** Seu palpite (não vale nota; a resposta aparece no Degrau 3):
   a) Não: precisaria medir o campo dentro da Terra, ponto por ponto.
   b) Sim: cerca de −1 C. A Terra é quase neutra.
   c) Sim: cerca de −700 mil coulombs.
   d) Não: a Terra é neutra; esse campo vem das nuvens.
   (Palpite: não há resposta certa agora; anote o seu. A resposta vem no Degrau 3.)

### Teste rápido da base

Seis perguntas, uma por ferramenta que o capítulo usa. Errou? Abre uma mini-revisão logo abaixo.

**[PERGUNTA pre1]** 1. Prefixos. O Problema 53 fala em 7,78 fC e 14,1 pC/m³. Quanto é 1 fC (femtocoulomb) em coulombs?
   a) \(10^{-12}\) C
   b) \(10^{-15}\) C
   c) \(10^{-9}\) C
   d) \(10^{-6}\) C
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre1.md`.

**[PERGUNTA pre2]** 2. Produto escalar. Dois vetores de módulos 5 e 2 fazem um ângulo de 60° entre si. O produto escalar deles vale:
   a) 10
   b) 8,66
   c) 5
   d) 0
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre2.md`.

**[PERGUNTA pre3]** 3. Áreas. A área de uma esfera de raio r e a área lateral (só a parede, sem as tampas) de um cilindro de raio r e altura h são:
   a) \(4\pi r^2\) e \(2\pi r h\)
   b) \(\pi r^2\) e \(2\pi r h\)
   c) \(\tfrac43\pi r^3\) e \(\pi r^2 h\)
   d) \(4\pi r^2\) e \(\pi r^2 h\)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre3.md`.

**[PERGUNTA pre4]** 4. Campo de uma carga (Cap. 22). A 2 cm de uma partícula carregada, o campo vale 800 N/C. A 4 cm, ele vale:
   a) 400 N/C
   b) 3 200 N/C
   c) 800 N/C
   d) 200 N/C
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre4.md`.

**[PERGUNTA pre5]** 5. Bolinha no fio (Cap. 21). Uma bolinha de peso mg está parada, pendurada num fio que faz um ângulo θ com a vertical, empurrada por uma força horizontal F. Então:
   a) \(F = mg\sin\theta\)
   b) \(F = mg\cos\theta\)
   c) \(F = mg\tan\theta\)
   d) \(F = mg/\tan\theta\)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre5.md`.

**[PERGUNTA pre6]** 6. Integral de potência. Quanto vale \(\displaystyle\int_0^{R} r^3\,dr\)?
   a) \(3R^2\)
   b) \(\dfrac{R^4}{4}\)
   c) \(\dfrac{R^3}{3}\)
   d) \(R^4\)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre6.md`.

## Fluxo
12 min · a base de todas as questões

Por que isso existe. A lei de Gauss descobre a carga escondida dentro de uma superfície medindo quanto campo atravessa essa superfície. Esse "quanto atravessa" se chama fluxo. É a mesma conta de quanto sol bate num painel solar inclinado: um painel deitado de frente para o sol pega tudo; de lado, nada.

### A ideia: chuva numa janela

Chuva caindo reta. Uma claraboia (janela deitada) pega toda a chuva que cai sobre a área dela. Incline a janela e ela pega menos. Ponha a janela em pé e a chuva passa rente ao vidro: não entra nada.

O que manda não é a área da janela, e sim a área que a chuva enxerga. A conta é: intensidade da chuva × área × cos θ, onde θ é o ângulo entre a chuva e a reta perpendicular à janela.

[FIGURA: Três janelas na chuva vertical. À esquerda, janela horizontal: todas as gotas acertam. No meio, janela inclinada a 50 graus: só uma parte das gotas acerta (cosseno de 50 graus, cerca de 64 por cento). À direita, janela vertical: as gotas passam rente e nenhuma acerta. Em cada janela, uma seta preta perpendicular a ela marca a normal.]

Figura 1-1. Mesma janela, mesma chuva: o que muda é o ângulo θ entre a chuva e a normal da janela.
Onde a analogia quebra. (1) A chuva é água que se move; o campo elétrico não "escoa", nada atravessa a superfície de verdade. Fluxo é só uma conta (campo × área × cosseno). (2) A chuva só vem de cima; o campo pode vir de qualquer lado, e aí o sinal do fluxo passa a importar (logo abaixo).

### A conta: vetor área e cosseno

Para não ter de falar "a reta perpendicular à superfície" toda hora, o livro cria o vetor área \(\vec A\): perpendicular à superfície (é a normal), com módulo igual à área.

Num campo uniforme e numa superfície plana, o fluxo elétrico é o produto escalar:

[FIGURA: Uma placa plana em perspectiva. Do centro sai uma seta preta vertical, o vetor área, perpendicular à placa. Uma seta âmbar, o campo E, sai do mesmo ponto inclinada, fazendo um ângulo theta com a normal. Uma linha tracejada leva a ponta de E até a normal: a parte de E ao longo da normal vale E cos theta.]

Figura 1-2. Só a parte de E ao longo da normal (E cos θ) atravessa a placa.
\[\Phi = \vec E\cdot\vec A = E\,A\cos\theta\qquad(\mathrm{N\cdot m^2/C})\]Eq. 23-3

Se o campo varia de ponto a ponto, ou a superfície é curva, você corta a superfície em quadradinhos \(d\vec A\), faz a mesma conta em cada um e soma tudo: \(\Phi = \int \vec E\cdot d\vec A\).

▸ [recolhido, abre ao clicar] Ver de onde vem a integral
   Num quadradinho pequeno, o campo é praticamente uniforme e a superfície é praticamente plana. Então o fluxo dele é \(\Delta\Phi = \vec E\cdot\Delta\vec A\). O fluxo total é a soma: \(\Phi \approx \sum \vec E\cdot\Delta\vec A\). Encolhendo os quadradinhos até \(d\vec A\), a soma vira a integral (Eq. 23-2). Nas questões deste guia você quase nunca vai integrar de verdade: a simetria transforma a integral em "E × área".

### Superfície fechada: o sinal conta

[FIGURA: Uma superfície fechada de forma irregular. Três pontos marcados. No ponto 1, em cima à direita, a normal aponta para fora e o campo também aponta para fora: fluxo positivo. No ponto 2, à esquerda, a normal aponta para fora e o campo aponta para dentro: fluxo negativo. No ponto 3, embaixo, o campo é paralelo à superfície: fluxo zero.]

Figura 1-3. Setas pretas: normais (sempre para fora). Setas âmbar: campo.

Numa superfície fechada (uma bola, uma caixa, uma "batata"), a regra é: a normal aponta sempre para fora. Então:
- campo saindo (θ < 90°): fluxo positivo;
- campo entrando (θ > 90°): fluxo negativo;
- campo rasante (θ = 90°): fluxo zero.

O fluxo total é a soma de tudo, com sinais: \(\Phi = \oint \vec E\cdot d\vec A\) (Eq. 23-4). O círculo na integral quer dizer "na superfície fechada inteira".

### Ficha das grandezas novas
| Grandeza | O que é e unidade | Valores reais | Se ela aumenta… | Armadilha |
| Φ (fluxo) | quanto campo atravessa uma superfície; N·m²/C; é um número com sinal, não um vetor | um próton cercado por qualquer superfície: 1,8 × 10⁻⁸; uma carga de 1 µC: 1,1 × 10⁵; a esfera em volta da Terra: −7,6 × 10¹⁶ | mais campo atravessa (ou o campo é mais forte, ou a área maior, ou mais de frente) | fluxo zero não quer dizer campo zero: pode entrar tanto quanto sai |
| \(\vec A\) (vetor área) | vetor perpendicular à superfície, com módulo = área; m² | uma folha A4: 0,062 m² (deitada no campo de tempo bom, Φ ≈ 9 N·m²/C); um painel solar de casa: uns 2 m² | o fluxo cresce na mesma proporção | numa superfície fechada, sempre para fora; numa aberta, o enunciado diz o lado |
| θ | ângulo entre \(\vec E\) e a normal; de 0° a 180° | 0° (de frente), 90° (rasante), 180° (de frente, mas entrando) | cos θ cai: de +1 (0°) a 0 (90°) a −1 (180°) | não é o ângulo com a superfície: esse dá sen no lugar de cos |

### Experimente: girar um quadrado no campo

**[PERGUNTA prev-w1]** Antes de mexer: você vai girar um quadrado num campo uniforme. Quando a normal do quadrado fica a 90° do campo, o fluxo…
   a) é máximo
   b) é negativo
   c) é zero
   d) vale metade do máximo
   (Previsão antes do widget w1. Responda, depois abra conferir/prev-w1.md.)

[WIDGET INTERATIVO — W1 — Quadrado girando num campo uniforme] Linhas de campo horizontais apontando para a direita. Um quadrado visto de lado (um segmento) gira em torno do centro; sua normal é uma seta preta. As linhas que atravessam o quadrado ficam destacadas em âmbar.
   Controles: Ângulo θ entre o campo e a normal (graus):
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: Problema 1 do livro

Um quadrado de 3,2 mm de lado está num campo uniforme de 1 800 N/C. As linhas de campo fazem 35° com a normal. Tome a normal "para fora", como se o quadrado fosse a tampa de uma caixa. Qual é o fluxo?

[FIGURA: Problema 1 visto de lado. O quadrado é um segmento horizontal. A normal aponta para cima. As linhas de campo descem da direita para a esquerda, atravessando a tampa de cima para baixo, a 35 graus da vertical.]

Figura 1-4. Problema 1 (reconstruída a partir do PDF, Fig. 23-30), vista de lado.

Entender A = (3,2 × 10⁻³ m)² = 1,02 × 10⁻⁵ m²; E = 1 800 N/C. As linhas descem e atravessam a tampa de fora para dentro.

Modelar Superfície plana, campo uniforme: \(\Phi = EA\cos\theta\), com θ entre \(\vec E\) e a normal.

Resolver em símbolos O 35° da figura é entre a normal e a reta das linhas. Mas \(\vec E\) aponta para baixo e a normal para cima: o ângulo entre os dois vetores é θ = 180° − 35° = 145°.

▸ [recolhido, abre ao clicar] Por que 145° e não 35°?
   O cosseno precisa do ângulo entre os dois vetores, cada um com seu sentido. A normal aponta para cima, \(\vec E\) aponta para baixo: eles estão "quase opostos". cos 145° = −0,82 diz exatamente isso: o campo atravessa contra a normal, ou seja, entra na caixa.

Calcular \(\Phi = (1800)(1{,}02\times10^{-5})\cos145^\circ = -0{,}015\) N·m²/C.

Verificar Sinal negativo: o campo entra pela tampa. Gabarito do livro: −0,015 N·m²/C. Ordem de grandeza: o quadrado é minúsculo (10⁻⁵ m²), então o fluxo é pequeno.

### Agora você completa: Problema 3 do livro

O cubo da Fig. 23-31 tem 1,40 m de aresta. Ache o fluxo pela face direita (a que tem normal \(+\hat\jmath\)) para cada campo uniforme abaixo, em N/C. Comece pela área da face: (1,40 m)² = 1,96 m². Em componentes, \(\vec E\cdot\vec A = E_xA_x + E_yA_y + E_zA_z\), e aqui \(\vec A = (1{,}96\ \text{m}^2)\,\hat\jmath\).

[FIGURA: Cubo com eixos: z para cima, y para a direita, x saindo do papel em diagonal para baixo e para a esquerda. A face da direita, perpendicular ao eixo y, está destacada, com a normal j apontando para a direita.]

Figura 1-5. Cubo do Problema 3 (Fig. 23-31, reconstruída do PDF).

**[CAMPO lac1-1]** (a) E = 6,00 î: Φ = ______ N·m²/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac1-1.md`. A página aceita tolerância de ±0.01 N·m²/C.

**[CAMPO lac1-2]** (b) E = −2,00 ĵ: Φ = ______ N·m²/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac1-2.md`. A página aceita tolerância de 2 %.

**[CAMPO lac1-3]** (c) E = −3,00 î + 4,00 k̂: Φ = ______ N·m²/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac1-3.md`. A página aceita tolerância de ±0.01 N·m²/C.

**[CAMPO lac1-4]** (d) Fluxo total pelo cubo, em qualquer dos três casos: ______ N·m²/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac1-4.md`. A página aceita tolerância de ±0.01 N·m²/C.

### Erros comuns
- Muita gente usa o ângulo entre o campo e a superfície. Na verdade θ é com a normal, porque é a normal que diz "de frente". Se o enunciado der o ângulo com a superfície, use 90° menos ele.
- Muita gente pensa que fluxo é um vetor, porque nasce de dois vetores. Na verdade é um número (com sinal), porque o produto escalar de dois vetores é um número.
- Muita gente esquece o sinal. Na verdade, numa superfície fechada, campo entrando dá fluxo negativo, porque a normal aponta para fora e o cosseno fica negativo.
- Muita gente pensa que fluxo total zero quer dizer campo zero. Na verdade o Problema 3(d) tem campo diferente de zero e fluxo total zero, porque tudo o que entra por um lado sai pelo outro.

### Checkpoint do Degrau 1

[FIGURA: Teste 1 do livro: um cubo de faces com área A. Os eixos: x para a direita, y para cima, z saindo do papel em diagonal para baixo e para a esquerda. O campo E, uniforme, aponta no sentido positivo de z, para fora do papel. A face da frente é a que está virada para quem olha.]

Figura do Teste 1 do livro (reconstruída do PDF). O campo aponta em +z, saindo do papel; a face da frente está virada para você.

**[PERGUNTA ck1-1]** (Teste 1b) Qual é o fluxo pela face traseira do cubo?
   a) +EA
   b) 0
   c) +EA, igual ao da frente
   d) −EA
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck1-1.md`.

**[PERGUNTA ck1-2]** (Teste 1d) E o fluxo pelo cubo inteiro?
   a) 0
   b) 2EA
   c) EA
   d) −EA
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck1-2.md`.

**[PERGUNTA ck1-3]** (Pergunta 1a do livro) O vetor área de uma superfície é \(\vec A = (2\hat\imath + 3\hat\jmath)\) m², e o campo é \(\vec E = 4\hat\imath\) N/C. O fluxo é:
   a) 20 N·m²/C
   b) 12 N·m²/C
   c) 8 N·m²/C
   d) 14,4 N·m²/C
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck1-3.md`.

Habilidades desbloqueadas: fluxo com cosseno e com componentes; sinal numa superfície fechada. Ainda nenhuma questão inteira: falta saber quanto fluxo uma carga produz. É o próximo degrau.

Onde isso volta: no Degrau 2, o fluxo por uma superfície fechada vira um detector de carga. No Cap. 30, o fluxo magnético \(\Phi_B = \int\vec B\cdot d\vec A\) usa exatamente a mesma conta, e é a variação dele que gera corrente num gerador.

## Lei de Gauss
15 min · destrava o Problema 5

Por que isso existe. Dá para saber quanta carga há dentro de uma caixa fechada sem abrir: basta somar o fluxo que atravessa as paredes. O livro compara com "descobrir o presente pelo papel de embrulho". É assim que um copo de Faraday (um copo metálico ligado a um medidor) mede a carga de um objeto posto dentro dele. E é a primeira das quatro equações de Maxwell.

### A ideia: um aspersor dentro de uma tela

Ponha um aspersor de jardim ligado dentro de uma tela fechada, de qualquer formato. Toda a água que ele joga atravessa a tela de dentro para fora. (Numa tela torta, um jato pode sair, entrar e sair de novo; o saldo é o mesmo.) Tela maior ou menor, redonda ou torta: a água que sai por segundo é a mesma.

Agora deixe chover lá fora. Cada gota que entra na tela por cima sai por baixo. Saldo da chuva: zero. Medindo só o saldo (sai − entra), você descobre a vazão do aspersor, não importa quanta chuva caia.
Onde a analogia quebra. (1) A água anda de verdade; o campo não anda (Degrau 1). (2) Carga negativa seria um "ralo" que puxa o campo para dentro; um aspersor não faz isso. (3) A chuva de fora muda o campo em cada ponto da superfície. O que ela não muda é o saldo. (4) A água sempre se conserva; o fluxo elétrico só não depende do tamanho da tela porque o campo cai exatamente com 1/r² (veja o "ver de onde vem" abaixo).

[FIGURA: Dois painéis. À esquerda, uma carga positiva dentro de uma superfície fechada: cada uma das 8 linhas que saem dela cruza a superfície uma vez, para fora (marcas verdes). À direita, uma carga positiva do lado de fora: as linhas que acertam a superfície entram (marca vermelha) e depois saem (marca verde). Saldo zero.]

Figura 2-1. Verde: a linha sai (+1). Vermelho: entra (−1). Só a carga de dentro deixa saldo. O número de linhas desenhadas é arbitrário (aqui 8; no W2, 12): o que importa é a proporção.

Com linhas de campo é igual. As linhas nascem nas cargas positivas, em número proporcional à carga. Uma carga dentro da superfície tem todas as suas linhas cruzando a superfície para fora. Uma carga fora tem cada linha entrando e saindo.

Então o fluxo total só "enxerga" a carga de dentro. Essa é a lei de Gauss.
\[\varepsilon_0\,\Phi = q_{env}\qquad\text{ou}\qquad \varepsilon_0\oint\vec E\cdot d\vec A = q_{env}\]Eqs. 23-6 e 23-7
- \(q_{env}\) é a carga envolvida: a soma algébrica (com sinais) do que está dentro. Se for positiva, o fluxo é para fora; negativa, para dentro.
- O \(\vec E\) da integral é o campo total, das cargas de dentro e de fora. As de fora só não mudam o saldo.
- A lei vale sempre. Se houver vidro, óleo ou plástico dentro, q_env inclui a carga que o material acumula ao se polarizar; o Cap. 25 mostra como contar isso.

▸ [recolhido, abre ao clicar] Ver de onde vem (a lei de Coulomb disfarçada)
   Envolva uma carga pontual q com uma esfera de raio r centrada nela. Pelo Cap. 22, em toda a esfera \(E = \dfrac{q}{4\pi\varepsilon_0 r^2}\), apontando para fora, perpendicular à superfície. Então \(\Phi = E \cdot 4\pi r^2 = \dfrac{q}{4\pi\varepsilon_0 r^2}\cdot4\pi r^2 = \dfrac{q}{\varepsilon_0}\). O r² do campo cancela o r² da área: qualquer raio dá o mesmo fluxo. A lei de Gauss só funciona porque o campo cai exatamente com 1/r². E uma superfície de outra forma? Olhe da carga. Cada pedacinho da superfície tapa um cone fino de direções, com a ponta na carga. Se o pedacinho está mais longe, ele precisa ser maior para tapar o mesmo cone (área ∝ r²), mas o campo ali é mais fraco (∝ 1/r²): o fluxo pelo cone é o mesmo. Se está inclinado, a área cresce, mas o cos θ diminui na mesma proporção. Os cones de todas as direções juntos dão sempre q/ε₀, qualquer que seja a forma. E, como \(k = 1/(4\pi\varepsilon_0)\), as leis de Gauss e de Coulomb dizem a mesma coisa.

### Experimente: contar linhas

**[PERGUNTA prev-w2]** Antes de mexer: uma carga B, de fora, fica encostada na superfície gaussiana. O fluxo total pela superfície…
   a) aumenta muito
   b) fica negativo
   c) não muda
   d) depende da forma da superfície
   (Previsão antes do widget w2. Responda, depois abra conferir/prev-w2.md.)

[WIDGET INTERATIVO — W2 — Saldo de linhas numa superfície fechada] Uma superfície fechada tracejada, com a carga A dentro e a carga B, que pode ser movida. Doze linhas saem de cada carga. Cada cruzamento com a superfície é marcado em verde, se a linha sai, ou em vermelho, se entra.
   Controles: Posição da carga B (horizontal):; +−; círculoquadradobatata
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Truque da simetria: repartir o fluxo

A lei de Gauss dá o fluxo pela superfície inteira. Às vezes o problema pergunta por um pedaço dela. Se a superfície é feita de pedaços iguais, e uma rotação (ou reflexão) que deixa a carga no lugar leva cada pedaço no outro, cada pedaço leva a mesma fração do total. Sem essa simetria, não dá para repartir.

[FIGURA: Dois cubos. À esquerda, a carga está no centro do cubo e as seis faces têm a mesma cor: cada uma leva 1/6 do fluxo. À direita, a carga está perto da face da direita: essa face é mais escura, as outras mais claras, e não dá para repartir igual.]

Figura 2-2. Mais escuro = mais fluxo. Repartir por igual só vale se uma rotação leva cada face na outra sem tirar a carga do lugar.

### Ficha das grandezas novas
| Grandeza | O que é e unidade | Valores reais | Se ela aumenta… | Armadilha |
| \(q_{env}\) | soma, com sinais, das cargas dentro da superfície gaussiana; C | um próton: 1,6 × 10⁻¹⁹ C; esfera do Problema 53: 7,8 × 10⁻¹⁵ C; uma nuvem de tempestade: dezenas de coulombs | o fluxo total cresce na mesma proporção (Φ = q_env/ε₀) | fluxo zero não quer dizer "nada dentro": pode ter +q e −q |
| ε₀ | constante elétrica (permissividade do vácuo); C²/(N·m²) | 8,85 × 10⁻¹² (sempre o mesmo). \(k = 1/(4\pi\varepsilon_0) = 8{,}99\times10^9\) | é constante; num material (Cap. 25) o efeito é parecido com ε₀ maior: campo menor | dividir por ε₀ deixa números enormes: 1 µC dá 1,1 × 10⁵ N·m²/C |
| superfície gaussiana | superfície fechada e imaginária que você escolhe para aplicar a lei | uma esfera, um cubo, uma "lata"; pode atravessar objetos | o fluxo só muda se ela passar a envolver mais carga | ela não existe; não tem carga nem altera o campo |

### Exemplo resolvido: o fluxo pela metade de uma esfera

Uma carga q = 1,8 µC está no centro de uma esfera gaussiana. (a) Qual é o fluxo pela esfera inteira? (b) E só pela metade de cima?

[FIGURA: Esfera gaussiana tracejada com a carga positiva no centro. A metade de cima está destacada. Setas âmbar radiais saem da carga atravessando a esfera, igualmente para cima e para baixo.]

Figura 2-3. As duas metades estão na mesma posição em relação à carga.

Entender q = 1,8 × 10⁻⁶ C no centro. Incógnitas: Φ total e Φ da metade de cima.

Modelar Lei de Gauss na esfera inteira (que é fechada). A metade de cima não é fechada, então a lei não vale direto para ela: use a simetria.

Resolver em símbolos (a) \(\Phi = q/\varepsilon_0\). (b) As duas metades são iguais e estão na mesma posição em relação à carga: \(\Phi_{cima} = \Phi/2 = q/(2\varepsilon_0)\).

▸ [recolhido, abre ao clicar] Por que não posso usar a lei de Gauss direto na metade de cima?
   Porque a lei fala de superfícies fechadas. A metade de cima é uma tigela aberta: não envolve nada. Você precisa fechar a conta pela superfície inteira e depois repartir.

Calcular (a) \(\Phi = \dfrac{1{,}8\times10^{-6}}{8{,}85\times10^{-12}} = 2{,}0\times10^5\) N·m²/C. (b) \(1{,}0\times10^5\) N·m²/C.

Verificar O Problema 7 do livro pede o fluxo dessa mesma carga por um cubo de 55 cm: o gabarito é 2,0 × 10⁵ N·m²/C, igual. A forma não importa. E se a carga estivesse fora do centro? O total continuaria 2,0 × 10⁵, mas a metade mais próxima da carga levaria mais que a metade.

### Agora você completa: Problema 15 do livro

Uma carga +q está num vértice de um cubo gaussiano. Qual é o fluxo, em múltiplos de q/ε₀, (a) por uma das faces que contêm o vértice e (b) por uma das outras faces? Dica do método: monte 8 cubos iguais em volta do vértice. A carga fica no centro do cubão.

[FIGURA: Um cubo grande formado por 8 cubos pequenos, com a carga positiva no centro do cubo grande, que é um vértice de cada cubo pequeno. Um dos cubos pequenos, o original, está destacado.]

Figura 2-4. Com 8 cubos em volta do vértice, a carga fica no centro do cubão (desenho do guia).

**[CAMPO lac2-1]** Fração do fluxo total q/ε₀ que atravessa o cubo original: ______ (número puro)
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac2-1.md`. A página aceita tolerância de 2 %.

**[CAMPO lac2-2]** (a) Face que contém o vértice, em unidades de q/ε₀: ______ (número puro)
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac2-2.md`. A página aceita tolerância de ±0.001 (número puro).

**[CAMPO lac2-3]** (b) Uma das outras três faces, em unidades de q/ε₀: ______ (número puro)
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac2-3.md`. A página aceita tolerância de 2 %.

### Erros comuns
- Muita gente pensa que uma superfície gaussiana maior pega mais fluxo. Na verdade o fluxo só depende da carga envolvida, porque o campo cai com 1/r² e a área cresce com r²: um compensa o outro.
- Muita gente pensa que, como as cargas de fora não entram em q_env, elas não fazem campo na superfície. Na verdade fazem; só que o fluxo delas soma zero, porque cada linha que entra também sai.
- Muita gente aplica Φ = q_env/ε₀ a um pedaço aberto da superfície (uma face, uma tampa). Na verdade a lei vale só para a superfície fechada; para um pedaço, use simetria, porque um pedaço aberto não "envolve" nada.
- Muita gente pensa que a lei de Gauss sempre dá o campo. Na verdade ela sempre dá o fluxo; o campo só sai fácil quando há simetria (Degraus 3 a 7).

### Checkpoint do Degrau 2

**[PERGUNTA ck2-1]** (Teste 3 do livro) Um fluxo Φᵢ atravessa uma esfera gaussiana de raio r em volta de uma partícula carregada. Você troca a esfera por (a) uma esfera maior, (b) um cubo de lado r e (c) um cubo de lado 2r, sempre envolvendo a partícula. O novo fluxo é:
   a) maior em (a) e (c), menor em (b)
   b) igual a Φᵢ nos três casos
   c) menor em (a), porque longe o campo é mais fraco
   d) diferente nos cubos, porque o campo não é perpendicular às faces
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck2-1.md`.

(Teste 2 do livro, em forma de tabela, com números do guia.) Fluxo por face de três cubos gaussianos, em N·m²/C; + quer dizer que sai, − que entra.
| Cubo | frente | trás | cima | baixo | esquerda | direita |
| 1 | +5 | +7 | +2 | −7 | −4 | −3 |
| 2 | +10 | +3 | +5 | −3 | −4 | −6 |
| 3 | +2 | +5 | −6 | −8 | −7 | −5 |

**[PERGUNTA ck2-2]** Qual cubo envolve uma carga total negativa?
   a) o cubo 1
   b) o cubo 2
   c) o cubo 3
   d) nenhum
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck2-2.md`.

**[PERGUNTA ck2-3]** Uma carga +q está do lado de fora de um cubo gaussiano, bem perto de uma das faces. O fluxo total pelo cubo é:
   a) zero
   b) −q/ε₀, porque as linhas entram
   c) q/(6ε₀)
   d) depende da distância até a face
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck2-3.md`.

Dúvidas da turma deste degrau: por que a forma não importa? · e se o próton do P5 estivesse a d/4?

Habilidades desbloqueadas: lei de Gauss e o truque de repartir o fluxo por simetria. Você já consegue fazer o Problema 5.

Onde isso volta: nos Degraus 3 a 7 a mesma lei vai dar o campo, quando a simetria deixa E igual em toda a superfície. No Cap. 32, a lei de Gauss do magnetismo diz que o fluxo magnético por qualquer superfície fechada é zero: não existe "carga magnética" isolada.

## Esferas
18 min · destrava o Problema 52

Por que isso existe. No Cap. 22, o campo de uma esfera carregada seria uma integral tripla. Com a lei de Gauss e a simetria, sai em duas linhas. Serve para planetas, gotas de chuva carregadas, a cúpula de um gerador Van de Graaff e o núcleo de um átomo.

### Por que E é igual em toda a esfera gaussiana

Pegue um ponto P a uma distância r do centro e gire a esfera em torno da reta que liga o centro a P. A esfera fica igualzinha e P não sai do lugar, então o campo em P não pode mudar. Se \(\vec E\) tivesse uma parte "de lado" (perpendicular a essa reta), ela giraria junto: contradição. Sobra só a parte radial (para fora ou para o centro).

E, girando a esfera em torno do centro, qualquer ponto à distância r vai parar em qualquer outro: o módulo é o mesmo em toda a esfera de raio r. Vale para a esfera uniforme e também quando ρ só depende de r.

Isso transforma a integral da lei de Gauss numa multiplicação. Numa esfera gaussiana de raio r, centrada no mesmo ponto, \(\vec E\) é paralelo à normal e tem o mesmo valor em toda parte: \(\oint\vec E\cdot d\vec A = E\cdot4\pi r^2\).

### A receita (vale para os Degraus 3 a 7)
- Simetria: que forma tem o campo? (Aqui: radial, igual a uma mesma distância.)
- Superfície gaussiana pelo ponto onde você quer E, acompanhando a simetria. (Aqui: esfera de raio r.)
- Fluxo: só nas partes onde E é perpendicular e constante: Φ = E × (área dessas partes). (Aqui: \(E\cdot4\pi r^2\).) É essa simetria que permite, quando q_env = 0, concluir E = 0. Sem ela, fluxo zero não diz nada sobre E em cada ponto (Degrau 1).
- Carga envolvida: só o que está dentro da gaussiana. Desenhe e veja.
- Iguale e isole: \(\varepsilon_0 E\cdot(\text{área}) = q_{env}\). O sinal de q_env dá o sentido.

### Resolvendo o aquecimento: a carga da Terra
- Simetria: o campo é radial (para dentro) e, pela observação, igual em toda a volta.
- Gaussiana: esfera logo acima do chão, raio R = 6,37 × 10⁶ m.
- Fluxo: o campo entra, \(\Phi = -E\cdot4\pi R^2 = -150\times5{,}10\times10^{14} = -7{,}6\times10^{16}\) N·m²/C.
- Carga envolvida: a da Terra (a camada fina de ar dentro da esfera quase não conta).
- \(q_{env} = \varepsilon_0\Phi = -6{,}8\times10^5\) C.

Resposta do aquecimento: a terceira alternativa (cerca de −700 mil coulombs). As outras: não é preciso medir dentro da Terra, porque a lei de Gauss só pede o campo na superfície fechada; −1 C faria no chão um campo de 2 × 10⁻⁴ N/C, e não 150; e uma Terra neutra daria fluxo zero, mas o campo entra em toda a volta.

São uns 4 × 10²⁴ elétrons a mais. Espalhados pelo planeta, dão menos de um milhão por cm² de chão; cada cm² de superfície sólida tem uns 10¹⁵ átomos: um elétron extra para cada bilhão de átomos. Bastou um número porque supusemos o campo igual em toda a volta (isso é observação, não simetria: a Terra tem montanhas e nuvens). Sem essa hipótese, a lei de Gauss usaria a média de E sobre a esfera.

### A intuição: dentro de uma casca, o campo some

[FIGURA: Casca esférica carregada vista em corte. Um ponto P dentro dela, perto da parede direita. Dois cones estreitos saem de P: o da direita acerta um pedaço pequeno da casca, perto; o da esquerda acerta um pedaço grande, longe. Os empurrões dos dois pedaços se cancelam.]

Figura 3-1. O pedaço perto empurra mais forte (1/r²), mas é pequeno; o longe é fraco, mas grande (área ∝ r²). As duas setas âmbar, os empurrões dos dois pedaços, têm o mesmo tamanho: se cancelam.

Pegue um ponto P dentro de uma casca fina e uniforme, perto da parede da direita. Imagine um cone estreito de direções saindo de P para a direita e o cone oposto, para a esquerda (as linhas tracejadas da figura). O pedaço de parede que o cone da direita acerta está perto: empurra forte, mas é pequeno. O da esquerda é bem maior, mas está longe e empurra fraco.

O empurrão cai com 1/r² e a área do pedaço cresce com r²: os dois se cancelam exatamente. Pela lei de Gauss, é ainda mais rápido: uma esfera gaussiana dentro da casca não envolve carga, então Φ = 0; como a simetria deixa E igual e radial em toda a gaussiana, E = 0.

### Os resultados
Casca fina Eqs. 23-15 e 23-16\[E = 0\ \ (r<R),\qquad E = \frac{q}{4\pi\varepsilon_0 r^2}\ \ (r>R)\]
Esfera uniforme, dentro (r ≤ R) Eq. 23-20\[E = \frac{\rho\,r}{3\varepsilon_0} = \frac{q\,r}{4\pi\varepsilon_0R^3}\]

Fora de qualquer distribuição com simetria esférica, o campo é o de uma carga pontual com a carga toda no centro. Dentro, use a receita: o que muda de caso para caso é só o passo 4, a carga envolvida.

▸ [recolhido, abre ao clicar] Ver de onde vem a fórmula de dentro da esfera uniforme
   Esfera de raio R com carga q espalhada uniformemente: \(\rho = \dfrac{q}{\tfrac43\pi R^3}\). Uma esfera gaussiana de raio r < R envolve só o volume \(\tfrac43\pi r^3\): \(q_{env} = \rho\cdot\tfrac43\pi r^3 = q\,\dfrac{r^3}{R^3}\) (Eq. 23-19). Lei de Gauss: \(\varepsilon_0 E\cdot4\pi r^2 = \rho\cdot\tfrac43\pi r^3\), então \(E = \dfrac{\rho r}{3\varepsilon_0}\). Trocando ρ: \(E = \dfrac{q r}{4\pi\varepsilon_0R^3}\). Cresce em linha reta com r: no centro é zero, na superfície é máximo.

Regra geral do passo 4, para ρ uniforme: \(q_{env} = \rho\times\)(volume de material carregado que fica dentro da gaussiana). Se o objeto tem um buraco concêntrico, o buraco não conta. (Um buraco fora do centro quebra a simetria esférica, e a receita não serve mais.)

Isolante × condutor. Num isolante (plástico, vidro, borracha), a carga fica onde foi posta, até no meio do volume: é por isso que faz sentido falar em ρ. Num condutor (metal), a carga em excesso corre até a superfície (Degrau 6). Todos os objetos com ρ deste guia (esferas, cascas grossas, cilindros) são isolantes.

### Ficha das grandezas novas
| Grandeza | O que é e unidade | Valores reais | Se ela aumenta… | Armadilha |
| ρ | densidade volumétrica de carga: carga por m³; C/m³ | casca do Problema 52: 1,84 nC/m³; ar de uma nuvem de tempestade: da ordem de nC/m³; pó de chocolate num cano (Problema 60): 1,1 × 10⁻³ C/m³ | q_env e E crescem na mesma proporção | "ρ × volume" só vale se ρ for igual em todo o volume (se não, Degrau 4) |
| r | raio da sua esfera gaussiana: onde você quer o campo; m | o que o enunciado pedir: r = a/2, r = 1,5a, r = 3b… | dentro de uma esfera uniforme, E cresce (∝ r); fora, E cai (∝ 1/r²) | não confunda com R, a, b, que são do objeto e não mudam |
| R, a, b | raios do objeto (externo, interno); m | Terra: 6,37 × 10⁶ m; esfera do Problema 53: 5,60 cm | com a mesma carga, o campo na superfície cai (∝ 1/R²) | eles dizem onde estão as fronteiras entre as regiões |

### Experimente: esfera, casca grossa e casca fina

**[PERGUNTA prev-w3]** Antes de mexer: numa esfera maciça com carga uniforme, onde o campo é máximo?
   a) no centro
   b) em r = R/2
   c) na superfície
   d) não tem máximo: cresce sempre com r
   (Previsão antes do widget w3. Responda, depois abra conferir/prev-w3.md.)

[WIDGET INTERATIVO — W3 — Campo de uma esfera com cavidade] À esquerda, o corte de uma esfera de raio R com uma cavidade de raio a, e uma esfera gaussiana tracejada de raio r. À direita, o gráfico do campo E em função de r/R, com um marcador no r escolhido.
   Controles: Raio da cavidade a/R:; Raio da esfera gaussiana r/R:
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: esfera uniforme (Problema 78 do livro)

Uma carga de 6,00 pC está distribuída uniformemente numa esfera de raio 4,00 cm. Ache o módulo do campo (a) a 6,00 cm do centro e (b) a 3,00 cm do centro.

[FIGURA: Esfera carregada de raio 4 cm. Duas esferas gaussianas tracejadas: uma de raio 3 cm, dentro da esfera; outra de raio 6 cm, fora.]

Figura 3-2. Uma gaussiana para cada ponto pedido.

Entender q = 6,00 × 10⁻¹² C, R = 0,0400 m. Pontos: r = 0,0600 m (fora) e r = 0,0300 m (dentro).

Modelar Simetria esférica → receita com esfera gaussiana de raio r. Hipótese: ρ uniforme.

Resolver em símbolos (a) r > R: q_env = q, \(E = \dfrac{q}{4\pi\varepsilon_0 r^2}\). (b) r < R: \(q_{env} = q\,r^3/R^3\), \(E = \dfrac{q\,r}{4\pi\varepsilon_0R^3}\).

▸ [recolhido, abre ao clicar] Por que em (b) não posso usar kq/r²?
   Porque a esfera gaussiana de 3 cm não envolve a carga toda: a parte entre 3 e 4 cm fica fora, e carga de fora não entra na lei de Gauss. Só (3/4)³ = 42 % da carga está dentro.

Calcular (a) \(E = \dfrac{(8{,}99\times10^9)(6{,}00\times10^{-12})}{(0{,}0600)^2} = 15{,}0\) N/C. (b) \(E = \dfrac{(8{,}99\times10^9)(6{,}00\times10^{-12})(0{,}0300)}{(0{,}0400)^3} = 25{,}3\) N/C.

Verificar Na superfície daria 33,7 N/C, o máximo. Os dois valores são menores que isso, como manda o gráfico do W3. Resposta calculada pelo guia (o Problema 78 é par, sem gabarito oficial).

### Agora você completa: Problema 49 (b), (c) e (d) do livro

Uma esfera maciça de raio a = 2,00 cm tem carga uniforme q₁ = +5,00 fC. Em volta dela há uma casca metálica concêntrica que começa em b = 2,00a. Ache o módulo do campo em (b) r = a/2, (c) r = a e (d) r = 1,50a. Nos três pontos a casca fica fora da gaussiana; ela só vai importar no Degrau 6. Responda em mN/C (1 mN/C = 10⁻³ N/C).

[FIGURA: Esfera maciça carregada de raio a no centro. Em volta, uma casca metálica cinza que vai de 2a a 2,4a. Esferas gaussianas tracejadas em a/2, a e 1,5a.]

Figura 3-3. Problema 49 (desenho do guia a partir do enunciado).

**[CAMPO lac3-1]** (b) r = a/2: E = ______ mN/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac3-1.md`. A página aceita tolerância de 2 %.

**[CAMPO lac3-2]** (c) r = a: E = ______ mN/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac3-2.md`. A página aceita tolerância de 2 %.

**[CAMPO lac3-3]** (d) r = 1,50a: E = ______ mN/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac3-3.md`. A página aceita tolerância de 2 %.

### Erros comuns
- Muita gente usa \(kq/r^2\) dentro de uma esfera carregada. Na verdade, dentro vale \(kq_{env}/r^2\) com q_env menor que q, porque a carga entre r e R fica fora da gaussiana.
- Muita gente pensa que o campo é máximo no centro, "onde a carga está". Na verdade no centro E = 0, porque a carga está em volta, puxando igualmente para todos os lados.
- Muita gente esquece de tirar a cavidade numa casca grossa e usa \(\rho\cdot\tfrac43\pi r^3\). Na verdade o buraco não tem carga: \(q_{env} = \rho\cdot\tfrac43\pi(r^3 - a^3)\), porque só conta o material que está dentro da gaussiana.
- Muita gente troca r por R no meio da conta. Na verdade r é onde você mede e R é o tamanho do objeto, porque a gaussiana passa pelo ponto pedido, não pela superfície do objeto.
- Muita gente faz o erro inverso: usa a fórmula de dentro (\(kq\,r/R^3\) ou \(\rho(r^3-a^3)/3\varepsilon_0r^2\)) num ponto de fora. Na verdade, fora, q_env já é a carga total e para de crescer, então \(E = kq/r^2\), porque a gaussiana não envolve mais nenhum material novo.

### Checkpoint do Degrau 3

**[PERGUNTA ck3-1]** Uma casca esférica fina, de raio R, tem carga Q uniforme. O campo em r = R/2 vale:
   a) zero
   b) \(kQ/(R/2)^2\)
   c) \(kQ/R^2\)
   d) \(kQ/(2R^2)\)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck3-1.md`.

**[PERGUNTA ck3-2]** (Problema 65b do livro) Numa esfera maciça com carga uniforme, quanto vale E(R/2)/E(R)?
   a) 1/4
   b) 1/2
   c) 1/8
   d) 1
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck3-2.md`.

**[PERGUNTA ck3-3]** Uma casca grossa, de raio interno a e externo b, tem ρ uniforme. Para uma gaussiana de raio r com a < r < b, a carga envolvida é:
   a) \(\rho\cdot\tfrac43\pi r^3\)
   b) \(\rho\cdot\tfrac43\pi(b^3 - a^3)\)
   c) \(\rho\cdot4\pi r^2\)
   d) \(\rho\cdot\tfrac43\pi(r^3 - a^3)\)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck3-3.md`.

Dúvidas da turma deste degrau: por que radial? · quando q_env = 0 dá E = 0? · fora da casca grossa · onde está a carga positiva? · 300 V até a cabeça?

Habilidades desbloqueadas: a receita de 5 passos, cascas, esfera uniforme e casca grossa. Você já consegue fazer o Problema 52.

Onde isso volta: no Degrau 4, ρ deixa de ser uniforme. No Degrau 6, as cascas viram metálicas. Em Física 2, a gravidade dentro de um planeta uniforme cresce com r pela mesma conta (a "lei de Gauss da gravitação"). No Cap. 24, você vai calcular o potencial de uma esfera a partir desses campos.

## Cascas de cebola
15 min · destrava o Problema 53

Por que isso existe. Na vida real, a carga quase nunca é uniforme. A nuvem de elétrons de um átomo é mais densa perto do núcleo; a Terra é mais densa no centro (para a gravidade, a conta é a mesma). Quando ρ muda com r, "ρ × volume" dá errado. A saída é somar cascas finas, como as camadas de uma cebola.

### A ideia: descascar a cebola

Uma cebola é feita de camadas. Se cada camada é bem fina, a densidade dentro dela quase não muda: vale "ρ × volume da camada". Somando as camadas de dentro até o raio r, você tem toda a carga envolvida.

E o volume de uma camada fina? Descasque e abra: ela vira uma folha de área \(4\pi r^2\) e espessura dr. Volume: \(dV = 4\pi r^2\,dr\).
Onde a analogia quebra. A cebola tem camadas de verdade, com espessura fixa. Aqui as cascas são imaginárias e cada vez mais finas: no limite, a soma vira uma integral. E a ideia só funciona se ρ for a mesma em toda a casca, ou seja, se ρ depender só de r. Por que as cascas de fora de r não entram na conta? Pelo Degrau 3: dentro de uma casca uniforme, o campo dela é zero.

[FIGURA: À esquerda, uma esfera em corte, mais escura perto da borda. Uma casca de raio r e espessura dr está destacada. À direita, a mesma casca aberta como uma folha fina, de área 4 pi r ao quadrado e espessura dr.]

Figura 4-1. Uma casca fina, aberta, é uma folha: dV = 4πr² dr.

### A conta
\[dq = \rho(r')\,4\pi r'^2\,dr' \qquad\Longrightarrow\qquad q_{env}(r) = \int_0^{r}\rho(r')\,4\pi r'^2\,dr'\]

Depois, o passo 5 da receita é igual ao do Degrau 3: \(E = \dfrac{q_{env}(r)}{4\pi\varepsilon_0 r^2}\).

▸ [recolhido, abre ao clicar] Por que escrever r′ (r linha) dentro da integral?
   Porque são dois papéis diferentes. O r é o raio da sua esfera gaussiana: fixo durante a conta, é o limite de cima. O r′ percorre as cascas, de 0 até r. Se você usar a mesma letra para os dois, é fácil "tirar o r da integral" sem querer. Conferência: com ρ constante, \(\int_0^r\rho\,4\pi r'^2dr' = \rho\cdot\tfrac43\pi r^3\), o resultado do Degrau 3.

### Ficha das grandezas novas
| Grandeza | O que é e unidade | Valores reais | Se ela aumenta… | Armadilha |
| ρ(r) | densidade que muda com a distância ao centro; C/m³ | Problema 53: de 0 no centro a 14,1 pC/m³ na borda | mais carga nas cascas onde ela é maior | a constante tem unidade estranha: em ρ = Cr², C sai em C/m⁵ |
| dr′ | espessura de uma casca fina; m | "tão pequena quanto quiser": é o limite da soma | — | dr′ sozinho é um comprimento; volume é 4πr′² dr′ |
| q_env(r) | carga somada de 0 até r; C | começa em 0 no centro e chega a q na borda | sempre cresce com r enquanto há carga (ρ > 0) | para um ponto dentro, o limite é r, não R |

### Experimente: onde fica a carga

**[PERGUNTA prev-w4]** Antes de mexer: numa esfera com ρ ∝ r² (a carga se concentra perto da borda), que fração da carga total fica dentro de r = R/2?
   a) metade
   b) 1/8, igual à esfera uniforme
   c) mais que 1/8
   d) bem menos que 1/8
   (Previsão antes do widget w4. Responda, depois abra conferir/prev-w4.md.)

[WIDGET INTERATIVO — W4 — Cascas de cebola] À esquerda, o corte de uma esfera com anéis sombreados conforme a densidade, e uma esfera gaussiana tracejada de raio r. À direita, o gráfico de E dividido por E na superfície, em função de r/R, para o modelo escolhido; o outro modelo aparece tracejado.
   Controles: uniformeρ ∝ r²; Raio da esfera gaussiana r/R:
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: esfera com ρ = Cr²

Uma esfera isolante de raio R = 10,0 cm tem \(\rho = Cr^2\), com C = 5,0 µC/m⁵. Ache (a) a carga total, (b) E em r = R e (c) E em r = R/2.

Entender ρ cresce do centro (0) para a borda (C R² = 5,0 × 10⁻⁸ C/m³). Simetria esférica.

Modelar ρ não é uniforme → cascas: \(dq = \rho\,4\pi r'^2dr'\). Depois, a receita com a esfera gaussiana de raio r.

Resolver em símbolos \(q_{env}(r) = \displaystyle\int_0^r Cr'^2\cdot4\pi r'^2\,dr' = 4\pi C\int_0^r r'^4dr' = \frac{4\pi C r^5}{5}\). Então \(E = \dfrac{q_{env}}{4\pi\varepsilon_0r^2} = \dfrac{C r^3}{5\varepsilon_0}\) (dentro).

▸ [recolhido, abre ao clicar] Por que r′⁴ e não r′²?
   Porque entram dois r′²: um da densidade (Cr′²) e outro da área da casca (4πr′²). Esquecer o da área é o erro mais comum deste degrau.

Calcular (a) \(q = \dfrac{4\pi(5{,}0\times10^{-6})(0{,}100)^5}{5} = 1{,}26\times10^{-10}\) C. (b) \(E(R) = \dfrac{(5{,}0\times10^{-6})(0{,}100)^3}{5(8{,}85\times10^{-12})} = 113\) N/C. (c) \(E(R/2) = E(R)/2^3 = 14{,}1\) N/C.

Verificar Na superfície, a esfera tem de parecer uma carga pontual: \(kq/R^2 = 8{,}99\times10^9\times1{,}26\times10^{-10}/0{,}0100 = 113\) N/C. Bate. Se você tivesse usado "ρ da borda × volume", daria 2,09 × 10⁻¹⁰ C, 67 % a mais: a borda é a parte mais densa. Resposta calculada pelo guia.

[FIGURA: Gráfico de E em função de r para a esfera com rho igual a C r ao quadrado: dentro, E cresce como r ao cubo, devagar no começo e rápido perto da borda, até 113 N/C em r = R; fora, cai como 1 sobre r ao quadrado.]

Figura 4-2. E(r) do exemplo: r³ dentro (a carga está perto da borda), 1/r² fora, sem salto em R.

### Agora você completa: Problema 55 do livro (ao contrário)

Uma distribuição esférica de carga produz um campo radial, para fora, de módulo \(E = Kr^4\). Qual é ρ(r)? Aqui você anda pela receita ao contrário: do campo para a carga envolvida, e da carga envolvida para a densidade.

**[CAMPO lac4-1]** 1. Lei de Gauss: q_env(r) = 4πε₀ r² E = (?) × π ε₀ K r⁶. O (?) vale: ______ (número)
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac4-1.md`. A página aceita tolerância de 2 %.

**[CAMPO lac4-2]** 2. Carga numa casca fina: dq = (dq_env/dr) dr = (?) × π ε₀ K r⁵ dr. O (?) vale: ______ (número)
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac4-2.md`. A página aceita tolerância de 2 %.

**[CAMPO lac4-3]** 3. Como dq = ρ · 4πr² dr: ρ = (?) × ε₀ K r³. O (?) vale: ______ (número)
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac4-3.md`. A página aceita tolerância de 2 %.

### Erros comuns
- Muita gente faz \(q = \rho\cdot\tfrac43\pi R^3\) com ρ variável. Na verdade isso só vale com ρ constante, porque não existe "o" valor de ρ para pôr ali: cada casca tem o seu.
- Muita gente integra só \(\rho\,dr\). Na verdade o volume da casca é \(4\pi r^2dr\), porque uma casca é uma folha de área 4πr², não um fio.
- Muita gente usa a mesma letra r para o limite e para a variável, e tira o r da integral. Na verdade r′ varia e r é fixo, porque a gaussiana tem um raio só, mas as cascas dentro dela têm vários.
- Muita gente integra até R para um ponto de dentro. Na verdade o limite é r, porque as cascas entre r e R estão fora da gaussiana.

### Checkpoint do Degrau 4

**[PERGUNTA ck4-1]** Com \(\rho = Ar\), a carga de uma casca fina de raio r e espessura dr é:
   a) \(Ar\,dr\)
   b) \(Ar\cdot\tfrac43\pi r^3\)
   c) \(Ar\cdot4\pi r^2\,dr\)
   d) \(A\cdot4\pi r^2\,dr\)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck4-1.md`.

**[PERGUNTA ck4-2]** Numa esfera de raio R com \(\rho = Ar\), alguém calcula a carga total como \(AR\cdot\tfrac43\pi R^3\). O resultado sai:
   a) certo
   b) maior que o real
   c) menor que o real
   d) certo só se R = 1 m
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck4-2.md`.

**[PERGUNTA ck4-3]** Dentro de uma certa esfera, o campo tem o mesmo módulo em todo r. Então ρ é proporcional a:
   a) 1/r
   b) r
   c) uma constante
   d) 1/r²
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck4-3.md`.

Habilidades desbloqueadas: somar cascas com ρ(r) e andar pela receita nos dois sentidos. Você já consegue fazer o Problema 53.

Onde isso volta: num cilindro com ρ(r) (Problema 32 do livro), a fatia fina é uma casca cilíndrica, \(dV = 2\pi r L\,dr\). Em Física 1, o momento de inércia de uma esfera sai da mesma soma de cascas. No Cap. 26, a resistência de um fio de seção variável também é uma soma de fatias.

## Cilindros
15 min · destrava os Problemas 24 e 76

Por que isso existe. Fios, cabos coaxiais de internet e TV, o fio central de um contador Geiger, linhas de transmissão: tudo é comprido e redondo. Até o corpo de uma pessoa debaixo de uma nuvem de tempestade vira um "fio" na conta (exemplo abaixo). Para tudo isso, a superfície gaussiana é uma lata.

### A ideia: uma mangueira furada

Pense numa mangueira de jardim muito comprida, com furinhos iguais ao longo dela toda. A água sai de lado, nunca ao longo da mangueira. Envolva um trecho de comprimento h com uma lata sem tampa: toda a água daquele trecho sai pela parede da lata.

Uma lata mais larga tem parede maior (\(2\pi r h\)): a mesma água se espalha mais. Como a parede cresce só com r (e não com r², como a esfera), a água por m² cai com 1/r.
Onde a analogia quebra. (1) A mangueira de verdade tem fim, e perto das pontas a água sai torta. O fio "infinito" é uma aproximação: vale longe das pontas e a distâncias pequenas comparadas ao comprimento. (2) A água anda; o campo não. (3) Na conta, só conta a carga do trecho que está dentro da lata, λh, como só conta a água dos furos de dentro. (4) A mangueira tem água por dentro. Num tubo carregado (Problema 24), a carga fica na parede e, dentro dele, E = 0: o miolo é "seco". A analogia vale para a carga no eixo, não para o tubo.

[FIGURA: Um fio vertical carregado positivamente. Em volta, uma lata cilíndrica tracejada de raio r e altura h. Setas âmbar saem radialmente pela parede lateral. Nas tampas de cima e de baixo, as setas são paralelas à tampa: não atravessam.]

Figura 5-1. A lata gaussiana: fluxo só pela parede (área 2πrh); nas tampas, o campo é rasante.

### A receita com a lata
- Simetria: num fio longo e uniforme, \(\vec E\) não pode apontar ao longo do fio (para cima e para baixo é tudo igual). Também não pode girar em volta dele, como um redemoinho: espelhe o fio num plano que contém o eixo; o fio fica igual, mas um redemoinho trocaria de sentido. Sobra: radial, com o mesmo módulo a uma mesma distância r.
- Gaussiana: lata coaxial (com o mesmo eixo do fio), de raio r (passando pelo ponto) e altura h qualquer.
- Fluxo: parede: \(E\cdot2\pi rh\). Tampas: zero (rasante).
- Carga envolvida: o trecho de fio dentro da lata: \(q_{env} = \lambda h\).
- Iguale: \(\varepsilon_0E\cdot2\pi rh = \lambda h\).
\[E = \frac{\lambda}{2\pi\varepsilon_0\,r}\]Eq. 23-12

O h some: a altura da lata é escolha sua e não muda nada. O campo cai com 1/r. Para fora se λ > 0, para o fio se λ < 0. Vale também fora de qualquer cilindro longo com simetria cilíndrica, com λ = carga total por metro dentro da lata.
- Tubo de parede fina: dentro, a lata não envolve carga nenhuma, então E = 0. É o mesmo raciocínio da casca esférica.
- Cilindro maciço com ρ uniforme: o passo 4 usa a regra do Degrau 3: \(q_{env} = \rho\times\)(volume de material dentro da lata). O resto é igual.

### Experimente: por que 1/r², 1/r ou nada?

**[PERGUNTA prev-w5]** Antes de mexer: você se afasta de 1 m para 2 m de um fio muito longo carregado. O campo…
   a) cai para 1/4
   b) cai pela metade
   c) não muda
   d) dobra
   (Previsão antes do widget w5. Responda, depois abra conferir/prev-w5.md.)

[WIDGET INTERATIVO — W5 — Ponto, fio e placa] À esquerda, a superfície gaussiana da geometria escolhida, crescendo com a distância r. À direita, três curvas de E em função de r, normalizadas para valer 1 em r = 1 m: 1 sobre r ao quadrado (carga pontual), 1 sobre r (fio) e constante (placa). Um marcador mostra o valor atual.
   Controles: pontofioplaca; Distância r (m):
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Ficha das grandezas novas
| Grandeza | O que é e unidade | Valores reais | Se ela aumenta… | Armadilha |
| λ | carga por metro de comprimento; C/m | barra do Problema 29: 3,1 × 10⁻¹³ C/m; fio de um contador Geiger: 2 × 10⁻⁸ C/m; o corpo da mulher do exemplo abaixo: 1,3 × 10⁻⁵ C/m (perto da faísca) | E cresce na mesma proporção | se o problema dá a carga total Q e o comprimento L, λ = Q/L |
| h | altura da lata gaussiana; m | qualquer uma: você escolhe | fluxo e carga envolvida crescem juntos: E não muda | se h não sumiu da sua conta, tem erro |
| r | distância ao eixo (não ao centro de um ponto); m | Problema 24: R/2 e 2R, com R = 3,00 cm | fora: E cai com 1/r | é distância perpendicular ao eixo, medida na horizontal do desenho |

### Exemplo resolvido: a mulher na tempestade (Exemplo 23.06 do livro)

Uma nuvem de tempestade empurrou elétrons do corpo de uma mulher para o chão, deixando-a positiva (os cabelos dela se arrepiaram). Modele o corpo como um cilindro de altura L = 1,8 m e raio R = 0,10 m, com a carga Q uniforme. O ar sofre ruptura (vira condutor e sai faísca) quando E passa de 2,4 MN/C. Para que Q o ar em volta dela está a ponto de romper?

[FIGURA: Um cilindro vertical de 1,8 metro de altura e 0,10 metro de raio, carregado positivamente, representando o corpo. Setas de campo saem horizontalmente da superfície.]

Figura 5-2. O corpo como um cilindro (Fig. 23-16c do livro, simplificada).

Entender L = 1,8 m, R = 0,10 m, E crítico = 2,4 × 10⁶ N/C na superfície (r = R). Incógnita: Q. (O livro usa 2,4 × 10⁶ N/C aqui e 3 × 10⁶ N/C em outros lugares: a ruptura do ar depende da umidade e da pressão.)

Modelar R ≪ L, então, longe das pontas, o corpo parece um fio longo: \(E = \lambda/(2\pi\varepsilon_0 r)\) com λ = Q/L. Hipótese: carga uniforme ao longo do corpo.

Resolver em símbolos Na superfície, r = R: \(E_c = \dfrac{Q/L}{2\pi\varepsilon_0R}\), então \(Q = 2\pi\varepsilon_0 R L E_c\).

▸ [recolhido, abre ao clicar] Por que posso tratar um corpo de 1,8 m como "infinito"?
   Porque o ponto que importa está a 0,10 m do eixo, 18 vezes menos que o comprimento. Para quem está tão perto, as pontas estão "longe". O erro cresce perto da cabeça e dos pés.

Calcular \(Q = 2\pi(8{,}85\times10^{-12})(0{,}10)(1{,}8)(2{,}4\times10^6) = 2{,}4\times10^{-5}\) C = 24 µC.

Verificar Unidade: C²/(N·m²) × m × m × N/C = C. λ = 1,3 × 10⁻⁵ C/m, umas 600 vezes a do fio de um contador Geiger. E se R fosse 5 cm (um braço)? Com a mesma λ, o campo dobraria: partes finas do corpo (dedos, cabelo) chegam à ruptura primeiro.

### Agora você completa: Problema 31 do livro

Duas cascas cilíndricas longas, coaxiais, de paredes finas, têm raios de 3,0 cm e 6,0 cm. A interna tem λ₁ = +5,0 × 10⁻⁶ C/m e a externa λ₂ = −7,0 × 10⁻⁶ C/m. (O livro em português diz "3,0 e 6,0 m"; é erro de tradução: o gabarito só bate com cm.)

[FIGURA: Corte de duas cascas cilíndricas coaxiais: a interna, de 3 cm, positiva; a externa, de 6 cm, negativa. Dois pontos marcados: um a 4 cm do eixo, entre as cascas, e outro a 8 cm, fora das duas.]

Figura 5-3. Problema 31 (desenho do guia a partir do enunciado). Uma lata para cada ponto.

**[CAMPO lac5-1]** (a) r = 4,0 cm: E = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac5-1.md`. A página aceita tolerância de 3 %.

**[PERGUNTA lac5-2]** (b) O sentido do campo em r = 4,0 cm é:
   a) para fora (longe do eixo)
   b) para dentro (para o eixo)
   → Escolha ANTES de abrir `conferir/lac5-2.md`.

**[CAMPO lac5-3]** (c) r = 8,0 cm: E = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac5-3.md`. A página aceita tolerância de 2 %.

**[PERGUNTA lac5-4]** (d) O sentido do campo em r = 8,0 cm é:
   a) para fora (longe do eixo)
   b) para dentro (para o eixo)
   → Escolha ANTES de abrir `conferir/lac5-4.md`.

### Erros comuns
- Muita gente usa 1/r² para um fio. Na verdade é 1/r, porque a parede da lata cresce só com r, enquanto a esfera cresce com r².
- Muita gente põe fluxo nas tampas da lata. Na verdade é zero, porque o campo é radial e passa rente às tampas.
- Muita gente escreve \(q_{env} = \lambda r\) ou \(\lambda\cdot2\pi r\). Na verdade \(q_{env} = \lambda h\), porque λ é carga por metro de fio, e dentro da lata há h metros de fio.
- Muita gente pensa que dentro de um tubo carregado há campo "por estar cercado de carga". Na verdade é zero, porque uma lata dentro do tubo não envolve carga.

### Checkpoint do Degrau 5

**[PERGUNTA ck5-1]** Na lata gaussiana em volta de um fio longo, por que as tampas não têm fluxo?
   a) Porque o campo é zero nas tampas.
   b) Porque o campo é paralelo às tampas.
   c) Porque a área das tampas é pequena.
   d) Porque o fluxo de uma tampa cancela o da outra.
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck5-1.md`.

**[PERGUNTA ck5-2]** (Problema 25 do livro) Uma linha infinita de carga produz 4,5 × 10⁴ N/C a 2,0 m. A densidade linear de carga é:
   a) 0,80 µC/m
   b) 2,5 µC/m
   c) 5,0 µC/m
   d) 10 µC/m
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck5-2.md`.

**[PERGUNTA ck5-3]** A altura h da lata aparece no resultado final para E?
   a) Não: o fluxo e a carga envolvida crescem os dois com h.
   b) Sim: quanto maior h, maior E.
   c) Sim: E ∝ 1/h.
   d) Só se h for maior que r.
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck5-3.md`.

Dúvidas da turma deste degrau: por que o cilindro não é carga pontual? · quanto vale E em r = R?

Habilidades desbloqueadas: lata gaussiana, fio, tubo fino, cilindro maciço. Você já consegue fazer o Problema 24 e o Problema 76. O Problema 29 precisa ainda do Degrau 6.

Onde isso volta: no Degrau 6, as cascas coaxiais viram metálicas (Problema 29). No Cap. 25, o capacitor cilíndrico usa exatamente E = λ/(2πε₀r). No Cap. 29, o campo magnético de um fio com corrente também cai com 1/r, pela mesma ideia de simetria, mas com um laço circular no lugar da lata (lei de Ampère): lá o campo gira em volta do fio.

## Condutores
15 min · destrava o Problema 29

Por que isso existe. Metal blinda. Um carro atingido por um raio protege quem está dentro; a malha de um cabo coaxial impede que ruído de fora entre no sinal; laboratórios fazem medidas delicadas dentro de "gaiolas de Faraday". Tudo sai de uma regra só: dentro do metal em equilíbrio, E = 0.

### A ideia: a multidão que se acomoda

Um metal tem elétrons livres, que andam à vontade lá dentro. Se houvesse campo no metal, eles sentiriam força e se mexeriam. E se mexem mesmo: até que as cargas deslocadas criem um campo que cancela o de fora. Aí ninguém mais é empurrado. Isso leva muito menos de um microssegundo.

É como a água de um aquário inclinado: ela corre até a superfície ficar plana, e então para. No metal, o equivalente de "ninguém mais correr" é E = 0 em todo o interior.
Onde a analogia quebra. Na água, quem nivela é a gravidade; no metal, é a própria repulsão entre as cargas. E a água ocupa o volume todo, enquanto a carga em excesso de um metal vai toda para a superfície (logo abaixo). O que fica "plano" no metal é o potencial elétrico, assunto do Cap. 24.

### Três consequências, todas pela lei de Gauss
- A carga em excesso fica na superfície. Uma gaussiana logo abaixo da superfície, dentro do metal, tem E = 0 em todos os pontos: Φ = 0, então q_env = 0. A carga não pode estar no volume.
- Cavidade com carga q dentro: uma gaussiana dentro do metal, envolvendo a cavidade, também tem Φ = 0. Então a parede da cavidade tem de ter −q, para somar zero com a partícula.
- Conservação: a carga total do condutor, Q, é a soma das superfícies. Se a interna tem −q, a externa tem Q + q.

[FIGURA: Um pedaço de metal cinza com uma cavidade. Dentro da cavidade, uma partícula positiva q. Na parede da cavidade, sinais negativos. Na superfície externa do metal, sinais positivos. Uma superfície gaussiana tracejada passa dentro do metal, em volta da cavidade, onde E = 0.]

Figura 6-1. Condutor neutro com +q na cavidade: −q na parede da cavidade, +q na superfície externa.

Fora de uma casca esférica, a carga externa se espalha uniformemente, não importa onde a partícula esteja lá dentro. Então, fora, o campo é o de uma carga Q + q no centro. A parede da cavidade é que fica desigual: mais carga perto da partícula.

### Ficha das grandezas novas
| Grandeza | O que é e unidade | Valores reais | Se ela aumenta… | Armadilha |
| carga induzida | carga que aparece numa superfície do metal porque outra carga está perto; C | parede de uma cavidade com +3 µC dentro: exatamente −3 µC | acompanha a carga que a induz, com sinal oposto | aparece mesmo num condutor neutro: ele separa +/−, não cria carga |
| E no metal | campo dentro do material do condutor, em equilíbrio | sempre 0 (em equilíbrio eletrostático) | não aumenta: se aparecer, as cargas se movem até zerar | E = 0 é no metal; numa cavidade com carga dentro, há campo |
| σ junto a um condutor | carga por área na superfície; o campo logo fora é proporcional a ela (a fórmula sai no Degrau 7) | satélite do Problema 19: 4,5 × 10⁻⁷ C/m²; acima de uns 2,7 × 10⁻⁵ C/m² o ar em volta rompe (3 × 10⁶ N/C) | E logo fora cresce na mesma proporção | σ é a carga por área da face que você está olhando; a fórmula do campo e a diferença para uma folha isolante estão no Degrau 7 |

### Experimente: casca metálica com uma partícula dentro

**[PERGUNTA prev-w6]** Antes de mexer: uma partícula de +3 µC é posta dentro de uma casca metálica neutra. A carga na superfície externa da casca fica:
   a) zero, porque a casca é neutra
   b) −3 µC
   c) depende de onde a partícula está
   d) +3 µC
   (Previsão antes do widget w6. Responda, depois abra conferir/prev-w6.md.)

[WIDGET INTERATIVO — W6 — Cargas induzidas numa casca metálica] Corte de uma casca esférica metálica, cinza. Dentro da cavidade, uma partícula com a carga escolhida. Sinais na parede interna e na superfície externa mostram as cargas induzidas. Setas mostram o campo na cavidade e do lado de fora.
   Controles: Carga da partícula q (µC):; Carga total da casca Q (µC):; no centrofora do centro
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: Exemplo 23.05 do livro

Uma casca metálica esférica, neutra, tem raio interno R. Uma partícula de −5,0 µC está a R/2 do centro. Quais são as cargas das superfícies interna e externa? Estão uniformemente distribuídas? Como é o campo dentro e fora?

[FIGURA: Casca metálica esférica com uma partícula negativa fora do centro. Na parede interna, sinais positivos concentrados do lado da partícula. Na superfície externa, sinais negativos espalhados uniformemente.]

Figura 6-2. Fig. 23-13b do livro (reconstruída): + desigual dentro, − uniforme fora.

Entender Casca neutra (Q = 0); partícula q = −5,0 µC fora do centro. Incógnitas: carga e distribuição de cada superfície.

Modelar Em equilíbrio, E = 0 no metal. Gaussiana esférica dentro do metal, envolvendo a cavidade.

Resolver em símbolos Φ = 0 na gaussiana → \(q + q_{int} = 0\) → \(q_{int} = -q\). Com q = −5,0 µC: \(q_{int} = +5{,}0\) µC. Conservação: \(q_{int} + q_{ext} = Q = 0\), então \(q_{ext} = -q_{int} = -5{,}0\) µC.

▸ [recolhido, abre ao clicar] Por que a carga de fora fica uniforme, se a partícula está fora do centro?
   Porque a carga de dentro (partícula + parede da cavidade) soma zero e, juntas, elas não fazem campo nenhum no metal: a parede da cavidade se arruma exatamente para isso. Para a superfície externa, é como se não houvesse nada dentro. Sozinha numa esfera, ela se espalha por igual.

Calcular Interna: +5,0 µC, concentrada do lado da partícula. Externa: −5,0 µC, uniforme.

Verificar Total da casca: +5,0 − 5,0 = 0, neutra. Fora, o campo é o de −5,0 µC no centro (aponta para dentro), qualquer que seja a posição da partícula. Dentro da cavidade, o campo é torto (Fig. 23-13b do livro).

### Agora você completa: Problema 21 do livro

Um condutor tem carga total de +10 × 10⁻⁶ C. Dentro dele há uma cavidade, e dentro da cavidade está uma partícula de carga q = +3,0 × 10⁻⁶ C. Ache a carga (a) da superfície da cavidade e (b) da superfície externa. Responda em µC, com sinal.

**[CAMPO lac6-1]** (a) superfície da cavidade: ______ µC
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac6-1.md`. A página aceita tolerância de 2 %.

**[CAMPO lac6-2]** (b) superfície externa: ______ µC
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac6-2.md`. A página aceita tolerância de 2 %.

### Erros comuns
- Muita gente pensa que um condutor neutro não tem carga em lugar nenhum. Na verdade ele pode ter −q numa superfície e +q na outra, porque neutro quer dizer soma zero, não ausência de carga.
- Muita gente põe a carga do condutor espalhada pelo volume. Na verdade ela fica na superfície, porque uma gaussiana logo abaixo da superfície tem Φ = 0.
- Muita gente dá à superfície externa só a carga do condutor, Q. Na verdade é Q + q, porque a parede da cavidade "usou" −q e a soma das duas superfícies tem de dar Q.
- Muita gente pensa que dentro de uma cavidade o campo é sempre zero. Na verdade só é zero se não houver carga na cavidade, porque uma partícula lá dentro faz campo até a parede.

### Checkpoint do Degrau 6

(Pergunta 9 do livro) Uma pequena esfera carregada está dentro de uma casca metálica. Cargas (esfera, casca) em três situações: (1) +4q, 0; (2) −6q, +10q; (3) +16q, −12q.

**[PERGUNTA ck6-1]** Ordene as situações pela carga da superfície interna da casca, da maior para a menor (com sinal):
   a) 3, 1, 2
   b) 2, 1, 3
   c) todas iguais
   d) 2, 3, 1
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck6-1.md`.

**[PERGUNTA ck6-2]** E pela carga da superfície externa?
   a) 3, 2, 1
   b) 2, 3, 1
   c) 1, 2, 3
   d) todas iguais (+4q)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck6-2.md`.

**[PERGUNTA ck6-3]** Uma casca metálica tem carga −2 µC e a cavidade dela está vazia. O campo dentro da cavidade:
   a) é zero
   b) aponta para a parede
   c) aponta para o centro
   d) depende da espessura da casca
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck6-3.md`.

Dúvida da turma deste degrau: e se a casca do P29 for aterrada?

Habilidades desbloqueadas: E = 0 no metal, cargas induzidas e conservação nas superfícies. Com o Degrau 5, você já consegue fazer o Problema 29.

Onde isso volta: no Cap. 24, todo o condutor fica no mesmo potencial. No Cap. 25, as cargas das placas de um capacitor vão para as faces de dentro pelo mesmo motivo (Fig. 23-18 do livro, no cartão "o resto do capítulo").

## Placas
12 min · destrava o Problema 39

Por que isso existe. Folhas carregadas estão no tambor de uma impressora a laser, nos filtros eletrostáticos que tiram fuligem das chaminés e, principalmente, nos capacitores (Cap. 25). Perto de uma placa grande acontece algo estranho: o campo não enfraquece quando você se afasta.

### A ideia: a formiga e a parede

Você é uma formiga a 1 mm de uma parede gigantesca. Afaste-se para 2 mm: a parede continua tapando metade do seu céu. Os pedaços bem na sua frente ficaram mais longe, mas agora você "vê" mais pedaços pelos lados. Um efeito compensa o outro.

Com a placa carregada é igual. Volte ao W5, escolha "placa" e mexa no r: a curva é horizontal (o campo é constante). A gaussiana (uma latinha atravessando a placa) tem tampas de área fixa, que não crescem quando você se afasta.
Onde a analogia quebra. Uma placa real tem borda. Quando a sua distância fica comparável ao tamanho dela, a placa já não tapa metade do céu, e o campo começa a cair até virar o de uma carga pontual. No Cap. 22, o campo de um disco no eixo mostra isso: perto, σ/2ε₀; longe, kq/z². "Placa infinita" quer dizer: perto, e longe das bordas.

### A receita com a latinha
- Simetria: \(\vec E\) perpendicular à placa, com o mesmo módulo dos dois lados, para longe da placa se σ > 0.
- Gaussiana: latinha atravessando a placa, com uma tampa de área A de cada lado.
- Fluxo: pelas duas tampas, \(2EA\). A parede é rasante: zero.
- Carga envolvida: o pedaço de placa dentro da latinha: \(\sigma A\).
- Iguale: \(\varepsilon_0\cdot2EA = \sigma A\).

[FIGURA: Placa vertical com cargas positivas, vista de lado. Uma latinha gaussiana tracejada atravessa a placa, com uma tampa de cada lado. Setas de campo saem pelas duas tampas, para longe da placa.]

Figura 7-1. Fluxo pelas duas tampas; a parede da latinha é rasante.
\[E = \frac{\sigma}{2\varepsilon_0}\qquad(\text{placa isolante})\]Eq. 23-13

A área A some, e a distância nem aparece. Para σ < 0, o campo aponta para a placa, dos dois lados.

### Isolante × condutor: σ/2ε₀ ou σ/ε₀?

[FIGURA: Dois desenhos. À esquerda, uma folha isolante fina com uma latinha atravessando: o campo sai pelas duas tampas. À direita, a superfície de um bloco de metal, com a latinha metade dentro do metal: dentro o campo é zero, e o campo sai só pela tampa de fora.]

Figura 7-2. Mesma σ na face, mesma latinha: no condutor, o fluxo sai por uma tampa só.

Na superfície de um condutor, a latinha tem uma tampa dentro do metal, onde E = 0 (Degrau 6). Todo o fluxo sai pela outra: \(\varepsilon_0EA = \sigma A\), então \(E = \sigma/\varepsilon_0\) (Eq. 23-11). O condutor não "dobra" o campo: o campo só existe de um lado.

Nas duas fórmulas, σ é a carga por área da superfície que você está olhando. Cuidado com placas condutoras finas: se o problema dá a carga total por área, σ_tot, ela se divide pelas duas faces (σ_tot/2 em cada), e o campo fora volta a ser σ_tot/(2ε₀).

### Duas placas: some com sinais

Com duas placas isolantes, as cargas não se mexem. Calcule σ/(2ε₀) de cada uma, como se a outra não existisse, e some com sinais, região por região. Cada placa empurra para longe dela se positiva e puxa se negativa.

Exemplo 23.07 do livro: σ₊ = 6,8 µC/m² e σ₋ = −4,3 µC/m². Fora, os campos se opõem: 1,4 × 10⁵ N/C. Entre as placas, somam: 6,3 × 10⁵ N/C. Se as duas tivessem a mesma σ positiva, entre elas os campos se cancelariam.

[FIGURA: Duas placas verticais: a da esquerda positiva, a da direita negativa. Em cada uma das três regiões, setas tracejadas mostram o campo de cada placa e uma seta roxa mostra o total: à esquerda, total pequeno para a esquerda; entre as placas, total grande para a direita; à direita, total pequeno para a direita.]

Figura 7-3. Exemplo 23.07 do livro (reconstruído): campo de cada placa (tracejado) e total (roxo), em cada região.

### Ficha das grandezas novas
| Grandeza | O que é e unidade | Valores reais | Se ela aumenta… | Armadilha |
| σ | carga por área; C/m² | placa do Problema 39: alguns nC/m²; placas do Exemplo 23.07: 6,8 µC/m²; acima de uns 27 µC/m² junto a um condutor, o ar rompe | E cresce na mesma proporção | σ/2ε₀ é de folha isolante; σ/ε₀ é logo fora de condutor; σ é sempre a da face que você olha |
| distância à placa | quão longe você está da placa; m | "perto" = bem menor que o tamanho da placa | perto: nada muda; longe (comparável ao tamanho): E cai | não procure a distância na fórmula: ela não está lá |

### Exemplo resolvido: um elétron solto perto de uma folha carregada

Uma folha de plástico muito grande tem σ = +2,0 µC/m². (a) Qual é o campo a 1,0 cm e a 5,0 cm dela? (b) Qual é a aceleração de um elétron solto ali?

Entender Folha isolante, σ > 0. Distâncias pequenas comparadas à folha. Elétron: q = −e, m = 9,11 × 10⁻³¹ kg.

Modelar Simetria plana: \(E = \sigma/(2\varepsilon_0)\), perpendicular à folha, para longe dela. Força: \(\vec F = q\vec E\) (Cap. 22).

Resolver em símbolos \(E = \dfrac{\sigma}{2\varepsilon_0}\) nas duas distâncias. \(a = \dfrac{eE}{m} = \dfrac{e\sigma}{2\varepsilon_0m}\), apontando para a folha (carga negativa, força oposta ao campo).

▸ [recolhido, abre ao clicar] Por que a distância não entra?
   Porque a latinha pode ter qualquer comprimento: as tampas têm a mesma área A, esteja você a 1 cm ou a 5 cm. O fluxo que sai é sempre 2EA, e a carga dentro é sempre σA.

Calcular (a) \(E = \dfrac{2{,}0\times10^{-6}}{2(8{,}85\times10^{-12})} = 1{,}1\times10^5\) N/C, nas duas distâncias. (b) \(a = \dfrac{(1{,}60\times10^{-19})(1{,}13\times10^5)}{9{,}11\times10^{-31}} = 2{,}0\times10^{16}\) m/s².

Verificar 1,1 × 10⁵ N/C está abaixo da ruptura do ar (3 × 10⁶ N/C): plausível. A aceleração é 2 × 10¹⁵ vezes g: por isso o peso de um elétron quase nunca importa. Resposta calculada pelo guia.

### Agora você completa: esfera flutuando sobre uma placa

Uma esferinha de massa m = 5,0 mg e carga q = +3,0 × 10⁻⁸ C flutua parada acima de uma placa isolante horizontal, muito grande, uniformemente carregada. Qual é σ? (Use g = 9,8 m/s².)

[FIGURA: Placa horizontal com cargas positivas embaixo. Acima dela, uma esferinha positiva parada, com a força elétrica para cima e o peso para baixo, do mesmo tamanho.]

Figura 7-4. Desenho do guia: duas forças, mesmo módulo.

**[CAMPO lac7-1]** 1. Peso: mg = ______ N
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac7-1.md`. A página aceita tolerância de 2 %.

**[CAMPO lac7-2]** 2. Campo necessário: E = mg/q = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac7-2.md`. A página aceita tolerância de 2 %.

**[CAMPO lac7-3]** 3. Densidade da placa: σ = ______ C/m²
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac7-3.md`. A página aceita tolerância de 2 %.

### Erros comuns
- Muita gente usa σ/ε₀ para uma folha isolante. Na verdade é σ/(2ε₀), porque o fluxo sai pelas duas tampas da latinha; σ/ε₀ é só junto a um condutor, onde um dos lados tem E = 0.
- Muita gente pensa que o campo de uma placa cai com a distância, como o de uma carga. Na verdade, perto de uma placa grande, ele é constante, porque a área das tampas não cresce com a distância.
- Muita gente desenha o campo só de um lado da placa. Na verdade ele existe dos dois lados, com o mesmo módulo, porque a placa é igual vista de cada lado.
- Muita gente mistura o ângulo do fio com a vertical e com a horizontal. Na verdade, numa bolinha pendurada num fio, o ângulo que entra em tan θ = F/(mg) é com a vertical, porque é a vertical que segura o peso. Confira no desenho qual é o ângulo dado.

### Checkpoint do Degrau 7

[FIGURA: Teste 4 do livro. Duas placas verticais, isolantes, com a mesma densidade de carga positiva, nas pontas. Entre elas, a distâncias iguais d: o ponto 2, o ponto 3, uma esfera com carga positiva uniforme, e o ponto 4. O ponto 1 fica acima do ponto 2.]

Figura do Teste 4 do livro (reconstruída do PDF, pág. 173). As duas placas têm a mesma σ positiva; a esfera tem carga uniforme positiva.

**[PERGUNTA ck7-1]** (Teste 4) Ordene os pontos 1 a 4 pelo módulo do campo, do maior para o menor.
   a) 1, 2, 3, 4 (mais perto da placa, mais campo)
   b) 2, 1, 3, 4
   c) todos iguais
   d) 3 e 4 empatados, depois 2, depois 1
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck7-1.md`.

**[PERGUNTA ck7-2]** Junto a uma folha isolante com densidade σ, E = σ/(2ε₀). Junto à superfície de um condutor com densidade σ nessa superfície, E = σ/ε₀. Por que o dobro?
   a) Porque o metal conduz melhor o campo.
   b) Porque dentro do metal E = 0, e todo o fluxo sai por um lado só.
   c) Porque o condutor tem o dobro de carga.
   d) Porque uma das fórmulas do livro está errada.
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck7-2.md`.

**[PERGUNTA ck7-3]** A 1 cm de uma placa isolante grande, E = 500 N/C. A 3 cm (ainda longe das bordas), E vale:
   a) 500/9 ≈ 56 N/C
   b) 500/3 ≈ 170 N/C
   c) 500 N/C
   d) 1 500 N/C
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck7-3.md`.

Dúvidas da turma deste degrau: o ângulo do P39 · e se a placa do P39 fosse condutora? · até onde a placa é "infinita"?

Habilidades desbloqueadas: campo de placa isolante, contraste com condutor, equilíbrio com força elétrica. Você já consegue fazer o Problema 39.

Onde isso volta: no Cap. 24, a diferença de potencial entre placas é V = Ed (campo uniforme). No Cap. 25, o capacitor de placas paralelas tem E = σ/ε₀ entre as placas (duas placas condutoras, cartão abaixo).

## O resto do capítulo em 2 minutos

Nenhuma das suas questões usa estes tópicos. Leia para saber que existem e onde estão no livro.
| Tópico | A ideia em uma frase | No livro |
| Fluxo de campo não uniforme | Se o campo muda de ponto a ponto numa face plana (ex.: \(\vec E = 3{,}0x\,\hat\imath\)), mas a face é perpendicular a x, o x é o mesmo em toda a face e sai da integral. Os Problemas 9 a 11 treinam isso com cubos. | Exemplos 23.02 e 23.04 |
| Duas placas condutoras | Aproximadas, as cargas de sinais opostos se atraem e vão todas para as faces de dentro: entre as placas E = σ/ε₀; fora, zero. É o capacitor do Cap. 25. | Fig. 23-18, Eq. 23-14 |
| Campo junto a um condutor | Logo fora da superfície de um condutor, \(E = \sigma/\varepsilon_0\), perpendicular à superfície. Onde a superfície é mais pontuda, σ é maior: é por isso que para-raios são pontudos. | Eq. 23-11 |
| Gauss e Coulomb | As duas leis dizem a mesma coisa sobre cargas paradas; uma sai da outra (Eq. 23-10). Gauss é mais cômoda com simetria; Coulomb, sem ela. | Módulo 23-2 |

## As questões

Na ordem da mais fácil para a mais difícil. Tente sozinho primeiro; a ajuda só abre se você pedir, um nível por vez. Ímpares têm gabarito do livro; pares têm "resposta calculada pelo guia, sem gabarito oficial".
Constantes (as do livro)
- ε₀ = 8,85 × 10⁻¹² C²/(N·m²)
- k = 1/(4πε₀) = 8,99 × 10⁹ N·m²/C²
- e = 1,602 × 10⁻¹⁹ C
- g = 9,8 m/s²
- 1 mg = 10⁻⁶ kg; 1 nC = 10⁻⁹ C; 1 pC = 10⁻¹² C; 1 fC = 10⁻¹⁵ C
- 1 mN/C = 10⁻³ N/C

Como digitar: vírgula ou ponto; potências como 3,01e-9, 3,01×10^-9 ou 3,01×10⁻⁹; vale pi, π, √3 e frações. A unidade já está indicada ao lado do campo.

### Problema 5
nível · no livro; Degrau 2

Usa: lei de Gauss numa superfície fechada; repartir o fluxo por simetria.

Na Fig. 23-33, um próton está a uma distância d/2 do centro de um quadrado de aresta d (na reta perpendicular ao quadrado que passa pelo centro dele). Qual é o módulo do fluxo elétrico através do quadrado? (Sugestão: pense no quadrado como uma das faces de um cubo de aresta d.)

[FIGURA: Figura 23-33: um quadrado de aresta d visto em perspectiva, deitado. Um próton fica acima do centro do quadrado, a uma distância d/2.]

Figura 23-33 (reconstruída a partir do PDF).

**[CAMPO P5-a]** |Φ| pelo quadrado = ______ N·m²/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P5-a.md`. A página aceita tolerância de 2 %.

> Antes de pedir ajuda: já desenhou o quadrado e o próton? Já listou os dados (repare: d não tem valor) e a incógnita? Já sabe de que degrau é?

**[AJUDA de P5]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P5-1.md` (Dica 1: onde olhar), `ajuda/P5-2.md` (Dica 2: plano), `ajuda/P5-3.md` (Dica 3: primeiro passo), `ajuda/P5-4.md` (Resolução comentada), `ajuda/P5-5.md` (Resposta).

### Problema 24
nível · no livro; Degrau 5

Usa: lata gaussiana; carga envolvida de um tubo fino; campo de fio; gráfico E(r).

A Fig. 23-40 mostra uma seção de um tubo longo, de metal, de paredes finas, com raio R = 3,00 cm e carga por unidade de comprimento λ = 2,00 × 10⁻⁸ C/m. Determine o módulo E do campo elétrico a uma distância radial (a) r = R/2,00 e (b) r = 2,00R. (c) Faça um gráfico de E em função de r para 0 ≤ r ≤ 2,00R.

[FIGURA: Figura 23-40: um trecho de tubo metálico longo, de parede fina, visto em perspectiva, com cargas positivas na superfície. O raio R vai do eixo até a parede.]

Figura 23-40 (reconstruída a partir do PDF).

**[CAMPO P24-a]** (a) E em r = R/2 = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P24-a.md`. A página aceita tolerância de ±1 N/C.

**[CAMPO P24-b]** (b) E em r = 2R = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P24-b.md`. A página aceita tolerância de 2 %.

**[PERGUNTA P24-c]** (c) Qual descrição bate com o gráfico de E(r), de 0 a 2R?
   Antes de escolher: esboce E(r) no papel, de 0 a 2R, marcando os valores de (a) e (b) e o que acontece em r = R. Depois veja qual descrição bate com o seu esboço.
   a) Cresce em linha reta de 0 (no eixo) até R e depois cai como 1/r.
   b) Zero de 0 até R; em R salta para um valor máximo e depois cai como 1/r, valendo a metade desse máximo em 2R.
   c) Zero de 0 até R; depois cai como 1/r², valendo um quarto do pico em 2R.
   d) Cai como 1/r desde o eixo, muito grande perto de r = 0.
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/P24-c.md`.

> Antes de pedir ajuda: já desenhou o tubo em corte (vista de frente)? Já marcou onde está a carga e onde ficam os pontos R/2 e 2R? Já sabe de que degrau é?

**[AJUDA de P24]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P24-1.md` (Dica 1: onde olhar), `ajuda/P24-2.md` (Dica 2: plano), `ajuda/P24-3.md` (Dica 3: primeiro passo), `ajuda/P24-4.md` (Resolução comentada), `ajuda/P24-5.md` (Resposta).

### Problema 52
nível ·· no livro; Degrau 3

Usa: esfera gaussiana; carga envolvida de uma casca grossa com ρ uniforme; três regiões.

A Fig. 23-57 mostra uma casca esférica com uma densidade volumétrica de carga uniforme ρ = 1,84 nC/m³, raio interno a = 10,0 cm e raio externo b = 2,00a. Determine o módulo do campo elétrico (a) em r = 0, (b) em r = a/2,00, (c) em r = a, (d) em r = 1,50a, (e) em r = b e (f) em r = 3,00b.

[FIGURA: Figura 23-57: corte de uma casca esférica grossa. O material entre os raios a e b tem cargas positivas espalhadas; o miolo, de raio a, é vazio.]

Figura 23-57 (reconstruída a partir do PDF).

**[PERGUNTA P52-abc]** (a), (b) e (c): em r = 0, r = a/2 e r = a, o campo é:
   a) zero nos três pontos
   b) zero no centro e crescendo até r = a
   c) o mesmo valor nos três, diferente de zero
   d) muito grande no centro e menor em a
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/P52-abc.md`.

**[CAMPO P52-d]** (d) E em r = 1,50a = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P52-d.md`. A página aceita tolerância de 2 %.

**[CAMPO P52-e]** (e) E em r = b = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P52-e.md`. A página aceita tolerância de 2 %.

**[CAMPO P52-f]** (f) E em r = 3,00b = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P52-f.md`. A página aceita tolerância de 2 %.

> Antes de pedir ajuda: já desenhou a casca em corte e marcou os seis pontos? Já separou em quais regiões eles caem? Já sabe de que degrau é?

**[AJUDA de P52]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P52-1.md` (Dica 1: onde olhar), `ajuda/P52-2.md` (Dica 2: plano), `ajuda/P52-3.md` (Dica 3: primeiro passo), `ajuda/P52-4.md` (Resolução comentada), `ajuda/P52-5.md` (Resposta).

### Problema 76
Problemas Adicionais (sem nível no livro); Degrau 5

Usa: lata gaussiana dentro e fora; carga envolvida = ρ × volume.

Um cilindro muito longo, de raio R, possui uma distribuição volumétrica de carga uniforme. (a) Mostre que, a uma distância r < R do eixo do cilindro, \(E = \dfrac{\rho r}{2\varepsilon_0}\), em que ρ é a densidade volumétrica de carga. (b) Escreva uma expressão para E do lado de fora do cilindro. (Carga no volume: o cilindro é isolante.)

[FIGURA: Esquema do guia: um cilindro maciço longo, em perspectiva, com carga espalhada no volume e raio R.]

Esquema do guia (o livro não tem figura).

A resposta é uma expressão. Escreva-a no papel e confira com os valores-teste: ρ = 1,00 µC/m³, R = 2,00 cm.

**[CAMPO P76-a]** (a) teste: E em r = 1,50 cm = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P76-a.md`. A página aceita tolerância de 2 %.

**[PERGUNTA P76-b]** (b) Do lado de fora (r > R), E =
   a) \(\dfrac{\rho r}{2\varepsilon_0}\)
   b) \(\dfrac{\rho R^2}{2\varepsilon_0 r^2}\)
   c) \(\dfrac{\rho R^2}{2\varepsilon_0 r}\)
   d) \(\dfrac{\rho R}{2\varepsilon_0}\)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/P76-b.md`.

**[CAMPO P76-c]** (b) teste: E em r = 5,00 cm = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P76-c.md`. A página aceita tolerância de 2 %.

> Antes de pedir ajuda: já desenhou o cilindro em corte, com um ponto dentro e outro fora? Já sabe de que degrau é?

**[AJUDA de P76]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P76-1.md` (Dica 1: onde olhar), `ajuda/P76-2.md` (Dica 2: plano), `ajuda/P76-3.md` (Dica 3: primeiro passo), `ajuda/P76-4.md` (Resolução comentada), `ajuda/P76-5.md` (Resposta).

### Problema 29
nível ·· no livro; Degraus 5 e 6

Usa: lata gaussiana com λ = Q/L; sinal de q_env → sentido; cargas induzidas num condutor.

A Fig. 23-42 é uma seção de uma barra condutora de raio R₁ = 1,30 mm e comprimento L = 11,00 m no interior de uma casca coaxial (condutora), de paredes finas, de raio R₂ = 10,0R₁ e mesmo comprimento L. A carga da barra é Q₁ = +3,40 × 10⁻¹² C; a carga da casca é Q₂ = −2,00Q₁. Determine (a) o módulo E e (b) a direção (para dentro ou para fora) do campo elétrico a uma distância radial r = 2,00R₂. Determine (c) E e (d) a direção do campo elétrico para r = 5,00R₁. Determine a carga (e) na superfície interna e (f) na superfície externa da casca.

(A tradução perdeu a palavra "condutora": o original fala em "conducting shell", e o gabarito de (e) e (f) só bate assim. Coaxial: com o mesmo eixo da barra.)

[FIGURA: Figura 23-42 em corte: barra condutora fina no centro, de raio R1 e carga Q1 positiva, dentro de uma casca condutora coaxial de raio R2 = 10 R1 e carga Q2 negativa. Dois pontos marcados: a 5 R1 do eixo, entre a barra e a casca, e a 2 R2, fora de tudo. O comprimento L é perpendicular ao papel.]

Figura 23-42 em corte (reconstruída a partir do PDF, que a mostra em perspectiva).

**[CAMPO P29-a]** (a) E em r = 2,00R₂ = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P29-a.md`. A página aceita tolerância de 2 %.

**[PERGUNTA P29-b]** (b) A direção do campo em r = 2,00R₂ é:
   a) para fora (longe do eixo)
   b) para dentro (para o eixo)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/P29-b.md`.

**[CAMPO P29-c]** (c) E em r = 5,00R₁ = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P29-c.md`. A página aceita tolerância de 2 %.

**[PERGUNTA P29-d]** (d) A direção do campo em r = 5,00R₁ é:
   a) para fora (longe do eixo)
   b) para dentro (para o eixo)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/P29-d.md`.

**[CAMPO P29-e]** (e) carga na superfície interna da casca = ______ C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P29-e.md`. A página aceita tolerância de 2 %.

**[CAMPO P29-f]** (f) carga na superfície externa da casca = ______ C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P29-f.md`. A página aceita tolerância de 2 %.

> Antes de pedir ajuda: já desenhou o corte com a barra, a casca e os dois pontos (5R₁ e 2R₂)? Já converteu as cargas em λ? Já sabe de que degraus é?

**[AJUDA de P29]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P29-1.md` (Dica 1: onde olhar), `ajuda/P29-2.md` (Dica 2: plano), `ajuda/P29-3.md` (Dica 3: primeiro passo), `ajuda/P29-4.md` (Resolução comentada), `ajuda/P29-5.md` (Resposta).

### Problema 39
nível ·· no livro; Degrau 7

Usa: campo de placa isolante; equilíbrio de uma bolinha no fio; sinal da carga.

Na Fig. 23-49, uma pequena esfera isolante, de massa m = 1,0 mg e carga q = 2,0 × 10⁻⁸ C (distribuída uniformemente em todo o volume), está pendurada em um fio isolante que faz um ângulo θ = 30° com uma placa vertical, isolante, uniformemente carregada (vista em seção reta). Considerando a força gravitacional a que a esfera está submetida e supondo que a placa possui uma grande extensão, calcule a densidade superficial de carga σ da placa. (A placa é vertical, então θ também é o ângulo do fio com a vertical, como na figura.)

[FIGURA: Figura 23-49: uma placa vertical com cargas positivas, à esquerda. Um fio preso no alto da placa desce inclinado para a direita, fazendo o ângulo theta com a placa. Na ponta, uma pequena esfera de massa m e carga q.]

Figura 23-49 (reconstruída a partir do PDF).

**[CAMPO P39-a]** σ (com sinal) = ______ C/m²
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P39-a.md`. A página aceita tolerância de 2 %.

> Antes de pedir ajuda: já desenhou as forças na esfera? Já listou os dados (em SI) e a incógnita? Já sabe de que degrau é?

**[AJUDA de P39]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P39-1.md` (Dica 1: onde olhar), `ajuda/P39-2.md` (Dica 2: plano), `ajuda/P39-3.md` (Dica 3: primeiro passo), `ajuda/P39-4.md` (Resolução comentada), `ajuda/P39-5.md` (Resposta).

### Problema 53
nível ··· no livro; Degrau 4

Usa: somar cascas com ρ(r); esfera gaussiana; gráfico E(r).

Uma esfera isolante, de raio R = 5,60 cm, possui uma distribuição de carga não uniforme ρ = (14,1 pC/m³)r/R, em que r é a distância do centro da esfera. (a) Determine a carga da esfera. (b) Determine o módulo E do campo elétrico em r = 0, (c) em r = R/2,00 e (d) em r = R. (e) Faça um gráfico de E em função de r.

[FIGURA: Esquema do guia: esfera em corte, mais clara no centro e mais escura na borda, porque ρ cresce em linha reta de zero no centro até 14,1 pC por metro cúbico na superfície.]

Esquema do guia (o livro não tem figura).

**[CAMPO P53-a]** (a) carga da esfera q = ______ C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P53-a.md`. A página aceita tolerância de 2 %.

**[CAMPO P53-b]** (b) E em r = 0 = ______ mN/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P53-b.md`. A página aceita tolerância de ±0.001 mN/C.

**[CAMPO P53-c]** (c) E em r = R/2 = ______ mN/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P53-c.md`. A página aceita tolerância de 2 %.

**[CAMPO P53-d]** (d) E em r = R = ______ mN/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P53-d.md`. A página aceita tolerância de 2 %.

**[PERGUNTA P53-e]** (e) Qual descrição bate com o gráfico de E(r)?
   Antes de escolher: esboce E(r) no papel, de 0 a 2R, com os valores de (b), (c) e (d) marcados. Depois veja qual descrição bate.
   a) Cresce em linha reta até R e cai como 1/r² depois.
   b) Cresce como r² (uma parábola) até R e depois cai como 1/r², sem salto em R.
   c) Cresce como r² até R e depois fica constante.
   d) Cresce como r³ até R e depois cai como 1/r².
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/P53-e.md`.

> Antes de pedir ajuda: já escreveu ρ em função de r e viu que ela não é constante? Já listou os dados em SI? Já sabe de que degrau é?

**[AJUDA de P53]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P53-1.md` (Dica 1: onde olhar), `ajuda/P53-2.md` (Dica 2: plano), `ajuda/P53-3.md` (Dica 3: primeiro passo), `ajuda/P53-4.md` (Resolução comentada), `ajuda/P53-5.md` (Resposta).

## Dúvidas da turma

Perguntas que quatro alunos-teste fizeram ao estudar a primeira versão deste guia, com as respostas do Professor. Cada uma diz de que degrau é. As contas estão no calculos.py do guia.

Degrau 2 · Lei de Gauss

"Professor, por que a forma da superfície gaussiana não importa?"

Olhe da carga. Cada pedacinho da superfície tapa um cone fino de direções. Se o pedacinho está mais longe, ele precisa ser maior para tapar o mesmo cone (área ∝ r²), mas o campo ali é mais fraco (∝ 1/r²): o fluxo pelo cone é o mesmo. Inclinado, ele tem mais área, mas o cos θ diminui na mesma proporção. Somando os cones de todas as direções, dá q/ε₀ em qualquer forma. Esse cancelamento só acontece porque o campo cai exatamente com 1/r².

Degrau 2 · Problema 5

"E se o próton do Problema 5 estivesse a d/4 do quadrado?"

O truque do cubo falha: o próton não seria o centro de um cubo com esse quadrado como face. Pela geometria (o "ângulo sólido" que o quadrado ocupa visto do próton), o quadrado receberia 29,5 % do fluxo total, 5,34 × 10⁻⁹ N·m²/C, e não 1/6. Com o próton encostando no quadrado, a fração tende à metade: o quadrado tapa metade do "céu" do próton, como a metade da esfera do Degrau 2.

Degrau 3 · Esferas

"Professor, por que o campo de uma esfera tem de ser radial? Não existe outra direção?"

Gire a esfera em torno da reta que liga o centro ao ponto P. A esfera não muda e P fica no mesmo lugar, então o campo em P também não pode mudar. Se \(\vec E\) tivesse uma parte "de lado", ela giraria junto com a rotação. Logo, essa parte é zero e sobra a radial. Num cilindro, o argumento parecido é espelhar o fio num plano que contém o eixo (Degrau 5).

Degrau 3 · Esferas

"No Degrau 1 o guia diz que fluxo zero não quer dizer campo zero. Mas nas cascas a gente conclui E = 0 só porque q_env = 0. Quando pode?"

Só quando a simetria garante que E tem o mesmo módulo e é perpendicular em toda a gaussiana (esfera, lata, latinha). Aí Φ = E × área, e Φ = 0 obriga E = 0. Sem simetria, Φ = 0 só diz que entra tanto quanto sai. (Que uma cavidade vazia dentro de um metal tem E = 0, qualquer que seja a forma dela, é verdade, mas a prova usa o potencial, no Cap. 24.)

Degrau 3 · Problema 52

"No P52(f), fora da casca, eu continuo usando ρ × (volume dentro da gaussiana)?"

Continua valendo, mas o volume com carga dentro da gaussiana para de crescer em r = b: ele é a casca inteira, \(\tfrac43\pi(b^3 - a^3)\). Então, fora, q_env é a carga total da casca, constante, e E cai com 1/r², como uma carga pontual no centro. Usar r³ − a³ em 3b dá um campo dezenas de vezes maior que o certo.

Degrau 3 · a carga da Terra

"Se a Terra tem −6,8 × 10⁵ C, onde está a carga positiva que equilibra?"

No ar. Os −6,8 × 10⁵ C são a carga dentro de uma esfera logo acima do chão. O Problema 13 do livro dá 60 N/C a 300 m de altura: uma esfera nessa altura envolve só −2,7 × 10⁵ C. A diferença, cerca de +4 × 10⁵ C, está no ar entre o chão e 300 m. "Carga da Terra" depende de onde você põe a gaussiana.

Degrau 3 · aquecimento

"Com 150 N/C, há uns 300 V entre o chão e a minha cabeça? Por que eu não sinto nada?"

No ar parado, longe de você, sim: 150 N/C × 2 m ≈ 300 V. Mas o seu corpo conduz: ele fica todo no potencial do chão e entorta o campo em volta de você. E o ar quase não conduz, então não passa corrente que você sinta. (Potencial é o Cap. 24.)

Degrau 5 · Problema 29

"No P29 eu usei kQ/r² e deu 45 N/C. Por que a barra não é uma carga pontual? Como eu ia perceber?"

Pela forma e pelas distâncias: a barra tem 11 m e o ponto está a 2,6 cm do eixo. Visto de tão perto, a carga não está "num ponto": está espalhada ao longo de um comprimento enorme, comparado à distância. Comprido e redondo → lata, E = λ/(2πε₀r). Só bem de longe (distância ≫ 11 m) ele viraria carga pontual.

Degrau 5 · Problema 24

"Quanto vale E exatamente em r = R no tubo? 0 ou 1,2 × 10⁴ N/C?"

Numa parede de espessura zero, nenhum dos dois: o campo salta de 0 (dentro) para λ/(2πε₀R) (logo fora). Numa parede real, ele sobe de 0 a 1,2 × 10⁴ N/C dentro da espessura da parede. No gráfico, desenhe o salto em R.

Degrau 6 · Problema 29

"E se a casca do P29 fosse ligada à terra?"

A superfície interna continua com −3,40 pC: a barra ainda está lá dentro e a induz. A superfície externa, que tinha −3,40 pC, descarrega para a terra e fica com zero. Fora, E = 0. É assim que a malha de um cabo coaxial impede que o sinal de dentro "vaze" para fora.

Degrau 7 · Problema 39

"No P39, por que o ângulo com a placa é o ângulo com a vertical?"

Porque a placa é vertical: medir a partir dela ou a partir de qualquer reta vertical dá o mesmo ângulo (são paralelas). O que entra em tan θ = F/(mg) é sempre o ângulo do fio com a vertical, porque é a vertical que segura o peso.

Degrau 7 · Problema 39

"E se a placa do P39 fosse de metal?"

A esfera carregada induziria carga na placa e seria atraída por ela, como por uma carga "imagem" do outro lado: força k q²/(2d)², com d a distância até a placa. Com a esfera a 1 cm, essa força seria 9 × 10⁻³ N, 1 600 vezes a força qE do problema (5,7 × 10⁻⁶ N). Ela só ficaria menor que qE com a esfera a mais de uns 40 cm. A conta simples do P39 só serve para placa isolante.

Degrau 7 · Placas

"Até que distância uma placa de verdade é 'infinita'?"

Use o disco do Cap. 22: \(E/E_\infty = 1 - z/\sqrt{z^2+R^2}\). O erro passa de 10 % a partir de z ≈ 0,1R. Uma placa quadrada de 10 cm de lado equivale a um disco de 5,6 cm de raio: a 1 cm dela, o campo é 83 % de σ/(2ε₀), e não 100 %.

## Síntese: que superfície gaussiana eu uso?

Leia de cima para baixo e use a ferramenta da primeira pergunta cuja resposta é "sim". (No caso do metal, depois continue descendo para achar a simetria.)

- Pedem o fluxo por um pedaço de superfície (uma face, uma tampa)? Sim: feche a superfície, aplique a lei de Gauss no todo e reparta por simetria, se os pedaços forem iguais e igualmente posicionados em relação à carga. (Degrau 2; P5.)

- Há metal no problema (barra, casca, cavidade num condutor)? Sim: E = 0 dentro do metal. Uma gaussiana dentro do metal dá as cargas induzidas: superfície interna = −(carga dentro da cavidade); externa = total − interna. Depois, siga para a simetria certa. (Degrau 6; P29.)

- A carga tem simetria esférica (esfera, cascas, ρ que só depende de r)? Sim: esfera gaussiana de raio r pelo ponto. q_env = ρ × volume de material dentro (ρ uniforme) ou \(\int_0^r\rho\,4\pi r'^2dr'\) (ρ variável). (Degraus 3 e 4; P52, P53.)

- A carga tem simetria cilíndrica (fio, tubo, cilindro longo)? Sim: lata coaxial de raio r e altura h; fluxo só na parede, E·2πrh. q_env = λh ou ρ × volume de material dentro. (Degrau 5; P24, P76, P29.)

- A carga tem simetria plana (placa grande)? Sim: latinha atravessando a placa: E = σ/(2ε₀) para folha isolante; E = σ/ε₀ logo fora de um condutor. (Degrau 7; P39.)

- Nenhuma simetria? A lei de Gauss continua valendo, mas não dá o campo: volte à superposição e às integrais do Cap. 22.

### Equações do capítulo: quando usar e quando não usar
| Equação | Use quando… | Não use quando… |
| \(\Phi = EA\cos\theta\) | campo uniforme e superfície plana | o campo varia ou a superfície é curva (use simetria ou integre) |
| \(\varepsilon_0\Phi = q_{env}\) | qualquer superfície fechada | a superfície é aberta (face, tampa); há vidro, óleo ou plástico dentro (Cap. 25) |
| \(E = \dfrac{q}{4\pi\varepsilon_0r^2}\) | fora de qualquer distribuição esférica (q = carga total) | dentro da distribuição (use q_env) |
| \(E = \dfrac{\rho r}{3\varepsilon_0}\) | dentro de uma esfera maciça com ρ uniforme | casca grossa (tire a cavidade concêntrica) ou ρ variável (some cascas) |
| \(E = 0\) | dentro de uma casca fina com carga uniforme ou de um tubo fino longo; no metal de um condutor em equilíbrio | a cavidade tem carga dentro |
| \(E = \dfrac{\lambda}{2\pi\varepsilon_0 r}\) | fora de um fio ou cilindro longo (λ = carga por metro dentro da lata) | perto das pontas; dentro de um cilindro com carga no volume |
| \(E = \dfrac{\rho r}{2\varepsilon_0}\) | dentro de um cilindro maciço com ρ uniforme | fora do cilindro (refaça a lata: o material com carga para em R) |
| \(E = \dfrac{\sigma}{2\varepsilon_0}\) | perto de uma folha isolante grande, longe das bordas (σ da folha) | junto a um condutor; longe da placa (distância comparável ao tamanho) |
| \(E = \dfrac{\sigma}{\varepsilon_0}\) | logo fora da superfície de um condutor (σ da face que você olha) | folha isolante (aí é σ/2ε₀) |

### Régua de números reais

Para saber se uma resposta é "grande" ou "pequena". Os valores sem fonte no guia são ordens de grandeza.
| Campo E (N/C) | O que é |
| 2 × 10⁻² | superfície da esfera do Problema 53 |
| 0,2 a 0,9 | dentro e fora da casca do Problema 29 |
| 150 | ar perto do chão, em dia de tempo bom |
| da ordem de 10⁴ | chão debaixo de uma nuvem de tempestade |
| 1,1 × 10⁵ | perto de uma folha com 2 µC/m² (Degrau 7) |
| 2,4 a 3 × 10⁶ | o ar rompe: faísca (Degraus 5 a 7) |
| 5 × 10¹¹ | campo do próton sobre o elétron do hidrogênio |
| Carga (C) | O que é |
| 1,6 × 10⁻¹⁹ | um próton (Problema 5) |
| 7,8 × 10⁻¹⁵ | esfera do Problema 53 |
| 3,4 × 10⁻¹² | barra do Problema 29 |
| 1,3 × 10⁻⁵ | cúpula de Van de Graaff de 20 cm de raio, no limite do ar |
| 2,4 × 10⁻⁵ | a mulher na tempestade (Degrau 5) |
| −6,8 × 10⁵ | a Terra (Degrau 3) |

## Revisão intercalada

Nove perguntas misturando os degraus, fora de ordem de propósito: na prova, ninguém avisa de que degrau é a questão. Marque a confiança antes de conferir.

**[PERGUNTA rev-1]** 1. Uma carga pontual está dentro de uma esfera gaussiana. Você dobra o raio da esfera. O fluxo total:
   a) cai para 1/4
   b) dobra
   c) não muda
   d) cai pela metade
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-1.md`.

**[PERGUNTA rev-2]** 2. A 3 cm de um fio longo carregado, E = 600 N/C. A 6 cm, E vale:
   a) 150 N/C
   b) 300 N/C
   c) 600 N/C
   d) 1 200 N/C
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-2.md`.

**[PERGUNTA rev-3]** 3. Uma partícula de +2 µC está na cavidade de um condutor cuja carga total é −5 µC. A carga da superfície externa do condutor é:
   a) −5 µC
   b) −7 µC
   c) +2 µC
   d) −3 µC
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-3.md`.

**[PERGUNTA rev-4]** 4. Uma folha isolante grande tem σ = 8,85 nC/m². Perto dela, E vale:
   a) 500 N/C
   b) 1 000 N/C
   c) 250 N/C
   d) depende da distância
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-4.md`.

**[PERGUNTA rev-5]** 5. Numa esfera de raio R com ρ ∝ r, que fração da carga total fica dentro de r = R/2?
   a) 1/2
   b) 1/8
   c) 1/4
   d) 1/16
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-5.md`.

**[PERGUNTA rev-6]** 6. Um campo uniforme de 200 N/C atravessa um quadrado de 10 cm de lado cuja normal faz 60° com o campo. O fluxo é:
   a) 2,0 N·m²/C
   b) 1,7 N·m²/C
   c) 1,0 N·m²/C
   d) 0
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-6.md`.

**[PERGUNTA rev-7]** 7. Numa esfera maciça com carga uniforme, de raio R, quanto vale E(2R)/E(R)?
   a) 1/2
   b) 1/4
   c) 2
   d) 1
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-7.md`.

**[CAMPO rev-8]** 8. Uma casca esférica fina, de raio 10 cm, tem +4,0 nC. A 20 cm do centro, E = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/rev-8.md`. A página aceita tolerância de 2 %.

**[CAMPO rev-9]** 9. Um fio longo tem λ = 3,0 nC/m. A 4,0 cm dele, E = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/rev-9.md`. A página aceita tolerância de 2 %.

### Onde você estava confiante e errou

Ainda não há respostas com confiança marcada.

### Plano de revisão

Espaçar a revisão fixa mais que estudar tudo de uma vez. Os problemas abaixo são ímpares (têm gabarito) e não estão neste guia; cada sessão mistura degraus.
| Quando | O que fazer | Degraus |
| Hoje (10 min) | Numa folha, sem olhar, refaça o exemplo da esfera do Problema 78 (Degrau 3) e o da mulher na tempestade (Degrau 5). Depois confira. | 3, 5 |
| +1 dia | Problemas 13, 17 e 45 do livro. | 2, 3, 6 |
| +3 dias | Problemas 19, 27, 47 e 77. | 3, 5, 6 |
| +7 dias | Problemas 23, 57, 63, 75 e 81, e uma questão deste guia que você só resolveu com ajuda de nível 3 ou mais. | 3 a 7 |

▸ [recolhido, abre ao clicar] Gabarito do livro para o plano de revisão
   P13: 3,54 µC. P17: (a) 37 µC; (b) 4,1 × 10⁶ N·m²/C. P45: (a) 2,50 × 10⁴ N/C; (b) 1,35 × 10⁴ N/C. P19: (a) 4,5 × 10⁻⁷ C/m²; (b) 5,1 × 10⁴ N/C. P27: 3,8 × 10⁻⁸ C/m². P47: −7,5 nC. P77: (a) +4,0 µC; (b) −4,0 µC. P23: (a) 0,32 µC; (b) 0,14 µC. P75: 3,6 nC. P57: (a) 0; (b) 2,88 × 10⁴ N/C; (c) 200 N/C. P63: −1,04 nC. P81: (a) 0,25R; (b) 2,0R.

Seu progresso fica salvo só neste navegador. Apagar meu progresso
