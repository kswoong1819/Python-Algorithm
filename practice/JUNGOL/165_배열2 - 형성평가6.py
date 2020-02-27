dr = [-1,-1]
dc = [-1,1]

def init(arr):
    for i in range(N):
        for j in range(N):
            if i % 2 == 0 and j % 2 == 0:
                arr[i][j] = 1
            elif i % 2 != 0 and j % 2 != 0:
                arr[i][j] = 1

def change(r,c):
    tmp = 0
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        tmp += arr[nr][nc]
    arr[r][c] = tmp

N = 5
arr = [[0]*N for _ in range(N)]
init(arr)

for i in range(1, N):
    for j in range(N):
        if arr[i][j] == 1:
            change(i, j)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()