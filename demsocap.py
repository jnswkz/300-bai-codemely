#bainaychuaACbignumbucacchos
def main():
    n , x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0

    for i in range(n):
        for j in range(i, n):
            if a[i]**2 + a[j] == x:
                ans += 1
                # print(i)
                # print(j)
    print(ans)
    return 0

if __name__ == '__main__':
    main()
