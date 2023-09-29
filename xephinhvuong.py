from math import sqrt

t = int(input())
for _ in range(t):
    n = int(input())
    if (n==2):
        print("1 2")
        continue

    x = int(sqrt(n))
    while(True):
        if (n%x==0):
            print(x, n//x)
            break
        x -= 1
