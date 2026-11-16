# Rodada 1: consolidação das críticas e respostas do Professor

Relatórios: `aluno-1-base-fragil.md` (haiku, 68 itens), `aluno-2-resolvedor.md` (haiku, 12 itens), `aluno-3-monitor.md` (sonnet, 27 itens + 133 conferências numéricas), `aluno-4-visual.md` (sonnet, 32 itens).

**Processo.** Desta vez os alunos leram a cópia cega (`aluno/`), não o HTML; a ajuda e as respostas ficavam em arquivos separados. Os quatro pararam no meio por uma queda de rede (erro de DNS) e foram retomados do ponto em que estavam. O Aluno 2 diz que abriu `conferir/P9-a.md` antes de responder ao P9; o resto do placar dele é limpo.

**Placar da v1.**
- Aluno 1: teste de base 5/6; checkpoints de primeira 2/3, 1/3, 3/3, 2/3, 2/3, 1/3 (Degraus 1 a 6); lacunas 18/22; previsões 5/6; revisão 6/6; nenhum erro com confiança 3.
- Aluno 2: as 8 questões (17 campos) resolvidas sem abrir nenhum nível de ajuda (P9-a contaminado pela falha de protocolo).
- Aluno 3: nenhuma resposta, exemplo, lacuna, "e se" ou leitura de widget numericamente errada.

**Prioridade usada:** o que bloqueia > erros físicos > o que vários alunos apontaram > o resto.

## 1. Tabela única

