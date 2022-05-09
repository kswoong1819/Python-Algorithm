import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(st):
    q = [st]
    while q:
        r, c, z = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and check[nr][nc][z] == -1:
                    check[nr][nc][z] = check[r][c][z] + 1
                    q.append((nr, nc, z))
                if arr[nr][nc] == 1 and z == 0 and check[nr][nc][z + 1] == -1:
                    check[nr][nc][z + 1] = check[r][c][z] + 1
                    q.append((nr, nc, z + 1))


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
check = [[[-1] * 2 for l in range(M)] for _ in range(N)]
arr[0][0] = 2
check[0][0][0] = 1

bfs((0, 0, 0))

if check[N-1][M-1][0] == -1:
    ans = check[N-1][M-1][1]
elif check[N-1][M-1][1] == -1:
    ans = check[N-1][M-1][0]
else:
    ans = min(check[N-1][M-1])

print(ans)