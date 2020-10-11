import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs():
    q = deque()
    q.append(N)
    while q:
        n = q.popleft()
        if n == K:
            return visited[n]
        for nxt in (n - 1, n + 1, 2 * n):
            if 0 <= nxt <= 100000 and not visited[nxt]:
                if nxt == 2 * n and n != 0:
                    visited[nxt] = visited[n]
                    q.appendleft(nxt)
                else:
                    visited[nxt] = visited[n] + 1
                    q.append(nxt)


N, K = map(int, input().split())
visited = [0] * 100001
print(bfs())
