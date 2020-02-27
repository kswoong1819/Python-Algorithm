import sys

sys.stdin = open('input.txt')

dr = [0, 1]
dc = [1, 0]

def count(r, c):
    count_r = 1
    count_c = 1
    for i in range(2):
        while 1:
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nc >= N:
                break
            if matrix[nr][nc] == 0:
                break
            if matrix[nr][nc] != 0 and i == 0:
                r = nr
                c = nc
                count_c += 1
            if matrix[nr][nc] != 0 and i == 1:
                r = nr
                c = nc
                count_r += 1
    return count_r, count_c

def change(r, c, Cr, Cc):
    for i in range(r, r + Cr):
        for j in range(c, c + Cc):
            matrix[i][j] = 0

def insertSort(n):
    for size in range(1, cnt):
        init = n[size]
        val = n[size][0] * n[size][1]
        i = size
        while i > 0 and n[i-1][0] * n[i-1][1] > val:
            n[i] = n[i-1]
            i -= 1
        n[i] = init

T = int(input())

for t in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    result = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                cnt +=1
                Cr, Cc = count(i, j)
                result.append([Cr,Cc])
                change(i, j, Cr, Cc)

    insertSort(result)

    print('#{} {} '.format(t+1, cnt), end='')
    for i in range(cnt):
        print(' '.join(map(str, result[i])), end=' ')
    print()