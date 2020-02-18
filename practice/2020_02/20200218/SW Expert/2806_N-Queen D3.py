# import sys
# sys.stdin = open('input.txt', 'r')

def change(x, y, z):
    for i in range(N):
        for j in range(N):
            check[x][j] = check[i][y] = z
            if 0 <= x + i < N and 0 <= y + i < N:
                check[x + i][y + i] = z
            if 0 <= x - i < N and 0 <= y - i < N:
                check[x - i][y - i] = z
            if 0 <= y - i < N and 0 <= x + i < N:
                check[x + i][y - i] = z
            if 0 <= x - i < N and 0 <= y + i < N:
                check[x - i][y + i] = z
    return check


def go(k, n, j):
    if k == n:
        print(A)
    for i in range(N):
        if check[i][j] == 1:
            continue
        change(i, j, 1)
        A.append(i)
        go(k + 1, n, j + 1)
        A.pop()
        change(i, j, 0)


T = int(input())

for t in range(T):
    N = int(input())
    check = [[0] * N for _ in range(N)]

    A = []

    go(0, N, 0)
