import sys

sys.stdin = open('input.txt')


def dfs(n, dist, visited):
    global max_dist, max_idx
    for ed, d in matrix[n]:
        if visited[ed]:
            continue
        if dist[ed] == 0:
            dist[ed] = d + dist[n]
            if max_dist < dist[ed]:
                max_dist = dist[ed]
                max_idx = ed
            visited[ed] = 1
            dfs(ed, dist, visited)
            visited[ed] = 0


V = int(input())
matrix = [[] for _ in range(V + 1)]
for i in range(V):
    arr = list(map(int, input().split()))
    st = arr[0]
    j = 1
    while arr[j] != -1:
        matrix[st].append([arr[j], arr[j + 1]])
        j += 2

max_dist = 0
max_idx = 0
dist = [0] * (V + 1)
visited = [0] * (V + 1)
visited[1] = 1
dfs(1, dist, visited)

dist = [0] * (V + 1)
visited[1] = 0
visited[max_idx] = 1
dfs(max_idx, dist, visited)
print(max_dist)
