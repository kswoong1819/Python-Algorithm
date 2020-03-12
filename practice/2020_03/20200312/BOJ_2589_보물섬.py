dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(st):
    q = [st]
    ans = 0
    while q:
        r, c, cnt = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if island_map[nr][nc] == 'L' and visited[nr][nc] == 0:
                    q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = 1
                    ans = max(ans, cnt + 1)
    return ans


N, M = map(int, input().split())
island_map = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if island_map[i][j] == 'L':
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            tmp = bfs((i, j, 0))
            result = max(result, tmp)

print(result)