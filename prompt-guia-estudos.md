# Prompt: guia de estudos interativo (HTML) por capítulo + rodada de alunos

> Cole o bloco abaixo no Claude Code, dentro da pasta `fisica/` (a que contém `halliday-v3/`).
> Preencha só `QUESTOES`. O capítulo é perguntado na hora da execução.

---

**VARIÁVEIS**
- `CAPITULO` = *(não preencha: pergunte ao usuário no início)*
- `QUESTOES` =
  ```
  <cole aqui as questões do capítulo. Pode ser só a numeração
   (ex.: "Testes 1, 3 — Perguntas 1, 5, 9 — Problemas 3, 7, 12, 25, 41, 58")
   ou o enunciado completo.>
  ```
- `FONTE` = `halliday-v3/` (capítulos em `cap-NN-*.md`, índice em `00-indice.md`, respostas em `gabarito.md`)
- `SAIDA` = `guias/cap-NN-<slug>/` (crie; `<slug>` = nome do arquivo do capítulo sem `cap-NN-` e sem `.md`)

## Papéis

- **Você é o Professor** e o orquestrador. Roda no modelo da sessão principal (o mais forte). Faz o plano, escreve o guia, consolida as críticas e escreve a versão final.
- **4 Alunos** são subagentes em modelos mais leves (2 × `haiku`, 2 × `sonnet`), criados com a ferramenta Agent depois da versão 1. Eles estudam pelo guia, tentam resolver as questões e questionam o conteúdo e o Professor.

## Objetivo

Um guia de estudos em **um único arquivo HTML** sobre `CAPITULO`, que leve o aluno degrau por degrau (*hill climbing*: começa embaixo e sobe), do zero até conseguir resolver **sozinho** as `QUESTOES`. Sucesso não é o aluno ler a resolução; é ele conseguir fazer a próxima questão sem ela. O guia explica o porquê das coisas, não só resultados e definições, e não é denso.

## Etapa 0 — Perguntas iniciais (antes de qualquer outra coisa)

1. Leia `FONTE/00-indice.md` e pergunte ao usuário qual capítulo estudar, listando número e título. Espere a resposta.
2. Se `QUESTOES` estiver vazio, ou não bater com o capítulo escolhido, pergunte. Se vierem só números, extraia os enunciados do capítulo. Se vierem com texto, use o texto e confira com o livro.
3. **Durante todo o trabalho:** se algo ambíguo mudar o resultado (dado que só existia na figura, divergência com o gabarito, questão que não existe), pergunte ao usuário em vez de supor. Dúvida pequena: decida, registre no `plano.md` e siga.

## Etapa 1 — Ler a fonte (sabendo dos defeitos dela)

Leia o capítulo inteiro, em partes (`offset`/`limit`), e o bloco do capítulo em `gabarito.md`. O texto veio de uma conversão de PDF:
- **As figuras foram removidas.** Só sobraram as legendas (ex.: `Figura 25-18 Pergunta 1.`). Dados que estavam só no desenho não estão no texto.
- **Muitas equações em destaque sumiram** (ex.: "assume a seguinte forma:" seguido de nada). Reconstrua-as pelo seu conhecimento do Halliday e confira com o texto em volta.
- **Subscritos se soltaram em linhas próprias** (`C e C` seguido da linha `1 2` = C₁ e C₂; `V = 20,0 V` seguido da linha `s` = Vₛ).
- Nos Problemas, `·`, `··`, `···` = dificuldade. O gabarito só traz os Testes e as **ímpares** de Perguntas e Problemas.
- Não altere nada em `FONTE/`.

## Etapa 2 — Plano (projeto reverso: das questões para os degraus)

