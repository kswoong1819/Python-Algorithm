import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    matrix_N = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            sum_M = 0
            for i in range(x, x+M):
                for j in range(y, y+M):
                    sum_M += matrix_N[i][j]
            if ans < sum_M:
                ans = sum_M
    print('#{} {}'.format(t+1, ans))