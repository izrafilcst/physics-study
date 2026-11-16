# Reteste da v2 (Aluno 2, resolvedor, prova amanhã)

Guia testado: versão cega (`scratchpad/reteste/guia-v2-cego.html`), com ajuda em arquivos separados e caixa de constantes no começo das questões.

## Aviso: eu não era um aluno cego neste teste

A versão é cega, mas eu não. Na rodada 1 vi as respostas de P7 (todas), P10 (a), P23 (a), P21 e, depois de tentar, as de P23 (b–d), P10 (b), P42 (b) e P50. Por isso, nesta rodada, sabia de antemão as respostas de quase tudo. O que este reteste mede de fato é: o enunciado e as dicas mudaram o suficiente para eu não precisar ver o gabarito? Só sei responder isso para P42(a) e para o termo novo de P10(b1), que não tinham sido vistos antes.

Outras leituras que devo declarar:
- Li os níveis 1 a 3 da P7 **depois** de resolver. Li a Dica 1 com `cat` via Bash, em desacordo com a instrução de usar Read. Os demais arquivos foram lidos com Read.
- Li a Dica 3 da P10 e a Dica 3 da P23 **depois** de responder cada item.
- Não abri nenhum nível antes de tentar. Não abri níveis 4 e 5 em nenhuma questão.
- Abri `conferir/questoes.txt` só depois de ter todas as respostas finais.
- Não refiz P73 nem P42(b) como questão nova: P73 não estava na lista, e P42(b) era a mesma conta da rodada 1.

## (a) Placar

| Questão | Situação | Minha resposta | Bateu com `conferir/questoes.txt`? | Observação |
|---|---|---|---|---|
| P7 | Sem ajuda (resolvi antes de abrir qualquer nível) | −4 | Sim (−4, tol 2 %) | Eu já sabia −4 da rodada 1. |
| P10 (a) | Sem ajuda | −2,83 (−2√2) | Sim (−2,828) | Já sabia da rodada 1. |
| P10 (b1) | Sem ajuda | −0,354 (−1/(2√2)) | Sim (−0,3536) | Valor novo, não visto antes. |
| P10 (b2) | Sem ajuda | Não (alternativa b) | Sim (alternativa b) | Já sabia da rodada 1. |
| P23 (a)–(d) | Sem ajuda | 0; 12,0 cm; 0; 4,90×10⁻²⁶ N | Sim nos quatro | Já sabia tudo da rodada 1. |
| P21 | Sem ajuda | 3,77×10⁻⁸ C, por 2πb(R₂² − R₁²) | Sim (3,770×10⁻⁸) | Já sabia da rodada 1. |
| P42 (a) | Sem ajuda | sen θ = 0,0208 (x/2L com x=5 cm, L=120 cm) | Sim (0,02083) | Valor novo. |
| P42 (b) | Sem ajuda | 2,38×10⁻⁸ C | Sim (2,383×10⁻⁸) | Já sabia da rodada 1. |
| P50 (a) | Sem ajuda | 58,99 cm (com os valores-teste) | Sim (58,99) | Já sabia da rodada 1. |
| P50 (b) | Sem ajuda | 7,34 cm | Sim (7,344) | Já sabia da rodada 1. |

Nenhuma questão exigiu ajuda para ser resolvida. Nenhuma foi "não resolvida".

## (b) Pontos 1 a 6 da rodada 1

**1. P7 (contaminação na rodada 1).** Resolvido: **sim** no que diz respeito ao guia cego. Os cartões não trazem resposta nem resolução, e as ajudas estão em arquivos separados, então o problema que eu tive não se repete. Mas as dicas continuam fortes demais:
- Nível 1 ("A partícula 3 está fora do par 1–2. O que isso diz sobre os sinais…?"): **adequado**, porque aponta para o sinal e para a magnitude sem dar a conta.
- Nível 2 caiu de 5 passos para 3. Ainda é uma receita: "Iguale os módulos e simplifique." **Parcial**: melhorou, mas continua quase uma receita.
- Nível 3 continua com a equação pronta: "k|q₁||q₃|/(2L)² = k|q₂||q₃|/L²". **Não resolvido**: é a mesma crítica da rodada 1, item 3.

