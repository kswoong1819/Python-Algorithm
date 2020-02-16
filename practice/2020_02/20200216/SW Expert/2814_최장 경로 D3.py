import sys
sys.stdin = open('input.txt', 'r')

def dfs(visited, V):
    for i in range(1, N+1):
        if arr[V][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)
    return visited


T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().split())
        arr[x][y] = arr[y][x] = 1

    maxlen = 0
    for i in range(1, N+1):
        tmp = dfs([i], i)
        print(i, tmp)
        if len(tmp) > maxlen:
            maxlen = len(tmp)

    print(maxlen)