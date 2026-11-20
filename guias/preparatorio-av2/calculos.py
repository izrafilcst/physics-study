"""Contas do Preparatório da Avaliação 2 (caps. 21–23 e 28–30).

Rode com:  python3 -I calculos.py
Cada linha mostra o valor calculado e, quando existe, o do gabarito do livro
(ou o da alternativa marcada como certa na prova antiga). Diferença acima de 2 % vira "<<< DIVERGE".
"""
import math

k = 8.99e9          # N·m²/C²
eps0 = 8.85e-12     # C²/(N·m²)
mu0 = 4 * math.pi * 1e-7  # T·m/A
e = 1.60e-19        # C
me = 9.11e-31       # kg
mp = 1.67e-27       # kg
c = 3.00e8          # m/s


def mostra(rotulo, valor, ref=None, unid=''):
    s = f'{rotulo:<62} {valor: .4e} {unid}'
    if ref is not None:
        dif = abs(valor - ref) / abs(ref) if ref != 0 else abs(valor)
        s += f'   | ref {ref: .4e}  dif {100 * dif:5.2f} %'
        if dif > 0.02:
            s += '  <<< DIVERGE'
    print(s)


def titulo(t):
    print('\n== ' + t)


def cruz(u, w):
    return (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0])


# ------------------------------------------------------------------ degraus
titulo('D1 exemplo: onde a 3ª carga fica em equilíbrio (q1=+4 µC em 0, q2=-1 µC em 3 cm)')
d = 3.0
r = math.sqrt(4.0 / 1.0)
mostra('x (cm)', d * r / (r - 1), 6.0, 'cm')

titulo('D1 lacunas: +2,0 nC em x = ±3,0 cm, P em y = 4,0 cm')
E1 = k * 2.0e-9 / 0.05 ** 2
mostra('r (m)', math.hypot(0.03, 0.04), 0.05, 'm')
mostra('E de cada carga (N/C)', E1, unid='N/C')
mostra('E total = 2 E1 (4/5) (N/C), em +y', 2 * E1 * 0.8, unid='N/C')

titulo('D2 lacunas: esfera R = 10 cm, rho = C r, C = 3,0 µC/m^4')
mostra('q = pi C R^4 (C)', math.pi * 3.0e-6 * 0.10 ** 4, sum(3.0e-6 * ((j + .5) * 0.1 / 2000) * 4 * math.pi * ((j + .5) * 0.1 / 2000) ** 2 * (0.1 / 2000) for j in range(2000)), 'C')

titulo('D2 exemplo: carga por metro de cilindro com rho = rho0(1 - r/R)')
rho0, R = 6.0e-6, 0.020
lam_d2 = math.pi * rho0 * R ** 2 / 3
N = 2000
num = sum(rho0 * (1 - (i + .5) / N) * 2 * math.pi * ((i + .5) * R / N) * (R / N) for i in range(N))
mostra('lambda = pi rho0 R²/3 (C/m)', lam_d2, num, 'C/m')

titulo('D3 exemplo: barra no eixo (símbolos) — teste numérico Q=1 nC, L=10 cm, a=5 cm')
Q, L, a = 1e-9, 0.10, 0.05
E_form = k * Q / (a * (a + L))
lam = Q / L
E_int = sum(k * lam * (L / 4000) / (a + (i + .5) * L / 4000) ** 2 for i in range(4000))
mostra('E = kQ/(a(a+L)) (N/C)', E_form, E_int, 'N/C')

titulo('D3 lacunas: quarto de círculo, R = 5,0 cm, Q = +2,0 nC, E no centro')
R, Q, phi = 0.050, 2.0e-9, math.pi / 2
lam = Q / (R * phi)
mostra('lambda (C/m)', lam)
mostra('E = (2k lambda/R) sen(phi/2) (N/C)', 2 * k * lam / R * math.sin(phi / 2))

