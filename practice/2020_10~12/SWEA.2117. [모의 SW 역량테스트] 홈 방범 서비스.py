import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def check(k):
    global result
    kfee = k * k + (k - 1) * (k - 1)
    for i in range(N):
        for j in range(N):
            h = sevice(k, [i, j])
            hfee = h * M
            if hfee - kfee < 0:
                continue
            result = max(result, h)


def sevice(K, st):
    q = deque()
    q.append(st)
    visited = [st]
    point = sum(st)
    home = 0
    if matrix[st[0]][st[1]] == 1:
        home += 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if [nr, nc] in visited:
                continue
            if (nr + nc) - point > K:
                continue
            if matrix[nr][nc] == 1:
                home += 1
            q.append([nr, nc])
            visited.append([nr, nc])
    return home


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for k in range(N, 0, -1):
        check(k)

    print('#{} {}'.format(t+1, result))