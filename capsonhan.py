x, n, m = map(int, input().split())
res = ((x**n -1)/(x-1)) %m
print(res)