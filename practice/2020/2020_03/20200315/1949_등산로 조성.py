import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c, d, cnt):
    global maxans
    if maxans < cnt:
        maxans = cnt
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if check[nr][nc] == 0 and matrix[r][c] > matrix[nr][nc]:
                check[nr][nc] = 1
                dfs(nr, nc, d, cnt + 1)
            elif check[nr][nc] == 0 and d == 1 and matrix[r][c] > matrix[nr][nc] - K:
                org = matrix[nr][nc]
                check[nr][nc] = 1
                matrix[nr][nc] = matrix[r][c] - 1
                dfs(nr, nc, 0, cnt + 1)
                matrix[nr][nc] = org
    check[r][c] = 0


T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [[0] * N for _ in range(N)]

    pick = 0
    for i in range(N):
        pick = max(pick, max(matrix[i]))

    maxans = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == pick:
                check[i][j] = 1
                dfs(i, j, 1, 1)

    print('#{} {}'.format(t + 1, maxans))
