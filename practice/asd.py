from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    global resultcnt

    while q:

        r, c, cnt = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >=M or nc < 0 or nc >= N :
                continue
            if tomato[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                ncnt  = cnt + 1
                tomato[nr][nc] = 1
                resultcnt = max(resultcnt, ncnt)
                q.append((nr, nc, ncnt))


N, M = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

q = deque()
resultcnt = 0

for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            q.append((i,j,0))
bfs()

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and tomato[i][j] == 0:
            resultcnt = -1

print(resultcnt)