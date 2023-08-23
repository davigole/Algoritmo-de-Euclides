def mdc(a, b):
    a = abs(a)
    b = abs(b)
    
    if (a == 0): return b
    if (b == 0): return a
    
    for i in range(min(a, b), 0, -1):
        if ((a % i) == 0 and (b % i) == 0):
            return i