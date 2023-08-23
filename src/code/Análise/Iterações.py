# Algoritmos Modificados para Retornar o Número de Iterações

from math import sqrt, floor

def SolucaoIngenua(a, b):
    if (a == 0 or b == 0): return 0

    a = abs(a)
    b = abs(b)
    
    iters = 0
    
    for i in range(min(a, b), 0, -1):
        iters += 1
        
        if ((a % i) == 0 and (b % i) == 0):
            return iters

def AlgoritmoDeEuclides(a, b):
    a = abs(a)
    b = abs(b)
    
    iters = 0
    
    while (a and b):
        iters += 1
        
        temp = b
        b = a % b
        a = temp
    
    return iters

def Fatorar(n):
    fatores = []
    
    d = 2
    iters = 0
    
    while (d*d < n):
        while ((n % d) == 0):
            fatores.append(d)
            n /= d
        d += 1
        iters += 1
    
    if (n != 1): fatores.append(int(n))
    return iters, fatores

def FatoraçãoPrima(a, b):
    a = abs(a)
    b = abs(b)
    
    if (a == 0): return 1
    if (b == 0): return 1
    
    i1, A = Fatorar(a)
    i2, B = Fatorar(b)
    
    res = 1
    iters = i1 + i2
    
    for d in set(A):
        iters += 1
        res *= d**min(A.count(d), B.count(d))
    return iters