N = int(input())
arr = [[i for i in range(j, j + N)] for j in range(1, N * N + 1, N)]

for i in range(N):
    for j in range(N):
        print(arr[j][i], end=' ')
    print()