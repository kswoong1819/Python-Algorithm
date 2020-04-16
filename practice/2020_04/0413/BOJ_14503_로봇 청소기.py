import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(x, y, nd):
    cnt = 1
    r, c = x, y
    d = nd
    while 1:
        for i in range(4):
            dir = (d - 1 - i) % 4
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < N and 0 <= nc < M:
                if room[nr][nc] == 0:
                    cnt += 1
                    room[nr][nc] = 2
                    r, c = nr, nc
                    d = dir
                    break
        else:
            nr = r - dr[d % 4]
            nc = c - dc[d % 4]
            if 0 <= nr < N and 0 <= nc < M:
                if room[nr][nc] == 1:
                    break
                r, c = nr, nc
    return cnt


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

room[r][c] = 2
ans = dfs(r, c, d)
print(ans)
