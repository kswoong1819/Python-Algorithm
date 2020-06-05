import sys

sys.stdin = open('input.txt')
import copy


def check(f):
    for j in range(W):
        spec = f[0][j]
        cnt = 1
        for i in range(1, D):
            if spec == f[i][j]:
                cnt += 1
                if cnt >= K:
                    break
            else:
                spec = f[i][j]
                cnt = 1
        else:
            return False
    return True


def medicine(st, n):
    if n == len(area):
        used = [0] * n
        test_film = copy.deepcopy(film)
        change(n, 0, area, used, test_film)
        return
    for i in range(st, D):
        area.append(i)
        medicine(i + 1, n)
        area.pop()


def change(n, st, area, used, test_film):
    global flag
    if n < st:
        return

    for i in range(n):
        if used[i] == 0:
            test_film[area[i]] = [0] * W
        if used[i] == 1:
            test_film[area[i]] = [1] * W
    if check(test_film):
        flag = True
        return

    for i in range(st, n):
        used[i] = 1
        change(n, i + 1, area, used, test_film)
        used[i] = 0


T = int(input())
for t in range(T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    flag = False
    cnt = 0
    flag = check(film)
    if K == 1:
        flag = True
    while not flag:
        cnt += 1
        area = []
        medicine(0, cnt)

    print('#{} {}'.format(t + 1, cnt))
