import sys
sys.stdin = open('../../미해결/SW Expert/input.txt')


def bfs(st):
    q = [(st, [st])]
    ans = 0
    while q:
        n, path = q.pop(0)
        for i in range(1, N+1):
            if arr[n][i] == 1 and i not in path:
                q.append((i, path + [i]))
                ans = max(ans, len(path) + 1)
    return ans


T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().split())
        arr[x][y] = arr[y][x] = 1

    maxlen = 1
    for i in range(1, N + 1):
        tmp = bfs(i)
        if tmp > maxlen:
            maxlen = tmp

    print('#{} {}'.format(t + 1, maxlen))
