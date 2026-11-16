# Guia (cópia cega para alunos-agente)

Este arquivo é o texto que a página mostra, na mesma ordem. As figuras aparecem como [FIGURA: descrição]; as capturas de tela estão em `rodada-1/telas/`. Perguntas e campos de resposta estão marcados; a conferência de cada um está em `conferir/<id>.md`, e a ajuda das questões em `ajuda/<Q>-<n>.md`.

Halliday, Fundamentos de Física, vol. 3 — Capítulo 22 Tema: automático

# Campos elétricos

Uma subida em seis degraus, do "o que é um campo?" até resolver sozinho os Problemas 8, 9, 15, 26, 29, 31, 38 e 81.

Tempo: cerca de 1 h 50 min nos degraus e 1 h 40 min nas questões. Faça em duas ou três sessões.

## Como usar este guia
- Suba na ordem: cada degrau só usa o que veio antes. Responda às perguntas antes de ver a resposta.
- Nas questões, tente sozinho primeiro; se travar, abra a ajuda um nível por vez.
- Seu progresso fica salvo neste navegador. Passe para o degrau seguinte quando acertar 2 de 3 no checkpoint.

## Mapa da subida

Cada degrau destrava as questões marcadas em cima dele. Toque num degrau para ir até ele.
- Degrau 0: Aquecimento
- Degrau 1: Força por coulomb (destrava P81)
- Degrau 2: Na mesma reta (destrava P8)
- Degrau 3: No plano (destrava P9, P15)
- Degrau 4: Arcos (destrava P29, P26)
- Degrau 5: Barra reta (destrava P31)
- Degrau 6: Disco (destrava P38)

Depois dos degraus: o resto do capítulo em 2 minutos, as questões, síntese e revisão intercalada.
0

## Aquecimento
10 min · uma pergunta para guardar e seis para checar a base

### Uma bola flutuando no ar?

Neste instante, o ar à sua volta tem um campo elétrico de uns 150 N/C apontando para baixo. É o "campo de tempo bom", criado pelas cargas da atmosfera e do chão. Você vai entender o que esse número quer dizer no Degrau 1.

Imagine uma esfera de enxofre de 4,4 N de peso (uns 450 g). Daria para fazê-la flutuar nesse campo, só carregando a esfera com eletricidade?

[FIGURA: Esfera amarela de enxofre no ar. Setas âmbar verticais para baixo representam o campo elétrico atmosférico de cerca de 150 N/C. Uma seta preta para baixo é o peso, 4,4 N. Uma seta tracejada para cima, com ponto de interrogação, é a força elétrica que queremos.]

Figura 0-1. A pergunta-gancho: o campo da atmosfera segura a esfera?

**[PERGUNTA gancho]** Seu palpite (não vale nota; a resposta aparece no Problema 81):
   a) Sim, e com pouca carga, como a de um balão esfregado no cabelo.
   b) Na conta dá, mas a carga seria tão grande que na prática não dá.
   c) Não: campo elétrico não faz força em enxofre.
   d) Não: 150 N/C é fraco demais para mover qualquer coisa.
   (Palpite: não há resposta certa agora; anote o seu. A resposta vem no Problema 81.)

### Teste rápido da base

Seis perguntas, uma por ferramenta que o capítulo usa. Errou? Abre uma mini-revisão logo abaixo.

**[PERGUNTA pre1]** 1. Prefixos. A carga do Problema 31 é 4,23 fC. Quanto é isso em coulombs?
   a) \(4{,}23\times10^{-12}\) C
   b) \(4{,}23\times10^{-15}\) C
   c) \(4{,}23\times10^{-9}\) C
   d) \(4{,}23\times10^{-18}\) C
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre1.md`.

**[PERGUNTA pre2]** 2. Lei de Coulomb (Cap. 21). Duas cargas a 6 cm se repelem com 0,8 N. Aproximando-as até 3 cm, a força passa a ser:
   a) 0,4 N
   b) 1,6 N
   c) 3,2 N
   d) 0,2 N
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre2.md`.

**[PERGUNTA pre3]** 3. Componentes. Um vetor de módulo 10 faz 135° com o semieixo x positivo. Suas componentes (x, y) são:
   a) (−7,07; +7,07)
   b) (+7,07; +7,07)
   c) (−7,07; −7,07)
   d) (+7,07; −7,07)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre3.md`.

**[PERGUNTA pre4]** 4. Ângulo pelo quadrante. Um vetor tem componentes (−3, −4). Qual é a orientação dele em relação ao semieixo x positivo?
   a) 53°
   b) −53°
   c) 127°
   d) 233° (ou −127°)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre4.md`.

**[PERGUNTA pre5]** 5. Integral de potência. Quanto vale \(\displaystyle\int_a^{a+L}\frac{dx}{x^2}\)?
   a) \(\ln\dfrac{a+L}{a}\)
   b) \(\dfrac{L}{a(a+L)}\)
   c) \(\dfrac{L}{a^2}\)
   d) \(\dfrac{1}{(a+L)^2}-\dfrac{1}{a^2}\)
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre5.md`.

**[PERGUNTA pre6]** 6. Equilíbrio. Uma bolinha de peso W está parada no ar. Só duas forças agem nela: o peso e uma força elétrica F. Então:
   a) F > W, para cima
   b) F = W, para baixo
   c) F = W, para cima
   d) F = 2W, para cima
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/pre6.md`.
1

## Campo = força por coulomb
15 min · destrava o Problema 81

Por que isso existe. No Capítulo 21, uma carga empurrava outra sem tocar nela. Como a segunda "sabe" que a primeira está lá? Resposta: cada carga cria em volta de si um campo elétrico, e é o campo, no lugar onde a outra está, que a empurra. Em engenharia, o campo decide quando o ar vira condutor e solta faísca: acima de uns 3 × 10⁶ N/C.

### A ideia: uma plaquinha de preço em cada ponto

Pense numa feira. Cada barraca tem uma plaquinha: "R$ 8 o quilo". A plaquinha está lá mesmo que ninguém compre. Quando você compra, a conta é preço × quantidade.

O campo elétrico é a plaquinha de cada ponto do espaço: diz quantos newtons cada coulomb vai sentir ali. Por isso a unidade é N/C. A força é a conta: força = carga × campo.
Onde a analogia quebra. (1) Preço é só um número; o campo é um vetor: diz quanto e para onde. (2) Não existe quilo negativo, mas existe carga negativa: ela sente a força no sentido oposto ao do campo. (3) Um comprador enorme pode mudar o preço da feira; uma carga grande empurra as cargas que criam o campo e muda o campo. Por isso a definição usa uma carga de teste pequena.

[FIGURA: Painel a: um objeto carregado à esquerda e uma pequena carga de prova positiva q0 no ponto P, com uma seta preta F0 apontando para a direita. Painel b: o mesmo objeto, sem a carga de prova; no ponto P, uma seta âmbar E na mesma direção.]

Figura 1-1. A carga de prova mede o campo; o campo existe sem ela. O vetor E nasce em P.

Para medir o campo num ponto P, ponha ali uma carga pequena e positiva \(q_0\) (a carga de prova), meça a força \(\vec F_0\) e divida:
\[\vec E = \frac{\vec F_0}{q_0}\]Eq. 22-1

Virando a conta ao contrário: uma carga q qualquer, num ponto onde o campo é \(\vec E\), sente
\[\vec F = q\,\vec E\]Eq. 22-28

Se q > 0, \(\vec F\) tem o sentido de \(\vec E\). Se q < 0, o sentido é o oposto. O módulo é \(F = |q|E\).

### O campo de uma carga pontual

Ponha a carga de prova a uma distância r de uma partícula de carga q. A lei de Coulomb dá a força; dividindo por \(q_0\), a carga de prova some da conta:
\[E = k\,\frac{|q|}{r^2} = \frac{1}{4\pi\varepsilon_0}\,\frac{|q|}{r^2}\]Eq. 22-3

Sentido: para longe da partícula se q é positiva; para a partícula se q é negativa. Desenhe a seta com a origem em P (o ponto onde você quer o campo), nunca na carga.

▸ [recolhido, abre ao clicar] Ver de onde vem
   Coulomb: \(F_0 = k\dfrac{|q|\,q_0}{r^2}\). Pela Eq. 22-1, \(E = \dfrac{F_0}{q_0} = k\dfrac{|q|}{r^2}\). O \(q_0\) aparece em cima e embaixo e se cancela. Por isso o campo depende só de quem o cria (q) e de onde você está (r), nunca de quem o mede.

[FIGURA: Duas cargas. À esquerda, carga positiva com linhas de campo radiais saindo dela e setas âmbar apontando para fora: setas longas perto da carga e setas quatro vezes menores no dobro da distância. À direita, carga negativa com linhas entrando e setas âmbar apontando para a carga.]

Figura 1-2. Cada seta é o campo no ponto onde ela nasce. No dobro da distância, a seta fica 4 vezes menor (1/r²). As linhas finas são linhas de campo: saem das cargas positivas e chegam às negativas.

Linhas de campo são o desenho do campo inteiro: em cada ponto, o campo é tangente à linha; onde as linhas ficam juntas, o campo é forte. Elas nascem em cargas positivas e terminam em negativas. São só uma ferramenta de visualização: nenhuma questão deste guia pede que você as desenhe.

### Ficha das grandezas novas
| Grandeza | O que é e unidade | Valores reais | Se ela aumenta… | Armadilha |
| \(\vec E\), campo elétrico | força por coulomb, vetor; N/C | ar em tempo bom: 100–150 N/C; 1,0 nC a 3,0 cm: 1,0 × 10⁴ N/C; ar vira condutor: 3 × 10⁶ N/C; dentro do átomo de H: 5 × 10¹¹ N/C | a força em qualquer carga ali aumenta na mesma proporção | E não depende da carga de prova |
| \(q_0\), carga de prova | carga pequena e positiva usada para definir E; C | "pequena" quer dizer: não mexe nas cargas que criam o campo | F₀ aumenta, mas F₀/q₀ continua igual | ela não entra na Eq. 22-3 |
| q (fonte) e r | carga que cria o campo e distância dela até P; C e m | próton: 1,602 × 10⁻¹⁹ C; balão esfregado: alguns nC | |q| dobra → E dobra; r dobra → E cai para ¼ | usar |q| na fórmula; o sinal só decide o sentido |
| k e ε₀ | constantes; k = 1/(4πε₀) | k = 8,99 × 10⁹ N·m²/C²; ε₀ = 8,85 × 10⁻¹² C²/(N·m²) | (são fixas) | o livro escreve 1/(4πε₀) em vez de k; é o mesmo número |

### Experimente: o campo cai com 1/r²

**[PERGUNTA prev-w1]** Antes de mexer: se você dobrar a distância r entre a carga e o ponto P, o campo em P fica…
   a) pela metade
   b) igual
   c) um quarto
   d) o dobro
   (Previsão antes do widget w1. Responda, depois abra conferir/prev-w1.md.)

