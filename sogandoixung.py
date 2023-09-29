number = int(input())
while(not(number%10)):
    number = number//10
print("YES" if str(number) == str(number)[::-1] else "NO")
