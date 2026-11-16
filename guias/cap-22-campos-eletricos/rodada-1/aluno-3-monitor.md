# Aluno 3, Monitor cético: Cap. 22 (guia-v1.html)

Eu refiz as contas sozinho (`rodada-1/aluno-3-contas.py`, só biblioteca padrão, sem ler o `calculos.py` do Professor; `python3 -I aluno-3-contas.py --md` imprime a tabela completa de 133 itens). Comparei as figuras com o PDF original do livro (páginas 82, 99, 115 a 117, 120, 122, 125 a 127, 129). Testei o verificador numérico rodando o próprio `lerNumero` e `bate` do HTML em Node com cerca de 130 entradas.

**Resultado em uma linha:** as respostas das 8 questões, dos exemplos, das lacunas, dos "e se..." e das leituras de widget estão certas (nenhuma conta do guia diverge). O que encontrei são inconsistências de texto, uma instrução de integral que leva a zero, simplificações que vão doer nos Caps. 23 a 25, feedbacks de erro com número errado e furos nas analogias. **Nada bloqueia.**

---

## 1. Itens de crítica

Gravidade: **bloqueia** (o aluno não consegue avançar ou aprende errado sem perceber), **atrapalha** (confunde ou causa erro mais tarde), **polimento**.

| # | Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|---|
| C1 | Degrau 4, "E se as metades tiverem sinais opostos?" (`guia-v1.html`, linha 1202) | salto lógico (instrução que leva a erro) | **atrapalha** | "A integral é a mesma, só que com sen θ no lugar de cos θ." Com os limites do método (−φ/2 a +φ/2), ∫sen θ dθ = 0 (seno é ímpar): quem segue a frase ao pé da letra acha E = 0. O certo é 2∫₀^{φ/2} sen θ dθ (ou integrar \|sen θ\|). "A mesma integral" só coincide em valor para φ = π (2kλ/r nos dois casos). Para outro φ difere: o modo ± do W4 usa 2(1−cos(φ/2))/φ (0,637 em 180°); para φ = 360° o arco uniforme dá 0 e o ± dá 0,637 kQ/r². A Síntese repete só "integre com seno". O P26-3 já está certo (2∫₀^{π/2}), então o erro é só no texto do degrau. | Escrever: "integre só a metade de cima, de 0 a φ/2, com sen θ, e dobre (a de baixo, com sinal oposto, empurra para o mesmo lado)". Ajustar a linha da Síntese. |
| C2 | Degrau 5: `prev-w5` a) e b) contra o widget W5, o exemplo da barra de 10 cm e `ck5-3` a) | erro numérico (inconsistência) | **atrapalha** | prev-w5 a): "Com D = L, o erro ainda é de **33 %**"; b): "D = 2L, **uns 7 %**". O widget imprime "erra **25 %** (para menos)" em D = L, o exemplo diz "25 % abaixo do valor certo" e ck5-3 a) diz "25 % é o erro bem de perto (P a meio comprimento da ponta)". Meu cálculo (integral numérica): barra/ponto = 1,3333 em D = L e 1,0667 em D = 2L. Então 33 % e 6,7 % são relativos ao valor pontual; 25 % e 6,25 % são relativos ao valor real. O mesmo D = L recebe dois números, e o aluno que testa no widget vê 25 %. Em D = 5L e D = 10L as duas definições coincidem (1 %, 0,25 %). | Uma definição só (a do widget: erro do pontual em relação ao real = (L/2D)²). Corrigir prev-w5 para 25 % e 6 %. |
| C3 | Degrau 5 "De longe, a barra vira um ponto" e Síntese, 3º item | simplificação que vai causar erro | **atrapalha** | "Isso vale para qualquer objeto carregado: visto de longe, ele parece um ponto." / "trate o objeto como carga pontual com a carga total. Erro ≈ (tamanho/2D)²". (i) Falha com carga total nula: um dipolo cai com 1/D³ (o guia cita isso em "resto do capítulo"); P26 e P27 têm Q_total = 0 e campo não nulo no centro, e a "pontual" daria 0. (ii) (L/2D)² é da barra no eixo com D medido do **centro**; para o disco no eixo calculei erro = 0,75(R/z)² (3,2 % em z/R = 4,8; a regra com tamanho = 2R daria 4,3 %). Se D for medido de uma ponta, o erro é linear em L/D. | "Qualquer objeto com carga total ≠ 0, com D medido do centro da carga." Na Síntese: "erro da ordem de (tamanho/D)², o fator depende da forma". |
| C4 | Degrau 6, Erros comuns ("σ/(2ε₀) para disco ou placa isolante com carga **numa face**"), `rev-3` d), tabela de equações | simplificação que vai causar erro (Caps. 23 e 25) | **atrapalha** | Numa folha fina isolante só conta a densidade **total** (soma das duas faces). Com 5,3 µC/m² em cada face, E_m = 2·5,3e-6/(2ε₀) = 5,99e5 N/C = σ/ε₀ (calculei). Escrito "carga numa face", o aluno guarda "σ/ε₀ = carga dos dois lados" ou "uma face só dá metade". Em condutor, σ/ε₀ vem do σ da face onde se mede, o que o guia não diz. Além disso, E_m é o limite z → 0⁺: ao atravessar o disco o campo salta de −σ/(2ε₀) para +σ/(2ε₀) (a Eq. 22-26 vale só para z > 0) e isso nunca é dito. Esse salto é a ponte para Gauss e condutores. | Definir σ como densidade total da folha fina, dizer "E_m = lim z→0⁺" e que o campo inverte ao atravessar o plano (salto σ/ε₀). |
| C5 | `data-erros` de `lac-a-3`, `lac-r-1`, `lac-b-2`, `lac-mil-1` | erro numérico (feedback aponta para o número errado) | polimento | **lac-a-3**: 0,66 com a mensagem "Calculadora em graus?". Calculadora em graus dá 44,95·sen 1° = **0,784**; 0,66 é a resposta certa (37,82) vezes sen 1°. **lac-r-1**: 8,99e8 com "r = 1 em vez de 0,010 m?". Isso daria 8,99 N/C; 8,99e8 corresponde a r = 10⁻⁴ m (converteu duas vezes). **lac-b-2**: 15,17 com "usou 4,0 m como a". Isso daria 8,67; 15,17 = kq/a² com a = 4 (carga toda em x = 0). **lac-mil-1**: 1,572e-11 é a massa **em gramas** (cgs completo); a mensagem diz "densidade em g/cm³ **ou** raio em cm". | Trocar por 0,784; 8,99; 8,67 (ou trocar as mensagens). Em lac-mil-1: "resultado em gramas? 1 g = 10⁻³ kg". |
| C6 | Fig. 22-42 (P15) e Dica 1 | figura confusa | polimento | O PDF (p. 122) só tem o triângulo 3-1-2, com P no **ponto médio da hipotenusa** e o ângulo reto em P entre 1–2 e 3–P. "P é o centro do quadrado de lado a" e a Dica 1 ("q₁ e q₂ estão numa mesma reta que passa por P (a diagonal)") falam de um quadrado que não está desenhado. As coordenadas do SVG estão certas (3 na origem, 1 em (0, a), 2 em (a, 0), P = (a/2, a/2)). | Pontilhar o 4º vértice (a, a) ou dizer "P é o ponto médio de 1–2". |
| C7 | Notação de ângulo em todo o guia | termo não definido (símbolo sobrecarregado) | **atrapalha** (leve) | θ = ângulo do pedacinho a partir do eixo de simetria (Degrau 4); θ = orientação do campo a partir de +x (Degrau 3, campos P9-b, P15-b, P26-b); α no P26-3; "ângulo com a vertical" em lac-p-2. No P26 o aluno traz o θ do Degrau 4 e não sabe de onde medir. O Degrau 3 ainda diz "Nada de procurar o ângulo certo para o cosseno" e o Degrau 4 integra cos θ. | α (ou β) para o pedacinho, em todo o guia; θ só para a resposta. |
| C8 | Degrau 3, "E_x = E·Δx/r, E_y = E·Δy/r" | termo não definido | polimento | Δx e Δy não são definidos (módulo? P − carga?). A regra "sinais tirados do desenho" obriga o aluno a inverter à mão para −q (P9). A forma vetorial com q com sinal, E⃗ = (kq/r²) r̂ (r̂ da carga para P), nunca aparece. Ela evita a regra extra e reaparece nos Caps. 23 e 24. | Definir Δ = P − posição da carga; mostrar a forma vetorial uma vez. |
| C9 | Degrau 2 (`prev-w2`, lacuna `lac-r`, regra "\|q\| ∝ r²") e linhas "Usa:" | dica entrega demais | **atrapalha** | O truque do P8 aparece três vezes antes da questão. prev-w2: +1 nC a 1 cm e +4 nC a 2 cm dá zero. lac-r: +1 nC a 1 cm e −4 nC a 2 cm dão 8,99e4 e 8,99e4, total zero. O texto diz "uma carga 4 vezes maior a uma distância 2 vezes maior faz o mesmo campo". O P8 é 3e a d e 12e a 2d (também 1:4 em d:2d). As linhas "Usa:" ainda nomeiam o método: P8 "cancelamento de campos alinhados", P15 "cancelamento de um par", P26 "simetria com sinais opostos". | Trocar os números da lacuna para um caso que **não** cancele (ex.: −3 nC a 2 cm); tirar "cancelamento" das linhas "Usa:". |
| C10 | Questões (Degrau 3 e Síntese) | falta prática | **atrapalha** | As respostas de campo vetorial são 0 (P8), 180° (P9), 45° (P15), −90° (P26) e 180° (P31). Nenhuma exige somar dois vetores de módulos diferentes com ângulo fora dos eixos. O "ângulo pelo quadrante", tema central do Degrau 3, só é exercitado em múltipla escolha (pre4, ck3-2, rev-4). | Uma lacuna extra: P15 com q₁ = +2e dá **179 N/C a 18,4°** (calculei). |
| C11 | Degraus 4 e 6 (carga horária) | denso demais | **atrapalha** | Degrau 4 (20 min): analogia, λ, método em 6 passos, dedução, caso ±, ficha, widget, exemplo, lacuna de 3 campos, 4 erros e checkpoint com 2 figuras. A captura `desktop-d4.png` tem cerca de 7500 px de altura. Degrau 6 (15 min): dedução do anel, do disco, 3 limites, binômio, normalização E/E_m, widget e 3 gráficos. | Mover "metades opostas" para junto do P26 (ou tirar do degrau); marcar a dedução do disco e o binômio como "leia depois". |
| C12 | Degrau 6, analogia dos anéis de tronco (`guia-v1.html`, linha 1509) | outro (analogia) | polimento | "Um disco carregado é isso: uma **pilha** de anéis concêntricos." "Pilha" sugere empilhar em z (um cilindro). Os anéis do disco são coplanares e encaixados; no tronco, cada anel é uma casca 3D. | "Anéis encaixados, todos no mesmo plano." |
| C13 | Degrau 2, ventiladores e aspiradores | outro (analogia) | **atrapalha** (leve) | O barquinho tem de ser a carga de prova **positiva**. Se o aluno imaginar um elétron, o ventilador o puxa, o que contradiz "positiva empurra" e o Degrau 1. A caixa "Onde a analogia quebra" cita cone de vento e 1/r², mas não isso. | Acrescentar: "o barco é a carga de prova positiva; um elétron seria um barco que o ventilador puxa". |
| C14 | Degrau 5, fila de ventiladores: "Campos elétricos não se bloqueiam" | simplificação que vai causar erro (Cap. 23) | **atrapalha** (leve) | Vale para cargas fixas (superposição). No Cap. 23 o aluno vê blindagem (gaiola de Faraday, cavidade em condutor) e lê "o campo é bloqueado". | Uma frase: "a blindagem do Cap. 23 vem de cargas que se movem no condutor e criam campo contrário; aqui as cargas estão fixas". |
| C15 | Degrau 4, mesa redonda | outro (analogia) | polimento | "Se a mesa está cheia, o disco não sai do lugar" vale só no centro exato. Num anel, fora do centro (no plano), E ≠ 0; o aluno vai trazer "dentro do anel é zero" para Gauss (isso só vale em casca esférica ou cilíndrica). A caixa também não cobre as metades de sinais opostos: quem só usa a mesa prevê cancelamento, mas um grupo empurra e o outro puxa e os efeitos **somam** (P26). | "Só no centro" e uma linha sobre sinais opostos. |
| C16 | Degrau 6, formiga no campo de futebol | outro (analogia) | polimento | "Andar um passo para cima não muda nada": E cai 10 % em z = 0,1R (0,9005 E_m, calculei), e o widget mostra "placa infinita (erra 11 %)" onde `prev-w6` diz "quase igual". A analogia também não dá a razão (a área vista cresce como r² e compensa o 1/r²), que é a ideia do Gauss. | "Muda pouco (≤ 10 % até z = 0,1R)" e uma linha com a razão. |
| C17 | Degrau 1, caixa "Onde a analogia quebra" (feira) | outro (analogia) | polimento | A lista é honesta, mas: (a) preços não se somam, e a superposição, o próximo passo, não tem espelho na feira (só no D2, com outra analogia); (b) o item (3) ("um comprador enorme muda o preço") vale para fontes móveis ou condutores. Com cargas fixas qualquer q vale em F = qE; o aluno pode concluir que F = qE falha para q grande. | "q₀ pequena serve para não deslocar as fontes; com fontes fixas, qualquer q vale." |
| C18 | P81-4 (b) | polimento | polimento | "as duas metades se repeliriam com cerca de k(q/2)²/R² ≈ 10⁹ N": a conta dá 1,39e9 N (39 % acima). A exata (casca) é 6,96e8 ≈ 7e8, que o texto cita logo depois. A esfera de enxofre é isolante e maciça; a conta supõe carga na superfície. | Dar só a exata, ou "ordem de 10⁹ N" e "se a carga ficar na superfície". |
| C19 | Verificador, P81-a | verificador | polimento | −0,03 e −3×10⁻² são **recusados** (2,3 % do alvo, tolerância 2 %) com feedback genérico; "−29 mC" não é lido. Dados com 2 algarismos e "da ordem de 150 N/C". | Tolerância 5 % neste campo, ou dica "dê 2 algarismos". |
| C20 | Verificador, P8-a e campos com unidade | verificador | polimento | Quem escreve "zero" ou "nulo" recebe "Não consegui ler". `data-abs=3` aceita 2 e 1e-5 (ok). Em P38-a ("cm") e lac-d-3 ("m"), "0,069 m" e "34,6 cm" não são lidos (o texto de erro orienta, e "34,6" sem unidade cai na mensagem de potência de 10). | Aceitar "zero"; aceitar sufixos m, cm, mm. |
| C21 | Figuras de questão: papel quadriculado | figura confusa | polimento | Em P8 (captura `desktop-p8.png`) o fundo quadriculado parece uma malha de coordenadas; "d" fica na diagonal (√2 quadradinhos) e o rótulo "d" é cortado pelo tracejado perto de q₂. O P38 já está sem grade (certo). Fig. 22-54: a/L desenhado 0,63; real 1,47 (12,0/8,15). O livro também não está em escala, mas o guia diz "reconstruída" sem avisar "fora de escala". | Tirar a grade das figuras de questão; "fora de escala" na 22-54. |
| C22 | Degrau 3, exemplo, "Verificar" | outro | polimento | "o resultado, que tem o fator 4/5 → 0": 4/5 é um número; o que tende a 0 é y/r. | "o fator y/r → 0". |
| C23 | Degrau 1, exemplo do hidrogênio, "Verificar" | outro | polimento | "A força bate com a lei de Coulomb (ke²/r², o mesmo número)": é circular (F = eE **é** ke²/r²). Os números (5,15e11 N/C, 8,24e-8 N, 1,7e5 vezes a ruptura) estão certos. | Verificar contra o peso do elétron (F/mg ≈ 10⁴⁰) ou contra a ruptura do ar. |
| C24 | Síntese, tabela ("Fig. 22-14 do livro") | outro | polimento | No PDF, a 22-14**a** é o caso do Degrau 5 (P no prolongamento); "fora da reta" são 22-14**b** e **c**. | Citar 22-14b/c. |
| C25 | Termos: "semicírculo" | termo não definido | polimento | A barra é uma semicircunferência (o enunciado do P29 diz assim); "semicírculo" é a área. O guia usa "semicírculo" no Degrau 4, no checkpoint e nas dicas. | "Semicircunferência" onde é a barra. |
| C26 | Dicas: `P15-3`, `P31-2`, `P38-3` | dica entrega demais | polimento | A dica 3 do P15 dá r², E₁, E₂ e E₃ (a solução quase pronta, e a Dica 1 já diz "o que acontece com os campos delas?"). A dica 2 do P31 dá o plano de (a) a (e), inclusive a armadilha de (d) ("a ponta perto fica a D − L/2"). A dica 3 do P38 diz "cruza 0,5E_m numa linha vertical da grade". Não achei dica **fraca**; achei dicas fortes demais cedo. | Esconder o ponto-chave até o nível 4. |
| C27 | P38, texto da dica 2 ("quatro divisões") | polimento | polimento | O número de divisões só está no `aria-label` do SVG e na dica; a figura (como a do livro) não o escreve. A leitura "z_s = 4 divisões" é inferida dos riscos. Confirmei no PDF que são 4 (riscos em ¼, ½, ¾ e z_s). | Marcar os riscos do eixo de forma visível (já há riscos curtos). |

