import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def spread():
    n_dust = [[0] * C for _ in range(R)]
    n_dust[cleaner[0]][0] = -1
    n_dust[cleaner[1]][0] = -1
    for i in range(R):
        for j in range(C):
            if dust[i][j] > 0:
                n_dust[i][j] += dust[i][j]
                if dust[i][j] < 5:
                    continue
                for z in range(4):
                    nr = i + dr[z]
                    nc = j + dc[z]
                    if nr < 0 or nr >= R or nc < 0 or nc >= C:
                        continue
                    if n_dust[nr][nc] == -1:
                        continue
                    n_dust[nr][nc] += dust[i][j] // 5
                    n_dust[i][j] -= dust[i][j] // 5
    return n_dust


def work(dust):
    global all_dust
    # upper
    all_dust -= dust[cleaner[0] - 1][0]
    for i in range(cleaner[0] - 2, -1, -1):
        dust[i + 1][0] = dust[i][0]
    dust[0][:C - 1] = dust[0][1:C]
    for i in range(1, cleaner[0] + 1):
        dust[i - 1][C - 1] = dust[i][C - 1]
    dust[cleaner[0]][2:C] = dust[cleaner[0]][1:C - 1]
    dust[cleaner[0]][1] = 0

    # lower
    all_dust -= dust[cleaner[1] + 1][0]
    for i in range(cleaner[1] + 2, R):
        dust[i - 1][0] = dust[i][0]
    dust[R - 1][:C - 1] = dust[R - 1][1:C]
    for i in range(R - 2, cleaner[1] - 1, -1):
        dust[i + 1][C - 1] = dust[i][C - 1]
    dust[cleaner[1]][2:C] = dust[cleaner[1]][1:C - 1]
    dust[cleaner[1]][1] = 0
    return


R, C, T = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(R)]

cleaner = []
all_dust = 2
for i in range(R):
    all_dust += sum(dust[i])
    if dust[i][0] == -1:
        cleaner.append(i)

for t in range(T):
    dust = spread()
    work(dust)

print(all_dust)
