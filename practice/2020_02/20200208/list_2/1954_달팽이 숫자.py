import sys
sys.stdin = open('input.txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for t in range(T):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]

    value = 1
    r = 0
    c = -1
    dir = 1

    while value <= N*N:
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or matrix[nr][nc] != 0:
            dir = (dir + 1) % 4
        else:
            matrix[nr][nc] = value
            value += 1
            r = nr
            c = nc

    print('#{}'.format(t+1))
    for i in range(N):
        for j in range(N):
            print(matrix[i][j],end=' ')
        print()