import sys
sys.stdin = open('input.txt', 'r')

def multi(N, C):
    if C == 1:
        return N
    else:
        return multi(N,C-1) * N

for t in range(10):
    T = int(input())
    N,C = map(int, input().split())
    print('#{} {}'.format(T,multi(N,C)))
