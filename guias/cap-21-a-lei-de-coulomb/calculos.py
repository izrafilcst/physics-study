#!/usr/bin/env python3
"""Contas do guia do Capítulo 21 (A Lei de Coulomb).

Rodar com:  python3 -I calculos.py
Cada linha mostra: rótulo · valor calculado · valor do gabarito (se existir) · status.
Status "DIVERGE" = diferença relativa > 2 % em relação ao gabarito do livro.
Só biblioteca padrão (sem numpy).
"""
import math

# ---------------------------------------------------------------- constantes (valores do livro)
k = 8.99e9            # N·m²/C²   (1/4πε0)
eps0 = 8.85e-12       # C²/(N·m²)
e = 1.602e-19         # C
m_e = 9.109e-31       # kg
m_p = 1.67e-27        # kg (Exemplo 21.04 usa 1,67e-27)
G = 6.67e-11          # N·m²/kg²
g = 9.8               # m/s²

divergencias = []


def br(v, s=3):
    """Formata em notação científica pt-BR com s algarismos significativos."""
    if v == 0:
        return "0"
    exp = int(math.floor(math.log10(abs(v))))
    man = v / 10 ** exp
    man = round(man, s - 1)
    if abs(man) >= 10:
        man /= 10
        exp += 1
    txt = f"{man:.{s-1}f}".replace(".", ",")
    return txt if exp == 0 else f"{txt} × 10^{exp}"


def algs(txt):
    """Número de algarismos significativos de um valor escrito como no livro ('1,3e7', '-14', '2,00e10')."""
    man = txt.lower().split("e")[0].replace("-", "").replace("+", "").replace(",", "").replace(".", "")
    return len(man.lstrip("0")) or 1


def arred(v, s):
    if v == 0:
        return 0.0
    return round(v, -int(math.floor(math.log10(abs(v)))) + (s - 1))


def item(rotulo, valor, unidade="", gabarito=None, s=3, tol_abs=None, nota=""):
    """gabarito: string como no livro (ex.: '1,3e7') ou número; 0 usa tol_abs."""
    linha = f"  {rotulo:<58} = {br(valor, s):>18} {unidade:<7}"
    if gabarito is not None:
        g_txt = gabarito if isinstance(gabarito, str) else repr(gabarito)
        gval = float(g_txt.replace(",", "."))
        if gval == 0:
            ok = abs(valor) <= (tol_abs if tol_abs is not None else 1e-12)
            dif = 0.0 if ok else float("inf")
            status = "ok" if ok else "DIVERGE"
        else:
            dif = abs(valor - gval) / abs(gval)
            if dif <= 0.02:
                status = "ok"
            elif isinstance(gabarito, str) and arred(valor, algs(g_txt)) == arred(gval, algs(g_txt)):
                status = f"ok (igual com {algs(g_txt)} alg. signif. do gabarito)"
            else:
                status = "DIVERGE"
        linha += f" | gabarito {br(gval, s):>12}  ({dif*100:5.2f} %) {status}"
        if status == "DIVERGE":
            divergencias.append(rotulo + (f" — {nota}" if nota else ""))
    else:
        linha += " | sem gabarito (calculado pelo guia)"
    if nota:
        linha += f"  [{nota}]"
    print(linha)
    return valor


def coulomb(q1, q2, r):
    return k * abs(q1) * abs(q2) / r ** 2


def secao(t):
    print("\n" + "=" * 100 + f"\n{t}\n" + "=" * 100)


# ================================================================= DEGRAU 0 — gancho
secao("DEGRAU 0 — Aquecimento (gancho: a carga de um copo d'água)")
massa_agua = 250.0          # g  (250 cm³)
M_agua = 18.015             # g/mol
N_A = 6.022e23
moleculas = massa_agua / M_agua * N_A
q_copo = item("P33: carga positiva em 250 cm³ de água", moleculas * 10 * e, "C", gabarito="1,3e7", s=2)
F_dois_copos = item("Força entre duas cargas q_copo a 1,00 m", k * q_copo ** 2 / 1.0 ** 2, "N")
F_sol_terra = item("Atração gravitacional Sol–Terra (comparação)", G * 1.989e30 * 5.972e24 / 1.496e11 ** 2, "N")
item("Razão F_dois_copos / F_sol_terra", F_dois_copos / F_sol_terra, "", s=2)

