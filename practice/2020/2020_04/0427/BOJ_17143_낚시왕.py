import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]
d_reverse = [0, 2, 1, 4, 3]


def move_shark():
    n_arr = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if arr[i][j] != 0:
                r, c = i, j
                s, d, z = arr[i][j]
                nr = r + (s * dr[d]) % ((R - 1) * 2)
                nc = c + (s * dc[d]) % ((C - 1) * 2)

                for _ in range(2):
                    if nr < 1:
                        nr = 2 - nr
                        d = d_reverse[d]
                    elif nr > R:
                        nr = 2 * R - nr
                        d = d_reverse[d]
                    elif nc < 1:
                        nc = 2 - nc
                        d = d_reverse[d]
                    elif nc > C:
                        nc = 2 * C - nc
                        d = d_reverse[d]

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
    arr = move_shark()
    king += 1

print(total)
