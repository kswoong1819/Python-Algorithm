import sys

sys.stdin = open('input.txt')

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]


def go(r, c):
    global ans_cnt
    check = []
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if mine[nr][nc] == '*':
                return
            if mine[nr][nc] == '.':
                check.append((nr, nc))
    ans_cnt += 1
    mine[r][c] = 0
    count_star(check)


def count_star(check):
    while check:
        r, c = check.pop(0)
        cnt = 0
        tmp = []
        if mine[r][c] != '.':
            continue
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if mine[nr][nc] == '*':
                cnt += 1
            if mine[nr][nc] == '.' and (nr, nc) not in check:
                tmp.append((nr, nc))
        mine[r][c] = cnt
        if cnt == 0:
            check += tmp


T = int(input())
res = []
for t in range(T):
    N = int(input())
    mine = [list(input()) for _ in range(N)]

    ans_cnt = 0
    for i in range(N):
        for j in range(N):
            if mine[i][j] == '.':
                go(i, j)

    for i in range(N * N):
        x = i // N
        y = i % N
        if mine[x][y] == '.':
            ans_cnt += 1

    print('#{} {}'.format(t + 1, ans_cnt))