Escreva `SAIDA/plano.md` antes de qualquer HTML:
1. **Habilidades:** para cada questão, as habilidades que ela exige (ex.: "reconhecer série × paralelo num circuito desenhado", "escolher a superfície gaussiana", "resolver em símbolos antes de pôr números"). Monte a matriz questão × habilidade.
2. **Pré-requisitos** de capítulos anteriores e de matemática (vetores, derivada, integral...) que as questões usam.
3. **Degraus:** de 4 a 7, do mais concreto ao mais abstrato. Para cada um: objetivo em uma frase, habilidades que entrega, questões que desbloqueia, tempo estimado (10–15 min). Cada degrau só usa o que os anteriores ensinaram. Tópicos do capítulo que nenhuma questão usa entram como um cartão curto de "visão geral", sem aprofundar.
4. **Ordem das questões**, da mais fácil à mais difícil, presas aos degraus.
5. **Figuras:** toda figura que o guia vai ter (explicativas e das questões) e de onde vêm os dados de cada uma.
6. Decisões tomadas sem perguntar ao usuário.

## Etapa 3 — Contas

Toda conta numérica do guia (exemplos, resoluções, respostas usadas na conferência) sai de `SAIDA/calculos.py`, executado com `python3 -I`. O script imprime cada resultado ao lado da resposta do gabarito (quando existe) e marca divergência acima de 2 %. Não faça conta de cabeça.
- Questões pares não têm gabarito: o guia diz "resposta calculada pelo guia, sem gabarito oficial".
- Se o seu resultado divergir do gabarito, investigue (dado da figura? interpretação do enunciado?). Se não resolver, mostre os dois valores no guia e avise o usuário na entrega.

## Etapa 4 — Escrever `SAIDA/guia-v1.html`

### Como ensinar (técnicas com evidência: aplique, não dê palestra sobre elas)

| Técnica | Como aparece no guia |
|---|---|
| Projeto reverso e aprendizagem para o domínio (Wiggins & McTighe; Bloom) | degraus ligados às habilidades das questões; checkpoint no fim de cada degrau ("suba quando acertar 2 de 3") |
| Do concreto ao abstrato (*concreteness fading*) | cada ideia começa num fenômeno ou analogia, passa pela figura e só então chega à equação |
| Prever antes de ver (Prever–Observar–Explicar; perguntas conceituais de Mazur) | antes de cada widget ou resultado: "o que acontece se...?" com alternativas; a resposta vem depois |
| Prática de recuperação (Roediger & Karpicke) | perguntas curtas com feedback imediato, que explica por que cada alternativa errada é errada |
| Exemplos resolvidos com esmaecimento (Sweller; Renkl) | 1 exemplo completo comentado → 1 exemplo com passos faltando para o aluno completar → questão sozinho |
| Autoexplicação e interrogação elaborativa (Chi; Dunlosky et al., 2013) | dentro dos exemplos, "por que este passo?" com a resposta escondida |
| Princípios multimídia (Mayer) | figura ao lado do texto que a explica; rótulos no próprio desenho; nada decorativo; um bloco = uma ideia |
| Refutação de concepções erradas | caixa "Muita gente pensa X → na verdade é Y, porque Z" em cada degrau |
| Intercalação e espaçamento (Rohrer; Cepeda) | revisão final misturando os degraus; plano de revisão (hoje, +1, +3 e +7 dias) |
| Metacognição e calibração | antes de revelar uma resposta, o aluno marca a confiança (1–3); o guia mostra onde ele estava confiante e errou |
| Método de engenharia para resolver problemas (Pólya) | o mesmo roteiro em **todas** as resoluções: **Entender** (desenho, dados, incógnita) → **Modelar** (lei ou princípio + hipóteses) → **Resolver em símbolos** → **Calcular** (SI, algarismos significativos) → **Verificar** (unidade, ordem de grandeza, casos-limite, sinal) |

### O que cada degrau contém

