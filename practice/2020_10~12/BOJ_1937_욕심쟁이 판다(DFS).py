import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(1000000)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c):
    if visited[r][c]:
        return visited[r][c]
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if forest[r][c] < forest[nr][nc]:
                visited[r][c] = max(visited[r][c], dfs(nr, nc) + 1)
    return visited[r][c]


N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        result = max(result, dfs(i, j))

print(result)
