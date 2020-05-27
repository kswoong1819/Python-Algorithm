import sys

sys.stdin = open('../../2020_05/0527/input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def go(k, r, c, S, Y, visited):
    global ans, check
    if check == 7:
        return
    if Y > 3:
        return
    if k == 7:
        print(visited)
        for x, y in visited:
            matrix[x][y] = 1
        ans += 1
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5 and [nr, nc] not in visited:
            visited.append([nr, nc])
            if matrix[nr][nc] == 1:
                check += 1
            if arr[nr][nc] == 'Y':
                go(k + 1, nr, nc, S, Y + 1, visited)
            if arr[nr][nc] == 'S':
                go(k + 1, nr, nc, S + 1, Y, visited)
            if matrix[nr][nc] == 1:
                check -= 1
            visited.pop()


arr = [list(input()) for _ in range(5)]

ans = 0
matrix = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        check = 1
        if arr[i][j] == 'Y':
            go(1, i, j, 0, 1, [[i,j]])
        if arr[i][j] == 'S':
            go(1, i, j, 1, 0, [[i,j]])

print(ans)
