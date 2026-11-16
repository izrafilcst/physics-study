# Rodada 1, Aluno 1 ("Base frágil"): relatório do guia cap. 21 (Lei de Coulomb)

Guia testado: `/home/swampert/Documents/fisica/guias/cap-21-a-lei-de-coulomb/guia-v1.html`

## Aviso de metodologia (leia antes do placar)

- **Degrau 0 não foi cego.** Li o bloco inteiro com a ferramenta Read e as chaves `data-correta="b"` e os feedbacks apareceram antes de eu responder. Não conto nada do Degrau 0 no placar.
- **Degrau 1 foi cego.** Usei um filtro (awk) que remove `data-correta`, `data-certa`, `data-resp` e os blocos `quiz-fb`, `resposta-prev` e `mini-rev`. Respondi, anotei a confiança e só depois li o feedback de cada quiz (linhas 938–973, com Read).
- **Degrau 2 em diante não foi cego.** Ao tentar ler o feedback com um comando Bash (sed), o classificador de permissões bloqueou a ação. Passei a usar Read, mas Read também mostra os atributos de resposta, então os degraus 2–6 e as lacunas deles não são cegos. Não tenho placar válido para eles.
- A confiança do Degrau 1 foi estimada no momento da resposta (eu não a escrevi antes de conferir, o que é uma falha minha do procedimento).

## 1. Itens de crítica

| # | Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|---|
| 1 | Degrau 1, lacuna l1 ("Problema 3") | dica entrega demais | atrapalha | Linha 911, visível antes do botão "Conferir lacunas": "Gabarito do livro para o Problema 3: 1,39 m." | Mover o gabarito para dentro do estado "Conferir" ou para um revelado com botão. |
| 2 | Degrau 1, figura f1a (repulsão/atração) | figura confusa | atrapalha | Os rótulos "F⃗₁₂" e "F⃗₂₁" ficam flutuando no meio do par (x=194 e x=246), não em cada seta. Não dá para saber qual seta é de qual carga. | Rotular cada seta separadamente, ou pôr "F₁₂ (força de 2 sobre 1)" perto da seta da esquerda. |
| 3 | Degrau 1, Intuição, "A 'influência' ... aparece um $4\pi$ na constante da lei" | salto lógico | atrapalha | Eu li "cada pedacinho recebe 1/4 da luz" e "por isso a força cai com 1/r²", mas o 4π em k sai do enunciado sem explicar ε₀. A ficha só diz "constante elétrica" e não define permissividade. | Uma frase: "ε₀ é a permissividade do vácuo; $k = 1/(4\pi\varepsilon_0)$ é só a forma de escrever a mesma lei." |
| 4 | Degrau 1, prever w1 ("Antes de mexer") | dica fraca | atrapalha | Eu li a bola de vidro com a área 4× e errei ("a metade"). O salto de "área 4× maior" para "força 1/4" fica só no texto, sem uma linha de conexão antes da pergunta. | Antes da pergunta, escrever "área 4× → força ÷ 4 → força ∝ 1/r²" como conta explícita. |
| 5 | Degrau 1, ficha das grandezas, "Atrito do dia a dia" e "Atrito, cola..." | termo não definido | polimento | "atrito" aqui é eletrização por atrito, mas no Degrau 3 e no mundo da Física 1 "atrito" é a força de superfície. Não há aviso. | Escrever "atrito (eletrização por contato)" na primeira vez e pôr uma nota. |
| 6 | Degrau 1, ficha, "o dono do gato do Prob. 56", "Prob. 4", "Prob. 33" | denso demais | polimento | Referências a problemas que não estão na lista de questões, sem explicação. Eu não sabia o que era "Prob. 56". | Tirar as referências ou pôr uma nota "(problema do livro, fora deste guia)". |
| 7 | Degrau 1, "Onde a analogia quebra": "E não existe luz negativa que apague a outra" | denso demais | polimento | Frase de duas ideias seguidas (cargas negativas e sinal) que eu não consegui seguir. | Dividir em duas frases. |
| 8 | Degrau 2, Intuição, "Mesmo sinal ... O ponto fica mais perto da carga menor." | salto lógico | atrapalha | A frase dá a regra sem dizer por que a carga menor fica do lado perto. O porquê ("a carga forte precisa de uma distância maior para empatar") só aparece indiretamente no feedback de outro quiz. | Uma frase de justificativa logo depois da regra. |
| 9 | Degrau 2, figura f2a, legenda "seta de cima: força da carga da esquerda; de baixo: da direita" | figura confusa | polimento | A legenda está em baixo da figura, depois dos quatro painéis. Eu só achei depois de procurar. | Pôr a legenda perto das setas ou em cada painel. |
| 10 | Degrau 2, lacuna l2, bloco "Calcular" | dica entrega demais | atrapalha | Antes de eu preencher, o texto já escreve o resultado: "$s = \dfrac{L}{\sqrt3 - 1}$". Sobra só copiar a conta. | Mostrar a expressão só depois de o aluno tentar, ou deixar a expressão em branco. |
| 11 | Degrau 2, lacuna l2, "Verificar" | dica entrega demais | atrapalha | "Gabarito do livro: (a) −14 cm; (b) 0." aparece antes de "Conferir lacunas" (mesmo problema do item 1). | Igual ao item 1. |
| 12 | Degrau 3, "Ângulo pequeno" | salto lógico | atrapalha | "x ∝ q^{2/3}" aparece só no feedback do prever w3 ("Para ângulos pequenos, x ∝ q^{2/3}, e 2^{2/3} = 1,59"). Não há nenhuma linha que mostre de onde vem a relação. | Derivar em três linhas: tan θ ≈ θ ≈ kq²/(mg x²)… e até o resultado. |
| 13 | Degrau 3, lacuna l3 ("Problema 52"), linha "Resposta calculada pelo guia (questão par, sem gabarito oficial): $Q = -1{,}11\times10^{-5}$ C" | falta prática / outro | bloqueia | O campo "Módulo de Q" espera um número positivo ("escreva como 1,11e-5"), mas o texto diz Q negativo. Não sei se digito com sinal. Também a frase "sem gabarito oficial" e o gabarito aparecem antes de "Conferir". | Decidir um sinal, dizer qual é, e pedir só o módulo no campo (o texto já fala de módulo). |
| 14 | Degrau 3, lacuna l3, "escreva como 1,11e-5, por exemplo" | falta prática | polimento | O guia pede vírgula decimal no restante ("2,19e6") e aqui pede "1,11e-5" com ponto no exemplo. | Padronizar o exemplo com o formato da seção de questões. |
| 15 | Degrau 4, lacuna l4 (Problema 10/11), figura 21-25 | figura confusa | atrapalha | A figura não mostra o sinal de cada carga (todas cinza, só números). O enunciado dá os sinais, mas eu tive de voltar e cruzar o texto com a figura. A legenda explica "as cores mudam de problema para problema", o que não ajuda a ler esta figura. | Mostrar os sinais na figura (+ e −) ou pôr uma legenda de sinais fixa. |
| 16 | Degrau 4, lacuna l4, "Calcular" | dica entrega demais | atrapalha | "Cada componente de $F_{32}$ vale $F_{32}/\sqrt2 = 0{,}0254$ N." dá o passo que é o centro da questão. | Tirar o parágrafo; deixar o aluno achar a componente. |
| 17 | Degrau 4, lacuna l4, "Verificar" | dica entrega demais | atrapalha | "Gabarito do livro: (a) 0,17 N; (b) −0,046 N." aparece antes de "Conferir". (Mesmo padrão dos itens 1, 11, 13.) | Padronizar: gabarito só depois de conferir. |
| 18 | Degrau 4, Exemplo 21.01c, "$F_x = -1{,}25\times10^{-25}$ N; $F_y = 1{,}78\times10^{-24}$ N; $F = 1{,}78\times10^{-24}$ N." | salto lógico | atrapalha | O módulo sai igual a F_y sem a conta $\sqrt{F_x^2 + F_y^2}$. Eu não percebi que $F_x \ll F_y$ torna a raiz praticamente F_y. | Escrever a raiz e depois dizer "F_x é 14 vezes menor que F_y, então F ≈ F_y". |
| 19 | Degrau 4, Problema 11, enunciado vs. legenda | outro | polimento | O título diz "Problema 11: a mesma figura do Problema 10", a legenda diz "Problemas 10, 11 e 70", e o enunciado diz "Fig. 21-25". Três referências diferentes para a mesma coisa. | Escolher uma forma e repetir igual. |
| 20 | Degrau 5, Formalização e lacuna l5, "Regra do quociente" | termo não definido | **bloqueia** | "Regra do quociente" aparece em "Regra do quociente: $g'(x) = \dfrac{(x^2+a^2)\cdot1 - x\cdot2x}{...}$". Em nenhum lugar do guia há a fórmula $(u/v)' = (u'v - uv')/v^2$. O mini-teste do Degrau 0 revisa só a regra da cadeia. Sem a fórmula eu não consigo derivar $g$ e não consigo fazer o Degrau 5. | Incluir a fórmula da regra do quociente no mini-revisão do Degrau 0, ao lado da regra da cadeia. |
| 21 | Degrau 5, Intuição, "fator $x/r$" | termo não definido | atrapalha | $r$ aparece antes de ser definido (a definição $r = \sqrt{x^2+d^2}$ só está na Formalização, uns parágrafos depois). | Definir $r$ na primeira vez em que aparece. |
| 22 | Degrau 5, "x → ∞" e a lacuna l5 (limite de g) | termo não definido | atrapalha | "Limite" e "x → ∞" nunca são explicados. O aluno tem de saber que $g(x) \to 0$ sem nenhuma ajuda. | Uma linha: "x → ∞ quer dizer x cada vez maior; o valor de g vai para o número que se aproxima." |
| 23 | Degrau 5, lacuna l5, "Verificar": "Nas bordas g = 0 e no ponto crítico g > 0: é um máximo ✓" | salto lógico | atrapalha | Comparar o valor no ponto crítico com as bordas não prova que é máximo se houver outros pontos críticos. A frase não diz por que este é o único ponto crítico. | Acrescentar: "e a derivada só se anula em x = a (um único ponto crítico), então...". |
| 24 | Degrau 5, prever w5 | dica fraca | polimento | A pergunta pede o ponto de força máxima antes de o aluno ter a fórmula $F(x)$. Só dá para chutar. | Mover a previsão para depois da fórmula, ou pôr a pergunta em forma de "qual dos três casos-limite..." |
| 25 | Degrau 6, Intuição, "a soma vira integral" | termo não definido | atrapalha | "Integral" aparece como ideia ("a soma vira integral") sem nenhuma definição e sem o símbolo ∫ explicado. A Formalização usa $\int$ direto. | Uma frase: "∫ é o símbolo da soma contínua; $\int f\,dr$ soma as fatias $f\,dr$." |
| 26 | Degrau 6, Ficha, "barra isolante do Prob. 51: $-4{,}00\ \mu$C/m³" | denso demais | polimento | Na mesma página há "barra" com $\rho = bx^2$, $b = -2\,\mu$C/m⁵ (exemplo 51b) e a ficha dá uma densidade em C/m³ para a "barra do Prob. 51". Não sei se é a mesma barra. | Esclarecer ou tirar a referência. |
| 27 | Degrau 6, prever w6 e widget, legenda "b = 3,0 µC/m² (não é a do Problema 21)" | outro | polimento | Se o parêntese diz que não é o do Problema 21, a ficha dizia "Prob. 21: 3,0 µC/m²". Dá a impressão de que o valor está errado. | Tirar a menção ao Problema 21 nessa legenda. |
| 28 | Geral, pré-requisitos (Degrau 0) | outro | polimento | O texto manda "Marque também quanto você confia na resposta, antes de conferir", mas no HTML não encontrei nenhum controle de confiança (1, 2, 3). Pode estar no JS, mas na tela eu não achei. | Pôr os três botões de confiança em cada quiz, ou tirar a instrução. |
| 29 | Geral, lacunas "gabarito do livro" | dica entrega demais | atrapalha | Padrão repetido: os itens 1, 11, 13 e 17 mostram o gabarito antes do botão "Conferir". | Padronizar o bloco "Verificar" para não conter o número final. |
| 30 | Questões, P7 | outro | polimento | Na escada de ajuda, o card inteiro (incluindo "Resolução comentada" e "Resposta") fica no HTML. Escondido, mas acessível pelo DOM. | Montar o conteúdo das ajudas só depois do clique (JS), não deixar no HTML. |

