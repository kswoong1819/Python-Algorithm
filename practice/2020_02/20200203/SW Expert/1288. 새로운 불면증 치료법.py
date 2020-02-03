import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    check_list = []
    k = kN = 1

    while len(check_list) != 10:
        kN = k*N
        for n in str(kN):
            if n not in check_list:
                check_list.append(n)
        k += 1
    print('#{} {}'.format(t+1,kN))
