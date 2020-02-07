import sys
sys.stdin = open('input.txt', 'r')

def check_mat(mat):
    count = 0
    for i in range(N):
        for j in range(N):
            ch_count = 0
            if mat[i][j] == 1 and j == 0:
                while 1:
                    if mat[i][j] == 1:
                        ch_count += 1
                    if mat[i][j] == 0 or j == N-1:
                        break
                    j += 1
            if mat[i][j] == 1 and mat[i][j - 1] != 1:
                while 1:
                    if mat[i][j] == 1:
                        ch_count += 1
                    if mat[i][j] == 0 or j == N-1:
                        break
                    j += 1
            if ch_count == K:
                count += 1

    return count


T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_c = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            matrix_c[i][j] = matrix[j][i]

    result = check_mat(matrix) + check_mat(matrix_c)
    print('#{} {}'.format(t+1,result))

