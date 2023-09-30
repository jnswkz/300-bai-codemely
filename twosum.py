n , k = map(int, input().split())
a = list(map(int, input().split()))
done = False
for i in a:
    if not(done) and (k - i) in a:
        print(a.index(i), a.index(k - i))
        done = True
if (not done):
    print("NO")