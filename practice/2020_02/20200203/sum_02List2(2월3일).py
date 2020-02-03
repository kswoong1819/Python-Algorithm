import sys
sys.stdin = open('input.txt', 'r')

for t in range(10):
    case = input()
    matrix = [list(map(int, input().split())) for _ in range(100)]
    list_sum = []

    for i in range(100):
        x_sum = y_sum = z_sum = 0
        for j in range(100):
            x_sum += matrix[i][j]
            y_sum += matrix[j][i]
            if i == j:
                z_sum += matrix[i][j]
        list_sum.append(x_sum)
        list_sum.append(y_sum)
        list_sum.append(z_sum)

    max_num = list_sum[0]
    for n in range(1, len(list_sum)):
        if max_num < list_sum[n]:
            max_num = list_sum[n]
    print('#{} {}'.format(t+1,max_num))