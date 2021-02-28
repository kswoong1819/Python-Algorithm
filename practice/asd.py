def dfs(k, arr, dp, visited):
    visited[k] = 1
    for i in range(10):
        if visited[arr[i]] == 1:
            continue
        dfs(arr[i], arr, dp, visited)
        dp[k] += arr[arr[i]]

visited = [0] * 10
dp = [0] * 10
arr = [x for x in range(9, -1, -1)]
dfs(1, arr, dp, visited)