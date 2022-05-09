import sys;
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(T):
    list_sum = []
    num = []
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    for i in range(N-M+1):
        sum = 0
        for j in range(i, i + M):
            sum += num[j]
        list_sum.append(sum)

    for x in range(len(list_sum)-1, -1, -1):
        for y in range(x):
            if list_sum[y] > list_sum[y + 1]:
                list_sum[y], list_sum[y + 1] = list_sum[y + 1], list_sum[y]

    print('#{} {}'.format(t+1, list_sum[-1] - list_sum[0]))