Observação honesta sobre P7 e demais questões: não li os cartões de P73, P42, P50, P10, P23 e P21, por limite de tempo. O único que li foi P7, e a resolução estava visível no dump (ver item 30), então não tentei P7.

## 2. Perguntas ao Professor

1. Professor, por que aparece um $4\pi$ na constante $k$ se a explicação foi "a luz se espalha pela esfera"? De onde vem $\varepsilon_0$, e por que ele não é explicado antes de $k = 1/(4\pi\varepsilon_0)$?
2. Professor, o que é a "regra do quociente" do Degrau 5? Ela não aparece no mini-teste do Degrau 0 e eu não sei como derivar $g'(x)$ sem ela.
3. Professor, no Exemplo 21.01c, por que a força total é $1{,}78\times10^{-24}$ N e não a raiz de $F_x^2 + F_y^2$? Ela é só $F_y$?
4. Professor, por que o gabarito do Problema 3 aparece antes de eu clicar em "Conferir lacunas"? Isso não estraga o exercício?
5. Professor, no Problema 52 o texto diz $Q = -1{,}11\times10^{-5}$ C, mas o campo espera um número positivo. Qual sinal eu digito?
6. Professor, "$x \propto q^{2/3}$" aparece só no feedback do simulador do Degrau 3. De onde vem essa relação? Eu não consigo deduzi-la.

