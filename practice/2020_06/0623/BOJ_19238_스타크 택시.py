import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def find_customer(st):
    global F, M
    q = deque()
    q.append(st + [0])
    check1[st[0]][st[1]] = 1
    dq = []
    while q:
        r, c, cnt = q.popleft()
        if F <= cnt:
            M = -1
            return
        if dq and dq[0][2] <= cnt:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1 or check1[nr][nc]:
                    continue
                check1[nr][nc] = 1
                if arr[nr][nc] < 0:
                    dq.append([nr, nc, cnt + 1])
                else:
                    q.append([nr, nc, cnt + 1])
    if not dq:
        M = -1
        return
    customer = sorted(dq)
    x, y, cnt = customer[0]
    for x2, y2, cnt2 in customer:
        if x == x2 and y > y2:
            y = y2
    F -= cnt
    return go(x, y, -arr[x][y])


def go(x, y, idx):
    global F, M
    arr[x][y] = 0
    arrival = arrivals[idx]
    q = deque()
    q.append([x, y, 0])
    check2[x][y] = 1
    while q:
        r, c, cnt = q.popleft()
        if F <= cnt:
            M = -1
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1 or check2[nr][nc]:
                    continue
                if nr == arrival[0] and nc == arrival[1]:
                    F += cnt + 1
                    return arrival
                check2[nr][nc] = 1
                q.append([nr, nc, cnt + 1])


N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
st_x, st_y = map(int, input().split())
arrivals = [0]
for i in range(1, 1 + M):
    de_x, de_y, ar_x, ar_y = map(int, input().split())
    arr[de_x - 1][de_y - 1] = -i
    arrivals.append([ar_x - 1, ar_y - 1])

nxt_st = [st_x - 1, st_y - 1]
while M > 0:
    check1 = [[0] * N for _ in range(N)]
    check2 = [[0] * N for _ in range(N)]
    nxt_st = find_customer(nxt_st)
    M -= 1

if M < 0:
    print('-1')
else:
    print(F)
