import sys
sys.stdin = open('input.txt', 'r')

def dfs(visited, V):
    for i in range(1, 1+N):
        if arr[V][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)
    return visited


N = int(input())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    arr[x][y] = arr[y][x] = 1

print(len(dfs([1], 1))-1)