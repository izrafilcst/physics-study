"""Contas do guia do Capítulo 22 (Campos Elétricos).

Toda conta numérica do guia sai daqui. Rode com:  python3 -I calculos.py
Cada linha mostra o valor calculado e, quando existe, a resposta do gabarito do
livro. Divergência acima de 2 % é marcada com  <<< DIVERGE.
"""
import math

# Constantes (as do livro)
k = 8.99e9          # N·m²/C²
e = 1.602e-19       # C
eps0 = 8.85e-12     # C²/(N·m²)
g = 9.8             # m/s²
m_e = 9.11e-31      # kg
E_RUPTURA = 3.0e6   # N/C, ruptura do ar (Módulo 22-6 / Problema 42)

LINHAS = []


def mostra(rotulo, valor, gabarito=None, unidade="", tol=0.02, ref="gabarito"):
    """Imprime o valor; se houver gabarito, compara (erro relativo)."""
    txt = f"{rotulo:<58} {valor: .4g} {unidade}"
    if gabarito is not None:
        if gabarito == 0:
            ok = abs(valor) < 1e-9
            err = abs(valor)
        else:
            err = abs(valor - gabarito) / abs(gabarito)
            ok = err <= tol
        txt += f"   | {ref} {gabarito:.4g}  ({err*100:.2f} %)"
        if not ok:
            txt += "  <<< DIVERGE"
    print(txt)
    LINHAS.append(txt)
    return valor


