import sys
sys.stdin = open("input.txt")

def floyd_warshall(n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    arr[i][j] = 0
                    continue
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

n = int(input())
m = int(input())
arr = [[float('inf')] * n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)

floyd_warshall(n)
for i in range(n):
    for j in range(n):
        if arr[i][j] == float('inf'):
            print(0, end = ' ')
        else:
            print(arr[i][j], end = ' ')
    print()
