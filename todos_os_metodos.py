# EP1 - Cálculo de raízes com métodos numéricos
# Aluno: SeuNomeSobrenome
# RA: XXXXXXX

import math

# ------------------------
# Funções
# ------------------------
def f1(x, d):
    """Função F1: f(x) = x - (0,20 + 0,05*d)*cos(x)"""
    a = 0.20 + 0.05 * d
    return x - a * math.cos(x)

def f2(x, d):
    """Função F2: f(x) = (0,30 + 0,01*d)*x^2 - 1"""
    a = 0.30 + 0.01 * d
    return a * (x**2) - 1

def f3(x, d):
    """Função F3: f(x) = exp(-(0,10+0,02*d)*x) - x"""
    a = 0.10 + 0.02 * d
    return math.exp(-a * x) - x

# Funções g(x) para Ponto Fixo (garantem contração)
def g1(x, d):
    a = 0.20 + 0.05 * d
    return a * math.cos(x)

def g2(x, d):
    a = 0.30 + 0.01 * d
    return math.sqrt(1 / a)

def g3(x, d):
    a = 0.10 + 0.02 * d
    return math.exp(-a * x)

# Derivadas para Newton
def df1(x, d):
    a = 0.20 + 0.05 * d
    return 1 + a * math.sin(x)

def df2(x, d):
    a = 0.30 + 0.01 * d
    return 2 * a * x

def df3(x, d):
    a = 0.10 + 0.02 * d
    return -a * math.exp(-a * x) - 1

# ------------------------
# Métodos
# ------------------------
def bissecao(funcao, a, b, tol, d):
    print(f"{'Iter':<5}{'a':<15}{'b':<15}{'m':<15}{'f(m)':<15}{'|b-a|':<15}")
    print("-"*80)
    iteracao = 1
    while True:
        m = (a + b) / 2
        fm = funcao(m, d)
        print(f"{iteracao:<5}{a:<15.10f}{b:<15.10f}{m:<15.10f}{fm:<15.10f}{abs(b-a):<15.10f}")
        if abs(fm) < tol or abs(b - a) < tol:
            print(f"\nRaiz aproximada: x ≈ {m:.7f}")
            print("Número de iterações:", iteracao)
            break
        if funcao(a, d) * funcao(m, d) < 0:
            b = m
        else:
            a = m
        iteracao += 1

def ponto_fixo(g, x0, tol, d):
    print(f"{'Iter':<5}{'x':<15}{'g(x)':<15}{'Erro':<15}")
    print("-"*60)
    iteracao = 1
    while True:
        x1 = g(x0, d)
        erro = abs(x1 - x0)
        print(f"{iteracao:<5}{x0:<15.10f}{x1:<15.10f}{erro:<15.10f}")
        if erro < tol:
            print(f"\nRaiz aproximada: x ≈ {x1:.7f}")
            print("Número de iterações:", iteracao)
            break
        x0 = x1
        iteracao += 1

def newton(funcao, derivada, x0, tol, d):
    print(f"{'Iter':<5}{'x':<15}{'f(x)':<15}{'Erro':<15}")
    print("-"*60)
    iteracao = 1
    while True:
        fx = funcao(x0, d)
        dfx = derivada(x0, d)
        x1 = x0 - fx / dfx
        erro = abs(x1 - x0)
        print(f"{iteracao:<5}{x0:<15.10f}{fx:<15.10f}{erro:<15.10f}")
        if erro < tol or abs(fx) < tol:
            print(f"\nRaiz aproximada: x ≈ {x1:.7f}")
            print("Número de iterações:", iteracao)
            break
        x0 = x1
        iteracao += 1

def secantes(funcao, x0, x1, tol, d):
    print(f"{'Iter':<5}{'x0':<15}{'x1':<15}{'x2':<15}{'Erro':<15}")
    print("-"*70)
    iteracao = 1
    while True:
        f0 = funcao(x0, d)
        f1 = funcao(x1, d)
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        erro = abs(x2 - x1)
        print(f"{iteracao:<5}{x0:<15.10f}{x1:<15.10f}{x2:<15.10f}{erro:<15.10f}")
        if erro < tol or abs(funcao(x2, d)) < tol:
            print(f"\nRaiz aproximada: x ≈ {x2:.7f}")
            print("Número de iterações:", iteracao)
            break
        x0, x1 = x1, x2
        iteracao += 1

# ------------------------
# Programa principal
# ------------------------
ra = int(input("Digite o RA: "))
d = ra % 10
tol = 1e-6

# Escolha da função
if d % 3 == 0:
    funcao, g, derivada = f1, g1, df1
    funcao_nome = f"f(x) = x - (0.20 + 0.05*{d})*cos(x)"
    intervalo = (0, math.pi/2)
    chute = 0.5
elif d % 3 == 1:
    funcao, g, derivada = f2, g2, df2
    funcao_nome = f"f(x) = (0.30 + 0.01*{d})*x^2 - 1"
    intervalo = (0, 2)
    chute = 1.0
else:
    funcao, g, derivada = f3, g3, df3
    funcao_nome = f"f(x) = exp(-(0.10 + 0.02*{d})*x) - x"
    intervalo = (0, 1)
    chute = 0.5

# Escolha do método
if d % 4 == 0:
    metodo, metodo_nome = "bissecao", "Bisseção"
elif d % 4 == 1:
    metodo, metodo_nome = "ponto_fixo", "Ponto Fixo"
elif d % 4 == 2:
    metodo, metodo_nome = "newton", "Newton-Raphson"
else:
    metodo, metodo_nome = "secantes", "Secantes"

# ------------------------
# Saída inicial
# ------------------------
print("\n================ INFORMAÇÕES INICIAIS ================")
print(f"RA: {ra}")
print(f"d = {d}")
print(f"Função escolhida: {funcao_nome}")
print(f"Método escolhido: {metodo_nome}")
print("======================================================\n")

# Executa o método
if metodo == "bissecao":
    a, b = intervalo
    bissecao(funcao, a, b, tol, d)
elif metodo == "ponto_fixo":
    ponto_fixo(g, chute, tol, d)
elif metodo == "newton":
    newton(funcao, derivada, chute, tol, d)
elif metodo == "secantes":
    x0, x1 = intervalo
    secantes(funcao, x0, x1, tol, d)
