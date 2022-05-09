import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, P = map(int, input().split())
    quo = N // P
    remain = N - P * quo
    S2 = (quo + 1) * remain
    S1 = N - S2
    M1 = S1 // quo
    M2 = remain
    result = quo**M1 * (quo+1)**M2

    print('#{} {}'.format(t+1, result))