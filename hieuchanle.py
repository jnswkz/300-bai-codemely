n = int(input())
a= list(map(int, input().split()))
print(sum( (-1)**(i+1)*a[i] for i in range(n) ))