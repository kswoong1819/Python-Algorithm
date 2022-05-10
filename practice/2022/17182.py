import sys
sys.stdin = open('input.txt')

def floyd_warshall():
    for z in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = min(arr[i][j], arr[i][z] + arr[z][j])

def back_tracking(k2, n2, cur):
    global result
    if sum(visited) == n2:
        result = min(result, cur)
        return
    for i in range(n2):
        if visited[i] == 1:
            continue
        visited[i] = 1
        back_tracking(i, n2, cur + arr[k2][i])
        visited[i] = 0

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

floyd_warshall()

visited = [0] * n
visited[k] = 1
result = float('inf')
back_tracking(k, n, 0)
print(result)
