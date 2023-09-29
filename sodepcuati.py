n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mina = min(a)
minb = min(b)
if mina < minb:
    print(str(mina) + str(minb))
else:
    print(str(minb) + str(mina))