[WIDGET INTERATIVO — W1 — Campo de uma carga pontual] Carga à esquerda e ponto P a uma distância r ajustável; a seta do campo em P muda de tamanho com 1/r ao quadrado.
   Controles: Distância r (em unidades de r₀ = 3,0 cm):; +1,0 nC+2,0 nC−1,0 nC
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: o campo dentro do átomo de hidrogênio

No modelo simples do átomo de hidrogênio, o elétron fica a \(r = 5{,}29\times10^{-11}\) m do próton. Qual é o campo do próton nesse ponto? Que força ele faz no elétron?

Entender Fonte: o próton (q = +e). Ponto: onde está o elétron. Incógnitas: E (módulo e sentido) e F no elétron.

Modelar Próton = carga pontual → Eq. 22-3. Força no elétron → Eq. 22-28 com q = −e.

▸ [recolhido, abre ao clicar] Por que o campo do próton não depende da carga do elétron?
   Porque o campo é do próton: ele está lá com ou sem o elétron. A carga do elétron só entra no segundo passo, na força.

Resolver em símbolos \(E = k\dfrac{e}{r^2}\), para longe do próton. \(F = |{-e}|\,E = \dfrac{ke^2}{r^2}\), em sentido oposto ao de \(\vec E\) (carga negativa), ou seja, para o próton.

Calcular \(E = \dfrac{(8{,}99\times10^{9})(1{,}602\times10^{-19})}{(5{,}29\times10^{-11})^2} = 5{,}15\times10^{11}\ \text{N/C}\). \(F = (1{,}602\times10^{-19})(5{,}15\times10^{11}) = 8{,}24\times10^{-8}\ \text{N}\).

Verificar Unidade: C × N/C = N. A força bate com a lei de Coulomb do Cap. 21 (\(ke^2/r^2\), o mesmo número). Ordem de grandeza: esse campo é 170 mil vezes o que faz o ar soltar faísca; por isso é tão difícil arrancar o elétron do átomo.

### Agora você completa: a gota de Millikan (Problema 39 do livro)

Uma gota de óleo de raio 1,64 µm e massa específica 0,851 g/cm³ fica parada entre as placas quando o campo vertical, para baixo, vale 1,92 × 10⁵ N/C. Qual é a carga da gota, em múltiplos de e? (Use g = 9,8 m/s².)

Entender Parada → equilíbrio entre peso e força elétrica.

Modelar \(m = \rho\,\tfrac43\pi r^3\) (cuidado: 0,851 g/cm³ = 851 kg/m³); \(|q|E = mg\).

**[CAMPO lac-mil-1]** Massa da gota, m = ______ kg
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-mil-1.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-mil-2]** Peso, mg = ______ N
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-mil-2.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-mil-3]** |q| = mg/E = ______ C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-mil-3.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-mil-4]** |q|/e = ______ (número puro)
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-mil-4.md`. A página aceita 2 % de tolerância.

**[PERGUNTA lac-mil-5]** O sinal da carga: o campo aponta para baixo e a gota está parada. A carga é…
   a) negativa: q = −5e
   b) positiva: q = +5e
   c) tanto faz
   → Escolha ANTES de abrir `conferir/lac-mil-5.md`.

### Erros comuns
- Muita gente pensa que, com uma carga de prova maior, o campo fica maior. Na verdade a força fica maior, mas F₀/q₀ não muda, porque a força cresce na mesma proporção da carga de prova.
- Muita gente pensa que uma carga negativa cria "campo negativo". Na verdade o campo é um vetor; o módulo vem com |q| e o sinal só diz o sentido (para a carga).
- Muita gente desenha a seta do campo saindo da carga até P. Na verdade a seta nasce em P, porque ela representa o campo naquele ponto (Fig. 1-2). Desenhar na carga leva a somas erradas.
- Muita gente pensa que a força sempre aponta como o campo. Na verdade isso só vale para carga positiva; elétrons sentem força oposta ao campo.

### Checkpoint do Degrau 1

Marque a confiança antes de conferir. Suba quando acertar 2 de 3 de primeira.

[FIGURA: Teste 3 do livro: eixos x e y; acima do eixo x, uma seta E apontando para a direita (sentido positivo de x); um elétron e sobre o eixo x, à esquerda da origem.]

Figura do Teste 3 do livro (reconstruída a partir do PDF).

**[PERGUNTA ck1-1]** (Teste 3a) Qual é a orientação da força elétrica sobre o elétron?
   a) para a direita
   b) para a esquerda
   c) para cima
   d) nenhuma: campo uniforme não faz força
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck1-1.md`.

**[PERGUNTA ck1-2]** (Teste 3c) O elétron se movia para a direita antes de o campo ser ligado. Com o campo ligado, a velocidade dele…
   a) aumenta
   b) permanece constante
   c) diminui
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck1-2.md`.

**[PERGUNTA ck1-3]** Num ponto P, uma carga de prova de +2,0 nC sente 6,0 × 10⁻⁶ N para o norte. Trocando por uma carga de −4,0 nC no mesmo ponto, a força é:
   a) 1,2 × 10⁻⁵ N para o sul
   b) 1,2 × 10⁻⁵ N para o norte
   c) 3,0 × 10⁻⁶ N para o sul
   d) 6,0 × 10⁻⁶ N para o sul
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck1-3.md`.

Habilidade desbloqueada: força de um campo sobre uma carga, com o sentido certo, e equilíbrio com o peso. Você já consegue fazer o Problema 81 (a resposta do seu palpite do aquecimento está lá).

Onde isso volta: todos os degraus seguintes só somam campos de cargas pontuais. No Cap. 24, o potencial é "energia por coulomb", a mesma ideia; no Cap. 28, o campo magnético faz força \(q\vec v\times\vec B\).
2

## Na mesma reta
12 min · destrava o Problema 8

Por que isso existe. Quase nada tem uma carga só: uma molécula, um capacitor, um cabo têm muitas. O campo num ponto é a soma vetorial dos campos de todas elas. O caso mais simples (e o mais traiçoeiro) é quando as cargas estão alinhadas com o ponto.
\[\vec E = \vec E_1 + \vec E_2 + \cdots + \vec E_n\]Eq. 22-4 (superposição)

Cada \(\vec E_i\) é calculado como se a carga i estivesse sozinha (Degrau 1). Depois, soma-se como vetor.

### A ideia: ventiladores e aspiradores

Imagine um barquinho em P, num canal reto. Cada carga positiva é um ventilador que sopra o barco para longe dela; cada carga negativa é um aspirador que o puxa para ela. O barco sente a soma dos sopros e puxões.
Onde a analogia quebra. Ventiladores reais sopram num cone e os ventos se misturam; um campo elétrico age em todas as direções e os campos se somam exatamente, sem se atrapalhar (é isso que "superposição" quer dizer). E o sopro de um ventilador não cai exatamente com 1/r².

[FIGURA: Quatro casos numa reta horizontal com o ponto P no meio. Carga positiva à esquerda: campo em P para a direita. Carga negativa à esquerda: campo em P para a esquerda. Carga positiva à direita: campo para a esquerda. Carga negativa à direita: campo para a direita.]

Figura 2-1. Numa reta, o campo em P só pode apontar para um lado ou para o outro. Positiva empurra para longe; negativa puxa para si.

Daí sai uma regra de bolso para duas cargas alinhadas com P. Os campos têm sentidos opostos (e podem se cancelar) quando:
- estão do mesmo lado de P e têm sinais opostos; ou
- estão em lados opostos de P e têm o mesmo sinal.

Nos outros casos, os campos apontam para o mesmo lado e se somam.

Para cancelar de verdade, falta o módulo empatar: \(k|q_1|/r_1^2 = k|q_2|/r_2^2\). Ou seja, |q| proporcional a r²: uma carga 4 vezes maior a uma distância 2 vezes maior faz o mesmo campo.

Na conta, escolha um sentido como positivo (por exemplo, +x) e dê a cada campo um sinal tirado do desenho: \(E_x = \pm E_1 \pm E_2\). Os módulos vêm sempre com |q|.

### Experimente: dois campos numa reta

**[PERGUNTA prev-w2]** Antes de mexer: uma carga de +1 nC está 1 cm à esquerda de P, e uma de +4 nC está 2 cm à direita de P. O campo total em P…
   a) aponta para a direita
   b) aponta para a esquerda (a carga maior ganha)
   c) é zero
   d) depende do valor de k
   (Previsão antes do widget w2. Responda, depois abra conferir/prev-w2.md.)

[WIDGET INTERATIVO — W2 — Duas cargas numa reta] Eixo com o ponto P fixo no centro e duas cargas, A e B, de posição e valor ajustáveis. Em P aparecem as setas dos campos de A e de B e, embaixo, a seta roxa do campo total.
   Controles: Carga A (nC):; Posição de A (cm):; Carga B (nC):; Posição de B (cm):
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: lados opostos, sinais opostos

\(q_A = +2{,}0\) nC está em x = −2,0 cm e \(q_B = -3{,}0\) nC em x = +3,0 cm. Qual é o campo na origem?

[FIGURA: Eixo x de −3 a +4 cm. Carga A positiva em −2 cm, carga B negativa em +3 cm, ponto P na origem. Em P, o campo de A e o campo de B apontam ambos para +x; o campo total, roxo, também para +x.]

Figura 2-2. A empurra P para longe (para +x); B puxa P para si (também para +x).

Entender Duas cargas na reta x; P entre elas; incógnita: \(\vec E\) em P.

Modelar Superposição; cada campo pela Eq. 22-3; sentidos pela Fig. 2-1.

Resolver em símbolos \(E_A = k\dfrac{|q_A|}{r_A^2}\), para +x (A é positiva e está à esquerda). \(E_B = k\dfrac{|q_B|}{r_B^2}\), para +x (B é negativa e está à direita). \(E_x = E_A + E_B\).

▸ [recolhido, abre ao clicar] Por que os dois somam, se as cargas têm sinais opostos?
   Porque estão em lados opostos de P. Lados opostos + sinais opostos = mesmo sentido. A regra junta as duas coisas: lado e sinal.

Calcular \(E_A = \dfrac{(8{,}99\times10^9)(2{,}0\times10^{-9})}{(0{,}020)^2} = 4{,}50\times10^4\) N/C; \(E_B = \dfrac{(8{,}99\times10^9)(3{,}0\times10^{-9})}{(0{,}030)^2} = 3{,}00\times10^4\) N/C. Total: \(7{,}5\times10^4\) N/C, para +x.

Verificar Unidade N/C. Se B fosse +3,0 nC, ela empurraria P para −x e sobraria \(4{,}50\times10^4 - 3{,}00\times10^4 = 1{,}5\times10^4\) N/C para +x.

### Agora você completa: mesmo lado, sinais opostos

