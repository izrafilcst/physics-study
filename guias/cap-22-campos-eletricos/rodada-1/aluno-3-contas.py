#!/usr/bin/env python3
"""Aluno 3 (monitor cético): conferência independente das contas do guia do Cap. 22.
Não importa nem lê calculos.py. Só biblioteca padrão (math).
Cada linha imprime: item | valor do guia | meu valor | diferença relativa | ok?
Os "valores do guia" foram copiados do texto/HTML (data-resp, exemplos, conferir/*.md).
Os meus valores usam as constantes do livro (k = 8,99e9; e = 1,602e-19; g = 9,8; eps0 = 8,85e-12)
e, quando a integral importa, integração numérica (Simpson) em vez da fórmula fechada.
"""
import math
import sys

k = 8.99e9
eps0 = 8.85e-12
e = 1.602e-19
g = 9.8
pi = math.pi
linhas = []


def reg(nome, guia, meu, tol=0.02, absol=None, ang=False):
    if ang:
        d = (((meu - guia) % 360) + 540) % 360 - 180
        ok = abs(d) <= 1.5
        dif = f"{d:+.3f} deg"
    elif absol is not None:
        ok = abs(meu - guia) <= absol
        dif = f"{meu - guia:+.3g}"
    else:
        rel = abs(meu - guia) / abs(guia) if guia != 0 else abs(meu)
        ok = rel <= tol
        dif = f"{100 * (meu - guia) / guia:+.2f} %" if guia != 0 else f"{meu:+.3g}"
    linhas.append((nome, guia, meu, dif, ok))


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def soma_vetorial(cargas, P):
    """cargas: lista de (q, (x,y)); devolve (Ex, Ey) em P, por força bruta."""
    Ex = Ey = 0.0
    for q, (x, y) in cargas:
        dx, dy = P[0] - x, P[1] - y
        r = math.hypot(dx, dy)
        E = k * q / r**2
        Ex += E * dx / r
        Ey += E * dy / r
    return Ex, Ey


# ---------------- Aquecimento / pré-teste ----------------
reg("pre1 4,23 fC em C", 4.23e-15, 4.23 * 1e-15)
reg("pre2 F a 3 cm (0,8 N a 6 cm)", 3.2, 0.8 * (6 / 3) ** 2)
reg("pre3 Ax (10 a 135 graus)", -7.07, 10 * math.cos(math.radians(135)), tol=0.01)
reg("pre3 Ay", 7.07, 10 * math.sin(math.radians(135)), tol=0.01)
reg("pre4 angulo de (-3,-4)", 233.13, math.degrees(math.atan2(-4, -3)) % 360, ang=True)
a_, L_ = 1.0, 2.0
reg("pre5 int dx/x^2 = L/(a(a+L)) (a=1,L=2)", 2 / 3, simpson(lambda x: 1 / x**2, a_, a_ + L_))

# ---------------- P81 ----------------
W, E81 = 4.4, 150.0
q81 = -W / E81
reg("P81a q (C)", -0.02933, q81)
reg("P81 n de eletrons (1,8e17)", 1.8e17, abs(q81) / e, tol=0.03)
m81 = W / g
V = m81 / 2070.0
R81 = (3 * V / (4 * pi)) ** (1 / 3)
reg("P81 massa (kg) 0,449", 0.449, m81, tol=0.005)
reg("P81 raio (m) 3,7 cm", 0.037, R81, tol=0.01)
Esup = k * abs(q81) / R81**2
reg("P81 E superficie (1,9e11)", 1.9e11, Esup, tol=0.02)
reg("P81 Esup/Ear (63 mil)", 63000, Esup / 3e6, tol=0.01)
reg("P81 F entre metades ~ k(q/2)^2/R^2 (1e9)", 1e9, k * (abs(q81) / 2) ** 2 / R81**2, tol=0.5)
reg("P81 F exata casca = kq^2/(8R^2) (7e8)", 7e8, k * q81**2 / (8 * R81**2), tol=0.05)
reg("P81 e se E=3e6: q (1,5 uC)", 1.5e-6, W / 3e6, tol=0.04)
reg("P81 e se: Esup com essa q (9,5e6)", 9.5e6, k * (W / 3e6) / R81**2, tol=0.02)
qmax = 3e6 * R81**2 / k
reg("P81 q max sem faisca (4,6e-7)", 4.6e-7, qmax, tol=0.02)
reg("P81 forca com qmax a 150 N/C (7e-5 N)", 7e-5, qmax * 150, tol=0.03)
reg("P81 massa sustentada (7 mg)", 7e-6, qmax * 150 / g, tol=0.03)

