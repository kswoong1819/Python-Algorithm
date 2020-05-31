import sys

sys.stdin = open('input.txt')

from collections import deque

dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]

able_dir = {1: (1, 3, 4), 2: (2, 3, 4), 3: (1, 2, 3), 4: (1, 2, 4)}


def bfs(st, ed, matrix):
    q = deque()
    q.append(st + [0])
    ans = float('inf')
    while q:
        r, c, d, cnt = q.popleft()
        if cnt > ans:
            continue
        if r == ed[0] and c == ed[1]:
            if ed[2] in able_dir[d]:
                cnt += 1
            else:
                cnt += 2
            ans = min(ans, cnt)
            continue
        dir = able_dir[d]
        for i in dir:
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 < nr <= M and 0 < nc <= N and matrix[nr][nc] != 1:
                matrix[nr][nc] = 1
                if i == d:
                    if r == st[0] and c == st[1]:
                        cnt = 1
                    q.append([nr, nc, i, cnt])
                else:
                    q.append([nr, nc, i, cnt + 2])
    return ans


M, N = map(int, input().split())
matrix = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(M)]
st = list(map(int, input().split()))
ed = list(map(int, input().split()))

matrix[st[0]][st[1]] = 1

print(bfs(st, ed, matrix))