\(q_C = +1{,}0\) nC está em x = +1,0 cm e \(q_D = -4{,}0\) nC em x = +2,0 cm. Qual é o campo na origem?

[FIGURA: Eixo x. Ponto P na origem. Carga C positiva, +1,0 nC, em x = 1,0 cm. Carga D negativa, −4,0 nC, em x = 2,0 cm. Sem setas: desenhe você.]

Figura 2-3. Desenhe você as setas em P antes de preencher.

**[CAMPO lac-r-1]** E_C (módulo) = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-r-1.md`. A página aceita 2 % de tolerância.

**[PERGUNTA lac-r-2]** Sentido de \(\vec E_C\) em P:
   a) +x (para a direita)
   b) −x (para a esquerda)
   → Escolha ANTES de abrir `conferir/lac-r-2.md`.

**[CAMPO lac-r-3]** E_D (módulo) = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-r-3.md`. A página aceita 2 % de tolerância.

**[PERGUNTA lac-r-4]** Sentido de \(\vec E_D\) em P:
   a) +x (para a direita)
   b) −x (para a esquerda)
   → Escolha ANTES de abrir `conferir/lac-r-4.md`.

**[CAMPO lac-r-5]** Campo total em P, E_x = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-r-5.md`. A página aceita 2 % de tolerância.

### Erros comuns
- Muita gente soma os módulos: E = E₁ + E₂. Na verdade isso só vale quando os dois apontam para o mesmo lado; a soma é vetorial.
- Muita gente pensa que "a carga maior ganha". Na verdade ganha quem tem o maior |q|/r²: uma carga 4 vezes maior a uma distância 2 vezes maior empata.
- Muita gente pensa que campo zero num ponto quer dizer "não há cargas por perto". Na verdade pode haver cargas enormes cujos campos se cancelam exatamente ali.

### Checkpoint do Degrau 2

[FIGURA: Teste 1 do livro: no eixo x, da esquerda para a direita, o ponto S, o elétron e, o ponto R logo à direita do elétron, e o próton p mais à direita.]

Figura do Teste 1 do livro (reconstruída a partir do PDF). O próton e o elétron têm cargas de mesmo módulo.

**[PERGUNTA ck2-1]** (Teste 1a e 1b) Qual é o sentido do campo criado só pelo elétron no ponto S e no ponto R?
   a) S: para a esquerda; R: para a direita
   b) os dois para a direita
   c) S: para a direita; R: para a esquerda
   d) os dois para a esquerda
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck2-1.md`.

**[PERGUNTA ck2-2]** (Teste 1d) Qual é o sentido do campo total em S?
   a) para a direita
   b) para a esquerda
   c) zero, porque as cargas têm o mesmo módulo
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck2-2.md`.

[FIGURA: Pergunta 4 do livro: quatro sistemas numa reta, com o ponto central marcado e cargas a d e 2d de cada lado. Sistema 1: +e, −e, −e, +e. Sistema 2: +e, +e, −e, −e. Sistema 3: −e, +e, +e, +e. Sistema 4: −e, −e, +e, −e.]

Figura da Pergunta 4 do livro (reconstruída). Espaçamento d entre vizinhos; o ponto central fica entre a 2ª e a 3ª carga.

**[PERGUNTA ck2-3]** (Pergunta 4) Ordene os sistemas pelo módulo do campo no ponto central, do maior para o menor.
   a) 1, 2, 3, 4
   b) 4, 2, 3, 1
   c) 2, 3, 4, 1
   d) 2, 4, 3, 1
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck2-3.md`.

Habilidade desbloqueada: somar campos alinhados com P e enxergar cancelamentos. Você já consegue fazer o Problema 8 (nele, as cargas estão em duas retas que passam por P: trate cada reta como este degrau).

Onde isso volta: no P15 (Degrau 3) um par de cargas se cancela do mesmo jeito; no Cap. 23, a lei de Gauss usa simetria para dizer quais campos somem.
3

## No plano
18 min · destrava os Problemas 9 e 15

Por que isso existe. Fora de uma reta, os campos apontam em direções diferentes e não dá para somar com "mais ou menos". A saída é a mesma do Cap. 21 para forças: componentes. É o que um programa de simulação faz em cada ponto de uma placa de circuito para achar onde o campo é perigoso.

### A ideia: duas contas separadas

Somar vetores no plano é fazer duas contas independentes: uma só com as componentes x (leste-oeste), outra só com as y (norte-sul). Como num endereço do centro da cidade: "3 quadras a leste e 4 ao norte". Só no fim você junta as duas para achar o módulo e a orientação.
Onde a analogia quebra. Num trajeto, um deslocamento começa onde o outro termina. Os campos, não: todos nascem em P. Você só usa a mesma aritmética de componentes; não "anda" de um vetor para o outro.

[FIGURA: Duas cargas positivas iguais, uma em x = −3,0 cm e outra em x = +3,0 cm. O ponto P está no eixo y, em y = 4,0 cm; as distâncias até P são 5,0 cm. Em P, o campo de cada carga aponta para longe dela, inclinado. As componentes horizontais tracejadas têm sentidos opostos e se cancelam; as verticais se somam. O campo total, roxo, aponta para cima.]

Figura 3-1. As componentes x (tracejadas) se cancelam; as y se somam. O triângulo 3-4-5 da geometria é o mesmo das componentes.

O truque da geometria. O campo de cada carga aponta ao longo da reta carga–P. Então o triângulo que você desenha com as distâncias (3, 4, 5) é semelhante ao triângulo das componentes:
\[E_x = E\cdot\frac{\Delta x}{r},\qquad E_y = E\cdot\frac{\Delta y}{r}\]

com os sinais tirados do desenho. Nada de procurar "o ângulo certo" para o cosseno.

A simetria economiza conta. Duas cargas de mesmo |q|, simétricas em relação a uma reta que passa por P:
- mesmo sinal → o campo total fica sobre a reta de simetria (a mediatriz);
- sinais opostos → o campo total fica paralelo à reta que liga as cargas.
\[E = \sqrt{E_x^2 + E_y^2},\qquad \theta = \text{ângulo com o semieixo }+x\text{, pelo quadrante de }(E_x, E_y)\]

O ângulo pede desenho. A calculadora devolve \(\arctan(E_y/E_x)\) só entre −90° e +90°. Os vetores (3, 4) e (−3, −4) dão a mesma razão 4/3 e o mesmo 53°, mas apontam para lados opostos.

Faça em três passos: ângulo de referência \(\arctan(|E_y|/|E_x|)\); quadrante pelo desenho; ajuste. No 2º quadrante, 180° − ref; no 3º, 180° + ref (ou −180° + ref); no 4º, −ref.

[FIGURA: Eixos x e y. Um vetor roxo com componentes −3 e −4, no terceiro quadrante. Um arco mostra o ângulo de 233 graus medido a partir do semieixo x positivo; um arco pequeno mostra o ângulo de referência de 53 graus entre o vetor e o semieixo x negativo.]

Figura 3-2. atan(4/3) = 53° é só o ângulo de referência. O vetor (−3, −4) está no 3º quadrante: 233° (ou −127°).

### Experimente: duas cargas e P no eixo y

**[PERGUNTA prev-w3]** Antes de mexer: duas cargas positivas iguais em x = −3 e x = +3, e P no eixo y, acima delas. Para onde aponta o campo total em P?
   a) para +x
   b) a 45°
   c) para +y
   d) o campo é zero
   (Previsão antes do widget w3. Responda, depois abra conferir/prev-w3.md.)

[WIDGET INTERATIVO — W3 — Componentes e simetria] Duas cargas no eixo x em −3 e +3; a da esquerda pode ser positiva ou negativa. O ponto P sobe pelo eixo y. Em P, setas dos dois campos, as componentes tracejadas e a seta roxa do campo total.
   Controles: Altura de P (y, em cm):; +q−q
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: duas cargas iguais e P na mediatriz

Duas cargas de +2,0 nC estão em (−3,0 cm; 0) e (+3,0 cm; 0). Qual é o campo em P = (0; 4,0 cm)? (É a Figura 3-1.)

Entender Desenho: Fig. 3-1. Dados: q, posições. Incógnitas: módulo e orientação de \(\vec E\) em P.

Modelar Superposição de duas cargas pontuais. Simetria: mesmo sinal → só sobra a componente y.

Resolver em símbolos \(r = \sqrt{3{,}0^2+4{,}0^2} = 5{,}0\) cm. Cada campo: \(E_1 = E_2 = kq/r^2\). Componentes y: \(E_{1y} = E_{2y} = E_1\cdot\tfrac{4}{5}\). Total: \(E = 2E_1\cdot\tfrac45\), para +y.

▸ [recolhido, abre ao clicar] Por que 4/5 e não 3/5?
   A componente y corresponde ao lado vertical do triângulo, que mede 4,0 cm, dividido pela hipotenusa (5,0 cm). O lado horizontal (3,0 cm) daria a componente x, que se cancela.

Calcular \(E_1 = \dfrac{(8{,}99\times10^9)(2{,}0\times10^{-9})}{(0{,}050)^2} = 7{,}19\times10^3\) N/C; \(E = 2(7{,}19\times10^3)(0{,}80) = 1{,}15\times10^4\) N/C, a 90° (para +y).

Verificar Caso-limite: se P descesse até a origem (y → 0), os dois campos seriam horizontais e opostos: E = 0. Faz sentido com o resultado, que tem o fator 4/5 → 0. Unidade: N/C.

### Agora você completa: Problema 69 do livro

Duas partículas, ambas com carga de valor absoluto 12 nC, ocupam dois vértices de um triângulo equilátero de 2,0 m de lado. Qual é o módulo do campo no terceiro vértice (a) se as duas cargas são positivas e (b) se uma é positiva e a outra negativa?

[FIGURA: Triângulo equilátero de lado 2,0 m. Duas cargas de 12 nC nos vértices da base; o ponto P no vértice de cima. A linha vertical tracejada, do meio da base até P, é o eixo de simetria.]

Figura 3-3. Os sinais ficam para você decidir em cada item.

**[CAMPO lac-p-1]** Módulo do campo de cada carga em P = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-p-1.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-p-2]** Ângulo entre cada campo e o eixo de simetria (vertical) = ______ °
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-p-2.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-p-3]** (a) duas positivas: E = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-p-3.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-p-4]** (b) uma positiva e uma negativa: E = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-p-4.md`. A página aceita 2 % de tolerância.

### Erros comuns
- Muita gente confia no atan da calculadora. Na verdade ele não sabe o quadrante; desenhe o vetor antes de escrever o ângulo.
- Muita gente usa a distância horizontal (ou o lado do quadrado) como r. Na verdade r é a distância em linha reta da carga até P: Pitágoras. No centro de um quadrado de lado a, r = a/√2.
- Muita gente pensa que a simetria sempre cancela a componente x. Na verdade depende dos sinais: com sinais opostos, a componente que sobra é justamente a x (paralela à reta das cargas).

### Checkpoint do Degrau 3

[FIGURA: Pergunta 3 do livro: duas cargas −q no eixo x, à mesma distância d da origem, uma de cada lado. O ponto P está no eixo y, acima da origem.]

Figura da Pergunta 3 do livro (reconstruída a partir do PDF).

**[PERGUNTA ck3-1]** (Pergunta 3) Que componentes se cancelam em P, e para onde aponta o campo total?
   a) as x se cancelam; o total aponta para +y
   b) as y se cancelam; o total aponta para −x
   c) as x se cancelam; o total aponta para −y
   d) nada se cancela
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck3-1.md`.