1. **Por que isso existe** (2–3 linhas): que problema esse assunto resolve e onde aparece em engenharia.
2. **Intuição:** analogia de professor 10/10, caso-limite exagerado ("e se d fosse quase zero?") ou aplicação real, com figura explicativa. Toda analogia termina com **"onde a analogia quebra"**.
3. **Formalização:** a equação, com cada termo apontado na figura. A derivação fica recolhida em "ver de onde vem".
4. **Ficha de cada variável nova:** o que é, unidade, **valores típicos reais** (ordem de grandeza, de quanto a quanto), o que acontece com o todo quando ela aumenta ou diminui, armadilha comum.
5. **Widget interativo** quando houver relação entre grandezas (sliders → valores e gráfico atualizam ao vivo), sempre precedido de uma pergunta de previsão.
6. **Exemplo resolvido** → **exemplo com lacunas**.
7. **Erros comuns** (refutação).
8. **Checkpoint:** 2–3 questões de recuperação, com confiança e feedback. Use os "Testes" do livro quando servirem.
9. **Habilidades desbloqueadas:** links para as questões que o aluno já consegue fazer.
10. **Onde isso volta:** 1 linha ligando ao resto do capítulo e aos capítulos seguintes.

**Estrutura da página:** cabeçalho (capítulo, tempo total, "como usar este guia" em 3 linhas, barra de progresso) → **Degrau 0: aquecimento** (pergunta-gancho sobre um fenômeno real + teste rápido de pré-requisitos, com mini-revisão para quem errar) → **mapa da subida** (figura com degraus, conceitos e questões ligadas) → degraus → **questões** → **síntese** (fluxograma "que ferramenta uso neste problema?" + tabela de equações com quando usar e quando **não** usar) → **revisão intercalada**.

### Questões e ajuda (a ajuda só aparece se o aluno pedir)

Cada questão de `QUESTOES` é um cartão com:
- Enunciado limpo (subscritos e equações consertados), dificuldade, degraus e habilidades que usa.
- **A figura da questão reconstruída**, sempre que a original tinha figura (ver "Figuras e gráficos").
- Campo para o aluno digitar a resposta e **conferir** sem ver a resolução: o campo diz a unidade esperada; números com tolerância de 2 %; conceituais por alternativas.
- Antes da primeira dica, um lembrete do roteiro: "já desenhou? já listou dados e incógnita?".
- Botões de ajuda, **todos fechados por padrão e liberados um de cada vez, em ordem**:
  1. **Dica 1 — Onde olhar:** que princípio e qual degrau. Sem equação.
  2. **Dica 2 — Plano:** a estratégia em passos, sem números.
  3. **Dica 3 — Primeiro passo:** a montagem (equações em símbolos), sem o resultado.
  4. **Resolução comentada:** o roteiro Entender → Verificar completo, com o **porquê de cada passo**, as contas, a checagem e um "e se..." (o que muda se um dado mudar).
  5. **Resposta:** do gabarito do livro, ou "calculada pelo guia" nas pares.
- Depois da resolução: "Que passo você não teria visto sozinho?" (campo livre, salvo no navegador).
- Marque cada bloco de ajuda com `data-questao="<id>"` e `data-nivel="1"` a `"5"`, para os alunos-agente lerem um nível por vez.

Cada dica deve deixar o aluno capaz de dar o próximo passo sozinho: ensina a pensar, não entrega o resultado.

### Figuras e gráficos

- Desenhe em **SVG inline** (ou canvas via JS), em estilo de livro-texto: limpo, rótulos nos próprios elementos, os mesmos símbolos do texto.
- **Figuras explicativas:** situação física (cargas, linhas de campo, circuitos, espiras), antes/depois, analogias ilustradas, mapa da subida, fluxograma de decisão. Animação só quando o movimento é a ideia (ex.: capacitor carregando, fluxo variando).
- **Figuras das questões:** reconstrua a partir do enunciado, da legenda e do seu conhecimento da figura original do Halliday. Gráficos com eixos, unidades, escala (ex.: "escala vertical definida por dₛ = 1,00 pm") e grade suficiente para ler valores.
- A legenda sempre diz "Figura NN-XX (reconstruída)". Se um valor necessário só existia no desenho:
  1. tente deduzi-lo a partir do gabarito, e diga na legenda que fez isso;
  2. se não der, pesquise na web;
  3. se ainda não der, pergunte ao usuário.

  Nunca invente um dado em silêncio. Figura com dúvida leva o selo "⚠ reconstrução aproximada — confira no livro" e entra nas pendências da entrega.

