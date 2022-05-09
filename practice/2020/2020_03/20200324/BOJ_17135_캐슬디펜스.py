import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
import copy


def archer(k, st):
    global ans
    if k == 3:
        tmp = attack(A)
        ans = max(ans, tmp)
    for i in range(st, M):
        if visited[i]:
            continue
        visited[i] = 1
        A.append((N, i))
        archer(k + 1, i + 1)
        A.pop()
        visited[i] = 0


def attack(n):
    cnt = 0
    check_en = copy.deepcopy(enemy)
    while check_en:
        can = []
        for r1, c1 in n:
            ch_min = 987654321
            x, y = 20, 20
            for r2, c2 in check_en:
                dis = abs(r1 - r2) + abs(c1 - c2)
                if ch_min > dis and dis <= D:
                    ch_min = dis
                    x, y = r2, c2
                if ch_min == dis and y >= c2 and dis <= D:
                    ch_min = dis
                    x, y = r2, c2
            if x != 20:
                if [x, y] not in can:
                    cnt += 1
                    can.append([x, y])
        for k in can:
            check_en.remove(k)
        i = 0
        while len(check_en) > i:
            if check_en[i][0] + 1 < N:
                check_en[i][0] += 1
                i += 1
            else:
                del check_en[i]
    return cnt


N, M, D = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
matrix.append([2] * M)

enemy = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            enemy.append([i, j])

ans = 0
visited = [0] * M
A = []
archer(0, 0)

print(ans)
