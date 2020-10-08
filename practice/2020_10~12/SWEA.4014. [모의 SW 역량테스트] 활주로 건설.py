import sys

sys.stdin = open('input.txt')


def check(ln, r, c):
    if ln == 0:
        dr, dc = 0, 1
    else:
        dr, dc = 1, 0

    floor = road[r][c]
    cnt = 1
    flag = True
    while 1:
        r += dr
        c += dc
        if not flag and cnt >= X:
            flag = True
            cnt = 0
        if r >= N or c >= N:
            if not flag:
                return False
            return True
        if floor == road[r][c]:
            cnt += 1
            continue
        else:
            if not flag or abs(floor - road[r][c]) > 1:
                return False
            if floor - road[r][c] == -1:
                if cnt >= X:
                    floor = road[r][c]
                    cnt = 1
                    continue
                return False
            if floor - road[r][c] == 1:
                floor = road[r][c]
                cnt = 1
                flag = False
                continue


T = int(input())
for t in range(T):
    N, X = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(2):
        for j in range(N):
            if i == 0:
                if check(i, j, 0):
                    result += 1
            else:
                if check(i, 0, j):
                    result += 1

    print('#{} {}'.format(t + 1, result))
