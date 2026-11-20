# Plano — Guia do Capítulo 23: Lei de Gauss

**Questões pedidas:** Problemas 5, 24, 29, 39, 52, 53 e 76.
**Fonte:** `halliday-v3/cap-23-lei-de-gauss.md` + `gabarito.md` + PDF original (`../FIsica 3 Eletromagnetismo Halliday.pdf`, págs. 138–195), usado só para ver as figuras e as equações que a conversão perdeu.

| Questão | Dificuldade (livro) | Figura | Gabarito oficial |
|---|---|---|---|
| P5 | · | 23-33 | 3,01 nN·m²/C |
| P24 | · | 23-40 | — (par) |
| P29 | ·· | 23-42 | (a) 0,214 N/C; (b) para dentro; (c) 0,855 N/C; (d) para fora; (e) −3,40 × 10⁻¹² C; (f) −3,40 × 10⁻¹² C |
| P39 | ·· | 23-49 | 5,0 nC/m² |
| P52 | ·· | 23-57 | — (par) |
| P53 | ··· | (sem figura) | (a) 7,78 fC; (b) 0; (c) 5,58 mN/C; (d) 22,3 mN/C |
| P76 | adicional | (sem figura) | — (par) |

---

## 1. Habilidades (matriz questão × habilidade)

| Código | Habilidade |
|---|---|
| H1 | Entender **fluxo** como "quanto campo atravessa": Φ = EA cos θ (campo uniforme, superfície plana), com o vetor área normal à superfície |
| H2 | Dar o **sinal do fluxo** numa superfície fechada: normal para fora; campo saindo = +, entrando = −, rasante = 0 |
| H3 | Aplicar a **lei de Gauss**, ε₀Φ = q_env: só a carga de dentro conta; a forma e o tamanho da superfície não importam |
| H4 | Usar **simetria para repartir o fluxo** entre partes iguais de uma superfície fechada (faces do cubo, metades da esfera) |
| H5 | **Escolher a superfície gaussiana** que acompanha a simetria (esfera, cilindro, "latinha") e que **passa pelo ponto** onde se quer E; saber em que partes há fluxo |
| H6 | Calcular **q_env** em cada caso: λh, σA, ρV (uniforme), soma de cargas, com sinal |
| H7 | **Integrar ρ(r) em cascas**: dq = ρ(r)·4πr² dr (esfera) para densidade não uniforme |
| H8 | **Condutor em equilíbrio**: E = 0 no metal; carga em excesso na superfície; carga induzida na superfície interna = −(carga dentro da cavidade); externa = total − interna |
| H9 | Dar o **sentido** de E (para fora ou para dentro) pelo sinal de q_env |
| H10 | Usar o campo de uma **placa isolante grande**, E = σ/(2ε₀), que não depende da distância |
| H11 | **Equilíbrio com fio inclinado** (Cap. 21): tan θ = F_e/(mg) |
| H12 | **Montar e ler o gráfico E(r)** por regiões (dentro / na casca / fora), com os casos-limite e a continuidade |
| H13 | Resolver em símbolos antes de pôr números; conferir unidade, sinal e casos-limite |

| | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 | H10 | H11 | H12 | H13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **P5** | ● | ● | ● | ● | | | | | | | | | ● |
| **P52** | | | ● | | ● | ● | | | | | | ● | ● |
| **P53** | | | ● | | ● | ● | ● | | | | | ● | ● |
| **P24** | | | ● | | ● | ● | | | ● | | | ● | ● |
| **P76** | | | ● | | ● | ● | | | | | | ● | ● |
| **P29** | | | ● | | ● | ● | | ● | ● | | | | ● |
| **P39** | | | ● | | ● | ● | | | | ● | ● | | ● |

## 2. Pré-requisitos

- **Capítulo 22:** campo de carga pontual, E = k|q|/r² = q/(4πε₀r²); superposição; F = qE (sentido oposto a E se q < 0).
- **Capítulo 21:** equilíbrio de uma bolinha pendurada num fio: T cos θ = mg, T sen θ = F, tan θ = F/(mg).
- **Física 1 / Cálculo 1:** produto escalar (A·B = AB cos θ); áreas e volumes (esfera 4πr² e 4πr³/3; cilindro 2πrh e πr²h); integral de potência (∫r³ dr = r⁴/4); prefixos até femto.
- O Degrau 0 tem um teste rápido de 6 itens (um por pré-requisito), com mini-revisão para quem errar.

## 3. Degraus (do concreto ao abstrato)

