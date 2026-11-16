# Plano — Guia do Capítulo 21: A Lei de Coulomb

**Questões pedidas:** Problemas 7, 10, 21, 23, 42, 50 e 73.
**Fonte:** `halliday-v3/cap-21-a-lei-de-coulomb.md` + `gabarito.md` + PDF original (`../FIsica 3 Eletromagnetismo Halliday.pdf`, págs. 35–72), usado só para ver as figuras que a conversão perdeu.

| Questão | Dificuldade (livro) | Gabarito oficial |
|---|---|---|
| P7 | ·· | −4,00 |
| P10 | ·· | — (par) |
| P21 | ··· | 3,8 × 10⁻⁸ C |
| P23 | ··· | (a) 0; (b) 12 cm; (c) 0; (d) 4,9 × 10⁻²⁶ N |
| P42 | adicional | — (par); o P43 ímpar, (b) 3,1 cm, serve de conferência |
| P50 | adicional | — (par) |
| P73 | adicional | (a) 2,19 × 10⁶ m/s; (b) 1,09 × 10⁶ m/s; (c) diminuiria |

---

## 1. Habilidades (matriz questão × habilidade)

| Código | Habilidade |
|---|---|
| H1 | Calcular o **módulo** da força de Coulomb (converter µC, nC e cm; elevar r ao quadrado; ordem de grandeza) |
| H2 | Decidir o **sentido** da força pelo desenho (sinais iguais repelem, opostos atraem), sem confiar no sinal algébrico da Eq. 21-4 |
| H3 | Somar forças na mesma reta com sinal (componente x) |
| H4 | Achar onde a força resultante se anula (análise por regiões: entre as cargas × fora delas) |
| H5 | Decompor forças no plano (diagonal = a√2, componentes com cos/sen, quadrante do ângulo) |
| H6 | Usar simetria para ver quais componentes se cancelam |
| H7 | Escrever a força como função da posição F(x) e analisar casos-limite (x = 0, x → ∞) |
| H8 | Achar máximo e mínimo com derivada (regras do quociente e da cadeia) e conferir as bordas do intervalo |
| H9 | Pôr a força elétrica no diagrama de corpo livre junto com T e mg (ΣF = 0) |
| H10 | Usar a força elétrica como força centrípeta (MCU) |
| H11 | Equilíbrio de torques com forças elétricas (corpo rígido) |
| H12 | Aproximação de ângulo pequeno (tan θ ≈ sen θ ≈ θ) e saber quando ela vale |
| H13 | Calcular a carga total a partir de uma densidade ρ variável (dq = ρ dV; casca fina dV = 4πr² dr; integral) |
| H14 | Resolver em símbolos antes de pôr números; verificar unidade, sinal e casos-limite |

| | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 | H10 | H11 | H12 | H13 | H14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **P7** | ● | ● | ● | ● | | | | | | | | | | ● |
| **P73** | ● | | | | | | | | | ● | | | | ● |
| **P42** | ● | ● | | | | | | | ● | | | ● | | ● |
| **P50** | ● | ● | | | | | | | ● | | ● | | | ● |
| **P10** | ● | ● | | | ● | ● | | | | | | | | ● |
| **P23** | ● | ● | | | ● | ● | ● | ● | | | | | | ● |
| **P21** | | | | | | | | | | | | | ● | ● |

## 2. Pré-requisitos

- **Física 1:** vetores e componentes (cap. 3), 2ª lei de Newton e diagrama de corpo livre (cap. 5), força centrípeta e MCU (cap. 6), torque e equilíbrio de corpo rígido (cap. 12), lei da gravitação (cap. 13: mesma forma da lei de Coulomb).
- **Matemática:** notação científica e prefixos (m, µ, n, p); trigonometria (sen, cos, tan, ângulo de 45°, diagonal do quadrado); derivada (regra do quociente e da cadeia, ponto crítico); integral de potência (∫ r dr); área da esfera (4πr²) e volume ((4/3)πr³).
- O Degrau 0 tem um teste rápido de 6 itens, um por pré-requisito, com mini-revisão para quem errar.

