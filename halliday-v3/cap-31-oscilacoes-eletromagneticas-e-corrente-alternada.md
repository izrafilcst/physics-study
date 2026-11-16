CAPÍTULO 31
Oscilações Eletromagnéticas e Corrente Alternada
31-1 OSCILAÇÕES EM UM CIRCUITO LC
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
31.01 Desenhar o diagrama esquemático de um circuito LC e explicar quais são as grandezas que oscilam e o que constitui um
período da oscilação.
31.02 Desenhar os gráficos da diferença de potencial do capacitor e da corrente do indutor de um circuito LC em função do
tempo e indicar o período T nos dois gráficos.
31.03 Explicar a analogia entre um oscilador bloco-mola e um circuito LC.
31.04 Conhecer a relação entre a frequência angular ω, a indutância L e a capacitância C de um circuito LC.
31.05 Demonstrar a equação diferencial da carga q do capacitor em um circuito LC a partir da energia de um sistema bloco-
mola e determinar a função q(t) que descreve a variação, com o tempo, da carga do capacitor.
31.06 Calcular a carga q do capacitor de um circuito LC em qualquer instante de tempo e definir a amplitude Q das oscilações
de carga.
31.07 Calcular a corrente i(t) que descreve a variação, com o tempo, da corrente do indutor de um circuito LC a partir da função
q(t) que descreve a variação, com o tempo, da carga do capacitor.
31.08 Calcular a corrente i no indutor de um circuito LC em qualquer instante de tempo e definir a amplitude I das oscilações de
corrente.
31.09 Conhecer a relação entre a amplitude da carga Q, a amplitude da corrente I e a frequência angular ω em um circuito LC.
31.10 Determinar a energia do campo magnético U (t), a energia do campo elétrico U (t) e a energia total de um circuito LC a
B E
partir das expressões da carga q e da corrente i em função do tempo.
31.11 Desenhar gráficos da energia do campo magnético U (t), da energia do campo elétrico U (t) e da energia total de um
B E
circuito LC em função do tempo.
31.12 Calcular os valores máximos da energia do campo magnético U (t) e da energia do campo elétrico U (t) e a energia total
B E
de um circuito LC.
Ideias-Chave
• Em um circuito LC, a energia é transferida periodicamente do campo elétrico do capacitor para o campo magnético do indutor,
e vice-versa; os valores instantâneos das duas formas de energia são
em que q é a carga instantânea do capacitor e i é a corrente instantânea do indutor.
• A energia total U (= U + U ) de um circuito LC é constante.
E B
• De acordo com a lei de conservação da energia,

é a equação diferencial que descreve as oscilações da carga do capacitor em um circuito LC.
• A solução da equação diferencial é
q = Q cos(ωt + ϕ) (carga),
em que Q é a amplitude da carga (carga máxima do capacitor) e a frequência angular das oscilações é dada por
• A constante de fase ϕ é determinada pelas condições iniciais (no instante t = 0) do circuito.
• A corrente no circuito no instante t é dada pela equação
i = ωQ sen(ωt + ϕ) (corrente),
em que ωQ é a amplitude I da corrente.
O que É Física?
Já discutimos a física básica dos campos elétricos e magnéticos e o armazenamento de energia nos
campos elétricos e magnéticos de capacitores e indutores. Vamos agora examinar a aplicação dessa física
à transferência da energia para os locais onde será utilizada. Por exemplo, a energia produzida em uma
usina de energia elétrica deve chegar até a casa do leitor para poder alimentar um computador. O valor
total dessa física aplicada é hoje em dia tão elevado que é quase impossível estimá-lo. Na verdade, a
civilização moderna seria impossível sem ela.
Em quase todo o mundo, a energia elétrica é transferida, não como uma corrente constante (corrente
contínua, ou CC), mas como uma corrente que varia senoidalmente com o tempo (corrente alternada, ou
CA). O desafio para os cientistas e engenheiros é projetar sistemas de CA que transfiram energia de
forma eficiente e aparelhos capazes de utilizar essa energia.
Em nossa discussão de sistemas alternados, o primeiro passo será examinar as oscilações em um
circuito simples, constituído por uma indutância L e uma capacitância C.
Oscilações em um Circuito LC: Análise Qualitativa
Dos três componentes básicos dos circuitos, a resistência R, a capacitância C e a indutância L,
discutimos até agora as combinações em série RC (no Módulo 27-4) e RL (no Módulo 30-6). Nos dois
tipos de circuito, descobrimos que a carga, a corrente e a diferença de potencial crescem e decrescem
exponencialmente. A escala de tempo do crescimento ou decaimento é dada por uma constante de tempo
τ, que pode ser capacitiva ou indutiva.
Vamos agora examinar a combinação de dois componentes que faltam, a combinação LC. Veremos
que, nesse caso, a carga, a corrente e a diferença de potencial não decaem exponencialmente com o

tempo, mas variam senoidalmente com um período T e uma frequência angular ω. As oscilações
resultantes do campo elétrico do capacitor e do campo magnético do indutor são chamadas de oscilações
eletromagnéticas. Quando um circuito se comporta dessa forma, dizemos que ele está oscilando.
As partes a a h da Fig. 31-1 mostram estágios sucessivos das oscilações de um circuito LC simples.
De acordo com a Eq. 25-21, a energia armazenada no campo elétrico do capacitor em qualquer instante é
dada por
Figura 31-1 Oito estágios em um ciclo de oscilação de um circuito LC sem resistência. Os histogramas mostram a energia armazenada no
campo magnético e no campo elétrico. Também são mostradas as linhas de campo magnético do indutor e as linhas de campo elétrico do
capacitor. (a) O capacitor está totalmente carregado; a corrente é zero. (b) O capacitor está se descarregando; a corrente está aumentando.
(c) O capacitor está totalmente descarregado; a corrente é máxima. (d) O capacitor está se carregando com a polaridade oposta à de (a); a
corrente está diminuindo. (e) O capacitor está totalmente carregado com a polaridade oposta à de (a); a corrente é zero. (f) O capacitor está
se descarregando; a corrente está aumentando no sentido oposto ao de (b). (g) O capacitor está totalmente descarregado; a corrente é
máxima. (h) O capacitor está se carregando; a corrente está diminuindo.
em que q é a carga do capacitor nesse instante. De acordo com a Eq. 30-49, a energia armazenada no
campo magnético do indutor em qualquer instante é dada por

em que i é a corrente no indutor nesse instante.
A partir de agora, vamos adotar a convenção de representar os valores instantâneos das grandezas
elétricas de um circuito por letras minúsculas, como q, e as amplitudes das mesmas grandezas por letras
maiúsculas, como Q. Com essa convenção em mente, vamos supor que inicialmente a carga q do
capacitor da Fig. 31-1 é o valor máximo Q e a corrente i no indutor é zero. Esse estado inicial do circuito
está representado na Fig. 31-1a. As barras que representam os níveis de energia mostram que, nesse
instante, com corrente zero no indutor e carga máxima no capacitor, a energia U do campo magnético é
B
zero e a energia U do campo elétrico é máxima. Durante as oscilações do circuito, a energia é
E
transferida do campo elétrico para o campo magnético, e vice-versa, mas a energia total permanece
constante.
Logo após o instante inicial, o capacitor começa a se descarregar através do indutor, com as cargas
positivas se movendo no sentido anti-horário, como mostra a Fig. 31-1b. Isso significa que uma corrente
i, dada por dq/dt e com o sentido de cima para baixo no indutor, começa a circular. Com a diminuição da
carga do capacitor, a energia armazenada no campo elétrico do capacitor também diminui. Essa energia é
transferida para o campo magnético que aparece nas vizinhanças do indutor por causa da existência da
corrente i. Assim, o campo elétrico diminui e o campo magnético aumenta enquanto a energia é
transferida do campo elétrico para o campo magnético.
Depois de algum tempo, o capacitor perde toda a carga (Fig. 31-1c) e, portanto, o campo elétrico e a
energia armazenada no campo elétrico se anulam. Nesse instante, toda a energia foi transferida para o
campo magnético do indutor. O campo magnético está, portanto, com o valor máximo, e a corrente no
indutor é a corrente máxima I.
Embora a carga do capacitor seja zero nesse instante, a corrente no sentido anti-horário continua a
existir, já que o indutor não permite que a corrente diminua instantaneamente para zero. A corrente
continua a transferir cargas positivas da placa de cima para a placa de baixo do capacitor através do
circuito (Fig. 31-1d). Assim, a energia que estava armazenada no indutor começa a acumular cargas no
capacitor. A corrente no indutor diminui gradualmente durante o processo. No instante em que,
finalmente, toda a energia é transferida de volta para o capacitor (Fig. 31-1e), a corrente no indutor se
anula momentaneamente. A situação da Fig. 31-1e é idêntica à da Fig. 31-1a, exceto pelo fato de que o
capacitor agora está carregado com a polaridade oposta.
Em seguida, o capacitor volta a se descarregar, mas agora a corrente tem o sentido horário (Fig. 31-
1f). Raciocinando como antes, vemos que a corrente passa por um máximo (Fig. 31-1g) e depois diminui
(Fig. 31-1h) até que o circuito volta à situação inicial (Fig. 31-1a). O processo se repete com uma
frequência f e, portanto, com uma frequência angular ω = 2πf. Em um circuito LC ideal, em que não existe
resistência, toda a energia do campo elétrico do capacitor é transferida para a energia do campo
magnético do indutor, e vice-versa. Por causa da lei de conservação da energia, as oscilações continuam
indefinidamente. As oscilações não precisam começar com toda a energia no campo elétrico; a situação

inicial poderia ser qualquer outro estágio da oscilação.
Para determinar a carga q do capacitor em função do tempo, podemos usar um voltímetro para medir
a diferença de potencial (ou tensão) v entre as placas do capacitor C. De acordo com a Eq. 25-1, temos
C
que nos permite calcular o valor de q. Para determinar a corrente, podemos ligar um pequeno resistor R
em série com o capacitor e o indutor e medir a diferença de potencial v entre os terminais do resistor; v
R R
é proporcional a i por meio da relação
v = iR.
R
Estamos supondo que R é tão pequeno que seu efeito sobre o comportamento do circuito pode ser
desprezado. A variação, com o tempo, de v e v , e, portanto, de q e i, é mostrada na Fig. 31-2. As quatro
C R
grandezas variam de forma senoidal.
Figura 31-2 (a) A diferença de potencial entre os terminais do capacitor da Fig. 31-1 em função do tempo. Essa grandeza é proporcional à
carga do capacitor. (b) Um potencial proporcional à corrente no circuito da Fig. 31-1. As letras se referem aos diferentes estágios de
oscilação da Fig. 31-1.
Em um circuito LC real, as oscilações não continuam indefinidamente porque sempre existe uma
resistência que retira energia dos campos elétrico e magnético e a dissipa na forma de energia térmica (o
circuito se aquece). Isso significa que a amplitude das oscilações diminui com o tempo, como mostra a
Fig. 31-3. A Fig. 31-3 é semelhante à Fig. 15-17, que mostra o decaimento das oscilações mecânicas de
um sistema bloco-mola por causa do atrito.

Keysight	Technologies,	Inc.	Reproduzido	com	permissão,	cortesia	de	Keysight	Technologies.
Figura	31-3 	Imagem	na	tela	de	um	osciloscópio	que	mostra	o	amortecimento	das	oscilações	em	um	circuito	RLC	por	causa	da	dissipação
de	energia	no	resistor.
	Teste	1
Um	capacitor	carregado	e	um	indutor	são	ligados	em	série	no	instante	t	=	0.	Determine,	em	termos	do	período	T	das	oscilações
resultantes,	o	tempo	t	>	0	necessário	para	que	as	seguintes	grandezas	atinjam	o	valor	máximo:	(a)	a	carga	do	capacitor;	(b)	a
tensão	do	capacitor,	com	a	polaridade	inicial;	(c)	a	energia	armazenada	no	campo	elétrico;	(d)	a	corrente	no	circuito.
Analogia	Eletromecânica
Vamos	examinar	mais	de	perto	a	analogia	entre	o	circuito	LC	oscilante	da	Fig.	31-1	 e	 um	 sistema
oscilante	 bloco-mola.	 No	 caso	 do	 sistema	 bloco-mola,	 existem	 dois	 tipos	 de	 energia	 envolvidos:	 a
energia	potencial	da	mola	distendida	ou	comprimida	e	a	energia	cinética	do	bloco	em	movimento.	As
duas	energias	são	dadas	pelas	expressões	que	aparecem	na	coluna	de	energia	da	esquerda	da	Tabela	31-
1.
Tabela	31-1	Comparação	das	Energias	de	Dois	Sistemas	Oscilantes
|            | Sistema	Bloco-Mola |                  | 	   |            | Circuito	LC |                     |
| ---------- | ------------------ | ---------------- | --- | ---------- | ----------- | ------------------- |
| Componente |                    | Energia          | 	   | Componente |             | Energia             |
| Mola       |                    |                  | 	   | Capacitor  |             |                     |
|            |                    | Potencial,	kx2/2 |     |            |             | Elétrica,	(1/C)q2/2 |
| Bloco      |                    | Cinética,	mv2/2  | 	   | Indutor    |             | Magnética,	Li2/2    |
|            | v	=	dx/dt          |                  | 	   |            | i	=	dq/dt   |                     |
A	tabela	também	apresenta,	na	coluna	de	energia	da	direita,	os	dois	tipos	de	energia	envolvidos	nas
oscilações	de	um	circuito	LC.	As	linhas	horizontais	da	tabela	revelam	uma	analogia	entre	as	formas	dos
dois	pares	de	energias:	as	energias	mecânicas,	do	sistema	bloco-mola,	e	as	energias	eletromagnéticas,	do
sistema	indutor-capacitor.	As	equações	para	v	e	i	que	aparecem	na	última	linha	da	tabela	ajudam	a
completar	a	analogia.	Elas	mostram	que	q	corresponde	a	x	e	i	corresponde	a	v	(nas	duas	equações,	a
segunda	variável	é	a	derivada	da	primeira	em	relação	ao	tempo).	Essas	correspondências	sugerem	que,
nas	expressões	da	energia,	1/C	corresponde	a	k	e	L	corresponde	a	m.	Assim,
|     | q	corresponde	a	x, |     | 	   | 1/C	corresponde	a	k, |     |     |
| --- | ------------------ | --- | --- | -------------------- | --- | --- |
|     | i	corresponde	a	v  |     | e   | L	corresponde	a	m.   |     |     |
Essas	correspondências	sugerem	que,	em	um	oscilador	LC,	o	capacitor	se	comporta	matematicamente
como	a	mola	de	um	sistema	bloco-mola,	e	o	indutor	se	comporta	como	o	bloco.

Vimos no Módulo 15-1 que a frequência angular de oscilação de um sistema bloco-mola sem atrito é
As correspondências sugerem que, para determinar a frequência angular de oscilação de um circuito LC
ideal (sem resistência), k deve ser substituído por 1/C e m por L, o que nos dá
Oscilações em um Circuito LC: Análise Quantitativa
Vamos agora mostrar explicitamente que a Eq. 31-4 é a expressão correta para a frequência angular das
oscilações em um circuito LC. Ao mesmo tempo, examinaremos mais de perto a analogia entre as
oscilações de um circuito LC e de um sistema bloco-mola. Começamos por ampliar um pouco nosso
tratamento anterior do oscilador mecânico bloco-mola.
O Oscilador Bloco-Mola
Analisamos as oscilações do sistema bloco-mola no Capítulo 15 em termos da transferência de energia,
mas não chegamos a escrever a equação diferencial que governa essas oscilações; é o que vamos fazer
agora.
A energia total U de um oscilador bloco-mola é dada, em qualquer instante de tempo, pela equação
em que U e U são, respectivamente, a energia cinética do bloco e a energia potencial da mola. Se o
b m
atrito é desprezível, a energia total U não varia com o tempo, ou seja, dU/dt = 0. Assim, temos
Entretanto, v = dx/dt e dv/dt = d2x/dt2. Com essas substituições, a Eq. 31-6 se torna
A Eq. 31-7 é a equação diferencial a que obedecem às oscilações massa-mola sem atrito.
A solução geral da Eq. 31-7, ou seja, a função x(t) que descreve as oscilações, é (como vimos na
Eq. 15-3)

em que X é a amplitude das oscilações mecânicas (representada por x no Capítulo 15), ω é a frequência
m
angular das oscilações e ϕ é uma constante de fase.
O Oscilador LC
Vamos agora analisar as oscilações de um circuito LC sem resistência, procedendo exatamente como
fizemos no caso do oscilador bloco-mola. A energia total U presente em qualquer instante em um circuito
LC oscilante é dada por
em que U é a energia armazenada no campo magnético do indutor e U é a energia armazenada no campo
B E
elétrico do capacitor. Como supusemos que a resistência do circuito é zero, nenhuma energia é
transformada em energia térmica e U permanece constante, ou seja, dU/dt = 0. Assim, temos
Entretanto, i = dq/dt e di/dt = d2q/dt2. Com essas substituições, a Eq. 31-10 se torna
Essa é a equação diferencial que descreve as oscilações em um circuito LC sem resistência. As Eqs. 31-
11 e 31-7 têm exatamente a mesma forma matemática.
Oscilações de Carga e de Corrente
Quando duas equações diferenciais são matematicamente equivalentes, as soluções também são
matematicamente equivalentes. Como q corresponde a x, podemos escrever a solução geral da Eq. 31-11,
por analogia com a Eq. 31-8, como
em que Q é a amplitude das variações de carga, ω é a frequência angular das oscilações eletromagnéticas
e ϕ é a constante de fase. Derivando a Eq. 31-12 em relação ao tempo, obtemos a corrente em um circuito
LC:

A amplitude I dessa corrente senoidal é
e, portanto, podemos reescrever a Eq. 31-13 na forma
Frequências Angulares
Podemos confirmar que a Eq. 31-12 é uma solução da Eq. 31-11 substituindo a Eq. 31-12 e sua derivada
segunda em relação ao tempo na Eq. 31-11. A derivada primeira da Eq. 31-12 é a Eq. 31-13. A derivada
segunda é, portanto,
Substituindo q e d2q/dt2 por seus valores na Eq. 31-11, obtemos
Dividindo ambos os membros por Q cos(ωt + ϕ) e reagrupando os termos, obtemos
Assim, a Eq. 31-12 é realmente uma solução da Eq. 31-11, contanto que . Observe que a
expressão de ω é a mesma da Eq. 31-4, à qual chegamos usando correspondências.
A constante de fase ϕ da Eq. 31-12 é determinada pelas condições que existem em um dado instante,
como t = 0, por exemplo. De acordo com a Eq. 31-12, se ϕ = 0 no instante t = 0, q = Q e, de acordo com
a Eq. 31-13, i = 0. Essas são as condições representadas na Fig. 31-1a.
Oscilações da Energia Elétrica e Magnética
De acordo com as Eqs. 31-1 e 31-12, a energia elétrica armazenada no circuito LC no instante t é dada
por

Figura	31-4 	Energia	magnética	e	energia	elétrica	armazenada	no	circuito	da	Fig.	31-1	em	função	do	tempo.	Observe	que	a	soma	das	duas
energias	é	constante.	T	é	o	período	das	oscilações.
De	acordo	com	as	Eqs.	31-2	e	31-13,	a	energia	magnética	armazenada	é	dada	por
Substituindo	ω	por	seu	valor,	dado	pela	Eq.	31-4,	temos
A	Fig.	31-4	mostra	os	gráficos	de	U (t)	e	U (t)	para	o	caso	de	ϕ	=	0.	Observe	que
|                              |     | E             | B            |
| ---------------------------- | --- | ------------- | ------------ |
| 1. O	valor	máximo	tanto	de	U |     | (t)	como	de	U | (t)	é	Q2/2C. |
|                              |     | E             | B            |
2. Em	qualquer	instante,	a	soma	de	U (t)	e	U (t)	também	é	Q2/2C.
|             |                 | E                           | B   |
| ----------- | --------------- | --------------------------- | --- |
| 3. Quando	U | (t)	é	máxima,	U | (t)	é	mínima,	e	vice-versa. |     |
|             | E               | B                           |     |
	Teste	2
Um	capacitor	em	um	circuito	LC	tem	uma	diferença	de	potencial	máxima	de	17	V	e	uma	energia	máxima	de	160	μJ.	Quando	o
capacitor	tem	uma	diferença	de	potencial	de	5	V	e	uma	energia	de	10	μJ,	(a)	qual	é	a	força	eletromotriz	entre	os	terminais	do
indutor	e	(b)	qual	a	energia	armazenada	no	campo	magnético?
	Exemplo	31.01			Variação	de	potencial	e	taxa	de	variação	da	corrente	em	um	circuito	LC
Um	capacitor	de	1,5	μF	é	carregado	por	uma	bateria	de	57	V,	que,	em	seguida,	é	desligada.	No	instante	t	=	0,	um	indutor	de	12
mH	é	ligado	ao	capacitor	para	formar	um	circuito	LC	(Fig.	31-1).
(a)	Qual	é	a	diferença	de	potencial	v (t)	entre	os	terminais	do	indutor	em	função	do	tempo?
L

IDEIAS-CHAVE
(1) A corrente e as diferenças de potencial do circuito (a diferença de potencial do capacitor e a diferença de potencial do indutor)
variam de forma senoidal. (2) Podemos aplicar a um circuito oscilante a mesma regra das malhas que aplicamos a circuitos não
oscilantes no Capítulo 27.
Cálculos: Aplicando a regra das malhas ao circuito Fig. 31-1, temos, para qualquer instante de tempo t,
ou seja, como a diferença de potencial para o circuito como um todo é zero, a diferença de potencial v do indutor é sempre igual à
L
diferença de potencial v do capacitor. Assim, podemos calcular v (t) a partir de v (t) e podemos calcular v (t) a partir de q(t)
C L C C
usando a Eq. 25-1 (q = CV).
Como a diferença de potencial v (t) é máxima no instante t = 0 em que as oscilações começam, a carga q do capacitor
C
também é máxima nesse instante. Assim, a constante de fase ϕ é zero e a Eq. 31-12 nos dá
[Note que a função cosseno realmente passa por um máximo (= 1) para t = 0, o que nos dá q = Q.] Para calcular a diferença de
potencial v (t), dividimos ambos os membros da Eq. 31-19 por C para obter
C
e usamos a Eq. 25-1 para escrever
Aqui, V é a amplitude das oscilações da diferença de potencial v do capacitor.
C C
De acordo com a Eq. 31-18, v = v ; portanto,
C L
Podemos calcular o lado direito da Eq. 31-21 observando que a amplitude V é igual à diferença de potencial inicial (máxima) de
C
57 V entre os terminais do capacitor. Em seguida, usamos a Eq. 31-4 para calcular ω:
Assim, a Eq. 31-21 se torna

(b) Qual é a máxima taxa de variação (di/dt) da corrente no circuito?
máx
IDEIA-CHAVE
Com a carga do capacitor oscilando de acordo com a Eq. 31-12, a corrente tem a forma da Eq. 31-13. Como ϕ = 0, a equação nos
dá
i = −ωQ sen ωt.
Cálculos: Derivando a equação anterior em relação ao tempo, obtemos
Podemos simplificar essa equação substituindo Q por CV (já que conhecemos C e V, mas não conhecemos Q) e substituindo ω por
C C
, de acordo com a Eq. 31-4. O resultado é o seguinte:
Isso significa que a taxa de variação da corrente varia senoidalmente e seu valor máximo é
31-2 OSCILAÇÕES AMORTECIDAS EM UM CIRCUITO RLC
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
31.13 Desenhar o diagrama esquemático de um circuito RLC série e explicar por que as oscilações do circuito são amortecidas.
31.14 A partir das expressões das energias do campo e da taxa de dissipação da energia em um circuito RLC, escrever uma
equação diferencial para a carga do capacitor.
31.15 Escrever uma expressão para a carga do capacitor de um circuito RLC em função do tempo, q(t).
31.16 Saber que, em um circuito RLC, a carga do capacitor e a energia do campo elétrico do capacitor diminuem
exponencialmente com o tempo.
31.17 Conhecer a relação entre a frequência angular ω’ das oscilações de um circuito RLC e a frequência angular ω de um
circuito LC com os mesmos valores de indutância e capacitância.
31.18 Escrever uma expressão para a energia U do campo elétrico do capacitor de um circuito RLC em função do tempo.
E
Ideias-Chave
• As oscilações de um circuito RLC são amortecidas por causa da presença de um componente dissipativo no circuito. A

variação com o tempo da carga do capacitor é dada pela equação
• A solução dessa equação diferencial é
q = Qe−Rt/2L cos(ω–t + ϕ),
em que
Para pequenos valores de R, ω’ ≈ ω.
Oscilações Amortecidas em um Circuito RLC
Um circuito formado por uma resistência, uma indutância e uma capacitância é chamado de circuito RLC.
Vamos discutir apenas o caso de circuitos RLC série, como o da Fig. 31-5. Com uma resistência R
presente, a energia eletromagnética total U do circuito (a soma da energia elétrica e da energia
magnética) não é constante, como no circuito LC, pois parte da energia é transformada pela resistência
em energia térmica. Por causa dessa perda de energia, as oscilações de carga, corrente e diferença de
potencial diminuem continuamente de amplitude e dizemos que as oscilações são amortecidas. Como
vamos ver, esse amortecimento é análogo ao do oscilador bloco-mola amortecido do Módulo 15-5.
Para analisar as oscilações do circuito, necessitamos de uma equação que expresse a energia
eletromagnética total U no circuito em função do tempo. Como a resistência não armazena energia
eletromagnética, podemos usar a Eq. 31-9 para escrever a energia total da seguinte forma:
No caso que estamos examinando, a energia eletromagnética total diminui com o tempo, já que parte da
energia é transformada em energia térmica. De acordo com a Eq. 26-27, a taxa com a qual essa
transformação ocorre é dada por
Figura 31-5 Circuito RLC série. Enquanto a carga contida no circuito oscila entre o indutor e o capacitor, parte da energia do circuito é
dissipada no resistor, o que reduz progressivamente a amplitude das oscilações.

em que o sinal negativo indica que U diminui com o tempo. Derivando a Eq. 31-22 em relação ao tempo
e substituindo o resultado na Eq. 31-23, obtemos
Substituindo i por dq/dt e di/dt por d2q/dt2, obtemos
que é a equação diferencial para as oscilações amortecidas de um circuito RLC.
Diminuição da Carga. A solução da Eq. 31-24 é
em que
e , como no caso de um oscilador não amortecido. A Eq. 31-25 expressa a variação da carga do
capacitor em um circuito RLC; ela é análoga à Eq. 15-42, que descreve o deslocamento do bloco em um
oscilador bloco-mola amortecido.
A Eq. 31-25 descreve uma oscilação senoidal (a função cosseno) com uma amplitude
exponencialmente decrescente Qe−Rt/2L (o fator que multiplica o cosseno). A frequência angular ωʹ das
oscilações amortecidas é sempre menor que a frequência angular das oscilações não amortecidas;
entretanto, vamos considerar apenas situações nas quais a resistência R é suficientemente pequena para
que ωʹ possa ser substituída por ω.
Diminuição da Energia. Vamos agora escrever uma expressão para a energia eletromagnética total
U do circuito em função do tempo. Para isso, basta calcular a energia armazenada no campo elétrico do
capacitor, que é fornecida pela Eq. 31-1 (U = q2/2C). Substituindo a Eq. 31-25 na Eq. 31-1, obtemos
E
Assim, a energia do campo elétrico oscila de acordo com um termo proporcional ao quadrado do
cosseno, e a amplitude das oscilações diminui exponencialmente com o tempo. Um cálculo semelhante
para a energia do campo magnético levaria a um resultado análogo.
Exemplo 31.02 Amplitude da carga em um circuito RLC
Um circuito RLC série tem uma indutância L = 12 mH, uma capacitância C = 1,6 μF, uma resistência R = 1,5 Ω e começa a oscilar no

instante t = 0.
(a) Em que instante t a amplitude das oscilações da carga do circuito é 50% do valor inicial? (Note que o valor inicial da carga não
é dado.)
IDEIA-CHAVE
A amplitude das oscilações da carga diminui exponencialmente com o tempo t. De acordo com a Eq. 31-25, a amplitude das
oscilações da carga em um instante t é dada por Qe−t/2L, em que Q é a amplitude no instante t = 0.
Cálculos: Estamos interessados em determinar o instante no qual a amplitude das oscilações da carga é 0,50Q, ou seja, o instante
em que
Qe−Rt/2L = 0,50Q.
Dividindo ambos os membros por Q (o que elimina Q da equação, mostrando que não é preciso conhecer a carga inicial) e
tomando o logaritmo natural de ambos os membros, obtemos
Explicitando t e substituindo os valores conhecidos, obtemos
(b) Quantas oscilações o circuito executou até esse instante?
IDEIA-CHAVE
O tempo necessário para o circuito completar uma oscilação é o período T = 2π/ω, em que a frequência angular das oscilações,
para pequenos valores de R, é dada pela Eq. 31-4 .
Cálculo: No intervalo de tempo Δt = 0,0111 s, o número de oscilações completas é
Assim, a amplitude diminui 50% em cerca de 13 oscilações. Esse amortecimento é bem mais lento que o da Fig. 31-3, em que a
amplitude diminui mais de 50% em apenas uma oscilação.

31-3 OSCILAÇÕES FORÇADAS EM TRÊS CIRCUITOS SIMPLES
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
31.19 Saber a diferença entre corrente alternada e corrente contínua.
31.20 Escrever a equação da força eletromotriz de um gerador de CA em função do tempo, usando como parâmetros a
amplitude da força eletromotriz e a frequência angular de excitação.
31.21 Escrever a equação da corrente de um gerador de CA em função do tempo, usando como parâmetros a amplitude da
corrente, a frequência angular de excitação e a constante de fase em relação à força eletromotriz.
31.22 Desenhar o diagrama esquemático de um circuito RLC série alimentado por um gerador de CA.
31.23 Saber a diferença entre a frequência angular de excitação ω e a frequência angular natural ω.
d
31.24 Conhecer a condição de ressonância de um circuito RLC série e o efeito da ressonância sobre a amplitude da corrente.
31.25 Desenhar os diagramas esquemáticos dos três circuitos básicos (carga puramente resistiva, carga puramente capacitiva
e carga puramente indutiva) e diagramas fasoriais da tensão v(t) e da corrente i(t) associados.
31.26 Conhecer as equações da tensão v(t) e da corrente i(t) nos três circuitos básicos.
31.27 Identificar a velocidade angular, a amplitude, a componente vertical e o ângulo de rotação dos fasores de tensão e corrente
associados aos três circuitos básicos.
31.28 Identificar as constantes de fase associadas aos três circuitos básicos e interpretá-las em termos das orientações
relativas dos fasores da tensão e da corrente e também em termos de avanços e atrasos.
31.29 Usar a frase mnemônica “ELI, que TOLICE!”
31.30 Conhecer a relação entre a amplitude V da tensão e a amplitude I da corrente para os três circuitos básicos.
31.31 Calcular a reatância capacitiva X e a reatância indutiva X .
C L
Ideias-Chave
• Um circuito RLC série executa oscilações forçadas com uma frequência angular ω quando é ligado a uma fonte cuja força
d
eletromotriz é dada por
• A corrente no circuito é
i = I sen(ω t − ϕ),
d
em que ϕ é a constante de fase da corrente.
• A diferença de potencial entre os terminais de um resistor que conduz uma corrente alternada é dada por V = IR; a corrente
R
está em fase com a diferença de potencial.
o
• No caso de um capacitor, V = IX , em que X = 1/ω C é a reatância capacitiva; a corrente está adiantada de 90 em relação
C C′ C d
o
à diferença de potencial (ϕ = –90 = π/2 rad).
o
• No caso de um indutor, V = IX , em que X = ω L é a reatância indutiva; a corrente está atrasada de 90 em relação à
L L L d
o
diferença de potencial (ϕ = +90 = +π/2 rad).

Corrente Alternada
As oscilações de um circuito RLC não são amortecidas se uma fonte de tensão externa fornece energia
suficiente para compensar a energia dissipada na resistência R. Os aparelhos elétricos usados nas
fábricas, escritórios e residências contêm um número muito grande de circuitos RLC, que são alimentados
pela rede de distribuição de energia elétrica. Na grande maioria dos casos, a energia é fornecida na
forma de correntes e tensões senoidais, sistema que é conhecido como corrente alternada ou CA. (No
caso das correntes e tensões que não variam com o tempo, como as fornecidas por uma bateria, o sistema
é conhecido como corrente contínua ou CC.) No sistema de corrente alternada usado no Brasil, a tensão
e a corrente mudam de sentido 120 vezes por segundo e, portanto, têm uma frequência f = 60 Hz.
Oscilações dos Elétrons. À primeira vista, a corrente alternada pode parecer uma forma estranha de
fornecer energia a um circuito. Vimos que a velocidade de deriva dos elétrons de condução em um fio
comum é da ordem de 4 × 10−5 m/s. Se o sentido de movimento dos elétrons se inverte a cada 1/120 s, os
elétrons se deslocam apenas cerca de 3 × 10−7 m a cada meio ciclo. Assim, em média, um elétron passa
apenas por 10 átomos da rede cristalina do material de que é feito o fio antes de dar meia-volta. Nesse
ritmo, o leitor deve estar se perguntando: Como o elétron consegue chegar a algum lugar?
A resposta é simples: O elétron não precisa ir “a algum lugar”. Quando dizemos que a corrente em
um fio é um ampère, isso significa que as cargas passam por qualquer plano que intercepta totalmente o
fio à taxa de um coulomb por segundo. A velocidade com a qual os portadores passam pelo plano não é o
único parâmetro importante: um ampère pode corresponder a muitos portadores de carga se movendo
devagar ou a poucos portadores de carga se movendo depressa. Além disso, o sinal para os elétrons
passarem a se mover no sentido oposto, que tem origem na força eletromotriz alternada produzida nos
geradores das usinas elétricas, se propaga ao longo dos condutores com uma velocidade quase igual à
velocidade da luz. Todos os elétrons, onde quer que estejam, recebem essa instrução praticamente no
mesmo instante. Finalmente, convém observar que em muitos dispositivos, como as lâmpadas e as
torradeiras, o sentido do movimento não é importante, contanto que os elétrons estejam em movimento e
transfiram energia para o dispositivo por meio de colisões com átomos.
Por que Usar CA? A principal vantagem da corrente alternada é a seguinte: Quando a corrente
muda de sentido, o mesmo acontece com o campo magnético nas vizinhanças do condutor. Isso torna
possível usar a lei de indução de Faraday, o que, entre outras coisas, significa que podemos aumentar ou
diminuir à vontade a diferença de potencial usando um dispositivo, conhecido como transformador, que
será discutido mais tarde. Além disso, a corrente alternada é mais fácil de gerar e utilizar que a corrente
contínua no caso de máquinas rotativas como geradores e motores.
Força Eletromotriz e Corrente. Fig. 31-6 mostra um tipo simples de gerador de corrente alternada.
Quando a espira condutora é forçada a girar na presença do campo magnético externo uma força
eletromotriz senoidal é induzida na espira:
A frequência angular ω da força eletromotriz é igual à velocidade angular de rotação da espira, a fase é
d