| Degrau | Objetivo (1 frase) | Habilidades | Desbloqueia | Tempo |
|---|---|---|---|---|
| **0 — Aquecimento** | Dar um palpite sobre "a carga da Terra a partir de um número medido no chão" e checar a base. | — | — | 10 min |
| **1 — Fluxo** | Calcular quanto campo atravessa uma superfície, com o sinal certo numa superfície fechada. | H1, H2 | (base do P5) | 12 min |
| **2 — Lei de Gauss** | Usar "fluxo total = carga de dentro / ε₀" e repartir o fluxo por simetria. | H3, H4 | **P5** | 15 min |
| **3 — Esferas** | Aplicar a receita de 5 passos à simetria esférica (cascas, esfera e casca grossa uniformes). | H5, H6, H12 | **P52** | 18 min |
| **4 — Cascas de cebola** | Somar a carga em cascas finas quando ρ muda com r. | H7, H12 | **P53** | 15 min |
| **5 — Cilindros** | Usar o cilindro gaussiano para fios, tubos e cilindros maciços. | H5, H6, H9, H12 | **P24, P76** | 15 min |
| **6 — Condutores** | Usar E = 0 no metal para achar as cargas induzidas e o campo em cada região. | H8, H9 | **P29** | 15 min |
| **7 — Placas** | Usar o campo de uma placa grande (σ/2ε₀) com forças e equilíbrio. | H10, H11 | **P39** | 12 min |

Total dos degraus: cerca de 1 h 55 min; com as 7 questões, cerca de 3 h 30 min (em duas ou três sessões).

**Fora das questões (cartões de visão geral, sem aprofundar):** fluxo de campo não uniforme por integração (Exemplo 23.02 e Problemas 9–11); duas placas isolantes por superposição (Exemplo 23.07); duas placas condutoras e o fator 2 (Fig. 23-18); campo junto a um condutor, E = σ/ε₀ (Eq. 23-11), aparece só como contraste no Degrau 7; equivalência Gauss ↔ Coulomb (Eq. 23-10, aparece no Degrau 3).

### Sequência didática de cada degrau (exemplo resolvido → exemplo com lacunas → questão)

| Degrau | Exemplo resolvido | Exemplo com lacunas | Checkpoint |
|---|---|---|---|
| 1 | Problema 1 do livro (quadrado inclinado, fluxo negativo; gabarito −0,015 N·m²/C) | Problema 3 do livro (cubo, face direita; gabarito (a) 0; (b) −3,92; (c) 0; (d) 0) | Teste 1 (b, d) + Pergunta 1(a) |
| 2 | Carga no centro de uma esfera: fluxo pela metade de cima (q/2ε₀), com os números do Problema 7 (gabarito 2,0 × 10⁵ N·m²/C) | Problema 15 do livro (carga no vértice do cubo; gabarito (a) 0; (b) 0,0417) | Teste 3 + Teste 2 (adaptado em tabela) + carga do lado de fora |
| 3 | Esfera maciça uniforme: derivação de E = ρr/(3ε₀) e números do Problema 78 (calculado pelo guia) | Problema 49 (b), (c), (d) do livro (gabarito 56,2; 112; 49,9 mN/C) | casca fina (E = 0 dentro) + Problema 65(b) (0,500) + carga de uma casca grossa |
| 4 | Esfera com ρ = Cr² (calculado pelo guia) | Problema 55 do livro, ao contrário (de E para ρ; gabarito 6Kε₀r³) | dq de uma casca fina + por que ρV falha + "E constante → ρ ∝ 1/r" |
| 5 | Linha infinita (Eq. 23-12) + Exemplo 23.06 (mulher na tempestade: Q ≈ 24 µC) | Problema 31 do livro (duas cascas coaxiais; gabarito 2,3 × 10⁶ N/C para fora; 4,5 × 10⁵ N/C para dentro) | bases sem fluxo + dobrar r + h se cancela |
| 6 | Exemplo 23.05 do livro (−5,0 µC dentro de casca metálica neutra) | Problema 21 do livro (cavidade num condutor; gabarito −3,0 µC e +13 µC) | Pergunta 9 (a), (b) + campo dentro do metal |
| 7 | Placa isolante: derivação de σ/2ε₀ com a "latinha" + elétron solto perto da placa (calculado pelo guia) | Esfera flutuando acima de uma placa horizontal (calculado pelo guia) | Teste 4 + isolante × condutor + distância |

### Widgets (cada um precedido de uma pergunta de previsão; tela e leitura borradas até a previsão)

