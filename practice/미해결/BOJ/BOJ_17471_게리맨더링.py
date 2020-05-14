import sys

sys.stdin = open('../../2020_05/0514/input.txt')


def dfs(n, cur):
    global gap
    for i in range(1, 1+N):
        if arr[n][i] == 1 and


N = int(input())
population = list(map(int, input().split()))
total = sum(population)
arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
   connect = list(map(int, input().split()))
   for j in range(1, len(connect)-1):
       arr[connect[0]][connect[j]] = 1

gap = float('inf')
for st in range(1, N+1):
    dfs(st, population[st])