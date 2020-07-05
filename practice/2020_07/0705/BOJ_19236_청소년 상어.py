import sys

sys.stdin = open('input.txt')
import copy

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def feeding(r, c, eaten, arr):
    global ans
    d = arr[r][c][1]
    nr, nc = r, c
    n_arr = move(arr)
    while 1:
        nr += dr[d]
        nc += dc[d]
        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
            if ans < eaten:
                ans = eaten
            break
        if n_arr[nr][nc][0] == 0:
            continue
        eat = n_arr[nr][nc][0]
        n_arr[nr][nc][0] = -1
        n_arr[r][c][0] = 0
        feeding(nr, nc, eaten + eat, n_arr)
        n_arr[nr][nc][0] = eat
        n_arr[r][c][0] = -1


def move(arr):
    tmp_arr = copy.deepcopy(arr)
    num = 1
    while num <= 16:
        flag = True
        for i in range(4):
            if flag == False:
                break
            for j in range(4):
                if flag and tmp_arr[i][j][0] == num:
                    d = tmp_arr[i][j][1]
                    check = 0
                    while check < 8:
                        nr = i + dr[d]
                        nc = j + dc[d]
                        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4 or tmp_arr[nr][nc][0] == -1:
                            d += 1
                            d %= 8
                            check += 1
                            continue
                        if tmp_arr[nr][nc][0] >= 0:
                            flag = False
                            tmp_arr[i][j], tmp_arr[nr][nc] = tmp_arr[nr][nc], tmp_arr[i][j]
                            tmp_arr[nr][nc][1] = d
                            break
        num += 1
    return tmp_arr


matrix = [[] for _ in range(4)]
for i in range(4):
    fish = list(map(int, input().split()))
    for j in range(4):
        n = j * 2
        matrix[i].append([fish[n], fish[n + 1] - 1])

ans = 0
tmp = matrix[0][0][0]
matrix[0][0][0] = -1
feeding(0, 0, tmp, matrix)

print(ans)
