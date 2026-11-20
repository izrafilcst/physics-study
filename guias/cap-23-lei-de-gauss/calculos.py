"""Contas do guia do Capítulo 23 (Lei de Gauss).

Toda conta numérica do guia sai daqui. Rode com:  python3 -I calculos.py
Cada linha mostra o valor calculado e, quando existe, a resposta do gabarito do
livro. Divergência acima de 2 % é marcada com  <<< DIVERGE.
Questões pares não têm gabarito: aparecem como "calculada pelo guia".
"""
import math

# Constantes (as do livro)
k = 8.99e9          # N·m²/C²
eps0 = 8.85e-12     # C²/(N·m²)
e = 1.602e-19       # C
g = 9.8             # m/s²
m_e = 9.11e-31      # kg
R_TERRA = 6.37e6    # m (Apêndice C do livro)
E_RUPTURA = 3.0e6   # N/C

LINHAS = []
DIVERGENCIAS = []


def mostra(rotulo, valor, gabarito=None, unidade="", tol=0.02, ref="gabarito"):
    """Imprime o valor; se houver gabarito, compara (erro relativo)."""
    txt = f"{rotulo:<62} {valor: .4g} {unidade}"
    if gabarito is not None:
        if gabarito == 0:
            ok = abs(valor) < 1e-12
            err = abs(valor)
        else:
            err = abs(valor - gabarito) / abs(gabarito)
            ok = err <= tol
        txt += f"   | {ref} {gabarito:.4g}  ({err*100:.2f} %)"
        if not ok:
            txt += "  <<< DIVERGE"
            DIVERGENCIAS.append(rotulo)
    print(txt)
    LINHAS.append(txt)
    return valor


def titulo(t):
    print("\n" + "=" * 80 + "\n" + t + "\n" + "=" * 80)


def E_linha(lam, r):
    """Campo de uma linha infinita (ou de qualquer distribuição com simetria cilíndrica vista de fora)."""
    return lam / (2 * math.pi * eps0 * r)


def E_esfera_fora(q, r):
    return q / (4 * math.pi * eps0 * r**2)


# ---------------------------------------------------------------------------
titulo("DEGRAU 0 — gancho (carga da Terra) e pré-requisitos")
E_tb = 150.0  # N/C, para baixo (campo de "tempo bom", Problema 81 do Cap. 22)
A_terra = 4 * math.pi * R_TERRA**2
mostra("Área da Terra 4πR²", A_terra, unidade="m²")
mostra("Fluxo pela esfera em volta da Terra (para dentro)", -E_tb * A_terra, unidade="N·m²/C")
Q_terra = mostra("Carga da Terra Q = ε0 Φ", -eps0 * E_tb * A_terra, unidade="C")
mostra("  ... em número de elétrons em excesso", abs(Q_terra) / e)
mostra("  ... elétrons em excesso por m² do chão", abs(Q_terra) / e / A_terra, unidade="1/m²")
mostra("  ... elétrons em excesso por cm² do chão", abs(Q_terra) / e / A_terra / 1e4, unidade="1/cm²")
mostra("  ... átomos da superfície (~1e15 por cm²) por elétron extra", 1e15 / (abs(Q_terra) / e / A_terra / 1e4))
mostra("Pré 1: 45,0 fC em C", 45.0e-15, unidade="C")
mostra("Pré 2: E·A com E=(4î) e A=(2î+3ĵ): 4·2 + 0·3", 4 * 2 + 0 * 3, unidade="N·m²/C")
mostra("Pré 3: área da esfera de raio 2,0 cm", 4 * math.pi * 0.02**2, unidade="m²")
mostra("Pré 3: volume da casca a=1 b=2 (unid.)  (4/3)π(8-1)", 4 / 3 * math.pi * (2**3 - 1**3))
mostra("Pré 4: dobrar r num campo kq/r² multiplica E por", 1 / 2**2)
mostra("Pré 5: tan 30°", math.tan(math.radians(30)))
mostra("Pré 6: ∫0^R r³ dr com R = 2", 2**4 / 4)

