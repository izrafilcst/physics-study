# Rodada 1: consolidação das críticas e respostas do Professor

Relatórios: `aluno-1-base-fragil.md` (haiku), `aluno-2-resolvedor.md` (haiku), `aluno-3-monitor.md` (sonnet), `aluno-4-visual.md` (sonnet). Os quatro leram a cópia cega (`aluno/`), sem acesso às respostas no código-fonte.

**Placar da v1.**
- **Aluno 1 (base frágil):**
  - Teste da base: 5/6 (errou o pre4, 1/r em vez de 1/r²).
  - Checkpoints dos Degraus 1 a 7: 21/21 de primeira; previsões 6/6; revisão 7/7.
  - Lacunas: 20/21 (errou lac3-3, a fórmula de dentro da esfera usada fora).
  - Questões, todas sem ajuda: P5, P24, P39, P52, P53, P76 certas; P29 com 5/6 (errou a, com kQ/r²; a Dica 1 bastou para corrigir).
- **Aluno 2 (resolvedor):**
  - 19/21 itens de primeira.
  - P52(f) errado (41,4 N/C: fórmula de dentro usada fora).
  - P39 só com ajuda até o nível 3, por dúvida sobre o ângulo.
  - As outras cinco questões sem ajuda.
- **Ressalva:** os dois alunos acertaram vários checkpoints com confiança 1 ou 2, e o Aluno 2 leu pouco dos degraus (usou a síntese e a tabela de equações).

**Prioridade usada:**
1. o que bloqueia (nada bloqueou);
2. erros físicos e raciocínios que parecem gerais e não são;
3. o que vários alunos apontaram;
4. o resto.

A coluna "Alunos" diz quem levantou o item.

## 1. Tabela única

