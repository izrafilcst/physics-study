# Reteste do Aluno 2 (resolvedor) na v2, Cap. 23

Limite do teste: não foi cego. Na rodada 1 eu já tinha visto as respostas (P52-f = 1,348 N/C; P39 = 5,0e-9 C/m²; P76 = 847 / c / 452; P24-c = b; P53-e = b). Por isso, os valores abaixo vêm da memória ou de conta refeita, não de resolução sem consulta. O que consegui medir com honestidade foi a leitura das dicas e dos enunciados.

Arquivos lidos da v2: guia-cego.md (linhas 990–1389), ajuda/P52-1, P52-2, P52-3, P5-3, P29-3, P39-3, P76-3, conferir/P52-f, P5-a, P29-a, P29-c, P39-a, P53-a. Não li o HTML nem os arquivos da rodada 1.

## 1. Pontos da rodada 1

| Ponto | Veredito | Evidência citada | O que ainda falta |
|---|---|---|---|
| 1. P52(f), gaussiana fora da casca | RESOLVIDO | ajuda/P52-2.md, linha 7: "Fora (r > b), a gaussiana já envolve a casca inteira." Com essa frase, a Dica 2 aponta o que eu errei. Só a Dica 1 não bastava (linha 6: "a regra 'q_env = ρ × volume de material dentro da gaussiana'"). conferir/P52-f.md, linha 9, agora reconhece "41.39" com explicação. | A seção "Dúvidas da turma" (guia-cego.md, linha 1245) escreve "Usar r³ − a³ em 3b dá 41 N/C em vez de 1,35 N/C". Isso entrega o gabarito da questão. Tirar esse número da dúvida. |
| 2a. P39, de que reta o ângulo é medido (enunciado) | MELHOROU, MAS AINDA ATRAPALHA | Enunciado (guia-cego.md, linha 1165): "(A placa é vertical, então θ também é o ângulo do fio com a vertical, como na figura.)" Isso responde a pergunta. Mas a legenda da figura (linha 1167) diz "fazendo o ângulo theta com a placa", e conferir/P39-a.md (linha 13) diz "Os 30° são com a placa, que é vertical". Ou seja, o enunciado diz vertical e a figura e a conferência dizem placa. | Alinhar a legenda da figura e a frase da conferência com "com a vertical". |
| 2b. P39, Dica 3 entrega a cadeia inteira? | RESOLVIDO | ajuda/P39-3.md, linha 6: agora só "T cos θ = mg e T sen θ = qE. Daqui: elimine T e troque E pelo campo da placa." A combinação tan θ e a relação E = σ/(2ε₀) saíram da dica. | Nada essencial. A relação com σ fica para a tabela de equações. |
| 2c. P39, precisou de ajuda para refazer a conta? | Conta refeita sem ajuda | Com a vertical: qE = mg·tan 30° → E ≈ 282,9 N/C → σ = 2ε₀E ≈ 5,0e-9 C/m². Refiz de memória, não às cegas. | Não medi o efeito real do enunciado novo sobre um aluno sem resposta prévia. |
| 3. P29, casca condutora no enunciado | MELHOROU, MAS AINDA ATRAPALHA | Enunciado (linha 1126): "dentro de uma casca coaxial (condutora), de paredes finas". Ok. Mas logo abaixo (linha 1128) aparece: "(A tradução perdeu a palavra 'condutora': o original fala em 'conducting shell', e o gabarito de (e) e (f) só bate assim. ...)". É uma nota de produção, do mesmo tipo da nota de P76 que eu tinha criticado. | Remover a nota. A palavra "condutora" já está no enunciado. |
| 4a. P76, nota de produção | RESOLVIDO | A nota "(A equação de (a) se perdeu...)" não aparece mais. Linha 1096 só diz "(Carga no volume: o cilindro é isolante.)", que é informação válida para o aluno. | Nada. |
| 4b. P76, tabela entrega (b) | RESOLVIDO | Tabela, linha 1319: "fora do cilindro (refaça a lata: o material com carga para em R)". A fórmula de fora saiu. | Ressalva: o "Mostre que" de (a) continua com E = ρr/(2ε₀) escrito no enunciado (linha 1096). A tabela continua dando essa fórmula também. |
| 5a. Dica 3 de P5 | RESOLVIDO | ajuda/P5-3.md, linha 6: "Escreva a lei de Gauss para o cubo inteiro... Quanto vale q_env? Depois: que fração de Φ_cubo passa por uma face só?" Deixa o passo conceitual (1/6, por simetria) para o aluno. | Nada essencial. |
| 5b. Dica 3 de P29 | RESOLVIDO | ajuda/P29-3.md, linha 6: pergunta "Que objetos ficam dentro de uma lata de raio 2R₂?" e "Para uma gaussiana dentro do metal, quanto vale Φ?". Deixa a soma das cargas e o sinal para o aluno. | Nada essencial. |
| 5c. Dica 3 de P52 | MELHOROU, MAS AINDA ATRAPALHA | ajuda/P52-3.md, linha 6: "No material: ε₀E·4πr² = ρ·(4/3)π(r³ − a³)". A equação do material inteiro sai pronta, que é quase a conta de (d) e (e). Só o trecho "E fora: que volume de material fica dentro da gaussiana?" fica para o aluno. | Tirar a equação e deixar só a pergunta sobre o volume. |
| 5d. Dica 3 de P76 | MELHOROU, MAS AINDA ATRAPALHA | ajuda/P76-3.md, linha 6: "Dentro: q_env = ρ·πr²h e ε₀E·2πrh = q_env." Isso é a conta toda de (a). Só "E fora: até onde vai o material..." fica para o aluno. | Dar só a pergunta "que carga está dentro da lata" e deixar a equação. |
| 6. Constantes com nC | RESOLVIDO | guia-cego.md, linha 1008: "1 nC = 10⁻⁹ C". | nC/m³ não aparece escrito, mas a conversão é direta. |
| 7. Conferências com a origem do valor | RESOLVIDO | conferir/P5-a.md, linha 6: "Gabarito do livro: 3,01 × 10⁻⁹". conferir/P29-a.md, linha 6: "Gabarito do livro: 0,214 N/C". conferir/P29-c.md, linha 6: "Gabarito do livro: 0,855 N/C". conferir/P39-a.md, linha 7: "Gabarito do livro: 5,0 nC/m²". conferir/P53-a.md, linha 6: "Gabarito do livro: 7,78 fC". | P5-a mostra 3,01 (arredondado), mas a tolerância aceita 3,017. Não é um erro, mas o aluno pode estranhar a diferença. |
| 8. Esboço antes da escolha em P24-c e P53-e | NÃO VERIFICÁVEL NESTA RODADA | guia-cego.md, linhas 1049 e 1202: "Antes de escolher: esboce E(r) no papel...". Não consigo testar isso como aluno, porque já sabia que a resposta era b nos dois casos. | Leitura: o esboço de P24-c pede os valores de (a) e (b), e o de P53-e pede (b), (c) e (d). Quem tem pressa pode pular o esboço e chutar. Sugestão: pedir um esboço de três pontos, nomeados, em vez de "esboce E(r)". |