# ---------------------------------------------------------------------------
titulo("DEGRAU 1 — fluxo")
# Exemplo resolvido: Problema 1
lado = 3.2e-3
A = lado**2
mostra("P1: área do quadrado", A, unidade="m²")
mostra("P1: fluxo E A cos(180°-35°)", 1800 * A * math.cos(math.radians(145)), -0.015, "N·m²/C")
mostra("P1 (erro comum): sem o sinal, E A cos 35°", 1800 * A * math.cos(math.radians(35)), unidade="N·m²/C")
mostra("P1 (erro comum): E A sen 35°", 1800 * A * math.sin(math.radians(35)), unidade="N·m²/C")
# Lacuna: Problema 3, face direita com normal +ĵ, aresta 1,40 m
A3 = 1.40**2
mostra("P3: área da face", A3, unidade="m²")
mostra("P3(a) E = 6,00î: Φ face direita", 6.00 * 0, 0, "N·m²/C")
mostra("P3(b) E = -2,00ĵ: Φ face direita", -2.00 * A3, -3.92, "N·m²/C")
mostra("P3(c) E = -3,00î + 4,00k̂: Φ face direita", 0.0, 0, "N·m²/C")
mostra("P3(d) fluxo total (campo uniforme)", 0.0, 0, "N·m²/C")
# Pergunta 1(a)
mostra("Pergunta 1(a): (2î+3ĵ)·(4î)", 2 * 4 + 3 * 0, 8, "N·m²/C")
# Widget W1: E = 1000 N/C, quadrado de 10 cm
mostra("W1: Φ com E=1000 N/C, A=0,01 m², θ=60°", 1000 * 0.01 * math.cos(math.radians(60)), unidade="N·m²/C")
mostra("W1: Φ com θ=120°", 1000 * 0.01 * math.cos(math.radians(120)), unidade="N·m²/C")
# Revisão 6
mostra("Revisão: 200 N/C, quadrado 0,1 m, θ=60°", 200 * 0.1**2 * math.cos(math.radians(60)), unidade="N·m²/C")
# Ficha: valores típicos de fluxo
mostra("Ficha: fluxo de um próton  e/ε0", e / eps0, unidade="N·m²/C")
mostra("Ficha: fluxo de 1 µC  (1e-6/ε0)", 1e-6 / eps0, unidade="N·m²/C")

# ---------------------------------------------------------------------------
titulo("DEGRAU 2 — lei de Gauss")
q7 = 1.8e-6
mostra("Ex. resolvido: Problema 7, fluxo total q/ε0", q7 / eps0, 2.0e5, "N·m²/C")
mostra("Ex. resolvido: metade de cima da esfera q/(2ε0)", q7 / (2 * eps0), unidade="N·m²/C")
mostra("Ex. resolvido: uma face de cubo com q no centro q/(6ε0)", q7 / (6 * eps0), unidade="N·m²/C")
mostra("P15(a) face que contém o vértice", 0.0, 0)
mostra("P15(b) outra face, em unidades de q/ε0: (1/8)/3", 1 / 8 / 3, 0.0417)
# Teste 2 adaptado: fluxos por face (+ = para fora), N·m²/C
cubos = {
    "1": [+5, +7, +2, -7, -4, -3],
    "2": [+10, +3, +5, -3, -4, -6],
    "3": [+2, +5, -6, -8, -7, -5],
}
for nome, fl in cubos.items():
    tot = sum(fl)
    mostra(f"Teste 2 adaptado: cubo {nome}, fluxo total", tot, unidade="N·m²/C")
    mostra(f"  q_env = ε0 Φ (cubo {nome})", eps0 * tot, unidade="C")
# Questão P5
P5 = mostra("P5: |Φ| = e/(6ε0)", e / (6 * eps0), 3.01e-9, "N·m²/C")
mostra("P5 (erro comum): e/ε0 (cubo inteiro)", e / eps0, unidade="N·m²/C")
mostra("P5 (erro comum): e/(2ε0) (meia esfera)", e / (2 * eps0), unidade="N·m²/C")
mostra("P5 (erro comum): e/(4ε0)", e / (4 * eps0), unidade="N·m²/C")
mostra("P5 (erro comum): campo × área com k e/(d/2)² · d² = 4ke", 4 * k * e, unidade="N·m²/C")

