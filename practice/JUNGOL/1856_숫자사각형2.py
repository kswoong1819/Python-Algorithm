N, M = map(int, input().split())
arr = [[i for i in range(j, j + M)] for j in range(1, N * M + 1, M)]

for i in range(N):
    for j in range(M):
        print(arr[i][j + (-2 * j - 1) * (i % 2)], end=' ')
    print()
