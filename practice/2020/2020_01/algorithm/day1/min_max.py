T = int(input())

for t in range(T):
    N = int(input())
    num = list(map(int, input().split(' ')))
    for i in range(len(num)-1,0,-1):
        for j in range(0,i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    print('#{} {}'.format(t+1, num[len(num)-1] - num[0]))