Não encontrei: erro físico de resposta, sinal trocado, unidade errada, resposta final errada, tolerância que rejeite resposta certa de questão (fora C19).

---

## 2. Tabela de conferência numérica

Meu script (`aluno-3-contas.py`) soma campos de cargas pontuais por força bruta, integra por Simpson e fatia arcos em 8000 cargas. Constantes do livro: k = 8,99e9; ε₀ = 8,85e-12; e = 1,602e-19; g = 9,8. "dif" é a diferença relativa (ou absoluta, ou em graus).

| item | valor do guia | meu valor | dif | ok? |
|---|---|---|---|---|
| pre1: 4,23 fC | 4,23e-15 C | 4,23e-15 | 0 | ok |
| pre2: força a 3 cm | 3,2 N | 3,2 | 0 | ok |
| pre3: componentes de 10 a 135° | −7,07; +7,07 | −7,071; +7,071 | 0,02 % | ok |
| pre4: ângulo de (−3, −4) | 233° | 233,13° | 0 | ok |
| pre5: ∫dx/x² = L/(a(a+L)) | 2/3 (a=1, L=2) | 0,6667 | 0 | ok |
| P81a: q | −0,02933 C | −0,02933 | +0,01 % | ok |
| P81: nº de elétrons | 1,8e17 | 1,831e17 | +1,7 % (arredondamento) | ok |
| P81: massa; raio da esfera | 0,449 kg; 3,7 cm | 0,449; 3,727 | 0; +0,7 % | ok |
| P81: E na superfície; ÷ ruptura | 1,9e11; 63 mil | 1,898e11; 63 270 | −0,09 %; +0,4 % | ok |
| P81: força entre metades "≈ 10⁹ N" | 1e9 | 1,392e9 | **+39 %** | só como ordem de grandeza (C18) |
| P81: força exata (casca) kq²/(8R²) | 7e8 N | 6,96e8 | −0,6 % | ok |
| P81 e se: q com E = 3e6; E_sup | 1,5 µC; 9,5e6 | 1,467 µC; 9,491e6 | −2,2 %; −0,09 % | ok |
| P81 e se: q_máx sem faísca; F a 150 N/C; massa | 4,6e-7 C; 7e-5 N; 7 mg | 4,636e-7; 6,954e-5; 7,10 mg | +0,8 %; −0,7 %; +1,4 % | ok |
| H: E; F; E/ruptura | 5,15e11; 8,24e-8; 1,7e5 | 5,146e11; 8,245e-8; 1,715e5 | −0,07 %; +0,06 %; +0,9 % | ok |
| ficha: 1 nC a 3 cm; elétrons em 4,23 fC | 1,0e4; 26 mil | 9989; 26 400 | −0,1 %; +1,6 % | ok |
| Millikan: m; mg; \|q\|; \|q\|/e | 1,572e-14; 1,541e-13; 8,026e-19; 5,0 | idem; 5,01 | ≤ 0,2 % | ok |
| ck1-3: E; F com −4 nC | 3,0e3 N/C; 1,2e-5 N | 3,0e3; 1,2e-5 | 0 | ok |
| W1: constante 9989·\|q\|/r² | 9989 | 9989 | 0 | ok |
| D2 exemplo: E_A; E_B; total; "se B fosse +" | 4,50e4; 3,00e4; 7,5e4; 1,5e4 | 4,495e4; 2,997e4; 7,492e4; 1,498e4 | −0,11 % | ok |
| lac-r-1, -3, -5 | 8,99e4; 8,99e4; 0 | 8,99e4; 8,99e4; 0 | 0 | ok |
| ck2-3: \|E\| dos 4 sistemas (ke/d²) | 2,5; 2,0; 0,5; 0 (ordem 2,4,3,1) | idem | 0 | ok |
| prev-w2: +1 nC a 1 cm e +4 nC a 2 cm | 0 | 0 | 0 | ok |
| rev-6: 2E | 1,798e5 | 1,798e5 | 0 | ok |
| D3 exemplo: E₁; \|E\|; ângulo | 7,19e3; 1,15e4; 90° | 7192; 1,151e4; 90° | +0,03 %; +0,06 % | ok |
| P9a \|E\| | 1,381e-10 | 1,381e-10 | −0,01 % | ok |
| P9b ângulo | 180° | 180° | 0 | ok |
| P9: E de uma carga; com +q,+q; com y = 40 m | 1,151e-10; 1,841e-10; 2,7e-13 | 1,151e-10; 1,841e-10; 2,674e-13 | −0,02 %; +0,01 %; −0,95 % | ok |
| P69: lac-p-1, (a), (b), 30° | 26,97; 46,71; 26,97; 30° | idem | ≤ 0,01 % | ok |
| P15a; P15b | 160 N/C; 45° | 160,0; 45° | +0,01 % | ok |
| P15: E de q₁; e se q₁ = +2e; e se q₃ = −2e | 80; 179; −135° | 80,01; 178,9; −135° | +0,01 %; −0,05 % | ok |
| P8: \|E\|; E₁; E₃; E₄ | 0; 288; 172,8; 172,8 | 0; 288,0; 172,8; 172,8 | ≤ 0,01 % | ok |
| P8 e se: q₄ na diagonal oposta | 346 N/C | 345,6 | +0,01 % | ok |
| ck3-2; rev-4; ck3-3 | 135°; −45°; 0,707 | idem | 0 | ok |
| D4: arco 120°; semicírculo; anel | 0,827; 0,64; 0 | 0,827 (=3√3/2π); 0,6366; 0 | 0; −0,5 % | ok |
| P29 razão; e se quarto de círculo | π/2; 1,11 | 1,5708; 1,111 | 0; +0,06 % | ok |
| P71: φ; λ; E | 2 rad; 5e-9; 37,82 | idem | 0; 0; +0,01 % | ok (gabarito 38) |
| P26a; P26b | 20,6 N/C; −90° | 20,60 (8000 cargas); −90° | +0,02 % | ok |
| P26 e se: +2q no semicírculo | 20,6 | 20,60 | +0,02 % | ok |
| P27 citado no P26-4 | 23,8 | 23,76 | −0,15 % | ok (gabarito 23,8) |
| ck4-3: arranjos (E = 1 para a) | e = 2; b = 1,414; a = c = 1; d = 0 | idem | 0 | ok |
| D5 exemplo: E; pelo centro; erro do centro | 5,99e3; 4,50e3; 25 % | 5993; 4495; 25,0 % | +0,06 %; −0,11 % | ok |
| D5: ponta perto; ponta longe; dist. equivalente | 1,80e4; 2,00e3; 8,7 cm | 1,798e4; 1998; 8,66 cm | −0,11 % | ok |
| P67 | 60,68 N/C | 60,68 | 0 | ok (gabarito 61) |
| P31a λ | −5,19e-14 C/m | −5,19e-14 | 0 | ok |
| P31b; ponta perto; ponta longe; pelo centro | 1,573e-3; 2,641e-3; 9,366e-4; 1,472e-3 | idem | ≤ 0,03 % | ok |
| P31: erro do centro "uns 7 %" | 7 % | 6,4 % (rel. ao real); 6,9 % (rel. ao pontual) | **−8 %** | aceitável, mas é o C2 de novo |
| P31d; P31e | 1,521e-8; 1,521e-8 | 1,521e-8; 1,521e-8 | +0,01 % | ok |
| P31: diferença d/e; "a = 0,5 cm → 4,8×" | 7e-7; 4,8 | 6,6e-7; 4,84 | −5 %; +0,8 % | ok |
| rev-1: real; pelo centro | 0,50; 0,44 | 0,500; 0,444 | 0; +1 % | ok |
| **prev-w5: erro em D = L; D = 2L** | **33 %; 7 %** | **25 % ou 33 % (conforme a referência); 6,25 % ou 6,67 %** | inconsistente | **C2** |
| ck5-3: D = 10L | 0,25 % | 0,25 % | 0 | ok |
| P34 exemplo: σ/2ε₀; parêntese; E; Q; kQ/z²; "3 % acima" | 2,99e5; 0,0210; 6,29e3; 1,04e-8; 6,50e3; 3 % | 2,994e5; 0,02102; 6,294e3 (também por 4000 anéis); 1,041e-8; 6,497e3; 3,22 % | ≤ 0,15 % | ok |
| P35: z/R; z | 0,577; 0,346 m | 0,5774; 0,3464 | 0,1 % | ok |
| P38: R (z = 4,0 cm) | 6,928 cm | 6,928 | 0 | ok |
| P38: E/E_m em 8 cm; em 2 cm; em 6 cm | 0,24; (0,7226 no SVG); (0,345 no SVG) | 0,2441; 0,7226; 0,3453 | +1,7 %; 0; +0,1 % | ok |
| P38 e se: 0,25E_m em 4 cm | R = 3,5 cm | 3,53 | +0,8 % | ok |
| prev-w6: disco em z = 0,1R; erro "placa infinita" | 0,90; 11 % | 0,9005; 11,05 % | 0,06 % | ok |
| rev-3: σ/2ε₀; σ/ε₀ | 3,0e5; 6,0e5 | 2,994e5; 5,989e5 | −0,19 % | ok |
| ck6-1: ordem a > b > c | a, b, c | vale em 10 valores de z (0,01R a 50R) | n/a | ok |
| W4: φ = 60°; 270° | (leituras do widget) | 0,955; 0,300 | n/a | ok |
| plano de revisão: P5; P41; P63 | 56 pC; 1,5e3 N/C e 2,4e-16 N; 8,87e-15 N e 120 | 55,6 pC; 1500 e 2,403e-16; 8,867e-15 e 119,8 | ≤ 0,7 % | ok |

