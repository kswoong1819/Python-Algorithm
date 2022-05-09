import sys
sys.stdin = open('input.txt')

def bfs(V):
    q = [V]
    visited = []
    while q:
        n = q.pop(0)
        if n not in visited:
            visited.append(n)
            result.remove(n)
            for i in range(1, N+1):
                if check[n][i] == 1 and i not in visited:
                    q.append(i)


N, M = map(int, input().split())
check = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    check[u][v] = check[v][u] = 1

cnt = 0
result = [i for i in range(1, N+1)]
while len(result):
    bfs(result[0])
    cnt += 1

print(cnt)