# ================================================================= DEGRAU 1 — par de cargas
secao("DEGRAU 1 — Duas cargas: módulo e sentido")
item("P5 (exemplo resolvido): F entre 3,00 µC e -1,50 µC a 12,0 cm", coulomb(3.00e-6, -1.50e-6, 0.120), "N", gabarito=2.81)
item("P3 (exemplo com lacunas): r para F = 5,70 N (26,0 µC; -47,0 µC)",
     math.sqrt(k * 26.0e-6 * 47.0e-6 / 5.70), "m", gabarito=1.39)
F_pp = item("Ex. 21.04a: dois prótons a 4,0e-15 m (elétrica)", coulomb(e, e, 4.0e-15), "N", gabarito="14", s=2)
F_pg = item("Ex. 21.04b: mesmos prótons (gravitacional)", G * m_p ** 2 / (4.0e-15) ** 2, "N", gabarito="1,2e-35", s=2)
item("Razão elétrica/gravitacional para dois prótons", F_pp / F_pg, "", s=2)
item("Checkpoint D1: F entre +2,0 µC e -2,0 µC a 3,0 cm", coulomb(2.0e-6, -2.0e-6, 0.030), "N", s=2)
item("Ficha: P26 Na+ e Cl- a 2,82e-10 m", coulomb(e, e, 2.82e-10), "N")
item("Ficha: P4 carga do relâmpago (2,5e4 A × 20 µs)", 2.5e4 * 20e-6, "C", s=2)

# ================================================================= DEGRAU 2 — superposição na reta
secao("DEGRAU 2 — Superposição na reta: onde a força se anula")
# Ex. 21.02: q1 = +8q em 0, q2 = -2q em L. Ponto à direita de q2: 8/x² = 2/(x-L)²  ->  x = 2L
L = 1.0
x = None
# resolver 8 (x-L)^2 = 2 x^2  (x > L)
a_, b_, c_ = 8 - 2, -16 * L, 8 * L ** 2
x1 = (-b_ + math.sqrt(b_ ** 2 - 4 * a_ * c_)) / (2 * a_)
item("Ex. 21.02 (exemplo resolvido): posição de equilíbrio (em unidades de L)", x1, "L", gabarito=2.0)
# P13: q1=+1 µC em 0, q2=-3 µC em L=10 cm; ponto à esquerda de q1 a distância s: 1/s² = 3/(s+L)²
Lc = 10.0  # cm
s13 = Lc / (math.sqrt(3) - 1)
item("P13 (exemplo com lacunas): coordenada x do ponto de força nula", -s13, "cm", gabarito="-14", s=2)
# P7
item("P7: q1/q2 (L23 = L12)", -((1 + 1) ** 2) / 1 ** 2, "", gabarito=-4.00)
item("P7 'e se' (= P40): q1/q2 com L23 = 2 L12", -((1 + 2) ** 2) / 2 ** 2, "")
item("P7 caso-limite: L23 = 1000 L12", -((1 + 1000) ** 2) / 1000 ** 2, "", s=4)
# Revisão: +q e +4q separadas por L; ponto de força nula entre elas
item("Revisão: +q e +4q, ponto nulo a partir de +q (em L)", 1 / (1 + 2), "L")

