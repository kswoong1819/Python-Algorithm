import sys

sys.stdin = open('input.txt')
from collections import deque


def find(st, ed):
    global ans
    q = deque()
    q.append(st)
    while q:
        n, cnt = q.popleft()
        if n == ed:
            return cnt
        for i in range(2):
            if n + U < F:
                q.append([n + U, cnt+1])
            if n - D > S:
                q.append([n - D, cnt+1])

F, S, G, U, D = map(int, input().split())

if S > G:
    S, G = G, S
    U, D = D, U

ans = float('inf')
ans = find([S, 0], G)
print(ans)
