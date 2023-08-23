def mdc(a, b):
    a = abs(a)
    b = abs(b)
    
    if (a == 0): return b
    if (b == 0): return a
    
    return mdc(b, a % b)
