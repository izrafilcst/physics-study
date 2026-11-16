# Plano — Guia do Capítulo 22: Campos Elétricos

**Questões pedidas:** Problemas 8, 9, 15, 26, 29, 31, 38 e 81.
**Fonte:** `halliday-v3/cap-22-campos-eletricos.md` + `gabarito.md` + PDF original (`../FIsica 3 Eletromagnetismo Halliday.pdf`, págs. 76–138), usado só para ver as figuras e equações que a conversão perdeu.

| Questão | Dificuldade (livro) | Figura | Gabarito oficial |
|---|---|---|---|
| P8 | ·· | 22-36 | — (par) |
| P9 | ·· | 22-37 | (a) 1,38 × 10⁻¹⁰ N/C; (b) 180° |
| P15 | ·· | 22-42 | (a) 160 N/C; (b) 45° |
| P26 | ·· | 22-50 | — (par) |
| P29 | ·· | 22-52 | 1,57 |
| P31 | ·· | 22-54 | (a) −5,19 × 10⁻¹⁴ C/m; (b) 1,57 × 10⁻³ N/C; (c) −180°; (d) 1,52 × 10⁻⁸ N/C; (e) 1,52 × 10⁻⁸ N/C |
| P38 | ·· | 22-58 | — (par) |
| P81 | adicional | (sem figura) | (a) −0,029 C; (b) a esfera seria desintegrada pela repulsão |

---

## 1. Habilidades (matriz questão × habilidade)

| Código | Habilidade |
|---|---|
| H1 | Entender o campo como "força por coulomb" e usar **F = qE** (sentido de F igual ao de E para q > 0, oposto para q < 0) |
| H2 | Calcular o **módulo** do campo de uma carga pontual, E = k\|q\|/r² (prefixos µ, n, p, f; elevar r ao quadrado) |
| H3 | Desenhar o **sentido** do campo **no ponto P** (para longe de +, para perto de −), sem confiar no sinal algébrico |
| H4 | Somar campos **na mesma reta** e enxergar **cancelamentos** (cargas proporcionais a r², lados e sinais) |
| H5 | Somar campos **no plano**: distâncias (Pitágoras, diagonal), componentes com sinal, simetria que zera uma componente |
| H6 | Dar a **orientação** de um vetor em relação ao semieixo x positivo (quadrante; atan não basta) |
| H7 | Usar **densidade de carga** (λ = Q/L; comprimento de arco s = rφ; σ = Q/A) |
| H8 | **Método do elemento** em arcos: dq = λ ds, ds = r dθ, todos os elementos à mesma distância; simetria; ∫cos θ dθ |
| H9 | **Método do elemento** em barra reta com P no prolongamento: a distância varia, ∫dx/x² |
| H10 | **Casos-limite**: longe, toda distribuição vira carga pontual; perto do disco, vira placa infinita |
| H11 | Usar a fórmula do **disco** no eixo, E = (σ/2ε₀)(1 − z/√(z² + R²)), e ler um **gráfico** normalizado (E/Eₘ) |
| H12 | **Equilíbrio** com força elétrica e peso (ΣF = 0) e **checar a viabilidade** por ordem de grandeza (ruptura do ar, repulsão) |
| H13 | Resolver em símbolos antes de pôr números; verificar unidade, sinal e casos-limite |

| | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 | H10 | H11 | H12 | H13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **P81** | ● | ● | | | | | | | | ● | | ● | ● |
| **P8** | | ● | ● | ● | | | | | | | | | ● |
| **P9** | | ● | ● | | ● | ● | | | | | | | ● |
| **P15** | | ● | ● | ● | ● | ● | | | | | | | ● |
| **P29** | | ● | | | ● | | ● | ● | | ● | | | ● |
| **P26** | | | ● | | ● | ● | ● | ● | | | | | ● |
| **P31** | | ● | ● | | | ● | ● | | ● | ● | | | ● |
| **P38** | | | | | | | ● | | | ● | ● | | ● |

## 2. Pré-requisitos

- **Capítulo 21:** lei de Coulomb, F = k\|q₁q₂\|/r²; sinais iguais repelem; soma vetorial de forças.
- **Física 1:** vetores e componentes (cap. 3); 2ª lei de Newton e equilíbrio, ΣF = 0 (cap. 5).
- **Matemática:** notação científica e prefixos até o femto (f = 10⁻¹⁵); trigonometria (sen, cos, tan, triângulo 3-4-5, diagonal do quadrado); ângulo de um vetor pelo quadrante; integral de potência (∫x⁻² dx = −1/x) e ∫cos θ dθ = sen θ.
- O Degrau 0 tem um teste rápido de 6 itens, um por pré-requisito, com mini-revisão para quem errar.

## 3. Degraus (do concreto ao abstrato)

