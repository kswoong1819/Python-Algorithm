import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs():
    result = 0
    q = deque()
    nq = deque()
    q.append([0, 0])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 1:
                    continue
                if matrix[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append([nr, nc])
                elif matrix[nr][nc] == 1:
                    if check_melt(nr, nc):
                        visited[nr][nc] = 1
                        nq.append([nr, nc])
        if len(q) == 0 and len(nq) != 0:
            result += 1
            q = nq.copy()
            melting(nq)
            nq = deque()
    return result


def check_melt(r, c):
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if matrix[nr][nc] == 0 and visited[nr][nc] == 1:
                cnt += 1
    if cnt >= 2:
        return True
    return False


def melting(arr):
    while arr:
        r, c = arr.popleft()
        matrix[r][c] = 0


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
print(bfs())
