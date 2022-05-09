import sys

sys.stdin = open('input.txt', 'r')


import sys
sys.setrecursionlimit(100000)
dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]


def dfs(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M or farm[nr][nc] == 0:
            continue
        if farm[nr][nc] == 1:
            farm[nr][nc] = 2
            dfs(nr, nc)


T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]

    for i in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                count += 1
                farm[i][j] = 2
                dfs(i, j)
    print(count)
