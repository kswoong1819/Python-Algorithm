import sys

sys.stdin = open('input.txt')

from collections import deque
import copy

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def choice_store(st, K):
    global result
    if len(ch_store) == K:
        tmp = delivery(ch_store)
        if tmp < result:
            result = tmp
        return
    for i in range(st, len(store)):
        if store[i] in ch_store:
            continue
        ch_store.append(store[i])
        choice_store(i + 1, K)
        ch_store.pop()


def delivery(arr):
    tmp_city = copy.deepcopy(city)
    q = deque(arr)
    nq = deque()
    cnt = home
    tm = 1
    tmp_result = 0
    while q:
        if cnt == 0:
            return tmp_result
        r, c = q.popleft()
        tmp_city[r][c] = -1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if tmp_city[nr][nc] == -1:
                    continue
                if tmp_city[nr][nc] == 1:
                    cnt -= 1
                    tmp_result += tm
                tmp_city[nr][nc] = -1
                nq.append([nr, nc])
        if len(q) == 0:
            tm += 1
            q = nq
            nq = deque()
    return tmp_result


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
store = []
home = 0
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            store.append([i, j])
        if city[i][j] == 1:
            home += 1

result = float('inf')
ch_store = []
choice_store(0, M)

print(result)
