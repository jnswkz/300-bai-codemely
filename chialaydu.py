mod = []
n, k = map(int, input().split())
for i in input().split():
    mod.append(int(i) % k)
mod = set(mod)
print(len(mod))