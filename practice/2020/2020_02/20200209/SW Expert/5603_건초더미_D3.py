import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    s_list = []
    s_sum = 0
    for x in range(N):
        tmp = int(input())
        s_list.append(tmp)
        s_sum += tmp

    count = 0
    for i in s_list:
        if i > s_sum//N:
            count += i - s_sum//N
        else:
            count += s_sum//N -i

    print('#{} {}'.format(t+1, count//2))