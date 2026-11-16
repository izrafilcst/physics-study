# Prompt: dividir o Halliday em capítulos + gabarito

> Cole o bloco abaixo no Claude Code, dentro da pasta onde está o arquivo.
> Ajuste só as duas variáveis do início.

---

**VARIÁVEIS**
- `ENTRADA` = `haliday.md`
- `SAIDA` = `halliday-v3`   (diretório a criar, ao lado do arquivo de entrada)

## Objetivo

`ENTRADA` é um volume do livro *Fundamentos de Física* (Halliday, Resnick, Walker) convertido para texto. Ele tem ~1,4 MB, grande demais para carregar inteiro. Divida-o em arquivos menores, para que depois eu possa pedir material de estudo de um assunto específico carregando só o capítulo necessário e o gabarito.

## Regra de execução (obrigatória)

**Não leia o arquivo inteiro e não reescreva o conteúdo você mesmo.** Escreva um script Python, salve-o ao lado de `ENTRADA` como `dividir_halliday.py` e execute-o com `python3 -I`. Para entender o formato, leia apenas trechos pequenos (`offset`/`limit`) ou use `grep -n`. Toda a divisão deve ser por **intervalos de linhas copiados literalmente**.

## O que gerar em `SAIDA/`

```
00-indice.md                 tabela: cap. | título | arquivo | módulos | KB
00-front-matter.md           tudo antes do primeiro capítulo (créditos, sumário, prefácio)
cap-NN-<titulo-sem-acentos>.md   UM POR CAPÍTULO, texto na íntegra
apendices.md                 Apêndices A–G
tabelas-de-referencia.md     tabelas que sobram depois do gabarito (fórmulas, prefixos SI, constantes, conversões)
gabarito.md                  gabarito de TODOS os capítulos, num único arquivo
```

Cada `cap-NN-*.md` contém o capítulo inteiro, sem cortar nada: módulos, objetivos, texto, Exemplos, Testes, Táticas, Revisão e Resumo, Perguntas, Problemas, e também as notas de rodapé do fim do capítulo (o bloco depois de `_______________`). **Não resuma, não traduza, não corrija, não reformate e não apague linhas.** Os arquivos de capítulo, front matter, apêndices e tabelas são cópias literais; não acrescente cabeçalhos a eles.

## Como achar as fronteiras (já validado neste arquivo)

Procure os marcadores **na ordem abaixo**. Vários textos aparecem também no sumário, no começo, ou dentro de frases, então respeite as restrições.

1. **Início de capítulo:** linha que é *somente* `CAPÍTULO <n>` em **maiúsculas** (regex `^\s*CAPÍTULO\s+(\d+)\s*$`, sem ignorar caixa). `Capítulo 25` em minúsculas dentro de frases, e `Capítulo N` no gabarito, **não** contam. Os números devem ser consecutivos (aqui: 21 a 32). Se não forem, pare e me avise.
2. **Fim do último capítulo:** a primeira linha `APÊNDICE <letra>` depois do último início de capítulo. Entre a palavra e a letra pode haver tabs (regex `^\s*APÊNDICE\s*[A-Z]\s*$`). Procure só *depois* do último capítulo, porque `APÊNDICES` e `RESPOSTAS` também aparecem no sumário.
3. **Título do capítulo:** pegue da lista "SUMÁRIO GERAL" do começo (linha `<n> <Título>`). Se não achar, use a linha seguinte ao marcador.
4. **Apêndices:** do primeiro `APÊNDICE` até a linha `R E S P O S T A S` (letras separadas por espaço).
5. **Respostas (gabarito):** da linha `R E S P O S T A S` até a primeira linha que começa o bloco de tabelas finais: `FÓRMULAS MATEMÁTICAS`, `PREFIXOS DO SI` ou `ALGUMAS CONSTANTES FÍSICAS`. Procure **só depois** de `R E S P O S T A S`, porque `FÓRMULAS MATEMÁTICAS` também aparece dentro do Apêndice E.
6. **Tabelas de referência:** dessa linha até o fim do arquivo.

Os intervalos devem ser contíguos e cobrir o arquivo de ponta a ponta, na ordem: front matter, capítulos, apêndices, respostas, tabelas.

## Como montar o `gabarito.md`

O bloco de respostas é organizado por capítulo: uma linha `Capítulo <n>` e, em seguida, três parágrafos rotulados:
`T` (Testes), `P` (Perguntas ímpares) e `PR` (Problemas ímpares).

- **Escopo:** inclua **somente** o que o livro traz. Itens pares não têm resposta no livro. **Não resolva, não invente e não complete nada.**
- Copie as linhas das respostas **literalmente**, na ordem original, e acrescente apenas estes cabeçalhos:
  - no topo do arquivo: `# Gabarito — Fundamentos de Física (Halliday, Resnick, Walker)` e uma nota dizendo que o arquivo traz só as respostas dos Testes e das Perguntas e Problemas ímpares, e que os pares não têm resposta no livro;
  - por capítulo: `## Capítulo <n> — <título>`;
  - antes de cada bloco: `### Testes`, `### Perguntas (ímpares)`, `### Problemas (ímpares)`.
- **Não quebre as respostas item a item.** Mantenha os parágrafos como o livro os traz.
- **Armadilha conhecida:** um rótulo só vale se for o **próximo da sequência** `T → P → PR` dentro do capítulo. Uma linha quebrada pode começar com `T 9. (a) 5,01 × 10–22 T`, em que o `T` é a unidade tesla, e não o rótulo de Testes. Implemente como uma máquina de estados: depois que `PR` começou, nenhum `T` ou `P` abre um novo bloco.

## Verificação (rode e mostre o resultado; não declare sucesso sem isto)

Erros, se qualquer um falhar:
1. Existe exatamente um arquivo por capítulo, com a numeração consecutiva, e cada um começa com a linha `CAPÍTULO <n>`.
2. Os intervalos são contíguos, sem lacuna nem sobreposição, e a soma das linhas copiadas é igual ao total de linhas de `ENTRADA`.
3. No `gabarito.md` há um bloco por capítulo, na mesma ordem dos capítulos, com `T`, `P` e `PR` exatamente uma vez cada, nessa ordem.
4. Se você removesse os cabeçalhos que acrescentou, o conteúdo do `gabarito.md` seria idêntico ao bloco de respostas da origem (ignorando linhas vazias).

Avisos (relate, mas não pare):
5. Cada capítulo deveria conter as linhas `Revisão e Resumo`, `Perguntas` e `Problemas`. **Neste arquivo, o cap. 31 não tem a linha do título "Revisão e Resumo"** (o texto do resumo está lá, só o título se perdeu). Isso é do arquivo de origem; não tente consertar.

Se algum marcador do passo "fronteiras" não for encontrado ou der um resultado inesperado, **pare e me diga o que viu**; não improvise.

## Restrições

- Não altere `ENTRADA`.
- O arquivo não tem imagens. Mantenha referências como "Fig. 22-30" exatamente como estão; não tente descrever ou recriar figuras.
- Não crie nenhum arquivo além dos listados e do script `dividir_halliday.py`.

## Entrega

Ao terminar, mostre uma tabela com arquivo, intervalo de linhas de `ENTRADA`, nº de linhas e KB, o resultado de cada verificação (erros e avisos) e o caminho do script.