ω t, e a amplitude é (o índice significa máxima). Se a espira faz parte de um circuito elétrico, a força
d
eletromotriz produz uma corrente senoidal (alternada) no circuito com a mesma frequência angular ω ,
d
que nesse caso é chamada de frequência angular de excitação. Podemos escrever a corrente na forma
em que I é a amplitude da corrente. (Por convenção, a fase da corrente é normalmente escrita como ω t −
d
ϕ e não como ω t + ϕ). Uma constante de fase ϕ foi introduzida na Eq. 31-29 porque a corrente i pode não
d
estar em fase com a força eletromotriz. (Como vamos ver, a constante de fase depende do circuito ao qual
o gerador está ligado.) Podemos também escrever a corrente i em termos da frequência de excitação f
d
da força eletromotriz, substituindo ω por 2πf na Eq. 31-29.
d d
Figura 31-6 Nos geradores de corrente alternada, uma espira condutora é forçada a girar na presença do campo magnético externo. Na
prática, a força eletromotriz induzida em uma bobina com muitas espiras é colhida por escovas que se apoiam em anéis rotativos solidários
com bobina. Cada anel está ligado a uma extremidade da bobina e faz contato com o resto do circuito do gerador por meio de uma das
escovas.
Oscilações Forçadas
Como vimos, depois de um estímulo inicial, a carga, a diferença de potencial e a corrente nos circuitos
LC e RLC (para valores suficientemente pequenos de R) oscilam com uma frequência angular .
Essas oscilações recebem o nome de oscilações livres (livres de qualquer força eletromotriz externa), e
a frequência angular ω é chamada de frequência angular natural.
Quando a fonte externa de força eletromotriz alternada da Eq. 31-28 é ligada a um circuito RLC,
dizemos que as oscilações de carga, diferença de potencial e corrente são oscilações forçadas. Essas
oscilações sempre acontecem na frequência angular de excitação ω .
d
Qualquer que seja a frequência angular natural ω de um circuito, as oscilações forçadas de carga, corrente e diferença de potencial
acontecem na frequência angular de excitação ω .
d
Por outro lado, como vamos ver no Módulo 31-4, a amplitude das oscilações depende da diferença entre
ω e ω. Quando as duas frequências são iguais (uma situação conhecida como ressonância), a amplitude
d
da corrente I no circuito é máxima; quanto maior a diferença entre ω e ω, menor a amplitude das
d

oscilações.
Três Circuitos Simples
Daqui a pouco, vamos estudar um sistema constituído por uma fonte de força eletromotriz alternada e um
circuito RLC série, como o sistema da Fig. 31-7, e obter expressões para a amplitude I e constante de
fase ϕ da corrente no circuito em função da amplitude e frequência angular ω da força eletromotriz.
d
Antes, porém, vamos examinar três circuitos mais simples, constituídos apenas pela fonte e um
componente como R, C e L. Começaremos com um componente resistivo (uma carga resistiva pura).
Figura 31-7 Circuito de uma malha formado por um resistor, um capacitor e um indutor. Um gerador, representado por uma senoide no
interior de um círculo, produz uma força eletromotriz alternada que estabelece uma corrente alternada no circuito. O sentido da força
eletromotriz e da corrente varia periodicamente.
Carga Resistiva
A Fig. 31-8 mostra um circuito formado por um resistor R e um gerador de corrente alternada cuja força
eletromotriz é dada pela Eq. 31-28. De acordo com a regra das malhas, temos
De acordo com a Eq. 31-28, temos
Como a amplitude V da diferença de potencial (ou tensão) entre os terminais da resistência é igual à
R
amplitude da força eletromotriz, podemos escrever:
Usando a definição de resistência (R = V/i), podemos escrever a corrente na resistência como
De acordo com a Eq. 31-29, a corrente também pode ser escrita na forma

em que I é a amplitude da corrente i na resistência. Comparando as Eqs. 31-31 e 31-32, vemos que, no
R R
caso de uma carga resistiva pura, a constante de fase ϕ é nula.
Figura 31-8 Circuito formado por um resistor e um gerador de corrente alternada.
Vemos também que a amplitude da tensão e a amplitude da corrente estão relacionadas pela equação
Embora essa relação tenha sido demonstrada apenas para o circuito da Fig. 31-8, ela se aplica a qualquer
resistência em qualquer circuito.
Comparando as Eqs. 31-30 e 31-31, vemos que as grandezas variáveis com o tempo v e i são
R R
funções de sen ω t com ϕ = 0o. Isso significa que as duas grandezas estão em fase, ou seja, passam ao
d
mesmo tempo pelos máximos e pelos mínimos. A Fig. 31-9a, que é um gráfico de v (t) e i (t), ilustra esse
R R
fato. Observe que os valores máximos de v e i não diminuem com o tempo porque o gerador fornece
R R
energia ao circuito para compensar a energia dissipada em R.
As grandezas variáveis com o tempo v e i podem ser representadas geometricamente por fasores.
R R
Como vimos no Módulo 16-6, fasores são vetores que giram em torno de uma origem. Os fasores que
representam a tensão e a corrente no resistor da Fig. 31-8 são mostrados na Fig. 31-9b para um instante
de tempo arbitrário t. Esses fasores têm as seguintes propriedades:
Velocidade angular: Os dois fasores giram em torno da origem no sentido anti-horário com uma
velocidade angular igual à frequência angular ω de v e i .
d R R
Comprimento: O comprimento de cada fasor representa a amplitude de uma grandeza alternada, V no
R
caso da tensão e I no caso da corrente.
R
Projeção: A projeção de cada fasor no eixo vertical representa o valor da grandeza alternada no instante
t, v no caso da tensão e i no caso da corrente.
R R
Ângulo de rotação: O ângulo de rotação de cada fasor é igual à fase da grandeza alternada no instante t.
Na Fig. 31-9b, a tensão e a corrente estão em fase; como têm a mesma velocidade angular e o mesmo
ângulo de rotação, os dois fasores giram juntos.
Acompanhe mentalmente a rotação. Não é fácil ver que a tensão e a corrente atingem os valores
máximos v = V e i = I quando o ângulo de rotação é 90o (ou seja, quando os dois fasores estão
R R R R
apontando verticalmente para cima)? As Eqs. 31-30 e 31-32 fornecem os mesmos resultados.
Teste 3
Quando aumentamos a frequência de excitação de um circuito com uma carga resistiva pura, (a) a amplitude V aumenta, diminui
R

ou permanece a mesma? (b) A amplitude I aumenta, diminui ou permanece a mesma?
R
Figura 31-9 (a) Gráfico da corrente i no resistor e da diferença de potencial v entre os terminais do resistor em função do tempo t. A
R R
corrente e a diferença de potencial estão em fase e completam um ciclo em um período T. (b) Diagrama fasorial correspondente ao gráfico
mostrado em (a).
Exemplo 31.03 Diferença de potencial e corrente para uma carga resistiva pura
No circuito da Fig. 31-8, a resistência R é 200 Ω e o gerador produz uma força eletromotriz de amplitude = 36,0 V e frequência
f = 60,0 Hz.
d
(a) Qual é a diferença de potencial v (t) entre os terminais do resistor em função do tempo t, e qual é a amplitude V de v (t)?
R R R
IDEIA-CHAVE
Em um circuito com uma carga puramente resistiva, a diferença de potencial v (t) entre os terminais do resistor é igual à diferença
R
de potencial (t) entre os terminais do gerador.
Cálculos: Nesse caso, v (t) = (t) e V = . Como é conhecida, podemos escrever
R R
Para determinar v (t), usamos a Eq. 31-28 para escrever
R
e, em seguida, fazemos = 36,0 V e
ω = 2πf = 2π(60 Hz) 120π
d d

para obter
v = (36,0 V) sen(120πt),
R
Podemos deixar o argumento do seno nessa forma, por conveniência, ou escrevê-lo como (377 rad/s)t ou (377 s−1)t.
(b) Qual é a corrente i (t) no resistor e qual é a amplitude I de i (t)?
R R R
IDEIA-CHAVE
Em um circuito de CA com uma carga resistiva pura, a corrente alternada i (t) no resistor está em fase com a diferença de potencial
R
alternada v (t) entre os terminais do resistor, ou seja, a constante de fase ϕ da corrente é zero.
R
Cálculos: Nesse caso, podemos escrever a Eq. 31-29 na forma
De acordo com a Eq. 31-33, a amplitude I é
R
Substituindo este valor e fazendo ω = 2πf = 120π na Eq. 31-35, obtemos
d d
Figura 31-10 Circuito formado por um capacitor C e um gerador de corrente alternada.
Carga Capacitiva
A Fig. 31-10 mostra um circuito formado por um capacitor C e um gerador de corrente alternada cuja
força eletromotriz é dada pela Eq. 31-28. Aplicando a regra das malhas e procedendo como fizemos para
obter a Eq. 31-30, descobrimos que a diferença de potencial entre os terminais do capacitor é dada por
em que V é a amplitude da tensão alternada no capacitor. Usando a definição de capacitância, também
C
podemos escrever

Nosso interesse, porém, está na corrente e não na carga. Assim, derivamos a Eq. 31-37 para obter
Vamos agora modificar a Eq. 31-38 de duas formas. Em primeiro lugar, para padronizar a notação,
vamos definir uma grandeza X , conhecida como reatância capacitiva de um capacitor, por meio da
C
relação
O valor de X depende da capacitância e da frequência angular de excitação ω . Sabemos, da definição
C d
de constante de tempo capacitiva (τ = RC), que a unidade de C no SI pode ser expressa em segundos por
ohm. Usando essa unidade na Eq. 31-39, vemos que a unidade de X no SI é o ohm, a mesma da
C
resistência R.
Em segundo lugar, substituímos cos ω t na Eq. 31-38 por um seno com um deslocamento de fase de
d
90o:
cos ω t = sen(ω t + 90°).
d d
Para mostrar que essa identidade está correta, basta deslocar uma senoide de 90o no sentido negativo.
Com as duas modificações, a Eq. 31-38 se torna
De acordo com a Eq. 31-29, podemos escrever a corrente i no capacitor da Fig. 31-10 na forma
C
em que I é a amplitude de i . Comparando as Eqs. 31-40 e 31-41, vemos que, para uma carga capacitiva
C C
pura, a constante de fase ϕ da corrente é −90o. Vemos também que a amplitude da tensão e a amplitude da
corrente estão relacionadas pela equação
Embora essa relação tenha sido demonstrada apenas para o circuito da Fig. 31-10, ela se aplica a
qualquer capacitância em qualquer circuito de corrente alternada.
Comparando as Eqs. 31-36 e 31-40 ou examinando a Fig. 31-11a, vemos que as grandezas v e i
C C
estão defasadas de 90o (o que equivale a π/2 rad ou um quarto de ciclo) e i está adiantada em relação a
C
v , ou seja, quando medimos i e v no circuito da Fig. 31-10 em função do tempo, i atinge o valor
C C C C

máximo um quarto de ciclo antes de v .
C
Essa relação entre i e v está ilustrada no diagrama fasorial da Fig. 31-11b. Enquanto os fasores
C C
que representam as duas grandezas giram com a mesma velocidade angular no sentido anti-horário, o
fasor I se mantém à frente do fasor V , e o ângulo entre os dois fasores tem um valor constante de 90o, ou
C C
seja, quando o fasor I coincide com o eixo vertical, o fasor V coincide com o eixo horizontal. É fácil
C C
verificar que o diagrama fasorial da Fig. 31-11b é compatível com as Eqs. 31-36 e 31-40.
o
Figura 31-11 (a) A corrente no capacitor está adiantada de 90 (= π/2 rad) em relação à tensão. (b) Diagrama fasorial correspondente ao
gráfico que está mostrado em (a).
Teste 4
A figura mostra, em (a), uma curva senoidal S(t) = sen(ω t) e três outras curvas senoidais A(t), B(t) e C(t), todas da forma sen(ω t
d d
− ϕ). (a) Coloque as outras três curvas na ordem do valor de ϕ, começando pelo maior valor positivo e terminando no maior valor
negativo. (b) Estabeleça a correspondência entre as curvas da parte (a) da figura e os fasores da parte (b). (c) Qual das curvas da
parte (a) está adiantada em relação a todas as outras?
Exemplo 31.04 Diferença de potencial e corrente para uma carga capacitiva pura

Na	Fig.	31-10,	a	capacitância	C	é	15,0	μF	e	o	gerador	produz	uma	força	eletromotriz	senoidal	de	amplitude	 	=	36,0	V	e
frequência	f 	=	60,0	Hz.
d
(a)	Qual	é	a	diferença	de	potencial	v (t)	entre	os	terminais	do	capacitor	em	função	do	tempo	e	qual	é	a	amplitude	V	de	v (t)?
C C C
IDEIA-CHAVE
Em	um	circuito	com	uma	carga	puramente	capacitiva,	a	diferença	de	potencial	v (t)	entre	os	terminais	do	capacitor	é	igual	à
C
| diferença	de	potencial	 | (t)	entre	os	terminais	do	gerador. |     |     |     |
| ----------------------- | ---------------------------------- | --- | --- | --- |
Cálculos:	Nesse	caso,	v (t)	=	 (t)	e	V	=	 .	Como	 	é	conhecida,	podemos	escrever
C C
| Para	determinar	v | (t),	usamos	a	Eq.	31-28	para	escrever |     |     |     |
| ----------------- | ------------------------------------- | --- | --- | --- |
C
Em	seguida,	fazemos	 	=	36,0	V	e	ω 	=	2πf 	=	120π	na	Eq.	31-43	para	obter
d d
| (b)	Qual	é	a	corrente	i | (t)	no	circuito	e	qual	é	a	amplitude	I	de	i | (t)? |     |     |
| ----------------------- | ------------------------------------------- | ---- | --- | --- |
|                         | C C                                         | C    |     |     |
IDEIA-CHAVE
Em	um	circuito	de	CA	com	uma	carga	capacitiva	pura,	a	corrente	alternada	i (t)	no	capacitor	está	adiantada	de	90o	em	relação	à
C
diferença	de	potencial	alternada	v (t)	entre	os	terminais	do	capacitor,	ou	seja,	a	constante	de	fase	ϕ	para	a	corrente	é	−90o	ou
C
−π/2	rad.
Cálculos:	Nesse	caso,	podemos	escrever	a	Eq.	31-29	na	forma
Para	calcular	a	amplitude	I	da	corrente	no	capacitor	usando	a	Eq.	31-42	(V	=	IX ),	precisamos	conhecer	a	reatância	capacitiva	X .
|     | C   |     | C C C | C   |
| --- | --- | --- | ----- | --- |
De	acordo	com	a	Eq.	31-39	(X 	=	1/ω C),	em	que	ω 	=	2πf ,	podemos	escrever
|     | C d d d |     |     |     |
| --- | ------- | --- | --- | --- |
Nesse	caso,	de	acordo	com	a	Eq.	31-42,	temos

Substituindo esse valor e ω = 2πf = 120π na Eq. 31-44, obtemos
d d
Carga Indutiva
A Fig. 31-12 mostra um circuito formado por um indutor L e um gerador de corrente alternada cuja força
eletromotriz é dada pela Eq. 31-28. Aplicando a regra das malhas e procedendo como fizemos para obter
a Eq. 31-30, constatamos que a diferença de potencial entre os terminais do indutor é dada por
em que V é a amplitude da tensão alternada v no indutor. Utilizando a Eq. 30-35 ( = −L di/dt),
L L
podemos escrever a diferença de potencial entre os terminais de um indutor L no qual a corrente está
variando à taxa di /dt na forma
L
Combinando as Eqs. 31-45 e 31-46, obtemos
Figura 31-12 Circuito formado por um indutor L e um gerador de corrente alternada.
Nosso interesse, porém, está na corrente e não na derivada da corrente em relação ao tempo. Assim,
integramos a Eq. 31-47 para obter
Vamos agora modificar a Eq. 31-48 de duas formas. Em primeiro lugar, para padronizar a notação,
vamos definir a grandeza X , conhecida como reatância indutiva de um indutor, por meio da relação
L

O valor de X depende tanto da indutância como da frequência angular de excitação ω . Sabemos, da
L d
definição de constante de tempo indutiva (τ = L/R), que a unidade de L no SI pode ser expressa em
L
ohms-segundos. Usando essa unidade na Eq. 31-49, vemos que a unidade de X no SI é o ohm, a mesma
L
da resistência R e da reatância capacitiva X .
C
Em segundo lugar, substituímos −cos ω t na Eq. 31-48 por um seno com um deslocamento de fase de
d
90o:
−cos ω t = sen(ω t − 90o).
d d
Para mostrar que a identidade está correta, basta deslocar uma senoide 90o no sentido positivo.
Com essas duas modificações, a Eq. 31-48 se torna
De acordo com a Eq. 31-29, também podemos escrever a corrente no indutor como
em que I é a amplitude de i . Comparando as Eqs. 31-50 e 31-51, vemos que, para uma carga indutiva
L L
pura, a constante de fase ϕ da corrente é +90o. Vemos também que a amplitude da tensão e a amplitude da
corrente estão relacionadas pela equação
Embora essa relação tenha sido demonstrada apenas para o circuito da Fig. 31-12, ela se aplica a
qualquer indutância em qualquer circuito de corrente alternada.
Comparando as Eqs. 31-45 e 31-50 ou examinando a Fig. 31-13a, vemos que as grandezas v e i
L L
estão defasadas de 90o, e i está atrasada em relação a v , ou seja, quando medimos i e v no circuito da
L L L L
Fig. 31-12 em função do tempo, i atinge o valor máximo um quarto de ciclo depois de v .
L L
Essa relação entre i e v está ilustrada no diagrama fasorial da Fig. 31-13b. Enquanto os fasores
L L
que representam as duas grandezas giram com a mesma velocidade angular no sentido anti-horário, o
fasor V se mantém à frente do fasor I e o ângulo entre os dois fasores tem um valor constante de 90o, ou
L L
seja, quando o fasor V coincide com o eixo vertical, o fasor I coincide com o eixo horizontal. É fácil
L L
verificar que o diagrama fasorial da Fig. 31-13b é compatível com as Eqs. 31-45 e 31-50.

o
Figura 31-13 (a) A corrente no indutor está adiantada de 90 (= π/2 rad) em relação à tensão. (b) Diagrama fasorial correspondente ao
gráfico mostrado em (a).
Teste 5
Quando aumentamos a frequência de excitação de um circuito que contém uma carga capacitiva pura, (a) a amplitude V aumenta,
C
diminui ou permanece a mesma? (b) A amplitude I aumenta, diminui ou permanece a mesma? Quando aumentamos a frequência
C
de excitação de um circuito que contém uma carga indutiva pura, (c) a amplitude V aumenta, diminui ou permanece a mesma? (d)
L
A amplitude I aumenta, diminui ou permanece a mesma?
L
Táticas para a Solução de Problemas
Tensões e Correntes em Circuitos de CA: A Tabela 31-2 mostra a relação entre a corrente i e a tensão v nos três tipos de
componentes que acabamos de discutir. Quando uma tensão alternada é aplicada a esses componentes, a corrente está em fase
com a tensão nos resistores, está adiantada em relação à tensão nos capacitores e está atrasada em relação à tensão nos indutores.
Alguns estudantes usam a frase mnemônica “ELI, que TOLICE!” para não esquecer essas relações. ELI contém a letra L

