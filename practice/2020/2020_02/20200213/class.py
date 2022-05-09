#
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# print(fibo(10))
#
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return factorial(n-1) * n
#
# print(factorial(998))

# n = 10
# def fibo1(n):
#     if n >= 2 and len(memo) <= n:
#         memo.append(fibo1(n-1) + fibo1(n-2))
#         print(memo)
#     return memo[n]
#
# memo = [0,1]
# print(fibo1(n))

import sys
sys.stdin = open('input.txt', 'r')

def dfs(visited, V):
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)


N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

dfs([1], 1)











