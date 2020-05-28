import sys

sys.stdin = open('input.txt')
from collections import deque


def invite():
    q = deque()
    q.append([1, 0])
    result = 0
    while q:
        n, cnt = q.popleft()
        for i in friend[n]:
            if cnt + 1 > 2 or check[i]:
                continue
            result += 1
            check[i] = 1
            q.append([i, cnt + 1])

    return result


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    friend = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        friend[a].append(b)
        friend[b].append(a)

    check = [0] * (N + 1)
    check[1] = 1
    ans = invite()

    print('#{} {}'.format(t + 1, ans))
