import sys

sys.stdin = open('input.txt', 'r')


def init():
    for i in range(row + 1):
        matrix[i][0] = 1
        matrix[i][col] = 1
        for j in range(col + 1):
            matrix[0][j] = 1
            matrix[row][j] = 1


def point(a):
    if a[0] == 1:
        return 0, a[1]
    if a[0] == 2:
        return row, a[1]
    if a[0] == 3:
        return a[1], 0
    if a[0] == 4:
        return a[1], col


def left_count():
    my_loca = point(loca[-1])
    dir = 0
    r = my_loca[0]
    c = my_loca[1]
    count = 1
    while 1:
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr > row or nc < 0 or nc > col:
            dir = (dir + 1) % 4
        elif matrix[nr][nc] == 2:
            break
        elif nr >= 0 and nr <= row and nc >= 0 and nc <= col and matrix[nr][nc] == 1:
            count += 1
            r = nr
            c = nc
    return count


def right_count():
    my_loca = point(loca[-1])
    dir = 2
    r = my_loca[0]
    c = my_loca[1]
    count = 1
    while 1:
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr > row or nc < 0 or nc > col:
            dir = (dir - 1) % 4
        elif matrix[nr][nc] == 2:
            break
        elif nr >= 0 and nr <= row and nc >= 0 and nc <= col and matrix[nr][nc] == 1:
            count += 1
            r = nr
            c = nc
    return count


dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

col, row = map(int, input().split())
store_count = int(input())
loca = [list(map(int, input().split())) for _ in range(store_count + 1)]

matrix = [[0] * (col + 1) for _ in range(row + 1)]
init()

result = 0
for i in range(store_count):
    store = point(loca[i])
    matrix[store[0]][store[1]] = 2
    if left_count() > right_count():
        result += right_count()
    else:
        result += left_count()
    matrix[store[0]][store[1]] = 1

print(result)