# ---------------- Degrau 1 ----------------
rH = 5.29e-11
EH = k * e / rH**2
reg("D1 H: E (5,15e11)", 5.15e11, EH, tol=0.005)
reg("D1 H: F (8,24e-8)", 8.24e-8, e * EH, tol=0.005)
reg("D1 H: E/3e6 (170 mil)", 1.7e5, EH / 3e6, tol=0.01)
reg("D1 ficha: 1 nC a 3 cm (1,0e4)", 1.0e4, k * 1e-9 / 0.03**2, tol=0.01)
reg("D1 ficha: 26 mil eletrons (4,23 fC)", 2.6e4, 4.23e-15 / e, tol=0.02)
# Millikan
rho, r = 851.0, 1.64e-6
m = rho * 4 / 3 * pi * r**3
reg("Millikan m (kg)", 1.572e-14, m)
reg("Millikan mg (N)", 1.541e-13, m * g)
reg("Millikan |q| (C)", 8.026e-19, m * g / 1.92e5)
reg("Millikan |q|/e", 5.0, m * g / 1.92e5 / e, tol=0.03)
reg("ck1-3 E = 6e-6/2e-9", 3.0e3, 6.0e-6 / 2.0e-9)
reg("ck1-3 F com -4 nC", 1.2e-5, 4.0e-9 * 3.0e3)
# w1 (leitura no texto/widget): E = 9989*|q|/r^2 com r em unidades de 3 cm
reg("W1 constante 9989 (q em nC, r em 3 cm)", 9989, k * 1e-9 / 0.03**2, tol=0.001)

# ---------------- Degrau 2 ----------------
EA = k * 2.0e-9 / 0.02**2
EB = k * 3.0e-9 / 0.03**2
reg("D2 ex: E_A", 4.50e4, EA, tol=0.005)
reg("D2 ex: E_B", 3.00e4, EB, tol=0.005)
reg("D2 ex: total (7,5e4)", 7.5e4, EA + EB, tol=0.01)
reg("D2 ex: 'se B fosse +3 nC' (1,5e4)", 1.5e4, EA - EB, tol=0.01)
# lacuna: C=+1nC em +1 cm, D=-4 nC em +2 cm
EC = k * 1e-9 / 0.01**2
ED = k * 4e-9 / 0.02**2
reg("D2 lac-r-1 E_C", 8.99e4, EC)
reg("D2 lac-r-3 E_D", 8.99e4, ED)
Ex_tot, _ = soma_vetorial([(1e-9, (0.01, 0)), (-4e-9, (0.02, 0))], (0, 0))
reg("D2 lac-r-5 total (força bruta)", 0.0, Ex_tot, absol=900)
# ck2-3: ordenar quatro sistemas (posições -2d,-d,+d,+2d; unidade k e/d^2)
sistemas = {1: [1, -1, -1, 1], 2: [1, 1, -1, -1], 3: [-1, 1, 1, 1], 4: [-1, -1, 1, -1]}
pos = [-2, -1, 1, 2]
res = {}
for s, qs in sistemas.items():
    Ex, _ = soma_vetorial([(q, (x, 0)) for q, x in zip(qs, pos)], (0, 0))
    res[s] = abs(Ex) / k  # em unidades de e... com q=+-1 e d=1
for s in sistemas:
    reg(f"ck2-3 sistema {s}: |E| em ke/d^2", {1: 0.0, 2: 2.5, 3: 0.5, 4: 2.0}[s], res[s], absol=1e-9)
ordem = sorted(res, key=lambda s: -res[s])
print("ck2-3 ordem decrescente:", ordem, "(guia: 2, 4, 3, 1)")
# prev-w2
reg("prev-w2: +1 nC a 1 cm vs +4 nC a 2 cm (zero)", 0.0,
    soma_vetorial([(1e-9, (-0.01, 0)), (4e-9, (0.02, 0))], (0, 0))[0], absol=1e-6)
# rev-6
reg("rev-6: +q esq, -q dir: 2*E(1 cm)", 2 * k * 1e-9 / 1e-4,
    abs(soma_vetorial([(1e-9, (-0.01, 0)), (-1e-9, (0.01, 0))], (0, 0))[0]))

