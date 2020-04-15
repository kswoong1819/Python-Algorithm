import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]


def check(k):
    global print_check
    nx = x + dr[k]
    ny = y + dc[k]
    if 0 <= nx < N and 0 <= ny < M:
        print_check = 1
        return True
    else:
        return False


def copy(k):
    if matrix[x + dr[k]][y + dc[k]] == 0:
        matrix[x + dr[k]][y + dc[k]] = dice[1]
    else:
        dice[1] = matrix[x + dr[k]][y + dc[k]]
        matrix[x + dr[k]][y + dc[k]] = 0


N, M, x, y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))

dice = [0] * 6
print_check = 0

for i in move:
    if i == 1:
        if check(i):
            dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
            copy(i)
    if i == 2:
        if check(i):
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
            copy(i)
    if i == 3:
        if check(i):
            dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
            copy(i)
    if i == 4:
        if check(i):
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
            copy(i)
    if print_check:
        print(dice[0])
        x = x + dr[i]
        y = y + dc[i]
        print_check = 0
