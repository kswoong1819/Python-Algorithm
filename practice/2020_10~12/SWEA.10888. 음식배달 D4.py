import sys

sys.stdin = open('input.txt')


def choice(st):
    global result
    if 1 <= len(A) <= 10:
        result = min(calcul(A), result)
    for i in range(st, len(store)):
        if store[i] in A:
            continue
        A.append(store[i])
        choice(i + 1)
        A.pop()


def calcul(arr):
    dist = [float('inf')] * len(home)
    dist2 = 0
    for r, c, s in arr:
        dist2 += s
        for i in range(len(home)):
            a, b = home[i]
            tmp = abs(r - a) + abs(c - b)
            if dist[i] > tmp:
                dist[i] = tmp
    return sum(dist) + dist2


T = int(input())
for t in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    store = []
    home = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                home.append([i, j])
            if matrix[i][j] > 1:
                store.append([i, j, matrix[i][j]])
    result = float('inf')
    A = []
    choice(0)

    print('#{} {}'.format(t + 1, result))