(símbolo	do	indutor),	e	nessa	palavra	a	letra	I	(símbolo	de	corrente)	vem	depois	da	letra	E	(símbolo	de	força	eletromotriz	ou
tensão).	Assim,	em	um	indutor	a	corrente	está	atrasada	em	relação	à	tensão.	Por	outro	lado,	a	palavra	TOLICE	contém	a	letra	C
(símbolo	do	capacitor),	e	nessa	palavra	a	letra	I	vem	antes	da	letra	E,	que	significa	que	a	corrente	está	adiantada	em	relação	à
tensão.	O	leitor	também	pode	usar	a	frase	“Positivamente,	ELI,	isso	é	uma	TOLICE!”	para	se	lembrar	de	que	a	constante	de	fase	é
positiva	para	os	indutores.
Se	o	leitor	tiver	dificuldade	para	lembrar	se	X 	é	igual	a	ω C	(errado)	ou	1/ω C	(certo),	pense	que	C	fica	na	“cova”,	ou	seja,	no
|     |     |     | C   | d   | d   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
denominador.
Tabela	31-2	Relações	de	Fase	e	Amplitude	para	Correntes	e	Tensões	Alternadas
Resistência
|            |         |     |     |                  |     | Constante	de	Fase | Relação	de |
| ---------- | ------- | --- | --- | ---------------- | --- | ----------------- | ---------- |
| Componente | Símbolo | ou  |     | Fase	da	Corrente |     |                   |            |
|            |         |     |     |                  |     | (ou	Ângulo)	ϕ     | Amplitudes |
Reatância
| Resistor | R   | R   | Em	fase	com	v |     |     | 0o	(=	0	rad) | V	=	IR |
| -------- | --- | --- | ------------- | --- | --- | ------------ | ------ |
|          |     |     | R             |     |     |              | R R    |
−90o	(=	−π/2
| Capacitor | L   |           | Adiantada	de	90o	(=	π/2	rad)	em	relação	a	v |     |     |      |        |
| --------- | --- | --------- | ------------------------------------------- | --- | --- | ---- | ------ |
|           |     | X 	=	1/ωC |                                             |     |     |      | V	=	IX |
|           |     | C d       |                                             |     | C   | rad) | C C C  |
+90o	(=	+π/2
Indutor C X	=	ωL Atrasada	de	90o	(=	π/2	rad)	em	relação	a	v V	=	IX
|     |     | L d |     |     | L   | rad) | L L L |
| --- | --- | --- | --- | --- | --- | ---- | ----- |
	Exemplo	31.05	Diferença	de	potencial	e	corrente	para	uma	carga	indutiva	pura
Na	Fig.	31-12,	a	indutância	L	é	230	mH	e	o	gerador	produz	uma	força	eletromotriz	de	amplitude	 	=	36,0	V	e	frequência	f 	=
d
60,0	Hz.
(a)	Qual	é	a	diferença	de	potencial	v (t)	entre	os	terminais	do	indutor	e	qual	é	a	amplitude	V	de	v (t)?
|     |     | L   |     |     | L   | L   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
IDEIA-CHAVE
Em	um	circuito	com	uma	carga	puramente	indutiva,	a	diferença	de	potencial	v (t)	entre	os	terminais	do	indutor	é	sempre	igual	à
L
| diferença	de	potencial	 |     | (t)	entre	os	terminais	do	gerador. |     |     |     |     |     |
| ----------------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
Cálculos:	Nesse	caso,	v (t)	=	 (t)	e	V	=	 .	Como	 	é	conhecida,	podemos	escrever
|                   | L                                     |     | L   |     |     |     |     |
| ----------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
| Para	determinar	v | (t),	usamos	a	Eq.	31-28	para	escrever |     |     |     |     |     |     |
L

Em	seguida,	fazemos	 	=	36,0	V	e	ω 	=	2πf 	=	120π	na	Eq.	31-53	para	obter
d d
| (b)	Qual	é	a	corrente	i | (t)	no	circuito	e	qual	é	a	amplitude	I	de	i |     | (t)? |     |
| ----------------------- | ------------------------------------------- | --- | ---- | --- |
|                         | L                                           | L   | L    |     |
IDEIA-CHAVE
Em	um	circuito	de	CA	com	uma	carga	indutiva	pura,	a	corrente	alternada	i (t)	no	indutor	está	atrasada	90o	em	relação	à	diferença
L
de	potencial	alternada	v (t)	entre	os	terminais	do	indutor,	ou	seja,	a	constante	de	fase	ϕ	para	a	corrente	é	90o	ou	π/2	rad.	(Usando
L
o	artifício	mnemônico	da	Tática	1,	esse	circuito	é	“positivamente	um	circuito	ELI”,	o	que	nos	diz	que	a	força	eletromotriz	E	está
adiantada	em	relação	à	corrente	I	e	que	o	ângulo	de	fase	ϕ	é	positivo.)
Cálculos:	Como	o	ângulo	de	fase	ϕ	da	corrente	é	+90o	ou	+π/2	rad,	podemos	escrever	a	Eq.	31-29	na	forma
Para	calcular	a	amplitude	I	da	corrente	no	indutor	usando	a	Eq.	31-52	(V	=	IX ),	precisamos	conhecer	a	reatância	indutiva	X .	De
|                           | L                 |                           | L L L | L   |
| ------------------------- | ----------------- | ------------------------- | ----- | --- |
| acordo	com	a	Eq.	31-49	(X | 	=	ω L),	em	que	ω | 	=	2πf ,	podemos	escrever |       |     |
|                           | L d               | d d                       |       |     |
Nesse	caso,	de	acordo	com	a	Eq.	31-52,	temos
| Substituindo	esse	valor	e	ω | 	=	2πf 	=	120π	na	Eq.	31-54,	obtemos |     |     |     |
| --------------------------- | ------------------------------------ | --- | --- | --- |
d d
31-4	O	CIRCUITO	RLC	SÉRIE
Objetivos	do	Aprendizado
Depois	de	ler	este	módulo,	você	será	capaz	de	...
31.32	Desenhar	o	diagrama	esquemático	de	um	circuito	RLC	série.
31.33	Saber	em	que	condições	um	circuito	RLC	série	é	mais	indutivo	que	capacitivo,	mais	capacitivo	que	indutivo,	ou	está	em
ressonância.
31.34	Desenhar	gráficos	da	tensão	e	da	corrente	em	função	do	tempo	e	diagramas	fasoriais	para	circuitos	RLC	série	mais
indutivos	que	capacitivos,	mais	capacitivos	que	indutivos	e	em	ressonância.

31.35 Calcular a impedância Z de um circuito RLC série.
31.36 Conhecer a relação entre a amplitude I da corrente, a impedância Z e a amplitude da força eletromotriz.
31.37 Conhecer a relação entre a constante de fase ϕ e as tensões V e V e a relação entre a constante de fase ϕ, a
L C
resistência R e as reatâncias X e X .
L C
31.38 Conhecer os possíveis valores da constante de fase ϕ para um circuito mais indutivo que capacitivo, mais capacitivo que
indutivo ou que está em ressonância.
31.39 Conhecer a relação entre a frequência angular de excitação ω , a frequência angular natural ω, a indutância L e a
d
capacitância C.
31.40 Desenhar uma curva da amplitude da corrente em função da razão ω /ω, mostrar as regiões correspondentes a um
d
circuito mais indutivo que capacitivo, mais capacitivo que indutivo ou que está em ressonância, e explicar o que acontece
com a curva quando a resistência aumenta.
Ideias-Chave
• No caso de um circuito RLC série alimentado por uma fonte cuja força eletromotriz é dada por
e cuja corrente é dada por
i = I sen(ω t − ϕ),
d
a amplitude da corrente é dada por
• A constante de fase é dada por
• A impedância do circuito é
• A amplitude da corrente está relacionada à força eletromotriz da fonte e à impedância do circuito pela equação
• A amplitude I da corrente é máxima (I = /R) quando a frequência angular de excitação ω é igual à frequência angular natural
d
ω do circuito, uma situação conhecida como ressonância. Na ressonância, X = X , ϕ = 0, e a corrente está em fase com a
C L
força eletromotriz.
O Circuito RLC Série

Agora estamos em condições de analisar o caso em que a força eletromotriz alternada da Eq. 31-28,
é aplicada ao circuito RLC da Fig. 31-7. Como R, L e C estão em série, a mesma corrente
atravessa os três componentes. Estamos interessados em determinar a amplitude I e a constante de fase ϕ
da corrente e investigar a variação dessas grandezas com a frequência angular de excitação ω . A solução
d
é facilitada pelo uso de diagramas fasoriais como os que foram apresentados para os três circuitos
básicos no Módulo 31-3: carga capacitiva, carga indutiva e carga resistiva. Em particular, vamos fazer
uso das relações entre o fasor de tensão e o fasor da corrente nos três circuitos básicos. Vamos ver que os
circuitos RLC podem ser divididos em três tipos: mais indutivos que capacitivos, mais capacitivos que
indutivos e em ressonância.
Amplitude da Corrente
Começamos pela Fig. 31-14a, em que o fasor que representa a corrente da Eq. 31-56 é mostrado em um
instante de tempo arbitrário t. O comprimento do fasor é a amplitude I da corrente, a projeção do fasor no
eixo vertical é a corrente i no instante t e o ângulo de rotação do fasor é a fase ω t − ϕ da corrente no
d
instante t.
A Fig. 31-14b mostra os fasores que representam as tensões entre os terminais de R, L e C no mesmo
instante t. Os fasores estão orientados em relação ao fasor de corrente I da Fig. 31-14a de acordo com as
informações da Tabela 31-2.
Resistor: A corrente e tensão estão em fase e, portanto, o ângulo de rotação do fasor de tensão V é igual
R
ao ângulo de rotação da corrente I.
Capacitor: A corrente está adiantada de 90o em relação à tensão e, portanto, o ângulo de rotação do fasor
de tensão V é igual ao ângulo de rotação da corrente I menos 90o.
C
Indutor: A corrente está atrasada de 90o em relação à tensão e, portanto, o ângulo de rotação do fator de
tensão V é igual ao ângulo de rotação da corrente I mais 90o.
L
A Fig. 31-14b mostra também as tensões instantâneas v , v e v entre os terminais de R, C e L no
R C L
instante t; essas tensões são as projeções dos três fasores no eixo vertical da figura.
A Fig. 31-14c mostra o fasor que representa a força eletromotriz aplicada da Fig. 31-55. O
comprimento do fasor é o valor absoluto da força eletromotriz , a projeção do fasor no eixo vertical é
o valor da força eletromotriz no instante t, e o ângulo de rotação do fasor é a fase ω t da força
d
eletromotriz no instante t.
De acordo com a regra das malhas, a soma das tensões v , v e v é igual à força eletromotriz
R C L
aplicada :

Assim,	a	projeção	 	da	Fig.	31-14c	é	igual	a	soma	algébrica	das	projeções	v ,	v 	e	v 	da	Fig.	31-14b.
R C L
Como	todos	os	fasores	giram	com	a	mesma	velocidade	angular,	a	igualdade	é	mantida	para	qualquer
ângulo	de	rotação.	Em	particular,	isso	significa	que	o	fasor	 	da	Fig.	31-14c	é	igual	à	soma	vetorial	dos
| fasores	V | ,	V 	e	V 	da	Fig.	31-14b. |     |     |
| --------- | ------------------------- | --- | --- |
R C L
Essa	relação	está	indicada	na	Fig.	31-14d,	em	que	o	fasor	 	foi	desenhado	como	a	soma	dos	fasores
V ,	V 	e	V .	Como	os	fasores	V 	e	V 	têm	a	mesma	direção	e	sentidos	opostos,	podemos	simplificar	a
| R L | C   | L C |     |
| --- | --- | --- | --- |
soma	vetorial	combinando	V 	e	V 	para	formar	o	fasor	V 	−	V .	Em	seguida,	combinamos	esse	fasor	com
|     | L   | C   | L C |
| --- | --- | --- | --- |
V 	para	obter	o	fasor	total.	Como	vimos,	esse	fasor	é	igual	ao	fasor	 .
R
Os	dois	triângulos	da	Fig.	31-14d	são	triângulos	retângulos.	Aplicando	o	teorema	de	Pitágoras	a	um
deles,	obtemos
De	acordo	com	as	informações	da	Tabela	31-2,	essa	equação	pode	ser	escrita	na	forma
que,	depois	de	explicitarmos	a	corrente	I,	se	torna
Figura	31-14 	(a)	Fasor	que	representa	a	corrente	alternada	no	circuito	RLC	da	Fig.	31-7	em	um	instante	de	tempo	t.	O	diagrama	mostra	a
amplitude	I,	o	valor	instantâneo	i	e	a	fase	(ω t	−	ϕ)	da	corrente.	(b)	Fasores	que	representam	as	tensões	no	indutor,	no	resistor	e	no	capacitor,
d
orientados	em	relação	ao	fasor	do	item	(a),	que	representa	a	corrente.	(c)	Fasor	que	representa	a	força	eletromotriz	alternada	responsável
pela	corrente	representada	em	(a).	(d)	O	fasor	de	força	eletromotriz	é	igual	à	soma	vetorial	dos	três	fasores	de	tensão	representados	em	(b).
| Os	fasores	de	tensão	V | 	e	V 	foram	combinados	para	formar	o	fasor	V |     | 	−	V . |
| ---------------------- | -------------------------------------------- | --- | ------ |
|                        | L C                                          |     | L C    |
O	denominador	da	Eq.	31-60	é	chamado	de	impedância	do	circuito	para	a	frequência	de	excitação

ω e representado pelo símbolo Z:
d
Assim, a Eq. 31-60 pode ser escrita na forma
Substituindo X e X por seus valores, fornecidos pelas Eqs. 31-39 e 31-49, podemos escrever a Eq.
C L
31-60 na forma mais explícita:
Com isso, atingimos um dos nossos objetivos: expressar a amplitude I da corrente de um circuito
RLC série em função da força eletromotriz senoidal aplicada e do valor dos componentes.
O valor de I depende da diferença entre ω L e 1/ω C na Eq. 31-63 ou, o que é equivalente, da
d d
diferença entre X e X na Eq. 31-60. Nas duas equações, não importa qual das duas grandezas é maior, já
L C
que a diferença aparece elevada ao quadrado.
A corrente que estamos discutindo neste módulo é a corrente estacionária, que só é observada
algum tempo após a aplicação da força eletromotriz ao circuito. Nos momentos que se seguem à
aplicação da força eletromotriz, existe no circuito uma corrente transitória cuja duração (até que a
corrente estacionária se estabeleça) depende das constantes de tempo τ = L/R e τ = RC, o tempo
L C
necessário para que o capacitor e o indutor sejam “carregados”. A corrente transitória pode, por
exemplo, destruir um motor durante a partida se não foi levada em consideração no projeto do circuito do
motor.
Constante de Fase
De acordo com o triângulo de fasores da direita da Fig. 31-14d e a Tabela 31-2, podemos escrever
o que nos dá
Com isso, atingimos nosso segundo objetivo: expressar a constante de fase ϕ da corrente de um circuito

RLC série em função da força eletromotriz senoidal aplicada (neste caso, na verdade, o que importa é
apenas a frequência ω da força eletromotriz) e do valor dos componentes. Podemos obter três resultados
d
diferentes para a constante de fase, dependendo dos valores relativos de X e X .
L C
X > X : Nesse caso, dizemos que o circuito é mais indutivo que capacitivo. De acordo com a Eq. 31-
L C
65, ϕ é positivo em um circuito desse tipo, o que significa que o fasor I está atrasado em relação ao
fasor (Fig. 31-15a). Os gráficos de e i em função do tempo são semelhantes aos da Fig. 31-15b.
(As Figs. 31-14c e 31-14d foram desenhadas supondo que X > X .)
L C
X > X : Nesse caso, dizemos que o circuito é mais capacitivo que indutivo. De acordo com a Eq. 31-
C L
65, ϕ é negativo em um circuito desse tipo, o que significa que o fasor I está adiantado em relação ao
fasor (Fig. 31-15c). Os gráficos de e i em função do tempo são semelhantes aos da Fig. 31-15d.
X = X : Nesse caso, dizemos que o circuito está em ressonância, um estado que será discutido a seguir.
C L
De acordo com a Eq. 31-65, ϕ = 0o em um circuito desse tipo, o que significa que os fasores I e
estão em fase (Fig. 31-15e). Os gráficos de e i em função do tempo são semelhantes aos da Fig. 31-
15f.
Figura 31-15 Diagramas fasoriais e gráficos da força eletromotriz alternada e da corrente i para o circuito RLC da Fig. 31-7. No
diagrama fasorial (a) e no gráfico (b), a corrente i está atrasada em relação à força eletromotriz , e a constante de fase da corrente é
positiva. Em (c) e (d), a corrente i está adiantada em relação à força eletromotriz , e a constante de fase ϕ é negativa. Em (e) e (f), a
corrente está em fase com a força eletromotriz , e a constante de fase ϕ é zero.

Como ilustração, vamos considerar dois casos extremos: No circuito puramente indutivo da Fig.
31-12, em que X ≠ 0 e X = R = 0, a Eq. 31-65 nos dá ϕ = 90o (o valor máximo de ϕ), o que está de
L C
acordo com a Fig. 31-13b. No circuito puramente capacitivo da Fig. 31-10, em que X ≠ 0 e X = R = 0,
C L
a Eq. 31-65 nos dá ϕ = −90o (o valor mínimo de ϕ), o que está de acordo com a Fig. 31-11b.
Ressonância
A Eq. 31-63 fornece a amplitude I da corrente em um circuito RLC em função da frequência de excitação
ω da força eletromotriz aplicada. Para uma dada resistência R, a amplitude é máxima quando o termo
d
ω L − 1/ω C do denominador é zero, ou seja, quando
d d
Como a frequência angular natural ω do circuito RLC também é igual a , o valor I é máximo quando
a frequência angular de excitação é igual à frequência natural, ou seja, na ressonância. Assim, em um
circuito RLC série, a frequência angular de excitação para a qual a corrente é máxima e a frequência
angular de ressonância são dadas por
Curvas de Ressonância. A Fig. 31-16 mostra três curvas de ressonância para excitações senoidais
em três circuitos RLC série que diferem apenas quanto ao valor de R. As três curvas atingem o máximo
de amplitude I quando a razão ω /ω é 1,00, mas o valor máximo de I é inversamente proporcional a R. (O
d
valor máximo de I é sempre igual a /R; para entender a razão, basta combinar as Eqs. 31-61 e 31-62.)
Além disso, a largura das curvas (medida na Fig. 31-16 em metade do valor máximo de I) aumenta
quando R aumenta.

