CAPÍTULO 27
Circuitos
27-1 CIRCUITOS DE UMA MALHA
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
27.01 Conhecer a relação entre a força eletromotriz e o trabalho realizado.
27.02 Conhecer a relação entre a força eletromotriz, a corrente e a potência de uma fonte ideal.
27.03 Desenhar o diagrama esquemático de um circuito de uma malha com uma fonte e três resistores.
27.04 Usar a regra das malhas para escrever uma equação para as diferenças de potencial dos elementos de um circuito ao
longo de uma malha fechada.
27.05 Conhecer a relação entre a resistência e a diferença de potencial entre os terminais de um resistor (regra das
resistências).
27.06 Conhecer a relação entre a força eletromotriz e a diferença de potencial entre os terminais de uma fonte (regra das
fontes).
27.07 Saber que resistores em série são atravessados pela mesma corrente, que também é a mesma do resistor equivalente.
27.08 Calcular o resistor equivalente de resistores em série.
27.09 Saber que a diferença de potencial entre as extremidades de um conjunto de resistores em série é a soma das diferenças
de potencial entre os terminais dos resistores.
27.10 Calcular a diferença de potencial entre dois pontos de um circuito.
27.11 Conhecer a diferença entre uma fonte real e uma fonte ideal e substituir, no diagrama de um circuito, uma fonte real por
uma fonte real em série com uma resistência.
27.12 Calcular a diferença de potencial entre os terminais de uma fonte real para os dois sentidos possíveis da corrente no
circuito.
27.13 Saber o que significa aterrar um circuito, e representar esse aterramento em um diagrama esquemático.
27.14 Saber que aterrar um circuito não afeta a corrente do circuito.
27.15 Calcular a taxa de dissipação de energia de uma fonte real.
27.16 Calcular a potência fornecida ou recebida por uma fonte.
Ideias-Chave
• Uma fonte de tensão realiza trabalho sobre cargas elétricas para manter uma diferença de potencial entre os terminais. Se dW
é o trabalho elementar que a fonte realiza para fazer com que uma carga elementar atravesse a fonte do terminal negativo para
o terminal positivo da fonte, a força eletromotriz da fonte (trabalho por unidade de carga) é dada por
• Uma fonte ideal é uma fonte cuja resistência interna é zero. A diferença de potencial entre os terminais de uma fonte ideal é

igual à força eletromotriz.
• As fontes reais possuem uma resistência interna diferente de zero. A diferença de potencial entre os terminais de uma fonte
real é igual à força eletromotriz apenas se a corrente que atravessa a fonte for nula.
• A variação de potencial de um terminal para o outro de uma resistência R no sentido da corrente é dada por –iR, e a variação
no sentido oposto é dada por +iR, em que i é a corrente (regra das resistências).
• A variação de potencial de um terminal para o outro de uma fonte ideal no sentido do terminal negativo para o terminal positivo é
+ , e a variação no sentido oposto é − (regra das fontes).
• A lei de conservação da energia leva à regra das malhas:
Regra das Malhas. A soma algébrica das variações de potencial encontradas ao longo de uma malha completa de um circuito é
igual a zero.
A lei de conservação da carga leva à lei dos nós (Capítulo 26):
Lei dos Nós. A soma das correntes que entram em um nó de um circuito é igual à soma das correntes que saem do nó.
• Quando uma fonte real de força eletromotriz e resistência interna r realiza trabalho sobre os portadores de carga da corrente
i que atravessa a bateria, a taxa P com a qual a fonte transfere energia para os portadores de carga é dada por
P = iV.
em que V é a diferença de potencial entre os terminais da bateria.
• A taxa P com a qual a resistência interna da fonte dissipa energia é dada por
r
P = i2r.
r
• A taxa P com a qual a energia química da fonte é transformada em energia elétrica é dada por
fem
P = i .
fem
• Resistores ligados em série são atravessados pela mesma corrente e podem ser substituídos por um resistor equivalente cuja
resistência é dada por
O que É Física?
Estamos cercados de circuitos elétricos. Podemos nos orgulhar do número de aparelhos elétricos que
possuímos ou fazer uma lista mental dos aparelhos elétricos que gostaríamos de possuir. Todos esses
aparelhos, e a rede de distribuição de energia elétrica que os faz funcionar, dependem da engenharia
elétrica moderna. Não é fácil estimar o valor econômico atual da engenharia elétrica e seus produtos,
mas podemos ter certeza de que esse valor aumenta sem parar, à medida que mais e mais tarefas são
executadas eletricamente. Hoje em dia, os aparelhos de rádio e televisão são sintonizados eletricamente;
as mensagens são enviadas pela internet; os artigos científicos são publicados e copiados na forma de
arquivos digitais e lidos nas telas dos computadores.
A ciência básica da engenharia elétrica é a física. Neste capítulo, estudamos a física de circuitos
elétricos que contêm apenas resistores e fontes (e, no Módulo 27-4, capacitores). Vamos limitar nossa
discussão a circuitos nos quais as cargas se movem sempre no mesmo sentido, conhecidos como

circuitos de corrente contínua ou circuitos de CC. Começamos com a seguinte pergunta: Como é
possível colocar cargas elétricas em movimento?
“Bombeamento” de Cargas
Se quisermos fazer com que cargas elétricas atravessem um resistor, precisamos estabelecer uma
diferença de potencial entre as extremidades do dispositivo. Para isso, poderíamos ligar as extremidades
do resistor às placas de um capacitor carregado. O problema é que o movimento das cargas faria o
capacitor se descarregar e, portanto, depois de certo tempo, o potencial seria o mesmo nas duas placas.
Quando isso acontecesse, não haveria mais um campo elétrico no interior do resistor, e a corrente
deixaria de circular.
Para produzir uma corrente constante, precisamos de uma “bomba” de cargas, um dispositivo que,
realizando trabalho sobre os portadores de carga, mantenha uma diferença de potencial entre dois
terminais. Um dispositivo desse tipo é chamado de fonte de tensão ou, simplesmente, fonte. Dizemos
que uma fonte de tensão produz uma força eletromotriz , o que significa que submete os portadores de
carga a uma diferença de potencial . O termo força eletromotriz, às vezes abreviado para fem, é usado,
por questões históricas, para designar a diferença de potencial produzida por uma fonte de tensão,
embora, na verdade, não se trate de uma força.
No Capítulo 26, discutimos o movimento de portadores de carga em um circuito em termos do
campo elétrico existente no circuito; o campo produz forças que colocam os portadores de carga em
movimento. Neste capítulo, vamos usar uma abordagem diferente, discutindo o movimento dos portadores
de carga em termos de energia — uma fonte de tensão fornece a energia necessária para o movimento por
meio do trabalho que realiza sobre os portadores.
Uma fonte muito útil é a bateria, usada para alimentar uma grande variedade de máquinas, desde
relógios de pulso até submarinos. A fonte mais importante na vida diária, porém, é o gerador de
eletricidade, que, por meio de ligações elétricas (fios) a partir de uma usina de energia elétrica, cria uma
diferença de potencial nas residências e escritórios. As células solares, presentes nos painéis em forma
de asa das sondas espaciais, também são usadas para gerar energia em localidades remotas do nosso
planeta. Fontes menos conhecidas são as células de combustível dos ônibus espaciais e as termopilhas
que fornecem energia elétrica a algumas naves espaciais e estações remotas na Antártida e outros locais.
Nem todas as fontes são artificiais: organismos vivos, como enguias elétricas e até seres humanos e
plantas, são capazes de gerar eletricidade.
Embora os dispositivos mencionados apresentem diferenças significativas quanto ao modo de
operação, todos executam as mesmas funções básicas: realizar trabalho sobre portadores de carga e
manter uma diferença de potencial entre dois terminais.

Figura 27-1 Um circuito elétrico simples, no qual uma fonte de força eletromotriz realiza trabalho sobre portadores de carga e mantém
uma corrente constante i em um resistor de resistência R.
Trabalho, Energia e Força Eletromotriz
A Fig. 27-1 mostra um circuito formado por uma fonte (uma bateria, por exemplo) e uma única resistência
R (o símbolo de resistência e de um resistor é ). A fonte mantém um dos terminais (o terminal
positivo ou terminal +) a um potencial elétrico maior que o outro (o terminal negativo ou terminal −).
Podemos representar a força eletromotriz da fonte por meio de uma seta apontando do terminal negativo
para o terminal positivo, como na Fig. 27-1. Um pequeno círculo na origem da seta que representa a força
eletromotriz serve para distingui-la das setas que indicam a direção da corrente.
Quando uma fonte não está ligada a um circuito, a energia que existe no interior da fonte não provoca
nenhum movimento dos portadores de carga. Quando, porém, a fonte é ligada a um circuito, como na Fig.
27-1, essa energia faz com que portadores de carga (positivos, por convenção) sejam transferidos do
terminal negativo para o terminal positivo da fonte, ou seja, no sentido da seta que representa a força
eletromotriz. Esse movimento é parte da corrente que se estabelece no mesmo sentido em todo o circuito
(no caso da Fig. 27-1, o sentido horário).
No interior da fonte, os portadores de carga positivos se movem de uma região de baixo potencial
elétrico e, portanto, de baixa energia potencial elétrica (o terminal negativo) para uma região de alto
potencial elétrico e alta energia potencial elétrica (o terminal positivo). Esse movimento tem o sentido
contrário ao sentido no qual os portadores positivos se moveriam sob a ação do campo elétrico que
existe entre os dois terminais (que aponta do terminal positivo para o terminal negativo). Isso significa
que deve haver uma energia no interior da fonte realizando um trabalho sobre as cargas e forçando as
cargas a se moverem dessa forma. A energia pode ser química, como nas baterias e nas células de
combustível, ou mecânica, como nos geradores. Também pode resultar de diferenças de temperatura,
como nas termopilhas, ou ser fornecida pelo Sol, como nas células solares.
Vamos agora analisar o circuito da Fig. 27-1 do ponto de vista do trabalho e da energia. Em um
intervalo de tempo dt, uma carga dq passa por todas as seções retas do circuito, como a seção aa′. A
mesma carga entra no terminal de baixo potencial da fonte de tensão e sai do terminal de alto potencial.
Para que a carga dq se mova dessa forma, a fonte deve realizar sobre a carga um trabalho dW. Definimos
a força eletromotriz da fonte por meio desse trabalho:

Figura 27-2 (a) Como neste circuito > , o sentido da corrente é determinado pela bateria B. (b) As transferências de energia que
B A
acontecem no circuito.
Em palavras, a força eletromotriz de uma fonte é o trabalho por unidade de carga que a fonte realiza para
transferir cargas do terminal de baixo potencial para o terminal de alto potencial. A unidade de força
eletromotriz do SI tem dimensões de joule por coulomb; como vimos no Capítulo 24, essa unidade é
chamada de volt.
Uma fonte de tensão ideal é uma fonte na qual os portadores de carga não encontram resistência ao
se deslocarem do terminal negativo para o terminal positivo. A diferença de potencial entre os terminais
de uma fonte ideal é igual à força eletromotriz da fonte. Assim, por exemplo, uma bateria ideal com uma
força eletromotriz de 12,0 V mantém uma diferença de 12,0 V entre os terminais, esteja ou não a fonte
ligada a um circuito, e sejam quais forem as características do circuito.
Uma fonte de tensão real possui uma resistência interna diferente de zero. Quando uma fonte real
não está ligada a um circuito e, portanto, não conduz uma corrente elétrica, a diferença de potencial entre
os terminais é igual à força eletromotriz. Quando a fonte conduz uma corrente, a diferença de potencial é
menor que a força eletromotriz. As fontes reais serão discutidas no final deste módulo.
Quando uma fonte é ligada a um circuito, a fonte transfere energia para os portadores de carga que
passam por ela. Essa energia pode ser transferida dos portadores de carga para outros dispositivos do

circuito, e usada, por exemplo, para acender uma lâmpada. A Fig. 27-2a mostra um circuito formado por
duas baterias ideais recarregáveis A e B, uma resistência R e um motor elétrico M que é capaz de
levantar um objeto usando a energia que recebe dos portadores de carga do circuito. Observe que as
baterias estão ligadas de tal forma que tendem a fazer as cargas circularem em sentidos opostos. O
sentido da corrente é determinado pela bateria que possui a maior força eletromotriz, que, no caso,
estamos supondo que seja a bateria B, de modo que a energia química da bateria B diminui com a
transferência de parte da energia para os portadores de carga. Por outro lado, a energia química da
bateria A aumenta, pois o sentido da corrente no interior da bateria A é do terminal positivo para o
terminal negativo. Assim, a bateria B, além de fornecer energia para acionar o motor M e vencer a
resistência R, também carrega a bateria A. A Fig. 27-2b mostra as três transferências de energia; todas
diminuem a energia química da bateria B.
Cálculo da Corrente em um Circuito de uma Malha
Vamos discutir agora dois métodos diferentes para calcular a corrente no circuito de uma malha da Fig.
27-3; um dos métodos se baseia na lei de conservação da energia, e o outro no conceito de potencial. O
circuito que vamos analisar é formado por uma fonte ideal B cuja força eletromotriz é , um resistor de
resistência R e dois fios de ligação. (A menos que seja afirmado o contrário, vamos supor que os fios dos
circuitos possuem resistência desprezível. Na maioria dos casos, os fios servirão apenas para transferir
os portadores de corrente de um dispositivo para outro.)
Método da Energia
De acordo com a Eq. 26-27 (P = i2R), em um intervalo de tempo dt, uma energia dada por i2R dt é
transformada em energia térmica no resistor da Fig. 27-3. Como foi observado no Módulo 26-5, podemos
dizer que essa energia é dissipada no resistor. (Como estamos supondo que a resistência dos fios é
desprezível, os fios não dissipam energia.) Durante o mesmo intervalo, uma carga dq = i dt atravessa a
fonte B, e o trabalho realizado pela fonte sobre essa carga, de acordo com a Eq. 27-1, é dado por
dW = dq = i dt.
De acordo com a lei de conservação da energia, o trabalho realizado pela fonte (ideal) é igual à energia
térmica que aparece no resistor:
i dt = i2R dt.
Isso nos dá
= iR.
A força eletromotriz é a energia por unidade de carga transferida da fonte para as cargas que se movem

no circuito. A grandeza iR é a energia por unidade de carga transferida das cargas móveis para o resistor
e convertida em calor. Assim, essa equação mostra que a energia por unidade de carga transferida para as
cargas em movimento é igual à energia por unidade de carga transferida pelas cargas em movimento.
Explicitando i, obtemos
Método do Potencial
Suponha que começamos em um ponto qualquer do circuito da Fig. 27-3 e nos deslocamos mentalmente
ao longo do circuito em um sentido arbitrário, somando algebricamente as diferenças de potencial que
encontramos no caminho. Ao voltar ao ponto de partida, teremos voltado também ao potencial inicial.
Antes de prosseguir, queremos chamar a atenção para o fato de que esse raciocínio vale não só para
circuitos com uma malha, como o da Fig. 27-3, mas também para uma malha fechada de um circuito com
várias malhas, como os que serão discutidos no Módulo 27-2.
REGRA DAS MALHAS: A soma algébrica das variações de potencial encontradas ao longo de uma malha completa de um circuito é
zero.
Figura 27-3 Um circuito de uma malha no qual uma resistência R está ligada aos terminais de uma fonte ideal B de força eletromotriz . A
corrente resultante i é a mesma em todo o circuito.
Essa regra, também conhecida como lei das malhas de Kirchhoff (ou lei das tensões de Kirchhoff), em
homenagem ao físico alemão Gustav Robert Kirchhoff, equivale a dizer que cada ponto de uma montanha
possui apenas uma altitude em relação ao nível do mar. Se partimos de um ponto qualquer e voltamos ao
mesmo ponto depois de passear pela montanha, a soma algébrica das mudanças de altitude durante a
caminhada é necessariamente zero.
Na Fig. 27-3, vamos começar no ponto a, cujo potencial é V , e nos deslocar mentalmente no sentido
a

