import sys
sys.stdin = open('input.txt', 'r')

dc = [-1,1]

def dir_check(r,c):
    for i in range(2):
        nc = c + dc[i]
        if nc < 0 or nc >= 100:
            continue
        if ladder[r][nc] == 1:
            return i
    return 2

def go(st):
    col = st
    for i in range(100):
        dir = dir_check(i, col)
        if ladder[i][col] == 2:
            return True
        if dir < 2:
            while 1:
                nc = col + dc[dir]
                if nc < 0 or nc >= 100 or ladder[i][nc] == 0:
                    break
                if ladder[i][nc] == 1:
                    col = nc


for t in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[0][i] == 1:
            if go(i):
                print('#{} {}'.format(T,i))
