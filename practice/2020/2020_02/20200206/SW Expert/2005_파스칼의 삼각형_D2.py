import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    arr = [[1] * i for i in range(1, N+1)]

    for i in range(2, N):
        for j in range(len(arr[i])-2):
            arr[i][j+1] = arr[i-1][j] + arr[i-1][j+1]

    print('#{}'.format(t+1))
    for i in range(N):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()