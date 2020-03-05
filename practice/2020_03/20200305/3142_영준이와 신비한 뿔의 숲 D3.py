import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    uni = M * 2 - N
    twin = M - uni

    print('#{} {} {}'.format(t+1, uni, twin))