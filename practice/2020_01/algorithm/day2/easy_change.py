import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(T):
    N = int(input())
    money_count = []
    for i in money:
        n = N//i
        if n > 0:
            money_count.append(str(n))
            N -= n*i
        else:
            money_count.append(str(n))
    print('#{}'.format(t+1))
    print(' '.join(money_count))