# ---------------------------------------------------------------------------
titulo("DEGRAU 3 — simetria esférica")
mostra("Gancho resolvido: carga da Terra", Q_terra, unidade="C")
# Exemplo resolvido: Problema 78 (6,00 pC em esfera de 4,00 cm)
q78, R78 = 6.00e-12, 0.0400
rho78 = q78 / (4 / 3 * math.pi * R78**3)
mostra("P78: ρ = q/(4πR³/3)", rho78, unidade="C/m³")
mostra("P78(a) r = 6,00 cm (fora): k q / r²", k * q78 / 0.06**2, unidade="N/C")
mostra("P78(b) r = 3,00 cm (dentro): ρ r /(3ε0)", rho78 * 0.03 / (3 * eps0), unidade="N/C")
mostra("P78(b) conferência: k q r / R³", k * q78 * 0.03 / R78**3, unidade="N/C")
mostra("P78 na superfície: k q / R²", k * q78 / R78**2, unidade="N/C")
# Lacuna: Problema 49 (b), (c), (d)
a49, q49 = 0.0200, 5.00e-15
mostra("P49(b) r = a/2: k q r/a³", k * q49 * (a49 / 2) / a49**3, 56.2e-3, "N/C")
mostra("P49(c) r = a: k q/a²", k * q49 / a49**2, 112e-3, "N/C")
mostra("P49(d) r = 1,5a: k q/r²", k * q49 / (1.5 * a49)**2, 49.9e-3, "N/C")
mostra("P49 (erro comum em b): k q/(a/2)² (fórmula de fora)", k * q49 / (a49 / 2)**2, unidade="N/C")
# Checkpoint: Problema 65(b)
mostra("P65(a) fração da carga em R/2", 0.5**3, 0.125)
mostra("P65(b) E(R/2)/E(R)", 0.5, 0.500)
# Questão P52
rho52, a52 = 1.84e-9, 0.100
b52 = 2 * a52


def E52(r):
    if r <= a52:
        return 0.0
    if r <= b52:
        return rho52 * (r**3 - a52**3) / (3 * eps0 * r**2)
    return rho52 * (b52**3 - a52**3) / (3 * eps0 * r**2)


mostra("P52(a) r = 0 (calculada pelo guia)", E52(0.0), unidade="N/C")
mostra("P52(b) r = a/2", E52(a52 / 2), unidade="N/C")
mostra("P52(c) r = a", E52(a52), unidade="N/C")
P52d = mostra("P52(d) r = 1,5a", E52(1.5 * a52), unidade="N/C")
P52e = mostra("P52(e) r = b", E52(b52), unidade="N/C")
P52f = mostra("P52(f) r = 3b", E52(3 * b52), unidade="N/C")
mostra("P52 carga total da casca", rho52 * 4 / 3 * math.pi * (b52**3 - a52**3), unidade="C")
mostra("P52(f) conferência: k Q/r²", k * rho52 * 4 / 3 * math.pi * (b52**3 - a52**3) / (3 * b52)**2, unidade="N/C")
mostra("P52(f) conferência: E(b)/9", P52e / 9, unidade="N/C")
mostra("P52 (erro comum d): sem tirar a cavidade, ρ r/(3ε0)", rho52 * 1.5 * a52 / (3 * eps0), unidade="N/C")
mostra("P52 (erro comum d): casca toda (b³-a³) em r = 1,5a", rho52 * (b52**3 - a52**3) / (3 * eps0 * (1.5 * a52)**2), unidade="N/C")
mostra("P52 (erro comum e): sem tirar a cavidade, ρ b/(3ε0)", rho52 * b52 / (3 * eps0), unidade="N/C")
mostra("P52 (erro comum f): sem tirar a cavidade", rho52 * b52**3 / (3 * eps0 * (3 * b52)**2), unidade="N/C")
mostra("P52 (erro comum f): r = 3a em vez de 3b", rho52 * (b52**3 - a52**3) / (3 * eps0 * (3 * a52)**2), unidade="N/C")
# Widget W3 (unidades: r/R, E em ρR/(3ε0))
aW, rW = 0.4, 0.8
mostra("W3: a/R = 0,4, r/R = 0,8: (r³-a³)/r²", (rW**3 - aW**3) / rW**2)

