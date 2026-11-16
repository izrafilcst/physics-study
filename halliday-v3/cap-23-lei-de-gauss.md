CAPÍTULO 23
Lei de Gauss
23-1 FLUXO ELÉTRICO
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
23.01 Saber que a lei de Gauss relaciona o campo elétrico em pontos de uma superfície fechada (real ou imaginária, chamada
superfície gaussiana) à carga total envolvida pela superfície.
23.02 Saber que o fluxo elétrico Φ através de uma superfície é a quantidade de campo elétrico que atravessa a superfície.
23.03 Saber que o vetor área de uma superfície plana é um vetor perpendicular à superfície cujo módulo é igual à área da
superfície.
23.04 Saber que qualquer superfície pode ser dividida em elementos de área que são suficientemente pequenos e
suficientemente planos para serem associados a um vetor elemento de área d , perpendicular ao elemento, cujo módulo é
igual à área do elemento.
23.05 Calcular o fluxo Φ do campo elétrico através de uma superfície integrando o produto escalar do vetor campo elétrico ,
pelo vetor elemento de área d .
23.06 No caso de uma superfície fechada, explicar os sinais algébricos associados a fluxos para dentro e para fora da
superfície.
23.07 Calcular o fluxo total Φ através de uma superfície fechada integrando o produto escalar do vetor campo elétrico pelo
vetor elemento de área d .
23.08 Determinar se uma superfície fechada pode ser dividida em partes (como as faces de um cubo) para simplificar a
integração usada para calcular o fluxo através da superfície.
Ideias-Chave
• O fluxo elétrico Φ através de uma superfície é a quantidade de campo elétrico que atravessa a superfície.
• O vetor área d de um elemento de área de uma superfície é um vetor perpendicular ao elemento cujo módulo é igual à área
dA do elemento.
• O fluxo elétrico Φ através de uma área cujo vetor elemento de área é d é dado pelo produto escalar:
• O fluxo elétrico total através de uma superfície é dado por
em que a integração é executada ao longo de toda a superfície.
• O fluxo total através de uma superfície fechada (que é usado na lei de Gauss) é dado por

em que a integração é executada ao longo de toda a superfície.
O que É Física?
No Capítulo 22, calculamos o campo elétrico em pontos próximos de objetos macroscópicos, como
barras. A técnica que usamos era trabalhosa: dividir a distribuição de carga em elementos de carga dq;
calcular os campos elétricos d produzidos pelos elementos; determinar as componentes desses campos
elétricos. Em seguida, verificar se alguns desses componentes se cancelavam. Finalmente, somar os
componentes que não se cancelavam integrando os elementos ao longo de todo o objeto, com várias
mudanças de notação durante o percurso.
Um dos principais objetivos da física é descobrir formas simples de resolver problemas
aparentemente complexos. Um dos instrumentos usados pela física para conseguir esse objetivo é a
simetria. Neste capítulo, discutimos uma bela relação entre carga e campo elétrico que nos permite, em
certas situações de alta simetria, calcular o campo elétrico produzido por objetos macroscópicos usando
poucas equações algébricas. Essa relação é chamada de lei de Gauss e foi descoberta pelo matemático e
físico Carl Friedrich Gauss (1777-1855).
Vamos começar com alguns exemplos simples que dão uma ideia do espírito da lei de Gauss. A Fig.
23-1 mostra uma partícula de carga +Q cercada por uma esfera imaginária cujo centro é a posição da
partícula. Em todos os pontos da esfera (chamada de superfície gaussiana) os vetores do campo elétrico
têm o mesmo módulo (dado por E = kQ/r2) e apontam radialmente para longe da partícula (porque a
partícula é positiva). As linhas de campo elétrico também apontam para longe da partícula e têm a mesma
densidade (já que, como vimos no Capítulo 22, a densidade de linha de campo elétrico é proporcional ao
módulo do campo elétrico). Dizemos que os vetores do campo elétrico e as linhas de campo elétrico
atravessam a superfície.
Figura 23-1 Os vetores do campo elétrico e as linhas de campo elétrico atravessam uma superfície gaussiana imaginária, esférica, que
envolve uma partícula de carga +Q.

Figura 23-2 Agora a carga da partícula envolvida pela superfície gaussiana é +2Q.
Figura 23-3 Qual é a carga central?
A Fig. 23-2 é igual à Fig. 23-1, exceto pelo fato de que a carga da partícula é +2Q. Como a carga
envolvida é duas vezes maior, o módulo dos vetores do campo elétrico que atravessam a (mesma)
superfície gaussiana é duas vezes maior que na Fig. 23-1, e a densidade das linhas de campo elétrico
também é duas vezes maior. Foram observações como essa que levaram à lei de Gauss:
A lei de Gauss relaciona os campos elétricos nos pontos de uma superfície gaussiana (fechada) à carga total envolvida pela superfície.
Vamos examinar um terceiro exemplo, mostrado na Fig. 23-3, em que uma partícula está no centro da
mesma superfície gaussiana esférica. Quais são o sinal e o valor absoluto da carga? Como os vetores do
campo elétrico apontam para a partícula, sabemos que a carga da partícula é negativa. Além disso, como
o comprimento dos vetores é metade do comprimento dos vetores da Fig. 23-1, concluímos que o valor
absoluto da carga é 0,5Q. (Usar a lei de Gauss é como saber qual é o presente examinando o papel em
que o presente está embrulhado.)
Os problemas discutidos neste capítulo são de dois tipos. Nos problemas do primeiro tipo,
conhecemos a carga e usamos a lei de Gauss para determinar o campo elétrico em um dado ponto; nos do
segundo tipo, conhecemos o campo elétrico em uma superfície gaussiana e usamos a lei de Gauss para
determinar a carga envolvida pela superfície. Entretanto, na maioria dos casos, não podemos usar a lei de
Gauss simplesmente observando o sentido e o comprimento dos vetores do campo elétrico em um
desenho, como acabamos de fazer; precisamos de uma grandeza física que descreva a quantidade de

campo elétrico que atravessa uma superfície. Essa grandeza é chamada de fluxo elétrico.
Fluxo Elétrico
Superfície Plana, Campo Uniforme. Começamos com uma superfície plana, de área A, em uma região
onde existe um campo elétrico uniforme . A Fig. 23-4a mostra um dos vetores de campo elétrico
atravessando um pequeno quadrado de área ΔA (em que Δ significa “pequeno”). Na verdade, apenas a
componente x (de módulo E = E cos θ na Fig. 23-4b) atravessa a superfície. A componente y é paralela à
x
superfície e não aparece na lei de Gauss. A quantidade de campo elétrico que atravessa a superfície é
chamada de fluxo elétrico ΔΦ e é dada pelo produto do campo que atravessa a superfície pela área
envolvida:
ΔΦ = (E cos θ) ΔA.
Existe outro modo de escrever o lado direito da equação anterior para que apenas a componente de
que atravessa a superfície seja considerada. Definimos um vetor área ∆ que é perpendicular ao
quadrado e tem um módulo igual à área do quadrado (Fig. 23-4c). Nesse caso, podemos escrever
Figura 23-4 (a) Um vetor de campo elétrico atravessa um pequeno quadrado de uma superfície plana. (b) Apenas a componente x
atravessa o quadrado; a componente y é paralela ao quadrado. (c) O vetor área do quadrado é perpendicular ao quadrado e tem um módulo
igual à área do quadrado.
e o produto escalar nos fornece automaticamente a componente de que é paralela a ∆ e, portanto,
atravessa o quadrado.
Para determinar o fluxo total Φ que atravessa a superfície da Fig. 23-4, somamos o fluxo que
atravessa todos os pequenos quadrados da superfície:
Entretanto, como não queremos ter o trabalho de somar centenas (ou mais) de valores do fluxo,
transformamos a soma em uma integral reduzindo os pequenos quadrados de área ΔA em elementos de

área dA. Nesse caso, o fluxo total passa a ser dado por
Agora podemos calcular o fluxo total integrando o produto escalar para toda a superfície.
Produto Escalar. Podemos calcular o produto escalar que aparece no integrando da Eq. 23-2
escrevendo os dois vetores na notação dos vetores unitários. Na Fig. 23-4, por exemplo, d = dAî e
poderia ser, digamos, (4î + 4ĵ ) N/C. Também podemos calcular o produto escalar na notação módulo-
ângulo, na qual o resultado seria E cos θ dA. Se o campo elétrico é uniforme e a superfície é plana, o
produto E cos θ é constante e pode ser colocado do lado de fora do sinal de integração. A integral
restante, ∫dA, é apenas uma receita para somar todos os quadrados elementares para obter a área total,
mas já sabemos que a área total é A. Assim, o fluxo total nessa situação simples é
Superfície Fechada. Para relacionar o fluxo à carga usando a lei de Gauss, precisamos de uma
superfície fechada. Vamos usar a superfície fechada da Fig. 23-5, que está submetida a um campo elétrico
não uniforme. (Não se preocupe. As superfícies serão mais simples nos deveres de casa.) Como antes,
vamos começar pelo fluxo através de pequenos quadrados. Agora, porém, estamos interessados, não só
em saber se as componentes do campo elétrico atravessam a superfície, mas também se elas atravessam a
superfície de dentro para fora (como na Fig. 23-1), ou de fora para dentro (como na Fig. 23-3).
Sinal do Fluxo. Para levar em conta o sentido com o qual o campo elétrico atravessa a superfície,
usamos, como antes, um vetor área, ∆ , mas agora escolhemos como positivo o sentido para fora (da
superfície fechada). Assim, se o vetor campo elétrico aponta para fora, o campo elétrico e o vetor área
apontam no mesmo sentido, o ângulo entre os vetores é θ = 0 e cos θ = 1. Isso significa que o produto
escalar . ∆ é positivo e, portanto, o fluxo é positivo. Se o vetor campo aponta para dentro, o campo
elétrico e o vetor área apontam em sentidos opostos, o ângulo entre os vetores é θ = 180o e cos θ = –1.
Nesse caso, o produto escalar . Δ é negativo e o fluxo é negativo. Se o vetor campo elétrico é
paralelo à superfície, o campo elétrico é perpendicular ao vetor área, o ângulo entre os vetores é θ = 90o
e cos θ = 0. Nesse caso, o produto escalar . Δ é nulo e o fluxo é zero. A Fig. 23-5 mostra exemplos
das três situações. A conclusão é a seguinte:

Figura 23-5 Uma superfície gaussiana de forma arbitrária em uma região onde existe um campo elétrico. A superfície está dividida em
pequenos quadrados de área ΔA. Os vetores campo elétrico e área Δ são mostrados para três quadrados representativos, 1, 2 e 3.
Se o sentido do campo elétrico é para fora da superfície, o fluxo é positivo; se o sentido do campo elétrico é para dentro da superfície, o
fluxo é negativo; se o campo elétrico é paralelo à superfície, o fluxo é zero.
Fluxo Total. Em princípio, para determinar o fluxo total através da superfície da Fig. 23-5,
poderíamos calcular o fluxo através de pequenos quadrados e somar os resultados (levando em conta os
sinais algébricos). Entretanto, não há necessidade de executar esse trabalho exaustivo. Em vez disso,
podemos reduzir o tamanho dos pequenos quadrados até se tornarem áreas elementares d e calcular o
resultado por integração:
O círculo no sinal de integral indica que a integral deve se estender a toda a superfície fechada, já que
estamos calculando o fluxo total através da superfície (o fluxo não precisa ser todo para fora ou todo

para dentro da superfície; na Fig. 23-5, por exemplo, existem partes da superfície em que o fluxo é para
dentro e outras partes em que o fluxo é para fora). Não se esqueça de que estamos interessados no fluxo
total para podermos aplicar a lei de Gauss, que relaciona o fluxo total à carga envolvida pela superfície.
(A lei será nossa próxima atração.) Note que o fluxo é uma grandeza escalar (é verdade que trabalhamos
com vetores de campo elétrico, mas o fluxo é a quantidade de campo elétrico que atravessa a superfície,
e não o campo em si). A unidade de fluxo do SI é o newton-metro quadrado por coulomb (N·m2/C).
Teste 1
A figura mostra um cubo gaussiano, cujas faces têm área A, imerso em um campo elétrico uniforme orientado no sentido
positivo do eixo z. Determine, em termos de E e A, o fluxo (a) através da face frontal do cubo (a face situada no plano xy), (b)
através da face traseira, (c) através da face superior e (d) através do cubo como um todo.
Exemplo 23.01 Fluxo de um campo uniforme através de uma superfície cilíndrica
A Fig. 23-6 mostra uma superfície gaussiana na forma de um cilindro oco, de raio R, cujo eixo é paralelo a um campo elétrico
uniforme. Qual é o fluxo Φ do campo elétrico através do cilindro?
IDEIAS-CHAVE
De acordo com a Eq. 23-4, podemos calcular o fluxo Φ integrando o produto escalar . d para toda a superfície do cilindro.
Entretanto, a superfície do cilindro não pode ser descrita por meio de uma única equação. A forma de contornar esse problema é
separar a superfície em partes que possam ser integradas com facilidade.
Cálculos: Podemos realizar a integração escrevendo o fluxo como a soma de três integrais: uma para a base esquerda do
cilindro, a, outra para a superfície lateral do cilindro, b, e outra para a base direita do cilindro, c. Nesse caso, de acordo com a Eq.
23-4,

