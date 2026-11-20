# Rodada 1 — consolidação (Professor)

Alunos: **2 — Resolvedor** (haiku, cópia cega) e **3 — Monitor cético** (sonnet, guia completo + livro + provas).
Resumo: o Monitor refez ~190 contas e **não achou erro físico**; achou 3 erros de texto, 3 analogias com limite mal declarado e uma lacuna importante para a prova aberta (fio reto por Biot-Savart). O Resolvedor resolveu 16/17 sem ajuda (por conhecimento prévio, sem ler os degraus) e travou só no sentido da corrente da 29.11(b).

Legenda: R = Resolvedor; M = Monitor. Gravidade: B = bloqueia, A = atrapalha, P = polimento.

## 1. Tabela única

| # | Problema | Quem | Grav. | Decisão | O que muda na v2 |
|---|---|---|---|---|---|
| 1 | Correções do simulado legíveis na cópia cega antes da tentativa | R | B | Aceito (problema da cópia cega, não da página: na página ficam recolhidas) | Gerador cego (`rodada-1/gerar_cego.py`) manda `details.correcao-sim` e `details.usa` para `recolhido/NN.md` |
| 2 | 29.11(b): a regra "onde B zera entre dois fios" não está em lugar nenhum; Dica 1 não diz a pergunta | R | A | Aceito | Quadro "Dois fios paralelos: onde B zera?" no Degrau 6; Dica 1 reescrita como pergunta |
| 3 | O guia nunca deduz o fio reto por Biot-Savart; S4 pede "a partir de Biot-Savart"; falta o fio finito (sen θ) | M | A | Aceito (é o tipo de pedido da prova antiga dos arcos) | Degrau 6 ganha a dedução do fio reto finito (com a troca x = R tg θ) e os casos infinito e semi-infinito; tabela com fio finito; correção do S4 refeita com a dedução |
| 4 | "Na lista" da linha barra/arco/anel diz 8; são 4 | M | A | Aceito | 8 → 4 |
| 5 | Diagnóstico do S1: 18416 rotulado "não projetou" (é fator 2); não projetar dá 10501 | M | A | Aceito | 10501 → não projetou; 18416 → fator 2 |
| 6 | Analogia da porta com mola (D7) faz força parada; Lenz é amortecedor | M | A | Aceito | Analogia trocada por fecha-porta hidráulico (amortecedor), com quebra honesta |
| 7 | Analogia do volante (D5) esconde que r cresce com v | M | A | Aceito | Quebra ganha "no carro o raio não depende de v; aqui r ∝ v e o período é que fica fixo" |
| 8 | Irrigador (D4) não diz que o E de Gauss inclui as cargas de fora | M | A | Aceito | Uma frase na quebra |
| 9 | Três regras da mão direita misturadas no D6; ⊙/⊗ não definidos | M | A | Aceito | Caixa "três regras da mão direita" e ⊙ = ponta da flecha (sai), ⊗ = cauda (entra) |
| 10 | "Costuma vir no formulário": as provas antigas não têm formulário | M, R | A | Aceito | "Não sabemos se virá; sem formulário, use x = y tg θ" + a substituição feita no D6 |
| 11 | "Erros que custam ponto (todos aconteceram em provas reais)": só 5 de 8 são documentados | M | A | Aceito | Lista dividida: "aconteceu nas provas" (5) e "cuidado geral" (3) |
| 12 | Dicas 3 da PA7, PA8, PA9, PA10 já são a resposta simbólica final; Dica 2 da PA5 entrega o truque | M | A | Aceito em parte: Dica 3 deve ser a montagem (prompt), não o resultado | PA7, PA8, PA9, PA10 recortadas para a montagem; PA5 Dica 2 vira pergunta ("até onde vai a carga?"). PA4 e PA6 mantidas: a montagem já é curta por natureza |
| 13 | PA7-b "(?) × iγ" e PA2-b "(?) × Q/(4πε₀r²)" revelam a forma da resposta | M | A | Aceito | Conferência com valores-teste numéricos (PA7: i, α, γ dados; PA2: Q e r dados), com erros previstos |
| 14 | "Usa:" de cada questão entrega o método | R | A | Aceito | Virou bloco recolhido "Ideias que a questão usa (abra só se travar para começar)" |
| 15 | Sábado com 12 questões em ~2 h; quinta "~4 h" vs plano "~2 h" | M | A | Aceito | Cronograma com horas por dia; PA6, PA7 e PA10 viram "faça se errou a irmã do livro" (28.48 → PA7, 30.27 → PA10, widget → PA6) |
| 16 | Nada sobre indutância, RL, força entre fios, torque, Hall (estão nos caps. 28–30) | M | A | Aceito como cartão de visão geral (as listas não cobram; o prompt manda "cartão curto") | Quadro "Fora das listas, mas nos caps. 28–30" com as fórmulas, para ler na segunda |
| 17 | Raio-X cita 28.9 para a PA6; o 28.9 é seletor de velocidade | M | A | Aceito (conferido no livro: o mais próximo é o 28.21) | "28.20 e 28.21" |
| 18 | PA10 diz "a mesma figura do 30.27" sem figura | R | A | Aceito | Figura própria (lado 3,00 cm) |
| 19 | PA8: não diz que os trechos retos apontam para C | R | A | Aceito | Legenda: "trechos na reta que passa por C (radiais)" |
| 20 | Conferências das abertas falam em "alternativa D"; PA4 manda ignorar erro da prova | R, M | P/A | Aceito | Texto cita o valor, não a letra; a nota do erro de impressão ficou só na Resposta da PA4 |
| 21 | "Problema par" não definido; "lata" não definida | R | P | Aceito | Definidos (topo das questões; Degrau 4) |
| 22 | PA7/28.48 pedem o vetor, mas o campo pede um número | R | P | Aceito | Rótulo diz "o vetor é F = F_z k̂" |
| 23 | "6 das 10 integral de algo não uniforme": só 3 têm integrando não uniforme | M | P | Aceito | "6 das 10 pedem montar uma integral"; "e se λ = αx?" nas dúvidas |
| 24 | n = 10: tendência, não promessa | M | P | Aceito | Uma linha no raio-X |
| 25 | ck2-3: "+dx î de 3 a 1" também está certo | M | P | Aceito | Feedback e "Muita gente pensa" citam as duas montagens certas |
| 26 | PA9: γ = 1,004 não comentado | M | P | Aceito | Uma linha na resolução |
| 27 | O livro como distrator aparece em 4 questões; o guia só cita a PA10 | M | P | Aceito | Linha no raio-X: "se seu número bate com o do livro, os números da prova mudaram" |
| 28 | Cotas que se encontram formam "×" (29.11, 30.33, S5); R₁ colide na PA8; v encosta em B na PA9 | M | P | Aceito | Cotas separadas; rótulo e ponto movidos |
| 29 | PA8-a (c): "π vezes" → "2π vezes" | M | P | Aceito | Corrigido |
| 30 | 21.21 listado como destravado pelo Degrau 1 (é do Degrau 2) | M | P | Aceito | Removido da lista do D1 |
| 31 | "checkpoint 1 do Degrau 2" ambíguo | M | P | Aceito | "Checkpoint 2, questão 1" |
| 32 | lac6-1 e lac6-2 com o mesmo valor (passa digitando igual) | M | P | Aceito | r = 5,0 mm → 4,0 × 10⁻⁴ T |
| 33 | Raio-X longo para 5 min | M | P | Aceito em parte | O caso real do anel fica recolhido ("ver o caso real"); tabelas e rubrica ficam |
| 34 | "Força na direção de B (ĵ)" impreciso | M | P | Aceito | "na direção da componente γx ĵ de B" |
| 35 | Palpite na cópia cega aponta "Problema 81" | M | P | Aceito | Gerador corrigido |
| 36 | Plano §1 diz "2024.2 Q1 = A"; no PDF é C | M | P | Aceito | Plano cita o valor |
| 37 | P30-33(e) e P29-87(e) sem campo | R | P | Rejeitado: (e) do 30.33 é igual a (c) (dito na conferência) e (e) do 29.87 é teste de casos-limite, feito na resolução; um campo a mais não ensina nada |