# ---------------------------------------------------------------------------
titulo("DEGRAU 4 — cascas de cebola (ρ não uniforme)")
C4, R4 = 5.0e-6, 0.10  # ρ = C r², C em C/m⁵
mostra("Ex. resolvido: ρ na superfície C R²", C4 * R4**2, unidade="C/m³")
q4 = mostra("Ex. resolvido: carga total 4πC R⁵/5", 4 * math.pi * C4 * R4**5 / 5, unidade="C")
mostra("Ex. resolvido: E(R) = C R³/(5ε0)", C4 * R4**3 / (5 * eps0), unidade="N/C")
mostra("Ex. resolvido: conferência E(R) = k q/R²", k * q4 / R4**2, unidade="N/C")
mostra("Ex. resolvido: E(R/2) = C (R/2)³/(5ε0)", C4 * (R4 / 2)**3 / (5 * eps0), unidade="N/C")
mostra("Ex. resolvido (erro comum): ρ(R)·(4/3)πR³", C4 * R4**2 * 4 / 3 * math.pi * R4**3, unidade="C")
# Lacuna: Problema 55 ao contrário: E = K r⁴  ->  ρ = 6 K ε0 r³
mostra("P55: coeficiente de ε0 K r³ em ρ (d/dr(r⁶)/r²)", 6.0, 6.0)
# Checkpoint: E constante -> ρ ∝ 1/r ; revisão: fração de carga em R/2 para ρ ∝ r
mostra("Revisão: ρ ∝ r, fração da carga em R/2 = (1/2)⁴", 0.5**4)
mostra("Checkpoint 4-2: ρ=Ar, conta errada AR·(4/3)πR³ / certa πAR⁴", (4 / 3) / 1)
# Widget W4
mostra("W4: ρ ∝ r², r = R/2: fração de carga (1/2)⁵", 0.5**5)
mostra("W4: ρ ∝ r², r = R/2: E/E(R) = (1/2)³", 0.5**3)
# Questão P53
rs, R53 = 14.1e-12, 0.0560
q53 = mostra("P53(a) q = π ρs R³", math.pi * rs * R53**3, 7.78e-15, "C")
mostra("P53(a) conferência numérica (soma de 200000 cascas)",
       sum(rs * ((i + 0.5) * R53 / 200000) / R53 * 4 * math.pi * ((i + 0.5) * R53 / 200000)**2 * (R53 / 200000) for i in range(200000)),
       7.78e-15, "C")
mostra("P53(b) r = 0", 0.0, 0, "N/C")
mostra("P53(c) r = R/2: ρs R/(16 ε0)", rs * R53 / (16 * eps0), 5.58e-3, "N/C")
mostra("P53(d) r = R: ρs R/(4 ε0)", rs * R53 / (4 * eps0), 22.3e-3, "N/C")
mostra("P53(d) conferência: k q/R²", k * q53 / R53**2, 22.3e-3, "N/C")
mostra("P53 fora, r = 2R: E(R)/4", rs * R53 / (4 * eps0) / 4, unidade="N/C")
mostra("P53 (erro comum a): ρs·(4/3)πR³ (como se fosse uniforme)", rs * 4 / 3 * math.pi * R53**3, unidade="C")
mostra("P53 (erro comum a): sem o 4π da casca, ρs R³/4", rs * R53**3 / 4, unidade="C")
mostra("P53 (erro comum a): ρ médio (ρs/2) × volume", rs / 2 * 4 / 3 * math.pi * R53**3, unidade="C")
mostra("P53 (e se) esfera uniforme com a mesma q: E(R/2)", k * q53 * 0.5 / R53**2, unidade="N/C")
mostra("P53(c)/(d) = 1/4", (rs * R53 / (16 * eps0)) / (rs * R53 / (4 * eps0)))
mostra("P53 (erro comum c): ρ(R/2)·r/(3ε0)", (rs / 2) * (R53 / 2) / (3 * eps0), unidade="N/C")
mostra("P53 (erro comum d): ρs R/(3ε0)", rs * R53 / (3 * eps0), unidade="N/C")
mostra("P53 (erro comum c): k q (R/2)/R³ (como esfera uniforme)", k * q53 * 0.5 / R53**2, unidade="N/C")