| Widget | Degrau | O que faz |
|---|---|---|
| W1 | 1 | Gira um quadrado num campo uniforme; mostra o vetor área, θ, cos θ e Φ = EA cos θ (com sinal) |
| W2 | 2 | Superfície fechada (círculo, quadrado ou "batata") e duas cargas; arrasta a carga B para dentro e para fora; conta as linhas de cada carga que saem (+) e entram (−) |
| W3 | 3 | E(r) de uma esfera com cavidade de raio a ajustável (a = 0: esfera maciça; a → R: casca fina); esfera gaussiana de raio r e q_env |
| W4 | 4 | Cascas de cebola: ρ uniforme × ρ ∝ r²; mostra a fração de carga dentro de r e E(r) |
| W5 | 5 (e volta no 7) | Esfera, cilindro e placa gaussianos: área ∝ r², r ou constante → E ∝ 1/r², 1/r ou constante |
| W6 | 6 | Partícula de carga q dentro de casca metálica com carga Q; mostra as cargas das superfícies interna e externa e o campo em cada região |

W6 usa geometria esférica (como o Exemplo 23.05) e não a coaxial do P29, para o aluno transferir a regra em vez de ler a resposta.

## 4. Ordem das questões (da mais fácil à mais difícil)

1. **P5** (Degrau 2): fluxo de uma carga pontual por um quadrado = 1/6 do cubo.
2. **P24** (Degrau 5): tubo fino; dentro, q_env = 0; fora, linha infinita; gráfico com salto.
3. **P52** (Degrau 3): casca grossa uniforme; ρ × volume entre a e r; três regiões.
4. **P76** (Degrau 5): cilindro maciço; πr²h dentro, πR²h fora (resposta em símbolos, conferida com valores-teste).
5. **P29** (Degraus 5 e 6): coaxial com condutores; sinal de q_env dá o sentido; cargas induzidas.
6. **P39** (Degrau 7): placa isolante + pêndulo inclinado.
7. **P53** (Degrau 4): ρ ∝ r; integral em cascas; gráfico r² dentro e 1/r² fora.

## 5. Figuras

**Explicativas (SVG inline):**
- Mapa da subida (degraus → questões).
- D0: a Terra com o campo de "tempo bom" para baixo e uma esfera gaussiana em volta (pergunta-gancho), sem a resposta.
- D1: chuva atravessando uma janela inclinada (analogia); vetor área; três quadradinhos numa superfície fechada (sai +, entra −, rasante 0); figura do Problema 1 (pág. 179 do PDF) e cubo do Problema 3 (Fig. 23-31, pág. 179); cubo do Teste 1 (pág. 143).
- D2: contar linhas: carga dentro (cada linha cruza uma vez) e fora (entra e sai); a esfera cortada ao meio; cubo em volta da carga com 6 faces iguais; 8 cubos em volta do vértice (P15).
- D3: esfera gaussiana passando por P; cascas (dentro E = 0, fora como carga pontual); gráfico E(r) da esfera maciça; casca grossa com a esfera gaussiana entre a e b.
- D4: cebola em cascas, com uma casca de espessura dr destacada (área 4πr², volume 4πr² dr).
- D5: cilindro gaussiano em volta de um fio, com o fluxo só na lateral; vista de cima de cilindro maciço com o gaussiano dentro e fora.
- D6: metal com cavidade e superfície gaussiana dentro do metal; casca esférica com carga fora do centro (Fig. 23-13 reconstruída).
- D7: "latinha" atravessando a placa, fluxo pelas duas bases; pêndulo ao lado de uma placa vertical (diagrama de forças só na Dica 2 do P39); Teste 4 (pág. 173).
- Síntese: fluxograma "que superfície gaussiana eu uso?".

**Das questões (reconstruídas do PDF):**
| Figura | Dados | Origem |
|---|---|---|
| 23-33 (P5) | quadrado de aresta d, próton no eixo que passa pelo centro, a d/2 acima | PDF pág. 180 |
| 23-40 (P24) | tubo metálico de parede fina, raio R, carga + na superfície, eixo indicado | PDF pág. 184 |
| 23-42 (P29) | barra condutora de raio R₁ (carga Q₁) dentro de casca coaxial de raio R₂ (carga Q₂), em perspectiva com corte | PDF pág. 185 |
| 23-49 (P39) | placa vertical com cargas +, fio preso na placa fazendo θ com ela, esfera (m, q) afastada para a direita | PDF pág. 188 |
| 23-57 (P52) | casca esférica: cavidade de raio a, material com cargas + entre a e b | PDF pág. 191 |
| P53, P76 | o livro não tem figura; o guia desenha um esquema (esfera com densidade crescendo para fora; cilindro em corte com r e R) e diz que é do guia | — |

