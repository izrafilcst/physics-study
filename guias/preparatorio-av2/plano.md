# Plano — Preparatório da Avaliação 2 (caps. 21–23 e 28–30)

**Prova:** segunda, 23/11/2026, **toda aberta** (as provas antigas tinham 4 de múltipla escolha + 1 discursiva).
**Escopo confirmado pelo usuário:** caps. 21, 22, 23, 28, 29 e 30. Caps. 24–27 fora.
**Tempo disponível:** ~4 h/dia (qui à noite, sex, sáb, dom) → ~13 h.
**Saída:** `guia-v1.html` (v1), `guia-v2.html` (final), um arquivo só.

## 0. Fontes usadas

- Fotos em `fotos-prova/`: Avaliação 2 de 2024.1 (Q1–Q5), Avaliação 2 de 2024.2 (Q1–Q5), questão dos arcos (prova antiga), listas do quadro. A Avaliação 1 (termodinâmica) foi separada em `fotos-prova/avaliacao-1-termodinamica/` e não entra.
- A Q5 de 2024.1 (arco de 120°) estava só dentro do zip `19.26.04` (nome repetido): extraída para `fotos-prova/WhatsApp Image 2026-11-19 at 10.37.31 (do zip 19.26.04).jpeg`.
- Halliday `halliday-v3/` + PDF original (figuras 29-42, 29-88, 30-50, 30-54 vistas no PDF, págs. 546, 565, 626, 627).
- Guias v2 dos caps. 21, 22 e 23 (enunciados, dicas e respostas dos 22 problemas das listas).
- PDFs `fotos-prova/1 - segunda prova de fisica 2.pdf` (= Av2 2024.2) e `2 - segunda prova de fisica 2.pdf` (= Av2 2024.1), chegados durante o trabalho: versões digitadas das mesmas provas, sem questão nova. Confirmaram B = αx î + γx ĵ (2024.2 Q4) e a espira com canto na origem (2024.1 Q4). Revelaram que a 2024.2 Q2 imprime a alternativa como 6,74 × 10² N/C (erro de expoente da prova; a conta dá 10³) e que a ordem das alternativas da 2024.2 Q1 muda entre as versões (o guia cita o valor, não a letra).

## 1. Raio-X das provas antigas (incidência)

| Questão antiga | Tema | Cap. | Origem no livro | Certa (conferida) |
|---|---|---|---|---|
| 2024.2 Q1 | E de barra no eixo | 22 | parecida com P22.31 (lista) | 1,3 × 10⁷ N/C (letra muda entre versões: A na foto, C no PDF) |
| 2024.1 Q5 | E de arco de 120° com −Q | 22 | Exemplo 22.03 | 0,83 kQ/r², para a barra |
| 2024.2 Q5 | V e E no eixo do anel | 24/22 | texto do cap. 22/24 | adaptada: só E (cap. 22) |
| 2024.2 Q2 | Gauss, tubo fino | 23 | P23.24 (lista) com outros números | 6,74 × 10³ N/C |
| 2024.1 Q1 | Gauss, cilindro ρ = Ar² | 23 | P23.32(b), **mesmos números** | D, 3,6 N/C |
| 2024.2 Q3 | elétron acelerado + círculo em B | 28 | estilo P28.20/P28.21 | D, 1,18 × 10⁻³ T |
| 2024.2 Q4 | força em fio com B(x) | 28 | P28.48 (lista) em símbolos | A, (3iγ/2) k̂ |
| antiga Q4 | dois arcos, Biot-Savart | 29 | P29.8 com outros números | 1,33 μT |
| 2024.1 Q3 | solenoide + elétron em círculo | 29+28 | P29.53 com v dobrada | C, 0,54 A |
| 2024.1 Q4 | fem com B = 4t²y | 30 | P30.27 (lista) com outros números | E, 1,08 mV |
| 2024.1 Q2 | J = Cr², energia | 26 | — | **fora do escopo** (A, 2,7 × 10⁵ J) |

