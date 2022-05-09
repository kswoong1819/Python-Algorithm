import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    time = list(map(int, input().split()))

    H = time[0] + time[2]
    M = time[1] + time[3]

    if H > 12:
        H = H - 12
    if M > 60:
        M = M - 60
        H += 1

    print('#{} {} {}'.format(t + 1, H, M))
