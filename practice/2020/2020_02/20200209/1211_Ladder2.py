import sys
sys.stdin = open('input.txt', 'r')

dc = [-1,1]

def dir_ch(r,c):
    for i in range(2):
        nc = c + dc[i]
        if nc < 0 or nc >= 100:
            continue
        if matrix[r][nc] == 1:
            return i
    return 2

def go(st):
    count = 0
    c = st
    for i in range(100):
        dir = dir_ch(i,c)
        if dir < 2:
            while 1:
                nc = c + dc[dir]
                if nc < 0 or nc >= 100 or matrix[i][nc] == 0:
                    break
                count += 1
                c = nc
        count += 1
    return count

for t in range(10):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    result = 987654321
    idx = 987654321

    for i in range(len(matrix[0])):
        if matrix[0][i] == 1:
            tmp = go(i)
            if tmp <= result:
                result = tmp
                idx = i

    print('#{} {}'.format(T,idx))