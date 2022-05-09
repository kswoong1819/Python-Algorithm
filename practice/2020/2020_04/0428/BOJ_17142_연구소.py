import sys

sys.stdin = open('input.txt')
from collections import deque
import copy

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def choice(k, st):
    global ans
    if k == M:
        tmp = spread(A)
        ans = min(ans, tmp)
        return
    for i in range(st, len(virus)):
        if used[i]:
            continue
        A.append(virus[i])
        used[i] = 1
        lab[virus[i][0]][virus[i][1]] = 2
        choice(k + 1, i + 1)
        lab[virus[i][0]][virus[i][1]] = -1
        used[i] = 0
        A.pop()


def spread(arr):
    max_cnt = 0
    q = deque()
    q += arr
    n_lab = copy.deepcopy(lab)
    n_zero = zero
    while q:
        r, c, cnt = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if n_lab[nr][nc] == 0:
                    n_lab[nr][nc] = cnt
                    max_cnt = max(max_cnt, cnt)
                    n_zero -= 1
                    q.append([nr, nc, cnt + 1])
                if n_lab[nr][nc] == -1:
                    n_lab[nr][nc] = 1
                    q.append([nr, nc, cnt + 1])
    if n_zero != 0:
        max_cnt = float('inf')
    return max_cnt


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

virus = []
zero = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i, j, 3])
            lab[i][j] = -1
        if lab[i][j] == 0:
            zero += 1

ans = float('inf')
A = []
used = [0] * len(virus)
choice(0, 0)

if ans == float('inf'):
    print('-1')
elif ans < 2:
    print(0)
else:
    print(ans - 2)
