def dfs(visited, V, cnt):
    global ans
    for i in range(1, N+1):
        if arr[V][i] == 1 and i not in visited:
            visited.append(i)
            ans = max(ans, cnt+1)
            dfs(visited, i, cnt+1)
    return

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().split())
        arr[x][y] = arr[y][x] = 1

    maxlen = 1
    for i in range(1, N + 1):
        ans = 0
        dfs([i], i, 1)
        if ans > maxlen:
            maxlen = ans

    print('#{} {}'.format(t + 1, maxlen))