horário até estarmos de volta ao ponto a, anotando as mudanças de potencial que ocorrem no percurso.
Nosso ponto de partida será o terminal negativo da fonte. Como a fonte é ideal, a diferença de potencial
entre os terminais da fonte é . Assim, quando atravessamos a fonte, passando do terminal negativo para
o terminal positivo, a variação de potencial é + .
Quando passamos do terminal positivo da fonte para o terminal superior do resistor, não há variação
de potencial, já que a resistência do fio é desprezível. Quando atravessamos o resistor, o potencial varia
de acordo com a Eq. 26-8 (que pode ser escrita na forma V = iR). O potencial deve diminuir, pois
estamos passando do lado de potencial mais alto do resistor para o lado de potencial mais baixo. Assim,
a variação de potencial é −iR.
Voltamos ao ponto a pelo fio que liga o terminal inferior do resistor ao terminal negativo da fonte.
Uma vez que a resistência do fio é desprezível, não há variação de potencial nesse trecho do circuito. No
ponto a, o potencial é novamente V . Como percorremos todo o circuito, o potencial inicial, depois de
a
modificado pelas variações de potencial ocorridas ao longo do caminho, deve ser igual ao potencial
final, ou seja,
V + – iR = V .
a a
Subtraindo V de ambos os membros da equação, obtemos
a
– iR = 0.
Explicitando i nesta equação, obtemos o mesmo resultado, i = /R, que obtivemos usando o método da
energia (Eq. 27-2).
Se aplicarmos a regra da malha a um percurso no sentido anti-horário, o resultado será
– + iR = 0
e mais uma vez obteremos i = /R. Assim, o sentido no qual percorremos o circuito para aplicar a regra
das malhas é irrelevante.
Com o objetivo de facilitar o estudo de circuitos mais complexos que o da Fig. 27-3, vamos resumir
o que vimos até agora em duas regras para as diferenças de potencial produzidas pelos dispositivos do
circuito quando percorremos uma malha.
REGRA DAS RESISTÊNCIAS: Quando atravessamos uma resistência no sentido da corrente, a variação do potencial é −iR; quando
atravessamos uma resistência no sentido oposto, a variação é +iR.
REGRA DAS FONTES: Quando atravessamos uma fonte ideal no sentido do terminal negativo para o terminal positivo, a variação do

potencial é + ; quando atravessamos uma fonte no sentido oposto, a variação é − .
Teste 1
A figura mostra a corrente i em um circuito formado por uma fonte B e uma resistência R (além de fios de resistência desprezível).
(a) A seta que indica a força eletromotriz da fonte B deve apontar para a esquerda ou para a direita? Coloque os pontos a, b, e c na
ordem decrescente (b) do valor absoluto da corrente, (c) do potencial elétrico e (d) da energia potencial elétrica dos portadores de
carga.
Outros Circuitos de uma Malha
Nesta seção, vamos ampliar o circuito simples da Fig. 27-3 de duas formas.
Resistência Interna
A Fig. 27-4a mostra uma fonte real, de resistência interna r, ligada a um resistor externo de resistência R.
A resistência interna da fonte é a resistência elétrica dos materiais condutores que existem no interior da
fonte e, portanto, é parte integrante da fonte. Na Fig. 27-4a, porém, a fonte foi desenhada como se
pudesse ser decomposta em uma fonte ideal de força eletromotriz em série com um resistor de
resistência r. A ordem em que os símbolos dos dois dispositivos são desenhados é irrelevante.
Figura 27-4 (a) Circuito de uma malha com uma fonte real de força eletromotriz e resistência interna r. (b) O mesmo circuito,
representado de outra forma para mostrar as variações do potencial elétrico quando o circuito é percorrido no sentido horário a partir do ponto
a. O potencial V foi tomado arbitrariamente como zero; os outros potenciais foram calculados em relação a V .
a a
Aplicando a regra das malhas no sentido horário, a partir do ponto a, as variações do potencial nos
dão

Explicitando a corrente, obtemos
Observe que a Eq. 27-4 se reduz à Eq. 27-2 se a fonte for ideal, ou seja, se r = 0.
A Fig. 27-4b mostra graficamente as variações de potencial elétrico ao longo do circuito. (Para
estabelecer uma ligação mais direta da Fig. 27-4b com o circuito fechado da Fig. 27-4a, imagine o
gráfico desenhado na superfície lateral de um cilindro, com o ponto a da esquerda coincidindo com o
ponto a da direita.) Percorrer o circuito é como passear em uma montanha e voltar ao ponto de partida;
na chegada, você se encontra na mesma altitude em que estava quando partiu.
Neste livro, se não especificarmos uma resistência interna para a fonte ou afirmarmos que a fonte é
real, estará implícito que se trata de uma fonte ideal, ou seja, que a resistência interna da fonte é tão
pequena, em comparação com as outras resistências do circuito, que pode ser desprezada.
Resistências em Série
A Fig. 27-5a mostra três resistências ligadas em série a uma fonte ideal de força eletromotriz . Essa
descrição pouco tem a ver com o modo como as resistências estão desenhadas. A expressão “em série”
significa apenas que as resistências são ligadas uma após a outra e que uma diferença de potencial V é
aplicada às extremidades da ligação. Na Fig. 27-5a, as resistências estão ligadas uma após a outra entre
os pontos a e b, e uma diferença de potencial entre os pontos a e b é mantida por uma fonte. As
diferenças de potencial entre os terminais de cada resistência produzem a mesma corrente i em todas as
resistências. De modo geral,

Figura 27-5 (a) Três resistores ligados em série entre os pontos a e b. (b) Circuito equivalente, com os três resistores substituídos por uma
resistência equivalente R .
eq
Quando uma diferença de potencial V é aplicada a resistências ligadas em série, a corrente i é a mesma em todas as resistências, e a
soma das diferenças de potencial das resistências é igual à diferença de potencial aplicada V.
Observe que as cargas que atravessam resistências ligadas em série têm um único caminho possível. Se
existe mais de um caminho, as resistências não estão ligadas em série.
Resistências ligadas em série podem ser substituídas por uma resistência equivalente R percorrida pela mesma corrente i e com a
eq
mesma diferença de potencial total V que as resistências originais.
A Fig. 27-5b mostra a resistência equivalente R das três resistências da Fig. 27-5a.
eq
Para determinar o valor da resistência R da Fig. 27-5b, aplicamos a regra das malhas aos dois
eq
circuitos. Na Fig. 27-5a, começando no ponto a e percorrendo o circuito no sentido horário, temos

Na Fig. 27-5b, com as três resistências substituídas por uma resistência equivalente R , obtemos
eq
Igualando as Eqs. 27-5 e 27-6, obtemos
R = R + R + R .
eq 1 2 3
A extensão para n resistores é imediata e nos dá
Observe que, no caso de duas ou mais resistências ligadas em série, a resistência equivalente é maior que
a maior das resistências.
Teste 2
Na Fig. 27-5a, se R > R > R , coloque as três resistências na ordem decrescente (a) da corrente que passa pelas resistências e (b)
1 2 3
da diferença de potencial entre os terminais das resistências.
Figura 27-6 Existe uma diferença de potencial entre os pontos a e b, que são os terminais de uma fonte real.
Diferença de Potencial entre Dois Pontos
Muitas vezes, estamos interessados em determinar a diferença de potencial entre dois pontos de um
circuito. Assim, por exemplo, na Fig. 27-6, qual é a diferença de potencial V − V entre os pontos a e b?
b a
Para obter a resposta, vamos começar no ponto a (cujo potencial é V ) e nos deslocar, passando pela
a
fonte, até o ponto b (cujo potencial é V ), anotando as diferenças de potencial encontradas no percurso.
b
Quando passamos pela fonte, o potencial aumenta de . Quando passamos pela resistência interna r da
fonte, estamos nos movendo no sentido da corrente e, portanto, o potencial diminui de ir. A essa altura,

estamos no ponto b e temos
Para calcular o valor dessa expressão, precisamos conhecer a corrente i. Observe que o circuito é o
mesmo da Fig. 27-4a, para o qual, de acordo com a Eq. 27-4,
Substituindo i pelo seu valor, dado pela Eq. 27-9, na Eq. 27-8, obtemos
Substituindo os valores numéricos que aparecem na Fig. 27-6, temos
Suponha que tivéssemos escolhido percorrer o circuito no sentido anti-horário, passando pelo
resistor R em vez de passar pela fonte. Como, nesse caso, estaríamos nos movendo no sentido oposto ao
da corrente, o potencial aumentaria de iR. Assim,
Substituindo i pelo seu valor, dado pela Eq. 27-9, obtemos mais uma vez a Eq. 27-10. Assim,
substituindo os valores numéricos, obtemos o mesmo resultado, V − V = 8,0 V. No caso geral,
b a
Para determinar a diferença de potencial entre dois pontos de um circuito, começamos em um dos pontos e percorremos o circuito até
o outro ponto, somando algebricamente as variações de potencial que encontramos no percurso.
Diferença de Potencial entre os Terminais de uma Fonte Real
Na Fig. 27-6, os pontos a e b estão situados nos terminais da fonte; assim, a diferença de potencial V −
b
V é a diferença de potencial entre os terminais da fonte. De acordo com a Eq. 27-8, temos
a

De acordo com a Eq. 27-13, se a resistência interna r da fonte da Fig. 27-6 fosse zero, V seria igual
à força eletromotriz da fonte, ou seja, 12 V. Como r = 2,0 τ, V é menor que . De acordo com a Eq. 27-
11, V = 8,0 V. Observe que o resultado depende da corrente que atravessa a fonte. Se a fonte estivesse em
outro circuito no qual a corrente fosse diferente, V teria outro valor.
Aterramento de um Circuito
A Fig. 27-7a mostra o mesmo circuito da Fig. 27-6, exceto pelo fato de que o ponto a está ligado
diretamente à terra, o que é indicado pelo símbolo . Aterrar um circuito pode significar ligar o
circuito à superfície da Terra (na verdade, ao solo úmido, que é um bom condutor de eletricidade). Neste
diagrama, porém, o símbolo de terra significa apenas que o potencial é definido como zero no ponto em
que se encontra o símbolo. Assim, na Fig. 27-7a, o potencial do ponto a é definido como V = 0. Nesse
a
caso, conforme a Eq. 27-11, o potencial no ponto b é V = 8,0 V.
b
Figura 27-7 (a) O ponto a está ligado diretamente à terra. (b) O ponto b está ligado diretamente à terra.
A Fig. 27-7b mostra o mesmo circuito, exceto pelo fato de que agora é o ponto b que está ligado à
terra. Assim, o potencial do ponto b é definido como V = 0; nesse caso, de acordo com a Eq. 27-11, o
b
potencial no ponto a é V = −8,0 V.
a
Potência, Potencial e Força Eletromotriz
Quando uma bateria ou outro tipo de fonte de tensão realiza trabalho sobre portadores de carga para
estabelecer uma corrente i, o dispositivo transfere energia de sua fonte interna de energia (energia
química, no caso de uma bateria) para os portadores de carga. Como toda fonte real possui uma
resistência interna r, a fonte também dissipa uma parte da energia na forma de calor (Módulo 26-5).
Vamos ver agora como essas transferências estão relacionadas.
A potência P, fornecida pela fonte aos portadores de carga, é dada pela Eq. 26-26:
em que V é a diferença de potencial entre os terminais da fonte. De acordo com a Eq. 27-13, podemos

fazer V = = − ir na Eq. 27-14 para obter
Examinando a Eq. 27-15, reconhecemos o termo i2r como a potência P dissipada no interior da fonte
r
(Eq. 26-27) como
Nesse caso, o termo i da Eq. 27-15 é a soma da potência transferida para os portadores de carga com a
potência dissipada pela fonte, que pode ser chamada de P . Assim,
fonte
Quando uma bateria está sendo recarregada, com uma corrente passando no “sentido inverso”, a
transferência de energia é dos portadores de carga para a bateria; parte da energia é usada para aumentar
a energia química da bateria e parte é dissipada na resistência interna r da bateria. A taxa de variação da
energia química é dada pela Eq. 27-17, a taxa de dissipação é dada pela Eq. 27-16 e a taxa com a qual os
portadores de carga fornecem energia é dada pela Eq. 27-14.
Teste 3
Uma fonte possui uma força eletromotriz de 12 V e uma resistência interna de 2 τ. A diferença de potencial entre os terminais é
menor, maior ou igual a 12 V se a corrente que atravessa a fonte (a) é do terminal negativo para o terminal positivo, (b) é do
terminal positivo para o terminal negativo e (c) é zero?
Exemplo 27.01 Circuito de uma malha com duas fontes reais
As forças eletromotrizes e resistências do circuito da Fig. 27-8a têm os seguintes valores:
= 4,4 V, = 2,1 V,
1 2
r = 2,3 Ω, r = 1,8 Ω, R = 5,5 Ω.
1 2
(a) Qual é a corrente i no circuito?
IDEIA-CHAVE
Podemos obter uma expressão para a corrente i nesse circuito de uma malha aplicando uma vez a regra das malhas, na qual
somamos as variações de potencial ao longo da malha e igualamos a soma a zero.

Figura 27-8 (a) Circuito de uma malha com duas fontes reais e um resistor. As fontes estão em
oposição, ou seja, tendem a fazer a corrente atravessar o resistor em sentidos opostos. (b) Gráfico
dos potenciais, percorrendo o circuito no sentido horário a partir do ponto a e tomando
arbitrariamente o potencial do ponto a como zero. (Para estabelecer uma correlação direta da Fig.
27-8b com o circuito fechado da Fig. 27-8a, interrompa mentalmente o circuito no ponto a da Fig.
27-8a, desdobre para a esquerda a parte do circuito à esquerda de a e desdobre para a direita a
parte do circuito à direita de a.)
Cálculos: Embora conhecer o sentido de i não seja necessário, podemos determiná-lo com facilidade a partir dos valores
das forças eletromotrizes das duas fontes. Como é maior que , a fonte 1 controla o sentido de i, e a corrente tem o sentido
1 2
horário. Vamos aplicar a regra das malhas percorrendo o circuito no sentido anti-horário (contra a corrente), começando no ponto
a. O resultado é o seguinte:
– + ir + iR + ir + = 0.
1 1 2 2
O leitor pode verificar que a mesma equação é obtida quando aplicamos a regra das malhas no sentido horário ou começamos em
outro ponto do circuito. Além disso, vale a pena comparar a equação termo a termo com a Fig. 27-8b, que mostra graficamente as

