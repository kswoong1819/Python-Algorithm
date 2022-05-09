import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def group_bfs(st, val):
    q = [st]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if island_map[nr][nc] == 1:
                    island_map[nr][nc] = val
                    q.append((nr, nc))

def cnt_bfs(st, k):
    q = [st]
    ans = 987654321
    while q:
        r, c, cnt = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if island_map[nr][nc] == 0 and check[nr][nc] == 0:
                    q.append((nr, nc, cnt+1))
                    check[nr][nc] = 1
                if island_map[nr][nc] != k and island_map[nr][nc] != 0:
                    ans = min(ans, cnt)
    return ans

N = int(input())
island_map = [list(map(int, input().split())) for _ in range(N)]

val = 2
for i in range(N):
    for j in range(N):
        if island_map[i][j] == 1:
            island_map[i][j] = val
            group_bfs((i, j), val)
            val += 1

result = 987654321
for k in range(2, val):
    for i in range(N):
        for j in range(N):
            if island_map[i][j] == k:
                check = [[0]*N for _ in range(N)]
                tmp = cnt_bfs((i, j, 0), k)
                result = min(result, tmp)
print(result)