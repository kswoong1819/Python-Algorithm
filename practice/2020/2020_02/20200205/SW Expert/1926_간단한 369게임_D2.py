import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

for num in range(1,N+1):
    count = 0
    for n in str(num):
        if int(n) != 0 and int(n) % 3 == 0:
            count += 1
    if count == 1:
        print('-',end=' ')
    elif count == 2:
        print('--',end=' ')
    else:
        print(num,end=' ')