titulo('D4 exemplo: cilindro com rho = rho0 r/R (rho0 = 6,0 µC/m³, R = 2,0 cm)')
rho0, R = 6.0e-6, 0.020
mostra('E dentro, r = 1,0 cm: rho0 r²/(3 eps0 R)', rho0 * 0.01 ** 2 / (3 * eps0 * R), unid='N/C')
mostra('E na superfície: rho0 R/(3 eps0)', rho0 * R / (3 * eps0), unid='N/C')
mostra('E fora, r = 4,0 cm: rho0 R²/(3 eps0 r)', rho0 * R ** 2 / (3 * eps0 * 0.04), unid='N/C')

titulo('D5 exemplo (a): próton, v = (3î - 2ĵ)e5 m/s, B = 0,40 T k')
F = tuple(e * x for x in cruz((3e5, -2e5, 0.0), (0.0, 0.0, 0.40)))
mostra('Fx (N)', F[0], -1.28e-14, 'N')
mostra('Fy (N)', F[1], -1.92e-14, 'N')
titulo('D5 exemplo (b): próton acelerado por 500 V, B = 0,10 T')
v5 = math.sqrt(2 * e * 500 / mp)
mostra('v (m/s)', v5, unid='m/s')
mostra('r = mv/(eB) (m)', mp * v5 / (e * 0.10), unid='m')
titulo('D5 lacunas (c): fio em +y de 0 a 2 m, i = 3,0 A, B = (2,0 T/m²) y² î')
mostra('Fz (N)', -3.0 * 2.0 * (2.0 ** 3) / 3, -16.0, 'N')

titulo('D6 exemplo: semicircunferência + 2 segmentos radiais, R = 6,0 cm, i = 2,0 A')
mostra('B = mu0 i/(4R) (T)', mu0 * 2.0 / (4 * 0.060), unid='T')
titulo('D6 lacunas: fio grosso R = 2,0 mm, i = 10 A')
mostra('B(r = 1,0 mm) = mu0 i r/(2 pi R²) (T)', mu0 * 10 * 1e-3 / (2 * math.pi * (2e-3) ** 2), unid='T')
mostra('B(r = 4,0 mm) = mu0 i/(2 pi r) (T)', mu0 * 10 / (2 * math.pi * 4e-3), unid='T')

titulo('D7 exemplo: espira quadrada a = 0,10 m, B = (2,0 T/(m·s)) t x k')
mostra('fem = c a³/2 (V)', 2.0 * 0.10 ** 3 / 2, unid='V')
titulo('D7 lacunas: gerador N = 50, A = 0,020 m², B = 0,25 T, 600 rpm')
mostra('fem máx = N B A omega (V)', 50 * 0.25 * 0.020 * (600 * 2 * math.pi / 60), unid='V')

# ------------------------------------------------------------- provas antigas
titulo('PA1 (2024.2 Q1): barra 25 cm, lambda = 200 µC/m, P a 10 cm da ponta, no eixo')
lam, L, a = 200e-6, 0.25, 0.10
mostra('E = k lambda (1/a - 1/(a+L)) (N/C)', k * lam * (1 / a - 1 / (a + L)), 1.3e7, 'N/C')

titulo('PA2 (2024.1 Q5 = Exemplo 22.03): arco de 120° com -Q, E no centro')
mostra('E / (kQ/r²) = 3√3/(2π)  (livro: 0,83)', 3 * math.sqrt(3) / (2 * math.pi), 0.83)

titulo('PA3 (2024.2 Q5 adaptada): anel, teste q = 5,0 nC, R = 3,0 cm, z = 4,0 cm')
q, R, z = 5.0e-9, 0.030, 0.040
mostra('E = kqz/(z²+R²)^(3/2) (N/C)', k * q * z / (z * z + R * R) ** 1.5, unid='N/C')
mostra('z do máximo = R/√2 (m)', R / math.sqrt(2), unid='m')

titulo('PA4 (2024.2 Q2): tubo R = 4,00 cm, lambda = 3,00e-8 C/m, r = 2,00R')
mostra('E = lambda/(2 pi eps0 r) (N/C)', 3.0e-8 / (2 * math.pi * eps0 * 0.08), 6.74e3, 'N/C')

