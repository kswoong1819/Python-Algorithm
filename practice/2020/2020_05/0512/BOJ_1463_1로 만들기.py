import sys

sys.stdin = open('input.txt')
from collections import deque

N = int(input())
ans = float('inf')
q = deque()
q.append([N, 0])
while q:
    n, cnt = q.popleft()
    if cnt > ans:
        continue
    if n == 1:
        ans = min(ans, cnt)
        continue
    if n % 3 == 0:
        q.append([n // 3, cnt + 1])
    if n % 2 == 0:
        q.append([n // 2, cnt + 1])
    q.append([n - 1, cnt + 1])

print(ans)
