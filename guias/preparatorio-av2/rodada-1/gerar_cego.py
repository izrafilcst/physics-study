"""Gera a cópia "cega" do guia para os alunos-agente.

Versão do preparatório Av2: os <details class="correcao-sim"> (correções do simulado) e
<details class="usa"> (ideias da questão) vão para recolhido/NN.md, fora do texto.

Uso:  python3 -I gerar_cego.py <guia.html> <pasta-de-saida>

Saída:
  guia-cego.md            o que a página mostra, na ordem, sem respostas, sem
                          feedback e sem os níveis de ajuda
  ajuda/<Q>-<n>.md        cada nível de ajuda de cada questão, um arquivo por nível
  conferir/<id>.md        a resposta e o feedback de cada pergunta ou campo
                          (equivale a clicar em "Conferir" na página)

Assim o aluno-agente lê como um aluno real: responde, depois abre a conferência;
pede a ajuda um nível por vez.
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

VAZIOS = {'meta', 'link', 'input', 'br', 'img', 'hr', 'source', 'wbr'}
BLOCOS = {'p', 'div', 'section', 'article', 'header', 'main', 'nav', 'figure', 'figcaption',
          'ul', 'ol', 'li', 'table', 'tr', 'h1', 'h2', 'h3', 'h4', 'details', 'summary', 'label', 'thead', 'tbody'}


class No:
    def __init__(self, tag, attrs, pai=None):
        self.tag, self.attrs, self.pai, self.filhos = tag, dict(attrs), pai, []

    def cls(self):
        return self.attrs.get('class', '') or ''

    def tem(self, c):
        return c in self.cls().split()


class Arvore(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.raiz = No('raiz', {})
        self.atual = self.raiz

    def handle_starttag(self, tag, attrs):
        n = No(tag, attrs, self.atual)
        self.atual.filhos.append(n)
        if tag not in VAZIOS:
            self.atual = n

    def handle_startendtag(self, tag, attrs):
        self.atual.filhos.append(No(tag, attrs, self.atual))

    def handle_endtag(self, tag):
        n = self.atual
        while n is not self.raiz and n.tag != tag:
            n = n.pai
        if n is not self.raiz:
            self.atual = n.pai

    def handle_data(self, d):
        self.atual.filhos.append(d)


def texto(n):
    """Texto inline de um nó (sem SVG, sem ocultos)."""
    if isinstance(n, str):
        return n
    if n.tag in ('script', 'style', 'svg'):
        return ''
    if 'hidden' in n.attrs or 'data-oculto' in n.attrs:
        return ''
    return ''.join(texto(f) for f in n.filhos)


def limpa(s):
    return re.sub(r'\s+', ' ', s).strip()


class Cego:
    def __init__(self, saida):
        self.saida = saida
        self.linhas = []
        os.makedirs(os.path.join(saida, 'ajuda'), exist_ok=True)
        os.makedirs(os.path.join(saida, 'conferir'), exist_ok=True)

    def out(self, s=''):
        self.linhas.append(s)

    def grava(self, rel, conteudo):
        with open(os.path.join(self.saida, rel), 'w') as f:
            f.write(conteudo.strip() + '\n')

    # ---------- componentes ----------
    def quiz(self, n):
        qid = n.attrs.get('id', '?')
        tipo = n.attrs.get('data-tipo')
        enun = [f for f in n.filhos if not isinstance(f, str) and f.tem('enun')]
        self.out('')
        self.out(f'**[PERGUNTA {qid}]** ' + (limpa(texto(enun[0])) if enun else ''))
        alts = []
        self._busca(n, lambda x: x.tem('alt'), alts)
        letras = 'abcdefg'
        conf = [f'# Conferência de {qid}', '']
        mini = []
        self._busca(n, lambda x: x.tem('mini'), mini)
        for k, a in enumerate(alts):
            t = limpa(texto(a))
            self.out(f'   {letras[k]}) {t}')
            ok = a.attrs.get('data-ok') == '1'
            fb = a.attrs.get('data-fb', '')
            conf.append(f'- {letras[k]}) {"**CERTA**" if ok else "errada"} — {fb}')
        if tipo == 'palpite':
            self.out('   (Palpite: não há resposta certa agora; anote o seu. A resposta vem na questão PA9 (Degrau 6).)')
            return
        conf_req = n.attrs.get('data-conf') == '1'
        if n.attrs.get('data-prever'):
            self.out(f'   (Previsão antes do widget {n.attrs["data-prever"]}. Responda, depois abra conferir/{qid}.md.)')
        else:
            self.out(f'   → Escolha {"e marque a confiança (1 chute, 2 acho, 3 certeza) " if conf_req else ""}ANTES de abrir `conferir/{qid}.md`.')
        for m in mini:
            conf.append('')
            conf.append('Mini-revisão (aparece na página para quem erra): ' + limpa(''.join(texto(f) if not isinstance(f, str) else f for f in m.filhos)))
        self.grava(f'conferir/{qid}.md', '\n'.join(conf))

    def num(self, n):
        qid = n.attrs.get('id', '?')
        rot = n.attrs.get('data-rot', 'Resposta:')
        unid = n.attrs.get('data-unid', '')
        self.out('')
        self.out(f'**[CAMPO {qid}]** {rot} ______ {unid}')
        extra = []
        if n.attrs.get('data-lacuna'):
            extra.append('lacuna de exemplo: se errar, a página oferece "Mostrar a resposta"')
        if n.attrs.get('data-conf') == '1':
            extra.append('marque a confiança 1–3')
        self.out(f'   → Escreva seu valor{" (" + "; ".join(extra) + ")" if extra else ""} ANTES de abrir `conferir/{qid}.md`. A página aceita 2 % de tolerância.')
        conf = [f'# Conferência de {qid}', '', f'Campo: {rot} [{unid}]', '']
        resp = n.attrs.get('data-resp')
        conf.append(f'Valor esperado: {resp} {unid}' + ('  (ângulo: vale qualquer equivalente mod 360°, ±1,5°)' if n.attrs.get('data-ang') else ''))
        if n.attrs.get('data-abs'):
            conf.append(f'Tolerância absoluta: ±{n.attrs["data-abs"]}')
        if n.attrs.get('data-sinal'):
            conf.append('O sinal faz parte da resposta.')
        if n.attrs.get('data-mostra'):
            conf.append('Texto mostrado ao acertar: ' + n.attrs['data-mostra'])
        try:
            erros = json.loads(n.attrs.get('data-erros', '[]'))
        except Exception:
            erros = []
        if erros:
            conf.append('')
            conf.append('Erros comuns que a página reconhece (valor → mensagem):')
            for v, msg in erros:
                conf.append(f'- {v} → {msg}')
        depois = []
        self._busca(n, lambda x: 'data-oculto' in x.attrs, depois)
        for d in depois:
            conf.append('Mostrado depois de acertar: ' + limpa(''.join(f if isinstance(f, str) else texto(f) for f in d.filhos)))
        self.grava(f'conferir/{qid}.md', '\n'.join(conf))

    def widget(self, n):
        h = []
        self._busca(n, lambda x: x.tag == 'h4', h)
        svg = []
        self._busca(n, lambda x: x.tag == 'svg', svg)
        labels = []
        self._busca(n, lambda x: x.tag == 'label' or x.tem('seg'), labels)
        self.out('')
        self.out(f'[WIDGET INTERATIVO — {limpa(texto(h[0])) if h else ""}] ' + (svg[0].attrs.get('aria-label', '') if svg else ''))
        self.out('   Controles: ' + '; '.join(limpa(texto(l)) for l in labels if limpa(texto(l))))
        self.out('   (Você não consegue mexer nele aqui. Na página, ele fica borrado até a previsão ser respondida; as capturas de tela estão em rodada-1/telas/.)')

    def ajuda(self, n):
        q = n.attrs.get('data-q')
        niveis = []
        self._busca(n, lambda x: x.tem('nivel'), niveis)
        rot = [f for f in n.filhos if not isinstance(f, str) and f.tem('roteiro')]
        if rot:
            self.out('')
            self.out('> ' + limpa(texto(rot[0])))
        nomes = []
        for k, sec in enumerate(niveis, 1):
            titulo = sec.attrs.get('data-titulo', f'Nível {k}')
            nomes.append(f'`ajuda/{q}-{k}.md` ({titulo})')
            sub = Cego.__new__(Cego)
            sub.saida, sub.linhas = self.saida, []
            for f in sec.filhos:
                sub.bloco(f, 0)
            self.grava(f'ajuda/{q}-{k}.md', f'# {q}, nível {k}: {titulo}\n\n' + '\n'.join(sub.linhas))
        self.out('')
        self.out(f'**[AJUDA de {q}]** Na página, os botões abrem um nível por vez, em ordem. Leia só o próximo quando precisar: ' + ', '.join(nomes) + '.')

    # ---------- percurso ----------
    def _busca(self, n, pred, acc):
        for f in n.filhos:
            if isinstance(f, str):
                continue
            if pred(f):
                acc.append(f)
            else:
                self._busca(f, pred, acc)

    def _tem_bloco(self, n):
        for f in n.filhos:
            if isinstance(f, str):
                continue
            if f.tag in BLOCOS or f.tag == 'svg' or f.tem('quiz') or f.tem('num') or f.tem('widget') or f.tem('ajuda') or self._tem_bloco(f):
                return True
        return False

    def bloco(self, n, nivel):
        if isinstance(n, str):
            t = limpa(n)
            if t:
                self.out(t)
            return
        if n.tag in ('script', 'style', 'head'):
            return
        if 'hidden' in n.attrs or 'data-oculto' in n.attrs:
            return
        if n.tem('quiz'):
            return self.quiz(n)
        if n.tag == 'div' and n.tem('num'):
            return self.num(n)
        if n.tem('widget'):
            return self.widget(n)
        if n.tem('ajuda'):
            return self.ajuda(n)
        if n.tem('sem-katex') or n.tem('legenda-cores') or n.tem('progresso') or n.tem('btn-tema'):
            return
        if n.tag == 'svg':
            if n.attrs.get('aria-hidden') == 'true':
                return
            self.out('')
            self.out('[FIGURA: ' + n.attrs.get('aria-label', '(sem descrição)') + ']')
            return
        if n.tag in ('h1', 'h2', 'h3', 'h4'):
            self.out('')
            self.out('#' * int(n.tag[1]) + ' ' + limpa(texto(n)))
            return
        if n.tag == 'details' and (n.tem('correcao-sim') or n.tem('usa')):
            summ = [f for f in n.filhos if not isinstance(f, str) and f.tag == 'summary']
            sub = [limpa(texto(f)) if not isinstance(f, str) else limpa(f) for f in n.filhos if isinstance(f, str) or f.tag != 'summary']
            self.nrec = getattr(self, 'nrec', 0) + 1
            rel = f'recolhido/{self.nrec:02d}.md'
            os.makedirs(os.path.join(self.saida, 'recolhido'), exist_ok=True)
            self.grava(rel, '# ' + (limpa(texto(summ[0])) if summ else '') + '\n\n' + limpa(' '.join(sub)) + '\n')
            self.out('')
            self.out(f'▸ [recolhido, abre ao clicar] {limpa(texto(summ[0])) if summ else ""} → conteúdo em `{rel}` (abra só quando a página deixaria: depois de tentar)')
            return
        if n.tag == 'details':
            summ = [f for f in n.filhos if not isinstance(f, str) and f.tag == 'summary']
            self.out('')
            self.out(f'▸ [recolhido, abre ao clicar] {limpa(texto(summ[0])) if summ else ""}')
            sub = []
            for f in n.filhos:
                if isinstance(f, str) or f.tag != 'summary':
                    sub.append(limpa(texto(f)) if not isinstance(f, str) else limpa(f))
            conteudo = limpa(' '.join(sub))
            if conteudo:
                self.out('   ' + conteudo)
            return
        if n.tag == 'tr':
            cels = [limpa(texto(c)) for c in n.filhos if not isinstance(c, str) and c.tag in ('td', 'th')]
            self.out('| ' + ' | '.join(cels) + ' |')
            return
        if n.tag in ('p', 'figcaption', 'summary', 'label'):
            t = limpa(texto(n))
            # parágrafos que contêm componentes (raro) caem no percurso normal
            if t:
                self.out('')
                self.out(t)
            return
        if n.tag == 'li':
            # li pode ter blocos dentro (fluxograma)
            if any(not isinstance(f, str) and f.tag in ('p', 'div', 'ul', 'ol') for f in n.filhos):
                self.out('')
                self.out('- ' + limpa(texto(n)))
            else:
                self.out('- ' + limpa(texto(n)))
            return
        if n.tag == 'li' and n.pai is not None and n.pai.tem('escada'):
            return
        if n.tem('escada'):
            for li in [x for x in n.filhos if not isinstance(x, str)]:
                nome = []
                self._busca(li, lambda x: x.tem('nome'), nome)
                chips = []
                self._busca(li, lambda x: x.tem('chip-q'), chips)
                self.out(f'- Degrau {li.attrs.get("data-deg", "")[1:]}: {limpa(texto(nome[0])) if nome else ""}'
                         + (' (destrava ' + ', '.join(limpa(texto(c)) for c in chips) + ')' if chips else ''))
            return
        if not self._tem_bloco(n):
            t = limpa(texto(n))
            if t:
                self.out(t)
            return
        for f in n.filhos:
            self.bloco(f, nivel + 1)


def main():
    guia, saida = sys.argv[1], sys.argv[2]
    arv = Arvore()
    arv.feed(open(guia, encoding='utf-8').read())
    c = Cego(saida)
    corpo = [f for f in arv.raiz.filhos if not isinstance(f, str)]
    for f in corpo:
        c.bloco(f, 0)
    txt = '\n'.join(c.linhas)
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    cab = ('# Guia (cópia cega para alunos-agente)\n\n'
           'Este arquivo é o texto que a página mostra, na mesma ordem. As figuras aparecem como [FIGURA: descrição];'
           ' as capturas de tela estão em `rodada-1/telas/`. Perguntas e campos de resposta estão marcados;'
           ' a conferência de cada um está em `conferir/<id>.md`, e a ajuda das questões em `ajuda/<Q>-<n>.md`.\n')
    with open(os.path.join(saida, 'guia-cego.md'), 'w') as f:
        f.write(cab + '\n' + txt.strip() + '\n')
    print('linhas:', txt.count('\n'), '| conferir:', len(os.listdir(os.path.join(saida, 'conferir'))),
          '| ajuda:', len(os.listdir(os.path.join(saida, 'ajuda'))))


if __name__ == '__main__':
    main()