**[PERGUNTA ck3-2]** Um campo tem \(E_x = -2{,}0\) N/C e \(E_y = +2{,}0\) N/C. Qual é a orientação em relação ao semieixo x positivo?
   a) −45°
   b) 45°
   c) 225°
   d) 135°
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck3-2.md`.

**[PERGUNTA ck3-3]** Um ponto P fica no centro de um quadrado de lado a. Qual é a distância de um vértice até P?
   a) a/√2
   b) a/2
   c) a√2
   d) a
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck3-3.md`.

Habilidades desbloqueadas: componentes, simetria e ângulo pelo quadrante. Você já consegue fazer o Problema 9 e o Problema 15 (que junta este degrau com o cancelamento do Degrau 2).

Onde isso volta: nos Degraus 4 a 6, a simetria vai cancelar componentes de infinitos pedacinhos de uma vez. No Cap. 29, o campo magnético de vários fios se soma com estas mesmas componentes.
4

## Arcos
20 min · destrava os Problemas 29 e 26

Por que isso existe. Uma barra de plástico carregada tem bilhões de cargas: não dá para somar uma por uma. A saída é fatiar o objeto em pedacinhos tão pequenos que cada um vira uma carga pontual, e somar todos com uma integral. Programas de simulação de campo fazem exatamente isso, com milhões de pedaços. O arco é o caso mais amigável: no centro dele, todos os pedaços estão à mesma distância.

### A ideia: gente em volta de uma mesa redonda

Imagine pessoas sentadas em volta de uma mesa redonda, todas empurrando um disco de hóquei que está no centro, com a mesma força. Duas pessoas em lados opostos se anulam. Se a mesa está cheia, o disco não sai do lugar. Se só metade da mesa tem gente, os empurrões "de lado" se anulam aos pares e sobra um empurrão para o lado vazio.

No arco carregado é igual: cada pedacinho empurra (se positivo) o ponto central com a mesma intensidade, porque está à mesma distância r.
Onde a analogia quebra. Pessoas empurram com uma força que não depende da distância; o campo cai com 1/r². No arco isso não aparece porque todos estão no mesmo r, mas vai aparecer na barra reta (Degrau 5). E cargas negativas puxam em vez de empurrar.

Antes, uma grandeza nova. Num objeto fino, a carga vem por unidade de comprimento: a densidade linear de carga
\[\lambda = \frac{Q}{L}\quad(\text{C/m}),\qquad\text{num arco: } L = r\,\varphi\ \ (\varphi\text{ em radianos})\]

Um pedacinho de comprimento ds tem carga \(dq = \lambda\,ds\). Num arco, \(ds = r\,d\theta\).

[FIGURA: Arco carregado positivamente à esquerda do ponto P, simétrico em relação ao eixo horizontal. Um pedacinho dq acima do eixo, a um ângulo theta, e o pedacinho simétrico abaixo. Em P, os dois campos dE apontam para longe de cada pedacinho. As componentes verticais têm sentidos opostos e se cancelam; as horizontais se somam.]

Figura 4-1. Pedacinho dq e seu par simétrico dq′. As componentes perpendiculares ao eixo de simetria se cancelam; as paralelas se somam: dE cos θ cada.

### O método do elemento, em seis passos
- Desenhe um pedacinho ds no ângulo θ (medido a partir do eixo de simetria) e o par simétrico.
- Carga do pedacinho: \(dq = \lambda\,ds = \lambda\,r\,d\theta\). Use |λ|; o sinal entra no desenho.
- Campo do pedacinho (Eq. 22-3): \(dE = k\dfrac{dq}{r^2} = \dfrac{k\lambda}{r}\,d\theta\). Igual para todos: r não muda.
- Simetria: as componentes perpendiculares se cancelam aos pares; sobra \(dE\cos\theta\).
- Integre de uma ponta à outra do arco (abertura φ, de −φ/2 a +φ/2).
- Sentido pelo desenho: para longe do arco se positivo, para o arco se negativo. Se pedirem em termos de Q, troque \(\lambda = Q/(r\varphi)\).
\[E = \frac{k\lambda}{r}\int_{-\varphi/2}^{\varphi/2}\cos\theta\,d\theta = \frac{2k\lambda}{r}\,\sin\frac{\varphi}{2} = \frac{kQ}{r^2}\cdot\frac{\sin(\varphi/2)}{\varphi/2}\]centro de um arco uniforme

Dois casos que você vai usar: semicírculo (φ = π): \(E = \dfrac{2k\lambda}{r} = \dfrac{2kQ}{\pi r^2}\). Anel completo (φ = 2π): sen π = 0, então E = 0 no centro.

▸ [recolhido, abre ao clicar] Ver de onde vem a última forma
   Com \(\lambda = Q/(r\varphi)\): \(\dfrac{2k\lambda}{r}\sin\dfrac{\varphi}{2} = \dfrac{2kQ}{r^2\varphi}\sin\dfrac{\varphi}{2} = \dfrac{kQ}{r^2}\cdot\dfrac{\sin(\varphi/2)}{\varphi/2}\). O primeiro fator é o campo da carga toda num ponto a uma distância r; o segundo é sempre menor que 1. Esse "desconto" é o quanto os empurrões laterais se desperdiçam.

### E se as metades tiverem sinais opostos?

[FIGURA: Semicírculo à esquerda de P: quarto de cima positivo, quarto de baixo negativo. Um pedacinho positivo em cima empurra P para baixo e para a direita; o pedacinho negativo simétrico puxa P para baixo e para a esquerda. As componentes horizontais se cancelam; as verticais se somam para baixo.]

Figura 4-2. Metade + em cima, metade − embaixo: agora quem se cancela é a componente horizontal.

O pedaço + de cima empurra P para baixo e para a direita. O pedaço − simétrico puxa P para baixo e para a esquerda. Agora são as componentes horizontais que se cancelam, e as verticais se somam.

Regra: antes de integrar, desenhe o par simétrico com os sinais certos e veja qual componente some. A integral é a mesma, só que com \(\sin\theta\) no lugar de \(\cos\theta\), porque a componente que sobra é a outra.

### Ficha das grandezas novas
| Grandeza | O que é e unidade | Valores reais | Se ela aumenta… | Armadilha |
| λ | carga por metro de um objeto fino; C/m | barra do Problema 31: 5 × 10⁻¹⁴ C/m (uns 26 mil elétrons em 8 cm); barra de plástico esfregada: da ordem de 10⁻⁸ C/m | o campo cresce na mesma proporção | λ = Q/L com o comprimento do arco (rφ), não o raio |
| φ | abertura do arco, vista do centro; rad | semicírculo: π rad; quarto: π/2; 120°: 2π/3 | com a mesma carga total, o campo no centro diminui (até zero no anel) | s = rφ só vale com φ em radianos |
| dq, ds, dθ | carga, comprimento e ângulo de um pedacinho | "tão pequenos quanto quiser": a integral é o limite da soma | — | dE de cada pedaço é um vetor; some componentes, não módulos |

### Experimente: abrir o arco

**[PERGUNTA prev-w4]** Antes de mexer: você vai abrir um arco carregado, sempre com a mesma carga total Q e o mesmo raio, de um pedacinho até um anel completo. O campo no centro…
   a) aumenta sempre
   b) fica igual
   c) diminui até a metade
   d) diminui até zero no anel completo
   (Previsão antes do widget w4. Responda, depois abra conferir/prev-w4.md.)

[WIDGET INTERATIVO — W4 — Arco com abertura variável] Arco à esquerda do ponto P com abertura ajustável. Seta tracejada: campo de toda a carga concentrada num ponto do arco. Seta roxa: campo real do arco.
   Controles: Abertura φ (graus):; toda +Qmetade +, metade −
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: arco de 120° (Exemplo 22.03 do livro)

Uma barra de plástico com carga −Q uniforme tem a forma de um arco de 120° e raio r. O eixo x é o eixo de simetria e P é o centro de curvatura. Qual é o campo em P, em termos de Q e r?

[FIGURA: Arco de 120 graus, com carga negativa, à direita de P, simétrico em relação ao eixo x. A seta roxa do campo em P aponta para o arco, no sentido positivo de x.]

Figura 4-3. Arco do Exemplo 22.03 (reconstruído).

Entender Arco de abertura φ = 120° = 2π/3 rad, carga −Q, raio r. Incógnita: \(\vec E\) no centro.

Modelar Método do elemento. P está no eixo de simetria → as componentes y se cancelam.

Resolver em símbolos \(\lambda = \dfrac{Q}{r\varphi} = \dfrac{3Q}{2\pi r}\). \(E = \dfrac{k\lambda}{r}\displaystyle\int_{-60^\circ}^{60^\circ}\cos\theta\,d\theta = \dfrac{2k\lambda}{r}\sin 60^\circ = \dfrac{k\lambda\sqrt3}{r}\).

▸ [recolhido, abre ao clicar] Por que os limites são −60° e +60°?
   θ é medido a partir do eixo de simetria. O arco tem 120° no total, metade para cada lado: de −60° a +60°. Para avaliar o seno, tanto faz graus ou radianos; o que exige radianos é o comprimento do arco, \(s = r\varphi\).

Calcular \(E = k\sqrt3\cdot\dfrac{3Q}{2\pi r}\cdot\dfrac1r = \dfrac{3\sqrt3}{2\pi}\cdot\dfrac{kQ}{r^2} = 0{,}83\,\dfrac{kQ}{r^2}\). Carga negativa: o campo aponta para o arco, \(\vec E = 0{,}83\,\dfrac{kQ}{r^2}\,\hat\imath\).

Verificar 0,83 < 1: o arco faz um campo menor que o da carga toda concentrada num ponto a uma distância r. É o "desconto" dos empurrões laterais. No widget, φ = 120° dá 0,827.

### Agora você completa: Problema 71 do livro

Uma carga de 20 nC está distribuída uniformemente numa barra de 4,0 m, encurvada num arco de raio 2,0 m. Qual é o módulo do campo no centro de curvatura?