# ================================================================= DEGRAU 3 — força elétrica na mecânica
secao("DEGRAU 3 — A força elétrica entra na mecânica")
# exemplo resolvido: pêndulo
m_b, q_b, Q_b, r_b = 2.0e-3, 50e-9, 20e-9, 0.040
F_b = item("Ex. resolvido D3: força elétrica na bolinha (50 nC, 20 nC, 4,0 cm)", coulomb(q_b, Q_b, r_b), "N")
P_b = item("Ex. resolvido D3: peso da bolinha (2,0 g)", m_b * g, "N")
item("Ex. resolvido D3: ângulo do fio θ = atan(F/mg)", math.degrees(math.atan(F_b / P_b)), "graus")
item("Ex. resolvido D3: tração T", math.hypot(F_b, P_b), "N")
for th in (1, 5, 10, 20, 30):
    t = math.radians(th)
    item(f"Ângulo pequeno: (tan θ / sen θ - 1) para θ = {th}°", (math.tan(t) / math.sin(t) - 1) * 100, "%", s=2)
# exemplo com lacunas: P52 (MCU em torno de Q)
m52, q52, r52, v52 = 0.800e-3, 4.00e-6, 0.200, 50.0
item("P52 (exemplo com lacunas): |Q| para MCU", m52 * v52 ** 2 * r52 / (k * q52), "C", nota="Q negativo")
# mini-exemplo de torque
F_t = item("Mini-ex. torque: força entre 1,0 µC e 1,0 µC a 10 cm", coulomb(1e-6, 1e-6, 0.10), "N")
item("Mini-ex. torque: peso a 25 cm do apoio (lado direito)", F_t * 0.50 / 0.25, "N")
# P42
L42, m42, x42 = 1.20, 10e-3, 0.050
q42 = item("P42(b): |q|", math.sqrt(2 * math.pi * eps0 * m42 * g * x42 ** 3 / L42), "C", s=2)
th42 = (x42 / 2) / L42
item("P42 verificação: θ ≈ (x/2)/L", math.degrees(th42), "graus")
item("P42 verificação: F elétrica = k q²/x²", coulomb(q42, q42, x42), "N")
item("P42 verificação: F/(mg) (deve ≈ tan θ)", coulomb(q42, q42, x42) / (m42 * g), "")
item("P42 verificação: tan θ", math.tan(math.asin(th42)), "")
item("P43(b) (consistência): x' = x / 4^(1/3)", x42 * 100 / 4 ** (1 / 3), "cm", gabarito=3.1, s=2)
item("P42 'e se': fator em x quando q dobra (2^(2/3))", 2 ** (2 / 3), "")
# P50 — teste numérico das expressões simbólicas
L50, q50, Q50, h50, P50 = 1.00, 1.00e-6, 2.00e-6, 0.100, 10.0
F1 = coulomb(q50, Q50, h50)         # esquerda (+q)
F2 = coulomb(2 * q50, Q50, h50)     # direita (+2q)
x50 = item("P50(a) teste: x = (L/2)(1 + kqQ/(P h²)) com L=1 m, q=1 µC, Q=2 µC, h=10 cm, P=10 N",
           L50 / 2 * (1 + k * q50 * Q50 / (P50 * h50 ** 2)) * 100, "cm")
tau = (L50 / 2) * F2 - (L50 / 2) * F1 - P50 * (x50 / 100 - L50 / 2)
item("P50(a) teste: torque resultante em relação ao apoio (deve ser 0)", tau, "N·m", gabarito=0, tol_abs=1e-12)
h50b = item("P50(b) teste: h = sqrt(3kqQ/P)", math.sqrt(3 * k * q50 * Q50 / P50) * 100, "cm")
item("P50(b) teste: F1 + F2 - P com esse h (deve ser 0)",
     coulomb(q50, Q50, h50b / 100) + coulomb(2 * q50, Q50, h50b / 100) - P50, "N", gabarito=0, tol_abs=1e-9)
item("P50 curiosidade: x/L quando h é o do item (b)", 0.5 * (1 + 1 / 3), "L")
item("P50 'e se' (cargas trocadas, 2q à esquerda): x com valores-teste",
     L50 / 2 * (1 - k * q50 * Q50 / (P50 * h50 ** 2)) * 100, "cm")
# P73
a0 = 52.92e-12
def v_bohr(n):
    return math.sqrt(k * e ** 2 / (m_e * n ** 2 * a0))
