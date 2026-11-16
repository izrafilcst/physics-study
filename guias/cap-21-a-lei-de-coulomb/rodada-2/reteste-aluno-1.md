# Reteste da v2, Aluno 1 ("Base frágil")

Guia cego lido: `/tmp/claude-1000/-home-swampert-Documents-fisica/93ef5522-be14-4893-b202-653fbaf407ec/scratchpad/reteste/guia-v2-cego.html`

## Aviso de metodologia

- Escrevi cada resposta (com confiança) em `scratchpad/reteste/rascunho-aluno1.txt` antes de abrir o arquivo de conferência correspondente. Exceção abaixo.
- **Exceção 1, prever-w4 (Degrau 5):** li `conferir/prever-w4.txt` sem ter escrito a resposta antes. Não conta.
- **Exceção 2, lacuna l7 (Degrau 7):** `lacunas.txt` traz todas as lacunas de uma vez, e eu o abri depois de responder l1 a l6, mas antes de responder l7. Não respondi l7, então ela não conta como teste.
- Como a leitura do guia com Read mostra o texto inteiro, li o guia cego sem gabaritos (ele não os tem). O mesmo não vale para o exemplo do Degrau 3, que traz um número (ver item 3).
- Não usei Bash para ler o guia nem as conferências.

## (a) Os cinco pontos da rodada 1

### 1. Pré-requisito 5 (derivada) e a revisão rápida: **parcial**

- Respondi `a` (confiança 1). A certa é `b`. Errei porque esqueci a derivada da parte de dentro, como a revisão mostra.
- A revisão aparece no feedback (`conferir/quiz-pre5.txt`) e ensina a regra do quociente: "Regra do quociente, que o Degrau 6 usa: $\left(\dfrac{u}{v}\right)' = \dfrac{u'\,v - u\,v'}{v^2}$. Exemplo: $\left(\dfrac{x}{x^2+1}\right)' = \dfrac{1\cdot(x^2+1) - x\cdot 2x}{(x^2+1)^2} = \dfrac{1-x^2}{(x^2+1)^2}$."
- Entendi a fórmula e consigo acompanhar cada passo do exemplo. Não entendo por que ela tem essa forma. Só sei usá-la porque o exemplo mostra o caminho.
- Ainda falta: a revisão só aparece depois de errar ou acertar o pré-requisito 5. Quem não chega ao pré-requisito 5 nunca vê a regra do quociente antes do Degrau 6.

### 2. Degrau 6: caixa "Ferramenta de Cálculo" e lacuna l6: **parcial**

- A caixa diz: "Num quociente com potência no denominador, use as duas: derive $v = (x^2+a^2)^n$ pela cadeia, $v' = n(x^2+a^2)^{n-1}\cdot 2x$." Isso me permitiu fazer o passo de $v'$ (escolhi `b`, $4x(x^2+a^2)$, com confiança 1, e acertei).
- Na lacuna, o texto já escreve a linha do quociente: "$g'(x) = \dfrac{(x^2+a^2) - 4x^2}{(x^2+a^2)^3} = \dfrac{\square}{(x^2+a^2)^3}$". Sobra só escolher o numerador. Não sei explicar, a partir do texto, por que o fator $(x^2+a^2)$ sai do denominador. O texto diz "corte um fator $(x^2+a^2)$", mas não mostra o corte.
- Resultado: todas as seis respostas de l6 bateram (valor máximo: 0,32 contra 0,3248, dentro de 2%, mas foi chute com confiança 1, não cálculo).
- Ainda bloqueia: não consigo derivar $g$ sozinho sem a linha pronta. Se a linha do quociente for removida, eu travo ali.

### 3. Degrau 3: lacuna do próton girando em torno de −2e: **sim, com um problema**

- O sinal não confundiu, porque a lacuna nova não pede o sinal de $Q$. Escolhi `a` (força elétrica da carga −2e) com confiança 3 e `b` (raiz de $2ke^2/(mr)$) com confiança 2. Acertei l3.
- Problema: o enunciado do campo de cálculo diz: "escreva como 5,26e4, por exemplo". Esse é o próprio valor da resposta (o gabarito confere: 5.256e4). Escrevi 5,26e4 com confiança 1 e não sei se cheguei lá por conta ou pelo exemplo. Isso é entrega demais.

