import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    time = list(map(int, input().split()))

    max = time[-1]
    sum = 0
    for i in range(len(time)-1, -1, -1):
        if max < time[i]:
            max = time[i]
        else:
            sum += max - time[i]

    print('#{} {}'.format(t+1, sum))