**Figuras do guia contra o PDF** (coordenadas medidas no SVG):

| figura | PDF | guia | veredito |
|---|---|---|---|
| 22-36 (P8, p. 120) | q₁ acima-esq., q₂ abaixo-dir. a d; q₃ acima-dir. a d; q₄ mais d além de q₃; ângulo reto em P | q₁ e q₂ a 77,1 px de P; q₃ a 77,1; q₄ a 154,2 (= 2d); marcador de ângulo reto entre q₃ e q₂ | **confere** |
| 22-37 (P9, p. 120) | −q em −x, +q em +x, P em y | 90 px para cada lado, P a 120 px (3:4) | **confere** (até em escala) |
| 22-42 (P15, p. 122) | 3 na origem, 1 em (0, a), 2 em (a, 0), P no meio de 1–2, ângulo reto em P | P = (155, 125) = ponto médio de (80, 50) e (230, 200) | **confere**; só o "quadrado" não está desenhado (C6) |
| 22-50 (P26, p. 125) | semicircunferência à esquerda de P; +q em cima, −q embaixo | arco de (170, 30) a (80, 120) é +q; de (80, 120) a (170, 210) é −q; raio 90 | **confere** |
| 22-52 (P29, p. 126) | (a) semicircunferência à esquerda de P; (b) +Q a R à esquerda | arco e carga à esquerda; R = 70 px nos dois | **confere** |
| 22-54 (P31, p. 127) | barra à esquerda, P à direita a uma distância a da ponta | posições certas; a/L = 0,63 (real 1,47) | confere em posição, **fora de escala** (C21) |
| 22-58 (P38, p. 129) | curva cruza 0,5E_m na 2ª linha vertical; termina perto de ¼ de E_m | curva passa em (190, 115) = 2ª linha × 0,5E_m (exato); em z = 2, 6 e 8 cm: 0,7227, 0,3453, 0,244 | **confere**; z = 4,0 cm → R = 6,93 cm; z_s = 8,0 cm → E/E_m = 0,244 (leio 0,24 no PDF) |
| Teste 1 (p. 82), Teste 2 (p. 99), Perguntas 3, 4, 9 e 11 (p. 115 a 117) | S, e, R, p; três barras; −q, −q em ±d; 4 sistemas com d entre vizinhos; discos e anel; arcos | descrições do guia | **conferem**; gabaritos T1 (a)(b)(c)(d), T2, P3, P9 e P11 batem com o do livro. A ordem da Pergunta 4 (par, sem gabarito) calculei: 2, 4, 3, 1 |