| # | Problema | Alunos | Gravidade | Decisão | O que muda na v2 |
|---|---|---|---|---|---|
| 1 | "q_env = 0 ⇒ E = 0" usado em D3, P24, P52, ck3-1 e ck6-3 sem a condição de simetria; contradiz os erros comuns do D1 e D2 | 3 | atrapalha | **Aceito** | Passo 3 da receita ganha a condição ("só porque E é igual e perpendicular em toda a gaussiana"); ck6-3 diz que a blindagem de cavidade vale para qualquer forma, com prova no Cap. 24; P52(a) passa a usar "o centro está na cavidade". |
| 2 | "Não pode preferir direção, só sobra radial" não convence; no cilindro, "nem girar" não sai do argumento de rotação | 1, 3 | atrapalha | **Aceito** | D3: rotação em torno da reta centro–ponto. D5: reflexão num plano que contém o eixo (exclui o redemoinho). Vai para "Dúvidas da turma". |
| 3 | "Pela mesma lata (lei de Ampère)": no Cap. 29 o B é azimutal e a ferramenta é um laço | 3 | erro físico | **Aceito** | "Pela mesma ideia de simetria, com um laço circular no lugar da lata." |
| 4 | "Isolante" nunca definido; D6 diz que carga em condutor fica na superfície, mas P52/P76 têm carga no volume | 3 | atrapalha | **Aceito** | Caixa "isolante × condutor" no D3 (primeiro uso de ρ no volume); nota "(isolante)" no P76. |
| 5 | σ/ε₀ × σ/2ε₀: falta dizer "σ da face que você olha"; a ficha do D6 usa σ/ε₀ antes da dedução (D7); só texto recolhido | 1, 3, 4 | atrapalha | **Aceito** | A dedução sai do recolhido e vira figura com duas latinhas lado a lado no D7; a ficha do D6 remete ao D7; todas as fórmulas dizem "σ da superfície que você olha"; uma frase sobre placa condutora fina (σ_tot/2 por face). |
| 6 | P29 não diz que a casca é condutora (e/f só fazem sentido assim) | 2 | atrapalha | **Aceito** | Enunciado: "casca coaxial (condutora)", com nota: a tradução perdeu a palavra; o original diz "conducting shell" e o gabarito só bate assim. |
| 7 | P39: "30° com uma placa vertical" parece ambíguo | 1, 2 | atrapalha | **Aceito** | Nota no enunciado: a placa é vertical, então é o ângulo do fio com a vertical (como na figura). "Pêndulo" trocado por "bolinha num fio". |
| 8 | ck7-1 (Teste 4) cobra a soma de duas placas, ensinada só em "o resto do capítulo" | 3 | atrapalha | **Aceito** | Nova subseção "Duas placas: some com sinais" no D7, antes do checkpoint, com figura das três regiões e os números do Ex. 23.07. Sai da visão geral. |
| 9 | Dica 3 entrega a parte conceitual (P5, P29, P39, P52, P76) | 2, 3, 4 | atrapalha | **Aceito em parte** | O prompt define a Dica 3 como "a montagem em símbolos". Ela continua com equações, mas só a primeira e em forma de pergunta. P5: só a lei de Gauss no cubo, sem o "/6". P29: "o que fica dentro de cada lata?". P39: só as duas equações de equilíbrio. P52 e P76: só a região de dentro. |
| 10 | P52: Dica 1/2 não dizem que fora a carga envolvida é a total; erro 41,4 N/C não reconhecido | 2 | atrapalha | **Aceito** | A Dica 2 ganha "fora: a gaussiana já envolve a casca inteira"; 41,39 N/C entra nos erros reconhecidos; o D3 ganha o erro comum inverso (fórmula de dentro usada fora). |
| 11 | P29(a) com kQ/r² (45 N/C) não reconhecido | 1 | atrapalha | **Aceito** | Erro reconhecido com mensagem: "cilindros longos, não pontos". |
| 12 | Gráficos E(r) do P24(c) e P53(e) viraram múltipla escolha; P52 sem gráfico | 3, 4 | atrapalha | **Aceito em parte** | Antes das alternativas, uma caixa pede o esboço no papel com os pontos de referência. O gráfico aparece depois de acertar. A resolução do P52 ganha o gráfico E(r). Campo de desenho na página foi rejeitado: exigiria um editor gráfico que não cabe num arquivo único simples. |
| 13 | Tabela de equações entrega a resposta do P76(b); nota interna "se perdeu na conversão" vazou no P76 | 1, 2 | atrapalha | **Aceito** | A tabela diz só "fora: refaça a lata (o volume com carga para em R)"; nota removida. |
| 14 | Fig. 2-3 (P15): a carga não parece estar no vértice do cubo destacado | 3, 4 | atrapalha | **Aceito** | O cubo destacado é desenhado inteiro (frente e fundo), com a carga no canto dele. |
| 15 | "Truque da simetria" (chave do P5) sem figura; "mesma posição" vago | 3, 4 | atrapalha | **Aceito** | Figura nova (carga no centro: 6 faces iguais; fora do centro: não vale); critério reescrito: "levados um no outro por uma rotação ou reflexão que mantém a carga no lugar". |
| 16 | Rótulos cortados (Figs. 0-1, 2-2, 3-1, 6-1, P5, Dica 2 do P5, P53) e `\cdotp` em vermelho na Eq. 23-3 | 3, 4 | atrapalha | **Aceito** | Os 7 rótulos achados por script reposicionados; unidade com `\mathrm`. |
| 17 | Setas de cota com as pontas para dentro | 4 | polimento | **Aceito** | Marcador corrigido (pontas para fora). |
| 18 | Fig. 2-1 diz 8 linhas; W2 usa 12; W2 confunde cores (vermelho = entra e = carga +), linhas de A e B iguais | 1, 3, 4 | atrapalha | **Aceito** | Legenda "o número de linhas é arbitrário"; no W2: sai = círculo, entra = quadrado; linhas de B tracejadas; legenda dentro do widget; "as linhas contam saldo, não intensidade". |
| 19 | W6 abre já na resposta da previsão; não mostra a gaussiana no metal | 4 | polimento | **Aceito** | Começa com q = 0; gaussiana tracejada no metal desenhada. |
| 20 | W3 e W5 com texto miúdo no celular | 4 | atrapalha | **Aceito** | Fonte maior nos widgets. |
| 21 | W4 só tem ρ ∝ r², o P53 usa ρ ∝ r | 4 | atrapalha | **Rejeitado** | Acrescentar ρ ∝ r entregaria o gráfico e a razão E(R/2)/E(R) do P53. A transferência de r² para r é o que o degrau treina. A curva tracejada ganha nome. |
| 22 | Exemplo ρ = Cr² sem gráfico | 4 | atrapalha | **Aceito** | Gráfico E(r) do exemplo (r³ dentro, 1/r² fora). |
| 23 | Gráfico estático E(r) nos "resultados" do D3 | 4 | atrapalha | **Rejeitado** | Responderia a previsão do W3, que vem logo depois (prever antes de ver). |
| 24 | Mangueira (D5) contradiz o tubo do P24; "plano" do aquário com dois sentidos; aspersor não diz que só 1/r² conserva; "uma vez" vale só em superfície convexa; cebola não explica as cascas de fora | 3 | atrapalha / polimento | **Aceito** | As caixas "onde a analogia quebra" foram completadas. Formiga: rejeitado (já diz "mais pedaços pelos lados"). |
| 25 | Dielétrico: "o Cap. 25 ajusta a lei" sugere que ela falha | 3 | polimento | **Aceito** | "A lei continua valendo; q_env passa a incluir a carga induzida no material." |
| 26 | "O buraco não conta" sem dizer "concêntrico"; tabela sem "uniforme"/"longo" | 3 | polimento | **Aceito** | Condições escritas. |
| 27 | Terra: "a simetria garante" (é observação); onde está a carga positiva | 3 | polimento | **Aceito** | Frase corrigida; a carga do ar vai para "Dúvidas da turma". |
| 28 | Resposta do aquecimento não diz que era a (c); (b) e (d) não são desmontadas | 1, 3 | atrapalha | **Aceito** | "Resposta do aquecimento: a terceira alternativa", com uma linha contra cada uma das outras. Parágrafo vira lista de 5 passos. |
| 29 | Erros numéricos: lac1-2 reconhece −2,744 (certo: −2,80); P5 3,02 × 3,01 sem explicação; Terra −8 × 10¹⁶ × −7,6; "quase mil vezes" (são ~600); ruptura 2,4 × 3 × 10⁶ | 3 | polimento | **Aceito** | Todos corrigidos (conferidos no `calculos.py`). |
| 30 | P31(a): tolerância de 2 % recusaria o 2,3 × 10⁶ do livro | 3 | atrapalha | **Rejeitado em parte** | A página já usa 3 % e aceita 2,3 × 10⁶ (testado no navegador). A cópia cega é que dizia "2 %"; o gerador agora mostra a tolerância real. A nota do arredondamento foi corrigida: 2,25 com 2 algarismos. |
| 31 | D1, erro comum 4: "tem campo e fluxo total zero" (ambíguo) | 3 | atrapalha | **Aceito** | "tem campo diferente de zero e fluxo total zero". |
| 32 | "Cone", "coaxial", "concêntrica" não definidos | 1, 3 | polimento | **Aceito** | Definidos no primeiro uso. |
| 33 | "Pedaços de esferas" sem conta (por que a forma não importa) | 1 | atrapalha | **Aceito** | Recolhido reescrito com o argumento do cone (área ∝ r², campo ∝ 1/r²); vai para "Dúvidas da turma". |
| 34 | Placa com ρ no volume (P43) no plano de revisão, sem ter sido ensinada; revisão só conceitual | 3, 4 | atrapalha | **Aceito** | P43 sai do plano (entra P75); duas perguntas numéricas na revisão intercalada (esfera e fio). |
| 35 | Valores reais repetem dados dos exercícios; falta régua de campos e cargas | 4 | atrapalha | **Aceito** | "Régua de números reais" na síntese (do P53 ao núcleo do hidrogênio); ficha do D1 com a folha A4 no campo de tempo bom (9 N·m²/C). |
| 36 | Figuras de questões: P24 parece cilindro maciço; P29 sem os pontos 5R₁ e 2R₂ e com cotas emboladas; P52 com "+" só nas bordas; P53 sem legenda de tons | 3, 4 | atrapalha / polimento | **Aceito** | P24 com parede e interior vazio; P29 maior, com os dois pontos e o Q₁ junto da barra; P52 com "+" no material todo; P53 com "mais escuro = ρ maior". |
| 37 | Fig. 3-1 (setas sem nome), 3-3 (gaussiana em r = a some), 5-1 (parede sem destaque), 1-5 (rótulo de ĵ) | 4 | polimento | **Aceito** | Ajustes pequenos nas quatro. |
| 38 | Dica 2 do P39 desenha o diagrama de forças e diz "para longe da placa" | 3, 4 | polimento | **Rejeitado** | Dica 2 com o desenho esperado foi pedido dos alunos visuais no Cap. 21. O sentido da força já está na figura do livro (a esfera afastada e o "+" na placa). |
| 39 | "Usa:" das questões dá o método | 1, 2 | polimento | **Rejeitado** | O prompt pede, em cada questão, "degraus e habilidades que usa". |
| 40 | Síntese entrega a regra das cargas induzidas | 2 | polimento | **Rejeitado** | A síntese é resumo e fica depois das questões; o aluno que a lê antes escolheu não tentar. |
| 41 | Lacunas com o formato pronto (P3, P55); mini-revisão do pre4 só após o erro; checkpoints adivinháveis | 1 | polimento | **Rejeitado** | Lacuna é exemplo com esmaecimento (o formato é o andaime); a mini-revisão depois do erro é o desenho de prática de recuperação; o chute aparece na calibração de confiança. |
| 42 | "Números soltos" no fim de cada degrau, "Tema: automático", "2 % de tolerância" | 1, 3 | polimento | **Rejeitado (no guia)** | São defeitos da cópia cega (o número grande do degrau, o botão de tema). O gerador foi corrigido. |
| 43 | P29 "aterrada", P39 "condutora", P5 "a d/4", placa finita | 3, 4 | — | **Aceito** | Vão para "Dúvidas da turma". O "e se" do P39 estava errado (dizia "bastaria a metade"); foi reescrito com a força de imagem. |
| 44 | Inconsistência nas conferências (umas dizem a origem do valor, outras não); falta nC na caixa de constantes | 2 | polimento | **Aceito** | Toda resposta revelada diz "gabarito do livro" ou "calculada pelo guia"; nC incluído. |
| 45 | Ordem do mapa no celular (7 em cima); legendas "Eq." no celular; W1 "8 de 10"; W5 "placa até 4 m"; síntese "pare" × metal | 4, 3 | polimento | **Aceito em parte** | A escada continua de baixo para cima (é o mapa da subida). Os outros quatro foram ajustados. |

