N, M = map(int, input().split())

for i in range(1, N*M+1, M):
    for j in range(i, i+M):
        print(j, end=' ')
    print()