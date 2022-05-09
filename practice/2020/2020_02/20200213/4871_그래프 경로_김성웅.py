import sys
sys.stdin = open('input.txt', 'r')

def dfs(visited, A):
    for i in range(1, V+1):
        if arr[A][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)
    return visited


T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]

    for e in range(E):
        x, y = map(int, input().split())
        arr[x][y] = 1

    S, G = map(int, input().split())

    if G in dfs([S], S):
        print('#{} 1'.format(t+1))
    else:
        print('#{} 0'.format(t + 1))
