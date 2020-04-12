import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
from collections import deque


def bfs(st, ed):
    q = deque()
    q.append([st, [st]])
    while q:
        n, path = q.popleft()
        if n == ed:
            return path
        for i in heming[n]:
            if i not in path:
                q.append((i, path + [i]))

N, K = map(int, input().split())
code = ['']
heming = [[] for _ in range(N+1)]

for i in range(1, N+1):
    code.append(input())

x, y = map(int, input().split())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        cnt = 0
        for z in range(K):
            if code[i][z] != code[j][z]:
                cnt += 1
            if cnt > 1:
                break
        if cnt == 1:
            heming[i].append(j)

print(' '.join(map(str, bfs(x, y))))