# Rodada 1: relatório do Aluno 2 (Resolvedor, prova amanhã)

**Escopo do que fiz:** tentei as 17 questões completas (PA1 a P30-33) antes de abrir qualquer `conferir/` e li os enunciados, os "Usa:" e os lembretes "Antes de pedir ajuda". Não li nenhum degrau da teoria. Resolvi o simulado Q1 e Q4, mas com contaminação (ver item 1 da tabela). Só abri a ajuda do P29-11. Os degraus 0 a 7 não foram avaliados por mim: não li a teoria, então não aponto crítica sobre o texto deles.

**Aviso importante:** os 16 acertos sem ajuda vieram do meu conhecimento prévio de eletromagnetismo, não do guia. Em nenhum passo o guia me ensinou algo. Se um aluno que não sabe a matéria usar esta página, ele não chega às respostas só com o que está nela. Isso é um teste de quem já sabe, não de quem aprende.

---

## 1. Itens de crítica

| # | Local | Tipo | Gravidade | Evidência | Sugestão |
|---|---|---|---|---|---|
| 1 | Simulado, `guia-cego.md` linhas 1446 a 1501 (correções recolhidas) | outro (isolamento do teste) | **bloqueia** | Ao ler o arquivo, vi de uma vez as correções de Q1 a Q5 ("E = ... = 9,2·10³ N/C", "B = 8,2·10⁻⁵ T") antes de tentar qualquer questão do simulado. Por isso Q1 e Q4 não foram feitas às cegas. | Tirar as correções do arquivo da página e pô-las em `conferir/` (ex.: `conferir/S1-correcao.md`), como já é feito para os campos. |
| 2 | PA10 (linhas 1169 a 1177) | figura confusa / falta | **atrapalha** | Diz "Na figura (a mesma do Problema 30.27)", mas o bloco da PA10 não tem nenhum `[FIGURA]`. A posição da origem e os lados da espira só aparecem na figura do 30.27, que eu precisaria procurar. | Repetir a figura na PA10, ou escrever "espira com um canto na origem e lados sobre x e y". |
| 3 | P29-11, `ajuda/P29-11-1.md` (Dica 1) | dica fraca | **atrapalha** | "Degrau 6, tabela (fio longo) e a regra da mão direita. A ideia de 'onde zera numa reta' é a do Degrau 1." A dica não diz qual é a pergunta. Eu só destravei porque reconstruí a regra sozinho. | Dizer a pergunta: "Em P, fora dos dois fios, os campos se somam ou se anulam? Depende do sentido das correntes?" |
| 4 | P29-11 (Degrau 1 e Degrau 6, não li) | LACUNA (a verificar) | **atrapalha** | Errei (b) ao escolher "para dentro" porque inverti a regra: entre dois fios com correntes de mesmo sentido os campos se anulam; fora do par, a anulação exige sentidos opostos. Não sei se o Degrau 6 ensina isso. A dica 1 manda ao Degrau 1, que trata de cargas. | Verificar o Degrau 6. Se não tiver a regra, incluir o caso de dois fios com exemplo numérico e uma figura com as duas situações. |
| 5 | "Usa:" de quase todas as questões (ex.: PA6, PA8, P29-87, P30-33) | dica entrega demais | **atrapalha** | PA6: "Usa: ½mv² = eV; r = mv/(|q|B)", que já é a resolução. PA8: "trechos radiais; sentidos opostos", que já é a resposta do item (b). P29-87: "correntes opostas". P30-33: "i = ε/R; P = i²R; F = ∫ iB dr", a sequência inteira. | Esconder o "Usa:" atrás de um botão, ou trocar por "Ideias-chave" sem fórmula nem o passo decisivo. |
| 6 | PA7 e P28-48 (enunciado e campo) | outro (expectativa de resposta) | polimento | "Determine, em termos dos vetores unitários, a força..." mas o campo pede só F_z (escalar). Na prova eu escreveria F = ... k̂ ou só o número? | Pedir o vetor no campo, ou dizer "escreva a componente z". |
| 7 | P30-33 (e), P29-87 (e) | falta prática / outro | polimento | O enunciado pede (e) (taxa de trabalho, P30-33) e "teste dos casos especiais" (P29-87), mas a página só tem campos para (a) a (d) e (f). | Criar o campo ou tirar o item do enunciado. |
| 8 | PA8, enunciado e figura | figura confusa | **atrapalha** | "ligados por dois trechos retos horizontais na altura de C". Não diz que os trechos apontam para C. Tive de deduzir que eles são radiais e que não contribuem. | Escrever "os trechos retos apontam para C (são radiais)" ou desenhar essa relação. |
| 9 | Conferências das abertas: PA1-a, PA4-a, PA5-a, PA5-b, PA6-a, PA7-b, PA9-a, PA10-a | outro (formato) | polimento (PA4-a: **atrapalha**) | "Confere com a alternativa D da prova (3,6 N/C)"; "Confere com a alternativa C da prova"; "A prova imprimiu a alternativa como 6,74 × 10² N/C (erro de expoente)". As questões foram reescritas como abertas, e essas notas falam de alternativas. A do PA4-a ainda manda ignorar um erro da prova, o que confunde quem vai escrever a resposta. | Tirar referências a alternativas dos textos de campos abertos. Mover os erros de impressão da prova para um anexo à parte. |
| 10 | P28-48-b, PA8-b (conferir) | termo não definido | polimento | "Resposta calculada pelo guia (o Problema 29.8 é par)" e "sem gabarito oficial (problema par)". Não sei o que é "par". Outros campos dizem "Gabarito do livro" e não a mesma coisa. | Definir "par/ímpar" uma vez na página. Padronizar a origem da resposta (livro ou guia). |
| 11 | PA4 ("Usa: lata gaussiana") e figura da PA5 ("lata gaussiana tracejada") | termo não definido | polimento | "Lata" aparece como sinônimo de superfície gaussiana sem definição na página. Entendi pelo contexto. | Na primeira aparição: "lata = superfície gaussiana (cilindro ou esfera imaginária)". |
| 12 | Simulado, linha 1425 | falta de clareza | polimento | "A integral ... costuma vir no formulário da prova (Apêndice E)". "Costuma" não diz se vai vir na prova de amanhã. | Dizer se a integral será dada ou não. |