## 2. Respostas do Professor

**Resolvedor**
1. *PA10 sem figura.* Falha minha: agora tem figura própria.
2. *A regra dos dois fios está em algum degrau?* Não estava. Entrou no Degrau 6 (quadro "Dois fios paralelos: onde B zera?") e vai para as Dúvidas da turma.
3. *Correções do simulado no mesmo arquivo.* Na página elas ficam recolhidas; na sua cópia de texto apareceram por falha do gerador, já corrigida.
4. *O que é "problema par"?* O Halliday só traz no fim as respostas dos ímpares; nos pares, a resposta foi calculada pelo guia. → Dúvidas da turma.
5. *A prova é aberta?* Sim, toda aberta. As letras vinham das provas antigas (múltipla escolha); a v2 cita o valor. → Dúvidas da turma.
6. *Escrevo o vetor completo?* Sim: na prova escreva F = (3iγ/2) k̂. O campo da página só confere o número. → Dúvidas da turma.

**Monitor**
1. *Gauss com um fio carregado perto do cilindro.* A lei continua valendo (o fluxo da carga de fora é zero), mas E deixa de ter o mesmo valor em toda a lata; então ela não dá E. Use superposição: E do cilindro (Gauss) + E do fio (Gauss também), somados como vetores. → Dúvidas da turma (D4).
2. *S4: "metade do fio infinito" ou a integral?* Se o enunciado diz "a partir de Biot-Savart", escreva a integral e a troca x = R tg θ (agora no Degrau 6); "metade do infinito" é bom como checagem. → Dúvidas da turma (D6).
3. *Mola × amortecedor; ímã puxado com o dobro da velocidade.* O amortecedor é a imagem certa. Puxar o ímã duas vezes mais rápido dobra dΦ/dt e dobra a fem. → Dúvidas da turma (D7).
4. *30.33 com a barra indo para a direita.* A fem e a corrente trocam de sentido (o fluxo diminui em vez de aumentar); o módulo é o mesmo. Fio entre os trilhos: B troca de sentido no meio e a integral precisa ser separada em dois trechos. → resposta aqui; não entra na v2 (fora do que cai).
5. *Espira centrada em y = 0 com B = 4t²y.* O fluxo das metades se cancela: Φ = 0 e ε = 0. O atalho "B no centro" vale para B linear na posição, em qualquer posição da espira (média de função linear = valor no centro). → Dúvidas da turma (D7).
6. *Barra com λ = αx.* E = kα[L/a − ln(1 + L/a)]; de longe vira kQ/a² com Q = αL²/2 (conferido em `calculos.py`). → Dúvidas da turma (D3).
7. *Se cair "mostre que V = …" do anel?* O usuário tirou o cap. 24 do escopo. A dedução de V em 3 linhas está no raio-X (caso real), para garantir. → Dúvidas da turma.
8. *0,92c.* Aí γ = 2,55: r = γmv/(eB) e T = 2πγm/(eB) (o período passa a depender de v). Abaixo de ~0,1c a correção é menor que 0,5 %. → resposta aqui; na v2 só a linha da PA9.
9. *PA8 com trechos que não apontam para C.* Contribuem: use o fio finito com sen θ (agora no Degrau 6). Teste rápido: o trecho, prolongado, passa por C? Se passa, não contribui. → Dúvidas da turma (D6).
10. *Erro de impressão na prova.* Escreva a conta e o seu valor com unidade; em questão aberta, a conta certa vale o ponto. → Dúvidas da turma.
