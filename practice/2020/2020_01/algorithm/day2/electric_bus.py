import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    K,N,M = list(map(int, input().split()))
    station = list(map(int, input().split()))

    bus = K
    count = 0
    count_err = 0
    while bus <= N:
        if bus == N:
            bus += K
        elif bus in station:
            bus += K
            count += 1
            count_err = 0
        else:
            bus -= 1
            count_err += 1
            if count_err == K:
                count = 0
                break
    print('#{} {}'.format(t+1,count))