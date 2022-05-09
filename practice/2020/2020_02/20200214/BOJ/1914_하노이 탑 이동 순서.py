def dfs():
    if len(board[2]) == 3:
        return



N = int(input())

board = [[] for _ in range(3)]
for i in range(N, 0, -1):
    board[0].append(i)

print(board)