titulo('PA5 (2024.1 Q1 = P23.32): cilindro R = 4,0 cm, rho = A r², A = 2,5 µC/m^5')
A, R = 2.5e-6, 0.040
mostra('E(5,0 cm) = A R^4/(4 eps0 r) (N/C)', A * R ** 4 / (4 * eps0 * 0.05), 3.6, 'N/C')
mostra('E(3,0 cm) = A r³/(4 eps0) (N/C)  [P23.32a, par]', A * 0.03 ** 3 / (4 * eps0), unid='N/C')

titulo('PA6 (2024.2 Q3): elétron acelerado por 2,29 kV, círculo r = 0,137 m')
v6 = math.sqrt(2 * e * 2290 / me)
mostra('v (m/s)', v6, unid='m/s')
B6 = me * v6 / (e * 0.137)
mostra('B = m v/(e r) (T)', B6, 1.18e-3, 'T')
mostra('erro: esqueceu o 1/2 de K (v = sqrt(eV/m))', me * math.sqrt(e * 2290 / me) / (e * 0.137), 8.38e-4, 'T')
mostra('erro: usou r/2 (diâmetro)', 2 * B6, 2.36e-3, 'T')

titulo('PA7 (2024.2 Q4): fio no eixo x, i em +x, B = alpha x î + gamma x ĵ, x de 1 a 2 m')
mostra('F_z / (i gamma) = ∫1^2 x dx', (2 ** 2 - 1 ** 2) / 2, 1.5)

titulo('PA8 (prova antiga Q4 = P29.8 com outros números): dois arcos de 180°')
mostra('B = (mu0 i/4)(1/R1 - 1/R2) (T)', mu0 * 0.229 / 4 * (1 / 0.0329 - 1 / 0.0837), unid='T')
mostra('mesma conta com os números do P29.8 (par)', mu0 * 0.281 / 4 * (1 / 0.0315 - 1 / 0.0780), unid='T')

titulo('PA9 (2024.1 Q3 = P29.53 com v dobrada): solenoide 100 esp/cm, r = 2,30 cm')
n = 100 / 0.01
for frac, ref in ((0.046, 0.272), (0.092, 0.54)):
    B9 = me * frac * c / (e * 0.0230)
    mostra(f'v = {frac}c: B = m v/(e r) (T)', B9, unid='T')
    mostra(f'v = {frac}c: i = B/(mu0 n) (A)', B9 / (mu0 * n), ref, 'A')

titulo('PA10 (2024.1 Q4 = P30.27 com outros números): B = 4,0 t² y, espira de lado a')
for a, t, ref in ((0.020, 2.5, 80e-6), (0.0300, 10.0, 1.08e-3)):
    mostra(f'a = {a} m, t = {t} s: fem = 4 t a³ (V)', 4.0 * t * a ** 3, ref, 'V')
a, t, dt = 0.0300, 10.0, 1e-4


def fluxo(tt):
    M = 2000
    return sum(4.0 * tt ** 2 * ((j + .5) * a / M) * a * (a / M) for j in range(M))


mostra('PA10 por derivada numérica do fluxo (V)', (fluxo(t + dt) - fluxo(t - dt)) / (2 * dt), 1.08e-3, 'V')

# ---------------------------------------------------------------- lista 28–30
titulo('P28.5: B = Bx î + 3Bx ĵ, v = (2î + 4ĵ) m/s, F = (6,4e-19 N) k, elétron')
mostra('Bx (T)  [v × B = 2Bx k]', 6.4e-19 / (-e * 2.0), -2.0, 'T')

titulo('P28.48: i = 5,0 A em -x, B = 3,0 î + 8,0 x² ĵ (mT), x de 1 a 3 m')
mostra('Fz (N)  [par, sem gabarito]', -5.0 * 1e-3 * 8.0 * (3 ** 3 - 1 ** 3) / 3, unid='N')