## 2. Itens extras encontrados nesta leitura

| Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|
| Dúvidas da turma, guia-cego.md, linha 1245 (P52) | dica entrega demais | atrapalha | "Usar r³ − a³ em 3b dá 41 N/C em vez de 1,35 N/C." Essa resposta de dúvida já entrega o valor de P52-f. | Responder com o raciocínio ("a carga envolvida para de crescer em b"), sem o número. |
| Dúvidas da turma, linha 1281 (P39) | dica entrega demais | polimento | "O que entra em tan θ = F/(mg) é sempre o ângulo do fio com a vertical." A fórmula final já está na dúvida. | Manter a explicação sobre o ângulo e tirar a equação. |
| Régua de números reais, linha 1327 | dica entrega demais | polimento | "2 × 10⁻² — superfície da esfera do Problema 53". Isso dá a ordem de grandeza de P53-d (≈ 0,022 N/C). | Mover a régua para depois da conferência, ou tirar essa linha. |

## 3. Placar das questões refeitas

Os valores são de memória ou recalculados. Não foi uma resolução cega. "Ajuda" indica o que eu li para avaliar, não o que precisei para resolver.

| Questão | Como foi | Ajuda lida | Bateu com a conferência? |
|---|---|---|---|
| P52(f) | Não cego: eu sabia 1,348 N/C. Errei na rodada 1 e refiz a leitura da dica | Níveis 1 e 2 lidos, para avaliar | Bate com 1,348 (de memória). A conferência agora reconhece o erro 41,39 |
| P39 | Refeito com a vertical: E = mg·tan 30°/q, σ = 2ε₀E | Nível 3 lido, para avaliar. A conta não precisou dele | Bate com 5,007e-9 (de memória) |
| P5 | Não cego: sabia 3,017e-9 | Nível 3 lido, para avaliar | Bate (de memória) |
| P29 | Não cego. O enunciado agora diz condutora, e a conta não muda | Nível 3 lido, para avaliar | Bate (de memória) |
| P76 | Não cego: 847, c, 452 | Nenhuma | Bate (de memória) |
| P24-c, P53-e | Não cego: b e b | Nenhuma | Bate (de memória) |

## 4. Resumo do que mudou da v1 para a v2

Resolvido: o erro de P52-f ganhou a frase que faltava na Dica 2, a conferência reconhece o 41,39, a dica de P39 não entrega a cadeia, a nota de P76 saiu, a tabela não entrega (b), e as conferências mostram a origem do valor. Também entrou nC na constante.

Ainda atrapalha: a figura e a conferência de P39 continuam dizendo "com a placa", a nota de produção sobre "condutora" ficou em P29, a Dica 3 de P52 e a de P76 entregam a equação inteira, e a seção "Dúvidas da turma" entrega o valor de P52-f.