---

## 3. Verificador numérico: o que aceita e o que recusa

Rodei `lerNumero` e `bate` do próprio HTML em Node com cerca de 130 entradas.

| campo | aceita | recusa | observação |
|---|---|---|---|
| P8-a (resp 0, abs 3) | `0`, `0 N/C`, `0,0`, `1e-5`, `2` | `4` | `zero` dá erro de leitura (C20) |
| P9-a (1,381e-10, tol 2 %) | `1,38e-10`, `1,38×10^-10`, `1,38 × 10⁻¹⁰`, `1.38x10^-10`, `1,4e-10`, `1,36e-10`, com `N/C` | `1,35e-10`, `1,42e-10` | formatos variados ok |
| P9-b (ang 180, ±1,5°) | `180`, `-180`, `180°`, `179`, `540` | `178`, `181,6`, `π` | todo ângulo equivalente passa |
| P15-a / P15-b | `160`, `1,6e2`, `163`; `45`, `45°`, `405` | `164`; `46,6`, `225`, `π/4` | `225` tem mensagem própria (sentido invertido) |
| P26-b (−90) | `-90`, `270`, `−90°` (menos unicode), `-89` | `90` | mensagem própria para 90 |
| P29-a (π/2) | `π/2`, `pi/2`, `0,5π`, `1,57`, `1,6`, `1.5708` | `1,5` (4,5 % abaixo) | `1,6` passa (1,9 %) |
| P31-a (sinal) | `-5,19e-14`, `−5,19×10⁻¹⁴ C/m`, `-5,2e-14` | `5,19e-14` (mensagem "E o sinal?"), `-5e-14` | `-5e-14` recusado (3,7 %) |
| P31-b, -d, -e | `1,57e-3`, `0,00157`, `1,6e-3`; `1,52e-8`, `1,5e-8` | n/a | ok |
| P31-c | `180`, `-180` | `π` | ok |
| P38-a (6,928, tol 2 %) | `6,9`, `6,93`, `7`, `4√3`, `4*sqrt(3)`, `6,93 cm`, `6,8` | `6,5`, `7,1`, `0,069` | `7` passa (1,0 %) |
| P81-a (sinal) | `-0,029`, `-0,0293`, `-2,9e-2`, `-4,4/150` | `0,029` (diz "E o sinal?"), **`-0,03`**, **`-3e-2`** | C19; `-29 mC` ilegível |
| lac-mil-1 a 4 | `1,57e-14`, `1,572×10⁻¹⁴ kg`, `8e-19`, `5`, `5,0`, `4,9` | `-5` (mensagem "módulo"), `5,2` | ok |
| lac-r-5 (abs 900) | `0`, `-0`, `500` | `1000` | `500` é absurdo, mas inofensivo |
| lac-p-3 | `47`, `46,7`, `46`, `27√3` | `48` | ok |
| lac-a-3 | `38`, `37,8` | `37`, `39` | ok (37 está a 2,2 %) |
| lac-b-2 | `61`, `60,7`, `60` | `62` | ok |
| lac-d-2 | `0,577`, `1/√3`, `√3/3`, `0,58` | `0,6` | ok |
| lac-d-3 (unid "m") | `0,346`, `0,35`, `0,6/√3`, `0,6/1,73` | `34,6` (mensagem de potência de 10) | `34,6 cm` dá erro de leitura |

