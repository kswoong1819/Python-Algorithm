import sys
sys.stdin = open('input.txt', 'r')

def result(long, short):
    max = 0
    for i in range(len(long) - len(short) + 1):
        tmp = 0
        for j in range(len(short)):
            tmp += long[i+j] * short[j]
        if max < tmp:
            max = tmp
    return max

T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    numA = list(map(int, input().split()))
    numB = list(map(int, input().split()))

    if A > B:
        ans = result(numA, numB)
    else:
        ans = result(numB, numA)

    print('#{} {}'.format(t+1, ans))
