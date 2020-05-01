import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(r, c, visit):
    global ans
    q = set([(r, c, visit)])
    while q:
        r, c, visit = q.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and alpa[nr][nc] not in visit:
                q.add((nr, nc, visit + alpa[nr][nc]))
                ans = max(ans, len(visit) + 1)


R, C = map(int, input().split())
alpa = [list(input()) for _ in range(R)]

ans = 1
bfs(0, 0)
print(ans)
