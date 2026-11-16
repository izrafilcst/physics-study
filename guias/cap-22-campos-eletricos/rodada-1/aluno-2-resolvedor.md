# Relatório do Aluno 2 (Resolvedor, prova amanhã): Cap. 22, rodada 1

Escopo: P81, P8, P9, P15, P29, P26, P31, P38, nessa ordem. Não abri nenhum nível de ajuda (`ajuda/<Q>-n.md`). Não abri `guia-v1.html`, `calculos.py`, `plano.md` nem o livro. Não usei Bash: as contas foram feitas à mão. Não fiz as perguntas de revisão intercalada (rev-1 a rev-6), que estão fora da lista.

## Ordem real do meu trabalho (importante para ler o relatório)

- Li o enunciado e a figura de cada questão, tentei sozinho, anotei a resposta e a confiança, e só depois abri a conferência.
- Li a teoria dos degraus 1 a 6 **depois** de ter respondido as oito questões. Por isso as citações de "bloco que me ensinou" abaixo dizem o que o guia ensina, não o que eu usei antes de resolver. Tudo o que fiz antes da teoria saiu de física básica e da leitura do enunciado.
- **Falha de protocolo:** abri `conferir/P9-a.md` junto com `conferir/P8-a.md`, antes de ter escrito minha resposta de P9. O valor de P9-a ficou visível para mim, então o acerto de P9-a não conta como resolução limpa.

## 1. Itens de crítica

| # | Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|---|
| 1 | Degrau 5, bloco "A conta" (linha ~649), e tabela "Equações do capítulo" (linha ~1066) | dica entrega demais | atrapalha | A integral de 1/x² é feita por extenso (`k λ (1/a − 1/(a+L)) = kq/(a(a+L))`) e a fórmula fechada aparece também na tabela. P31-b vira substituição de números, mas o enunciado de P31 diz "integral com a distância variando". | Mostrar só `E = kλ∫dx/x²` e deixar o fechamento para a conferência ou para o P31 pedir a integral. Tirar a fórmula fechada da tabela até depois da questão. |
| 2 | `conferir/P31-b.md`, mensagem para o valor 0,001472 | dica entrega demais | atrapalha | "Use kq/(a(a+L))." O erro comum (distância ao centro) já é identificado, e a mensagem entrega a fórmula que a questão quer que o aluno construa. | Trocar por: "Você usou a distância ao centro; de perto erra cerca de 7 %. Escreva a integral de a até a+L e avalie." |
| 3 | Enunciado de P31 (letra a) | termo não definido / confuso | atrapalha | "a = 12,0 cm" em (b) e (c) e "a = 50 m" em (d) e (e). A mesma letra vale duas distâncias no mesmo problema. | Chamar a distância de 50 m de D (ou de d) e manter a = 12,0 cm. |
| 4 | `telas/desktop-p31.png` | figura confusa | polimento | Um símbolo "x" aparece sobreposto às setas de cota do L, na ponta direita da barra. Parece uma marca de erro ou rótulo perdido. | Remover o "x" ou separar a cota L da marca da ponta. |
| 5 | Degrau 3, "Erros comuns" (linha ~453) | dica entrega demais | polimento | "No centro de um quadrado de lado a, r = a/√2." É exatamente o passo de distância que P15 quer que o aluno encontre. | Tirar essa frase do erro comum e colocá-la na Dica 1 do P15, sem o valor pronto. |
| 6 | `conferir/P8-a.md`, mensagem para 288 | dica entrega demais | polimento | "288 → ... E o parceiro dela do outro lado?" Quem chega a 288 já recebe a ideia do cancelamento. | Trocar por uma pergunta sobre o sentido das setas de q1 e q2 em P, sem nomear o parceiro. |
| 7 | Síntese, "Que ferramenta uso" (linha ~1054) | termo não definido | polimento | "procure pares que se cancelam (lado + sinal, e |q| ∝ r²)". A expressão "lado + sinal" não está definida ali. A regra completa está no Degrau 2, linhas ~258 a 264, mas a síntese não aponta para esse bloco. | Escrever "(regra de bolso do Degrau 2)" ou repetir a regra por extenso. |
| 8 | `conferir/P9-a.md`, mensagem para 1,841e-10 | termo não definido | polimento | "Sobram as x: o fator é 3/5." O fator não aparece ligado à regra do Degrau 3, `E_x = E·Δx/r`. | Escrever: "Δx/r = 3/5; E_x = E·Δx/r." |
| 9 | Degrau 4, bloco de semicírculo (linha ~518) | dica entrega demais | polimento | `E = 2kQ/(πR²)` para o semicírculo já vem escrito. P29 vira a razão de duas expressões dadas, e não há passo de integração. | Para P29, pedir a derivação, ou usar outra abertura (quarto de círculo) que não esteja tabelada. |
| 10 | `conferir/P38-a.md`, mensagem para 4 | dica entrega demais | polimento | "4,0 cm é o z em que o campo cai à metade." Entrega a leitura do gráfico, que é o núcleo de P38 ("leitura de gráfico"). | Trocar por "Confira em qual linha vertical da grade a curva cruza a linha de 0,5 Eₘ." |
| 11 | `conferir/P26-b.md` e enunciado de P26-b | termo não definido | polimento | "orientação (em relação ao semieixo x positivo)" não diz a faixa. A conferência aceita −90° e 270° como equivalentes, mas o campo de entrada não avisa isso. | Escrever "entre 0° e 360°" ou "vale qualquer equivalente". |
| 12 | Síntese de P31 e P8 (ajuda ao aluno) | falta prática | polimento | Não há um passo de checagem por conta própria antes da conferência. Na P8, o zero veio de cancelamento total; um aluno que leu "zero" como erro não tem como saber se é cancelamento ou falha. | Acrescentar uma checagem: "Se o resultado der zero, confira se os pares que se cancelam têm o mesmo |q|/r²." |