| # | Problema | Alunos | Gravidade | Decisão | O que muda na v2 |
|---|---|---|---|---|---|
| 1 | Degrau 4 usa **integral, radiano, "d" (pedacinho) e cos θ** sem definir; a passagem dE → E e ∫cos θ dθ = sen θ não têm passo intermediário; o Degrau 5 também pula a primitiva | 1 | bloqueia | **Aceito** | Caixa "Ferramentas de Cálculo deste degrau" no Degrau 4: radiano (180° = π rad, s = rφ), "d" = pedacinho, integral = soma de infinitos pedacinhos, por que cos θ (a parte de dE ao longo do eixo), ∫cos θ dθ em duas linhas. No Degrau 5, a linha da primitiva −1/x. |
| 2 | Regra de avanço "suba com 2 de 3" não diz o que fazer com 0 ou 1 de 3 (o texto estático só fala do caso bom) | 1 | bloqueia | **Aceito** | Cada checkpoint ganha a regra completa: 2 ou 3 de primeira → suba; 0 ou 1 → releia os blocos que o feedback indicou, refaça e siga (a página deixa marcar o degrau como concluído). |
| 3 | "A integral é a mesma, só com sen θ no lugar de cos θ" (metades de sinais opostos): com os limites −φ/2 a +φ/2 dá **zero** | 1, 3 | atrapalha (erro de texto) | **Aceito** | "Integre só a metade de cima, de 0 a φ/2, com sen, e dobre: a metade de baixo empurra para o mesmo lado." Síntese ajustada. |
| 4 | "Para avaliar o seno, tanto faz graus ou radianos" lido como sen 60 = sen 60 rad; nenhum aviso sobre o modo da calculadora | 1 | atrapalha (erro de texto) | **Aceito** | "sen 60° = sen(π/3): o ângulo é o mesmo; confira se a calculadora está no modo da unidade que você digitou." |
| 5 | `prev-w5` diz 33 % e 7 % de erro; widget, exemplo e `ck5-3` dizem 25 % e 6,25 % (duas referências para "erro") | 3, 1 | atrapalha (inconsistência) | **Aceito** | Uma definição só: erro = diferença relativa ao valor certo = (L/2D)². prev-w5 corrigida (25 %, 6 %). "Erro" e "≫/≪" definidos no Degrau 5. |
| 6 | "Qualquer objeto vira ponto, erro ≈ (tamanho/2D)²" falha com carga total nula (dipolo, P26) e o fator depende da forma (disco: 0,75(R/z)²) | 3 | atrapalha | **Aceito** | "Qualquer objeto com carga total diferente de zero, com D medido do centro"; Síntese: "erro da ordem de (tamanho/D)², o fator depende da forma". |
| 7 | "σ/(2ε₀) com carga numa face": numa folha fina conta a densidade total; Eₘ é o limite z → 0⁺; o campo inverte ao atravessar o disco | 3 | atrapalha (vai doer no Cap. 23) | **Aceito** | σ = carga total por área da folha; Eₘ = valor logo acima (z → 0⁺); uma linha sobre o salto de −σ/(2ε₀) para +σ/(2ε₀) ao atravessar (ponte para Gauss). |
| 8 | Feedbacks de erro com número errado: `lac-a-3` (0,66 → 0,784 em graus), `lac-r-1` (8,99e8 → 8,99), `lac-b-2` (15,17 é "carga toda na ponta longe", 8,67 é "a = 4 m"), `lac-mil-1` (1,57e-11 é a massa em gramas) | 3, 1 | atrapalha | **Aceito** | Valores e mensagens refeitos no `calculos.py` (seção "V2"). |
| 9 | Previsões já respondidas logo acima (W1 pela ficha, W2 pelo parágrafo "4 vezes a carga, 2 vezes a distância", W3 pela Fig. 3-1, W4 por "sen π = 0", W6 pelo limite z → 0) | 1, 4, 3 | atrapalha | **Aceito** | Casos novos: W1 "dobro da distância e dobro da carga" (½); W2 "+1 nC a 1 cm × +4 nC a 3 cm" (o mais perto ganha); W3 "P desce até a origem" (zero); W4: o anel sai do texto anterior e vira descoberta; W6 "quanto vale E em z = R?" (0,29 Eₘ). |
| 10 | O truque 1:4 em d:2d aparece 3 vezes antes do P8 (previsão, regra, lacuna com resposta zero) e as linhas "Usa:" nomeiam o método ("cancelamento") | 3, 4, 2 | atrapalha | **Aceito** | Lacuna do Degrau 2 com um caso que **não** cancela (+1 nC a 1 cm e −3 nC a 2 cm: −2,25 × 10⁴ N/C). "Usa:" reescritas sem o método (o prompt exige mostrar as habilidades, então elas ficam, em termos neutros). |
| 11 | Fórmulas em bloco cortadas no celular sem aviso (a do P31, o limite de longe, L = rφ, a regra do ângulo) | 4 | atrapalha | **Aceito** | Equações longas quebradas em linhas (`aligned`); sombra de rolagem nas que ainda passarem da largura. |
| 12 | Texto dos SVG com 6–7 px no celular (P38, Teste 2, Pergunta 11, W2) | 4 | atrapalha | **Aceito** | Fonte dos SVG maior a ≤ 640 px; o gráfico do P38 separado do desenho do disco, em largura total. |
| 13 | Rótulo "Eq. 22-x" flutua para o parágrafo seguinte (a Eq. 22-16 parece ser a do disco) | 4, 1 | atrapalha | **Aceito** | Número da equação dentro do bloco, numa linha própria à direita. |
| 14 | Fig. 2-2 sem a seta roxa do total (o `aria-label` promete) | 4 | atrapalha | **Aceito** | Seta roxa do total desenhada. |
| 15 | Fig. 4-3: "120°" sem arco, lê-se como 60° | 4 | atrapalha | **Aceito** | Arco de 120° com "φ = 120°" e "60°" de cada lado. |
| 16 | Fig. 4-1: setas dE/dE′ parecem trocadas, rótulo "se cancelam" solto, falta a componente que sobra | 4 | atrapalha | **Aceito** | Rótulos "dE (de dq)" e "dE′ (de dq′)", tracejado prolongando cada reta pedaço–P, rótulo junto às componentes verticais. |
| 17 | W5: a diferença de 1 % em D = 5L ocupa 0,7 px; o gráfico não mostra o que a previsão pergunta | 4 | atrapalha | **Aceito** | W5 passa a plotar o **erro (%)** em escala logarítmica, com a faixa de 1 % sombreada. |
| 18 | P31: letra "a" para 12,0 cm e para 50 m; o centro e D não aparecem; figura fora de escala (a/L = 0,6 contra 1,47) | 2, 1, 4, 3 | atrapalha | **Aceito** | Nota no enunciado ("nos itens d e e o livro reusa a letra a; aqui chamamos de D"); Fig. 22-54 em escala, com o centro marcado; Fig. 5-1 com D tracejado. |
| 19 | W3 sem as componentes tracejadas que o texto promete; sem rótulos ±q; leitura em "kq/cm²" | 4 | atrapalha | **Aceito** | Componentes Ex e Ey do total tracejadas, cargas rotuladas, leitura também em N/C (q = 2,0 nC). |
| 20 | Falta um widget de F = qE com carga de prova de sinal escolhido (é o centro do Degrau 1 e do P81) | 4 | atrapalha | **Aceito** | W1 ganha "carga em P: nenhuma, +1 nC, −1 nC" com a seta preta F = qE e a leitura. |
| 21 | "r = a/√2" nos Erros comuns do Degrau 3, antes do ck3-3 e do P15 | 1, 2 | atrapalha | **Aceito** | O erro comum fica sem o valor ("r é a distância em linha reta: use Pitágoras"). |
| 22 | Termos sem definição: massa específica, mediatriz, hipotenusa, semelhante, arctan/atan, ângulo de referência, quadrante, condutor, tangente, média geométrica, binômio, ≫ | 1 | atrapalha | **Aceito** | Definidos no primeiro uso, em meia linha cada. |
| 23 | Passos Entender → Verificar nunca explicados antes do primeiro exemplo | 1 | atrapalha | **Aceito** | Legenda de uma linha antes do primeiro exemplo resolvido. |
| 24 | Símbolo θ sobrecarregado (ângulo do pedacinho e orientação do campo) | 3 | atrapalha | **Aceito** | Orientação do campo vira "ângulo com +x" (sem θ) no Degrau 3 e nos campos das questões; θ fica só para o pedacinho, como no livro. |
| 25 | Δx, Δy não definidos; falta a forma vetorial com sinal | 3 | polimento | **Aceito** | Δx = x_P − x_carga; forma vetorial \(\vec E = (kq/r^2)\hat r\) num bloco recolhido. |
| 26 | Nenhuma questão exige soma com módulos diferentes e ângulo fora dos eixos | 3 | atrapalha (falta prática) | **Aceito** | "Desafio" no Degrau 3: P15 com q₁ = +2e (179 N/C a 18,4°). |
| 27 | Analogias incompletas: barquinho = carga de prova **positiva**; mesa redonda só vale no centro e não cobre sinais opostos; "campos não se bloqueiam" vai colidir com blindagem; "pilha de anéis"; formiga "não muda nada" (cai 10 %); feira item 3 (com fontes fixas qualquer q vale) | 3 | atrapalha (leve) | **Aceito** | Uma frase em cada caixa "Onde a analogia quebra". |
| 28 | "Nenhuma das suas questões usa estes tópicos", mas o P9 é um dipolo | 1 | atrapalha (contradição) | **Aceito** | "Nenhuma questão pede as fórmulas destes tópicos (o P9 é um dipolo, mas se resolve somando duas cargas)". |
| 29 | Verificação do exemplo do hidrogênio é circular (F = eE é ke²/r²) e "difícil arrancar o elétron" é salto | 3, 1 | polimento | **Aceito** | Verificação contra o peso do elétron (F é 9 × 10²¹ vezes maior). |
| 30 | P81: "≈ 10⁹ N" é a estimativa grosseira (1,4 × 10⁹); a exata para carga na superfície é 7 × 10⁸ | 3 | polimento | **Aceito** | Dar os dois rótulos claros. |
| 31 | Verificador: P81 recusa −0,03 (dados com 2 algarismos); não lê "zero"; não converte cm ↔ m | 3 | polimento | **Aceito** | Tolerância de 5 % no P81-a; "zero"/"nulo" = 0; sufixos m, cm, mm convertidos para a unidade pedida. |
| 32 | Mensagens de conferência que entregam o passo: P31-b ("use kq/(a(a+L))"), P8 ("o parceiro"), P38 ("4,0 cm é o z...") | 2 | atrapalha | **Aceito** | Mensagens trocadas por perguntas que apontam o erro sem dar o passo. |
| 33 | Dica 2 do P31 entrega a armadilha do (d) (D − L/2) | 3 | polimento | **Aceito** | Essa linha desce para a Dica 3. |
| 34 | Fig. 22-42: "centro do quadrado" com o quadrado não desenhado | 3 | polimento | **Aceito** | 4º vértice pontilhado. |
| 35 | Fundo quadriculado das figuras parece escala; figuras de questão com grade | 3, 4 | polimento | **Aceito** | Grade mais fraca; figuras das questões sem grade. |
| 36 | P8: figura sem os valores das cargas; nada diz que zero é resposta possível | 4, 2 | atrapalha | **Aceito em parte** | Valores na figura (+5e, +5e, +3e, −12e). "Zero é uma resposta possível; confira por pares" vai para os Erros comuns do Degrau 2, não para o P8 (seria dica antes de pedir). |
| 37 | W2: sliders sem o valor; "total" sem seta quando zero | 4 | polimento | **Aceito** | Valor ao lado de cada slider; "total = 0" escrito. |
| 38 | Fig. 6-1 sem a componente que sobra; dois "z" | 4 | polimento | **Aceito** | Seta roxa vertical em P. |
| 39 | Mapa no celular invertido (6 no alto) e alinhado à direita | 4 | polimento | **Aceito** | Lista de 0 a 6, de cima para baixo. |
| 40 | Rótulos de passo (Entender...) sem recuo; linhas se atropelam | 4 | polimento | **Aceito** | Grade de duas colunas; no celular, rótulo acima do texto. |
| 41 | Ordens de grandeza que faltam (σ do P34 = 10 % do limite do ar; P15 ≈ campo de tempo bom; 3 × 10⁶ N/C = 3 kV/mm) | 4 | polimento | **Aceito em parte** | As três frases entram; régua logarítmica rejeitada (mais densa sem ganho para as questões). |
| 42 | Gota de Millikan sem diagrama de forças | 4 | polimento | **Aceito** | Diagrama pequeno no exemplo com lacunas. |
| 43 | Fig. 1-2: r e 2r em direções diferentes | 4 | polimento | **Aceito** | Seta de 2r também no eixo horizontal. |
| 44 | Pergunta 4 sem rótulo d; Pergunta 3 e 11 sem eixos rotulados; 53° longe do arco; Fig. 3-3 com rótulos cortados | 4 | polimento | **Aceito** | Ajustes de rótulo. |
| 45 | Densidade do enxofre "só para o P81b" (que é múltipla escolha) | 1 | polimento | **Aceito** | "(usada na resolução do P81b)". |
| 46 | "nível ··", "par" e tolerância de 2 % sem legenda | 1, 2 | polimento | **Aceito** | Legenda na abertura das questões (inclui "ângulos: vale qualquer equivalente, −90° = 270°"). |
| 47 | Fig. 22-14 citada como "fora da reta": é a 22-14b/c | 3 | polimento | **Aceito** | Corrigido. |
| 48 | "Semicírculo" para a barra (é semicircunferência) | 3 | polimento | **Aceito** | Trocado onde é a barra. |
| 49 | "fator 4/5 → 0" mistura número com limite | 1, 3 | polimento | **Aceito** | "o fator y/r → 0". |
| 50 | O Degrau 5 dá a fórmula fechada kq/(a(a+L)), então o P31 vira substituição | 2 | atrapalha | **Rejeitado** | O degrau existe para ensinar essa integral; o exemplo e a lacuna (P67) já treinam montá-la. O P31 cobra o que vem depois: λ com sinal, sentido, e o limite de longe. Pedir que o aluno refaça a integral no P31 não muda o que ele aprende. |
| 51 | A fórmula do semicírculo já vem pronta antes do P29 | 2 | polimento | **Rejeitado** | Mesmo motivo: é o resultado do degrau; o P29 treina compará-lo com a carga pontual. |
| 52 | Fig. 4-2 resolve a direção do P26 antes | 4 | polimento | **Rejeitado** | É a ideia do degrau (simetria com sinais); o P26 ainda pede montar λ do quarto, integrar e o módulo. |
| 53 | Acrescentar aos Erros comuns "o mais perto ganha", "mais pedaços não é mais campo", "disco menor com a mesma carga dá campo maior" | 1 | atrapalha | **Rejeitado** | Cada frase é a resposta de um checkpoint (ck2-2, ck4-3, ck6-1). Checkpoint é prática de recuperação; o feedback depois do erro já ensina o caso. |
| 54 | Numerar as divisões do eixo z do P38 | 1, 2 | atrapalha | **Rejeitado** | Achar quanto vale cada divisão é parte da habilidade (o livro só numera 0 e zₛ). A Dica 2 e o Erro comum 3 do Degrau 6 dizem isso. |
| 55 | W6 com modo "z em cm, R oculto" | 4 | atrapalha | **Rejeitado** | Resolveria o P38 por tentativa. A lacuna do P35 já treina a conta ao contrário. |
| 56 | Degraus 4 e 6 densos demais | 3 | atrapalha | **Aceito em parte** | As deduções continuam recolhidas; a parte "sinais opostos" fica (o P26 depende dela). A caixa de Cálculo do item 1 torna o Degrau 4 mais longo, mas tira o bloqueio. |
| 57 | Controles colados ("+1,0 nC+2,0 nC"), placeholder "Ainda não há respostas", gabarito do plano de revisão visível | 1 | polimento | **Rejeitado** | Os dois primeiros são da cópia cega (na página os botões são separados e o placeholder some com a primeira resposta). O gabarito do plano de revisão é recolhido de propósito, para conferir depois de fazer. |
| 58 | Item ∫x⁻² no teste de base antes de ensinar integral | 1 | atrapalha | **Aceito em parte** | O teste mede pré-requisito e a mini-revisão cobre; a v2 avisa que o Degrau 4 retoma integrais e explica o ∫cos θ que aparece na mini-revisão. |

