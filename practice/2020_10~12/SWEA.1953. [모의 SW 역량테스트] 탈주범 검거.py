import sys

sys.stdin = open('input.txt')

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

manhole = [[0], [0, 1, 2, 3], [1, 3], [0, 2], [0, 3], [0, 1], [1, 2], [2, 3]]


def bfs(st):
    q = deque()
    q.append(st)
    result = 1
    while q:
        r, c, cnt = q.popleft()
        if cnt >= L:
            return result
        hole = manhole[matrix[r][c]]
        for d in hole:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and matrix[nr][nc] != 0:
                nxt_hole = manhole[matrix[nr][nc]]
                tmp_d = (d + 2) % 4
                if tmp_d in nxt_hole:
                    visited[nr][nc] = 1
                    q.append([nr, nc, cnt + 1])
                    result += 1
    return result


T = int(input())
for t in range(T):
    N, M, R, C, L = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    point_cnt = bfs([R, C, 1])
    print('#{} {}'.format(t + 1, point_cnt))
