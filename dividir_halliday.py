#!/usr/bin/env python3
"""Divide um volume de 'Fundamentos de Fisica' (Halliday, Resnick, Walker, texto/markdown)
em arquivos por capitulo + gabarito unico.

Uso: python3 -I dividir_halliday.py <ENTRADA.md> <DIRETORIO_SAIDA>

Os arquivos de capitulo, front matter, apendices e tabelas sao copias literais de
intervalos de linhas. Apenas o gabarito.md recebe cabecalhos acrescentados.
"""
import re
import sys
import unicodedata
from pathlib import Path

src = Path(sys.argv[1])
out = Path(sys.argv[2])

if out.exists() and any(out.iterdir()):
    sys.exit(f"ERRO: {out} ja existe e nao esta vazio; nada foi escrito.")

with open(src, encoding="utf-8", newline="") as f:
    raw = f.read()
assert "\r" not in raw, "arquivo com CR; ajuste o script antes de seguir"
ends_nl = raw.endswith("\n")
lines = raw.split("\n")
if ends_nl:
    lines.pop()  # artefato do split: ultimo elemento vazio
N = len(lines)

errors, warnings = [], []


def find(pattern, start=0, end=None):
    rx = re.compile(pattern)
    for i in range(start, N if end is None else end):
        if rx.match(lines[i]):
            return i
    return None


def slug(text):
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()


def chunk_text(a, b):
    return "\n".join(lines[a:b]) + "\n"


# ---------------------------------------------------------------- fronteiras
ch_rx = re.compile(r"^\s*CAPÍTULO\s+(\d+)\s*$")  # maiusculas, linha isolada
starts = [(i, int(ch_rx.match(l).group(1))) for i, l in enumerate(lines) if ch_rx.match(l)]
if not starts:
    sys.exit("PARE: nenhum marcador 'CAPÍTULO <n>' encontrado.")
nums = [n for _, n in starts]
if nums != list(range(nums[0], nums[0] + len(nums))):
    sys.exit(f"PARE: numeros de capitulo nao consecutivos: {nums}")

last_start = starts[-1][0]
i_app = find(r"^\s*APÊNDICE\s*[A-Z]\s*$", last_start + 1)
i_resp = find(r"^\s*R\s?E\s?S\s?P\s?O\s?S\s?T\s?A\s?S\s*$", last_start + 1)
if i_app is None or i_resp is None or not (last_start < i_app < i_resp):
    sys.exit(f"PARE: marcadores inesperados (APENDICE={i_app}, RESPOSTAS={i_resp}).")
i_tail = find(r"^\s*(FÓRMULAS MATEMÁTICAS|PREFIXOS|ALGUMAS CONSTANTES)", i_resp + 1)
if i_tail is None:
    sys.exit("PARE: inicio das tabelas finais nao encontrado apos RESPOSTAS.")

ranges = [("front", None, 0, starts[0][0])]
for k, (i, n) in enumerate(starts):
    e = starts[k + 1][0] if k + 1 < len(starts) else i_app
    ranges.append(("chapter", n, i, e))
ranges += [("appendix", None, i_app, i_resp), ("answers", None, i_resp, i_tail), ("tables", None, i_tail, N)]

cursor = 0
for kind, n, s, e in ranges:
    if s != cursor or e <= s:
        sys.exit(f"PARE: intervalos nao contiguos em {kind} {n}: {s}..{e}, esperado inicio {cursor}")
    cursor = e
if cursor != N:
    sys.exit("PARE: intervalos nao chegam ao fim do arquivo")

# ---------------------------------------------------------------- titulos
titles = {}
for i, n in starts:
    j = i + 1
    while j < N and not lines[j].strip():
        j += 1
    next_line = lines[j].strip()
    m = find(rf"^{n} (.+)$", 0, starts[0][0])
    titles[n] = re.match(rf"^{n} (.+)$", lines[m]).group(1).strip() if m is not None else next_line
    if titles[n] != next_line:
        warnings.append(f"cap. {n}: titulo do sumario ({titles[n]!r}) difere da linha do capitulo ({next_line!r})")

