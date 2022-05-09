import sys

sys.stdin = open('input.txt')
from collections import deque


def bfs(st):
    q = deque([st])
    used[st] = 1
    color[st] = 1
    while q:
        n = q.popleft()
        for i in graph[n]:
            if used[i] == 0:
                used[i] = 1
                q.append(i)
                color[i] = color[n] * (-1)
            else:
                if color[i] == color[n]:
                    return False
    return True


K = int(input())
for k in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    flag = True
    used = [0] * (V + 1)
    color = [0] * (V + 1)
    for i in range(1, V + 1):
        if used[i] == 0:
            if not bfs(i):
                flag = False
                break

    if flag:
        print('YES')
    else:
        print('NO')
