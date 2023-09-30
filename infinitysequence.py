#https://math.stackexchange.com/questions/1174029/find-the-2000th-digit-of-the-series-1234567891011121314-cdots

numbers = ""
a = []
q = int(input())
for _ in range(q):
    n = int(input())
    a.append(n)
maxlen = max(a)

# #subtask 1:
# if maxlen < 1e6 :
num = 1 
while len(numbers) < maxlen:
    numbers += str(num)
    num += 1
for i in a:
    print(numbers[i-1])
# # #subtask 2: maxlen < 1e18
# else:
#     for n in a :
#         if n < 10:
#             print(n)
#             continue

#         m = 0
#         sumarrii = 0
#         while sumarrii < n:
#             m += 1
#             sumarrii += 9 * m * (10**(m-1))
#         # print(m)
#         s = 0
#         for i in range(m):
#             s += 9 * (i) * (10**(i-1))
#             # print(s)
        
#         x = round((n - s)/m) - 1
#         print(str(x+10**(m-1))[1])

