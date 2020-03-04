import sys

sys.stdin = open('input.txt')
import copy

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def wall(st, count):
    global anx_max
    if count == 0:
        check_lab = copy.deepcopy(lab)
        q_copy = copy.deepcopy(q)
        tmp = spread(check_lab, q_copy)
        if tmp > anx_max:
            anx_max = tmp
        return
    for x in range(st, N*M):
        i = x // M
        j = x % M
        if lab[i][j] == 0:
            lab[i][j] = 1
            wall(x + 1, count - 1)
            lab[i][j] = 0


def spread(check_lab, q_copy):
    virus = 0
    while q_copy:
        x, y = q_copy.pop(0)
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < N and 0 <= ny < M:
                if check_lab[nx][ny] == 0:
                    check_lab[nx][ny] = 2
                    virus += 1
                    if (nx, ny) not in q_copy:
                        q_copy.append((nx, ny))
    return zero - virus - 3


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
anx_max = 0

q = []
zero = 0
for i in range(N):
    for j in range(M):
        tmp = lab[i][j]
        if tmp == 2:
            q.append((i, j))
        elif tmp == 0:
            zero += 1

wall(0, 3)
print(anx_max)
