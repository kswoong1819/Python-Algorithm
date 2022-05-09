import sys
sys.stdin = open('input.txt', 'r')

dc = [-1,1]

def go(st):
    count = 0
    col = st
    for i in range(100):
        dir = check_dir(i, col)
        if dir < 2:
            while 1:
                nc = col + dc[dir]
                if nc < 0 or nc >= 100 or ladder[i][nc] == 0:
                    break
                count += 1
                col = nc
        count += 1
    return count

def check_dir(r,c):
    for i in range(2):
        nc = c + dc[i]
        if nc < 0 or nc >= 100:
            continue
        if ladder[r][nc] == 1:
            return i
    return 2


for t in range(10):
    T = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    min_value = 987654321
    min_idx = 987654321

    for i in range(len(ladder[0])):
        if ladder[0][i] == 1:
            tmp = go(i)
            if tmp <= min_value:
                min_value = tmp
                min_idx = i
    print('#{} {}'.format(T, min_idx))