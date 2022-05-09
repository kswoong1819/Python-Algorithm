import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())

    alpha = []
    for i in range(N):
        al, cnt = input().split()

        for i in range(int(cnt)):
            alpha.append(al)

    print('#{}'.format(t+1))
    for i in range(1, len(alpha) + 1):
        print(alpha[i - 1], end='')
        if i % 10 == 0:
            print()
    print()