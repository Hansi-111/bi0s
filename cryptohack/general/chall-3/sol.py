##gcd
def gcde(a, b):
    global x, y    
    if (a == 0):
        x = 0
        y = 1
        return b
    gcd = gcde(b % a, a)
    x1 = x
    y1 = y
    x = y1 - (b // a) * x1
    y = x1
    return gcd
a=66528
b=52920 
print(gcde(a,b))

#
