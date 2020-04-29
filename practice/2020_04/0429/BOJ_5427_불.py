import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def fire():
    q.append([x, y, 0])
    while q:
        r, c, check = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                if check:
                    continue
                return dist[r][c]
            if dist[nr][nc] or building[nr][nc] == '#':
                continue
            dist[nr][nc] = dist[r][c] + 1
            q.append([nr, nc, check])
    return 'IMPOSSIBLE'


T = int(input())

for t in range(T):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]

    dist = [[0] * w for _ in range(h)]
    x, y = 0, 0
    q = deque()

    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                dist[i][j] = 1
                q.append([i, j, 1])
            if building[i][j] == '@':
                x, y = i, j
                dist[x][y] = 1
                building[i][j] = '.'

    print(fire())
