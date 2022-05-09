import sys

sys.stdin = open('input.txt')


def calcul(arr, len_stair):
    if len(arr) == 0:
        return 0
    used = [0] * 3
    time = min(arr) - 1
    while 1:
        time += 1
        if len(arr) == 0 and used.count(0) == 3:
            break
        for u in range(3):
            if used[u] > 0:
                used[u] -= 1
        k = 0
        while len(arr) > k:
            if used.count(0) == 0:
                break
            if time >= arr[k]:
                for i in range(3):
                    if used[i] == 0:
                        used[i] = len_stair
                        arr.pop(k)
                        break
            else:
                k += 1
    return time


def track(st):
    global min_result
    stair1 = []
    stair2 = []
    for i, v in enumerate(visited):
        if v:
            stair1.append(dist[i - 1][0])
        else:
            stair2.append(dist[i - 1][1])
    tmp = max(calcul(stair1, stairs[0]), calcul(stair2, stairs[1]))
    if min_result > tmp:
        min_result = tmp

    for i in range(st, len(dist)):
        if visited[i]:
            continue
        visited[i] = 1
        track(i + 1)
        visited[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    P = []
    S = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                P.append([i, j])
            if matrix[i][j] >= 2:
                S.append([i, j])
                stairs.append(matrix[i][j])

    dist = []
    for pr, pc in P:
        tmp = []
        for sr, sc in S:
            length = abs(pr - sr) + abs(pc - sc)
            tmp.append(length)
        dist.append(tmp)

    min_result = float('inf')
    visited = [0] * len(P)
    track(0)
    print('#{} {}'.format(t + 1, min_result))