import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


def dessert(st):
    q = deque()
    q.append(st)
    R, C = st[0], st[1]
    ans = -1
    while q:
        r, c, d, visited = q.popleft()
        for i in range(4):
            if i < d:
                continue
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if cafe[nr][nc] in visited:
                if nr == R and nc == C and d > 1:
                    ans = max(ans, len(visited))
                continue
            q.append([nr, nc, i, visited + [cafe[nr][nc]]])
    return ans


T = int(input())
for t in range(T):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    result = -1
    for i in range(N):
        for j in range(1, N - 1):
            tmp = dessert([i, j, 0, [cafe[i][j]]])
            if result < tmp:
                result = tmp

    print('#{} {}'.format(t + 1, result))