## 3. Degraus (do concreto ao abstrato)

| Degrau | Objetivo (1 frase) | Habilidades | Desbloqueia | Tempo |
|---|---|---|---|---|
| **0 — Aquecimento** | Ver que a força elétrica é gigantesca, mas quase sempre se cancela, e checar os pré-requisitos. | — | — | 8 min |
| **1 — Duas cargas** | Calcular o módulo da força entre duas cargas e desenhar o sentido sem errar o sinal. | H1, H2, H14 | (base de tudo) | 12 min |
| **2 — Muitas cargas numa reta** | Somar forças na mesma reta e achar onde a resultante se anula. | H3, H4 | **P7** | 12 min |
| **3 — A força elétrica na mecânica** | Usar a força de Coulomb em ΣF = 0, em F = mv²/r e em Στ = 0. | H9, H10, H11, H12 | **P73, P42, P50** | 15 min |
| **4 — Muitas cargas no plano** | Decompor forças e usar a simetria para ver o que se cancela. | H5, H6 | **P10** | 15 min |
| **5 — Força que depende da posição** | Escrever F(x), ler os casos-limite e achar o máximo com derivada. | H7, H8 | **P23** | 15 min |
| **6 — Carga espalhada** | Somar a carga de cascas finas quando a densidade varia (integral). | H13 | **P21** | 12 min |

Total: ≈ 1 h 30 de degraus + ≈ 1 h 30 de questões.

**Cartão de visão geral (sem aprofundar)**, porque nenhuma questão usa estes tópicos: condutores e isolantes, carga induzida, aterramento, esferas iguais que se tocam e dividem a carga, teoremas das cascas, corrente i = dq/dt, conservação da carga.

Cada degrau começa num fenômeno ou numa analogia, passa por uma figura e só então chega à equação. Os exemplos esmaecem assim:

| Degrau | Exemplo resolvido | Exemplo com lacunas | Questão sozinho |
|---|---|---|---|
| 1 | P5 (2,81 N, tem gabarito) | P3 (1,39 m, tem gabarito) | — |
| 2 | Ex. 21.02 (x = 2L) | P13 (−14 cm, tem gabarito) | P7 |
| 3 | Pêndulo com carga fixa ao lado (θ = 16,0°) + mini-exemplo de torque (1,80 N) | P52 (MCU em torno de Q: Q = −1,11 × 10⁻⁵ C) | P73, P42, P50 |
| 4 | Ex. 21.01c (1,78 × 10⁻²⁴ N, 94,0°) | P11 (mesma figura do P10; 0,17 N e −0,046 N, tem gabarito) | P10 |
| 5 | Dipolo no eixo y e carga no eixo x (máximo em x = 0) | Máximo de x/(x² + a²) com derivada | P23 |
| 6 | P51(b) (barra com ρ = bx²; 1,33 × 10¹⁰ elétrons, tem gabarito) | Casca com ρ uniforme: a integral reproduz (4/3)π(r₂³ − r₁³)ρ | P21 |

## 4. Ordem das questões (presas aos degraus, da mais fácil à mais difícil dentro do que já foi ensinado)

1. **P7** (após D2): 1D, uma igualdade de módulos.
2. **P73** (após D3): uma força só, MCU.
3. **P42** (após D3): DCL com 3 forças + geometria + ângulo pequeno + demonstração.
4. **P50** (após D3): torque com duas forças elétricas + condição extra.
5. **P10** (após D4): 2D, diagonal, simetria, item (b) de raciocínio.
6. **P23** (após D5): 2D + função F(x) + derivada.
7. **P21** (após D6): integral em cascas.

## 5. Figuras

