import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    tc, N = input().split()
    arr = input().split()

    number = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    change = []
    for i in arr:
        change.append(number[i])

    change.sort()

    print('#{}'.format(t+1))
    for i in change:
        for j in number:
            if i == number[j]:
                print(j, end=' ')