# ---------------- Degrau 3 ----------------
Ex, Ey = soma_vetorial([(2e-9, (-0.03, 0)), (2e-9, (0.03, 0))], (0, 0.04))
reg("D3 ex mediatriz: E1 (7,19e3)", 7.19e3, k * 2e-9 / 0.05**2, tol=0.003)
reg("D3 ex mediatriz: |E| (1,15e4)", 1.15e4, math.hypot(Ex, Ey), tol=0.005)
reg("D3 ex mediatriz: angulo (90)", 90, math.degrees(math.atan2(Ey, Ex)), ang=True)
# P9
q = 3.20e-19
Ex, Ey = soma_vetorial([(-q, (-3.0, 0)), (q, (3.0, 0))], (0, 4.0))
reg("P9a |E| (1,38e-10)", 1.381e-10, math.hypot(Ex, Ey))
reg("P9b angulo (180)", 180, math.degrees(math.atan2(Ey, Ex)), ang=True)
reg("P9 E de uma carga (1,151e-10)", 1.151e-10, k * q / 25)
Ex2, Ey2 = soma_vetorial([(q, (-3.0, 0)), (q, (3.0, 0))], (0, 4.0))
reg("P9 e se +q,+q (1,84e-10)", 1.841e-10, math.hypot(Ex2, Ey2))
Ex3, Ey3 = soma_vetorial([(-q, (-3.0, 0)), (q, (3.0, 0))], (0, 40.0))
reg("P9 e se y=40 m (2,7e-13)", 2.7e-13, math.hypot(Ex3, Ey3), tol=0.02)
p_dip = q * 6.0
reg("P9 dipolo (mediatriz) k p / y^3 em y=40 m", 2.7e-13, k * p_dip / 40.0**3, tol=0.02)
# lac-p (P69): lado 2 m, 12 nC
Ep = k * 12e-9 / 4.0
P = (0, math.sqrt(3))
for sgn, nome, guia in [(+1, "a", 46.71), (-1, "b", 26.97)]:
    Ex, Ey = soma_vetorial([(12e-9, (-1.0, 0)), (sgn * 12e-9, (1.0, 0))], P)
    reg(f"D3 P69({nome}) (força bruta)", guia, math.hypot(Ex, Ey))
reg("D3 lac-p-1 E de cada", 26.97, Ep)
reg("D3 lac-p-2 angulo com a vertical (30)", 30, math.degrees(math.atan2(1.0, math.sqrt(3))), ang=True)
# P15: q3=+2e na origem, q1=+e em (0,a), q2=+e em (a,0), P=(a/2,a/2)
a = 6.00e-6
Ex, Ey = soma_vetorial([(e, (0, a)), (e, (a, 0)), (2 * e, (0, 0))], (a / 2, a / 2))
reg("P15a |E| (160)", 160.0, math.hypot(Ex, Ey))
reg("P15b angulo (45)", 45, math.degrees(math.atan2(Ey, Ex)), ang=True)
reg("P15 E de q1 sozinha (80)", 80.0, k * e / (a * a / 2), tol=0.005)
Ex, Ey = soma_vetorial([(2 * e, (0, a)), (e, (a, 0)), (2 * e, (0, 0))], (a / 2, a / 2))
reg("P15 e se q1=+2e: |E| (179)", 179.0, math.hypot(Ex, Ey), tol=0.005)
Ex, Ey = soma_vetorial([(e, (0, a)), (e, (a, 0)), (-2 * e, (0, 0))], (a / 2, a / 2))
reg("P15 e se q3=-2e: angulo (-135)", -135, math.degrees(math.atan2(Ey, Ex)), ang=True)
# P8: P na origem; q1 (-d,+d)/sqrt2 ...; d=5 um
d = 5.0e-6
c = d / math.sqrt(2)
cargas8 = [(5 * e, (-c, c)), (5 * e, (c, -c)), (3 * e, (c, c)), (-12 * e, (2 * c, 2 * c))]
Ex, Ey = soma_vetorial(cargas8, (0, 0))
reg("P8 |E| (0)", 0.0, math.hypot(Ex, Ey), absol=3)
reg("P8 E1 (288)", 288.0, k * 5 * e / d**2, tol=0.005)
reg("P8 E3 (172,8)", 172.8, k * 3 * e / d**2, tol=0.005)
reg("P8 E4 (172,8)", 172.8, k * 12 * e / (2 * d) ** 2, tol=0.005)
cargas8b = [(5 * e, (-c, c)), (5 * e, (c, -c)), (3 * e, (c, c)), (-12 * e, (-2 * c, -2 * c))]
Ex, Ey = soma_vetorial(cargas8b, (0, 0))
reg("P8 e se q4 na diagonal oposta (346)", 345.6, math.hypot(Ex, Ey), tol=0.005)
# ck3-2/rev-4
reg("ck3-2 angulo (-2,+2) = 135", 135, math.degrees(math.atan2(2, -2)), ang=True)
reg("rev-4 angulo (+3,-3) = -45", -45, math.degrees(math.atan2(-3, 3)), ang=True)
reg("ck3-3 r vertice-centro / a = 0,707", 0.707, math.hypot(0.5, 0.5), tol=0.001)

