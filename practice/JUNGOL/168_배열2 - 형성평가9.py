N = int(input())

arr = [[1]*N for _ in range(N)]

for i in range(2, N):
    for j in range(1, i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(N-1, -1, -1):
    for j in range(i+1):
        print(arr[i][j], end=' ')
    print()