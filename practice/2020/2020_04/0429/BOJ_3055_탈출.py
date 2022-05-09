import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def spread(dist):
    q.append([sx, sy, 1])
    while q:
        r, c, check = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if forest[nr][nc] == 'D' and check:
                    return dist[r][c]
                if dist[nr][nc] or forest[nr][nc] == 'X' or forest[nr][nc] == 'D':
                    continue
                dist[nr][nc] = dist[r][c] + 1
                q.append([nr, nc, check])
    return 'KAKTUS'


R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]

dist = [[0] * C for _ in range(R)]

q = deque()

for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            sx, sy = i, j
            dist[i][j] = 1
        elif forest[i][j] == '*':
            dist[i][j] = 1
            q.append([i, j, 0])

print(spread(dist))
