# Rodada 2: reteste da v2 (Alunos 1 e 2)

Os dois alunos foram retomados (mesmos agentes da rodada 1) e leram a cópia cega da v2 (`rodada-2/aluno/`), só nos pontos em que travaram ou que criticaram. Relatórios completos: `reteste-aluno-1.md` e `reteste-aluno-2.md`.

**Limite do teste:** os dois já tinham visto as respostas na rodada 1 e disseram isso. Os acertos de agora (lac3-3, P29(a), P52(f), P39) não medem se a v2 ensina melhor; o que o reteste mede é se o texto da v2 resolve o problema apontado.

## Aluno 1 (base frágil)

| Ponto da rodada 1 | Veredito na v2 | O que foi feito depois do reteste |
|---|---|---|
| lac3-3: fórmula de dentro usada fora | resolvido (o erro comum novo do Degrau 3 descreve o erro dele) | — |
| P29(a): kQ/r² num cilindro | resolvido ("Dúvidas da turma" e erro reconhecido) | — |
| Resposta do aquecimento não dita | resolvido ("a terceira alternativa") | — |
| "Só sobra radial" sem justificar | resolvido (argumento de rotação) | — |
| Por que a forma não importa | resolvido (argumento do cone) | — |
| Fig. 2-1 com 8 linhas × W2 com 12 | resolvido | — |
| "Cone" não definido | resolvido | — |
| σ/ε₀ na ficha do Degrau 6 antes da dedução | melhorou, mas ainda atrapalhava | **Corrigido:** a ficha não cita mais a fórmula; aponta para o Degrau 7, onde a dedução agora é visível, com figura |
| Nota de produção no P76 | nota sumiu; a fórmula de (a) continua no "mostre que" | **Mantido:** é o enunciado do livro (um "mostre que" dá o alvo); a conferência numérica testa a dedução |
| "Números soltos", "Tema: automático" | resolvido (eram defeitos da cópia cega) | — |

**Placar:** lac3-3 e P29(a) certos, mas não contam como "de primeira" (respostas vistas na rodada 1).

## Aluno 2 (resolvedor)

| Ponto da rodada 1 | Veredito na v2 | O que foi feito depois do reteste |
|---|---|---|
| P52(f): Dicas não diziam que fora a carga é a total; 41,4 N/C não reconhecido | resolvido | **Corrigido também:** "Dúvidas da turma" dava o valor de (f); número retirado |
| P39: de que reta é o ângulo | enunciado resolvido; Dica 3 resolvida | Legenda e conferência dizem "com a placa", o que é verdade (e o livro diz assim); o enunciado explica que é o mesmo ângulo. Mantido |
| P29: casca condutora | "(condutora)" no enunciado | A nota sobre o erro de tradução foi mantida: é informação para o aluno, como a do Problema 31 |
| P76: nota de produção e tabela que entregava (b) | resolvido | — |
| Dicas 3 entregavam o conceito | P5 e P29 resolvidas; P52 e P76 ainda escrevem a equação da região de dentro | **Mantido:** o prompt define a Dica 3 como "a montagem (equações em símbolos), sem o resultado"; a região de fora ficou para o aluno |
| Faltava nC | resolvido | — |
| Conferências sem origem do valor | resolvido | — |
| Esboço antes do gráfico | não verificável (ele já sabia a resposta) | Os dois pedidos de esboço já nomeiam três pontos de referência |

**Placar:** P52(f) e P39 certos sem ajuda para resolver (as ajudas lidas foram só para avaliar), mas de memória.

## Resultado

Nenhum ponto continuou **bloqueando**. Os dois "ainda atrapalha" que pediam mudança (σ/ε₀ na ficha e o valor do P52(f) nas "Dúvidas") foram corrigidos na v2 final. Os demais foram mantidos com justificativa. Como nada bloqueia, não houve segundo reteste. A v2 final foi verificada de novo no navegador (`verificacao-v2.json`, `cortes-v2.txt`).

**Pendência:** o reteste não é cego. Para medir de verdade se a v2 ensina melhor, seria preciso um aluno-agente novo, que nunca viu as respostas, fazendo a v2 do zero.
