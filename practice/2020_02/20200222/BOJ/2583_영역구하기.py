import sys
sys.stdin = open('input.txt', 'r')

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dfs(r, c):
    global cnt
    arr[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if arr[nr][nc] != 0:
            continue
        if arr[nr][nc] == 0:
            cnt += 1
            arr[nr][nc] = 1
            dfs(nr,nc)


M, N, K = map(int, input().split())

arr = [[0] * M for _ in range(N)]

for i in range(K):
    r1, c1, r2, c2 = list(map(int, input().split()))
    for x in range(r1,r2):
        for y in range(c1,c2):
            arr[x][y] += 1

cnt_li = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt = 1
            dfs(i, j)
            cnt_li.append(cnt)

cnt_li.sort()
print(len(cnt_li))
for i in cnt_li:
    print(i, end=' ')