# ---------------------------------------------------------------- escrita (copias literais)
out.mkdir(parents=True)
files = []  # (nome, ini, fim) em ordem do livro, so os literais


def write_literal(name, a, b):
    (out / name).write_text(chunk_text(a, b), encoding="utf-8", newline="")
    files.append((name, a, b))


chapter_file = {}
for kind, n, s, e in ranges:
    if kind == "front":
        write_literal("00-front-matter.md", s, e)
    elif kind == "chapter":
        chapter_file[n] = f"cap-{n:02d}-{slug(titles[n])}.md"
        write_literal(chapter_file[n], s, e)
    elif kind == "appendix":
        write_literal("apendices.md", s, e)
    elif kind == "tables":
        write_literal("tabelas-de-referencia.md", s, e)

# ---------------------------------------------------------------- gabarito
_, _, rs, re_ = next(r for r in ranges if r[0] == "answers")
ans_ch_rx = re.compile(r"^\s*Capítulo\s+(\d+)\s*$")
lab_rx = re.compile(r"^(T|P|PR)\s+\d+\.")
order = ["T", "P", "PR"]
label_title = {"T": "Testes", "P": "Perguntas (ímpares)", "PR": "Problemas (ímpares)"}

ans_ch = [(i, int(ans_ch_rx.match(lines[i]).group(1))) for i in range(rs, re_) if ans_ch_rx.match(lines[i])]
if [n for _, n in ans_ch] != nums:
    sys.exit(f"PARE: capitulos no gabarito {[n for _, n in ans_ch]} != capitulos {nums}")

gab = []  # (texto, gerado?)


def gen(t):
    gab.append((t, True))


gen("# Gabarito — Fundamentos de Física (Halliday, Resnick, Walker)")
gen("")
gen("> Reproduz **somente** o que o livro traz: respostas de todos os *Testes* e das *Perguntas* e")
gen("> *Problemas* de numeração **ímpar**. Itens pares não têm resposta no livro.")
gen("")
for k, (i, n) in enumerate(ans_ch):
    e = ans_ch[k + 1][0] if k + 1 < len(ans_ch) else re_
    gen(f"## Capítulo {n} — {titles[n]}")
    gen("")
    nxt, seen = 0, []
    for j in range(i + 1, e):
        m = lab_rx.match(lines[j])
        if m and nxt < 3 and m.group(1) == order[nxt]:  # maquina de estados T -> P -> PR
            if gab[-1][0] != "":
                gen("")
            gen(f"### {label_title[m.group(1)]}")
            gen("")
            seen.append(m.group(1))
            nxt += 1
        gab.append((lines[j], False))
    if seen != order:
        errors.append(f"gabarito cap. {n}: rotulos {seen}, esperado {order}")
    gen("")
(out / "gabarito.md").write_text("\n".join(t for t, _ in gab) + "\n", encoding="utf-8", newline="")

# ---------------------------------------------------------------- indice
idx = ["# Índice dos arquivos", "",
       "| Cap. | Título | Arquivo | Módulos | KB |", "|---|---|---|---|---|"]
for kind, n, s, e in ranges:
    if kind != "chapter":
        continue
    mods, seen_m = [], set()
    for j in range(s, e):
        m = re.match(r"^Módulo (\d+-\d+) (.+)$", lines[j])
        if m and m.group(1) not in seen_m:
            seen_m.add(m.group(1))
            mods.append(f"{m.group(1)} {m.group(2).strip()}")
    kb = (out / chapter_file[n]).stat().st_size / 1024
    idx.append(f"| {n} | {titles[n]} | `{chapter_file[n]}` | {'; '.join(mods)} | {kb:.0f} |")
