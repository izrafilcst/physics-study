import sys, json, re, collections
from html.parser import HTMLParser
src = open(sys.argv[1], encoding='utf-8').read()
ATTR_OK = re.compile(r'^(data-[a-z-]+|id|class|type|href|src|style|role|aria-[a-z]+|viewbox|points|d|x|y|x1|x2|y1|y2|cx|cy|r|rx|ry|width|height|for|hidden|lang|charset|name|content|rel|crossorigin|defer|onload|min|max|step|value|refx|refy|markerunits|markerwidth|markerheight|orient|focusable|transform|font-weight|text-anchor|inputmode|autocomplete|spellcheck|open|colspan)$')
ids = collections.Counter(); bad = []; posicoes = collections.Counter(); quizzes = []
class P(HTMLParser):
    def __init__(s): super().__init__(); s.cur = None
    def handle_starttag(s, tag, attrs):
        d = dict(attrs)
        for k, v in attrs:
            if not ATTR_OK.match(k): bad.append((s.getpos(), tag, k))
        if 'id' in d: ids[d['id']] += 1
        if 'data-erros' in d:
            try: json.loads(d['data-erros'])
            except Exception as e: bad.append((s.getpos(), 'JSON', d.get('id'), str(e)))
        if 'class' in d and 'quiz' in d['class'].split():
            s.cur = None
            if d.get('data-tipo') != 'palpite':
                s.cur = [d.get('id'), []]; quizzes.append(s.cur)
        if tag == 'button' and 'class' in d and 'alt' in d['class'].split() and s.cur is not None:
            s.cur[1].append(d.get('data-ok') == '1')
P().feed(src)
print('atributos suspeitos:', bad[:20])
print('ids repetidos:', [k for k, v in ids.items() if v > 1])
for qid, alts in quizzes:
    if alts.count(True) != 1: print('quiz sem exatamente 1 certa:', qid, alts)
    elif len(alts) >= 3: posicoes['abcdefg'[alts.index(True)]] += 1
print('posição da certa (quizzes com 3+ alternativas):', dict(sorted(posicoes.items())))
print('níveis por questão:', dict(collections.Counter(re.findall(r'data-questao="(P\d+)" data-nivel', src))))
hrefs = set(re.findall(r'href="#([\w-]+)"', src)); faltam = [h for h in hrefs if h not in ids and h not in ('qp','qn','qp-p','qn-p','pt')]
print('links internos sem alvo:', faltam)
print('tamanho:', len(src), 'bytes')