item("P73(a): v na órbita n = 1", v_bohr(1), "m/s", gabarito=2.19e6)
item("P73(b): v na órbita n = 2", v_bohr(2), "m/s", gabarito=1.09e6)
item("P73 extra: v na órbita n = 3 (revisão)", v_bohr(3), "m/s")
item("P73 verificação: v1/c", v_bohr(1) / 2.998e8 * 100, "%", s=2)
item("P73 verificação: força elétrica em n = 1", coulomb(e, e, a0), "N")

# ================================================================= DEGRAU 4 — superposição no plano
secao("DEGRAU 4 — Superposição no plano: componentes e simetria")
R = 0.0200
F12 = item("Ex. 21.01c: F12 (q1=1,60e-19, q2=3,20e-19, R=2,00 cm)", coulomb(1.60e-19, 3.20e-19, R), "N", gabarito=1.15e-24)
F14 = item("Ex. 21.01c: F14 (q4=-3,20e-19 a 3R/4)", coulomb(1.60e-19, 3.20e-19, 0.75 * R), "N", gabarito=2.05e-24)
# O livro arredonda F12 e F14 para 3 algarismos ANTES de somar; o guia reproduz isso (é o que o aluno faz):
F12r, F14r = 1.15e-24, 2.05e-24
Fx = item("Ex. 21.01c: componente x (com F12, F14 arredondados como no livro)", -F12r + F14r * math.cos(math.radians(60)), "N", gabarito=-1.25e-25)
Fy = item("Ex. 21.01c: componente y (idem)", F14r * math.sin(math.radians(60)), "N", gabarito=1.78e-24)
item("Ex. 21.01c: módulo da resultante", math.hypot(Fx, Fy), "N", gabarito=1.78e-24)
item("Ex. 21.01c: atan(Fy/Fx) da calculadora", math.degrees(math.atan(Fy / Fx)), "graus", nota="ângulo 'errado'")
item("Ex. 21.01c: ângulo correto (atan2)", math.degrees(math.atan2(Fy, Fx)), "graus", gabarito=94.0)
Fx_full = -F12 + F14 * math.cos(math.radians(60))
Fy_full = F14 * math.sin(math.radians(60))
item("Ex. 21.01c (nota): componente x sem arredondar no meio", Fx_full, "N",
     nota="difere 2 % do livro só por arredondamento intermediário")
item("Ex. 21.01c (nota): ângulo sem arredondar no meio", math.degrees(math.atan2(Fy_full, Fx_full)), "graus")
# P11 (exemplo com lacunas): mesma figura do P10
a = 0.050
q1, q2, q3, q4 = 100e-9, -100e-9, 200e-9, -200e-9
pos = {1: (0, a), 2: (a, a), 3: (0, 0), 4: (a, 0)}
carga = {1: q1, 2: q2, 3: q3, 4: q4}
def forca_sobre(i, cargas, posicoes):
    fx = fy = 0.0
    xi, yi = posicoes[i]
    for j in cargas:
        if j == i:
            continue
        xj, yj = posicoes[j]
        dx, dy = xi - xj, yi - yj
        r = math.hypot(dx, dy)
        f = k * cargas[i] * cargas[j] / r ** 2      # >0 repulsão (sentido de j para i)
        fx += f * dx / r
        fy += f * dy / r
    return fx, fy
