# Rodada 1: consolidação das críticas e respostas do Professor

Relatórios: `aluno-1-base-fragil.md` (haiku), `aluno-2-resolvedor.md` (haiku), `aluno-3-monitor.md` (sonnet), `aluno-4-visual.md` (sonnet).

**Observação de processo.** Os Alunos 1 e 2 leram o HTML como código-fonte e acabaram vendo respostas escondidas (`data-correta`, `data-resp`, níveis 4–5) antes da hora. O placar deles vale só onde eles mesmos disseram que a leitura foi cega:
- Aluno 1: Degrau 1 com 2 de 3; previsão do W1 errada.
- Aluno 2: P73, P42 e P50 resolvidas sem ajuda e sem ver a resposta. P10, P23 e P21 bateram, mas com alguma resposta vista antes. P7 contaminada.

Para um aluno humano, as respostas não aparecem na página. Isso é uma limitação do teste com agentes, não um defeito que o aluno real veja (ver decisão 41).

**Prioridade usada:** o que bloqueia > erros físicos > o que vários alunos apontaram > o resto. A coluna "Alunos" diz quem levantou o item.

## 1. Tabela única

| # | Problema | Alunos | Gravidade | Decisão | O que muda na v2 |
|---|---|---|---|---|---|
| 1 | "Regra do quociente" usada no degrau da F(x) sem nunca ser ensinada; "limite x → ∞" e o símbolo ∫ também não são definidos | 1 | bloqueia | **Aceito** | Pré-requisito 5 ganha mini-revisão com regra do quociente e da cadeia; caixa "ferramenta de Cálculo" no degrau F(x); uma linha definindo x → ∞ e ∫ no primeiro uso. |
| 2 | Lacuna do P52: campo pede número positivo, mas o texto ao lado diz "Q = −1,11×10⁻⁵ C" | 1 | bloqueia | **Aceito** | Campo rotulado "\|Q\| (sem sinal)"; o sinal é perguntado na lista de escolha; o valor final só aparece depois de conferir. |
| 3 | W2: setas viram só pontas; SVG gigante no desktop; slider quebra de linha; rótulo do eixo cortado | 4 | bloqueia | **Aceito** | W2 redesenhado: haste mínima, rótulos F₁/F₂/F na ponta, cor por fonte, telas lado a lado, largura máxima, rótulo do eixo dentro da área. |
| 4 | Verificador recusa respostas certas: "−14 cm" do gabarito no P13 (2,5 % fora); "−2√2" lido como −2 no P10(a) | 3 | atrapalha (dá "errado" para quem acertou) | **Aceito** | Leitor de número aceita √, frações, potências e sobrescritos, e rejeita sobras ("digite só o número"). Tolerância de 3 % na lacuna do P13. |
| 5 | Gancho: tela mostra 1,3×10⁷ C, mas 1,6×10²⁴ N e "46 vezes" só saem de 1,339×10⁷ C | 3 | erro numérico (polimento) | **Aceito** | Texto e figura usam 1,34×10⁷ C. |
| 6 | Nota do W1: "as de 2000 N" (o máximo possível é 562 N) | 3, 4 | erro numérico | **Aceito** | "as de 560 N". |
| 7 | Ficha do D1: "núcleo: 10⁻¹⁵ m" ao lado de "dois prótons: 14 N" (14 N é a 4 fm; a 1 fm daria 230 N) | 4 | erro de ordem de grandeza | **Aceito** | "14 N a 4,0 × 10⁻¹⁵ m". |
| 8 | Visão geral: "só os elétrons se movem" em água e corpo (lá são íons); "aterrar neutraliza" sem ressalva; "empurra os elétrons" vale só para carga negativa | 3 | erro físico | **Aceito** | Os três cartões reescritos (íons; aterrar fixa o potencial e neutraliza só sem cargas por perto; "reorganiza as cargas"). |
| 9 | Analogia da lâmpada: luz se cancela por interferência; o 1/r² da luz é da intensidade (∝ E²), não do campo; o 4π é convenção, não consequência | 3, 1 | erro físico (analogia) | **Aceito** | Caixa "onde quebra" reescrita com esses três pontos; o 4π e o ε₀ explicados em uma linha. |
| 10 | "Equilíbrio instável" sem qualificar (é ponto de sela: instável ao longo do eixo, estável na transversal) | 3, 4 | imprecisão | **Aceito** | "Instável ao longo do eixo"; Dúvidas da turma explica a sela com números do calculos.py e Earnshaw. |
| 11 | Degrau 3 denso demais (3 ferramentas, 1 lacuna); geometria sen θ = x/(2L) nunca ensinada; gangorra em 3 linhas; x ∝ q^(2/3) sem origem | 3, 4, 1 | atrapalha | **Aceito** | O degrau 3 vira dois: **Degrau 3, força centrípeta** (P73) e **Degrau 4, equilíbrio no fio e na gangorra** (P42, P50). Este ganha geometria do fio, exemplo da gangorra completo e lacuna própria. Total: 7 degraus (o máximo do plano). |
| 12 | Gabarito escrito antes do botão "Conferir" nas lacunas; expressões intermediárias que entregam o passo (s = L/(√3−1); F₃₂/√2 = 0,0254 N) | 1 | atrapalha | **Aceito** | O gabarito só aparece depois de acertar ou de pedir as respostas; os dois passos viraram lacunas. |
| 13 | Dicas 2–3 entregam demais (P7 Dica 2 é receita; P23 Dica 3 traz F(x) e F′(x); P10 Dica 3 traz F₁ₓ completa) | 2, 3, 4 | atrapalha | **Aceito em parte** | O prompt define a Dica 3 como "a montagem em símbolos", então ela continua com equações, mas só a primeira: P23 sem a derivada; P10 só o termo da diagonal; P7 Dica 2 em 3 passos. A Dica 1 do P23 não cita mais as bordas. |
| 14 | Para quem aprende vendo, nenhuma dica mostra o desenho esperado | 4 | atrapalha | **Aceito** | A Dica 2 de P7, P10 e P50 ganha o diagrama de forças esperado (sem números). |
| 15 | Constantes (k, e, mₑ, ε₀, g) não aparecem nas questões | 2 | atrapalha | **Aceito** | Caixa "Constantes" no topo das questões. |
| 16 | P42(a) "mostre" conferido por múltipla escolha chutável | 2, 3 | atrapalha | **Aceito** | Conferência do passo difícil por número: "com x = 5,0 cm e L = 120 cm, quanto vale sen θ?" (0,0208). |
| 17 | P10(b) "justifique" por múltipla escolha com a justificativa na alternativa certa | 2, 3 | atrapalha | **Aceito** | (b) vira conta: "que Q/q zera a força na partícula 2?" (−0,354), seguida de sim/não com feedback por alternativa. |
| 18 | P50: formato da resposta (expressão + valores-teste) só aparece depois do enunciado; não diz de que x depende | 2 | atrapalha | **Aceito** | Caixa logo após o enunciado: "a resposta é uma expressão em L, q, Q, P e h; confira com os valores-teste". |
| 19 | Resposta das questões de escolha só diz "Ainda não" | 3 | atrapalha | **Aceito** | Feedback por alternativa, como nos checkpoints. |
| 20 | Viés de posição: a certa é "b" em 56 % e "d" em 0 % das perguntas; os 6 pré-requisitos são todos "b" | 3 | atrapalha (contamina a calibração) | **Aceito** | As alternativas são reordenadas na montagem para espalhar a correta entre a, b, c e d. |
| 21 | Widgets travados já mostram a resposta (W1 "um quarto"; W2 "F = 0 em 2L") | 4 | atrapalha | **Aceito** | Tela e leitura escondidas até a previsão. |
| 22 | Glifo "F⃗" (seta combinante) vira quadradinho nos SVG | 4 | atrapalha | **Aceito** | Rótulos sem caractere combinante (F₁₂ em negrito). |
| 23 | Raiz some em "1/√2" nas legendas: a regra `.fig svg` deforma o SVG interno do KaTeX | 4 | atrapalha | **Aceito** | Regras de CSS restritas a `.fig > svg`, `.tela > svg` e `.mapa > svg`. |
| 24 | Cabeçalho sem margem lateral no celular (`.cabeca` zera o padding de `.wrap`) | 4 | atrapalha | **Aceito** | Padding só vertical no `.cabeca`. |
| 25 | Equações longas cortadas no celular (D1, D3, D4) | 4 | atrapalha | **Aceito** | Quebradas em linhas. |
| 26 | f1a: texto fala em "carga grande e pequena" e o desenho tem cargas iguais; rótulos soltos | 4, 1 | atrapalha | **Aceito** | f1a redesenhada: +3q grande e +q pequena com setas do mesmo tamanho e rótulo em cada seta. |
| 27 | f2a: cargas iguais (não mostra "mais perto da menor"); dois ✓ no painel de sinais opostos; setas desiguais onde "anula"; regra sem o porquê | 4, 3, 1 | atrapalha | **Aceito** | f2a com cargas de tamanhos diferentes, ✓ só no lado certo, setas iguais onde anula, cor por fonte, e uma frase com o porquê (√ da razão das cargas). |
| 28 | D2 sem nenhuma figura para o Ex. 21.02 e para o P13 | 4 | atrapalha | **Aceito** | Duas figuras novas (ex.: cotas 2L e L; lacuna: s e s + L). |
| 29 | f3a: T não fecha o equilíbrio; T não decomposta | 4 | atrapalha | **Aceito** | DCL redesenhado em escala, com T sen θ = Fₑ e T cos θ = mg tracejadas. |
| 30 | Gangorra: só o arco de F; braços não desenhados | 4 | atrapalha | **Aceito** | Figura nova no Degrau 4 com os dois arcos e as cotas dos braços. |
| 31 | f4a: metade direita sem força desenhada; mistura distância a√2 com componente F/√2 | 4 | atrapalha | **Aceito** | Dois mini-desenhos separados. |
| 32 | Figura do P11 cinza e sem valores | 4, 1 | atrapalha | **Aceito** | Cargas com cor, sinal e valor. |
| 33 | Teste 3: D com tamanhos diferentes em (a), (b), (c); texto alternativo de (b) errado | 4, 3 | atrapalha | **Aceito** | Mesmas d e D nos três; texto alternativo corrigido. |
| 34 | f5a: r, x e α não desenhados; resultante fora de escala; arco solto | 4, 3 | atrapalha | **Aceito** | f5a redesenhada com r, x, α, componentes tracejadas e resultante em escala. |
| 35 | D(Fx): parágrafo "duas coisas competem" pede um gráfico | 4 | atrapalha | **Aceito** | Mini-gráfico com x/r (sobe), 1/r² (desce) e o produto (pico). |
| 36 | Lacuna de derivada simples demais perto do P23 (x/(x²+a²)) | 3 | atrapalha | **Aceito** | Lacuna nova com g(x) = x/(x²+a²)², que exige quociente + cadeia (máximo em a/√3), sem ser o P23. |
| 37 | W1: eixo y se reescala (dobrar q não muda nada no gráfico); escala do desenho torta | 4, 3 | atrapalha | **Aceito** | Eixo y com números e o valor de F escrito no ponto; aviso "desenho fora de escala". |
| 38 | W3: L não muda o desenho; sem forças nem θ | 4 | atrapalha | **Aceito** | Fio proporcional a L, θ e as três forças desenhadas numa bolinha. |
| 39 | W4: a resultante cobre a força da diagonal; setas sem rótulo; passo 0,25 não chega em −2√2 | 4 | atrapalha | **Aceito em parte** | Resultante tracejada e deslocada; rótulos. **Rejeitado** o passo 0,01: com ele, o widget resolveria o P10(a) por tentativa; o passo 0,25 deixa ver que o zero está entre −2,75 e −3 e obriga a conta. |
| 40 | W5: setas minúsculas; eixo y muda ao trocar o modo | 4 | atrapalha | **Aceito** | Setas normalizadas; mesmo eixo nos dois modos, com a outra curva em tracejado. |
| 41 | Resoluções e respostas ficam no HTML (quem lê o código vê tudo) | 2, 1 | atrapalha (só para quem lê o código) | **Rejeitado** | O prompt exige um único arquivo autocontido e os blocos marcados por `data-nivel` para os alunos-agente. Na página, nada aparece antes do clique; esconder do código-fonte exigiria servidor ou cifra, contra o pedido. |
| 42 | Altímetro: barras vazias com pouco contraste; "Síntese" e "Revisão" com barras que nunca enchem; seção atual pouco marcada; mapa não mostra progresso | 4 | atrapalha | **Aceito** | Barras com contorno; Síntese/Revisão viram links sem barra; nó atual com pino; trilha rola até o nó atual; o mapa pinta degraus concluídos e questões resolvidas. |
| 43 | Sinal da carga só pela cor (W2, W4); sem legenda de cores | 4 | atrapalha | **Aceito** | Sinal sempre escrito; legenda "vermelho = +, azul = −" no topo. |
| 44 | Sinal branco sobre salmão no tema escuro | 4 | polimento | **Aceito** | Texto escuro nas cargas no tema escuro. |
| 45 | Convenção de sinais: D1 manda usar módulos, a Dica 3 do P10 usa sinais; Cap. 24 vai exigir o sinal | 3 | atrapalha | **Aceito** | Caixa "duas formas de escrever" no D1; nota no P10; "onde isso volta" avisa do Cap. 24. |
| 46 | λ e σ não aparecem (o Cap. 22 começa com eles) | 3 | atrapalha | **Aceito** | Tabelinha ρ, σ, λ no degrau da carga espalhada. |
| 47 | Hipóteses não ditas: Coulomb para cargas paradas, esferas vistas de fora; esferas condutoras pequenas no P42/P50; peso das esferas; L ≫ h | 3 | polimento | **Aceito** | Uma linha no D1 e hipóteses explícitas nas resoluções (com o erro de 3 % para L = 3h e 0,1 % para L = 10h). |
| 48 | Feedback do d3a incompleto ("Fₑ também muda") | 3 | polimento | **Aceito** | Frase completada. |
| 49 | Cabo de guerra: corda não empurra; equilíbrio estável × instável | 3 | polimento | **Aceito** | Caixa "onde quebra" completada. |
| 50 | Analogias de Bohr e gangorra sem a quebra completa | 3 | polimento | **Aceito** | Uma frase cada. |
| 51 | Plano de revisão manda refazer P13 e P11, já vistos com gabarito | 3 | polimento | **Aceito** | Trocados por P9, P19, P17 e P61 (ímpares com gabarito, ainda não vistos). |
| 52 | Termos sem definição: MEMS, eletroscópio, polo, articulada, carga de prova, "atrito" (eletrização) | 3, 1 | polimento | **Aceito** | Definidos no primeiro uso. |
| 53 | Tempos otimistas | 3 | polimento | **Aceito** | Tempos refeitos: cerca de 2 h nos degraus. |
| 54 | Ex. 21.01c: módulo sai igual a F_y sem a conta | 1 | atrapalha | **Aceito** | Raiz escrita e "F_x é 14 vezes menor que F_y". |
| 55 | Lacuna da F(x): "é máximo" sem dizer que é o único ponto crítico | 1 | polimento | **Aceito** | Frase incluída. |
| 56 | Previsão do W5 feita antes da fórmula | 1 | polimento | **Rejeitado** | Prever antes de ver é a técnica (Prever–Observar–Explicar). As alternativas são qualitativas e o texto anterior dá os dois casos-limite. |
| 57 | "Não achei os botões de confiança" | 1 | polimento | **Rejeitado** | Eles existem: o JavaScript os cria em cada quiz (verificado no navegador). O aluno leu o código, não a página. |
| 58 | Unidade de b no P21 | 2 | polimento | **Rejeitado** | O enunciado do livro já traz "b = 3,0 µC/m²". |
| 59 | Referências soltas ("Prob. 56", "Problema 40") | 1, 2 | polimento | **Aceito** | "(problema do livro, fora deste guia)". |
| 60 | KaTeX só pelo CDN: sem internet, as fórmulas viram texto cru | 3 | atrapalha (offline) | **Aceito em parte** | Aviso visível se o KaTeX não carregar. Embutir o KaTeX foi rejeitado: o prompt fixa o KaTeX do CDN como única dependência. |
| 61 | "Por que isso existe" sem números; P23 sem comparação de escala | 4 | polimento | **Aceito em parte** | Números onde a conta é segura (dois balões com 1 nC a 3 cm: 10 µN, o peso de 1 mg; P23: F_max ≈ 5500 vezes o peso de um elétron). |
| 62 | Mensagem "Escolha uma alternativa..." repetida em todo quiz | 4 | polimento | **Aceito** | Só no primeiro quiz de cada checkpoint. |
| 63 | Nomes diferentes para o mesmo degrau (mapa, lista, título) | 4 | polimento | **Aceito** | Um nome curto por degrau, igual em todo lugar. |

