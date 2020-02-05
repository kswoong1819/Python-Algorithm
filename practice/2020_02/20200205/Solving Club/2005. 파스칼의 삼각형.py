import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    arr = [[1] * x for x in range(1, N+1)]
    for i in range(1, N-1):
        for j in range(i):
            arr[i+1][j+1] = arr[i][j] + arr[i][j+1]
    print('#{}'.format(t+1))
    for y in range(N):
        for k in arr[y]:
            print(k, end=' ')
        print()