variações de potencial (com o potencial do ponto a tomado arbitrariamente como zero).
Explicitando a corrente i na equação anterior, obtemos
(b) Qual é a diferença de potencial entre os terminais da fonte 1 na Fig. 27-8a?
IDEIA-CHAVE
Precisamos somar as diferenças de potencial entre os pontos a e b.
Cálculos: Vamos começar no ponto b (o terminal negativo da fonte 1) e percorrer o circuito no sentido horário até chegar
ao ponto a (o terminal positivo da fonte 1), anotando as variações de potencial. O resultado é o seguinte:
V − ir + = V ,
b 1 1 a
o que nos dá
que é menor que a força eletromotriz da fonte. O leitor pode verificar que o resultado está correto começando no ponto b da Fig.
27-8a e percorrendo o circuito no sentido anti-horário até chegar ao ponto a. Este problema chama a atenção para dois fatos: (1)
A diferença de potencial entre dois pontos de um circuito não depende do caminho escolhido para ir de um ponto a outro. (2)
Quando a corrente que atravessa a bateria tem o sentido “correto”, a diferença de potencial entre os terminais é menor que o valor
nominal da força eletromotriz, ou seja, o valor de tensão que está escrito na bateria.
27-2 CIRCUITOS COM MAIS DE UMA MALHA
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
27.17 Conhecer a regra dos nós.
27.18 Desenhar um diagrama esquemático de um circuito formado por uma fonte e três resistores em paralelo e saber distingui-
lo do diagrama de um circuito formado por uma bateria e três resistores em série.
27.19 Saber que resistores em paralelo estão submetidos à mesma diferença de potencial, que também é a mesma do resistor
equivalente.

27.20 Calcular a resistência do resistor equivalente de vários resistores em paralelo.
27.21 Saber que a corrente total que atravessa uma combinação de resistores em paralelo é a soma das correntes que
atravessam os resistores.
27.22 No caso de um circuito com uma fonte, alguns resistores em paralelo e outros resistores em série, simplificar o circuito
por partes, usando resistores equivalentes, até que a corrente na fonte possa ser determinada, e depois trabalhar no
sentido inverso para calcular a corrente e a diferença de potencial de cada resistor.
27.23 Se um circuito não pode ser simplificado usando resistores equivalentes, identificar as malhas do circuito, escolher nomes
e sentidos para as correntes dos ramos, escrever equações para todas as malhas usando a regra das malhas e resolver o
sistema de equações resultante para obter as correntes dos ramos.
27.24 Em um circuito com fontes reais em série, substituí-las por uma única fonte ideal em série com um resistor.
27.25 Em um circuito com fontes reais em paralelo, substituí-las por uma única fonte ideal em série com um resistor.
Ideia-Chave
• Quando duas ou mais resistências estão em paralelo, elas são submetidas à mesma diferença de potencial. A resistência
equivalente de uma associação em paralelo de várias resistências é dada por
Figura 27-9 Circuito com mais de uma malha, formado por três ramos: o ramo da esquerda bad, o ramo da direita bcd e o ramo central
bd. O circuito também contém três malhas: a malha da esquerda badb, a malha da direita bcdb e a malha externa badcb.
Circuitos com Mais de uma Malha
A Fig. 27-9 mostra um circuito com mais de uma malha. Para simplificar a análise, vamos supor que as
fontes são ideais. Existem dois nós no circuito, nos pontos b e d, e três ramos ligando os nós: o ramo da
esquerda (bad), o ramo da direita (bcd) e o ramo central (bd). Quais são as correntes nos três ramos?
Vamos rotular arbitrariamente as correntes, usando um índice diferente para cada ramo. A corrente i
1
tem o mesmo valor em todos os pontos do ramo bad, i tem o mesmo valor em todos os pontos do ramo
2
bcd, e i tem o mesmo valor em todos os pontos do ramo bd. Os sentidos das correntes foram escolhidos
3
arbitrariamente.
Considere o nó d. As cargas entram no nó pelas correntes i e i e deixam o nó pela corrente i .
1 3 2
Como a carga total não pode mudar, a corrente total que chega tem que ser igual à corrente total que sai:

Podemos verificar facilmente que a aplicação dessa condição ao nó b leva à mesma equação. A Eq. 27-
18 sugere o seguinte princípio geral:
REGRA DOS NÓS: A soma das corrente que entram em um nó é igual à soma das correntes que saem do nó.
Essa regra também é conhecida como lei dos nós de Kirchhoff (ou lei das correntes de Kirchhoff). Trata-
se simplesmente de outra forma de enunciar a lei de conservação da carga: a carga não pode ser criada
nem destruída em um nó. Nossas ferramentas básicas para resolver circuitos complexos são, portanto, a
regra das malhas (baseada na lei de conservação da energia) e a regra dos nós (baseada na lei da
conservação da carga).
A Eq. 27-18 envolve três incógnitas. Para resolver o circuito (ou seja, para determinar o valor das
três correntes), precisamos de mais duas equações independentes que envolvam as mesmas variáveis.
Podemos obtê-las aplicando duas vezes a regra das malhas. No circuito da Fig. 27-9, temos três malhas:
a malha da esquerda (badb), a malha da direita (bcdb) e a malha externa (badcb). A escolha das duas
malhas é arbitrária; vamos optar pelas malhas da esquerda e da direita.
Percorrendo a malha da esquerda no sentido anti-horário a partir do ponto b, obtemos
Percorrendo a malha da direita no sentido anti-horário a partir do ponto b, obtemos
Agora dispomos de três equações (Eqs. 27-18, 27-19 e 27-20) tendo como incógnitas as três correntes;
esse sistema de equações pode ser resolvido por várias técnicas.
Se tivéssemos aplicado a regra das malhas à malha externa, teríamos obtido (percorrendo a malha
no sentido anti-horário a partir do ponto b) a seguinte equação:
– i R – i R – = 0.
1 1 1 2 2 2
Esta equação pode parecer uma informação nova, mas é, na verdade, a soma das Eqs. 27-19 e 27-20 e,
portanto, não constitui uma terceira equação independente obtida a partir da regra das malhas. (Por outro
lado, poderia ser usada para resolver o problema em combinação com a Eq. 27-18 e a Eq. 27-19 ou a
Eq. 27-20.)
Resistências em Paralelo
A Fig. 27-10a mostra três resistências ligadas em paralelo a uma fonte ideal de força eletromotriz . O

termo “em paralelo” significa que as três resistências estão ligadas entre si nas duas extremidades.
Assim, todas estão sujeitas à mesma diferença de potencial aplicada pela fonte. No caso geral,
Quando uma diferença de potencial V é aplicada a resistências ligadas em paralelo, todas as resistências são submetidas à mesma
diferença de potencial V.
Na Fig. 27-10a, a diferença de potencial aplicada V é mantida pela fonte. Na Fig. 27-10b, as três
resistências em paralelo foram substituídas por uma resistência equivalente R .
eq
Resistências ligadas em paralelo podem ser substituídas por uma resistência equivalente R com a mesma diferença de potencial V e a
eq
mesma corrente total i que as resistências originais.
Figura 27-10 (a) Três resistores ligados em paralelo entre os pontos a e b. (b) Circuito equivalente, com os três resistores substituídos por
uma resistência equivalente R .
eq
Para determinar o valor da resistência R da Fig. 27-10b, escrevemos as correntes nas resistências
eq
da Fig. 27-10a na forma
em que V é a diferença de potencial entre a e b. Aplicando a regra dos nós ao ponto a da Fig. 27-10a e
substituindo as correntes por seus valores, temos
Quando substituímos as resistências em paralelo pela resistência equivalente R (Fig. 27-10b), obtemos
eq

Comparando as Eqs. 27-21 e 27-22, temos
Generalizando esse resultado para o caso de n resistências, temos
No caso de duas resistências, a resistência equivalente é o produto das resistências dividido pela soma,
ou seja,
Note que, se duas ou mais resistências estão ligadas em paralelo, a resistência equivalente é menor
que a menor das resistências. A Tabela 27-1 mostra as relações de equivalência para resistores e
capacitores em série e em paralelo.
Tabela 27-1 Resistores e Capacitores em Série e em Paralelo
Em série Em paralelo Em série Em paralelo
Resistores Capacitores
A corrente é a mesma em todos os A diferença de potencial é a A carga é a mesma em todos os A diferença de potencial é a
resistores mesma em todos os resistores capacitores mesma em todos os capacitores
Teste 4
Uma fonte com uma diferença de potencial V entre os terminais é ligada a uma combinação de dois resistores iguais e passa a
conduzir uma corrente i. Qual é a diferença de potencial e qual a corrente em um dos resistores, se os resistores estiverem ligados
(a) em série e (b) em paralelo?
Exemplo 27.02 Resistores em paralelo e em série

A Fig. 27-11a mostra um circuito com mais de uma malha formado por uma fonte ideal e quatro resistências com os seguintes
valores:
R = 20 Ω, R = 20 Ω, = 12 V,
1 2
R = 30 Ω, R = 8,0 Ω.
3 4
(a) Qual é a corrente na fonte?
IDEIA-CHAVE
Observando que a corrente na fonte é a mesma que em R , vemos que é possível determinar a corrente aplicando a regra das
1
malhas a uma malha que inclui R , já que a diferença de potencial entre os terminais de R depende dessa corrente.
1 1
Método incorreto: As duas malhas que se prestam a esse papel são a malha da esquerda e a malha externa.
Observando que a seta que representa a força eletromotriz aponta para cima e, portanto, a corrente na fonte tem o sentido
horário, podemos aplicar a regra das malhas à malha da esquerda, começando no ponto a e percorrendo a malha no sentido
horário. Chamando de i a corrente na fonte, temos
+ – iR – iR – iR = 0 (incorreta).
1 2 4
Esta equação, porém, é incorreta, porque parte do pressuposto de que as correntes nas resistências R , R e R são iguais. As
1 2 4
correntes em R e R são realmente iguais, já que a corrente que passa por R também passa pela fonte e por R sem mudar de
1 4 4 1
valor. Entretanto, essa corrente se divide ao chegar ao nó b: uma parte da corrente passa por R e uma parte passa por R .
2 3
Método ineficaz: Para distinguir as várias correntes presentes no circuito, devemos rotulá-las, como na Fig. 27-11b.
Em seguida, começando no ponto a, podemos aplicar a regra das malhas à malha da esquerda, no sentido horário, para obter
+ – i R – i R – i R = 0.
1 1 2 2 1 4
Infelizmente, essa equação contém duas incógnitas, i e i ; necessitamos de pelo menos mais uma equação para resolver o
1 2
problema.
Método eficaz: Uma tática muito melhor é simplificar o circuito da Fig. 27-11b usando resistências equivalentes.
Observe que R e R não estão em série e, portanto, não podem ser substituídas por uma resistência equivalente; entretanto, R e
1 2 2
R estão em paralelo, de modo que podemos usar a Eq. 27-24 ou a Eq. 27-25 para calcular o valor da resistência equivalente R .
3 23
De acordo com a Eq. 27-25,
Podemos agora desenhar o circuito como na Fig. 27-11c; observe que a corrente em R deve ser i , já que as mesmas cargas que
23 1

passam por R e R também passam por R . Para esse circuito simples, com uma única malha, a regra das malhas (aplicada no
1 4 23
sentido horário, a partir do ponto a, como na Fig. 27-11d), nos dá
+ – i R – i R – i R = 0
1 1 1 23 2 4
Substituindo os valores dados, obtemos
12 V – i (20 Ω) – i (12 Ω) – i (8,0 Ω) = 0,
1 1 1
e, portanto,
(b) Qual é a corrente i em R ?
2 2
IDEIAS-CHAVE
(1) Podemos começar com o circuito equivalente da Fig. 27-11d, no qual R e R foram substituídas por R . (2) Como R e R estão
2 3 23 2 3
em paralelo, elas estão submetidas à mesma diferença de potencial, que também é a mesma de R .
23
Cálculos: Sabemos que a corrente em R é i = 0,30 A. Assim, podemos usar a Eq. 26-8 (R = V/i) e a Fig. 27-11e para
23 1
calcular a diferença de potencial V em R :
23 23
V = i R = (0,30 A)(12 Ω) = 3,6 V.
23 1 23
Isso significa que a diferença de potencial em R também é 3,6 V (Fig. 27-11f). De acordo com a Eq. 26-8 e a Fig. 27-11g, a
2
corrente i em R é dada por
2 2
(c) Qual é a corrente i em R ?
3 3
IDEIAS-CHAVE
Podemos encontrar a resposta de duas formas: (1) Usando a Eq. 26-8, como no item (b). (2) Usando a regra dos nós, segundo a
qual, no ponto b da Fig. 27-11b, a corrente que entra, i , e as correntes que saem, i e i , estão relacionadas pela equação
1 2 3
i = i + i .
1 2 3

Cálculo: Explicitando i na equação anterior, obtemos o resultado que aparece na Fig. 27-11g:
3

Figura 27-11 (a) Circuito com uma fonte ideal. (b) Escolha de nomes e sentidos para as
correntes. (c) Substituição de resistores em paralelo por um resistor equivalente. (d)-(g)
Substituição inversa para determinar as correntes nos resistores em paralelo.
Exemplo 27.03 Muitas fontes reais em série e em paralelo em um peixe elétrico
Os peixes elétricos são capazes de gerar correntes elétricas com o auxílio de células chamadas eletroplacas, que são fontes de
tensão biológicas. No peixe elétrico conhecido como poraquê, as eletroplacas estão dispostas em 140 linhas longitudinais, com
cerca de 5000 eletroplacas cada uma, como mostrado na Fig. 27-12a. Cada eletroplaca tem uma força eletromotriz de 0,15 V e
uma resistência interna r de 0,25 τ. A água em torno da enguia completa o circuito entre as extremidades do conjunto de
eletroplacas — uma situada na cabeça do animal e a outra situada na cauda.
(a) Se a água em torno da enguia tem uma resistência R = 800 τ, qual é o valor da corrente que o animal é capaz de produzir na
a
água?
IDEIA-CHAVE
Podemos simplificar o circuito da Fig. 27-12a substituindo combinações de fontes e resistências internas por fontes e resistências
equivalentes.
Cálculos: Considere uma linha. A força eletromotriz total de 5000 eletroplacas ligadas em série é a soma das forças
linha
eletromotrizes:
= 5000 = (5000)(0,15 V) = 750 V.
linha
A resistência total R de uma linha é a soma das resistências internas das 5000 eletroplacas:
linha
R = 5000r = (5000)(0,25 Ω) = 1250 Ω.
linha
Podemos agora representar cada uma das 140 linhas por uma única força eletromotriz e uma única resistência R (Fig. 27-
linha linha
12b).
Na Fig. 27-12b, a força eletromotriz entre o ponto a e o ponto b em todas as linhas é = 750 V. Como as linhas são
linha
iguais e estão todas ligadas ao ponto a da Fig. 27-12b, o potencial é o mesmo em todos os pontos b da figura. Assim, podemos
imaginar que todos os pontos b estão ligados entre si, formando um único ponto b. Uma vez que a força eletromotriz entre o
ponto a e esse ponto b único é = 750 V, podemos substituir o circuito da Fig. 27-12b pelo circuito da Fig. 27-12c.
linha

Figura 27-12 (a) Circuito usado para modelar uma enguia elétrica. Cada eletroplaca do animal
tem uma força eletromotriz e uma resistência interna r. Em cada uma das 140 linhas que se
estendem da cabeça à cauda da enguia existem 5000 eletroplacas. A resistência da água é R . (b) A
a
força eletromotriz e resistência R de cada linha. (c) A força eletromotriz entre os pontos a e
linha linha
b é . Entre os pontos b e c existem 140 resistências R em paralelo. (d) Circuito simplificado,
linha linha
com as resistências em paralelo substituídas por uma resistência equivalente R .
eq
Entre os pontos b e c da Fig. 27-12c existem 140 resistências R = 1250 τ, todas em paralelo. A resistência equivalente R dessa
linha eq
combinação é fornecida pela Eq. 27-24:
Substituindo as resistências em paralelo por R , obtemos o circuito simplificado da Fig. 27-12d. Aplicando a regra das malhas e
eq
percorrendo o circuito no sentido anti-horário a partir do ponto b, temos

