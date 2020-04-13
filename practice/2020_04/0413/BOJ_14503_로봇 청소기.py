import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dr = [0,1,0,-1]
dc = [-1,0,1,0]


def dfs(r, c, d, t):
    global cnt
    for i in range(4):
        dir = (d + i) % 4
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < M:
            if room[nr][nc] == 0:
                cnt += 1
                room[nr][nc] = 1
                dfs(nr, nc, dir+1, t)
    else:
        nr = r - dr[d % 4]
        nc = c - dc[d % 4]
        if 0 <= nr < N and 0 <= nc < M:
            if t == 0:
                dfs(nr, nc, d, 1)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

cnt = 1
room[r][c] = 1
dfs(r, c, d, 0)
print(cnt)
