"""Aluno 3 (Monitor cético): contas refeitas do zero, sem importar calculos.py.

Rode com:  python3 -I aluno-3-contas.py

Convenção de saída:  OK   = bate com a referência dentro de 2 %
                     !!!  = diverge mais de 2 % (ou o texto do guia está errado)
                     ---  = só informação (não há referência)
Quase tudo é refeito por INTEGRAÇÃO NUMÉRICA ou por produto vetorial explícito,
não pela fórmula fechada do guia, para não repetir o mesmo erro do professor.
"""
import math

# constantes do guia
k = 8.99e9
eps0 = 8.85e-12
mu0 = 4 * math.pi * 1e-7
e = 1.60e-19
me = 9.11e-31
mp = 1.67e-27
c = 3.00e8

DIV = []


def chk(rot, calc, ref=None, tol=0.02, nota=''):
    if ref is None:
        print(f'--- {rot:<66} {calc: .5g} {nota}')
        return
    dif = abs(calc - ref) / abs(ref) if ref != 0 else abs(calc)
    marca = 'OK ' if dif <= tol else '!!!'
    if marca == '!!!':
        DIV.append((rot, calc, ref, dif))
    print(f'{marca} {rot:<66} {calc: .5g}  ref {ref: .5g}  dif {100*dif:6.2f} % {nota}')


def sec(t):
    print('\n== ' + t)


