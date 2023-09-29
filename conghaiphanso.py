def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b, c, d = map(int, input().split())
e = a * d + b * c
f = b * d
g = gcd(e, f)
print(e // g, f // g)
