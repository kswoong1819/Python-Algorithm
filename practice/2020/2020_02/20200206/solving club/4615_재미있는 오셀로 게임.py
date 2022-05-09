import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())

for t in range(T):
    N, M = list(map(int, input().split()))
    play = [list(map(int, input().split())) for _ in range(M)]

    matrix = [[0] * N for _ in range(N)]

    matrix[N // 2 - 1][N // 2 - 1] = matrix[N // 2][N // 2] = 2
    matrix[N // 2][N // 2 - 1] = matrix[N // 2 - 1][N // 2] = 1

    def asd(matrix2):
        for i in play:
            y = i[0] - 1
            x = i[1] - 1
            matrix2[x][y] = i[2]

            for j in range(2, N):
                if matrix2[x][y] == matrix2[(x+j) % N][y]:
                    if (x+j) % N < x:
                        for z in range((x+j) % N + 1, x):
                            matrix2[z][y] = i[2]
                    else:
                        for z in range(x+1, (x+j) % N):
                            matrix2[z][y] = i[2]

                if matrix2[x][y] == matrix2[x][(y+j) % N]:
                    if (y+j) % N < y:
                        for z in range((y+j) % N + 1, y):
                            matrix2[x][z] = i[2]
                    else:
                        for z in range(y+1, (y+j) % N):
                            matrix2[x][z] = i[2]

                if matrix2[x][y] == matrix2[(y+j) % N][(x+j) % N]:
                    if (x+j) % N < x:
                        for z in range((x+j) % N + 1, x):
                            matrix2[z][z] = i[2]
                    else:
                        for z in range(x+1, (x+j) % N):
                            matrix2[z][z] = i[2]
        return matrix2

    print(asd(matrix))

    # count_1 = count_2 = 0
    # for k in matrix:
    #     for h in k:
    #         if h == 1:
    #             count_1 += 1
    #         else:
    #             count_2 += 1
    # print('#{} {} {}'.format(t+1, count_1, count_2))