Não encontrei nenhum item que bloqueasse a resolução. Todas as constantes estão no guia (k, ε₀, e, g, em "Constantes (as do livro)" e na ficha do Degrau 1), então não há LACUNA de constante. A Síntese e a teoria de cada degrau cobrem os passos que usei, com as exceções abaixo.

**LACUNA:** nenhuma marcada como LACUNA real. Ao isolar R em P38 (z/√(z²+R²) = 1/2, então R² = 3z²), o passo algébrico só aparece no bloco "Agora você completa: Problema 35" (lacuna lac-d-2). Está no mesmo degrau, então não é lacuna, mas é a mesma álgebra de P38 com números diferentes. Fica registrado como observação, não como lacuna.

## 2. Perguntas ao Professor

1. Professor, por que a fórmula fechada `kq/(a(a+L))` aparece no Degrau 5 e na tabela de equações se o P31 diz "integral com a distância variando"? Eu cheguei à resposta de P31 só trocando números, e isso não treina a integral.
2. Professor, por que P26-b aceita −90° e 270° sem avisar? Se o aluno escrever 270° e a conferência disser que está certo, ele não aprende que as duas expressões são iguais. Isso devia estar no enunciado.
3. Professor, na P38, de onde sai "cada divisão vale 2 cm" se o eixo só tem 0 e z_s numerados? O guia diz que a grade tem quatro partes, mas a leitura do z = 4 cm depende de eu contar a grade certo. Dá para pôr o valor 2 cm no gráfico?
4. Professor, por que o P8 aceita a resposta zero sem pedir que o aluno justifique o cancelamento? Eu acertei, mas poderia ter chutado zero por outro motivo.
5. Professor, na P9-a a conferência fala em "o fator é 3/5", mas a regra `E_x = E·Δx/r` do Degrau 3 é o que deveria ser usado. Por que a dica não aponta para ela?

## 3. Placar

Nenhuma ajuda foi aberta. Todas as oito questões foram feitas "sem ajuda". Abaixo, minha resposta, a confiança (1 a 3) e se bateu com a conferência.

