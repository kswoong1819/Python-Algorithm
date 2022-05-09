import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    L, U, X = map(int, input().split())

    if X < L:
        ans = L - X
    elif L <= X <= U:
        ans = 0
    else:
        ans = -1

    print('#{} {}'.format(t+1, ans))