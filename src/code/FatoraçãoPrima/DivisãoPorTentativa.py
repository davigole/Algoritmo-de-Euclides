def Fatorar(n):
    fatores = []
    
    d = 2
    
    while (d*d <= n):
        while ((n % d) == 0):
            fatores.append(d)
            n /= d
        d += 1
    
    if (n != 1): fatores.append(int(n))
    return fatores