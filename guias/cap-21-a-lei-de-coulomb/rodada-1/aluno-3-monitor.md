# Aluno 3 (Monitor cético) — Guia do Cap. 21, v1

Método: li o HTML inteiro (CSS só de relance), refiz em Python (`python3 -I`, só biblioteca padrão) todas as contas dos degraus, checkpoints, distratores, resoluções dos níveis 4 e 5 e valores de `data-resp`, reimplementei as fórmulas dos 6 widgets, comparei as 7 figuras de questão, o Teste 2 e o Teste 3 com as páginas do PDF (pg39, 44, 59, 60, 64, 67, 68, 69, 72) e li os trechos do livro em `cap-21-a-lei-de-coulomb.md`. Não abri navegador. Meus scripts ficaram na pasta de rascunho da sessão (`a3_checks.py`, `a3_ler.py`); nenhum arquivo do projeto foi alterado além deste relatório.

Resumo honesto: **todas as contas fecham** (nenhuma resposta numérica do guia está errada). Os problemas estão em (a) verificadores que recusam resposta certa, (b) lacunas de preparo entre o Degrau 3 e os problemas P42/P50, (c) dicas de nível 3 que já entregam o passo difícil, (d) frases fisicamente frouxas que vão morder nos caps. 22–25 e (e) analogias cujo "onde quebra" está pela metade. **Nenhum item bloqueia a subida**; classifiquei como "atrapalha" o que faz um aluno perder tempo ou ficar com ideia errada sem perceber.

---

## 1. Itens de crítica

Local: D0 a D6 = degraus; P7 etc. = questões; "l." = linha do `guia-v1.html`.

### 1a. Atrapalha

| # | Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|---|
| C1 | D3 inteiro (l. 1199–1441, "15 min") | denso demais · falta prática | **atrapalha** | Num degrau só: ΣF=0 com pêndulo, MCU, torque, ângulo pequeno, 3 figuras e 2 analogias. A única lacuna é o P52 (MCU, l. 1353). Pêndulo e torque têm só exemplo resolvido, e o de torque é um parágrafo de 3 linhas sem Entender/Modelar/Verificar (l. 1347–1351). Esses dois conteúdos destravam P42 e P50, os mais difíceis do grupo. O plano (tabela da seção 3) já previa só o P52 como lacuna. | Partir em 3a (equilíbrio), 3b (órbita), 3c (torque), ou pôr uma lacuna de pêndulo e uma de torque (ex.: refazer o mini-exemplo trocando 0,25 m por 0,40 m). |
| C2 | D3 → P42 | salto lógico | **atrapalha** | `sen θ = (x/2)/L` só aparece na Dica 3 do P42 (l. 2350) e na resolução. O exemplo do pêndulo (l. 1329–1345) tem θ sem nenhuma relação com o comprimento do fio; o widget W3 usa `x = 2L sen θ` no JavaScript (l. 3555) mas o texto não mostra isso. Quem abre só as Dicas 1–2 precisa reinventar a geometria. | Uma linha em D3 ("distância entre as esferas = 2L sen θ") e uma lacuna "ponha sen θ em função de x e L". |
| C3 | D2 lacuna P13 (l. 1130) | outro (verificador) | **atrapalha** | `data-resp="13.66" data-tol="0.02"` e `-13.66`. O gabarito do livro é −14 cm: 14 contra 13,66 é 2,5 % de diferença, fora da tolerância. Os dados do problema têm 2 algarismos (1,0 µC; 3,0 µC), então 14 é a resposta honesta; o aluno leva "vermelho". | Tolerância de 3 % nessa lacuna, ou aceitar a faixa 13,4 a 14,1. Regra geral: tolerância = max(2 %, meia unidade do último algarismo do gabarito). |
| C4 | P10(a) campo de resposta (l. 2508) e `lerNumero` (l. 2965) | outro (verificador) | **atrapalha** | A regex não tem âncora de fim. Refiz em Python: `"−2√2"` → −2,0; `"-2*sqrt(2)"` → −2,0; `"1/4"` → 1,0; `"10^-6"` → 10,0. Com −2√2 (forma em que o próprio guia escreve a resposta, l. 2550) o aluno recebe "Ainda não. Confira o desenho e a montagem antes das contas", justamente quando acertou. | Rejeitar entrada com caracteres sobrando, com mensagem "digite só o número, ex.: −2,83"; ou aceitar √ e /. |
| C5 | D1 Regra de ouro (l. 804–805), Mito 2 (l. 917) × P10 Dica 3 (l. 2536–2538), P10 resolução (l. 2550), P7 (l. 2176) | salto lógico (convenção de sinais) | **atrapalha** | D1: "um F negativo na calculadora ... você pôs sinais onde iam módulos". Mas a Dica 3 do P10 manda escrever a força "com os sinais das cargas (positivo = repulsão)" e a resolução usa `−kQq/a² − kQ²/(2√2 a²) = 0` com Q e q com sinal. É a forma vetorial (Eq. 21-1) disfarçada, que a D1 diz ser "fácil errar" (l. 809). O aluno recebe duas regras sem ponte e sem saber quando vale cada uma. | Uma frase no P10: "aqui uso a fórmula com sinal: positivo = repulsão; o sentido da componente vem da geometria. É a Eq. 21-1 sem escrever r̂." |
| C6 | D1 "Onde isso volta" (l. 979) | simplificação perigosa (Cap. 24) | **atrapalha** | "use módulos" aparece em D1 (3 vezes), Ex. P5, Mito 2, tabela de equações. O "volta" diz só que "a energia potencial kq1q2/r sai desta força". No Cap. 24, U e V levam o sinal de q (U<0 para atração). Um aluno treinado a pôr módulo vai errar o sinal da energia. | Aviso explícito: "no Cap. 24 o sinal de q entra na conta; aqui era só o módulo". |
| C7 | Nível 3 de P10 (l. 2536), P23 (l. 2628), P21 (l. 2704), P50 (l. 2446), P42 (l. 2350) | dica entrega demais | **atrapalha** | O "primeiro passo" já traz o passo mais difícil: P23 dá F(x) **e** F′(x) (sobra "igualar a zero"); P10 dá F1x completa com sinais e cos 45°; P21 reduz a ∫r dr; P50 dá a equação de torque com o sinal; P42 dá as 3 equações e o x/2. Sobra só álgebra. Além disso a Dica 1 do P23 (l. 2620: "x=0, fim do intervalo e meio") já é a receita das bordas que a D5 quer que o aluno lembre sozinho. | Nível 3 = 1 ingrediente (P23: "qual componente sobrevive e que fator a projeta?"); equações completas só no nível 4. Reescrever a Dica 1 do P23 sem citar as bordas. |
| C8 | P10(b) (l. 2513–2522), P42(a) (l. 2322–2331); feedback genérico no JS (l. 3246) | falta prática · dica entrega demais | **atrapalha** | O livro pede "Justifique" e "Mostre que"; o guia dá múltipla escolha com a justificativa pronta na alternativa certa. No P10(b), (b) "Sim, com Q = q" cai por inspeção e (d) "sinais opostos nunca ficam em equilíbrio" cai pelo Ex. 21.02: dá para acertar sem a conta. Quem erra só lê "Ainda não. Refaça o raciocínio" (ao contrário dos checkpoints, que explicam cada alternativa). | Pedir uma linha escrita (como a "reflexão") e dar feedback por alternativa; no P42(a), pedir a expressão de sen θ em campo de texto. |
| C9 | Visão geral, "Aterramento" (l. 2103) | erro físico (simplificação) | **atrapalha** (Caps. 23 a 25) | "Ligar à Terra neutraliza o objeto." Só vale longe de outras cargas (Ex. 21.03b do livro). Com um bastão carregado perto, o condutor aterrado fica com carga induzida diferente de zero; o que se iguala é o potencial (V = 0), não a carga. É erro clássico de prova do Cap. 24. | "...se não houver outras cargas por perto. No Cap. 24: aterrar fixa V = 0." |
| C10 | D6 (l. 1914–1917) e Cap. 22 | termo não definido · falta prática | **atrapalha** (Cap. 22) | Só se define ρ (volume). O Cap. 22 começa com dq = λ ds e σ dA (linha, anel, disco) e o próprio livro usa σ no P71. "O Cap. 23 inteiro depende dela" subestima o 22. D5 e D6 nunca se encontram (anel = x/(x²+d²)^{3/2} com dq contínuo). | Tabelinha ρ, σ, λ com dV, dA, ds; um exemplo de anel ligando D5 e D6. |
| C11 | D1 analogia da lâmpada (l. 742–743, 773) | erro físico (analogia) | **atrapalha** (Caps. 23 e 33) | (i) "não existe luz negativa que apague a outra": luz apaga luz por interferência destrutiva. (ii) O 1/r² da lâmpada é da **intensidade** (∝ E², potência/área); o 1/r² de Coulomb é da força, ∝ E. A amplitude de uma onda irradiada cai como 1/r. A analogia transporta "1/r²" entre grandezas diferentes e o aluno tropeça no Cap. 33–34. | Trocar "luz" por "fluxo que atravessa cada esfera" e dizer na caixa "a lâmpada mede energia (E²); aqui o 1/r² é do próprio campo". |
| C12 | Todos os quizzes (l. 620 a 2880) | outro (viés de posição) | **atrapalha** (calibração) | Contei `data-correta`: nas 32 perguntas de checkpoint/revisão a certa é **b em 18 (56 %)**, a em 10, c em 4, **d em nenhuma**; as 6 do teste de pré-requisitos são todas "b". Nos "prever" a certa é b em 5 de 7. O painel de calibração (confiança × acerto) fica contaminado: dá para chutar "b" com "tenho certeza". Também há alternativa certa mais longa/específica (D6 pergunta 1, único item com a integral; W3, único com "1,6 vez"). | Embaralhar posições; igualar comprimento; usar d como certa em ~25 %. |
| C13 | Cabeçalho (l. 9, 27, 28) | outro | **atrapalha** (offline) | KaTeX vem só do CDN jsdelivr, sem cópia local. Sem rede, as ~1100 fórmulas aparecem como `$\dfrac{...}$` e as `<svg>` continuam, mas a leitura das equações (o conteúdo do guia) some. Eu não pude testar offline (sem navegador), é inferência do código. | Embutir KaTeX (ou pelo menos avisar no topo "precisa de internet"). |
| C14 | D5 lacuna (l. 1827–1842) | falta prática | **atrapalha** | A derivada da lacuna é de x/(x²+a²) (quociente simples). O passo real do P23 é d/dx[x(x²+d²)^(−3/2)] (cadeia + produto), que só aparece pronto na Dica 3 (l. 2628). O pré-quiz 5 treina a cadeia isolada. | Trocar a lacuna por g(x) = x/(x²+a²)^(3/2), com a mesma estrutura de lacunas. |