– R – iR = 0.
linha a eq
Explicitando i e substituindo os valores conhecidos, obtemos
Se a cabeça ou a cauda da enguia está nas proximidades de um peixe, parte dessa corrente pode passar pelo corpo do peixe,
atordoando-o ou matando-o.
(b) Qual é corrente i em cada linha da Fig. 27-12a?
linha
IDEIA-CHAVE
Como todas as linhas são iguais, a corrente se divide igualmente entre elas.
Cálculo: Podemos escrever:
Assim, a corrente em cada linha é pequena, cerca de duas ordens de grandeza menor que a corrente que circula na água. Como a
corrente está bem distribuída no corpo da enguia, o animal não sofre nenhum incômodo ao produzir uma descarga elétrica.
Exemplo 27.04 Circuito com mais de uma malha e o sistema de equações de malha
A Fig. 27-13 mostra um circuito cujos elementos têm os seguintes valores: = 3,0 V, = 6,0 V, R = 2,0 Ω, R = 4,0 Ω. As três
1 2 1 2
fontes são ideais. Determine o valor absoluto e o sentido da corrente nos três ramos.
IDEIAS-CHAVE
Não vale a pena tentar simplificar o circuito, já que não existem dois resistores em paralelo, e os resistores que estão em série (no
ramo da direita e no ramo da esquerda) são muito fáceis de lidar. Assim, é melhor aplicar logo de saída as regras dos nós e das
malhas.
Regra dos nós: Escolhendo arbitrariamente o sentido das correntes, como mostra a Fig. 27-13, aplicamos a regra dos
nós ao ponto a para escrever
Como uma aplicação da regra dos nós ao ponto b fornece apenas uma repetição da Eq. 27-26, aplicamos a regra das malhas a duas

das	três	malhas	do	circuito.
Figura	27-13 	Circuito	de	duas	malhas	com	três	fontes	ideais	e	cinco	resistências.
Malha	da	esquerda: 	Escolhemos	arbitrariamente	a	malha	da	esquerda,	começamos	arbitrariamente	no	ponto	b	e
percorremos	arbitrariamente	a	malha	no	sentido	horário,	obtendo
|     |     | –i R 	+	 | 	–	i R 	–	(i | 	+	i )R 	–	 	=	0, |
| --- | --- | -------- | ------------ | ----------------- |
|     |     | 1 1      | 1 1 1        | 1 2 2 2           |
em	que	usamos	(i 	+	i )	em	vez	de	i 	para	representar	a	corrente	do	ramo	central.	Substituindo	os	valores	dados	e	simplificando,
1 2 3
obtemos
Malha	da	direita: 	Para	aplicar	a	regra	das	malhas	pela	segunda	vez,	escolhemos	arbitrariamente	percorrer	a	malha	da
direita	no	sentido	anti-horário	a	partir	do	ponto	b,	o	que	nos	dá
|     |     | –i R 	+	 | 	–	i R 	–	(i | 	+	i )R 	–	 	=	0, |
| --- | --- | -------- | ------------ | ----------------- |
|     |     | 2 1      | 2 2 1        | 1 2 2 2           |
Substituindo	os	valores	dados	e	simplificando,	obtemos
Solução	das	equações: 	Agora	temos	um	sistema	de	duas	equações	(Eqs.	27-27	e	27-28)	e	duas	incógnitas	(i 	e	i ),
1 2
que	podemos	resolver	“à	mão”	(o	que	é	fácil,	nesse	caso)	ou	usando	um	computador.	(Um	dos	métodos	mais	usados	para	resolver
sistemas	de	equações	envolve	o	uso	da	regra	de	Cramer,	apresentada	no	Apêndice	E	para	o	caso	simples	de	um	sistema	de	duas
equações	e	duas	incógnitas.)	O	resultado	é	o	seguinte:
(O	sinal	negativo	mostra	que	o	sentido	escolhido	para	i 	na	Fig.	27-13	está	errado,	mas	a	correção	só	deve	ser	feita	no	final	dos
1
| cálculos.)	Fazendo	i | 	=	−0,50	A	na	Eq.	27-28	e	explicitando	i |     | ,	obtemos |     |
| -------------------- | ---------------------------------------- | --- | --------- | --- |
|                      | 1                                        |     | 2         |     |

De acordo com a Eq. 27-26, temos
i = i + i = –0,50 A + 0,25 A
3 1 2
= –0,25 A.
O sinal positivo de i mostra que o sentido escolhido para a corrente está correto. Por outro lado, os sinais negativos de i e i
2 1 3
mostram que os sentidos escolhidos para as duas correntes estão errados. Assim, depois de executados todos os cálculos,
corrigimos a resposta invertendo as setas que indicam os sentidos de i e i na Fig. 27-13 e escrevendo
1 3
Atenção: A correção do sentido das correntes só deve ser feita depois que todas as correntes tiverem sido calculadas.
27-3 O AMPERÍMETRO E O VOLTÍMETRO
Objetivo do Aprendizado
Depois de ler este módulo, você será capaz de ...
27.26 Saber como funcionam o amperímetro e o voltímetro e qual deve ser a resistência interna desses instrumentos para que
eles indiquem corretamente a grandeza que está sendo medida.
Ideia-Chave
• Três instrumentos muito usados para medir grandezas elétricas são o amperímetro, que mede correntes, o voltímetro, que
mede tensões (diferenças de potencial), e o multímetro, que mede corrente, tensões e resistências.
O Amperímetro e o Voltímetro
O instrumento usado para medir correntes é chamado de amperímetro. Para medir a corrente em um fio,
em geral precisamos desligar ou cortar o fio e introduzir o amperímetro no circuito para que a corrente
passe pelo aparelho. (Na Fig. 27-14, o amperímetro A está sendo usado para medir a corrente i.) É
essencial que a resistência R do amperímetro seja muito menor que todas as outras resistências do
A
circuito; se não for assim, a simples presença do medidor mudará o valor da corrente que se pretende
medir.
O instrumento usado para medir diferenças de potencial é chamado de voltímetro. Para medir a
diferença de potencial entre dois pontos de um circuito, ligamos os terminais do voltímetro a esses
pontos sem desligar nem cortar nenhum fio do circuito. (Na Fig. 27-14, o voltímetro V está sendo usado
para medir a diferença de potencial entre os terminais de R .) É essencial que a resistência R do
1 V
voltímetro seja muito maior que a resistência dos elementos do circuito que estão ligados entre os
mesmos pontos do circuito que o voltímetro. Se não for assim, a simples presença do medidor mudará o

valor da diferença de potencial que se pretende medir.
Existem medidores que, dependendo da posição de uma chave, podem ser usados como um
amperímetro ou como um voltímetro e também, em geral, como um ohmímetro, um aparelho que mede a
resistência do elemento ligado entre seus terminais. Esses instrumentos multifuncionais são chamados de
multímetros.
Figura 27-14 Circuito de uma malha, mostrando como ligar um amperímetro (A) e um voltímetro (V).
27-4 CIRCUITOS RC
Objetivos do Aprendizado
Depois de ler este módulo, você será capaz de ...
27.27 Desenhar diagramas esquemáticos de circuitos RC em que o capacitor está sendo carregado e circuitos RC em que o
capacitor está sendo descarregado.
27.28 Escrever a equação de malha (uma equação diferencial) de um circuito RC em que o capacitor está sendo carregado.
27.29 Escrever a equação de malha (uma equação diferencial) de um circuito RC em que o capacitor está sendo descarregado.
27.30 Saber como varia a carga do capacitor, com o tempo, em um circuito RC.
27.31 Calcular a diferença de potencial do capacitor de um circuito RC a partir da variação, com o tempo, da carga do capacitor.
27.32 Calcular a corrente e a diferença de potencial do resistor de um circuito RC em função do tempo.
27.33 Calcular a constante de tempo capacitiva τ de um circuito RC.
27.34 Calcular a carga e a diferença de potencial do capacitor no instante inicial e após um longo tempo para circuitos RC em
que o capacitor está sendo carregado e circuitos RC em que o capacitor está sendo descarregado.
Ideias-Chave
• Quando uma força eletromotriz é aplicada a um resistor R e a um capacitor C ligados em série, a carga do capacitor aumenta
de acordo com a equação
em que C = q é a carga de equilíbrio (carga final) e RC = τ é a constante de tempo capacitiva do circuito.
0
• Durante a carga do capacitor, a corrente no circuito diminui de acordo com a equação

• Quando um capacitor C se descarrega através de um resistor R, a carga do capacitor diminui de acordo com a equação
• Durante a descarga do capacitor, a corrente no circuito diminui de acordo com a equação
Figura 27-15 Quando a chave S é colocada na posição a, o capacitor é carregado através do resistor. Mais tarde, quando a chave é
colocada na posição b, o capacitor é descarregado através do resistor.
Circuitos RC
Nos módulos anteriores, lidamos apenas com circuitos nos quais as correntes não variavam com o tempo.
Vamos agora iniciar uma discussão de correntes que variam com o tempo.
Carga de um Capacitor
O capacitor de capacitância C da Fig. 27-15 está inicialmente descarregado. Para carregá-lo, podemos
colocar a chave S na posição a. Isso completa um circuito RC série formado por um capacitor, uma fonte
ideal de força eletromotriz e uma resistência R.
Como vimos no Módulo 25-1, no momento em que o circuito é completado, cargas começam a se
mover (surge uma corrente) no circuito. Essa corrente acumula uma carga q cada vez maior nas placas do
capacitor e estabelece uma diferença de potencial V (= q/C) cada vez maior entre as placas do
C
capacitor. Quando a diferença de potencial é igual à diferença de potencial entre os terminais da fonte
(que é igual, por sua vez, à força eletromotriz ), a corrente deixa de circular. De acordo com a Eq. 25-1
(q = CV), a carga de equilíbrio (carga final) do capacitor é igual a C .
Vamos examinar mais de perto o processo de carga do capacitor. Em particular, estamos
interessados em saber como variam com o tempo a carga q, a diferença de potencial V e a corrente i
C
enquanto o capacitor está sendo carregado. Começamos por aplicar a regra das malhas ao circuito,
percorrendo-o no sentido horário a partir do terminal negativo da fonte. Temos

O último termo do lado esquerdo representa a diferença de potencial entre as placas do capacitor. O
termo é negativo porque a placa de cima do capacitor, que está ligada ao terminal positivo da fonte, tem
um potencial mais alto que a placa de baixo; assim, há uma queda de potencial quando passamos da placa
de cima para a placa de baixo do capacitor.
Não podemos resolver imediatamente a Eq. 27-30 porque a equação tem duas variáveis, i e q.
Entretanto, as variáveis não são independentes, pois estão relacionadas pela equação
Combinando as Eqs. 27-30 e 27-31, obtemos
Essa equação diferencial descreve a variação, com o tempo, da carga q no capacitor da Fig. 27-15. Para
resolvê-la, é preciso encontrar a função q(t) que satisfaz a Eq. 27-32 e que também satisfaz a condição de
que o capacitor está inicialmente descarregado, ou seja, de que q = 0 no instante t = 0.
Mais adiante vamos mostrar que a solução da Eq. 27-32 é
(A constante e que aparece na Eq. 27-33 é a base dos logaritmos naturais, 2,718 ..., e não a carga
elementar.) Observe que a Eq. 27-33 satisfaz a condição inicial, já que, para t = 0, o termo e−t/RC é igual a
1; portanto, q = 0. Observe também que, quando t tende a infinito (ou seja, após um longo período de
tempo), o termo e−t/RC tende a zero. Isso significa que a equação também prevê corretamente o valor final
da carga do capacitor, q = C . A Fig. 27-16a mostra o gráfico de q(t) em função de t durante a carga do
capacitor.
A derivada de q(t) é a corrente de carga do capacitor:
A Fig. 27-16b mostra o gráfico de i(t) em função de t durante o processo de carga do capacitor. Observe
que o valor inicial da corrente é /R e que a corrente tende a zero quando a carga do capacitor tende para
o valor final.
Um capacitor que está sendo carregado se comporta inicialmente como um fio comum. Após um longo período de tempo, o capacitor
se comporta como um fio partido.

De acordo com as Eqs. 25-1 (q = CV) e 27-33, a diferença de potencial V (t) entre as placas do
C
capacitor durante o processo de carga é dada por
De acordo com a Eq. 27-35, V = 0 no instante t = 0, em que o capacitor está totalmente descarregado, e
C
V = quando t → ∞ e a carga do capacitor tende para o valor final.
C
A Constante de Tempo
O produto RC que aparece nas Eqs. 27-33 a 27-35 tem dimensão de tempo (tanto porque o argumento de
uma exponencial deve ser adimensional como porque 1,0 Ω × 1,0 F = 1,0 s). O produto RC é chamado de
constante de tempo capacitiva do circuito e representado pela letra grega τ:
De acordo com a Eq. 27-33, no instante t = τ (= RC), a carga do capacitor inicialmente descarregado da
Fig. 27-15 aumentou de zero para
Em palavras, durante a primeira constante de tempo τ a carga aumentou de zero para 63% do valor final
C . Na Fig. 27-16, os triângulos no eixo dos tempos assinalam intervalos sucessivos de uma constante de
tempo durante a carga do capacitor. Os tempos de carga dos circuitos RC são frequentemente expressos
em termos de τ; quanto maior o valor de τ, maior o tempo necessário para carregar um capacitor.

Figura 27-16 (a) Gráfico da Eq. 27-33, que mostra a carga do capacitor da Fig. 27-15 em função do tempo. (b) Gráfico da Eq. 27-34, que
mostra a corrente de carga no circuito da Fig. 27-15 em função do tempo. As curvas foram plotadas para R = 2000 τ, C = 1 μF e = 10 V; os
triângulos representam intervalos sucessivos de uma constante de tempo τ.
Descarga de um Capacitor
Suponha agora que o capacitor da Fig. 27-15 esteja totalmente carregado, ou seja, com um potencial V
0
igual à força eletromotriz da fonte. Em um novo instante t = 0, a chave S é deslocada da posição a para
a posição b, fazendo com que o capacitor comece a se descarregar através da resistência R. Nesse caso,
como variam com o tempo a carga q do capacitor e a corrente i no circuito?
A equação diferencial que descreve a variação de q com o tempo é semelhante à Eq. 27-32, exceto
pelo fato de que agora, como a fonte não está mais no circuito, = 0. Assim,
A solução dessa equação diferencial é
em que q (= CV ) é a carga inicial do capacitor. O leitor pode verificar, por substituição, que a Eq. 27-39
0
é realmente uma solução da Eq. 27-38.
De acordo com a Eq. 27-39, a carga q diminui exponencialmente com o tempo, a uma taxa que
depende da constante de tempo capacitiva τ = RC. No instante t = τ, a carga do capacitor diminuiu para

q e−1 ou, aproximadamente, 37% do valor inicial. Observe que quanto maior o valor de τ, maior o tempo
0
de descarga.
Derivando a Eq. 27-39, obtemos a corrente i(t):
De acordo com a Eq. 27-40, a corrente também diminui exponencialmente com o tempo, a uma taxa dada
por τ. A corrente inicial i é igual a q/RC. Note que é possível calcular o valor de i simplesmente
0 0
aplicando a regra das malhas ao circuito no instante t = 0; nesse instante, o potencial inicial do capacitor,
V , está aplicado à resistência R e, portanto, a corrente é dada por i = V /R = (q /C)/R = q /RC. O sinal
0 0 0 0 0
negativo da Eq. 27-40 pode ser ignorado; significa simplesmente que, a partir do instante t = 0, a carga q
do capacitor vai diminuir.
Demonstração da Eq. 27-33
Para resolver a Eq. 27-32, dividimos todos os termos por R, o que nos dá
A solução geral da Eq. 27-41 é da forma
em que q é uma solução particular da equação diferencial, K é uma constante a ser determinada a partir
p
das condições iniciais e a = 1/RC é o coeficiente de q na Eq. 27-41. Para determinar q , fazemos dq/dt =
p
0 na Eq. 27-41 (o que corresponde à situação final de equilíbrio), fazemos q = q e resolvemos a
p
equação, obtendo
Para determinar K, primeiro substituímos a Eq. 27-43 na Eq. 27-42 para obter
q = C + Ke .
–at
Em seguida, usando a condição inicial q = 0 no instante t = 0, obtemos
0 = C + K,
ou K = −C . Finalmente, com os valores de q , a e K inseridos, a Eq. 27-42 se torna
p
q = C – C e ,
–t/RC

