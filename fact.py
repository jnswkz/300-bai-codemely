def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime
n = int(input())
prime = sieve(n)
temp = []
for i in range(2, n):
    if prime[i] :
        temp.append(i)
res = []
i = 2
while(i * i< n):
    while(n % i == 0):
        res.append(i)
        n //=i 
    i += 1

print("*".join(map(str, res)))
# import primefac
# factors = list( primefac.primefac(n) )
# print('*'.join(map(str, factors)))