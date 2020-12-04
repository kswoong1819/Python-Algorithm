import sys

sys.stdin = open('input.txt')

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def move(matrix):
    n_matrix = [[[] for p in range(N)] for _ in range(N)]
    overlap = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                for mi, si, di in matrix[i][j]:
                    si_2 = si % N
                    nr = (i + (dr[di] * si_2)) % 7
                    nc = (j + (dc[di] * si_2)) % 7
                    if n_matrix[nr][nc] and [nr, nc] not in overlap:
                        overlap.append([nr, nc])
                    n_matrix[nr][nc].append([mi, si, di])
    n_matrix = processOverlap(overlap, n_matrix)
    return n_matrix


def processOverlap(point, n_mat):
    for r, c in point:
        arr = n_mat[r][c]
        n_mat[r][c] = []
        total_m = 0
        total_s = 0
        total_d = 0
        for m, s, d in arr:
            total_m += m
            total_s += s
            total_d += d % 2
        n_m = total_m // 5
        n_s = total_s // len(arr)
        if total_d % len(arr):
            n_d = [1, 3, 5, 7]
        else:
            n_d = [0, 2, 4, 6]
        if n_m == 0:
            continue
        for d in n_d:
            n_mat[r][c].append([n_m, n_s, d])
    return n_mat


N, M, K = list(map(int, input().split()))
matrix = [[[] for p in range(N)] for _ in range(N)]

for i in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    matrix[r - 1][c - 1].append([m, s, d])

for k in range(K):
    matrix = move(matrix)

result = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            for z in matrix[i][j]:
                result += z[0]

print(result)