que é equivalente à Eq. 27-33.
Teste 5
A tabela mostra quatro conjuntos de valores para os componentes do circuito da Fig. 27-15. Coloque os conjuntos em ordem
decrescente de acordo (a) com a corrente inicial (com a chave na posição a) e (b) com o tempo necessário para que a corrente
diminua para metade do valor inicial.
1 2 3 4
(V) 12 12 10 10
R(Ω) 2 3 10 5
C(μF) 3 2 0,5 2
Exemplo 27.05 Descarga de um circuito RC para evitar um incêndio em uma parada para reabastecimento
Quando um carro está em movimento, elétrons passam do piso para os pneus e dos pneus para a carroceria. O carro armazena essa
carga em excesso como se a carroceria fosse uma das placas de um capacitor, e o piso fosse a outra placa (Fig. 27-17a). Quando o
carro para, ele descarrega o excesso de carga através dos pneus, da mesma forma como um capacitor se descarrega através de um
resistor. Se um objeto condutor se aproxima do carro antes que este esteja totalmente descarregado, a diferença de potencial
associada ao excesso de cargas pode produzir uma centelha entre o carro e o objeto. Suponha que o objeto condutor seja o bico de
uma mangueira de combustível. Nesse caso, a centelha inflamará o combustível, produzindo um incêndio, se a energia da
centelha exceder o valor crítico U = 50 mJ.
fogo
Quando o carro da Fig. 27-17a para no instante t = 0, a diferença de potencial entre o carro e o piso é V = 30 kV. A
0
capacitância do sistema carro-piso é C = 500 pF, e a resistência de cada pneu é R = 100 GΩ. Quanto tempo é preciso para que a
pneu
energia associada às cargas do carro caia abaixo do valor crítico U ?
fogo
IDEIAS-CHAVE
(1) Em qualquer instante t, a energia potencial elétrica U de um capacitor está relacionada à carga armazenada q pela Eq. 25-21 (U
= q2/2C). (2) Quando um capacitor está se descarregando, a carga diminui com o tempo, de acordo com a Eq. 27-39 (q = q e−t/RC).
0
Cálculos: Podemos tratar os pneus como resistores com uma extremidade em contato com a carroceria do carro e a outra
extremidade em contato com o piso. A Fig. 27-17b mostra os quatro resistores ligados em paralelo com a capacitância do carro, e
a Fig. 27-17c mostra a resistência equivalente R dos quatro resistores. De acordo com a Eq. 27-24, a resistência R é dada por

Figura 27-17 (a) Um carro eletricamente carregado e o piso se comportam como um capacitor
que pode se descarregar através dos pneus. (b) Circuito usado para modelar o capacitor carro-piso,
com as resistências dos quatro pneus R ligadas em paralelo. (c) A resistência equivalente R dos
pneu
pneus. (d) A energia potencial elétrica U do capacitor carro–piso diminui durante a descarga.
Quando o carro para, a carga em excesso é descarregada através da resistência R.
Vamos agora usar as duas Ideias-Chave para analisar a descarga. Substituindo a Eq. 27-39 na Eq. 25-21, obtemos
De acordo com a Eq. 25-1 (q = CV), podemos relacionar a carga inicial q do carro à diferença de potencial V : q = CV .
0 0 0 0
Substituindo essa equação na Eq. 27-45, obtemos

Tomando o logaritmo natural de ambos os membros, obtemos
Substituindo os valores conhecidos, descobrimos que o tempo que o carro leva para se descarregar até a energia U = 50 mJ é
fogo
Conclusão: Nas condições descritas neste exemplo, seria recomendável esperar pelo menos 9,4 s para começar a
abastecer o automóvel. Como esse tempo de espera é inaceitável durante uma corrida, a borracha dos pneus dos carros de corrida
é misturada com um material condutor (negro de fumo, por exemplo) para diminuir a resistência dos pneus e reduzir o tempo de
descarga. A Fig. 27-17d mostra a energia armazenada U em função do tempo t para resistências de 100 GΩ (o valor usado nos
cálculos) e 10 GΩ. Note que a energia chega muito mais depressa ao nível seguro U quando a resistência é reduzida para 10
fogo
GΩ.1
Revisão e Resumo
Força Eletromotriz Uma fonte de tensão realiza um trabalho sobre cargas elétricas para manter uma
diferença de potencial entre os terminais. Se dW é o trabalho realizado pela fonte para transportar uma
carga positiva dq do terminal negativo para o terminal positivo, a força eletromotriz (trabalho por
unidade de carga) da fonte é dada por
A unidade de força eletromotriz e de diferença de potencial no SI é o volt. Uma fonte de tensão ideal
não possui resistência interna; a diferença de potencial entre os terminais de uma fonte ideal é igual à
força eletromotriz. Uma fonte de tensão real possui resistência interna; a diferença de potencial entre os

terminais de uma fonte real é igual à força eletromotriz apenas quando a corrente que a atravessa é zero.
Análise de Circuitos A variação de potencial quando atravessamos uma resistência R no sentido da
corrente é −iR; a variação quando atravessamos a resistência no sentido oposto é +iR (regra das
resistências). A variação de potencial quando atravessamos uma fonte de tensão ideal do terminal
negativo para o terminal positivo é + ; a variação quando atravessamos a fonte no sentido oposto é −
(regra das fontes). A lei de conservação da energia leva à regra das malhas:
Regra das Malhas A soma algébrica das variações de potencial encontradas ao longo de uma malha
completa de um circuito é zero.
A lei de conservação das cargas leva à regra dos nós:
Regra dos Nós A soma das correntes que entram em um nó é igual à soma das correntes que saem
do nó.
Circuitos com uma Malha A corrente em um circuito com uma malha que contém uma única
resistência R e uma fonte de tensão de força eletromotriz e resistência r é dada por
que se reduz a i = /R para uma fonte ideal, ou seja, para uma fonte com r = 0.
Potência Quando uma fonte de tensão real de força eletromotriz e resistência r realiza trabalho sobre
portadores de carga, fazendo uma corrente i atravessar a fonte, a potência P transferida para os
portadores de carga é dada por
em que V é a diferença de potencial entre os terminais da fonte. A potência P dissipada na fonte é dada
r
por
A potência P fornecida pela fonte é dada por
fonte
Resistências em Série Quando duas ou mais resistências estão ligadas em série, todas são
percorridas pela mesma corrente. Resistências em série podem ser substituídas por uma resistência
equivalente dada por
Resistências em Paralelo Quando duas ou mais resistências estão ligadas em paralelo, todas são

submetidas à mesma diferença de potencial. Resistências em paralelo podem ser substituídas por uma
resistência equivalente dada por
Circuitos RC Quando uma força eletromotriz é aplicada a uma resistência R e uma capacitância C
em série, como na Fig. 27-15 com a chave na posição a, a carga do capacitor aumenta com o tempo de
acordo com a equação
em que C = q é a carga de equilíbrio (carga final) e RC = τ é a constante de tempo capacitiva do
0
circuito. Durante a carga do capacitor, a corrente é dada por
Quando um capacitor se descarrega através de uma resistência R, a carga do capacitor diminui com o
tempo de acordo com a equação
Durante a descarga do capacitor, a corrente é dada por
Perguntas
1 (a) Na Fig. 27-18a, com R > R , a diferença de potencial entre os terminais de R é maior, menor ou
1 2 2
igual à diferença de potencial entre os terminais de R ? (b) A corrente no resistor R é maior, menor ou
1 2
igual à corrente no resistor R ?
1
2 (a) Na Fig. 27-18a, os resistores R e R estão em série? (b) Os resistores R e R estão em paralelo?
1 3 1 2
(c) Coloque os quatro circuitos da Fig. 27-18 na ordem decrescente das resistências equivalentes.

Figura 27-18 Perguntas 1 e 2.
3 Os resistores R e R , com R > R , são ligados a uma fonte, primeiro separadamente, depois em série
1 2 1 2
e finalmente em paralelo. Coloque esses arranjos na ordem decrescente da corrente que atravessa a fonte.
4 Na Fig. 27-19, um circuito é formado por uma fonte e dois resistores uniformes; a parte do circuito ao
longo do eixo x é dividida em cinco segmentos iguais. (a) Suponha que R = R e coloque os segmentos na
1 2
ordem decrescente do módulo do campo elétrico médio no interior do segmento. (b) Repita o item (a)
supondo que R > R . (c) Qual é o sentido do campo elétrico ao longo do eixo x?
1 2
Figura 27-19 Pergunta 4.
5 Para cada circuito da Fig. 27-20, responda se os resistores estão ligados em série, em paralelo, ou
nem em série nem em paralelo.
Figura 27-20 Pergunta 5.
6 Labirinto de resistores. Na Fig. 27-21, todos os resistores têm uma resistência de 4,0 Ω e todas as
fontes (ideais) têm uma força eletromotriz de 4,0 V. Qual é a corrente no resistor R? (Se o leitor souber
escolher a malha apropriada, poderá responder à pergunta, de cabeça, em poucos segundos.)

Figura 27-21 Pergunta 6.
7 Inicialmente, um único resistor R é ligado a uma fonte ideal. Em seguida, o resistor R é ligado em
1 2
série com R . Quando o resistor R é introduzido no circuito, (a) a diferença de potencial entre os
1 2
terminais de R aumenta, diminui ou permanece a mesma? (b) A corrente em R aumenta, diminui ou
1 1
permanece a mesma? (c) A resistência equivalente R de R e R é maior, menor ou igual a R ?
12 1 2 1
8 Qual é a resistência equivalente de três resistores, todos de resistência R, se forem ligados a uma
fonte ideal (a) em série e (b) em paralelo? (c) A diferença de potencial da associação dos resistores em
série é maior, menor ou igual à diferença de potencial da associação dos resistores em paralelo?
9 Dois resistores são ligados a uma fonte. (a) Em que tipo de associação, em série ou em paralelo, as
diferenças de potencial dos resistores e da associação de resistores são iguais? (b) Em que tipo de
associação as correntes nos resistores e na resistência equivalente são iguais?
10 Labirinto de capacitores. Na Fig. 27-22, todos os capacitores têm uma capacitância de 6,0 μF, e
todas as fontes têm uma força eletromotriz de 10 V. Qual é a carga do capacitor C? (Se o leitor souber
escolher a malha apropriada, poderá responder à pergunta, de cabeça, em poucos segundos.)
Figura 27-22 Pergunta 10.
11 Inicialmente, um único resistor R é ligado a uma fonte ideal. Em seguida, o resistor R é ligado em
1 2
paralelo com R . Quando o resistor R é introduzido no circuito, (a) a diferença de potencial entre os
1 2

terminais de R aumenta, diminui ou permanece a mesma? (b) A corrente em R aumenta, diminui ou
1 1
permanece a mesma? (c) A resistência equivalente R de R e R é maior, menor ou igual a R ? (d) A
12 1 2 1
corrente total em R e R juntos é maior, menor ou igual à corrente em R antes da introdução de R ?
1 2 1 2
12 Quando a chave da Fig. 27-15 é colocada na posição a, uma corrente i passa a atravessar a
resistência R. A Fig. 27-23 mostra a corrente i em função do tempo para quatro conjuntos de valores de R
e da capacitância C: (1) R e C , (2) 2R e C , (3) R e 2C , (4) 2R e 2C . Qual é a curva correspondente
0 0 0 0 0 0 0 0
a cada conjunto?
Figura 27-23 Pergunta 12.
13 A Fig. 27-24 mostra três conjuntos de componentes que podem ser ligados alternadamente à mesma
fonte por meio de uma chave como a da Fig. 27-15. Os resistores e capacitores são todos iguais. Coloque
os conjuntos na ordem decrescente (a) da carga final do capacitor e (b) do tempo necessário para a carga
do capacitor atingir metade da carga final.
Figura 27-24 Pergunta 13.
Problemas
. - ... O número de pontos indica o grau de dificuldade do problema.

Informações adicionais disponíveis em O Circo Voador da Física de Jearl Walker, LTC, Rio de Janeiro, 2008.
Módulo 27-1 Circuitos de uma Malha
·1 Na Fig. 27-25, as fontes ideais têm forças eletromotrizes = 12 V e = 6,0 V e os resistores têm
1 2
resistências R = 4,0 Ω e R = 8,0 Ω. Determine (a) a corrente no circuito, (b) a potência dissipada no
1 2
resistor 1, (c) a potência dissipada no resistor 2, (d) a potência fornecida pela fonte 1 e (e) a potência
fornecida pela fonte 2. (f) A fonte 1 está fornecendo ou recebendo energia? (g) A fonte 2 está fornecendo
ou recebendo energia?
Figura 27-25 Problema 1.
·2 Na Fig. 27-26, as fontes ideais têm forças eletromotrizes = 150 V e = 50 V e os resistores têm
1 2
resistências R = 3,0 Ω e R = 2,0 Ω. Se o potencial no ponto P é tomado como 100 V, qual é o potencial
1 2
no ponto Q?
Figura 27-26 Problema 2.
·3 Uma bateria de automóvel com uma força eletromotriz de 12 V e uma resistência interna de 0,040 Ω
está sendo carregada com uma corrente de 50 A. Determine (a) a diferença de potencial V entre os
terminais da bateria, (b) a potência P dissipada no interior da bateria e (c) a potência P fornecida pela
r fem
bateria. Se a bateria depois de carregada é usada para fornecer 50 A ao motor de arranque, determine (d)
V e (e) P .
r
·4 A Fig. 27-27 mostra um conjunto de quatro resistores que faz parte de um circuito maior. O gráfico
abaixo do circuito mostra o potencial elétrico V(x) em função da posição x ao longo do ramo inferior do
conjunto, do qual faz parte o resistor 4; o potencial V é 12,0 V. O gráfico acima do circuito mostra o
A
potencial elétrico V(x) em função da posição x ao longo do ramo superior do conjunto, do qual fazem
parte os resistores 1, 2 e 3; as diferenças de potencial são ΔV = 2,00 V e ΔV = 5,00 V. O resistor 3 tem
B C
uma resistência de 200 Ω. Determine a resistência (a) do resistor 1 e (b) do resistor 2.