---

## 2. Perguntas ao Professor

1. Professor, por que a PA10 diz "a mesma figura do Problema 30.27" se não há figura nenhuma na PA10? Eu precisei procurar a origem da espira em outra seção.
2. Professor, a regra "fora do par de fios, o campo só se anula com correntes de sentidos opostos" está em algum degrau? Acertei o P29-11 (b) só depois de reconstruí-la sozinho com a mão direita. Se a prova pedir isso sem dica, erro de novo.
3. Professor, por que as correções do simulado estão no mesmo arquivo da página? Vi todas antes de começar Q1. Vou ter a mesma tentação na prova se o papel tiver as respostas perto.
4. Professor, o que quer dizer "problema par"? Por que alguns campos têm "Gabarito do livro" e outros "resposta calculada pelo guia"?
5. Professor, a prova de amanhã é aberta ou tem alternativas? Os textos de conferência dizem "alternativa D da prova" em questões que estão escritas como abertas.
6. Professor, no P28-48 e na PA7 o enunciado pede a força "em termos dos vetores unitários", mas o campo pede só a componente z. Na prova eu escrevo o vetor completo?

---

## 3. Placar

Questões completas (17): **16 resolvidas sem ajuda; 1 resolvida com ajuda até o nível 1 (P29-11); 0 não resolvidas.**