| Questão | Campo | Minha resposta (conf.) | Conferência | Bateu? |
|---|---|---|---|---|
| P81 | (a) carga | −2,93×10⁻² C (2) | −0,02933 C | sim |
| P81 | (b) alternativa | d (2) | d (certa) | sim |
| P8 | (a) \|E\| | 0 N/C (3) | 0 N/C | sim |
| P9 | (a) \|E\| | 1,38×10⁻¹⁰ N/C (2) | 1,381×10⁻¹⁰ N/C | sim (P9-a contaminado, ver protocolo) |
| P9 | (b) θ | 180° (3) | 180° | sim |
| P15 | (a) \|E\| | 160 N/C (2) | 160 N/C | sim |
| P15 | (b) θ | 45° (2) | 45° | sim |
| P29 | razão | π/2 ≈ 1,571 (3) | 1,5708 | sim |
| P26 | (a) \|E\| | 20,6 N/C (2) | 20,6 N/C | sim |
| P26 | (b) θ | 270° (−90°) (2) | −90° | sim |
| P31 | (a) λ | −5,19×10⁻¹⁴ C/m (3) | −5,19e-14 C/m | sim |
| P31 | (b) \|E\| em P | 1,57×10⁻³ N/C (2) | 1,573e-3 N/C | sim |
| P31 | (c) θ | 180° (2) | 180° | sim |
| P31 | (d) barra a 50 m | 1,52×10⁻⁸ N/C (2) | 1,521e-8 N/C | sim |
| P31 | (e) partícula a 50 m | 1,52×10⁻⁸ N/C (2) | 1,521e-8 N/C | sim |
| P38 | R | 6,93 cm (2) | 6,928 cm | sim |

Resumo do placar por questão:
- P81: resolvida sem ajuda.
- P8: resolvida sem ajuda.
- P9: resolvida sem ajuda (P9-a com a falha de protocolo).
- P15: resolvida sem ajuda.
- P29: resolvida sem ajuda.
- P26: resolvida sem ajuda.
- P31: resolvida sem ajuda.
- P38: resolvida sem ajuda.

Nenhuma questão ficou "com ajuda até o nível N" ou "não resolvida". Os 17 campos bateram com a conferência.

## 4. Passos e onde o guia ensina cada um (citação feita depois de ler a teoria)

- P81: F = qE e sinal da carga (Degrau 1, "Campo = força por coulomb", bloco "A ideia" e Eq. 22-28; e a Síntese, primeiro bullet). Equilíbrio com o peso (Checkpoint 1, pergunta pre6, e o bloco de equilíbrio).
- P8: campos alinhados, cancelamento e regra de bolso (Degrau 2, "Na mesma reta", bloco "A ideia" e a regra de bolso logo após a figura 2-1; "módulo empatar" com |q| ∝ r²).
- P9: componentes pelo triângulo 3-4-5 e ângulo pelo quadrante (Degrau 3, "No plano", bloco "O truque da geometria": E_x = E·Δx/r, e "Faça em três passos" para o ângulo).
- P15: cancelamento de um par (Degrau 2, mesma regra de bolso) e distância ao centro do quadrado (Degrau 3, "Erros comuns", r = a/√2).
- P29: campo de semicírculo no centro (Degrau 4, bloco "O método do elemento", caso semicírculo). Razão com a carga pontual, Eq. 22-3 (Degrau 1).
- P26: arco com sinais opostos (Degrau 4, "E se as metades tiverem sinais opostos?"), e λ = q/(πr/2) do método do elemento. A componente que sobra é a y.
- P31: λ com sinal (Degrau 4, "Ficha das grandezas novas", λ = Q/L). Campo de barra no prolongamento (Degrau 5, "A conta", fórmula fechada). Limite "de longe" (Degrau 5, "De longe, a barra vira um ponto").
- P38: campo do disco no eixo, Eq. 22-26 (Degrau 6, "A ideia" e a Eq. 22-26), e a leitura de E/Eₘ contra z (Degrau 6, "O que isso faz com os gráficos").

**LACUNA**: nenhuma marcada.

## 5. O que funcionou (para manter na versão 2)

- A ficha de constantes (k, ε₀, e, g) antes das questões. Sem ela, P8 e P31 teriam exigido procurar valores.
- As conferências com valor esperado e mensagens por erro específico, por exemplo "Sentido invertido" em P9-b, P15-b e P26-b. Elas apontam o erro de sinal sem entregar o resultado.
- A figura de P8 e a de P38, que trazem as informações necessárias (ângulo reto em P, divisões do eixo) sem ambiguidade.
- A regra de bolso do Degrau 2 e a regra das componentes do Degrau 3, que bastaram para resolver P8, P9 e P15 sem ajuda.
- A distinção "Eₘ = σ/(2ε₀), não σ/ε₀" (Degrau 6, "Erros comuns"), que evitou o erro mais provável em P38.
- O enunciado de P81 com a pergunta conceitual (b) separada da conta (a). Tentei sozinho e acertei as duas partes.
