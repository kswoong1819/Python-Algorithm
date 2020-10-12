import sys

sys.stdin = open('input.txt')

import copy

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def drop_point(K, matrix):
    global result
    if K == N:
        result = min(result, cnt_block(matrix))
        return
    for i in range(W):
        if result == 0:
            return
        t_matrix = copy.deepcopy(matrix)
        n_matrix = block_break(i, matrix)
        drop_point(K + 1, n_matrix)
        matrix = copy.deepcopy(t_matrix)


def block_break(num, tmp_ma):
    q = []
    for i in range(H):
        if tmp_ma[i][num] != 0:
            q.append([tmp_ma[i][num] - 1, i, num])
            tmp_ma[i][num] = 0
            break
    while q:
        n, r, c = q.pop(0)
        for i in range(4):
            nr, nc = r, c
            for j in range(n):
                nr += dr[i]
                nc += dc[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if tmp_ma[nr][nc] > 1:
                        q.append([tmp_ma[nr][nc] - 1, nr, nc])
                    tmp_ma[nr][nc] = 0
                else:
                    break
    zero_down(tmp_ma)
    return tmp_ma


def zero_down(arr):
    for i in range(W):
        for j in range(H - 2, -1, -1):
            if arr[j][i] != 0:
                r, c = j, i
                while 1:
                    nr = r + 1
                    if nr >= H or arr[nr][c] != 0:
                        break
                    else:
                        arr[nr][i] = arr[r][i]
                        arr[r][i] = 0
                        r = nr


def cnt_block(arr):
    total = W * H
    for a in arr:
        total -= a.count(0)
    return total


T = int(input())
for t in range(T):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    result = float('inf')
    drop_point(0, matrix)
    print('#{} {}'.format(t + 1, result))