·5 Uma corrente de 5,0 A é estabelecida de um circuito durante 6,0 min por uma bateria recarregável
com uma força eletromotriz de 6,0 V. Qual é a redução da energia química da bateria?
Figura 27-27 Problema 4.
·6 Uma pilha comum de lanterna pode fornecer uma energia da ordem de 2,0 W·h antes de se esgotar.
(a) Se uma pilha custa R$ 0,80, quanto custa manter acesa uma lâmpada de 100 W durante 8,0 h usando
pilhas? (b) Quanto custa manter acesa a mesma lâmpada usando a eletricidade da tomada se o preço da
energia elétrica é R$ 0,06 por quilowatt-hora?
·7 Um fio com uma resistência de 5,0 Ω é ligado a uma bateria cuja força eletromotriz é 2,0 V e cuja
resistência interna é 1,0 Ω. Em 2,0 min, (a) qual é a energia química consumida pela bateria? (b) Qual é a
energia dissipada pelo fio? (c) Qual é a energia dissipada pela bateria?
·8 Uma bateria de automóvel com uma força eletromotriz de 12,0 V tem uma carga inicial de 120 A·h.
Supondo que a diferença de potencial entre os terminais permanece constante até a bateria se descarregar
totalmente, durante quantas horas a bateria é capaz de fornecer uma potência de 100 W?
·9 (a) Qual é o trabalho, em elétrons-volts, realizado por uma fonte ideal de 12 V sobre um elétron que
passa do terminal positivo da fonte para o terminal negativo? (b) Se 3,40 × 1018 elétrons passam pela
fonte por segundo, qual é a potência da fonte em watts?
··10 (a) Na Fig. 27-28, qual deve ser o valor de R para que a corrente no circuito seja 1,0 mA? Sabe-se
que = 2,0 V, = 3,0 V, r = r = 3,0 Ω. (b) Qual é a potência dissipada em R?
1 2 1 2

Figura 27-28 Problema 10.
··11 Na Fig. 27-29, o trecho AB do circuito dissipa uma potência de 50 W quando a corrente i = 1,0 A
tem o sentido indicado. O valor da resistência R é 2,0 Ω. (a) Qual é a diferença de potencial entre A e B?
O dispositivo X não possui resistência interna. (b) Qual é a força eletromotriz do dispositivo X? (c) O
ponto B está ligado ao terminal positivo ou ao terminal negativo do dispositivo X?
Figura 27-29 Problema 11.
··12 A Fig. 27-30 mostra um resistor de resistência R = 6,00 Ω ligado a uma fonte ideal de força
eletromotriz = 12,0 V por meio de dois fios de cobre. Cada fio tem 20,0 cm de comprimento e 1,00 mm
de raio. Neste capítulo, desprezamos a resistência dos fios de ligação. Verifique se a aproximação é
válida para o circuito da Fig. 27-30, determinando (a) a diferença de potencial entre as extremidades do
resistor, (b) a diferença de potencial entre as extremidades de um dos fios, (c) a potência dissipada no
resistor e (d) a potência dissipada em um dos fios.
Figura 27-30 Problema 12.
··13 Um cabo subterrâneo, de 10 km de comprimento, está orientado na direção leste-oeste e é formado
por dois fios paralelos, ambos com uma resistência de 13 Ω/km. Um defeito no cabo faz com que surja
uma resistência efetiva R entre os fios a uma distância x da extremidade oeste (Fig. 27-31). Com isso, a
resistência total dos fios passa a ser 100 Ω, quando a medida é realizada na extremidade leste, e 200 Ω
quando a medida é realizada na extremidade oeste. Determine (a) o valor de x e (b) o valor de R.
Figura 27-31 Problema 13.
··14 Na Fig. 27-32a, as duas fontes têm uma força eletromotriz = 1,20 V, e a resistência externa R é
um resistor variável. A Fig. 27-32b mostra as diferenças de potencial V entre os terminais das duas fontes
em função de R: A curva 1 corresponde à fonte 1, e a curva 2 corresponde à fonte 2. A escala horizontal é

definida	por	R 	=	0,20	Ω.	Determine	(a)	a	resistência	interna	da	fonte	1	e	(b)	a	resistência	interna	da	fonte
s
2.
| Figura	27-32 | 	Problema	14. |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- |
··15			A	corrente	em	um	circuito	com	uma	única	malha	e	uma	resistência	R	é	5,0	A.	Quando	uma
resistência	de	2,0	Ω	é	ligada	em	série	com	R,	a	corrente	diminui	para	4,0	A.	Qual	é	o	valor	de	R?
···16			Uma	célula	solar	produz	uma	diferença	de	potencial	de	0,10	V,	quando	um	resistor	de	500	Ω	é
ligado	a	seus	terminais,	e	uma	diferença	de	potencial	de	0,15	V,	quando	o	valor	do	resistor	é	1000	Ω.
Determine	(a)	a	resistência	interna	e	(b)	a	força	eletromotriz	da	célula	solar.	(c)	A	área	da	célula	é	5,0
cm2	e	a	potência	luminosa	recebida	é	2,0	mW/cm2.	Qual	é	a	eficiência	da	célula	ao	converter	energia
luminosa	em	energia	térmica	fornecida	ao	resistor	de	1000	Ω?
···17			Na	Fig.	27-33,	a	fonte	1	tem	uma	força	eletromotriz	 	=	12,0	V	e	uma	resistência	interna	r 	=
|     |     |     | 1   |     | 1   |
| --- | --- | --- | --- | --- | --- |
0,016	Ω,	e	a	fonte	2	tem	uma	força	eletromotriz	 	=	12,0	V	e	uma	resistência	interna	r 	=	0,012	Ω.	As
|     |     | 2   |     | 2   |     |
| --- | --- | --- | --- | --- | --- |
fontes	são	ligadas	em	série	com	uma	resistência	externa	R.	(a)	Qual	é	o	valor	de	R	para	o	qual	a
diferença	de	potencial	entre	os	terminais	de	uma	das	fontes	é	zero?	(b)	Com	qual	das	duas	fontes	isso
acontece?
| Figura	27-33 | 	Problema	17. |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- |
Módulo	27-2				Circuitos	com	Mais	de	uma	Malha
·18				Na	Fig.	27-9,	determine	a	diferença	de	potencial	V 	–	V 	entre	os	pontos	d	e	c	se	 	=	4,0	V,	 	=	1,0
|           |            |                             | d c | 1   | 2   |
| --------- | ---------- | --------------------------- | --- | --- | --- |
| V,	R 	=	R | 	=	10	Ω,	R | 	=	5,0	Ω	e	a	fonte	é	ideal. |     |     |     |
| 1         | 2          | 3                           |     |     |     |
·19			Pretende-se	obter	uma	resistência	total	de	3,00	Ω	ligando	uma	resistência	de	valor	desconhecido	a
uma	 resistência	 de	 12,0	 Ω.	 (a)	 Qual	 deve	 ser	 o	 valor	 da	 resistência	 desconhecida?	 (b)	 As	 duas
resistências	devem	ser	ligadas	em	série	ou	em	paralelo?

·20 Quando duas resistências 1 e 2 são ligadas em série, a resistência equivalente é 16,0 Ω. Quando são
ligadas em paralelo, a resistência equivalente é 3,0 Ω. Determine (a) a menor e (b) a maior das duas
resistências.
·21 Quatro resistores de 18,0 Ω são ligados em paralelo a uma fonte ideal de 25,0 V. Qual é a corrente
na fonte?
·22 A Fig. 27-34 mostra cinco resistores de 5,00 Ω. Determine a resistência equivalente (a) entre os
pontos F e H e (b) entre os pontos F e G. (Sugestão: Para cada par de pontos, imagine que existe uma
fonte ligada entre os dois pontos.)
Figura 27-34 Problema 22.
·23 Na Fig. 27-35, R = 100 Ω, R = 50 Ω e as fontes ideais têm forças eletromotrizes = 6,0 V, =
1 2 1 2
5,0 V e = 4,0 V. Determine (a) a corrente no resistor 1, (b) a corrente no resistor 2 e (c) a diferença de
3
potencial entre os pontos a e b.
Figura 27-35 Problema 23.
·24 Na Fig. 27-36, R = R = 4,00 Ω e R = 2,50 Ω. Determine a resistência equivalente entre os pontos
1 2 3
D e E. (Sugestão: Imagine que existe uma fonte ligada entre os dois pontos.)
Figura 27-36 Problema 24.
·25 Nove fios de cobre de comprimento ℓ e diâmetro d são ligados em paralelo para formar um cabo de
resistência R. Qual deve ser o diâmetro D de um fio de cobre de comprimento ℓ para que a resistência do

fio seja a mesma do cabo?
··26 A Fig. 27-37 mostra uma fonte ligada a um resistor uniforme R . Um contato deslizante pode ser
0
deslocado ao longo do resistor do ponto x = 0, à esquerda, até o ponto x = 10 cm, à direita. O valor da
resistência à esquerda e à direita do contato depende da posição do contato. Determine a potência
dissipada no resistor R em função de x. Plote a função para = 50 V, R = 2000 Ω e R = 100 Ω.
0
Figura 27-37 Problema 26.
··27 Descarga lateral. A Fig. 27-28 ilustra uma das razões pelas quais é perigoso se abrigar
debaixo de uma árvore durante uma tempestade elétrica. Se um relâmpago atinge a árvore, parte da
descarga pode passar para a pessoa, especialmente se a corrente que atravessa a árvore atingir uma
região seca da casca e por isso tiver que atravessar o ar para chegar ao solo. Na figura, parte do
relâmpago atravessa uma distância d no ar e chega ao solo por meio da pessoa (que possui uma
resistência desprezível em comparação com a do ar). O resto da corrente viaja pelo ar paralelamente ao
tronco da árvore, percorrendo uma distância h. Se d/h = 0,400 e a corrente total é I = 5000 A, qual é o
valor da corrente que atravessa a pessoa?
Figura 27-38 Problema 27.
··28 A fonte ideal da Fig. 27-39a tem uma força eletromotriz = 6,0 V. A curva 1 da Fig. 27-39b mostra
a diferença de potencial V entre os terminais do resistor 1 em função da corrente i no resistor. A escala
do eixo vertical é definida por V = 18,0 V, e a escala do eixo horizontal é definida por i = 3,00 mA. As
s s
curvas 2 e 3 são gráficos semelhantes para os resistores 2 e 3. Qual é a corrente no resistor 2?

Figura 27-39 Problema 28.
··29 Na Fig. 27-40, R = 6,00 Ω, R = 18,0 Ω e a força eletromotriz da fonte ideal é = 12,0 V.
1 2
Determine (a) o valor absoluto e (b) o sentido (para a esquerda ou para a direita) da corrente i . (c) Qual
1
é a energia total dissipada nos quatro resistores em 1,00 min?
Figura 27-40 Problema 29.
··30 Na Fig. 27-41, as fontes ideais têm forças eletromotrizes = 10,0 V e = 0,500 , e todas as
1 2 1
resistências são de 4,00 Ω. Determine a corrente (a) na resistência 2 e (b) na resistência 3.
Figura 27-41 Problemas 30, 41 e 88.
··31 Na Fig. 27-42, as forças eletromotrizes das fontes ideais são = 5,0 V e = 12 V, as resistências
1 2
são de 2,0 Ω e o potencial é tomado como zero no ponto do circuito ligado à terra. Determine os
potenciais (a) V e (b) V nos pontos indicados.
1 2

| Figura	27-42 | 	Problema	31. |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- | --- | --- |
··32				As	duas	fontes	da	Fig.	27-43a	são	ideais.	A	força	eletromotriz	 	da	fonte	1	tem	um	valor	fixo,	mas
1
a	força	eletromotriz	 	da	fonte	2	pode	assumir	qualquer	valor	entre	1,0	V	e	10	V.	Os	gráficos	da	Fig.	27-
2
43b	mostram	as	correntes	nas	duas	fontes	em	função	de	 .	A	escala	vertical	é	definida	por	i 	=	0,20	A.
2 s
Não	se	sabe	de	antemão	que	curva	corresponde	à	fonte	1	e	que	curva	corresponde	à	fonte	2,	mas,	para	as
duas	curvas,	a	corrente	é	considerada	negativa	quando	o	sentido	da	corrente	é	do	terminal	positivo	para	o
terminal	negativo	da	bateria.	Determine	(a)	o	valor	de	 ,	(b)	o	valor	de	R 	e	(c)	o	valor	de	R .
|     |     |     |     | 1   | 1   | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Figura	27-43
	Problema	32.
··33				Na	Fig.	27-44,	a	corrente	na	resistência	6	é	i 	=	1,40	A	e	as	resistências	são	R 	=	R 	=	R 	=	2,00
|     |     |     |     | 6   |     | 1 2 | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- |
Ω,	R 	=	16,0	Ω,	R 	=	8,00	Ω	e	R 	=	4,00	Ω.	Qual	é	a	força	eletromotriz	da	fonte	ideal?
| 4            | 5             | 6   |     |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- | --- | --- |
| Figura	27-44 | 	Problema	33. |     |     |     |     |     |     |
··34			As	resistências	das	Figs.	27-45a	e	27-45b	são	todas	de	6,0	Ω	e	as	fontes	ideais	são	baterias	de	12
V.	(a)	Quando	a	chave	S	da	Fig.	27-45a	é	fechada,	qual	é	a	variação	da	diferença	de	potencial	V 	entre	os
1
terminais	do	resistor	1?	(b)	Quando	a	chave	S	da	Fig.	27-45b	é	fechada,	qual	é	a	variação	da	diferença
| de	potencial	V | 	entre	os	terminais	do	resistor	1? |     |     |     |     |     |     |
| -------------- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
1
| Figura	27-45 | 	Problema	34. |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- | --- | --- |
··35				Na	Fig.	27-46,	 	=	12,0	V,	R 	=	2000	Ω,	R 	=	3000	Ω	e	R 	=	4000	Ω.	Determine	as	diferenças	de
|     |     | 1   |     | 2   | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
potencial	(a)	V 	−	V ,	(b)	V 	−	V ,	(c)	V 	−	V 	e	(d)	V 	−	V .
|     | A B | B C | C D | A C |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

Figura 27-46 Problema 35.
··36 Na Fig. 27-47, = 6,00 V, = 12,0 V, R = 100 Ω, R = 200 Ω e R = 300 Ω. Um ponto do circuito
1 2 1 2 3
está ligado à terra (V = 0). Determine (a) o valor absoluto e (b) o sentido (para cima ou para baixo) da
corrente na resistência 1, (c) o valor absoluto e (d) o sentido (para a esquerda ou para a direita) da
corrente na resistência 2, (e) o valor absoluto e (f) o sentido (para a esquerda ou para a direita) da
corrente na resistência 3. (g) Determine o potencial elétrico no ponto A.
Figura 27-47 Problema 36.
··37 Na Fig. 27-48, R = 2,00 Ω, R = 5,00 Ω e a fonte é ideal. Qual é o valor de R que maximiza a
1 2 3
potência dissipada na resistência 3?
Figura 27-48 Problemas 37 e 98.
··38 A Fig. 27-49 mostra uma parte de um circuito. As resistências são R = 2,0 Ω, R = 4,0 Ω e R =
1 2 3
6,0 Ω e a corrente indicada é i = 6,0 A. A diferença de potencial entre os pontos A e B que ligam o
conjunto ao resto do circuito é V − V = 78 V. (a) O elemento representado como “?” está absorvendo
A B
energia do circuito ou cedendo energia ao circuito? (b) Qual é a potência absorvida ou fornecida pelo
elemento desconhecido?

Figura 27-49 Problema 38.
··39 Na Fig. 27-50, duas fontes de força eletromotriz = 12,0 V e uma resistência interna r = 0,300 Ω
são ligadas em paralelo com uma resistência R. (a) Para qual valor de R a potência dissipada no resistor
é máxima? (b) Qual é o valor da potência máxima?
Figura 27-50 Problemas 39 e 40.
··40 Duas fontes iguais, de força eletromotriz = 12,0 V e resistência interna r = 0,200 Ω, podem ser
ligadas a uma resistência R em paralelo (Fig. 27-50) ou em série (Fig. 27-51). Se R = 2,00r, qual é a
corrente i na resistência R (a) no caso da ligação em paralelo e (b) no caso da ligação em série? (c) Em
que tipo de ligação a corrente i é maior? Se R = r/2,00, qual é a corrente na resistência R (d) no caso da
ligação em paralelo e (e) no caso da ligação em série? (f) Em que tipo de ligação a corrente i é maior?
Figura 27-51 Problema 40.
··41 Na Fig. 27-41, = 3,00 V, = 1,00 V, R = 4,00 Ω, R = 2,00 Ω, R = 5,00 Ω e as duas fontes são
1 2 1 2 3
ideais. Determine a potência dissipada (a) em R , (b) em R e (c) em R . Determine a potência (d) da
1 2 3
fonte 1 e (e) da fonte 2.
··42 Na Fig. 27-52, um conjunto de n resistores em paralelo é ligado em série a um resistor e a uma
fonte ideal. Todos os resistores têm a mesma resistência. Se outro resistor de mesmo valor fosse ligado
em paralelo com o conjunto, a corrente na fonte sofreria uma variação de 1,25%. Qual é o valor de n?

