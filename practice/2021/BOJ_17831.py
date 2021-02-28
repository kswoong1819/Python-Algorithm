import sys
sys.stdin = open("input.txt")


def dfs(k):
    visited[k] = 1
    for i in range(len(arr[k])):
        nxt = arr[k][i]
        if visited[nxt] == 1:
            continue
        dfs(nxt)
        dp[k][i] += value[k] * value[nxt]
        dp[k][i] += dp[nxt][len(arr[nxt])]
        for j in range(len(arr[k])+1):
            if i == j:
                continue
            dp[k][j] += max(dp[nxt])


n = int(input())
visited = [0] * (n+1)
arr = [[] for _ in range(n+1)]
dp = [[0] * (n+1) for _ in range(n+1)]

arr_tmp = list(map(int, input().split()))
for i in range(2, n+1):
    arr[arr_tmp[i-2]].append(i)

value = [0] + list(map(int, input().split()))

dfs(1)
print(max(dp[1]))