## 2. Respostas do Professor

As marcadas com ★ vão para a seção "Dúvidas da turma" da v2, ligadas ao degrau.

**Aluno 1**
1. ★ *Por que o campo de uma esfera tem de ser radial?* Gire a esfera em torno da reta que liga o centro ao ponto P: a esfera não muda e P fica no lugar. Se E tivesse uma parte "de lado", ela giraria junto, e o campo em P mudaria sem nada ter mudado. Logo, não há parte de lado: sobra a radial. (D3)
2. ★ *Por que um tubo longo não é carga pontual (P29)?* Porque, perto dele (r ≪ L), a carga não está "num ponto": está espalhada ao longo de um comprimento enorme comparado à distância. Quem diz que é cilindro é a forma: comprido e redondo → lata. Só bem de longe (r ≫ L) ele viraria ponto. (D5)
3. ★ *P39: por que o ângulo com a placa é o ângulo com a vertical?* A placa é vertical: medir a partir dela ou a partir de uma reta vertical qualquer dá o mesmo ângulo (retas paralelas). (D7)
4. *A ficha do D6 usa σ/ε₀ antes da dedução?* Não era intencional. Agora remete ao D7, onde está a dedução com figura.
5. ★ *Por que a forma da superfície não importa?* Olhe da carga: cada pedacinho da superfície tapa um "cone" de direções. Se o pedaço estiver mais longe, a área dele cresce com r² e o campo cai com 1/r², e o fluxo pelo cone fica igual. Os cones de todas as direções juntos dão q/ε₀, seja qual for a forma. (D2)

