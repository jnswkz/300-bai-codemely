t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(round(sum(a)/n))