def titulo(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def angulo(vx, vy):
    """Orientação em graus em relação a +x, no intervalo (-180, 180]."""
    return math.degrees(math.atan2(vy, vx))


def campo_pontual(q, xq, yq, xp, yp):
    """Vetor campo em (xp, yp) de uma carga q em (xq, yq)."""
    dx, dy = xp - xq, yp - yq
    r = math.hypot(dx, dy)
    E = k * q / r**2           # com sinal: + aponta para longe da carga
    return E * dx / r, E * dy / r


# ---------------------------------------------------------------------------
titulo("DEGRAU 0 — gancho e pré-requisitos")
mostra("Prefixo: 4,23 fC em C", 4.23e-15, unidade="C")
mostra("Coulomb: r -> r/2 multiplica F por", (1 / 0.5) ** 2)
mostra("Vetor 10 a 135°: componente x", 10 * math.cos(math.radians(135)))
mostra("Vetor 10 a 135°: componente y", 10 * math.sin(math.radians(135)))
mostra("Ângulo de (-3, -4) [atan2]", angulo(-3, -4), unidade="°")
mostra("  mesmo ângulo em 0..360", angulo(-3, -4) % 360, unidade="°")
mostra("  atan(4/3) (o que a calculadora dá)", math.degrees(math.atan(4 / 3)), unidade="°")
a_, L_ = 0.05, 0.10
mostra("∫_a^(a+L) dx/x² com a=5 cm, L=10 cm (1/m)", 1 / a_ - 1 / (a_ + L_))
mostra("  = L/(a(a+L))", L_ / (a_ * (a_ + L_)))
mostra("∫_-60°^60° cos θ dθ = 2 sen 60°", 2 * math.sin(math.radians(60)))

# ---------------------------------------------------------------------------
titulo("DEGRAU 1 — campo = força por coulomb")
r_H = 5.29e-11
E_H = mostra("Ex. resolvido: E do próton a 5,29e-11 m", k * e / r_H**2, unidade="N/C")
mostra("  força no elétron F = eE", e * E_H, unidade="N")
mostra("  (confere com Coulomb k e²/r²)", k * e**2 / r_H**2, unidade="N")
mostra("  E_átomo / E_ruptura do ar", E_H / E_RUPTURA)
mostra("Ficha: elétron no campo de bom tempo, F = eE (150 N/C)", e * 150, unidade="N")
mostra("Ficha: peso do elétron", m_e * g, unidade="N")
mostra("  razão F_el / peso", e * 150 / (m_e * g))
# Exemplo com lacunas: Problema 39 (Millikan)
r_gota = 1.64e-6
rho_oleo = 851.0
m_gota = rho_oleo * 4 / 3 * math.pi * r_gota**3
mostra("Lacuna P39: massa da gota", m_gota, unidade="kg")
W_gota = mostra("Lacuna P39: peso da gota", m_gota * g, unidade="N")
q_gota = mostra("Lacuna P39: |q| = mg/E", W_gota / 1.92e5, unidade="C")
mostra("Lacuna P39: |q|/e (gabarito: 5, carga -5e)", q_gota / e, gabarito=5)
# W1: dobrar r
mostra("W1: E(2r)/E(r)", 1 / 4)
mostra("W1: carga 1,0 nC a 3,0 cm", k * 1e-9 / 0.03**2, unidade="N/C")

# ---------------------------------------------------------------------------
titulo("P81 — esfera de enxofre flutuando no campo atmosférico")
W = 4.4
E_atm = 150.0
q81 = -W / E_atm   # E para baixo; força tem de ser para cima -> q < 0
mostra("P81(a) q = -W/E", q81, gabarito=-0.029, unidade="C")
mostra("P81(a) q em múltiplos de e (|q|/e)", abs(q81) / e)
# Viabilidade: raio da esfera (densidade do enxofre: 2,07 g/cm³, valor de tabela)
rho_S = 2070.0
m_S = W / g
V_S = m_S / rho_S
R_S = (3 * V_S / (4 * math.pi)) ** (1 / 3)
mostra("P81(b) massa da esfera", m_S, unidade="kg")
mostra("P81(b) raio da esfera (enxofre 2,07 g/cm³)", R_S * 100, unidade="cm")
E_sup = mostra("P81(b) campo na superfície k|q|/R²", k * abs(q81) / R_S**2, unidade="N/C")
mostra("P81(b) E_superfície / E_ruptura", E_sup / E_RUPTURA)
F_hemi_est = k * (abs(q81) / 2) ** 2 / R_S**2
mostra("P81(b) estimativa: k(q/2)²/R² entre metades", F_hemi_est, unidade="N")
F_hemi = k * q81**2 / (8 * R_S**2)   # exato p/ casca uniforme: q²/(32πε0R²)
mostra("P81(b) exato (casca): k q²/(8R²)", F_hemi, unidade="N")
mostra("P81(b) essa força em 'toneladas-força' (/ (1000 g))", F_hemi / (1000 * g), unidade="t")
mostra("P81(b) carga máx. sem ruptura: E_rup R²/k", E_RUPTURA * R_S**2 / k, unidade="C")
mostra("P81(b) peso que essa carga sustentaria (q·150)", E_RUPTURA * R_S**2 / k * 150, unidade="N")
mostra("P81 e se E = 3e6 N/C (limite): |q| = W/E", W / E_RUPTURA, unidade="C")

# ---------------------------------------------------------------------------
titulo("DEGRAU 2 — na mesma reta")
# Ex. resolvido: +2,0 nC em x=-2,0 cm; -3,0 nC em x=+3,0 cm; campo na origem
EA = k * 2e-9 / 0.02**2
EB = k * 3e-9 / 0.03**2
mostra("Ex. D2: E_A (+2 nC a 2 cm), aponta +x", EA, unidade="N/C")
mostra("Ex. D2: E_B (-3 nC a 3 cm), aponta +x", EB, unidade="N/C")
mostra("Ex. D2: E total (+x)", EA + EB, unidade="N/C")
ex_check = sum(campo_pontual(q, x, 0, 0, 0)[0] for q, x in [(2e-9, -0.02), (-3e-9, 0.03)])
mostra("  conferência vetorial E_x", ex_check, unidade="N/C")
mostra("Ex. D2 e se B fosse +3 nC: E total (A - B)", EA - EB, unidade="N/C")
# Lacuna: +1,0 nC em x=+1,0 cm; -4,0 nC em x=+2,0 cm
EC = k * 1e-9 / 0.01**2
ED = k * 4e-9 / 0.02**2
mostra("Lacuna D2: E_C (+1 nC a 1 cm), aponta -x", EC, unidade="N/C")
mostra("Lacuna D2: E_D (-4 nC a 2 cm), aponta +x", ED, unidade="N/C")
lac = sum(campo_pontual(q, x, 0, 0, 0)[0] for q, x in [(1e-9, 0.01), (-4e-9, 0.02)])
mostra("Lacuna D2: E total", lac, unidade="N/C")
# Pergunta 4 do livro (par): cargas em -2d, -d, +d, +2d; campo no centro em ke/d²
sistemas = {1: [+1, -1, -1, +1], 2: [+1, +1, -1, -1], 3: [-1, +1, +1, +1], 4: [-1, -1, +1, -1]}
pos = [-2, -1, 1, 2]
for s, qs in sistemas.items():
    Ex = sum(campo_pontual(q, x, 0, 0, 0)[0] for q, x in zip(qs, pos))  # k=8.99e9 -> normalizar
    mostra(f"Pergunta 4, sistema {s}: |E| em unidades de ke/d²", abs(Ex) / k)

# ---------------------------------------------------------------------------
titulo("P8 — quatro partículas (Fig. 22-36)")
d8 = 5.0e-6
E1 = k * 5 * e / d8**2
E3 = k * 3 * e / d8**2
E4 = k * 12 * e / (2 * d8) ** 2
mostra("P8: E1 = E2 = k(5e)/d²", E1, unidade="N/C")
mostra("P8: E3 = k(3e)/d²", E3, unidade="N/C")
mostra("P8: E4 = k(12e)/(2d)²", E4, unidade="N/C")
# Geometria: P na origem; q1 em d(-1,1)/√2, q2 em d(1,-1)/√2, q3 em d(1,1)/√2, q4 em 2d(1,1)/√2
u = 1 / math.sqrt(2)
cargas8 = [(5 * e, -d8 * u, d8 * u), (5 * e, d8 * u, -d8 * u), (3 * e, d8 * u, d8 * u), (-12 * e, 2 * d8 * u, 2 * d8 * u)]
Ex8 = sum(campo_pontual(q, x, y, 0, 0)[0] for q, x, y in cargas8)
Ey8 = sum(campo_pontual(q, x, y, 0, 0)[1] for q, x, y in cargas8)
mostra("P8: |E| total (vetorial) — resposta do guia", math.hypot(Ex8, Ey8), unidade="N/C")
mostra("P8 e se q4 estivesse do outro lado (a 2d, ↙): |E|", E3 + E4, unidade="N/C")
mostra("P8 e se q4 = +12e (mesmo lugar): |E|", E3 + E4, unidade="N/C")

# ---------------------------------------------------------------------------
titulo("DEGRAU 3 — no plano")
# Ex. resolvido: +2,0 nC em (-3,0; 0) cm e (+3,0; 0) cm; P em (0; 4,0) cm
Ei = k * 2e-9 / 0.05**2
mostra("Ex. D3: E de cada carga (r = 5,0 cm)", Ei, unidade="N/C")
mostra("Ex. D3: E_y de cada = E·(4/5)", Ei * 0.8, unidade="N/C")
Ex3 = sum(campo_pontual(2e-9, x, 0, 0, 0.04)[0] for x in (-0.03, 0.03))
Ey3 = sum(campo_pontual(2e-9, x, 0, 0, 0.04)[1] for x in (-0.03, 0.03))
mostra("Ex. D3: E total (só y)", Ey3, unidade="N/C")
mostra("Ex. D3: E_x total", Ex3, unidade="N/C")
mostra("Ex. D3: ângulo", angulo(Ex3, Ey3), unidade="°")
# Lacuna: Problema 69 (ímpar): |q| = 12 nC, lado 2,0 m
E69 = k * 12e-9 / 2.0**2
mostra("Lacuna P69: E de cada carga", E69, unidade="N/C")
mostra("Lacuna P69(a): duas positivas, 2E cos 30°", 2 * E69 * math.cos(math.radians(30)), gabarito=47, unidade="N/C")
mostra("Lacuna P69(b): + e -, 2E sen 30°", 2 * E69 * math.sin(math.radians(30)), gabarito=27, unidade="N/C")
# Pergunta 3 (ímpar): dois -q simétricos; P no eixo y: campo total aponta -y (conceitual)
Ex_p3 = sum(campo_pontual(-1e-9, x, 0, 0, 0.04)[0] for x in (-0.03, 0.03))
Ey_p3 = sum(campo_pontual(-1e-9, x, 0, 0, 0.04)[1] for x in (-0.03, 0.03))
mostra("Pergunta 3: ângulo do campo total (gabarito: -y)", angulo(Ex_p3, Ey_p3), gabarito=-90, unidade="°")

# ---------------------------------------------------------------------------
titulo("P9 — dipolo e ponto na mediatriz (Fig. 22-37)")
q9 = 3.20e-19
r9 = math.hypot(3.0, 4.0)
E9 = mostra("P9: E de cada carga k q / r² (r = 5,00 m)", k * q9 / r9**2, unidade="N/C")
Ex9 = sum(campo_pontual(q, x, 0, 0, 4.0)[0] for q, x in [(-q9, -3.0), (q9, 3.0)])
Ey9 = sum(campo_pontual(q, x, 0, 0, 4.0)[1] for q, x in [(-q9, -3.0), (q9, 3.0)])
mostra("P9(a): |E|", math.hypot(Ex9, Ey9), gabarito=1.38e-10, unidade="N/C")
mostra("P9(a): pela fórmula 2E·(3/5)", 2 * E9 * 0.6, gabarito=1.38e-10, unidade="N/C")
mostra("P9(b): ângulo [atan2]", angulo(Ex9, Ey9) % 360, gabarito=180, unidade="°")
mostra("P9 e se as duas fossem +q: |E| = 2E(4/5), a 90°", 2 * E9 * 0.8, unidade="N/C")
mostra("P9 e se P subisse para y=40 m: |E| (cai ~1/r³)", 2 * k * q9 / (3**2 + 40**2) * (3 / math.hypot(3, 40)), unidade="N/C")

# ---------------------------------------------------------------------------
titulo("P15 — três partículas e o centro do quadrado (Fig. 22-42)")
a15 = 6.00e-6
cargas15 = [(e, 0, a15), (e, a15, 0), (2 * e, 0, 0)]
Ex15 = sum(campo_pontual(q, x, y, a15 / 2, a15 / 2)[0] for q, x, y in cargas15)
Ey15 = sum(campo_pontual(q, x, y, a15 / 2, a15 / 2)[1] for q, x, y in cargas15)
mostra("P15: distância de cada carga a P, a/√2", a15 / math.sqrt(2) * 1e6, unidade="µm")
mostra("P15: E1 = E2 = k e /(a²/2)", k * e / (a15**2 / 2), unidade="N/C")
mostra("P15(a): |E| = k(2e)/(a²/2) = 4ke/a²", math.hypot(Ex15, Ey15), gabarito=160, unidade="N/C")
mostra("P15(b): ângulo", angulo(Ex15, Ey15), gabarito=45, unidade="°")
mostra("P15 e se q3 = -2e: ângulo", angulo(*[sum(c) for c in zip(*[campo_pontual(q, x, y, a15/2, a15/2) for q, x, y in [(e, 0, a15), (e, a15, 0), (-2*e, 0, 0)]])]), unidade="°")
mostra("P15 e se q1 = +2e (q2, q3 iguais): |E|", math.hypot(*[sum(c) for c in zip(*[campo_pontual(q, x, y, a15/2, a15/2) for q, x, y in [(2*e, 0, a15), (e, a15, 0), (2*e, 0, 0)]])]), unidade="N/C")

# ---------------------------------------------------------------------------
titulo("DEGRAU 4 — arcos")


def campo_arco(Q, r, phi, n=200000):
    """Campo (Ex, Ey) no centro de um arco de abertura phi, simétrico em torno
    do semieixo -x... aqui: arco centrado na direção +x (elementos em ângulo θ
    de -phi/2 a +phi/2), carga Q uniforme. Soma numérica de pedacinhos."""
    lam = Q / (r * phi)
    Ex = Ey = 0.0
    dth = phi / n
    for i in range(n):
        th = -phi / 2 + (i + 0.5) * dth
        dq = lam * r * dth
        dE = k * dq / r**2
        Ex += -dE * math.cos(th)   # positivo: aponta para longe do elemento
        Ey += -dE * math.sin(th)
    return Ex, Ey


def campo_arco_formula(Q, r, phi):
    return 2 * k * (Q / (r * phi)) * math.sin(phi / 2) / r


# Exemplo 22.03: arco de 120°, carga -Q; em unidades de kQ/r²
fator_120 = campo_arco_formula(1, 1, math.radians(120)) / k
mostra("Ex. 22.03: E/(kQ/r²) para 120° [3√3/(2π)]", fator_120, gabarito=3 * math.sqrt(3) / (2 * math.pi))
mostra("  em Q/(ε0 r²): fator/(4π)", fator_120 / (4 * math.pi))
Exn, Eyn = campo_arco(1.0, 1.0, math.radians(120), n=20000)
mostra("  conferência numérica (soma de 20000 pedaços)", math.hypot(Exn, Eyn) / k, gabarito=fator_120)
# Lacuna: Problema 71 (ímpar): Q = 20 nC, comprimento 4,0 m, raio 2,0 m
phi71 = 4.0 / 2.0
lam71 = 20e-9 / 4.0
mostra("Lacuna P71: ângulo do arco (rad)", phi71)
mostra("Lacuna P71: λ", lam71, unidade="C/m")
mostra("Lacuna P71: E = 2kλ sen(φ/2)/r", 2 * k * lam71 * math.sin(phi71 / 2) / 2.0, gabarito=38, unidade="N/C")
# W4: razão E_arco / E_ponto = sen(φ/2)/(φ/2)
for graus in (10, 60, 120, 180, 270, 360):
    phi = math.radians(graus)
    mostra(f"W4: E_arco/E_ponto para φ = {graus}°", math.sin(phi / 2) / (phi / 2))
# Pergunta 11 (ímpar): arcos de 90° com carga Q cada; E em unidades de E_a
Ea = campo_arco_formula(1, 1, math.radians(90))


def soma_quartos(cargas):
    """cargas: lista (Q, ângulo central do quarto em graus). Retorna |E|/Ea."""
    Ex = Ey = 0.0
    for Q, c in cargas:
        mag = Q * Ea   # com sinal: + aponta para longe do arco (sentido oposto a c)
        Ex += -mag * math.cos(math.radians(c))
        Ey += -mag * math.sin(math.radians(c))
    return math.hypot(Ex, Ey) / Ea


p11 = {"a": [(1, 45)], "b": [(1, 45), (1, 135)], "c": [(1, 45), (1, 135), (1, 225)],
       "d": [(1, 45), (1, 135), (1, 225), (1, 315)], "e": [(1, 45), (1, 135), (1, 225), (-1, 315)]}
for nome, c in p11.items():
    mostra(f"Pergunta 11 ({nome}): E/E_a  (gabarito: e, b, a=c, d)", soma_quartos(c))

# ---------------------------------------------------------------------------
titulo("P29 — semicírculo × carga pontual (Fig. 22-52)")
# E_arco = 2kλ/R com λ = Q/(πR) -> 2kQ/(πR²); E_ponto = kQ/R²
mostra("P29: E_arco em kQ/R² (2/π)", 2 / math.pi)
mostra("P29: E_novo/E_antigo = π/2", math.pi / 2, gabarito=1.57)
Exs, Eys = campo_arco(1.0, 1.0, math.pi, n=20000)
mostra("  conferência numérica 1/(E_arco/kQR⁻²)", 1 / (math.hypot(Exs, Eys) / k), gabarito=1.57)

titulo("P26 — semicírculo com metade + e metade - (Fig. 22-50)")
q26 = 4.50e-12
r26 = 0.0500
lam26 = q26 / (math.pi * r26 / 2)
mostra("P26: λ de cada quarto = q/(πr/2)", lam26, unidade="C/m")
mostra("P26: E de um quarto, componente y = kλ/r", k * lam26 / r26, unidade="N/C")
E26 = mostra("P26(a): |E| = 2kλ/r = 4kq/(πr²)", 4 * k * q26 / (math.pi * r26**2), unidade="N/C")
mostra("P26(a): pela forma q/(π² ε0 r²)", q26 / (math.pi**2 * eps0 * r26**2), unidade="N/C")
# conferência numérica: semicírculo à esquerda (θ de 90° a 270°); + em cima, - embaixo
n = 40000
Ex = Ey = 0.0
for i in range(n):
    th = math.pi / 2 + (i + 0.5) * math.pi / n
    q_el = (q26 if th < math.pi else -q26) / (n / 2)
    fx, fy = campo_pontual(q_el, r26 * math.cos(th), r26 * math.sin(th), 0, 0)
    Ex += fx
    Ey += fy
mostra("  conferência numérica |E|", math.hypot(Ex, Ey), gabarito=E26, unidade="N/C")
mostra("P26(b): ângulo", angulo(Ex, Ey), unidade="°")
mostra("P26 e se tudo fosse +q (carga 2q): |E| = 2k(2q/(πr))/r", 2 * k * (2 * q26 / (math.pi * r26)) / r26, unidade="N/C")
mostra("P27 (ímpar, revisão): círculo inteiro ±, R = 8,50 cm, q = 15,0 pC", 4 * k * 15e-12 / (math.pi * 0.085**2) * 1, gabarito=23.8, unidade="N/C")

# ---------------------------------------------------------------------------
titulo("DEGRAU 5 — barra reta")
# Ex. resolvido: L = 10 cm, q = +5,0 nC, P a a = 5,0 cm da ponta
Lb, qb, ab = 0.10, 5e-9, 0.05
mostra("Ex. D5: E = kq/(a(a+L))", k * qb / (ab * (ab + Lb)), unidade="N/C")
mostra("Ex. D5: carga pontual no centro (10 cm)", k * qb / (ab + Lb / 2) ** 2, unidade="N/C")
mostra("Ex. D5: carga pontual na ponta (5 cm)", k * qb / ab**2, unidade="N/C")
mostra("Ex. D5: carga pontual na ponta longe (15 cm)", k * qb / (ab + Lb) ** 2, unidade="N/C")
mostra("Ex. D5: média geométrica √(a(a+L)) em cm", math.sqrt(ab * (ab + Lb)) * 100, unidade="cm")
# conferência numérica
n = 100000
soma = sum(k * (qb / n) / (ab + (i + 0.5) * Lb / n) ** 2 for i in range(n))
mostra("  conferência numérica", soma, gabarito=k * qb / (ab * (ab + Lb)), unidade="N/C")
# Lacuna: Problema 67 (ímpar): λ = 9,0 nC/m, x de 0 a 3,0 m, P em x = 4,0 m
mostra("Lacuna P67: E = kλL/(a(a+L)), a = 1,0 m, L = 3,0 m", k * 9e-9 * 3.0 / (1.0 * 4.0), gabarito=61, unidade="N/C")
# W5: razão E_barra / E_ponto(centro) = 1/(1 - (L/2D)²)
for D_L in (0.6, 1, 2, 5, 10):
    mostra(f"W5: E_barra/E_ponto com D = {D_L} L", 1 / (1 - (1 / (2 * D_L)) ** 2))

titulo("P31 — barra no eixo x (Fig. 22-54)")
L31, q31, a31 = 0.0815, 4.23e-15, 0.120
mostra("P31(a): λ = -q/L", -q31 / L31, gabarito=-5.19e-14, unidade="C/m")
E31 = mostra("P31(b): |E| = kq/(a(a+L))", k * q31 / (a31 * (a31 + L31)), gabarito=1.57e-3, unidade="N/C")
n = 100000
soma31 = sum(k * (q31 / n) / (a31 + (i + 0.5) * L31 / n) ** 2 for i in range(n))
mostra("  conferência numérica", soma31, gabarito=E31, unidade="N/C")
mostra("P31(c): direção (para a barra, -x): 180° ≡ -180°", 180.0, gabarito=180, unidade="°")
D31 = 50.0
Ed = mostra("P31(d): barra, D = 50 m do centro: kq/(D² - L²/4)", k * q31 / (D31**2 - L31**2 / 4), gabarito=1.52e-8, unidade="N/C")
Ee = mostra("P31(e): carga pontual a 50 m: kq/D²", k * q31 / D31**2, gabarito=1.52e-8, unidade="N/C")
mostra("P31: diferença relativa (d)-(e)", (Ed - Ee) / Ee)
mostra("P31 e se a = 0,5 cm: E_barra / E_ponto(centro)", (k * q31 / (0.005 * 0.0865)) / (k * q31 / (0.005 + L31 / 2) ** 2))

# ---------------------------------------------------------------------------
titulo("DEGRAU 6 — disco")


def disco(sigma, R, z):
    return sigma / (2 * eps0) * (1 - z / math.sqrt(z**2 + R**2))


# Ex. resolvido: Problema 34 (par): R = 2,5 cm, σ = 5,3 µC/m², z = 12 cm
s34, R34, z34 = 5.3e-6, 0.025, 0.12
mostra("Ex. P34: σ/(2ε0)", s34 / (2 * eps0), unidade="N/C")
mostra("Ex. P34: fator (1 - z/√(z²+R²))", 1 - z34 / math.sqrt(z34**2 + R34**2))
E34 = mostra("Ex. P34: E", disco(s34, R34, z34), unidade="N/C")
Q34 = s34 * math.pi * R34**2
mostra("Ex. P34: Q = σπR²", Q34, unidade="C")
Ep34 = mostra("Ex. P34: conferência carga pontual kQ/z²", k * Q34 / z34**2, unidade="N/C")
mostra("Ex. P34: diferença relativa (ponto - disco)/disco", (Ep34 - E34) / E34)
# conferência numérica por anéis
n = 200000
soma = 0.0
for i in range(n):
    rr = (i + 0.5) * R34 / n
    dq = s34 * 2 * math.pi * rr * (R34 / n)
    soma += k * dq * z34 / (z34**2 + rr**2) ** 1.5
mostra("  conferência numérica (soma de anéis)", soma, gabarito=E34, unidade="N/C")
# Lacuna: Problema 35 (ímpar): R = 0,600 m, E = Em/2
mostra("Lacuna P35: z = R/√3", 0.600 / math.sqrt(3), gabarito=0.346, unidade="m")
# Pergunta 9 (ímpar): mesma Q; (a) disco R, (b) disco 2R, (c) anel R..2R; P a altura h
h = 1.0  # escala arbitrária: P à mesma altura; testar várias alturas


def disco_Q(Q, Rin, Rout, z):
    sigma = Q / (math.pi * (Rout**2 - Rin**2))
    return sigma / (2 * eps0) * (z / math.sqrt(z**2 + Rin**2) - z / math.sqrt(z**2 + Rout**2))


for hz in (0.5, 1.0, 2.0):
    va = disco_Q(1e-9, 0, 1, hz)
    vb = disco_Q(1e-9, 0, 2, hz)
    vc = disco_Q(1e-9, 1, 2, hz)
    mostra(f"Pergunta 9, z = {hz}R: a > b > c ? (a/b, b/c)", va / vb)
    mostra(f"                       b/c", vb / vc)

titulo("P38 — raio do disco pelo gráfico (Fig. 22-58)")
z_meio = 0.040   # lido no gráfico: E = 0,5 Em em z = 4,0 cm (zs = 8,0 cm)
R38 = mostra("P38: R = √3 · z_meio", math.sqrt(3) * z_meio * 100, unidade="cm")
mostra("P38: conferência E/Em em z = 4,0 cm", 1 - 0.04 / math.sqrt(0.04**2 + (R38 / 100) ** 2), gabarito=0.5)
mostra("P38: E/Em em z = 2,0 cm (gráfico ≈ 0,72)", 1 - 0.02 / math.sqrt(0.02**2 + (R38 / 100) ** 2), gabarito=0.725, ref="leitura do gráfico (±0,01)", tol=0.05)
mostra("P38: E/Em em z = 8,0 cm (gráfico ≈ 0,24)", 1 - 0.08 / math.sqrt(0.08**2 + (R38 / 100) ** 2), gabarito=0.239, ref="leitura do gráfico (±0,01)", tol=0.05)
mostra("P38 e se E/Em = 0,25 em z = 4 cm: R = z√((1/(0,75²))-1)", 0.04 * math.sqrt(1 / 0.75**2 - 1) * 100, unidade="cm")
# W6: aproximações
for zr in (0.1, 0.577, 1, 3, 10):
    disco_n = 1 - zr / math.sqrt(zr**2 + 1)
    ponto_n = 1 / (2 * zr**2)
    mostra(f"W6: z/R = {zr}: disco E/Em", disco_n)
    mostra(f"     carga pontual E/Em = R²/(2z²)", ponto_n)

# ---------------------------------------------------------------------------
titulo("Revisão intercalada e plano de revisão (ímpares do livro)")
mostra("P5: |q| = E r²/k (2,0 N/C a 50 cm)", 2.0 * 0.5**2 / k, gabarito=56e-12, unidade="C")
mostra("P41(a): E = F/|q|", 3.0e-6 / 2.0e-9, gabarito=1.5e3, unidade="N/C")
mostra("P41(b): F no próton", e * 1.5e3, gabarito=2.4e-16, unidade="N")
mostra("P7: E no centro do quadrado (só y)", abs(sum(campo_pontual(q, x, y, 0.025, 0.025)[1] for q, x, y in
       [(10e-9, 0, 0.05), (-20e-9, 0.05, 0.05), (20e-9, 0, 0), (-10e-9, 0.05, 0)])), gabarito=1.02e5, unidade="N/C")
# P23: anel em z: E = kqz/(z²+R²)^1,5. Anel 1 a z = R, anel 2 a z = 2R (em unidades de R)
mostra("P23: q1/q2 (anéis, d = 3R, P a R do anel 1)",
       (2 / (2**2 + 1) ** 1.5) / (1 / (1**2 + 1) ** 1.5), gabarito=0.506)
mostra("P37: redução % (disco -> anel R/2..R, P a 2R)",
       100 * (1 - (2 / math.sqrt(4 + 0.25) - 2 / math.sqrt(5)) / (1 - 2 / math.sqrt(5))), gabarito=28)

# ---------------------------------------------------------------------------
titulo("Valores de erros comuns (o verificador do guia reconhece e explica)")
mostra("P81 erro: W·E", 4.4 * 150)
mostra("P81 erro: E/W", 150 / 4.4)
mostra("P81 e se E = 3e6 N/C: campo na superfície com q = W/E", k * (W / E_RUPTURA) / R_S**2, unidade="N/C")
mostra("P8 erro: E3 + E4", E3 + E4, unidade="N/C")
mostra("P8 erro: E1 + E2", 2 * E1, unidade="N/C")
mostra("P8 erro: soma de todos os módulos", 2 * E1 + E3 + E4, unidade="N/C")
mostra("P9 erro: uma carga só", E9, unidade="N/C")
mostra("P9 erro: 2E (somou módulos)", 2 * E9, unidade="N/C")
mostra("P9 erro: 2E·(4/5)", 2 * E9 * 0.8, unidade="N/C")
mostra("P15 erro: k(2e)/a² (r = a)", k * 2 * e / a15**2, unidade="N/C")
mostra("P15 erro: ke/a²", k * e / a15**2, unidade="N/C")
mostra("P15 erro: soma de módulos 80+80+160", 2 * k * e / (a15**2 / 2) + 4 * k * e / a15**2, unidade="N/C")
mostra("P26 erro: um quarto só", k * lam26 / r26, unidade="N/C")
mostra("P26 erro: dobrou (2 × 20,6)", 2 * E26, unidade="N/C")
mostra("P29 erro: inverso 2/π", 2 / math.pi)
mostra("P29 erro: λ = Q/R", 0.5)
mostra("P29 erro: sem o fator 2", math.pi)
mostra("P29 e se fosse um quarto de círculo: E_ponto/E_arco", (math.pi / 4) / math.sin(math.pi / 4))
mostra("P31 erro: kq/a² (toda a carga na ponta perto)", k * q31 / a31**2, unidade="N/C")
mostra("P31 erro: kq/(a+L)² (ponta longe)", k * q31 / (a31 + L31) ** 2, unidade="N/C")
mostra("P31 erro: kq/(a+L/2)² (centro)", k * q31 / (a31 + L31 / 2) ** 2, unidade="N/C")
mostra("P31: número de elétrons na barra q/e", q31 / e)
mostra("P38 erro: z/√3", 4.0 / math.sqrt(3), unidade="cm")
mostra("P38 erro: 2√3 z", 2 * math.sqrt(3) * 4.0, unidade="cm")
mostra("Ficha: σ máximo antes da ruptura (σ/2ε0 = 3e6)", 2 * eps0 * E_RUPTURA, unidade="C/m²")

# ---------------------------------------------------------------------------
titulo("V2 — números novos pedidos pela rodada 1")
# prev-w2 novo: +1 nC a 1 cm à esquerda e +4 nC a 3 cm à direita (o mais perto ganha)
mostra("prev-w2 v2: E de +1 nC a 1 cm (→)", k * 1e-9 / 0.01**2, unidade="N/C")
mostra("prev-w2 v2: E de +4 nC a 3 cm (←)", k * 4e-9 / 0.03**2, unidade="N/C")
mostra("prev-w2 v2: total (+ = direita)", k * 1e-9 / 0.01**2 - k * 4e-9 / 0.03**2, unidade="N/C")
# lacuna D2 v2: +1 nC em x=+1 cm e -3 nC em x=+2 cm (mesmo lado, sinais opostos, não cancela)
EC2 = k * 1e-9 / 0.01**2
ED2 = k * 3e-9 / 0.02**2
mostra("lacuna D2 v2: E_C (-x)", EC2, unidade="N/C")
mostra("lacuna D2 v2: E_D (+x)", ED2, unidade="N/C")
lac2 = sum(campo_pontual(q, x, 0, 0, 0)[0] for q, x in [(1e-9, 0.01), (-3e-9, 0.02)])
mostra("lacuna D2 v2: E_x total (negativo = -x)", lac2, unidade="N/C")
mostra("lacuna D2 v2 erro: somou módulos", EC2 + ED2, unidade="N/C")
mostra("lacuna D2 v2 erro: r=1 cm para D", k * 3e-9 / 0.01**2, unidade="N/C")
# feedbacks corrigidos
mostra("lac-a-3 erro: calculadora em graus 2kλ sen(1°)/r", 2 * k * 5e-9 * math.sin(math.radians(1)) / 2.0, unidade="N/C")
mostra("lac-r-1 erro: r = 1 m em vez de 0,010 m", k * 1e-9 / 1.0**2, unidade="N/C")
mostra("lac-b-2 erro: a = 4,0 m na fórmula (kλL/(a(a+L)))", k * 9e-9 * 3.0 / (4.0 * 7.0), unidade="N/C")
mostra("lac-b-2 erro: carga toda na ponta longe kq/(4 m)²", k * 27e-9 / 4.0**2, unidade="N/C")
mostra("lac-mil-1 erro: massa em gramas", m_gota * 1000, unidade="g")
# prev-w6 novo: E/Em em z = R
mostra("prev-w6 v2: E/Em em z = R (1 - 1/√2)", 1 - 1 / math.sqrt(2))
# desafio D3: P15 com q1 = +2e
v = [sum(c) for c in zip(*[campo_pontual(q, x, y, a15/2, a15/2) for q, x, y in [(2*e, 0, a15), (e, a15, 0), (2*e, 0, 0)]])]
mostra("desafio D3 (P15 com q1=+2e): |E|", math.hypot(*v), unidade="N/C")
mostra("desafio D3: ângulo com +x", angulo(*v), unidade="°")
mostra("desafio D3: Ex", v[0], unidade="N/C")
mostra("desafio D3: Ey", v[1], unidade="N/C")
mostra("desafio D3 erro: atan(Ey/Ex) ok aqui (1º quadrante)", math.degrees(math.atan(v[1]/v[0])), unidade="°")
# hidrogênio: verificação nova (força / peso do elétron)
mostra("Ex. H v2: F elétrica / peso do elétron", 8.245e-8 / (m_e * g))
# W5 v2: erro relativo ao valor certo = (L/2D)²
for D_L in (0.6, 1, 2, 5, 10):
    mostra(f"W5 v2: erro (%) do ponto com D = {D_L} L", 100 * (1 / (2 * D_L)) ** 2)
# disco: σ em cada face (folha fina) -> σ_total
mostra("D6 v2: 5,3 µC/m² em cada face: E_m = σ_total/(2ε0)", 2 * 5.3e-6 / (2 * eps0), unidade="N/C")
mostra("D6 v2: σ do P34 / σ máximo antes da ruptura", 5.3e-6 / (2 * eps0 * E_RUPTURA))
mostra("D6 v2: erro do ponto no disco ~ 0,75 (R/z)² em z/R = 4,8", 0.75 / 4.8**2)
mostra("  exato em z/R = 4,8: (ponto-disco)/disco", ((1/(2*4.8**2)) - (1 - 4.8/math.sqrt(4.8**2+1))) / (1 - 4.8/math.sqrt(4.8**2+1)))
# P31 figura em escala: a/L
mostra("P31: a/L (para desenhar em escala)", a31 / L31)

# ---------------------------------------------------------------------------
titulo("Reteste (rodada 2): exercícios novos de transferência")
# arco de 90°, raio 10 cm, +2,0 nC: campo no centro
phi_t = math.pi / 2
lam_t = 2e-9 / (0.10 * phi_t)
mostra("Reteste A: λ do arco de 90° (r = 10 cm, 2,0 nC)", lam_t, unidade="C/m")
mostra("Reteste A: E = 2kλ sen(φ/2)/r", 2 * k * lam_t * math.sin(phi_t / 2) / 0.10, unidade="N/C")
mostra("Reteste A: conferência numérica", math.hypot(*campo_arco(2e-9, 0.10, phi_t, n=20000)), unidade="N/C")
mostra("Reteste A erro: carga toda num ponto a 10 cm", k * 2e-9 / 0.10**2, unidade="N/C")
# barra de 20 cm, +4,0 nC, P no prolongamento a 10 cm da ponta
mostra("Reteste B: E = kq/(a(a+L)), L = 20 cm, a = 10 cm, q = 4,0 nC", k * 4e-9 / (0.10 * 0.30), unidade="N/C")
mostra("Reteste B erro: carga no centro (20 cm)", k * 4e-9 / 0.20**2, unidade="N/C")

print("\nResumo: linhas com divergência > 2 %:")
div = [l for l in LINHAS if "DIVERGE" in l]
print("\n".join(div) if div else "  nenhuma")