Figura	31-16 	Curvas	de	ressonância	do	circuito	RLC	da	Fig.	31-7	para	L	=	100	μH,	C	=	100	pF	e	três	valores	diferentes	de	R.	A
amplitude	I	da	corrente	alternada	depende	da	diferença	entre	a	frequência	angular	de	excitação	ω 	e	a	frequência	angular	natural	ω.	A	seta
d
horizontal	em	cada	curva	mostra	a	largura	a	meia	altura,	que	é	a	largura	da	curva	nos	pontos	em	que	a	corrente	é	metade	da	corrente
máxima	e	constitui	uma	medida	da	seletividade	do	circuito.	À	esquerda	do	ponto	ω /ω	=	1,00,	o	circuito	é	principalmente	mais	capacitivo	que
d
| indutivo,	com	X | 	>	X ;	à	direita,	é	mais	indutivo	que	capacitivo,	com	X | 	>	X . |
| --------------- | ------------------------------------------------------- | ------ |
|                 | C L                                                     | L C    |
Para	compreender	o	significado	físico	da	Fig.	31-16,	considere	o	modo	como	as	reatâncias	X 	e	X
L C
variam	quando	aumentamos	a	frequência	angular	de	excitação	ω ,	começando	com	um	valor	muito	menor
d
que	a	frequência	natural	ω.	Para	pequenos	valores	de	ω ,	a	reatância	X 	(=	ω L)	é	pequena	e	a	reatância
d L d
X 	(=	1/ω C)	é	grande.	Assim,	o	circuito	é	altamente	capacitivo	e	a	impedância	é	dominada	pelo	elevado
| C          | d                              |     |
| ---------- | ------------------------------ | --- |
| valor	de	X | ,	que	mantém	a	corrente	baixa. |     |
C
Quando	aumentamos	ω ,	a	reatância	X 	continua	a	dominar,	mas	diminui	gradualmente,	enquanto	a
d C
reatância	X 	 aumenta.	 Com	 a	 diminuição	 de	 X ,	 a	 impedância	 diminui	 e	 a	 corrente	 aumenta,	 como
|     | L C |     |
| --- | --- | --- |
podemos	ver	no	lado	esquerdo	da	curva	de	ressonância	da	Fig.	31-16.	Quando	a	diminuição	de	X 	e	o
C
aumento	de	X 	fazem	com	que	as	duas	reatâncias	sejam	iguais,	a	corrente	atinge	o	valor	máximo	e	o
L
circuito	está	em	ressonância,	com	ω 	=	ω.
d
Quando	ω 	continua	a	aumentar,	a	reatância	X 	se	torna	cada	vez	mais	dominante	em	relação	à
|     | d   | L   |
| --- | --- | --- |
reatância	X .	A	impedância	aumenta	por	causa	de	X 	e	a	corrente	diminui,	como	do	lado	direito	da	curva
|     | C   | L   |
| --- | --- | --- |
de	ressonância	da	Fig.	31-16.	Resumindo:	O	lado	de	baixa	frequência	angular	da	curva	de	ressonância	é

dominado pela reatância do capacitor, o lado de alta frequência angular é dominado pela reatância do
indutor e a ressonância acontece no centro da curva.
Teste 6
As reatâncias capacitiva e indutiva, respectivamente, de três circuitos RLC série excitados senoidalmente são: (1) 50 Ω, 100 Ω; (2)
100 Ω, 50 Ω; (3) 50 Ω, 50 Ω. (a) Responda para cada circuito: A corrente está adiantada em relação à força eletromotriz aplicada,
está atrasada em relação à força eletromotriz aplicada ou a corrente e a força eletromotriz aplicada estão em fase? (b) Qual dos
circuitos está em ressonância?
Exemplo 31.06 Amplitude da corrente, impedância e constante de fase
No circuito da Fig. 31-7, Sejam R = 200 Ω, C = 15,0 μF, L = 230 mH, f = 60,0 Hz e = 36,0 V. (Os valores dos parâmetros são os
d
mesmos de exemplos anteriores.)
(a) Qual é a amplitude I da corrente?
IDEIA-CHAVE
De acordo com a Eq. 31-62 (I = /Z), a amplitude da corrente I depende da amplitude da força eletromotriz aplicada e da
impedância Z do circuito.
Cálculos: Precisamos determinar o valor de Z, que depende da resistência R, da reatância capacitiva X e da reatância indutiva X . A
C L
resistência do circuito é a resistência do resistor R. A reatância capacitiva é a reatância do capacitor C; de acordo com um exemplo
anterior, X = 177 Ω. A reatância indutiva é a reatância do indutor L; de acordo com um exemplo anterior, X = 86,7 Ω. A
C L
impedância do circuito é, portanto,
Assim, temos
(b) Qual é a constante de fase ϕ da corrente no circuito em relação à força eletromotriz aplicada?
IDEIA-CHAVE

De acordo com a Eq. 31-65, a constante de fase depende da reatância indutiva, da reatância capacitiva e da resistência.
Cálculo: Explicitando ϕ na Eq. 31-65, obtemos
O fato de obtermos uma constante de fase negativa já era esperado, pois a carga é principalmente capacitiva, com X > X . Nas
C L
palavras da frase mnemônica, este é um circuito TOLICE — a corrente está adiantada em relação à força eletromotriz.
31-5 POTÊNCIA EM CIRCUITOS DE CORRENTE ALTERNADA
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
31.41 Conhecer a relação entre o valor médio quadrático e a amplitude da corrente, a tensão e força eletromotriz nos circuitos
de CA.
31.42 Desenhar a corrente e a tensão em função do tempo para um circuito de CA puramente capacitivo, puramente indutivo e
puramente resistivo, e indicar o valor de pico e o valor médio quadrático da corrente e da tensão em cada caso.
31.43 Conhecer a relação entre a potência média P , a corrente média quadrática I e a resistência R.
méd rms
31.44 Calcular a potência instantânea armazenada ou dissipada nos componentes de um circuito RLC série alimentado por uma
fonte alternada.
31.45 No caso de um circuito RLC série alimentado por uma fonte alternada, explicar o que acontece (a) com o valor médio da
energia armazenada no circuito e (b) com o valor médio da energia fornecida ao circuito pela fonte ao ser atingido o regime
estacionário.
31.46 Conhecer a relação entre o fator de potência cos ϕ, a resistência R e a impedância Z de um circuito de CA.
31.47 Conhecer a relação entre a potência média P , a força eletromotriz média quadrática , a corrente média quadrática
méd rms
I e o fator de potência cos ϕ.
rms
31.48 Saber qual é o valor do fator de potência para o qual a potência dissipada na carga resistiva é máxima.
Ideias-Chave
• Em um circuito RLC série alimentado por uma fonte de CA, a potência média P fornecida pela fonte é igual à potência
méd
dissipada no resistor:
• O nome rms é um acrônimo de root-mean-square (valor médio quadrático, em inglês). Os valores rms da corrente, da tensão
e da força eletromotriz estão relacionados aos valores máximos das respectivas grandezas pelas equações
. O fator cos ϕ é chamado de fator de potência do circuito.
Potência em Circuitos de Corrente Alternada

No circuito RLC da Fig. 31-7, a fonte de energia é o gerador de corrente alternada. Parte da energia
fornecida pelo gerador é armazenada no campo elétrico do capacitor, parte é armazenada no campo
magnético do indutor e parte é dissipada como energia térmica no resistor. No regime estacionário, isto é,
depois de transcorrido um tempo suficiente para que o circuito se estabilize, a energia média armazenada
no capacitor e no indutor juntos permanece constante. A transferência líquida de energia é, portanto, do
gerador para o resistor, onde a energia eletromagnética é convertida em energia térmica.
2
Figura 31-17 (a) Gráfico de sen θ em função de θ. O valor médio da função ao longo de um ciclo é zero. (b) Gráfico de sen θ em função
de θ. O valor médio da função ao longo de um ciclo é 1/2.
A taxa instantânea com a qual a energia é dissipada no resistor pode ser escrita, com a ajuda das
Eqs. 26-27 e 31-29, na forma
A taxa média com a qual a energia é dissipada no resistor é a média no tempo da Eq. 31-68. Em um ciclo
completo, o valor médio de sen θ é zero (Fig. 31-17a), mas o valor médio de sen2 θ é 1/2 (Fig. 31-17b).
(Observe na Fig. 31-17b que as partes sombreadas sob a curva, que ficam acima da reta horizontal +1/2,
completam exatamente os espaços vazios que ficam abaixo da mesma reta.) Assim, de acordo com a Eq.
31-68, podemos escrever
A grandeza é chamada valor médio quadrático, ou valor rms,1 da corrente I:

Podemos escrever a Eq. 31-69 na forma
A Eq. 31-71 tem a mesma forma que a Eq. 26-27 (P = i2R); isso significa que, usando a corrente rms,
podemos calcular a taxa média de dissipação de energia em circuitos de corrente alternada como se
estivéssemos trabalhando com um circuito de corrente contínua.
Podemos também definir o valor rms de uma tensão alternada e de uma força eletromotriz alternada:
Os instrumentos usados em circuitos de corrente alternada, como amperímetros e voltímetros, são quase
sempre calibrados para indicar valores de I , V e . Assim, quando ligamos um voltímetro de
rms rms rms
corrente alternada a uma tomada de parede e obtemos um valor de 120 V, trata-se da tensão rms. O valor
máximo da diferença de potencial em uma tomada de parede é . Em geral, os cientistas
e engenheiros usam os valores rms das grandezas elétricas, e não os valores máximos.
Como o fator de proporcionalidade nas Eqs. 31-70 e 31-72 é o mesmo para as três variáveis,
podemos escrever as Eqs. 31-62 e 31-60 como
e, na verdade, essa é, na prática, a forma que mais se usa.
Podemos usar a relação I = /Z para escrever a Eq. 31-71 de outra forma. Temos
rms rms
Acontece que, de acordo com a Fig. 31-14d, a Tabela 31-2 e a Eq. 31-62, R/Z é o cosseno da
constante de fase ϕ:
A Eq. 31-74 se torna, portanto,
em que o termo cos ϕ recebe o nome de fator de potência. Como cos ϕ = cos(−ϕ), a Eq. 31-76 é
independente do sinal da constante de fase ϕ.
Para maximizar a taxa com a qual a energia é fornecida a uma carga resistiva em um circuito RLC,

devemos manter o fator de potência o mais próximo possível da unidade, o que equivale a manter a
constante de fase ϕ da Eq. 31-29 o mais próximo possível de zero. Se, por exemplo, o circuito é
altamente indutivo, ele pode se tornar menos indutivo ligando um capacitor adicional em série com o
circuito. (Lembre-se de que colocar uma capacitância em série com uma capacitância já existente reduz a
capacitância total C e de que a reatância capacitiva é inversamente proporcional à capacitância.) As
eq
empresas de energia elétrica costumam ligar capacitores em série com as linhas de transmissão para
obter esse resultado.
Teste 7
(a) Se a corrente em um circuito RLC série com excitação senoidal está adiantada em relação à força eletromotriz, devemos
aumentar ou diminuir a capacitância para aumentar a taxa com a qual a energia da fonte é fornecida à resistência? (b) Essa
mudança aproxima ou afasta a frequência de ressonância do circuito da frequência da força eletromotriz da fonte?
Exemplo 31.07 Fator de potência e potência média de um circuito RLC alimentado por uma fonte
Um circuito RLC série, alimentado por uma fonte com = 120 V e f = 60,0 Hz, contém uma resistência R = 200 Ω, uma
rms d
indutância com uma reatância indutiva X = 80,0 Ω e uma capacitância com uma reatância capacitiva X = 150 Ω.
L C
(a) Determine o fator de potência cos ϕ e a constante de fase ϕ do circuito.
IDEIA-CHAVE
O fator de potência cos ϕ pode ser calculado a partir da resistência R e da impedância Z usando a Eq. 31-75 (cos ϕ = R/Z).
Cálculos: Para calcular Z, usamos a Eq. 31-61:
A Eq. 31-75 nos dá
Tomando o arco cosseno, obtemos
ϕ = cos−1 0,944 = ±19,3o
Tanto +19,3o como −19,3o têm um cosseno de 0,944. Para determinar qual é o sinal correto, temos que verificar se a corrente
está adiantada ou atrasada em relação à força eletromotriz. Como X > X , o circuito é mais capacitivo que indutivo, com a corrente
C L

adiantada em relação à força eletromotriz. Assim, o ângulo de fase ϕ deve ser negativo:
Poderíamos também ter usado a Eq. 31-65 para calcular ϕ. Nesse caso, uma calculadora forneceria a resposta já com o sinal
negativo.
(b) Qual é a taxa média P com a qual a energia é dissipada na resistência?
méd
IDEIAS-CHAVE
Existem duas formas de abordar o problema: (1) Como estamos supondo que o circuito está no regime estacionário, a taxa com a
qual a energia é dissipada na resistência é igual à taxa com a qual a energia é fornecida ao circuito, que pode ser calculada com o
auxílio da Eq. 31-76 (P = I cos ϕ). (2) A taxa com a qual a energia é dissipada na resistência R pode ser calculada a partir
méd rmsrms
do valor rms da corrente, I , usando a Eq. 31-71 .
rms
Primeira abordagem: O valor rms da força eletromotriz, , é um dos dados do problema, e o valor de cos ϕ foi calculado no
rms
item (a). O valor de I pode ser calculado a partir do valor rms da força eletromotriz e da impedância Z do circuito (que é
rms
conhecida) usando a Eq. 31-73:
Substituindo este resultado na Eq. 31-76, obtemos
Segunda abordagem: Temos
(c) Que nova capacitância C deve ser usada no circuito para maximizar P sem mudar os outros parâmetros do circuito?
nova méd
IDEIAS-CHAVE
(1) A taxa média P com a qual a energia é fornecida e dissipada é máxima quando o circuito está em ressonância com a força
méd
eletromotriz aplicada. (2) A ressonância acontece para X = X .
C L

Cálculos: De acordo com os dados do problema, temos X > X . Assim, precisamos reduzir X para conseguir a ressonância. De
C L C
acordo com a Eq. 31-39 (X = 1/ω C); isso significa que a nova capacitância deve ser maior que a anterior.
C d
De acordo com a Eq. 31-39, a condição X = X pode ser escrita na forma
C L
Substituindo ω por 2πf (porque conhecemos f e não ω ) e explicitando C , obtemos
d d d d nova
Usando o mesmo método do item (b), é possível mostrar que com o novo valor de capacitância, C , P atinge o valor máximo
nova méd
de
31-6 TRANSFORMADORES
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
31.49 Saber por que as linhas de transmissão de energia elétrica trabalham com baixa corrente e alta tensão.
31.50 Saber por que é preciso usar transformadores nas duas extremidades de uma linha de transmissão.
31.51 Calcular a dissipação de energia em uma linha de transmissão.
31.52 Saber qual é a diferença entre o primário e o secundário de um transformador.
31.53 Conhecer a relação entre a tensão e o número de espiras nos dois lados de um transformador.
31.54 Saber qual é a diferença entre um transformador elevador de tensão e um transformador abaixador de tensão.
31.55 Conhecer a relação entre a corrente e o número de espiras nos dois lados de um transformador.
31.56 Conhecer a relação entre a potência de entrada e a potência de saída de um transformador ideal.
31.57 Saber calcular a resistência equivalente da carga do ponto de vista do primário de um transformador.
31.58 Conhecer a relação entre a resistência equivalente e a resistência real.
31.59 Explicar qual é o papel de um transformador no casamento de impedâncias.
Ideias-Chave
• Um transformador (considerado ideal) é formado por um núcleo de ferro que contém dois enrolamentos, o enrolamento
primário, com N espiras, e o enrolamento secundário, com N espiras. Se o enrolamento primário está ligado a um gerador de
p s
corrente alternada, a relação entre as tensões do enrolamento primário e do enrolamento secundário é dada por

• A relação entre as correntes nos dois enrolamentos é dada por
• A resistência equivalente do circuito secundário, do ponto de vista do gerador, é dada por
• em que R é a carga resistiva do circuito secundário. A razão N /N é chamada de relação de espiras do transformador.
p s
Transformadores
Necessidades de um Sistema de Transmissão de Energia Elétrica
Quando a carga de um circuito de corrente alternada é uma resistência pura, o fator de potência da Eq.
31-76 é cos 0o = 1 e a força eletromotriz aplicada é igual à tensão V entre os terminais da carga.
rms rms
Assim, com uma corrente I na carga, a energia é fornecida e dissipada a uma taxa média de
rms
(Na Eq. 31-77 e no restante deste módulo, vamos adotar a prática usual de omitir os índices que indicam
tratar-se de grandezas rms. A menos que seja dito explicitamente o contrário, os cientistas e engenheiros
supõem que os valores de todas as correntes e tensões alternadas são valores rms, já que são esses os
valores indicados pelos instrumentos de medida.) A Eq. 31-77 mostra que, para satisfazer a uma dada
necessidade de energia, temos uma larga faixa de opções, desde uma alta corrente I e uma baixa tensão V
até uma baixa corrente I e uma alta tensão V; o que importa, em termos de potência fornecida à carga, é o
produto IV.
Nos sistemas de distribuição de energia elétrica, é desejável, por motivos de segurança e para maior
eficiência dos equipamentos, que a tensão seja relativamente baixa tanto na ponta da geração (nas usinas
de energia elétrica) como na ponta do consumo (nas residências e indústrias). Ninguém acharia razoável
que uma torradeira ou um trem elétrico de brinquedo fosse alimentado com 10 kV. Por outro lado, na
transmissão de energia elétrica da usina de geração até o consumidor final, é desejável trabalhar com a
menor corrente possível (e, portanto, com a maior tensão possível) para minimizar as perdas do tipo I2R
(conhecidas como perdas ôhmicas) nas linhas de transmissão.
Considere, por exemplo, a linha de 735 kV usada para transmitir energia elétrica da usina
hidrelétrica La Grande 2, em Quebec, para a cidade de Montreal, situada a 1000 km de distância.
Suponha que a corrente é 500 A e que o fator de potência é praticamente 1. Nesse caso, de acordo com a

