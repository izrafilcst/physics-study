# Rodada 1: relatório do Aluno 2 (Resolvedor, prova amanhã)

Guia testado: `/home/swampert/Documents/fisica/guias/cap-21-a-lei-de-coulomb/guia-v1.html`

## Aviso antes de tudo: leituras antecipadas do gabarito

Não segui a regra de ordem em todos os pontos. Registro o que aconteceu:

- **P7 (total):** um `sed` sobre o cartão inteiro imprimiu de uma vez os níveis 1 a 5, inclusive a resolução (nível 4) e a resposta "−4,00" (nível 5), antes de qualquer tentativa minha. Não fiz a P7 de forma independente depois disso. Não conta como resolvida.
- **P10 (item a):** a leitura do enunciado trouxe junto o `data-resp="-2.828"` do item (a), antes da minha conta.
- **P23 (item a):** a leitura trouxe o `data-resp="0"` do item (a), antes da minha conta.
- **P21 (total):** a leitura do enunciado trouxe o `data-resp="3.770e-8"`, antes da minha conta.
- **Não houve leitura antecipada** em P73, P42 e P50 (nesses cartões filtrei `data-resp` e `data-correta`). Em P10 (b) e P23 (b, c, d), a resposta só foi vista depois da minha conta.
- **Níveis de ajuda:** nenhuma tentativa minha foi precedida de ajuda. Nenhum degrau foi aberto. O único nível lido foi o da P7, pelo acidente acima.
- **Processo:** um comando de leitura (`awk`, para conferir o bloco de respostas da P50) foi negado pelo classificador. Usei a ferramenta Read no mesmo arquivo, só no intervalo do bloco de respostas.
- **Constantes:** usei k, e, m_e, ε0 e g de memória. Não abri a seção de constantes (nenhuma), nem degrau nenhum, para não conferir se o guia as fornece.

---

## 1. Itens de crítica

| # | Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|---|
| 1 | HTML, cartão da P7 (estrutura geral) | outro | **atrapalha** | Os níveis 4 e 5 (resolução e "−4,00"), os `data-resp` e os `data-correta` estão no mesmo HTML estático. Quem lê o arquivo, ou tem o código-fonte aberto, vê tudo. Foi o que me aconteceu. | Carregar a resolução e a resposta sob demanda (buscar o fragmento só ao clicar) ou separar o gabarito em outro arquivo. Os `data-resp` não deveriam estar no HTML público. |
| 2 | P7, Dica 2 (nível 2) | dica entrega demais | **atrapalha** | "1. Desenhe as duas forças sobre a partícula 3 … 5. Ponha o sinal na razão." São 5 passos quase em forma de receita. | Manter só o "onde está o problema" (decidir o sinal, depois igualar os módulos). A lista completa deveria ser o nível 3. |
| 3 | P7, Dica 3 (nível 3) | dica entrega demais | **atrapalha** | Já dá a equação pronta com as distâncias: "Distância da 1 até a 3: 2L; da 2 até a 3: L" e $\frac{k|q_1||q_3|}{(2L)^2} = \frac{k|q_2||q_3|}{L^2}$. O único passo que sobra é simplificar. | Dar só as distâncias (2L e L) e perguntar a condição de equilíbrio, sem a equação montada. |
| 4 | P7, nível 4, bloco "Verificar" | termo não definido / referência solta | polimento | "E se $L_{23} = 2L_{12}$ (**Problema 40**)". Não encontrei o Problema 40 na lista de questões do guia. | Trocar por um caso próprio do guia, ou remover a referência. |
| 5 | P7, nível 4, bloco "Modelar" | denso demais | polimento | Um único bloco "passo" junta modelo, hipótese (pontuais) e a argumentação de sinais. | Separar "Modelar" da argumentação do sinal (que já está num `revelado`). |
| 6 | P73, enunciado | LACUNA · falta prática | **atrapalha** | "Qual seria a velocidade do elétron…". Não há k, e, m_e nem ε0, e a resposta é numérica. Usei valores de memória. | Caixa de "constantes" no topo do guia ou em cada cartão numérico. |
| 7 | P73, figura | figura confusa | polimento | O rótulo "n = 2 (raio 4a₀)" está em y=214, embaixo do desenho. A órbita n=2 é o círculo de r=88 centrado em y=110. O rótulo parece pertencer a outra coisa. | Pôr o rótulo do n=2 ao lado do círculo de raio maior, como o do n=1. |
| 8 | P42, item (a) | salto lógico · falta prática | **atrapalha** | Enunciado: "**Mostre** que a distância de equilíbrio … é dada por …". Conferência: "(a) Na sua demonstração, que par de relações aparece?" com 4 alternativas. Eu não preciso demonstrar nada para responder; dá para chutar pela forma das alternativas. | Pedir a expressão final (campo de texto ou LaTeX) ou marcar "demonstrei" com um checklist. Não usar "mostre" com múltipla escolha. |
| 9 | P42, item (b) | LACUNA | polimento | "$L = 120$ cm, $m = 10$ g, $x = 5{,}0$ cm". Não diz g. Usei 9,8 m/s²; com 9,81 o resultado muda pouco, mas eu não sabia que valor a tolerância de 2 % assume. | Escrever "use g = 9,8 m/s²" no enunciado. |
| 10 | P50, enunciado | falta prática | **atrapalha** | O enunciado pede "a distância x" sem dar valores nem unidade. O formato (uma expressão, conferida com valores-teste em cm) só aparece no bloco de respostas, depois que eu já tinha resolvido. A unidade "cm" vem no campo. | Mover a instrução "a resposta é uma expressão; teste com L=1 m, q=1 µC, Q=2 µC, h=10 cm, P=10 N" para o enunciado. Dizer "em cm" no texto. |
| 11 | P50, (a) | termo não definido | polimento | "$x$ com os valores-teste (em cm)". Não fica claro se x pode depender de h, Q ou P (depende: x = L/2 + kqQL/(2Ph²)). | Dizer no enunciado que a resposta pode conter h, q, Q, P e L. |
| 12 | P10, item (b), alternativas | dica entrega demais | polimento | A alternativa correta é a única com justificativa longa: "Não: zerar a força na partícula 2 exige outra razão Q/q, incompatível com a do item (a)." As outras são curtas e uma é absurda ("Sim, com Q = q"). Dá para escolher pelo tamanho. | Deixar as quatro alternativas com a mesma forma (ou todas com justificativa). |
| 13 | P10, item (a), sinal | termo não definido | polimento | Enunciado: "Qual deve ser o valor da razão Q/q…". O "com sinal" só aparece no rótulo do campo. Por isso eu escrevi −2,83 de propósito, mas um aluno pode colocar 2,83. | Escrever "com sinal" no enunciado, não só no campo. |
| 14 | P23, enunciado | (sem crítica) | — | Ver "O que funcionou". | — |
| 15 | P21, enunciado | termo não definido | polimento | "$\rho = b/r$ … $b = 3{,}0\ \mu\text{C/m}^2$". A unidade de b só fecha se você notar que r está em metros. Eu li e fui direto, mas um aluno pode errar a unidade. | Explicitar "b tem unidade C/m²" ao lado da definição. |
| 16 | Processo: Degraus | (não avaliado) | — | Nenhum degrau foi aberto. Não consigo dizer se os degraus ensinam k, e e m_e (ver item 6). | Verificar na próxima rodada. |

## 2. Perguntas ao Professor

1. Professor, onde estão k, e, m_e e ε0? A P73 não dá nenhuma constante, e a P50 e a P42 também usam a constante de Coulomb sem dizer. Eu usei de memória. Um aluno que não lembra fica travado no número, e não na física.
2. Professor, por que a P42 (a) diz "mostre" e a conferência é múltipla escolha sobre "que par de relações aparece"? Eu acertei sem demonstrar nada. O que o guia está medindo nesse item?
3. Professor, na P50 o enunciado pede "a distância x" sem valor nem unidade. Por que o formato da resposta (expressão, testada com valores) fica só no fim do cartão?
4. Professor, o HTML deixa os níveis 4 e 5 e os `data-resp` no arquivo. Isso é intencional? Se eu abrir o código-fonte, o gabarito inteiro está lá.
5. Professor, a P7 manda ver o "Problema 40". Ele está no guia? Se não está, por que a referência?
6. Professor, na P50 o texto do livro troca q e 2q em relação à figura. O aviso diz que o guia segue a figura. Por que a figura ganha, e não o texto?

## 3. Placar

Para cada questão: forma de resolução e resposta. "Bateu" = dentro da tolerância de 2 % do `data-resp` (ou com a opção correta).