Figura 27-52 Problema 42.
··43 O leitor dispõe de um suprimento de resistores de 10 Ω, capazes de dissipar no máximo 1,0 W sem
serem inutilizados. Qual é o número mínimo desses resistores que é preciso combinar em série ou em
paralelo para obter uma resistência de 10 Ω capaz de dissipar 5,0 W?
··44 Na Fig. 27-53, R = 100 Ω, R = R = 50,0 Ω, R = 75,0 Ω e a força eletromotriz da fonte ideal é
1 2 3 4
= 6,00 V. (a) Determine a resistência equivalente. Determine a corrente (b) na resistência 1, (c) na
resistência 2, (d) na resistência 3 e (e) na resistência 4.
Figura 27-53 Problemas 44 e 48.
··45 Na Fig. 27-54, as resistências são R = 1,0 Ω e R = 2,0 Ω e as forças eletromotrizes das fontes
1 2
ideais são = 2,0 V, = = 4,0 V. Determine (a) o valor absoluto e (b) o sentido (para cima ou para
1 2 3
baixo) da corrente na fonte 1, (c) o valor absoluto e (d) o sentido da corrente na fonte 2, (e) o valor
absoluto e (f) o sentido da corrente na fonte 3, (g) a diferença de potencial V − V .
a b
Figura 27-54 Problema 45.
··46 Na Fig. 27-55a, o resistor 3 é um resistor variável e a força eletromotriz da fonte ideal é = 12 V.
A Fig. 27-55b mostra a corrente i na fonte em função de R . A escala horizontal é definida por R = 20 Ω.
3 3s
A curva tem uma assíntota de 2,0 mA para R → ∞. Determine (a) a resistência R e (b) a resistência R .
3 1 2
Figura 27-55 Problema 46.

···47 Um fio de cobre de raio a = 0,250 mm tem uma capa de alumínio de raio externo b = 0,380 mm. A
corrente no fio composto é i = 2,00 A. Usando a Tabela 26-1, calcule a corrente (a) no cobre e (b) no
alumínio. (c) Se uma diferença de potencial V = 12,0 V entre as extremidades mantém a corrente, qual é o
comprimento do fio composto?
···48 Na Fig. 27-53, R = 7,00 Ω, R = 12,0 Ω, R = 4,00 Ω e a força eletromotriz da fonte ideal é =
1 2 3
24,0 V. Determine para qual valor de R a potência fornecida pela fonte aos resistores é igual (a) a 60,0
4
W, (b) ao maior valor possível P e (c) ao menor valor possível P . Determine (d) P e (e) P .
máx mín máx mín
Módulo 27-3 O Amperímetro e o Voltímetro
··49 (a) Na Fig. 27-56, determine a leitura do amperímetro para = 5,0 V (fonte ideal), R = 2,0 Ω, R
1 2
= 4,0 Ω e R = 6,0 Ω. (b) Mostre que, se a fonte for colocada na posição do amperímetro e vice-versa, a
3
leitura do amperímetro será a mesma.
Figura 27-56 Problema 49.
··50 Na Fig. 27-57, R = 2,00R, a resistência do amperímetro é desprezível e a fonte é ideal. A corrente
1
no amperímetro corresponde a que múltiplo de /R?
Figura 27-57 Problema 50.
··51 Na Fig. 27-58, um voltímetro de resistência R = 300 Ω e um amperímetro de resistência R = 3,00
V A
Ω estão sendo usados para medir uma resistência R em um circuito que também contém uma resistência
R = 100 Ω e uma fonte ideal de força eletromotriz = 12,0 V. A resistência R é dada por R = V/i, em que
0
V é a diferença de potencial entre os terminais de R, e i é a leitura do amperímetro. A leitura do
voltímetro é V′, que é a soma de V com a diferença de potencial entre os terminais do amperímetro.
Assim, a razão entre as leituras dos dois medidores não é R e sim a resistência aparente R′ = V′/i. Se R =
85,0 Ω, determine (a) a leitura do amperímetro, (b) a leitura do voltímetro e (c) o valor de R′. (d) Se R
A
diminui, a diferença entre R’ e R aumenta, diminui ou permanece a mesma?

Figura 27-58 Problema 51.
··52 Um ohmímetro simples é construído ligando uma pilha de lanterna de 1,50 V em série com uma
resistência R e um amperímetro capaz de medir correntes entre 0 e 1,00 mA, como mostra a Fig. 27-59. A
resistência R é ajustada de tal forma que, quando os fios de prova são encostados um no outro, o ponteiro
mostra o valor de 1,00 mA, que corresponde à deflexão máxima. Determine o valor da resistência externa
que, quando colocada em contato com os fios de prova, provoca uma deflexão do ponteiro do
amperímetro de (a) 10,0%, (b) 50,0% e (c) 90,0% da deflexão máxima. (d) Se o amperímetro tem uma
resistência de 20,0 Ω e a resistência interna da fonte é desprezível, qual é o valor de R?
Figura 27-59 Problema 52.
··53 Na Fig. 27-14, suponha que = 3,0 V, r = 100 Ω, R = 250 Ω e R = 300 Ω. Se a resistência do
1 2
voltímetro R é 5,0 kΩ, que erro percentual o voltímetro introduz na medida da diferença de potencial
V
entre os terminais de R ? Ignore a presença do amperímetro.
1
··54 Quando os faróis de um automóvel são acesos, um amperímetro em série com os faróis indica 10,0
A e um voltímetro em paralelo com os faróis indica 12,0 V (Fig. 27-60). Quando o motor de arranque é
acionado, a leitura do amperímetro cai para 8,00 A e a luz dos faróis fica mais fraca. Se a resistência
interna da bateria é 0,0500 Ω e a resistência interna do amperímetro é desprezível, determine (a) a força
eletromotriz da bateria e (b) a corrente no motor de arranque quando os faróis estão acesos.

Figura 27-60 Problema 54.
··55 Na Fig. 27-61, o valor de R pode ser ajustado com o auxílio de um contato deslizante até que os
s
potenciais dos pontos a e b sejam iguais. (Um teste para verificar se essa condição foi satisfeita é ligar
temporariamente um amperímetro sensível entre os pontos a e b; se os potenciais dos dois pontos forem
iguais, a indicação do amperímetro será zero.) Mostre que, quando esta condição é satisfeita, R =
x
R R /R . Uma resistência desconhecida (R ) pode ser medida em termos de uma resistência de referência
s 2 1 x
(R ) usando esse circuito, conhecido como ponte de Wheatstone.
s
Figura 27-61 Problema 55.
··56 Na Fig. 27-62, um voltímetro de resistência R = 300 Ω e um amperímetro de resistência R = 3,00
V A
Ω estão sendo usados para medir uma resistência R em um circuito que também contém uma resistência
R = 100 Ω e uma fonte ideal de força eletromotriz = 12,0 V. A resistência R é dada por R = V/i, em que
0
V é a leitura do voltímetro e i é a corrente na resistência R. Entretanto, a leitura do amperímetro não é i e
sim i′, que é a soma de i com a corrente no voltímetro. Assim, a razão entre as leituras dos dois
medidores não é R e sim a resistência aparente R′ = V/i′. Se R = 85,0 Ω, determine (a) a leitura do
amperímetro, (b) a leitura do voltímetro e (c) o valor de R′. (d) Se R aumenta, a diferença entre R′ e R
V
aumenta, diminui ou permanece a mesma?
Figura 27-62 Problema 56.
Módulo 27-4 Circuitos RC
·57 A chave S da Fig. 27-63 é fechada no instante t = 0, fazendo com que um capacitor inicialmente
descarregado, de capacitância C = 15,0 μF, comece a se carregar através de um resistor de resistência R

= 20,0 Ω. Em que instante a diferença de potencial entre os terminais do capacitor é igual à diferença de
potencial entre os terminais do resistor?
Figura 27-63 Problemas 57 e 96.
·58 Em um circuito RC série, = 12,0 V, R = 1,40 MΩ e C = 1,80 μF. (a) Calcule a constante de tempo.
(b) Determine a carga máxima que o capacitor pode receber ao ser carregado. (c) Qual é o tempo
necessário para que a carga do capacitor atinja o valor de 16,0 μC?
·59 Que múltiplo da constante de tempo τ é o tempo necessário para que um capacitor inicialmente
descarregado seja carregado com 99,0% da carga final em um circuito RC série?
·60 Um capacitor com uma carga inicial q é descarregado através de um resistor. Que múltiplo da
0
constante de tempo τ é o tempo necessário para que o capacitor descarregue (a) um terço da carga inicial
e (b) dois terços da carga inicial?
·61 Um resistor de 15,0 kΩ e um capacitor são ligados em série, e uma diferença de potencial de 12,0 V
é aplicada bruscamente ao conjunto. A diferença de potencial entre os terminais do capacitor aumenta
para 5,00 V em 1,30 μs. (a) Calcule a constante de tempo do circuito. (b) Determine a capacitância C do
capacitor.
··62 A Fig. 27-64 mostra o circuito de uma lâmpada piscante como as que são usadas nas obras de
estrada. Uma lâmpada fluorescente L (de capacitância desprezível) é ligada em paralelo com o capacitor
C de um circuito RC. Existe uma corrente na lâmpada apenas quando a diferença de potencial aplicada à
lâmpada atinge a tensão de ruptura V ; nesse instante, o capacitor se descarrega totalmente através da
L
lâmpada e a lâmpada fica acesa por alguns instantes. Para uma lâmpada com uma tensão de ruptura V =
L
72,0 V, ligada a uma bateria ideal de 95,0 V e a um capacitor de 0,150 μF, qual deve ser o valor da
resistência R para que a lâmpada pisque duas vezes por segundo?
Figura 27-64 Problema 62.
··63 No circuito da Fig. 27-65, = 1,2 kV, C = 6,5 μF e R = R = R = 0,73 MΩ. Com o capacitor C
1 2 3
totalmente descarregado, a chave S é fechada bruscamente no instante t = 0. Determine, para o instante t =
0, (a) a corrente i no resistor 1, (b) a corrente i no resistor 2 e (c) a corrente i no resistor 3. Determine,
1 2 3

para t → ∞ (ou seja, após várias constantes de tempo), (d) i , (e) i , (f) i . Determine a diferença de
1 2 3
potencial V no resistor 2 (g) em t = 0 e (h) para t → ∞. (i) Faça um esboço do gráfico de V em função
2 2
de t no intervalo entre esses dois instantes extremos.
Figura 27-65 Problema 63.
··64 Um capacitor com uma diferença de potencial inicial de 100 V começa a ser descarregado por
meio de um resistor quando uma chave é fechada no instante t = 0. No instante t = 10,0 s, a diferença de
potencial no capacitor é 1,00 V. (a) Qual é a constante de tempo do circuito? (b) Qual é a diferença de
potencial no capacitor no instante t = 17,0 s?
··65 Na Fig. 27-66, R = 10,0 kΩ, R = 15,0 kΩ, C = 0,400 μF e a bateria ideal tem uma força
1 2
eletromotriz = 20,0 V. Primeiro, a chave é mantida por um longo tempo na posição fechada, até que seja
atingido o regime estacionário. Em seguida, a chave é aberta no instante t = 0. Qual é a corrente no
resistor 2 no instante t = 4,00 ms?
Figura 27-66 Problemas 65 e 99.
··66 A Fig. 27-67 mostra dois circuitos com um capacitor carregado que pode ser descarregado por um
resistor quando uma chave é fechada. Na Fig. 27-67a, R = 20,0 Ω e C = 5,00 μF. Na Fig. 27-67b, R =
1 1 2
10,0 Ω e C = 8,00 μF. A razão entre as cargas iniciais dos dois capacitores é q /q = 1,50. No instante t
2 02 01
= 0, as duas chaves são fechadas. Em que instante t os dois capacitores possuem a mesma carga?
Figura 27-67 Problema 66.
··67 A diferença de potencial entre as placas de um capacitor de 2,0 μF com fuga (o que significa que
há passagem de carga de uma placa para a outra) diminui para um quarto do valor inicial em 2,0 s. Qual é
a resistência equivalente entre as placas do capacitor?

··68 Um capacitor de 1,0 μF com uma energia inicial armazenada de 0,50 J é descarregado através de
um resistor de 1,0 MΩ. (a) Qual é a carga inicial do capacitor? (b) Qual é a corrente no resistor quando a
descarga começa? Escreva expressões que permitam calcular, em função do tempo t, (c) a diferença de
potencial V no capacitor, (d) a diferença de potencial V no resistor e (e) a potência P dissipada pelo
C R R
resistor.
···69 Um resistor de 3,00 MΩ e um capacitor de 1,00 μF são ligados em série com uma fonte ideal de
força eletromotriz = 4,00 V. Depois de transcorrido 1,00 s, determine (a) a taxa de aumento da carga do
capacitor, (b) a taxa de armazenamento de energia no capacitor, (c) a taxa de dissipação de energia no
capacitor e (d) a taxa de fornecimento de energia pela fonte.
Problemas Adicionais
70 Cada uma das seis fontes reais da Fig. 27-68 possui uma força eletromotriz de 20 V e uma
resistência de 4,0 Ω. (a) Qual é a corrente na resistência (externa) R = 4,0 Ω? (b) Qual é a diferença de
potencial entre os terminais de uma das fontes? (c) Qual é a potência fornecida por uma das fontes? (d)
Qual é a potência dissipada na resistência interna de uma das fontes?
Figura 27-68 Problema 70.
71 Na Fig. 27-69, R = 20,0 Ω, R = 10,0 Ω e a força eletromotriz da fonte ideal é = 120 V. Determine
1 2
a corrente no ponto a (a) com apenas a chave S fechada, (b) com apenas as chaves S e S fechadas e (c)
1 1 2
com as três chaves fechadas.
Figura 27-69 Problema 71.
72 Na Fig. 27-70, a força eletromotriz da fonte ideal é = 30,0 V e as resistências são R = R = 14 Ω,
1 2
R = R = R = 6,0 Ω, R = 2,0 Ω e R = 1,5 Ω. Determine (a) i , (b) i , (c) i , (d) i e (e) i .
3 4 5 6 7 2 4 1 3 5