| Questão | Resultado | Nível de ajuda | Confiança (1ª tentativa) |
|---|---|---|---|
| PA1 | resolvida | sem ajuda | 3 |
| PA2-a (direção) | resolvida | sem ajuda | 2 |
| PA2-b (fator 0,83) | resolvida | sem ajuda | 2 |
| PA3-a | resolvida | sem ajuda | 3 |
| PA3-b | resolvida | sem ajuda | 3 |
| PA4-a | resolvida | sem ajuda | 3 |
| PA4-b | resolvida | sem ajuda | 3 |
| PA5-a | resolvida | sem ajuda | 2 |
| PA5-b | resolvida | sem ajuda | 2 |
| PA6-a | resolvida | sem ajuda | 3 |
| P28-5-a | resolvida | sem ajuda | 3 |
| PA7-a | resolvida | sem ajuda | 3 |
| PA7-b | resolvida | sem ajuda | 3 |
| P28-48-a | resolvida | sem ajuda | 3 |
| P28-48-b | resolvida | sem ajuda | 2 |
| P29-11-a | resolvida | sem ajuda | 2 |
| P29-11-b | resolvida **após errar** | **nível 1** | 2 (errei) |
| PA8-a | resolvida | sem ajuda | 3 |
| PA8-b | resolvida | sem ajuda | 2 |
| P29-87-a | resolvida | sem ajuda | 2 |
| P29-87-b | resolvida | sem ajuda | 3 |
| P29-87-c | resolvida | sem ajuda | 1 |
| P29-87-d | resolvida | sem ajuda | 3 |
| PA9-a | resolvida | sem ajuda | 2 |
| P30-19-a | resolvida | sem ajuda | 3 |
| P30-27-a | resolvida | sem ajuda | 2 |
| P30-27-b | resolvida | sem ajuda | 2 |
| PA10-a | resolvida | sem ajuda | 3 |
| P30-33-a a d | resolvidas | sem ajuda | 2 em todos |
| Simulado Q1 (S1-b) | resolvida, **contaminada** | sem ajuda | 2 |
| Simulado Q4 (S4-b) | resolvida, **contaminada** | sem ajuda | 2 |

Dos 32 campos de resposta, 31 bateram na primeira tentativa. O único erro foi P29-11 (b), a escolha do sentido. Na escolha do sentido, a confiança 2 não me salvou: o erro veio de uma regra invertida.

---

## 4. O que funcionou (não remover)

- **Mensagens por erro comum.** Exemplos: "1.907 → Esse é o campo em r = 3,0 cm" (PA5-a); "4e-05 → Você fez Φ/t" (P30-27-a); "−0.4 → ĵ × î = −k̂" (P28-5-a). Cada uma me mostrou exatamente onde eu errei, sem entregar o caminho.
- **Sinal marcado nos campos.** "O sinal faz parte da resposta" (P28-5-a, P28-48-b) evitou que eu ignorasse o sinal.
- **Explicação por alternativa.** PA2-a, PA3-a, P28-48-a, P29-11-b e P29-87-d explicam por que cada alternativa errada está errada. Foi isso que me corrigiu na P29-11 (b) quando li o motivo.
- **Tolerância de 2 % e aceitação de notação** ("1,28e7", "1,28 × 10^7"). Não me deixou brigar com formato.
- **Lembretes "Antes de pedir ajuda".** Perguntas como "já desenhou dois pedaços simétricos?" me fizeram reconferir o desenho antes de qualquer dica.
- **Ajuda escalonada.** O botão de um nível por vez me deixou tentar entre níveis, como esperado.
- **Checagens dentro das correções.** Exemplo: P29-87-d "a amperiana envolve i − i = 0". Mostra o raciocínio em uma linha.
- **Rubrica do simulado** com pontos por item (desenho, lei e montagem, resultado em símbolos, números, sentido).
- **Figuras redesenhadas com cores** (PA5, cores mais fortes na borda para ρ maior). Dá para ler a densidade sem texto.

---

## Apêndice: minhas tentativas (antes de abrir qualquer conferir)

