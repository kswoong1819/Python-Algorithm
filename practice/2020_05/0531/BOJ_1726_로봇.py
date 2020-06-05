import sys

sys.stdin = open('input.txt')

from collections import deque

dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]


def bfs(visited):
    q = deque()
    q.append([stx - 1, sty - 1, std, 0])
    while q:
        r, c, d, cnt = q.popleft()
        if r == edx - 1 and c == edy - 1 and d == edd:
            return cnt
        nr, nc = r, c
        for i in range(3):
            nr += dr[d]
            nc += dc[d]
            if 0 <= nr < M and 0 <= nc < N:
                if visited[nr][nc][d] == 1:
                    continue
                if matrix[nr][nc] != 1:
                    visited[nr][nc][d] = 1
                    q.append([nr, nc, d, cnt + 1])
                else:
                    break
        for i in range(1, 5):
            if d != i and visited[r][c][i] == 0:
                visited[r][c][i] = 1
                if (d == 1 and i == 2) or (d == 2 and i == 1) or (d == 3 and i == 4) or (d == 4 and i == 3):
                    q.append([r, c, i, cnt + 2])
                else:
                    q.append([r, c, i, cnt + 1])


M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
stx, sty, std = map(int, input().split())
edx, edy, edd = map(int, input().split())

visited = [[[0] * 5 for _ in range(N)] for _ in range(M)]
visited[stx - 1][sty - 1][std] = 1

print(bfs(visited))