Figura 27-70 Problema 72.
73 Os fios A e B, ambos com 40,0 m de comprimento e 2,60 mm de diâmetro, são ligados em série. Uma
diferença de potencial de 60,0 V é aplicada às extremidades do fio composto. As resistências são R =
A
0,127 Ω e R = 0,729 Ω. Para o fio A, determine (a) o módulo J da densidade de corrente e (b) a
B
diferença de potencial V. (c) De que material é feito o fio A? (Veja a Tabela 26-1.) Para o fio B,
determine (d) J e (e) V. (f) De que material é feito o fio B?
74 Determine (a) o valor absoluto e (b) o sentido (para cima ou para baixo) da corrente i na Fig. 27-
71, em que todas as resistências são de 4,0 Ω e todas as fontes são ideais e têm uma força eletromotriz de
10 V. (Sugestão: O problema pode ser resolvido de cabeça.)
Figura 27-71 Problema 74.
75 Suponha que, enquanto você está sentado em uma cadeira, a separação de cargas entre sua
roupa e a cadeira faz com que seu corpo fique a um potencial de 200 V, com uma capacitância de 150 pF
entre você e a cadeira. Quando você se levanta, o aumento da distância entre seu corpo e a cadeira faz a
capacitância diminuir para 10 pF. (a) Qual é o novo valor do potencial do seu corpo? Esse potencial
diminui com o tempo, pois a carga tende a se escoar pelos sapatos (você é um capacitor que está se
descarregando através de uma resistência). Suponha que a resistência efetiva para a descarga é 300 GΩ.
Se você toca num componente eletrônico enquanto o seu potencial é maior que 100 V, o componente pode

ficar inutilizado. (b) Quanto tempo você deve esperar para que o potencial do seu corpo chegue ao nível
seguro de 100 V?
Se você usar uma pulseira condutora em contato com a terra, seu potencial não aumentará tanto
quando você se levantar; além disso, a descarga será mais rápida, pois a resistência da ligação à terra
será menor que a dos sapatos. (c) Suponha que, no momento em que você se levanta, o potencial do seu
corpo é 1400 V e a capacitância entre o seu corpo e a cadeira é 10 pF. Qual deve ser a resistência entre a
pulseira e a terra para que o seu corpo chegue ao potencial de 100 V em 0,30 s, ou seja, em um tempo
menor que o que você levaria para tocar, por exemplo, em um computador?
76 Na Fig. 27-72, as forças eletromotrizes das fontes ideais são = 20,0 V, = 10,0 V e = 5,00 V, e
1 2 3
as resistências são todas de 2,00 Ω. Determine (a) o valor absoluto e (b) o sentido (para a direita ou para
a esquerda) da corrente i . (c) A fonte 1 fornece ou absorve energia? (d) Qual é a potência fornecida ou
1
absorvida pela fonte 1? (e) A fonte 2 fornece ou absorve energia? (f) Qual é a potência fornecida ou
absorvida pela fonte 2? (g) A fonte 3 fornece ou absorve energia? (h) Qual é a potência fornecida ou
absorvida pela fonte 3?
Figura 27-72 Problema 76.
77 Para fabricar um resistor cuja resistência varia muito pouco com a temperatura, pode-se utilizar uma
combinação em série de um resistor de silício com um resistor de ferro. Se a resistência total desejada é
1000 Ω e a temperatura de referência é 20oC, determine a resistência (a) do resistor de silício e (b) do
resistor de ferro. (Sugestão: Consulte a Tabela 26-1.)
78 Na Fig. 27-14, suponha que = 5,0 V, r = 2,0 Ω, R = 5,0 Ω e R = 4,0 Ω. Se a resistência do
1 2
amperímetro R é 0,10 Ω, que erro percentual essa resistência introduz na medida da corrente? Ignore a
A
presença do voltímetro.
79 Um capacitor C inicialmente descarregado é carregado totalmente por uma fonte de força
eletromotriz constante ligada em série com um resistor R. (a) Mostre que a energia final armazenada no
capacitor é igual à metade da energia fornecida pela fonte. (b) Integrando o produto i2R no intervalo de
carga, mostre que a energia térmica dissipada pelo resistor também é igual à metade da energia fornecida

pela fonte.
80 Na Fig. 27-73, R = 5,00 Ω, R = 10,0 Ω, R = 15,0 Ω, C = 5,00 μF, C = 10,0 μF e a fonte ideal tem
1 2 3 1 2
uma força eletromotriz = 20,0 V. Supondo que o circuito está no regime estacionário, qual é a energia
total armazenada nos dois capacitores?
Figura 27-73 Problema 80.
81 Na Fig. 27-5a, determine a diferença de potencial entre os terminais de R para = 12 V, R = 3,0 Ω,
2 1
R = 4,0 Ω e R = 5,0 Ω.
2 3
82 Na Fig. 27-8a, calcule a diferença de potencial entre a e c considerando o percurso que envolve R,
r e .
1 1
83 O controlador de um jogo de fliperama é formado por um resistor variável em paralelo com um
capacitor de 0,220 μF. O capacitor é carregado com 5,00 V e descarregado pelo resistor. O tempo para
que a diferença de potencial entre as placas do capacitor diminua para 0,800 V é medido por um relógio
que faz parte do jogo. Se a faixa útil de tempos de descarga vai de 10,0 μs a 6,00 ms, determine (a) o
menor valor e (b) o maior valor da resistência do resistor.
84 A Fig. 27-74 mostra o circuito do indicador de combustível usado nos automóveis. O indicador
(instalado no painel) tem uma resistência de 10 Ω. No tanque de gasolina existe uma boia ligada a um
resistor variável cuja resistência varia linearmente com o volume de combustível. A resistência é 140 Ω,
quando o tanque está cheio, e 20 Ω, quando o tanque está vazio. Determine a corrente no circuito (a)
quando o tanque está vazio, (b) quando o tanque está pela metade e (c) quando o tanque está cheio.
Considere a bateria uma fonte ideal.
Figura 27-74 Problema 84.
85 O motor de arranque de um automóvel está girando muito devagar, e o mecânico não sabe se o

problema	está	no	motor,	no	cabo	ou	na	bateria.	De	acordo	com	o	manual,	a	resistência	interna	da	bateria
de	12	V	não	deveria	ser	maior	que	0,020	Ω,	a	resistência	do	motor	não	deveria	ultrapassar	0,200	Ω	e	a
resistência	do	cabo	não	deveria	ser	maior	que	0,040	Ω.	O	mecânico	liga	o	motor	e	mede	11,4	V	entre	os
terminais	da	bateria,	3,0	V	entre	as	extremidades	do	cabo	e	uma	corrente	de	50	A.	Qual	é	o	componente
defeituoso?
86			Dois	resistores,	R 	e	R ,	podem	ser	ligados	em	paralelo	ou	em	série	entre	os	terminais	de	uma	fonte
1 2
ideal	de	força	eletromotriz	 .	Estamos	interessados	em	que	a	potência	dissipada	pela	combinação	dos
resistores	em	paralelo	seja	cinco	vezes	maior	que	a	potência	dissipada	pela	combinação	dos	resistores
em	série.	Se	R 	=	100	Ω,	determine	(a)	o	menor	e	(b)	o	maior	dos	dois	valores	de	R 	que	satisfazem	essa
1 2
condição.
87				O	circuito	da	Fig.	27-75	mostra	um	capacitor,	duas	fontes	ideais,	dois	resistores	e	uma	chave	S.
Inicialmente,	a	chave	S	permaneceu	aberta	por	um	longo	tempo.	Se	a	chave	é	fechada	e	permanece	nesta
posição	por	um	longo	tempo,	qual	é	a	variação	da	carga	do	capacitor?	Suponha	que	C	=	10	μF,	 	=	1,0	V,
1
| 	=	3,0	V,	R  | 	=	0,20	Ω	e	R | 	=	0,40	Ω. |     |     |
| ------------ | ------------- | ---------- | --- | --- |
| 2            | 1             | 2          |     |     |
| Figura	27-75 | 	Problema	87. |            |     |     |
88			Na	Fig.	27-41,	R 	=	10,0	Ω,	R 	=	20,0	Ω	e	as	forças	eletromotrizes	das	fontes	ideais	são	 	=	20,0	V
|     |     | 1   | 2   | 1   |
| --- | --- | --- | --- | --- |
e	 	=	50,0	V.	Qual	deve	ser	o	valor	de	R 	para	que	a	corrente	na	fonte	1	seja	zero?
| 2   |     |     | 3   |     |
| --- | --- | --- | --- | --- |
89				Na	Fig.	27-76,	R	=	10	Ω.	Qual	é	a	resistência	equivalente	entre	os	pontos	A	e	B?	(Sugestão:	Imagine
que	existe	uma	fonte	ligada	entre	os	pontos	A	e	B.)
90			(a)	Na	Fig.	27-4a,	mostre	que	a	potência	dissipada	em	R	é	máxima	para	R	=	r.	(b)	Mostre	que	a
| potência	máxima	é	P	=	 |               | 2/4r. |     |     |
| ---------------------- | ------------- | ----- | --- | --- |
| Figura	27-76           | 	Problema	89. |       |     |     |
91			Na	Fig.	27-77,	as	forças	eletromotrizes	das	fontes	ideais	são	 	=	12,0	V	e	 	=	4,00	V	e	as
1 2

resistências são todas de 4,00 Ω. Determine (a) o valor absoluto de i , (b) o sentido (para cima ou para
1
baixo) de i , (c) o valor absoluto de i e (d) o sentido de i . (e) A fonte 1 fornece ou absorve energia? (f)
1 2 2
Qual é a potência fornecida ou absorvida pela fonte 1? (g) A fonte 2 fornece ou absorve energia? (h)
Qual é a potência fornecida ou absorvida pela fonte 2?
Figura 27-77 Problema 91.
92 A Fig. 27-78 mostra uma parte de um circuito pelo qual está passando uma corrente I = 6,00 A. As
resistências são R = R = 2,00R = 2,00R = 4,00 Ω. Qual é a corrente i no resistor 1?
1 2 3 4 1
Figura 27-78 Problema 92.
93 Pretende-se dissipar uma potência de 10 W em um resistor de 0,10 Ω ligando o resistor a uma fonte
cuja força eletromotriz é 1,5 V. (a) Qual deve ser a diferença de potencial aplicada ao resistor? (b) Qual
deve ser a resistência interna da fonte?
94 A Fig. 27-79 mostra três resistores de 20,0 Ω. Determine a resistência equivalente (a) entre os
pontos A e B, (b) entre os pontos A e C, (c) entre os pontos B e C. (Sugestão: Imagine que existe uma
fonte ligada entre os pontos indicados.)
Figura 27-79 Problema 94.
95 Uma linha de transmissão de 120 V é protegida por um fusível de 15 A. Qual é o número máximo de
lâmpadas de 500 W que podem ser ligadas em paralelo na linha sem queimar o fusível?

96 A Fig. 27-63 mostra uma fonte ideal de força eletromotriz = 12 V, um resistor de resistência R =
4,0 Ω e um capacitor descarregado de capacitância C = 4,0 μF. Se a chave S é fechada, qual é a corrente
no resistor no instante em que a carga do capacitor é 8,0 μC?
97 N fontes iguais de força eletromotriz e resistência interna r podem ser ligadas em série (Fig. 27-80a)
ou em paralelo (Fig. 27-80b) antes que o conjunto seja ligado a uma resistência R. Mostre que a corrente
na resistência R será a mesma nos dois arranjos, se R = r.
Figura 27-80 Problema 97.
98 Na Fig. 27-48, R = R = 10,0 Ω e a força eletromotriz da fonte ideal é = 12,0 V. (a) Qual o valor
1 2
de R que maximiza a potência fornecida pela fonte? (b) Qual o valor da potência máxima?
3
99 Na Fig. 27-66, a força eletromotriz da fonte ideal é = 30 V, as resistências são R = 20 kΩ e R =
1 2
10 kΩ, e o capacitor está descarregado. Determine a corrente (a) na resistência 1 e (b) na resistência 2 no
instante em que a chave é fechada. (c) Depois de transcorrido um longo tempo, qual é a corrente na
resistência 2?
100 Na Fig. 27-81, as forças eletromotrizes das fontes ideais são = 20,0 V, = 10,0 V, = 5,00 V e
1 2 3
= 5,00 V, e todas as resistências são de 2,00 Ω. Determine (a) o valor absoluto e (b) o sentido (para a
4
direita ou para a esquerda) da corrente i e (c) o valor absoluto e (d) o sentido (para a direita ou para a
1
esquerda) da corrente i . (Sugestão: O problema pode ser resolvido de cabeça.) (e) Qual é a potência
2
fornecida ou recebida pela fonte 4? (f) A fonte 4 está fornecendo ou recebendo energia?

| Figura	27-81 	Problema	100. |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- |
101				Na	Fig.	27-82,	uma	fonte	ideal	de	força	eletromotriz	 	=	12,0	V	é	ligada	a	um	circuito	cujas
resistências	são	R 	=	6,00	Ω,	R 	=	12,00	Ω,	R 	=	4,00	Ω,	R 	=	3,00	Ω	e	R 	=	5,00	Ω.	Qual	é	a	diferença
|     | 1   | 2   | 3   | 4   | 5   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
de	potencial	da	resistência	5?
| Figura	27-82 	Problema	101. |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- |
102			A	tabela	a	seguir	mostra	a	diferença	de	potencial	V 	entre	os	terminais	de	uma	fonte	para	vários
T
valores	da	corrente	i	fornecida	pela	fonte.	(a)	Escreva	uma	equação	que	represente	a	relação	entre	V 	e	i
T
e	execute	uma	regressão	linear	em	uma	calculadora,	usando	os	números	da	tabela,	para	determinar	a	reta
de	V 	em	função	de	i	que	melhor	se	ajusta	aos	dados.	Use	os	resultados	do	ajuste	para	calcular	(b)	a	força
T
eletromotriz	da	fonte	e	(c)	a	resistência	interna	da	fonte.
| i(A) | 50,0 | 75,0 | 100  | 125  | 150  | 175  | 200  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| V(V) | 10,7 | 9,00 | 7,70 | 6,00 | 4,80 | 3,00 | 1,70 |
T
103				Na	Fig.	27-83,	 	=	6,00	V,	 	=	12,0	V,	R 	=	200	Ω	e	R 	=	100	Ω.	Determine	(a)	o	valor	absoluto	e
|     | 1   | 2   | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
(b)	o	sentido	(para	cima	ou	para	baixo)	da	corrente	na	resistência	1,	(c)	o	valor	absoluto	e	(d)	o	sentido
(para	a	direita	ou	para	a	esquerda)	da	corrente	na	resistência	2	e	(e)	o	valor	absoluto	e	(f)	o	sentido	(para
cima	ou	para	baixo)	da	corrente	na	fonte	2.

Figura 27-83 Problema 103.
104 Uma lâmpada de 120 V com dois filamentos pode operar em três níveis de potência: 100, 200 e
300 W. Um dos filamentos queima. Depois disso, a lâmpada funciona com a mesma luminosidade
(dissipa a mesma potência) que antes quando o interruptor está na posição de menor luminosidade ou na
posição de maior luminosidade, mas não acende quando o interruptor está na posição intermediária. (a)
De que forma estão ligados os filamentos nas três posições do interruptor? (b) Qual é a resistência do
filamento de menor resistência? (c) Qual é a resistência do filamento de maior resistência?
105 Na Fig. 27-84, R = R = 2,0 Ω, R = 4,0 Ω, R = 3,0 Ω, R = 1,0 Ω, R = R = R = 8,0 Ω e as
1 2 3 4 5 6 7 8
forças eletromotrizes das fontes são = 16 V e = 8,0 V. Determine (a) o valor absoluto e (b) o sentido
1 2
(para cima ou para baixo) da corrente i , e (c) o valor absoluto e (d) o sentido (para cima ou para baixo)
1
da corrente i . Determine a potência fornecida ou absorvida (e) pela fonte 1 e (f) pela fonte 2. (g) A fonte
2
1 está fornecendo ou absorvendo energia? (h) A fonte 2 está fornecendo ou absorvendo energia?
Figura 27-84 Problema 105.

_______________
1Na verdade, de acordo com a Eq. 27-47, o tempo que a energia leva para chegar ao valor seguro é
diretamente proporcional à resistência dos pneus. (N.T.)

