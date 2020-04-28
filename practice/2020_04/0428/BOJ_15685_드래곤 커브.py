import sys

sys.stdin = open('input.txt')

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def curb(x, y, d, g):
    curb_dir = [[d], [(d + 1) % 4]]
    cnt = 0
    while cnt <= g:
        if cnt < 2:
            dir = curb_dir[cnt][0]
            x += dx[dir]
            y += dy[dir]
            if 0 <= x < M and 0 <= y < M:
                matrix[y][x] = 1
        else:
            curb_dir.append(make_dir(curb_dir, cnt))
            for i in curb_dir[cnt]:
                x += dx[i]
                y += dy[i]
                if 0 <= x < M and 0 <= y < M:
                    matrix[y][x] = 1
        cnt += 1


def make_dir(arr, c):
    result = []
    for i in range(c - 1):
        for j in arr[i]:
            result.append((j + 2) % 4)
    result += arr[c - 1]
    return result


def box_check(r, c):
    nr, nc = r, c
    for i in range(4):
        nr += dy[i]
        nc += dx[i]
        if nr < 0 or nr >= M or nc < 0 or nc >= M:
            return 0
        if matrix[nr][nc] == 0:
            return 0
    return 1


N = int(input())
M = 101
matrix = [[0] * M for _ in range(M)]
for i in range(N):
    x, y, d, g = map(int, input().split())
    matrix[y][x] = 1
    curb(x, y, d, g)

ans = 0
for i in range(M):
    for j in range(M):
        if matrix[i][j] == 1:
            ans += box_check(i, j)

print(ans)