### 1b. Polimento

| # | Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|---|
| C15 | D0 gancho (l. 579–580; figura l. 591–596) | erro numérico (arredondamento) | **polimento** | O texto mostra 1,3×10⁷ C por copo; com esse valor, k q²/1² = 1,52×10²⁴ N e a razão com Sol–Terra é 43. O guia escreve 1,6×10²⁴ N e "46 vezes", que saem de 1,339×10⁷ C sem arredondar. O aluno cético que refizer com o número da tela vai achar que errou. | Usar "1,34×10⁷ C", ou "cerca de 1,5×10²⁴ N, umas 43 vezes". |
| C16 | W1, nota (l. 866) | erro numérico | **polimento** | "as de 2000 N não caberiam": o máximo possível (5 µC e 5 µC a 2 cm) é **562 N**. | "as de 560 N". |
| C17 | W1 desenho (JS l. 3436) | figura confusa | **polimento** | `dpx = 60 + (R−2)/28·230`: R=2 cm → 60 px; R=30 cm → 290 px (razão 4,8, não 15) e o rótulo diz "r = ... cm". Num widget sobre 1/r² a escala torta confunde. | Avisar "fora de escala" ou usar escala linear. |
| C18 | D2 Ex. 21.02 (l. 1100), R8 (l. 2880–2890) | erro físico (impreciso) | **polimento** | "Esse equilíbrio é instável", sem qualificar. Refiz: com o próton em (2L+δ): dF_x/dx = +2 (L=1) ⇒ instável ao longo de x. Mas em (2L, 0,01L): F_y = −0,0100 (restauradora) ⇒ estável na transversal. É um ponto de sela. Com um elétron (D2 pergunta 3 troca o próton por elétron) todas as forças invertem: estável ao longo de x, instável na transversal. | "instável ao longo do eixo" (e, se quiser, citar Earnshaw). |
| C19 | D2 cabo de guerra (l. 997–999) | erro físico (limite da analogia) | **polimento** | "puxa (atração) ou empurra (repulsão)": numa corda só se puxa. A bandeira no cabo de guerra tem equilíbrio estável; as cargas, instável (Ex. 21.02). A analogia só descreve "entre as cargas"; as regiões de fora (onde moram P7, P13, Ex. 21.02) não têm equivalente. | Acrescentar à caixa "quebra". |
| C20 | D1 (l. 743) | erro físico (causalidade) | **polimento** | "por isso aparece um 4π na constante": o livro diz "por motivos históricos e para simplificar outras expressões". Em unidades gaussianas F = q1q2/r² sem 4π; o SI pôs o 4π em k para ele sumir da lei de Gauss. | "o 4π é a mesma área 4πr² que o Cap. 23 vai usar; o SI escolheu deixá-lo aqui." |
| C21 | Visão geral (l. 2101) | erro físico | **polimento** | "Em condutores (metais, corpo humano, água de torneira), elétrons de condução andam livres ... Só os elétrons se movem": na água e no corpo quem se move são íons. O livro diz "elétrons, no caso dos metais". | "em metais, elétrons; em água e corpo, íons". |
| C22 | Visão geral (l. 2102) | imprecisão | **polimento** | "empurra os elétrons dele para um lado": só se a carga que se aproxima é negativa; se for positiva, atrai. Também vale para isolantes (polarização), não citada. | "reorganiza as cargas: afasta as de mesmo sinal, atrai as de sinal oposto". |
| C23 | D1 Ex. P5 (l. 877); ficha (l. 836); P42 (l. 2296); P50 (l. 2389); P73 (l. 2263) | salto lógico (hipótese não dita) | **polimento** | "Eq. 21-4 só vale para partículas (ou esferas com carga uniforme)" sem "vistas de fora" e sem "longe de outras cargas" (o livro tem essa ressalva, pg39: carga da casca ≫ carga da partícula). P42 e P50 usam "esferas condutoras" e ninguém diz que Coulomb é aproximado (x ≫ raio). Nenhuma ocorrência de "repouso"/"estático": P73 usa Coulomb num elétron a 0,7 % de c. | Uma linha em D1: "vale para cargas paradas (ou lentas), pontuais ou esferas vistas de fora"; hipótese explícita em P42/P50/P73. |
| C24 | D3 mini-exemplo (l. 1347–1351) e P50 (l. 2454) | hipótese não dita | **polimento** | A esfera da ponta direita tem peso e fica a 0,50 m do apoio; o exemplo ignora. No P50 o livro diz "barra de massa desprezível", mas não "esferas de peso desprezível"; "L ≫ h" aparece só na resolução, não no enunciado. Refiz o erro de ignorar as forças cruzadas: componente vertical da repulsão +Q(esq.)→2q = 3,5×10⁻³ N contra 3,6 N (0,1 %) com L=1 m e h=10 cm. | Dizer "pesos das esferas desprezados" e quantificar o 0,1 %. |
| C25 | D3 d3a feedback (l. 1400–1403) | salto lógico | **polimento** | "mais peso: tan θ = Fe/(mg) diminui" ignora que Fe cresce quando x diminui. Conclusão certa (confirmei no W3: m×2 reduz θ), argumento incompleto. | "Fe sobe um pouco, mas menos que mg". |
| C26 | D3 analogia solar (l. 1243–1244) | limite de analogia | **polimento** | Só cita a radiação. Falta: no gravitacional qualquer raio vale; no Bohr r = n²a₀ (o P73 diz). Falta também dizer que o elétron real não tem trajetória. | Uma frase. |
| C27 | D3 gangorra (l. 1245) | analogia sem "quebra" | **polimento** | É a única analogia sem caixa "onde quebra". A reação da força elétrica está numa esfera fora do sistema (Q fixa, apoiada no chão). | Frase curta. |
| C28 | D2 figura (l. 1030–1048) | figura confusa | **polimento** | No painel de baixo (sinais opostos) aparece "✓ pode anular" à esquerda **e** à direita, e a legenda diz que só um funciona. As duas cargas estão desenhadas iguais (r=12); com módulos iguais não há ponto de força nula em lugar nenhum. | Desenhar + maior e − menor, e marcar ✓ só no lado certo. |
| C29 | D1 fig. lâmpada (l. 779–791) | figura confusa | **polimento** | Os dois arcos mostram comprimento ×2 (é uma seção 2D) e o rótulo diz "área 4× maior". Quem olha vê "o dobro". | Desenhar um quadrado r×r e outro 2r×2r em cada esfera. |
| C30 | D5 fig. f5a (l. 1729–1731) | figura | **polimento** | Cada componente x mede 50 px, a soma desenhada mede 76 px (devia ser 100). Os rótulos "F de baixo" ficam junto da seta de cima (certo, mas parece trocado). | Refazer escala; rotular "da carga de baixo". |
| C31 | Fig. Teste 3, texto alternativo (l. 1626) | figura confusa (leitor de tela) | **polimento** | "(b) p, e a d, p a D do primeiro próton": no PDF (pg44) e no SVG, D é a distância do **elétron** ao segundo próton. A figura está certa; o texto alternativo não. | Corrigir o texto. |
| C32 | Revisão, plano (l. 2902–2903) | outro | **polimento** | "Faça os Problemas 13 e 40 do livro" e "faça o Problema 11": o 13 e o 11 já foram as lacunas de D2 e D4, com gabarito na tela. Refazer o mesmo item mede memória da resposta. | Trocar por outros ímpares com gabarito (P9, P19, P29) ou refazer com valores novos. |
| C33 | Vários (l. 1207, 1284, 1000, 2389) | termo não definido | **polimento** | "MEMS", "eletroscópio", "polo", "articulada" sem definição; "carga de prova" usada no texto (l. 1000) antes de a legenda defini-la (l. 1048) e nunca dito "pequena, que não perturba as fixas" (Cap. 22: q₀ → 0). | Glossário de 6 linhas. |
| C34 | Tempos (l. 574, 730, 987, 1203, 1448, 1702, 1911) | denso demais | **polimento** | 15 min para D3, D4 ou D5, cada um com pré-quiz + widget + exemplo + lacuna + mitos + 3 perguntas, é otimista para quem vê pela primeira vez. Soma 89 min só se nada demorar. | Medir com 2 alunos reais e ajustar o rótulo. |