Nenhum dado das questões depende só da figura: todos os valores estão no enunciado. As figuras servem para o aluno ver a geometria.

## 6. Decisões tomadas sem perguntar ao usuário

1. **"Questões 5, 24, 29, 39, 52, 53, 76" = Problemas.** As Perguntas do capítulo vão só até 12, e 24–76 só existem nos Problemas.
2. **Constantes:** ε₀ = 8,85 × 10⁻¹² C²/(N·m²), k = 8,99 × 10⁹ N·m²/C², e = 1,602 × 10⁻¹⁹ C, g = 9,8 m/s² (as do livro).
3. **P29(b) e (d):** "direção (para dentro ou para fora)" = radial, para o eixo ou para longe dele.
4. **P39:** a esfera está afastada da placa, então as duas cargas têm o mesmo sinal; q > 0 → σ > 0 (a figura do livro mostra + na placa). O guia diz isso.
5. **P24(c) e P53(e) pedem gráficos.** Gráfico não dá para conferir num campo de texto. O guia pergunta a forma do gráfico por alternativas (descritas em palavras) e mostra o gráfico certo depois.
6. **P76 tem resposta em símbolos.** O aluno escreve a expressão no papel e confere com valores-teste (ρ = 1,00 µC/m³, R = 2,00 cm; E em r = 1,00 cm e r = 4,00 cm), além de uma pergunta de alternativas sobre a forma.
7. **P5:** a resposta do gabarito, "3,01 nN·m²/C", é 3,01 × 10⁻⁹ N·m²/C. O campo pede N·m²/C e aceita 3,01e-9.
8. **Erro de tradução no Problema 31** (usado como exemplo com lacunas no Degrau 5): o texto diz "3,0 e 6,0 m de raio", mas o gabarito só bate com 3,0 e 6,0 **cm**. O guia usa cm e avisa.
9. **Erro de tradução na Pergunta 5** (elétron entre placas): a tabela do livro em português (+4σ/−σ e +4σ/−5σ) não dá o gabarito "todos empatados"; a edição em inglês tem +7σ/−σ e +3σ/−5σ. O guia não usa essa pergunta.
10. **Teste 2:** as setas do desenho são difíceis de reconstruir com certeza. O guia usa a mesma ideia com uma tabela de fluxos por face (números do guia), sem fingir que é a figura do livro.
11. **Exemplos com lacunas** tirados de Problemas ímpares que não estão na lista (1, 3, 7, 15, 21, 31, 49, 55): têm gabarito, então o aluno confere. Os de Degraus 3, 4 e 7 sem gabarito (P78, ρ = Cr², placa horizontal) são "calculados pelo guia". O plano de revisão usa outros ímpares (13, 17, 19, 23, 25, 27, 43, 45, 47, 57, 63, 65, 67, 75, 77, 81).
12. **Lições dos Caps. 21 e 22 aplicadas desde a v1:** leitor de número que aceita vírgula, ×10^, sobrescritos, π, √ e frações; respostas só depois de conferir; feedback por alternativa; alternativa certa espalhada entre a, b, c e d; caixa de constantes nas questões; widgets borrados até a previsão; sinal sempre escrito (não só pela cor); CSS do SVG restrito às figuras; equações longas quebradas no celular; botão "Apagar meu progresso"; dica 2 com o desenho esperado nas questões com geometria.
13. **Alunos-agente leem uma cópia cega** (`rodada-1/aluno/`, gerada por `rodada-1/gerar_cego.py`) desde a rodada 1, para não verem respostas no código-fonte (lição do Cap. 21).
14. **Navegador:** o plugin Playwright desta sessão não conectou; a verificação usa o pacote `playwright` do cache do npx com o Chrome do sistema (`/usr/bin/google-chrome`), por um script em `rodada-1/verificar.js`.

## 7. Verificação da v1