### Escrita (não ser denso)

- Parágrafos de no máximo ~4 linhas; um bloco = uma ideia; todo termo técnico definido no primeiro uso.
- Resumo primeiro; detalhes em blocos recolhidos.
- Tom de conversa, em segunda pessoa, português do Brasil, vírgula decimal, unidades SI e a notação do livro (para o aluno conseguir voltar a ele).

### Técnica do HTML

- Um único arquivo autocontido. Única dependência externa: KaTeX com versão fixa (`cdn.jsdelivr.net/npm/katex@0.16.9`, com o `auto-render`). O resto em JS e CSS puros.
- Funciona no celular (390 px) e no computador; tema claro e escuro; imprime de forma legível.
- Progresso (degraus concluídos, checkpoints, respostas) salvo em `localStorage`, dentro de `try/catch`; a página funciona sem ele.
- Acessível: navegação por teclado, `aria-expanded` nos botões, texto alternativo nas figuras.
- Se a skill `frontend-design` estiver disponível, carregue-a antes de escrever o HTML.

### Verificação da v1 (faça e registre no fim do `plano.md`)

1. `calculos.py` roda sem erro, e as divergências com o gabarito estão explicadas.
2. Toda questão de `QUESTOES` está no guia, com os 5 níveis de ajuda e com figura quando a original tinha.
3. Abra o HTML num navegador (Playwright ou outra ferramenta de navegador, se houver): sem erros no console; toda ajuda começa fechada; os níveis abrem em ordem; os widgets respondem; o layout funciona a 390 px e a 1280 px. Salve capturas de tela de cada seção em `SAIDA/rodada-1/telas/`. Se não houver navegador disponível, diga isso na entrega.

## Etapa 5 — Rodada de alunos (crítica da v1)

Crie os 4 alunos **na mesma mensagem**, para rodarem em paralelo: ferramenta Agent, `subagent_type: general-purpose`, com o `model` da tabela. Cada um recebe: o caminho de `guia-v1.html`, os enunciados de `QUESTOES`, seu perfil e tarefa, e o formato do relatório. Só o Aluno 3 lê o capítulo do livro. Cada um salva o relatório em `SAIDA/rodada-1/aluno-N-<perfil>.md` e devolve um resumo de 5 linhas.

| Aluno | Modelo | Perfil | Tarefa |
|---|---|---|---|
| 1 — Base frágil | `haiku` | Passou raspando nas matérias anteriores; trava em matemática e em jargão. | Estuda do Degrau 0 ao fim, na ordem. Responde cada checkpoint **antes** de ver a resposta e conta o que errou e por quê. Marca todo salto lógico, termo não definido, "por quê?" sem resposta e lugar onde se perdeu, citando a frase exata. |
| 2 — Resolvedor (prova amanhã) | `haiku` | Quer resolver as questões e lê o mínimo. | Em cada questão, na ordem: tenta sozinho; depois lê a ajuda **um nível por vez** (`data-nivel`) e anota em que nível destravou. Para cada passo que deu, cita a parte do guia que o ensinou; se precisou de algo que o guia não ensina, marca **LACUNA**. Aponta dicas que entregaram demais ou de menos e confere a resposta final. Se leu a resolução antes de tentar, diz. |
| 3 — Monitor cético | `sonnet` | O aluno que corrige o professor. Pode ler o capítulo e o gabarito. | Confere física, sinais, unidades e contas (refaz em Python); acha simplificações que vão causar erro mais tarde; testa os limites das analogias; compara cada figura reconstruída com o enunciado. Faz perguntas "e se...?" difíceis ao Professor. |
| 4 — Visual e prático | `sonnet` | Aprende vendo; futuro engenheiro. | Avalia cada figura, gráfico e widget: ensina ou só enfeita? Eixos, unidades e escalas batem com o enunciado? Onde o texto ficou denso e uma figura resolveria? Lê as capturas de `rodada-1/telas/`, se houver. Cobra aplicações reais e ordens de grandeza. |