Contagem (uma questão pode contar em dois temas): campo de distribuição contínua 3 · Gauss 2 · força magnética 3 · fontes de B 2 · indução 1 · Coulomb 0.
**Achados que orientam o foco:**
1. A prova é o Halliday com os números trocados; 4 das 10 vêm direto das listas, as outras de problemas vizinhos ou de exemplos/deduções do texto.
2. 6 de 10 exigem montar uma integral de algo não uniforme (λ dx, ρ(r) dV, B(y) dA, B(x) dx). Vira o Degrau 2 ("fatiar e somar").
3. Na discursiva de 2024.2, "mostre detalhadamente" perdeu a nota por escrever V = kq/r sem integrar dq. Em prova aberta, a dedução vale ponto: rubrica + "na folha da prova" em cada resolução.
4. Erros reais nas provas: interior × exterior no Gauss (1,9 em vez de 3,6 N/C), produto vetorial (ĵ em vez de k̂), fator ½ da energia cinética, raio × diâmetro.

## 2. Habilidades (H) e matriz questão × habilidade

H1 somar vetores por componentes e simetria · H2 equilíbrio de forças (Coulomb + mecânica) · H3 escrever o elemento (dq, dV, dA, dL) e os limites · H4 integrar dE com componentes e simetria · H5 escolher gaussiana e achar q_env (inclusive com ρ(r)) · H6 condutor: E = 0 dentro, cargas induzidas · H7 produto vetorial com î, ĵ, k̂ · H8 movimento circular em B + energia de aceleração · H9 força em fio, inclusive com B variável · H10 Biot-Savart: fio e arco, sentido (⊙/⊗) · H11 Ampère com densidade de corrente uniforme · H12 fluxo não uniforme por faixas · H13 Faraday/Lenz, gerador, fem de movimento · H14 escrever a resolução para a prova aberta.

| Questão | Hs |
|---|---|
| PA1 barra (2024.2 Q1) | H3 H4 H14 |
| PA2 arco 120° (2024.1 Q5) | H3 H4 H1 H14 |
| PA3 anel (2024.2 Q5 adapt.) | H3 H4 H14 |
| PA4 tubo (2024.2 Q2) | H5 H6 |
| PA5 cilindro ρ = Ar² (2024.1 Q1) | H3 H5 |
| PA6 elétron acelerado (2024.2 Q3) | H8 |
| PA7 fio com B(x) (2024.2 Q4) | H3 H7 H9 |
| PA8 dois arcos (antiga Q4) | H10 H14 |
| PA9 solenoide + elétron (2024.1 Q3) | H8 H11 |
| PA10 fem B = 4t²y (2024.1 Q4) | H12 H13 |
| P28.5 | H7 |
| P28.48 | H3 H7 H9 |
| P29.11 | H10 H1 |
| P29.87 | H11 |
| P30.19 | H13 |
| P30.27 | H12 H13 |
| P30.33 | H3 H12 H13 |
| Cartões 21: 7, 10, 21, 23, 42, 50, 73 | H1 H2 (H3 no 21) |
| Cartões 22: 8, 9, 15, 26, 29, 31, 38, 81 | H1 H3 H4 |
| Cartões 23: 5, 24, 29, 39, 52, 53, 76 | H5 H6 (H3 no 53) |

## 3. Pré-requisitos

Vetores (componentes, módulo, ângulo pelo quadrante; î × ĵ = k̂ e ciclos); integrais ∫xⁿ dx, ∫dx/x², ∫dx/x = ln; substituição u = z² + R²; volume de casca fina (4πr² dr, 2πrL dr); MCU (F = mv²/r); energia cinética ½mv² e "ganho qV ao atravessar uma ddp V" (usado em problemas do cap. 28; é só uma linha, não o cap. 24 inteiro). Degrau 0 testa tudo isso.

## 4. Degraus (enxutos)

| Degrau | Objetivo (1 frase) | Hs | Desbloqueia | Tempo |
|---|---|---|---|---|
| 0 Aquecimento | Testar pré-requisitos e ler o raio-X da prova | — | — | 10 min |
| 1 Cargas pontuais | Somar forças e campos de cargas pontuais por componentes e simetria | H1 H2 | cartões 21.x, 22.8/9/15/81 | 25 min |
| 2 Fatiar e somar | Escrever dq, dV, dA, dL e os limites em qualquer geometria | H3 | (base de 3, 4, 5, 7) | 25 min |
| 3 Campo de barras, arcos e anéis | Integrar dE usando simetria para matar componentes | H4 | PA1, PA2, PA3, cartões 22.26/29/31/38 | 35 min |
| 4 Gauss | Escolher a gaussiana e achar q_env, com ρ(r) e condutores | H5 H6 | PA4, PA5, cartões 23.x | 35 min |
| 5 Força magnética | F = qv × B, círculo em B, força em fio com B(x) | H7 H8 H9 | P28.5, P28.48, PA6, PA7 | 35 min |
| 6 Fontes de B | Biot-Savart (fio, arco) e Ampère (fio grosso, coaxial, solenoide) | H10 H11 | PA8, P29.11, P29.87, PA9 | 40 min |
| 7 Indução | Fluxo (por faixas), Faraday/Lenz, gerador, fem de movimento | H12 H13 | P30.19, P30.27, PA10, P30.33 | 40 min |