Para todos os pontos da base a, o ângulo θ entre e d é 180o e o módulo E do campo é o mesmo. Assim,
em que ∫A é igual à área da base, A (= πr2). Analogamente, na base c, em que θ = 0 para todos os pontos,
Finalmente, para a superfície lateral b do cilindro, em que θ = 90o para todos os pontos,
Substituindo os três valores na Eq. 23-5, obtemos
Este resultado já era esperado; como todas as linhas de campo que representam o campo elétrico atravessam a superfície
gaussiana, entrando pela base esquerda e saindo pela base direita, o fluxo total deve ser nulo.
Figura 23-6 Uma superfície gaussiana cilíndrica, fechada pelos planos das bases, imersa em um
campo elétrico uniforme. O eixo do cilindro é paralelo à direção do campo.
Exemplo 23.02 Fluxo de um campo elétrico não uniforme através de um cubo
O cubo gaussiano que aparece na Fig. 23-7a está submetido a um campo elétrico não uniforme dado por = 3,0xî + 4,0ĵ, com E
em newtons por coulomb e x em metros. Qual é o fluxo elétrico na face direita, na face esquerda e na face superior do cubo? (As

outras faces serão consideradas no Exemplo 23.04.)
IDEIA-CHAVE
Podemos calcular o fluxo Φ através de uma superfície integrando o produto escalar . d ao longo da superfície.
Face direita: O vetor área é sempre perpendicular à superfície e aponta para fora. Assim, no caso da face direita do
cubo, o vetor d aponta no sentido positivo do eixo x. Um elemento desse tipo é mostrado nas Figs. 23-7b e 23-7c, mas o vetor d
tem a mesma direção para todos os elementos de área pertencentes a essa face. Na notação dos vetores unitários,
De acordo com a Eq. 23-4, o fluxo Φ através da face direita do cubo é dado por
d

Figura 23-7 (a) Um cubo gaussiano, com uma aresta no eixo x, imerso em um campo elétrico não
uniforme que depende do valor de x. (b) A cada elemento de área podemos associar um vetor
perpendicular ao elemento, que aponta para fora do cubo. (c) Face direita: a componente x do
campo atravessa a face e produz um fluxo positivo (para fora do cubo). A componente y não
atravessa a face e não produz um fluxo. (d) Face esquerda: a componente x do campo produz um
fluxo negativo (para dentro do cubo). (e) Face superior: a componente y do campo produz um fluxo
positivo (para fora do cubo).
Deveríamos calcular essa integral para a face direita, mas observamos que x tem o mesmo valor, 3,0 m, em todos os pontos da
face e, portanto, podemos substituir x por esse valor. Explicando melhor: Embora x seja uma variável quando percorremos a face
direita do cubo de cima para baixo e da esquerda para a direita, como a face direita do cubo é perpendicular ao eixo x, todos os
pontos da face têm a mesma coordenada x. (As coordenadas y e z não estão envolvidas na integração.) Assim, temos

A integral ∫dA nos dá simplesmente a área A = 4,0 m2 da face direita; assim,
Face esquerda: O método para calcular o fluxo através da face esquerda é o mesmo que foi usado para a face direita.
Apenas duas coisas mudam: (1) O vetor área elementar d agora aponta no sentido negativo do eixo x e, portanto, d = –dAî
(Fig. 23-7d). (2) O valor constante de x agora é 1,0 m. Com essas duas mudanças, verificamos que o fluxo Φ através da face
e
esquerda é dado por
Face superior: Como o vetor área elementar d agora aponta no sentido positivo do eixo y, d = dAĵ (Fig. 23-7e). O
fluxo Φ através da face superior é, portanto,
s
23-2 LEI DE GAUSS
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
23.09 Usar a lei de Gauss para relacionar o fluxo total Φ através de uma superfície fechada à carga total q envolvida pela
env
superfície.
23.10 Saber que o sinal algébrico da carga envolvida corresponde ao sentido (para fora ou para dentro) do fluxo através da
superfície gaussiana.
23.11 Saber que a carga do lado de fora de uma superfície gaussiana não contribui para o fluxo total através da superfície
fechada.
23.12 Calcular o módulo do campo elétrico produzido por uma partícula carregada usando a lei de Gauss.
23.13 Saber que, no caso de uma partícula carregada ou uma esfera uniformemente carregada, a lei de Gauss pode ser
aplicada usando uma superfície gaussiana que é uma esfera concêntrica com a carga ou com a esfera carregada.

Ideias-Chave
• A lei de Gauss relaciona o fluxo total Φ através de uma superfície fechada à carga total q envolvida pela superfície:
env
ε Φ = q (lei de Gauss).
0 env
• A lei de Gauss também pode ser escrita em termos do campo elétrico que atravessa a superfície gaussiana:
Lei de Gauss
A lei de Gauss relaciona o fluxo total Φ de um campo elétrico através de uma superfície fechada
(superfície gaussiana) à carga total q envolvida pela superfície. Em notação matemática,
env
Usando a Eq. 23-4, a definição de fluxo, podemos escrever a lei de Gauss na forma
As Eqs. 23-6 e 23-7 são válidas somente se, na região envolvida pela superfície gaussiana, existe apenas
vácuo ou ar (que, para efeitos práticos, quase sempre pode ser considerado equivalente ao vácuo). No
Capítulo 25, uma versão modificada da lei de Gauss será usada para analisar situações em que a região
contém materiais como mica, óleo e vidro.
Nas Eqs. 23-6 e 23-7, a carga total q é a soma algébrica das cargas positivas e negativas
env
envolvidas pela superfície gaussiana, e pode ser positiva, negativa ou nula. Incluímos o sinal, em vez de
usar o valor absoluto da carga envolvida, porque o sinal nos diz alguma coisa a respeito do fluxo total
através da superfície gaussiana: Se q é positiva, o fluxo é para fora; se q é negativa, o fluxo é para
env env
dentro.
A carga do lado de fora da superfície, mesmo que seja muito grande ou esteja muito próxima, não é
incluída no termo q da lei de Gauss. A localização das cargas no interior da superfície de Gauss é
env
irrelevante; as únicas coisas que importam para calcular o lado direito das Eqs. 23-6 e 23-7 são o valor
absoluto e o sinal da carga total envolvida. A grandeza do lado esquerdo da Eq. 23-7, por outro lado, é
o campo elétrico produzido por todas as cargas, tanto as que estão do lado de dentro da superfície de
Gauss como as que estão do lado de fora. Isso pode parecer incoerente, mas é preciso ter em mente o
seguinte fato: A contribuição do campo elétrico produzido por uma carga do lado de fora da superfície
gaussiana para o fluxo através da superfície é sempre nula, já que o número de linhas de campo que
entram na superfície devido a essa carga é igual ao número de linhas que saem.

Vamos aplicar essas ideias à Fig. 23-8, que mostra duas cargas pontuais, de mesmo valor absoluto e
sinais opostos, e as linhas de campo que descrevem os campos elétricos criados pelas cargas no espaço
em torno das cargas. A figura mostra também quatro superfícies gaussianas vistas de perfil. Vamos
discuti-las uma a uma.
Figura 23-8 Duas cargas pontuais, de mesmo valor absoluto e sinais opostos, e as linhas de campo que representam o campo elétrico.
Quatro superfícies gaussianas são vistas de perfil. A superfície S envolve a carga positiva. A superfície S envolve a carga negativa. A
1 2
superfície S não envolve nenhuma carga. A superfície S envolve as duas cargas.
3 4
Superfície S . O campo elétrico aponta para fora em todos os pontos da superfície. Isso significa que
1
o fluxo do campo elétrico através da superfície é positivo e, de acordo com a lei de Gauss, a carga
envolvida pela superfície também é positiva. (Em outras palavras, se Φ é positivo na Eq. 23-6, q
env
deve ser positiva.)
Superfície S . O campo elétrico aponta para dentro em todos os pontos da superfície. Isso significa
2
que o fluxo do campo elétrico é negativo e, de acordo com a lei de Gauss, a carga envolvida também
é negativa.
Superfície S . De acordo com a lei de Gauss, como a superfície não envolve nenhuma carga, o fluxo
3
do campo elétrico através da superfície é nulo. Isso é razoável, já que todas as linhas de campo que
entram na superfície pela parte de cima saem pela parte de baixo.
Superfície S . A carga total envolvida pela superfície é nula, já que as cargas envolvidas pela
4

superfície têm o mesmo valor absoluto e sinais opostos. Assim, de acordo com a lei de Gauss, o fluxo
do campo elétrico através dessa superfície deve ser zero. Isso é razoável, já que o número de linhas
de campo que entram na superfície pela parte de baixo é igual ao número de linhas de campo que
saem pela parte de cima.
O que aconteceria se colocássemos uma carga gigantesca Q nas proximidades da superfície S da Fig. 23-
4
8? A configuração de linhas de campo certamente seria modificada, mas o fluxo total através das quatro
superfícies gaussianas continuaria o mesmo. Isso é uma consequência do fato de que todas as linhas de
campo produzidas pela carga Q atravessariam totalmente as quatro superfícies gaussianas sem contribuir
para o fluxo total. O valor de Q não apareceria de nenhuma forma na lei de Gauss, já que Q estaria do
lado de fora das quatro superfícies gaussianas que estamos discutindo.
Teste 2
A figura mostra três situações nas quais um cubo gaussiano está imerso em um campo elétrico. As setas e valores indicam a
direção das linhas de campo e o módulo (em N · m2/C) do fluxo que atravessa as seis faces de cada cubo. (As setas mais claras
estão associadas às faces ocultas.) Em que situação o cubo envolve (a) uma carga total positiva, (b) uma carga total negativa e (c)
uma carga total nula?
Lei de Gauss e Lei de Coulomb
A lei de Gauss pode ser usada para determinar o campo elétrico produzido por uma partícula carregada.
Nesse caso, o campo tem simetria esférica (depende apenas da distância r entre o ponto considerado e a
partícula). Para tirar proveito dessa simetria, envolvemos a partícula em uma esfera gaussiana com
centro na partícula, como mostra a Fig. 23-9 para uma partícula com uma carga positiva q. Como todos
os pontos da superfície da esfera estão à mesma distância r da partícula, o campo elétrico tem o mesmo
valor E em todos os pontos da superfície da esfera, o que facilita bastante o cálculo da integral.

Figura 23-9 Uma superfície gaussiana esférica com centro em uma partícula de carga q.
O método a ser usado é o mesmo visto anteriormente. Escolhemos um elemento de área na superfície
da esfera e desenhamos um vetor área d perpendicular ao elemento, apontando para fora da esfera. A
simetria da situação mostra que o campo elétrico também é perpendicular à superfície da esfera e
aponta para fora da esfera, o que significa que o ângulo entre e d é θ = 0. Assim, a lei de Gauss nos
dá
em que q = q. Como o módulo E do campo elétrico é igual em todos os elementos de área, ele pode ser
env
colocado do lado de fora do sinal de integração, o que nos permite escrever
A integral restante é apenas uma receita para somar todas as áreas elementares, mas já sabemos que a
área total é 4πr2. Substituindo a integral pelo seu valor na Eq. 23-9, obtemos
A Eq. 23-10 é exatamente igual à Eq. 22-3, que obtivemos usando a lei de Coulomb.
Teste 3
Um fluxo Φ atravessa uma esfera gaussiana de raio r que envolve uma única partícula carregada. Suponha que a esfera gaussiana
i
seja substituída (a) por uma esfera gaussiana maior, (b) por um cubo gaussiano de lado r e (c) por um cubo gaussiano de lado 2r.
Em cada caso, o fluxo total através da nova superfície gaussiana é maior, menor ou igual a Φ?
i

Exemplo 23.03 Uso da lei de Gauss para determinar um campo elétrico
A Fig. 23-10a mostra, em seção reta, uma casca esférica de plástico de raio R = 10 cm e espessura desprezível, com carga Q = –
16e distribuída uniformemente. No centro da casca está uma partícula de carga q = +5e. Qual é o campo elétrico (módulo e
orientação) (a) em um ponto P situado a uma distância r = 6 cm do centro da casca e (b) em um ponto P situado a uma distância
1 1 2
r = 12,0 cm do centro da casca?
2
IDEIAS-CHAVE
(1) Como o sistema mostrado na Fig. 23-10a tem simetria esférica, é conveniente usar uma superfície gaussiana concêntrica com
a casca para determinar o campo elétrico. (2) Para calcular o campo elétrico em um ponto, devemos fazer a superfície gaussiana
passar por esse ponto (para que o campo em que estamos interessados seja o mesmo campo que aparece no produto escalar
da lei de Gauss). (3) A lei de Gauss relaciona o fluxo elétrico total através de uma superfície fechada à carga envolvida pela
superfície. As cargas externas são ignoradas.
Cálculos: Para determinar o campo no ponto P , construímos uma esfera gaussiana com P na superfície, ou seja, uma
1 1
esfera gaussiana de raio r . Como a carga envolvida pela esfera gaussiana é positiva, o fluxo elétrico através da superfície é
1
positivo e, portanto, aponta para fora da esfera. Assim, o campo atravessa a superfície de dentro para fora. Além disso, devido
à simetria esférica, é perpendicular à superfície, como mostra a Fig. 23-10b. A casca de plástico não aparece na figura porque está
do lado de fora da superfície gaussiana e, portanto, sua carga não é envolvida pela superfície.
Figura 23-10 (a) Uma casca de plástico carregada com uma partícula carregada no centro. (b)
Para determinar o campo elétrico no ponto P , construímos uma esfera gaussiana passando pelo
1