### 4. Lacunas dos Degraus 1, 2 e 5: o gabarito aparece antes de conferir?: **não, resolvido**

- Lendo o guia cego, nenhum gabarito aparece antes do botão "Conferir lacunas" nos Degraus 1, 2 e 5. O gabarito só aparece no arquivo de conferência.
- Acertei l1 (a, 10,99, 1,388, b), l2 (b, a, b, 13,66, −13,66), l5 (b, a, b, 0,0719, 0,1438, 0,03596, 0,02543, 0,1692, −0,0465), todas dentro de 2%.
- Ressalva: no Degrau 5, a lacuna dá o passo "Cada componente de $F_{32}$ vale $F_{32}/\sqrt2 =$" como campo, o que ajuda, mas não entrega o número.
- Ressalva: a lacuna l1 (Degrau 1) diz "Isolando r na Eq. 21-4: r = √(□)", então a forma da raiz já vem pronta. Entendi, mas dei o chute "a" com confiança 2 sem certeza do porquê.

### 5. Explicações novas

| Ponto da rodada 1 | Destravou? | Frase do guia |
|---|---|---|
| Degrau 2: por que o ponto de força nula fica perto da carga menor | **sim** | "Para empatar, $\|q\|/r^2$ tem de ser igual para as duas, ou seja, $r \propto \sqrt{\|q\|}$. A carga fraca precisa estar mais perto: com $+4q$ e $+q$, o ponto fica 2 vezes ($\sqrt4$) mais longe da $+4q$ que da $+q$." |
| Degrau 4: origem de $x \propto q^{2/3}$ | **não** | Na conferência de prever-w3: "A demonstração de $x^3 \propto q^2$ é o item (a) do Problema 42." O Degrau 4 não tem a derivação. Não li o Problema 42. |
| Degrau 5: Exemplo 21.01c com a raiz | **sim** | "Coincide com $F_y$ porque $F_x$ é 14 vezes menor: ao quadrado, mal pesa na raiz." Conferi: $1{,}78/0{,}125 \approx 14$. |

Dúvidas extras da rodada 1 que também mudaram:
- O $4\pi$ de $k$ (Degrau 1): parcial. O texto diz "É escolha de unidades. O SI escreve a constante como $k = 1/(4\pi\varepsilon_0)$, em que $\varepsilon_0$ é a constante elétrica (ou permissividade do vácuo)." Entendi que o $4\pi$ é convenção. "Permissividade" continua sem definição.
- Problema 52 do sinal de Q: destravou, porque a lacuna nova não pede o sinal.

## (b) Placar dos checkpoints (Degraus 2 a 7)

Cada resposta foi escrita antes de abrir a conferência. Confiança: 1 = chute, 2 = acho que sei, 3 = tenho certeza.

| Degrau | Acertos de primeira | Respostas (escolha, confiança) |
|---|---|---|
| 2 | **3 de 3** | a (2), b (2), c (2) |
| 3 | **3 de 3** | d (3), a (2), c (3) |
| 4 | **3 de 3** | d (2), b (3), b (2) |
| 5 | **3 de 3** | d (3), a (2), c (3) |
| 6 | **3 de 3** | a (2), a (2), b (2) |
| 7 | **3 de 3** | d (2), a (3), b (2) |

Previsões: w2 (Degrau 2) acertei (d, confiança 2). w1 (Degrau 1) acertei (d, confiança 3). w3 (Degrau 4) acertei (c, confiança 1). w5 (Degrau 6) acertei (c, confiança 2). w4 (Degrau 5) não conta (ver aviso). w6 (Degrau 7) não respondi.

Observação: os checkpoints do Degrau 3 (c) e do Degrau 7 (c) se respondem pelo próprio texto, por exemplo "a força muda a direção da velocidade, mas não o módulo" e "$b = \rho\,r$". Acertar foi fácil, então o placar sozinho não mede muito.

## (c) O que ainda bloqueia ou atrapalha

