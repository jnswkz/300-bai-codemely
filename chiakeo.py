t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    result = 0
    for party in a:
        if (m%(party+1) == 0):
            result += m//(party+1)
        else :
            result += m//(party+1) + m%(party+1)
    print(result)
