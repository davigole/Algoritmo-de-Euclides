def mdc(a, b):
    a = abs(a)
    b = abs(b)
    
    while (a and b):
        temp = b
        b = a % b
        a = temp
    
    return max(a, b)