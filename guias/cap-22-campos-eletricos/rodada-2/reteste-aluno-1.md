# Reteste do Aluno 1 (base frágil) na versão 2 do guia

Li a cópia cega da v2 (`rodada-2/aluno/guia-cego.md`) em partes. Não abri o HTML, `calculos.py` nem `plano.md`. Respondi e marquei a confiança antes de abrir cada conferência.

**Aviso de contaminação.** Vários itens já tinham sido vistos na v1, com gabarito e feedback. Eles estão marcados como "contaminado" e não contam como reteste limpo. Os retestes limpos são: prev-w2, lac-r-3, lac-r-5, prev-w3 e os exercícios A e B.

---

## 1. Pontos da v1 · resolvido na v2?

| Ponto da v1 | Resolvido na v2? | Evidência (frase da v2 ou resultado) |
|---|---|---|
| Degrau 4: "somar todos com uma integral" sem definição (bloqueia) | **sim** | "Integral É a soma de infinitos pedacinhos. ∫ₐᵇ f(θ) dθ soma f(θ)·dθ de θ = a até θ = b. Para calcular: ache uma função cuja derivada é f (a primitiva)…" |
| Degrau 4: radiano nunca definido (bloqueia) | **sim** | "Radiano É o ângulo em que o arco tem o mesmo comprimento do raio. Uma volta (360°) mede 2π rad, então 180° = π rad, 90° = π/2 rad e 120° = 2π/3 rad." |
| Degrau 4: o "d" de dq, ds, dθ (bloqueia) | **sim** | "O 'd' na frente de uma letra Quer dizer 'um pedacinho muito pequeno de'. ds é um pedacinho de comprimento do arco… ds = r dθ." |
| Degrau 4: por que cos θ (bloqueia) | **sim** | "Separe cada dE em duas partes… (pela trigonometria do triângulo da figura, cos θ é a fração de dE que aponta ao longo do eixo)." |
| Degrau 4: ∫cos θ dθ sem explicação (bloqueia) | **em parte** | "A derivada de sen θ é cos θ, então a primitiva de cos θ é sen θ: ∫ cos θ dθ de −α a α = 2 sen α." Consigo seguir. Mas "derivada" não é definida no guia. |
| Degrau 4: frase do seno com sinais opostos ("a integral é a mesma") (atrapalha) | **sim** | "A conta muda em dois pontos… integre só a metade de cima, de 0 a φ/2, e dobre: E = (2kλ/r)(1 − cos(φ/2))." E: "de −φ/2 a +φ/2, ∫sen θ dθ dá zero (o seno é ímpar)." |
| Degrau 4: "tanto faz graus ou radianos" para o seno (atrapalha) | **sim** | "sen 60° = sen(π/3 rad) = 0,866, mas sen(60 rad) é outro número." |
| Degrau 4: lac-a-3, calculadora em graus (atrapalha) | **sim** | Mensagem nova: "0.7845 → Calculadora em graus? Aqui o ângulo é 1 rad." Usei sen(1 rad) e obtive 37,8 N/C. |
| Degrau 4: ck4-3, "mais pedaços = mais campo" (atrapalha) | **não** | Os "Erros comuns" do degrau 4 continuam os mesmos quatro, sem o aviso sobre pedaços que se cancelam. |
| Degrau 4: prev-w4 com o caso do anel dado antes da previsão (atrapalha) | **sim** | Agora: "E um anel completo? Descubra no widget, mais abaixo." |
| Degrau 5: "A conta" sem a primitiva (bloqueia) | **sim** | "E = kλ∫…dx/x² = kλ[−1/x]ₐ^{a+L} = kλ(1/a − 1/(a+L))." E: "A primitiva de 1/x² = x⁻² é −1/x… 'Valor em cima menos valor embaixo'." |
| Degrau 5: "erro" nunca definido em prev-w5 e ck5-3 (atrapalha) | **sim** | "O erro de trocar a barra por um ponto, isto é, a diferença dividida pelo valor certo, é exatamente (L/2D)²." |
| Degrau 3: lac-p-4, valor 0 sem mensagem (atrapalha) | **sim** | Mensagem nova para 0: "Sinais opostos não cancelam tudo: cancelam a componente ao longo do eixo de simetria e somam a paralela à base." |
| Degrau 3: "semelhante" sem razão (salto lógico) | **sim** | "(mesmos ângulos, lados proporcionais)" |
| Degrau 3: "mediatriz" sem definição | **sim** | "a mediatriz: a reta perpendicular ao segmento entre as cargas, passando pelo meio dele" |
| Degrau 3: arctan e quadrante sem tabela | **sim** | Tabela 2º/1º/3º/4º quadrante com 180° − ref, ref, 180° + ref, −ref. |
| Degrau 3: "hipotenusa" sem definição | **sim** | "(o lado maior, oposto ao ângulo reto: 5,0 cm)" |
| Degrau 3: "a 90°" sem referência | **sim** | "a 90° do semieixo +x" |
| Degrau 3: "fator 4/5 → 0" confuso | **sim** | "o fator 4/5 é y/r, e y/r → 0 quando y → 0." |
| Degrau 3: "r = a/√2" entregue antes do checkpoint | **sim** | Removido; agora só "use Pitágoras". |
| Degrau 3: lac-p-2, lac-p-3, lac-p-4 | **sim, mas contaminado** | Repeti 30°, 46,7 N/C e 27,0 N/C. Já sabia os gabaritos. |
| Degrau 2: prev-w2 com a regra que dava a resposta | **em parte** | Previsão nova (1 nC a 1 cm, 4 nC a 3 cm). Mas a regra "Quem ganha não é a carga maior: é a de maior |q|/r²" está antes da previsão e ainda ajuda a respondê-la. |
| Degrau 2: ck2-2, mesmo módulo com distâncias diferentes | **em parte** | A regra "é a de maior |q|/r²" cobre o caso. Mas, como está antes do checkpoint, ela quase entrega ck2-2. |
| Degrau 2: ck2-3 (ordem dos sistemas) | **não** | A figura continua sem dizer a ordem das cargas (esquerda → direita) nem a posição de P. |
| Degrau 2: "0,020 m" sem conversão | **sim** | "Em metros: 2,0 cm = 0,020 m e 3,0 cm = 0,030 m." |
| Regra de avanço: 1 de 3 não tinha resposta | **sim** | "Acertou 0 ou 1: releia os blocos que o feedback indicar, refaça as que errou e então siga (a página deixa marcar o degrau como concluído)." |
| Resto do capítulo: P9 é dipolo mas o texto diz "nenhuma" | não verificado | Não reli essa seção na v2. |
| P31: letra a usada com dois sentidos | não verificado | Não reli os enunciados das questões na v2. |

