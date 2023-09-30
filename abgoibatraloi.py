string = input()
ab = string.index("AB")
ba = string.index("BA")
if ab != -1 and ba != -1:
    if abs(ab - ba) > 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")