- **PA1:** E = kλL/(a(a+L)), a = 0,10 m, a+L = 0,35 m, λ = 2,00×10⁻⁴ C/m. 1,798×10⁶ × 7,143 = 1,284×10⁷ N/C, para +x.
- **PA2-a:** carga negativa puxa o campo para a barra, +x. **PA2-b:** E = 2k|λ|sen60°/r com |λ| = 3Q/(2πr); fator 3√3/(2π) = 0,827.
- **PA3-a:** a) (r e cos θ são constantes). **PA3-b:** kqz/(z²+R²)^{3/2} = 8,99e9·5e-9·0,04/(0,05)³ = 1,44×10⁴ N/C.
- **PA4-a:** E = 2kλ/r = 539,4/0,08 = 6,74×10³ N/C. **PA4-b:** dentro de metal, E = 0.
- **PA5-a:** Q_enc = πLAR⁴/2; E = AR⁴/(4ε₀r) = 6,4×10⁻¹²/1,77×10⁻¹² = 3,6 N/C. **PA5-b:** E = Ar³/(4ε₀) = 6,75×10⁻¹¹/3,54×10⁻¹¹ = 1,9 N/C.
- **PA6-a:** v = √(2eV/m); B = √(2meV)/(er) = 2,584×10⁻²³/2,192×10⁻²⁰ = 1,18×10⁻³ T.
- **P28-5-a:** v × B tem z = 2Bₓ; F = −e·2Bₓ = 6,4×10⁻¹⁹, logo Bₓ = −2,0 T.
- **PA7-a:** dF = i dx (γx) k̂ (î × ĵ = k̂); direção k̂. **PA7-b:** iγ∫₁²x dx = 1,5 iγ.
- **P28-48-a:** dL ∝ î, só By faz força, então ±k̂. **P28-48-b:** F_z = −i∫₁³ 8×10⁻³x² dx = −5·8×10⁻³·26/3 = −0,347 N.
- **P29-11-a:** B₁ = B₂ em P, d₁+d₂ = 2,25 cm para o fio 1 e d₂ = 1,50 cm para o fio 2: i₂ = 6,5·1,50/2,25 = 4,33 A.
- **P29-11-b (ERRADA na 1ª):** respondi "para dentro", com a regra invertida (achei que fora do par as correntes de mesmo sentido se anulam). Depois do nível 1, refiz a conta com a mão direita: as duas correntes para dentro dão campos de mesmo sentido em P (fora dos fios), então para anular é preciso sentido oposto. Resposta: para fora.
- **PA8-a:** b) μ₀iφ/(4πR). **PA8-b:** (μ₀i/4)(1/R₁ − 1/R₂) = (3,14×10⁻⁷)(0,229)(30,40 − 11,95) = 1,33×10⁻⁶ T.
- **P29-87-a** (r < c): μ₀ir/(2πc²) = 2,4×10⁻⁵·0,002/1,6×10⁻⁵ = 3,0×10⁻³ T. **P29-87-b** (c < r < b): μ₀i/(2πr) = 2,4×10⁻³ T. **P29-87-c** (b < r < a): i_env = 120·(1 − (r²−b²)/(a²−b²)) = 61,6 A; B = μ₀i_env/(2πr) = 6,5×10⁻⁴ T. **P29-87-d:** a) zero.
- **PA9-a:** v = 0,092·3×10⁸ = 2,76×10⁷ m/s; B = mv/(er) = 6,83×10⁻³ T; i = B/(μ₀n), n = 10⁴ m⁻¹: i = 0,544 A.
- **P30-19-a:** ω = 1000·2π/60 = 104,7 rad/s; ε = NBAω = 100·3,5·0,15·104,7 = 5,50×10³ V.
- **P30-27-a:** Φ = ∫∫B dA = 2t²a³; dΦ/dt = 4ta³ = 3,2×10⁻⁵·t; em t = 2,5 s: 8,0×10⁻⁵ V. **P30-27-b:** fluxo para fora crescendo, corrente induzida horária: a).
- **PA10-a:** dΦ/dt = 4·10·(0,03)³ = 1,08×10⁻³ V.
- **P30-33:** ε = v·(μ₀i/2π)·ln((a+L)/a) = 5·2×10⁻⁵·ln 11 = 2,40×10⁻⁴ V; i = ε/R = 6,0×10⁻⁴ A; P = i²R = 1,44×10⁻⁷ W; F = P/v = 2,9×10⁻⁸ N.
- **Simulado Q1:** E = kQ/(y√(y²+L²/4)) = 35,96/(0,05·0,0781) = 9,2×10³ N/C, para cima, longe da barra. Contaminada: li a correção antes.
- **Simulado Q4:** B = μ₀i/(4R) + 2·μ₀i/(4πR) = 5,03×10⁻⁵ + 3,20×10⁻⁵ = 8,2×10⁻⁵ T, para dentro do papel. Contaminada: li a correção antes.