ponto. O campo elétrico atravessa a superfície da esfera de dentro para fora. O vetor área no
mesmo ponto aponta para fora. (c) Para determinar o campo elétrico no ponto P , construímos uma
2
esfera gaussiana passando pelo ponto. O campo elétrico atravessa a superfície de fora para dentro,
enquanto o vetor área no mesmo ponto aponta para fora.
Considere um elemento de área da esfera na posição do ponto P . O vetor elemento de área d aponta para fora (os
1
elementos de área sempre apontam para fora da superfície gaussiana) e é perpendicular à superfície da esfera. Assim, o ângulo θ
entre e d é zero. O lado esquerdo da Eq. 23-7 (lei de Gauss) se torna então
em que, na última passagem, passamos o módulo E do campo elétrico para fora da integral porque tem o mesmo valor em todos
os pontos da esfera gaussiana. A integral restante é simplesmente uma receita para calcular a área total de todos os elementos de
área da superfície esférica, mas já sabemos que a área da superfície da esfera é 4πr2. Substituindo esses resultados, a Eq. 23-7 nos
dá
ε E4πr2 = q .
0 env
A única carga envolvida pela superfície gaussiana que passa por P é a carga da partícula. Explicitando E e fazendo q = 5e e r =
1 env
r = 6,00 × 10–2 m, descobrimos que o módulo do campo elétrico no ponto P é
1 1
Para determinar o campo elétrico no ponto P , construímos uma esfera gaussiana com P na superfície. Dessa vez, a carga
2 2
total envolvida pela esfera gaussiana é q = q + Q = 5e + (–16e) = –11e. Como a carga total é negativa, os vetores campo
env
elétrico atravessam a superfície gaussiana de fora para dentro, como mostra a Fig. 23-10c. Assim, o ângulo θ entre e d é
180o, e o produto escalar dos dois vetores é E dA cos 180o = –E dA. Explicitando E na lei de Gauss e fazendo q = –11e e r = r =
env 2
12,00 × 10–2 m, obtemos

Note que, se tivéssemos usado um cubo gaussiano, em vez de respeitar a simetria esférica do problema usando uma esfera
gaussiana, o módulo e o ângulo do campo elétrico seriam diferentes em cada ponto da superfície do cubo e o cálculo da integral
se tornaria extremamente difícil.
Exemplo 23.04 Uso da lei de Gauss para determinar uma carga elétrica
Qual é a carga elétrica envolvida pelo cubo gaussiano do Exemplo 23.02?
IDEIA-CHAVE
A carga envolvida por uma superfície fechada (real ou imaginária) está relacionada ao fluxo elétrico total que atravessa a
superfície pela lei de Gauss, dada pela Eq. 23-6 (ε Φ = q ).
0 env
Fluxo: Para usar a Eq. 23-6, precisamos conhecer o fluxo que atravessa as seis faces do cubo. Já conhecemos o fluxo que
atravessa a face direita (Φ = 36 N · m2/C), o fluxo que atravessa a face esquerda (Φ = –12 N · m2/C) e o fluxo que atravessa a face
d e
de cima (Φ = 16 N · m2/C).
c
O cálculo do fluxo que atravessa a face de baixo é igual ao cálculo do fluxo que atravessa a face de cima, exceto pelo fato de
que, agora, o vetor área d aponta para baixo, no sentido negativo do eixo y (lembre-se de que o vetor área sempre aponta para
fora da superfície de Gauss). Nesse caso, d = – dAĵ e
Φ = 16 N · m2/C.
b
No caso da face dianteira, d = dA , e no caso da fase traseira, d = –dA . Quando calculamos o produto escalar do campo
elétrico = 3,0xî + 4,0ĵ por esses vetores área, o resultado é zero e, portanto, o fluxo elétrico através das duas faces é nulo. O
fluxo total através das seis faces é, portanto,
Φ=(36 – 12 + 16 – 16 + 0 + 0) N · m2/C
=24 N · m2/C.
Carga envolvida: Finalmente, usamos a lei de Gauss para calcular a carga q envolvida pelo cubo:
env
Assim, o cubo envolve uma carga total positiva.
23-3 UM CONDUTOR CARREGADO
Objetivos do Aprendizado

Depois de ler este módulo, você será capaz de ...
23.14 Usar a relação entre a densidade superficial de carga σ e a área da superfície para calcular a carga de um condutor.
23.15 Saber que, se uma carga em excesso (positiva ou negativa) for introduzida em um condutor isolado, a carga se
acumulará na superfície; o interior do condutor permanecerá neutro.
23.16 Conhecer o valor do campo elétrico no interior de um condutor isolado.
23.17 No caso de um condutor com uma cavidade que contém um objeto carregado, determinar a carga na superfície da
cavidade e na superfície externa do condutor.
23.18 Explicar de que forma a lei de Gauss é usada para determinar o módulo E do campo elétrico nas proximidades da
superfície de um condutor com uma densidade superficial de carga uniforme σ.
23.19 No caso de uma superfície uniformemente carregada de um condutor, conhecer a relação entre a densidade superficial de
carga σ e o módulo E do campo elétrico nas vizinhanças do condutor e a relação entre o sinal da carga e o sentido do
campo elétrico.
Ideias-Chave
• Todas as cargas em excesso de um condutor isolado se concentram na superfície externa do condutor.
• O campo no interior do um condutor carregado é zero e o campo elétrico nas proximidades do condutor é perpendicular à
superfície e tem um módulo proporcional à densidade superficial de carga:
Um Condutor Carregado
A lei de Gauss permite demonstrar um teorema importante a respeito dos condutores:
Se uma carga em excesso é introduzida em um condutor, a carga se concentra na superfície do condutor; o interior do condutor
permanece neutro.
Esse comportamento dos condutores é razoável, já que cargas do mesmo sinal se repelem. A ideia é que,
ao se acumularem na superfície, as cargas em excesso se mantêm afastadas o máximo possível umas das
outras. Podemos usar a lei de Gauss para demonstrar matematicamente essa afirmação.
A Fig. 23-11a mostra uma vista em corte de um pedaço de cobre, pendurado por um fio isolante,
com uma carga em excesso q. Colocamos uma superfície gaussiana logo abaixo da superfície do
condutor.

Figura 23-11 (a) Um pedaço de cobre, com uma carga q, pendurado por um fio isolante. Uma superfície gaussiana é colocada logo abaixo
da superfície do condutor. (b) O pedaço de cobre agora possui uma cavidade. Uma superfície gaussiana é colocada no interior do condutor,
perto da superfície da cavidade.
O campo elétrico no interior do condutor deve ser nulo; se não fosse assim, o campo exerceria uma
força sobre os elétrons de condução (elétrons livres), que estão sempre presentes em um condutor, e isso
produziria uma corrente elétrica. (Em outras palavras, haveria um movimento de cargas no interior do
condutor.) Como não pode haver uma corrente perpétua em um condutor que não faz parte de um circuito
elétrico, o campo elétrico deve ser nulo.
(Um campo elétrico interno existe durante certo tempo, enquanto o condutor está sendo carregado.
Entretanto, a carga adicional logo se distribui de tal forma que o campo elétrico interno se anula e as
cargas param de se mover. Quando isso acontece, dizemos que as cargas estão em equilíbrio
eletrostático.)
Se é zero em todos os pontos do interior do pedaço de cobre, deve ser zero em todos os pontos da
superfície gaussiana, já que a superfície escolhida, embora esteja próxima da superfície, fica no interior
do pedaço de cobre. Isso significa que o fluxo que atravessa a superfície gaussiana também é zero. De
acordo com a lei de Gauss, portanto, a carga total envolvida pela superfície de Gauss deve ser nula.
Como o excesso de carga não está no interior da superfície de Gauss, só pode estar na superfície do
condutor.
Um Condutor Carregado com uma Cavidade Interna
A Fig. 23-11b mostra o mesmo condutor, agora com uma cavidade interna. É talvez razoável supor que,

ao removermos o material eletricamente neutro para formar a cavidade, não mudamos a distribuição de
carga nem a configuração dos campos elétricos, que continuam sendo as mesmas da Fig. 23-11a. Vamos
usar a lei de Gauss para demonstrar matematicamente essa conjectura.
Colocamos uma superfície gaussiana envolvendo a cavidade, próximo da superfície, no interior do
condutor. Como = 0 no interior do condutor, o fluxo através dessa superfície também é nulo. Assim, a
superfície não pode envolver nenhuma carga. A conclusão é que não existe carga em excesso na
superfície da cavidade; toda a carga em excesso permanece na superfície externa do condutor, como na
Fig. 23-11a.
Remoção do Condutor
Suponha que, por um passe de mágica, fosse possível “congelar” as cargas em excesso na superfície do
condutor, talvez revestindo-as com uma fina camada de plástico, e que o condutor pudesse ser removido
totalmente. Isso seria equivalente a aumentar a cavidade da Fig. 23-11b até que ocupasse todo o condutor.
O campo elétrico não sofreria nenhuma alteração; continuaria a ser nulo no interior da fina camada de
carga e permaneceria o mesmo em todos os pontos do exterior. Isso mostra que o campo elétrico é criado
pelas cargas e não pelo condutor; este constitui apenas um veículo para que as cargas assumam suas
posições de equilíbrio.
O Campo Elétrico Externo
Vimos que as cargas em excesso de um condutor isolado se concentram na superfície do condutor. A
menos que o condutor seja esférico, porém, essas cargas não se distribuem de modo uniforme. Em outras
palavras, no caso de condutores não esféricos, a densidade superficial de carga σ (carga por unidade de
área) varia ao longo da superfície. Em geral, essa variação torna muito difícil determinar o campo
elétrico criado por cargas superficiais, a não ser nas proximidades da superfície, pois, nesse caso, o
campo elétrico pode ser determinado com facilidade usando a lei de Gauss. Para isso, consideramos uma
região da superfície suficientemente pequena para que possamos desprezar a curvatura e usamos um
plano para representar a região. Em seguida, imaginamos um pequeno cilindro gaussiano engastado na
superfície, como na Fig. 23-12: Uma das bases está do lado de dentro do condutor, a outra base está do
lado de fora, e o eixo do cilindro é perpendicular à superfície do condutor.

Figura 23-12 (a) Vista em perspectiva e (b) vista lateral de uma pequena parte de um condutor de grande extensão com uma carga
positiva na superfície. Uma superfície gaussiana cilíndrica, engastada perpendicularmente no condutor, envolve parte das cargas. Linhas de
campo elétrico atravessam a base do cilindro que está do lado de fora do condutor, mas não a base que está do lado de dentro. A base que
está do lado de fora tem área A e o vetor área é .
O campo elétrico na superfície e logo acima da superfície também é perpendicular à superfície.
Se não fosse, ele teria uma componente paralela à superfície do condutor que exerceria forças sobre as
cargas superficiais, fazendo com que elas se movessem. Esse movimento, porém, violaria nossa
suposição implícita de que estamos lidando com um corpo em equilíbrio eletrostático. Assim, é
perpendicular à superfície do condutor.
Vamos agora calcular o fluxo através da superfície gaussiana. Não há fluxo através da base que se
encontra dentro do condutor, já que, nessa região, o campo elétrico é nulo. Também não há fluxo através
da superfície lateral do cilindro, pois do lado de dentro do condutor o campo é nulo e do lado de fora o
campo elétrico é paralelo à superfície lateral do cilindro. Assim, o único fluxo que atravessa a superfície
gaussiana é o que atravessa a base que se encontra fora do condutor, em que é perpendicular ao plano
da base. Supomos que a área da base, A, é suficientemente pequena para que o módulo E do campo seja
constante em toda a base. Nesse caso, o fluxo através da base do cilindro é EA e esse é o fluxo total Φ
que atravessa a superfície gaussiana.
A carga q envolvida pela superfície gaussiana está na superfície do condutor e ocupa uma área A.
env
Se σ é a carga por unidade de área, q é igual a σA. Quando substituímos q por σA e Φ por EA, a lei de
env env
Gauss (Eq. 23-6) se torna
ε EA = σ ,
0 A
e, portanto,

