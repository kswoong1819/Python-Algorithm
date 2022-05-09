import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
from heapq import heappush, heappop

def bfs(st):
    dist = [float('inf')] * (V + 1)
    dist[st] = 0
    q = []
    heappush(q, [0, st])
    while q:
        dist_tmp, n = heappop(q)
        if dist[n] < dist_tmp:
            continue
        for i in check[n]:
            cost = dist_tmp + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                q.append((cost, i[0]))
    return dist


V, E = map(int, input().split())
K = int(input())
check = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    check[u].append((v, w))

dist = bfs(K)
for i in range(1, V + 1):
    print('INF' if dist[i] == float('inf') else dist[i])