**[CAMPO lac-a-1]** Abertura do arco, φ = s/r = ______ rad
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-a-1.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-a-2]** λ = ______ C/m
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-a-2.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-a-3]** E = (2kλ/r) sen(φ/2) = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-a-3.md`. A página aceita 2 % de tolerância.

### Erros comuns
- Muita gente calcula o campo do arco como se a carga toda estivesse num ponto do arco. Na verdade o arco dá menos, pelo fator \(\sin(\varphi/2)/(\varphi/2)\), porque parte de cada empurrão é lateral e se cancela.
- Muita gente pensa que um anel completo tem campo máximo no centro. Na verdade é zero: cada pedaço tem um parceiro do lado oposto.
- Muita gente usa graus em \(s = r\varphi\). Na verdade essa relação só vale em radianos.
- Muita gente carrega o sinal de λ dentro da integral e se perde. Na verdade é mais seguro integrar com |λ| e decidir o sentido pelo desenho (passo 6).

### Checkpoint do Degrau 4

[FIGURA: Teste 2 do livro, três barras isolantes. (a) Semicírculo à esquerda de P: quarto de cima com −Q, quarto de baixo com +Q. (b) Barra vertical à esquerda de P, com +Q na metade de cima e +Q na de baixo. (c) Barra vertical com +Q em cima e −Q embaixo.]

Figura do Teste 2 do livro (reconstruída a partir do PDF).

**[PERGUNTA ck4-1]** (Teste 2a) Qual é a orientação do campo total em P na barra (a)?
   a) +x
   b) −x
   c) −y
   d) +y
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck4-1.md`.

**[PERGUNTA ck4-2]** (Teste 2c) E na barra (c)?
   a) −y
   b) +x
   c) +y
   d) zero
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck4-2.md`.

[FIGURA: Pergunta 11 do livro: cinco arranjos de barras com forma de quarto de círculo, cada uma com carga +Q, em volta da origem. (a) só o primeiro quadrante. (b) primeiro e segundo. (c) primeiro, segundo e terceiro. (d) os quatro. (e) os quatro, mas o do quarto quadrante tem carga −Q.]

Figura da Pergunta 11 do livro (reconstruída). Todas as barras vermelhas têm +Q; no arranjo (e), a do 4º quadrante tem −Q.

**[PERGUNTA ck4-3]** (Pergunta 11) Ordene os cinco arranjos pelo módulo do campo no centro, do maior para o menor. (Chame de E o campo do arranjo (a).)
   a) e, d, b, a = c
   b) d, c, b, a, e
   c) e, b, a = c, d
   d) b, e, a = c, d
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck4-3.md`.

Habilidades desbloqueadas: λ, método do elemento no arco e simetria com sinais. Você já consegue fazer o Problema 29 e o Problema 26.

Onde isso volta: no Degrau 6, um anel visto de um ponto do eixo usa o mesmo raciocínio. No Cap. 29, o campo magnético no centro de um arco de corrente sai de uma integral idêntica (todos os pedaços à mesma distância).
5

## Barra reta
18 min · destrava o Problema 31

Por que isso existe. No arco, todo pedaço estava à mesma distância e r saía da integral. Numa barra reta com P no prolongamento, cada pedaço está a uma distância diferente, e a integral finalmente trabalha. É o modelo mais simples de um fio ou de uma trilha carregada visto de uma das pontas, e mostra quando dá para "trocar a barra por um ponto".

### A ideia: uma fila de ventiladores

A barra é uma fila de cargas. Olhando de P, a primeira da fila (a uma distância a) empurra forte; a última (a uma distância a + L) empurra bem menos, porque o campo cai com 1/x². Aqui ninguém se cancela: todos empurram P na mesma direção, ao longo da barra. Só que com intensidades diferentes.
Onde a analogia quebra. Numa fila de ventiladores, os da frente bloqueiam o vento dos de trás. Campos elétricos não se bloqueiam: cada pedaço contribui como se estivesse sozinho (superposição).

[FIGURA: Barra horizontal carregada, de comprimento L, à esquerda do ponto P, no mesmo eixo. Um pedacinho dx está a uma distância x de P. A ponta mais próxima da barra está a uma distância a de P.]

Figura 5-1. O pedacinho dx está a uma distância x de P; x vai de a (ponta perto) até a + L (ponta longe).

[FIGURA: Gráfico da função 1 sobre x ao quadrado, decrescente. A área sob a curva entre x = a e x = a + L está sombreada: é a integral.]

Figura 5-2. A integral é a área sob 1/x² entre a e a + L. Os pedaços perto de P (à esquerda do gráfico) pesam muito mais.

### A conta

Pedacinho: \(dq = \lambda\,dx\). Campo dele em P: \(dE = k\dfrac{\lambda\,dx}{x^2}\), sempre ao longo do eixo. Como todos têm a mesma direção, não há componente para cancelar: é só somar.
\[E = k\lambda\int_a^{a+L}\frac{dx}{x^2} = k\lambda\left(\frac1a - \frac1{a+L}\right) = \frac{k\lambda L}{a(a+L)} = \frac{k\,|q|}{a\,(a+L)}\]P no prolongamento da barra

Sentido: para longe da barra, se a carga é positiva; para a barra, se é negativa.

Uma leitura que ajuda a lembrar: é a fórmula da carga pontual, \(kq/r^2\), com \(r^2\) trocado por \(a(a+L)\). A "distância equivalente" \(\sqrt{a(a+L)}\) fica entre a ponta perto e a ponta longe (é a média geométrica das duas).

### De longe, a barra vira um ponto

Chame de D a distância de P até o centro da barra. Então a = D − L/2 e a + L = D + L/2, e
\[E = \frac{kq}{(D - L/2)(D + L/2)} = \frac{kq}{D^2 - L^2/4}\ \xrightarrow{\ D\,\gg\,L\ }\ \frac{kq}{D^2}\]

Quando D é muito maior que L, o termo L²/4 fica desprezível e sobra a carga pontual. Isso vale para qualquer objeto carregado: visto de longe, ele parece um ponto.

### Experimente: quando a barra vira um ponto?

**[PERGUNTA prev-w5]** Antes de mexer: a que distância do centro da barra (em comprimentos L) tratar a barra como carga pontual erra cerca de 1 %?
   a) D = L
   b) D = 2L
   c) D = 5L
   d) D = 50L
   (Previsão antes do widget w5. Responda, depois abra conferir/prev-w5.md.)

[WIDGET INTERATIVO — W5 — Barra × carga pontual] Gráfico da razão entre o campo da barra e o campo de uma carga pontual no centro dela, em função de D sobre L, de 0,6 a 10. A curva começa alta e cai até quase 1. Um marcador móvel mostra o valor escolhido.
   Controles: D/L (distância ao centro, em comprimentos da barra):
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: barra de 10 cm vista de perto

Uma barra fina de 10 cm tem carga +5,0 nC uniforme. Qual é o campo num ponto P do prolongamento da barra, a 5,0 cm da ponta mais próxima?

Entender Fig. 5-1 com L = 0,10 m, a = 0,050 m, q = 5,0 × 10⁻⁹ C. Incógnita: E em P.

Modelar Barra uniforme, P no prolongamento → todos os dE na mesma direção; a distância varia → integral de 1/x².

Resolver em símbolos \(E = \dfrac{kq}{a(a+L)}\), para longe da barra.

▸ [recolhido, abre ao clicar] Por que não posso usar a distância até o centro (10 cm)?
   Porque os pedaços de perto pesam mais que os de longe (1/x² não é uma reta). Usar o centro subestima: dá 4,50 × 10³ N/C, 25 % abaixo do valor certo. Só vale de longe (widget W5).

Calcular \(E = \dfrac{(8{,}99\times10^9)(5{,}0\times10^{-9})}{(0{,}050)(0{,}150)} = 5{,}99\times10^3\) N/C, para longe da barra.

Verificar O resultado tem de ficar entre "toda a carga na ponta perto" (1,80 × 10⁴ N/C) e "toda a carga na ponta longe" (2,00 × 10³ N/C). Fica. A distância equivalente, \(\sqrt{0{,}050\times0{,}150}\) = 8,7 cm, está entre 5 e 15 cm.

### Agora você completa: Problema 67 do livro

Uma corda com densidade linear uniforme de 9,0 nC/m se estende ao longo do eixo x, de x = 0 até x = 3,0 m. Qual é o módulo do campo no ponto x = 4,0 m?

**[CAMPO lac-b-1]** Distância de P até a ponta mais próxima, a = ______ m
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-b-1.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-b-2]** E = kλL/(a(a+L)) = ______ N/C
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-b-2.md`. A página aceita 2 % de tolerância.

### Erros comuns
- Muita gente usa a distância até o centro da barra como r. Na verdade isso só funciona de longe (D ≳ 5L); de perto, o erro passa de 25 %.
- Muita gente põe λ onde deveria ir q (ou o contrário). Na verdade \(k\lambda L/(a(a+L)) = kq/(a(a+L))\): confira a unidade (λL é carga).
- Muita gente inverte os limites, acha um E negativo e conclui que o campo "aponta para o outro lado". Na verdade o sinal da integral depende só da ordem dos limites; o sentido sai do desenho.

### Checkpoint do Degrau 5

**[PERGUNTA ck5-1]** Uma barra com carga negativa uniforme está à esquerda de P, no mesmo eixo. O campo em P aponta…
   a) para longe da barra (+x)
   b) para a barra (−x)
   c) perpendicular à barra
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck5-1.md`.

**[PERGUNTA ck5-2]** Por que na barra (P no prolongamento) não aparece um cos θ, como no arco?
   a) porque todos os pedaços estão à mesma distância de P
   b) porque λ é constante
   c) porque todos os dE apontam na mesma direção
   d) porque cos θ e sen θ se cancelam
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck5-2.md`.

**[PERGUNTA ck5-3]** P está a D = 10L do centro de uma barra. Tratar a barra como carga pontual no centro erra cerca de:
   a) 25 %
   b) 2,5 %
   c) zero
   d) 0,25 %
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck5-3.md`.

Habilidades desbloqueadas: integral com a distância variando e o limite "de longe". Você já consegue fazer o Problema 31.

Onde isso volta: no Cap. 24, o potencial da mesma barra sai de ∫dx/x (um logaritmo). No Cap. 29, o campo magnético de um trecho de fio reto usa a mesma ideia de integrar ao longo da linha.
6

## Disco
15 min · destrava o Problema 38

Por que isso existe. Placas de capacitor, telas sensíveis ao toque e o cilindro de uma copiadora são superfícies carregadas. O disco é a ponte entre os dois casos que você mais vai usar: de longe, ele é uma carga pontual; de perto, é uma placa infinita, com campo constante. É dessa placa que sai o capacitor do Cap. 25.

### A ideia: anéis de tronco de árvore

Corte um tronco e veja os anéis. Um disco carregado é isso: uma pilha de anéis concêntricos, do centro até a borda. Você já sabe tratar um anel (é o arco do Degrau 4 fechado e visto de um ponto do eixo). Somando os anéis, sai o disco.

