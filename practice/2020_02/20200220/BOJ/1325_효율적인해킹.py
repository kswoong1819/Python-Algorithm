import sys
sys.stdin = open('input.txt')

def dfs(visited, V):
    for i in range(1, N+1):
        if arr[V][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)
            if i in visited:
                return visited

N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    arr[y][x] = 1

count_list = []
max_com = 0
for i in range(1, N+1):
    if dfs([i], i):
        tmp = len(dfs([i], i))
        if max_com < tmp:
            max_com = tmp
            count_list = []
        if max_com == tmp:
            count_list.append(i)

for i in count_list:
    print(i, end=' ')
