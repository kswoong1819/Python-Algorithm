sys.stdin = open('input.txt')
import sys

input = sys.stdin.readline
from heapq import heappush, heappop


def bfs(st, ed):
    dist = [float('inf')] * (N + 1)
    dist[st] = 0
    q = []
    heappush(q, (0, st))
    while q:
        dist_tmp, now = heappop(q)
        if dist[now] < dist_tmp:
            continue
        for nxt, ncost in lines[now]:
            cost = dist_tmp + ncost
            if dist[nxt] > cost:
                dist[nxt] = cost
                q.append((cost, nxt))
    return dist[ed]


N, E = map(int, input().split())
lines = [[] for _ in range(N + 1)]
for i in range(E):
    a, b, c = map(int, input().split())
    lines[a].append((b, c))
    lines[b].append((a, c))
n1, n2 = map(int, input().split())

path1 = bfs(1, n1) + bfs(n1, n2) + bfs(n2, N)
path2 = bfs(1, n2) + bfs(n2, n1) + bfs(n1, N)
ans = min(path1, path2)

if ans == float('inf'):
    print('-1')
else:
    print(ans)