### 1c. Onde a analogia quebra: está honesto?

| Analogia | O que a caixa admite | O que falta (limite real) | Veredito |
|---|---|---|---|
| Lâmpada na esfera (D1) | luz viaja e carrega energia; "só serve para o 1/r²" | luz também se anula (interferência); 1/r² é da intensidade, não do campo; a amplitude irradiada cai 1/r; 4π é convenção; só vale em 3D | **Parcial**, com um erro (C11). |
| Cabo de guerra (D2) | os times se cansam; superposição | corda não empurra; equilíbrio estável × instável (Ex. 21.02); só cobre "entre as cargas" | **Parcial** (C19). O que mais importa (zero fora do par) não tem correspondente. |
| Sistema solar/Bohr (D3) | irradia e cai em ~10⁻¹¹ s (refiz: 1,6×10⁻¹¹ s) | raios quantizados × qualquer raio; sem trajetória | **Boa**, a única com número. Falta um pouco (C26). |
| Gangorra (D3) | nada | reação em corpo fora do sistema; peso das esferas | **Sem caixa** (C27). |
| Quadras (D4) | só ruas × diagonal | — | **Honesta e suficiente.** |
| Densidade populacional (D6) | espessura → 0; carga discreta | população é por área, ρ por volume; densidade pontual é limite, não média | **Honesta.** |

