import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    matrix = [[int(i) for i in input()] for _ in range(N)]

    result = 0
    n = N//2
    for i in range(n+1):
        for j in range(n - i, n + i + 1):
            result += matrix[i][j]
    for i in range(n+1,N):
        for j in range(i - n, 3*n - i + 1):
            result += matrix[i][j]
    print('#{} {}'.format(t+1, result))