**Explicativas** (todas em SVG inline, desenhadas pelo guia):
- D0: mapa da subida (escada com degraus, conceitos e questões).
- D1: par de cargas com setas (repulsão e atração, mesmo módulo, 3ª lei); "lei do inverso do quadrado" (a mesma influência espalhada numa esfera de área 4πr²).
- D2: regiões do eixo (entre as cargas / fora) com as setas, mostrando onde a força pode se anular.
- D3: DCL da bolinha pendurada (T, mg, F); órbita de Bohr; gangorra com torque.
- D4: decomposição de uma força em componentes; quadrado com diagonal a√2 e as forças sobre a partícula 1.
- D5: gráfico F(x) com x = 0, x = d/√2 e cauda 1/x².
- D6: cebola de cascas finas (r, dr, dV = 4πr²dr).
- Síntese: fluxograma "que ferramenta uso?".

**Widgets** (sliders, valores e gráficos ao vivo): D1 par de cargas (F × r); D2 ponto de força nula na reta; D3 pêndulo (x × q, exato × ângulo pequeno); D4 quadrado (forças sobre 1 em função de Q/q); D5 F(x) para cargas iguais × opostas; D6 soma de N cascas convergindo para a integral.

**Figuras das questões** (reconstruídas em SVG a partir do PDF do livro, que foi consultado):

| Figura | Questão | De onde vêm os dados |
|---|---|---|
| 21-23 | P7 | PDF pág. 59: ordem 1–2–3 no eixo x, cotas L₁₂ e L₂₃. Confirmada também pelo gabarito (−4,00 só sai com 3 à direita de 2). |
| 21-25 | P10 | PDF pág. 60: 1 em cima à esquerda, 2 em cima à direita, 3 embaixo à esquerda (origem), 4 embaixo à direita; lado a. Confirmada pelo gabarito do P11 (0,17 N; −0,046 N), que o calculos.py reproduz. |
| 21-32 | P23 | PDF pág. 64: 1 em y = +d, 2 em y = −d, 3 no eixo x. |
| 21-39 | P42 | PDF pág. 68: dois fios de comprimento L presos no mesmo ponto, ângulo θ de cada lado da vertical, esferas q separadas por x. |
| 21-42 | P50 | PDF pág. 69: **+q na ponta esquerda, +2q na direita**, bloco P pendurado à direita do apoio, a uma distância x da ponta esquerda; +Q a uma distância h abaixo de cada esfera. |
| — | P21 | O livro não tem figura. Figura explicativa da casca (r₁ = 4 cm, r₂ = 6 cm, casca fina dr), marcada como "figura do guia". |
| — | P73 | O livro não tem figura. Figura explicativa das órbitas n = 1 e n = 2 (escala r = n²a₀), marcada como "figura do guia". |

Nenhuma figura precisou do selo "⚠ reconstrução aproximada": todas foram conferidas no PDF.

## 6. Decisões tomadas sem perguntar ao usuário