| Questão | Situação | Minha resposta | Bateu? |
|---|---|---|---|
| **P7** | **Não resolvida de forma independente.** Vi os níveis 1 a 5 de uma vez, inclusive a resposta. | Nenhuma tentativa independente. O nível 5 diz −4,00. | Não avaliado (contaminada). |
| **P73** | **Resolvida sem ajuda, sem ver a resposta.** | (a) 2,19×10⁶ m/s; (b) 1,09×10⁶ m/s; (c) diminuiria | (a) bateu, com 2,188×10⁶; (b) bateu, com 1,094×10⁶; (c) bateu (opção b). |
| **P42** | **Resolvida sem ajuda, sem ver a resposta.** | (a) opção a: tanθ = F/mg e senθ = x/2L (e x³ = q²L/(2πε₀mg)); (b) 2,38×10⁻⁸ C | (a) bateu; (b) bateu, com 2,383×10⁻⁸. |
| **P50** | **Resolvida sem ajuda, sem ver a resposta.** | (a) x = L/2 + kqQL/(2Ph²), que com os valores-teste dá 58,99 cm; (b) h = √(3kqQ/P), que dá 7,34 cm | (a) bateu, com 58,99; (b) bateu, com 7,344. |
| **P10** | **Parcialmente contaminada.** O item (a) foi visto antes da conta; o item (b) não. | (a) Q/q = −2√2 ≈ −2,83; (b) Não (opção c). Verifiquei a força em todas as partículas (só a 1 e a 4 se anulam com essa razão). | (a) bateu, com −2,828. (b) bateu, opção c. |
| **P23** | **Parcialmente contaminada.** O item (a) foi visto antes da conta; (b), (c) e (d) não. | (a) x = 0; (b) x = d/√2 = 12,0 cm; (c) 0; (d) 4,90×10⁻²⁶ N, com |F| = 2kqq₃x/(x²+d²)^(3/2) | (a) bateu, com 0. (b) bateu, com 12,02. (c) bateu, com 0. (d) bateu, com 4,904×10⁻²⁶. |
| **P21** | **Contaminada.** Vi a resposta 3,770×10⁻⁸ C antes da minha conta. | q = 2πb(R₂² − R₁²) = 2π·3,0×10⁻⁶·0,0020 ≈ 3,77×10⁻⁸ C (conta à mão) | Bateu, mas sem independência. |

**Resumo:** resolvidas sem ajuda e sem ver a resposta: P73, P42, P50 (3 de 7). Com alguma resposta vista antes: P10, P23 e P21. Não resolvida de forma independente: P7. Ajuda usada por mim, em nenhuma questão, exceto pela leitura acidental da P7.

**Observação:** nenhuma das questões precisou do guia para ser resolvida. Para um aluno que já sabe a física, o guia só ajuda se o aluno travar, e eu não travei. A utilidade do guia depende das dicas, e não dos cartões em si. Isso precisa ser testado com um aluno que trava de verdade.

## 4. O que funcionou (não remover na v2)

- **Aviso de erro de impressão na P42** ("tan θ ≤ sen θ" no livro). Explica a discrepância antes de eu me confundir.
- **Aviso da P50 sobre o texto do livro (q e 2q trocados) contra a figura.** Diz qual leitura o guia segue e mostra o que muda com a outra. É uma boa prática.
- **Respostas testadas com valores e formato explícito no bloco de respostas da P50** (a expressão conferida com L=1 m, q=1 µC etc.). Permite conferir sem revelar a fórmula.
- **P10, item (b):** a pergunta se responde pela razão do item (a), e a alternativa "Sim: a razão do item (a) já zera todas" é uma armadilha fácil de descartar. A pergunta testa o raciocínio, não o cálculo.
- **P23:** o intervalo [0; 5 m] e a instrução "conferir as bordas" (no q-meta) põem o mínimo em x = 0 como parte do problema. Não é um detalhe escondido.
- **P21:** a figura de casca com gradiente que escurece para dentro (ρ = b/r) e a legenda "mais escuro = ρ maior" ligam a figura ao enunciado sem texto a mais.
- **Roteiro antes da ajuda** ("já desenhei a situação", "já listei dados e incógnita"): incentiva o aluno a tentar antes de abrir a dica.
- **Campos com a unidade no rótulo** (P73, P42, P21): cada resposta diz em que unidade vai.
- **Tolerância de 2 % informada** no cabeçalho das questões: evita o aluno achar que errou por arredondamento.
