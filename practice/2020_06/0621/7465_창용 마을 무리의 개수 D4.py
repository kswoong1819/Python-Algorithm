import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(st):
    q = deque()
    q.append(st)
    while q:
        n = q.popleft()
        for i in check[n]:
            if visited[i]:
                continue
            visited[i] = 1
            q.append(i)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    check = [[] for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        check[x].append(y)
        check[y].append(x)

    cnt = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        cnt += 1
        bfs(i)

    print('#{} {}'.format(t+1, cnt))