titulo('P29.11: i1 = 6,5 A, d1 = 0,75 cm, d2 = 1,50 cm')
mostra('i2 = i1 d2/(d1 + d2) (A)', 6.5 * 1.50 / (0.75 + 1.50), 4.3, 'A')

titulo('P29.87: cabo coaxial a = 2,0 cm, b = 1,8 cm, c = 0,40 cm, i = 120 A')
a, b, cc, i = 0.020, 0.018, 0.0040, 120.0


def Bcoax(r):
    if r < cc:
        return mu0 * i * r / (2 * math.pi * cc ** 2)
    if r < b:
        return mu0 * i / (2 * math.pi * r)
    if r < a:
        return mu0 * i * (a * a - r * r) / (2 * math.pi * (a * a - b * b) * r)
    return 0.0


for rr in (0.002, 0.004, 0.010, 0.018, 0.019, 0.025):
    mostra(f'B(r = {100 * rr:.1f} cm) (T)', Bcoax(rr), unid='T')

titulo('P30.19: N = 100, 50 x 30 cm, B = 3,50 T, 1000 rpm')
mostra('fem máx = N B A omega (V)', 100 * 3.50 * 0.50 * 0.30 * (1000 * 2 * math.pi / 60), 5.50e3, 'V')

titulo('P30.33: L = 10,0 cm, v = 5,00 m/s, R = 0,400 Ω, i = 100 A, a = 10,0 mm')
L, v, Rb, i, a = 0.100, 5.00, 0.400, 100.0, 0.0100
fem = mu0 * i * v / (2 * math.pi) * math.log((a + L) / a)
ii = fem / Rb
mostra('(a) fem (V)', fem, 240e-6, 'V')
mostra('(b) i induzida (A)', ii, 0.600e-3, 'A')
mostra('(c) P = i² R (W)', ii ** 2 * Rb, 0.144e-6, 'W')
Fm = ii * mu0 * i / (2 * math.pi) * math.log((a + L) / a)
mostra('(d) F (N)', Fm, 2.87e-8, 'N')
mostra('(e) F v (W)', Fm * v, 0.144e-6, 'W')

# ------------------------------------------------------------------ simulado
titulo('S1: barra L = 12 cm, Q = 4,0 nC, ponto na mediatriz a y = 5,0 cm')
L, Q, y = 0.12, 4.0e-9, 0.050
lam = Q / L
E_s1n = sum(k * lam * (L / 4000) * y / (y * y + (-L / 2 + (j + .5) * L / 4000) ** 2) ** 1.5 for j in range(4000))
mostra('E = kQ/(y sqrt(y² + L²/4)) (N/C)', k * Q / (y * math.sqrt(y * y + (L / 2) ** 2)), E_s1n, 'N/C')

titulo('S2: casca cilíndrica a = 2,0 cm, b = 5,0 cm, rho = A/r, A = 1,5 nC/m²')
A, a, b = 1.5e-9, 0.020, 0.050
mostra('E(3,5 cm) = A (r - a)/(eps0 r) (N/C)', A * (0.035 - a) / (eps0 * 0.035), unid='N/C')
mostra('E(8,0 cm) = A (b - a)/(eps0 r) (N/C)', A * (b - a) / (eps0 * 0.080), unid='N/C')

titulo('S3: próton acelerado por 1,5 kV, B = 0,30 T')
v3 = math.sqrt(2 * e * 1500 / mp)
mostra('v (m/s)', v3, unid='m/s')
mostra('r (m)', mp * v3 / (e * 0.30), unid='m')
mostra('T = 2 pi m/(eB) (s)', 2 * math.pi * mp / (e * 0.30), unid='s')
mostra('F = e v B (N)', e * v3 * 0.30, unid='N')

titulo('S4: grampo (2 fios semi-infinitos + semicircunferência), R = 5,0 cm, i = 8,0 A')
R, i = 0.050, 8.0
mostra('B = mu0 i/(4R) + mu0 i/(2 pi R) (T)', mu0 * i / (4 * R) + mu0 * i / (2 * math.pi * R), unid='T')

