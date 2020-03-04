import sys

sys.stdin = open('input.txt', 'r')


def bfs(V):
    queue = [V]
    visited = []
    while queue:
        n = queue.pop()
        if n not in visited:
            visited.append(n)
            cnt = 0
            for i in range(1, N + 1):
                if arr[n][i] == 1 and i not in visited:
                    queue.append(i)
                    cnt += 1
            if cnt == 0:
                print(visited)
                return visited


T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().split())
        arr[x][y] = arr[y][x] = 1

    maxlen = 1
    for i in range(1, N + 1):
        tmp = len(bfs(i))
        if tmp > maxlen:
            maxlen = tmp

    print('#{} {}'.format(t + 1, maxlen))
