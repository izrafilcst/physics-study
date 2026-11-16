# Reteste do Aluno 2 (Resolvedor) na versão 2 do guia (Etapa 8)

Material lido: `rodada-2/aluno/guia-cego.md`, `rodada-2/aluno/conferir/*` e `rodada-2/aluno/ajuda/*`, além de `rodada-2/telas/desktop-p31.png`. Não abri o HTML, `calculos.py`, `plano.md` nem `rodada-1/aluno/`.

Ordem de trabalho: para cada campo escrevi a resposta e a confiança antes de abrir a conferência. A exceção está assinalada no desafio do P15 (ver abaixo).

## 1. Tabela: ponto da v1 · resolvido na v2? · evidência

| # | Ponto da v1 | Resolvido na v2? | Evidência (frase nova ou arquivo) |
|---|---|---|---|
| 1 | Letra "a" do P31 (enunciado e figura) | **em parte** | Figura: sim. O "x" sobreposto às cotas sumiu, a marca de centro foi acrescentada e a legenda diz "aqui em escala". Enunciado: ainda diz "uma distância a = 50 m do centro da barra" em (d) e (e). Só há uma nota logo abaixo, em `guia-cego.md`: "Atenção: nos itens (d) e (e) o livro reusa a letra a para outra distância (50 m, medida do centro da barra). Neste guia ela se chama D." O enunciado continua usando "a" e a nota diz que se chama D: o texto se contradiz. |
| 2 | Mensagem de `P31-b` para 0,001472 (entregava kq/(a(a+L))) | **sim** | Agora: "Você usou a distância até o centro da barra. De perto (a ~ L), isso erra uns 7 %. Some os pedacinhos de a até a + L (Degrau 5)." A fórmula saiu. |
| 3 | Mensagem de `P8-a` para 288 (dizia "o parceiro dela do outro lado?") | **sim** | Agora: "288 N/C é o campo de q₁ (ou q₂) sozinha. Some com sinais, reta por reta." Não nomeia o cancelamento. |
| 4 | Mensagem de `P38-a` para 4 (entregava z = 4 cm) | **sim** | Agora: "Você leu um z no gráfico e parou aí. O raio sai da fórmula do disco usando esse ponto (Degrau 6)." O valor de z não aparece. |
| 5 | Mensagem de `P9-a` para 1,841e-10 (dizia só "o fator é 3/5") | **sim** | Agora: "Sobram as x: Eₓ = E·Δx/r, com Δx/r = 3/5." A regra do Degrau 3 aparece. |
| 6 | "Usa:" das questões | **sim** | P8: "soma de campos alinhados com P" (antes: "cancelamento..."). P9: "Pitágoras, componentes, simetria, ângulo pelo quadrante" (saiu "triângulo 3-4-5"). P15: "distâncias até P, campo de carga pontual, soma de campos, ângulo" (saiu "distância até o centro de um quadrado, cancelamento de um par"). P31 e P38 mantiveram o texto. |
| 7 | Síntese: "procure pares que se cancelam (lado + sinal, e \|q\| ∝ r²)" | **sim** | Agora: "procure pares que se cancelam (regra de bolso do Degrau 2: lado e sinal, e \|q\|/r² igual)". Aponta para o bloco. |
| 8 | Aviso de ângulos equivalentes (estava só na conferência) | **sim** | Linha do guia, antes das questões: "Ângulos valem em qualquer forma equivalente (−90° = 270°; 180° = −180°)." |
| 9 | Degrau 3, erros comuns: "No centro de um quadrado de lado a, r = a/√2" | **sim** | Trocado por "Muita gente usa a distância horizontal (ou o lado do quadrado) como r. Na verdade r é a distância em linha reta da carga até P: use Pitágoras." |
| 10 | Degrau 5, bloco "A conta": integral por extenso e fórmula fechada | **não** | A integral continua escrita em linhas (`k λ [−1/x]ₐ^{a+L} = ... = kq/(a(a+L))`), e a primitiva de 1/x² ainda vem explicada. A nota nova ("Valor em cima menos valor embaixo") não remove o resultado. |
| 11 | Tabela "Equações do capítulo": kq/(a(a+L)) | **não** | A linha continua com a fórmula fechada para a barra no prolongamento. P31-b ainda vira substituição de números. |

Acrescentei, por conta própria: a conferência de `P31-b` ficou melhor, mas o item 10 e o item 11 ainda permitem resolver P31-b sem integrar. Esse é o principal problema que sobrou.

## 2. Placar dos itens novos (feitos sem ajuda, salvo onde indicado)

| Item | Minha resposta (conf.) | Conferência | Bateu? | Nível de ajuda |
|---|---|---|---|---|
| lac-r-1 (E_C) | 8,99×10⁴ N/C (3) | 8,99×10⁴ | sim | nenhum |
| lac-r-2 (sentido E_C) | −x, para a esquerda (3) | b, certa | sim | nenhum |
| lac-r-3 (E_D) | 6,74×10⁴ N/C (3) | 6,742×10⁴ | sim | nenhum |
| lac-r-4 (sentido E_D) | +x, para a direita (3) | a, certa | sim | nenhum |
| lac-r-5 (E_x, com sinal) | −2,25×10⁴ N/C (3) | −2,248×10⁴ | sim | nenhum |
| P15-des-a (q₁ = +2e) | 288 N/C (2) | 178,9 N/C | **não** | nenhum; corrigi depois de ver a conferência |
| P15-des-b (ângulo) | −11,3° (2) | 18,43° | **não** | nenhum; corrigi depois de ver a conferência |