## 2. Respostas do Professor

Marcadas com **[DT]**: vão para a seção "Dúvidas da turma" da v2, ligadas ao degrau.

### Aluno 1 (base frágil)

1. *Por que o palpite do gancho só volta no P81?* Porque o P81 é a mesma pergunta, com números. O fim do Degrau 1 já aponta para lá; a v2 repete a pergunta do gancho no próprio cartão do P81, com o seu palpite.
2. *Por que a regra de cancelamento vinha antes da previsão do W2?* Erro de ordem. Na v2 a previsão usa um caso que a regra não responde de cara (o mais perto ganha).
3. *A integral é a mesma com seno?* **[DT → D4]** Não com os mesmos limites. De −φ/2 a +φ/2, ∫sen θ dθ = 0, porque as duas metades se cancelariam se tivessem o mesmo sinal. Com sinais opostos, a metade de baixo empurra para o mesmo lado da de cima: integre de 0 a φ/2 e dobre. Para o semicírculo, 2∫₀^{π/2} sen θ dθ = 2.
4. *Por que radianos sem definir?* **[DT → D4]** Falha do guia. Um radiano é o ângulo em que o arco tem o comprimento do raio; uma volta (360°) tem 2π rad, então 180° = π rad e 120° = 2π/3 rad. É por isso que s = rφ só vale em radianos.
5. *Fiz 1 de 3: posso seguir?* Pode, mas releia antes os blocos que o feedback indicou e refaça as que errou. A página deixa marcar o degrau como concluído; a regra "2 de 3" é um sinal de que a base está firme, não uma tranca.
6. *Por que a Eq. 22-28 vem antes da 22-3?* Os números são os do livro, para você conseguir voltar a ele. O guia segue a ordem que ensina melhor, não a do livro.
7. *O que é "erro" em "erra 1 %"?* **[DT → D5]** A diferença entre o valor aproximado e o certo, dividida pelo certo. Com a barra, (E_certo − E_ponto)/E_certo = (L/2D)². O guia dava 33 % num lugar e 25 % em outro porque misturava as duas referências; agora é uma só.
8. *O P9 é um dipolo ou não?* **[DT → visão geral]** É: duas cargas iguais e opostas. Mas o problema se resolve somando dois campos (Degrau 3), sem as fórmulas de dipolo, que valem para pontos distantes. O P9 até confere uma previsão da teoria do dipolo: na mediatriz, o campo é oposto a \(\vec p\).
9. *Como sei se o arco tem "um só sinal"?* Pelo enunciado: "carga +q na parte superior e −q na inferior" (P26) é o caso de sinais opostos; "carga +Q distribuída uniformemente" (P29) é um só sinal.

