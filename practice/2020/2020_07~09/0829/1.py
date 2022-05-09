import sys

sys.stdin = open('input.txt')
from collections import deque


def bfs(st, ed):
    q = deque()
    q.append(st)
    while q:
        site, r, c = q.popleft()
        for i in range(n + 2):
            if visited[site][i]:
                continue
            a, b = point[i][0], point[i][1]
            dist = abs(a - r) + abs(b - c)
            if dist <= 1000:
                if i == ed[0]:
                    return True
                visited[site][i] = 1
                q.append([i, a, b])
    return False


T = int(input())

for t in range(T):
    n = int(input())
    point = [list(map(int, input().split())) for _ in range(n + 2)]
    visited = [[0] * (n + 2) for _ in range(n + 2)]
    visited[0][0] = 1
    check = bfs([0] + point[0], [n + 1] + point[n + 1])

    if check:
        print('happy')
    else:
        print('sad')
