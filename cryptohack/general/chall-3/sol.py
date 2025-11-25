###mathematics
x, y = 0, 1
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
def modInverse(a,m):
    g=gcde(a,m)
    if (g!=1):
        print("Inverse doesn't exist")
    else:
        res=(x%m+m)%m
        print("Modular Inverse is",res)

def inverse_multiplicative_mod(a,b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = inverse_multiplicative_mod(b,a%b)
    x = y1
    y = x1 - y1 * (a//b)
    return gcd, x, y #x will be inverse if gcd = 1, else its bezouts co-efficient
p=26513
q=32321
print(inverse_multiplicative_mod(p,q))
print(pow(3,-1,13)%13)
print(pow(273246787654,65536,65537))