## 2. Respostas do Professor

Marcadas com **[DT]**: vão para a seção "Dúvidas da turma" da v2, ligadas ao degrau certo.

### Aluno 1 (base frágil)

1. *Por que aparece 4π em k, e de onde vem ε₀?* **[DT → D1]** O 4π é uma escolha de unidades do SI, não uma consequência da lei. ε₀ (permissividade do vácuo) é a constante que o SI usa para medir "quanto o vácuo deixa passar" a interação elétrica. Escrever k = 1/(4πε₀) põe à vista a área da esfera, 4πr², e com isso a lei de Gauss (Cap. 23) fica sem 4π. Em outro sistema de unidades (o gaussiano), a lei de Coulomb é só F = q₁q₂/r².
2. *O que é a regra do quociente?* **[DT → degrau F(x)]** (u/v)′ = (u′v − uv′)/v². Ela agora está na mini-revisão do Degrau 0 e numa caixa do degrau da F(x). Truque: escrever u/v = u·v⁻¹ e usar produto + cadeia dá o mesmo resultado.
3. *Por que a força total no Ex. 21.01c é 1,78×10⁻²⁴ N e não a raiz?* **[DT → D5]** É a raiz: √((−0,125)² + 1,775²) × 10⁻²⁴ = 1,78×10⁻²⁴ N. Coincide com F_y porque F_x é 14 vezes menor; ao quadrado, F_x² vira 1/200 de F_y² e mal muda a raiz.
4. *Por que o gabarito aparecia antes de "Conferir"?* Erro do guia. Corrigido.
5. *No P52, que sinal eu digito?* Nenhum: o campo pede |Q|. O sinal é a lista de escolha logo antes (Q negativa, porque precisa atrair).
6. *De onde vem x ∝ q^(2/3)?* **[DT → D4]** É o resultado do item (a) do Problema 42: x³ = q²L/(2πε₀mg). Como x³ ∝ q², x ∝ q^(2/3). Dobrar q multiplica x por 2^(2/3) = 1,59.