Sem sobreposição entre a janela do certo e as janelas dos erros previstos em nenhum campo de questão.

---

## 4. Analogias: onde quebram e se a caixa é honesta

| analogia | caixa "Onde a analogia quebra" | o que falta (mais grave primeiro) |
|---|---|---|
| **Feira / preço por quilo** (D1) | Honesta nos 3 pontos (vetor, quilo negativo, comprador grande). | (a) Preços não somam: o próximo passo é superposição e a analogia é muda sobre ela. (b) O ponto (3) vale para fontes móveis ou condutores; com cargas fixas q grande não muda o campo (C17). |
| **Ventiladores e aspiradores** (D2) | Honesta (cone, mistura de ventos, 1/r²). | O barquinho é uma carga de prova positiva; com elétron a analogia contradiz o D1 (C13). Falta dizer que o vento precisa de um meio e o campo não. |
| **Mesa redonda** (D4) | Honesta (força constante vs 1/r², cargas negativas puxam). | "Mesa cheia → zero" só no centro exato (C15). Não cobre sinais opostos nas metades (P26), onde os efeitos somam. |
| **Fila de ventiladores** (D5) | Boa: "os da frente bloqueiam os de trás; campos não". | O "não se bloqueiam" vai colidir com blindagem no Cap. 23 (C14). |
| **Anéis de tronco** (D6) | Boa (espessuras, z ≪ R). | "Pilha" (C12). |
| **Formiga no campo de futebol** (D6) | Menciona z ≪ R e bordas. | "Não muda nada" é forte: cai 10 % em 0,1R. Falta a razão (área ∝ r²). Não dá o que acontece em z = 0 (salto de sinal) (C16, C4). |

