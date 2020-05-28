import sys

sys.stdin = open('input.txt')
from collections import deque


def go(N):
    q = deque()
    visited = deque()
    q.append([N, C])
    visited.append(N)
    ans = 0
    f = False
    if length != len(set(str(N))):
        f = True

    while q:
        n, cnt = q.popleft()
        if f or not cnt % 2:
            ans = max(ans, n)

        if cnt == 0:
            continue

        for i in range(length):
            for j in range(i + 1, length):
                if i == j:
                    continue
                nxt_N = change(n, i, j)
                if nxt_N not in visited:
                    visited.append(nxt_N)
                    q.append([nxt_N, cnt - 1])
    return ans


def change(num, x, y):
    A = [0] * length
    for i in range(length - 1, -1, -1):
        tmp = num % 10
        num //= 10
        A[i] = tmp

    A[x], A[y] = A[y], A[x]

    nxt = A[0]
    for i in range(length - 1):
        nxt = nxt * 10 + A[i + 1]

    return nxt


T = int(input())

for t in range(T):
    N, C = map(int, input().split())

    length = len(str(N))
    result = go(N)

    print('#{} {}'.format(t + 1, result))
