from DivisãoPorTentativa import Fatorar

def mdc(a, b):
    a = abs(a)
    b = abs(b)
    
    if (a == 0): return b
    if (b == 0): return a
    
    A = Fatorar(a)
    B = Fatorar(b)
    res = 1
    
    for d in set(A):
        res *= d**min(A.count(d), B.count(d))
    return res