| Degrau | Objetivo (1 frase) | Habilidades | Desbloqueia | Tempo |
|---|---|---|---|---|
| **0 — Aquecimento** | Prever se dá para fazer uma bola flutuar no campo elétrico da atmosfera e checar os pré-requisitos. | — | — | 10 min |
| **1 — Campo = força por coulomb** | Calcular o campo de uma carga e a força que um campo faz numa carga, com o sentido certo. | H1, H2, H3 | **P81** | 15 min |
| **2 — Na mesma reta** | Somar campos de cargas alinhadas com P e ver quando eles se cancelam. | H4 | **P8** | 12 min |
| **3 — No plano** | Somar campos com componentes, usar a simetria e dar o ângulo certo. | H5, H6 | **P9, P15** | 18 min |
| **4 — Arcos** | Calcular o campo no centro de um arco carregado somando pedacinhos que estão todos à mesma distância. | H7, H8, H10 | **P29, P26** | 20 min |
| **5 — Barra reta** | Calcular o campo no prolongamento de uma barra, onde cada pedacinho está a uma distância diferente. | H7, H9, H10 | **P31** | 18 min |
| **6 — Disco** | Usar a fórmula do disco, seus limites e o gráfico E/Eₘ × z. | H10, H11 | **P38** | 15 min |

Total dos degraus: cerca de 1 h 50 min; com as 8 questões, cerca de 3 h 30 min (em duas ou três sessões).

**Fora das questões (cartões de visão geral, sem aprofundar):** linhas de campo (resumidas no Degrau 1), dipolo elétrico e seu campo (1/z³), carga em movimento num campo uniforme (impressora a jato de tinta), dipolo num campo (torque, energia, micro-ondas), experimento de Millikan, ruptura dielétrica.

### Sequência didática de cada degrau (exemplo resolvido → exemplo com lacunas → questão)

| Degrau | Exemplo resolvido | Exemplo com lacunas | Checkpoint |
|---|---|---|---|
| 1 | Campo do próton no átomo de H e força no elétron | Gota de Millikan (Problema 39 do livro, gabarito −5e) | Teste 3 do livro + 2 itens |
| 2 | Duas cargas em lados opostos (somam) | Duas cargas do mesmo lado, sinais opostos (cancelam) | Teste 1 do livro + Pergunta 4 |
| 3 | Duas cargas iguais e P na mediatriz (triângulo 3-4-5) | Problema 69 do livro (triângulo equilátero; gabarito 47 e 27 N/C) | Pergunta 3 do livro + ângulo pelo quadrante |
| 4 | Exemplo 22.03 do livro (arco de 120°) | Problema 71 do livro (arco de 2 rad; gabarito 38 N/C) | Teste 2 + Pergunta 11 do livro |
| 5 | Barra de 10 cm, 5,0 nC, P a 5,0 cm da ponta | Problema 67 do livro (gabarito 61 N/C) | 3 itens próprios |
| 6 | Problema 34 do livro (disco, z = 12 cm), com conferência pela carga pontual | Problema 35 do livro (gabarito 0,346 m) | Pergunta 9 do livro + 2 itens |

### Widgets (cada um precedido de uma pergunta de previsão; leitura escondida até a previsão)

| Widget | Degrau | O que faz |
|---|---|---|
| W1 | 1 | Arrasta o ponto P em volta de uma carga ±; mostra o vetor E em P e o valor de E; dobrar r divide por 4 |
| W2 | 2 | Duas cargas numa reta (posição e carga ajustáveis); setas dos dois campos em P e a soma |
| W3 | 3 | Duas cargas ±q simétricas; P sobe no eixo y; componentes, soma e ângulo |
| W4 | 4 | Arco de abertura φ (10° a 360°) com carga Q fixa; E no centro comparado com a carga pontual; modo "metade +, metade −" |
| W5 | 5 | Barra de comprimento L; P no prolongamento; razão E_barra/E_ponto em função de D/L |
| W6 | 6 | Curva E/Eₘ × z/R do disco, com as aproximações de placa infinita e de carga pontual |

## 4. Ordem das questões (da mais fácil à mais difícil)

1. **P81** (Degrau 1): F = qE com peso; sinal da carga; viabilidade.
2. **P8** (Degrau 2): dois pares de cargas alinhados com P; tudo se cancela.
3. **P9** (Degrau 3): duas cargas opostas; P na mediatriz; componente y se cancela.
4. **P15** (Degraus 2 e 3): centro do quadrado; um par se cancela; sobra a diagonal.
5. **P29** (Degrau 4): semicírculo × carga pontual (razão π/2).
6. **P26** (Degrau 4): semicírculo com metades de sinais opostos.
7. **P31** (Degrau 5): barra no eixo; λ; limite de longe.
8. **P38** (Degrau 6): disco; leitura do gráfico; resolver para R.

## 5. Figuras

