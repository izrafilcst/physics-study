# Rodada 2: reteste na v2

Alunos retomados com o mesmo agente (SendMessage), lendo a cópia cega da v2 (`rodada-2/aluno/`). Relatórios completos: `reteste-aluno-1.md` e `reteste-aluno-2.md`.

## Aluno 1 (base frágil, haiku)

Refez só o que o travou ou o fez errar na v1, e fez dois exercícios novos de transferência.

| Ponto da v1 | Gravidade na v1 | Na v2 |
|---|---|---|
| Integral sem definição (Degrau 4) | bloqueia | **resolvido** (caixa "Ferramentas de Cálculo") |
| Radiano nunca definido | bloqueia | **resolvido** |
| O "d" de dq, ds, dθ | bloqueia | **resolvido** |
| Por que cos θ | bloqueia | **resolvido** (passo 4 reescrito) |
| ∫cos θ dθ sem passo | bloqueia | **em parte**: "derivada" não era definida → corrigido depois do reteste (parte E) |
| Primitiva da barra (Degrau 5) | bloqueia | **resolvido** |
| Regra de avanço com 1 de 3 | bloqueia | **resolvido** |
| "A integral é a mesma, com seno" | atrapalha | **resolvido** |
| "Tanto faz graus ou radianos" | atrapalha | **resolvido** |
| Feedback de lac-a-3 com valor errado | atrapalha | **resolvido** |
| "Erro" não definido (prev-w5, ck5-3) | atrapalha | **resolvido** |
| Previsão do W2 respondida antes | atrapalha | **em parte**: a frase "quem ganha é |q|/r²" ainda vinha antes → retirada depois do reteste (parte E) |
| Ordem das cargas na Pergunta 4 | atrapalha | era só a descrição da figura na cópia cega; a descrição agora diz "da esquerda para a direita" (parte E) |
| ck4-3 ("mais pedaços") sem aviso nos Erros comuns | atrapalha | **mantido** (decisão 53 da consolidação: o checkpoint é prática de recuperação; o feedback ensina depois do erro) |

**Placar limpo** (itens que ele não tinha visto): previsão nova do W2 ✓ (confiança 2), previsão nova do W3 ✓ (confiança 3), lacunas novas lac-r-3 ✓ e lac-r-5 ✓ (com o sinal). **4 de 4.**
**Transferência** (sem conferência): arco de 90°, r = 10 cm, 2,0 nC → 1,62 × 10³ N/C (`calculos.py`: 1619 N/C ✓); barra de 20 cm, 4,0 nC, a = 10 cm → 1,20 × 10³ N/C (`calculos.py`: 1199 N/C ✓). Na v1 ele travava justamente nesse método.
Os demais itens refeitos (lacunas do Degrau 3 e 4, prev-w5, ck5-3) deram 11 de 11, mas estão contaminados: ele já tinha visto o gabarito na v1.

## Aluno 2 (resolvedor, haiku)

Na v1 resolveu as 8 questões sem ajuda; o reteste conferiu os pontos que ele apontou, os itens novos e as dicas, que ele não tinha usado.

| Ponto da v1 | Na v2 |
|---|---|
| Mensagens de conferência que entregavam o passo (P31-b, P8-a, P38-a, P9-a) | **resolvido** (as quatro) |
| "Usa:" nomeando o método | **resolvido** |
| Síntese "lado + sinal" sem referência | **resolvido** |
| Ângulos equivalentes sem aviso | **resolvido** |
| r = a/√2 nos Erros comuns | **resolvido** |
| Letra "a" com dois sentidos no P31 | **em parte**: a figura e a nota mudaram, mas o enunciado de (d) ainda dizia "a = 50 m" → corrigido para "D = 50 m" depois do reteste (parte E) |
| Fórmula fechada da barra no Degrau 5 e na tabela | **mantido** (decisão 50: o degrau ensina a integral; o P31 cobra sinal, sentido e limite de longe) |

**Itens novos, sem ajuda:** lacuna nova do Degrau 2, 5 de 5 ✓. Desafio do P15: errou de primeira (288 N/C, −11,3°, por usar 8ke/a² para q₁) e corrigiu com a conferência; não conta como resolvido sem ajuda. Ele pediu uma dica própria para o desafio → acrescentada (parte E).
**Dicas** (avaliadas pela primeira vez): P26 níveis 1 e 2 na medida, nível 3 "entrega demais" (monta a integral inteira); P38 níveis 1 a 3 na medida. A Dica 3 do P26 foi **mantida**: o prompt define o nível 3 como "a montagem (equações em símbolos), sem o resultado", e é isso que ela faz.

## Conclusão

Nenhum ponto ainda bloqueia. Os quatro resíduos não bloqueantes encontrados no reteste foram corrigidos na v2 (parte E) sem nova rodada, porque o prompt só pede outra rodada para o que ainda bloquear. Três críticas continuam rejeitadas, com justificativa na consolidação (fórmula da barra no degrau, aviso "mais pedaços" antes do checkpoint, Dica 3 do P26).
