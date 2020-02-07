import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    num1, num2 = map(int, input().split())

    board = [[0] * 300 for _ in range(300)]
    value = 1

    for i in range(1, 300):
        r = i
        c = 1
        for j in range(1, i + 1):
            board[r][c] = value
            value += 1
            r -= 1
            c += 1

    x = y = 0
    for i in range(1, 300):
        for j in range(1, 300):
            if board[i][j] == num1:
                x += j
                y += i
            if board[i][j] == num2:
                x += j
                y += i

    print('#{} {}'.format(t+1, board[y][x]))