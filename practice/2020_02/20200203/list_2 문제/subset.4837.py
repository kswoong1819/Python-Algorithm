import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    count = 0
    for n in range(1,14-N):
        sum_N = 0
        for i in range(n, n+N):
            sum_N += i
        if sum_N == K:
            count += 1
    print('#{} {}'.format(t+1, count))