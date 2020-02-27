N = int(input())

'''
alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
arr = [[alpa[i % 26] for i in range(j, j+N)] for j in range(0, N*N, N)]
''' # 문자열이용

arr = [[chr((i%26) + 65) for i in range(j, j+N)] for j in range(0, N*N, N)]

for i in range(N):
    for j in range(N):
        if j % 2:
            print(arr[j][-1-i], end=' ')
        else:
            print(arr[j][i], end=' ')
    print()