Assim, o módulo do campo elétrico logo acima da superfície de um condutor é proporcional à densidade
superficial de carga do condutor. Se a carga do condutor é positiva, o campo elétrico aponta para fora do
condutor, como na Fig. 23-12; se é negativa, o campo elétrico aponta para dentro do condutor.
As linhas de campo da Fig. 23-12 devem terminar em cargas negativas externas ao condutor. Quando
aproximamos essas cargas do condutor, a densidade de carga local na superfície do condutor é
modificada, o que também acontece com o módulo do campo elétrico, mas a relação entre σ e E continua
a ser dada pela Eq. 23-11.
Exemplo 23.05 Casca metálica esférica, campo elétrico e carga
A Fig. 23-13a mostra uma seção reta de uma casca metálica esférica de raio interno R. Uma partícula com uma carga de –5,0 μC
está situada com o centro a uma distância R/2 do centro da casca. Se a casca é eletricamente neutra, quais são as cargas
(induzidas) na superfície interna e na superfície externa? Essas cargas estão distribuídas uniformemente? Qual é a configuração do
campo elétrico do lado de dentro e do lado de fora da casca?
IDEIAS-CHAVE
A Fig. 23-13b mostra uma seção reta de uma superfície gaussiana esférica no interior do metal, perto da superfície interna da
casca. O campo elétrico é zero no interior do metal (e, portanto, na superfície gaussiana, que está no interior do metal). Isso
significa que o fluxo elétrico através da superfície gaussiana também é zero. De acordo com a lei de Gauss, portanto, a carga total
envolvida pela superfície gaussiana é zero.
Raciocínio: Como existe uma carga de –5,0 μC no interior da casca, deve haver uma carga de +5,0 μC na superfície interna
da casca para que a carga envolvida seja zero. Se a partícula estivesse no centro de curvatura da casca, as cargas positivas estariam
distribuídas uniformemente ao longo da superfície interna da casca. Como, porém, a partícula está fora do centro, a distribuição
de carga positiva é assimétrica, como mostra a Fig. 23-13b; as cargas positivas tendem a se concentrar na parte da superfície
interna que está mais próxima da partícula (já que a carga da partícula é negativa).
Como a casca é eletricamente neutra, para que a superfície interna tenha uma carga de +5,0 μC é preciso que elétrons, com
uma carga total de –5,0 μC, sejam transferidos da superfície interna para a superfície externa, onde se distribuem uniformemente,
como mostra a Fig. 23-13b. A distribuição de carga negativa é uniforme porque a casca é esférica e porque a distribuição
assimétrica de carga positiva na superfície interna não pode produzir um campo elétrico no interior do metal para afetar a
distribuição de carga na superfície externa.

Figura 23-13 (a) Uma partícula com carga negativa está situada no interior de uma casca
metálica esférica eletricamente neutra. (b) Em consequência, cargas positivas se distribuem de
modo assimétrico na superfície interna da casca, e uma quantidade igual de carga negativa se
distribui uniformemente na superfície externa.
A Fig. 23-13b mostra também as linhas de campo do lado de dentro e do lado de fora da casca. Todas as linhas de campo
interceptam perpendicularmente as superfícies da casca e a superfície da partícula. Do lado de dentro da casca, a configuração de
linhas de campo é assimétrica por causa da assimetria da distribuição de carga positiva. Do lado de fora, o padrão é o mesmo que
se a carga pontual estivesse no centro de curvatura e a casca não existisse. Na verdade, a configuração seria a mesma para
qualquer posição da carga pontual no interior da casca.
23-4 APLICAÇÕES DA LEI DE GAUSS: SIMETRIA CILÍNDRICA
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
23.20 Explicar como a lei de Gauss pode ser usada para calcular o módulo do campo elétrico do lado de fora de uma linha de
carga ou do lado de fora da superfície de um cilindro de material isolante (uma barra de plástico, por exemplo) com uma
densidade linear de carga uniforme λ.
23.21 Conhecer a relação entre a densidade linear de carga λ em uma superfície cilíndrica e o módulo E do campo elétrico a
uma distância r do eixo central da superfície cilíndrica.
23.22 Explicar como a lei de Gauss pode ser usada para calcular o módulo E do campo elétrico no interior de um cilindro
isolante (uma barra de plástico, por exemplo) com uma densidade volumétrica de carga uniforme ρ.
Ideia-Chave
• O campo elétrico em um ponto nas proximidades de uma linha de carga (ou barra cilíndrica), de comprimento infinito, com uma
densidade linear de carga uniforme λ é perpendicular à linha, e o módulo do campo é dado por

em que r é a distância entre o ponto e a linha.
Aplicações da Lei de Gauss: Simetria Cilíndrica
A Fig. 23-14 mostra uma parte de uma barra de plástico cilíndrica, de comprimento infinito, com uma
densidade linear uniforme de carga positiva λ. Vamos obter uma expressão para o módulo do campo
elétrico a uma distância r do eixo da barra. Poderíamos fazer isso usando o método do Capítulo 22
(usar uma carga elementar dq, que produziria um campo elementar d , etc.). Entretanto, a lei de Gauss
permite resolver o problema de uma forma muito mais simples (e mais elegante).
Figura 23-14 Uma superfície gaussiana cilíndrica envolvendo parte de uma barra de plástico cilíndrica, de comprimento infinito, com uma
densidade linear uniforme de carga positiva.
A distribuição de carga e a configuração do campo elétrico têm simetria cilíndrica. Para calcular o
campo a uma distância r, envolvemos um trecho da barra com um cilindro gaussiano concêntrico, de raio
r e altura h. (Para determinar o campo elétrico em um ponto, devemos fazer a superfície gaussiana passar
por esse ponto.) Em seguida, usamos a lei de Gauss para relacionar a carga envolvida pelo cilindro ao
fluxo total do campo elétrico através da superfície do cilindro.
Para começar, observe que, por causa da simetria, o campo elétrico em qualquer ponto do espaço
aponta radialmente para longe da barra (porque a carga da barra é positiva; se a carga fosse negativa, o
campo elétrico apontaria radialmente para o eixo da barra). Isso significa que, nas bases do cilindro, o
campo elétrico é paralelo à superfície e, portanto, o fluxo através das bases do cilindro é zero.
Para calcular o fluxo através da superfície lateral do cilindro, note que, em todos os elementos de
área da superfície lateral, o vetor área d aponta radialmente para longe do cilindro (para fora da
superfície gaussiana), ou seja, na mesma direção e no mesmo sentido que o campo elétrico. Assim, o
produto escalar que aparece na lei de Gauss é simplesmente E dA cos 0o = E dA, e podemos passar E

para fora da integral. A integral restante é simplesmente uma receita para somar as áreas de todos os
elementos de área da superfície lateral do cilindro, mas já sabemos que o resultado é o produto da altura
h do cilindro pela circunferência da base, 2πr. O fluxo total através do cilindro é, portanto,
Φ = EA cos θ = E(2 πrh) cos 0 = E(2 πrh).
Do outro lado da lei de Gauss, temos a carga q envolvida pelo cilindro. Como a densidade linear
env
de carga (carga por unidade de comprimento) é uniforme, a carga envolvida é λh. Assim, a lei de Gauss,
ε Φ = q ,
0 env
ε E(2 πrh) = λh,
0
nos dá
Esse é o campo elétrico produzido por uma linha de carga infinitamente longa em um ponto situado a uma
distância r da linha. O campo aponta radialmente para longe da linha de carga, se a carga for positiva,
e radialmente na direção da linha de carga, se a carga for negativa. A Eq. 23-12 também fornece o valor
aproximado do campo produzido por uma linha de carga finita em pontos não muito próximos das
extremidades da linha (em comparação com a distância da linha).
Se a barra possui uma densidade volumétrica de carga ρ uniforme, podemos usar um método
semelhante para calcular o módulo do campo elétrico no interior da barra. Para isso, basta reduzir o raio
do cilindro gaussiano da Fig. 23-14 até que a superfície lateral do cilindro esteja no interior da barra.
Nesse caso, como a densidade de carga é uniforme, a carga q envolvida pelo cilindro será
env
proporcional ao volume do cilindro.
Exemplo 23.06 A lei de Gauss e uma descarga para cima em uma tempestade elétrica
A mulher da Fig. 23-15 estava em uma plataforma de observação do Sequoia National Park quando uma grande nuvem de
tempestade passou no céu. Muitos elétrons de condução do corpo da mulher foram repelidos para a terra pela base da nuvem,
negativamente carregada (Fig. 23-16a), o que deixou o corpo da mulher positivamente carregado. Observando a fotografia da
Fig. 23-15, é possível concluir que o corpo da mulher está carregado, já que os fios de cabelo se repelem mutuamente e se
projetam para cima ao longo das linhas de campo elétrico produzidas pela carga do corpo.

Courtesea da NOAA
Figura 23-15 Uma nuvem de tempestade deixou esta mulher positivamente carregada.
A mulher não foi atingida por um relâmpago, mas estava correndo um sério risco, pois o campo elétrico estava a ponto de
causar uma ruptura dielétrica no ar à sua volta. Essa ruptura teria ocorrido ao longo de uma trajetória ascendente, o que é
chamado de descarga para cima. Uma descarga para cima é perigosa porque a ionização que produz nas moléculas do ar libera
um grande número de elétrons. Se a mulher da Fig. 23-15 tivesse provocado uma descarga para cima, os elétrons livres do ar
teriam sido atraídos para o seu corpo (Fig. 23-16b), produzindo um choque possivelmente fatal. Um choque elétrico é perigoso
porque, dependendo da intensidade, pode interromper a respiração ou os batimentos cardíacos, além de causar queimaduras.
Vamos modelar o corpo da mulher como um cilindro vertical estreito, de altura L = 1,8 m e raio R = 0,10 m (Fig. 23-16c).
Suponha que a carga Q esteja uniformemente distribuída ao longo do cilindro e que a ruptura dielétrica ocorra quando o módulo
do campo elétrico excede o valor crítico E = 2,4 MN/C. Para qual valor de Q o ar em volta da mulher está a ponto de sofrer uma
c
ruptura dielétrica?
IDEIAS-CHAVE
Como R << L, podemos aproximar a distribuição de carga por uma linha comprida de carga. Além disso, como estamos supondo
que a distribuição de carga é uniforme, o módulo do campo elétrico é dado aproximadamente pela Eq. 23-12 (E = λ/2πε r).
0
Cálculos: Substituindo o campo elétrico E pelo valor crítico E, a distância radial r pelo raio do cilindro R, e a densidade
c
linear de carga λ pela razão Q/L, temos

ou
Substituindo as constantes por valores numéricos, temos
Figura 23-16 (a) Muitos elétrons de condução do corpo da mulher foram repelidos para a terra
pela base da nuvem, negativamente carregada, o que deixou o corpo positivamente carregado. (b)
Em uma descarga para cima, o ar sofre uma ruptura dielétrica, permitindo que elétrons livres
criados no ar sejam atraídos para o corpo da mulher. (c) O corpo da mulher pode ser representado
por um cilindro.
23-5 APLICAÇÕES DA LEI DE GAUSS: SIMETRIA PLANAR
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
23.23 Usar a lei de Gauss para calcular o módulo E do campo elétrico nas proximidades de uma superfície plana, isolante, de
grandes dimensões, com uma densidade superficial de carga uniforme σ.
23.24 No caso de pontos nas proximidades de uma superfície plana, isolante, de grandes dimensões, com uma densidade
superficial de carga uniforme σ, conhecer a relação entre a densidade de carga e o módulo E do campo elétrico e a relação
entre o sinal da carga e o sentido do campo elétrico.
23.25 No caso de pontos nas proximidades de duas superfícies planas, condutoras, de grandes dimensões, com uma
densidade superficial de carga σ, conhecer a relação entre a densidade de carga e o módulo E do campo elétrico e a
relação entre o sinal das cargas e o sentido do campo elétrico.

Ideias-Chave
• O campo elétrico produzido por uma placa isolante infinita com uma densidade superficial de carga σ é perpendicular ao plano
da placa e tem um módulo proporcional à densidade superficial de carga da placa:
• O campo elétrico entre duas placas condutoras carregadas é perpendicular ao plano das placas e tem um módulo proporcional
à densidade superficial de carga das placas:
Aplicações da Lei de Gauss: Simetria Planar
Placa Isolante
A Fig. 23-17 mostra uma parte de uma placa fina, infinita, isolante, com uma densidade superficial de
carga positiva σ. Uma folha de plástico, com uma das superfícies uniformemente carregada, pode ser um
bom modelo. Vamos calcular o campo elétrico a uma distância r da placa.
Uma superfície gaussiana adequada para esse tipo de problema é um cilindro com o eixo
perpendicular à placa e com uma base de cada lado da placa, como mostra a figura. Por simetria, é
perpendicular à placa e, portanto, às bases do cilindro. Além disso, como a carga é positiva, aponta
para longe da placa, e, portanto, as linhas de campo elétrico atravessam as duas bases do cilindro no
sentido de dentro para fora. Como as linhas de campo são paralelas à superfície lateral do cilindro, o
produto . d é nulo nessa parte da superfície gaussiana. Assim, . d é igual a E dA nas bases do
cilindro e é igual a zero na superfície lateral. Nesse caso, a lei de Gauss,
nos dá

