# Reteste (rodada 2): Aluno 2, Resolvedor

Escopo: refiz P29-11 (a e b), o simulado (5 questões) e olhei as Dicas 3 de PA8 e PA10. Li o Degrau 6 (linhas 600 a 720) antes do P29-11. Li os recolhidos só depois de tentar e de conferir.

**Contaminação, que pesa no resultado:**
- Eu já tinha visto, na rodada 1, as respostas de P29-11, PA8, PA10 e das correções do simulado (valores 9,2·10³ N/C, 72,6 e 63,6 N/C, 8,2·10⁻⁵ T e 6,0·10⁻⁷ V). Por isso o reteste não é cego. As contas abaixo foram refeitas por derivação, mas a memória pode ter guiado algumas escolhas.
- O Degrau 6 que eu li antes do P29-11 (linhas 650 a 654) já contém a regra "fora do par, sentidos opostos". Ela também cita "(Problema 29.11)" logo após a regra, o que entrega o sentido da resposta. Meu acerto em (b) não prova que eu aplicaria a regra sem ela.

---

## 1. P29-11, (a) e (b), refeito

**Degrau 6 ensina o passo em que travei? Sim.** Linhas 650 a 654: "Dois fios paralelos: onde B zera? É a regra das duas cargas do Degrau 1, trocando sinal por sentido da corrente." Depois: "Correntes no mesmo sentido: os campos se opõem entre os fios... Correntes em sentidos opostos: entre os fios os campos se somam; o zero fica fora do par, do lado do fio de menor corrente (Problema 29.11)." Na rodada 1 a regra não estava nesse ponto (eu não li o degrau e inverti a lógica). Ela agora está no degrau e cobre o caso.

**Problema:** a frase "(Problema 29.11)" no fim da regra é a própria questão. Quem lê o degrau antes da tentativa recebe o sentido da resposta. Gravidade: **atrapalha**. Sugestão: tirar a referência ou pô-la no pós-conferir.

**Nova Dica 1 (`ajuda/P29-11-1.md`):** diz a pergunta certa: "Em P, fora do par de fios, os campos dos dois fios se somam ou se opõem? Isso depende do sentido das correntes." Não entrega a resposta. Ponto positivo: a dica remete ao quadro certo.

| Campo | Resultado | Nível | Confiança |
|---|---|---|---|
| (a) i₂ | 4,33 A, certo | sem ajuda | 3 |
| (b) sentido | para fora, certo | sem ajuda (regra já lida no degrau) | 3 |

Ainda bloqueia? Nada bloqueia. Atrapalha: a referência ao 29.11 dentro do degrau (acima).

---

## 2. Simulado (5 questões, às cegas com a ressalva acima)

Antes de abrir conferir, escrevi as contas (resumo):

- **Q1 (b):** E = kQ/(y√(y²+L²/4)) = 35,96/(0,05·0,0781) = 9,21×10³ N/C, para cima, longe da barra. Confiança 2.
- **Q2 (b):** r = 3,5 cm, entre a e b: E = A(r−a)/(ε₀r) = 72,6 N/C. Confiança 2.
- **Q2 (c):** r = 8 cm, fora de b: E = A(b−a)/(ε₀r) = 63,6 N/C. Confiança 2.
- **Q3 (b):** v = √(2eV/m) = 5,36×10⁵ m/s; r = mv/(eB) = 1,87×10⁻² m. Confiança 3.
- **Q3 (c):** T = 2πm/(eB) = 2,19×10⁻⁷ s. Confiança 3.
- **Q4 (b):** semicírculo μ₀i/(4R) = 5,03×10⁻⁵ T; dois trechos semi-infinitos 2·μ₀i/(4πR) = 3,20×10⁻⁵ T; total 8,2×10⁻⁵ T, para dentro. Confiança 2.
- **Q5 (b):** fem = (μ₀a/2π)·ln(3,5)·(di/dt) = 2×10⁻⁸·1,253·24 = 6,0×10⁻⁷ V; corrente = ε/R = 3,0×10⁻⁵ A. Confiança 2.
- **Q5 (c):** anti-horária.

Conferências: todos os campos batem (S1-b 9208; S2-b 72,64; S2-c 63,56; S3-b 1,8653×10⁻² m; S3-c 2,186×10⁻⁷ s; S4-b 8,2265×10⁻⁵ T; S5-b 6,013×10⁻⁷ V). Sem ajuda. A corrente de Q5 (b) não tem campo na página, então não foi conferida diretamente.

