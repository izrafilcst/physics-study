# Aluno 2 (Resolvedor), rodada 1, Cap. 23 (Lei de Gauss)

Escopo do que li: enunciados das questões (guia-cego.md, linhas 964–1171), a síntese "que superfície gaussiana eu uso?" (linhas 1173–1187), a tabela de equações (1189–1199), o aquecimento (linhas 33–98) e o Fluxo/Lei de Gauss até a linha 260. Não li os degraus 3 a 7 inteiros, nem as resoluções comentadas (ajuda nível 4) nem as respostas (nível 5). Não abri guia-v1.html, calculos.py nem o livro.

Ordem: respondi cada questão antes de abrir ajuda ou conferência, com uma exceção, que admito abaixo. Confesso também que abri as conferências de P52 em lote antes de ler a ajuda de P52-f. Assim o nível 2 de P52 não é um teste limpo.

## 1. Itens de crítica

| # | Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|---|
| 1 | ajuda/P52-1.md, linha 6 (Dica 1 manda para a regra do Degrau 3) | salto lógico | atrapalha | Errei P52-f: dei 41,4 N/C; o esperado é 1,348 N/C. Apliquei a fórmula de dentro da casca (ρ(r³ − a³)/...) com r = 3b. A regra "q_env = ρ × volume de material dentro da gaussiana" não diz o que fazer quando a gaussiana engloba a casca toda. | Acrescentar uma linha no Degrau 3: "r > b: q_env = carga total da casca, constante; E cai com 1/r²". Apontar a linha da tabela "fora de qualquer distribuição esférica (q = carga total)" (guia-cego.md, linha 1193). |
| 2 | ajuda/P52-2.md, linhas 5–8 | dica fraca | atrapalha | A Dica 2 separa "fora (r > b)" e manda "Ache q_env em cada região", mas não diz qual é o q_env de fora. Quem já tem a noção de regiões pode continuar errando a conta, como eu. | Trocar por "Fora de tudo (r > b), a carga envolvida é a carga total da casca". |
| 3 | conferir/P52-f.md, linhas 8–11 | outro (erro comum não reconhecido) | polimento | 41,4 N/C não está na lista. A página reconhece 1,54, 5,39 e 12,13, mas não o erro mais provável: usar a fórmula de dentro fora da casca. | Adicionar "41.4 → Em 3b a cavidade não deve ser subtraída: a carga envolvida já é a total da casca." |
| 4 | guia-cego.md, linha 1126 (enunciado de P39) | termo não definido | atrapalha | "faz um ângulo θ = 30° com uma placa vertical" não diz se o ângulo é com a placa ou com a vertical. Respondi com confiança 1. Dá tan 30° (5,0e-9), tan 60° (1,5e-8) ou sen 30°. A conferência esclarece (conferir/P39-a.md, linha 12). O aquecimento (pre5, linhas 85–90) já define θ a partir da vertical, mas o enunciado de P39 não diz isso. | Escrever "faz um ângulo θ com a vertical (paralela à placa)". |
| 5 | ajuda/P39-3.md, linha 6 | dica entrega demais | polimento | A Dica 3 traz a cadeia inteira: T cos θ = mg, T sen θ = qE, qE = mg tan θ, E = σ/(2ε₀). Sobra só a aritmética. | Dar só as duas equações de equilíbrio. Deixar a combinação e a relação com σ para o aluno. |
| 6 | guia-cego.md, linha 1089 (enunciado de P29) | premissa não definida | atrapalha | Diz "casca coaxial de paredes finas", sem dizer que é condutora. As perguntas (e) e (f) só fazem sentido se a casca for condutora. Só a síntese (linha 1179) chama a casca de "metal". Assumi condutora sem perceber a lacuna. | "casca metálica (condutora), de paredes finas". |
| 7 | guia-cego.md, linha 1197 (tabela de equações, linha de E = ρr/2ε₀) | dica entrega demais | atrapalha | A célula diz "fora do cilindro (aí é ρR²/(2ε₀r))". Isso é a resposta de P76-b, que é múltipla escolha. A alternativa c fica trivial. | Tirar o "(aí é …)". Deixar "fora: use outra gaussiana (ver P76-b)". |
| 8 | guia-cego.md, linha 1059 (enunciado de P76) | outro (texto interno vazou) | atrapalha | "(A equação de (a) se perdeu na conversão do livro; é esta.)" é uma nota de produção dirigida a quem revisa, e chega ao aluno. Além disso, a equação já está no enunciado, então "mostre que" vira só conferir. | Remover a nota. Pedir "deduza a expressão de E para r < R" e tirar a equação do enunciado. |
| 9 | guia-cego.md, linha 1057 (Usa de P76) e linha 998 (Usa de P24: "campo de fio") | dica entrega demais | polimento | Os "Usa:" dizem o método e, no P24, a fórmula. Parte do raciocínio que a questão quer treinar já vem pronta. | Deixar o "Usa:" só com o nome do degrau, por exemplo "Degrau 5, cilindros". |
| 10 | guia-cego.md, linha 972 (constantes e prefixos) | falta prática | polimento | A lista tem pC e fC, mas não nC. P52 usa 1,84 nC/m³ e tive de deduzir a conversão. | Acrescentar "1 nC = 10⁻⁹ C; 1 nC/m³ = 10⁻⁹ C/m³". |
| 11 | conferir/P29-a.md, P29-c.md, P39-a.md, P53-b.md | outro (inconsistência) | polimento | Alguns acertos mostram "Resposta calculada pelo guia" ou "gabarito do livro" (P24, P52, P76, P29-b). Outros não mostram nada (P5-a, P29-a, P29-c, P39-a, P53-b). Não está claro qual regra vale. | Mostrar sempre a origem do valor quando o acerto for revelado. |
| 12 | guia-cego.md, linhas 1177–1183 (síntese) | dica entrega demais | polimento | A síntese já dá a regra das cargas induzidas ("superfície interna = −(carga dentro da cavidade)"), que basta para P29-e e P29-f. Quem lê a síntese antes pula o raciocínio. | Mover essa regra para o Degrau 6. Deixar a síntese só com a pergunta "qual gaussiana". |

