import sys

sys.stdin = open('input.txt')
from heapq import heappop, heappush


def infection(x):
    q = []
    heappush(q, (0, x))
    while q:
        total, st = heappop(q)
        for time, ed in computer[st]:
            nxt_T = total + time
            if dist[ed] > nxt_T:
                dist[ed] = nxt_T
                heappush(q, (nxt_T, ed))


T = int(input())
for t in range(T):
    n, d, c = map(int, input().split())
    computer = [[] for _ in range(n)]
    for i in range(d):
        a, b, s = map(int, input().split())
        heappush(computer[b - 1], [s, a - 1])

    dist = [float('inf')] * n
    dist[c - 1] = 0
    infection(c - 1)

    cnt = 0
    ans = 0
    for d in dist:
        if d == float('inf'):
            continue
        cnt += 1
        if ans < d:
            ans = d

    print(cnt, ans)