**2. P10, itens (a) e (b), e a Dica 3.** A Dica 3 nova fala só do termo da diagonal: "a força dela (repulsão, módulo kQ²/2a²) aponta a 45° para fora. A componente x dessa força vale −kQ²/(2a²)·1/√2". Julgamento: **entrega demais** para o item (a), porque dá o termo mais difícil já com sinal e fator, e sobra só somar com a força de 2. Além disso, **não ajuda em (b1)**, que é o caso da partícula 2: o termo de diagonal que importa ali é o da partícula 3, e a dica não o menciona. Sobre o problema do (b) da rodada 1 (alternativa correta longa e distratores curtos): **resolvido**. Agora a alternativa correta é "Não." e tem o mesmo tamanho das outras.

**3. P23 e P21 (contaminadas).** A contaminação de leitura **foi resolvida pelo guia cego**: os cartões não trazem `data-resp` nem gabarito. Não consigo medir o efeito real porque já sabia as respostas. A Dica 3 do P23, que para em F(x), tem dois problemas:
- Entrega demais: "$$F(x) = \frac{2k\,q_1q_3\,x}{(x^2+d^2)^{3/2}}$$". Isso tira o passo de componentes e simetria, que é uma das habilidades listadas no cartão.
- Não avisa sobre as bordas do intervalo. A questão pede o mínimo em [0; 5 m], e o mínimo está em x = 0, na borda. A dica não fala disso.
- Frase confusa: "como na lacuna do Degrau 6". Não sei o que é "lacuna". Termo não definido.

**4. P42(a), conferência numérica.** O campo pede sen θ com os dados de (b). Medir o passo da demonstração: **parcial**. Mede só a relação geométrica sen θ = x/(2L). Não mede o balanço de forças tan θ = F/mg nem a manipulação até x³. Um aluno que sabe a geometria acerta sem demonstrar nada. O próprio enunciado admite: "A demonstração não dá para conferir aqui". A crítica da rodada 1 foi melhorada, mas o passo de força continua sem teste.

**5. P50, formato da resposta.** Ficou claro antes de eu começar? **Sim.** O parágrafo "Formato da resposta" vem logo depois do enunciado, antes da figura, e diz que as respostas são expressões em L, q, Q, P e h, com os valores-teste e a unidade em cm. Eu li isso antes de resolver. Resolvido.

**6. Caixa de constantes.** Resolve a falta de k, e, mₑ e g? **Sim.** A caixa traz k = 8,99×10⁹, ε₀, e, mₑ, mₚ e g = 9,8 m/s². Usei esses valores e bateu com o gabarito. Resolvido. Observação menor: a caixa fica no começo da seção de questões, e não ao lado de cada cartão. Quem começar na P42 precisa subir para encontrá-la.

## (c) O que ainda bloqueia

Nada me bloqueou nesta rodada. Os pontos que ainda atrapalham, para um aluno que trava de verdade:
- **P10, Dica 3 não cobre (b1).** Um aluno travado em (b1) não recebe ajuda do nível 3. Local: `ajuda/p10-nivel3.txt`. Evidência: a dica só fala da partícula 4 e da componente x do termo de 1.
- **P23, Dica 3:** "como na lacuna do Degrau 6" é um termo que o aluno não conhece. Local: `ajuda/p23-nivel3.txt`.
- **P23, Dica 3:** não avisa sobre as bordas do intervalo. Local: mesma dica.
- **P7, Dica 3 (nível 3):** equação pronta. Local: `ajuda/p7-nivel3.txt`.
- **P42(a):** o campo só mede a geometria. Local: enunciado de (a) em `guia-v2-cego.html`, linha 1941.

## Resumo (5 linhas)

1. Placar: as 10 respostas refeitas foram resolvidas sem ajuda e todas bateram com `conferir/questoes.txt`. Mas eu já conhecia a maioria pela rodada 1, então o teste mede pouco.
2. Resolvidos: contaminação de leitura (cartões cegos), formato da P50 (antes da resolução), caixa de constantes (k, e, mₑ, g), alternativa longa da P10(b).
3. Parcial: Dica 2 da P7 (ainda receita de 3 passos) e P42(a), que só mede a geometria sen θ = x/2L.
4. Ainda ruim: Dica 3 da P7 (equação pronta); Dica 3 da P23 (entrega F(x), ignora as bordas, usa o termo "lacuna" sem definir); Dica 3 da P10 (entrega o termo da diagonal de 1 e não ajuda em (b1)).
5. Relatório em /home/swampert/Documents/fisica/guias/cap-21-a-lei-de-coulomb/rodada-2/reteste-aluno-2.md. Nota de processo: usei Bash (cat) para ler uma dica, contra a instrução de usar Read.