# ---------------------------------------------------------------------------
titulo("DEGRAU 5 — simetria cilíndrica")
# Exemplo 23.06
L6, R6, Ec = 1.8, 0.10, 2.4e6
Q6 = mostra("Ex. 23.06: Q = 2π ε0 R L Ec", 2 * math.pi * eps0 * R6 * L6 * Ec, unidade="C")
mostra("Ex. 23.06: λ = Q/L", Q6 / L6, unidade="C/m")
mostra("Ex. 23.06: conferência E(R) = λ/(2π ε0 R)", E_linha(Q6 / L6, R6), unidade="N/C")
# Lacuna: Problema 31 (raios em cm; o texto em português diz m por engano)
# O gabarito tem 2 algarismos: 2,2475e6 vira "2,3e6" arredondando 2,25 para cima. Tolerância de 3 %.
mostra("P31(a) r = 4,0 cm: λ1/(2π ε0 r)", E_linha(5.0e-6, 0.040), 2.3e6, "N/C", tol=0.03)
mostra("P31(c) r = 8,0 cm: |λ1+λ2|/(2π ε0 r)", abs(E_linha(5.0e-6 - 7.0e-6, 0.080)), 4.5e5, "N/C")
mostra("P31 (se os raios fossem em m, r=4 cm estaria dentro de tudo)", 0.0)
mostra("P31 (erro comum a): λ1+λ2 em 4 cm", abs(E_linha(-2.0e-6, 0.040)), unidade="N/C")
mostra("P31 (erro comum a): só λ2 em 4 cm", E_linha(7.0e-6, 0.040), unidade="N/C")
mostra("P31 (erro comum a): kλ/r² (fórmula de ponto)", k * 5.0e-6 / 0.040**2, unidade="N/C")
mostra("P31 (erro comum c): |λ1|+|λ2| em 8 cm", E_linha(12.0e-6, 0.080), unidade="N/C")
mostra("P31 (erro comum c): só λ1 em 8 cm", E_linha(5.0e-6, 0.080), unidade="N/C")
mostra("P25: λ = 2π ε0 r E", 2 * math.pi * eps0 * 2.0 * 4.5e4, 5.0e-6, "C/m")
mostra("P25 (erro): ε0 r E", eps0 * 2.0 * 4.5e4, unidade="C/m")
mostra("P25 (erro): π ε0 r E", math.pi * eps0 * 2.0 * 4.5e4, unidade="C/m")
mostra("P25 (erro): 4π ε0 r E", 4 * math.pi * eps0 * 2.0 * 4.5e4, unidade="C/m")
# Questão P24
lam24, R24 = 2.00e-8, 0.0300
mostra("P24(a) r = R/2 (calculada pelo guia)", 0.0, unidade="N/C")
P24b = mostra("P24(b) r = 2R: λ/(2π ε0 r)", E_linha(lam24, 2 * R24), unidade="N/C")
mostra("P24 logo fora do tubo, r = R", E_linha(lam24, R24), unidade="N/C")
mostra("P24 (erro comum a): fórmula do fio em R/2", E_linha(lam24, R24 / 2), unidade="N/C")
mostra("P24 (e se) cilindro maciço com a mesma λ: E(R/2)", E_linha(lam24, R24) / 2, unidade="N/C")
mostra("P24 (erro comum b): r = R", E_linha(lam24, R24), unidade="N/C")
mostra("P24 (erro comum b): λ/(4π ε0 r²) (fórmula de esfera)", lam24 / (4 * math.pi * eps0 * (2 * R24)**2), unidade="N/C")
mostra("P24 (erro comum b): λ/(2 ε0 r) (sem π)", lam24 / (2 * eps0 * 2 * R24), unidade="N/C")
# Questão P76: valores-teste
rho76, R76 = 1.00e-6, 0.0200
mostra("P76 teste: r = 1,50 cm (dentro) ρ r/(2ε0)", rho76 * 0.0150 / (2 * eps0), unidade="N/C")
mostra("P76 teste: r = 5,00 cm (fora) ρ R²/(2ε0 r)", rho76 * R76**2 / (2 * eps0 * 0.0500), unidade="N/C")
mostra("P76 conferência: fora = λ/(2π ε0 r) com λ = ρπR²", E_linha(rho76 * math.pi * R76**2, 0.0500), unidade="N/C")
mostra("P76 (erro comum): ρ r/(3ε0) (fórmula da esfera) em 1,5 cm", rho76 * 0.0150 / (3 * eps0), unidade="N/C")
mostra("P76 (erro comum): fórmula de dentro usada fora (5 cm)", rho76 * 0.0500 / (2 * eps0), unidade="N/C")
mostra("P76 (erro comum): ρ r/ε0 (sem o 2) em 1,5 cm", rho76 * 0.0150 / eps0, unidade="N/C")
mostra("P76 continuidade em r = R: ρR/(2ε0)", rho76 * R76 / (2 * eps0), unidade="N/C")
mostra("P76 (erro comum): ρR²/(2ε0 r²) em 5 cm", rho76 * R76**2 / (2 * eps0 * 0.05**2), unidade="N/C")
# Ficha: valores típicos de λ
mostra("Ficha: λ do fio do contador Geiger (P75: 3,6 nC em 16 cm)", 3.6e-9 / 0.16, unidade="C/m")
mostra("P75 conferência: q = 2π ε0 r L E", 2 * math.pi * eps0 * 0.014 * 0.16 * 2.9e4, 3.6e-9, "C")
mostra("P29: λ da barra Q1/L", 3.40e-12 / 11.00, unidade="C/m")

