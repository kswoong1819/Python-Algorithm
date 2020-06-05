import sys

sys.stdin = open('input.txt')
from heapq import heappush, heappop

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def break_cnt():
    q = []
    heappush(q, [0, 0, 0])
    while q:
        d, r, c = heappop(q)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                nd = d + maze[nr][nc]
                if visited[nr][nc] > nd:
                    visited[nr][nc] = nd
                    heappush(q, [nd, nr, nc])
                # if maze[nr][nc] == 0:
                #     if visited[nr][nc] > d:
                #         visited[nr][nc] = d
                #         heappush(q, [d, nr, nc])
                # elif maze[nr][nc] == 1:
                #     if visited[nr][nc] > d + 1:
                #         visited[nr][nc] = d + 1
                #         heappush(q, [d + 1, nr, nc])


M, N = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]
visited[0][0] = 0
break_cnt()
print(visited[N - 1][M - 1])
