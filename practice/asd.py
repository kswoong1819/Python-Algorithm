import sys

sys.stdin = open('input.txt')

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]


def go(r, c):
    global ans_cnt
    q = [(r, c)]
    while q:
        r,c = q.pop(0)
        mine[r][c] = '*'
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if mine[nr][nc] == 0:
                    q.append((nr,nc))
                    continue
                else:
                    mine[nr][nc] = '*'

def count_star(r, c):
    mine[r][c] = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if mine[nr][nc] == '*':
            mine[r][c] += 1


T = int(input())
res = []
for t in range(T):
    N = int(input())
    mine = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if mine[i][j] == '.':
                count_star(i, j)

    ans_cnt = 0
    for i in range(N):
        for j in range(N):
            if mine[i][j] == 0:
                ans_cnt += 1
                go(i, j)

    for i in range(N):
        for j in range(N):
            if mine[i][j] != '*':
                ans_cnt += 1

    print('#{} {}'.format(t + 1, ans_cnt))
