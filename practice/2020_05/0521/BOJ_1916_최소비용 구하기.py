import sys

sys.stdin = open('input.txt')
from heapq import heappop, heappush


def dijkstra(st):
    dist[st] = 0
    ride_bus = []
    heappush(ride_bus, [0, st])
    while ride_bus:
        cost, n = heappop(ride_bus)
        if dist[n] < cost:
            continue
        for n2, c2 in bus[n]:
            nxt_c = cost + c2
            if dist[n2] > nxt_c:
                dist[n2] = nxt_c
                heappush(ride_bus, [nxt_c, n2])


N = int(input())
D = int(input())
bus = [[] for _ in range(N + 1)]
for d in range(D):
    n1, n2, c = map(int, input().split())
    bus[n1].append([n2, c])
st, ed = map(int, input().split())
dist = [float('inf') for _ in range(N + 1)]

dijkstra(st)
print(dist[ed])