**Instrução comum aos alunos:** "Você é um aluno, não um revisor educado. Não finja que entendeu. Crítica vaga ('poderia ser mais claro') não vale: diga onde e por quê."

**Formato do relatório (todos):**
1. **Itens de crítica**, em tabela: local (degrau, questão ou id) · tipo (erro físico · salto lógico · termo não definido · denso demais · figura confusa · dica fraca · dica entrega demais · falta prática · outro) · gravidade (**bloqueia** = não consegui seguir · **atrapalha** · **polimento**) · evidência (frase citada ou passo em que travou) · sugestão.
2. **Perguntas ao Professor:** no mínimo 3, na voz do aluno ("Professor, por que...?"), sobre o conteúdo ou sobre as escolhas do Professor.
3. **Placar** (Alunos 1 e 2): checkpoints acertados; questões resolvidas sem ajuda, com ajuda até o nível N, ou não resolvidas.
4. **O que funcionou** (para não ser removido na v2).

## Etapa 6 — Consolidação e respostas do Professor

Escreva `SAIDA/rodada-1/consolidacao.md`:
1. **Tabela única** de todos os itens (junte duplicatas e anote quantos alunos levantaram cada um): problema · alunos · gravidade · **decisão** (aceito ou rejeitado, com justificativa) · o que muda na v2.
   - Prioridade: o que **bloqueia** a resolução de questões > erros físicos > o que vários alunos apontaram > o resto.
   - Rejeite, explicando, a crítica que contradiz a física ou que deixaria o guia mais denso sem ganho de aprendizado.
2. **Respostas do Professor** a cada pergunta dos alunos. As que revelam uma dúvida que um aluno real também teria vão para a seção "Dúvidas da turma" da v2.

## Etapa 7 — `SAIDA/guia-v2.html` (versão final)

- Reescreva (não remende) as seções com itens que bloqueiam ou atrapalham; mantenha o que os alunos disseram que funcionou.
- Acrescente a seção **"Dúvidas da turma"**: as perguntas dos alunos e as respostas do Professor, cada uma ligada ao degrau certo.
- Recalcule em `calculos.py` tudo o que mudou e repita a verificação da Etapa 4.
- Não apague a v1.

## Etapa 8 — Reteste

Volte aos Alunos 1 e 2 (retome o mesmo agente com SendMessage; se não der, crie um novo com o mesmo perfil e modelo) e peça que refaçam, **na v2**, só os pontos em que travaram. Salve em `SAIDA/rodada-2/reteste.md`. Se algo ainda bloquear, corrija a v2 e reteste esse ponto mais uma vez, no máximo. Se continuar falhando, liste como pendência.

## Entrega

Ao terminar, mostre:
- o caminho de `guia-v2.html` (para abrir: `xdg-open <caminho>`);
- os degraus: título, tempo e questões que cada um desbloqueia;
- o placar dos Alunos 1 e 2 na v1 e no reteste;
- as 5 maiores mudanças da v1 para a v2 e qual aluno motivou cada uma;
- **pendências:** figuras com "⚠ reconstrução aproximada", divergências com o gabarito e o que não deu para verificar no navegador.

Não diga que terminou sem ter feito as verificações. Se pulou alguma, diga qual e por quê.