### Aluno 2 (resolvedor)

1. *Onde estão k, e, mₑ e ε₀?* Faltavam. Agora há uma caixa de constantes no topo das questões.
2. *Por que P42(a) "mostre" com múltipla escolha?* Foi uma escolha ruim. A v2 confere o passo difícil da demonstração com um número (sen θ = x/(2L) = 0,0208) e mostra a demonstração completa no nível 4.
3. *Por que o formato do P50 ficava no fim?* Erro de ordem. Agora vem logo depois do enunciado.
4. *As respostas estão no código-fonte: é intencional?* É um compromisso. Um único arquivo HTML, sem servidor, não consegue esconder nada de quem lê o código. Para quem usa a página, nada aparece antes do clique. Os blocos marcados por nível servem justamente para vocês, alunos-agente, lerem um nível por vez.
5. *O que é o Problema 40?* Um problema do livro (fora da lista), com a mesma figura do P7. Agora aparece como "(Problema 40 do livro)".
6. *Por que a figura ganha do texto no P50?* **[DT → P50]** Três motivos. (1) A figura é a mesma da edição original em inglês, cujo texto diz "left and right… q and 2q, respectively": +q à esquerda. (2) A figura mostra o bloco à direita do apoio, e isso só equilibra se a ponta empurrada com mais força (2q) for a direita. (3) A figura é independente da tradução, e o texto passou por ela. Dois elementos do próprio livro concordam entre si; só o texto traduzido discorda.