fx3, fy3 = forca_sobre(3, carga, pos)
item("P11 (exemplo com lacunas): componente x da força sobre 3", fx3, "N", gabarito=0.17, s=2)
item("P11 (exemplo com lacunas): componente y da força sobre 3", fy3, "N", gabarito=-0.046, s=2)
item("P11 parcial: força de 1 sobre 3 (módulo)", coulomb(q1, q3, a), "N")
item("P11 parcial: força de 2 sobre 3 (módulo, diagonal)", coulomb(q2, q3, math.sqrt(2) * a), "N")
item("P11 parcial: força de 4 sobre 3 (módulo)", coulomb(q4, q3, a), "N")
# P10
razao10 = -2 * math.sqrt(2)
item("P10(a): Q/q", razao10, "")
Qv, qv = 1e-6, 1e-6 / razao10
c10 = {1: Qv, 2: qv, 3: qv, 4: Qv}
f1 = forca_sobre(1, c10, pos)
f4 = forca_sobre(4, c10, pos)
f2 = forca_sobre(2, c10, pos)
item("P10 teste: |F| sobre 1 com Q/q = -2√2 (deve ser 0)", math.hypot(*f1), "N", gabarito=0, tol_abs=1e-9)
item("P10 teste: |F| sobre 4 com Q/q = -2√2 (deve ser 0)", math.hypot(*f4), "N", gabarito=0, tol_abs=1e-9)
item("P10(b): Q/q necessário para anular a força sobre 2", -1 / (2 * math.sqrt(2)), "")
F2_unid = math.hypot(*f2) / (k * qv ** 2 / a ** 2)
item("P10 'e se': |F| sobre 2 (em unidades de k q²/a²)", F2_unid, "", s=3)

# ================================================================= DEGRAU 5 — força que varia com a posição
secao("DEGRAU 5 — Força que varia com a posição: F(x), limites e máximo")
qd, q3d, dd = 1.0e-9, 1.0e-9, 0.030
item("Ex. resolvido D5 (dipolo): F(0) = 2kqq3/d² (1,0 nC; 1,0 nC; d = 3,0 cm)", 2 * k * qd * q3d / dd ** 2, "N", s=2)
item("Ex. resolvido D5: F(d)/F(0) = 1/2^(3/2)", 1 / 2 ** 1.5, "", s=3)
# lacuna: g(x) = x/(x²+a²), máximo em x = a, g(a) = 1/(2a)
amax = 1.0
xs = [i / 10000 for i in range(1, 50000)]
xm = max(xs, key=lambda x: x / (x ** 2 + amax ** 2))
item("Lacuna D5: máximo de x/(x²+a²) por varredura (a = 1)", xm, "a", gabarito=1.0)
# P23
q23, q3_23, d23 = 3.20e-19, 6.40e-19, 0.170
def F23(x):
    return 2 * k * q23 * q3_23 * x / (x ** 2 + d23 ** 2) ** 1.5
item("P23(a): x do mínimo (F(0) = 0)", 0.0, "cm", gabarito=0, tol_abs=1e-12)
xmax = item("P23(b): x do máximo = d/√2", d23 / math.sqrt(2) * 100, "cm", gabarito=12)
xs = [i * 1e-5 for i in range(0, 500001)]          # 0 a 5,0 m, passo 0,01 mm
xv = max(xs, key=F23)
item("P23(b) conferência por varredura (0 a 5,0 m)", xv * 100, "cm", gabarito=12)
item("P23(c): valor mínimo F(0)", F23(0.0), "N", gabarito=0, tol_abs=1e-40)
Fmax = item("P23(d): F máx = 4kqq3/(3√3 d²)", 4 * k * q23 * q3_23 / (3 * math.sqrt(3) * d23 ** 2), "N", gabarito=4.9e-26, s=3)
item("P23(d) conferência: F(d/√2) direto", F23(d23 / math.sqrt(2)), "N", gabarito=4.9e-26)
item("P23 verificação: F(5,0 m) (borda do intervalo)", F23(5.0), "N")
item("P23 verificação: F(5,0 m)/F máx", F23(5.0) / Fmax * 100, "%", s=2)

# ================================================================= DEGRAU 6 — carga espalhada
secao("DEGRAU 6 — Carga espalhada: densidade e integral")
Lb, A = 2.00, 4.00e-4
qa51 = item("P51(a): carga (ρ = -4,00 µC/m³ uniforme)", -4.00e-6 * Lb * A, "C")
item("P51(a): número de elétrons", abs(qa51) / e, "", gabarito=2.00e10)
qb51 = item("P51(b) (exemplo resolvido): q = b A L³/3, b = -2,00 µC/m⁵", -2.00e-6 * A * Lb ** 3 / 3, "C")
item("P51(b) (exemplo resolvido): número de elétrons", abs(qb51) / e, "", gabarito=1.33e10)
# lacuna: casca com ρ0 uniforme
rho0, r1, r2 = 5.0e-6, 0.040, 0.060
q_form = item("Lacuna D6: casca uniforme ρ0=5,0 µC/m³, fórmula (4/3)π(r2³-r1³)ρ0",
              rho0 * 4 / 3 * math.pi * (r2 ** 3 - r1 ** 3), "C")