### 1d. Figuras: comparação com o PDF

| Figura | Resultado |
|---|---|
| 21-23 (P7), pg59 | Confere: 1, 2, 3 em ordem, L₁₂ entre 1 e 2, L₂₃ entre 2 e 3, sem sinais. |
| 21-25 (P10, P11, P70), pg60 | Confere: 1 em cima à esquerda, 2 em cima à direita, 3 embaixo à esquerda (origem), 4 embaixo à direita; eixos pelos cantos 1–3 e 3–4. As componentes do P11 (0,1693 e −0,0465 N) batem com o gabarito. |
| 21-32 (P23), pg64 | Confere: 1 em +d, 2 em −d, 3 no eixo x. |
| 21-39 (P42), pg68 | Confere: dois fios de comprimento L do mesmo ponto, θ de cada lado da vertical, x entre as esferas. |
| 21-42 (P50), pg69 | **Confere com o PDF e a discrepância do texto é real.** O PDF português diz (pg69) "nas extremidades **direita e esquerda** ... carga positiva q e 2q, **respectivamente**" (⇒ q à direita, 2q à esquerda); a figura mostra **+q à esquerda, +2q à direita**, bloco P à direita do apoio, com x medido da ponta esquerda. O guia segue a figura e avisa (l. 2391). |
| P42, enunciado, pg67 | O PDF realmente imprime "tan θ ≤ sen θ" (o aviso do guia é verdadeiro) e a fórmula x = (q²L/2πε₀mg)^(1/3). |
| Teste 2, pg39 | e, p, p em reta: confere (gabarito do livro: esquerda, esquerda, esquerda). |
| Teste 3, pg44 | (a), (b), (c) conferem; só o texto alternativo de (b) está errado (C31). |
| Fig. 21-7e/f (Ex. 21.01c) | Não tive a página; conferi a geometria do SVG: 4 a 3R/4 e 59,8°; comprimentos das setas 52 : 92 : 80 px = 1,15 : 2,05 : 1,78 (escala 45 px por 10⁻²⁴ N). Coerente. |
| P21 e P73 | "Figura do guia" (o livro não tem). Raios proporcionais: 4 : 6 e 1 : 4. |

---

## 2. Perguntas ao Professor

