import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    card = input()
    result = [13,13,13,13]
    matrix = [[card[x] for x in range(y, y+3)] for y in range(0, len(card), 3)]

    flag = True
    for x in range(len(matrix)):
        for y in range(x+1, len(matrix)):
            if matrix[x] == matrix[y]:
                print('#{} ERROR'.format(t+1))
                flag = False
                break

    if flag:
        for j in card:
            if j == 'S':
                result[0] -= 1
            elif j == 'D':
                result[1] -= 1
            elif j == 'H':
                result[2] -= 1
            elif j == 'C':
                result[3] -= 1
        print('#{} '.format(t+1), end='')
        for i in result:
            print(i, end=' ')
        print()