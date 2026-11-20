# Relatório do Aluno 1 (base frágil), Cap. 23, Lei de Gauss

Leitura feita: guia-cego.md inteiro (linhas 1 a 1270), conferências de cada id respondido, ajuda P29-1, e duas capturas (widget-w2.png, desktop-d3.png). Respostas dadas antes de cada conferência.

## 1. Itens de crítica

| Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|
| Degrau 0, gancho | salto lógico | atrapalha | "A resposta vem no Degrau 3." O Degrau 3 dá "−680 mil coulombs" mas não diz que isso é a opção c. Fica para o aluno fazer a correspondência sozinho. | No Degrau 3, dizer explicitamente: "Resposta do gancho: c." |
| Degrau 0, pre4 | polimento | polimento | Errei (escolhi a, campo com 1/r). A fórmula k·q/r² só aparece na mini-revisão, depois do erro. | Pôr a regra "campo cai com 1/r²" ao lado da pergunta, ou numa linha de lembrete antes do teste. |
| Degrau 1, Problema 3 (lacunas) | dica entrega demais | polimento | O enunciado já dá "A = 1,96 m² ĵ". Só falta multiplicar. | Deixar o aluno achar o vetor área, ou tirar o valor do enunciado. |
| Degrau 2, "Ver de onde vem" (esfera) | salto lógico | atrapalha | "Uma superfície de outra forma pode ser vista como pedaços de esferas e partes rasantes; o resultado continua q/ε₀." Não há conta. Logo depois vem ck2-1 ("a forma não importa"), e eu só acertei por chute de confiança 2. | Dar uma linha de conta ou um desenho do argumento dos pedaços. |
| Degrau 2, widget W2 × Figura 2-1 | erro de consistência | atrapalha | A figura diz "cada uma das 8 linhas que saem dela". O widget W2 mostra "A (+, dentro): 12 saídas" e o texto diz "Doze linhas saem de cada carga". Confirmei na captura. | Padronizar o número de linhas (8 ou 12) nos dois lugares. |
| Degrau 3, "Por que E é igual em toda a esfera" | salto lógico | atrapalha | "Só sobra uma possibilidade: E radial ... com o mesmo módulo". Não mostro por que o campo não pode ter componente tangencial. Isso se repete no Degrau 5 ("Sobra: radial"). | Explicar o caso tangencial (uma componente tangencial quebraria a simetria por rotação) ou dizer "assumimos que". |
| Degrau 3, "A intuição: dentro de uma casca" | termo não definido | atrapalha | "Dois cones estreitos saem de P" e "o pedaço 'visto' pelo mesmo cone". Cone não foi definido; a figura 3-1 ajuda, mas o texto não diz o que é o cone. | Definir: "cone = conjunto de direções que saem de P". |
| Degrau 3, Erros comuns | dica fraca | atrapalha | Errei lac3-3 (r = 1,5a, fora da esfera de raio a). Usei a fórmula de dentro, E = kq·r/a³ (dando 169 mN/C; gabarito 49,9). Os erros comuns só listam o uso de kq/r² dentro, nunca o erro inverso. | Incluir: "fora da esfera de raio a, use kq/r²; dentro, kq·r/a³". |
| Degrau 4, Problema 55 (lacunas) | dica entrega demais | polimento | O enunciado escreve a forma "(?) × π ε₀ K r⁶", então a lacuna já vem com a forma pronta. | Deixar a forma em aberto, ou aceitar a expressão completa. |
| Degrau 6, Ficha "σ junto a um condutor" | salto lógico (ordem) | atrapalha | A Ficha do Degrau 6 já usa "E = σ/ε₀" logo fora do condutor. A dedução só aparece no Degrau 7 ("Por que lá é σ/ε₀?"). | Mover a linha da Ficha para o Degrau 7 ou citar a dedução ali. |
| Degrau 7, P39 e "Erros comuns" | termo não definido / ambiguidade | atrapalha | "θ = 30° com uma placa vertical". Para resolver, preciso entender que o ângulo com a placa é o ângulo com a vertical. O erro comum cita "pêndulo", que não foi definido. | Escrever no enunciado "30° com a vertical (a placa é vertical)". |
| Degrau 7, "A ideia: a formiga e a parede" | polimento | polimento | "Volte ao W5 ... a curva é reta." Não fica claro se é reta horizontal. | "a curva é horizontal (constante)". |
| Degrau 7, "Onde a analogia quebra" | termo não definido | polimento | "Foi o que o disco do Cap. 22 mostrou." O disco do Cap. 22 não é citado em lugar nenhum deste guia. | Trocar por uma frase autocontida. |
| P76 | dica entrega demais | atrapalha | "A equação de (a) se perdeu na conversão do livro; é esta." O enunciado pede "Mostre que" e o guia já dá E = ρr/(2ε₀). | Manter o pedido de derivação ou dar só o valor-teste. |
| P29, cabeçalho "Usa:" | dica entrega demais | polimento | "Usa: lata gaussiana com λ = Q/L" já indica o método. Não cheguei a usá-lo: apliquei kQ/r² (ponto) em P29-a e errei. Com essa linha no cabeçalho, o erro era evitável. | Manter o cabeçalho, mas com a dica só depois da tentativa. |
| Final de cada degrau (linhas 31, 98, 241, 369, 505, 612, 738, 847) | outro | polimento | Aparecem números soltos "0", "1", "2" ... "7" depois do último checkpoint de cada degrau. Não sei o que são. | Remover ou transformar em rótulo ("Fim do degrau 2"). |
| Linha 5 | outro | polimento | "Tema: automático". Não sei o que significa. | Remover ou explicar. |
| Final da revisão intercalada | outro | polimento | "Onde você estava confiante e errou — Ainda não há respostas com confiança marcada." Parece texto de estado vazio. | Esconder a seção enquanto estiver vazia. |
| Checkpoints em geral | falta prática | atrapalha | Vários acertos foram com confiança 1 ou 2 (ex.: ck4-2, ck4-3, ck6-1, ck7-1, prev-w4, P52 e P53 sem nenhuma pista). Isso mostra que parte dos checkpoints é adivinhável, o que reduz o efeito de "2 de 3 para passar". | Mais de uma alternativa "quase certa" e perguntas que exijam a conta, não só a escolha. |