### Aluno 3 (monitor)

1. *E se eu empurrar o próton do Ex. 21.02 para cima?* **[DT → D2]** Ele volta. Em (2L; 0,01L) a força vertical é −0,0100 (em kqq_p/L²): restauradora. Ao longo do eixo, em (2,01L; 0) a força é +0,0196: empurra para longe. É um ponto de sela, instável ao longo do eixo e estável na transversal. Com um elétron, os papéis se invertem. O teorema de Earnshaw garante que nenhum arranjo de cargas paradas tem equilíbrio estável em todas as direções. Por isso armadilhas de íons usam campos oscilantes.
2. *No P7, e se eu soltar as três?* **[DT → P7]** Com q₁/q₂ = −4 e q₃ = q₁, as três ficam com força zero (o calculos.py confere). Não é coincidência. As forças internas somam zero (3ª lei), então, se a força é nula em duas partículas, é nula na terceira de graça. Basta escolher q₃ para zerar a da partícula 2. O equilíbrio é instável (Earnshaw).
3. *Módulos (D1) ou sinais (Dica 3 do P10)? E no Cap. 24?* **[DT → D1]** São duas formas da mesma lei. (a) Módulo pela Eq. 21-4 e sentido pelo desenho: segura para iniciantes. (b) Com sinais: F = kq₁q₂/r² multiplicada pelo vetor unitário que vai da fonte até a partícula; positivo = repulsão. A (b) dispensa o desenho, mas exige o vetor unitário certo. No Cap. 24, U = kq₁q₂/r leva o sinal, e aí o sinal é obrigatório.
4. *Qual o limite de "barra longa" no P50?* **[DT → P50]** A componente vertical da força cruzada dividida pela principal vale h³/(L² + h²)^(3/2). Com L = 10h, 0,1 %; com L = 3h, 3,2 %. As componentes horizontais não fazem torque: estão na linha da barra, que passa pelo apoio.
5. *Dá para resolver o P42 sem aproximar? O "≤" é limite?* **[DT → P42]** Dá, numericamente: sen²θ·tan θ = kq²/(4L²mg). No item (b), x exato = 4,9993 cm contra 5,0 cm. O "≤" não pode ser limite: para 0 < θ < 90°, tan θ = sen θ / cos θ > sen θ sempre. "tan θ ≤ sen θ" é falso para todo ângulo do problema, então é erro de digitação de "≈".
6. *Esferas condutoras: a carga não se redistribui?* Redistribui. A correção relativa é da ordem de (R/x)³, desprezível para esferas "pequenas" (R ≪ x), que é a hipótese do enunciado. Agora isso está escrito nas resoluções.
7. *A lâmpada explica o 1/r² de Coulomb?* Só a geometria (algo que se espalha igualmente por esferas cada vez maiores). A intensidade da luz é ∝ E², a amplitude cai com 1/r, e a luz pode se cancelar por interferência. A caixa "onde quebra" foi reescrita com isso.
8. *Aterrar com um bastão carregado perto?* **[DT → visão geral]** A esfera aterrada fica com carga induzida diferente de zero (de sinal oposto ao do bastão). O que o aterramento fixa é o potencial (V = 0, Cap. 24). Ela só fica neutra se não houver outras cargas por perto.
9. *Massa reduzida e radiação no P73?* **[DT → P73]** A massa reduzida muda v em 0,027 %, muito abaixo da tolerância. Pela física clássica, o colapso levaria 1,6×10⁻¹¹ s. Uma volta leva 1,5×10⁻¹⁶ s, então daria para fazer cerca de 10⁵ voltas: o MCU é uma boa descrição "por volta", mas não para sempre. Foi esse impasse que levou à mecânica quântica.
10. *No P23, e se q₃ fosse negativa?* O módulo da força é o mesmo, então as respostas não mudam. Mas x = 0 vira equilíbrio estável ao longo de x (as atrações puxam de volta) e instável ao longo de y.
11. *O plano de revisão repete P13 e P11?* Corrigido: agora são P9, P19, P17 e P61.
12. *Quanto tempo leva o D3?* Os tempos foram refeitos (o D3 virou dois degraus) e somam cerca de 2 h.

