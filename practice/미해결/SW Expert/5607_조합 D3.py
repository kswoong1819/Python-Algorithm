import sys
sys.stdin = open('../../2020_03/20200305/input.txt')

T = int(input())

for t in range(T):
    N, R = map(int, input().split())

    first = 1
    second = 1
    for i in range(R):
        first *= N
        N -= 1
        second *= R
        R -= 1

    print('#{} {}'.format(t+1, round(first/second)))