E o comportamento de perto tem uma imagem simples: uma formiga no meio de um campo de futebol não vê as bordas. Para ela, o gramado é "infinito", e andar um passo para cima não muda nada. Perto do disco, o campo quase não muda com z.
Onde a analogia quebra. Os anéis de um tronco têm espessuras diferentes; os nossos são todos finos (dr) e têm a mesma densidade σ. E a "formiga" só vê o disco como infinito se estiver longe da borda e perto da superfície: z ≪ R.

Grandeza nova: a densidade superficial de carga, \(\sigma = Q/A\) (C/m²). Num disco, \(A = \pi R^2\).

[FIGURA: Disco visto em perspectiva, com o eixo z vertical passando pelo centro e o ponto P acima. Um anel fino de raio r e largura dr está destacado. Dois pedaços opostos do anel criam em P campos inclinados; as componentes horizontais se cancelam e sobra a vertical, ao longo de z.]

Figura 6-1. O disco como soma de anéis. Em cada anel, as componentes horizontais se cancelam aos pares; sobra só a componente ao longo de z.

Um anel de carga q e raio R, num ponto do eixo a uma distância z:
\[E_{\text{anel}} = \frac{k\,q\,z}{(z^2+R^2)^{3/2}}\]Eq. 22-16

O disco de densidade σ e raio R, num ponto do eixo:
\[E = \frac{\sigma}{2\varepsilon_0}\left(1 - \frac{z}{\sqrt{z^2+R^2}}\right)\]Eq. 22-26

▸ [recolhido, abre ao clicar] Ver de onde vem o anel
   Todo pedaço dq do anel está à mesma distância \(\sqrt{z^2+R^2}\) de P (como no arco). O campo de cada um vale \(dE = k\,dq/(z^2+R^2)\). Pedaços diametralmente opostos cancelam a componente horizontal; sobra \(dE\cos\theta\), com \(\cos\theta = z/\sqrt{z^2+R^2}\), igual para todos. Somando o anel inteiro: \(E = \dfrac{k z}{(z^2+R^2)^{3/2}}\displaystyle\int dq = \dfrac{kqz}{(z^2+R^2)^{3/2}}\).

▸ [recolhido, abre ao clicar] Ver de onde vem o disco
   Um anel de raio r e largura dr tem área \(2\pi r\,dr\) e carga \(dq = \sigma\,2\pi r\,dr\). Pela fórmula do anel: \(dE = \dfrac{k z\,\sigma\,2\pi r\,dr}{(z^2+r^2)^{3/2}}\). Com \(k\,2\pi = \dfrac{1}{2\varepsilon_0}\): \[E = \frac{\sigma z}{2\varepsilon_0}\int_0^R\frac{r\,dr}{(z^2+r^2)^{3/2}} = \frac{\sigma z}{2\varepsilon_0}\left[-\frac{1}{\sqrt{z^2+r^2}}\right]_0^R = \frac{\sigma z}{2\varepsilon_0}\left(\frac1z - \frac{1}{\sqrt{z^2+R^2}}\right)\] que é a Eq. 22-26. (A integral sai com a substituição \(u = z^2 + r^2\), \(du = 2r\,dr\).)

### Os três limites que você precisa enxergar
- Logo acima do centro (z → 0): o parêntese vale 1 e \(E = \dfrac{\sigma}{2\varepsilon_0}\). É o maior valor no eixo; chame de \(E_m\). Repare: não depende de R.
- Disco enorme (R → ∞): \(E = \dfrac{\sigma}{2\varepsilon_0}\) em qualquer z: o campo de uma placa infinita (Eq. 22-27), uniforme.
- Longe (z ≫ R): o disco vira um ponto, \(E \approx \dfrac{kQ}{z^2}\) com \(Q = \sigma\pi R^2\).

▸ [recolhido, abre ao clicar] Ver a conta do limite de longe
   \(\dfrac{z}{\sqrt{z^2+R^2}} = \left(1+\dfrac{R^2}{z^2}\right)^{-1/2} \approx 1 - \dfrac{R^2}{2z^2}\) quando R/z é pequeno (binômio). Então \(E \approx \dfrac{\sigma}{2\varepsilon_0}\cdot\dfrac{R^2}{2z^2} = \dfrac{\sigma\pi R^2}{4\pi\varepsilon_0 z^2} = \dfrac{kQ}{z^2}\).

O que isso faz com os gráficos. Dividindo a Eq. 22-26 por \(E_m\):
\[\frac{E}{E_m} = 1 - \frac{z}{\sqrt{z^2+R^2}} = 1 - \frac{z/R}{\sqrt{(z/R)^2+1}}\]

A curva de E/Eₘ depende só de z/R. Todo disco uniforme tem a mesma curva; um disco maior só "estica" o eixo z. Um gráfico de E/Eₘ contra z (em cm) esconde o raio dentro da escala horizontal.

### Experimente: disco, placa e ponto

**[PERGUNTA prev-w6]** Antes de mexer: bem perto do disco (z = 0,1R), o campo do disco é quase igual ao de…
   a) uma carga pontual com a mesma carga
   b) uma placa infinita com o mesmo σ
   c) zero
   (Previsão antes do widget w6. Responda, depois abra conferir/prev-w6.md.)

[WIDGET INTERATIVO — W6 — Campo no eixo do disco] Gráfico de E sobre E m em função de z sobre R, de 0 a 3. Curva cheia: disco. Linha tracejada horizontal em 1: placa infinita. Curva pontilhada: carga pontual. Um marcador móvel sobre a curva do disco.
   Controles: z/R:
   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)

### Exemplo resolvido: disco pequeno visto de longe (Problema 34 do livro)

Um disco de 2,5 cm de raio tem σ = 5,3 µC/m² na face superior. Qual é o campo num ponto do eixo a 12 cm do centro?

Entender R = 0,025 m, z = 0,12 m, σ = 5,3 × 10⁻⁶ C/m². Incógnita: E no eixo.

Modelar Disco uniforme, ponto no eixo → Eq. 22-26. Previsão: z/R = 4,8, então o resultado deve ficar perto do de uma carga pontual.

Resolver em símbolos \(E = \dfrac{\sigma}{2\varepsilon_0}\left(1 - \dfrac{z}{\sqrt{z^2+R^2}}\right)\).

▸ [recolhido, abre ao clicar] Por que não usar logo kQ/z², já que está longe?
   Pode, como estimativa. Mas "longe" é relativo: com z/R = 4,8 o erro é de uns 3 %. Use a fórmula exata e a pontual como conferência.

Calcular \(\dfrac{\sigma}{2\varepsilon_0} = \dfrac{5{,}3\times10^{-6}}{2(8{,}85\times10^{-12})} = 2{,}99\times10^5\) N/C; parêntese: \(1 - \dfrac{12}{\sqrt{144+6{,}25}} = 0{,}0210\); \(E = 6{,}29\times10^3\) N/C. (Problema par: resposta calculada pelo guia.)

Verificar Carga pontual: \(Q = \sigma\pi R^2 = 1{,}04\times10^{-8}\) C e \(kQ/z^2 = 6{,}50\times10^3\) N/C, 3 % acima. Bate com a previsão: de longe o disco parece um ponto, mas não exatamente.

### Agora você completa: Problema 35 do livro

A que distância, ao longo do eixo de um disco uniforme de 0,600 m de raio, o campo vale metade do campo no centro?

Modelar \(\dfrac{E}{E_m} = 1 - \dfrac{z}{\sqrt{z^2+R^2}} = \dfrac12\).

**[CAMPO lac-d-1]** Então z/√(z² + R²) vale ______ (número puro)
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-d-1.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-d-2]** Elevando ao quadrado e isolando: z/R = ______ (número puro)
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-d-2.md`. A página aceita 2 % de tolerância.

**[CAMPO lac-d-3]** z = ______ m
   → Escreva seu valor (lacuna de exemplo: se errar, a página oferece "Mostrar a resposta") ANTES de abrir `conferir/lac-d-3.md`. A página aceita 2 % de tolerância.

### Erros comuns
- Muita gente escreve \(E_m = \sigma/\varepsilon_0\). Na verdade, para um disco ou placa isolante com carga numa face, é \(\sigma/(2\varepsilon_0)\). O \(\sigma/\varepsilon_0\) aparece no condutor e entre as placas de um capacitor (Caps. 23 e 25).
- Muita gente pensa que o campo no centro do disco é zero, "como no anel". Na verdade logo acima do centro do disco o campo é o máximo, σ/(2ε₀). O anel dá zero no centro porque todos os pedaços estão no mesmo plano empurrando para os lados.
- Muita gente lê o gráfico como se o eixo estivesse em z/R quando ele está em cm (ou o contrário). Na verdade o raio está escondido na escala: ache primeiro quanto vale cada divisão.

### Checkpoint do Degrau 6

[FIGURA: Pergunta 9 do livro: três objetos com a mesma carga Q, vistos em perspectiva, com o ponto P à mesma altura acima do centro de cada um. (a) disco de raio R. (b) disco de raio 2R. (c) anel plano com raio interno R e raio externo 2R.]

Figura da Pergunta 9 do livro (reconstruída a partir do PDF). Os três têm a mesma carga Q.

**[PERGUNTA ck6-1]** (Pergunta 9) Ordene pelo módulo do campo em P, do maior para o menor.
   a) b, a, c
   b) a, b, c
   c) c, b, a
   d) a = b = c
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck6-1.md`.

**[PERGUNTA ck6-2]** Mantendo σ, você dobra o raio de um disco. O campo logo acima do centro (Eₘ)…
   a) dobra
   b) cai para ¼
   c) quadruplica
   d) não muda
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck6-2.md`.

**[PERGUNTA ck6-3]** Um disco tem E = 0,5Eₘ em z = 3,0 cm. Outro disco uniforme, com o dobro do raio, tem E = 0,5Eₘ em:
   a) 1,5 cm
   b) 3,0 cm
   c) 6,0 cm
   d) 12 cm
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/ck6-3.md`.

Habilidades desbloqueadas: fórmula do disco, seus limites e a leitura de um gráfico normalizado. Você já consegue fazer o Problema 38.

Onde isso volta: no Cap. 23, a lei de Gauss dá o campo da placa infinita em duas linhas; no Cap. 25, duas placas com cargas opostas formam um capacitor, com campo σ/ε₀ entre elas.

## O resto do capítulo em 2 minutos

