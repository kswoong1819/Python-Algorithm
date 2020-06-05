import sys

sys.stdin = open('input.txt')
from collections import deque


def bfs(st, ed):
    q = deque()
    q.append([st, 0])
    while q:
        n, cnt = q.popleft()
        if n == ed:
            return cnt
        for i in range(3):
            num = n + plus[i]
            if 0 <= num <= 100000 and visited[num] == 0:
                visited[num] = cnt + 1
                q.append([num, cnt + 1])
            num = n - plus[i]
            if 0 <= num <= 100000 and visited[num] == 0:
                visited[num] = cnt + 1
                q.append([num, cnt + 1])
        for i in range(2):
            num = n * multi[i]
            if 0 <= num <= 100000 and visited[num] == 0:
                visited[num] = cnt + 1
                q.append([num, cnt + 1])


A, B, N, M = map(int, input().split())
visited = [0] * 100001
visited[N] = 1

plus = [1, A, B]
multi = [A, B]

print(bfs(N, M))