idx += ["", "Outros arquivos: `00-front-matter.md`, `apendices.md`, `tabelas-de-referencia.md`, `gabarito.md`.", ""]
(out / "00-indice.md").write_text("\n".join(idx), encoding="utf-8", newline="")

# ---------------------------------------------------------------- verificacao (relendo do disco)
# 1. um arquivo por capitulo, consecutivos, cada um comeca com 'CAPÍTULO n'
for n in nums:
    first = (out / chapter_file[n]).read_text(encoding="utf-8").split("\n", 1)[0]
    if first.strip() != f"CAPÍTULO {n}":
        errors.append(f"{chapter_file[n]} comeca com {first!r}")
# 2. reconstrucao byte a byte: arquivos literais (do disco) + bloco de respostas original == entrada
lit_before = "".join((out / nm).read_text(encoding="utf-8") for nm, a, b in files if b <= rs)
lit_after = "".join((out / nm).read_text(encoding="utf-8") for nm, a, b in files if a >= re_)
rebuilt = lit_before + chunk_text(rs, re_) + lit_after
expected = "\n".join(lines) + ("\n" if ends_nl else "")
if rebuilt != expected:
    errors.append("reconstrucao byte a byte da entrada FALHOU")
if sum(b - a for _, a, b in files) + (re_ - rs) != N:
    errors.append("soma de linhas != total de linhas da entrada")
# 3. gabarito relido do disco: blocos por capitulo, T/P/PR uma vez cada, na ordem
gdisk = (out / "gabarito.md").read_text(encoding="utf-8").split("\n")
g_ch = [int(m.group(1)) for l in gdisk if (m := re.match(r"^## Capítulo (\d+) — ", l))]
if g_ch != nums:
    errors.append(f"gabarito: capitulos {g_ch} != {nums}")
g_secs = [l for l in gdisk if l.startswith("### ")]
if g_secs != [f"### {label_title[x]}" for _ in nums for x in order]:
    errors.append("gabarito: sequencia de secoes diferente de (T, P, PR) x capitulos")
# 4. sem os cabecalhos acrescentados, o conteudo == bloco de respostas da origem (ignorando vazias)
orig_body = [lines[j] for j in range(ans_ch[0][0], re_) if not ans_ch_rx.match(lines[j]) and lines[j] != ""]
gab_body = [t for t, g in gab if not g and t != ""]
if orig_body != gab_body:
    errors.append("gabarito: conteudo difere do bloco de respostas da origem")
# 5. avisos: secoes finais por capitulo
for n in nums:
    txt = (out / chapter_file[n]).read_text(encoding="utf-8").split("\n")
    for label, rx in (("Revisão e Resumo", r"^(REVISÃO E RESUMO|Revisão e Resumo)$"),
                      ("Perguntas", r"^(PERGUNTAS|Perguntas)$"),
                      ("Problemas", r"^(PROBLEMAS|Problemas)$")):
        if not any(re.match(rx, l) for l in txt):
            warnings.append(f"cap. {n}: linha '{label}' nao encontrada")

# ---------------------------------------------------------------- relatorio
print(f"entrada: {src} ({N} linhas)  ->  saida: {out}")
print(f"{'arquivo':62s} {'linhas da entrada':>19s} {'n linhas':>9s} {'KB':>6s}")
for name, a, b in files:
    kb = (out / name).stat().st_size / 1024
    print(f"{name:62s} {f'{a+1}-{b}':>19s} {b-a:>9d} {kb:>6.0f}")
print(f"{'gabarito.md  (bloco de respostas)':62s} {f'{rs+1}-{re_}':>19s} {re_-rs:>9d} {(out/'gabarito.md').stat().st_size/1024:>6.0f}")
print(f"{'00-indice.md  (gerado)':62s} {'—':>19s} {'—':>9s} {(out/'00-indice.md').stat().st_size/1024:>6.0f}")
print("\nERROS:", errors if errors else "nenhum")
print("AVISOS:", warnings if warnings else "nenhum")
sys.exit(1 if errors else 0)
