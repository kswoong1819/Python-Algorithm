def dfs(k, r, cur):
    global ans
    if ans < cur:
        return
    if k == N - 1:
        ans = min(ans, cur + office[r][0])
        return
    for i in range(1, N):
        if office[r][i] == 0:
            continue
        if visited[i]:
            continue
        visited[i] = 1
        dfs(k + 1, i, cur + office[r][i])
        visited[i] = 0


T = int(input())

for t in range(T):
    N = int(input())
    office = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    ans = float('inf')
    dfs(0, 0, 0)

    print('#{} {}'.format(t + 1, ans))
