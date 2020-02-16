import sys

sys.stdin = open('input.txt', 'r')

def dfs(visites, V):



T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().split())
        arr[x][y] = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            dfs(i)