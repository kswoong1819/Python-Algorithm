import sys
sys.stdin = open('input.txt', 'r')

def dfs(visited, V):
    for i in range(N):
        if arr[V][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)
    return visited


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        tmp = dfs([], i)
        if j in tmp:
            result[i][j] = 1

for i in range(N):
    for j in range(N):
        print(result[i][j], end=' ')
    print()