N = 200000
dr = (r2 - r1) / N
q_int = sum(rho0 * 4 * math.pi * (r1 + (i + 0.5) * dr) ** 2 * dr for i in range(N))
item("Lacuna D6: mesma casca por soma de cascas finas", q_int, "C", gabarito=q_form)
# P21
b = 3.0e-6
q21 = item("P21: q = 2πb(r2² - r1²)", 2 * math.pi * b * (r2 ** 2 - r1 ** 2), "C", gabarito=3.8e-8, s=2)
q21_num = sum((b / (r1 + (i + 0.5) * dr)) * 4 * math.pi * (r1 + (i + 0.5) * dr) ** 2 * dr for i in range(N))
item("P21 conferência por soma numérica", q21_num, "C", gabarito=3.8e-8)
V = 4 / 3 * math.pi * (r2 ** 3 - r1 ** 3)
item("P21 erro comum: ρ(r1) × V", b / r1 * V, "C")
item("P21 erro comum: ρ(r2) × V", b / r2 * V, "C")
item("P21 'e se' esfera maciça r1 = 0: 2πb r2²", 2 * math.pi * b * r2 ** 2, "C")
for n_camadas in (1, 2, 5, 20, 100):
    drn = (r2 - r1) / n_camadas
    s_esq = sum((b / (r1 + i * drn)) * 4 * math.pi * (r1 + i * drn) ** 2 * drn for i in range(n_camadas))
    item(f"Widget D6: soma com {n_camadas:>3} camadas (raio interno de cada)", s_esq, "C", s=4)

# ================================================================= REVISÃO INTERCALADA
secao("REVISÃO INTERCALADA")
item("R2: P26 Na+ Cl- (2,82e-10 m)", coulomb(e, e, 2.82e-10), "N")
item("R5: P43(b) nova distância", x42 * 100 / 4 ** (1 / 3), "cm", gabarito=3.1, s=2)
item("R6: P51(a) elétrons em excesso", abs(qa51) / e, "", gabarito=2.00e10)
item("R7: v na órbita n = 3", v_bohr(3), "m/s")

secao("OUTROS NÚMEROS CITADOS NO TEXTO (distratores, verificações, 'e se')")
item("Checkpoint D1 distrator (a): r = 3 (cm sem converter)", k * 4e-12 / 3.0 ** 2, "N", s=2)
item("Checkpoint D1 distrator (b): r sem elevar ao quadrado", k * 4e-12 / 0.030, "N", s=2)
item("D3: erro de trocar tan por sen a 16,0° (%)", (1 / math.cos(math.radians(16.0)) - 1) * 100, "%", s=2)
item("P42: erro de trocar tan por sen a 1,19° (%)", (1 / math.cos(math.radians(1.19)) - 1) * 100, "%", s=2)
item("D3/P73: razão força elétrica / gravitacional (próton–elétron)", k * e ** 2 / (G * 1.6726e-27 * m_e), "", s=2)
item("P73: razão m_p / m_e", 1.6726e-27 / m_e, "", s=4)
item("P73 'e se' (núcleo +2e, mesmo raio): v1·√2", v_bohr(1) * math.sqrt(2), "m/s")
item("P11: cada componente da força diagonal F32/√2", coulomb(q2, q3, math.sqrt(2) * a) / math.sqrt(2), "N")
item("P50: kqQ/h² com valores-teste (1 µC, 2 µC, 10 cm)", coulomb(1e-6, 2e-6, 0.10), "N")
item("R2 distrator: k e²/r (r sem quadrado)", k * e ** 2 / 2.82e-10, "N", s=2)
item("R2 distrator: k e/r² (faltou uma carga)", k * e / 2.82e-10 ** 2, "N", s=2)
item("R6 distrator: cm² não convertido (V = 8 'm³')", 4.00e-6 * 2.00 * 4.00 / e, "", s=3)
item("R7 distrator: v1/9", v_bohr(1) / 9, "m/s")
item("R7 distrator: v1/√3", v_bohr(1) / math.sqrt(3), "m/s")
item("R7 distrator: 3·v1", 3 * v_bohr(1), "m/s")
r1w, r2w = 0.010, 0.050
exw = 2 * math.pi * b * (r2w ** 2 - r1w ** 2)
item("Widget D6 (r1 = 1 cm, r2 = 5 cm): integral", exw, "C")
s1w = (b / r1w) * 4 * math.pi * r1w ** 2 * (r2w - r1w)
item("Widget D6: soma com 1 camada", s1w, "C")
item("Widget D6: erro com 1 camada (%)", (s1w - exw) / exw * 100, "%", s=2)