# ---------------------------------------------------------------------------
titulo("DEGRAU 6 — condutores")
mostra("Ex. 23.05: carga na superfície interna", +5.0e-6, unidade="C")
mostra("Ex. 23.05: carga na superfície externa (casca neutra)", 0 - 5.0e-6, unidade="C")
mostra("P21(a) superfície da cavidade = -q", -3.0e-6, -3.0e-6, "C")
mostra("P21(b) superfície externa = 10 µC - (-3 µC)", 10e-6 - (-3.0e-6), 1.3e-5, "C")
# Pergunta 9 (gabarito: (a) 2, 1, 3; (b) todos +4q)
for nome, (qe, qc) in {"1": (4, 0), "2": (-6, 10), "3": (16, -12)}.items():
    mostra(f"Pergunta 9, situação {nome}: interna (em q)", -qe)
    mostra(f"Pergunta 9, situação {nome}: externa (em q)", qc + qe)
# Questão P29
Q1, L29, R1 = 3.40e-12, 11.00, 1.30e-3
R2, Q2 = 10.0 * R1, -2.00 * Q1
lam_a = (Q1 + Q2) / L29
mostra("P29(a) r = 2R2: |λ1+λ2|/(2π ε0 r)", abs(E_linha(lam_a, 2 * R2)), 0.214, "N/C")
mostra("P29(b) sinal de q_env em r = 2R2 (−1 = para dentro)", math.copysign(1, Q1 + Q2))
mostra("P29(c) r = 5R1: λ1/(2π ε0 r)", E_linha(Q1 / L29, 5 * R1), 0.855, "N/C")
mostra("P29(d) sinal de q_env em r = 5R1 (+1 = para fora)", math.copysign(1, Q1))
mostra("P29(e) superfície interna da casca = -Q1", -Q1, -3.40e-12, "C")
mostra("P29(f) superfície externa = Q2 - (-Q1)", Q2 + Q1, -3.40e-12, "C")
mostra("P29 (erro comum a): só Q2", abs(E_linha(Q2 / L29, 2 * R2)), unidade="N/C")
mostra("P29 (erro comum a): |Q1|+|Q2|", E_linha((Q1 + abs(Q2)) / L29, 2 * R2), unidade="N/C")
mostra("P29 (erro comum a): r = R2 em vez de 2R2", abs(E_linha(lam_a, R2)), unidade="N/C")
mostra("P29 (erro comum a): sem dividir por L", abs((Q1 + Q2) / (2 * math.pi * eps0 * 2 * R2)), unidade="N/C")
mostra("P29 (erro comum c): r = 5R2", E_linha(Q1 / L29, 5 * R2), unidade="N/C")
mostra("P29 (erro comum c): sem dividir por L", E_linha(Q1, 5 * R1), unidade="N/C")
mostra("P29: razão (c)/(a) = (2R2)/(5R1)", (2 * R2) / (5 * R1))
mostra("P29 total da casca Q2", Q2, unidade="C")
mostra("P29 (erro comum c): Q1+Q2", abs(E_linha((Q1 + Q2) / L29, 5 * R1)), unidade="N/C")