**Pergunta sobre Q4 (Biot-Savart e o Degrau 6):** sim, dá para seguir. O exemplo "fio reto pela lei de Biot-Savart" (linhas 691 a 708) faz o caso geral e fecha com "Fio semi-infinito (θ de 0 a 90°): μ₀i/(4πR), a metade". A correção recolhida só usa esse resultado e a troca x = R tgθ, que o exemplo já ensina. O que faltou para eu deduzir o semi-infinito por conta própria foi escrever a integral com limites (não fiz no papel); o degrau dá o modelo, mas não tem o passo "o trecho de 0 a 90° equivale à metade" como frase própria, e isso é o que eu teria usado.

**Notas pela rubrica** (dou eu mesmo; sem desenho escrito em nenhuma questão):

| Questão | Desenho (0,2) | Lei e montagem (0,8) | Símbolos (0,4) | Números (0,4) | Sentido e checagem (0,2) | Total |
|---|---|---|---|---|---|---|
| Q1 | 0,1 | 0,8 | 0,4 | 0,4 | 0,1 | **1,8** |
| Q2 | 0,1 | 0,8 | 0,4 | 0,4 | 0,1 | **1,8** |
| Q3 | 0,1 | 0,8 | 0,4 | 0,4 | 0,2 | **1,9** |
| Q4 | 0,1 | 0,4 | 0,4 | 0,4 | 0,1 | **1,4** |
| Q5 | 0,1 | 0,3 | 0,4 | 0,4 | 0,2 | **1,4** |

Total: **8,3 de 10**. Q4 perde na lei/montagem (não derivei o semi-infinito no papel). Q5 perde na lei/montagem (usei a fórmula de Φ dada, sem o "mostre", porque no papel não derivei). Q1 e Q2 perdem em desenho e sentido (não desenhei e não escrevi "radial para fora" na Q2).

---

## 3. Dicas 3 (PA8 e PA10)

- **`ajuda/PA8-3.md`:** "Escreva o B de cada arco com φ = π e decida o sentido de cada um (⊙ ou ⊗) antes de juntar os dois." Deixa o próximo passo para mim e não dá o resultado. Não diz que os trechos retos não contribuem; isso fica para a dica 2 ou o degrau. **Polimento.** Ainda assim dá para dar o passo sozinho.
- **`ajuda/PA10-3.md`:** "dΦ = (4,0t²y)·a·dy, com y de 0 a a. Integre e depois derive em t." Entrega a montagem inteira (a faixa, o integrando e os limites), que é a parte difícil de P30-27 (fatiar). Sobra só álgebra e o sinal. **Entrega demais** (no sentido de montagem). Contaminada: eu já sabia a resposta (1,08·10⁻³ V) da rodada 1, então minha avaliação não é isenta.

---

## 4. Em 3 linhas: o "Ideias que a questão usa" resolve o "Usa:"?

Em parte. O bloco de P29-11 (`recolhido/10.md`) lista só temas ("B de fio longo; sentido pela mão direita; onde o campo zera numa reta"), sem fórmula nem passo, e fica recolhido até eu travar. Isso resolve o problema do "Usa:" que mostrava a resolução na tela. Não verifiquei nas outras questões se o "Usa:" foi trocado da mesma forma: só olhei o P29-11 nesta rodada.

---

## Placar do reteste

- P29-11 (a) e (b): resolvidas sem ajuda (regra lida antes no Degrau 6).
- Simulado: 5 de 5 campos com resposta conferida e batendo; nota pela rubrica 8,3/10 (dada por mim).
- PA8-3 e PA10-3: avaliadas (PA10-3 entrega demais, PA8-3 é polimento).

Gravidades pendentes:
- **Atrapalha:** o "(Problema 29.11)" dentro da regra do Degrau 6 entrega o sentido da própria questão.
- **Atrapalha:** PA10-3 entrega a montagem da faixa (não a resposta).
- **Polimento:** PA8-3 não diz que os trechos radiais dão zero.
- **Polimento:** a Q4 do simulado não explicita "o semi-infinito é metade do fio infinito" como frase própria, para quem tem de deduzir na prova.
