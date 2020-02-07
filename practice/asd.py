board = [[0] * 5 for _ in range(5)]
value = 1

for i in range(1, 5):
    r = i
    c = 1
    for j in range(1, i + 1):
        board[r][c] = value
        value += 1
        r -= 1
        c += 1