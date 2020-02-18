# import sys
# sys.stdin = open('input.txt', 'r')

def check(candi, col):
    current_row = len(candi)
    for queen_row in range(current_row):
        if candi[queen_row] == col or abs(candi[queen_row] - col) == current_row - queen_row:
            return False
    return True

def go(n, row, candidate):
    if row == n:
        A.append(candidate[:])
        return
    for i in range(N):
        if check(candidate, i):
            candidate.append(i)
            go(n, row+1, candidate)
            candidate.pop()


T = int(input())

for t in range(T):
    N = int(input())
    A = []

    go(N, 0, [])
    print('#{} {}'.format(t+1, len(A)))