Eq. 31-77, a potência elétrica fornecida pela usina é
A resistência da linha de transmissão é da ordem de 0,220 Ω/km; assim, a resistência total para o
percurso de 1000 km é 220 Ω. A potência dissipada na linha devido a essa resistência é
P = I2R = (500 A)2(220 Ω) = 55,0 MW,
méd
que corresponde a quase 15% da potência total transmitida.
Imagine o que aconteceria se multiplicássemos a corrente por dois e reduzíssemos a tensão à
metade. A potência fornecida pela usina continuaria a mesma, 368 MW, mas a potência dissipada na linha
de transmissão passaria a ser
P = I2R = (1000 A)2(220 Ω) = 220 MW,
méd
que corresponde a quase 60% da potência total transmitida. É por isso que existe uma regra geral para as
linhas de transmissão de energia elétrica: Usar a maior tensão possível e a menor corrente possível.
O Transformador Ideal
A regra da transmissão de energia elétrica leva a uma incompatibilidade entre as condições para que a
eletricidade seja distribuída de forma eficiente e as condições para que seja gerada e utilizada de forma
segura. O problema, porém, pode ser contornado por um dispositivo capaz de aumentar (para a
transmissão) e reduzir (para o consumo) a tensão nos circuitos, mantendo praticamente constante o
produto corrente × tensão. Esse dispositivo é o transformador, que não tem partes móveis, utiliza a lei
de indução de Faraday e não funciona com corrente contínua.
O transformador ideal da Fig. 31-18 é formado por duas bobinas, com diferentes números de
espiras, enroladas em um núcleo de ferro. (Não existe contato elétrico entre as bobinas e o núcleo.) O
enrolamento primário, com N espiras, está ligado a um gerador de corrente alternada cuja força
p
eletromotriz é dada por
O enrolamento secundário, com N espiras, está ligado a uma resistência de carga R, mas não há corrente
s
no circuito se a chave S estiver aberta (vamos supor, por enquanto, que isso é verdade). Vamos supor
também que, como se trata de um transformador ideal, a resistência dos enrolamentos é desprezível. Nos
transformadores bem projetados, de alta capacidade, a dissipação de energia nos enrolamentos pode ser
menor que 1%; assim, a hipótese é razoável.

Figura 31-18 Um transformador ideal, formado por duas bobinas enroladas em um núcleo de ferro, ligado a uma fonte e uma carga. Um
gerador de corrente alternada produz uma corrente no enrolamento da esquerda (o primário). O enrolamento da direita (o secundário) é
ligado à carga resistiva R quando a chave S é fechada.
Nessas condições, o enrolamento primário (ou, simplesmente, primário) do transformador se
comporta como uma indutância pura, e o circuito primário é semelhante ao da Fig. 31-12. Assim, a
(pequena) corrente do primário, também chamada de corrente de magnetização I , está atrasada de 90o
mag
em relação à tensão V do primário; o fator de potência do primário (= cos ϕ na Eq. 31-76) é zero e
p
nenhuma potência é transferida do gerador para o transformador.
Mesmo assim, a pequena corrente alternada I do primário produz um fluxo magnético alternado Φ
mag B
no núcleo de ferro. A função do núcleo é reforçar o fluxo e transferi-lo, praticamente sem perdas, para o
enrolamento secundário (ou, simplesmente, secundário) do transformador. Como varia com o tempo, Φ
B
induz uma força eletromotriz (= dΦ /dt) em cada espira do primário e do secundário. No primário,
espira B
a tensão V é o produto de pelo número de espiras do primário N , ou seja, V = N .
p espira p p espira p
Analogamente, no secundário, a tensão é V = N . Podemos, portanto, escrever
s espira s
Se N > N , o transformador é chamado de transformador elevador de tensão, já que, nesse caso, a
s p
tensão V no secundário é maior que a tensão V no primário. Quando N < N , o transformador recebe o
s p s p
nome de transformador abaixador de tensão.
Com a chave S aberta, nenhuma energia é transferida do gerador para o resto do circuito. Quando a
chave S é fechada, ligando o secundário à carga R (a carga poderia conter componentes indutivos e
capacitivos, mas vamos supor que é puramente resistiva), várias coisas acontecem:
1. Uma corrente alternada I passa a existir no circuito secundário, e uma potência é
s
dissipada na carga resistiva.
2. A corrente do secundário produz um fluxo magnético alternado no núcleo de ferro; esse fluxo induz
uma força eletromotriz no primário que se opõe à força eletromotriz do gerador.
3. A tensão V do primário não pode mudar em resposta à nova força eletromotriz, já que, de acordo
p
com a regra das malhas, é sempre igual à força eletromotriz do gerador.

4. Para manter a tensão V , o gerador passa a produzir, além de I , uma corrente I no circuito
p mag p
primário; a amplitude e a fase de I são tais que a força eletromotriz induzida por I no primário
p p
cancela exatamente a força eletromotriz induzida no primário por I . Como a constante de fase de I
s p
não é 90o como a constante de fase de I , a corrente I pode transferir energia do gerador para o
mag p
primário.
Transferência de Energia. Nosso interesse é calcular a relação entre I e I ; para isso, em vez de
s p
analisar com detalhes o funcionamento do transformador, vamos simplesmente aplicar a lei de
conservação da energia. A potência elétrica transferida do gerador para o primário é igual a V I . A
p p
potência recebida pelo secundário (por meio do campo magnético que enlaça os dois enrolamentos) é
V I . Como estamos supondo que o transformador é ideal, nenhuma energia é dissipada nos enrolamentos
s s
e, portanto, de acordo com a lei de conservação na energia,
I V = I V .
p p s s
Substituindo V por seu valor, dado pela Eq. 31-79, obtemos
s
De acordo com a Eq. 31-80, a corrente I do secundário pode ser muito diferente da corrente I do
s p
primário, dependendo da relação de espiras N /N .
p s
A corrente I aparece no circuito primário por causa da carga resistiva R do circuito secundário.
p
Para calcular I , fazemos I = V /R na Eq. 31-80 e substituímos V por seu valor, dado pela Eq. 31-79. O
p s s s
resultado é o seguinte:
A Eq. 31-81 é da forma I = V /R , em que a resistência equivalente R é dada por
p p eq eq
A resistência equivalente R é a resistência de carga “do ponto de vista” do gerador; o gerador produz
eq
uma corrente I e uma tensão V como se estivesse ligado a uma resistência R .
p p eq
Casamento de Impedâncias
A Eq. 31-82 sugere outra aplicação para o transformador. Nos circuitos de corrente contínua, para que a
transferência de energia de uma fonte para uma carga seja máxima, a resistência interna da fonte deve ser
igual à resistência da carga. A mesma condição se aplica aos circuitos de corrente alternada, exceto pelo

fato de que, nesse caso, são as impedâncias (e não as resistências) que devem ser iguais. Em muitos
casos, a condição não é satisfeita. Nos aparelhos de som, por exemplo, a saída do amplificador tem uma
alta impedância, e a entrada dos alto-falantes tem uma baixa impedância. Podemos compatibilizar (casar)
as impedâncias de dois dispositivos ligando-os por um transformador com uma relação de espiras
apropriada.
Teste 8
A fonte de alimentação alternada de um circuito tem uma resistência interna menor que a carga resistiva do circuito. Para
aumentar a transferência de energia da fonte para a carga, decidiu-se usar um transformador de casamento de impedâncias. (a) O
valor de N deve ser maior ou menor que o valor de N ? (b) Isso faz do transformador um transformador elevador de tensão ou um
s p
transformador abaixador de tensão?
Exemplo 31.08 Relação de espiras, potência média e correntes de um transformador
Um transformador instalado em um poste funciona com V = 8,5 kV do lado do primário e fornece energia elétrica a várias casas
p
das vizinhanças com V = 120 V; as duas tensões são valores rms. Suponha que o transformador é ideal e a carga é resistiva.
s
(a) Qual é a relação de espiras N /N do transformador?
p s
IDEIA-CHAVE
A relação de espiras N /N está relacionada às tensões (conhecidas) do primário e do secundário pela Eq. 31-79 (V = V N/N ).
p s s p s p
Cálculo: A Eq. 31-79 pode ser escrita na forma
(Observe que o lado direito da Eq. 31-83 é o inverso da relação de espiras.) Invertendo ambos os membros da Eq. 31-83,
temos
(b) A potência média consumida nas casas atendidas pelo transformador é 78 kW. Quais são as correntes no primário e no
secundário do transformador?
IDEIA-CHAVE

Como	a	carga	é	resistiva,	o	fator	de	potência	cos	ϕ	é	unitário	e,	portanto,	a	potência	média	fornecida	e	consumida	é	dada	pela	Eq.
| 31-77	(P 	=	 I	=	IV). |     |     |
| --------------------- | --- | --- |
méd
| Cálculos:	No	circuito	primário,	com	V |     | 	=	8,5	kV,	a	Eq.	31-77	nos	dá |
| ------------------------------------- | --- | ----------------------------- |
p
No	circuito	secundário,	temos
| É	fácil	verificar	que	I	=	I | (N /N),	como	exige	a	Eq.	31-80. |     |
| --------------------------- | ------------------------------- | --- |
s p p s
(c)	Qual	é	a	carga	resistiva	R	do	circuito	secundário?	Qual	é	a	carga	correspondente	R 	do	circuito	primário?
s p
Primeira	abordagem:	Podemos	usar	a	equação	V	=	IR	para	relacionar	a	carga	resistiva	à	tensão	e	à	corrente.	No	caso	do	circuito
secundário,	temos
No	caso	do	circuito	primário,	temos
Segunda	abordagem:	Podemos	usar	o	fato	de	que	R 	é	a	carga	resistiva	“do	ponto	de	vista”	do	gerador,	dada	pela	Eq.	31-82	[R
p eq
| =	(N /N)2R].	Fazendo	R | 	=	R 	e	R	=	R,	obtemos |     |
| ---------------------- | ---------------------- | --- |
| p s                    | eq p                   | s   |
	Revisão	e	Resumo
Transferências	 de	 Energia	 em	 um	 Circuito	 LC 	 Em	 um	 circuito	 LC	 oscilante,	 a	 energia	 é
transferida	periodicamente	do	campo	elétrico	do	capacitor	para	o	campo	magnético	do	indutor,	e	vice-
versa;	os	valores	instantâneos	das	duas	formas	de	energia	são

em que q é a carga instantânea do capacitor e i é a corrente instantânea no indutor. A energia total U (= U
E
+ U ) permanece constante.
B
Oscilações de Carga e de Corrente em um Circuito LC De acordo com a lei de conservação
da energia,
é a equação diferencial das oscilações de um circuito LC (sem resistência). A solução da Eq. 31-11 é
em que Q é a amplitude da carga (carga máxima do capacitor), e a frequência angular ω das oscilações é
dada por
A constante de fase ϕ da Eq. 31-12 é determinada pelas condições iniciais (em t = 0) do sistema.
A corrente i no sistema em um instante qualquer t é dada por
em que ωQ é a amplitude I da corrente.
Oscilações Amortecidas As oscilações de um circuito LC são amortecidas quando um componente
dissipativo R é introduzido no circuito. Nesse caso, temos
A solução da Eq. 31-24 é
em que
Consideramos apenas as situações em que R é pequeno e, portanto, o amortecimento é pequeno; nesse
caso, ω′ ≈ ω.
Correntes Alternadas; Oscilações Forçadas Um circuito RLC série pode sofrer oscilações
forçadas com uma frequência angular de excitação ω se for submetida a uma força eletromotriz da
d
forma

A corrente produzida no circuito pela força eletromotriz é dada por
em que ϕ é a constante de fase da corrente.
Ressonância A amplitude I da corrente em um circuito RLC série excitado por uma força
eletromotriz senoidal é máxima (I = /R) quando a frequência angular de excitação ω é igual à
d
frequência angular natural ω do circuito (ou seja, na ressonância). Nesse caso, X = X , ϕ = 0 e a
C L
corrente está em fase com a força eletromotriz.
Componentes Isolados A diferença de potencial alternada entre os terminais de um resistor tem
uma amplitude V = IR; a corrente está em fase com a diferença de potencial.
R
No caso de um capacitor, V = IX , em que X = 1/ω C é a reatância capacitiva; a corrente está
C C C d
adiantada de 90o em relação à diferença de potencial (ϕ = −90o = −π/2 rad).
No caso de um indutor, V = IX , em que X = ω L é a reatância indutiva; a corrente está atrasada de 90o
L L L d
em relação à diferença de potencial (ϕ = 90o = π/2 rad).
Circuitos RLC Série No caso de um circuito RLC série com uma força eletromotriz dada pela Eq.
31-28 e uma corrente dada pela Eq. 31-29,
e
Definindo a impedância Z do circuito como
podemos escrever a Eq. 31-60 como I = /Z.
Potência Em um circuito RLC série, a potência média P fornecida pelo gerador é igual à potência
méd
média dissipada no resistor:
Aqui, rms significa valor médio quadrático. Os valores médios quadráticos estão relacionados aos
valores máximos pelas equações I = . O termo cos ϕ é chamado de fator
rms
de potência do circuito.
Transformadores Um transformador (considerado ideal) é formado por um núcleo de ferro que

contém dois enrolamentos: o enrolamento primário, com N espiras, e o enrolamento secundário, com N
p s
espiras. Se o enrolamento primário é ligado a um gerador de corrente alternada, as tensões no primário e
no secundário estão relacionadas pela equação
As correntes nos enrolamentos estão relacionadas pela equação
e a resistência equivalente do circuito secundário, do ponto de vista do gerador, é dada por
em que R é a carga resistiva do circuito secundário. A razão N /N é chamada de relação de espiras.
p s
Perguntas
1 A Fig. 31-19 mostra três circuitos LC oscilantes com indutores e capacitores iguais. Coloque os
circuitos na ordem decrescente do tempo necessário para que os capacitores se descarreguem totalmente.
Figura 31-19 Pergunta 1.
2 A Fig. 31-20 mostra os gráficos da tensão v do capacitor em dois circuitos LC que contêm
C
capacitâncias iguais e têm a mesma carga máxima Q. (a) A indutância L do circuito 1 é maior, menor ou
igual à do circuito 2? (b) A corrente I no circuito 1 é maior, menor ou igual à corrente no circuito 2?
Figura 31-20 Pergunta 2.
3 Um capacitor carregado e um indutor são ligados para formar um circuito fechado no instante t = 0.
Em termos do período T das oscilações resultantes, determine o tempo necessário para que as seguintes

grandezas passem por um máximo pela primeira vez: (a) U , (b) o fluxo magnético no indutor, (c) di/dt e
B
(d) a força eletromotriz do indutor.
4 Quais valores da constante de fase ϕ da Eq. 31-12 permitem que as situações (a), (c), (e) e (g) da Fig.
31-1 ocorram no instante t = 0?
5 A curva a da Fig. 31-21 mostra a impedância Z de um circuito RC excitado em função da frequência
angular de excitação ω . As outras duas curvas são semelhantes, mas foram traçadas para valores
d
diferentes da resistência R e da capacitância C. Coloque as três curvas na ordem decrescente do valor
correspondente de R.
Figura 31-21 Pergunta 5.
6 As cargas dos capacitores de três circuitos LC oscilantes variam segundo as equações (1) q = 2 cos
4t, (2) q = 4 cos t, (3) q = cos 4t (com q em coulombs e t em segundos). Coloque os circuitos na ordem
decrescente (a) da amplitude da corrente e (b) do período das oscilações.
Figura 31-22 Pergunta 7.
7 Uma fonte de força eletromotriz alternada é conectada sucessivamente a um resistor, um capacitor e
um indutor. Depois que a fonte é conectada, faz-se variar a frequência de excitação f , e a amplitude I da
d
corrente resultante é medida e plotada. Estabeleça a correspondência entre as curvas da Fig. 31-22 e os
dispositivos.
8 Os valores da constante de fase ϕ para quatro circuitos RLC série com excitação senoidal são (1)
−15o, (2) 35o, (3) π/3 rad e (4) −π/6 rad. (a) Em que circuito(s) a carga é mais capacitiva que indutiva?
(b) Em que circuito(s) a corrente está atrasada em relação à força eletromotriz?

Figura 31-23 Pergunta 9.
9 A Fig. 31-23 mostra a corrente i e a força eletromotriz de excitação de um circuito RLC série. (a) A
constante de fase é positiva ou negativa? (b) Para aumentar a potência transferida para a carga resistiva,
é preciso aumentar ou diminuir o valor de L? (c) A outra possibilidade é aumentar ou diminuir o valor de
C?
10 A Fig. 31-24 mostra três situações como as da Fig. 31-15. (a) A frequência angular de excitação é
maior, menor ou igual à frequência angular de ressonância do circuito na situação 1? (b) Responda à
mesma pergunta para a situação 2. (c) Responda à mesma pergunta para a situação 3.
Figura 31-24 Pergunta 10.
11 A Fig. 31-25 mostra a corrente i e a força eletromotriz aplicada para um circuito RLC série. (a) A
curva da corrente é deslocada para a esquerda ou para a direita em relação à curva da força eletromotriz
e a amplitude da curva é maior ou menor se o valor de L aumenta ligeiramente? (b) Responda às mesmas
perguntas para o valor de C. (c) Responda às mesmas perguntas para o valor de ω .
d
12 A Fig. 31-25 mostra a corrente i e a força eletromotriz em um circuito RLC série. (a) A corrente
está adiantada ou atrasada em relação à força eletromotriz? (b) A carga do circuito é mais capacitiva que
indutiva ou mais indutiva que capacitiva? (c) A frequência angular ω da força eletromotriz é maior ou
d
menor que a frequência angular natural ω?
Figura 31-25 Perguntas 11 e 12.
13 O diagrama fasorial da Fig. 31-26 corresponde a uma fonte de força eletromotriz alternada ligada a
um resistor, capacitor ou indutor? (b) Se a velocidade angular dos fasores aumentar, o comprimento do
fasor que representa a corrente deve aumentar ou diminuir para manter a escala do desenho?

