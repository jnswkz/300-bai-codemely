n, m, k = map(int, input().split())
a = list(map(int, input().split()))
distance = []
for i in range(n):
    if a[i] == 0 :
        continue
    if a[i] <= k:
        distance.append(abs(i+1 - m))
print(min(distance) * 10 if len(distance) > 0 else -1)
    