# ---------------- Degrau 4 ----------------
# campo no centro de um arco: integra cos(theta) numericamente
def E_arco(Q, r_, phi):
    lam = Q / (r_ * phi)
    return simpson(lambda th: k * lam / r_ * math.cos(th), -phi / 2, phi / 2)

fator = lambda phi: E_arco(1.0, 1.0, phi) / k
reg("D4 120 graus: fator (0,827)", 0.827, fator(2 * pi / 3), tol=0.002)
reg("D4 3sqrt3/(2pi) exato", 3 * math.sqrt(3) / (2 * pi), fator(2 * pi / 3), tol=1e-6)
reg("D4 semicirculo: 2/pi (0,64)", 0.64, fator(pi), tol=0.01)
reg("D4 anel completo: 0", 0.0, fator(2 * pi), absol=1e-9)
# P29
reg("P29 razao (pi/2)", pi / 2, (k / 1.0) / (k * fator(pi)))
reg("P29 e se quarto de circulo (1,11)", 1.11, 1 / fator(pi / 2), tol=0.005)
# lac-a (P71)
phi71 = 4.0 / 2.0
reg("P71 phi (2 rad)", 2.0, phi71)
reg("P71 lambda (5e-9)", 5e-9, 20e-9 / 4.0)
reg("P71 E (37,8)", 37.82, E_arco(20e-9, 2.0, phi71), tol=0.002)
# P26: quarto de cima +q, quarto de baixo -q; semicirculo a esquerda de P; força bruta fatiando
def campo_arco_fatiado(cargas_arcos, r_, n=4000):
    Ex = Ey = 0.0
    for qtot, a0, a1 in cargas_arcos:
        dq = qtot / n
        for i in range(n):
            a = a0 + (a1 - a0) * (i + 0.5) / n
            pos_ = (r_ * math.cos(a), r_ * math.sin(a))
            ex, ey = soma_vetorial([(dq, pos_)], (0, 0))
            Ex += ex
            Ey += ey
    return Ex, Ey

q26, r26 = 4.50e-12, 0.0500
Ex, Ey = campo_arco_fatiado([(q26, pi / 2, pi), (-q26, pi, 3 * pi / 2)], r26)
reg("P26a |E| (20,6) fatiando em 8000 cargas", 20.6, math.hypot(Ex, Ey), tol=0.002)
reg("P26b angulo (-90)", -90, math.degrees(math.atan2(Ey, Ex)), ang=True)
reg("P26 formula 4kq/(pi r^2)", 20.6, 4 * k * q26 / (pi * r26**2), tol=0.002)
reg("P26 e se semicirculo +2q: (20,6)", 20.6, 2 * k * (2 * q26 / (pi * r26)) / r26, tol=0.002)
# P27 conferência citada
Ex, Ey = campo_arco_fatiado([(15e-12, 0, pi), (-15e-12, pi, 2 * pi)], 0.085, n=3000)
reg("P27 (citado no P26-4): 23,8 N/C", 23.8, math.hypot(Ex, Ey), tol=0.003)
# w4 modo +/-: fator 2(1-cos(phi/2))/phi em phi=pi
reg("W4 +/-: fator em 180 graus (2/pi)", 2 / pi, 2 * (1 - math.cos(pi / 2)) / pi, tol=1e-9)
# ck4-3: arranjos (E = campo de um quarto de circulo, unidade 1)
def quarto(sgn, quadrante):
    # campo no centro de um quarto de circulo no quadrante dado (1..4): aponta ao longo da diagonal oposta
    ang = math.radians(45 + 90 * (quadrante - 1) + 180)
    return (sgn * math.cos(ang), sgn * math.sin(ang))

def soma(*vs):
    return math.hypot(sum(v[0] for v in vs), sum(v[1] for v in vs))

