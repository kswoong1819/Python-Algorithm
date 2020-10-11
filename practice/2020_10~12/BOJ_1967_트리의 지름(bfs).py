import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(st):
    q = deque()
    q.append([st, 0])
    visited = [0] * (N + 1)
    visited[st] = 1
    while q:
        ne, we = q.popleft()
        for nn, nw in s[ne]:
            if not visited[nn]:
                visited[nn] = nw + we
                q.append([nn, nw + we])
    return visited


N = int(input())
s = [[] for _ in range(N + 1)]
for n in range(N - 1):
    a = list(map(int, input().split()))
    s[a[0]].append([a[1], a[2]])
    s[a[1]].append([a[0], a[2]])

bfs1 = bfs(1)
max_point = bfs1.index(max(bfs1))
bfs2 = bfs(max_point)
if N == 1:
    print(0)
else:
    print(max(bfs2))