Eu daria a nota "honesta, mas incompleta". As caixas citam as falhas óbvias; as que doem depois (blindagem, anel, positivo/negativo) não aparecem.

---

## 5. Perguntas ao Professor

1. **(P8, estabilidade)** Professor, deu E = 0 em P. Se eu largar ali uma carga de prova positiva, ela fica em equilíbrio estável? Calculei a derivada do campo em P em 3D (q₁, q₂, q₃, q₄ no plano). Ao longo de q₃–q₄ é **+7** ke/d³ (instável); ao longo de q₁–q₂, **−18,5** (restauradora); fora do plano, **+11,5** (instável). A soma é exatamente 0. É uma sela, e é por isso que a soma dá zero? Isso é o teorema de Earnshaw? Vamos ver no Cap. 23 por quê?
2. **(P9, ponto fora da mediatriz)** E se P estiver na origem (y → 0)? Calculei 2kq/9 = 6,39e-10 N/C para −x, 4,6 vezes o de y = 4 m, e o "6/5" vira 2. A regra "sinais opostos → campo paralelo à reta das cargas" continua valendo dentro do segmento? E se P estiver no eixo x, em x = +6 m (fora do segmento, mais perto de +q)?
3. **(P31, para que serve o (e))** A 50 m o campo da barra e o da partícula diferem em 7e-7. Com 3 algarismos eles são iguais. A partir de que D a diferença aparece no 3º algarismo? Calculei D = 22,4 L = 1,8 m. Então, por que o livro pede 50 m (600 L)? Se eu pedisse 1,8 m, os dois números ficariam diferentes?
4. **(W5, definição de erro)** Em D = L o erro de trocar a barra por um ponto é 25 % (referência o valor real) ou 33 % (referência o pontual)? O `prev-w5` diz 33 % e o widget diz 25 %. Qual é a "certa" para a regra do 1 %, e por que (L/2D)² serve para a barra mas não para o disco (calculei 0,75(R/z)²)?
5. **(Degrau 6, Cap. 23)** Se o disco tiver σ em **cada** face, o campo logo acima do centro vira σ/ε₀ (5,99e5 N/C para 5,3 µC/m², calculei)? Então o σ do guia é a densidade total da folha? E um disco **condutor** com a mesma carga total, com σ_face(r) = Q/(4πR√(R²−r²)): o campo logo acima do centro é metade do isolante (calculei razão 0,500)? Por que o guia diz "isolante com carga numa face"?
6. **(Degrau 4, metades opostas)** Se eu aplico "a mesma integral com seno" de −φ/2 a +φ/2, dá zero. Quais limites usar? E por que o resultado do P26 (φ = π) coincide com 2kλ/r do semicírculo uniforme, mas não coincide para outro φ?
7. **(Analogia/Cap. 23)** Na fila de ventiladores, "campos não se bloqueiam". Se eu colocar uma chapa de cobre entre a barra e P, o campo em P muda? Se muda, a superposição falhou? Ou o cobre é uma carga nova?
8. **(Cap. 24)** A "distância equivalente" do campo da barra é √(a(a+L)) = 8,66 cm no exemplo. Existe uma distância equivalente para o potencial? Calculei L/ln((a+L)/a) = 9,10 cm, que é diferente. A "distância equivalente" depende da grandeza?
9. **(P29 e P26, arco como ponto)** Qual a distância equivalente do semicírculo do P29? Calculei r√(π/2) = 1,253 r (a carga toda num ponto do eixo a essa distância daria o mesmo campo). Em geral, r√((φ/2)/sen(φ/2)). E trocar cada quarto do P26 por uma carga pontual no meio do quarto dá 22,88 N/C, 11 % acima: é de propósito que o erro é o mesmo 1,11 do "e se quarto de círculo" do P29?
10. **(P15, "e se" com ângulo)** Com q₁ = +2e o campo vira 179 N/C. A que ângulo? Calculei **18,4°**. Por que o texto da ajuda diz só "outra direção"? É um caso ótimo para praticar o quadrante.
11. **(P81, algarismos)** No P81 meu −0,03 C foi recusado e −0,029 passou. Com "da ordem de 150 N/C", quantos algarismos o senhor espera do aluno?

