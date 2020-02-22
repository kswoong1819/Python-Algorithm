import sys
sys.stdin = open('input.txt', 'r')

def dfs(visited, V):
    for i in range(1, N+1):
        if arr[V][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)
            if i in visited:
                return visited

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().split())
        arr[x][y] = arr[y][x] = 1

    maxlen = 1
    for i in range(1, N+1):
        if dfs([i], i):
            tmp = len(dfs([i], i))
            if tmp > maxlen:
                maxlen = tmp

    print('#{} {}'.format(t+1, maxlen))