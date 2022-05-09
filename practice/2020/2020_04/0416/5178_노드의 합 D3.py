def find(n):
    global ans
    if n * 2 > N:
        ans += arr[n]
    else:
        find(n * 2)
        if n * 2 != N:
            find(n * 2 + 1)


T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)
    for i in range(M):
        x, y = map(int, input().split())
        arr[x] = y
    ans = 0
    find(L)
    print('#{} {}'.format(t + 1, ans))
