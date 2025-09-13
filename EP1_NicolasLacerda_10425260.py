# Função F1: f(x) = x - a*cosx
# com a = 0,20 + 0,05*0
# portando a = 0,20
# Método : Bisseção

import math
# Função F1: f(x) = x - (0,2+ 0,05*d)*math.cos(x)

# Tolerância = 0,0000001
tol = math.pow(10, -6)

ra = int(input("Digite o RA: "))
d = ra % 10
print(d)
if d % 3 == 0:
    print("usa função F1")
    #usa F1
elif d % 3 == 1:
    print("usa função F2")
elif d % 3 == 2:
    print("Usa função F3")


# Chutes iniciais para F1
def chutes_f1():
    a = 0
    b = math.pi/2

# CONSTRUIR UM LOOP DAS FUNÇÕES ATÉ CHEGAR NA TOLERÂNCIA


def ponto_medio(a, b):
    x = 0
    x = (a + b)/2

    return x

def calculo_f1(x):
    resultado = x - 0.2*math.cos(x)
    return resultado

a = 0
b = math.pi/2

# Cabeçalho da tabela
print(f"{'Iter':<5}{'a':<15}{'b':<15}{'m':<15}{'f(m)':<15}{'|b-a|':<15}")
print("-"*80)

iteracao = 1

while True:

    #calcula o ponto médio para ir fazendo a bisseção
    m = ponto_medio(a, b)
    fm = calculo_f1(m)

    print(f"{iteracao:<5}{a:<15.10f}{b:<15.10f}{m:<15.10f}{fm:<15.10f}{abs(b-a):<15.10f}")

    # se chegar no erro acaba loop
    if abs(fm) < tol:
        print(f"\nRaiz aproximada encontrada: x ≈ {m:.7f}")
        break
    # se f(a)*f(b) < 0 então o intervalo está entre 
    if calculo_f1(a)*calculo_f1(m) < 0:
        b = m
    if calculo_f1(m)*calculo_f1(b) < 0:
        a = m

    iteracao += 1

print("Número de iterações:", iteracao)