1. **Professor, e se eu empurrar o próton do Ex. 21.02 para cima, em vez de para a esquerda ou direita?** Refiz a conta: em (2L, 0,01L) a força vertical é −0,0100 (kq q_p/L² por unidade), ou seja, restauradora. Então o equilíbrio é instável ao longo do eixo e estável na transversal? E se for um elétron (a pergunta 3 do checkpoint D2), os papéis se invertem? O guia só diz "instável".
2. **Professor, no P7 o enunciado diz que 1 e 2 são fixas. E se eu soltar as três?** Com a razão −4 e q₃ = q₁ = −4q₂, as três forças se anulam ao mesmo tempo (confere: na 1, na 2 e na 3). Isso é coincidência? E esse equilíbrio de três cargas livres é estável?
3. **Professor, por que a D1 diz "nunca ponha sinal na Eq. 21-4" e depois a Dica 3 do P10 escreve a força "com os sinais das cargas, positivo = repulsão"?** Quando devo usar uma e quando a outra? E no Cap. 24, onde U = kq₁q₂/r leva o sinal, como evitar que eu leve o hábito do módulo?
4. **Professor, o P50 manda desprezar as forças "cruzadas" (a +Q da esquerda sobre a esfera 2q da direita). Qual é o limite de "barra longa"?** Com os valores-teste (L = 1 m, h = 10 cm) refiz: 0,1 % no torque. Mas se L = 3h, ou no item (b) com h = 7,3 cm e L menor, quanto erra? O guia só diz "L ≫ h" na resolução, não no enunciado.
5. **Professor, no P42 usamos tan θ ≈ sen θ. Dá para resolver sem aproximar?** Fica sen²θ·tan θ = kq²/(4L²mg), que só se resolve numericamente (no (b), x exato = 4,9993 cm). E para q grande, x → 2L. Em que valor de θ a "demonstração" deixa de valer, e por que o livro imprime "≤"? Se for erro de digitação, como eu sei que não é um limite?
6. **Professor, P42 e P50 falam em "esferas condutoras", e a lei de Coulomb com cargas no centro só vale para distribuição uniforme.** Quando duas esferas condutoras carregadas estão a 5 cm uma da outra, a carga se redistribui. Qual deve ser o raio para o guia poder dizer que o erro é desprezível? Isso não deveria estar nas hipóteses?
7. **Professor, na D1 o guia diz que a "influência" se espalha como a luz de uma lâmpada. Mas luz se anula por interferência e a amplitude de uma onda irradiada cai como 1/r, não 1/r².** Em que sentido, exatamente, a lâmpada explica o 1/r² de Coulomb? E o 4π: é geometria ou convenção?
8. **Professor, "ligar à Terra neutraliza o objeto". E se tiver um bastão carregado perto da esfera aterrada?** A esfera fica com carga induzida diferente de zero? Então o que o aterramento fixa, a carga ou o potencial?
9. **Professor, no P73 a conta usa a massa do elétron e o próton parado. Se eu usar massa reduzida e a relatividade, quanto muda v?** Refiz a massa reduzida: v cai 0,03 %, longe do 2 % de tolerância. E o elétron acelerado irradia (a própria caixa diz isso): em que ordem de grandeza a conta continua válida durante uma volta?
10. **Professor, no P23 q₃ é positiva. E se fosse negativa?** O módulo máximo é o mesmo (4,9×10⁻²⁶ N), mas então x = 0 vira equilíbrio estável ao longo de x? E o mínimo do módulo continua em x = 0?
11. **Professor, o plano de revisão manda "fazer o Problema 13 e o Problema 11" depois de 3 e 7 dias, mas eles já foram as lacunas de D2 e D4, com o gabarito na tela.** Isso treina o raciocínio ou a memória da resposta? Pode me dar outros dois ímpares com gabarito?
12. **Professor, as D3, D4 e D5 têm "15 min". Quanto tempo o senhor gastou fazendo D3 sem ajuda?** (Eu gastei mais de 15 só nas contas de verificação.)

---

## 3. Contas refeitas

Constantes iguais às do guia (k = 8,99×10⁹; ε₀ = 8,85×10⁻¹²; e = 1,602×10⁻¹⁹; mₑ = 9,109×10⁻³¹; g = 9,8). "ok" = igual dentro do número de algarismos do guia.

