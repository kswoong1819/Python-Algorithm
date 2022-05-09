import sys

sys.stdin = open('input.txt')
from heapq import heappop, heappush


def comeback(x):
    q = []
    heappush(q, [0, x])
    while q:
        total, st = heappop(q)
        for time, ed in road[st]:
            nxt_T = total + time
            if dist[ed] > nxt_T:
                dist[ed] = nxt_T
                heappush(q, [nxt_T, ed])


N, M, X = map(int, input().split())
road = [[] for _ in range(N)]
for i in range(M):
    x, y, Ti = map(int, input().split())
    heappush(road[x - 1], (Ti, y - 1))

answer = [0] * N
for i in range(N):
    dist = [float('inf')] * N
    dist[i] = 0
    comeback(i)

    if i == X - 1:
        for j in range(N):
            answer[j] += dist[j]
    else:
        answer[i] += dist[X - 1]

print(max(answer))
