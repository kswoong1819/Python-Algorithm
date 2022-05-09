import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def move(ro, cm, cn, matrix):
    r, c = robots[ro]
    n, d = matrix[r][c]
    if cm == "L":
        cn %= 4
        for i in range(cn):
            d -= 1
            d %= 4
        matrix[r][c] = [n, d]
    if cm == "R":
        cn %= 4
        for i in range(cn):
            d += 1
            d %= 4
        matrix[r][c] = [n, d]
    if cm == "F":
        for i in range(cn):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < B and 0 <= nc < A:
                if matrix[nr][nc] != 0:
                    X = n
                    Y = matrix[nr][nc][0]
                    return 'Robot {} crashes into robot {}'.format(X, Y)
                matrix[r][c] = 0
                matrix[nr][nc] = [n, d]
                robots[n] = [nr, nc]
                r, c = nr, nc
            else:
                X = n
                return 'Robot {} crashes into the wall'.format(X)
    return "OK"


A, B = map(int, input().split())
matrix = [[0] * A for _ in range(B)]
N, M = map(int, input().split())
robots = [0]
for n in range(1, N + 1):
    x, y, d = list(input().split())
    if d == 'E':
        d = 0
    if d == 'S':
        d = 1
    if d == 'W':
        d = 2
    if d == 'N':
        d = 3
    matrix[abs(B - int(y))][int(x) - 1] = [n, d]
    robots.append([abs(B - int(y)), int(x) - 1])

for m in range(M):
    robot, com, cnt = list(input().split())
    result = move(int(robot), com, int(cnt), matrix)
    if result != "OK":
        break
print(result)