a_ = soma(quarto(1, 1))
b_ = soma(quarto(1, 1), quarto(1, 2))
c_ = soma(quarto(1, 1), quarto(1, 2), quarto(1, 3))
d_ = soma(quarto(1, 1), quarto(1, 2), quarto(1, 3), quarto(1, 4))
e_ = soma(quarto(1, 1), quarto(1, 2), quarto(1, 3), quarto(-1, 4))
print(f"ck4-3: a={a_:.3f} b={b_:.3f} c={c_:.3f} d={d_:.3f} e={e_:.3f} (guia: e=2, b=1,414, a=c=1, d=0)")
reg("ck4-3 e", 2.0, e_, tol=1e-6)
reg("ck4-3 b", math.sqrt(2), b_, tol=1e-6)
reg("ck4-3 c", 1.0, c_, tol=1e-6)
reg("ck4-3 d", 0.0, d_, absol=1e-9)

# ---------------- Degrau 5 ----------------
def E_barra_axial(q, L, a):
    lam = q / L
    return simpson(lambda x: k * lam / x**2, a, a + L)

q5, L5, a5 = 5.0e-9, 0.10, 0.050
reg("D5 ex barra: E (5,99e3)", 5.99e3, E_barra_axial(q5, L5, a5), tol=0.002)
reg("D5 ex: pelo centro (4,50e3)", 4.50e3, k * q5 / 0.10**2, tol=0.002)
reg("D5 ex: erro do centro 25 %", 25.0, 100 * (1 - (k * q5 / 0.10**2) / E_barra_axial(q5, L5, a5)), tol=0.02)
reg("D5 ex: tudo na ponta perto (1,80e4)", 1.80e4, k * q5 / a5**2, tol=0.002)
reg("D5 ex: tudo na ponta longe (2,00e3)", 2.00e3, k * q5 / (a5 + L5) ** 2, tol=0.002)
reg("D5 ex: dist. equivalente (8,7 cm)", 8.7, 100 * math.sqrt(a5 * (a5 + L5)), tol=0.01)
# P67 (lac-b)
reg("P67 E (60,68)", 60.68, E_barra_axial(9e-9 * 3.0, 3.0, 1.0), tol=0.001)
# P31
q31, L31, a31 = 4.23e-15, 0.0815, 0.120
reg("P31a lambda (-5,19e-14)", -5.19e-14, -q31 / L31, tol=0.002)
Eb = E_barra_axial(q31, L31, a31)
reg("P31b |E| (1,573e-3)", 1.573e-3, Eb, tol=0.002)
reg("P31 tudo na ponta perto (2,641e-3)", 2.641e-3, k * q31 / a31**2, tol=0.002)
reg("P31 tudo na ponta longe (9,366e-4)", 9.366e-4, k * q31 / (a31 + L31) ** 2, tol=0.002)
reg("P31 pelo centro (1,472e-3)", 1.472e-3, k * q31 / (a31 + L31 / 2) ** 2, tol=0.002)
reg("P31 erro do centro 'uns 7 %' (rel. ao pontual)", 7.0, 100 * (Eb - k * q31 / (a31 + L31 / 2) ** 2) / (k * q31 / (a31 + L31 / 2) ** 2), tol=0.15)
reg("P31 erro do centro (rel. ao real)", 7.0, 100 * (Eb - k * q31 / (a31 + L31 / 2) ** 2) / Eb, tol=0.15)
D = 50.0
Ed = E_barra_axial(q31, L31, D - L31 / 2)
Ee = k * q31 / D**2
reg("P31d barra a 50 m (1,521e-8)", 1.521e-8, Ed, tol=0.002)
reg("P31e particula a 50 m (1,521e-8)", 1.521e-8, Ee, tol=0.002)
reg("P31 diferença relativa d/e (7e-7)", 7e-7, (Ed - Ee) / Ee, tol=0.1)
reg("P31 e se a=0,5 cm: razao a barra/pontual no centro (4,8)", 4.8,
    E_barra_axial(q31, L31, 0.005) / (k * q31 / (0.005 + L31 / 2) ** 2), tol=0.01)