1. **"Atividades 7, 10, 21, 23, 42, 50, 73" = Problemas.** As Perguntas do cap. 21 só vão até 12, e o gabarito do Problema 7 (−4,00) bate com a interpretação.
2. **P50:** o texto convertido (e o PDF em português) diz "nas extremidades **direita e esquerda** … q e 2q, **respectivamente**", mas a figura do próprio livro mostra **+q à esquerda e +2q à direita**, como no original em inglês. O guia segue a figura, avisa a troca no enunciado e mostra no "e se…" o que muda se as cargas forem trocadas (o x muda de sinal no termo de correção; o h do item (b) não muda).
3. **P42:** o livro escreve "tan θ ≤ sen θ", que é erro de digitação de "tan θ ≈ sen θ". O enunciado limpo corrige.
4. **Constantes:** k = 8,99 × 10⁹ N·m²/C², ε₀ = 8,85 × 10⁻¹² C²/(N·m²), e = 1,602 × 10⁻¹⁹ C, mₑ = 9,109 × 10⁻³¹ kg (tabela do livro), g = 9,8 m/s².
5. **P23:** o intervalo é 0 ≤ x ≤ 5,0 m. O mínimo é em x = 0 (F = 0), não em x = 5,0 m (lá F = 1,5 × 10⁻²⁸ N, que é pequeno mas não zero).
6. **P50, hipóteses:** a barra é longa (L ≫ h), então se desprezam as forças "cruzadas" (+q com o +Q da direita, +2q com o +Q da esquerda); a repulsão entre +q e +2q é interna à barra e se cancela.
7. **P42 e P50 (simbólicos)** ganham, além das alternativas, uma conferência numérica: o aluno põe valores-teste na expressão dele (P50: x = 59,0 cm e h = 7,34 cm com L = 1,00 m, q = 1,00 µC, Q = 2,00 µC, h = 10,0 cm, P = 10,0 N).
8. **Ex. 21.01c:** o guia reproduz o arredondamento intermediário do livro (F₁₂ = 1,15 × 10⁻²⁴ N e F₁₄ = 2,05 × 10⁻²⁴ N antes de somar). Sem esse arredondamento, Fx = −1,28 × 10⁻²⁵ N e θ = 94,1°, e isso aparece numa nota.
9. **Tolerância das respostas:** 2 % relativa; resposta zero usa tolerância absoluta (P23: 0,5 cm e 10⁻³⁰ N).

---

## 7. Verificação da v1

1. **`calculos.py`** (`python3 -I calculos.py`): roda sem erro e não aponta divergência > 2 %. Cinco comparações ficam acima de 2 % só porque o gabarito tem 2 algarismos significativos (P33, Ex. 21.04a/b, P13); com a precisão do gabarito elas batem, e o script marca "ok (igual com 2 alg. signif.)". No Ex. 21.01c, o livro arredonda F₁₂ e F₁₄ antes de somar; o guia reproduz isso e mostra, numa nota, o valor sem arredondar (−1,28 × 10⁻²⁵ N; 94,1°). O script também pegou um erro meu: um distrator da Revisão 2 dizia "18 N" quando kₑ/r² = 1,8 × 10¹⁰ N. Corrigido.
2. **Cobertura:** as 7 questões estão no guia (P7, P73, P42, P50, P10, P23, P21), cada uma com os 5 níveis marcados com `data-questao`/`data-nivel` (35 blocos) e com figura (5 reconstruídas do PDF + 2 "figura do guia", porque o livro não tem figura no P21 nem no P73).
3. **Navegador** (Playwright/Chromium, servidor local):
   - Console: nenhum erro (o 404 do favicon foi resolvido com um favicon embutido). KaTeX: 1111 fórmulas renderizadas, 0 erros.
   - Ajuda: os 35 blocos começam fechados; só a Dica 1 começa habilitada. O 1º clique sem o roteiro marcado destaca o lembrete; o 2º abre. Os níveis abrem em ordem; a reflexão aparece depois do nível 4.
   - Respostas: "4" no P7 → "o módulo está certo, mas o sinal não"; "2,19e4" no P73a → "fator de 10⁻²"; "2,19×10⁶" (sobrescrito) é aceito.
   - Widgets: travados até a previsão; depois respondem aos sliders (W1 a W6 testados, valores conferidos).
   - Checkpoint, calibração e progresso se atualizam; as lacunas são conferidas.
   - Layout: a 1280 px, sem rolagem lateral. A 390 px havia rolagem lateral de 48 px (equação longa dentro da grade de duas colunas); corrigido com `min-width: 0`, agora sem rolagem. Os títulos do mapa estouravam as caixas e os botões de ajuda quebravam em 3 linhas no celular; ambos corrigidos.
   - Tema escuro e impressão capturados.
   - Capturas em `rodada-1/telas/` (`desktop-*.png`, `celular-*.png`, `escuro-*.png`, `impressao-topo.png`), com o altímetro fixo desligado só durante a captura.
