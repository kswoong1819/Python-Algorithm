T = int(input())

for t in range(T):
    num = map(int, input().split(' '))
    maxnum = max(num)
    print('#{} {}'.format(t+1,maxnum))