# erros quoted: W5 / prev-w5 / ck5-3 / rev-1
f = lambda x: 1 / (1 - 1 / (4 * x * x))
for D_ , nome, tx_rel_pont, tx_rel_real in [(1.0, "D=L", 33.0, 25.0), (2.0, "D=2L", 7.0, 6.25), (5.0, "D=5L", 1.0, 1.0),
                                                (10.0, "D=10L", 0.25, 0.25)]:
    # razão barra/ponto pela integral numérica
    L1, a1 = 1.0, D_ - 0.5
    barra = simpson(lambda x: 1 / x**2, a1, a1 + L1)
    ponto = 1 / D_**2
    print(f"{nome}: barra/ponto={barra/ponto:.4f}; erro do ponto rel. ao real={100*(1-ponto/barra):.2f} %;"
          f" erro rel. ao pontual={100*(barra/ponto-1):.2f} %; (guia prev-w5/ck5-3: {tx_rel_pont} %; widget: {tx_rel_real} %)")
reg("rev-1 real (a=L): 0,50 kq/L^2", 0.50, simpson(lambda x: 1 / x**2, 1.0, 2.0), tol=1e-6)
reg("rev-1 pelo centro: 0,44 (arredondado)", 0.44, 1 / 1.5**2, tol=0.02)
reg("ck5-3 D=10L: 1/(1-1/400)", 1.0025, f(10.0), tol=1e-4)

# ---------------- Degrau 6 ----------------
def E_anel(q, R, z):
    return k * q * z / (z * z + R * R) ** 1.5

def E_disco_num(sigma, R, z, n=4000):
    # soma de aneis finos, sem usar a forma fechada
    return simpson(lambda r_: E_anel(sigma * 2 * pi * r_, r_, z), 0, R, n)

def E_disco_fech(sigma, R, z):
    return sigma / (2 * eps0) * (1 - z / math.sqrt(z * z + R * R))

sig, Rd, zd = 5.3e-6, 0.025, 0.12
reg("P34 ex: sigma/2eps0 (2,99e5)", 2.99e5, sig / (2 * eps0), tol=0.002)
reg("P34 ex: parenteses (0,0210)", 0.0210, 1 - zd / math.sqrt(zd**2 + Rd**2), tol=0.005)
reg("P34 ex: E (6,29e3) fechada", 6.29e3, E_disco_fech(sig, Rd, zd), tol=0.002)
# a soma de aneis usa k=1/(4 pi eps0)
kk = 1 / (4 * pi * eps0)
def E_anel2(q, R, z):
    return kk * q * z / (z * z + R * R) ** 1.5
reg("P34 ex: E por soma de aneis", 6.29e3, simpson(lambda r_: E_anel2(sig * 2 * pi * r_, r_, zd), 0, Rd, 4000), tol=0.002)
Qd = sig * pi * Rd**2
reg("P34 ex: Q (1,04e-8)", 1.04e-8, Qd, tol=0.005)
reg("P34 ex: kQ/z^2 (6,50e3)", 6.50e3, k * Qd / zd**2, tol=0.005)
reg("P34 ex: pontual 3 % acima", 3.0, 100 * (k * Qd / zd**2 / E_disco_fech(sig, Rd, zd) - 1), tol=0.1)
reg("P35 z/R (0,577)", 0.57735, 1 / math.sqrt(3), tol=1e-4)
reg("P35 z (0,346 m, gabarito 3 alg.)", 0.346, 0.6 / math.sqrt(3), tol=0.002)
# P38: bissecção na curva
def razao(x):
    return 1 - x / math.sqrt(x * x + 1)
lo, hi = 0.0, 10.0
for _ in range(100):
    mid = (lo + hi) / 2
    if razao(mid) > 0.5:
        lo = mid
    else:
        hi = mid
xmeio = lo
R38 = 4.0 / xmeio
reg("P38 R (6,928 cm) com z=4,0 cm", 6.928, R38, tol=0.0005)
reg("P38 E/Em em z=zs=8 cm (0,24)", 0.24, razao(8.0 / R38), tol=0.02)
reg("P38 E/Em em z=2 cm (conferência da figura: 0,7226)", 0.7226, razao(2.0 / R38), tol=0.001)
reg("P38 E/Em em z=6 cm", 0.345, razao(6.0 / R38), tol=0.01)
# e se E=0,25Em em z=4: R?
lo, hi = 0.0, 10.0
for _ in range(100):
    mid = (lo + hi) / 2
    if razao(mid) > 0.25:
        lo = mid
    else:
        hi = mid
