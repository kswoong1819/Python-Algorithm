import sys
sys.stdin = open('input.txt')


def dfs(visited, V):
    for i in range(1, N + 1):
        if check[V][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)
    return visited

def bfs(V):
    queue = [V]
    visited = []
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            for i in range(1, N+1):
                if check[n][i] == 1 and i not in visited:
                    queue.append(i)
    return visited


N, M, V = map(int, input().split())

check = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    check[x][y] = check[y][x] = 1

print(' '.join(map(str, dfs([V], V))))
print(' '.join(map(str, bfs(V))))