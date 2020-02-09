import sys
sys.stdin = open('input.txt', 'r')

dr = [-1,1]

def check(r,c,dir):
    nr = r + dr[dir]
    if nr < 0 or nr >= N:
        matrix[r][c] = 0
        return 0
    if matrix[nr][c] == 0:
        matrix[r][c], matrix[nr][c] = matrix [nr][c], matrix[r][c]
        return 1
    return 0


for t in range(10):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    while 1:
        count = 0
        for i in range(N):
            for j in range(N):
                if matrix[j][i] == 1:
                    count += check(j,i,1)
                if matrix[i][j] == 2:
                    count += check(i,j,0)
        if count == 0:
            break

    result = 0
    for i in range(N-1):
        for j in range(N):
            if matrix[i][j] == 1 and matrix[i+1][j] == 2:
                result += 1

    print('#{} {}'.format(t+1, result))