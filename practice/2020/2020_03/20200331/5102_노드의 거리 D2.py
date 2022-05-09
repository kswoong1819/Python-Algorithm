def bfs(st, ed):
    q = [st]
    visited = []
    while q:
        n, cnt = q.pop(0)
        visited.append(n)
        for i in range(1, V + 1):
            if lines[n][i] == 1 and i not in visited:
                q.append((i, cnt + 1))
                if i == ed:
                    return cnt + 1
    return 0


T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    lines = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        x, y = map(int, input().split())
        lines[x][y] = lines[y][x] = 1

    S, G = map(int, input().split())
    ans = bfs((S, 0), G)
    print('#{} {}'.format(t + 1, ans))
