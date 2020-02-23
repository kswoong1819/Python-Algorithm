N, M = map(int, input().split())

arr = [[i*j for i in range(1, M+1)] for j in range(1, N+1)]

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()