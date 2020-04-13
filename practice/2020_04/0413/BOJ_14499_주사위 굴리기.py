import sys
sys.stdin = open('input.txt')

N, M, x, y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))

dice = [0] * 6

t, b = 0, 5
for i in move:
    if i == 1:
        t += 2
        b += 2
    if i == 2:
        
    if i == 3:

    if i == 4:
