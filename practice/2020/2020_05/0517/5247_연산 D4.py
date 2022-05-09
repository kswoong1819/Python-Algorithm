from collections import deque

T = int(input())

visited = [-1] * 1000001
for t in range(T):
    N, M = map(int, input().split())
    visited[N] = t

    q = deque([[N, 0]])
    while q:
        n, cnt = q.popleft()
        if n == M:
            print('#{} {}'.format(t + 1, cnt))
            break
        if 0 < n + 1 <= 1000000 and visited[n + 1] != t:
            q.append((n + 1, cnt + 1))
            visited[n + 1] = t

        if 0 < n - 1 <= 1000000 and visited[n - 1] != t:
            q.append((n - 1, cnt + 1))
            visited[n - 1] = t

        if 0 < n * 2 <= 1000000 and visited[n * 2] != t:
            q.append((n * 2, cnt + 1))
            visited[n * 2] = t

        if 0 < n - 10 <= 1000000 and visited[n - 10] != t:
            q.append((n - 10, cnt + 1))
            visited[n - 10] = t