### Aluno 2 (resolvedor)

1. *Por que a fórmula fechada da barra aparece antes do P31?* Ver item 50: o degrau ensina a integral; o P31 cobra λ com sinal, sentido e o limite de longe.
2. *Por que o P26-b aceita −90° e 270° sem avisar?* Porque são a mesma direção. A v2 diz isso na abertura das questões.
3. *De onde sai "cada divisão vale 2 cm" no P38?* **[DT → P38]** Do próprio gráfico: o eixo vai de 0 a zₛ = 8,0 cm e tem 4 divisões iguais, então cada uma vale 8,0/4 = 2,0 cm. Ler a escala assim é parte do problema (o livro também só numera 0 e zₛ).
4. *O P8 aceita zero sem pedir justificativa?* A conferência é numérica; a justificativa está na resolução comentada. A v2 avisa nos Erros comuns do Degrau 2 que zero é resposta possível e que se confere por pares.
5. *Por que a conferência do P9 fala em "fator 3/5" e não em E_x = E·Δx/r?* Mensagem reescrita para apontar a regra.

### Aluno 3 (monitor)

1. *P8: uma carga de prova em P fica em equilíbrio estável?* **[DT → D2]** Não. Suas derivadas estão certas: restauradora ao longo de q₁–q₂, instável ao longo de q₃–q₄ e fora do plano. É um ponto de sela. A soma das três derivadas é zero porque o campo não tem divergência fora das cargas (é a lei de Gauss do Cap. 23 em forma local); por isso nenhum arranjo de cargas paradas dá equilíbrio estável em todas as direções (teorema de Earnshaw).
2. *P9 com P na origem ou no eixo x fora do segmento?* **[DT → D3]** Na origem, os dois campos apontam para −x e somam: 2kq/9 = 6,39 × 10⁻¹⁰ N/C. A regra "sinais opostos → campo paralelo à reta das cargas" vale em toda a mediatriz. No eixo x fora do segmento (x = +6 m), o +q (a 3 m) empurra para +x e o −q (a 9 m) puxa para −x; ganha o mais perto, para +x. A regra não fala desse caso: ela é para pontos da mediatriz.
3. *P31: por que 50 m?* Porque o livro quer mostrar que, longe, as duas contas coincidem. Com D = 1,8 m (22 L) a diferença aparece no 3º algarismo; com 50 m ela é de 7 × 10⁻⁷.
4. *W5: 25 % ou 33 %? E por que (L/2D)² não vale para o disco?* **[DT → D5]** 25 % (referência: o valor certo); o guia agora usa só essa. O fator depende da forma: para a barra no eixo é exatamente (L/2D)²; para o disco no eixo, de longe, é 0,75(R/z)². O que vale sempre é "cai com o quadrado de tamanho/distância" (se a carga total não for zero).
5. *σ em cada face? Disco condutor?* **[DT → D6]** Para uma folha fina, o que conta é a carga total por área: com 5,3 µC/m² em cada face, σ_total = 10,6 µC/m² e Eₘ = 6,0 × 10⁵ N/C. No condutor, o campo junto à superfície é σ_face/ε₀ (Cap. 23), e a carga não fica uniforme (concentra na borda). O guia trata o disco isolante uniforme do livro.
6. *Metades opostas: quais limites?* Ver resposta 3 do Aluno 1. Para φ = π os dois resultados coincidem (2kλ/r) por acaso: ∫₀^{π/2} sen = ∫₀^{π/2} cos = 1. Para outro φ, o caso ± dá 2kλ(1 − cos(φ/2))/r.
7. *Chapa de cobre entre a barra e P: a superposição falha?* **[DT → D5]** Não. O cobre tem elétrons livres que se movem e criam um campo contrário; o campo em P é a soma do da barra com o das cargas induzidas no cobre. A superposição continua valendo; o que mudou é que apareceram cargas novas (Cap. 23, blindagem).
8. *Distância equivalente para o potencial?* Existe e é outra: L/ln((a+L)/a) = 9,10 cm no exemplo (a sua conta). Cada grandeza tem a sua média, porque 1/r e 1/r² pesam os pedaços de forma diferente.
9. *Distância equivalente do semicírculo; quartos do P26 como pontos?* Sua conta está certa: r√((φ/2)/sen(φ/2)), 1,25r para o semicírculo. O erro de 11 % ao trocar cada quarto por um ponto é o mesmo fator 1,11 do quarto de círculo do P29, porque é o mesmo arco de 90°.
10. *P15 com q₁ = +2e: que ângulo?* 18,4° (179 N/C). Virou o "Desafio" do Degrau 3.
11. *P81: quantos algarismos?* Dois (os dados têm dois). A v2 aceita 5 % nesse campo, e −0,03 passa.

