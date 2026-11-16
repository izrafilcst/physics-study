"""v2, parte E: correções não bloqueantes apontadas no reteste (rodada 2)."""
import sys

ARQ = '/home/swampert/Documents/fisica/guias/cap-22-campos-eletricos/guia-v2.html'
s = open(ARQ, encoding='utf-8').read()
erros = []


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        erros.append(f'[{c}x, esperado {n}] {old[:90]!r}')
        return
    s = s.replace(old, new)


# 1. a regra "|q|/r²" vinha antes da previsão do W2 e a respondia (Aluno 1)
rep('\n      <p>Quem ganha não é a carga maior: é a de maior <b>|q|/r²</b>.</p>', '')
# 2. "derivada" sem definição (Aluno 1)
rep('<dd>A derivada de sen θ é cos θ, então a primitiva de cos θ é sen θ:',
    '<dd>A derivada (Cálculo 1) mede quanto uma função muda por unidade de θ; a derivada de sen θ é cos θ. Então a primitiva de cos θ é sen θ:')
# 3. ordem das cargas na Pergunta 4 (Aluno 1)
rep('aria-label="Pergunta 4 do livro: quatro sistemas numa reta, com o ponto central marcado e cargas a d e 2d de cada lado. Sistema 1: +e, −e, −e, +e.',
    'aria-label="Pergunta 4 do livro: quatro sistemas numa reta, com o ponto central marcado entre a 2ª e a 3ª carga e cargas a d e 2d de cada lado. Cargas listadas da esquerda para a direita. Sistema 1: +e, −e, −e, +e.')
# 4. P31: o enunciado ainda dizia "a = 50 m" (Aluno 2)
rep('Determine o módulo do campo elétrico produzido em um ponto situado no eixo x, a uma distância a = 50 m do centro da barra,',
    'Determine o módulo do campo elétrico produzido em um ponto situado no eixo x, a uma distância D = 50 m do centro da barra,')
rep('<p class="pequeno">Atenção: nos itens (d) e (e) o livro reusa a letra a para outra distância (50 m, medida do <b>centro</b> da barra). Neste guia ela se chama D.</p>',
    '<p class="pequeno">Atenção: nos itens (d) e (e) o livro reusa a letra a para essa distância de 50 m, medida do <b>centro</b> da barra. Neste guia ela se chama D, para não confundir com o a = 12,0 cm dos itens (b) e (c).</p>')
# 5. dica para o desafio do P15 (Aluno 2)
rep('<div class="num" id="P15-des-a" data-lacuna="1"',
    '<details><summary>Dica do desafio</summary><p>As três cargas estão à mesma distância a/√2 de P, e cada campo aponta ao longo de uma diagonal. Calcule o módulo de cada um (o de uma carga e vale 80 N/C; o de 2e, 160 N/C), decomponha cada um em x e y (cada componente é o módulo dividido por √2, com o sinal do desenho) e some.</p></details>\n        <div class="num" id="P15-des-a" data-lacuna="1"')

open(ARQ, 'w', encoding='utf-8').write(s)
print('erros:' if erros else 'ok, sem erros')
for e in erros:
    print(' ', e)
sys.exit(1 if erros else 0)