**Aluno 2**
1. ★ *P52(f): fora da casca, uso a carga total?* Sim. Quando a gaussiana já envolve o material inteiro, q_env para de crescer: é a carga total da casca, e E cai com 1/r². (D3)
2. *P39: e se a prova disser só "com a placa"?* Olhe a figura; se a placa é vertical, é o ângulo com a vertical (resposta 3 do Aluno 1).
3. *P29: a casca é condutora?* Sim. O português perdeu a palavra; o original diz "conducting shell", e o gabarito de (e) e (f) só bate assim.
4. *P76(a): deduzir ou só conferir?* Deduzir. A conferência numérica só confirma o resultado da dedução.
5. *Por que não havia nC?* Esquecimento; incluído.

**Aluno 3**
1. ★ *P5 com o próton a d/4?* O truque do cubo falha. Pelo ângulo sólido do quadrado, Ω = 4 arcsen[d²/(d² + 4h²)]: com h = d/4, o quadrado recebe 29,5 % do fluxo total (5,34 × 10⁻⁹ N·m²/C). Com h → 0, recebe a metade, como a metade da esfera do D2. (D2; `calculos.py`)
2. ★ *P39 com placa condutora?* A esfera induz carga na placa e é atraída por ela (força de "imagem", k q²/(2d)²). Com a esfera a 1 cm, essa força é 9 × 10⁻³ N, 1 600 vezes a força qE do problema (5,7 × 10⁻⁶ N); só ficaria pequena a mais de ~40 cm. A conta simples deixaria de valer. O "e se" da v1, que dizia "bastaria a metade", estava errado e foi corrigido. (D7)
3. ★ *P29 com a casca aterrada?* A superfície externa perde os −3,40 pC para a terra; a interna continua −3,40 pC (a barra ainda a induz). Fora, E = 0: é a blindagem de um cabo coaxial. (D6)
4. *Cavidade deslocada no P76?* A lata não serve mais (sem simetria). Por superposição (cilindro cheio + cilindro de carga −ρ no buraco), o campo dentro da cavidade fica uniforme, ρd/(2ε₀). É prova, não invenção: superposição vale sempre.
5. *P53 condutor?* Num condutor a carga iria toda para a superfície (D6): E = 0 dentro e 22,3 mN/C logo fora. ρ ∝ r só existe num isolante, que agora o guia define.
6. *E se o campo caísse com 1/r^2,01?* O fluxo por uma esfera passaria a depender do raio e a lei de Gauss deixaria de valer. É por isso que o expoente é medido com tanta precisão.
7. ★ *Onde está a carga positiva da conta da Terra?* No ar. A −6,8 × 10⁵ C é a carga dentro de uma esfera logo acima do chão. Com os dados do Problema 13 (60 N/C a 300 m), a esfera a 300 m envolve só −2,7 × 10⁵ C: entre o chão e 300 m o ar tem cerca de +4 × 10⁵ C. (D3)
8. *Carga no meio de uma aresta ou no centro de uma face?* Os cubos em volta ainda dividem o total (4 ou 2), mas as faces de cada cubo já não são todas equivalentes; algumas exigem integral (ou ângulo sólido).
9. ★ *Quando q_env = 0 permite concluir E = 0?* Só quando a simetria garante E igual e perpendicular em toda a gaussiana (esfera, lata, latinha). Sem simetria, Φ = 0 não diz nada sobre E em cada ponto. A blindagem de uma cavidade vazia num condutor vale para qualquer forma, mas a prova usa o potencial (Cap. 24). (D3)
10. *Tubo finito (L = 10R)?* Dentro, E já não é exatamente zero perto das pontas; no centro fica pequeno. Fora do escopo do guia; o Cap. 22 dá o método (somar anéis).
11. *Barra isolante com ρ no P29?* Em 5R₁ e 2R₂ nada muda (só importa a carga envolvida). Dentro da barra, E = ρr/(2ε₀), como no P76.
12. ★ *Quanto vale E exatamente em r = R no P24?* Numa camada de espessura zero, o campo não está definido em r = R: ele salta de 0 para λ/(2πε₀R). Numa parede real, ele cresce dentro da espessura da parede. No gráfico, desenhe o salto. (D5)

