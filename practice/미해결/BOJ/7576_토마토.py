import sys
sys.stdin = open('../../2020_02/20200221/BOJ/input.txt', 'r')

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def dfs(r,c):
    box[r][c] = 2
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if box[nr][nc] == -1:
            continue
        if box[nr][nc] == 0:
            box[nr][nc] = 1

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while 1:
    count_1 = 0
    count_0 = 0
    li_1 = []
    for i in range(N):
        count_1 += box[i].count(1)
        count_0 += box[i].count(0)
        for j in range(M):
            if box[i][j] == 1:
                li_1.append([i,j])
    for i in range(len(li_1)):
        dfs(li_1[i][0], li_1[i][1])
    if count_1 == 0:
        if count_0 != 0:
            cnt = 0
        break
    cnt += 1

print(cnt-1)