Figura 31-26 Pergunta 13.
Problemas
. - ... O número de pontos indica o grau de dificuldade do problema.
Informações adicionais disponíveis em O Circo Voador da Física de Jearl Walker,
LTC, Rio de Janeiro, 2008.
Módulo 31-1 Oscilações em um Circuito LC
·1 Um circuito LC oscilante é formado por um indutor de 75,0 mH e um capacitor de 3,60 μF. Se a carga
máxima do capacitor é 2,90 μC, determine (a) a energia total presente no circuito e (b) a corrente
máxima.
·2 A frequência de oscilação de um circuito LC é 200 kHz. No instante t = 0, a placa A do capacitor está
com a carga positiva máxima. Determine em que instante t > 0 (a) a placa estará novamente, pela
primeira vez, com a carga positiva máxima, (b) a outra placa do capacitor estará pela primeira vez com a
carga positiva máxima e (c) o indutor estará pela primeira vez com o campo magnético máximo.
·3 Em um circuito LC oscilante, a energia total é convertida de energia elétrica no capacitor em energia
magnética no indutor em 1,50 μs. Determine (a) o período das oscilações e (b) a frequência das
oscilações. (c) Se a energia magnética é máxima em um dado instante, quanto tempo é necessário para
que ela seja máxima novamente?
·4 Qual é a capacitância de um circuito LC oscilante se a carga máxima do capacitor é 1,60 μC e a
energia total é 140 μJ?
·5 Em um circuito LC oscilante, L = 1,10 mH e C = 4,00 μF. A carga máxima do capacitor é 3,00 μC.
Determine a corrente máxima.
·6 Um corpo de 0,50 kg oscila em movimento harmônico simples, preso a uma mola que, quando
alongada de 2,00 mm em relação à posição de equilíbrio, possui uma força restauradora de 8,0 N.
Determine (a) a frequência angular de oscilação, (b) o período de oscilação e (c) a capacitância de um
circuito LC com o mesmo período, se L = 5,0 H.
·7 A energia de um circuito LC oscilante que contém um indutor de 1,25 H é 5,70 μJ. A carga máxima
do capacitor é 175 μC. Para um sistema mecânico com o mesmo período, determine (a) a massa, (b) a

constante da mola, (c) o deslocamento máximo e (d) a velocidade escalar máxima.
·8 Um circuito com uma única malha é formado por indutores (L , L , ...), capacitores (C , C , ...) e
1 2 1 2
resistores (R , R , ...), como na Fig. 31-27a. Mostre que, qualquer que seja a sequência de componentes
1 2
no circuito, o comportamento do circuito é igual ao do circuito LC simples da Fig. 31-27b. (Sugestão:
Considere a regra das malhas e veja o Problema 47 do Capítulo 30.)
Figura 31-27 Problema 8.
·9 Em um circuito LC oscilante com L = 50 mH e C = 4,0 μF, a corrente está inicialmente no máximo.
Quanto tempo é necessário para que o capacitor se carregue totalmente pela primeira vez?
·10 Osciladores LC têm sido usados em circuitos ligados a alto-falantes para criar alguns dos sons da
música eletrônica. Que indutância deve ser usada com um capacitor de 6,7 μF para produzir uma
frequência de 10 kHz, que fica aproximadamente na metade da faixa de frequências audíveis?
··11 Um capacitor variável, de 10 a 365 pF, e um indutor formam um circuito LC de frequência variável
usado para sintonizar um receptor de rádio. (a) Qual é a razão entre a maior frequência e a menor
frequência natural que pode ser obtida usando este capacitor? Se o circuito deve ser usado para obter
frequências entre 0,54 MHz e 1,60 MHz, a razão calculada no item (a) é grande demais. A faixa de
frequências pode ser modificada ligando um capacitor em paralelo com o capacitor variável. (b) Qual
deve ser o valor da capacitância adicional para que a faixa de frequências seja a faixa desejada? (c)
Qual deve ser a indutância do indutor do circuito?
··12 Em um circuito LC oscilante, quando uma energia igual a 75% da energia total está armazenada no
campo magnético do indutor, determine (a) a fração da carga máxima que está armazenada no capacitor e
(b) a fração da corrente máxima que está atravessando o indutor.
··13 Em um circuito LC oscilante, L = 3,00 mH e C = 2,70 μH. No instante t = 0, a carga do capacitor é
zero e a corrente é 2,00 A. (a) Qual é a carga máxima do capacitor? (b) Em que instante de tempo t > 0 a
taxa com a qual a energia é armazenada no capacitor é máxima pela primeira vez? (c) Qual é o valor da
taxa máxima?
··14 Para montar um circuito LC oscilante, você dispõe de um indutor de 10 mH, um capacitor de 5,0
μF e um capacitor de 2,0 μF. Determine (a) a menor frequência, (b) a segunda menor frequência, (c) a
segunda maior frequência e (d) a maior frequência de oscilação que pode ser conseguida combinando
esses componentes.
··15 Um circuito LC oscilante formado por um capacitor de 1,0 nF e um indutor de 3,0 mH tem uma
tensão máxima de 3,0 V. Determine (a) a carga máxima do capacitor, (b) a corrente máxima do circuito e

(c) a energia máxima armazenada no campo magnético do indutor.
··16 Um indutor é ligado a um capacitor cuja capacitância pode ser ajustada por meio de um botão.
Queremos que a frequência desse circuito LC varie linearmente com o ângulo de rotação do botão, de 2 ×
105 Hz até 4 × 105 Hz, quando o botão gira de 180o. Se L = 1,0 mH, plote a capacitância desejada C em
função do ângulo de rotação do botão.
··17 Na Fig. 31-28, R = 14,0 Ω, C = 6,20 μF, L = 54,0 mH e a fonte ideal tem uma força eletromotriz
= 34,0 V. A chave é mantida na posição a por um longo tempo e depois é colocada na posição b.
Determine (a) a frequência e (b) a amplitude das oscilações resultantes.
Figura 31-28 Problema 17.
··18 Em um circuito LC oscilante, a amplitude da corrente é 7,50 mA, a amplitude da tensão é 250 mV e
a capacitância é 220 nF. Determine (a) o período de oscilação, (b) a energia máxima armazenada no
capacitor, (c) a energia máxima armazenada no indutor, (d) a taxa máxima de variação da corrente e (e) a
taxa máxima de aumento da energia do indutor.
··19 Use a regra das malhas para obter a equação diferencial de um circuito LC (Eq. 31-11).
··20 Em um circuito LC oscilante no qual C = 4,00 μF, a diferença de potencial máxima entre os
terminais do capacitor durante as oscilações é 1,50 V e a corrente máxima no indutor é 50,0 mA.
Determine (a) a indutância L e (b) a frequência das oscilações. (c) Qual é o tempo necessário para que a
carga do capacitor aumente de zero até o valor máximo?
··21 Em um circuito LC oscilante com C = 64,0 μF, a corrente é dada por i = (1,60) sen(2500t + 0,680),
em que t está em segundos, i está em ampères e a constante de fase está em radianos. (a) Quanto tempo
após o instante t = 0 a corrente atinge o valor máximo? (b) Qual é o valor da indutância L? (c) Qual é a
energia total?
··22 Um circuito série formado por uma indutância L e uma capacitância C oscila com uma frequência
1 1
angular ω. Um segundo circuito série, contendo uma indutância L e uma capacitância C , oscila com a
2 2
mesma frequência angular. Qual é, em termos de ω, a frequência angular de oscilação de um circuito série
formado pelos quatro componentes? Despreze a resistência do circuito. (Sugestão: Use as expressões da
capacitância equivalente e da indutância equivalente; veja o Módulo 25-4 e o Problema 47 do Capítulo
30.)
··23 Em um circuito LC oscilante, L = 25,0 mH e C = 7,80 μF. No instante t = 0, a corrente é 9,20 mA, a

carga do capacitor é 3,80 μC e o capacitor está sendo carregado. Determine (a) a energia total do
circuito, (b) a carga máxima do capacitor e (c) a corrente máxima do circuito. (d) Se a carga do capacitor
é dada por q = Q cos(ωt + ϕ), qual é o ângulo de fase ϕ? Suponha que os dados são os mesmos, exceto
pelo fato de que o capacitor está sendo descarregado no instante t = 0. Qual é o valor de ϕ nesse caso?
Módulo 31-2 Oscilações Amortecidas em um Circuito RLC
··24 Um circuito de uma única malha é formado por um resistor de 7,20 Ω, um indutor de 12,0 H e um
capacitor de 3,20 μF. Inicialmente, o capacitor possui uma carga de 6,20 μC e a corrente é zero. Calcule
a carga do capacitor após N ciclos completos (a) para N = 5, (b) para N = 10 e (c) para N = 100.
··25 Que resistência R deve ser ligada em série com uma indutância L = 220 mH e uma capacitância C
= 12,0 μF para que a carga máxima do capacitor caia para 99,0% do valor inicial após 50,0 ciclos?
(Suponha que ωʹ ≈ ω.)
··26 Em um circuito RLC série oscilante, determine o tempo necessário para que a energia máxima
presente no capacitor durante uma oscilação diminua para metade do valor inicial. Suponha que q = Q em
t = 0.
···27 Em um circuito RLC oscilante, mostre que ΔU/U, a fração da energia perdida por ciclo de
oscilação, é dada com boa aproximação por 2πR/ωL. A grandeza ωL/R é chamada de Q do circuito (Q
significa qualidade). Um circuito de alto Q possui uma baixa resistência e uma baixa perda de energia (=
2π/Q) por ciclo.
Módulo 31-3 Oscilações Forçadas em Três Circuitos Simples
·28 Um capacitor de 1,50 μF é ligado, como na Fig. 31-10, a um gerador de corrente alternada com
= 30,0 V. Determine a amplitude da corrente alternada resultante se a frequência da força eletromotriz for
(a) 1,00 kHz e (b) 8,00 kHz.
·29 Um indutor de 50,0 mH é ligado, como na Fig. 31-12, a um gerador de corrente alternada com =
30,0 V. Determine a amplitude da corrente alternada resultante se a frequência da força eletromotriz for
(a) 1,00 kHz e (b) 8,00 kHz.
·30 Um resistor de 50,0 Ω é ligado, como na Fig. 31-8, a um gerador de corrente alternada com =
30,0 V. Determine a amplitude da corrente alternada resultante se a frequência da força eletromotriz for
(a) 1,00 kHz e (b) 8,00 kHz.
·31 (a) Para que frequência um indutor de 6,0 mH e um capacitor de 10 μF têm a mesma reatância? (b)
Qual é o valor da reatância? (c) Mostre que a frequência é a frequência natural de um circuito oscilador
com os mesmos valores de L e C.
··32 A força eletromotriz de um gerador de corrente alternada é dada por = sen ω t, com = 25,0
d
V e ω = 377 rad/s. O gerador é ligado a um indutor de 12,7 H. (a) Qual é o valor máximo da corrente?
d
(b) Qual é a força eletromotriz do gerador no instante em que a corrente é máxima? (c) Qual é a corrente

no instante em que a força eletromotriz do gerador é −12,5 V e está aumentando em valor absoluto?
··33 Um gerador de corrente alternada tem uma força eletromotriz = sen(ω t − π/4), em que = 30,0
d
V e ω = 350 rad/s. A corrente produzida no circuito ao qual o gerador está ligado é i(t) = I sen(ω t −
d d
3π/4), em que I = 620 mA. Em que instante após t = 0 (a) a força eletromotriz do gerador atinge pela
primeira vez o valor máximo e (b) a corrente atinge pela primeira vez o valor máximo? (c) O circuito
contém um único componente além do gerador. Trata-se de um capacitor, de um indutor ou de um
resistor? Justifique sua resposta. (d) Qual é o valor da capacitância, da indutância ou da resistência desse
componente?
··34 Um gerador de corrente alternada com uma força eletromotriz = sen ω t, em que = 25,0 V e
d
ω = 377 rad/s, é ligado a um capacitor de 4,15 μF. (a) Qual é o valor máximo da corrente? (b) Qual é a
d
força eletromotriz do gerador no instante em que a corrente é máxima? (c) Qual é a corrente quando a
força eletromotriz é −12,5 e está aumentando em valor absoluto?
Módulo 31-4 O Circuito RLC Série
·35 Uma bobina com 88 mH de indutância e resistência desconhecida e um capacitor de 0,94 μF são
ligados em série com um gerador cuja frequência é 930 Hz. Se a diferença de fase entre a tensão aplicada
pelo gerador e a corrente no circuito é 75o, qual é a resistência da bobina?
·36 Uma fonte alternada, de frequência variável, um capacitor de capacitância C e um resistor de
resistência R são ligados em série. A Fig. 31-29 mostra a impedância Z do circuito em função da
frequência angular de excitação ω . A curva possui uma assíntota de 500 Ω e a escala do eixo horizontal
d
é definida por ω = 300 rad/s. A figura mostra também a reatância X do capacitor em função de ω .
ds C d
Determine o valor (a) de R e (b) de C.
Figura 31-29 Problema 36.
·37 Um motor elétrico possui uma resistência efetiva de 32,0 Ω e uma reatância indutiva de 45,0 Ω
quando está em carga. A amplitude da tensão da fonte alternada é 420 V. Calcule a amplitude da corrente.
·38 A Fig. 31-30 mostra a amplitude I da corrente em função da frequência angular de excitação ω de
d
um circuito RLC. A escala do eixo vertical é definida por I = 4,00 A. A indutância é 200 μH e a
s
amplitude da força eletromotriz é 8,0 V. Determine o valor (a) de C e (b) de R.

Figura 31-30 Problema 38.
·39 Remova o indutor do circuito da Fig. 31-7 e faça R = 200 Ω, C = 15,0 μF, f = 60,0 Hz e = 36,0
d
V. Determine o valor (a) de Z, (b) de ϕ e (c) de I. (d) Desenhe um diagrama fasorial.
·40 Uma fonte alternada com uma força eletromotriz de 6,00 V e com um ângulo de fase de 30,0o é
ligada a um circuito RLC série. Quando a diferença de potencial entre os terminais do capacitor atinge o
valor máximo positivo de 5,00 V, qual é a diferença de potencial entre os terminais do indutor (incluindo
o sinal)?
·41 Na Fig. 31-7, faça R = 200 Ω, C = 70,0 μF, L = 230 mH, f = 60,0 Hz e = 36,0 V. Determine o
d
valor (a) de Z, (b) de ϕ e (c) de I. (d) Desenhe um diagrama fasorial.
·42 Uma fonte de corrente alternada, de frequência variável, um indutor de indutância L e um resistor de
resistência R são ligados em série. A Fig. 31-31 mostra a impedância Z do circuito em função da
frequência de excitação ω , com a escala do eixo horizontal definida por ω = 1600 rad/s. A figura
d ds
mostra também a reatância X do indutor em função de ω . Determine o valor (a) de R e (b) de L.
L d
Figura 31-31 Problema 42.
·43 Remova o capacitor do circuito da Fig. 31-7 e faça R = 200 Ω, L = 230 mH, f = 60,0 Hz e =
d
36,0 V. Determine o valor (a) de Z, (b) de ϕ e (c) de I. (d) Desenhe um diagrama fasorial.
··44 Um gerador de corrente alternada com = 220 V e f = 400 Hz produz oscilações em um circuito
d
RLC série com R = 220 Ω, L = 150 mH e C = 24,0 μF. Determine (a) a reatância capacitiva X , (b) a
C
impedância Z e (c) a amplitude I da corrente. Um segundo capacitor com a mesma capacitância é ligado
em série com os outros componentes. Determine se o valor de (d) X , (e) Z e (f) I aumenta, diminui ou
C
permanece o mesmo.
··45 (a) Em um circuito RLC, a amplitude da tensão do indutor pode ser maior que a força eletromotriz
do gerador? (b) Considere um circuito RLC com = 10 V, R = 10 Ω, L = 1,0 H e C = 1,0 μF. Determine

a amplitude da tensão do indutor na frequência de ressonância.
··46 Uma fonte alternada de frequência variável f é ligada em série com um resistor de 50,0 Ω e um
d
capacitor de 20,0 μF. A amplitude da força eletromotriz é 12,0 V. (a) Desenhe um diagrama fasorial para
o fasor V (tensão do resistor) e para o fasor V (tensão do capacitor). (b) Para que frequência de
R C
excitação f os dois fasores têm o mesmo comprimento? Para essa frequência, determine (c) o ângulo de
d
fase em graus, (d) a velocidade angular de rotação dos fasores e (e) a amplitude da corrente.
··47 Um circuito RLC como o da Fig. 31-7 tem R = 5,00 Ω, C = 20,0 μF, L = 1,00 H e = 30,0 V. (a)
Para que frequência angular ω a amplitude da corrente é máxima, como nas curvas de ressonância da
d
Fig. 31-16? (b) Qual é o valor máximo? (c) Para que frequência angular ω < ω a amplitude da corrente
d1 d
tem metade do valor máximo? (d) Para que frequência angular ω > ω a amplitude da corrente tem
d2 d
metade do valor máximo? (e) Qual é o valor de (ω − ω )/ω, a largura de linha relativa a meia altura da
d2 d1
curva de ressonância desse circuito?
··48 A Fig. 31-32 mostra um circuito RLC, alimentado por um gerador, que possui dois capacitores
iguais e duas chaves. A amplitude da força eletromotriz é 12,0 V e a frequência do gerador é 60,0 Hz.
Com as duas chaves abertas, a corrente está adiantada 30,9o em relação à tensão. Com a chave S fechada
1
e a chave S aberta, a corrente está adiantada 15,0o em relação à tensão. Com as duas chaves fechadas, a
2
amplitude da corrente é 447 mA. Determine o valor (a) de R, (b) de C e (c) de L.
Figura 31-32 Problema 48.
··49 Na Fig. 31-33, um gerador de frequência ajustável é ligado a um circuito formado pela resistência
R = 100 Ω, as indutâncias L = 1,70 mH e L = 2,30 mH e as capacitâncias C = 4,00 μF, C = 2,50 μF e
1 2 1 2
C = 3,50 μF. (a) Qual é a frequência de ressonância do circuito? (Sugestão: Veja o Problema 47 do
3
Capítulo 30.) Determine o que acontece com a frequência de ressonância (b) quando R aumenta, (c)
quando L aumenta e (d) quando C é removido do circuito.
1 3
Figura 31-33 Problema 49.
··50 Uma fonte de força eletromotriz alternada, de frequência variável f , é ligada em série com um
d
resistor de 80,0 Ω e um indutor de 40,0 mH. A amplitude da força eletromotriz é 6,00 V. (a) Desenhe um

