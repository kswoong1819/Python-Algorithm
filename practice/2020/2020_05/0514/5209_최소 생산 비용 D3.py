def go(k, total):
    global ans
    if total > ans:
        return
    if k == N:
        ans = min(ans, total)
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        go(k + 1, total + factory[k][i])
        visited[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    ans = float('inf')

    go(0, 0)
    print('#{} {}'.format(t + 1, ans))
