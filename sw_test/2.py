import sys

sys.stdin = open('input.txt')


def check(ports):
    global result, cnt
    connect = [0] * len(iot)
    for i in ports:
        pr, pc = port[i]
        for j in range(len(iot)):
            if connect[j]:
                continue
            r, c, k = iot[j]
            dist = abs(r - pr) + abs(c - pc)
            if dist <= k + AP:
                connect[j] = 1
    if connect.count(0) == 0:
        result = cnt
        return False
    return True


def tracking(K, st, arr):
    global flag
    if not flag:
        return
    if len(arr) == K:
        flag = check(arr)
        return
    for i in range(st, len(port)):
        arr.append(i)
        tracking(K, i + 1, arr)
        arr.pop()


T = int(input())
for t in range(T):
    N, AP = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    iot = []
    port = []
    for i in range(N):
        for j in range(N):
            if 0 < matrix[i][j] <= 3:
                iot.append([i, j, matrix[i][j]])
            if matrix[i][j] == 9:
                port.append([i, j])
    flag = True
    cnt = 1
    result = -1
    while flag:
        tracking(cnt, 0, [])
        cnt += 1
        if cnt > 5 or cnt > len(port):
            flag = False
    print('#{} {}'.format(t + 1, result))