### Aluno 4 (visual)

1. *No W1, como vejo a força dobrar se o gráfico se reescala?* O eixo y agora tem números, e o valor de F aparece no ponto. Dobrar q₁ dobra os números do eixo.
2. *Posso desenhar o diagrama de corpo livre fora de escala na prova?* **[DT → D4]** Pode, desde que as direções e os sentidos estejam certos. Mas, se der para fechar o triângulo de forças (Fₑ + mg + T = 0), ele já mostra tan θ = Fₑ/mg. A figura da v2 está em escala por isso.
3. *Por que o braço do peso se mede do apoio?* **[DT → D4]** Porque o torque é sempre em relação a um ponto, e escolhemos o apoio (que não se move) para a força dele sumir da conta. Se você medir uma força do apoio e outra da ponta, está misturando dois pontos de referência, e a equação não descreve nada. No P50, por exemplo, sai x > L, um bloco fora da barra.
4. *14 N a que distância?* A 4,0×10⁻¹⁵ m (o raio do núcleo de ferro). A 1×10⁻¹⁵ m seriam 230 N. Corrigido na ficha.
5. *Por que o ponto de força nula fica do lado da carga menor?* **[DT → D2]** Para as forças empatarem, |q|/r² tem de ser igual para as duas cargas, ou seja, r ∝ √|q|. A carga menor precisa estar mais perto para compensar ser fraca. Com +q e +4q, o ponto fica a uma distância da +4q duas vezes (√4) maior que da +q.
6. *No P23, devo desenhar o gráfico em log?* Não precisa. Basta o teste das bordas (x = 0 e x = 5,0 m) e o ponto crítico.
7. *Vermelho = + e azul = − é padrão?* É a convenção mais comum em livros e simuladores, mas não é universal (o Halliday desenha todas as partículas em vermelho). Por isso a v2 sempre escreve o sinal também.
8. *Confio na proporção das figuras do livro?* Não: a figura mostra a disposição, e os números vêm do enunciado. Desenhe a sua figura com as proporções dos dados.
9. *Como mostro que um equilíbrio é instável?* Desloque um pouco e veja o sentido da força: se ela aponta para longe do equilíbrio, é instável. Ver a resposta 1 do Aluno 3 (com números).
