import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    q = deque()
    for i in range(N):
        q.append([cheese[i], i])

    i = 0
    while len(q) != 1:
        q[0][0] //= 2

        if q[0][0] == 0:
            if N + i < M:
                q.popleft()
                q.append([cheese[N+i], N +i])
                i+= 1
            else:
                q.popleft()
        else:
            q.append(q.popleft())
    print('#{} {}'.format(t+1, q[0][1]+1))