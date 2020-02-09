import sys
sys.stdin = open('input.txt', 'r')

def sum_M(x, y):
    tmp = 0
    for i in range(x, x+M):
        for j in range(y, y+M):
            tmp += matrix[i][j]
    return tmp

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if result < sum_M(i,j):
                result = sum_M(i,j)

    print('#{} {}'.format(t+1, result))