N = int(input())

alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
arr = [[alpa[i % 26] for i in range(j, j+N)] for j in range(0, N*N, N)]

for i in range(N):
    for j in range(N):
        print(arr[-j-1][-i-1], end=' ')
    print()