1. **`calculos.py`** roda sem erro (`python3 -I calculos.py`): 180 linhas, **nenhuma divergência** com o gabarito. Conferidos com gabarito: P5, P29 (a–f), P39, P53 (a–d) e os exemplos/lacunas (P1, P3, P7, P15, P49, P55, P65, P31, P25, P21, P75, P19, Pergunta 1, Pergunta 9). Única observação: no P31(a) o cálculo dá 2,25 × 10⁶ N/C e o gabarito, com 2 algarismos, escreve 2,3 × 10⁶ (arredondou 2,25 para cima). O script compara com 3 % de tolerância e o campo do guia aceita os dois valores. P24, P52 e P76 são pares: "calculada pelo guia, sem gabarito oficial".
2. **Questões:** as 7 estão no guia, cada uma com os 5 níveis de ajuda (`data-questao`, `data-nivel` 1–5). Têm figura reconstruída do PDF as cinco que têm figura no livro (P5, P24, P29, P39, P52); P53 e P76 têm esquema do guia, marcado como tal.
3. **Navegador** (Playwright do cache do npx + Chrome do sistema, servidor local; script `rodada-1/verificar.js`): nenhum erro no console; KaTeX renderizou 242 fórmulas, 0 erros; 35 níveis de ajuda fechados no início, só a Dica 1 liberada em cada questão; abrir a Dica 1 libera só a Dica 2; os 6 widgets começam borrados e destravam depois da previsão; leituras conferidas com o `calculos.py` (W1: 5,0 e −5,0 N·m²/C em 60° e 120°; W2: saldo +12 com B fora, 0 com B negativa dentro, também na "batata"; W3: 0,700 com a = 0,4R e r = 0,8R; W4: 3,1 % e 0,125 com ρ ∝ r² em R/2; W5: 0,500 (fio) e 0,250 (ponto) em 2 m; W6: externa +2 µC com q = +3, Q = −1); conferência numérica testada com `3,01e-9`, `3,02×10⁻⁹`, `5,99×10^3`, erro de sinal, erro de potência de 10, erro de unidade (N/C × mN/C) e erros comuns reconhecidos; gráfico do P24 escondido até acertar; checkpoint e barra de progresso funcionando; palpite do aquecimento reaparece no Degrau 3. Sem rolagem horizontal a 390 px e a 1280 px. Capturas em `rodada-1/telas/` (celular, desktop, os 6 widgets, tema escuro e impressão).
4. **Defeitos achados e corrigidos na própria verificação:** (a) rolagem horizontal no celular (509 px), causada por duas fórmulas lado a lado no Degrau 3 (grade sem `min-width: 0`); (b) "saldo -12" com hífen no W2; (c) ponto duplicado no palpite; (d) rótulos sobrepostos nos eixos do W3, W4, W5 e na legenda do W6; (e) a alternativa certa do P24(c) mostrava o valor de E em 2R, que é a resposta do item (b): números retirados.
5. **Incidente de processo:** a pasta temporária da sessão foi limpa durante uma pausa e as partes do HTML se perderam; foram reescritas a partir do conteúdo já revisado, numa pasta `_partes/` dentro do capítulo (apagada no fim).
6. **Para a rodada de alunos:** `rodada-1/gerar_cego.py` gera `rodada-1/aluno/` (texto visível da página, ajuda em um arquivo por nível, conferência em um arquivo por pergunta).

## 8. v2 (depois da rodada de alunos)

Decisões em `rodada-1/consolidacao.md` (45 itens: 36 aceitos no todo ou em parte, 9 rejeitados com justificativa). A v2 foi montada a partir das mesmas partes da v1, reescritas onde a crítica pedia; a v1 ficou intacta.

**Verificação da v2** (mesmos scripts da v1; capturas e resultado em `rodada-2/`):
1. `calculos.py`: 212 linhas, nenhuma divergência com o gabarito. Contas novas: fração do fluxo do P5 com o próton a d/4 (0,295, por ângulo sólido, conferida com 1/6 em d/2 e 1/2 em h → 0), carga da Terra vista a 200 e 300 m (Problema 13), força de imagem no P39 com placa condutora, placa finita (z ≈ 0,1R para 10 % de erro), régua de campos e cargas, as duas perguntas numéricas novas da revisão e os erros comuns novos (41,4 N/C no P52(f); 45,2 N/C no P29(a); −2,80 na lacuna do Problema 3).
2. Questões: as 7 com os 5 níveis; P24(c) e P53(e) pedem esboço antes das alternativas; P52 ganhou gráfico na resolução; toda resposta revelada diz a origem.
3. Navegador (`rodada-2/verificacao-v2.json`): nenhum erro no console; 242 fórmulas, 0 erros de KaTeX; ajuda fechada e em ordem; 6 widgets destravam; leituras iguais às do `calculos.py`; conferência numérica com os mesmos testes da v1; sem rolagem a 390 e 1280 px. `rodada-1/medir_cortes.js` não acha nenhum rótulo de SVG fora da área visível nem fórmula com erro. Capturas em `rodada-2/telas/`, agora também dos widgets em outros modos (W1 a 135°, W2 "batata" com B negativa, W3 com cavidade, W4 com ρ ∝ r², W5 placa, W6 fora do centro) e das figuras novas (`fig-*.png`).