### Aluno 4 (visual)

1. *P8 dá zero mesmo? E se q₄ estivesse do outro lado?* **[DT → D2]** Dá zero: os dois pares se cancelam (|q|/r² igual, sentidos opostos). Com q₄ na outra diagonal, q₃ e q₄ ficariam em lados opostos com sinais opostos: os campos se somariam, 346 N/C.
2. *Fig. 4-3: o 120° é o arco inteiro?* É o arco inteiro, 60° para cada lado do eixo; por isso a integral vai de −60° a +60°. A figura da v2 marca os dois.
3. *Fig. 4-1: posso desenhar cada dE ao longo da reta pedaço–P?* **[DT → D4]** Pode e deve: o dE de um pedaço positivo fica na reta que liga o pedaço a P, apontando para longe do pedaço. Por isso as setas parecem "cruzadas": a de cima vem do pedaço de baixo.
4. *No P31(d), uso a = 50 m ou 50 − L/2?* 50 m é a distância ao **centro**; a ponta perto fica a 50 − L/2. Com a fórmula kq/(D² − L²/4) não precisa escolher. A diferença é de 7 × 10⁻⁷ (relativa).
5. *Como enxergo o 1 % no W5?* Não enxergava: era defeito do gráfico. A v2 plota o erro em escala logarítmica com a faixa de 1 %.
6. *P38: como uso z/R = 1/√3 se R é a incógnita?* **[DT → P38]** Use ao contrário: você lê no gráfico o z da metade (4,0 cm) e sabe que, para qualquer disco, esse z vale R/√3. Então R = √3 × 4,0 cm.
7. *O 1:4 em d:2d é coincidência?* É de propósito no livro (P8). O guia exagerou e mostrou o mesmo par três vezes antes; a v2 deixa uma só. Na prova, o sinal é: |q| proporcional a r², então compare |q|/r² antes de calcular.
