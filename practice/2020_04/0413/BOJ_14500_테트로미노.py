import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def tech(r, c, k, cur):
    global ans
    if k == 4:
        if ans < cur:
            ans = cur
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if visited[nr][nc] == 0:
            visited[nr][nc] = 1
            tech(nr, nc, k + 1, cur + paper[nr][nc])
            visited[nr][nc] = 0


def fuck(r, c):
    global ans
    total = 0
    if r == 0 and c == 0:
        return
    elif r == 0 and c != 0 and c != M - 1:
        total = paper[r][c] + paper[r][c - 1] + paper[r][c + 1] + paper[r + 1][c]
    elif r != 0 and c == 0 and r != N - 1:
        total = paper[r][c] + paper[r - 1][c] + paper[r + 1][c] + paper[r][c + 1]
    elif 0 < r < N - 1 and 0 < c < M - 1:
        total = paper[r][c] + paper[r - 1][c] + paper[r + 1][c] + paper[r][c + 1] + paper[r][c - 1]
        total -= min([paper[r - 1][c], paper[r + 1][c], paper[r][c + 1], paper[r][c - 1]])
    if ans < total:
        ans = total


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        tech(i, j, 1, paper[i][j])
        visited[i][j] = 0
        fuck(i, j)

print(ans)
