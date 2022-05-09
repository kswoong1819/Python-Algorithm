import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())

    speed = 0
    dis = 0
    for i in range(N):
        up = list(map(int, input().split()))

        if up[0] == 0:
            dis += speed

        if up[0] == 1:
            speed += up[1]
            dis += speed

        if up[0] == 2:
            speed -= up[1]
            if speed < 0:
                speed =0
            dis += speed

    print('#{} {}'.format(t+1,dis))