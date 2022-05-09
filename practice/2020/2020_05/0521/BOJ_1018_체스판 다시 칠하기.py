import sys

sys.stdin = open('input.txt')
import copy
from collections import deque

dr = [0, 1]
dc = [1, 0]


def color_change(st):
    tmp_chess = copy.deepcopy(chess)
    R, C = st
    q = deque()
    q.append(st)
    cnt = 0
    while q:
        r, c = q.popleft()
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if R <= nr < R + 8 and C <= nc < C + 8 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if tmp_chess[r][c] == tmp_chess[nr][nc]:
                    cnt += 1
                    if tmp_chess[r][c] == 'B':
                        tmp_chess[nr][nc] = 'W'
                    else:
                        tmp_chess[nr][nc] = 'B'
                q.append([nr, nc])
    if cnt > 32:
        cnt = 64 - cnt
    return cnt


N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]

ans = 64
for i in range(N - 7):
    for j in range(M - 7):
        visited = [[0] * M for _ in range(N)]
        visited[i][j] = 1
        tmp = color_change([i, j])
        ans = min(tmp, ans)

print(ans)
