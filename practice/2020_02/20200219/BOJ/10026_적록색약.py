import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def change(r, c, color, arr):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[nr][nc] == 1:
            continue
        if arr[nr][nc] == color:
            arr[nr][nc] = 1
            change(nr, nc, color, arr)

N = int(input())
painting = [list(input()) for _ in range(N)]
painting_2 = [[0]*N for _ in range(N)]
cnt = cnt_2 = 0

for i in range(N):
    for j in range(N):
        if painting[i][j] == 'B':
            painting_2[i][j] = 'B'
        else:
            painting_2[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if painting[i][j] != 1:
            if painting[i][j] == 'B' or painting[i][j] == 'R':
                cnt += 1
                change(i, j, painting[i][j], painting)
            else:
                cnt += 1
        if painting_2[i][j] != 1:
            cnt_2 += 1
            change(i, j, painting_2[i][j], painting_2)

print(cnt, cnt_2)
