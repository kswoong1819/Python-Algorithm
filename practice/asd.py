from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
check = [[False]*m for _ in range(n)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def bfs(i, j):
    q = deque()
    q.append((i, j, 0))
    check[i][j] = True
    dist = 0
    while q:
        x, y, d = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if check[nx][ny] is False and a[nx][ny] == 'L':
                q.append((nx, ny, d+1))
                check[nx][ny] = True
                dist = max(dist, d+1)
    return dist

ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            check = [[False]*m for _ in range(n)]
            ans = max(ans, bfs(i, j))
print(ans)