---

## 2. Placar das perguntas e lacunas refeitas

**Limpos (sem gabarito visto antes):**

| Item | Resposta | Confiança | Resultado |
|---|---|---|---|
| prev-w2 (nova) | c, aponta para a direita (5 × 10⁴ N/C) | 2 | ✓ |
| lac-r-3 (valor mudou para 6,742 × 10⁴) | 6,75 × 10⁴ N/C | — | ✓ (desvio de 0,1 %) |
| lac-r-5 (valor mudou para −2,248 × 10⁴) | −2,25 × 10⁴ N/C | — | ✓ (desvio de 0,1 %) |
| prev-w3 (nova) | b, vai a zero | 3 | ✓ |

**Contaminados (gabarito já visto na v1; não contam como reteste):**

| Item | Minha resposta | Confiança | Resultado |
|---|---|---|---|
| lac-r-1 | 9,0 × 10⁴ N/C | — | ✓ (mas o gabarito era o mesmo) |
| lac-r-2 | b | — | ✓ |
| lac-r-4 | a | — | ✓ |
| lac-p-2 | 30° | — | ✓ |
| lac-p-3 | 46,7 N/C | — | ✓ |
| lac-p-4 | 27,0 N/C | — | ✓ |
| lac-a-1 | 2 rad | — | ✓ |
| lac-a-2 | 5 × 10⁻⁹ C/m | — | ✓ |
| lac-a-3 | 37,8 N/C | — | ✓ |
| prev-w5 | c, D = 5L | 2 | ✓ |
| ck5-3 | d, 0,25 % | 3 | ✓ |
| ck2-2 | a, para a direita | 2 | não reabri a conferência |
| ck2-3 | d, 2-4-3-1 | 1 | não reabri a conferência |
| ck4-3 | c, e-b-a=c-d | 2 | não reabri a conferência |

Resumo: **4 de 4 limpos certos**. Os contaminados, em 11 respostas conferidas, deram 11 de 11 certas, mas isso não diz nada sobre o que eu entendi de fato. Não consigo afirmar que resolveria ck2-2, ck2-3 e ck4-3 sem ajuda.

---

## 3. Exercícios de transferência (sem conferência)

**A) Arco de 90°, raio 10 cm, carga +2,0 nC uniforme.**

- φ = π/2 rad. Comprimento do arco: s = rφ = 0,157 m.
- λ = Q/(rφ) = 2,0 × 10⁻⁹ / (0,10 × π/2) = 1,27 × 10⁻⁸ C/m.
- E = (2kλ/r)·sen(φ/2) = (2 × 8,99 × 10⁹ × 1,27 × 10⁻⁸ / 0,10) × sen(45°) = 2289 × 0,707 ≈ **1,62 × 10³ N/C**.
- Conferi pelo fator: kQ/r² = 1,80 × 10³ N/C; sen(π/4)/(π/4) = 0,900; produto 1,62 × 10³ N/C.

**B) Barra reta de 20 cm, carga +4,0 nC uniforme, P no prolongamento a 10 cm da ponta mais próxima.**

- a = 0,10 m; L = 0,20 m; a + L = 0,30 m.
- E = kQ/(a(a+L)) = (8,99 × 10⁹ × 4,0 × 10⁻⁹) / (0,10 × 0,30) = 35,96 / 0,030 ≈ **1,20 × 10³ N/C**.

---

## 4. O que ainda bloqueia ou atrapalha

Nada que bloqueie o degrau 4 ou o degrau 5 agora. Restam estes pontos:

1. **"derivada" é usada sem definição** no bloco ∫cos θ dθ (Degrau 4). Atrapalha pouco, mas é um termo que eu não tenho.
2. **ck2-3 (ordem dos sistemas)**: a figura continua sem dizer a ordem das cargas nem onde P está. Atrapalha.
3. **ck4-3 ("mais pedaços")**: os "Erros comuns" do Degrau 4 não ganharam o aviso sobre cargas que se cancelam. Atrapalha; foi o erro que cometi.
4. **Regra "quem ganha é |q|/r²" antes do checkpoint 2**: a regra quase entrega ck2-2. Vale mover para depois da previsão, como foi feito com o anel.
5. **"Ver a mesma regra em forma vetorial" (Degrau 3)** usa r̂ sem definir o vetor unitário. Polimento.
6. Não reli resto do capítulo (dipolo), questões P31 e Degrau 6 na v2. Não sei se os itens 58–64 da v1 mudaram.