Nenhuma das suas questões usa estes tópicos. Leia para saber que existem e onde estão no livro.
| Tópico | A ideia em uma frase | No livro |
| Dipolo elétrico | Duas cargas +q e −q separadas por d; o momento dipolar \(p = qd\) aponta de − para +. Longe, no eixo, \(E = 2kp/z^3\): cai mais rápido que 1/z², porque as duas cargas quase se cancelam. (No P9, o campo tem a direção oposta a \(\vec p\), como prevê a teoria para pontos da mediatriz.) | Módulo 22-3 |
| Carga num campo uniforme | F = qE é constante, então a carga faz um movimento de projétil, com qE/m no lugar de g. É assim que uma impressora a jato de tinta desvia as gotas. | Módulo 22-6, Exemplo 22.04 |
| Dipolo num campo | A força total num dipolo em campo uniforme é zero, mas há torque \(\vec\tau = \vec p\times\vec E\), que tenta alinhar \(\vec p\) com \(\vec E\). Energia: \(U = -\vec p\cdot\vec E\). O micro-ondas aquece a comida girando os dipolos da água. | Módulo 22-7 |
| Experimento de Millikan | Gotas de óleo equilibradas num campo mostram que toda carga é um múltiplo inteiro de e = 1,60 × 10⁻¹⁹ C (você refez isso no Degrau 1). | Módulo 22-6 |
| Ruptura dielétrica | Acima de uns 3 × 10⁶ N/C, o campo arranca elétrons do ar, o ar vira condutor e sai faísca. Esse limite aparece no Problema 81. | Módulo 22-6 |

## As questões

Na ordem da mais fácil para a mais difícil. Tente sozinho primeiro; a ajuda só abre se você pedir, um nível por vez. Ímpares têm gabarito do livro; pares têm "resposta calculada pelo guia, sem gabarito oficial".
Constantes (as do livro)
- k = 1/(4πε₀) = 8,99 × 10⁹ N·m²/C²
- ε₀ = 8,85 × 10⁻¹² C²/(N·m²)
- e = 1,602 × 10⁻¹⁹ C
- g = 9,8 m/s²
- ruptura do ar: 3,0 × 10⁶ N/C
- enxofre: 2,07 g/cm³ (só para o P81b)

Como digitar: vírgula ou ponto; potências como 1,38e-10, 1,38×10^-10 ou 1,38×10⁻¹⁰; vale pi, π, √3 e frações. A unidade já está indicada ao lado do campo.

### Problema 81
Problemas Adicionais; Degrau 1

Usa: F = qE com sinal, equilíbrio com o peso, campo de carga pontual, ordem de grandeza.

Existe na atmosfera um campo elétrico \(\vec E\), dirigido verticalmente para baixo, cujo módulo é da ordem de 150 N/C. Estamos interessados em fazer "flutuar" nesse campo uma esfera de enxofre com 4,4 N de peso, carregando-a eletricamente. (a) Qual deve ser a carga da esfera (sinal e valor absoluto)? (b) Por que o experimento não pode ser realizado na prática?

**[CAMPO P81-a]** (a) carga q, com sinal = ______ C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P81-a.md`. A página aceita 2 % de tolerância.

**[PERGUNTA P81-b]** (b) Por que não dá para fazer na prática?
   a) A carga necessária é pequena demais para ser medida.
   b) O campo da atmosfera varia de um dia para o outro, e a esfera cairia.
   c) O enxofre é isolante, e isolantes não podem ser carregados.
   d) A carga seria tão grande que a esfera se despedaçaria pela própria repulsão (e o ar em volta viraria condutor).
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/P81-b.md`.

> Antes de pedir ajuda: já desenhou a esfera com as forças? Já listou os dados e a incógnita? Já sabe de que degrau é?

**[AJUDA de P81]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P81-1.md` (Dica 1: onde olhar), `ajuda/P81-2.md` (Dica 2: plano), `ajuda/P81-3.md` (Dica 3: primeiro passo), `ajuda/P81-4.md` (Resolução comentada), `ajuda/P81-5.md` (Resposta).

### Problema 8
nível ·· no livro; Degrau 2

Usa: campo de carga pontual, sentido pelo sinal, cancelamento de campos alinhados com P.

Na Fig. 22-36, as quatro partículas são mantidas fixas e têm cargas \(q_1 = q_2 = +5e\), \(q_3 = +3e\) e \(q_4 = -12e\). A distância d = 5,0 µm. Qual é o módulo do campo elétrico no ponto P?

[FIGURA: Figura 22-36 reconstruída. O ponto P está no vértice de um ângulo reto. Numa diagonal, q1 fica acima e à esquerda de P, a uma distância d, e q2 abaixo e à direita, também a d. Na outra diagonal, para cima e à direita, q3 está a d de P e q4 está logo depois, a mais d (2d de P).]

Figura 22-36 (reconstruída a partir do PDF do livro). As duas diagonais se cruzam em ângulo reto em P.

**[CAMPO P8-a]** |E| em P = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P8-a.md`. A página aceita 2 % de tolerância.

> Antes de pedir ajuda: já desenhou as setas em P? Já calculou |q|/r² de cada carga em unidades de e/d²?

**[AJUDA de P8]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P8-1.md` (Dica 1: onde olhar), `ajuda/P8-2.md` (Dica 2: plano), `ajuda/P8-3.md` (Dica 3: primeiro passo), `ajuda/P8-4.md` (Resolução comentada), `ajuda/P8-5.md` (Resposta).

### Problema 9
nível ·· no livro; Degrau 3

Usa: Pitágoras, componentes com o triângulo 3-4-5, simetria com sinais opostos, ângulo pelo quadrante.

A Fig. 22-37 mostra duas partículas carregadas mantidas fixas no eixo x: \(-q = -3{,}20\times10^{-19}\) C, no ponto x = −3,00 m, e \(q = 3{,}20\times10^{-19}\) C, no ponto x = +3,00 m. Determine (a) o módulo e (b) a orientação (em relação ao semieixo x positivo) do campo elétrico no ponto P, para o qual y = 4,00 m.

[FIGURA: Figura 22-37 reconstruída: eixos x e y; carga −q em x = −3,00 m, carga +q em x = +3,00 m, ponto P no eixo y em y = 4,00 m.]

Figura 22-37 (reconstruída a partir do PDF do livro).

**[CAMPO P9-a]** (a) |E| = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P9-a.md`. A página aceita 2 % de tolerância.

**[CAMPO P9-b]** (b) orientação θ = ______ °
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P9-b.md`. A página aceita 2 % de tolerância.

> Antes de pedir ajuda: já desenhou os dois vetores em P? Já calculou a distância de cada carga até P?

**[AJUDA de P9]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P9-1.md` (Dica 1: onde olhar), `ajuda/P9-2.md` (Dica 2: plano), `ajuda/P9-3.md` (Dica 3: primeiro passo), `ajuda/P9-4.md` (Resolução comentada), `ajuda/P9-5.md` (Resposta).

### Problema 15
nível ·· no livro; Degraus 2 e 3

Usa: distância até o centro de um quadrado, cancelamento de um par, campo de carga pontual, ângulo.

Na Fig. 22-42, as três partículas são mantidas fixas no lugar e têm cargas \(q_1 = q_2 = +e\) e \(q_3 = +2e\). A distância a = 6,00 µm. Determine (a) o módulo e (b) a direção do campo elétrico no ponto P.

[FIGURA: Figura 22-42 reconstruída: partícula 3 na origem; partícula 1 no eixo y, a uma distância a acima da origem; partícula 2 no eixo x, a uma distância a à direita. P fica no centro do quadrado de lado a, no cruzamento das retas tracejadas que ligam 1 a 2 e 3 a P, com um ângulo reto marcado.]

Figura 22-42 (reconstruída a partir do PDF do livro). P é o centro do quadrado de lado a.

**[CAMPO P15-a]** (a) |E| = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P15-a.md`. A página aceita 2 % de tolerância.

**[CAMPO P15-b]** (b) direção θ (em relação a +x) = ______ °
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P15-b.md`. A página aceita 2 % de tolerância.

> Antes de pedir ajuda: já marcou as três distâncias até P? Já viu quais cargas estão alinhadas com P?

**[AJUDA de P15]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P15-1.md` (Dica 1: onde olhar), `ajuda/P15-2.md` (Dica 2: plano), `ajuda/P15-3.md` (Dica 3: primeiro passo), `ajuda/P15-4.md` (Resolução comentada), `ajuda/P15-5.md` (Resposta).

### Problema 29
nível ·· no livro; Degrau 4

Usa: λ de um semicírculo, campo no centro de um arco, carga pontual, resolver em símbolos.

A Fig. 22-52a mostra uma barra isolante com uma carga +Q distribuída uniformemente. A barra forma uma semicircunferência de raio R e produz um campo elétrico de módulo E no centro de curvatura P. Se a barra é substituída por uma carga pontual situada a uma distância R do ponto P (Fig. 22-52b), qual é a razão entre o novo valor de E e o antigo valor?

[FIGURA: Figura 22-52 reconstruída. (a) Semicircunferência de raio R com carga +Q, à esquerda do ponto P, que fica no centro de curvatura. (b) Uma carga pontual +Q à esquerda de P, a uma distância R.]

Figura 22-52 (reconstruída a partir do PDF do livro).

**[CAMPO P29-a]** E_novo / E_antigo = ______ (número puro)
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P29-a.md`. A página aceita 2 % de tolerância.

> Antes de pedir ajuda: já escreveu o campo do arco e o da carga pontual em símbolos (Q e R)?

**[AJUDA de P29]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P29-1.md` (Dica 1: onde olhar), `ajuda/P29-2.md` (Dica 2: plano), `ajuda/P29-3.md` (Dica 3: primeiro passo), `ajuda/P29-4.md` (Resolução comentada), `ajuda/P29-5.md` (Resposta).

### Problema 26
nível ·· no livro; Degrau 4

Usa: λ de um quarto de círculo, simetria com sinais opostos, integral no arco, orientação.

Na Fig. 22-50, uma barra fina de vidro forma uma semicircunferência de raio r = 5,00 cm. Uma carga +q = 4,50 pC está distribuída uniformemente na parte superior da barra, e uma carga −q = −4,50 pC está distribuída uniformemente na parte inferior da barra. Determine (a) o módulo e (b) a orientação (em relação ao semieixo x positivo) do campo elétrico \(\vec E\) no ponto P, situado no centro do semicírculo.

[FIGURA: Figura 22-50 reconstruída: semicircunferência de raio r à esquerda do ponto P, que fica na origem. O quarto de cima, no segundo quadrante, tem carga +q; o quarto de baixo, no terceiro quadrante, tem carga −q.]

Figura 22-50 (reconstruída a partir do PDF do livro).

**[CAMPO P26-a]** (a) |E| = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P26-a.md`. A página aceita 2 % de tolerância.

**[CAMPO P26-b]** (b) orientação θ = ______ °
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P26-b.md`. A página aceita 2 % de tolerância.

> Antes de pedir ajuda: já desenhou um pedaço de cima, o pedaço simétrico de baixo e os dois dE em P?

**[AJUDA de P26]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P26-1.md` (Dica 1: onde olhar), `ajuda/P26-2.md` (Dica 2: plano), `ajuda/P26-3.md` (Dica 3: primeiro passo), `ajuda/P26-4.md` (Resolução comentada), `ajuda/P26-5.md` (Resposta).