Figura 23-17 (a) Vista em perspectiva e (b) vista lateral de uma pequena parte de uma placa de grande extensão com uma carga positiva
na superfície. Uma superfície gaussiana cilíndrica, com o eixo perpendicular à placa e uma base de cada lado da placa, envolve parte das
cargas.
em que σA é a carga envolvida pela superfície gaussiana. Explicitando E, obtemos
Como estamos considerando uma placa infinita com uma densidade de carga uniforme, esse resultado é
válido para qualquer ponto que esteja a uma distância finita da placa. A Eq. 23-13 é igual à Eq. 22-27,
que foi obtida por integração das componentes do campo elétrico produzido por elementos de carga.
Duas Placas Condutoras
A Fig. 23-18a mostra uma vista de perfil de uma placa condutora fina, infinita, com um excesso de carga
positiva. Como vimos no Módulo 23-3, a carga em excesso está na superfície da placa. Como a placa é
fina e muito extensa, podemos supor que praticamente toda a carga em excesso está nas duas faces
maiores da placa.
Se não existe um campo elétrico externo para forçar as cargas positivas a assumirem determinada
distribuição, as cargas se distribuem uniformemente nas duas faces com uma densidade superficial de
carga σ . De acordo com a Eq. 23-11, essas cargas criam, nas proximidades da superfície, um campo
1
elétrico de módulo E = σ /ε . Como a carga em excesso é positiva, o campo aponta para longe da placa.
1 0
A Fig. 23-18b mostra uma placa do mesmo tipo com um excesso de carga negativa e uma densidade
superficial de carga com o mesmo valor absoluto σ . A única diferença é que, agora, o campo aponta na
1
direção da placa.
Suponha que as placas das Figs. 23-18a e 23-18b sejam colocadas lado a lado (Fig. 23-18c). Como
as placas são condutoras, quando as aproximamos, as cargas em excesso de uma placa atraem as cargas
em excesso da outra, e todas as cargas em excesso se concentram na superfície interna das placas, como

mostra a Fig. 23-18c. Como existe agora uma quantidade de carga duas vezes maior nas superfícies
internas, a nova densidade superficial de carga (que vamos chamar de σ) nas faces internas é 2σ . Assim,
1
o módulo do campo elétrico em qualquer ponto entre as placas é dado por
Esse campo aponta para longe da placa positiva e na direção da placa negativa. Como não existe excesso
de carga nas faces externas, o campo elétrico do lado de fora das placas é zero.
Como as cargas das placas se moveram quando as placas foram aproximadas, a Fig. 23-18c não é a
superposição das Figs. 23-18a e 23-18b; em outras palavras, a distribuição de carga no sistema de duas
placas não é simplesmente a soma das distribuições de carga das placas isoladas.
A razão pela qual nos damos ao trabalho de discutir situações tão pouco realistas como os campos
produzidos por uma placa infinita carregada e um par de placas infinitas carregadas é que a análise de
situações “infinitas” permite obter boas aproximações para problemas reais. Assim, a Eq. 23-13 vale
também para uma placa isolante finita, contanto que estejamos lidando com pontos próximos da placa e
razoavelmente distantes das bordas. A Eq. 23-14 se aplica a um par de placas condutoras finitas, contanto
que não estejamos lidando com pontos muito próximos das bordas. O problema das bordas de uma placa,
e o motivo pelo qual procuramos, na medida do possível, nos manter afastados delas, é que, perto de uma
borda, não podemos usar a simetria planar para determinar as expressões dos campos. Perto da borda, as
linhas de campo são curvas (é o chamado efeito de borda) e os campos elétricos são muito difíceis de
expressar matematicamente.
Figura 23-18 (a) Uma placa condutora fina, infinita, com um excesso de carga positiva. (b) Uma placa do mesmo tipo com um excesso de
carga negativa. (c) As duas placas colocadas lado a lado.
Exemplo 23.07 Campo elétrico nas proximidades de duas placas isolantes carregadas paralelas
A Fig. 23-19a mostra partes de duas placas de grande extensão, isolantes, paralelas, com uma carga uniforme do lado esquerdo.
Os valores das densidades superficiais de carga são σ = 6,8 μC/m2 para a placa positivamente carregada e σ = 4,3 μC/m2 para
(+) (–)
a placa negativamente carregada.
Determine o campo elétrico (a) à esquerda das placas, (b) entre as placas e (c) à direita das placas.

IDEIA-CHAVE
Como as cargas estão fixas (as placas são isolantes), podemos determinar os campos elétricos produzidos pelas placas da Fig. 23-
19a (1) calculando o campo de cada placa como se a outra não existisse e (2) somando algebricamente os resultados. (Não há
necessidade de usar uma soma vetorial porque os campos são paralelos.)
Cálculos: Em qualquer ponto, o campo elétrico produzido pela placa positiva aponta para longe da placa e, de acordo
(+)
com a Eq. 23-13, tem o módulo dado por
Em qualquer ponto, o campo elétrico produzido pela placa negativa aponta na direção da placa e tem um módulo dado por
(–)
A Fig. 23-19b mostra os campos criados pelas placas à esquerda das placas (E), entre as placas (C) e à direita das placas (D).
Os campos resultantes nas três regiões podem ser obtidos usando o princípio de superposição. À esquerda, o módulo do
campo é
Figura 23-19 (a) Duas placas de grande extensão, isolantes, paralelas, com uma carga uniforme
do lado esquerdo. (b) Campos elétricos criados pelas duas placas. (c) Campo total criado pelas
duas placas, obtido por superposição.

Como E é maior que E , o campo elétrico total nessa região aponta para a esquerda, como mostra a Fig. 23-19c. À direita
(+) (–) E
das placas, o campo elétrico tem o mesmo módulo, mas aponta para a direita, como mostra a Fig. 23-19c.
D
Entre as placas, os dois campos se somam e temos
O campo elétrico aponta para a direita.
C
23-6 APLICAÇÕES DA LEI DE GAUSS: SIMETRIA ESFÉRICA
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
23.26 Saber que uma casca esférica com uma distribuição uniforme de carga atrai ou repele uma partícula carregada situada do
lado de fora da casca como se toda a carga da casca estivesse concentrada no centro da casca.
23.27 Saber que uma casca esférica com uma distribuição uniforme de carga não exerce nenhuma força eletrostática sobre
uma partícula carregada situada no interior da casca.
23.28 No caso de um ponto situado do lado de fora de uma casca esférica com uma distribuição uniforme de carga, conhecer a
relação entre o módulo E do campo elétrico, a carga q da casca e a distância r entre o ponto e o centro da casca.
23.29 No caso de um ponto situado no interior de uma casca esférica com uma distribuição uniforme de carga, conhecer o valor
do módulo E do campo elétrico.
23.30 No caso de uma esfera com uma distribuição uniforme de carga, determinar o módulo e a orientação do campo elétrico
em pontos no interior da esfera e do lado de fora da esfera.
Ideias-Chave
• Em um ponto do lado de fora de uma casca esférica com uma carga q distribuída uniformemente, o campo elétrico produzido
pela casca é radial (orientado para fora da casca ou na direção do centro da casca, dependendo do sinal da carga), e o módulo
do campo é dado pela equação
em que r é a distância entre o ponto e o centro da casca. O campo seria o mesmo se toda a carga estivesse concentrada no
centro da casca.
• Em todos os pontos do interior de uma casca esférica com uma distribuição uniforme de carga, o campo elétrico criado pela
casca é zero.
• Em um ponto do interior de uma esfera com uma distribuição uniforme de carga, o campo elétrico é radial e o módulo do

campo é dado pela equação
em que q é a carga da esfera, R é o raio da esfera e r é a distância entre o ponto e o centro da esfera.
Aplicações da Lei de Gauss: Simetria Esférica
Vamos agora usar a lei de Gauss para demonstrar os dois teoremas das cascas que foram apresentados no
Módulo 21-1. O primeiro diz o seguinte:
Uma partícula carregada situada do lado de fora de uma casca esférica com uma distribuição uniforme de carga é atraída ou repelida
como se toda a carga estivesse situada no centro da casca.
A Fig. 23-20 mostra uma casca esférica carregada, de raio R, com uma carga total q e duas superfícies
gaussianas concêntricas, S e S . Quando usamos o método do Módulo 23-2 e aplicamos a lei de Gauss à
1 2
superfície S , para a qual r ≥ R, o resultado é o seguinte:
2
Figura 23-20 Vista em seção reta de uma casca esférica fina, uniformemente carregada, com uma carga total q. Duas superfícies
gaussianas, S e S , também são mostradas. A superfície S envolve a casca, e a superfície S envolve apenas a cavidade vazia que existe no
1 2 2 1
interior da casca.
Esse campo é igual ao que seria criado por uma carga pontual q localizada no centro da casca. Assim, a
força que uma casca de carga q exerce sobre uma partícula carregada situada do lado de fora da casca é a
mesma que a força exercida por uma partícula pontual de carga q situada no centro da casca. Fica assim
demonstrado o primeiro teorema das cascas.
O segundo teorema das cascas diz o seguinte:

Uma partícula carregada situada no interior de uma casca esférica com uma distribuição uniforme de carga não é atraída nem repelida
pela casca.
Aplicando a lei de Gauss à superfície S , para a qual r < R, obtemos
1
já que a superfície S não envolve nenhuma carga. Assim, se existe uma partícula carregada no interior da
1
casca, a casca não exerce nenhuma força sobre a partícula. Fica assim demonstrado o segundo teorema
das cascas.
Toda distribuição de carga esfericamente simétrica, como a distribuição de raio R e densidade
volumétrica de carga ρ da Fig. 23-21, pode ser substituída por um conjunto de cascas esféricas
concêntricas. Para fins de aplicação dos dois teoremas das cascas, a densidade volumétrica de carga ρ
deve ter um valor único para cada casca, mas não precisa ser a mesma para todas as cascas. Assim, para
a distribuição de carga como um todo, ρ pode variar, mas apenas em função de r, a distância radial a
partir do centro de curvatura. Podemos, portanto, caso seja necessário, examinar o efeito da distribuição
de carga “camada por camada”.
Na Fig. 23-21a, todas as cargas estão no interior de uma superfície gaussiana com r > R. As cargas
produzem um campo elétrico na superfície gaussiana como se houvesse apenas uma carga pontual situada
no centro, e a Eq. 23-15 pode ser aplicada.
A Fig. 23-21b mostra uma superfície gaussiana com r < R. Para determinar o campo elétrico em
pontos da superfície gaussiana, consideramos dois conjuntos de cascas carregadas: um conjunto do lado
de dentro da superfície gaussiana e outro conjunto do lado de fora. De acordo com a Eq. 23-16, as cargas
do lado de fora da superfície gaussiana não criam um campo elétrico na superfície gaussiana. De acordo
com a Eq. 23-15, as cargas do lado de dentro da superfície gaussiana criam o mesmo campo que uma
carga pontual de mesmo valor situada no centro. Chamando essa carga de q′, podemos escrever a Eq. 23-
15 na forma

Figura 23-21 Os pontos representam uma esfera feita de material isolante com uma distribuição de carga de simetria esférica e raio R,
cuja densidade volumétrica de carga ρ é função apenas da distância do centro. Uma superfície gaussiana concêntrica com r > R é mostrada
em (a). Uma superfície gaussiana semelhante, com r < R, é mostrada em (b).
Uma vez que a distribuição de carga no interior da esfera de raio R é uniforme, podemos calcular
a carga q′ envolvida por uma superfície esférica de raio r (Fig. 23-21b) usando a seguinte relação:
ou

o que nos dá
Substituindo na Eq. 23-17, obtemos
Teste 4
A figura mostra duas placas de grande extensão, paralelas, isolantes, com densidades superficiais de carga iguais, uniformes e
positivas, e uma esfera com uma densidade volumétrica de carga uniforme e positiva. Coloque em ordem decrescente os quatro
pontos numerados, de acordo com o módulo do campo elétrico existente no local.
Revisão e Resumo
Lei de Gauss A lei de Gauss e a lei de Coulomb são formas diferentes de descrever a relação entre
carga e campo elétrico em situações estáticas. A lei de Gauss é expressa pela equação
em que q é a carga total no interior de uma superfície imaginária fechada (conhecida como superfície
env
gaussiana) e Φ é o fluxo total do campo elétrico através da superfície:
A lei de Coulomb pode ser demonstrada a partir da lei de Gauss.
Aplicações da Lei de Gauss Usando a lei de Gauss e, em alguns casos, princípios de simetria, é
possível demonstrar várias propriedades importantes de sistemas eletrostáticos, entre as quais as

seguintes:
1. As cargas em excesso de um condutor estão concentradas na superfície externa do condutor.
2. O campo elétrico externo nas vizinhanças da superfície de um condutor carregado é perpendicular à
superfície e tem um módulo dado por
em que σ é a densidade superficial de carga.
No interior do condutor, E = 0.
3. O campo elétrico produzido em um ponto do espaço por uma linha de carga infinita com densidade
linear de carga uniforme λ é perpendicular à linha de carga e tem um módulo dado por
em que r é a distância entre o ponto e a linha de carga.
4. O campo elétrico produzido por uma placa isolante infinita com densidade superficial de carga
uniforme σ é perpendicular ao plano da placa e tem um módulo dado por
5. O campo elétrico em um ponto do lado de fora de uma casca esférica uniformemente carregada, de
raio R e carga total q, aponta na direção radial e tem um módulo dado por
em que r é a distância entre o ponto e o centro da casca. (A carga se comporta, para pontos externos,
como se estivesse concentrada no centro da esfera.) O campo do lado de dentro de uma casca
esférica uniformemente carregada é zero:
6. O campo elétrico em um ponto no interior de uma esfera uniformemente carregada aponta na
direção radial e tem um módulo dado por
em que q é a carga da esfera, R é o raio da esfera e r é a distância entre o ponto e o centro da casca.

