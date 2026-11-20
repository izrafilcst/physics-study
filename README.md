# physics-study

Guias de estudo interativos do *Fundamentos de Física*, vol. 3 (Halliday, Resnick, Walker), um por capítulo. Cada guia é **um único arquivo HTML**: abre em qualquer navegador e não precisa instalar nada.

## Guias disponíveis

| Capítulo | Abra este arquivo | Questões | Situação |
|---|---|---|---|
| 21. A Lei de Coulomb | [`guias/cap-21-a-lei-de-coulomb/guia-v2.html`](guias/cap-21-a-lei-de-coulomb/guia-v2.html) | Problemas 7, 10, 21, 23, 42, 50 e 73 | pronto (versão final) |
| 22. Campos Elétricos | [`guias/cap-22-campos-eletricos/guia-v1.html`](guias/cap-22-campos-eletricos/guia-v1.html) | Problemas 8, 9, 15, 26, 29, 31, 38 e 81 | em andamento (só a v1) |
| 23. Lei de Gauss | [`guias/cap-23-lei-de-gauss/guia-v2.html`](guias/cap-23-lei-de-gauss/guia-v2.html) | Problemas 5, 24, 29, 39, 52, 53 e 76 | pronto (versão final) |

Em cada capítulo, abra a **maior versão** que existir (`guia-v2.html` é a final; a `guia-v1.html` é a de antes da revisão).

## Como abrir no computador

**Pelo terminal** (dentro da pasta `fisica`):

```bash
xdg-open guias/cap-21-a-lei-de-coulomb/guia-v2.html
```

**Pelo gerenciador de arquivos:** entre na pasta do capítulo e dê dois cliques em `guia-v2.html`. Se abrir num editor de texto em vez do navegador, clique com o botão direito → *Abrir com* → Firefox ou Chrome. Também dá para arrastar o arquivo para uma janela do navegador.

> Na primeira vez, **precisa de internet**: as fórmulas são desenhadas pela biblioteca KaTeX, que vem da rede. Sem internet, elas aparecem como texto entre `$...$` e o guia mostra um aviso no topo. O resto (texto, figuras, simuladores, checkpoints) funciona offline.

## Como abrir no celular

O jeito mais simples é servir a pasta pela rede de casa. O computador e o celular precisam estar **no mesmo Wi-Fi**.

1. No computador, dentro da pasta `fisica`:
   ```bash
   python3 -m http.server 8000 --directory guias
   ```
2. Descubra o IP do computador (em outro terminal):
   ```bash
   hostname -I
   ```
   Use o primeiro número, algo como `192.168.0.15`.
3. No navegador do celular, abra:
   ```
   http://192.168.0.15:8000/cap-21-a-lei-de-coulomb/guia-v2.html
   ```
   trocando `192.168.0.15` pelo seu IP.
4. Quando terminar, volte ao terminal do passo 1 e aperte `Ctrl+C`.

Se o celular não conectar, provavelmente o firewall do computador bloqueia a porta 8000. Com o `ufw`, libere com `sudo ufw allow 8000/tcp`.

Outra opção é copiar o arquivo `guia-v2.html` para o celular (ele é autocontido) e abri-lo num navegador. Se a parte interativa não funcionar desse jeito, use o servidor acima.

## Seu progresso

- O guia lembra o que você fez (degraus concluídos, respostas, dicas abertas, anotações) **no navegador e no aparelho em que você estudou**. Em outro navegador, outro aparelho ou numa aba anônima, ele começa do zero.
- Limpar os dados de navegação apaga o progresso.
- Para recomeçar de propósito, use o botão **Apagar meu progresso**, no fim da página.

## Como usar o guia

1. Suba um degrau por vez. Cada um termina num checkpoint: acertou 2 de 3 de primeira, pode subir.
2. Antes de cada resultado, o guia pede um palpite. Chute antes de ver: palpite errado também ensina.
3. Nas questões, resolva no papel e confira a resposta no campo. As ajudas abrem uma de cada vez, só quando você pede, da Dica 1 até a resolução comentada.

O topo da página tem um "altímetro" com o seu progresso e um mapa da subida com as questões que cada degrau destrava.

## O que tem na pasta de cada capítulo

| Arquivo | O que é |
|---|---|
| `guia-v2.html` | o guia final, para estudar |
| `guia-v1.html` | a primeira versão, antes da revisão pelos alunos-teste |
| `plano.md` | o plano do guia: habilidades por questão, degraus, figuras, decisões e verificações |
| `calculos.py` | todas as contas do guia, conferidas com o gabarito do livro; rode com `python3 -I calculos.py` |
| `rodada-1/` | relatórios dos quatro alunos-teste, a consolidação das críticas e as capturas de tela |
| `rodada-2/` | o reteste da versão final |

## Como gerar o guia de outro capítulo

Abra o Claude Code dentro desta pasta (`fisica`) e cole o conteúdo de [`prompt-guia-estudos.md`](prompt-guia-estudos.md). Ele pergunta o capítulo e as questões, e cria a pasta `guias/cap-NN-.../`. Depois, acrescente a linha do capítulo novo na tabela "Guias disponíveis" acima.
