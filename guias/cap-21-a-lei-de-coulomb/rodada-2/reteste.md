# Rodada 2: reteste na v2 (Alunos 1 e 2)

Relatórios completos: `reteste-aluno-1.md` e `reteste-aluno-2.md`.

**Como foi feito.** Na rodada 1, os dois alunos-agente leram o HTML como código e viram respostas antes da hora. Para o reteste, o Professor gerou uma **versão cega** do guia (sem `data-correta`, `data-resp`, feedbacks, ajudas nem Dúvidas da turma). As ajudas ficaram em arquivos separados, um por nível, e as respostas em arquivos de conferência, abertos só depois de responder. Os mesmos agentes foram retomados com SendMessage.

**Limite honesto.** O Aluno 2 já conhecia quase todas as respostas da rodada 1. O placar dele mede sobretudo se enunciados e dicas bastam, não a resolução do zero. Os únicos valores novos para ele foram P10(b1) e P42(a). O Aluno 1 respondeu os checkpoints às cegas, com exceção da previsão w4 e da lacuna l7, que ele mesmo declarou contaminadas.

## Placar: v1 × reteste

| | Rodada 1 (v1) | Reteste (v2) |
|---|---|---|
| **Aluno 1, checkpoints** | D1: 2 de 3. D0 e D2–D6: não valeram (viu as respostas). | D2 a D7: **3 de 3 em todos os seis** (confiança 2 a 3). Pré-requisito 5 errado (esqueceu a cadeia). |
| **Aluno 1, previsões** | w1 errada ("metade") | w1, w2, w3 e w5 certas (w4 não conta) |
| **Aluno 1, lacunas** | l1 incompleta; demais contaminadas | l1, l2, l3, l4a, l4b, l5 e l6 certas (l6 com o valor final chutado; l7 não respondida) |
| **Aluno 2, questões** | Sem ajuda e sem ver a resposta: P73, P42, P50. Contaminadas: P10(a), P23(a), P21. P7 não independente. | 10 itens refeitos (P7, P10 a/b1/b2, P23 a–d, P21, P42 a/b, P50 a/b), **todos sem ajuda e certos**. Inéditos para ele: P10(b1) e P42(a). |

## Pontos em que travaram: o que aconteceu

| Ponto (rodada 1) | Aluno | Reteste 1 | Correção feita | Reteste 2 |
|---|---|---|---|---|
| Regra do quociente não ensinada | 1 | Parcial: segue o exemplo, mas a linha "corte um fator" vinha pronta | Corte mostrado passo a passo na lacuna do Degrau 6 | — (não bloqueava mais) |
| Sinal no P52 | 1 | Destravou (lacuna nova sem ambiguidade) | Exemplo de formato "5,26e4" era a própria resposta: trocado por "1,23e4" | Confirmado ok |
| Gabarito antes de conferir | 1 | Resolvido | — | — |
| Por que o ponto nulo fica perto da carga menor | 1 | Destravou ("r ∝ √\|q\|") | — | — |
| Raiz no Ex. 21.01c | 1 | Destravou | — | — |
| **Origem de x ∝ q^(2/3)** | 1 | **Ainda bloqueava** | A previsão do W3 deixou de afirmar a lei sem prova e passou a explicar o "menos que o dobro" com o que o degrau ensina | **Parcial**: entendeu e explicou o motivo qualitativo; o número 1,59 continua sem prova no degrau, de propósito (a prova é o P42(a)) |
| Contaminação (P7, P10, P23, P21) | 2 | Resolvida pela versão cega | — | — |
| Constantes ausentes | 2 | Resolvido (caixa de constantes) | — | — |
| P42(a) chutável | 2 | Parcial: agora mede a geometria (sen θ), não o balanço de forças | — | — |
| P50, formato da resposta | 2 | Resolvido | — | — |
| P10(b) chutável | 2 | Resolvido (conta antes da conclusão) | A Dica 3 também cobre a partícula 2 | — |
| Dica 3 da P23: "lacuna do Degrau 6" vago, bordas não citadas | 2 | Atrapalha | Referência explícita e lembrete das bordas | — |

## Pendências (continuam depois do segundo reteste)

1. **x ∝ q^(2/3) no Degrau 4 (Aluno 1): parcial.** O aluno entende por que x cresce menos que o dobro, mas o fator 1,59 só é provado no Problema 42(a). Isso é decisão de projeto: pôr a derivação no degrau entregaria a demonstração do P42(a). Para um aluno de base frágil, o caminho é fazer o P42 logo depois do Degrau 4, que é a ordem do guia.
2. **Dica 3 continua com a montagem em símbolos** (P7, P10, P23). O Aluno 2 acha que entrega demais. **Mantido**, porque o prompt define a Dica 3 como "a montagem (equações em símbolos), sem o resultado"; o que foi enxugado é o que passava disso (a derivada no P23, a soma completa no P10).
3. **P42(a) mede só o passo geométrico** (sen θ = x/2L). A demonstração completa não tem conferência automática; ela fica no nível 4.
