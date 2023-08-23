# Algoritmo de Euclides - Múltiplos Inteiros

from AlgoritmoDeEuclides import mdc

def mdcEstendido(*inteiros):
    res = inteiros[0]
    for i in inteiros[1:]:
        res = mdc(res, i)
    
    return res