import sys

sys.stdin = open('input.txt')

# from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def active_check(matrix):
    nq = []
    st = 0
    while st < len(cell):
        cell[st][3] -= 1
        if cell[st][3] == 0:
            r, c, s, t = cell.pop(st)
            dead_cell.append(s)
            matrix[r][c] = -1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if matrix[nr][nc] == 0:
                    matrix[nr][nc] = s
                    nq.append([nr, nc, s, s + 1])
        else:
            st += 1
    return nq


def del_cell():
    st = 0
    while st < len(dead_cell):
        dead_cell[st] -= 1
        if dead_cell[st] == 0:
            dead_cell.pop(st)
        else:
            st += 1


T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    area = [[0] * K + list(map(int, input().split())) + [0] * K for _ in range(N)]
    upanddown = [[0] * (2 * K + M) for _ in range(K)]
    matrix = upanddown + area + upanddown

    visited = []
    cell = []
    for i in range(2 * K + N):
        for j in range(2 * K + M):
            if matrix[i][j] > 0:
                cell.append([i, j, matrix[i][j], matrix[i][j] + 1])
                visited.append([i, j])

    dead_cell = []
    for k in range(1, K + 1):
        cell = sorted(cell, key=lambda x: x[2], reverse=True)
        arr = active_check(matrix)
        cell.extend(arr)
        del_cell()

    print('#{} {}'.format(t + 1, len(cell) + len(dead_cell)))
