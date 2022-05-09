import sys

sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def go(st, V):
    q = deque()
    q.append(st)
    visited = []
    ans = 987654321
    while q:
        r, c, cnt = q.popleft()
        visited.append((r, c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <= M and 0 <= nc <= N:
                if matrix[nr][nc] >= 0 and (nr, nc) not in visited:
                    if matrix[nr][nc] == V:
                        ans = min(ans, cnt + 1)
                    else:
                        q.append((nr, nc, cnt + 1))
    return ans


N, M = map(int, input().split())
store = int(input())
matrix = [[0] * (N + 1) for _ in range(M + 1)]

r = c = 0
for i in range(1, store + 2):
    x, y = map(int, input().split())
    if x == 1:
        r, c = 0, y
    if x == 2:
        r, c = M, y
    if x == 3:
        r, c = y, 0
    if x == 4:
        r, c = y, N
    matrix[r][c] = i
    if i == store + 1:
        Xr, Xc = r, c

for i in range(1, M):
    for j in range(1, N):
        matrix[i][j] = -1
result = 0
for i in range(store):
    result += go((Xr, Xc, 0), i + 1)

print(result)
