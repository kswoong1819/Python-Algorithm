import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
arr = [[] for _ in range(n+1)]
visited = [1] * (n+1)
dp = [[1, 0] for _ in range(n+1)]

def dfs(k):
    visited[k] = 0
    for i in arr[k]:
        if visited[i]:
            dfs(i)
            dp[k][0] += dp[i][1]
            dp[k][1] += max(dp[i][0], dp[i][1])

for i in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1)

print(n - max(dp[1][0], dp[1][1]))
