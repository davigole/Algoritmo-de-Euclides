def Fatorar(n):
    fatores = []
    
    for d in range(2, n+1):
        while ((n % d) == 0):
            fatores.append(d)
            n /= d
    return fatores