Cada degrau: por que existe (2 linhas) → intuição com figura (+ onde a analogia quebra) → fórmulas com ficha curta → exemplo resolvido (roteiro Entender → Verificar, "por quê?" recolhidos) → exemplo com lacunas → erros comuns (refutação) → checkpoint 3 questões com confiança → desbloqueia → onde volta.
Widgets (3, cada um com pergunta de previsão): W4 E(r) de cilindro com ρ = A rⁿ; W5 raio da órbita em B (V, B, partícula); W7 fluxo e fem na espira com B = c t² y.

## 5. Ordem das questões

PA1 → PA2 → PA3 (D3) · PA4 → PA5 (D4) · P28.5 → PA6 → P28.48 → PA7 (D5) · P29.11 → PA8 → P29.87 → PA9 (D6) · P30.19 → P30.27 → PA10 → P30.33 (D7).
Cartões 21–23 (enunciado, 2 dicas, resposta, link para o guia v2 antigo) agrupados por capítulo, depois das questões completas.
**Simulado aberto** (domingo, 2 h, 5 questões novas no estilo do professor, rubrica para autocorreção): S1 barra na mediatriz (22) · S2 casca cilíndrica com ρ = A/r (23) · S3 próton acelerado em B (28) · S4 grampo: 2 fios semi-infinitos + semicírculo (29) · S5 espira perto de fio com i(t) (30).

## 6. Cronograma

Qui (noite, ~2 h): Raio-X, D0, D1, cartões do cap. 21 (só os que errar no checkpoint). · Sex (4 h): D2, D3, D4, PA1–PA5, cartões 22/23 escolhidos. · Sáb (4 h): D5, D6, D7, as 7 da lista 28–30, PA6–PA10. · Dom (4 h): simulado (2 h, no papel, cronometrado) + correção pela rubrica + revisão intercalada + refazer erros. · Seg (30 min): formulário + "erros que custam ponto".

## 7. Figuras

| Figura | Dados de onde |
|---|---|
| Fatias (4 painéis: dx, R dθ, 2πrL dr, a dy) | explicativa |
| Barra no eixo, arco com par simétrico, anel com dE e componentes | explicativa (padrão Halliday 22-) |
| Lata gaussiana em cilindro; W4 E(r) | explicativa |
| Regra da mão direita / órbita; fio com B(x) e dF | explicativa |
| Arco com ds e r̂; coaxial com amperianas | explicativa; Fig. 29-88 do PDF |
| Espira com faixa dy; trilhos + fio (Fig. 30-54) | Figs. 30-50 e 30-54 do PDF |
| PA1 barra/ponto; PA2 arco 120° (Exemplo 22.03, foto da prova); PA3 anel; PA4 tubo; PA5 cilindro; PA7 fio no eixo x; PA8 dois arcos (foto da prova); PA9 solenoide; PA10 espira 3 cm | fotos das provas + texto |
| P29.11 (Fig. 29-42); P29.87 (Fig. 29-88); P30.27 (Fig. 30-50); P30.33 (Fig. 30-54) | PDF, págs. 546, 565, 626, 627 |
| S1, S2, S4, S5 | desenhadas pelo guia (questões novas) |

Nenhuma figura dependeu de dado que só existia no desenho: os dados numéricos estão nos enunciados. Na PA8, os sentidos das correntes foram lidos da foto (arco externo anti-horário, interno horário): a prova só pede o módulo.

## 8. Decisões tomadas sem perguntar

