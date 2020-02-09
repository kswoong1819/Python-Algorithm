import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    num = input()

    count = 0
    if num[0] == '1':
        count += 1
    for i in range(1, len(num)):
        if num[i-1] != num[i]:
            count += 1

    print('#{} {}'.format(t+1,count))