# ---------------------------------------------------------------------------
titulo("DEGRAU 7 — placas")
sig7 = 2.0e-6
E7 = mostra("Ex. resolvido: placa σ = 2,0 µC/m², E = σ/(2ε0)", sig7 / (2 * eps0), unidade="N/C")
mostra("Ex. resolvido: aceleração de um elétron eE/m", e * E7 / m_e, unidade="m/s²")
mostra("Ex. resolvido: comparação com g", e * E7 / m_e / g)
# Lacuna: esfera flutuando sobre placa horizontal
mL, qL = 5.0e-6, 3.0e-8
mostra("Lacuna: peso m g", mL * g, unidade="N")
EL = mostra("Lacuna: E necessário = m g / q", mL * g / qL, unidade="N/C")
mostra("Lacuna: σ = 2 ε0 E", 2 * eps0 * EL, unidade="C/m²")
mostra("Lacuna (erro comum): σ = ε0 E", eps0 * EL, unidade="C/m²")
# Questão P39
m39, q39, th = 1.0e-6, 2.0e-8, math.radians(30)
mostra("P39: σ = 2 ε0 m g tan θ / q", 2 * eps0 * m39 * g * math.tan(th) / q39, 5.0e-9, "C/m²")
mostra("P39: força elétrica m g tan θ", m39 * g * math.tan(th), unidade="N")
mostra("P39: campo da placa E = F/q", m39 * g * math.tan(th) / q39, unidade="N/C")
mostra("P39 (e se) placa condutora: σ = ε0 E", eps0 * m39 * g * math.tan(th) / q39, unidade="C/m²")
mostra("P39 (erro comum): σ = ε0 E (fórmula de condutor)", eps0 * m39 * g * math.tan(th) / q39, unidade="C/m²")
mostra("P39 (erro comum): sen θ no lugar de tan θ", 2 * eps0 * m39 * g * math.sin(th) / q39, unidade="C/m²")
mostra("P39 (erro comum): cos θ no lugar de tan θ", 2 * eps0 * m39 * g * math.cos(th) / q39, unidade="C/m²")
mostra("P39 (erro comum): tan 60° (ângulo com a horizontal)", 2 * eps0 * m39 * g * math.tan(math.radians(60)) / q39, unidade="C/m²")
mostra("P39 (erro comum): 1,0 mg = 1e-3 kg", 2 * eps0 * 1e-3 * g * math.tan(th) / q39, unidade="C/m²")
# Visão geral: Exemplo 23.07
Ep, En = 6.8e-6 / (2 * eps0), 4.3e-6 / (2 * eps0)
mostra("Ex. 23.07: E(+) = σ+/(2ε0)", Ep, unidade="N/C")
mostra("Ex. 23.07: E(-) = |σ-|/(2ε0)", En, unidade="N/C")
mostra("Ex. 23.07: à esquerda E(+) - E(-)", Ep - En, unidade="N/C")
mostra("Ex. 23.07: entre as placas E(+) + E(-)", Ep + En, unidade="N/C")
# Ficha: σ máximo de um condutor no ar
mostra("Ficha: σ máximo antes da ruptura do ar ε0·3e6", eps0 * E_RUPTURA, unidade="C/m²")
mostra("Ficha: σ do satélite (P19 gabarito 4,5e-7)", 2.4e-6 / (4 * math.pi * 0.65**2), 4.5e-7, "C/m²")
# Teste 4: só a esfera conta (placas iguais se cancelam entre elas)
mostra("Teste 4: E nos pontos 3 e 4 / E no ponto 2 = (2d/d)²", (2 / 1)**2)

# ---------------------------------------------------------------------------
titulo("V2 — correções e contas das 'Dúvidas da turma'")
mostra("lac1-2 (erro comum): aresta em vez de área, -2,00 × 1,40", -2.00 * 1.40, unidade="N·m²/C")
mostra("P5 com e = 1,60e-19 (o livro): e/(6ε0)", 1.60e-19 / (6 * eps0), 3.01e-9, "N·m²/C")
# Ângulo sólido de um quadrado de lado d visto do eixo a uma distância h: Ω = 4 asin(d²/(d² + 4h²))
def fracao_quadrado(h_sobre_d):
    return 4 * math.asin(1 / (1 + 4 * h_sobre_d**2)) / (4 * math.pi)
