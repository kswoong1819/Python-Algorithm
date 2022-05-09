import sys

sys.stdin = open('../../2020_04/0429/input.txt')


def R_oper():
    n_C = 0

    for i in range(R):
        k = [0] * 101
        for j in range(C):
            k[arr[i][j]] += 1
            arr[i][j] = 0
        p = 0
        for x in range(1, max(k) + 1):
            if p >= 100:
                break
            for y in range(1, 101):
                if k[y] == x:
                    arr[i][p] = y
                    arr[i][p + 1] = x
                    p += 2
                    n_C = max(n_C, p)
                if p >= 100:
                    break
    return n_C


def C_oper():
    n_R = 0
    for j in range(C):
        k = [0] * 101
        for i in range(R):
            k[arr[i][j]] += 1
            arr[i][j] = 0
        p = 0
        for x in range(1, max(k) + 1):
            if p >= 100:
                break
            for y in range(1, 101):
                if k[y] == x:
                    arr[p][j] = y
                    arr[p + 1][j] = x
                    p += 2
                    n_R = max(n_R, p)
                if p >= 100:
                    break
    return n_R


r, c, k = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    arr[i][:3] = list(map(int, input().split()))

R, C = 3, 3
cnt = 0

while arr[r - 1][c - 1] != k:
    if cnt > 100:
        cnt = '-1'
        break
    if R >= C:
        C = R_oper()
    elif R < C:
        R = C_oper()
    cnt += 1

print(cnt)
