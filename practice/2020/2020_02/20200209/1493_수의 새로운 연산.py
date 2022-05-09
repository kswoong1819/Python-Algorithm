import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    n1, n2 = map(int, input().split())
    matrix = [[0]*300 for _ in range(300)]
    value = 1

    for i in range(1, 300):
        r = i
        c = 1
        for j in range(1, i+1):
            matrix[r][c] = value
            value += 1
            r -= 1
            c += 1

    x = y = 0
    for i in range(300):
        for j in range(300):
            if matrix[i][j] == n1:
                x += i
                y += j
            if matrix[i][j] == n2:
                x += i
                y += j
    print('#{} {}'.format(t+1, matrix[x][y]))