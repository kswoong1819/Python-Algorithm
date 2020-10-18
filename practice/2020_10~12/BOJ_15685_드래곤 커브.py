import sys

sys.stdin = open('input.txt')

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def curb(x, y, d, g):
    dir = [d]
    matrix[y][x] = 1
    ny = y + dr[d]
    nx = x + dc[d]
    matrix[ny][nx] = 1
    for k in range(g):
        n_dir = []
        for i in range(len(dir) - 1, -1, -1):
            nd = dir[i]
            nd += 1
            nd %= 4
            ny += dr[nd]
            nx += dc[nd]
            matrix[ny][nx] = 1
            n_dir.append(nd)
        dir.extend(n_dir)


N = int(input())
matrix = [[0] * 101 for _ in range(101)]
for n in range(N):
    X, Y, D, G = list(map(int, input().split()))
    curb(X, Y, D, G)

result = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] == 1:
            if matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1] == 1:
                result += 1

print(result)