Observações sobre o desafio:
- Erro meu de conta: usei 8ke/a² como campo de q₁ (+2e), mas é k·2e/r² com r² = a²/2, ou seja, 4ke/a². Com 4ke/a², o total é (4,24; 1,41)·ke/a², com ke/a² ≈ 40 N/C, o que dá 178,9 N/C e 18,4°.
- Não abri ajuda. Mas li a conferência antes de refazer a conta, então o desafio não conta como resolvido sem ajuda. Vale só como "errei de primeira; corrigi com a conferência".
- A mensagem de erro de `P15-des-a` para 160 ("Esse é o campo de q₃ sozinha") e a de 400 ("Você somou os módulos") funcionaram como diagnóstico.

Demais campos que refiz para contexto (todos com resposta anotada antes da conferência): P8-a 0 N/C (3, bateu); P9-a 1,38×10⁻¹⁰ N/C (2, bateu); P9-b 180° (3, bateu); P15-a 160 N/C (3, bateu); P15-b 45° (3, bateu); P26-a 20,6 N/C (2, bateu); P26-b 270° (2, bateu, pela regra de equivalentes); P31-a −5,19×10⁻¹⁴ C/m (3, bateu); P31-b 1,57×10⁻³ N/C (2, bateu); P31-c 180° (2, bateu); P31-d e P31-e 1,52×10⁻⁸ N/C (2, bateu); P38-a 6,93 cm (2, bateu).

Atenção: P26 e P38 já tinham sido resolvidos na v1. Por isso, as avaliações de dicas abaixo não medem se eu daria o próximo passo sem a dica; avalio se o conteúdo de cada nível dá o próximo passo sem entregar o resultado.

## 3. Avaliação das dicas (P26 e P38, níveis 1 a 3, lidos um por vez)

**P26, nível 1 (onde olhar):** na medida. Aponta o Degrau 4 (parte "E se as metades tiverem sinais opostos?", Fig. 4-2) e o Teste 2a, e pede para decidir pela simetria qual componente sobra. Não dá número nem fórmula.

**P26, nível 2 (plano):** na medida, no limite. Lista desenhar o par, ver qual componente sobra, λ = q/(πr/2) e "integre a componente que sobra num quarto e multiplique por 2". O último passo é quase o método inteiro, mas a conta de integração e de constantes continua para o aluno.

**P26, nível 3 (primeiro passo):** entrega demais. Dá λ, dE = (kλ/r)dα, a componente dE·sen α para baixo e a integral completa E = 2∫₀^{π/2}(kλ/r)·sen α dα. Sobra só avaliar ∫sen α = 1 e multiplicar. O primeiro passo deveria ser montar o dE e a componente; o nível 3 faz isso no lugar do aluno. Sugestão: ficar com λ e a orientação do ângulo α, e deixar dE e a integral para o aluno.

**P38, nível 1 (onde olhar):** na medida. Aponta a fórmula do disco dividida por Eₘ e o Problema 35, que é o mesmo raciocínio ao contrário. Para mim, a referência ao Problema 35 quase resolve a álgebra, mas o aluno ainda precisa ler a escala e aplicar a fórmula.

**P38, nível 2 (plano):** na medida. Quatro passos: achar a escala (zₛ em 4 divisões), ler um ponto (z, E/Eₘ) num cruzamento, escrever E/Eₘ pela fórmula e isolar R. Não dá o z nem o R. O passo "ler um ponto num cruzamento" continua sendo do aluno.

**P38, nível 3 (primeiro passo):** na medida. Dá a equação E/Eₘ = 1 − z/√(z²+R²) e pergunta em que z a curva cruza 0,5Eₘ. Não dá o z (4 cm) nem o R. Único reparo: "numa linha vertical da grade" já sugere que o cruzamento cai numa divisão, o que é verdade e é ajuda, mas não entrega o número.

## 4. O que AINDA atrapalha (para a v3)

1. **Degrau 5, "A conta", e tabela "Equações do capítulo" (itens 10 e 11 acima).** A integral está feita por extenso e a fórmula fechada da barra aparece na tabela. P31-b vira substituição. Sugestão: mostrar só `E = kλ∫ₐ^{a+L} dx/x²`, deixar o fechamento para depois da questão, e tirar a linha `kq/(a(a+L))` da tabela até o aluno ter integrado.
2. **Enunciado de P31, alíneas (d) e (e).** Ainda diz "a = 50 m". A nota "Neste guia ela se chama D" fica abaixo e contradiz o enunciado. Sugestão: escrever "uma distância D = 50 m do centro da barra" direto no enunciado.
3. **Nível 3 de P26 (entrega demais).** Monta a integral inteira. Sugestão acima.
4. **Desafio do P15 sem ponto de partida.** O texto diz "Faça depois de acertar o P15", mas não há ajuda própria para o desafio: quem errou a conta de q₁ não tem como saber onde errou sem a conferência. Sugestão: uma dica de nível 1 do tipo "Compare o módulo de q₁ com o de q₃: qual é |q|/r² de cada um?"
5. **Figura de P31 (versão 2):** ficou limpa. Não há item novo.

Nenhum item novo de crítica bloqueia. O que sobra é o item 1 (Degrau 5) e o item 2 (letra "a" no enunciado).
