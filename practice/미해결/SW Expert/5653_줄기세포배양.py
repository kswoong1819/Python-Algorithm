import sys

sys.stdin = open('../../2020_07~09.../0713/input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def active_check():
    nq = []
    st = 0
    while st < len(cell):
        cell[st][2] -= 1
        if cell[st][2] == 0:
            r, c, t = cell.pop(st)
            time = matrix[r][c]
            matrix[r][c] = -1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if matrix[nr][nc] == 0:
                    nq.append([nr, nc, time])
        else:
            st += 1
    return nq


def spread(q):
    add_cell = []
    while q:
        r, c, t = q.pop()
        if matrix[r][c] < t:
            matrix[r][c] = t
            add_cell.append([r, c, t])
            dead_cell.append(t)
    return add_cell


def alive_cell():
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

    cell = []
    for i in range(2 * K + N):
        for j in range(2 * K + M):
            if matrix[i][j] > 0:
                cell.append([i, j, matrix[i][j]])

    dead_cell = []
    add_cell = []
    for k in range(1, K):
        arr = active_check()
        cell.extend(add_cell)
        a = sorted(arr, key=lambda x: x[2])
        add_cell = spread(a)
        alive_cell()

    print('#{} {}'.format(t + 1, len(add_cell) + len(cell) + len(dead_cell)))