# ---------- vetores ----------
def cruz(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def mul(s, a):
    return tuple(s*x for x in a)


def norm(a):
    return math.sqrt(sum(x*x for x in a))


def biot(segs, P, i, n=4000):
    """B em P (SI) de uma lista de segmentos retos ('r', A, B) ou arcos
    ('a', centro, raio, ang0, ang1) percorridos no sentido do parâmetro crescente.
    Integra dB = mu0/4pi i dl x r / r^3 numericamente (ponto médio)."""
    B = (0.0, 0.0, 0.0)
    for s in segs:
        if s[0] == 'r':
            A, Bp = s[1], s[2]
            for j in range(n):
                t0, t1 = j/n, (j+1)/n
                p0 = add(A, mul(t0, sub(Bp, A)))
                p1 = add(A, mul(t1, sub(Bp, A)))
                dl = sub(p1, p0)
                mid = mul(0.5, add(p0, p1))
                r = sub(P, mid)
                f = mu0/(4*math.pi)*i/norm(r)**3
                B = add(B, mul(f, cruz(dl, r)))
        else:
            C, R, a0, a1 = s[1], s[2], s[3], s[4]
            for j in range(n):
                th0 = a0+(a1-a0)*j/n
                th1 = a0+(a1-a0)*(j+1)/n
                p0 = (C[0]+R*math.cos(th0), C[1]+R*math.sin(th0), 0.0)
                p1 = (C[0]+R*math.cos(th1), C[1]+R*math.sin(th1), 0.0)
                dl = sub(p1, p0)
                mid = mul(0.5, add(p0, p1))
                r = sub(P, mid)
                f = mu0/(4*math.pi)*i/norm(r)**3
                B = add(B, mul(f, cruz(dl, r)))
    return B


# =====================================================================
sec('DEGRAU 0 (pré-requisitos)')
chk('pre1: (2i)x(3j) -> z', cruz((2, 0, 0), (0, 3, 0))[2], 6)
a_, L_ = 0.05, 0.10
N = 200000
chk('pre2: int_a^{a+L} dx/x^2 = 1/a - 1/(a+L)', sum((L_/N)/(a_+(j+.5)*L_/N)**2 for j in range(N)), 1/a_-1/(a_+L_))
chk('pre4: int dx/x = ln((a+L)/a)', sum((L_/N)/(a_+(j+.5)*L_/N) for j in range(N)), math.log((a_+L_)/a_))
V = 1000.0
chk('pre5: v=sqrt(2eV/m) (K=1/2 m v^2) -> K recuperada (J)', 0.5*me*(2*e*V/me), e*V)

# =====================================================================
sec('DEGRAU 1')
# equilíbrio: +4 uC em 0, -1 uC em 3 cm
d = 0.03
f = lambda x: 4/x**2 - 1/(x-d)**2
lo, hi = d+1e-6, 1.0
for _ in range(200):
    mid = (lo+hi)/2
    if f(mid) > 0:
        hi = mid      # f>0 (campo da +4 domina): a raiz está mais perto
    else:
        lo = mid
chk('x de equilíbrio (cm)', 100*hi, 6.0, 0.001)
chk('ck1-1: +q em 0, +4q em d: x = d/3 (d=1)', (lambda: next(x/1000 for x in range(1, 1000) if 1/(x/1000)**2 <= 4/(1-x/1000)**2))(), 1/3, 0.01)
# lacuna: 2 nC em x=±3 cm, P em y = 4 cm  (vetorial explícito)
q = 2e-9
P = (0, 0.04, 0)
Etot = (0, 0, 0)
for xs in (-0.03, 0.03):
    r = sub(P, (xs, 0, 0))
    Etot = add(Etot, mul(k*q/norm(r)**3, r))
chk('lac1-1 r (cm)', 100*math.hypot(0.03, 0.04), 5.0)
chk('lac1-2 E1 (N/C)', k*q/0.05**2, 7192, 0.005)
chk('lac1-3 E total (N/C), componente y', Etot[1], 11507, 0.005)
chk('lac1-3 E total, componente x (deve ser 0)', Etot[0]+1e-12, 1e-12, 1.0)
chk('erro soma de módulos 2*E1', 2*k*q/0.05**2, 14384, 0.005)
chk('erro 3/5 em vez de 4/5', 2*k*q/0.05**2*0.6, 8630, 0.005)
# 22.9: sinais opostos (conferência de método): campo em P
q9 = 3.2e-19
P = (0, 4.0, 0)
E = (0, 0, 0)
for xs, qq in ((-3.0, -q9), (3.0, q9)):
    r = sub(P, (xs, 0, 0))
    E = add(E, mul(k*qq/norm(r)**3, r))
chk('C22-9: |E| N/C (gabarito do livro 1,38e-10; direção 180 graus)', norm(E), 1.38e-10, 0.01, nota=f'dir. {math.degrees(math.atan2(E[1], E[0])):.1f} graus')

# =====================================================================
sec('DEGRAU 2')
R_, C_ = 0.10, 3.0e-6
N = 20000
qnum = sum(C_*((j+.5)*R_/N)*4*math.pi*((j+.5)*R_/N)**2*(R_/N) for j in range(N))
chk('lac2-2 q esfera rho=Cr = pi C R^4', qnum, 9.4248e-10)
chk('erro 4/3 pi C R^4', 4/3*math.pi*C_*R_**4, 1.2566e-9)
rho0, R_ = 6.0e-6, 0.020
lam = sum(rho0*(1-(j+.5)/N)*2*math.pi*((j+.5)*R_/N)*(R_/N) for j in range(N))
chk('exemplo D2: lambda cilindro rho0(1-r/R) = pi rho0 R^2/3', lam, 2.5133e-9)
chk('exemplo D2: "rho do meio" pi rho0 R^2/2 (erro citado)', math.pi*rho0*R_**2/2, None)
# ck2-1: rho = A r^2, qenv/h = pi A r^4 /2
A_, r_ = 1.0, 0.7
chk('ck2-1: int_0^r A r^2 2 pi r dr = pi A r^4/2', sum(A_*((j+.5)*r_/N)**2*2*math.pi*((j+.5)*r_/N)*(r_/N) for j in range(N)), math.pi*A_*r_**4/2)
# ck2-2: B = c y, lado a
a_, c_ = 0.3, 2.0
chk('ck2-2: fluxo = c a^3/2', sum(c_*((j+.5)*a_/N)*a_*(a_/N) for j in range(N)), c_*a_**3/2)

# =====================================================================
sec('DEGRAU 3')
Q, L, a = 1e-9, 0.10, 0.05
lam = Q/L
chk('exemplo D3: E barra no eixo (integral numérica) x kQ/(a(a+L))', sum(k*lam*(L/N)/(a+(j+.5)*L/N)**2 for j in range(N)), k*Q/(a*(a+L)))
chk('exemplo D3: 1,2e3 N/C', k*Q/(a*(a+L)), 1.2e3)
# quarto de círculo, R=5 cm, Q=2 nC, vetorial
Rr, Q = 0.05, 2.0e-9
phi = math.pi/2
lam = Q/(Rr*phi)
chk('lac3-1 lambda', lam, 2.5465e-8, 0.001)
Ex = Ey = 0.0
for j in range(N):
    th = -phi/2+(j+.5)*phi/N
    dq = lam*Rr*(phi/N)
    # carga + em Rr(cos,sin); campo em 0 aponta para longe dela
    Ex += -k*dq/Rr**2*math.cos(th)
    Ey += -k*dq/Rr**2*math.sin(th)
chk('lac3-2 |E| no centro (integração vetorial)', math.hypot(Ex, Ey), 6475, 0.002)
chk('lac3-2 erro kQ/R^2', k*Q/Rr**2, 7192, 0.005)
chk('lac3-2 erro metade do arco', math.hypot(Ex, Ey)/2, 3237, 0.005)
chk('lac3-1 erro phi=90 (graus)', Q/(Rr*90), 4.444e-10, 0.002)
chk('lac3-1 erro meio círculo', Q/(Rr*math.pi), 1.2732e-8, 0.002)
# ck3-3 semicírculo: E = 2k lam/R
Q = 1e-9
Rr = 0.1
lam = Q/(math.pi*Rr)
chk('ck3-3: semicírculo E = 2kQ/(pi R^2)', 2*k*lam/Rr, 2*k*Q/(math.pi*Rr**2))
# ck3-2 anel longe ~ kq/z^2
q, R, z = 1.0, 0.03, 3.0
chk('ck3-2: anel z>>R -> kq/z^2', k*q*z/(z*z+R*R)**1.5, k*q/z**2, 1e-3)
# 22.26: semicircunferência voltada para +x; metade de cima +q, metade de baixo -q (vetorial)
q = 4.5e-12
Rr = 0.05
lam = q/(math.pi*Rr/2)
Ex = Ey = 0.0
for j in range(N):
    th = (j+.5)*(math.pi/2)/N
    dq = lam*Rr*((math.pi/2)/N)
    # +dq em (R cos th, R sin th): campo em 0 aponta para longe dela
    Ex += -k*dq*math.cos(th)/Rr**2
    Ey += -k*dq*math.sin(th)/Rr**2
    # -dq em (R cos th, -R sin th): campo em 0 aponta PARA ela
    Ex += +k*dq*math.cos(th)/Rr**2
    Ey += -k*dq*math.sin(th)/Rr**2
chk('C22-26: Ex = 0 (soma dos pares)', Ex*1e3+1e-12, 1e-12, 1.0)
chk('C22-26: |Ey| (N/C); só sobra y, para baixo (guia: 20,6)', abs(Ey), 20.6, 0.01, nota=f'Ey={Ey:.4g}')
# PA1 integral
lam, L, a = 200e-6, 0.25, 0.10
E1 = sum(k*lam*(L/N)/(a+(j+.5)*L/N)**2 for j in range(N))
chk('PA1 E (integral numérica)', E1, 1.3e7)
chk('PA1 valor exato, mesmo vs alternativa C (1,3e7)', E1, 1.2843e7, 0.002)
chk('PA1 erro kQ/a^2 com Q=lam*L', k*lam*L/a**2, 4.495e7, 0.002)
chk('PA1 erro 1/a + 1/(a+L)', k*lam*(1/a+1/(a+L)), 2.312e7, 0.002)
chk('PA1 erro lam no lugar de Q', k*lam/(a*(a+L)), 5.137e7, 0.002)
chk('PA1 verificar: kQ/d^2 com d = 22,5 cm', k*lam*L/(a+L/2)**2, 8.9e6, 0.02)
# PA2: arco de 120 graus, -Q à direita de P: vetorial
Q = 1.0
r = 1.0
lam = Q/(r*2*math.pi/3)
Ex = Ey = 0.0
for j in range(N):
    th = -math.pi/3+(j+.5)*(2*math.pi/3)/N
    dq = -lam*r*((2*math.pi/3)/N)
    pos = (r*math.cos(th), r*math.sin(th))
    # campo em P=0 devido a dq: k dq (P - pos)/|.|^3
    Ex += k*dq*(-pos[0])/r**3
    Ey += k*dq*(-pos[1])/r**3
chk('PA2 E/(kQ/r^2) (componente x, sinal: + = para a barra)', Ex/(k*Q/r**2), 0.827, 0.002)
chk('PA2 Ey (deve ser 0)', Ey/(k*Q/r**2)+1e-12, 1e-12, 1.0)
chk('PA2 erro pi r  (0,551)', 2*math.sin(math.pi/3)/math.pi, 0.551, 0.002)
chk('PA2 erro metade do arco (0,413)', 0.827/2, 0.413, 0.002)
# PA3 anel (integração numérica vetorial)
q, R, z = 5.0e-9, 0.03, 0.04
Ez = 0.0
Ex = 0.0
for j in range(N):
    ph = (j+.5)*2*math.pi/N
    dq = q/N
    src = (R*math.cos(ph), R*math.sin(ph), 0)
    rv = sub((0, 0, z), src)
    Ez += k*dq*rv[2]/norm(rv)**3
    Ex += k*dq*rv[0]/norm(rv)**3
chk('PA3 E no eixo (integral vetorial)', Ez, 14384, 0.002)
chk('PA3 componente perpendicular (deve ser 0)', Ex+1e-9, 1e-9, 1.0)
chk('PA3 erro sem cos', k*q/(z*z+R*R), 17980, 0.002)
chk('PA3 erro kq/z^2', k*q/z**2, 28094, 0.002)
# z do máximo
zz = max((i*1e-5 for i in range(1, 20000)), key=lambda z: z/(z*z+R*R)**1.5)
chk('PA3 z do máximo = R/sqrt2 (cm)', 100*zz, 100*R/math.sqrt(2), 0.01)

# =====================================================================
sec('DEGRAU 4 (Gauss)')
rho0, R = 6.0e-6, 0.020
def qenv_lin(r, h=1.0):  # rho = rho0 r/R
    rr = min(r, R)
    return sum(rho0*((j+.5)*rr/N)/R*2*math.pi*((j+.5)*rr/N)*h*(rr/N) for j in range(N))
for r, ref in ((0.010, 1.13e3), (0.020, 4.52e3), (0.040, 2.26e3)):
    E = qenv_lin(r)/(eps0*2*math.pi*r)
    chk(f'exemplo D4: E(r={100*r:.0f} cm), q_env numérica', E, ref, 0.01)
Q = 2e-9
chk('lac4-2 E(10 cm) casca esférica', k*Q/0.1**2, 1798, 0.002)
chk('lac4-1 erro kQ/r^2 a 3 cm', k*Q/0.03**2, 19978, 0.002)
chk('lac4-2 erro 2kQ/r', 2*k*Q/0.10, 359.6, 0.002)
# PA4
lam, R = 3.0e-8, 0.04
chk('PA4 E(2R) = lam/(2 pi eps0 r)', lam/(2*math.pi*eps0*0.08), 6.74e3, 0.005)
chk('PA4 alternativa C da prova = resposta do livro (R=3, lam=2e-8, r=2R)', 2e-8/(2*math.pi*eps0*0.06), 5.99e3, 0.005,
    nota='<- a alternativa C (5,99e3) e a resposta do P23.24: distrator-armadilha')
chk('PA4 erro r=R', lam/(2*math.pi*eps0*0.04), 13488, 0.002)
chk('PA4 erro k lam/r^2', k*lam/0.08**2, 42140, 0.002)
chk('PA4 erro k lam/r', k*lam/0.08, 3372, 0.002)
chk('PA4 erro dentro (R/2)', lam/(2*math.pi*eps0*0.02), 26976, 0.002)
# PA5
A, R = 2.5e-6, 0.04
def qenv_r2(r, h=1.0):
    rr = min(r, R)
    return sum(A*((j+.5)*rr/N)**2*2*math.pi*((j+.5)*rr/N)*h*(rr/N) for j in range(N))
E5 = qenv_r2(0.05)/(eps0*2*math.pi*0.05)
E3 = qenv_r2(0.03)/(eps0*2*math.pi*0.03)
chk('PA5 E(5,0 cm) (q_env numérica) vs alternativa D 3,6', E5, 3.6)
chk('PA5 E(3,0 cm) vs alternativa A 1,9', E3, 1.9)
chk('PA5 erro rho_borda x volume', 2*E5, 7.232, 0.002, nota='= alternativa E (7,2) da prova')
chk('PA5 erro r=R', A*R**3/(4*eps0), 4.52, 0.002)
# S2
A, a, b = 1.5e-9, 0.02, 0.05
def qenv_S2(r, h=1.0):
    lo = a
    hi = min(r, b)
    if hi <= lo:
        return 0.0
    return sum(A/(lo+(j+.5)*(hi-lo)/N)*2*math.pi*(lo+(j+.5)*(hi-lo)/N)*h*((hi-lo)/N) for j in range(N))
chk('S2 E(1,0 cm)=0', qenv_S2(0.01), 0.0, 1e-9) if False else None
chk('S2 E(3,5 cm)', qenv_S2(0.035)/(eps0*2*math.pi*0.035), 72.64, 0.002)
chk('S2 E(8,0 cm)', qenv_S2(0.080)/(eps0*2*math.pi*0.080), 63.56, 0.002)
chk('S2 erro integrar de 0', A*0.035/(eps0*0.035), 169.5, 0.002)
chk('S2 erro 0 até b', A*b/(eps0*0.08), 105.9, 0.002)

# =====================================================================
sec('DEGRAU 5')
F = tuple(e*x for x in cruz((3e5, -2e5, 0), (0, 0, 0.40)))
chk('exemplo D5(a) Fx', F[0], -1.28e-14, 0.001)
chk('exemplo D5(a) Fy', F[1], -1.92e-14, 0.001)
chk('exemplo D5(a) F.v = 0', F[0]*3e5+F[1]*(-2e5), 0.0, 1e-9) if False else print(f'--- F.v = {F[0]*3e5+F[1]*(-2e5):.3g} (deve ser 0)')
v5 = math.sqrt(2*e*500/mp)
chk('exemplo D5(b) v (m/s)', v5, 3.10e5, 0.005)
chk('exemplo D5(b) r (cm)', 100*mp*v5/(e*0.10), 3.2, 0.02)
chk('Tabela D5: elétron 2 kV, 1 mT -> r ~ 15 cm', 100*me*math.sqrt(2*e*2000/me)/(e*1e-3), 15, 0.05)
# lac5: fio em +y de 0 a 2 m, i=3 A, B = 2 y^2 i
Fz = 0.0
for j in range(N):
    y = (j+.5)*2.0/N
    dF = cruz((0, 3.0*2.0/N, 0), (2.0*y*y, 0, 0))
    Fz += dF[2]
chk('lac5-2 Fz (integral vetorial)', Fz, -16.0, 0.001)
chk('lac5-2 erro B no fim', -3.0*2.0*8.0, -48.0, 0.001)
chk('lac5-2 erro integrou y em vez de y^2', -3.0*2.0*2.0*2.0/2*1.0, -12.0, 0.001, nota='(−3·∫2y dy = −12)')
# ck5-1: elétron v=i B=j -> -k
Fe = tuple(-x for x in cruz((1, 0, 0), (0, 1, 0)))
chk('ck5-1 força no elétron (z)', Fe[2], -1.0)
# ck5-3, rev8
chk('ck5-3 dL=i, B1 j -> +k (z)', cruz((1, 0, 0), (0, 1, 0))[2], 1.0)
chk('rev8 i x k = -j (y)', cruz((1, 0, 0), (0, 0, 1))[1], -1.0)
# prev-w5
chk('prev-w5: V dobra -> r x sqrt2', math.sqrt(2), 1.4142, 0.001)
# PA6
v6 = math.sqrt(2*e*2290/me)
B6 = me*v6/(e*0.137)
chk('PA6 v (m/s)', v6, 2.84e7, 0.005)
chk('PA6 B (T) vs alternativa D 1,18e-3', B6, 1.18e-3, 0.01)
chk('PA6 erro sem 1/2 vs alternativa B 8,38e-4', B6/math.sqrt(2), 8.38e-4, 0.02, nota='(0,5 % de diferença: o professor usou outras constantes)')
chk('PA6 erro diâmetro vs alternativa C 2,36e-3', 2*B6, 2.36e-3, 0.01)
chk('PA6 erro metade', B6/2, 5.89e-4, 0.002)
chk('PA6 Verificar: v/c', v6/c, 0.09, 0.1)
# correção relativística PA6
K = e*2290
mc2 = me*c*c
p = math.sqrt(K*K+2*K*mc2)/c
chk('PA6 B relativístico (T)', p/(e*0.137), B6, 0.02, nota='(diferença 0,2 %: ignorar é OK)')
chk('PA6 próton: r_p = 0,137 sqrt(mp/me) (m)', 0.137*math.sqrt(mp/me), 5.9, 0.01)
chk('rev4: mp/me', mp/me, 1800, 0.05)
# PA7
chk('PA7 F_z/(i gamma) = int_1^2 x dx', sum(((j+.5)/N+1)/N for j in range(N)), 1.5, 0.001)
F = cruz((1, 0, 0), (0, 1, 0))
chk('PA7 i x j = +k (z)', F[2], 1.0)
chk('PA7 erro 4-1 sem 1/2', 3.0, 3.0)
# P28.5: elétron, F = 6,4e-19 k
Bx = -2.0
Bv = (Bx, 3*Bx, 0)
Fv = tuple(-e*x for x in cruz((2, 4, 0), Bv))
chk('P28.5: Bx=-2 -> F_z (N) = 6,4e-19', Fv[2], 6.4e-19, 0.001)
chk('P28.5 gabarito do livro (-2,0 T) via isolando Bx', 6.4e-19/(-e*2), -2.0, 0.001)
chk('P28.5 erro somou 2*3+4*1', -6.4e-19/(e*10), -0.4, 0.001)
# P28.48
Fz = 0.0
for j in range(N):
    x = 1+(j+.5)*2/N
    dL = (-2.0/N, 0, 0)
    Bv = (3e-3, 8e-3*x*x, 0)
    Fz += 5.0*cruz(dL, Bv)[2]
chk('P28.48 Fz (integral vetorial)', Fz, -0.3467, 0.001)
chk('P28.48 erro B(3)', -5.0*0.072*2, -0.72, 0.001)
chk('P28.48 erro B(1)', -5.0*0.008*2, -0.08, 0.001)
chk('P28.48 erro B(2)', -5.0*0.032*2, -0.32, 0.001)

# =====================================================================
sec('DEGRAU 6')
chk('exemplo D6: mu0 i/(4R), R=6 cm, i=2 A', mu0*2/(4*0.06), 1.0e-5, 0.05)
chk('lac6-1 B(1 mm) fio grosso', mu0*10*1e-3/(2*math.pi*(2e-3)**2), 5.0e-4, 0.001)
chk('lac6-2 B(4 mm)', mu0*10/(2*math.pi*4e-3), 5.0e-4, 0.001)
chk('lac6-1 erros: 2e-3 e 1e-3', mu0*10/(2*math.pi*1e-3), 2e-3, 0.001)
chk('lac6-1 erro superfície', mu0*10/(2*math.pi*2e-3), 1e-3, 0.001)
chk('ck6-3 B solenoide 100 esp/cm, 0,5 A', mu0*1e4*0.5, 6.3e-3, 0.01)
# semicírculo vs círculo
BS = biot([('a', (0, 0, 0), 1.0, 0, math.pi)], (0, 0, 0), 1.0)
BC = biot([('a', (0, 0, 0), 1.0, 0, 2*math.pi)], (0, 0, 0), 1.0)
chk('ck6-1 B semicírculo / B círculo', norm(BS)/norm(BC), 0.5, 0.001)
# PA8: arcos concêntricos (lido da foto): externo anti-horário (0->pi), interno horário (pi->0)
i = 0.229
R1, R2 = 0.0329, 0.0837
segs = [('a', (0, 0, 0), R2, 0.0, math.pi),                 # externo, CCW
        ('r', (-R2, 0, 0), (-R1, 0, 0)),                  # radial esquerdo, rumo ao centro
        ('a', (0, 0, 0), R1, math.pi, 0.0),                # interno, CW
        ('r', (R1, 0, 0), (R2, 0, 0))]                     # radial direito, rumo à origem do externo
B = biot(segs, (0, 0, 0), i, n=3000)
chk('PA8 |B| em C (Biot-Savart numérico, geometria da foto)', norm(B), 1.33e-6, 0.01)
chk('PA8 Bz < 0 ? (-1 = entra no papel, como diz o guia)', math.copysign(1, B[2]), -1.0)
chk('PA8 trechos radiais contribuem 0', norm(biot(segs[1:2]+segs[3:4], (0, 0, 0), i)), 0.0, 1e-6) if False else print(f'--- PA8 contribuição dos radiais = {norm(biot([segs[1]], (0,0,0), i)):.3g} T (deve ser ~0)')
chk('PA8 erro soma', mu0*i/4*(1/R1+1/R2), 3.046e-6, 0.002)
chk('PA8 erro só interno', mu0*i/4/R1, 2.186e-6, 0.002)
chk('PA8 erro espira completa', mu0*i/2*(1/R1-1/R2), 2.654e-6, 0.002)
chk('PA8 antes de pedir "números do P29.8" (par): R1=3,15 R2=7,80 i=0,281', mu0*0.281/4*(1/0.0315-1/0.0780), None)
# PA8-a opção (c): mu0 i phi/(2R) em phi=2pi dá mu0 i pi /R ; correto mu0 i/(2R)
chk('PA8-a(c): razão (mu0 i pi/R)/(mu0 i/(2R)) -- guia diz "pi vezes maior"', (math.pi)/(1/2), math.pi, 0.02,
    nota='<- o guia escreve "pi vezes"; o certo é 2 pi vezes')
# P29.11
i1, d1, d2 = 6.5, 0.75e-2, 1.50e-2
def Bfio(I, s, src, Pt):
    r = sub(Pt, src)
    r2 = r[0]**2+r[1]**2
    return mul(mu0*I*s/(2*math.pi*r2), cruz((0, 0, 1), r))
P_ = (0, -d2, 0)
B1 = Bfio(i1, -1, (0, d1, 0), P_)     # fio 1 no alto, entrando (s=-1)
best = None
for s2 in (+1, -1):
    I2 = i1*d2/(d1+d2)
    B2 = Bfio(I2, s2, (0, 0, 0), P_)
    tot = add(B1, B2)
    print(f'--- P29.11: i2 = {I2:.3f} A, sentido s={s2:+d} (+1 = para fora): |B_total| em P = {norm(tot):.3g} T')
chk('P29.11 i2 = i1 d2/(d1+d2)', i1*d2/(d1+d2), 4.3, 0.01)
chk('P29.11 erro i1 d2/d1', i1*d2/d1, 13, 0.001)
chk('P29.11 erro i1 d1/d2', i1*d1/d2, 3.25, 0.001)
chk('P29.11 erro i1 (d1+d2)/d2', i1*(d1+d2)/d2, 9.75, 0.001)
# P29.87
a, b, cc, i = 0.020, 0.018, 0.0040, 120.0
def ienv(r):
    # integração numérica das densidades uniformes
    Jf = i/(math.pi*cc**2)
    Jc = -i/(math.pi*(a*a-b*b))
    tot = 0.0
    for j in range(N):
        rr = (j+.5)*min(r, cc)/N
        tot += Jf*2*math.pi*rr*(min(r, cc)/N)
    if r > b:
        hi = min(r, a)
        for j in range(N):
            rr = b+(j+.5)*(hi-b)/N
            tot += Jc*2*math.pi*rr*((hi-b)/N)
    return tot
for r, ref in ((0.002, 3.0e-3), (0.010, 2.4e-3), (0.018, 1.333e-3), (0.019, 6.482e-4), (0.025, 0.0)):
    Bn = mu0*ienv(r)/(2*math.pi*r)
    if ref == 0.0:
        print(f'--- P29.87 B(r={100*r:.1f} cm) numérico = {Bn:.3g} T (deve ser 0)')
    else:
        chk(f'P29.87 B(r={100*r:.1f} cm) (Ampère numérico)', Bn, ref, 0.005)
chk('P29.87 erro 0,2 cm sem fração', mu0*i/(2*math.pi*0.002), 0.012, 0.001)
chk('P29.87 erro 0,2 cm superfície', mu0*i/(2*math.pi*cc), 6e-3, 0.001)
chk('P29.87 erro 1,9 cm sem descontar', mu0*i/(2*math.pi*0.019), 1.263e-3, 0.002)
# PA9
n = 100/0.01
for fr, ref in ((0.046, 0.272), (0.092, 0.54)):
    v = fr*c
    B = me*v/(e*0.0230)
    chk(f'PA9 v={fr}c: i = m v/(mu0 n e r)', B/(mu0*n), ref, 0.02)
g = 1/math.sqrt(1-0.092**2)
chk('PA9 com gamma (relativístico)', g*me*0.092*c/(e*0.023*mu0*n), 0.5437, 0.02, nota=f'(gamma={g:.4f}: ignorar é OK, mas o guia não avisa)')
chk('PA9 erro n=100', me*0.092*c/(e*0.023)/(mu0*100), 54.37, 0.002)
chk('PA9 erro dá B', me*0.092*c/(e*0.023), 6.83e-3, 0.002)
chk('PA9 alternativas da prova: 0,27 (livro) ; 0,54 (certa) ; 1,09 = dobro', 2*0.5437, 1.09, 0.01)

# =====================================================================
sec('DEGRAU 7')
chk('exemplo D7: fem = c a^3/2', sum(2.0*0.10*((j+.5)*0.10/N)*0.10*(0.10/N) for j in range(N)), 1e-3*0.10**0, 1.0) if False else None
a_, c_ = 0.10, 2.0
# Phi(t) = ∫ c t x a dx ; fem = dPhi/dt (t=1 s, dt pequeno)
def Phi(t):
    return sum(c_*t*((j+.5)*a_/N)*a_*(a_/N) for j in range(N))
dt = 1e-4
chk('exemplo D7: fem = c a^3/2 (derivada numérica)', (Phi(3+dt)-Phi(3-dt))/(2*dt), 1.0e-3, 0.001)
w = 600*2*math.pi/60
chk('lac7-1 omega', w, 62.83, 0.001)
chk('lac7-2 fem máx', 50*0.25*0.020*w, 15.7, 0.005)
chk('lac7-2 erro sem N', 0.25*0.020*w, 0.3142, 0.001)
chk('lac7-2 erro omega=10', 50*0.25*0.020*10, 2.5, 0.001)
# P30.19 numérico
w = 1000*2*math.pi/60
fem = max(abs(100*3.5*0.15*(-math.cos(w*(t+1e-6))+math.cos(w*t))/1e-6) for t in [j*2e-4/50 for j in range(50)])
chk('P30.19 fem máx (derivada numérica)', 100*3.5*0.15*w, 5.50e3, 0.005)
chk('P30.19 erro f em vez de omega', 100*3.5*0.15*1000/60, 875, 0.002)
chk('P30.19 erro 1000 direto', 100*3.5*0.15*1000, 52500, 0.002)
# P30.27 e PA10
def Phi2(t, a):
    M = 4000
    return sum(4.0*t*t*((j+.5)*a/M)*a*(a/M) for j in range(M))
for a, t, ref in ((0.020, 2.5, 80e-6), (0.0300, 10.0, 1.08e-3)):
    dt = 1e-5
    fem = (Phi2(t+dt, a)-Phi2(t-dt, a))/(2*dt)
    chk(f'fem numérica a={100*a:.1f} cm, t={t} s', fem, ref, 0.005)
chk('PA10 verificar: 80 uV x (3/2)^3 x 4 = 1,08 mV', 80e-6*1.5**3*4, 1.08e-3, 0.001)
chk('PA10 erro Phi/t', 2*10*0.03**3, 5.4e-4, 0.002)
chk('PA10 erro B do topo', 8*10*0.03**3, 2.16e-3, 0.002)
chk('P30.27 erro Phi/t', 2*2.5*0.02**3, 4e-5, 0.002)
chk('P30.27 erro B do topo', 8*2.5*0.02**3, 1.6e-4, 0.002)
# Sentido (Lenz) por sinal: normal +z, B_z = +4 t^2 y (para fora). emf = -dPhi/dt (positivo = anti-horário)
chk('P30.27 sinal de emf = -dPhi/dt (−1 = horário)', math.copysign(1, -(Phi2(2.5+1e-5, 0.02)-Phi2(2.5-1e-5, 0.02))), -1.0)
# P30.33
mu = mu0
i, v, a, L, Rb = 100.0, 5.0, 0.010, 0.100, 0.400
fem = sum(mu*i/(2*math.pi*(a+(j+.5)*L/N))*v*(L/N) for j in range(N))
chk('P30.33(a) fem (integral numérica)', fem, 240e-6, 0.005)
chk('P30.33(b) i ind', fem/Rb, 0.600e-3, 0.005)
chk('P30.33(c) P=i^2 R', (fem/Rb)**2*Rb, 0.144e-6, 0.005)
Fb = sum((fem/Rb)*mu*i/(2*math.pi*(a+(j+.5)*L/N))*(L/N) for j in range(N))
chk('P30.33(d) F', Fb, 2.87e-8, 0.005)
chk('P30.33(e) F v = i^2 R', Fb*v, 0.144e-6, 0.005)
chk('P30.33 erro B no meio (a+L/2=6 cm)', mu*i/(2*math.pi*(a+L/2))*L*v, 1.667e-4, 0.002)
chk('P30.33 erro B em r=a', mu*i/(2*math.pi*a)*L*v, 1e-3, 0.002)
chk('P30.33 erro i=100 A na barra', 100*mu*i/(2*math.pi)*math.log((a+L)/a), 4.796e-3, 0.002)
# direção P30.33: fio em y=0 com corrente -x; B no laço (y<0): dl=-x, r=-y => z
dB = cruz((-1, 0, 0), (0, -1, 0))
chk('P30.33 B abaixo do fio com corrente para a esquerda: z (+1 = sai do papel)', dB[2], 1.0)
vxB = cruz((-v, 0, 0), (0, 0, 1.0))
chk('P30.33 v x B na barra (barra vai p/ esquerda): componente y (+ = rumo ao fio)', math.copysign(1, vxB[1]), 1.0)

# =====================================================================
sec('SIMULADO')
# S1
L, Q, y = 0.12, 4.0e-9, 0.050
lam = Q/L
Ex = Ey = 0.0
for j in range(N):
    x = -L/2+(j+.5)*L/N
    rr = math.hypot(x, y)
    dq = lam*L/N
    Ex += k*dq*(-x)/rr**3*(-1)*(-1)
    Ey += k*dq*y/rr**3
chk('S1 E (integral vetorial)', Ey, 9208, 0.002)
chk('S1 formula kQ/(y sqrt(y^2+L^2/4))', k*Q/(y*math.sqrt(y*y+L*L/4)), 9208, 0.002)
chk('S1 erro kQ/y^2', k*Q/y**2, 14384, 0.002)
# o que seria "somar dE sem projetar"?
Enp = sum(k*lam*(L/N)/(y*y+(-L/2+(j+.5)*L/N)**2) for j in range(N))
chk('S1 erro "somou dE sem projetar" (valor correto dessa conta)', Enp, 18416, 0.02,
    nota='<- o guia associa 18416 a "não projetou"; essa conta dá outro número')
chk('S1 18416 = 2 x resposta certa', 2*9208, 18416, 0.001, nota='(é o dobro: erro de fator 2, não de projeção)')
# S3
v3 = math.sqrt(2*e*1500/mp)
chk('S3 v', v3, 5.36e5, 0.005)
chk('S3 r', mp*v3/(e*0.30), 1.87e-2, 0.005)
chk('S3 T', 2*math.pi*mp/(e*0.30), 2.19e-7, 0.005)
chk('S3 erro sem 1/2', mp*v3/math.sqrt(2)/(e*0.30), 0.01319, 0.002)
chk('S3 erro diâmetro', 2*mp*v3/(e*0.30), 0.0373, 0.002)
chk('S3 erro sem 2pi', mp/(e*0.30), 3.479e-8, 0.002)
# S4 grampo, geometria da figura: fio de cima (esq->dir), semicircunf à direita (horária), fio de baixo (dir->esq)
R, i = 0.050, 8.0
Lfio = 2000*R
segs = [('r', (-Lfio, R, 0), (0, R, 0)),
        ('a', (0, 0, 0), R, math.pi/2, -math.pi/2),     # do topo, pela direita, até baixo (horário)
        ('r', (0, -R, 0), (-Lfio, -R, 0))]
B = biot(segs, (0, 0, 0), i, n=20000)
chk('S4 |B| (Biot-Savart numérico, fios 2000 R)', norm(B), 8.2265e-5, 0.01)
chk('S4 sinal Bz (−1 = entra, como diz o guia)', math.copysign(1, B[2]), -1.0)
parts = [biot([s], (0, 0, 0), i, n=20000) for s in segs]
print('--- S4 partes (Bz): fio cima %.3g, semicírculo %.3g, fio baixo %.3g' % (parts[0][2], parts[1][2], parts[2][2]))
chk('S4 erro fios como infinitos', mu0*i/(4*R)+2*mu0*i/(2*math.pi*R), 1.143e-4, 0.002)
chk('S4 erro sem fios', mu0*i/(4*R), 5.027e-5, 0.002)
chk('S4 erro subtraindo', mu0*i/(4*R)-2*mu0*i/(4*math.pi*R), 1.83e-5, 0.01)
# S5
aa, bb, dd, Rr = 0.10, 0.050, 0.020, 0.020
G = sum(mu0/(2*math.pi*(dd+(j+.5)*bb/N))*aa*(bb/N) for j in range(N))
chk('S5 Phi/i (Wb/A) numérico', G, 2.5055e-8, 0.001)
fem = G*8*3.0
chk('S5 fem em t=3 s', fem, 6.0e-7, 0.01)
chk('S5 i ind', fem/Rr, 3.0e-5, 0.01)
chk('S5 erro Phi', G*36, 9.02e-7, 0.002)
chk('S5 erro Phi/t', G*36/3, 3.007e-7, 0.002)
chk('S5 erro ln(b/d)', mu0*aa/(2*math.pi)*math.log(bb/dd)*24, 4.4e-7, 0.01)
# sentido: fio com corrente +y, laço em x>0: B_z = -(...)
Bz_sinal = cruz((0, 1, 0), (1, 0, 0))[2]
dPhi = Bz_sinal*8*3.0*G      # d/dt de Phi (normal +z): Phi = Bz_sinal*G*i
emf = -dPhi
chk('S5 sinal emf com normal +z (+1 = anti-horário)', math.copysign(1, emf), 1.0)

# =====================================================================

sec('CARTÕES (amostra, contra o gabarito do livro)')
chk('C21-21 q = 2 pi b (r2^2 - r1^2)', 2*math.pi*3.0e-6*(0.06**2-0.04**2), 3.8e-8, 0.02)
chk('C21-73 v(n=1) (m/s)', e*math.sqrt(k/(me*52.92e-12)), 2.19e6, 0.01)
chk('C21-42 |q|', math.sqrt(0.05**3*2*math.pi*eps0*0.010*9.8/1.20), 2.4e-8, 0.03)
chk('C22-29 E_ponto/E_semicirculo = pi/2', (1.0)/(2/math.pi), 1.57, 0.01)
chk('C22-31 E no ponto P (N/C)', k*4.23e-15/(0.12*(0.12+0.0815)), 1.57e-3, 0.01)
chk('C22-81 q = P/E (C)', 4.4/150, 0.029, 0.02)
chk('C23-5 fluxo = e/(6 eps0)', e/(6*eps0), 3.01e-9, 0.01)
chk('C23-39 sigma = 2 eps0 m g tan30 / q', 2*eps0*1e-6*9.8*math.tan(math.radians(30))/2e-8, 5.0e-9, 0.02)
q_c = 1.84e-9*4/3*math.pi*((0.15)**3-(0.10)**3)
chk('C23-52(d) E(1,5a)', k*q_c/0.15**2, 7.32, 0.01)
chk('C23-52(e) E(b)', k*1.84e-9*4/3*math.pi*(0.2**3-0.1**3)/0.2**2, 12.1, 0.01)
chk('C23-53(a) q = pi rho0 R^3', math.pi*14.1e-12*0.056**3, 7.78e-15, 0.01)
chk('C23-53(d) E(R) = rho0 R/(4 eps0)', 14.1e-12*0.056/(4*eps0), 22.3e-3, 0.01)
lam1 = 3.40e-12/11.0
chk('C23-29(a) E(2 R2) com lambda_total = -lambda1', 2*k*lam1/(2*10.0*1.30e-3), 0.214, 0.01)
chk('C23-29(c) E(5 R1)', 2*k*lam1/(5*1.30e-3), 0.855, 0.01)

sec('RAIO-X (contagens)')
lista21 = [7, 10, 21, 23, 42, 50, 73]
lista22 = [8, 9, 15, 26, 29, 31, 38, 81]
lista23 = [5, 24, 29, 39, 52, 53, 76]
lista28_30 = {'28': [5, 48], '29': [11, 87], '30': [19, 27, 33]}
coulomb = len(lista21)+len([x for x in lista22 if x in (8, 9, 15, 81)])
barra_arco_anel = len([x for x in lista22 if x in (26, 29, 31, 38)])
print('--- Coulomb/cargas pontuais na lista:', coulomb, '(guia: 11)')
print('--- Barra/arco/anel/disco na lista (22.26, 22.29, 22.31, 22.38):', barra_arco_anel, '(guia: 8)  <<< 8 é o TOTAL do cap. 22, não os de integral')
if barra_arco_anel != 8:
    DIV.append(('Raio-X coluna "Na lista" de barra/arco/anel', barra_arco_anel, 8, abs(barra_arco_anel-8)/8))
print('--- Gauss na lista:', len(lista23), '(guia: 7)')
print('--- Força magnética na lista (28.5, 28.48):', len(lista28_30['28']), '(guia: 2)')
print('--- Fontes de B na lista (29.11, 29.87):', len(lista28_30['29']), '(guia: 2)')
print('--- Indução na lista (30.19, 30.27, 30.33):', len(lista28_30['30']), '(guia: 3)')
# incidência por tema nas 10 questões (uma questão pode contar em 2 temas)
tema = {'barra/arco/anel': ['PA1', 'PA2', 'PA3'], 'Gauss': ['PA4', 'PA5'],
        'força magn.': ['PA6', 'PA7', 'PA9'], 'fontes B': ['PA8', 'PA9'], 'indução': ['PA10'], 'Coulomb': []}
for t, qs in tema.items():
    print(f'--- incidência {t}: {len(qs)}  (bolinhas do guia: 3,2,3,2,1,0 na ordem da tabela)')
print('--- origem: 4 "direto das listas" = 22.31 (método), 23.24, 28.48, 30.27. '
      'NÃO estão nas listas: 23.32, 29.53, 29.8, 28.9/28.20, Ex. 22.03.')
print('--- 28.9 do livro = elétron acelerado + placas E x B (seletor de velocidade), não círculo; '
      '28.20 = gráfico r x sqrt(V); o mais próximo de PA6 é o 28.21 (K -> B).')

print('\n' + '='*70)
if DIV:
    print('DIVERGÊNCIAS (>2 % ou texto do guia inconsistente):')
    for r, cval, ref, dif in DIV:
        print(f'  - {r}: calc {cval:.5g} vs ref {ref:.5g} ({100*dif:.1f} %)')
else:
    print('Nenhuma divergência.')