diagrama fasorial para o fasor V (a tensão no resistor) e para o fasor V (a tensão no indutor). (b) Para
R L
que frequência de excitação f os dois fasores têm o mesmo comprimento? Para essa frequência de
d
excitação, determine (c) o ângulo de fase em graus, (d) a velocidade angular de rotação dos fasores e (e)
a amplitude da corrente.
··51 A largura de linha relativa a meia altura Δω /ω de uma curva de ressonância, como as que
d
aparecem na Fig. 31-16, é a largura de linha na metade do valor máximo de I dividida pela frequência
angular de ressonância. Mostre que Δω /ω = R(3C/L)1/2, em que ω é a frequência angular de ressonância.
d
Observe que a razão Δω /ω aumenta quando R aumenta, como mostra a Fig. 31-16.
d
·52 Um voltímetro de CA com alta impedância é ligado sucessivamente aos terminais de um indutor,
aos terminais de um capacitor e aos terminais de um resistor em um circuito série ao qual é aplicada uma
força eletromotriz alternada de 100 V (rms); nos três casos, o instrumento fornece a mesma leitura em
volts. Qual é essa leitura?
Módulo 31-5 Potência em Circuitos de Corrente Alternada
·53 Um aparelho de ar condicionado ligado a uma tomada de 120 V rms é equivalente a uma resistência
de 12,0 Ω e uma reatância indutiva de 1,30 Ω ligadas em série. Determine (a) a impedância do aparelho
e (b) a potência consumida pelo aparelho.
·54 Qual é o valor máximo de uma tensão alternada cujo valor rms é 100 V?
·55 Que corrente contínua produz a mesma energia térmica, em um resistor, que uma corrente alternada
com um valor máximo de 2,60 A?
··56 Um dimmer típico, como os que são usados para regular a luminosidade das lâmpadas do palco
nos teatros, é composto por um indutor variável L (cuja indutância pode ser ajustada entre zero e L )
máx
ligado em série com uma lâmpada B, como mostra a Fig. 31-34. O circuito é alimentado com uma tensão
de 120 V rms, 60 Hz; a lâmpada é de 120 V, 1000 W. (a) Qual deve ser o valor de L para que a
máx
potência dissipada na lâmpada possa variar entre 200 e 1000 W? Suponha que a resistência da lâmpada é
independente da temperatura. (b) É possível usar um resistor variável (ajustável entre zero e R ) em vez
máx
de um indutor? (c) Nesse caso, qual deve ser o valor de R ? (d) Por que não se usa esse método?
máx
Figura 31-34 Problema 56.
··57 Em um circuito RLC como o da Fig. 31-7, suponha que R = 5,00 Ω, L = 60,0 mH, f = 60,0 Hz e
d
= 30,0 V. (a) Para qual valor de capacitância a potência dissipada na resistência é máxima? (b) Para qual
valor de capacitância a potência dissipada na resistência é mínima? Determine (c) a dissipação máxima,
(d) o ângulo de fase correspondente e (e) o fator de potência correspondente. Determine também (f) a

dissipação mínima, (g) o ângulo de fase correspondente e (h) o fator de potência correspondente.
··58 Mostre que a potência dissipada na resistência R da Fig. 31-35 é máxima quando R é igual à
resistência r do gerador de corrente alternada. (Na discussão do texto, supusemos tacitamente que r = 0.)
Figura 31-35 Problemas 58 e 66.
··59 Na Fig. 31-7, R = 15,0 Ω, C = 4,70 μF e L = 25,0 mH. O gerador produz uma força eletromotriz
com uma tensão rms de 75,0 V e uma frequência de 550 Hz. (a) Qual é a corrente rms? Determine a
tensão rms (b) em R, (c) em C, (d) em L, (e) em C e L juntos e (f) em R, C e L juntos. Determine a
potência média dissipada (g) em R, (h) em C e (i) em L.
··60 Em um circuito RLC série oscilante, R = 16,0 Ω, C = 31,2 μF, L = 9,20 mH e = sen ω t com
d
= 45,0 V e ω = 3000 rad/s. No instante t = 0,442 ms, determine (a) a taxa P com a qual a energia está
d g
sendo fornecida pelo gerador; (b) a taxa P com a qual a energia do capacitor está variando, (c) a taxa P
C L
com a qual a energia do indutor está variando e (d) a taxa P com a qual a energia está sendo dissipada
R
no resistor. (e) A soma de P , P e P é maior, menor ou igual a P ?
C L R g
··61 A Fig. 31-36 mostra um gerador de CA ligado aos terminais de uma “caixa-preta”. A caixa contém
um circuito RLC, possivelmente com mais de uma malha, cujos componentes e ligações são
desconhecidos. Medidas realizadas do lado de fora da caixa revelam que
(a) Qual é o fator de potência? (b) A corrente está adiantada ou atrasada em relação à força eletromotriz?
(c) O circuito no interior da caixa é mais indutivo ou mais capacitivo? (d) O circuito no interior da caixa
está sendo excitado na frequência de ressonância? (e) Deve haver um capacitor no interior da caixa? (f)
Deve haver um indutor no interior da caixa? (g) Deve haver um resistor no interior da caixa? (h) Qual é a
potência fornecida à caixa pelo gerador? (i) Por que não é preciso conhecer o valor de ω para responder
d
a essas perguntas?
Figura 31-36 Problema 61.

Módulo 31-6 Transformadores
·62 Um gerador fornece 100 V ao enrolamento primário de um transformador, que possui 50 espiras. Se
o enrolamento secundário possui 500 espiras, qual é a tensão no secundário?
·63 Um transformador possui 500 espiras no primário e 10 espiras no secundário. (a) Se V é 120 V
p
(rms), quanto é V , com o secundário em circuito aberto? Se o secundário está ligado a uma carga
s
resistiva de 15 Ω, determine (b) a corrente no primário e (c) a corrente no secundário.
·64 A Fig. 31-37 mostra um autotransformador, um componente no qual uma bobina com três terminais
é enrolada em um núcleo de ferro. Entre os terminais T e T existem 200 espiras, e entre os terminais T
1 2 2
e T existem 800 espiras. Qualquer par de terminais pode ser usado como os terminais do primário, e
3
qualquer par de terminais pode ser usado como os terminais do secundário. Para as escolhas que
resultam em um transformador elevador de tensão, determine (a) o menor valor da razão V /V , (b) o
s p
segundo menor valor da razão V /V e (c) o maior valor da razão V /V . Para as escolhas que resultam em
s p s p
um transformador abaixador de tensão, determine (d) o menor valor da razão V /V , (e) o segundo menor
s p
valor da razão V /V e (f) o maior valor da razão V /V .
s p s p
Figura 31-37 Problema 64.
··65 Um gerador de CA alimenta uma carga resistiva em uma fábrica distante por meio de uma linha de
transmissão de dois cabos. Na fábrica, um transformador abaixador de tensão reduz a tensão do valor de
transmissão V (rms) para um valor muito menor que é mais seguro e conveniente para ser usado na
t
fábrica. A resistência da linha de transmissão é 0,30 Ω/cabo e a potência do gerador é 250 kW. Se V =
t
80 kV, determine (a) a queda de tensão ΔV na linha de transmissão e (b) a potência P dissipada na linha.
d
Se V = 8,0 kV, determine o valor (c) de ΔV e (d) de P . Se V = 0,80 kV, determine o valor (e) de ΔV e (f)
t d t
de P .
d
Problemas Adicionais
66 Na Fig. 31-35, suponha que o retângulo da esquerda representa a saída (de alta impedância) de um
amplificador de áudio, com r = 1000 Ω. Suponha que R = 10 Ω representa a bobina (de baixa
impedância) de um alto-falante. Para que a transferência de energia para a carga R seja máxima, devemos
ter R = r, o que, nesse caso, não é verdade. Entretanto, os transformadores podem ser usados para
“transformar” resistências, fazendo com que estas se comportem eletricamente como se fossem maiores

ou menores do que realmente são. (a) Modifique o circuito da Fig. 31-35 de modo a incluir um
transformador entre o amplificador e o alto-falante para casar as impedâncias. (b) Qual deve ser a
relação de espiras do transformador?
67 Um gerador de corrente alternada produz uma força eletromotriz = sen(ω t − π/4), em que =
d
30,0 V e ω = 350 rad/s. A corrente no circuito ligado ao gerador é dada por i(t) = I sen(ω t + π/4), em
d d
que I = 620 mA. (a) Em que instante após t = 0 a força eletromotriz atinge o valor máximo pela primeira
vez? (b) Em que instante após t = 0 a corrente atinge o valor máximo pela primeira vez? (c) O circuito
contém um único componente além do gerador. Trata-se de um capacitor, de um indutor ou de um
resistor? Justifique sua resposta. (d) Qual é o valor do componente?
68 Um circuito RLC série é excitado por um gerador com uma frequência de 2000 Hz e uma amplitude
de 170 V. A indutância é 60,0 mH, a capacitância é 0,400 μF e a resistência é 200 Ω. (a) Qual é a
constante de fase em radianos? (b) Qual é a amplitude da corrente?
69 Um gerador com uma frequência de 3000 Hz aplica uma força eletromotriz de 120 V de amplitude a
um circuito RLC série. A resistência do circuito é 40,0 Ω, a capacitância é 1,60 μF e a indutância é 850
μH. Determine (a) a constante de fase em radianos e (b) a amplitude da corrente. (c) O circuito é mais
capacitivo, mais indutivo ou está em ressonância?
70 Um indutor de 45,0 mH possui uma reatância de 1,30 kΩ. (a) Qual é a frequência de operação do
circuito? (b) Qual é a capacitância de um capacitor com a mesma reatância na mesma frequência? Se a
frequência for multiplicada por dois, qual será a nova reatância (c) do indutor e (d) do capacitor?
71 Um circuito RLC é excitado por um gerador com uma força eletromotriz com 80,0 V de amplitude e
uma corrente com 1,25 A de amplitude. A corrente está adiantada de 0,650 rad em relação à tensão.
Determine (a) a impedância e (b) a resistência do circuito. (c) O circuito é mais indutivo, mais
capacitivo ou está em ressonância?
72 Um circuito RLC série é alimentado de tal forma que a tensão máxima no indutor é 1,50 vez a tensão
máxima no capacitor e 2,00 vezes a tensão máxima no resistor. (a) Qual é o ϕ do circuito? (b) O circuito
é mais indutivo, mais capacitivo ou está em ressonância? A resistência é 49,9 Ω e a amplitude da
corrente é 200 mA. (c) Qual é a amplitude da força eletromotriz de excitação?
73 Um capacitor de 158 μF e um indutor formam um circuito LC que oscila com uma frequência de 8,15
kHz e uma amplitude de corrente de 4,21 mA. Determine (a) a impedância, (b) a energia total do circuito
e (c) a carga máxima do capacitor.
74 Um circuito LC oscilante tem uma indutância de 3,00 mH e uma capacitância de 10,0 μF. Determine
(a) a frequência angular e (b) o período de oscilação. (c) No instante t = 0, o capacitor é carregado com
200 μC e a corrente é zero. Faça um esboço da carga do capacitor em função do tempo.
75 Em um circuito RLC série, a força eletromotriz máxima do gerador é 125 V e a corrente máxima é
3,20 A. Se a corrente está adiantada de 0,982 rad em relação à força eletromotriz do gerador, determine

(a) a impedância e (b) a resistência do circuito. (c) O circuito é mais capacitivo ou mais indutivo?
76 Um capacitor de 1,50 μF possui uma reatância capacitiva de 12,0 Ω. (a) Qual é a frequência de
operação do circuito? (b) Qual será a reatância capacitiva do capacitor se a frequência for multiplicada
por dois?
Figura 31-38 Problema 77.
77 Na Fig. 31-38, um gerador trifásico G produz energia elétrica, que é transmitida por três fios. Os
potenciais dos três fios (em relação a uma referência comum) são V = A sen ω t para o fio 1, V = A
1 d 2
sen(ω t − 120o) para o fio 2, e V = A sen(ω t − 240o) para o fio 3. Alguns equipamentos industriais
d 3 d
pesados (motores, por exemplo) possuem três terminais e são projetados para serem ligados diretamente
aos três fios. Para usar um dispositivo mais convencional de dois terminais (uma lâmpada, por exemplo),
basta ligar o dispositivo a dois dos três fios. Mostre que a diferença de potencial entre dois fios
quaisquer (a) oscila senoidalmente com frequência angular ω e (b) tem uma amplitude A .
d
78 Um motor elétrico ligado a uma tomada de 120 V, 60 Hz desenvolve uma potência mecânica de
0,100 hp (1 hp = 746 W). (a) Se o motor consome uma corrente rms de 0,650 A, qual é a resistência
efetiva do motor do ponto de vista da transferência de energia? (b) A resistência efetiva é igual à
resistência dos enrolamentos do motor, medida com um ohmímetro com o motor desligado da tomada?
79 (a) Em um circuito LC oscilante, qual é a carga, em termos da carga máxima Q do capacitor, quando
a energia do campo elétrico é 50,0% da energia do campo magnético? (b) Que fração de período deve
transcorrer após o instante em que o capacitor está totalmente carregado para que essa situação aconteça?
80 Um circuito RLC série é excitado por uma fonte alternada cuja frequência é 400 Hz e cuja força
eletromotriz tem uma amplitude de 90,0 V. A resistência do circuito é 20,0 Ω, a capacitância é 12,1 μF e
a indutância é 24,2 mH. Determine a diferença de potencial rms (a) no resistor, (b) no capacitor e (c) no
indutor. (d) Qual é a potência média dissipada no circuito?
81 Em um circuito RLC série excitado com uma frequência de 60,0 Hz, a tensão máxima no indutor é
2,00 vezes a tensão máxima no resistor e 2,00 vezes a tensão máxima no capacitor. (a) De que ângulo a
corrente está atrasada em relação à força eletromotriz do gerador? (b) Se a força eletromotriz máxima do
gerador é 30,0 V, qual deve ser a resistência do circuito para que a corrente máxima seja de 300 mA?
82 Um indutor de 1,50 mH em um circuito LC oscilante armazena uma energia máxima de 10,0 μJ. Qual
é a corrente máxima?
83 Um gerador de frequência ajustável é ligado em série com um indutor L = 2,50 mH e um capacitor C
= 3,00 μF. Para que frequência o gerador produz uma corrente com a maior amplitude possível no

circuito?
84 Um circuito RLC série possui uma frequência de ressonância de 6,00 kHz. Quando é excitado com
uma frequência de 8,00 kHz, o circuito possui uma impedância de 1,00 kΩ e uma constante de fase de
45o. Determine o valor de (a) R, (b) L e (c) C nesse circuito.
85 Um circuito LC oscila com uma frequência de 10,4 kHz. (a) Se a capacitância é 340 μF, qual é a
indutância? (b) Se a corrente máxima é 7,20 mA, qual é a energia total do circuito? (c) Qual é a carga
máxima do capacitor?
86 Quando está em carga e funcionando com uma tensão rms de 220 V, um motor consome uma corrente
rms de 3,00 A. A resistência do motor é 24,0 Ω e a reatância capacitiva é zero. Qual é a reatância
indutiva?
87 O gerador de corrente alternada da Fig. 31-39 fornece uma força eletromotriz de 120 V e 60,0 Hz.
Com a chave aberta como na figura, a corrente está adiantada de 20,0o em relação à força eletromotriz do
gerador. Quando a chave é colocada na posição 1, a corrente fica atrasada de 10,0o em relação à força
eletromotriz do gerador. Quando a chave é colocada na posição 2, a amplitude da corrente é 2,00 A.
Determine o valor (a) de R, (b) de L e (c) de C.
Figura 31-39 Problema 87.
88 Em um circuito LC oscilante, L = 8,00 mH e C = 1,40 μF. No instante t = 0, a corrente é máxima e
tem o valor de 12,0 mA. (a) Qual é a carga máxima do capacitor durante as oscilações? (b) Em que
instante de tempo t > 0 a taxa de variação da energia armazenada no capacitor é máxima pela primeira
vez? (c) Qual é o valor da taxa de variação?
89 No caso de um circuito RLC série, mostre que em um ciclo completo de período T (a) a energia
armazenada no capacitor não varia; (b) a energia armazenada no indutor não varia; (c) a energia
fornecida pela fonte alternada é (T/2) I cos ϕ; (d) a energia dissipada no resistor é TRI2/2. (e) Mostre
que os resultados dos itens (c) e (d) são iguais.
90 Que capacitância deve ser ligada a um indutor de 1,30 mH para que a frequência de ressonância do
circuito seja de 3,50 kHz?
91 Um circuito série com a combinação resistor-indutor-capacitor R , L , C tem a mesma frequência de
1 1 1
ressonância que um segundo circuito com uma combinação diferente, R , L , C . As duas combinações são
2 2 2
ligadas em série. Mostre que a frequência de ressonância do novo circuito é a mesma dos dois circuitos

separados.
92 Considere o circuito da Fig. 31-40. Com a chave S fechada e as outras duas chaves abertas, a
1
constante de tempo do circuito é τ . Com a chave S fechada e as duas outras chaves abertas, a constante
C 2
de tempo do circuito é τ . Com a chave S fechada e as outras duas chaves abertas, o circuito oscila com
L 3
um período T. Mostre que .
Figura 31-40 Problema 92.
93 Quando a força eletromotriz do gerador do Exemplo 31.07 é máxima, qual é a tensão (a) do gerador,
(b) do resistor, (c) do capacitor e (d) do indutor? Some as tensões, com os sinais apropriados, para
mostrar que os resultados satisfazem a regra das malhas.

_______________
1Do inglês root mean square. (N.T.)