1. **Origem de $x \propto q^{2/3}$ (Degrau 4).** Bloqueia a previsão w3 e a relação de ângulo pequeno. A referência ao Problema 42 não resolve, porque o degrau não tem a derivação.
   Evidência: "A demonstração de $x^3 \propto q^2$ é o item (a) do Problema 42."
   Sugestão: três linhas de derivação no Degrau 4, ou pelo menos um link para a seção do P42 com a derivação.

2. **Exemplo do Degrau 3 entrega o número da lacuna.** Atrapalha.
   Evidência: "escreva como 5,26e4, por exemplo".
   Sugestão: trocar o exemplo por outro número, ou tirar.

3. **Quociente pré-simplificado (Degrau 6).** Atrapalha. O passo de cortar $(x^2+a^2)$ não é explicado.
   Evidência: "Quociente e simplificação (corte um fator $(x^2+a^2)$)."
   Sugestão: uma linha dizendo por que o fator sai.

4. **Regra do quociente só aparece no feedback do pré-requisito 5.** Atrapalha. Quem acerta o pré-requisito 5 pode nunca ler a fórmula; quem erra precisa errar antes.
   Sugestão: pôr a fórmula da regra do quociente na caixa "Ferramenta de Cálculo" do Degrau 6, e também no teste de pré-requisitos.

5. **"Permissividade do vácuo" sem definição (Degrau 1).** Polimento. Sugestão: uma frase "a capacidade do vácuo de ... ", ou só "constante elétrica".

6. **Lacuna l7 e prever-w4 contaminadas nas minhas notas.** Não é problema do guia, só do meu teste.

## Resumo (5 linhas)

1. Placar dos checkpoints dos Degraus 2 a 7: 6 de 6 blocos com 3 de 3 de primeira (confiança 2 a 3). Previsões w1, w2, w3, w5 acertei.
2. Destravou: origem de $\sqrt{|q|}$ no Degrau 2 e o Exemplo 21.01c com a raiz no Degrau 5 (sim); regra do quociente e caixa de cálculo (parcial, a linha do quociente vem pronta).
3. Ainda bloqueia: origem de $x \propto q^{2/3}$ no Degrau 4 (remete ao Problema 42, que não tem a derivação).
4. Ainda atrapalha: o exemplo do Degrau 3 traz o número da resposta da lacuna ("5,26e4, por exemplo").
5. Gabaritos não aparecem mais antes de "Conferir" nos Degraus 1, 2 e 5, e a regra do quociente tem revisão; pré-requisito 5 errei (a em vez de b).

## Reteste 2: x ∝ q^(2/3) no Degrau 4 (último ponto)

Lido: guia cego, Degrau 4 (linhas 895 a 1010) e `conferir/prever-w3.txt` (nova explicação). Escrevi a minha própria explicação antes de abrir a nova.

**(a) Por que dobrar q faz x crescer menos que o dobro, com as minhas palavras:**
Dobrar q quadruplica a repulsão na distância antiga, então as bolinhas se afastam. Só que, quanto mais longe elas ficam, menor a força (cai com 1/x²), e o fio precisa de menos força para equilibrar. Então o afastamento para antes de dobrar. Entendo o motivo qualitativo. Não entendo por que o número é exatamente 1,59: a explicação diz que é a lei do item (a) do Problema 42, que não li.

**(b) Afirmações sem explicação no trecho:**
- "enquanto o fio só precisa de um pouco mais de inclinação para segurá-la". Não explica por que é "um pouco". Para eu ver isso, precisaria comparar $\tan\theta = F_e/(mg)$ com $F_e$ caindo com $1/x^2$, e o texto não faz essa conta.
- "Por que exatamente 1,59? Essa é a lei que você vai demonstrar no item (a) do Problema 42". O 1,59 fica sem prova no degrau.
- "usando a geometria do fio deste degrau". A geometria (L sen θ) está no degrau, mas o texto não liga ela à previsão.

**(c) Exemplo de formato da lacuna do Degrau 3:** agora está ok. A linha 827 diz "formato: 1,23e4, por exemplo". Esse número não é a resposta (5,26e4), então não entrega mais o valor.

**Veredito: parcial.** O motivo qualitativo ficou claro. Ainda não entendo de onde vem o 1,59, e a frase "um pouco mais de inclinação" continua sem justificativa no degrau.
