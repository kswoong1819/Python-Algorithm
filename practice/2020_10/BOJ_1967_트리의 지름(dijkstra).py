import sys

sys.stdin = open('input.txt')

from heapq import heappush, heappop


def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    while heap:
        we, ne = heappop(heap)
        for nn, nw in s[ne]:
            nxt_we = we + nw
            if dist[nn] > nxt_we:
                dist[nn] = nxt_we
                heappush(heap, [nxt_we, nn])
    dist[0] = 0
    return dist


N = int(input())
s = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a = list(map(int, input().split()))
    s[a[0]].append([a[1], a[2]])
    s[a[1]].append([a[0], a[2]])
di1 = dijkstra(1)
max_point = di1.index(max(di1))
di2 = dijkstra(max_point)
if N == 1:
    print(0)
else:
    print(max(di2))
