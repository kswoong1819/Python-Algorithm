import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]


def move_shark():
    n_arr = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if arr[i][j] != 0:
                r, c = i, j
                s, d, z = arr[i][j]
                nr = r + s * dr[d]
                nc = c + s * dc[d]
                if d <= 2:
                    if 0 < nr <= R:
                        pass
                    else:
                        if nr < 0:
                            nr = abs(nr)
                        if (nr // R) % 2 == 1:
                            d = 2
                            nr = 0 + (nr % R)
                        else:

                            d = 1
                            nr = (R - 2) - (nr % R)
                else:
                    if 0 < nc <= C:
                        pass
                    else:
                        if nc < 0:
                            nc = abs(nc)
                        if (nc // (C - 1)) % 2 == 0:
                            d = 3
                            nc = 2 * (nc // (C - 1)) + (nc % (C - 1))
                        else:
                            d = 4
                            nc = (C - 2) - (nc % (C - 1))
                if n_arr[nr][nc] == 0:
                    n_arr[nr][nc] = s, d, z
                else:
                    if n_arr[nr][nc][2] < arr[i][j][2]:
                        n_arr[nr][nc] = s, d, z
    return n_arr


R, C, M = map(int, input().split())
arr = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r][c] = s, d, z

king = 1
total = 0
while king <= C:
    for i in range(1, R + 1):
        if arr[i][king] != 0:
            total += arr[i][king][2]
            arr[i][king] = 0
            break
    print(total)
    arr = move_shark()
    king += 1

print(total)