## 3. Placar

**Checkpoints (válidos só onde o teste foi cego):**

| Degrau | Teste | Acertos de primeira | Confiança (estimada) | Válido? |
|---|---|---|---|---|
| 0 | Pré-requisitos (6 perguntas) | não contável (vi as chaves) | — | não |
| 1 | Checkpoint (3 perguntas) | **2 de 3**: d1a acertei (a), d1c acertei (c), d1b errei (respondi a, certa b) | d1a ≈ 2, d1b ≈ 1, d1c ≈ 1 | sim |
| 2 | Checkpoint (3 perguntas) | não contável (chaves visíveis) | — | não |
| 3 | Checkpoint (3 perguntas) | não contável | — | não |
| 4 | Checkpoint (3 perguntas) | não contável | — | não |
| 5 | Checkpoint (3 perguntas) | não contável | — | não |
| 6 | Checkpoint (3 perguntas) | não contável | — | não |

**Previsões:**

- w1 (Degrau 1, "dobrar r"): errei. Respondi "a metade"; a certa é "um quarto". Confiança ≈ 1.
- w2 a w6: não contáveis (chaves visíveis).

**Lacunas:**

- l1 (Degrau 1): preenchi a primeira seleção ("k|q₁||q₂| / F") e não conferi o restante. Sem placar.
- l2 a l6: não contáveis, e não tentei a parte numérica.

**Questões:**

- P7: **não tentei**. Li o cartão com a resolução visível no dump.
- P73, P42, P50, P10, P23, P21: **não li** (tempo).

## 4. O que funcionou (não remover na v2)

1. **Feedback por alternativa (`data-para`).** Cada opção errada explica por que está errada. No d1b eu li "Seria assim se a força caísse com 1/r" e entendi o meu erro na hora.
2. **Analogias com a seção "Onde a analogia quebra".** Bola de vidro (1/r²), cabo de guerra (superposição), quadras de cidade (componentes), densidade populacional (integral). A seção de quebra impede a analogia de ir longe demais.
3. **Revelados "por que ...?".** Em especial "por que só a raiz positiva?" (Degrau 2), "por que dividir uma equação pela outra?" (Degrau 3) e "por que sobra y, e não x?" (Degrau 5). Respondem a dúvida do aluno no lugar em que ela aparece.
4. **Ficha das grandezas com a coluna "Armadilha".** Ex.: "esquecer µ = 10⁻⁶" e "usar cm: como r vai ao quadrado, o erro vira um fator 10⁴". É o tipo de coisa que eu erraria sem avisar.
5. **Exemplo resolvido em quatro passos (Entender, Modelar, Calcular, Verificar).** Deu para seguir a estrutura mesmo sem entender tudo.
6. **Mitos (pensa / real / pq).** A forma "eu pensava X, o real é Y, porque Z" é clara e curta.
7. **Figura do diagrama de corpo livre (f3a) e a figura de regiões (f2a com ✓ e ✗).** Rótulos claros, forças bem separadas.
8. **P7 e a escada de ajuda.** A Dica 1 ("Degrau 2, a figura das regiões...") aponta onde olhar sem dar a conta, e a reflexão "que passo você não teria visto sozinho?" é boa.
9. **Mini-revisão do Degrau 0 com prefixos e áreas.** "(1 cm)² = (10⁻² m)² = 10⁻⁴ m²" me salvou de um erro que eu sei que cometo.
10. **Frase de orientação "Suba quando acertar 2 de 3 de primeira".** Deixa claro o critério de avanço.

## 5. Resumo (5 linhas)

1. Placar válido: Degrau 1 com 2 de 3 de primeira (d1a e d1c certas, d1b errada) e previsão w1 errada. Degraus 0 e 2 a 6 não são cegos, então não contam.
2. Problema mais grave: a "regra do quociente" (Degrau 5) é usada sem nunca ter sido definida, o que me bloqueia na derivada de g.
3. Segundo mais grave: o Problema 52 não diz qual sinal digitar (texto diz Q negativo, campo espera positivo).
4. O que mais ajudou: o feedback por alternativa, as analogias com "Onde a analogia quebra" e os revelados "por que ...?".
5. Crítica transversal: gabaritos ("Gabarito do livro: ...") aparecem antes do botão "Conferir" em vários degraus, o que entrega a resposta.