**Explicativas (SVG inline):**
- Mapa da subida (degraus → questões).
- D0: bola de enxofre no campo atmosférico (pergunta-gancho), sem a resposta.
- D1: carga de prova sondando o campo; vetores E desenhados nos pontos (comprimento ∝ E); linhas de campo de + e de −; F = qE para + e para − num campo uniforme; Teste 3 reconstruído (pág. 105 do PDF).
- D2: regra dos sinais na reta (4 casos); exemplos; Teste 1 reconstruído (pág. 82); Pergunta 4 reconstruída (pág. 115).
- D3: P na mediatriz com componentes; triângulo 3-4-5; quadrantes para o ângulo; Pergunta 3 reconstruída (pág. 115).
- D4: arco dividido em elementos, par simétrico, componentes que se cancelam e que se somam; ds = r dθ; Teste 2 (pág. 99) e Pergunta 11 (pág. 117) reconstruídos.
- D5: barra com elemento dx a distância x de P; gráfico 1/x² (área = integral).
- D6: disco como soma de anéis; anel com dE e componentes; Pergunta 9 reconstruída (pág. 116).
- Síntese: fluxograma "que ferramenta uso?".

**Das questões (reconstruídas a partir do PDF):**
| Figura | Dados | Origem |
|---|---|---|
| 22-36 (P8) | P no vértice de um ângulo reto; q₁ e q₂ a d de P, em lados opostos (diagonal ↖↘); q₃ a d e q₄ a 2d na outra diagonal (↗), do mesmo lado | PDF pág. 120 |
| 22-37 (P9) | −q em x = −3,00 m, +q em x = +3,00 m, P em y = 4,00 m | enunciado + PDF pág. 120 |
| 22-42 (P15) | q₃ na origem, q₁ em (0, a), q₂ em (a, 0), P no centro do quadrado | PDF pág. 122 (bate com o gabarito: 160 N/C a 45°) |
| 22-50 (P26) | semicírculo à esquerda de P: +q no quarto de cima (2º quadrante), −q no de baixo (3º) | PDF pág. 125 |
| 22-52 (P29) | (a) semicírculo à esquerda de P; (b) carga pontual à esquerda, a R de P | PDF pág. 126 |
| 22-54 (P31) | barra no eixo x, à esquerda; P à direita, a uma distância a da ponta direita | PDF pág. 127 |
| 22-58 (P38) | (a) disco; (b) gráfico E × z: eixo z de 0 a zₛ = 8,0 cm em 4 divisões de 2,0 cm; linhas em Eₘ e 0,5Eₘ; a curva cruza 0,5Eₘ em **z = 4,0 cm** | PDF pág. 129, ampliado a 300 dpi; conferido em mais dois pontos da curva (z = 2 cm: 0,72; z = 8 cm: 0,24), que batem com R = 6,93 cm |

Nenhuma figura das questões ficou com dúvida: todas foram conferidas no PDF. O P81 não tem figura no livro; o guia desenha o diagrama de forças só dentro da Dica 2.

## 6. Decisões tomadas sem perguntar ao usuário

1. **"Atividades 8, 9, 15, 26, 29, 31, 38 e 81" = Problemas.** As Perguntas do capítulo vão só até 14 e o 81 só existe nos Problemas (Adicionais).
2. **Constantes:** k = 8,99 × 10⁹ N·m²/C², e = 1,602 × 10⁻¹⁹ C, ε₀ = 8,85 × 10⁻¹² C²/(N·m²), g = 9,8 m/s² (as do livro).
3. **P38:** o valor "E = 0,5Eₘ em z = 4,0 cm" só existe no gráfico. Foi lido no PDF (não precisou de web nem do usuário) e conferido com a forma da curva. A legenda diz isso.
4. **P81(b):** o gabarito diz "a esfera seria desintegrada pela repulsão". O guia mostra as contas que sustentam isso e acrescenta a ruptura do ar (o campo na superfície passaria de 10¹¹ N/C, contra 3 × 10⁶ N/C de ruptura). Para estimar o raio da esfera, usa a densidade do enxofre, 2,07 g/cm³ (dado que não está no livro; valor de tabela). A resposta (b) é conceitual, então esse dado não muda a resposta do gabarito.
5. **P31(c):** o gabarito diz −180°. O guia aceita 180° ou −180° (é a mesma direção) e diz isso.
6. **P26:** a resposta não depende de o semicírculo estar à esquerda ou à direita de P; o guia desenha como no livro (à esquerda) e usa isso como pergunta "e se".
7. **Exemplos com lacunas** tirados de Problemas ímpares do livro que não estão na lista (39, 67, 69, 71, 35): têm gabarito, então o aluno confere. O plano de revisão usa outros ímpares (5, 7, 11, 23, 25, 27, 37, 41, 63, 87).
8. **Lições do Capítulo 21 aplicadas desde a v1** (da `consolidacao.md` daquele guia): leitor de número que aceita vírgula, ×10^, sobrescritos, π, √ e frações; respostas e gabaritos só aparecem depois de conferir; feedback por alternativa; alternativas certas espalhadas entre a, b, c, d; caixa de constantes nas questões; leitura dos widgets escondida até a previsão; sinal sempre escrito (não só a cor); CSS do SVG restrito às figuras (para não deformar o KaTeX); equações longas quebradas no celular.
9. **Ferramenta de leitura para os alunos-agente** (`rodada-1/ler_guia.py`): no Cap. 21, os alunos-agente leram o HTML cru e viram as respostas antes da hora. Agora eles leem o guia por uma ferramenta que mostra só o que a página mostra, libera a ajuda um nível por vez e confere respostas, sem revelar o gabarito.