secao("RODADA 1 — números das respostas do Professor e da v2")
item("v2 gancho: carga do copo com 3 alg. (1,34e7)", q_copo, "C", s=3)
item("v2 gancho: força com 1,34e7 C a 1 m", k * q_copo ** 2, "N", s=3)
item("v2 gancho: razão com Sol–Terra", k * q_copo ** 2 / F_sol_terra, "", s=2)
item("v2 W1: força máxima possível (5 µC, 5 µC, 2 cm)", coulomb(5e-6, 5e-6, 0.02), "N", s=2)
item("v2 D1: dois balões com 1,0 nC a 3,0 cm", coulomb(1e-9, 1e-9, 0.03), "N", s=2)
item("v2 D1: peso de 1,0 mg", 1e-6 * g, "N", s=2)
item("v2 D1 ficha: dois prótons a 1,0e-15 m", coulomb(e, e, 1.0e-15), "N", s=2)
item("v2 P23: peso de um elétron (comparação)", m_e * g, "N", s=2)
item("v2 P23: F máx / peso do elétron", 4.904e-26 / (m_e * g), "", s=2)
# P42 sem aproximar: sen²θ tanθ = k q² / (4 L² m g)
qv = 2.3825e-8
lo, hi = 1e-9, 1.5
for _ in range(200):
    mid = (lo + hi) / 2
    if math.sin(mid) ** 2 * math.tan(mid) - k * qv ** 2 / (4 * L42 ** 2 * m42 * g) > 0:
        hi = mid
    else:
        lo = mid
item("v2 P42: x exato sem aproximar (|q| = 2,3825e-8 C)", 2 * L42 * math.sin(lo) * 100, "cm", s=5)
item("v2 P42(a) conferência: sen θ = x/(2L) com x = 5,0 cm, L = 120 cm", 0.050 / (2 * 1.20), "", s=3)
# lacuna nova do degrau F(x): g(x) = x/(x²+a²)², máximo em a/√3
xs = [i / 100000 for i in range(1, 300000)]
xm = max(xs, key=lambda x: x / (x ** 2 + 1) ** 2)
item("v2 lacuna F(x): máximo de x/(x²+a²)² (a = 1), varredura", xm, "a", gabarito=1 / math.sqrt(3))
item("v2 lacuna F(x): valor máximo 9/(16√3) (a = 1)", xm / (xm ** 2 + 1) ** 2, "1/a³", gabarito=9 / (16 * math.sqrt(3)))
# P50: forças cruzadas (componente vertical cruzada / principal) = h³/(L²+h²)^(3/2)
for razao in (3, 10):
    item(f"v2 P50: força cruzada/força principal com L = {razao}h (%)", 100 / (razao ** 2 + 1) ** 1.5, "%", s=2)
# P7 com as três soltas: q3 = q1 zera tudo
q1t, q2t = -4.0, 1.0
def f_linha(i, qs, xs_):
    f = 0
    for j in range(3):
        if j != i:
            d = xs_[i] - xs_[j]
            f += qs[i] * qs[j] * math.copysign(1, d) / d ** 2
    return f