Perguntas
1 O vetor área de uma superfície é = (2î + 3ĵ )m2. Qual é o fluxo de um campo elétrico através da
superfície, se o campo é (a) = 4î N/C e (b) = 4 N/C?
2 A Fig. 23-22 mostra, em seção reta, três cilindros maciços de comprimento L e carga uniforme Q.
Concêntrica com cada cilindro, existe uma superfície gaussiana cilíndrica; as três superfícies gaussianas
têm o mesmo raio. Coloque as superfícies gaussianas em ordem decrescente do módulo do campo
elétrico em qualquer ponto da superfície.
Figura 23-22 Pergunta 2.
3 A Fig. 23-23 mostra, em seção reta, uma esfera central metálica, duas cascas metálicas e três
superfícies gaussianas esféricas concêntricas de raio R, 2R e 3R. As cargas dos três corpos, distribuídas
uniformemente, são as seguintes: esfera, Q; casca menor, 3Q; casca maior, 5Q. Coloque as três
superfícies gaussianas em ordem decrescente do módulo do campo elétrico em qualquer ponto da
superfície.
Figura 23-23 Pergunta 3.
4 A Fig. 23-24 mostra, em seção reta, duas esferas gaussianas e dois cubos gaussianos, no centro dos
quais existe uma partícula de carga positiva. (a) Coloque as quatro superfícies gaussianas em ordem
decrescente do fluxo elétrico que as atravessa. (b) Coloque as quatro superfícies gaussianas em ordem
decrescente do módulo do campo elétrico em qualquer ponto da superfície, e informe se os módulos são
uniformes ou variam de ponto para ponto da superfície.

Figura	23-24 	Pergunta	4.
5			Na	Fig.	23-25,	um	elétron	é	liberado	entre	duas	placas	infinitas	isolantes	horizontais,	com	densidades
superficiais	de	carga	σ 	e	σ ,	como	mostra	a	figura.	O	elétron	é	submetido	às	três	situações	mostradas
(+) (–)
na	tabela	a	seguir,	que	envolvem	as	densidades	superficiais	de	carga	e	a	distância	entre	as	placas.
Coloque	as	situações	em	ordem	decrescente	do	módulo	da	aceleração	do	elétron.
| Situação | σ   | σ   | Distância |
| -------- | --- | --- | --------- |
|          | (+) | (–) |           |
| 1        | +4σ | –4σ | d         |
| 2        | +4σ | –σ  | 4d        |
| 3        | +4σ | –5σ | 9d        |
Figura	23-25 	Pergunta	5.
6			Três	placas	infinitas	isolantes,	com	densidades	superficiais	de	carga	positivas	σ,	2σ	e	3σ,	foram
alinhadas	paralelamente,	como	as	duas	barras	da	Fig.	23-19a.	Qual	é	a	ordem	das	placas,	da	esquerda
para	a	direita,	se	o	campo	elétrico	 	produzido	pelas	barras	tem	módulo	E	=	0	em	uma	região	e	E	=	2σ/ε
0
em	outra	região?
7	 	 	 A	 Fig.	 23-26	 mostra	 as	 seções	 retas	 de	 quatro	 conjuntos	 de	 barras	 finas	 e	 muito	 compridas,
perpendiculares	ao	plano	da	figura.	O	valor	abaixo	de	cada	barra	indica	a	densidade	linear	uniforme	de
carga	da	barra,	em	microcoulombs	por	metro.	As	barras	estão	separadas	por	distâncias	d	ou	2d,	e	um
ponto	central	é	mostrado	a	meio	caminho	entre	as	barras	internas.	Coloque	os	conjuntos	em	ordem
decrescente	do	módulo	do	campo	elétrico	no	ponto	central.

Figura 23-26 Pergunta 7.
8 A Fig. 23-27 mostra quatro esferas maciças, todas com uma carga Q distribuída uniformemente. (a)
Coloque as esferas em ordem decrescente de acordo com a densidade volumétrica de carga. A figura
mostra também um ponto P para cada esfera, todos à mesma distância do centro da esfera. (b) Coloque as
esferas em ordem decrescente de acordo com o módulo do campo elétrico no ponto P.
Figura 23-27 Pergunta 8.
9 Uma pequena esfera carregada está no interior de uma casca esférica metálica, de raio R. Para três
situações, as cargas da esfera e da casca, respectivamente, são (1) +4q, 0; (2) –6q, +10q; (3) +16q, –12q.
Coloque as situações em ordem decrescente, de acordo com a carga (a) da superfície interna da casca e
(b) da superfície externa da casca.
10 Coloque em ordem decrescente as situações da Pergunta 9, de acordo com o módulo do campo
elétrico (a) no centro da casca e (b) em um ponto a uma distância 2R do centro da casca.
11 A Fig. 23-28 mostra uma parte de três longos cilindros carregados com o mesmo eixo. O cilindro
central A tem uma carga uniforme q = +3q . Que cargas uniformes devem ter os cilindros q e q para
A 0 B C
que (se for possível) o campo elétrico total seja zero (a) no ponto 1, (b) no ponto 2 e (c) no ponto 3?

Figura 23-28 Pergunta 11.
12 A Fig. 23-29 mostra quatro superfícies gaussianas de mesma superfície lateral cilíndrica e bases
diferentes. As superfícies estão em uma região onde existe um campo elétrico uniforme paralelo ao
eixo central dos cilindros. As formas das bases são as seguintes: S , hemisférios convexos; S ,
1 2
hemisférios côncavos; S , cones; S , discos planos. Coloque as superfícies em ordem decrescente, de
3 4
acordo (a) com o fluxo elétrico total e (b) com o fluxo elétrico através das bases superiores.
Figura 23-29 Pergunta 12.
Problemas
. - ... O número de pontos indica o grau de dificuldade do problema.
Informações adicionais disponíveis em O Circo Voador da Física de Jearl Walker,
LTC, Rio de Janeiro, 2008.
Módulo 23-1 Fluxo Elétrico
·1 A superfície quadrada da Fig. 23-30 tem 3,2 mm de lado e está imersa em um campo elétrico
uniforme de módulo E = 1800 N/C e com linhas de campo fazendo um ângulo de 35o com a normal, como
mostra a figura. Tome essa normal como apontando “para fora”, como se a superfície fosse a tampa de
uma caixa. Calcule o fluxo elétrico através da superfície.

Figura 23-30 Problema 1.
··2 Um campo elétrico dado por = 4,0î – 3,0(y2 + 2,0)ĵ, em que está em newtons por coulomb e y
está em metros, atravessa um cubo gaussiano com 2,0 m de aresta, posicionado da forma mostrada na Fig.
23-7. Determine o fluxo elétrico (a) através da face superior, (b) através da face inferior, (c) através da
face da esquerda e (d) através da face traseira. (e) Qual é o fluxo elétrico total através do cubo?
··3 O cubo da Fig. 23-31 tem 1,40 m de aresta e está orientado da forma mostrada na figura em uma
região onde existe um campo elétrico uniforme. Determine o fluxo elétrico através da face direita do
cubo se o campo elétrico, em newtons por coulomb, é dado por (a) 6,00î, (b) –2,00ĵ e (c) –3,00î + 4,00 .
(d) Qual é o fluxo total através do cubo nos três casos?
Figura 23-31 Problemas 3, 6 e 9.
Módulo 23-2 Lei de Gauss
·4 Na Fig. 23-32, uma rede para pegar borboletas está imersa em um campo elétrico uniforme de
módulo E = 3,0 mN/C, com o aro, um círculo de raio a = 11 cm, perpendicular à direção do campo. A
rede é eletricamente neutra. Determine o fluxo elétrico através da rede.

Figura 23-32 Problema 4.
·5 Na Fig. 23-33, um próton está uma distância d/2 do centro de um quadrado de aresta d. Qual é o
módulo do fluxo elétrico através do quadrado? (Sugestão: Pense no quadrado como uma das faces de um
cubo de aresta d.)
Figura 23-33 Problema 5.
·6 Em todos os pontos da superfície do cubo da Fig. 23-31, o campo elétrico é paralelo ao eixo z. O
cubo tem 3,0 m de aresta. Na face superior do cubo, = –34 N/C; na face inferior, = +20 N/C.
Determine a carga que existe no interior do cubo.
·7 Uma carga pontual de 1,8 μC está no centro de uma superfície gaussiana cúbica de 55 cm de aresta.
Qual é o fluxo elétrico através da superfície?
··8 Quando um chuveiro é aberto em um banheiro fechado, os respingos de água no piso do boxe
podem encher o ar de íons negativos e produzir um campo elétrico no ar de até 1000 N/C. Considere um
banheiro de dimensões 2,5 m × 3,0 m × 2,0 m. Suponha que no teto, no piso e nas quatro paredes o campo
elétrico no ar seja perpendicular à superfície e possua um módulo uniforme de 600 N/C. Suponha também
que o teto, o piso e as paredes formem uma superfície gaussiana que envolva o ar do banheiro. Determine
(a) a densidade volumétrica de carga ρ e (b) o número de cargas elementares e em excesso por metro
cúbico de ar.
··9 A Fig. 23-31 mostra uma superfície gaussiana com a forma de um cubo com 1,40 m de aresta.
Determine (a) o fluxo Φ através da superfície e (b) a carga q envolvida pela superfície se = 3,00yĵ
env
N/C, com y em metros; os valores de (c) Φ e (d) q se = [–4,00î + (6,00 + 3,00y)ĵ ] N/C.
env
··10 A Fig. 23-34 mostra uma superfície gaussiana com a forma de um cubo de 2,00 m de aresta, imersa
em um campo elétrico dado por = (3,00x + 4,00)î + 6,00ĵ + 7,00 N/C, com x em metros. Qual é a
carga total contida no cubo?
Figura 23-34 Problema 10.

··11 A Fig. 23-35 mostra uma superfície gaussiana com a forma de um cubo de 2,00 m de aresta, com
um vértice no ponto x = 5,00 m, y = 4,00 m. O cubo está imerso em um campo elétrico dado por = –
1 1
3,00î – 4,00y2ĵ + 3,00 N/C, com y em metros. Qual é a carga total contida no cubo?
Figura 23-35 Problema 11.
··12 A Fig. 23-36 mostra duas cascas esféricas isolantes mantidas fixas no lugar. A casca 1 possui uma
densidade superficial de carga uniforme de +6,0 μC/m2 na superfície externa e um raio de 3,0 cm; a casca
2 possui uma densidade superficial de carga uniforme de +4,0 μC/m2 na superfície externa e um raio de
2,0 cm; os centros das cascas estão separados por uma distância L = 10 cm. Qual é o campo elétrico no
ponto x = 2,0 cm, na notação dos vetores unitários?
Figura 23-36 Problema 12.
··13 Observa-se experimentalmente que o campo elétrico em uma região da atmosfera terrestre aponta
verticalmente para baixo. A uma altitude de 300 m, o campo tem um módulo de 60,0 N/C; a uma altitude
de 200 m, o módulo é 100 N/C. Determine a carga em excesso contida em um cubo com 100 m de aresta
e faces horizontais a 200 e 300 m de altitude.
··14 Fluxo e cascas isolantes. Uma partícula carregada está suspensa no centro de duas cascas
esféricas concêntricas muito finas, feitas de um material isolante. A Fig. 23-37a mostra uma seção reta do
sistema e a Fig. 23-37b mostra o fluxo Φ através de uma esfera gaussiana com centro na partícula em
função do raio r da esfera. A escala do eixo vertical é definida por Φ = 5,0 × 105 N · m2/C. (a)
s
Determine a carga da partícula central. (b) Determine a carga da casca A. (c) Determine a carga da casca
B.

Figura 23-37 Problema 14.
··15 Uma partícula de carga +q é colocada em um dos vértices de um cubo gaussiano. Determine o
múltiplo de q/ε que corresponde ao fluxo (a) através de uma das faces do cubo que contêm o vértice e
0
(b) através de uma das outras faces do cubo.
···16 A superfície gaussiana, em forma de paralelepípedo, da Fig. 23-38 envolve uma carga de +24,0ε
0
C e está imersa em um campo elétrico, que é fornecido por = [(10,0 + 2,00x)î – 3,00ĵ + bz ] N/C, com
x e z em metros e b uma constante. A face inferior está no plano xz; a face superior está no plano
horizontal que passa pelo ponto y = 1,00 m. Qual é o valor de b para x = 1,00 m, x = 4,00 m, z = 1,00
2 1 2 1
m e z = 3,00 m?
2
Figura 23-38 Problema 16.
Módulo 23-3 Um Condutor Carregado
·17 Uma esfera condutora uniformemente carregada com 1,2 m de diâmetro possui uma densidade
superficial de carga 8,1 μC/m2. Determine (a) a carga da esfera e (b) o fluxo elétrico através da
superfície da esfera.
·18 O campo elétrico nas vizinhanças da superfície lateral de um cilindro condutor tem um módulo E de
2,3 × 105 N/C. Qual é a densidade superficial de carga do cilindro?
·19 Os veículos espaciais que atravessam os cinturões de radiação da Terra podem interceptar um
número significativo de elétrons. O acúmulo de carga resultante pode danificar componentes eletrônicos e
prejudicar o funcionamento de alguns circuitos. Suponha que um satélite esférico feito de metal, com 1,3
m de diâmetro, acumule 2,4 μC de carga. (a) Determine a densidade superficial de carga do satélite. (b)
Calcule o módulo do campo elétrico nas vizinhanças do satélite devido à carga superficial.