**Aluno 4**
1. ★ *150 N/C no chão: há 300 V entre o chão e a minha cabeça?* No ar parado, sim, uns 300 V em 2 m. Você não sente porque o seu corpo é condutor: ele fica todo no potencial do chão e deforma o campo em volta, e o ar quase não conduz, então não passa corrente. P29 e P53 dão campos muito menores porque as cargas são de picocoulombs e femtocoulombs. A régua da síntese mostra isso. (D3)
2. *W2: linhas tortas?* O widget soma o fluxo carga por carga, o que vale porque o fluxo é linear. As linhas do campo total seriam curvas, mas o saldo não muda. Está dito no widget.
3. *E em r = R no P24:* resposta 12 do Aluno 3.
4. *Ver a parábola do P53 antes?* Não: é a transferência que o degrau treina (item 21).
5. *P15 com a carga na aresta ou na face:* resposta 8 do Aluno 3.
6. ★ *Até onde a "placa infinita" vale?* Para um disco de raio R, o erro passa de 10 % a partir de z ≈ 0,1R. Uma placa quadrada de 10 cm equivale a um disco de 5,6 cm: a 1 cm, o campo é 83 % de σ/2ε₀. (D7)
7. *Capacitância do coaxial:* é o Cap. 25. O "Onde isso volta" do D5 já aponta.