reg("P38 e se 0,25Em em 4 cm: R (3,5 cm)", 3.5, 4.0 / lo, tol=0.02)
reg("prev-w6 z=0,1R: disco (0,90)", 0.90, razao(0.1), tol=0.01)
reg("prev-w6 z=0,1R: erro de dizer 'placa infinita' (%)", 11.0, 100 * (1 - razao(0.1)) / razao(0.1), tol=0.05)
reg("rev-3 sigma/2eps0 (3,0e5)", 3.0e5, sig / (2 * eps0), tol=0.01)
reg("rev-3 sigma/eps0 (6,0e5)", 6.0e5, sig / eps0, tol=0.01)
# ck6-1: ordenar a, b, c para vários z
def Ea(Q, R, z): return E_disco_fech(Q / (pi * R * R), R, z)
def Ec(Q, z):
    s = Q / (pi * (4 - 1))  # R=1 interno, 2 externo
    return E_disco_fech(s, 2.0, z) - E_disco_fech(s, 1.0, z)
ordem_ok = True
for z in [0.01, 0.1, 0.3, 0.5, 1, 2, 3, 5, 10, 50]:
    A = Ea(1.0, 1.0, z); B = Ea(1.0, 2.0, z); C = Ec(1.0, z)
    if not (A > B > C):
        ordem_ok = False
        print("ck6-1 ordem quebra em z =", z, A, B, C)
print("ck6-1 a > b > c em todos os z testados:", ordem_ok)
# limite de longe e erro da regra (tamanho/2D)^2 no disco
for xr in [2, 4.8, 10]:
    exato = razao(xr)  # E/Em
    pont = 1 / (2 * xr * xr)
    print(f"disco z/R={xr}: pontual/exato-1 = {100*(pont/exato-1):.2f} %; regra (tamanho/2D)^2 com tamanho=2R: {100/(xr*xr):.2f} %; 0,75(R/z)^2 = {75/(xr*xr):.2f} %")

# ---------------- Gabarito do plano de revisão (conferência rápida) ----------------
reg("rev P5: |q| = E r^2/k (2 N/C? 56 pC)", 56e-12, 2.0 * 0.5**2 / k, tol=0.02)
reg("rev P41(a): E = F/|q| (1,5e3)", 1.5e3, 3.0e-6 / 2.0e-9, tol=0.01)
reg("rev P41(b): F = eE (2,4e-16)", 2.4e-16, e * 1.5e3, tol=0.02)
reg("rev P63(a): peso gota 1,2 um (8,87e-15)", 8.87e-15, 1000 * 4 / 3 * pi * (0.6e-6) ** 3 * g, tol=0.01)
reg("rev P63(b): n eletrons (120)", 120, 1000 * 4 / 3 * pi * (0.6e-6) ** 3 * g / (e * 462), tol=0.02)


# ---------------- Extras: perguntas "e se..." difíceis (calculadas por mim, não estão no guia) ----------------
print()
print("=== EXTRAS (e se difíceis) ===")

def campo3d(cargas, P):
    Ex = Ey = Ez = 0.0
    for q_, (x, y, z) in cargas:
        dx, dy, dz = P[0] - x, P[1] - y, P[2] - z
        r_ = math.sqrt(dx * dx + dy * dy + dz * dz)
        E_ = k * q_ / r_**3
        Ex += E_ * dx; Ey += E_ * dy; Ez += E_ * dz
    return (Ex, Ey, Ez)

# P8: P é equilíbrio estável para uma carga de prova positiva? Jacobiano de E em P (3D; a figura é plana)
c8 = [(5 * e, (-c, c, 0)), (5 * e, (c, -c, 0)), (3 * e, (c, c, 0)), (-12 * e, (2 * c, 2 * c, 0))]
h = 1e-9
u1 = (1 / math.sqrt(2), 1 / math.sqrt(2), 0)     # ao longo de q3-q4 (diagonal "para cima e à direita")
u2 = (-1 / math.sqrt(2), 1 / math.sqrt(2), 0)    # ao longo de q1-q2
u3 = (0, 0, 1)                                   # perpendicular ao plano
def dE_du(u):
    Ep = campo3d(c8, tuple(h * ui for ui in u)); Em = campo3d(c8, tuple(-h * ui for ui in u))
    return sum((Ep[i] - Em[i]) * u[i] for i in range(3)) / (2 * h)
d1, d2, d3 = dE_du(u1), dE_du(u2), dE_du(u3)
print(f"P8: dE_u/du ao longo de q3-q4: {d1:.4g} V/m^2; de q1-q2: {d2:.4g}; fora do plano: {d3:.4g}; soma (Laplace) = {d1+d2+d3:.3g}")
print("   (derivada negativa = força restauradora para carga de prova positiva; positiva = instável)")
print(f"   unidade natural ke/d^3 = {k*e/d**3:.4g};  razoes: {d1/(k*e/d**3):.3f}, {d2/(k*e/d**3):.3f}, {d3/(k*e/d**3):.3f}")

