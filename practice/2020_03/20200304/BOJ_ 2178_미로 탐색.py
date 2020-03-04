import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(start, end):
    q = [start]
    while q:
        tmp = q.pop(0)
        r, c = tmp
        if tmp == end:
            return visited[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 < nr <= N and 0 < nc <= M:
                if visited[nr][nc] == 0 and arr[nr][nc] == 1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))


N, M = map(int, input().split())
arr = [[0] * (M + 1)] + [[0] + list(map(int, input())) for _ in range(N)]

visited = [[0] * (M + 1) for _ in range(N + 1)]
visited[1][1] = 1
result = bfs((1, 1), (N, M))
print(result)