---

## 6. O que funcionou (não remover na v2)

- **Respostas, exemplos, lacunas e "e se..." todos certos.** 133 conferências, nenhuma divergência além de arredondamento. P8 = 0, P9 = 1,38e-10 a 180°, P15 = 160 a 45°, P26 = 20,6 a −90°, P29 = π/2, P31 = −5,19e-14, 1,57e-3, 180°, 1,52e-8, P38 = 6,93 cm, P81 = −0,029 C.
- **P38.** Curva conferida em 4 pontos da grade (a curva do SVG passa exatamente em 0,5E_m na 2ª linha vertical, 0,7227 em z = 2 cm, 0,3453 em 6 cm e 0,244 em 8 cm), o que bate com o PDF. A escolha de "z em que E = 0,5E_m" é a certa, porque é o único cruzamento exato da grade. O "E se... 0,25E_m em 4 cm → 3,5 cm" está certo.
- **Regra "lado + sinal" (D2), "|q| ∝ r²" e o triângulo 3-4-5 (D3).** Testei P8, P9, P15, P69, o exemplo do D2 e os 4 sistemas da Pergunta 4 por soma vetorial bruta: a regra sempre acerta.
- **O fator sen(φ/2)/(φ/2) e o "desconto dos empurrões laterais".** Bate com o W4 (0,827; 0,637; 0,955; 0,300) e vira o P29 em duas linhas.
- **A "distância equivalente" √(a(a+L)) e o "Verificar" com limites** (entre ponta perto e ponta longe): 8,66 cm entre 5 e 15 cm.
- **Ordens de grandeza do P81 (b).** 63 mil vezes a ruptura, 7e8 N ≈ 70 mil toneladas, 7 mg: tudo conferido, e a ideia de "carga máxima sem faísca" é muito boa.
- **As mensagens específicas de erro** dos campos de questão (P8, P9, P15, P26, P29, P31-b, P38, P81-a): refiz cada valor de `data-erros` e todos correspondem ao erro descrito; os 4 deslizes estão nas lacunas (C5).
- **Verificador**: aceita vírgula, `×10^`, sobrescritos, π, √, frações, unidade no fim e ângulo equivalente. Só falhou com palavras, prefixos (mC) e "cm" em campo "m".
- **Previsão antes do widget** e widgets com leituras corretas (W1 9989, W4, W5, W6).
- **Fig. 22-36, 22-37, 22-50, 22-52 e 22-58 reconstruídas fielmente**, com sinais e distâncias do enunciado.
- **Checkpoints e Perguntas 3, 4, 9 e 11 do livro** (o ck2-3 com a conta explícita, o ck4-3 com √2·E e 2E).
- **Plano de revisão com gabarito.** Os problemas citados (5, 41, 7, 11, 27, 23, 25, 37, 87, 63) são ímpares e casam com os degraus.