·20 Fluxo e cascas condutoras. Uma partícula carregada é mantida no centro de duas cascas esféricas
condutoras concêntricas, cuja seção reta aparece na Fig. 23-39a. A Fig. 23-39b mostra o fluxo Φ através
de uma esfera gaussiana com centro na partícula em função do raio r da esfera. A escala do eixo vertical
é definida por Φ = 5,0 × 105 N · m2/C. Determine (a) a carga da partícula central, (b) a carga da casca A
s
e (c) a carga da casca B.
Figura 23-39 Problema 20.
··21 Um condutor possui uma carga de +10 × 10–6 C. No interior do condutor existe uma cavidade; no
interior da cavidade está uma carga pontual q = +3,0 × 10–6 C. Determine a carga (a) da superfície da
cavidade e (b) da superfície externa do condutor.
Módulo 23-4 Aplicações da Lei de Gauss: Simetria Cilíndrica
·22 Um elétron é liberado a partir do repouso a 9,0 cm de distância de uma barra isolante retilínea
muito longa com uma densidade de carga uniforme de 6,0 μC por metro. Qual é o módulo da aceleração
inicial do elétron?
·23 (a) O cilindro condutor de uma máquina tem um comprimento de 42 cm e um diâmetro de 12 cm. O
campo elétrico nas proximidades da superfície do cilindro é 2,3 × 105 N/C. Qual é a carga total do
cilindro? (b) O fabricante deseja produzir uma versão compacta da máquina. Para isso, é necessário
reduzir o comprimento do cilindro para 28 cm e o diâmetro para 8,0 cm. O campo elétrico na superfície
do tambor deve permanecer o mesmo. Qual deve ser a carga do novo cilindro?
·24 A Fig. 23-40 mostra uma seção de um tubo longo, de metal, de parede finas, com raio R = 3,00 cm e
carga por unidade de comprimento λ = 2,00 × 10–8 C/m. Determine o módulo E do campo elétrico a uma
distância radial (a) r = R/2,00 e (b) r = 2,00R. (c) Faça um gráfico de E em função de r para 0 ≤ r ≤
2,00R.

Figura 23-40 Problema 24.
·25 Uma linha infinita de carga produz um campo de módulo 4,5 × 104 N/C a uma distância de 2,0 m.
Calcule a densidade linear de carga.
··26 A Fig. 23-41a mostra um cilindro fino, maciço, carregado, e uma casca cilíndrica coaxial, também
carregada. Os dois objetos são feitos de material isolante e possuem uma densidade superficial de carga
uniforme na superfície externa. A Fig. 23-41b mostra a componente radial E do campo elétrico em função
da distância radial r a partir do eixo comum. A escala do eixo vertical é definida por E = 3,0 × 103 N/C.
s
Qual é a densidade linear de carga da casca?
Figura 23-41 Problema 26.
··27 Um fio reto longo possui cargas negativas fixas com uma densidade linear de 3,6 nC/m. O fio é
envolvido por uma casca coaxial cilíndrica, isolante, de paredes finas, com 1,5 cm de raio. A casca
possui uma carga positiva na superfície externa, com uma densidade superficial σ, que anula o campo
elétrico do lado de fora da casca. Determine o valor de σ.
··28 Uma carga de densidade linear uniforme 2,0 nC/m está distribuída ao longo de uma barra longa,
fina, isolante. A barra está envolvida por uma casca longa, cilíndrica, coaxial, condutora (raio interno:
5,0 cm; raio externo: 10 cm). A carga da casca é zero. (a) Determine o módulo do campo elétrico a 15 cm
de distância do eixo da casca. (b) Determine a densidade superficial de carga na superfície interna e (c)
na superfície externa da casca.
··29 A Fig. 23-42 é uma seção de uma barra condutora de raio R = 1,30 mm e comprimento L = 11,00
1

m no interior de uma casca coaxial, de paredes finas, de raio R = 10,0R e mesmo comprimento L. A
2 1
carga da barra é Q = +3,40 × 10–12 C; a carga da casca é Q = –2,00Q . Determine (a) o módulo E e (b) a
1 2 1
direção (para dentro ou para fora) do campo elétrico a uma distância radial r = 2,00R . Determine (c) E e
2
(d) a direção do campo elétrico para r = 5,00R . Determine a carga (e) na superfície interna e (f) na
1
superfície externa da casca.
Figura 23-42 Problema 29.
··30 A Fig. 23-43 mostra pequenas partes de duas linhas de carga paralelas, muito compridas,
separadas por uma distância L = 8,0 cm. A densidade uniforme de carga das linhas é +6,0 μC/m para a
linha 1 e –2,0 μC/m para a linha 2. Em que ponto do eixo x o campo elétrico é zero?
Figura 23-43 Problema 30.
··31 Duas cascas cilíndricas longas, carregadas, coaxiais, de paredes finas, têm 3,0 e 6,0 m de raio. A
carga por unidade de comprimento é 5,0 × 10–6 C/m na casca interna e –7,0 × 10–6 C/m na casca externa.
Determine (a) o módulo E e (b) o sentido (para dentro ou para fora) do campo elétrico a uma distância
radial r = 4,0 cm. Determine (c) o módulo E e (d) o sentido do campo elétrico para r = 8,0 cm.
···32 Um cilindro maciço, longo, isolante, com 4,0 cm de raio, possui uma densidade volumétrica de
carga não uniforme ρ que é uma função da distância radial r a partir do eixo do cilindro: ρ = Ar2. Se A =
2,5 μC/m5, determine o módulo do campo elétrico (a) para r = 3,0 cm e (b) para r = 5,0 cm.
Módulo 23-5 Aplicações da Lei de Gauss: Simetria Planar
·33 Na Fig. 23-44, duas placas finas, condutoras, de grande extensão, são mantidas paralelas a uma

pequena distância uma da outra. Nas faces internas, as placas têm densidades superficiais de carga de
sinais opostos e valor absoluto 7,00 × 10–22 C/m2. Determine o campo elétrico, na notação dos vetores
unitários, (a) à esquerda das placas, (b) à direita das placas e (c) entre as placas.
Figura 23-44 Problema 33.
·34 Na Fig. 23-45, um pequeno furo circular de raio R = 1,80 cm foi aberto no meio de uma placa fina,
infinita, isolante, com uma densidade superficial de carga σ = 4,50 pC/m2. O eixo z, cuja origem está no
centro do furo, é perpendicular à placa. Determine, na notação dos vetores unitários, o campo elétrico no
ponto P, situado em z = 2,56 cm. (Sugestão: Use a Eq. 22-26 e o princípio de superposição.)
Figura 23-45 Problema 34.
·35 A Fig. 23-46a mostra três placas de plástico de grande extensão, paralelas e uniformemente
carregadas. A Fig. 23-46b mostra a componente x do campo elétrico em função de x. A escala do eixo
vertical é definida por E = 6,0 × 105 N/C. Determine a razão entre a densidade de carga na placa 3 e a
s
densidade de carga na placa 2.

Figura 23-46 Problema 35.
·36 A Fig. 23-47 mostra as seções retas de duas placas de grande extensão, paralelas, isolantes,
positivamente carregadas, ambas com uma distribuição superficial de carga σ = 1,77 × 10–22 C/m2.
Determine o campo elétrico , na notação dos vetores unitários, (a) acima das placas, (b) entre as placas
e (c) abaixo das placas.
Figura 23-47 Problema 36.
·37 Uma placa metálica quadrada, de 8,0 cm de lado e espessura insignificante, possui uma carga total
de 6,0 × 10–6 C. (a) Estime o valor do módulo E do campo elétrico perto do centro da placa (a 0,50 mm
do centro, por exemplo) supondo que a carga está distribuída uniformemente pelas duas faces da placa.
(b) Estime o valor de E a 30 m de distância (uma distância grande, em comparação com as dimensões da
placa) supondo que a placa é uma carga pontual.
··38 Na Fig. 23-48a, um elétron é arremessado verticalmente para cima, com uma velocidade v = 2,0 ×
s
105 m/s, a partir das vizinhanças de uma placa uniformemente carregada. A placa é isolante e muito
extensa. A Fig. 23-48b mostra a velocidade escalar v em função do tempo t até o elétron voltar ao ponto
de partida. Qual é a densidade superficial de carga da placa?

Figura 23-48 Problema 38.
··39 Na Fig. 23-49, uma pequena esfera isolante, de massa m = 1,0 mg e carga q = 2,0 × 10–8 C
(distribuída uniformemente em todo o volume), está pendurada em um fio isolante que faz um ângulo θ =
30o com uma placa vertical, isolante, uniformemente carregada (vista em seção reta). Considerando a
força gravitacional a que a esfera está submetida e supondo que a placa possui uma grande extensão,
calcule a densidade superficial de carga σ da placa.
Figura 23-49 Problema 39.
··40 A Fig. 23-50 mostra uma placa isolante, muito extensa, que possui uma densidade superficial de
carga uniforme σ = –2,00 μC/m2; a figura mostra também uma partícula de carga Q = 6,00 μC, a uma
distância d da placa. Ambas estão fixas no lugar. Se d = 0,200 m, para qual coordenada (a) positiva e (b)
negativa do eixo x (além do infinito) o campo elétrico total é zero? (c) Se d = 0,800 m, para qual
tot
coordenada do eixo x o campo é zero?
tot
Figura 23-50 Problema 40.
··41 Um elétron é arremessado na direção do centro de uma placa metálica que possui uma densidade

superficial de carga de –2,0 × 10–6 C/m2. Se a energia cinética inicial do elétron é 1,60 × 10–17 J e o
movimento do elétron muda de sentido (devido à repulsão eletrostática da placa) a uma distância
insignificante da placa, de que distância da placa o elétron foi arremessado?
··42 Duas grandes placas de metal com 1,0 m2 de área são mantidas paralelas a 5,0 cm de distância e
possuem cargas de mesmo valor absoluto e sinais opostos nas superfícies internas. Se o módulo E do
campo elétrico entre as placas é 55 N/C, qual é o valor absoluto da carga em cada placa? Despreze o
efeito de borda.
···43 A Fig. 23-51 mostra uma seção reta de uma placa isolante, muito extensa, com uma espessura d =
9,40 mm e uma densidade volumétrica de carga uniforme ρ = 5,80 fC/m3. A origem do eixo x está no
centro da placa. Determine o módulo do campo elétrico (a) em x = 0, (b) em x = 2,00 mm, (c) em x =
4,70 mm e (d) em x = 26,0 mm.
Figura 23-51 Problema 43.
Módulo 23-6 Aplicações da Lei de Gauss: Simetria Esférica
·44 A Fig. 23-52 mostra o módulo do campo elétrico do lado de dentro e do lado de fora de uma esfera
com uma distribuição uniforme de carga positiva em função da distância do centro da esfera. A escala do
eixo vertical é definida por E = 5,0 × 107 N/C. Qual é a carga da esfera?
s
Figura 23-52 Problema 44.
·45 Duas cascas esféricas concêntricas carregadas têm raios de 10,0 cm e 15,0 cm. A carga da casca
menor é 4,00 × 10–8 C e a da casca maior é 2,00 × 10–8 C. Determine o campo elétrico (a) em r = 12,0 cm
e (b) em r = 20,0 cm.
·46 Uma esfera isolante, carregada, de raio R, possui uma densidade de carga negativa uniforme, exceto
por um túnel estreito que atravessa totalmente a esfera, passando pelo centro. Um próton pode ser

colocado em qualquer ponto do túnel ou de um prolongamento do túnel. Seja F o módulo da força
R
eletrostática a que é submetido o próton quando está na superfície da esfera. Determine, em termos de R,
a que distância da superfície fica o ponto no qual o módulo da força é 0,50F quando o próton se
R
encontra (a) em um prolongamento do túnel e (b) dentro do túnel.
·47 Uma esfera condutora com 10 cm de raio tem uma carga desconhecida. Se o módulo do campo
elétrico a 15 cm do centro da esfera é 3,0 × 103 N/C e o campo aponta para o centro da esfera, qual é a
carga da esfera?
··48 Uma partícula carregada é mantida fixa no centro de uma casca esférica. A Fig. 23-53 mostra o
módulo E do campo elétrico em função da distância radial r. A escala do eixo vertical é definida por E =
s
10,0 × 107 N/C. Estime o valor da carga da casca.
Figura 23-53 Problema 48.
··49 Na Fig. 23-54, uma esfera maciça, de raio a = 2,00 cm, é concêntrica com uma casca esférica
condutora de raio interno b = 2,00a e raio externo c = 2,40a. A esfera possui carga uniforme q = +5,00
1
fC, e a casca, uma carga q = –q . Determine o módulo do campo elétrico (a) em r = 0, (b) em r = a/2,00,
2 1
(c) em r = a, (d) em r = 1,50a, (e) em r = 2,30a e (f) em r = 3,50a. Determine a carga (g) na superfície
interna e (h) na superfície externa da casca.
Figura 23-54 Problema 49.
··50 A Fig. 23-55 mostra duas cascas esféricas isolantes mantidas fixas no lugar no eixo x. A casca 1

