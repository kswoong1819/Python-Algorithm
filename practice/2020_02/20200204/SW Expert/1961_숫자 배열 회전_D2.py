import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    n = int(input())
    in_matrix = [list(map(int, input().split())) for _ in range(n)]
    out_matrix = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            sum = ''
            for x in range(n):
                sum += str(in_matrix[-x-1][i])
            out_matrix[i][j] = sum

        for j in range(n-1):
            sum = ''
            for y in range(n):
                sum += str(in_matrix[-i-1][-y-1])
            out_matrix[i][j+1] = sum

        for j in range(n-2):
            sum = ''
            for z in range(n):
                sum += str(in_matrix[z][-i-1])
            out_matrix[i][j+2] = sum

    print('#{}'.format(t+1))
    for i in range(n):
        for j in range(3):
            print(out_matrix[i][j], end=' ')
        print()