mostra("Dúvida P5: fração do fluxo com h = d/2 (deve ser 1/6)", fracao_quadrado(0.5), 1 / 6)
f4 = mostra("Dúvida P5: fração do fluxo com h = d/4", fracao_quadrado(0.25))
mostra("Dúvida P5: fluxo com h = d/4", f4 * e / eps0, unidade="N·m²/C")
mostra("Dúvida P5: fração com h → 0 (metade)", fracao_quadrado(1e-9), 0.5)
# Terra vista de uma gaussiana a 300 m (Problema 13: 60 N/C a 300 m, 100 N/C a 200 m)
mostra("Dúvida Terra: q_env com E = 100 N/C a 200 m", -eps0 * 100 * 4 * math.pi * (R_TERRA + 200)**2, unidade="C")
mostra("Dúvida Terra: q_env com E = 60 N/C a 300 m", -eps0 * 60 * 4 * math.pi * (R_TERRA + 300)**2, unidade="C")
mostra("Dúvida Terra: carga positiva no ar entre 0 e 300 m (com 150 N/C no chão)", -eps0 * 60 * 4 * math.pi * (R_TERRA + 300)**2 - Q_terra, unidade="C")
mostra("Dúvida 300 V: E × 2 m no campo de tempo bom", 150 * 2.0, unidade="V")
mostra("Aquecimento (b): campo no chão se a Terra tivesse -1 C", k * 1.0 / R_TERRA**2, unidade="N/C")
# Placa finita: disco de raio Rd, E/E∞ = 1 - z/sqrt(z² + Rd²)
Rd = math.sqrt(0.10**2 / math.pi)
mostra("Dúvida placa: raio do disco com a área de um quadrado de 10 cm", Rd, unidade="m")
mostra("Dúvida placa: E/E∞ a 1 cm desse disco", 1 - 0.01 / math.sqrt(0.01**2 + Rd**2))
mostra("Dúvida placa: z/R para erro de 10 % (1 - z/√(z²+R²) = 0,9)", 0.1 / math.sqrt(1 - 0.01))
# Placa condutora no P39: força de imagem k q²/(2d)² comparada com qE
Fe39 = m39 * g * math.tan(th)
for dd in (0.01, 0.10):
    mostra(f"Dúvida P39 condutora: força de imagem com a esfera a {dd*100:.0f} cm", k * q39**2 / (2 * dd)**2, unidade="N")
mostra("Dúvida P39 condutora: força elétrica do problema qE", Fe39, unidade="N")
mostra("Dúvida P39 condutora: distância em que imagem = qE", math.sqrt(k * q39**2 / (4 * Fe39)), unidade="m")
# Casca do P29 aterrada: externa vai a zero; interna continua -Q1
mostra("Dúvida P29 aterrada: carga que vai para a terra (externa antiga)", Q1 + Q2, unidade="C")
# Ficha D1: folha A4 no campo de tempo bom
mostra("Ficha D1: Φ numa folha A4 (0,0624 m²) deitada, E = 150 N/C", 150 * 0.210 * 0.297, unidade="N·m²/C")
# Régua de campos e cargas
mostra("Régua: núcleo do H sobre o elétron k e / a0²", k * e / 5.29e-11**2, unidade="N/C")
mostra("Régua: cúpula de Van de Graaff R = 20 cm no limite do ar, q = 4πε0R²·3e6", 4 * math.pi * eps0 * 0.20**2 * E_RUPTURA, unidade="C")
mostra("Mulher / fio Geiger: razão de λ", (Q6 / L6) / (3.6e-9 / 0.16))
# Revisão intercalada numérica
mostra("rev-8: casca fina de 10 cm com +4,0 nC, E a 20 cm", k * 4.0e-9 / 0.20**2, unidade="N/C")
mostra("rev-8 (erro): usou r = 10 cm", k * 4.0e-9 / 0.10**2, unidade="N/C")
mostra("rev-8 (erro): sem o quadrado", k * 4.0e-9 / 0.20, unidade="N/C")
mostra("rev-9: fio com λ = 3,0 nC/m, E a 4,0 cm", E_linha(3.0e-9, 0.040), unidade="N/C")
mostra("rev-9 (erro): kλ/r² (fórmula de ponto)", k * 3.0e-9 / 0.040**2, unidade="N/C")
mostra("rev-9 (erro): sem o 2 (λ/(4πε0 r))", k * 3.0e-9 / 0.040, unidade="N/C")
mostra("P52 (erro comum f): fórmula de dentro em 3b", rho52 * ((3 * b52)**3 - a52**3) / (3 * eps0 * (3 * b52)**2), unidade="N/C")
mostra("P29 (erro comum a): k|Q1+Q2|/r² (carga pontual)", k * abs(Q1 + Q2) / (2 * R2)**2, unidade="N/C")
mostra("Duas placas do D7 (Ex. 23.07): entre e fora", Ep + En, unidade="N/C")

# ---------------------------------------------------------------------------
titulo("RESUMO")
print(f"{len(LINHAS)} linhas; divergências com o gabarito: {len(DIVERGENCIAS)}")
for d in DIVERGENCIAS:
    print("  -", d)