## 2. Perguntas ao Professor

1. Em P52-f, a gaussiana fora da casca usa a carga total ou ainda "ρ × volume de material dentro"? A regra da Dica 1 me fez calcular como se a casca ainda estivesse crescendo. Dá para escrever a regra explicitamente para r > b?
2. Em P39, o 30° é com a placa ou com a vertical? Se na prova o enunciado disser só "com a placa", o que eu faço?
3. Em P29, a casca é condutora? Se for, em que lugar do guia isso fica dito antes da pergunta (e)?
4. Em P76-a, o "mostre que" pede que eu deduza E = ρr/(2ε₀) ou só que eu confira com número? A tabela de equações já dá a fórmula. O que vale na prova?
5. Por que a lista de prefixos tem pC e fC, mas não nC, se P52 usa nC/m³?

## 3. Placar

| Questão | Resultado | Ajuda usada | Conferência |
|---|---|---|---|
| P5 (Φ) | resolvida sem ajuda | nenhuma; usei o "Usa:" e a síntese (linha 1177) | bateu: 3,02e-9 contra 3,017e-9 (confiança 3) |
| P24 (a) | resolvida sem ajuda | nenhuma; tabela de equações (E = 0 no tubo fino) e síntese (lata coaxial) | bateu: 0 |
| P24 (b) | resolvida sem ajuda | nenhuma; tabela de equações (λ/2πε₀r) | bateu: 5,99e3 contra 5995 (confiança 2) |
| P24 (c) | resolvida sem ajuda | nenhuma | bateu: b |
| P52 (a, b, c) | resolvida sem ajuda | nenhuma | bateu: a |
| P52 (d) | resolvida sem ajuda | nenhuma | bateu: 7,32 contra 7,315 |
| P52 (e) | resolvida sem ajuda | nenhuma | bateu: 12,1 contra 12,13 |
| P52 (f) | não resolvida sem ajuda | errou (41,4); ajuda até o nível 2 sem efeito conclusivo | não bateu na 1ª tentativa; o valor 1,348 apareceu na conferência, que abri antes da ajuda. O destravamento não é comprovado |
| P76 (a, b, c) | resolvida sem ajuda | nenhuma | bateu: 847; c; 452 |
| P29 (a–f) | resolvida sem ajuda | nenhuma | bateu: 0,214; dentro; 0,855; fora; −3,40e-12; −3,40e-12. Ressalva: assumi casca condutora sem o enunciado dizer |
| P39 | com ajuda até o nível 3 | nível 1 (onde olhar), nível 2 (plano), nível 3 (primeiro passo), para resolver a dúvida do ângulo | bateu: 5,007e-9. Resposta fria 5,0e-9 já estava dada, com confiança 1; a ajuda confirmou a convenção |
| P53 (a–e) | resolvida sem ajuda | nenhuma; síntese (linha 1181) | bateu: 7,78e-15; 0; 5,58 mN/C; 22,3 mN/C; b |

Resumo: 7 questões, 19 de 21 campos e perguntas batem na primeira vez. P52-f é o único erro. A P39 foi a única com ajuda (até o nível 3).

## 4. O que funcionou

- A síntese "que superfície gaussiana eu uso?" (linhas 1173–1187) foi o caminho principal. Com ela resolvi P5, P24, P29, P53 e P76 sem abrir ajuda.
- A tabela de equações com "use quando / não use quando" (linhas 1189–1199) evitou o erro de usar E = ρr/3ε₀ fora da esfera maciça, por exemplo.
- As conferências explicam o porquê de cada alternativa (conferir/P24-c, P29-d, P53-e, P76-b). Isso ensina mais do que só dizer "errado".
- A lista de erros comuns em conferir/P5-a, P39-a e P53-a mostrou exatamente os erros em que eu cairia (por exemplo, usar E = σ/ε₀ numa placa isolante).
- O aquecimento, pre5, ensina a bolinha no fio com θ a partir da vertical e F = mg tan θ. Ajudou a fechar P39.
- O "Usa:" de cada questão deixou claro qual lei aplicar, e o "Antes de pedir ajuda" pede que se desenhe e liste os dados, o que é uma boa disciplina.