## 2. Perguntas ao Professor

1. Professor, por que o campo dentro de uma esfera carregada tem que ser radial? A frase "só sobra uma possibilidade" não me convenceu. Existe outra direção que eu não vi?
2. Professor, no Problema 29 eu usei kQ/r² e deu 45 N/C. Por que o tubo longo não é tratado como carga pontual, e como eu deveria ter percebido isso sem ajuda?
3. Professor, em P39 o enunciado diz "30° com uma placa vertical". Por que o ângulo com a placa é o mesmo que o ângulo com a vertical? O guia só diz isso no erro comum.
4. Professor, no Degrau 6 a Ficha já usa E = σ/ε₀, mas a dedução aparece só no Degrau 7. Esse uso antecipado é intencional?
5. Professor, por que a forma da superfície gaussiana não importa? A explicação com "pedaços de esferas" não me deu a conta.

## 3. Placar

**Checkpoints (acertos de primeira):**
- Degrau 0 (teste rápido): 5/6 (errei pre4). Gancho: sem conferência própria; a resposta só aparece no Degrau 3, e eu escolhi b (errado).
- Degrau 1: 3/3 (ck1-1, ck1-2, ck1-3).
- Degrau 2: 3/3.
- Degrau 3: 3/3.
- Degrau 4: 3/3.
- Degrau 5: 3/3.
- Degrau 6: 3/3.
- Degrau 7: 3/3.

**Previsões (prev-w1 a prev-w6):** 6/6 corretas.

**Campos de lacuna e de questão:**
- Degrau 1 (lac1-1 a lac1-4): 4/4.
- Degrau 2 (lac2-1 a lac2-3): 3/3.
- Degrau 3 (lac3-1 a lac3-3): 2/3. Errei lac3-3 (169 mN/C, gabarito 49,9).
- Degrau 4 (lac4-1 a lac4-3): 3/3.
- Degrau 5 (lac5-1 a lac5-4): 4/4.
- Degrau 6 (lac6-1, lac6-2): 2/2.
- Degrau 7 (lac7-1 a lac7-3): 3/3.
- Revisão intercalada (rev-1 a rev-7): 7/7.

**Questões (Problemas), resolvidas sem ajuda:**
- P5: resolvido sem ajuda (3,02e-9 N·m²/C, gabarito 3,017e-9).
- P24 (a, b, c): resolvido sem ajuda, as três partes corretas.
- P39: resolvido sem ajuda (σ = +5,0e-9 C/m²).
- P52 (a a f): resolvido sem ajuda, correto.
- P53 (a a e): resolvido sem ajuda, correto.
- P76 (a a c): resolvido sem ajuda, correto.
- P29: resolvido sem ajuda, 5 de 6 corretos. Errei P29-a (45 N/C, gabarito 0,2138), que usou a fórmula de carga pontual em vez de λ/(2πε₀r). Abri a ajuda nível 1 (P29-1) só depois da conferência; a Dica 1 teria bastado para corrigir: ela aponta o Degrau 5 e o exemplo das cascas coaxiais.

Nenhuma questão ficou sem resolução. Nenhuma foi resolvida com ajuda antes da resposta.

## 4. O que funcionou (não remover)

- A Ficha das grandezas novas, com a coluna "Armadilha": foi a referência que mais usei ao errar.
- A receita de 5 passos (simetria, gaussiana, fluxo, carga envolvida, iguala e isola), repetida nos Degraus 3 a 7.
- Os "Erros comuns" com a frase "Na verdade ..." que explica o motivo. Foram eles que me mostraram o erro de sinal e o da cavidade.
- As conferências dão a conta, não só o gabarito. O "Verificar" dos exemplos resolvidos também.
- As mini-revisões que aparecem depois do erro (pre1, pre2, pre4).
- Os "Por que ...?" escondidos, que respondem a dúvida no momento em que ela aparece.
- A Síntese "Que superfície gaussiana eu uso?" e a tabela "Use quando / Não use quando".
- O aviso "(O livro em português diz '3,0 e 6,0 m'; é erro de tradução ...)" no Problema 31. Resolveu uma dúvida que eu teria tido.
- A checklist "Antes de pedir ajuda" em cada problema.
- Os widgets com previsão antes de liberar: obrigam a pensar antes de mexer.
- A revisão intercalada, com perguntas fora de ordem: testou os degraus sem pistas.
