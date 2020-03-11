import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, X = input().split()
    N = int(N)

    ans = int(X, N) % (N-1)

    print('#{} {}'.format(t+1, ans))