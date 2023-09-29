n = int(input())

#initdatabase
dx =[]
dy =[]
u =0
v =0
#endinit

for i in range(n):
    x, y = map(int, input().split())
    dx.append(x)
    dy.append(y)

u, v = map(int, input().split())
cnt = 0
for i in range(len(dx)):
    for j in range(i+1, len(dx)):
        if dx[i]+dx[j]==u and dy[i]+dy[j]==v:
            cnt += 1
print(cnt)