| Item | Valor do guia | Meu valor | ok/diverge |
|---|---|---|---|
| D0: carga positiva em 250 mL de água | 1,3×10⁷ C | 1,339×10⁷ C | ok |
| D0: F entre dois copos a 1 m (com 1,3×10⁷ C exibido) | 1,6×10²⁴ N | 1,52×10²⁴ N (1,61×10²⁴ só com 1,339×10⁷) | **diverge** (C15) |
| D0: razão com Sol–Terra (3,54×10²² N) | 46 | 45,5 (43 com o 1,3×10⁷ exibido) | **diverge** (C15) |
| P5 (D1) | 2,81 N | 2,809 N | ok |
| P3: k·q₁·q₂ e r | 10,99 N·m²; 1,388 m | 10,986; 1,3883 | ok |
| Checkpoint D1 pergunta 3 (+2 µC e −2 µC a 3 cm) | 40 N | 39,96 N | ok |
| Distratores D1: 4,0×10⁻³ N e 1,2 N | idem | 4,0×10⁻³ N; 1,199 N | ok |
| Ex. 21.04: dois prótons a 4,0 fm | 14 N; 1,2×10⁻³⁵ N; 1,2×10³⁶ | 14,42 N; 1,16×10⁻³⁵ N; 1,24×10³⁶ | ok |
| Na⁺Cl⁻ a 2,82×10⁻¹⁰ m | 2,9×10⁻⁹ N | 2,901×10⁻⁹ N | ok |
| Distratores R2: 8,2×10⁻¹⁹ e 1,8×10¹⁰ N | idem | 8,18×10⁻¹⁹; 1,81×10¹⁰ | ok |
| W1: força máxima possível (5 µC, 5 µC, 2 cm) | "2000 N" | 561,9 N | **diverge** (C16) |
| Ex. 21.02: x = 2L; raiz negativa x = 2L/3 | 2L; 2L/3 | 2L; 0,667 L | ok |
| Ex. 21.02: estabilidade em 2L (dF_x/dx, L=1) | instável | +2 (instável em x); transversal restauradora | ok em x; incompleto (C18) |
| P13 lacuna: s e x | 13,66 cm; −13,66 cm | 13,660; −13,660 | ok; verificador recusa o "−14" do gabarito (2,5 %) (C3) |
| D2 checkpoint 1 (+q e +4q): s | L/3 | 0,3333 L | ok |
| D2 checkpoint 2 (+2q em 0, −q em L): ponto | x > L | 3,414 L | ok |
| Pêndulo D3: F_e; mg; θ; T | 5,62×10⁻³; 1,96×10⁻²; 16,0°; 2,04×10⁻² | 5,619×10⁻³; 1,960×10⁻²; 15,996°; 2,039×10⁻² | ok |
| Erro tan→sen: 1°, 5°, 10°, 20°, 30°, 16° | 0,015; 0,38; 1,5; 6,4; 15; ~4 % | 0,0152; 0,382; 1,543; 6,418; 15,47; 4,03 | ok |
| Gangorra: F e P | 0,899 N; 1,80 N | 0,899; 1,798 | ok |
| P52 lacuna: abs(Q) | 1,112×10⁻⁵ C | 1,1124×10⁻⁵ C | ok |
| Elétron clássico cai em | ~10⁻¹¹ s | 1,56×10⁻¹¹ s | ok (ordem) |
| P73: v₁, v₂, v₃ | 2,188×10⁶; 1,094×10⁶; 7,29×10⁵ m/s | 2,1878×10⁶; 1,0939×10⁶; 7,292×10⁵ | ok |
| P73: v₁/c; núcleo +2e | 0,73 %; 3,09×10⁶ | 0,7297 %; 3,094×10⁶ | ok |
| P73: distratores R7 | 2,43×10⁵; 1,26×10⁶; 6,56×10⁶ | v₁/9 = 2,431×10⁵; v₁/√3 = 1,263×10⁶; 3v₁ = 6,563×10⁶ | ok |
| P42(b): abs(q) | 2,383×10⁻⁸ C | 2,3825×10⁻⁸ C | ok |
| P42: θ; F_e; F_e/(mg) | 1,2°; 2,04×10⁻³; 0,0208 | 1,194°; 2,041×10⁻³; 0,02083 | ok |
| P42: x sem aproximar | (aprox. 5,0 cm) | 4,9993 cm | ok (0,014 %) |
| P43(b): x′ = x/4^(1/3); 2^(2/3) | 3,1 cm; 1,59 | 3,150 cm; 1,587 | ok |
| P50: kqQ/h² (valores-teste) | 1,80 N | 1,798 N | ok |
| P50(a): x (valores-teste) | 58,99 cm | 58,99 cm | ok |
| P50(b): h | 7,344 cm | 7,3444 cm | ok |
| P50: x com h de (b) | 2L/3 | 0,6667 L | ok |
| P50: leitura do texto PT (2q à esquerda) | 41,0 cm | 41,01 cm | ok |
| P50: força vertical cruzada / principal | (não citado) | 3,5×10⁻³ N / 3,6 N = 0,1 % | n/a |
| P11: F₃₁, F₃₄, F₃₂, componente | 0,0719; 0,1438; 0,03596; 0,0254 N | 0,07192; 0,14384; 0,03596; 0,02543 | ok |
| P11: F_x e F_y | 0,1692; −0,0465 N | 0,16927; −0,04649 | ok |
| P10: Q/q; F sobre 1 e 4 | −2√2; 0 | −2,828; 0 | ok |
| P10: F sobre 2 com Q/q = −2√2 | 3,50 kq²/a², para o centro | 3,500; (−1,−1)/√2 | ok |
| P10(b): Q/q para anular em 2 | −1/(2√2) | −0,3536 | ok |
| Ex. 21.01c: F₁₂, F₁₄ | 1,15×10⁻²⁴; 2,05×10⁻²⁴ | 1,1507; 2,0457 | ok |
| Ex. 21.01c: F_x; F_y; F; θ | −1,25×10⁻²⁵; 1,78×10⁻²⁴; 1,78×10⁻²⁴; 94,0° | −1,25; 1,775; 1,780; 94,03° | ok (com o arredondamento intermediário do livro) |
| D5: F(0); F(d)/F(0) | 2,0×10⁻⁵ N; 0,354 | 1,998×10⁻⁵; 0,3536 | ok |
| P23(b), (d) | 12,0 cm; 4,90×10⁻²⁶ N | 12,02 cm; 4,904×10⁻²⁶ | ok |
| P23: F(5,0 m); razão ao máximo | 1,5×10⁻²⁸ N; 0,3 % | 1,470×10⁻²⁸; 0,2998 % | ok |
| P51(a): n; P51(b): q e n | 2,00×10¹⁰; −2,13×10⁻⁹ C; 1,33×10¹⁰ | 1,9975×10¹⁰; −2,133×10⁻⁹; 1,3317×10¹⁰ | ok |
| D6 lacuna (casca ρ₀ uniforme) | 3,183×10⁻⁹ C | 3,1835×10⁻⁹ | ok |
| P21: q; ρ(r₂)V; ρ(r₁)V; esfera maciça | 3,77×10⁻⁸; 3,18×10⁻⁸; 4,78×10⁻⁸; 6,79×10⁻⁸ | 3,7699; 3,1835; 4,7752; 6,7858 (×10⁻⁸) | ok |
| W2: zero para q₂/q₁ = −0,25; +4 | 2L; L/3 | 2,000; 0,3333 | ok |
| W3 (50 nC, 0,5 m, 5 g): razão x(100 nC)/x(50 nC) exata | "cerca de 1,6" | 1,585 | ok |
| W3: x exato × aproximado (padrão) | — | 7,704 cm × 7,712 cm (θ = 4,4°) | ok |
| W4: força resultante em Q/q = −2,75; −3 | "bem pequena" (<0,15) | 0,108; 0,257 | ok |
| W5: máximo com cargas iguais | 0,9 (eixo) | 0,770 em x/d = 0,707 | ok |
| W6: N = 1, 5, 40 (erro da soma à esquerda) | "dezenas de %" | −66,7 %; −13,3 %; −1,7 % | ok |
| Parser: "−2√2" para o campo do P10(a) | aceito? | lido como −2 ⇒ "Ainda não" | **diverge** (C4) |

