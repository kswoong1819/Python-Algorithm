import sys

sys.stdin = open('../../2020_05/0506/input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def check():
    global total, total_cnt
    change = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 'x':
                for z in range(4):
                    nr = i + dr[z]
                    nc = j + dc[z]
                    if nr < 0 or nr >= N or nc < -1 or nc > M:
                        continue
                    nr %= M
                    nc %= M
                    if arr[nr][nc] == 'x':
                        continue
                    if arr[i][j] == arr[nr][nc]:
                        if [i, j] not in change:
                            change.append([i, j])
                        if [nr, nc] not in change:
                            change.append([nr, nc])
    if len(change):
        for x, y in change:
            total -= arr[x][y]
            total_cnt -= 1
            arr[x][y] = 'x'
    else:
        avg = total / total_cnt
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 'x':
                    continue
                if arr[i][j] < avg:
                    arr[i][j] += 1
                    total += 1
                elif arr[i][j] > avg:
                    arr[i][j] -= 1
                    total -= 1
    return


def rota(r, d, k):
    if d == 0:
        arr1 = arr[r][-k:]
        arr2 = arr[r][:-k]
        arr[r] = arr1 + arr2
    elif d == 1:
        arr1 = arr[r][:k]
        arr2 = arr[r][k:]
        arr[r] = arr2 + arr1
    return


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0
total_cnt = N * M
for i in range(N):
    total += sum(arr[i])

for t in range(T):
    x, d, k = map(int, input().split())
    if total_cnt == 0:
        continue
    for i in range(1, N):
        if i * x - 1 >= N:
            break
        rota(i * x - 1, d, k)

    check()

print(total)