possui uma densidade superficial de carga uniforme +4,0 μC/m2 na superfície externa e um raio de 0,50
cm, enquanto a casca 2 possui uma densidade superficial de carga uniforme –2,0μC/m2 na superfície
externa e um raio de 2,00 cm; a distância entre os centros é L = 6,0 cm. Determine o(s) ponto(s) do eixo x
(além do infinito) em que o campo elétrico é zero.
Figura 23-55 Problema 50.
··51 Na Fig. 23-56, uma casca esférica, isolante, com um raio interno a = 2,00 cm e um raio externo b =
2,40 cm, possui uma densidade volumétrica uniforme de carga positiva ρ = A/r, em que A é uma constante
e r é a distância em relação ao centro da casca. Além disso, uma pequena esfera de carga q = 45,0 fC
está situada no centro da casca. Qual deve ser o valor de A para que o campo elétrico no interior da
casca (a ≤ r ≤ b) seja uniforme?
Figura 23-56 Problema 51.
··52 A Fig. 23-57 mostra uma casca esférica com uma densidade volumétrica de carga uniforme ρ =
1,84 nC/m3, raio interno a = 10,0 cm e raio externo b = 2,00a. Determine o módulo do campo elétrico (a)
em r = 0, (b) em r = a/2,00, (c) em r = a, (d) em r = 1,50a, (e) em r = b e (f) em r = 3,00b.

Figura 23-57 Problema 52.
···53 Uma esfera isolante, de raio R = 5,60 cm, possui uma distribuição de carga não uniforme ρ =
(14,1 pC/m3)r/R, em que r é a distância do centro da esfera. (a) Determine a carga da esfera. (b)
Determine o módulo E do campo elétrico em r = 0, (c) em r = R/2,00 e (d) em r = R. (e) Faça um gráfico
de E em função de r.
···54 A Fig. 23-58 mostra, em seção reta, duas esferas de raio R, com distribuições volumétricas
uniformes de carga. O ponto P está na reta que liga os centros das esferas, a uma distância R/2,00 do
centro da esfera 1. Se o campo elétrico no ponto P é zero, qual é a razão q /q entre a carga da esfera 2 e
2 1
a carga da esfera 1?
Figura 23-58 Problema 54.
···55 Uma distribuição de carga não uniforme, de simetria esférica, produz um campo elétrico de
módulo E = Kr4, em que K é uma constante e r é a distância do centro da esfera. O campo aponta para
longe do centro da esfera. Qual é a distribuição volumétrica de carga ρ?
Problemas Adicionais
56 O campo elétrico em uma região do espaço é dado por = (x + 2)î N/C, com x em metros.
Considere uma superfície gaussiana cilíndrica, de raio 20 cm, coaxial com o eixo x. Uma das bases do
cilindro está em x = 0. (a) Determine o valor absoluto do fluxo elétrico através da outra base do cilindro,
situada em x = 2,0 m. (b) Determine a carga no interior do cilindro.
57 Uma esfera metálica, de espessura insignificante, tem um raio de 25,0 cm e uma carga de 2,00 × 10–7
C. Determine o valor de E (a) no interior da esfera, (b) junto à superfície da esfera e (c) a 3,00 m de
distância do centro da esfera.
58 Uma placa infinita de espessura insignificante, situada no plano xy, possui uma densidade superficial
de carga uniforme ρ = 8,0 nC/m2. Determine o fluxo elétrico através de uma esfera gaussiana com centro
na origem e 5,0 cm de raio.
59 Uma placa infinita que ocupa o espaço entre os planos x = –5,0 cm e x = +5,0 cm tem uma
densidade volumétrica de carga uniforme ρ = 1,2 nC/m3. Determine o módulo do campo elétrico (a) no
plano x = 4,0 cm; (b) no plano x = 6,0 cm.
60 O mistério do chocolate em pó. Explosões provocadas por descargas elétricas (centelhas)
constituem um sério perigo nas indústrias que lidam com pós muito finos. Uma dessas explosões

aconteceu em uma fábrica de biscoitos na década de 1970. Os operários costumavam esvaziar os sacos
de chocolate em pó que chegavam à fábrica em uma bandeja, da qual o material era transportado por
canos de plástico até o silo onde era armazenado. No meio do percurso, duas condições para que uma
explosão ocorresse foram satisfeitas: (1) o módulo do campo elétrico ultrapassou 3,0 × 106 N/C,
produzindo uma ruptura dielétrica do ar; (2) a energia da centelha resultante ultrapassou 150 mJ, fazendo
com que o pó explodisse. Vamos discutir a primeira condição.
Suponha que um pó carregado negativamente esteja passando por um cano cilíndrico, de plástico,
de raio R = 5,0 cm, e que as cargas associadas ao pó estejam distribuídas uniformemente com uma
densidade volumétrica ρ. (a) Usando a lei de Gauss, escreva uma expressão para o módulo do campo
elétrico no interior do cano em função da distância r do eixo do cano. (b) O valor de E aumenta ou
diminui quando r aumenta? (c) O campo aponta para o eixo do cilindro ou para longe do eixo? (d) Para
ρ = 1,1 × 10–3 C/m3 (um valor típico), determine o valor máximo de E e a que distância do eixo do cano
esse campo máximo ocorre. (e) O campo pode produzir uma centelha? Onde? (A história continua no
Problema 70 do Capítulo 24.)
61 Uma casca esférica, metálica, de raio a e espessura insignificante, possui uma carga q . Uma
a
segunda casca, concêntrica com a primeira, possui um raio b > a e uma carga q . Determine o campo
b
elétrico em pontos situados a uma distância r do centro das cascas (a) para r < a, (b) para a < r < b, e (c)
para r > b. (d) Explique o raciocínio que você usou para determinar o modo como as cargas estão
distribuídas nas superfícies internas e externas das cascas.
62 Uma carga pontual q = 1,0 × 10–7 C é colocada no centro de uma cavidade esférica, com 3,0 cm de
raio, aberta em um bloco de metal. Use a lei de Gauss para determinar o campo elétrico (a) a 1,5 cm de
distância do centro da cavidade e (b) no interior do bloco de metal.
63 Um próton, de velocidade v = 3,00 × 105 m/s, gira em órbita em torno de uma esfera carregada, de
raio r = 1,00 cm. Qual é a carga da esfera?
64 A Eq. 23-11 (E = σ/ε ) pode ser usada para calcular o campo elétrico em pontos da vizinhança de
0
uma esfera condutora carregada. Aplique a equação a uma esfera condutora, de raio r e carga q, e mostre
que o campo elétrico do lado de fora da esfera é igual ao campo produzido por uma carga pontual situada
no centro da esfera.
65 Uma carga Q está distribuída uniformemente em uma esfera de raio R. (a) Que fração da carga está
contida em uma esfera de raio r = R/2,00? (b) Qual é a razão entre o módulo do campo elétrico no ponto
r = R/2,00 e o campo elétrico na superfície da esfera?
66 Uma carga pontual produz um fluxo elétrico de –750 N · m2/C através de uma superfície esférica
gaussiana, de 10,0 cm de raio, com centro na carga. (a) Se o raio da superfície gaussiana for multiplicado
por dois, qual será o novo valor do fluxo? (b) Qual é o valor da carga pontual?
67 O campo elétrico no ponto P, a uma pequena distância da superfície externa de uma casca esférica
metálica com 10 cm de raio interno e 20 cm de raio externo, tem um módulo de 450 N/C e aponta para

longe do centro. Quando uma carga pontual desconhecida Q é colocada no centro da casca, o sentido do
campo permanece o mesmo e o módulo diminui para 180 N/C. (a) Determine a carga da casca. (b)
Determine o valor da carga Q. Depois que a carga Q é colocada, determine a densidade superficial de
carga (c) na superfície interna da casca e (d) na superfície externa da casca.
68 O fluxo de campo elétrico em cada face de um dado tem um valor absoluto, em unidades de 103 N ·
m2/C, igual ao número N de pontos da face (1 ≤ N ≤ 6). O fluxo é para dentro se N for ímpar e para fora
se N for par. Qual é a carga no interior do dado?
69 A Fig. 23-59 mostra uma vista em seção reta de três placas isolantes de grande extensão com uma
densidade uniforme de carga. As densidades superficiais de carga são σ = +2,00 μC/m2, σ = +4,00
1 2
μC/m2 e σ = –5,00 μC/m2; L = 1,50 cm. Qual é o campo elétrico no ponto P na notação dos vetores
3
unitários?
Figura 23-59 Problema 69.
70 Uma esfera isolante com 5,0 cm de raio tem uma densidade volumétrica uniforme de carga ρ = 3,2
μC/m3. Determine o módulo do campo elétrico (a) a 3,5 cm e (b) a 8,0 cm do centro da esfera.
71 Uma superfície gaussiana de forma hemisférica, com raio R = 5,68 cm, está imersa em um campo
elétrico uniforme de módulo E = 2,50 N/C. Não existem cargas no interior da superfície. Na base (plana)
da superfície, o campo é perpendicular à superfície e aponta para o interior da superfície. Determine o
fluxo (a) através da base e (b) através da parte curva da superfície.
72 Qual é a carga total envolvida pelo cubo gaussiano do Problema 2?
73 Uma esfera isolante tem uma densidade volumétrica de carga uniforme ρ. Seja o vetor que liga o
centro da esfera a um ponto genérico P no interior da esfera. (a) Mostre que o campo elétrico no ponto P
é dado por = ρ /3ε .(Note que o resultado não depende do raio da esfera.) (b) Uma cavidade esférica é
0
aberta na esfera, como mostra a Fig. 23-60. Usando o princípio da superposição, mostre que o campo
elétrico no interior da cavidade é uniforme e é dado por = ρ /3ε , em que é o vetor que liga o centro
0
da esfera ao centro da cavidade.

Figura 23-60 Problema 73.
74 Uma esfera com 6,00 cm de raio possui uma densidade de carga uniforme de 500 nC/m3. Considere
uma superfície gaussiana cúbica concêntrica com a esfera. Determine o fluxo elétrico através da
superfície cúbica se a aresta do cubo for (a) 4,00 cm e (b) 14,0 cm.
75 A Fig. 23-61 mostra um contador Geiger, aparelho usado para detectar radiação ionizante (radiação
com energia suficiente para ionizar átomos). O contador é formado por um fio central positivamente
carregado e um cilindro circular oco, coaxial, condutor, com uma carga negativa de mesmo valor
absoluto. As cargas criam um campo elétrico radial de alta intensidade entre o cilindro, que contém um
gás inerte rarefeito, e o fio. Uma partícula de radiação que penetra no aparelho através da parede do
cilindro ioniza alguns átomos do gás, produzindo elétrons livres, que são acelerados na direção do fio
positivo. O campo elétrico é tão intenso que, no percurso, os elétrons adquirem energia suficiente para
ionizar outros átomos do gás através de colisões, criando, assim, outros elétrons livres. O processo se
repete até os elétrons chegarem ao fio. A “avalanche” de elétrons resultante é recolhida pelo fio, gerando
um sinal que é usado para assinalar a passagem da partícula de radiação. Suponha que o fio central tenha
um raio de 25 μm e o cilindro tenha um raio interno de 1,4 cm e um comprimento de 16 cm. Se o campo
elétrico na superfície interna do cilindro é 2,9 × 104 N/C, qual é a carga positiva do fio central?
Figura 23-61 Problema 75.

76 Um cilindro muito longo, de raio R, possui uma distribuição volumétrica de carga uniforme. (a)
Mostre que, a uma distância r < R do eixo do cilindro,
em que ρ é a densidade volumétrica de carga. (b) Escreva uma expressão para E do lado de fora do
cilindro.
77 Uma casca condutora esférica tem uma carga de –14 μC na superfície externa e uma partícula
carregada na cavidade interna. Se a carga total da casca é –10 μC, determine a carga (a) da superfície
interna da casca e (b) da partícula.
78 Uma carga de 6,00 pC está distribuída uniformemente em uma esfera de raio r = 4,00 cm. Determine
o módulo do campo elétrico (a) a 6,00 cm do centro da esfera e (b) a 3,00 cm do centro da esfera.
79 A água em uma vala de irrigação, de largura l = 3,22 m e profundidade p = 1,04 m, corre com uma
velocidade de 0,207 m/s. O fluxo mássico da água através de uma superfície imaginária é o produto da
massa específica da água (1000 kg/m3) pelo fluxo volumétrico através da superfície. Determine o fluxo
mássico através das seguintes superfícies imaginárias: (a) uma superfície de área lp, totalmente
submersa, perpendicular à correnteza; (b) uma superfície de área 3lp/2, da qual uma área lp está
submersa, perpendicular à correnteza; (c) uma superfície de área lp/2, totalmente submersa,
perpendicular à correnteza; (d) uma superfície de área lp, metade da qual está submersa, perpendicular à
correnteza; (e) uma superfície de área lp, totalmente submersa, com a normal fazendo um ângulo de 34o
com a direção da correnteza.
80 Uma placa infinita, de espessura insignificante, situada no plano xy, tem uma densidade superficial
de carga uniforme ρ = 8,00 nC/m2; uma placa semelhante, situada no plano z = 2,00, tem uma densidade
superficial de carga uniforme ρ = 3,00 nC/m2. Determine o módulo do campo elétrico (a) no plano z =
1,00 e (b) no plano z = 3,00 m.
81 Uma esfera isolante tem uma densidade de carga uniforme. Determine, em termos do raio R da
esfera, a que distância do centro o módulo do campo elétrico é igual a 1/4 do valor máximo (a) do lado
de dentro da esfera e (b) do lado de fora da esfera.