---

## 4. O que funcionou (não remover na v2)

- **Figuras de questão fiéis ao PDF**: P7, P10/P11, P23, P42 e P50 batem em posição, rótulos e orientação; o Teste 2 e o Teste 3 também.
- **O tratamento do P50**: o aviso é verdadeiro (o PDF português troca mesmo q e 2q), o guia segue a figura e o original em inglês, e a resolução mostra a leitura alternativa (41,0 cm, h inalterado). Está certo e honesto. O aviso do P42 sobre "≤" também (o PDF imprime "≤").
- **Valores-teste do P50** (59,0 cm, 7,34 cm): é a única maneira justa de conferir resposta simbólica; os números estão certos.
- **A etapa "Verificar"** de todas as resoluções: casos-limite que de fato fecham (P7 com L₂₃ → ∞ dá −1,002; P50 com h de (b) dá x = 2L/3; P21 entre ρ(r₂)V e ρ(r₁)V; P42 conferido pelo P43 do gabarito).
- **Distratores numéricos dos checkpoints** (cm sem converter, r sem quadrado, v₁/9, v₁/√3, 3v₁): cada um corresponde a um erro real e os números estão certos. É o melhor feedback do guia.
- **"Erros comuns"** (18 mitos, 3 por degrau): todos concretos, curtos e corretos.
- **Dica 1 de P7, P73, P42, P50 e P21**: perguntas, não respostas. Boas.
- **Previsão antes do widget**: força o chute; os widgets estão fisicamente certos (W2, W4, W5, W6 batem com o que refiz; W3 mostra 1,585 vs "cerca de 1,6").
- **Mensagens do verificador** ("módulo certo, sinal errado"; "fator 10⁻²: unidade"): ajudam. Aceitar 2,19×10⁶ com sobrescrito também.
- **Nota do arredondamento intermediário no Ex. 21.01c** (−1,25×10⁻²⁵ do livro × −1,28×10⁻²⁵ sem arredondar).
- **Rótulo "calculada pelo guia, sem gabarito oficial"** nas pares: transparente.
- **Revisão intercalada com confiança** e painel "confiante e errou" (depois de corrigir C12).
- **Contas do `calculos.py`**: reproduzi todas independentemente.