1. 2024.2 Q5 pedia V do anel (cap. 24, fora do escopo) e depois E = −dV/dz. Virou "mostre, integrando dq, que E no eixo do anel é …" (cap. 22), mantendo o "mostre detalhadamente".
2. 2024.1 Q2 (J = Cr², cap. 26) fica fora; aparece só no raio-X como "fora do escopo".
3. A energia de aceleração (½mv² = |q|V) entra numa linha no Degrau 5: os problemas do cap. 28 a usam e a prova de 2024.2 cobrou.
4. Na PA7 a foto mostra "B = αx î + γx ĵ"; a componente î não gera força num fio em x, então a resposta não depende de ser αx ou α.
5. Alunos-agente: 2 (pedido do usuário): Resolvedor (haiku) e Monitor cético (sonnet), com cópia cega desde a rodada 1. Reteste só com o Resolvedor.
6. Questões convertidas para abertas: o campo de conferência aceita número (2 %) ou, nas literais, um valor-teste numérico ou alternativas.
7. Visual: mantida a identidade dos guias anteriores (o usuário já sabe usar; serifa no texto, verde-azulado nas ações, escada de degraus). O elemento novo e marcante é o **Raio-X da prova** (tabela de incidência + "de onde veio cada questão") e o cronograma de 4 dias. Cor nova só para o campo magnético (magenta), para não confundir com E (âmbar) e com a gaussiana (verde).

## 9. Verificação da v1

1. `python3 -I calculos.py` roda sem erro; nenhuma divergência acima de 2 % com o gabarito ou com a alternativa certa das provas (P29.53 → 0,272 A e P30.27 → 80 μV confirmam os métodos das PA9 e PA10).
2. As 17 questões completas têm os 5 níveis (`data-questao`/`data-nivel`), e todas as que tinham figura têm figura reconstruída (29-42, 29-88, 30-50, 30-54 do PDF; figuras das provas redesenhadas). Os 22 cartões têm 3 níveis e link para o guia v2 antigo.
3. Navegador (Playwright + Chrome do sistema, `rodada-1/verificar.js`, resultado em `rodada-1/verificacao-v1.json`): sem erros no console; KaTeX ok (374 fórmulas, 0 erros); 151 níveis fechados no início e abrindo em ordem; 3 widgets travados até a previsão e com leituras corretas; conferência numérica reconhece os erros previstos; palpite, relógio, calibração e persistência funcionam; sem rolagem lateral a 390 e a 1280 px. Capturas em `rodada-1/telas/` (cada seção nas duas larguras, widgets, resoluções, tema escuro, impressão).
4. Ajustes feitos depois da primeira captura: órbita do widget W5 cabendo no quadro, rótulo do seletor, subscritos em texto (q<sub>env</sub>), sobreposição na figura 30-54.

## 10. Rodada 1 e v2

- Alunos: Resolvedor (haiku, cópia cega) e Monitor cético (sonnet). Relatórios em `rodada-1/aluno-2-resolvedor.md` e `rodada-1/aluno-3-monitor.md`; decisões em `rodada-1/consolidacao.md` (36 aceitos, 1 rejeitado).
- Nenhum erro físico encontrado (Monitor refez ~190 contas). Mudanças principais da v2: dedução do fio reto por Biot-Savart (D6), regra dos dois fios (D6), três regras da mão direita, analogias do D5/D7/D4 corrigidas, Dicas 3 encurtadas para a montagem, "Usa:" recolhido, conferências por valores-teste (PA2, PA7), figura da PA10, cronograma realista, cartão "fora das listas", seção "Dúvidas da turma" (12 perguntas).
- Contas novas em `calculos.py` (seção v2): sem divergências.
- Verificação da v2 no navegador (`rodada-2/verificacao-v2.json`, capturas em `rodada-2/telas/`): sem erros no console, KaTeX ok (399 fórmulas), 151 níveis fechados e em ordem, widgets ok, sem rolagem lateral a 390 e 1280 px.
- Gerador cego (`rodada-1/gerar_cego.py`) corrigido: correções do simulado e "ideias da questão" vão para `recolhido/`; texto do palpite corrigido.
- Reteste (Resolvedor, `rodada-2/reteste.md`): 29.11 certa sem ajuda depois de ler o Degrau 6; simulado às cegas com os 7 campos certos, nota própria 8,3/10 pela rubrica. Nada bloqueia. Corrigidos depois do reteste: "(Problema 29.11)" tirado do quadro dos dois fios e das dúvidas; Dica 3 da PA10 encurtada (só a ideia da faixa); Dica 3 da PA8 lembra os trechos radiais. Verificação final da v2 no navegador: sem erros.
- Partes do HTML (`_partes/`) apagadas no fim, como nos guias anteriores; a v2 é autocontida.