# P31: a partir de que D a barra e a partícula diferem em 3 algarismos (0,05 %)?
Dmin = L31 / (2 * math.sqrt(5e-4))
print(f"P31: diferença relativa barra/partícula chega a 0,05 % em D = {Dmin:.2f} m = {Dmin/L31:.1f} L")

# P9 com P na origem (y=0)
Ex0, Ey0 = soma_vetorial([(-q, (-3.0, 0)), (q, (3.0, 0))], (0, 1e-9))
print(f"P9 em y -> 0: |E| = {math.hypot(Ex0,Ey0):.4g} N/C (2kq/9 = {2*k*q/9:.4g}), angulo {math.degrees(math.atan2(Ey0,Ex0)):.1f} graus")

# disco: sigma por face vs total (isolante fino) e condutor
sigma_tot = 5.3e-6
print(f"Disco isolante fino: E_m = sigma_total/(2 eps0) = {sigma_tot/(2*eps0):.4g}; com sigma em CADA face (total 2 sigma): {2*sigma_tot/(2*eps0):.4g} = sigma/eps0")
# condutor fino com carga total Q: sigma_face(r) = Q/(4 pi R sqrt(R^2-r^2)); em r=0: Q/(4 pi R^2)
Qd_ = sigma_tot * pi * 0.025**2
E_cond_centro = (Qd_ / (4 * pi * 0.025**2)) / eps0
E_iso_centro = (Qd_ / (pi * 0.025**2)) / (2 * eps0)
print(f"Mesma carga total Q={Qd_:.3g} C num disco R=2,5 cm: isolante uniforme E_m={E_iso_centro:.4g}; condutor (centro) = {E_cond_centro:.4g}; razão cond/iso = {E_cond_centro/E_iso_centro:.3f}")

# potencial do disco e consistência E = -dV/dz
def V_disco(sig, R, z): return sig / (2 * eps0) * (math.sqrt(z * z + R * R) - z)
z0, Rr = 0.03, 0.05
dV = (V_disco(1e-6, Rr, z0 + 1e-7) - V_disco(1e-6, Rr, z0 - 1e-7)) / 2e-7
print(f"disco: -dV/dz = {-dV:.5g}; E(Eq. 22-26) = {E_disco_fech(1e-6, Rr, z0):.5g}")

# P26: cada quarto trocado por carga pontual no meio do quarto
Ex, Ey = soma_vetorial([(q26, (r26 * math.cos(3 * pi / 4), r26 * math.sin(3 * pi / 4))), (-q26, (r26 * math.cos(5 * pi / 4), r26 * math.sin(5 * pi / 4)))], (0, 0))
print(f"P26: dois pontos no meio dos quartos: |E| = {math.hypot(Ex,Ey):.4g} (real 20,6), razao = {math.hypot(Ex,Ey)/20.603:.3f}")

# W5/W4/W6: leituras que o widget imprime (conferidas na fórmula)
print("W4 u: phi=60 graus fator", round(math.sin(math.radians(30)) / (pi / 6), 4), "; phi=270 graus", round(math.sin(3 * pi / 4) / (3 * pi / 4), 4))
print("W4 +/-: phi=360 graus fator", round(2 * (1 - math.cos(pi)) / (2 * pi), 4), "(anel com metades +/- => 4/(2pi)=0,637 kQ/r^2)")

# ---------------- saída ----------------
print()
print(f"{'item':62s} | {'guia':>12s} | {'meu':>12s} | {'dif':>12s} | ok")
for nome, guia, meu, dif, ok in linhas:
    print(f"{nome:62s} | {guia:12.4g} | {meu:12.4g} | {dif:>12s} | {'ok' if ok else 'DIVERGE'}")
print()
print("Itens que DIVERGEM:", [n for n, _, _, _, ok in linhas if not ok])
print("Total:", len(linhas), "itens;", sum(1 for *_, ok in linhas if ok), "ok")

if "--md" in sys.argv:
    print()
    print("| item | valor do guia | meu valor | diferença | ok? |")
    print("|---|---|---|---|---|")
    for nome, guia, meu, dif, ok in linhas:
        print(f"| {nome} | {guia:.4g} | {meu:.4g} | {dif} | {'ok' if ok else 'DIVERGE'} |")
