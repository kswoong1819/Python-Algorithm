import sys

sys.stdin = open('input.txt')
from collections import deque


def connect_cnt(v):
    q = deque()
    q.append([v, 0])
    visited = [0] * (N + 1)
    for i in range(v + 1):
        visited[v] = 1
    while q:
        n, cnt = q.popleft()
        for i in range(1, N + 1):
            if arr[n][i] == 1 and visited[i] == 0:
                q.append([i, cnt + 1])
                connect[v][i] = connect[i][v] = cnt + 1
                visited[i] = 1


N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
connect = [[99999] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

for i in range(1, N):
    connect_cnt(i)

ans = 0
total = float('inf')
for i in range(1, N + 1):
    if sum(connect[i]) < total:
        total = sum(connect[i])
        ans = i

print(ans)