qs3 = [q1t, q2t, q1t]
item("v2 P7 dúvida: força sobre 1 com q3 = q1 (unid. k/L²)", f_linha(0, qs3, [0, 1, 2]), "", gabarito=0, tol_abs=1e-12)
item("v2 P7 dúvida: força sobre 2 com q3 = q1", f_linha(1, qs3, [0, 1, 2]), "", gabarito=0, tol_abs=1e-12)
# Bohr: período e número de voltas antes do colapso clássico (1,6e-11 s)
T1 = 2 * math.pi * a0 / v_bohr(1)
item("v2 P73: período da órbita n = 1", T1, "s")
item("v2 P73: voltas em 1,6e-11 s", 1.6e-11 / T1, "", s=2)
mu = m_e * 1.6726e-27 / (m_e + 1.6726e-27)
item("v2 P73: variação de v com massa reduzida (%)", (math.sqrt(m_e / mu) - 1) * 100, "%", s=2)
# Ex. 21.02: estabilidade transversal (força em y no ponto (2L, 0,01L), unidades kq q_p/L²)
def forca_xy(px, py):
    fx = fy = 0
    for qq, cx in ((8, 0.0), (-2, 1.0)):
        dx, dy = px - cx, py
        r = math.hypot(dx, dy)
        fx += qq * dx / r ** 3
        fy += qq * dy / r ** 3
    return fx, fy
item("v2 Ex. 21.02: Fy em (2L; 0,01L) — negativo = restauradora", forca_xy(2.0, 0.01)[1], "", s=3)
item("v2 Ex. 21.02: Fx em (2,01L; 0) — positivo = foge", forca_xy(2.01, 0.0)[0], "", s=3)

secao("v2 — DEGRAUS 3 (centrípeta) e 4 (fio e gangorra) novos")
# D3: lacuna nova — próton em MCU em torno de carga fixa −2e, r = 1,0e-10 m
m_pr = 1.67e-27
v_lac = math.sqrt(k * 2 * e * e / (m_pr * 1.0e-10))
item("v2 D3 lacuna: v do próton em torno de −2e a 1,0e-10 m", v_lac, "m/s")
item("v2 D3 checkpoint: fator em v se a carga central dobra", math.sqrt(2), "", s=3)
# D4: exemplo do pêndulo com fio de 30 cm — afastamento da vertical
th_ex = math.atan(F_b / P_b)
item("v2 D4 ex.: afastamento da vertical L·sen θ (L = 30 cm)", 0.30 * math.sin(th_ex) * 100, "cm")
# D4: lacuna do pêndulo — m = 3,0 g, L = 50 cm, afastamento 2,0 cm
s_th = 0.020 / 0.50
item("v2 D4 lacuna: sen θ = 2,0/50", s_th, "", s=3)
F_lac = 3.0e-3 * g * math.tan(math.asin(s_th))
item("v2 D4 lacuna: F_e = mg tan θ (exato)", F_lac, "N")
item("v2 D4 lacuna: F_e = mg sen θ (aproximado)", 3.0e-3 * g * s_th, "N")
# D4: lacuna da gangorra com o peso a 0,40 m
item("v2 D4 lacuna: peso a 0,40 m do apoio", F_t * 0.50 / 0.40, "N")
# D4 checkpoint: bolinhas em fios de 1,0 m afastadas 4,0 cm
item("v2 D4 checkpoint: ângulo de cada fio (x = 4,0 cm, L = 1,0 m)", math.degrees(math.asin(0.02)), "graus")
item("v2 D4 distrator: usando x inteiro (sen θ = 0,04)", math.degrees(math.asin(0.04)), "graus")
item("v2 D4 'x ∝ q^(2/3)': fator para q ×2", 2 ** (2 / 3), "")

secao("RESUMO")
if divergencias:
    print("  Divergências > 2 % com o gabarito:")
    for d in divergencias:
        print("   -", d)
else:
    print("  Nenhuma divergência > 2 % com o gabarito.")