titulo('S5: espira 10 cm x 5 cm, lado próximo a 2,0 cm de fio, i = 4,0 t² (A), R = 0,020 Ω, t = 3,0 s')
aa, bb, dd = 0.10, 0.050, 0.020
G = mu0 * aa / (2 * math.pi) * math.log((dd + bb) / dd)
fem5 = G * 8.0 * 3.0
mostra('Phi/i (Wb/A)', G, unid='Wb/A')
mostra('fem (V)', fem5, unid='V')
mostra('i induzida (A)', fem5 / 0.020, unid='A')

# ------------------------------------------------------------------ v2 (rodada 1)
titulo('v2 — S1: somar |dE| sem projetar (erro previsto)')
L, Q, y = 0.12, 4.0e-9, 0.050
lam = Q / L
mostra('kλ(2/y)·arctg(L/2y) (N/C)', k * lam * (2 / y) * math.atan(L / (2 * y)), unid='N/C')

titulo('v2 — D6 lacunas: fio grosso, ponto fora em r = 5,0 mm')
mostra('B(r = 5,0 mm) = mu0 i/(2 pi r) (T)', mu0 * 10 / (2 * math.pi * 5e-3), 4.0e-4, 'T')

titulo('v2 — PA2 valor-teste: Q = 1,0 nC, r = 10 cm')
E_pa2 = 3 * math.sqrt(3) / (2 * math.pi) * k * 1.0e-9 / 0.10 ** 2
mostra('E = 0,827 kQ/r² (N/C)', E_pa2, unid='N/C')
mostra('erro: sem projetar (kQ/r²)', k * 1.0e-9 / 0.01, unid='N/C')
mostra('erro: comprimento de semicírculo', 2 * k * (1.0e-9 / (math.pi * 0.10)) / 0.10 * math.sin(math.pi / 3), unid='N/C')
mostra('erro: só metade do arco', E_pa2 / 2, unid='N/C')

titulo('v2 — PA7 valor-teste: i = 2,0 A, alpha = 3,0 T/m, gamma = 0,50 T/m')
i7, al, ga = 2.0, 3.0, 0.50
mostra('F_z = i gamma ∫1^2 x dx (N)', i7 * ga * 1.5, unid='N')
mostra('erro: usou alpha', i7 * al * 1.5, unid='N')
mostra('erro: sem o 1/2', i7 * ga * 3, unid='N')

titulo('v2 — dúvida: barra com lambda = alpha x, P a uma distância a da ponta')
alpha, L, a = 2.0e-6, 0.20, 0.05
N = 20000
num = sum(k * alpha * ((j + .5) * L / N) * (L / N) / (L + a - (j + .5) * L / N) ** 2 for j in range(N))
mostra('E = k alpha [L/a - ln(1 + L/a)] (N/C)', k * alpha * (L / a - math.log(1 + L / a)), num, 'N/C')
a = 50.0
mostra('de longe (a = 50 m): fórmula vs kQ/a², Q = alpha L²/2', k * alpha * (L / a - math.log(1 + L / a)), k * alpha * L ** 2 / 2 / a ** 2, 'N/C')

titulo('v2 — D6: fio reto finito por Biot-Savart (numérico) vs fórmula com sen')
i, R = 8.0, 0.050
x1, x2 = -0.03, 0.12   # extremidades do fio, medidas a partir do pé da perpendicular
M = 20000
num = sum(mu0 / (4 * math.pi) * i * R * ((x2 - x1) / M) / ((x1 + (j + .5) * (x2 - x1) / M) ** 2 + R ** 2) ** 1.5 for j in range(M))
s1, s2 = x1 / math.hypot(x1, R), x2 / math.hypot(x2, R)
mostra('B = mu0 i (sen th2 - sen th1)/(4 pi R) (T)', mu0 * i * (s2 - s1) / (4 * math.pi * R), num, 'T')
mostra('semi-infinito (S4): mu0 i/(4 pi R) (T)', mu0 * i / (4 * math.pi * R), unid='T')