### Problema 31
nível ·· no livro; Degrau 5

Usa: λ com sinal, integral com a distância variando, sentido para carga negativa, limite "de longe".

Na Fig. 22-54, uma barra isolante, de comprimento L = 8,15 cm, tem uma carga −q = −4,23 fC uniformemente distribuída. (a) Qual é a densidade linear de carga da barra? Determine (b) o módulo e (c) a direção (em relação ao semieixo x positivo) do campo elétrico produzido no ponto P, situado no eixo x, a uma distância a = 12,0 cm da extremidade da barra. Determine o módulo do campo elétrico produzido em um ponto situado no eixo x, a uma distância a = 50 m do centro da barra, (d) pela barra e (e) por uma partícula de carga −q = −4,23 fC colocada no lugar anteriormente ocupado pelo centro da barra.

[FIGURA: Figura 22-54 reconstruída: barra com carga −q no eixo x, de comprimento L, à esquerda; o ponto P fica à direita, no eixo x, a uma distância a da ponta direita da barra.]

Figura 22-54 (reconstruída a partir do PDF do livro).

**[CAMPO P31-a]** (a) λ (com sinal) = ______ C/m
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P31-a.md`. A página aceita 2 % de tolerância.

**[CAMPO P31-b]** (b) |E| em P = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P31-b.md`. A página aceita 2 % de tolerância.

**[CAMPO P31-c]** (c) direção θ = ______ °
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P31-c.md`. A página aceita 2 % de tolerância.

**[CAMPO P31-d]** (d) barra, a 50 m do centro: |E| = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P31-d.md`. A página aceita 2 % de tolerância.

**[CAMPO P31-e]** (e) partícula no centro, a 50 m: |E| = ______ N/C
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P31-e.md`. A página aceita 2 % de tolerância.

> Antes de pedir ajuda: já converteu cm e fC para o SI? Já marcou no desenho de onde até onde vai a distância x de um pedacinho até P?

**[AJUDA de P31]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P31-1.md` (Dica 1: onde olhar), `ajuda/P31-2.md` (Dica 2: plano), `ajuda/P31-3.md` (Dica 3: primeiro passo), `ajuda/P31-4.md` (Resolução comentada), `ajuda/P31-5.md` (Resposta).

### Problema 38
nível ·· no livro; Degrau 6

Usa: fórmula do disco no eixo, Eₘ = σ/(2ε₀), leitura de gráfico, isolar R.

A Fig. 22-58a mostra um disco circular uniformemente carregado. O eixo central z é perpendicular ao plano do disco e a origem está no centro do disco. A Fig. 22-58b mostra o módulo do campo elétrico no eixo z em função do valor de z, em termos do valor máximo \(E_m\) do módulo do campo elétrico. A escala do eixo z é definida por \(z_s\) = 8,0 cm. Qual é o raio do disco?

[FIGURA: Figura 22-58 reconstruída. (a) Disco com o eixo z vertical passando pelo centro. (b) Gráfico do módulo do campo no eixo em função de z, de 0 a z s igual a 8,0 cm, com o eixo horizontal dividido em quatro partes iguais. Linhas de grade horizontais em E m e em 0,5 E m. A curva começa em E m em z igual a zero e decresce; ela cruza a linha de 0,5 E m exatamente na segunda linha vertical da grade e termina, em z s, perto de um quarto de E m.]

Figura 22-58 (reconstruída a partir do PDF do livro, ampliado; a curva foi conferida em três pontos da grade). Como no livro, só 0 e zₛ estão numerados no eixo z.

**[CAMPO P38-a]** Raio do disco, R = ______ cm
   → Escreva seu valor (marque a confiança 1–3) ANTES de abrir `conferir/P38-a.md`. A página aceita 2 % de tolerância.

> Antes de pedir ajuda: já descobriu quanto vale cada divisão do eixo z? Já achou um ponto da curva que cai bem num cruzamento da grade?

**[AJUDA de P38]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: `ajuda/P38-1.md` (Dica 1: onde olhar), `ajuda/P38-2.md` (Dica 2: plano), `ajuda/P38-3.md` (Dica 3: primeiro passo), `ajuda/P38-4.md` (Resolução comentada), `ajuda/P38-5.md` (Resposta).

## Síntese: que ferramenta uso neste problema?

Leia de cima para baixo e pare na primeira pergunta cuja resposta é "sim".

- A carga já está num campo conhecido, e pedem força, aceleração ou equilíbrio? Sim: \(\vec F = q\vec E\). Se q < 0, a força é oposta ao campo. (Degrau 1; P81.)

- As fontes são poucas cargas pontuais? Sim: \(E = k|q|/r^2\) para cada uma, setas desenhadas em P, soma vetorial. Antes de calcular, procure pares que se cancelam (lado + sinal, e |q| ∝ r²). Numa reta: sinais tirados do desenho (Degrau 2; P8). No plano: componentes pelo triângulo da geometria e ângulo pelo quadrante (Degrau 3; P9, P15).

- P está muito longe da distribuição (distância ≫ tamanho do objeto)? Sim: trate o objeto como carga pontual com a carga total. Erro ≈ (tamanho/2D)². (Degraus 5 e 6; P31 d–e.)

- A carga está espalhada (λ ou σ)? Sim: existe fórmula pronta para esta geometria (arco visto do centro, barra vista do prolongamento, anel ou disco vistos do eixo)? Use-a (Degraus 4–6; P29, P26, P31, P38). Se não existe: método do elemento — dq, dE, simetria, integral.

### Equações do capítulo: quando usar e quando não usar
| Equação | Use quando… | Não use quando… |
| \(\vec F = q\vec E\) | uma carga está num campo criado por outras cargas | quiser o efeito do campo de uma carga sobre ela mesma (uma carga não sente o próprio campo) |
| \(E = k\dfrac{|q|}{r^2}\) | partícula, ou esfera uniforme vista de fora | objeto extenso visto de perto (barra, arco, disco) |
| \(\vec E = \sum\vec E_i\) | há várias fontes: sempre como vetores | for somar módulos de campos com direções diferentes |
| \(E = \dfrac{2k\lambda}{r}\sin\dfrac{\varphi}{2}\) | centro de curvatura de um arco uniforme (com um só sinal) | o ponto não é o centro, ou o arco tem partes de sinais opostos (aí a componente que sobra muda: integre com seno) |
| \(E = \dfrac{k|q|}{a(a+L)}\) | P no prolongamento de uma barra uniforme, a uma distância a da ponta | P fora da reta da barra (aí há componentes; Fig. 22-14 do livro) |
| \(E = \dfrac{kqz}{(z^2+R^2)^{3/2}}\) | eixo de um anel uniforme | fora do eixo |
| \(E = \dfrac{\sigma}{2\varepsilon_0}\left(1 - \dfrac{z}{\sqrt{z^2+R^2}}\right)\) | eixo de um disco isolante uniforme | fora do eixo; condutor (Cap. 23) |
| \(E = \dfrac{\sigma}{2\varepsilon_0}\) | perto de uma placa grande (z ≪ R), longe das bordas | longe da placa ou perto das bordas |

## Revisão intercalada

Seis perguntas misturando os degraus, fora de ordem de propósito: na prova, ninguém avisa de que degrau é a questão. Marque a confiança antes de conferir.

**[PERGUNTA rev-1]** 1. Uma barra positiva de comprimento L tem P no prolongamento, a uma distância L da ponta. Usar \(kq/(\text{distância ao centro})^2\) dá um valor…
   a) maior que o real
   b) menor que o real
   c) igual ao real
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-1.md`.

**[PERGUNTA rev-2]** 2. Um próton e um elétron estão no mesmo ponto de um campo uniforme. As forças elétricas sobre eles têm…
   a) mesmo módulo e sentidos opostos
   b) mesmo módulo e mesmo sentido
   c) módulos diferentes, porque as massas são diferentes
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-2.md`.

**[PERGUNTA rev-3]** 3. Logo acima do centro de um disco isolante com σ = 5,3 µC/m², o campo vale aproximadamente:
   a) zero
   b) depende do raio do disco
   c) 3,0 × 10⁵ N/C
   d) 6,0 × 10⁵ N/C
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-3.md`.

**[PERGUNTA rev-4]** 4. Um campo tem \(E_x = +3{,}0\) N/C e \(E_y = -3{,}0\) N/C. A orientação em relação a +x é:
   a) 45°
   b) 135°
   c) −45°
   d) −135°
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-4.md`.

**[PERGUNTA rev-5]** 5. Um anel completo, de raio R, tem carga +Q uniforme. No centro, o campo vale:
   a) kQ/R²
   b) 2kQ/(πR²)
   c) kQ/(2R²)
   d) zero
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-5.md`.

**[PERGUNTA rev-6]** 6. Há +q a 1 cm à esquerda de P e +q a 1 cm à direita (campo zero em P). Você troca a da direita por −q. O campo em P…
   a) continua zero
   b) vale o dobro do campo de uma carga, para a direita
   c) vale o dobro do campo de uma carga, para a esquerda
   → Escolha e marque a confiança (1 chute, 2 acho, 3 certeza) ANTES de abrir `conferir/rev-6.md`.

### Onde você estava confiante e errou

Ainda não há respostas com confiança marcada.

### Plano de revisão

Espaçar a revisão fixa mais que estudar tudo de uma vez. Os problemas abaixo são ímpares (têm gabarito) e não estão neste guia; cada sessão mistura degraus.
| Quando | O que fazer | Degraus |
| Hoje (10 min) | Numa folha, sem olhar, refaça o exemplo do arco de 120° (Degrau 4) e o da barra de 10 cm (Degrau 5). Depois confira. | 4, 5 |
| +1 dia | Problemas 5, 41 e 7 do livro. | 1, 2, 3 |
| +3 dias | Problemas 11, 27 e 23. | 2, 4, 6 |
| +7 dias | Problemas 25, 37, 87 e 63, e uma questão deste guia que você só resolveu com ajuda de nível 3 ou mais. | 1 a 6 |

▸ [recolhido, abre ao clicar] Gabarito do livro para o plano de revisão
   P5: 56 pC. P41: (a) 1,5 × 10³ N/C; (b) 2,4 × 10⁻¹⁶ N; (c) para cima; (d) 1,6 × 10⁻²⁶ N; (e) 1,5 × 10¹⁰. P7: (1,02 × 10⁵ N/C) ĵ. P11: −30 cm. P27: (a) 23,8 N/C; (b) −90°. P23: 0,506. P25: (a) 1,62 × 10⁶ N/C; (b) −45°. P37: 28 %. P87: (a) (−1,80 N/C) î; (b) (43,2 N/C) î; (c) (−6,29 N/C) î. P63: (a) 8,87 × 10⁻¹⁵ N; (b) 120.
